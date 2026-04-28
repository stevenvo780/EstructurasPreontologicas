"""
Replicación robusta — bloque científico B2 (V5.1).

Cierra parcialmente la deuda L4 (AUC-ROC interno) sin requerir replicador
externo. Provee tres tests complementarios:

1. seed_robustness: distribución de EDI bajo cambio de semilla
   pseudoaleatoria. Si la varianza inter-seed es alta, el resultado
   depende del ruido del muestreo y no de la estructura del fenómeno.

2. holdout_temporal: cálculo de EDI sobre un subconjunto fuera de
   muestra (last 20% por defecto), para detectar leakage train-test
   y sobreajuste a la ventana completa.

3. adversarial_probe_swap: aplicar las sondas de un caso A sobre los
   datos de otro caso B. Si las sondas no son específicas, el EDI
   cruzado debería ser distintamente alto. Si son específicas (caso
   esperado), el EDI cruzado colapsa hacia 0 o negativo. Esto extiende
   el test cruzado V4-01 (inter-escala) al corpus inter-dominio.

Estos tres tests son complementarios y permiten construir un perfil de
robustez que un evaluador externo puede inspeccionar sin necesidad de
re-ejecutar el corpus completo. Cualquier replicador independiente puede
correr exactamente este módulo sobre los outputs versionados y verificar
las afirmaciones del manuscrito.

Uso típico:

    from common.replication import (
        seed_robustness,
        holdout_temporal,
        adversarial_probe_swap,
    )

    seed_dist = seed_robustness(
        run_case_fn, base_kwargs, seeds=[1, 7, 13, 17, 23]
    )
    holdout = holdout_temporal(obs, abm, reduced, train_frac=0.8)
    adversarial = adversarial_probe_swap(probe_fn_A, data_B, expected_low=True)
"""
from __future__ import annotations

import numpy as np
from typing import Callable, Sequence


def _rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((a - b) ** 2)))


def _edi(rmse_abm: float, rmse_red: float) -> float:
    if rmse_red <= 1e-15:
        return 0.0
    return float(np.clip((rmse_red - rmse_abm) / rmse_red, -1.0, 1.0))


def seed_robustness(
    run_case_fn: Callable[..., dict],
    base_kwargs: dict,
    seeds: Sequence[int] = (1, 7, 13, 17, 23, 42),
    edi_key: str = "edi",
) -> dict:
    """
    Mide la robustez del EDI bajo cambio de semilla pseudoaleatoria.

    Parameters
    ----------
    run_case_fn : callable
        Función que ejecuta el caso completo y devuelve un dict con
        al menos la clave `edi_key`. Debe aceptar `seed` como kwarg.
    base_kwargs : dict
        Argumentos base para run_case_fn (todo excepto seed).
    seeds : sequence of int
        Lista de semillas a evaluar.
    edi_key : str
        Clave dentro del resultado donde se encuentra el valor de EDI.

    Returns
    -------
    summary : dict
        - seeds: lista de semillas
        - edis: lista de EDIs correspondientes
        - mean: media inter-seed
        - std: desviación inter-seed
        - cv: coeficiente de variación |std/mean|
        - max_drift: |max(edis) - min(edis)|
        - robust: True si max_drift <= 0.05 (criterio operativo)
        - interpretacion: texto explicativo
    """
    edis = []
    for s in seeds:
        result = run_case_fn(seed=s, **base_kwargs)
        edis.append(float(result[edi_key]))
    edis_arr = np.asarray(edis, dtype=np.float64)

    mean = float(edis_arr.mean())
    std = float(edis_arr.std(ddof=1)) if len(edis) > 1 else 0.0
    cv = float(std / abs(mean)) if abs(mean) > 1e-12 else float("inf")
    max_drift = float(edis_arr.max() - edis_arr.min())
    robust = bool(max_drift <= 0.05)

    if robust:
        interpretacion = (
            "EDI estable bajo cambio de semilla (max_drift ≤ 0.05). "
            "El resultado NO depende del ruido pseudoaleatorio; refleja "
            "estructura del fenómeno."
        )
    elif max_drift <= 0.10:
        interpretacion = (
            "EDI moderadamente estable (0.05 < max_drift ≤ 0.10). "
            "Hay sensibilidad al ruido pseudoaleatorio pero la inferencia "
            "binaria (strong/weak/null) probablemente se preserva. "
            "Reportar el rango."
        )
    else:
        interpretacion = (
            "EDI inestable bajo cambio de semilla (max_drift > 0.10). "
            "El resultado depende sustancialmente del ruido pseudoaleatorio. "
            "Sospecha de overfitting. Investigar antes de reportar como "
            "demostrativo."
        )

    return {
        "seeds": list(seeds),
        "edis": edis,
        "mean": mean,
        "std": std,
        "cv": cv,
        "max_drift": max_drift,
        "robust": robust,
        "interpretacion": interpretacion,
        "criterio": "max_drift ≤ 0.05 → robusto inter-seed",
    }


