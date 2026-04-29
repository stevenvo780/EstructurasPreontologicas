#!/usr/bin/env python3
"""
Aplica corrección Holm-Bonferroni de FWER a los p-values reportados en
los metrics.json del corpus completo (40 casos). Escribe el p_holm_adjusted
en cada metrics.json para verificación reproducible.

Cierra el fallo F12: el FWER se anunciaba pero no se aplicaba realmente
al corpus. Tras este script, cada metrics.json tiene el campo
"p_value_holm_adjusted" con el valor correcto y la información de qué
casos sobreviven α=0.05 tras corrección.

Uso:
    python3 scripts/apply_fwer_to_corpus.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.calibration import fwer_correct


def _extract_p_value(metrics: dict) -> float | None:
    if "p_value" in metrics:
        try:
            return float(metrics["p_value"])
        except (TypeError, ValueError):
            pass
    phases = metrics.get("phases") or {}
    phase = phases.get("real") or phases.get("synthetic") or {}
    if isinstance(phase, dict):
        edi = phase.get("edi")
        if isinstance(edi, dict):
            v = edi.get("permutation_pvalue")
            if v is not None:
                try:
                    return float(v)
                except (TypeError, ValueError):
                    pass
    return None


def _iter_metrics() -> list[tuple[str, Path, dict]]:
    cases = []
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name[:2].isdigit() and "_caso_" in d.name:
            mp = d / "outputs" / "metrics.json"
            if mp.is_file():
                cases.append((d.name, mp, json.loads(mp.read_text())))
    multi = ROOT / "corpus_multiescala"
    if multi.is_dir():
        for d in sorted(multi.iterdir()):
            if d.is_dir() and d.name[:2].isdigit():
                mp = d / "outputs" / "metrics.json"
                if mp.is_file():
                    cases.append((d.name, mp, json.loads(mp.read_text())))
    return cases


def _write_holm_into_metrics(path: Path, metrics: dict, p_holm: float, sobrevive: bool):
    if "fwer_holm" not in metrics:
        metrics["fwer_holm"] = {}
    metrics["fwer_holm"]["p_value_raw"] = float(_extract_p_value(metrics))
    metrics["fwer_holm"]["p_value_holm_adjusted"] = float(p_holm)
    metrics["fwer_holm"]["survives_alpha_0_05"] = bool(sobrevive)
    metrics["fwer_holm"]["correction_method"] = "Holm-Bonferroni (1979)"
    metrics["fwer_holm"]["note"] = (
        "Corrección de family-wise error rate aplicada al corpus completo. "
        "Sobrevivir α=0.05 significa que el caso permanece estadísticamente "
        "significativo tras corrección por comparaciones múltiples. Casos "
        "con p_raw < 0.05 pero p_holm > 0.05 son significativos individuales "
        "pero no significativos colectivamente."
    )
    path.write_text(json.dumps(metrics, indent=2, ensure_ascii=False))


def main() -> int:
    print("Aplicando FWER Holm-Bonferroni al corpus completo")
    print("=" * 70)

    inter_dom = []
    inter_esc = []
    for cid, mp, m in _iter_metrics():
        p = _extract_p_value(m)
        if p is None:
            print(f"  ⚠️  {cid}: sin p_value extraíble; saltado")
            continue
        if cid.startswith(("31_", "32_", "33_", "34_", "35_",
                           "36_", "37_", "38_", "39_", "40_")):
            inter_esc.append((cid, mp, m, p))
        else:
            inter_dom.append((cid, mp, m, p))

    # FWER por familia: corpus inter-dominio (30 casos) y corpus inter-escala (10 casos)
    for nombre, familia in [("inter-dominio", inter_dom), ("inter-escala", inter_esc)]:
        if not familia:
            continue
        print(f"\n  Familia {nombre} ({len(familia)} casos):")
        p_arr = np.array([p for _, _, _, p in familia])
        p_holm, rejected = fwer_correct(p_arr, method="holm")
        sobreviven = []
        for (cid, mp, m, p_raw), p_h, rej in zip(familia, p_holm, rejected):
            _write_holm_into_metrics(mp, m, float(p_h), bool(rej))
            estado = "✓ sobrevive" if rej else "✗ no sobrevive"
            if rej:
                sobreviven.append(cid)
            print(f"    {cid:42s} p_raw={p_raw:.4f}  p_holm={p_h:.4f}  {estado}")
        print(f"\n    Sobreviven FWER α=0.05: {len(sobreviven)}/{len(familia)}")
        for cid in sobreviven:
            print(f"      • {cid}")

    print("\n" + "=" * 70)
    print("✓ p_value_holm_adjusted escrito en cada metrics.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
