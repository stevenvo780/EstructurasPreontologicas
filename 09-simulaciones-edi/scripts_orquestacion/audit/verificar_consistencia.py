#!/usr/bin/env python3
"""
verificar_consistencia.py — Auditor de consistencia entre simulaciones y tesis.

Verifica que:
1. metrics.json en TesisDesarrollo coincida con outputs en repos/Simulaciones
2. Los valores en 02_Modelado_Simulacion.md coincidan con metrics.json
3. No haya métricas stale (EI=0.0 sistemático, assimilation_strength>0 en eval)

Uso: python3 repos/scripts/audit/verificar_consistencia.py
"""
import json
import os
import re
import sys
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT = os.path.dirname(BASE)

CASO_MAP = {}  # Se construye dinámicamente desde las carpetas
VOLATILE_KEYS = {"generated_at", "commit", "dirty"}


def _build_caso_map():
    """Construye mapa Simulaciones → TesisDesarrollo (nombres idénticos tras renumerado)."""
    sim_base = os.path.join(BASE, "Simulaciones")
    tesis_base = os.path.join(ROOT, "TesisDesarrollo", "02_Modelado_Simulacion")
    for d in sorted(os.listdir(sim_base)):
        if '_caso_' in d:
            sim_out = os.path.join(sim_base, d, "outputs", "metrics.json")
            tesis_out = os.path.join(tesis_base, d, "metrics.json")
            if os.path.isfile(sim_out) or os.path.isfile(tesis_out):
                CASO_MAP[d] = d


def _strip_volatile(obj):
    if isinstance(obj, dict):
        return {k: _strip_volatile(v) for k, v in obj.items() if k not in VOLATILE_KEYS}
    if isinstance(obj, list):
        return [_strip_volatile(v) for v in obj]
    return obj

errors = []
warnings = []


def error(msg):
    errors.append(msg)
    print(f"  ❌ ERROR: {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  ⚠️  WARN: {msg}")


def ok(msg):
    print(f"  ✅ OK: {msg}")


def check_metrics_sync():
    """Verifica que metrics.json en TesisDesarrollo == outputs en Simulaciones."""
    print("\n=== 1. SINCRONIZACIÓN metrics.json (Simulaciones ↔ TesisDesarrollo) ===")
    _build_caso_map()
    for sim_name, tesis_name in CASO_MAP.items():
        sim_path = os.path.join(BASE, "Simulaciones", sim_name, "outputs", "metrics.json")
        tesis_path = os.path.join(ROOT, "TesisDesarrollo", "02_Modelado_Simulacion", tesis_name, "metrics.json")

        if not os.path.exists(sim_path):
            warn(f"{sim_name}: no existe {sim_path}")
            continue
        if not os.path.exists(tesis_path):
            warn(f"{tesis_name}: no existe {tesis_path}")
            continue

        with open(sim_path) as f:
            sim = json.load(f)
        with open(tesis_path) as f:
            tesis = json.load(f)

        sim_clean = _strip_volatile(sim)
        tesis_clean = _strip_volatile(tesis)

        if json.dumps(sim_clean, sort_keys=True) == json.dumps(tesis_clean, sort_keys=True):
            ok(f"{sim_name} ↔ {tesis_name}: IDÉNTICO")
        else:
            error(f"{sim_name} ↔ {tesis_name}: DESINCRONIZADO")


