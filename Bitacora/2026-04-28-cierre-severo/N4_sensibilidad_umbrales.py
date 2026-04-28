"""N4 — Análisis de sensibilidad de la composición del corpus a umbrales.

Evalúa cómo cambia la clasificación strong/weak/suggestive/trend del corpus
bajo umbrales alternativos de EDI, no solo los publicados (0.10, 0.30).

Si la composición del corpus se desbarata radicalmente bajo umbrales razonables
distintos, los umbrales actuales son arbitrarios y deben justificarse pre-empíricamente.
"""

from __future__ import annotations
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


CORPUS_EDIS = {
    "04_energia": 0.6503,
    "16_deforestacion": 0.6020,
    "20_kessler": 0.3527,
    "27_riesgo_bio": 0.3326,
    "24_microplasticos": 0.7819,
    "13_politicas": 0.2972,
    "30_behavioral": 0.2622,
    "14_postverdad": 0.2428,
    "18_urbanizacion": 0.2358,
    "22_fosforo": 0.1924,
    "15_wikipedia": 0.1916,
    "05_epidemiologia": 0.1294,
    "11_movilidad": 0.1283,
    "09_finanzas": 0.0813,
    "21_salinizacion": 0.0184,
    "10_justicia": 0.2274,
    "26_starlink": 0.6892,
    "28_fuga_cerebros": 0.0249,
    "01_clima": 0.0111,
    "02_conciencia": -0.1165,
    "03_contaminacion": -0.0038,
    "12_paradigmas": -0.0060,
    "17_oceanos": -0.0154,
    "19_acidificacion": -0.0002,
    "23_erosion": -1.0000,
    "25_acuiferos": -0.1462,
    "29_iot": -0.8760,
}

P_VALUES = {
    "04_energia": 0.0, "16_deforestacion": 0.0, "20_kessler": 0.0, "27_riesgo_bio": 0.0022,
    "24_microplasticos": 0.0, "13_politicas": 0.0015, "30_behavioral": 0.044,
    "14_postverdad": 0.0, "18_urbanizacion": 0.0, "22_fosforo": 0.0, "15_wikipedia": 0.0,
    "05_epidemiologia": 0.0, "11_movilidad": 0.0020, "09_finanzas": 0.0, "21_salinizacion": 0.0028,
    "10_justicia": 0.4775, "26_starlink": 1.0, "28_fuga_cerebros": 0.9975, "01_clima": 0.9990,
}


def classify(edi: float, p: float, weak_threshold: float, strong_threshold: float) -> str:
    if edi <= 0:
        return "null"
    if p >= 0.05:
        return "trend"
    if edi >= strong_threshold:
        return "strong"
    if edi >= weak_threshold:
        return "weak"
    if edi >= 0.01:
        return "suggestive"
    return "trend"


def main():
    print("=== N4 — Sensibilidad a umbrales ===")
    print()
    schemes = {
        "publicado_0.10_0.30": (0.10, 0.30),
        "estricto_0.15_0.40":  (0.15, 0.40),
        "permisivo_0.05_0.20": (0.05, 0.20),
        "muy_estricto_0.20_0.50": (0.20, 0.50),
    }
    print(f"  {'Esquema':30s} {'Strong':>8s} {'Weak':>6s} {'Sugges':>7s} {'Trend':>6s} {'Null':>5s}")
    summary = {}
    for name, (wt, st) in schemes.items():
        counts = {"strong": 0, "weak": 0, "suggestive": 0, "trend": 0, "null": 0}
        for case, edi in CORPUS_EDIS.items():
            p = P_VALUES.get(case, 0.5)
            cls = classify(edi, p, wt, st)
            counts[cls] += 1
        summary[name] = counts
        print(f"  {name:30s} {counts['strong']:>8d} {counts['weak']:>6d} "
              f"{counts['suggestive']:>7d} {counts['trend']:>6d} {counts['null']:>5d}")
    print()

    publ = summary["publicado_0.10_0.30"]
    estricto = summary["estricto_0.15_0.40"]
    permisivo = summary["permisivo_0.05_0.20"]

    delta_strong_estricto = abs(publ["strong"] - estricto["strong"])
    delta_strong_permisivo = abs(publ["strong"] - permisivo["strong"])

    if delta_strong_estricto <= 1 and delta_strong_permisivo <= 2:
        verdict = "Composición ROBUSTA a umbrales razonables. Δstrong ≤ 2 en todos los esquemas."
    elif delta_strong_estricto <= 2 and delta_strong_permisivo <= 3:
        verdict = "Composición moderadamente sensible: pequeños cambios reorganizan algunos casos."
    else:
        verdict = "Composición FRÁGIL a umbrales. Cambios pequeños desbaratan la clasificación."

    print(f"  VEREDICTO: {verdict}")

    out = Path(__file__).parent / "N4_resultados.json"
    out.write_text(json.dumps({"summary": summary, "verdict": verdict},
                              indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Resultados: {out}")


if __name__ == "__main__":
    main()
