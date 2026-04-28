#!/usr/bin/env python3
"""Sincroniza outputs de repos/Simulaciones hacia TesisDesarrollo/02_Modelado_Simulacion.

Copia `outputs/metrics.json` y `outputs/report.md` de cada caso a:
`TesisDesarrollo/02_Modelado_Simulacion/<caso>/metrics.json` y `report.md`.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SIM_ROOT = ROOT / "repos" / "Simulaciones"
TESIS_ROOT = ROOT / "TesisDesarrollo" / "02_Modelado_Simulacion"


def _matches(case_name: str, case_filter: str | None) -> bool:
    if not case_filter:
        return True
    return case_filter.lower() in case_name.lower()


def sync_outputs(case_filter: str | None = None, dry_run: bool = False) -> tuple[int, int]:
    copied = 0
    checked = 0

    for case_dir in sorted(SIM_ROOT.glob("[0-9][0-9]_caso_*")):
        case = case_dir.name
        if not _matches(case, case_filter):
            continue

        checked += 1
        src_metrics = case_dir / "outputs" / "metrics.json"
        src_report = case_dir / "outputs" / "report.md"

        dst_dir = TESIS_ROOT / case
        dst_metrics = dst_dir / "metrics.json"
        dst_report = dst_dir / "report.md"

        if dry_run:
            if src_metrics.exists() or src_report.exists():
                print(f"[DRY] {case}")
            continue

        dst_dir.mkdir(parents=True, exist_ok=True)

        if src_metrics.exists():
            shutil.copy2(src_metrics, dst_metrics)
            copied += 1
        if src_report.exists():
            shutil.copy2(src_report, dst_report)
            copied += 1

    return checked, copied


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync outputs Simulaciones -> TesisDesarrollo")
    parser.add_argument("--case", help="Filtro parcial de caso (ej: clima, 06, falsacion)")
    parser.add_argument("--dry-run", action="store_true", help="Solo mostrar casos, sin copiar")
    args = parser.parse_args()

    checked, copied = sync_outputs(case_filter=args.case, dry_run=args.dry_run)
    print(f"Casos evaluados: {checked}")
    print(f"Archivos copiados: {copied}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
