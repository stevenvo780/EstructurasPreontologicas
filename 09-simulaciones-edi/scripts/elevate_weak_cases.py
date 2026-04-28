#!/usr/bin/env python3
"""
Elevación masiva V5.2 de casos débiles del corpus.

Aplica las cinco capas de refuerzo V5.1 a los 14 casos del corpus que NO
son invariantemente strong ni invariantemente null. Genera por caso un
metrics_enriched_v5_2.json paralelo y un reporte consolidado.

Uso:
    python3 scripts/elevate_weak_cases.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.case_elevation import elevate_case, CASES_TO_ELEVATE


def _collect_corpus_p_values(sims_root: Path) -> dict[str, float]:
    """Lee p-values de todos los casos para FWER."""
    all_p = {}
    for case_dir in sorted(sims_root.iterdir()):
        if not case_dir.is_dir() or not case_dir.name[:2].isdigit():
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
        edi_dict = phase.get("edi", {})
        if isinstance(edi_dict, dict):
            p = edi_dict.get("permutation_pvalue", 0.5)
        else:
            p = 0.5
        all_p[case_dir.name] = float(p)
    return all_p


def main() -> int:
    sims_root = ROOT
    print("=" * 78)
    print("Elevación masiva V5.2 — casos débiles del corpus")
    print("=" * 78)

    all_p = _collect_corpus_p_values(sims_root)
    print(f"\nP-values del corpus completo recolectados: {len(all_p)} casos")

    elevated = []
    summary_table = []

    for case_id in sorted(CASES_TO_ELEVATE.keys()):
        print(f"\n[{case_id}]")
        result = elevate_case(case_id, sims_root, all_p=all_p)
        if "error" in result:
            print(f"  ⚠️  error: {result['error']}")
            continue

        b1 = result["B1_calibration"]
        b5 = result["B5_threshold_invariance"]
        veredicto = result["elevacion_neta"]["veredicto"]

        print(f"  EDI canónico:                {b1['edi_canonical']:+.4f}")
        print(f"  p_naive (canónico):          {b1['p_value_naive_canonical']:.4f}")
        print(f"  p_block (V5.2 estimado):     {b1['p_value_block_bootstrap_estimated']:.4f}")
        print(f"  SE Newey-West estimado:      {b1['newey_west_se_estimated']:.4f}")
        if b1["fwer_position_in_corpus"]:
            print(f"  Holm-adjusted p:             {b1['fwer_position_in_corpus']['p_adjusted_holm']:.4f}")
            print(f"  Sobrevive FWER α=0.05:       {b1['fwer_position_in_corpus']['survives_fwer_at_alpha_0_05']}")
        print(f"  Invariante a umbrales:       {b5['invariant']} → {b5['invariant_level']}")
        print(f"  Veredicto: {veredicto}")

        # Escribir enriquecimiento paralelo
        out_path = sims_root / case_id / "outputs" / "metrics_enriched_v5_2.json"
        out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
        elevated.append(case_id)

        summary_table.append({
            "case_id": case_id,
            "edi": b1["edi_canonical"],
            "p_naive": b1["p_value_naive_canonical"],
            "p_block": b1["p_value_block_bootstrap_estimated"],
            "se_hac": b1["newey_west_se_estimated"],
            "p_holm": b1["fwer_position_in_corpus"]["p_adjusted_holm"] if b1["fwer_position_in_corpus"] else None,
            "fwer_survives": b1["fwer_position_in_corpus"]["survives_fwer_at_alpha_0_05"] if b1["fwer_position_in_corpus"] else None,
            "invariant": b5["invariant"],
            "invariant_level": b5["invariant_level"],
            "veredicto": veredicto,
        })

    # Reporte consolidado
    print("\n" + "=" * 78)
    print("Síntesis V5.2")
    print("=" * 78)
    elevados_robusto = [s for s in summary_table if "ROBUSTO" in s["veredicto"]]
    confirmados_marginal = [s for s in summary_table if "MARGINAL" in s["veredicto"]]
    sensibles = [s for s in summary_table if "SENSIBLE" in s["veredicto"]]
    confirmados_null = [s for s in summary_table if "NULL" in s["veredicto"]]
    parciales = [s for s in summary_table if "PARCIALMENTE" in s["veredicto"]]

    print(f"  Total elevados:               {len(elevated)}")
    print(f"  ELEVADOS A ROBUSTO:           {len(elevados_robusto)}")
    print(f"  ELEVADOS PARCIALMENTE:        {len(parciales)}")
    print(f"  CONFIRMADOS MARGINAL:         {len(confirmados_marginal)}")
    print(f"  SENSIBLES A UMBRALES:         {len(sensibles)}")
    print(f"  CONFIRMADOS NULL post-calib:  {len(confirmados_null)}")

    full_report = {
        "version_protocolo": "V5.2",
        "fecha": "2026-04-28",
        "deuda_objetivo": "elevación de casos débiles del corpus inter-dominio",
        "n_elevados": len(elevated),
        "summary_table": summary_table,
        "elevados_a_robusto": [s["case_id"] for s in elevados_robusto],
        "elevados_parcialmente": [s["case_id"] for s in parciales],
        "confirmados_marginal": [s["case_id"] for s in confirmados_marginal],
        "sensibles_a_umbrales": [s["case_id"] for s in sensibles],
        "confirmados_null_post_calibracion": [s["case_id"] for s in confirmados_null],
    }
    out_json = sims_root / "ELEVACION_V5_2_REPORT.json"
    out_json.write_text(json.dumps(full_report, indent=2, ensure_ascii=False))
    print(f"\n✓ JSON consolidado: {out_json}")

    # Markdown consolidado
    md_lines = [
        "# Elevación masiva V5.2 — casos débiles del corpus",
        "",
        "Aplicación de las cinco capas V5.1 (calibración avanzada, replicación robusta, pre-registro criptográfico, sensibilidad a umbrales, sondas independientes) a los 14 casos del corpus inter-dominio que NO son invariantemente strong ni invariantemente null.",
        "",
        "## Síntesis",
        "",
        f"- **Total casos elevados:** {len(elevated)}",
        f"- **Elevados a ROBUSTO** (invariante + p_block sig + sobrevive FWER): {len(elevados_robusto)}",
        f"- **Elevados PARCIALMENTE** (invariante + p_block sig pero no sobrevive FWER): {len(parciales)}",
        f"- **CONFIRMADOS MARGINAL** post-calibración: {len(confirmados_marginal)}",
        f"- **SENSIBLES a umbrales** (declarados como casos de borde): {len(sensibles)}",
        f"- **CONFIRMADOS NULL** post-calibración: {len(confirmados_null)}",
        "",
        "## Tabla por caso",
        "",
        "| Caso | EDI | p_naive | p_block | SE HAC | p_Holm | Inv? | Lvl Inv | Veredicto |",
        "|------|----:|---------:|---------:|--------:|--------:|:----:|---------|-----------|",
    ]
    for s in summary_table:
        inv = "✓" if s["invariant"] else "✗"
        lvl = s["invariant_level"] or "—"
        verd = s["veredicto"].split(":")[0]
        p_holm_str = f"{s['p_holm']:.4f}" if s["p_holm"] is not None else "—"
        md_lines.append(
            f"| {s['case_id']} | {s['edi']:+.3f} | {s['p_naive']:.4f} | "
            f"{s['p_block']:.4f} | {s['se_hac']:.4f} | "
            f"{p_holm_str} | "
            f"{inv} | {lvl} | **{verd}** |"
        )

    md_lines.extend([
        "",
        "## Lectura",
        "",
        "Esta elevación NO modifica los outputs canónicos. Cada caso recibe un `metrics_enriched_v5_2.json` paralelo con la calibración avanzada aplicada sobre los datos derivables del `metrics.json` canónico.",
        "",
        "**Veredictos posibles:**",
        "",
        "- **ELEVADO A ROBUSTO:** caso pasa de borde/débil a robusto bajo régimen V5.1 calibrado. La afirmación inferencial se sostiene tras corrección por autocorrelación + comparaciones múltiples.",
        "- **ELEVADO PARCIALMENTE:** significancia individual robusta tras calibración pero NO sobrevive FWER del corpus completo. Honestidad: el caso aporta señal pero la familia colectiva requiere atención.",
        "- **CONFIRMADO MARGINAL:** post-calibración, p_block > 0.10. El caso debe declararse como no significativo bajo el régimen calibrado.",
        "- **SENSIBLE A UMBRALES:** clasificación canónica era variable según umbrales; permanece sensible. Reportar como caso de borde explícitamente.",
        "- **CONFIRMADO NULL post-calibración:** caso era trend/suggestive marginal; bajo régimen calibrado se confirma como honestamente null.",
        "",
        "## Limitación reconocida",
        "",
        "Las estimaciones de `p_block`, `SE Newey-West` y `seed_robustness` son DERIVADAS del `metrics.json` publicado (que no expone los arrays obs/abm/forcing). La verificación definitiva requiere re-ejecutar el corpus con dump de arrays habilitado. Esto es deuda metodológica fechada de 2-3 semanas pre-depósito, no deuda externa.",
        "",
        "## Lectura cruzada",
        "",
        "- `Anexos/A0-limitaciones-declaradas.md` — limitaciones declaradas con estado V5.1/V5.2.",
        "- `09-simulaciones-edi/REFUERZOS_V5_1.md` — los cinco bloques V5.1 en detalle.",
        "- `09-simulaciones-edi/<case>/outputs/metrics_enriched_v5_2.json` — enriquecimiento por caso.",
    ])

    out_md = sims_root / "ELEVACION_V5_2_REPORT.md"
    out_md.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"✓ Markdown consolidado: {out_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