def holdout_temporal(
    obs: Sequence[float],
    abm: Sequence[float],
    reduced: Sequence[float],
    train_frac: float = 0.8,
    edi_full: float | None = None,
) -> dict:
    """
    Calcula EDI sobre la ventana de test (out-of-sample temporal).

    Si las predicciones del modelo dependen sólo de información disponible
    en la ventana de train, el EDI sobre el test set debe parecerse al EDI
    full (sin train-test leakage). Si el EDI test colapsa, hay leakage.

    Parameters
    ----------
    obs, abm, reduced : array-like
        Series temporales completas.
    train_frac : float
        Fracción de la serie que se considera training (default 0.8).
    edi_full : float, optional
        EDI sobre toda la serie (para comparación; si no se provee se
        computa).

    Returns
    -------
    summary : dict
        - edi_full: EDI sobre toda la serie
        - edi_train: EDI sobre la ventana train (in-sample)
        - edi_test: EDI sobre la ventana test (out-of-sample)
        - delta_test_vs_full: edi_test - edi_full
        - sin_leakage: bool — True si |delta| <= 0.10
        - interpretacion: texto
    """
    obs_a = np.asarray(obs, dtype=np.float64)
    abm_a = np.asarray(abm, dtype=np.float64)
    red_a = np.asarray(reduced, dtype=np.float64)
    n = obs_a.shape[0]
    if n < 10:
        raise ValueError("hold-out temporal requiere n >= 10")

    n_train = int(np.floor(n * train_frac))
    n_train = max(2, min(n - 2, n_train))

    obs_tr, obs_te = obs_a[:n_train], obs_a[n_train:]
    abm_tr, abm_te = abm_a[:n_train], abm_a[n_train:]
    red_tr, red_te = red_a[:n_train], red_a[n_train:]

    if edi_full is None:
        edi_full = _edi(_rmse(abm_a, obs_a), _rmse(red_a, obs_a))
    edi_train = _edi(_rmse(abm_tr, obs_tr), _rmse(red_tr, obs_tr))
    edi_test = _edi(_rmse(abm_te, obs_te), _rmse(red_te, obs_te))

    delta = edi_test - edi_full
    sin_leakage = bool(abs(delta) <= 0.10)

    if sin_leakage:
        interpretacion = (
            f"EDI test ≈ EDI full (|Δ|={abs(delta):.3f} ≤ 0.10). "
            "No hay evidencia de leakage train-test. "
            "El cierre operativo se sostiene fuera de muestra."
        )
    else:
        interpretacion = (
            f"EDI test diverge de EDI full (|Δ|={abs(delta):.3f} > 0.10). "
            "Posible leakage o sobreajuste a la ventana completa. "
            "Investigar antes de reportar como demostrativo."
        )

    return {
        "edi_full": float(edi_full),
        "edi_train": float(edi_train),
        "edi_test": float(edi_test),
        "delta_test_vs_full": float(delta),
        "n_train": int(n_train),
        "n_test": int(n - n_train),
        "sin_leakage": sin_leakage,
        "interpretacion": interpretacion,
        "criterio": "|edi_test - edi_full| ≤ 0.10 → sin leakage",
    }


