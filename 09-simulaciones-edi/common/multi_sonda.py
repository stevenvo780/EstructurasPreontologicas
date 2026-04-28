"""multi_sonda.py — Programa multi-sonda ejecutado.

Para cada caso strong seleccionado:
  1. Genera la serie de referencia con la sonda primaria del caso, usando
     parámetros y forcing del case_config.json.
  2. Genera la serie observada coupled (la misma que la fase synthetic del
     aparato simula) con la sonda primaria.
  3. Genera la serie observada coupled con la sonda alternativa, manteniendo
     el mismo forcing exógeno y la misma estructura de ruido.
  4. Calcula EDI = 1 - RMSE_alternativa / RMSE_no_ode usando el mismo
     procedimiento que el aparato.
  5. Compara contra el EDI primario disponible en outputs/metrics.json.
  6. Veredicto: convergencia fuerte, moderada o divergencia.

Salida: 09-simulaciones-edi/multi_sonda/results.json
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Dict, List

import numpy as np

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "09-simulaciones-edi" / "common"))

from ode_models import simulate_ode_model  # noqa: E402

# Mapeo: caso → (sonda primaria efectiva, sonda alternativa)
CASOS = {
    "04_caso_energia": {
        "primary": "mean_reversion",   # actual del caso
        "alternative": "thermo_balance",
        "alt_params": {"ode_lambda": 0.15, "ode_gamma": 0.10, "ode_delta": 0.2},
        "esperado_edi": 0.30,
    },
    "16_caso_deforestacion": {
        "primary": "accumulation_decay",  # actual del caso
        "alternative": "spatial_logistic",
        "alt_params": {"ode_K": 1.0},
        "esperado_edi": 0.45,
    },
    "27_caso_riesgo_biologico": {
        "primary": "saturation_growth",  # actual del caso
        "alternative": "seir_demographic",
        "alt_params": {"ode_sigma": 0.2, "ode_mu": 0.05, "ode_xi": 0.1},
        "esperado_edi": 0.25,
    },
}


def _gen_forcing(steps: int, fcfg: dict, seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    ftype = fcfg.get("type", "linear_cycle")
    base = float(fcfg.get("base", 0.0))
    slope = float(fcfg.get("slope", 0.05))
    cycle_amp = float(fcfg.get("cycle_amp", 0.2))
    cycle_period = float(fcfg.get("cycle_period", 20))
    noise_std = float(fcfg.get("noise_std", 0.03))
    t = np.arange(steps)
    if ftype == "oscillator":
        f = base + cycle_amp * np.sin(2 * np.pi * t / cycle_period)
    else:
        f = base + slope * t + cycle_amp * np.sin(2 * np.pi * t / cycle_period)
    f = f + rng.normal(0.0, noise_std, size=steps)
    return f


def _simulate(model: str, forcing: np.ndarray, params: dict, seed: int) -> np.ndarray:
    """Llama al simulador del repo con la sonda solicitada."""
    full_params = {**params, "forcing_series": forcing.tolist(),
                   "ode_key": "y"}
    out = simulate_ode_model(full_params, len(forcing), seed=seed)
    return np.asarray(out["y"], dtype=float)


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))


def run_multi_sonda(case_dir: Path, primary: str, alternative: str,
                    alt_params: dict, seed: int = 42) -> dict:
    cfg = json.loads((case_dir / "case_config.json").read_text(encoding="utf-8"))
    syn = cfg.get("synthetic", {})
    fcfg = syn.get("forcing", {})
    tparams = syn.get("true_params", {})
    metrics_path = case_dir / "outputs" / "metrics.json"
    metrics = json.loads(metrics_path.read_text(encoding="utf-8")) if metrics_path.exists() else {}

    syn_phase = metrics.get("phases", {}).get("synthetic", {})
    val_steps = int(syn_phase.get("data", {}).get("val_steps", 20))
    total_steps = int(syn_phase.get("data", {}).get("steps", 40))
    if total_steps <= val_steps + 5:
        total_steps = val_steps + 30
    train_steps = total_steps - val_steps

    forcing = _gen_forcing(total_steps, fcfg, seed=seed)

    # serie de referencia: la verdad sintética con sonda primaria
    obs = _simulate(primary, forcing, tparams, seed=seed)

    # forecast con sonda primaria (el "ABM+ODE coupled" en su lectura ODE)
    pred_primary = _simulate(primary, forcing, tparams, seed=seed + 1)
    rmse_primary = rmse(pred_primary[train_steps:], obs[train_steps:])

    # forecast con sonda alternativa, mismos parámetros base + alt_params
    alt_full = {**tparams, **alt_params, "model": alternative}
    pred_alt = _simulate(alternative, forcing, alt_full, seed=seed + 2)
    rmse_alt = rmse(pred_alt[train_steps:], obs[train_steps:])

    # baseline no-ODE: forcing puro reescalado (proxy del "no_ode" del aparato)
    rmse_no_ode = rmse(forcing[train_steps:], obs[train_steps:])

    edi_primary = 1.0 - rmse_primary / rmse_no_ode if rmse_no_ode > 1e-9 else None
    edi_alt = 1.0 - rmse_alt / rmse_no_ode if rmse_no_ode > 1e-9 else None

    # Veredicto cualitativo
    delta = (edi_alt - edi_primary) if (edi_alt is not None and edi_primary is not None) else None
    if delta is None:
        verdict = "indeterminado"
    elif abs(delta) <= 0.10:
        verdict = "convergencia fuerte"
    elif abs(delta) <= 0.20:
        verdict = "convergencia moderada"
    else:
        verdict = "divergencia"

    edi_aparato_canonico = float(syn_phase.get("edi", {}).get("value", float("nan")))

    return {
        "case_dir": case_dir.name,
        "case_name": cfg.get("case_name", case_dir.name),
        "primary_model": primary,
        "alternative_model": alternative,
        "train_steps": train_steps,
        "val_steps": val_steps,
        "rmse_primary_simulado": rmse_primary,
        "rmse_alternativa_simulado": rmse_alt,
        "rmse_no_ode_simulado": rmse_no_ode,
        "edi_primary_simulado": edi_primary,
        "edi_alternativa_simulado": edi_alt,
        "delta_edi_alt_vs_primary": delta,
        "edi_aparato_canonico": edi_aparato_canonico,
        "verdict": verdict,
    }


def main():
    cases = sys.argv[1:] or list(CASOS.keys())
    results = []
    for c in cases:
        cfg = CASOS.get(c)
        if cfg is None:
            print(f"SKIP {c}: not in CASOS")
            continue
        case_dir = REPO / "09-simulaciones-edi" / c
        if not case_dir.exists():
            print(f"SKIP {c}: dir missing")
            continue
        try:
            r = run_multi_sonda(case_dir, cfg["primary"], cfg["alternative"], cfg["alt_params"])
            results.append(r)
            print(f"{r['case_dir']:40s}  primary={cfg['primary']:22s} alt={cfg['alternative']:18s}  "
                  f"EDI_p={r['edi_primary_simulado']:+.3f}  EDI_alt={r['edi_alternativa_simulado']:+.3f}  Δ={r['delta_edi_alt_vs_primary']:+.3f}  → {r['verdict']}")
        except Exception as exc:
            import traceback
            traceback.print_exc()
            print(f"FAIL {c}: {exc}")
    out = REPO / "09-simulaciones-edi" / "multi_sonda" / "results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"\nReport written to: {out}")


if __name__ == "__main__":
    main()
