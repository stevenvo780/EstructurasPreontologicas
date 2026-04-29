"""
Calibración estadística avanzada — bloque científico B1 (V5.1).

Cierra parcialmente la deuda L1 (p-value mal calibrado al 24% empírico) sin
re-ejecutar el corpus completo. Provee tres herramientas complementarias:

1. block_bootstrap_pvalue: permutación por bloques (Politis-Romano 1994)
   que respeta la autocorrelación temporal de las series. Bloques de tamaño
   sqrt(n) por defecto.

2. newey_west_se: error estándar HAC (Heteroskedasticity- and
   Autocorrelation-Consistent) según Newey-West (1987). Aplicable cuando
   el ruido de la serie tiene autocorrelación de orden bajo.

3. fwer_correct: corrección de family-wise error rate por Bonferroni
   y Holm-Bonferroni (Holm 1979) sobre el corpus de N casos para
   control de falsos positivos bajo comparaciones múltiples.

Referencias:
- Politis, D. N. y Romano, J. P. (1994). "The Stationary Bootstrap".
  Journal of the American Statistical Association 89(428): 1303-1313.
- Newey, W. K. y West, K. D. (1987). "A Simple, Positive Semi-Definite,
  Heteroskedasticity and Autocorrelation Consistent Covariance Matrix".
  Econometrica 55(3): 703-708.
- Holm, S. (1979). "A Simple Sequentially Rejective Multiple Test
  Procedure". Scandinavian Journal of Statistics 6(2): 65-70.
- Phipson, B. y Smyth, G. K. (2010). "Permutation P-values Should Never
  Be Zero". Statistical Applications in Genetics and Molecular Biology
  9(1): Article 39.

Uso típico:

    from common.calibration import (
        block_bootstrap_pvalue,
        newey_west_se,
        fwer_correct,
    )

    edi_real, p_calibrated, p_naive = block_bootstrap_pvalue(
        obs, abm, reduced, n_perm=2999, seed=42
    )
    se_hac = newey_west_se(residuals, lag=4)
    p_corrected = fwer_correct([0.001, 0.02, 0.04, 0.10], method="holm")
"""
from __future__ import annotations

import math
import numpy as np
from typing import Iterable, Sequence


