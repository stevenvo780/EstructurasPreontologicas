#!/usr/bin/env python3
"""run_pairs.py — 09-simulaciones-edi/_coupling

Corre los pares de acoplamiento inter-estructura registrados y agrega el
eje N (No-localidad) del IHO: N_axis = media de edi_coupling entre pares.
Ver common_coupling.py para la definicion del proxy (reduccion de RMSE OLS
AR1 con vs sin driver cruzado, split cronologico fuera de muestra).

Uso: python3 run_pairs.py   (desde 09-simulaciones-edi/_coupling/)
Emite: N_coupling.json
"""
import json
import os
import statistics
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

PAIRS = [
    ("deforestacion_clima", "run_coupling.py"),
    ("acidificacion_fosforo", "run_coupling.py"),
]


def main():
    pairs_out = []
    for dirname, script in PAIRS:
        script_path = os.path.join(HERE, dirname, script)
        print(f"[run_pairs] corriendo par '{dirname}'...")
        proc = subprocess.run([sys.executable, script_path], cwd=os.path.dirname(script_path),
                               capture_output=True, text=True, timeout=300)
        if proc.returncode != 0:
            print(f"  ! fallo ({proc.returncode}): {proc.stderr[-800:]}", file=sys.stderr)
            continue
        metrics_path = os.path.join(HERE, dirname, "outputs", "coupling_metrics.json")
        if not os.path.exists(metrics_path):
            print(f"  ! {dirname}: sin coupling_metrics.json")
            continue
        with open(metrics_path, "r", encoding="utf-8") as f:
            m = json.load(f)
        if "error" in m:
            print(f"  ! {dirname}: {m['error']}")
            continue
        pairs_out.append({
            "a": m["pair"]["a"],
            "b": m["pair"]["b"],
            "edi_coupling": m["edi_coupling"],
            "method": m["method"],
            "n": m["n"],
            "years_overlap": m.get("years_overlap"),
        })
        print(f"  ✓ {dirname}: edi_coupling={m['edi_coupling']:+.4f} (n={m['n']})")

    valid = [p["edi_coupling"] for p in pairs_out if isinstance(p.get("edi_coupling"), (int, float))]
    n_axis = statistics.mean(valid) if valid else None

    out = {
        "axis": "N (No-localidad / acoplamiento inter-estructura)",
        "method": "proxy_rmse_reduction_ar1_ols_lagged_driver (ver common_coupling.py); "
                  "N_axis = media de edi_coupling entre los pares registrados",
        "pairs": pairs_out,
        "N_axis": n_axis,
    }

    out_path = os.path.join(HERE, "N_coupling.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[run_pairs] escrito {out_path}")
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