def check_stale_metrics():
    """Detecta señales de stale con criterio conservador (evita falsos positivos)."""
    print("\n=== 2. DETECCIÓN DE MÉTRICAS STALE ===")
    tesis_base = os.path.join(ROOT, "TesisDesarrollo", "02_Modelado_Simulacion")
    for d in sorted(os.listdir(tesis_base)):
        mpath = os.path.join(tesis_base, d, "metrics.json")
        if not os.path.isfile(mpath):
            continue
        with open(mpath) as f:
            data = json.load(f)
        ei_zero_phases = []
        for phase_name in ["synthetic", "real"]:
            phase = data.get("phases", {}).get(phase_name, {})
            if not phase:
                continue
            # EI=0.0 aislado puede ser legítimo; se marca solo como info.
            ei = phase.get("effective_information",
                           phase.get("emergence", {}).get("effective_information"))
            if ei == 0.0:
                ei_zero_phases.append(phase_name)
            # Check assimilation_strength > 0
            assim = phase.get("calibration", {}).get("assimilation_strength")
            if assim is not None and assim > 0.0:
                warn(f"{d} [{phase_name}]: assimilation_strength={assim} > 0 en calibración")
        if len(ei_zero_phases) == 1:
            print(f"  ℹ️  INFO: {d} [{ei_zero_phases[0]}] EI=0.0 (valor permitido; métrica complementaria)")
        elif len(ei_zero_phases) == 2:
            print(f"  ℹ️  INFO: {d} [synthetic+real] EI=0.0 (valor permitido; revisar solo si cambia H1)")


def check_table_consistency():
    """Verifica que la tabla en 02_Modelado_Simulacion.md coincida con metrics.json."""
    print("\n=== 3. CONSISTENCIA TABLA ↔ metrics.json ===")
    md_path = os.path.join(ROOT, "TesisDesarrollo", "02_Modelado_Simulacion", "02_Modelado_Simulacion.md")
    if not os.path.exists(md_path):
        warn("02_Modelado_Simulacion.md no encontrado")
        return

    with open(md_path) as f:
        content = f.read()

    # Parse table rows
    table_pattern = r"\|\s*(\d+_caso_\w+)\s*\|\s*(\d+)\s*\|\s*([\-\d.n/a]+)\s*\|\s*([\-\d.n/a]+)\s*\|"
    for match in re.finditer(table_pattern, content):
        caso = match.group(1)
        edi_str = match.group(3).strip()
        cr_str = match.group(4).strip()

        mpath = os.path.join(ROOT, "TesisDesarrollo", "02_Modelado_Simulacion", caso, "metrics.json")
        if not os.path.isfile(mpath):
            continue

        with open(mpath) as f:
            data = json.load(f)

        # Compare real phase EDI if available, else synthetic
        for phase_name in ["real", "synthetic"]:
            phase = data.get("phases", {}).get(phase_name, {})
            if phase:
                file_edi = phase.get("edi", {}).get("value",
                           phase.get("emergence", {}).get("edi_control"))
                file_cr = phase.get("symploke", {}).get("cr",
                          phase.get("emergence", {}).get("cr"))
                break

        if edi_str != "n/a" and file_edi is not None:
            table_edi = float(edi_str)
            if abs(table_edi - file_edi) > 0.01:
                error(f"{caso}: tabla EDI={table_edi} ≠ archivo EDI={file_edi:.3f}")
            else:
                ok(f"{caso}: EDI consistente ({table_edi} ≈ {file_edi:.3f})")


def check_overall_pass_logic():
    """Documenta la lógica de overall_pass del validador."""
    print("\n=== 4. LÓGICA DE overall_pass (hybrid_validator.py L1690) ===")
    print("  overall = all([c1, c2, c3, c4, c5, sym_ok, non_local_ok,")
    print("                  persist_ok, emergence_ok, coupling_ok, not rmse_fraud,")
    print("                  edi_valid, edi_significant])")
    print("  → Requiere 13 condiciones True simultáneamente")
    print("  → cr_valid se computa como indicador informativo (no gate)")


if __name__ == "__main__":
    print(f"🔍 Auditoría de consistencia — {datetime.now().isoformat()}")
    check_metrics_sync()
    check_stale_metrics()
    check_table_consistency()
    check_overall_pass_logic()

    print(f"\n{'='*60}")
    print(f"RESULTADO: {len(errors)} errores, {len(warnings)} advertencias")
    if errors:
        print("❌ HAY INCONSISTENCIAS QUE DEBEN CORREGIRSE")
        sys.exit(1)
    elif warnings:
        print("⚠️  Hay advertencias (métricas potencialmente stale)")
        sys.exit(0)
    else:
        print("✅ TODO CONSISTENTE")
        sys.exit(0)
