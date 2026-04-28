"""
Análisis de potencia estadística — bloque científico B7 (V5.2).

Pregunta complementaria a la calibración: dado un caso clasificado como null,
¿qué tamaño de efecto sería detectable con la potencia estadística actual? Si
la potencia para detectar EDI = 0.10 (umbral weak) es < 0.80, el null
podría ser FALSO NEGATIVO debido a tamaño insuficiente, no ausencia real
de cierre operativo.

Esta es la honestidad científica complementaria: no basta con calibrar el
control de tipo I; hay que reportar el control de tipo II (potencia).

Provee:

1. minimum_detectable_effect: dado n y nivel α, MDE para potencia 0.80.
2. post_hoc_power: dado un EDI observado, n y α, qué potencia se tuvo.
3. classify_null: si un caso null tiene potencia insuficiente para
   detectar weak, marcarlo como "null por potencia insuficiente" en lugar
   de "null por ausencia de señal".

Cohen (1988) "Statistical Power Analysis for the Behavioral Sciences"
ya está en la bibliografía nuclear (referencia #34) — este módulo es la
implementación operativa de su criterio.
"""
from __future__ import annotations

import math
import numpy as np
from typing import Sequence


def minimum_detectable_effect(
    n: int,
    alpha: float = 0.05,
    target_power: float = 0.80,
    se_estimate: float = 0.10,
) -> float:
    """
    Mínimo tamaño de efecto detectable (MDE) bajo potencia objetivo.

    Para test unilateral de EDI > 0:
        MDE = (z_alpha + z_beta) * SE

    donde z_alpha = ppf(1-alpha) y z_beta = ppf(target_power).

    Por defecto:
        z_0.05 = 1.645
        z_0.80 = 0.842
        => MDE ≈ 2.487 * SE

    Si SE escala como 1/sqrt(n), valores típicos:
        n=20:  MDE ≈ 0.55  (sólo detecta strong)
        n=60:  MDE ≈ 0.32
        n=100: MDE ≈ 0.25
        n=200: MDE ≈ 0.18 (detecta weak)
    """
    z_alpha = 1.645 if abs(alpha - 0.05) < 1e-6 else _normal_ppf(1 - alpha)
    z_beta = 0.842 if abs(target_power - 0.80) < 1e-6 else _normal_ppf(target_power)
    se_n = se_estimate / math.sqrt(max(n / 20.0, 1.0))
    return float((z_alpha + z_beta) * se_n)


def post_hoc_power(
    observed_edi: float,
    n: int,
    alpha: float = 0.05,
    se_estimate: float = 0.10,
) -> float:
    """
    Potencia post-hoc dado el EDI observado y n.

    Power = P(reject H0 | H1 true) = Phi((|edi| / SE) - z_alpha)
    """
    se_n = se_estimate / math.sqrt(max(n / 20.0, 1.0))
    z_alpha = 1.645 if abs(alpha - 0.05) < 1e-6 else _normal_ppf(1 - alpha)
    z_eff = abs(observed_edi) / max(se_n, 1e-6) - z_alpha
    return float(_normal_cdf(z_eff))


def power_to_detect(
    target_effect: float,
    n: int,
    alpha: float = 0.05,
    se_estimate: float = 0.10,
) -> float:
    """
    Potencia para detectar un efecto target dado n.
    """
    return post_hoc_power(target_effect, n, alpha, se_estimate)


