"""N3 — AUC-ROC de discriminación strong vs null: EDI vs ARIMA-RMSE.

El aparato afirma que su valor diferencial es DISCRIMINACIÓN, no predicción.
Aquí lo medimos: ¿clasifica EDI los casos strong/null del corpus mejor
que un ARIMA-RMSE simple?

Toma los 8 casos del baselines anterior (5 strong + 3 falsación) +
los nulls del corpus completo. Computa AUC-ROC para cada métrica como
clasificador binario strong vs no-strong.
"""

from __future__ import annotations
import json
from pathlib import Path
import numpy as np

REPO = Path(__file__).resolve().parents[2]


def auc_roc(scores: np.ndarray, labels: np.ndarray) -> float:
    """Área bajo curva ROC manual (sin sklearn por simplicidad)."""
    n = len(scores)
    pos = np.sum(labels == 1)
    neg = np.sum(labels == 0)
    if pos == 0 or neg == 0:
        return float("nan")
    # ranking
    order = np.argsort(scores)[::-1]  # mayor score = clase positiva
    sorted_labels = labels[order]
    tpr_prev = 0.0
    fpr_prev = 0.0
    auc = 0.0
    tp = 0
    fp = 0
    for lab in sorted_labels:
        if lab == 1:
            tp += 1
        else:
            fp += 1
        tpr = tp / pos
        fpr = fp / neg
        auc += (fpr - fpr_prev) * (tpr + tpr_prev) / 2
        tpr_prev, fpr_prev = tpr, fpr
    return float(auc)


def main():
    print("=== N3 — AUC-ROC discriminación strong vs no-strong ===")
    print()

    cases = {
        "04_caso_energia": {"edi": 0.6503, "label_strong": 1, "rmse_arima": 0.3905, "rmse_rw": 0.5060, "rmse_coupled": 1.5253},
        "16_caso_deforestacion": {"edi": 0.5802, "label_strong": 1, "rmse_arima": 0.0616, "rmse_rw": 0.0435, "rmse_coupled": 0.9330},
        "20_caso_kessler": {"edi": 0.3527, "label_strong": 1, "rmse_arima": 0.4075, "rmse_rw": 0.4316, "rmse_coupled": 0.6723},
        "27_caso_riesgo_biologico": {"edi": 0.3326, "label_strong": 1, "rmse_arima": 0.3328, "rmse_rw": 0.2497, "rmse_coupled": 1.9400},
        "24_caso_microplasticos": {"edi": 0.7819, "label_strong": 1, "rmse_arima": 0.1146, "rmse_rw": 0.1284, "rmse_coupled": 1.4017},
        "06_falsacion_exo": {"edi": 0.0551, "label_strong": 0, "rmse_arima": 0.5150, "rmse_rw": 0.5028, "rmse_coupled": None},
        "07_falsacion_ns": {"edi": -0.8819, "label_strong": 0, "rmse_arima": 0.5150, "rmse_rw": 0.5028, "rmse_coupled": None},
        "08_falsacion_obs": {"edi": -1.0000, "label_strong": 0, "rmse_arima": 0.5150, "rmse_rw": 0.5028, "rmse_coupled": None},
        "01_clima": {"edi": 0.0111, "label_strong": 0, "rmse_arima": None, "rmse_rw": None, "rmse_coupled": None},
        "10_justicia": {"edi": 0.2274, "label_strong": 0, "rmse_arima": None, "rmse_rw": None, "rmse_coupled": None},
        "26_starlink": {"edi": 0.6892, "label_strong": 0, "rmse_arima": None, "rmse_rw": None, "rmse_coupled": None},
        "28_fuga_cerebros": {"edi": 0.0249, "label_strong": 0, "rmse_arima": None, "rmse_rw": None, "rmse_coupled": None},
    }

    keys = list(cases.keys())
    edi_scores = np.array([cases[k]["edi"] for k in keys])
    labels = np.array([cases[k]["label_strong"] for k in keys])

    auc_edi = auc_roc(edi_scores, labels)

    keys_with_arima = [k for k in keys if cases[k]["rmse_arima"] is not None]
    arima_signal = np.array([cases[k]["rmse_rw"] - cases[k]["rmse_arima"]
                             for k in keys_with_arima])
    labels_arima = np.array([cases[k]["label_strong"] for k in keys_with_arima])
    auc_arima = auc_roc(arima_signal, labels_arima)

    rw_minus_arima = np.array([cases[k]["rmse_rw"] / cases[k]["rmse_arima"]
                                for k in keys_with_arima])
    auc_arima_ratio = auc_roc(rw_minus_arima, labels_arima)

    print(f"  Casos totales: {len(keys)} ({sum(labels)} strong, {len(keys) - sum(labels)} no-strong)")
    print()
    print(f"  AUC-ROC con EDI como score: {auc_edi:.4f}")
    print(f"  AUC-ROC con (RMSE_rw - RMSE_arima) como score: {auc_arima:.4f}")
    print(f"  AUC-ROC con (RMSE_rw / RMSE_arima) como score: {auc_arima_ratio:.4f}")
    print()
    print(f"  AUC ideal: 1.0 (separación perfecta)")
    print(f"  AUC random: 0.5")
    print()
    delta = auc_edi - max(auc_arima, auc_arima_ratio)
    print(f"  Diferencia AUC EDI vs mejor ARIMA: {delta:+.4f}")

    if delta >= 0.10:
        verdict = (f"EDI domina en discriminación: AUC EDI ({auc_edi:.3f}) "
                   f"supera mejor ARIMA ({max(auc_arima, auc_arima_ratio):.3f}) "
                   "por al menos 0.10. Valor diferencial confirmado.")
    elif delta >= 0:
        verdict = (f"EDI tiene ventaja marginal en discriminación: "
                   f"AUC EDI = {auc_edi:.3f}, mejor ARIMA = "
                   f"{max(auc_arima, auc_arima_ratio):.3f}. "
                   "Ventaja menor a 0.10; el aparato no es claramente superior.")
    else:
        verdict = (f"ARIMA discrimina MEJOR que EDI: AUC ARIMA = "
                   f"{max(auc_arima, auc_arima_ratio):.3f} > EDI = {auc_edi:.3f}. "
                   "El valor diferencial del aparato no se sostiene en este test.")

    print(f"\n  VEREDICTO: {verdict}")

    out = Path(__file__).parent / "N3_resultados.json"
    out.write_text(json.dumps({
        "auc_edi": auc_edi,
        "auc_arima_diff": auc_arima,
        "auc_arima_ratio": auc_arima_ratio,
        "delta": delta,
        "verdict": verdict,
        "n_strong": int(sum(labels)),
        "n_no_strong": int(len(keys) - sum(labels)),
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Resultados: {out}")


if __name__ == "__main__":
    main()
