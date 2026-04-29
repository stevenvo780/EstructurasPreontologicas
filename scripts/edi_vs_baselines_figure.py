"""
Figura comparativa EDI acoplado vs baselines — ampliación F33.

Usa `09-simulaciones-edi/baselines/baselines_report.json` (producido por F15)
y genera dos paneles:
  - Panel izquierdo: barras agrupadas RMSE acoplado vs persistencia, RW, ARIMA, VAR
  - Panel derecho: EDI vs cada baseline (1 - RMSE_acoplado / RMSE_baseline) ordenado

Salida: figures/corpus/edi_vs_baselines.{png,svg}
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "09-simulaciones-edi" / "baselines" / "baselines_report.json"
OUT_DIR = ROOT / "figures" / "corpus"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> int:
    if not REPORT.exists():
        print(f"missing {REPORT}; run scripts/baselines_arima_var.py first", file=sys.stderr)
        return 1
    with open(REPORT) as f:
        data = json.load(f)
    results = [r for r in data["results"] if "skip_reason" not in r]
    if not results:
        print("no valid results", file=sys.stderr)
        return 1

    cases = [r["case_id"].replace("_caso_", " ").replace("_", " ") for r in results]
    n = len(cases)

    rmse_coupled = np.array([r["rmse"]["abm_coupled_val"] for r in results])
    rmse_persist = np.array([r["rmse"].get("persistence", np.nan) for r in results])
    rmse_rw = np.array([r["rmse"].get("random_walk", np.nan) for r in results])
    rmse_arima = np.array([r["rmse"].get("arima_1_1_1", r["rmse"].get("arima_1_0_1", np.nan)) for r in results])
    rmse_var = np.array([r["rmse"].get("var_obs_forcing", np.nan) for r in results])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Panel 1: barras agrupadas RMSE
    bar_w = 0.16
    x = np.arange(n)
    ax1.bar(x - 2*bar_w, rmse_coupled, bar_w, label="acoplado", color="#1f6f3a", edgecolor="#222")
    ax1.bar(x - bar_w, rmse_persist, bar_w, label="persistencia", color="#bd9b3a", edgecolor="#222")
    ax1.bar(x, rmse_rw, bar_w, label="random walk", color="#a8843b", edgecolor="#222")
    ax1.bar(x + bar_w, rmse_arima, bar_w, label="ARIMA", color="#3b78b8", edgecolor="#222")
    ax1.bar(x + 2*bar_w, rmse_var, bar_w, label="VAR + forcing", color="#7a4dc4", edgecolor="#222")
    ax1.set_xticks(x)
    ax1.set_xticklabels(cases, rotation=30, ha="right", fontsize=9)
    ax1.set_ylabel("RMSE en held-out")
    ax1.set_title("RMSE: modelo acoplado vs baselines no-estructurales")
    ax1.legend(fontsize=9, loc="upper left")
    ax1.grid(axis="y", alpha=0.3)
    ax1.set_yscale("log")

    # Panel 2: EDI vs baselines
    edi_persist = np.where(rmse_persist > 0, 1 - rmse_coupled / rmse_persist, np.nan)
    edi_rw = np.where(rmse_rw > 0, 1 - rmse_coupled / rmse_rw, np.nan)
    edi_arima = np.where(rmse_arima > 0, 1 - rmse_coupled / rmse_arima, np.nan)
    edi_var = np.where(rmse_var > 0, 1 - rmse_coupled / rmse_var, np.nan)

    ax2.bar(x - 1.5*bar_w, edi_persist, bar_w, label="vs persistencia", color="#bd9b3a", edgecolor="#222")
    ax2.bar(x - 0.5*bar_w, edi_rw, bar_w, label="vs random walk", color="#a8843b", edgecolor="#222")
    ax2.bar(x + 0.5*bar_w, edi_arima, bar_w, label="vs ARIMA", color="#3b78b8", edgecolor="#222")
    ax2.bar(x + 1.5*bar_w, edi_var, bar_w, label="vs VAR", color="#7a4dc4", edgecolor="#222")
    ax2.axhline(0, color="#222", linewidth=0.8)
    ax2.set_xticks(x)
    ax2.set_xticklabels(cases, rotation=30, ha="right", fontsize=9)
    ax2.set_ylabel(r"EDI vs baseline $= 1 - RMSE_{acopl}/RMSE_{base}$")
    ax2.set_title("EDI relativo: positivo = acoplado mejor; negativo = baseline mejor")
    ax2.legend(fontsize=9, loc="lower right")
    ax2.grid(axis="y", alpha=0.3)

    fig.suptitle(
        "Modelo acoplado EDI vs baselines no-estructurales (F15)\n"
        f"7 casos con `primary_arrays.json` — held-out evaluation",
        fontsize=12,
    )
    fig.tight_layout()
    for ext in ("png", "svg"):
        out = OUT_DIR / f"edi_vs_baselines.{ext}"
        fig.savefig(out, dpi=150)
        print(f"  → {out}")
    plt.close(fig)
    return 0


if __name__ == "__main__":
    sys.exit(main())