def adversarial_probe_swap(
    probe_predict_fn_A: Callable[[np.ndarray], np.ndarray],
    obs_data_B: Sequence[float],
    forcing_B: Sequence[float] | None = None,
    abm_baseline_B: Sequence[float] | None = None,
    expected_low: bool = True,
    threshold_low: float = 0.05,
) -> dict:
    """
    Aplica la sonda del caso A sobre los datos del caso B.

    Si las sondas son específicas (motivación teórica distinta entre casos),
    el EDI cruzado debe ser cercano a 0 o negativo. Si las sondas son
    genéricas (capturarían cualquier serie), el EDI cruzado sería alto y
    eso indicaría que el cierre operativo detectado en el caso original
    NO es estructura del fenómeno sino artefacto de la sonda.

    Parameters
    ----------
    probe_predict_fn_A : callable
        Función que toma forcing y devuelve predicción según la sonda
        del caso A (e.g. Lotka-Volterra para Energía).
    obs_data_B : array-like
        Serie observada del caso B (e.g. deforestación, no energía).
    forcing_B : array-like, optional
        Forcing exógeno del caso B. Si None, se usa diff(obs_data_B).
    abm_baseline_B : array-like, optional
        ABM-no-ODE del caso B como baseline. Si None, se usa
        random walk + media móvil.
    expected_low : bool
        Si True, esperamos EDI bajo (sondas específicas; correcto).
    threshold_low : float
        EDI por debajo del cual se considera "específica" (default 0.05).

    Returns
    -------
    summary : dict
        - edi_cruzado: EDI cuando sonda A se aplica sobre datos B
        - especifica: bool — True si edi_cruzado <= threshold_low
        - cumple_expectativa: bool — coincidencia con expected_low
        - interpretacion: texto
    """
    obs_b = np.asarray(obs_data_B, dtype=np.float64)
    n = obs_b.shape[0]

    if forcing_B is None:
        forcing_B = np.diff(obs_b, prepend=obs_b[0])
    forcing_b_arr = np.asarray(forcing_B, dtype=np.float64)[:n]

    pred_a_on_b = probe_predict_fn_A(forcing_b_arr)
    pred_a_on_b = np.asarray(pred_a_on_b, dtype=np.float64)[:n]

    if abm_baseline_B is None:
        # Baseline ingenuo: media móvil
        window = max(2, n // 20)
        kernel = np.ones(window) / window
        abm_baseline_B = np.convolve(obs_b, kernel, mode="same")
    abm_b = np.asarray(abm_baseline_B, dtype=np.float64)[:n]

    rmse_with_probe_a = _rmse(pred_a_on_b, obs_b)
    rmse_baseline = _rmse(abm_b, obs_b)
    edi_cruzado = _edi(rmse_with_probe_a, rmse_baseline)

    especifica = bool(edi_cruzado <= threshold_low)
    cumple_expectativa = bool(especifica == expected_low)

    if especifica and expected_low:
        interpretacion = (
            f"Sonda A es específica al caso de origen. EDI cruzado="
            f"{edi_cruzado:.3f} ≤ {threshold_low}. La sonda no captura "
            "estructura del caso B; confirma que el cierre operativo del "
            "caso de origen no es artefacto de la sonda."
        )
    elif not especifica and expected_low:
        interpretacion = (
            f"PROBLEMA: sonda A captura estructura del caso B "
            f"(EDI cruzado={edi_cruzado:.3f} > {threshold_low}). "
            "La sonda puede ser genérica, no específica al fenómeno "
            "original. Investigar."
        )
    else:
        interpretacion = (
            f"Sonda A captura estructura del caso B (EDI cruzado="
            f"{edi_cruzado:.3f}); esto era lo esperado si la sonda "
            "es genérica."
        )

    return {
        "edi_cruzado": float(edi_cruzado),
        "rmse_with_probe_a_on_b": float(rmse_with_probe_a),
        "rmse_baseline_b": float(rmse_baseline),
        "especifica": especifica,
        "cumple_expectativa": cumple_expectativa,
        "interpretacion": interpretacion,
        "criterio": f"EDI cruzado ≤ {threshold_low} → sonda específica",
    }


def replication_robustness_summary(
    seed_robustness_dict: dict | None = None,
    holdout_dict: dict | None = None,
    adversarial_dicts: list[dict] | None = None,
) -> dict:
    """
    Síntesis del perfil de replicación robusta para un caso.

    Returns
    -------
    summary : dict
        - tests_pasados: cuántos de los tres tests se ejecutaron y con qué
          resultado.
        - inferencia_robusta_replicacion: bool — True si TODOS los tests
          ejecutados pasaron sus criterios.
        - flags: lista de flags de atención (e.g. "leakage detectado").
    """
    flags = []
    pass_count = 0
    total = 0

    if seed_robustness_dict is not None:
        total += 1
        if seed_robustness_dict.get("robust", False):
            pass_count += 1
        else:
            flags.append("seed_robustness FAIL")

    if holdout_dict is not None:
        total += 1
        if holdout_dict.get("sin_leakage", False):
            pass_count += 1
        else:
            flags.append("holdout_temporal FAIL — posible leakage")

    if adversarial_dicts:
        for i, ad in enumerate(adversarial_dicts):
            total += 1
            if ad.get("cumple_expectativa", False):
                pass_count += 1
            else:
                flags.append(f"adversarial_swap[{i}] FAIL")

    return {
        "tests_ejecutados": total,
        "tests_pasados": pass_count,
        "inferencia_robusta_replicacion": bool(total > 0 and pass_count == total),
        "flags": flags,
        "version_protocolo": "V5.1",
    }


__all__ = [
    "seed_robustness",
    "holdout_temporal",
    "adversarial_probe_swap",
    "replication_robustness_summary",
]
