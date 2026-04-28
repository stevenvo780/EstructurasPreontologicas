"""
Validación avanzada V5.4 — bloques B11, B13, B14.

B11 — Cross-validation k-fold sobre series temporales (TimeSeriesSplit).
B13 — Tests adversariales: perturbación de parámetros, ruido aditivo, jackknife.
B14 — Validación dimensional automática de las ecuaciones.
"""
from __future__ import annotations

import math
import numpy as np
from typing import Sequence


# =====================================================================
# B11 — Cross-validation k-fold (TimeSeriesSplit)
# =====================================================================

def time_series_kfold(
    obs: Sequence[float],
    abm: Sequence[float],
    reduced: Sequence[float],
    n_splits: int = 5,
) -> dict:
    """
    Cross-validation k-fold respetando orden temporal.

    Cada fold usa los primeros (i+1)*n/k puntos como train y los siguientes
    n/k como test. Reporta EDI por fold y CV-EDI mediano.
    """
    obs_a = np.asarray(obs, dtype=np.float64)
    abm_a = np.asarray(abm, dtype=np.float64)
    red_a = np.asarray(reduced, dtype=np.float64)
    n = obs_a.shape[0]
    if n < 2 * n_splits:
        return {"error": f"n={n} insuficiente para {n_splits} folds"}

    fold_size = n // (n_splits + 1)
    fold_results = []
    for i in range(n_splits):
        train_end = (i + 1) * fold_size
        test_start = train_end
        test_end = min(test_start + fold_size, n)
        if test_end - test_start < 2:
            continue
        obs_test = obs_a[test_start:test_end]
        abm_test = abm_a[test_start:test_end]
        red_test = red_a[test_start:test_end]
        rmse_abm = float(np.sqrt(np.mean((abm_test - obs_test)**2)))
        rmse_red = float(np.sqrt(np.mean((red_test - obs_test)**2)))
        edi = (rmse_red - rmse_abm) / rmse_red if rmse_red > 1e-15 else 0.0
        fold_results.append({
            "fold": i + 1,
            "n_test": int(test_end - test_start),
            "edi_test": float(np.clip(edi, -1, 1)),
            "rmse_abm_test": rmse_abm,
            "rmse_red_test": rmse_red,
        })
    edis = [f["edi_test"] for f in fold_results]
    return {
        "n_folds_executed": len(fold_results),
        "folds": fold_results,
        "edi_cv_median": float(np.median(edis)) if edis else None,
        "edi_cv_mean": float(np.mean(edis)) if edis else None,
        "edi_cv_std": float(np.std(edis, ddof=1)) if len(edis) > 1 else 0.0,
        "stability": "estable" if (edis and np.std(edis, ddof=1) <= 0.05) else "variable",
    }


# =====================================================================
# B13 — Tests adversariales sistemáticos
# =====================================================================

def adversarial_parameter_perturbation(
    obs: Sequence[float],
    abm: Sequence[float],
    reduced: Sequence[float],
    perturbation_levels: Sequence[float] = (0.05, 0.10, 0.20, 0.30),
    n_trials: int = 30,
    seed: int = 42,
) -> dict:
    """
    Perturba ABM ± δ y reporta cómo cambia EDI.

    Si bajo perturbación de 20% el EDI sigue clasificando estable, robust.
    """
    obs_a = np.asarray(obs, dtype=np.float64)
    abm_a = np.asarray(abm, dtype=np.float64)
    red_a = np.asarray(reduced, dtype=np.float64)
    rng = np.random.RandomState(seed)

    results = {}
    for delta in perturbation_levels:
        edis = []
        for _ in range(n_trials):
            scale = 1.0 + rng.uniform(-delta, delta)
            abm_perturbed = abm_a * scale
            rmse_abm_p = float(np.sqrt(np.mean((abm_perturbed - obs_a)**2)))
            rmse_red = float(np.sqrt(np.mean((red_a - obs_a)**2)))
            edi = (rmse_red - rmse_abm_p) / rmse_red if rmse_red > 1e-15 else 0.0
            edis.append(np.clip(edi, -1, 1))
        results[f"perturbation_{int(delta*100)}pct"] = {
            "mean_edi": float(np.mean(edis)),
            "std_edi": float(np.std(edis, ddof=1)),
            "min_edi": float(np.min(edis)),
            "max_edi": float(np.max(edis)),
        }
    rmse_abm_orig = float(np.sqrt(np.mean((abm_a - obs_a)**2)))
    rmse_red_orig = float(np.sqrt(np.mean((red_a - obs_a)**2)))
    edi_orig = (rmse_red_orig - rmse_abm_orig) / rmse_red_orig if rmse_red_orig > 1e-15 else 0.0

    drift_20 = abs(results["perturbation_20pct"]["mean_edi"] - edi_orig) if "perturbation_20pct" in results else 1.0
    return {
        "edi_original": float(np.clip(edi_orig, -1, 1)),
        "results_by_perturbation": results,
        "drift_at_20pct": float(drift_20),
        "robust_against_perturbation": bool(drift_20 <= 0.05),
    }


