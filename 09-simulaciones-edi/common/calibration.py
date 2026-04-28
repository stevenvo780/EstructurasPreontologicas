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


def block_bootstrap_pvalue(
    obs_val: Sequence[float],
    abm_val: Sequence[float],
    reduced_val: Sequence[float],
    n_perm: int = 2999,
    block_size: int | None = None,
    seed: int = 42,
) -> tuple[float, float, float]:
    """
    Block-permutation test para EDI bajo autocorrelación temporal.

    A diferencia de la permutación independiente clásica (que asume
    intercambiabilidad bajo H0), este test permuta bloques contiguos de
    tamaño `block_size`, preservando la estructura local de autocorrelación.
    Esto evita la inflación del Type-I error que ocurre cuando las series
    tienen memoria.

    Por defecto block_size = max(2, ceil(sqrt(n))), siguiendo la
    recomendación estándar para estacionariedad débil.

    Returns
    -------
    edi_real : float
        EDI puntual sobre los datos sin permutar.
    p_block : float
        p-value calibrado bajo block-bootstrap (más conservador y
        correctamente calibrado bajo autocorrelación).
    p_naive : float
        p-value bajo permutación simple (la versión miscalibrada legacy);
        se reporta para comparación y para cuantificar el shift.
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
    n_blocks = int(math.ceil(n / block_size))

    edi_real = float(_compute_edi_vec(
        _rmse(abm, obs).reshape(()), _rmse(red, obs).reshape(())
    ))

    rng = np.random.RandomState(seed)

    # ------- block-bootstrap -------
    # Para cada permutación: tomamos n_blocks índices de inicio aleatorios
    # y concatenamos bloques de longitud block_size.
    starts = rng.randint(0, max(1, n - block_size + 1), size=(n_perm, n_blocks))
    # Construir matriz de índices (n_perm, n)
    offsets = np.arange(block_size)
    idx_blocks = (starts[:, :, None] + offsets[None, None, :]).reshape(n_perm, -1)[:, :n]
    obs_perm_block = obs[idx_blocks]  # (n_perm, n)
    rmse_abm_null_b = _rmse(abm[None, :], obs_perm_block)
    rmse_red_null_b = _rmse(red[None, :], obs_perm_block)
    null_edis_block = _compute_edi_vec(rmse_abm_null_b, rmse_red_null_b)
    p_block = float((np.sum(null_edis_block >= edi_real) + 1) / (n_perm + 1))

    # ------- permutación simple (legacy) para comparación -------
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
