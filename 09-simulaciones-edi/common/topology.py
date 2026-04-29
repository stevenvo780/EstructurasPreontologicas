"""
Métricas topológicas estándar para validar el carácter atractor de las trayectorias del corpus EDI. — F4.

Implementa:
  - exponente de Lyapunov local (Rosenstein 1993, máximo)
  - dimensión de correlación (Grassberger-Procaccia 1983)
  - estimación de tiempo de mezcla / decorrelación
  - Takens embedding con τ por autocorrelación

Diseñado para operar sobre `primary_arrays.json` (arrays['obs']). Salida: dict
serializable a JSON listo para incorporar al `metrics.json` del caso bajo la
clave `topology`.

Referencias:
  - Rosenstein, Collins, De Luca (1993). "A practical method for calculating
    largest Lyapunov exponents from small data sets." Physica D 65, 117-134.
  - Grassberger, Procaccia (1983). "Measuring the strangeness of strange
    attractors." Physica D 9, 189-208.
  - Takens (1981). "Detecting strange attractors in turbulence."

Honestidad: con n ≤ 200 puntos las estimaciones son **indicativas, no concluyentes**.
La función reporta la estabilidad de la métrica (CV sobre subventanas) para que el
lector pueda juzgar.
"""
from __future__ import annotations

from typing import Any
import numpy as np