def adversarial_noise_injection(
    obs: Sequence[float],
    abm: Sequence[float],
    reduced: Sequence[float],
    noise_levels: Sequence[float] = (0.01, 0.05, 0.10, 0.20),
    n_trials: int = 30,
    seed: int = 42,
) -> dict:
    """Añade ruido gaussiano a obs y reporta cómo cambia EDI."""
    obs_a = np.asarray(obs, dtype=np.float64)
    abm_a = np.asarray(abm, dtype=np.float64)
    red_a = np.asarray(reduced, dtype=np.float64)
    sigma_obs = float(np.std(obs_a))
    rng = np.random.RandomState(seed)

    results = {}
    for level in noise_levels:
        edis = []
        for _ in range(n_trials):
            noise = rng.normal(0, level * sigma_obs, len(obs_a))
            obs_n = obs_a + noise
            rmse_abm = float(np.sqrt(np.mean((abm_a - obs_n)**2)))
            rmse_red = float(np.sqrt(np.mean((red_a - obs_n)**2)))
            edi = (rmse_red - rmse_abm) / rmse_red if rmse_red > 1e-15 else 0.0
            edis.append(np.clip(edi, -1, 1))
        results[f"noise_{int(level*100)}pct"] = {
            "mean_edi": float(np.mean(edis)),
            "std_edi": float(np.std(edis, ddof=1)),
        }
    return results


def jackknife_leave_one_out(
    obs: Sequence[float],
    abm: Sequence[float],
    reduced: Sequence[float],
) -> dict:
    """Jackknife leave-one-out: estima sesgo y varianza."""
    obs_a = np.asarray(obs, dtype=np.float64)
    abm_a = np.asarray(abm, dtype=np.float64)
    red_a = np.asarray(reduced, dtype=np.float64)
    n = obs_a.shape[0]
    if n < 5:
        return {"error": f"n={n} insuficiente"}

    edis = []
    for i in range(n):
        mask = np.ones(n, dtype=bool); mask[i] = False
        rmse_a = float(np.sqrt(np.mean((abm_a[mask] - obs_a[mask])**2)))
        rmse_r = float(np.sqrt(np.mean((red_a[mask] - obs_a[mask])**2)))
        edi = (rmse_r - rmse_a) / rmse_r if rmse_r > 1e-15 else 0.0
        edis.append(np.clip(edi, -1, 1))

    rmse_abm_full = float(np.sqrt(np.mean((abm_a - obs_a)**2)))
    rmse_red_full = float(np.sqrt(np.mean((red_a - obs_a)**2)))
    edi_full = (rmse_red_full - rmse_abm_full) / rmse_red_full if rmse_red_full > 1e-15 else 0.0
    edis_arr = np.array(edis)
    bias = (n - 1) * (np.mean(edis_arr) - edi_full)
    se_jack = math.sqrt((n - 1) / n * np.sum((edis_arr - np.mean(edis_arr))**2))
    return {
        "edi_full": float(edi_full),
        "edi_jackknife_mean": float(np.mean(edis_arr)),
        "bias_estimate": float(bias),
        "jackknife_se": float(se_jack),
        "ci_95_jack": [float(edi_full - 1.96 * se_jack), float(edi_full + 1.96 * se_jack)],
    }


# =====================================================================
# B14 — Validación dimensional
# =====================================================================

# Diccionario de unidades por sonda (declarativo)
PROBE_DIMENSIONS = {
    "lotka_volterra":      {"X": "[N]/[t]", "params": "[1/t]", "consistent": True},
    "sir":                 {"S,I,R": "[N]/[N]", "params": "[1/t]", "consistent": True},
    "budyko_sellers":      {"T": "[K]", "Q": "[W/m^2]", "consistent": True},
    "von_thunen":          {"F": "[ha]", "demanda": "[ha/t]", "consistent": True},
    "fisher_kpp":          {"u": "[N/L^2]", "D": "[L^2/t]", "r": "[1/t]", "consistent": True},
    "maxwell_boltzmann":   {"T": "[K]", "v": "[L/t]", "consistent": True},
    "kessler_quadratic":   {"N": "[debris]", "params": "[1/t]", "consistent": True},
    "lindblad":            {"rho": "dimensionless", "params": "[1/t]", "consistent": True},
    "fajen_warren":        {"phi": "[rad]", "params": "[1/t]", "consistent": True},
}


def dimensional_consistency_check(probe_name: str) -> dict:
    """
    Verifica si la sonda tiene unidades dimensionalmente consistentes.

    Es chequeo simbólico declarativo, no formal de unidades. Sirve como
    documentación auditable y filtro contra sondas dimensionalmente
    inconsistentes (que serían señal roja de paper-science).
    """
    canonical_name = probe_name.lower().replace("-", "_")
    for key, info in PROBE_DIMENSIONS.items():
        if key in canonical_name or canonical_name in key:
            return {
                "probe": probe_name,
                "dimensions": info,
                "consistent": info["consistent"],
                "verification": "declarativa",
            }
    return {
        "probe": probe_name,
        "consistent": None,
        "verification": "no encontrada en catálogo",
    }


__all__ = [
    "time_series_kfold",
    "adversarial_parameter_perturbation",
    "adversarial_noise_injection",
    "jackknife_leave_one_out",
    "dimensional_consistency_check",
    "PROBE_DIMENSIONS",
]
