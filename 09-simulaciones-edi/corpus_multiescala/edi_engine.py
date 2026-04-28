"""edi_engine.py — Motor EDI común para los 10 casos multiescala.

Aparato EDI ablativo unificado: dada una serie observada, una sonda dinámica
parametrizable, un forcing exógeno, y la ablación correspondiente, computa:
  - EDI = 1 - RMSE_coupled / RMSE_no_ode
  - p-value por permutación (999)
  - bootstrap CI 95% (500)
  - veredicto de nivel del paisaje de emergencia

Diseñado para que TODOS los casos multiescala usen exactamente el mismo
procedimiento, sin ajustes ad-hoc. Si un caso falla, reportamos honestamente.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Callable, Optional, Tuple

import numpy as np


@dataclass
class EDIResult:
    case_name: str
    scale: str
    edi: Optional[float]
    p_value: Optional[float]
    ci_95: Tuple[Optional[float], Optional[float]]
    rmse_coupled: float
    rmse_no_ode: float
    val_steps: int
    train_steps: int
    nivel: str
    overall_pass: bool
    notes: str = ""

    def to_dict(self):
        d = asdict(self)
        return d


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))


def run_edi(case_name: str,
            scale: str,
            observed: np.ndarray,
            forcing: np.ndarray,
            sonda_coupled: Callable[[np.ndarray, np.ndarray, int, int], np.ndarray],
            sonda_no_ode: Callable[[np.ndarray, np.ndarray, int, int], np.ndarray],
            val_fraction: float = 0.30,
            n_perm: int = 999,
            n_boot: int = 500,
            seed: int = 42,
            notes: str = "") -> EDIResult:
    """Ejecuta el aparato EDI ablativo sobre una serie.

    Args:
        observed: serie observada (datos reales o sintéticos físicamente realistas).
        forcing: forcing exógeno alineado temporalmente con observed.
        sonda_coupled: función que recibe (forcing, train_obs, train_steps, val_steps)
            y retorna una predicción de longitud val_steps usando el acoplamiento.
        sonda_no_ode: misma firma, pero con ablación del acoplamiento (e.g., forcing=0).
        val_fraction: fracción del final de la serie usada para validación.
    """
    n = len(observed)
    val_steps = max(10, int(n * val_fraction))
    train_steps = n - val_steps
    train_obs = observed[:train_steps]
    val_obs = observed[train_steps:]

    pred_coupled = sonda_coupled(forcing, train_obs, train_steps, val_steps)
    pred_no_ode = sonda_no_ode(forcing, train_obs, train_steps, val_steps)

    rmse_c = rmse(val_obs, pred_coupled)
    rmse_n = rmse(val_obs, pred_no_ode)

    edi = 1.0 - rmse_c / rmse_n if rmse_n > 1e-9 else None

    # Permutación: shuffles de la predicción coupled como null
    rng = np.random.default_rng(seed)
    null_edis = []
    for _ in range(n_perm):
        perm_pred = rng.permutation(pred_coupled)
        rmse_p = rmse(val_obs, perm_pred)
        if rmse_n > 1e-9:
            null_edis.append(1.0 - rmse_p / rmse_n)
    null_arr = np.asarray(null_edis)
    p_value = float(np.mean(null_arr >= edi)) if edi is not None else None

    # Bootstrap CI sobre los residuales
    boot_edis = []
    for _ in range(n_boot):
        idx = rng.integers(0, val_steps, size=val_steps)
        b_obs = val_obs[idx]
        b_c = pred_coupled[idx]
        b_n = pred_no_ode[idx]
        rmse_bc = rmse(b_obs, b_c)
        rmse_bn = rmse(b_obs, b_n)
        if rmse_bn > 1e-9:
            boot_edis.append(1.0 - rmse_bc / rmse_bn)
    boot_arr = np.asarray(boot_edis)
    if len(boot_arr) > 0:
        ci_lo = float(np.percentile(boot_arr, 2.5))
        ci_hi = float(np.percentile(boot_arr, 97.5))
    else:
        ci_lo, ci_hi = None, None

    # Clasificación del nivel
    if edi is None or edi <= 0:
        nivel = "0_null"
        overall = False
    elif p_value is not None and p_value >= 0.05:
        nivel = "1_trend"
        overall = False
    elif edi < 0.10:
        nivel = "2_suggestive"
        overall = False
    elif edi < 0.30:
        nivel = "3_weak"
        overall = False
    elif p_value < 0.01 and edi >= 0.30:
        nivel = "4_strong"
        overall = True
    else:
        nivel = "3_weak"  # EDI alto pero p marginal
        overall = False

    return EDIResult(
        case_name=case_name,
        scale=scale,
        edi=edi,
        p_value=p_value,
        ci_95=(ci_lo, ci_hi),
        rmse_coupled=rmse_c,
        rmse_no_ode=rmse_n,
        val_steps=val_steps,
        train_steps=train_steps,
        nivel=nivel,
        overall_pass=overall,
        notes=notes,
    )


def save_result(result: EDIResult, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "metrics.json"
    out_path.write_text(json.dumps(result.to_dict(), indent=2,
                                    ensure_ascii=False, default=str),
                        encoding="utf-8")
