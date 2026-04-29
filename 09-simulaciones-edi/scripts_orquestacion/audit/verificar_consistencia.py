#!/usr/bin/env python3
"""Verifica consistencia básica del layout actual de simulaciones.

La versión histórica comparaba `Simulaciones/` contra `TesisDesarrollo/`.
El layout vigente usa `09-simulaciones-edi/<caso>/outputs/metrics.json` como
fuente de verdad y apéndices en `10-apendices-tecnicos/`.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
ROOT = BASE.parent
CASE_RE = re.compile(r"^\d\d_caso_")

errors: list[str] = []
warnings: list[str] = []


def error(msg: str) -> None:
    errors.append(msg)
    print(f"  ERROR: {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"  WARN: {msg}")


def ok(msg: str) -> None:
    print(f"  OK: {msg}")


def case_dirs() -> list[Path]:
    return sorted(d for d in BASE.iterdir() if d.is_dir() and CASE_RE.match(d.name))


def load_phase(metrics_path: Path) -> dict | None:
    data = json.loads(metrics_path.read_text(encoding="utf-8"))
    return data.get("phases", {}).get("real") or data.get("phases", {}).get("synthetic")


def phase_edi(phase: dict | None) -> float | None:
    if not phase:
        return None
    edi = phase.get("edi")
    if isinstance(edi, dict):
        return edi.get("value")
    if isinstance(edi, (int, float)):
        return float(edi)
    return None


def check_metrics_presence() -> None:
    print("\n=== 1. metrics.json por caso ===")
    total = 0
    readable = 0
    for case_dir in case_dirs():
        total += 1
        metrics_path = case_dir / "outputs" / "metrics.json"
        if not metrics_path.exists():
            error(f"{case_dir.name}: falta outputs/metrics.json")
            continue
        try:
            phase = load_phase(metrics_path)
        except Exception as exc:  # pragma: no cover - diagnostic path
            error(f"{case_dir.name}: metrics.json ilegible ({exc})")
            continue
        if phase_edi(phase) is None:
            error(f"{case_dir.name}: EDI no disponible en fase real/synthetic")
            continue
        readable += 1
    ok(f"{readable}/{total} casos inter-dominio con metrics.json legible y EDI")


def check_primary_arrays() -> None:
    print("\n=== 2. primary_arrays.json ===")
    cases = case_dirs()
    arrays = [d for d in cases if (d / "outputs" / "primary_arrays.json").exists()]
    real = 0
    reconstructed = 0
    for case_dir in arrays:
        data = json.loads((case_dir / "outputs" / "primary_arrays.json").read_text(encoding="utf-8"))
        extra = data.get("extra", {})
        if extra.get("verified_real_data") is True:
            real += 1
        elif extra.get("verified_real_data") is False:
            reconstructed += 1
    ok(f"{len(arrays)}/{len(cases)} casos con primary_arrays.json")
    ok(f"{real} arrays reales verificados; {reconstructed} reconstruidos desde metrics")


def check_appendix_table() -> None:
    print("\n=== 3. Tabla A.8.1 vs metrics.json ===")
    appendix = ROOT / "10-apendices-tecnicos" / "01-tablas-crudas-corpus-interdominio.md"
    if not appendix.exists():
        warn("No existe apéndice inter-dominio")
        return

    text = appendix.read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*(\d\d)\s*\|[^|]*\|[^|]*\|\s*(-?\d+(?:\.\d+)?)\s*\|", text, flags=re.M)
    checked = 0
    for case_num, edi_s in rows:
        candidates = [d for d in case_dirs() if d.name.startswith(f"{case_num}_")]
        if not candidates:
            continue
        metrics_path = candidates[0] / "outputs" / "metrics.json"
        if not metrics_path.exists():
            continue
        current = phase_edi(load_phase(metrics_path))
        if current is None:
            continue
        table_edi = float(edi_s)
        checked += 1
        if abs(table_edi - current) > 0.01:
            warn(
                f"{candidates[0].name}: tabla EDI={table_edi:.4f} "
                f"vs metrics real/synthetic={current:.4f}"
            )
    ok(f"{checked} filas de Tabla A.8.1 contrastadas")


def check_overall_pass_logic() -> None:
    print("\n=== 4. Lógica de overall_pass ===")
    print("  overall_pass requiere el gate compuesto C1-C5 + controles auxiliares + EDI válido/significativo.")
    print("  Si una fila tiene EDI alto pero p alto u overall_pass=False, no debe leerse como strong demostrativo.")


if __name__ == "__main__":
    print(f"Auditoría de consistencia — {datetime.now().isoformat()}")
    check_metrics_presence()
    check_primary_arrays()
    check_appendix_table()
    check_overall_pass_logic()

    print(f"\nRESULTADO: {len(errors)} errores, {len(warnings)} advertencias")
    if errors:
        sys.exit(1)
    sys.exit(0)
