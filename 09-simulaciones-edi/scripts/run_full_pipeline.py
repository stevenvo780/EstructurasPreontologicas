#!/usr/bin/env python3
"""
Pipeline V5.3 end-to-end.

Orquesta los nueve bloques científicos sobre los 40 casos del corpus en
secuencia con verificación binaria por etapa. Es el script
"anti-paper-science": cada caso pasa por el filtro completo y emerge con
una calificación QES, una clasificación honesta, y trazabilidad
criptográfica.

Etapas (orden fijo):

    1. FETCH_MANIFEST por caso (Q1 trazabilidad)
    2. SETUP_HASH por caso (Q4 reproducibilidad)
    3. protocolo_simulacion.md (Q3 calidad sonda)
    4. Enrichment V5.2 universal (Q7 calibración + B1 + FWER)
    5. Sondas independientes B4 extendidas (Q5 multi-sonda)
    6. Análisis de potencia B7 (control Type-II)
    7. Sensibilidad a umbrales B5
    8. Auditoría QES (Q1-Q7 → categoría)
    9. Reporte consolidado V5.3
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _run(cmd: list[str], stage: str) -> tuple[bool, str]:
    print(f"\n=== {stage} ===")
    t0 = time.time()
    r = subprocess.run(
        cmd, cwd=ROOT, capture_output=True, text=True, timeout=300
    )
    dt = time.time() - t0
    ok = (r.returncode == 0)
    last_lines = "\n".join(r.stdout.splitlines()[-5:])
    if ok:
        print(f"  ✓ ({dt:.1f}s)\n{last_lines}")
    else:
        print(f"  ✗ ({dt:.1f}s)\n  stderr: {r.stderr[-500:]}")
    return ok, r.stdout


def main() -> int:
    print("=" * 80)
    print("Pipeline V5.3 end-to-end — corpus completo (40 casos)")
    print("=" * 80)

    stages = [
        (["python3", "scripts/generate_fetch_manifests.py"],
         "1/9 — FETCH_MANIFEST por caso (Q1 trazabilidad)"),
        (["python3", "scripts/freeze_setup.py", "--all"],
         "2a/9 — SETUP_HASH inter-dominio (Q4)"),
        (["python3", "scripts/freeze_multiescala.py"],
         "2b/9 — SETUP_HASH inter-escala (Q4)"),
        (["python3", "scripts/generate_protocols.py"],
         "3/9 — protocolo_simulacion.md (Q3)"),
        (["python3", "scripts/enrich_all_cases.py"],
         "4/9 — Enrichment V5.2 universal (Q7)"),
        (["python3", "scripts/run_independent_probes.py"],
         "5/9 — Sondas independientes B4 (Q5)"),
        (["python3", "scripts/run_power_analysis.py"],
         "6/9 — Análisis de potencia B7"),
        (["python3", "scripts/run_threshold_sensitivity.py"],
         "7/9 — Sensibilidad a umbrales B5"),
        (["python3", "scripts/audit_corpus_quality.py"],
         "8/9 — Auditoría QES (Q1-Q7)"),
    ]

    results = []
    for cmd, stage in stages:
        ok, _ = _run(cmd, stage)
        results.append((stage, ok))

    # Etapa 9: reporte consolidado
    print("\n=== 9/9 — Generando reporte consolidado V5.3 ===")
    report = _build_consolidated_report(results)
    out = ROOT / "PIPELINE_V5_3_REPORT.md"
    out.write_text(report, encoding="utf-8")
    print(f"  ✓ {out}")

    print("\n" + "=" * 80)
    print("Pipeline V5.3 completado")
    print(f"  Etapas exitosas: {sum(1 for _, ok in results if ok)}/{len(results)}")
    print("=" * 80)
    return 0 if all(ok for _, ok in results) else 1


def _build_consolidated_report(stages_results: list) -> str:
    qes_path = ROOT / "QES_AUDIT_REPORT.json"
    qes_data = {}
    if qes_path.is_file():
        try:
            qes_data = json.loads(qes_path.read_text())
        except Exception:
            pass

    lines = [
        "# Pipeline V5.3 — Reporte consolidado",
        "",
        f"Ejecutado: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}",
        "",
        "## Etapas ejecutadas",
        "",
        "| # | Etapa | Estado |",
        "|--:|-------|--------|",
    ]
    for i, (stage, ok) in enumerate(stages_results, start=1):
        emoji = "✅" if ok else "❌"
        lines.append(f"| {i} | {stage} | {emoji} |")

    if qes_data:
        cats = qes_data.get("categories", {})
        lines.extend([
            "",
            "## Calificación final del corpus (QES)",
            "",
            "| Categoría | Casos |",
            "|-----------|------:|",
            f"| ROBUSTO (QES ≥ 0.85) | {cats.get('ROBUSTO', 0)} |",
            f"| DEMOSTRATIVO (QES 0.70 - 0.85) | {cats.get('DEMOSTRATIVO', 0)} |",
            f"| PROGRAMÁTICO (QES 0.55 - 0.70) | {cats.get('PROGRAMÁTICO', 0)} |",
            f"| PILOTO (QES 0.40 - 0.55) | {cats.get('PILOTO', 0)} |",
            f"| INADMISIBLE (QES < 0.40) | {cats.get('INADMISIBLE', 0)} |",
            "",
            "## Top 10 casos por QES",
            "",
            "| Caso | QES | Categoría |",
            "|------|----:|-----------|",
        ])
        results = qes_data.get("results_sorted", [])
        for r in results[:10]:
            lines.append(f"| {r['case_id']} | {r['QES']:.3f} | {r['category']} |")

    lines.extend([
        "",
        "## Política anti-paper-science",
        "",
        "Ningún caso entra a afirmación demostrativa si su QES < 0.70. Casos en categoría PROGRAMÁTICO o inferior se declaran explícitamente como modo programático con criterios de elevación.",
        "",
        "## Reproducibilidad",
        "",
        "Pipeline reproducible bit-a-bit con:",
        "",
        "```bash",
        "cd 09-simulaciones-edi",
        "python3 scripts/run_full_pipeline.py",
        "```",
        "",
        "## Lectura cruzada",
        "",
        "- `09-simulaciones-edi/QES_AUDIT_REPORT.md` — auditoría detallada por caso",
        "- `09-simulaciones-edi/CIERRE_V5_2.md` — síntesis de los ocho bloques V5.2",
        "- `09-simulaciones-edi/HASHES_PRE_EJECUCION.json` — pre-registro inter-dominio",
        "- `09-simulaciones-edi/corpus_multiescala/HASHES_PRE_EJECUCION_INTER_ESCALA.json` — pre-registro inter-escala",
        "",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