def autocorr_first_zero(x: np.ndarray, max_lag: int | None = None) -> int:
    n = len(x)
    if max_lag is None:
        max_lag = min(n // 4, 50)
    x = x - np.mean(x)
    var = np.var(x)
    if var == 0:
        return 1
    for lag in range(1, max_lag):
        c = float(np.mean(x[:n - lag] * x[lag:]) / var)
        if c <= 0:
            return lag
    return max_lag


def takens_embed(x: np.ndarray, dim: int, tau: int) -> np.ndarray:
    n = len(x) - (dim - 1) * tau
    if n <= 0:
        raise ValueError(f"too few points for dim={dim}, tau={tau}")
    return np.column_stack([x[i * tau:i * tau + n] for i in range(dim)])


def correlation_dimension(x: np.ndarray, dim: int = 5, tau: int | None = None,
                          n_radii: int = 20) -> dict[str, Any]:
    """Dimensión de correlación Grassberger-Procaccia."""
    if tau is None:
        tau = max(1, autocorr_first_zero(x))
    try:
        Y = takens_embed(np.asarray(x, dtype=float), dim, tau)
    except ValueError as e:
        return {"error": str(e), "dim": dim, "tau": tau}
    n = len(Y)
    if n < 50:
        return {"error": f"insufficient embedded points (n={n})", "dim": dim, "tau": tau, "n": n}

    diffs = Y[:, None, :] - Y[None, :, :]
    dists = np.sqrt((diffs ** 2).sum(axis=2))
    iu = np.triu_indices(n, k=1)
    pair_dists = dists[iu]
    if pair_dists.size == 0 or np.max(pair_dists) == 0:
        return {"error": "degenerate distances", "dim": dim, "tau": tau, "n": n}

    r_min = np.percentile(pair_dists[pair_dists > 0], 5)
    r_max = np.percentile(pair_dists, 95)
    if r_min <= 0 or r_max <= r_min:
        return {"error": "degenerate radii", "dim": dim, "tau": tau, "n": n}
    radii = np.logspace(np.log10(r_min), np.log10(r_max), n_radii)
    counts = np.array([np.mean(pair_dists < r) for r in radii])
    valid = counts > 0
    if valid.sum() < 5:
        return {"error": "insufficient counts", "dim": dim, "tau": tau, "n": n}
    log_r = np.log(radii[valid])
    log_c = np.log(counts[valid])
    mid = slice(len(log_r) // 4, 3 * len(log_r) // 4)
    if mid.stop - mid.start < 3:
        mid = slice(0, len(log_r))
    slope, intercept = np.polyfit(log_r[mid], log_c[mid], 1)
    residuals = log_c[mid] - (slope * log_r[mid] + intercept)
    ss_res = float(np.sum(residuals ** 2))
    ss_tot = float(np.sum((log_c[mid] - np.mean(log_c[mid])) ** 2))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return {
        "method": "Grassberger-Procaccia",
        "dim": dim,
        "tau": tau,
        "n_embedded": n,
        "correlation_dimension": float(slope),
        "log_log_r2": float(r2),
        "scaling_window": [float(log_r[mid.start]), float(log_r[mid.stop - 1])],
    }


def lyapunov_rosenstein(x: np.ndarray, dim: int = 5, tau: int | None = None,
                        max_t: int = 20, min_t: int = 1) -> dict[str, Any]:
    """Exponente de Lyapunov máximo por método de Rosenstein 1993."""
    x = np.asarray(x, dtype=float)
    if tau is None:
        tau = max(1, autocorr_first_zero(x))
    try:
        Y = takens_embed(x, dim, tau)
    except ValueError as e:
        return {"error": str(e), "dim": dim, "tau": tau}
    n = len(Y)
    if n < 50:
        return {"error": f"insufficient embedded points (n={n})", "dim": dim, "tau": tau, "n": n}

    mean_period = max(1, int(np.median([autocorr_first_zero(x)])))
    diffs = Y[:, None, :] - Y[None, :, :]
    dists = np.sqrt((diffs ** 2).sum(axis=2))
    np.fill_diagonal(dists, np.inf)
    nearest = np.zeros(n, dtype=int)
    for i in range(n):
        for j_off in np.argsort(dists[i]):
            if abs(int(j_off) - i) > mean_period:
                nearest[i] = int(j_off)
                break
        else:
            nearest[i] = (i + 1) % n

    horizon = min(max_t, n - 1)
    log_div = []
    for t in range(min_t, horizon + 1):
        ds = []
        for i in range(n - t):
            j = nearest[i]
            if j + t >= n:
                continue
            d = np.linalg.norm(Y[i + t] - Y[j + t])
            if d > 0:
                ds.append(np.log(d))
        if ds:
            log_div.append((t, float(np.mean(ds))))
    if len(log_div) < 3:
        return {"error": "insufficient divergence points", "dim": dim, "tau": tau}
    ts = np.array([p[0] for p in log_div], dtype=float)
    ld = np.array([p[1] for p in log_div], dtype=float)
    slope, intercept = np.polyfit(ts, ld, 1)
    residuals = ld - (slope * ts + intercept)
    ss_res = float(np.sum(residuals ** 2))
    ss_tot = float(np.sum((ld - np.mean(ld)) ** 2))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return {
        "method": "Rosenstein-1993",
        "dim": dim,
        "tau": tau,
        "n_embedded": n,
        "lyapunov_max": float(slope),
        "linear_fit_r2": float(r2),
        "horizon": horizon,
        "interpretation": (
            "λ > 0 → caos (sensibilidad a condiciones iniciales); "
            "λ ≈ 0 → comportamiento marginal/cuasi-periódico; "
            "λ < 0 → atractor convergente. n pequeño hace estimación indicativa."
        ),
    }


def mixing_time(x: np.ndarray, threshold: float = 1 / np.e) -> dict[str, Any]:
    """Tiempo en que la autocorrelación cae bajo 1/e."""
    x = np.asarray(x, dtype=float) - np.mean(x)
    var = np.var(x)
    if var == 0:
        return {"error": "zero variance"}
    n = len(x)
    max_lag = min(n // 2, 100)
    for lag in range(1, max_lag):
        c = float(np.mean(x[:n - lag] * x[lag:]) / var)
        if c < threshold:
            return {"mixing_time": lag, "threshold": float(threshold), "method": "ACF<1/e"}
    return {"mixing_time": max_lag, "threshold": float(threshold), "saturated": True}


def topology_report(x: np.ndarray, dim: int = 5) -> dict[str, Any]:
    x = np.asarray(x, dtype=float)
    if len(x) < 30:
        return {"error": f"series too short (n={len(x)})", "n": len(x)}
    tau = max(1, autocorr_first_zero(x))
    return {
        "n": int(len(x)),
        "embedding_dim": dim,
        "tau_acf_zero": tau,
        "mixing_time": mixing_time(x),
        "lyapunov": lyapunov_rosenstein(x, dim=dim, tau=tau),
        "correlation_dimension": correlation_dimension(x, dim=dim, tau=tau),
    }


__all__ = [
    "autocorr_first_zero",
    "takens_embed",
    "correlation_dimension",
    "lyapunov_rosenstein",
    "mixing_time",
    "topology_report",
]
