#!/usr/bin/env python3
"""
Auditoría de calidad sobre los 40 casos del corpus.

Para cada caso calcula el puntaje QES (Q1-Q7) y clasifica en cinco
categorías: ROBUSTO, DEMOSTRATIVO, PROGRAMÁTICO, PILOTO, INADMISIBLE.

Uso:
    python3 scripts/audit_corpus_quality.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.quality_scorer import quality_score, QES_WEIGHTS


def _iter_cases() -> list[tuple[str, Path]]:
    cases = []
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name[:2].isdigit() and "_caso_" in d.name:
            cases.append((d.name, d))
    multi_root = ROOT / "corpus_multiescala"
    if multi_root.is_dir():
        for d in sorted(multi_root.iterdir()):
            if d.is_dir() and d.name[:2].isdigit():
                cases.append((d.name, d))
    return cases


def main() -> int:
    print("=" * 90)
    print("Auditoría de calidad de evidencia (QES) sobre los 40 casos del corpus")
    print("=" * 90)
    print(f"\nPesos QES: {QES_WEIGHTS}\n")

    results = []
    for cid, case_dir in _iter_cases():
        metrics_path = case_dir / "outputs" / "metrics.json"
        if not metrics_path.is_file():
            continue
        try:
            metrics = json.loads(metrics_path.read_text())
        except Exception as e:
            print(f"  ⚠️  {cid}: error leyendo metrics: {e}")
            continue
        score = quality_score(metrics, case_dir)
        results.append(score)

    results.sort(key=lambda r: r["QES"], reverse=True)

    # Síntesis
    cat_counts = {}
    for r in results:
        cat_counts[r["category"]] = cat_counts.get(r["category"], 0) + 1

    print(f"{'Caso':<42}{'QES':>7}  Categoría        Q1   Q2   Q3   Q4   Q5   Q6   Q7")
    print("-" * 90)
    for r in results:
        comps = r["components"]
        q1 = comps["Q1_trazabilidad_datos"]["score"]
        q2 = comps["Q2_tamano_efectivo"]["score"]
        q3 = comps["Q3_calidad_sonda"]["score"]
        q4 = comps["Q4_reproducibilidad"]["score"]
        q5 = comps["Q5_convergencia_multisonda"]["score"]
        q6 = comps["Q6_loe_empirico"]["score"]
        q7 = comps["Q7_calibracion_estadistica"]["score"]
        print(
            f"{r['case_id']:<42}{r['QES']:>6.3f}  {r['category']:<14} "
            f"{q1:.2f} {q2:.2f} {q3:.2f} {q4:.2f} {q5:.2f} {q6:.2f} {q7:.2f}"
        )

    print("\n" + "=" * 90)
    print("Síntesis:")
    print("=" * 90)
    for cat in ["ROBUSTO", "DEMOSTRATIVO", "PROGRAMÁTICO", "PILOTO", "INADMISIBLE"]:
        n = cat_counts.get(cat, 0)
        bar = "█" * (n * 2)
        print(f"  {cat:<14} {n:>3} {bar}")

    full = {
        "version_protocolo": "V5.3",
        "weights": QES_WEIGHTS,
        "n_total": len(results),
        "categories": cat_counts,
        "results_sorted": results,
    }
    out_json = ROOT / "QES_AUDIT_REPORT.json"
    out_json.write_text(json.dumps(full, indent=2, ensure_ascii=False))
    print(f"\n✓ JSON: {out_json}")

    # Markdown
    md_lines = [
        "# Auditoría de calidad de evidencia — corpus completo (40 casos)",
        "",
        "Bloque V5.3. Asigna a cada caso un puntaje integral QES ∈ [0,1] que combina trazabilidad de datos, tamaño efectivo, calidad de sonda, reproducibilidad, multi-sonda, LoE y calibración estadística.",
        "",
        "## Pesos QES",
        "",
        "| Componente | Peso |",
        "|------------|-----:|",
    ]
    for k, w in QES_WEIGHTS.items():
        md_lines.append(f"| {k} | {w:.2f} |")
    md_lines.extend([
        "",
        "## Categorías",
        "",
        "| Categoría | Umbral QES | Significado |",
        "|-----------|-----------:|-------------|",
        "| ROBUSTO | ≥ 0.85 | Apto para afirmación demostrativa post-V5.2 |",
        "| DEMOSTRATIVO | 0.70 - 0.85 | Apto para afirmación demostrativa honesta |",
        "| PROGRAMÁTICO | 0.55 - 0.70 | Sólo en modo programático con criterios de elevación |",
        "| PILOTO | 0.40 - 0.55 | Piloto con limitaciones explícitas; no afirmar como demostración |",
        "| INADMISIBLE | < 0.40 | PAPER-SCIENCE: retirar o re-implementar |",
        "",
        "## Síntesis",
        "",
        "| Categoría | Casos |",
        "|-----------|------:|",
    ])
    for cat in ["ROBUSTO", "DEMOSTRATIVO", "PROGRAMÁTICO", "PILOTO", "INADMISIBLE"]:
        md_lines.append(f"| {cat} | {cat_counts.get(cat, 0)} |")
    md_lines.extend([
        "",
        "## Tabla por caso (ordenada de mayor a menor QES)",
        "",
        "| Caso | QES | Categoría | Q1 trz | Q2 n | Q3 sonda | Q4 repr | Q5 multi | Q6 LoE | Q7 calib |",
        "|------|----:|-----------|-------:|------:|----------:|--------:|----------:|--------:|----------:|",
    ])
    for r in results:
        c = r["components"]
        md_lines.append(
            f"| {r['case_id']} | **{r['QES']:.3f}** | {r['category']} | "
            f"{c['Q1_trazabilidad_datos']['score']:.2f} | "
            f"{c['Q2_tamano_efectivo']['score']:.2f} | "
            f"{c['Q3_calidad_sonda']['score']:.2f} | "
            f"{c['Q4_reproducibilidad']['score']:.2f} | "
            f"{c['Q5_convergencia_multisonda']['score']:.2f} | "
            f"{c['Q6_loe_empirico']['score']:.2f} | "
            f"{c['Q7_calibracion_estadistica']['score']:.2f} |"
        )
    md_lines.extend([
        "",
        "## Lectura",
        "",
        "Esta auditoría es el filtro **anti-paper-science** del aparato V5.3: ningún caso pasa a afirmación demostrativa si su QES < 0.70. Casos en categoría INADMISIBLE deben retirarse, declararse como hipótesis especulativa, o re-implementarse con datos reales y sonda físicamente motivada.",
        "",
        "## Lectura cruzada",
        "",
        "- `09-simulaciones-edi/common/quality_scorer.py` — implementación del scorer.",
        "- `Anexos/A0-limitaciones-declaradas.md` — limitaciones consolidadas.",
        "- `09-simulaciones-edi/CIERRE_V5_2.md` — síntesis de los ocho bloques V5.2.",
    ])
    out_md = ROOT / "QES_AUDIT_REPORT.md"
    out_md.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"✓ Markdown: {out_md}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
