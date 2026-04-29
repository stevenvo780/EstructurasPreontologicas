"""
Visualización del corpus EDI — F33.

Genera figuras a partir de los metrics.json del corpus macro (09-simulaciones-edi/<caso>/outputs/)
y del corpus multiescala (09-simulaciones-edi/corpus_multiescala/<caso>/outputs/).

Salida: figures/corpus/
- corpus_edi_bars.{png,svg}     barras EDI con CI 95% por caso (macro)
- corpus_multiescala_scatter.{png,svg} escala espacial vs temporal (multiescala)
- corpus_qes_distribution.{png,svg} distribución QES por categoría
- corpus_summary_table.csv      tabla CSV con todos los campos relevantes
"""
from __future__ import annotations
import json
import csv
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = ROOT / "09-simulaciones-edi"
OUT_DIR = ROOT / "figures" / "corpus"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DOMAIN_MAP = {
    "01_caso_clima": "físico",
    "02_caso_conciencia": "social",
    "03_caso_contaminacion": "ecológico",
    "04_caso_energia": "social-técnico",
    "05_caso_epidemiologia": "biológico",
    "06_caso_falsacion_exogeneidad": "control",
    "07_caso_falsacion_no_estacionariedad": "control",
    "08_caso_falsacion_observabilidad": "control",
    "09_caso_finanzas": "social",
    "10_caso_justicia": "social",
    "11_caso_movilidad": "social-técnico",
    "12_caso_paradigmas": "social",
    "13_caso_politicas_estrategicas": "social",
    "14_caso_postverdad": "social",
    "15_caso_wikipedia": "social-técnico",
    "16_caso_deforestacion": "ecológico",
    "17_caso_oceanos": "físico",
    "18_caso_urbanizacion": "social",
    "19_caso_acidificacion_oceanica": "físico-químico",
    "20_caso_kessler": "físico-técnico",
    "21_caso_salinizacion": "ecológico",
    "22_caso_fosforo": "biogeoquímico",
    "23_caso_erosion_dialectica": "social",
    "24_caso_microplasticos": "ecológico",
    "25_caso_acuiferos": "físico",
    "26_caso_starlink": "físico-técnico",
    "27_caso_riesgo_biologico": "biológico",
    "28_caso_fuga_cerebros": "social",
    "29_caso_iot": "social-técnico",
    "30_caso_behavioral_dynamics": "individual",
    "41_caso_wolfram_extendido": "computacional",
    "42_caso_histeresis_institucional": "social",
}

MULTIESCALA_DOMAIN = {
    "31_decoherencia_cuantica": ("cuántico", -9, -6),
    "32_espin_orbita": ("atómico", -10, -15),
    "33_villin_headpiece": ("molecular", -9, -6),
    "34_michaelis_menten": ("bioquímico", -8, -3),
    "35_ciclo_celular": ("celular", -5, 3),
    "36_nfkb": ("celular", -5, 2),
    "37_hrv_cardiaco": ("organísmico", 0, 0),
    "38_locomocion_alternativa": ("organísmico", 0, 0),
    "39_cefeidas_ogle": ("astrofísico", 11, 5),
    "40_cumulos_globulares": ("astrofísico", 18, 14),
}


def extract_macro_record(case_dir: Path) -> dict | None:
    metrics_file = case_dir / "outputs" / "metrics.json"
    if not metrics_file.exists():
        return None
    try:
        with open(metrics_file) as f:
            m = json.load(f)
    except Exception as e:
        print(f"WARN parsing {metrics_file}: {e}", file=sys.stderr)
        return None

    case_id = case_dir.name
    phases = m.get("phases", {})
    syn = phases.get("synthetic") or phases.get("real") or {}
    edi = syn.get("edi", {})
    return {
        "case_id": case_id,
        "case_name": m.get("case", case_id),
        "domain": DOMAIN_MAP.get(case_id, "no clasificado"),
        "edi": edi.get("value"),
        "ci_lo": edi.get("ci_lo"),
        "ci_hi": edi.get("ci_hi"),
        "p_value": edi.get("permutation_pvalue"),
        "valid": edi.get("valid"),
        "loe_factor": edi.get("loe_factor"),
        "overall_pass": syn.get("overall_pass"),
    }


def extract_multiescala_record(case_dir: Path) -> dict | None:
    metrics_file = case_dir / "outputs" / "metrics.json"
    if not metrics_file.exists():
        return None
    try:
        with open(metrics_file) as f:
            m = json.load(f)
    except Exception as e:
        print(f"WARN parsing {metrics_file}: {e}", file=sys.stderr)
        return None
    case_id = case_dir.name
    domain_info = MULTIESCALA_DOMAIN.get(case_id, ("desconocido", 0, 0))
    ci = m.get("ci_95") or [None, None]
    return {
        "case_id": case_id,
        "case_name": m.get("case_name", case_id),
        "domain": domain_info[0],
        "log_length_m": domain_info[1],
        "log_time_s": domain_info[2],
        "edi": m.get("edi"),
        "ci_lo": ci[0] if ci else None,
        "ci_hi": ci[1] if ci else None,
        "p_value": m.get("p_value"),
        "overall_pass": m.get("overall_pass"),
    }


