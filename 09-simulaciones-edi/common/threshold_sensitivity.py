"""
Análisis de sensibilidad a umbrales — bloque científico B5 (V5.1).

Cierra parcialmente la deuda L3: la composición del corpus depende de los
umbrales (0.10/0.30 → 5 strong; 0.15/0.40 → 3; 0.05/0.20 → 9). El cap
06-01 §5.4 ya lo declara honestamente; este módulo lo MECANIZA: cualquier
evaluador puede correr el análisis sobre los EDI publicados y obtener la
distribución completa de clasificaciones bajo perturbación de umbrales.

Provee:

1. classify_corpus(edi_values, thresholds): clasifica un corpus dado un
   par de umbrales (weak_low, strong_low).
2. sweep_threshold_grid: barre una grilla de umbrales y devuelve la matriz
   de conteos por nivel.
3. robust_strong_set: devuelve el conjunto de casos que permanecen
   strong bajo TODA la grilla razonable. Esos son los casos cuya
   clasificación es independiente de la elección de umbrales.

La intuición filosófica: los casos verdaderamente robustos no son los que
sobreviven a UN par de umbrales; son los que sobreviven a CUALQUIER par
de umbrales razonables. Esa es la versión mecanizada de "los hallazgos no
dependen del ojo del investigador".
"""
from __future__ import annotations

import numpy as np
from typing import Iterable, Sequence


def classify_corpus(
    edi_values: dict[str, float],
    weak_low: float = 0.10,
    strong_low: float = 0.30,
    p_values: dict[str, float] | None = None,
    p_threshold: float = 0.05,
) -> dict[str, str]:
    """
    Clasifica un corpus en niveles {null, trend, suggestive, weak, strong}.

    Reglas (consistentes con cap 03-04 §"Niveles del paisaje"):
        - strong:     EDI ≥ strong_low  y p < p_threshold
        - weak:       weak_low ≤ EDI < strong_low  y p < p_threshold
        - suggestive: 0.01 ≤ EDI < weak_low  y p < p_threshold
        - trend:      EDI > 0  y  p ≥ p_threshold
        - null:       EDI ≤ 0
    """
    classification = {}
    for case_id, edi in edi_values.items():
        p = p_values.get(case_id, 0.0) if p_values else 0.0
        if edi <= 0:
            classification[case_id] = "null"
        elif p >= p_threshold:
            classification[case_id] = "trend"
        elif edi < 0.01:
            classification[case_id] = "trend"
        elif edi < weak_low:
            classification[case_id] = "suggestive"
        elif edi < strong_low:
            classification[case_id] = "weak"
        else:
            classification[case_id] = "strong"
    return classification


def sweep_threshold_grid(
    edi_values: dict[str, float],
    weak_lows: Iterable[float] = (0.05, 0.075, 0.10, 0.125, 0.15),
    strong_lows: Iterable[float] = (0.20, 0.25, 0.30, 0.35, 0.40),
    p_values: dict[str, float] | None = None,
) -> dict:
    """
    Barre una grilla de umbrales y retorna la matriz de clasificaciones.

    Returns
    -------
    summary : dict
        - grid: lista de (weak_low, strong_low, classification_dict)
        - counts: dict {(wl, sl): {level: count}}
        - per_case_invariance: dict {case_id: set de niveles bajo la grilla}
        - robust_strong: lista de casos siempre strong bajo toda la grilla
        - robust_null: lista siempre null
    """
    grid_results = []
    counts = {}
    per_case = {cid: set() for cid in edi_values}

    for wl in weak_lows:
        for sl in strong_lows:
            if sl <= wl:
                continue
            cls = classify_corpus(edi_values, wl, sl, p_values)
            grid_results.append((wl, sl, cls))
            cnt = {}
            for c, level in cls.items():
                cnt[level] = cnt.get(level, 0) + 1
                per_case[c].add(level)
            counts[(wl, sl)] = cnt

    robust_strong = sorted(c for c, levels in per_case.items() if levels == {"strong"})
    robust_null = sorted(c for c, levels in per_case.items() if levels == {"null"})

    return {
        "grid_size": len(grid_results),
        "weak_lows": list(weak_lows),
        "strong_lows": list(strong_lows),
        "counts_by_grid": {f"{wl}/{sl}": cnt for (wl, sl), cnt in counts.items()},
        "per_case_invariance": {c: sorted(levels) for c, levels in per_case.items()},
        "robust_strong": robust_strong,
        "robust_null": robust_null,
        "n_cases": len(edi_values),
    }


def robust_classification_summary(sweep_result: dict) -> str:
    """
    Devuelve un resumen textual del barrido para incluir en cap 06-01 §5.4.
    """
    n = sweep_result["n_cases"]
    rs = sweep_result["robust_strong"]
    rn = sweep_result["robust_null"]
    invariant = len(rs) + len(rn)
    lines = [
        f"Análisis de sensibilidad a umbrales (V5.1):",
        f"  - corpus de {n} casos evaluados sobre grilla de "
        f"{len(sweep_result['weak_lows'])} × {len(sweep_result['strong_lows'])} "
        f"pares de umbrales (weak_low × strong_low)",
        f"  - casos SIEMPRE strong (invariantes a cualquier umbral razonable): "
        f"{len(rs)} → {rs}",
        f"  - casos SIEMPRE null (invariantes a cualquier umbral razonable): "
        f"{len(rn)}",
        f"  - clasificación invariante: {invariant}/{n} = "
        f"{invariant / n * 100:.0f}% del corpus",
    ]
    return "\n".join(lines)


__all__ = [
    "classify_corpus",
    "sweep_threshold_grid",
    "robust_classification_summary",
]