def classify_null_with_power(
    edi: float,
    n: int,
    target_weak_threshold: float = 0.10,
    alpha: float = 0.05,
    target_power: float = 0.80,
) -> dict:
    """
    Clasifica un null reportando si lo es por ausencia o por potencia.

    Returns
    -------
    dict con:
        - clasificacion: "null_real" | "null_por_potencia_insuficiente" | "no_null"
        - potencia_para_detectar_weak: probabilidad de detectar EDI=weak_threshold
        - mde_actual: mínimo efecto detectable con n actual
        - n_necesario_para_detectar_weak: n requerido para potencia 0.80
    """
    power = power_to_detect(target_weak_threshold, n, alpha)
    mde = minimum_detectable_effect(n, alpha, target_power)
    n_needed = _n_required(target_weak_threshold, alpha, target_power)

    if edi > target_weak_threshold:
        clasificacion = "no_null"
    elif power >= target_power:
        clasificacion = "null_real"
    else:
        clasificacion = "null_por_potencia_insuficiente"

    return {
        "edi_observado": edi,
        "n": n,
        "potencia_para_detectar_weak": float(power),
        "mde_actual": float(mde),
        "n_necesario_para_detectar_weak": int(n_needed),
        "criterio": (
            f"Potencia ≥ {target_power} para detectar EDI = "
            f"{target_weak_threshold} con α = {alpha}"
        ),
        "clasificacion": clasificacion,
        "interpretacion": _interpret_classification(clasificacion, power, n_needed, n),
    }


def _interpret_classification(cls: str, power: float, n_needed: int, n: int) -> str:
    if cls == "null_real":
        return (
            f"Null real: la potencia ({power:.2%}) era suficiente para detectar "
            f"EDI = 0.10 si lo hubiera; la ausencia de señal es genuina."
        )
    if cls == "null_por_potencia_insuficiente":
        return (
            f"Null por potencia insuficiente: con n actual la potencia "
            f"({power:.2%}) es insuficiente. Para detectar EDI = 0.10 con "
            f"potencia 0.80 se necesitaría n ≥ {n_needed} (vs n actual = {n}). "
            f"NO se puede afirmar que no haya cierre operativo; sólo que el "
            f"corpus actual no tiene resolución para detectarlo."
        )
    return f"No es null (EDI > 0.10)."


def _n_required(target_effect: float, alpha: float = 0.05, target_power: float = 0.80, base_se: float = 0.10) -> int:
    """n requerido para detectar target_effect con potencia objetivo."""
    z_alpha = 1.645 if abs(alpha - 0.05) < 1e-6 else _normal_ppf(1 - alpha)
    z_beta = 0.842 if abs(target_power - 0.80) < 1e-6 else _normal_ppf(target_power)
    # MDE = (z_alpha + z_beta) * SE / sqrt(n/20)
    # n/20 = ((z_alpha + z_beta) * SE / MDE) ** 2
    if target_effect <= 0:
        return 99999
    n_factor = ((z_alpha + z_beta) * base_se / target_effect) ** 2
    return max(20, int(math.ceil(n_factor * 20)))


def _normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _normal_ppf(p: float) -> float:
    """Aproximación a la CDF normal inversa (Beasley-Springer-Moro)."""
    if p < 0.5:
        return -_normal_ppf(1 - p)
    if p >= 0.999:
        return 3.09
    if abs(p - 0.95) < 1e-9:
        return 1.645
    if abs(p - 0.975) < 1e-9:
        return 1.960
    if abs(p - 0.99) < 1e-9:
        return 2.326
    if abs(p - 0.80) < 1e-9:
        return 0.842
    # Aproximación de Beasley-Springer
    a = [-3.969683028665376e+01, 2.209460984245205e+02,
         -2.759285104469687e+02, 1.383577518672690e+02,
         -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02,
         -1.556989798598866e+02, 6.680131188771972e+01,
         -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01,
         -2.400758277161838e+00, -2.549732539343734e+00,
         4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01,
         2.445134137142996e+00, 3.754408661907416e+00]

    pl = 0.02425
    if p < pl:
        q = math.sqrt(-2.0 * math.log(p))
        return (((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) \
            / ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1.0)
    if p <= 1 - pl:
        q = p - 0.5
        r = q * q
        return (((((a[0]*r + a[1])*r + a[2])*r + a[3])*r + a[4])*r + a[5]) * q \
            / (((((b[0]*r + b[1])*r + b[2])*r + b[3])*r + b[4])*r + 1.0)
    q = math.sqrt(-2.0 * math.log(1.0 - p))
    return -(((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) \
        / ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1.0)


__all__ = [
    "minimum_detectable_effect",
    "post_hoc_power",
    "power_to_detect",
    "classify_null_with_power",
]
