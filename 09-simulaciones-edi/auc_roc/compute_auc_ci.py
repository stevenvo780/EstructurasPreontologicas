"""
compute_auc_ci.py — Regenerador autocontenido del AUC-ROC del corpus
inter-dominio y su CI bootstrap estratificado (B=2000, seed=42).

Cierra deuda B-T-NEW-AUC-METH §8 ("script auc_roc_compute.py autocontenido,
no dependiente de Bitacora/, que reciba metrics.json y produzca AUC + CI").

Alcance honesto (CLAUDE.md §4):
  - La cifra AUC=0.886 mide consistencia interna del umbral EDI ≥ 0.33,
    NO discriminación contra un baseline externo. Score y etiqueta son
    funciones del mismo EDI. La comparación contra ARIMA está retirada.
  - El CI bootstrap con n=12 produce [0.66, 1.00]: incertidumbre amplia;
    no se sostienen afirmaciones de superioridad fina contra alternativas
    cuyas AUCs caigan dentro del intervalo.

Comando regenerador (declarado en methodology.md §4):
    python3 09-simulaciones-edi/auc_roc/compute_auc_ci.py --seed 42

Salida (stdout):
    AUC point: 0.8857
    Bootstrap mean: 0.8861
    CI 95% percentile: [0.6571, 1.0000]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


# Datos primarios (lectura literal de N3_auc_roc_discriminacion.py:51-68;
# documentados en auc_roc/methodology.md §2). Mantener como fuente canónica
# hasta que cada metrics.json de los 12 casos exponga campos uniformes.
CASES = [
    ("04_caso_energia",          0.6503, 1),
    ("16_caso_deforestacion",    0.5802, 1),
    ("20_caso_kessler",          0.3527, 1),
    ("27_caso_riesgo_biologico", 0.3326, 1),
    ("24_caso_microplasticos",   0.7819, 1),
    ("06_falsacion_exo",         0.0551, 0),
    ("07_falsacion_ns",         -0.8819, 0),
    ("08_falsacion_obs",        -1.0000, 0),
    ("01_clima",                 0.0111, 0),
    ("10_justicia",              0.2274, 0),
    ("26_starlink",              0.6892, 0),  # EDI alto + gate=false → null
    ("28_fuga_cerebros",         0.0249, 0),
]


def auc_roc(scores: np.ndarray, labels: np.ndarray) -> float:
    """
    AUC-ROC vía Mann-Whitney U (equivalente a trapecio sobre TPR/FPR sin empates).

    Implementación manual idéntica a N3_auc_roc_discriminacion.py:19-42 para
    reproducibilidad bit-a-bit con el cómputo canónico declarado en
    methodology.md §4. No depende de sklearn.
    """
    n = len(scores)
    pos = int(np.sum(labels == 1))
    neg = int(np.sum(labels == 0))
    if pos == 0 or neg == 0:
        return float("nan")
    order = np.argsort(scores, kind="stable")[::-1]
    sl = labels[order]
    tpr_prev = fpr_prev = auc = 0.0
    tp = fp = 0
    for lab in sl:
        if lab == 1:
            tp += 1
        else:
            fp += 1
        tpr = tp / pos
        fpr = fp / neg
        auc += (fpr - fpr_prev) * (tpr + tpr_prev) / 2.0
        tpr_prev, fpr_prev = tpr, fpr
    return float(auc)


def bootstrap_ci_stratified(scores: np.ndarray, labels: np.ndarray,
                             b: int = 2000, seed: int = 42,
                             ci: float = 0.95) -> dict:
    """
    Bootstrap percentile CI estratificado preservando cuentas por clase.
    Convención estándar para AUC sobre muestras pequeñas
    (Carpenter & Bithell 2000, Statistics in Medicine 19:1141-1164).
    """
    rng = np.random.RandomState(seed)
    ip = np.where(labels == 1)[0]
    ineg = np.where(labels == 0)[0]
    aucs = np.empty(b, dtype=np.float64)
    for i in range(b):
        rp = rng.choice(ip, size=len(ip), replace=True)
        rn = rng.choice(ineg, size=len(ineg), replace=True)
        idx = np.concatenate([rp, rn])
        aucs[i] = auc_roc(scores[idx], labels[idx])
    finite = aucs[np.isfinite(aucs)]
    alpha = (1.0 - ci) / 2.0 * 100
    return {
        "n_boot": b,
        "n_finite": int(finite.size),
        "mean": float(np.mean(finite)),
        "ci_lo": float(np.percentile(finite, alpha)),
        "ci_hi": float(np.percentile(finite, 100 - alpha)),
        "samples": aucs,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description="AUC-ROC del corpus + CI bootstrap")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--n-boot", type=int, default=2000)
    ap.add_argument("--ci", type=float, default=0.95)
    ap.add_argument("--out-json", type=str, default=None,
                    help="Si se pasa, escribe resultado en JSON.")
    args = ap.parse_args(argv)

    scores = np.array([c[1] for c in CASES], dtype=np.float64)
    labels = np.array([c[2] for c in CASES], dtype=np.int64)

    point = auc_roc(scores, labels)
    boot = bootstrap_ci_stratified(scores, labels, b=args.n_boot,
                                    seed=args.seed, ci=args.ci)

    print(f"AUC point: {point:.4f}")
    print(f"Bootstrap mean: {boot['mean']:.4f}")
    print(f"CI {int(args.ci*100)}% percentile: "
          f"[{boot['ci_lo']:.4f}, {boot['ci_hi']:.4f}]")
    print(f"  n={len(scores)}  pos={int(labels.sum())}  neg={int((labels==0).sum())}")
    print(f"  bootstrap: B={boot['n_boot']}, seed={args.seed}, "
          f"finite_replicas={boot['n_finite']}")

    if args.out_json:
        out = {
            "auc_point": point,
            "bootstrap": {k: v for k, v in boot.items() if k != "samples"},
            "config": {"seed": args.seed, "n_boot": args.n_boot, "ci": args.ci},
            "cases": [{"case": c[0], "edi": c[1], "label_strong": c[2]}
                      for c in CASES],
            "note": ("AUC mide consistencia umbral interna, NO discriminación "
                     "externa. Comparación contra ARIMA retirada. Ver "
                     "09-simulaciones-edi/auc_roc/methodology.md."),
        }
        Path(args.out_json).write_text(json.dumps(out, indent=2))
        print(f"  → JSON escrito en {args.out_json}")


if __name__ == "__main__":
    main()