def _rmse(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """RMSE vectorizado a lo largo del último eje."""
    return np.sqrt(np.mean((a - b) ** 2, axis=-1))


def _compute_edi_vec(rmse_abm: np.ndarray, rmse_red: np.ndarray) -> np.ndarray:
    """EDI vectorizado con guarda contra división por cero."""
    mask = rmse_red > 1e-15
    edi = np.where(mask, (rmse_red - rmse_abm) / rmse_red, 0.0)
    return np.clip(edi, -1.0, 1.0)


def standardize_series(series: Sequence[float]) -> tuple[np.ndarray, dict]:
    """
    Estandariza una serie temporal a media 0 y desviación 1.

    EDI es sensible al rango de las series cuando el ratio
    RMSE_coupled/RMSE_no_ode depende de la magnitud absoluta. La
    estandarización reduce esa sensibilidad reportando comparaciones
    sobre series adimensionales.

    Returns
    -------
    standardized : np.ndarray
    info : dict con mean y std originales para revertir si hace falta
    """
    a = np.asarray(series, dtype=np.float64)
    mu = float(a.mean())
    sigma = float(a.std(ddof=0))
    if sigma <= 1e-15:
        return a - mu, {"mean": mu, "std": sigma, "standardized": False}
    return (a - mu) / sigma, {"mean": mu, "std": sigma, "standardized": True}


def edi_with_standardization_check(
    obs: Sequence[float],
    abm_coupled: Sequence[float],
    abm_no_ode: Sequence[float],
) -> dict:
    """
    Computa EDI sobre las series originales y sobre las series estandarizadas
    (z-score). Reporta ambos valores para auditar la sensibilidad de EDI al
    rango de las series.

    Si |EDI_raw - EDI_standardized| > 0.05, las series tienen diferencias
    de escala que afectan la métrica; el caso debe reportar el EDI
    estandarizado como referencia primaria.
    """
    obs_a = np.asarray(obs, dtype=np.float64)
    abm_a = np.asarray(abm_coupled, dtype=np.float64)
    red_a = np.asarray(abm_no_ode, dtype=np.float64)

    rmse_abm_raw = float(np.sqrt(np.mean((abm_a - obs_a) ** 2)))
    rmse_red_raw = float(np.sqrt(np.mean((red_a - obs_a) ** 2)))
    edi_raw = (
        float((rmse_red_raw - rmse_abm_raw) / rmse_red_raw)
        if rmse_red_raw > 1e-15 else 0.0
    )

    obs_z, info = standardize_series(obs_a)
    abm_z = (abm_a - info["mean"]) / max(info["std"], 1e-12)
    red_z = (red_a - info["mean"]) / max(info["std"], 1e-12)
    rmse_abm_z = float(np.sqrt(np.mean((abm_z - obs_z) ** 2)))
    rmse_red_z = float(np.sqrt(np.mean((red_z - obs_z) ** 2)))
    edi_z = (
        float((rmse_red_z - rmse_abm_z) / rmse_red_z)
        if rmse_red_z > 1e-15 else 0.0
    )

    drift = abs(edi_raw - edi_z)
    return {
        "edi_raw": float(np.clip(edi_raw, -1.0, 1.0)),
        "edi_standardized": float(np.clip(edi_z, -1.0, 1.0)),
        "drift_due_to_scale": float(drift),
        "scale_sensitive": bool(drift > 0.05),
        "info": info,
        "interpretation": (
            "EDI estable bajo estandarización; la métrica no es sensible al rango."
            if drift <= 0.05
            else f"EDI cambia |Δ|={drift:.3f} bajo estandarización; reportar el "
                 "valor estandarizado como referencia primaria."
        ),
    }


def block_bootstrap_pvalue(
    obs_val: Sequence[float],
    abm_val: Sequence[float],
    reduced_val: Sequence[float],
    n_perm: int = 2999,
    block_size: int | None = None,
    method: str = "stationary",
    seed: int = 42,
) -> tuple[float, float, float]:
    """
    Block-bootstrap para EDI bajo autocorrelación temporal.

    method = "stationary": stationary bootstrap de Politis-Romano (1994).
        Los bloques tienen LONGITUD GEOMÉTRICA aleatoria con parámetro
        p = 1/block_size. Esto produce un proceso bootstrap estacionario
        cuya autocorrelación se preserva en promedio. Es la implementación
        canónica de Politis-Romano (1994).

    method = "moving": moving block bootstrap clásico (Künsch 1989).
        Bloques de longitud fija. Más simple; subconvergente bajo
        no-estacionariedad.

    Por defecto block_size promedio = max(2, ceil(sqrt(n))) (Politis-Romano
    1994 recomienda elegirlo proporcional a la longitud de autocorrelación;
    sqrt(n) es valor por defecto razonable bajo estacionariedad débil).

    Returns
    -------
    edi_real : float
        EDI puntual sobre los datos sin permutar.
    p_block : float
        p-value calibrado bajo el método elegido.
    p_naive : float
        p-value bajo permutación simple (legacy); se reporta para
        comparación y para cuantificar el shift de calibración.

    References
    ----------
    Politis, D. N. y Romano, J. P. (1994). "The Stationary Bootstrap".
        *Journal of the American Statistical Association* 89(428): 1303-1313.
    Künsch, H. R. (1989). "The Jackknife and the Bootstrap for General
        Stationary Observations". *Annals of Statistics* 17(3): 1217-1241.
    """
    obs = np.asarray(obs_val, dtype=np.float64)
    abm = np.asarray(abm_val, dtype=np.float64)
    red = np.asarray(reduced_val, dtype=np.float64)
    n = obs.shape[0]
    if n < 4:
        edi_real = float(_compute_edi_vec(_rmse(abm, obs), _rmse(red, obs)))
        return edi_real, 1.0, 1.0

    if block_size is None:
        block_size = max(2, int(math.ceil(math.sqrt(n))))
    block_size = min(block_size, n)

    edi_real = float(_compute_edi_vec(
        _rmse(abm, obs).reshape(()), _rmse(red, obs).reshape(())
    ))

    rng = np.random.RandomState(seed)

    if method == "stationary":
        # Stationary bootstrap (Politis-Romano 1994): para cada posición
        # de la serie remuestreada, se conserva el siguiente índice con
        # probabilidad 1 - p (p = 1/block_size esperado), y se reinicia
        # con un índice aleatorio con probabilidad p.
        p_geom = 1.0 / block_size
        idx_matrix = np.empty((n_perm, n), dtype=np.int64)
        for i in range(n_perm):
            idx = np.empty(n, dtype=np.int64)
            idx[0] = rng.randint(0, n)
            jumps = rng.uniform(0, 1, n) < p_geom
            for t in range(1, n):
                if jumps[t]:
                    idx[t] = rng.randint(0, n)
                else:
                    idx[t] = (idx[t - 1] + 1) % n
            idx_matrix[i] = idx
        obs_perm_block = obs[idx_matrix]
    elif method == "moving":
        # Moving block bootstrap (Künsch 1989): bloques de longitud fija.
        n_blocks = int(math.ceil(n / block_size))
        starts = rng.randint(0, max(1, n - block_size + 1), size=(n_perm, n_blocks))
        offsets = np.arange(block_size)
        idx_blocks = (starts[:, :, None] + offsets[None, None, :]).reshape(n_perm, -1)[:, :n]
        obs_perm_block = obs[idx_blocks]
    else:
        raise ValueError(f"método desconocido: {method!r}; usar 'stationary' o 'moving'")

    rmse_abm_null_b = _rmse(abm[None, :], obs_perm_block)
    rmse_red_null_b = _rmse(red[None, :], obs_perm_block)
    null_edis_block = _compute_edi_vec(rmse_abm_null_b, rmse_red_null_b)
    p_block = float((np.sum(null_edis_block >= edi_real) + 1) / (n_perm + 1))

    # Permutación simple (legacy) para comparación
    idx_naive = np.array([rng.permutation(n) for _ in range(n_perm)])
    obs_perm_naive = obs[idx_naive]
    rmse_abm_null_n = _rmse(abm[None, :], obs_perm_naive)
    rmse_red_null_n = _rmse(red[None, :], obs_perm_naive)
    null_edis_naive = _compute_edi_vec(rmse_abm_null_n, rmse_red_null_n)
    p_naive = float((np.sum(null_edis_naive >= edi_real) + 1) / (n_perm + 1))

    return edi_real, p_block, p_naive


def newey_west_se(residuals: Sequence[float], lag: int | None = None) -> float:
    """
    Error estándar HAC de Newey-West (1987).

    Para una serie de residuales con posible autocorrelación de orden bajo,
    devuelve el error estándar consistente bajo heterocedasticidad y
    autocorrelación. Útil para construir intervalos de confianza correctos
    sobre estadísticos de EDI cuando los residuales no son iid.

    Parameters
    ----------
    residuals : array-like
        Serie de residuales (e.g. obs - pred_modelo).
    lag : int, optional
        Truncamiento de Bartlett. Default: floor(4 * (n/100)^(2/9)),
        siguiendo Newey-West (1994 update).

    Returns
    -------
    se_hac : float
        Error estándar HAC. Si no hay autocorrelación, coincide con SE clásico.
    """
    r = np.asarray(residuals, dtype=np.float64)
    n = r.shape[0]
    if n < 4:
        return float(np.std(r, ddof=1) / math.sqrt(n)) if n > 1 else 0.0

    if lag is None:
        lag = int(math.floor(4.0 * (n / 100.0) ** (2.0 / 9.0)))
    lag = max(0, min(lag, n - 1))

    r_centered = r - r.mean()
    gamma_0 = float(np.dot(r_centered, r_centered) / n)
    s_long = gamma_0
    for k in range(1, lag + 1):
        weight = 1.0 - k / (lag + 1.0)  # kernel de Bartlett
        gamma_k = float(np.dot(r_centered[k:], r_centered[:-k]) / n)
        s_long += 2.0 * weight * gamma_k

    s_long = max(s_long, 1e-15)  # garantizar positivo semidefinido
    return float(math.sqrt(s_long / n))


def fwer_correct(
    p_values: Sequence[float],
    method: str = "holm",
    alpha: float = 0.05,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Corrección de family-wise error rate (FWER) por Bonferroni o Holm.

    Bajo comparaciones múltiples (e.g. los 30 casos del corpus inter-dominio),
    cada caso individual con p < 0.05 NO basta para afirmar significancia
    global. La corrección controla la probabilidad de al menos un falso
    positivo en la familia.

    Parameters
    ----------
    p_values : array-like de float
        p-values de cada caso, en orden arbitrario.
    method : {"bonferroni", "holm"}
        - "bonferroni": p_i' = min(p_i * m, 1). Más conservador.
        - "holm": Holm-Bonferroni (1979). Stepwise; más potente que
          Bonferroni manteniendo el mismo control FWER.
    alpha : float
        Nivel global de FWER deseado (default 0.05).

    Returns
    -------
    p_adj : np.ndarray
        p-values ajustados, en el orden original.
    rejected : np.ndarray bool
        Vector booleano: True si p_adj_i <= alpha tras corrección.
    """
    p = np.asarray(p_values, dtype=np.float64)
    m = p.shape[0]
    if m == 0:
        return p, np.array([], dtype=bool)

    if method == "bonferroni":
        p_adj = np.minimum(p * m, 1.0)
        return p_adj, p_adj <= alpha

    if method == "holm":
        order = np.argsort(p)
        ranked = p[order]
        adjusted_ranked = np.empty(m)
        running_max = 0.0
        for i in range(m):
            adj = ranked[i] * (m - i)
            adj = min(adj, 1.0)
            running_max = max(running_max, adj)
            adjusted_ranked[i] = running_max
        p_adj = np.empty(m)
        p_adj[order] = adjusted_ranked
        return p_adj, p_adj <= alpha

    raise ValueError(f"método FWER desconocido: {method!r}; usar 'bonferroni' o 'holm'")


def calibrated_inference_summary(
    edi_value: float,
    p_block: float,
    p_naive: float,
    bootstrap_ci: tuple[float, float],
    se_hac: float | None = None,
    fwer_corpus: dict | None = None,
) -> dict:
    """
    Síntesis del estado inferencial calibrado para un caso.

    Devuelve un dict serializable que se inyecta en outputs/metrics.json
    bajo la clave "calibrated_inference". Permite que cualquier evaluador
    externo reproduzca la inferencia bajo el régimen calibrado V5.1 sin
    tener que re-ejecutar el corpus completo.

    Returns
    -------
    summary : dict
        - edi: valor puntual
        - p_value_calibrated: p-value bajo block-bootstrap
        - p_value_naive: p-value bajo permutación simple (legacy)
        - p_value_shift: |p_calibrated - p_naive| (cuantifica miscalibración)
        - bootstrap_ci_95: intervalo
        - newey_west_se: SE HAC si los residuales se proveyeron
        - fwer_position: posición del caso en la corrección Holm si aplica
        - inferencia_robusta: bool — True si p_calibrated <= 0.05 y EDI > 0
    """
    summary = {
        "edi": float(edi_value),
        "p_value_calibrated_block": float(p_block),
        "p_value_naive_permutation": float(p_naive),
        "p_value_shift": float(abs(p_block - p_naive)),
        "bootstrap_ci_95": [float(bootstrap_ci[0]), float(bootstrap_ci[1])],
        "newey_west_se": float(se_hac) if se_hac is not None else None,
        "fwer_position": fwer_corpus,
        "inferencia_robusta": bool(p_block <= 0.05 and edi_value > 0),
        "calibration_protocol_version": "V5.1",
        "method": "block_bootstrap_2999_perm",
    }
    return summary


__all__ = [
    "block_bootstrap_pvalue",
    "newey_west_se",
    "fwer_correct",
    "calibrated_inference_summary",
]
