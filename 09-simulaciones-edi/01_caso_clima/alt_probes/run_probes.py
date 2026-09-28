#!/usr/bin/env python3
"""run_probes.py — 01_caso_clima/alt_probes

Corre las sondas alternativas del caso Clima (mismo fenomeno, distinto
observable/instrumento) y agrega la DISPERSION del EDI entre sondas:
el eje V (Viscosidad) del IHO -- "no hay vista sin sonda": cuanto se mueve
la lectura del hiperobjeto segun con que instrumento se lo mira.

Uso: python3 run_probes.py   (desde 09-simulaciones-edi/01_caso_clima/alt_probes/)
Emite: V_dispersion.json
"""
import json
import os
import statistics
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Sondas registradas + la sonda "base" (caso original, instrumento de referencia).
PROBES = ["co2_instrument", "annual_window", "decadal_smoothed"]
BASE_CASE_DIR = os.path.normpath(os.path.join(HERE, ".."))


def _run_validate(validate_py):
    """Ejecuta validate.py de una sonda; True si corrio sin error."""
    proc = subprocess.run(
        [sys.executable, validate_py],
        cwd=os.path.dirname(validate_py),
        capture_output=True, text=True, timeout=600,
    )
    ok = proc.returncode == 0
    if not ok:
        print(f"  ! fallo ({proc.returncode}): {proc.stderr[-800:]}", file=sys.stderr)
    return ok


def _load_edi(metrics_path):
    with open(metrics_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    ph = d.get("phases", {}).get("real") or d.get("phases", {}).get("synthetic")
    if not ph:
        return None
    edi = ph.get("edi", {})
    return edi.get("value")


def main():
    results = []

    # Sonda de referencia: el caso base (instrumento = temperatura, mensual, sin suavizar).
    base_metrics = os.path.join(BASE_CASE_DIR, "outputs", "metrics.json")
    if os.path.exists(base_metrics):
        edi = _load_edi(base_metrics)
        if edi is not None:
            results.append({"name": "base_temperatura_mensual", "edi": edi})

    for name in PROBES:
        probe_dir = os.path.join(HERE, name)
        validate_py = os.path.join(probe_dir, "src", "validate.py")
        if not os.path.exists(validate_py):
            print(f"  ! {name}: no existe {validate_py}, se omite")
            continue
        print(f"[run_probes] corriendo sonda '{name}'...")
        ok = _run_validate(validate_py)
        metrics_path = os.path.join(probe_dir, "outputs", "metrics.json")
        if not ok or not os.path.exists(metrics_path):
            print(f"  ! {name}: sin metrics.json utilizable, se omite del agregado")
            continue
        edi = _load_edi(metrics_path)
        if edi is None:
            print(f"  ! {name}: metrics.json sin edi.value, se omite")
            continue
        results.append({"name": name, "edi": edi})
        print(f"  ✓ {name}: EDI={edi:+.4f}")

    edis = [r["edi"] for r in results]
    if len(edis) >= 2:
        edi_spread = max(edis) - min(edis)
        v_axis = statistics.pstdev(edis)
    else:
        edi_spread = None
        v_axis = None

    out = {
        "axis": "V (Viscosidad / dependencia-instrumento)",
        "method": "dispersion del EDI (fase real cuando existe, si no sintetica) entre "
                  ">=2 sondas del mismo fenomeno (clima) que difieren SOLO en el "
                  "observable/instrumento (co2 vs temperatura) o en la ventana/agregacion "
                  "temporal (mensual interpolado vs anual nativo vs suavizado decadal). "
                  "V_axis = desviacion estandar poblacional del EDI entre sondas.",
        "probes": results,
        "edi_spread": edi_spread,
        "V_axis": v_axis,
    }

    out_path = os.path.join(HERE, "V_dispersion.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[run_probes] escrito {out_path}")
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
