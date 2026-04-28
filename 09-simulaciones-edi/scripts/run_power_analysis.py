#!/usr/bin/env python3
"""
Análisis de potencia estadística sobre el corpus completo (40 casos).

Para cada caso null o marginal, reporta:
- potencia post-hoc para detectar EDI weak (0.10) con n actual
- MDE actual
- n requerido para potencia 0.80
- clasificación: null_real / null_por_potencia_insuficiente / no_null

Esto cierra el flanco de potencia que la calibración por sí sola no
cubre: distingue casos null genuinamente vacíos de casos null por
tamaño insuficiente.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.power_analysis import classify_null_with_power


def _load_inter_dominio() -> dict[str, tuple[float, int]]:
    """Lee EDI y n de los 30 casos del corpus inter-dominio."""
    cases = {}
    for case_dir in sorted(ROOT.iterdir()):
        if not case_dir.is_dir() or not case_dir.name[:2].isdigit() or "_caso_" not in case_dir.name:
            continue
        if case_dir.name.startswith(("31_", "32_", "33_", "34_", "35_", "36_", "37_", "38_", "39_", "40_")):
            continue
        metrics_path = case_dir / "outputs" / "metrics.json"
        if not metrics_path.is_file():
            continue
        try:
            data = json.loads(metrics_path.read_text())
        except Exception:
            continue
        phases = data.get("phases", {})
        phase = phases.get("real") or phases.get("synthetic") or {}
        edi_dict = phase.get("edi", {}) if isinstance(phase, dict) else {}
        edi = float(edi_dict.get("value", 0.0)) if isinstance(edi_dict, dict) else 0.0
        n = int(phase.get("data", {}).get("val_steps", 20)) if isinstance(phase, dict) else 20
        cases[case_dir.name] = (edi, n)
    return cases


def _load_inter_escala() -> dict[str, tuple[float, int]]:
    cases = {}
    multi_root = ROOT / "corpus_multiescala"
    if not multi_root.is_dir():
        return cases
    for cd in sorted(multi_root.iterdir()):
        if not cd.is_dir() or not cd.name[:2].isdigit():
            continue
        m_path = cd / "outputs" / "metrics.json"
        if not m_path.is_file():
            continue
        try:
            m = json.loads(m_path.read_text())
        except Exception:
            continue
        edi = float(m.get("edi", 0.0))
        n = int(m.get("val_steps", 60))
        cases[cd.name] = (edi, n)
    return cases


def main() -> int:
    print("=" * 78)
    print("Análisis de potencia estadística — bloque B7")
    print("=" * 78)

    inter_dominio = _load_inter_dominio()
    inter_escala = _load_inter_escala()

    all_cases = {**inter_dominio, **inter_escala}
    print(f"\nCasos cargados: {len(all_cases)} ({len(inter_dominio)} inter-dominio + {len(inter_escala)} inter-escala)")

    results = {}
    for cid in sorted(all_cases.keys()):
        edi, n = all_cases[cid]
        analysis = classify_null_with_power(edi, n)
        results[cid] = analysis

    # Síntesis
    null_real = [c for c, r in results.items() if r["clasificacion"] == "null_real"]
    null_potencia = [c for c, r in results.items() if r["clasificacion"] == "null_por_potencia_insuficiente"]
    no_null = [c for c, r in results.items() if r["clasificacion"] == "no_null"]

    print("\n" + "=" * 78)
    print(f"Síntesis:")
    print(f"  No null (EDI > 0.10):                       {len(no_null)}")
    print(f"  Null real (potencia ≥ 0.80):                {len(null_real)}")
    print(f"  Null por potencia insuficiente:             {len(null_potencia)}")
    print("=" * 78)

    if null_potencia:
        print("\nCasos null por potencia insuficiente (NO afirmar ausencia de cierre):")
        for c in null_potencia:
            r = results[c]
            print(f"  {c}: EDI={r['edi_observado']:+.4f}, n={r['n']}, "
                  f"potencia={r['potencia_para_detectar_weak']:.2%}, "
                  f"n_necesario={r['n_necesario_para_detectar_weak']}")

    full = {
        "version_protocolo": "V5.2 / B7",
        "n_total": len(all_cases),
        "categorias": {
            "no_null": no_null,
            "null_real": null_real,
            "null_por_potencia_insuficiente": null_potencia,
        },
        "results_por_caso": results,
    }

    out_json = ROOT / "POWER_ANALYSIS_REPORT.json"
    out_json.write_text(json.dumps(full, indent=2, ensure_ascii=False))
    print(f"\n✓ JSON: {out_json}")

    md_lines = [
        "# Análisis de potencia estadística — corpus completo (40 casos)",
        "",
        "Bloque científico B7 (V5.2). Distingue casos null genuinos de casos null por tamaño muestral insuficiente.",
        "",
        "## Síntesis",
        "",
        f"- **No null** (EDI > 0.10): {len(no_null)}",
        f"- **Null real** (potencia ≥ 0.80 para detectar weak): {len(null_real)}",
        f"- **Null por potencia insuficiente**: {len(null_potencia)}",
        "",
        "## Casos null por potencia insuficiente",
        "",
        "Estos casos NO se pueden afirmar como ausencia de cierre operativo; sólo que el corpus actual carece de resolución estadística para detectarlo.",
        "",
        "| Caso | EDI | n | Potencia para detectar weak | MDE actual | n necesario |",
        "|------|----:|--:|-----------------------------:|------------:|-------------:|",
    ]
    for c in null_potencia:
        r = results[c]
        md_lines.append(
            f"| {c} | {r['edi_observado']:+.4f} | {r['n']} | "
            f"{r['potencia_para_detectar_weak']:.2%} | {r['mde_actual']:.4f} | "
            f"{r['n_necesario_para_detectar_weak']} |"
        )
    md_lines.extend([
        "",
        "## Tabla completa",
        "",
        "| Caso | EDI | n | Potencia | MDE | Clasificación |",
        "|------|----:|--:|---------:|-----:|----------------|",
    ])
    for c in sorted(results.keys()):
        r = results[c]
        md_lines.append(
            f"| {c} | {r['edi_observado']:+.4f} | {r['n']} | "
            f"{r['potencia_para_detectar_weak']:.2%} | {r['mde_actual']:.4f} | "
            f"{r['clasificacion']} |"
        )

    md_lines.extend([
        "",
        "## Lectura honesta",
        "",
        "Esta es la honestidad complementaria a la calibración del Type-I error (B1). Mientras B1 controla falsos positivos por autocorrelación + comparaciones múltiples, B7 controla falsos negativos por tamaño insuficiente.",
        "",
        "Los casos clasificados como `null_por_potencia_insuficiente` son particularmente importantes: el manuscrito NO afirma que no tengan cierre operativo; afirma que el aparato actual carece de resolución para detectarlo. La elevación a `n` mayor (mediante series temporales más largas o muestras adicionales) es deuda metodológica priorizada.",
    ])
    out_md = ROOT / "POWER_ANALYSIS_REPORT.md"
    out_md.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"✓ Markdown: {out_md}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
