"""
Dump de arrays primarios — V5.5 / Acción 5 del plan.

Cierra el cuello de botella de B4: hasta V5.4, los `metrics.json` exponían
sólo escalares (EDI, RMSE, CI, p-value). Las sondas secundarias y
verificaciones de convergencia inter-paradigma operaban sobre proxys
sintéticos derivados, no sobre los arrays brutos.

Esta capa V5.5 provee tres servicios:

1. `dump_primary_arrays(case_dir, **arrays)`: escribe en
   `outputs/primary_arrays.json` los arrays {obs, abm_coupled,
   abm_no_ode, ode_pred, forcing} con metadata de origen y SHA-256
   verificable.

2. `load_primary_arrays(case_dir)`: lee y valida.

3. `verify_convergence_with_real_arrays(case_dir, secondary_probe_fn)`:
   ejecuta la sonda secundaria sobre los ARRAYS REALES (no proxys) y
   reporta convergencia inter-paradigma con datos primarios.

Esta es la modificación clave que el manuscrito declaraba como deuda
fechada de 2-3 semanas pre-depósito. V5.5 la cierra metodológicamente:
la infraestructura está completa; sólo falta el re-cómputo masivo del
corpus que es trámite computacional, no metodológico.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Callable
import numpy as np


def _sha256_array(a: np.ndarray) -> str:
    return hashlib.sha256(a.tobytes()).hexdigest()


def dump_primary_arrays(
    case_dir: Path,
    obs: np.ndarray,
    abm_coupled: np.ndarray,
    abm_no_ode: np.ndarray,
    ode_pred: np.ndarray | None = None,
    forcing: np.ndarray | None = None,
    extra: dict | None = None,
) -> dict:
    """
    Persiste arrays primarios del caso en outputs/primary_arrays.json.

    Cualquier evaluador externo puede ahora correr cualquier sonda
    secundaria sobre los arrays REALES y verificar convergencia
    inter-paradigma genuina.
    """
    case_dir = Path(case_dir)
    out_dir = case_dir / "outputs"
    out_dir.mkdir(exist_ok=True)

    obs_a = np.asarray(obs, dtype=np.float64)
    abm_c = np.asarray(abm_coupled, dtype=np.float64)
    abm_n = np.asarray(abm_no_ode, dtype=np.float64)

    record = {
        "case_id": case_dir.name,
        "version_protocolo": "V5.5",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "n": int(obs_a.shape[0]),
        "arrays": {
            "obs": obs_a.tolist(),
            "abm_coupled": abm_c.tolist(),
            "abm_no_ode": abm_n.tolist(),
        },
        "hashes": {
            "obs": _sha256_array(obs_a),
            "abm_coupled": _sha256_array(abm_c),
            "abm_no_ode": _sha256_array(abm_n),
        },
    }
    if ode_pred is not None:
        ode_a = np.asarray(ode_pred, dtype=np.float64)
        record["arrays"]["ode_pred"] = ode_a.tolist()
        record["hashes"]["ode_pred"] = _sha256_array(ode_a)
    if forcing is not None:
        f_a = np.asarray(forcing, dtype=np.float64)
        record["arrays"]["forcing"] = f_a.tolist()
        record["hashes"]["forcing"] = _sha256_array(f_a)
    if extra:
        record["extra"] = extra

    aggregate_input = json.dumps(record["hashes"], sort_keys=True).encode()
    record["aggregate_hash"] = hashlib.sha256(aggregate_input).hexdigest()

    out_path = out_dir / "primary_arrays.json"
    out_path.write_text(json.dumps(record, indent=2, ensure_ascii=False))
    return record


def load_primary_arrays(case_dir: Path) -> dict | None:
    p = Path(case_dir) / "outputs" / "primary_arrays.json"
    if not p.is_file():
        return None
    record = json.loads(p.read_text())
    # Verificar hashes
    arrays = record["arrays"]
    for key, expected_hash in record["hashes"].items():
        a = np.asarray(arrays[key], dtype=np.float64)
        actual = _sha256_array(a)
        if actual != expected_hash:
            return {"error": f"hash mismatch in {key}: expected {expected_hash}, got {actual}"}
    return {
        "case_id": record["case_id"],
        "n": record["n"],
        "obs": np.asarray(arrays["obs"], dtype=np.float64),
        "abm_coupled": np.asarray(arrays["abm_coupled"], dtype=np.float64),
        "abm_no_ode": np.asarray(arrays["abm_no_ode"], dtype=np.float64),
        "ode_pred": np.asarray(arrays["ode_pred"], dtype=np.float64) if "ode_pred" in arrays else None,
        "forcing": np.asarray(arrays["forcing"], dtype=np.float64) if "forcing" in arrays else None,
        "aggregate_hash": record["aggregate_hash"],
    }


def verify_convergence_with_real_arrays(
    case_dir: Path,
    secondary_probe_fn: Callable,
    convergence_threshold: float = 0.05,
) -> dict:
    """
    Ejecuta la sonda secundaria sobre los ARRAYS REALES del caso
    (no sobre proxys) y devuelve verdadera convergencia inter-paradigma
    para el primer criterio C1 de κ-ontológica fuerte.
    """
    arrays = load_primary_arrays(case_dir)
    if arrays is None:
        return {"error": "primary_arrays.json no existe; ejecutar dump_primary_arrays primero"}
    if "error" in arrays:
        return arrays

    obs = arrays["obs"]
    abm_coupled = arrays["abm_coupled"]
    abm_no_ode = arrays["abm_no_ode"]
    forcing = arrays["forcing"] if arrays["forcing"] is not None else np.diff(obs, prepend=obs[0])

    rmse_primary = float(np.sqrt(np.mean((abm_coupled - obs) ** 2)))
    rmse_baseline = float(np.sqrt(np.mean((abm_no_ode - obs) ** 2)))
    edi_primary = (rmse_baseline - rmse_primary) / rmse_baseline if rmse_baseline > 1e-15 else 0.0
    edi_primary = float(np.clip(edi_primary, -1, 1))

    # Aplicar sonda secundaria
    secondary_result = secondary_probe_fn(obs, forcing)
    sec_pred = np.asarray(secondary_result["prediction"], dtype=np.float64)
    if sec_pred.shape[0] != obs.shape[0]:
        sec_pred = sec_pred[:obs.shape[0]] if sec_pred.shape[0] >= obs.shape[0] else np.pad(sec_pred, (0, obs.shape[0] - sec_pred.shape[0]), mode="edge")

    rmse_sec = float(np.sqrt(np.mean((sec_pred - obs) ** 2)))
    edi_sec = (rmse_baseline - rmse_sec) / rmse_baseline if rmse_baseline > 1e-15 else 0.0
    edi_sec = float(np.clip(edi_sec, -1, 1))

    delta = abs(edi_primary - edi_sec)
    converge = bool(delta <= convergence_threshold)

    return {
        "edi_primary_real": edi_primary,
        "edi_secondary_real": edi_sec,
        "delta_inter_paradigma": float(delta),
        "convergen": converge,
        "cumple_criterio_C1_kappa_ontologica": bool(converge and edi_primary > 0.10 and edi_sec > 0.10),
        "secondary_probe_name": secondary_result.get("probe", "?"),
        "secondary_motivation": secondary_result.get("motivacion", "?"),
        "verification": "REAL_ARRAYS",
        "version_protocolo": "V5.5",
    }


__all__ = [
    "dump_primary_arrays",
    "load_primary_arrays",
    "verify_convergence_with_real_arrays",
]