def load_qes_report() -> dict:
    qes = SIM_DIR / "QES_AUDIT_REPORT.json"
    if not qes.exists():
        return {}
    with open(qes) as f:
        return json.load(f)


def fig_edi_bars(records: list[dict]) -> None:
    """Barras EDI por caso macro con CI 95% bootstrap."""
    valid = [r for r in records if r.get("edi") is not None and r.get("ci_lo") is not None and r.get("ci_hi") is not None]
    valid.sort(key=lambda r: r["edi"], reverse=True)
    if not valid:
        print("WARN no records with CI for bar plot", file=sys.stderr)
        return
    edis = np.array([r["edi"] for r in valid])
    los = np.array([r["ci_lo"] for r in valid])
    his = np.array([r["ci_hi"] for r in valid])
    err_low = np.maximum(edis - los, 0)
    err_high = np.maximum(his - edis, 0)
    labels = [r["case_id"].replace("_caso_", " ").replace("_", " ") for r in valid]
    colors = []
    for r in valid:
        e = r["edi"]
        if e is None:
            colors.append("#999999")
        elif e >= 0.55:
            colors.append("#1f6f3a")  # strong
        elif e >= 0.30:
            colors.append("#3b78b8")  # weak admisible
        elif e >= 0:
            colors.append("#bd9b3a")  # marginal
        else:
            colors.append("#a83232")  # null/falsacion

    fig, ax = plt.subplots(figsize=(11, max(6, 0.32 * len(valid))))
    y = np.arange(len(valid))
    ax.barh(y, edis, xerr=[err_low, err_high], color=colors, edgecolor="#333", linewidth=0.6, capsize=3)
    ax.axvline(0.55, color="#1f6f3a", linestyle="--", linewidth=0.8, alpha=0.6, label="strong (0.55)")
    ax.axvline(0.30, color="#3b78b8", linestyle="--", linewidth=0.8, alpha=0.6, label="weak (0.30)")
    ax.axvline(0.0, color="#444", linestyle="-", linewidth=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("EDI (con CI 95% bootstrap)")
    ax.set_title("Corpus EDI macro — distribución por caso (ordenado por EDI)")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(OUT_DIR / f"corpus_edi_bars.{ext}", dpi=150)
    plt.close(fig)
    print(f"  → corpus_edi_bars.{{png,svg}}  ({len(valid)} casos)")


def fig_multiescala_scatter(records: list[dict]) -> None:
    valid = [r for r in records if r.get("edi") is not None]
    if not valid:
        print("WARN multiescala empty", file=sys.stderr)
        return
    xs = np.array([r["log_length_m"] for r in valid])
    ys = np.array([r["log_time_s"] for r in valid])
    edis = np.array([r["edi"] for r in valid])
    sizes = np.clip((edis + 1.5) * 200, 30, 600)

    fig, ax = plt.subplots(figsize=(9, 6))
    sc = ax.scatter(xs, ys, s=sizes, c=edis, cmap="RdYlGn", vmin=-1.0, vmax=1.0,
                    edgecolors="#222", linewidths=0.8, alpha=0.85)
    for r, x, y in zip(valid, xs, ys):
        label = r["case_id"].split("_", 1)[1] if "_" in r["case_id"] else r["case_id"]
        ax.annotate(label, (x, y), xytext=(6, 6), textcoords="offset points", fontsize=7)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("EDI")
    ax.set_xlabel("log₁₀ longitud característica (m)")
    ax.set_ylabel("log₁₀ tiempo característico (s)")
    ax.set_title("Corpus multiescala — EDI sobre escalas espacio-temporales (10 casos)")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(OUT_DIR / f"corpus_multiescala_scatter.{ext}", dpi=150)
    plt.close(fig)
    print(f"  → corpus_multiescala_scatter.{{png,svg}}  ({len(valid)} casos)")


def fig_qes_distribution(qes_data: dict) -> None:
    if not qes_data:
        print("WARN no QES data", file=sys.stderr)
        return
    cats = qes_data.get("categories", {})
    if not cats:
        return
    order = ["ROBUSTO", "DEMOSTRATIVO", "PROGRAMÁTICO", "PILOTO", "INADMISIBLE"]
    counts = [cats.get(c, 0) for c in order]
    colors = ["#1f6f3a", "#3b78b8", "#bd9b3a", "#a8843b", "#a83232"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    bars = ax1.bar(order, counts, color=colors, edgecolor="#222")
    for b, n in zip(bars, counts):
        ax1.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.3, str(n),
                 ha="center", fontsize=10, fontweight="bold")
    ax1.set_ylabel("número de casos")
    ax1.set_title(f"QES — categorías (n={qes_data.get('n_total', sum(counts))})")
    ax1.grid(axis="y", alpha=0.3)

    results = qes_data.get("results_sorted", [])
    qes_vals = sorted([r["QES"] for r in results if r.get("QES") is not None], reverse=True)
    ax2.plot(range(1, len(qes_vals) + 1), qes_vals, marker="o", linewidth=1.2, color="#222")
    ax2.axhline(0.85, color="#1f6f3a", linestyle="--", alpha=0.7, label="ROBUSTO ≥ 0.85")
    ax2.axhline(0.70, color="#3b78b8", linestyle="--", alpha=0.7, label="DEMOSTRATIVO ≥ 0.70")
    ax2.axhline(0.55, color="#bd9b3a", linestyle="--", alpha=0.7, label="PROGRAMÁTICO ≥ 0.55")
    ax2.axhline(0.40, color="#a8843b", linestyle="--", alpha=0.7, label="PILOTO ≥ 0.40")
    ax2.set_xlabel("rango (ordenado descendente)")
    ax2.set_ylabel("QES")
    ax2.set_title("QES — distribución acumulada")
    ax2.legend(fontsize=8, loc="lower left")
    ax2.grid(alpha=0.3)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(OUT_DIR / f"corpus_qes_distribution.{ext}", dpi=150)
    plt.close(fig)
    print(f"  → corpus_qes_distribution.{{png,svg}}  ({len(qes_vals)} casos QES)")


def fig_domain_heatmap(records: list[dict]) -> None:
    """Heatmap dominio × banda EDI."""
    valid = [r for r in records if r.get("edi") is not None]
    if not valid:
        return
    bands = [("strong (≥0.55)", lambda e: e >= 0.55),
             ("weak (0.30-0.55)", lambda e: 0.30 <= e < 0.55),
             ("marginal (0-0.30)", lambda e: 0.0 <= e < 0.30),
             ("null/neg (<0)", lambda e: e < 0.0)]
    domains = sorted(set(r["domain"] for r in valid if r["domain"] != "control"))
    M = np.zeros((len(domains), len(bands)), dtype=int)
    for r in valid:
        if r["domain"] == "control":
            continue
        di = domains.index(r["domain"])
        for bi, (_, pred) in enumerate(bands):
            if pred(r["edi"]):
                M[di, bi] += 1
                break
    fig, ax = plt.subplots(figsize=(9, max(4, 0.45 * len(domains))))
    im = ax.imshow(M, cmap="YlGnBu", aspect="auto")
    ax.set_xticks(range(len(bands)))
    ax.set_xticklabels([b[0] for b in bands], rotation=20, ha="right")
    ax.set_yticks(range(len(domains)))
    ax.set_yticklabels(domains)
    for i in range(len(domains)):
        for j in range(len(bands)):
            if M[i, j] > 0:
                ax.text(j, i, str(M[i, j]), ha="center", va="center",
                        color="white" if M[i, j] > M.max() * 0.5 else "#222",
                        fontweight="bold", fontsize=10)
    ax.set_title("Corpus macro — distribución por dominio y banda EDI")
    fig.colorbar(im, ax=ax, label="casos")
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(OUT_DIR / f"corpus_domain_heatmap.{ext}", dpi=150)
    plt.close(fig)
    print(f"  → corpus_domain_heatmap.{{png,svg}}  ({len(domains)} dominios)")


def write_csv(macro: list[dict], multi: list[dict]) -> None:
    out = OUT_DIR / "corpus_summary_table.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["scope", "case_id", "case_name", "domain", "edi", "ci_lo", "ci_hi",
                    "p_value", "overall_pass", "log_length_m", "log_time_s"])
        for r in macro:
            w.writerow(["macro", r["case_id"], r.get("case_name"), r["domain"],
                        r["edi"], r["ci_lo"], r["ci_hi"], r["p_value"],
                        r.get("overall_pass"), "", ""])
        for r in multi:
            w.writerow(["multiescala", r["case_id"], r.get("case_name"), r["domain"],
                        r["edi"], r["ci_lo"], r["ci_hi"], r["p_value"],
                        r.get("overall_pass"), r.get("log_length_m"), r.get("log_time_s")])
    print(f"  → corpus_summary_table.csv  ({len(macro)} macro + {len(multi)} multiescala)")


def main() -> int:
    macro_dirs = sorted([d for d in SIM_DIR.iterdir()
                         if d.is_dir() and re.match(r"^\d+_caso_", d.name)])
    macro_records = [r for r in (extract_macro_record(d) for d in macro_dirs) if r]

    multi_root = SIM_DIR / "corpus_multiescala"
    multi_dirs = sorted([d for d in multi_root.iterdir()
                         if d.is_dir() and re.match(r"^\d+_", d.name)]) if multi_root.exists() else []
    multi_records = [r for r in (extract_multiescala_record(d) for d in multi_dirs) if r]

    qes_data = load_qes_report()

    print(f"corpus macro: {len(macro_records)}, multiescala: {len(multi_records)}")
    print(f"figures → {OUT_DIR}")

    fig_edi_bars(macro_records)
    fig_multiescala_scatter(multi_records)
    fig_qes_distribution(qes_data)
    fig_domain_heatmap(macro_records)
    write_csv(macro_records, multi_records)
    return 0


if __name__ == "__main__":
    sys.exit(main())
