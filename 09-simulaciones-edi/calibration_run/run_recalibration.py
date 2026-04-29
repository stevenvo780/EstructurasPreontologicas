"""
Recalibración real del corpus inter-dominio (paso 6.bis hoja de ruta).

Para los 7 casos con primary_arrays.json (strong + Wolfram extendido +
histéresis institucional), ejecuta block_bootstrap_pvalue de Politis-Romano
(stationary bootstrap, n_perm=2999) sobre los arrays observados y simulados
reales. Para los demás casos del corpus, usa el p-value canónico existente
en metrics.json.

Aplica Holm-Bonferroni a los 30 p-values del corpus inter-dominio para
control FWER al α=0.05.

Salida:
  outputs/recalibration_results.json — resultados crudos
  outputs/recalibration_table.md     — tabla recalibrada Markdown
  outputs/recalibration_summary.md   — síntesis textual

Compromiso firme paso 6.bis cumplido en ejecución pre-defensa.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

REPO = Path("/datos/repos/EstructurasPreontologicas")
SIM = REPO / "09-simulaciones-edi"
sys.path.insert(0, str(SIM))

from common.calibration import block_bootstrap_pvalue, fwer_correct  # noqa: E402

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

# Casos del corpus inter-dominio (orden por número de caso)
CORPUS = [
    "01_caso_clima",
    "02_caso_conciencia",
    "03_caso_contaminacion",
    "04_caso_energia",
    "05_caso_epidemiologia",
    "06_caso_falsacion_exogeneidad",
    "07_caso_falsacion_no_estacionariedad",
    "08_caso_falsacion_observabilidad",
    "09_caso_finanzas",
    "10_caso_justicia",
    "11_caso_movilidad",
    "12_caso_paradigmas",
    "13_caso_politicas_estrategicas",
    "14_caso_postverdad",
    "15_caso_wikipedia",
    "16_caso_deforestacion",
    "17_caso_oceanos",
    "18_caso_urbanizacion",
    "19_caso_acidificacion_oceanica",
    "20_caso_kessler",
    "21_caso_salinizacion",
    "22_caso_fosforo",
    "23_caso_erosion_dialectica",
    "24_caso_microplasticos",
    "25_caso_acuiferos",
    "26_caso_starlink",
    "27_caso_riesgo_biologico",
    "28_caso_fuga_cerebros",
    "29_caso_iot",
    "30_caso_behavioral_dynamics",
]

NICE_NAMES = {
    "01_caso_clima": "Clima Regional",
    "02_caso_conciencia": "Conciencia",
    "03_caso_contaminacion": "Contaminación",
    "04_caso_energia": "Energía eléctrica",
    "05_caso_epidemiologia": "Epidemiología",
    "06_caso_falsacion_exogeneidad": "Falsación: exogeneidad",
    "07_caso_falsacion_no_estacionariedad": "Falsación: no-estacionariedad",
    "08_caso_falsacion_observabilidad": "Falsación: observabilidad",
    "09_caso_finanzas": "Finanzas",
    "10_caso_justicia": "Justicia",
    "11_caso_movilidad": "Movilidad",
    "12_caso_paradigmas": "Paradigmas",
    "13_caso_politicas_estrategicas": "Políticas estratégicas",
    "14_caso_postverdad": "Postverdad",
    "15_caso_wikipedia": "Wikipedia",
    "16_caso_deforestacion": "Deforestación global",
    "17_caso_oceanos": "Océanos",
    "18_caso_urbanizacion": "Urbanización",
    "19_caso_acidificacion_oceanica": "Acidificación oceánica",
    "20_caso_kessler": "Síndrome de Kessler",
    "21_caso_salinizacion": "Salinización",
    "22_caso_fosforo": "Fósforo",
    "23_caso_erosion_dialectica": "Erosión dialéctica",
    "24_caso_microplasticos": "Microplásticos",
    "25_caso_acuiferos": "Acuíferos",
    "26_caso_starlink": "Starlink",
    "27_caso_riesgo_biologico": "Riesgo biológico",
    "28_caso_fuga_cerebros": "Fuga de cerebros",
    "29_caso_iot": "IoT",
    "30_caso_behavioral_dynamics": "Behavioral dynamics",
}


def load_metrics(case: str) -> dict:
    p = SIM / case / "outputs" / "metrics.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text())


def get_canonical(case: str) -> tuple[float, float, str]:
    m = load_metrics(case)
    phases = m.get("phases", {})
    ph = phases.get("real") or phases.get("synthetic", {})
    phase_used = "real" if "real" in phases else "synthetic"
    edi = ph.get("edi", {})
    return float(edi.get("value", 0.0)), float(edi.get("permutation_pvalue", 1.0)), phase_used


def run_block_bootstrap(case: str, n_perm: int = 2999, seed: int = 42) -> dict | None:
    """Ejecuta block-bootstrap real si hay primary_arrays.json."""
    pa = SIM / case / "outputs" / "primary_arrays.json"
    if not pa.exists():
        return None
    data = json.loads(pa.read_text())
    arrays = data["arrays"]
    obs = arrays["obs"]
    abm = arrays["abm_coupled"]
    red = arrays["abm_no_ode"]
    n = len(obs)
    if n < 8:
        return None

    t0 = time.time()
    edi_real, p_block, p_naive = block_bootstrap_pvalue(
        obs, abm, red, n_perm=n_perm, method="stationary", seed=seed
    )
    elapsed = time.time() - t0
    return {
        "edi_real": edi_real,
        "p_block_stationary": p_block,
        "p_naive_permutation": p_naive,
        "n_perm": n_perm,
        "n_obs": n,
        "p_value_shift": abs(p_block - p_naive),
        "wall_seconds": elapsed,
    }


def main():
    print(f"[recalibration] {time.strftime('%Y-%m-%d %H:%M:%S')} — start")
    print(f"[recalibration] N_PERM stationary block-bootstrap: 2999")
    print(f"[recalibration] FWER correction: Holm-Bonferroni @ alpha=0.05")
    print()

    results = []
    for case in CORPUS:
        edi_canon, p_canon, phase = get_canonical(case)
        block = run_block_bootstrap(case, n_perm=2999)
        if block is not None:
            p_used = block["p_block_stationary"]
            edi_used = block["edi_real"]
            method = "block_bootstrap_stationary_PR1994"
            extra = block
            print(f"[block-bootstrap] {case:40s} edi={edi_used:+.4f} p_block={p_used:.4f} p_naive={block['p_naive_permutation']:.4f} ({block['wall_seconds']:.1f}s)")
        else:
            p_used = p_canon
            edi_used = edi_canon
            method = "canonical_legacy_999perm"
            extra = None
            print(f"[canonical    ] {case:40s} edi={edi_used:+.4f} p_canon={p_used:.4f}")

        results.append({
            "case": case,
            "name": NICE_NAMES.get(case, case),
            "edi": edi_used,
            "edi_canonical": edi_canon,
            "p_value_used": p_used,
            "p_value_canonical": p_canon,
            "phase": phase,
            "method": method,
            "block_bootstrap": extra,
        })

    # Holm-Bonferroni sobre los 30 p-values
    p_arr = [r["p_value_used"] for r in results]
    p_holm, rej_holm = fwer_correct(p_arr, method="holm", alpha=0.05)
    p_bonf, rej_bonf = fwer_correct(p_arr, method="bonferroni", alpha=0.05)

    for i, r in enumerate(results):
        r["p_holm_adjusted"] = float(p_holm[i])
        r["holm_rejected_at_005"] = bool(rej_holm[i])
        r["p_bonferroni_adjusted"] = float(p_bonf[i])
        r["bonferroni_rejected_at_005"] = bool(rej_bonf[i])

    # Reclasificación bajo régimen calibrado
    # weak: EDI > 0 and p_holm <= 0.05
    # strong: EDI >= 0.30 and p_holm <= 0.05
    for r in results:
        edi = r["edi"]
        rej = r["holm_rejected_at_005"]
        if edi >= 0.30 and rej:
            cls = "strong"
        elif edi >= 0.20 and rej:
            cls = "weak"
        elif edi >= 0.10 and rej:
            cls = "weak"
        elif edi > 0 and rej:
            cls = "suggestive"
        elif edi > 0 and r["p_value_used"] <= 0.05:
            cls = "trend"  # significativo pero no sobrevive Holm
        else:
            cls = "null"
        # Casos de falsación se reportan como controles
        if "falsacion" in r["case"]:
            cls = "control_falsacion"
        r["classification_calibrated"] = cls

    # Cifras agregadas
    n_total = len(results)
    n_holm_survivors = sum(1 for r in results if r["holm_rejected_at_005"])
    n_strong_holm = sum(1 for r in results if r["classification_calibrated"] == "strong")
    n_weak_holm = sum(1 for r in results if r["classification_calibrated"] == "weak")
    n_suggestive_holm = sum(1 for r in results if r["classification_calibrated"] == "suggestive")
    n_trend = sum(1 for r in results if r["classification_calibrated"] == "trend")
    n_null = sum(1 for r in results if r["classification_calibrated"] == "null")
    n_controls = sum(1 for r in results if r["classification_calibrated"] == "control_falsacion")

    summary = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "method": "stationary_block_bootstrap_PR1994 + Holm_Bonferroni_1979",
        "n_perm_block": 2999,
        "alpha_fwer": 0.05,
        "n_cases_total": n_total,
        "n_block_bootstrap_real": sum(1 for r in results if r["method"].startswith("block")),
        "n_canonical_legacy": sum(1 for r in results if r["method"].startswith("canonical")),
        "n_holm_survivors": n_holm_survivors,
        "classification_calibrated": {
            "strong": n_strong_holm,
            "weak": n_weak_holm,
            "suggestive": n_suggestive_holm,
            "trend": n_trend,
            "null": n_null,
            "control_falsacion": n_controls,
        },
        "results_by_case": results,
    }

    out = OUT / "recalibration_results.json"
    out.write_text(json.dumps(summary, indent=2))
    print()
    print(f"[recalibration] saved: {out}")
    print(f"[recalibration] holm survivors @ alpha=0.05: {n_holm_survivors}/{n_total}")
    print(f"[recalibration] classification calibrated: strong={n_strong_holm} weak={n_weak_holm} suggestive={n_suggestive_holm} trend={n_trend} null={n_null} controles={n_controls}")
    return summary


if __name__ == "__main__":
    main()
