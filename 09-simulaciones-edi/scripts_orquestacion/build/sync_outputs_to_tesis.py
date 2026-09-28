#!/usr/bin/env python3
"""Verifica outputs in-place de cada caso (ex sync hacia TesisDesarrollo).

Historial: copiaba outputs/metrics.json y outputs/report.md desde
repos/Simulaciones hacia TesisDesarrollo/02_Modelado_Simulacion. Ambos
árboles se retiraron en la consolidación mono-repo: los outputs ya viven en
09-simulaciones-edi/<caso>/outputs/. Desde 2026-09-28 este script verifica
su presencia en lugar de copiar.

Salida: exit 0 si todos los casos tienen outputs/metrics.json; exit 1 si
falta algún metrics.json. Un report.md faltante es WARN (casos 41/42 no
generan reporte narrativo por diseño) y no falla.
"""

from __future__ import annotations

import argparse
from pathlib import Path


EDI_DIR = Path(__file__).resolve().parents[2]


def _matches(case_name: str, case_filter: str | None) -> bool:
    if not case_filter:
        return True
    return case_filter.lower() in case_name.lower()


def check_outputs(
    case_filter: str | None = None,
) -> tuple[int, list[str], list[str]]:
    """Retorna (revisados, metrics faltantes, reports faltantes)."""
    checked = 0
    missing_metrics: list[str] = []
    missing_reports: list[str] = []
    for case_dir in sorted(EDI_DIR.glob("[0-9][0-9]_caso_*")):
        if not case_dir.is_dir():
            continue
        case = case_dir.name
        if not _matches(case, case_filter):
            continue
        checked += 1
        if not (case_dir / "outputs" / "metrics.json").exists():
            missing_metrics.append(f"{case}:outputs/metrics.json")
        if not (case_dir / "outputs" / "report.md").exists():
            missing_reports.append(f"{case}:outputs/report.md")
    return checked, missing_metrics, missing_reports


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verifica outputs in-place (sin copiar; TesisDesarrollo retirado)"
    )
    parser.add_argument("--case", help="Filtro parcial de caso (ej: clima, 06, falsacion)")
    parser.add_argument("--dry-run", action="store_true", help="Solo mostrar casos, sin verificar")
    args = parser.parse_args()

    if args.dry_run:
        n = 0
        for case_dir in sorted(EDI_DIR.glob("[0-9][0-9]_caso_*")):
            if case_dir.is_dir() and _matches(case_dir.name, args.case):
                print(f"[DRY] {case_dir.name}")
                n += 1
        print(f"Casos evaluados: {n}")
        return 0

    checked, missing_metrics, missing_reports = check_outputs(case_filter=args.case)
    print(f"Casos evaluados: {checked}")
    print("Archivos copiados: 0 (verificación in-place; nada que sincronizar)")
    if missing_reports:
        print("WARN reports faltantes (no falla):")
        for m in missing_reports:
            print(f"  - {m}")
    if missing_metrics:
        print("Faltan metrics.json:")
        for m in missing_metrics:
            print(f"  - {m}")
        return 1
    print("metrics.json presente en todos los casos evaluados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
