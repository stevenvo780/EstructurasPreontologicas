"""V4-06 — Hostile testing del motor edi_engine bajo random walk masivo.

500 random walks aplicados al motor edi_engine.py con sondas paramétricas
genéricas. Reporta tasa empírica de overall_pass bajo nulo.

Si la tasa > 1%, los strong del corpus multiescala pueden contener falsos
positivos del motor.
"""

from __future__ import annotations
import sys
import json
from pathlib import Path
import numpy as np

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "09-simulaciones-edi" / "corpus_multiescala"))

from edi_engine import run_edi


def gen_random_walk(n_steps, sigma=0.3, seed=0):
    rng = np.random.default_rng(seed)
    return np.cumsum(rng.normal(0.0, sigma, n_steps))


def gen_neutral_forcing(n_steps, seed=1):
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    return 0.5 + 0.3 * np.sin(2 * np.pi * t / 25) + rng.normal(0, 0.05, n_steps)


def sonda_generica_coupled(forcing, train_obs, train_steps, val_steps):
    """Sonda AR(1) genérica con coupling al forcing."""
    n = len(train_obs)
    target = float(np.mean(train_obs))
    diffs = np.diff(train_obs)
    drives = forcing[:n - 1]
    if np.var(drives) < 1e-9:
        beta = 0.0
    else:
        beta = float(np.cov(diffs, drives)[0, 1] / np.var(drives))
    alpha = 0.5
    s = float(train_obs[-1])
    pred = np.zeros(val_steps)
    for i in range(val_steps):
        f = forcing[train_steps + i]
        s = (1 - alpha) * s + alpha * target + beta * f
        pred[i] = s
    return pred


def sonda_generica_no_ode(forcing, train_obs, train_steps, val_steps):
    """Ablación: AR(1) sin coupling al forcing."""
    target = float(np.mean(train_obs))
    alpha = 0.5
    s = float(train_obs[-1])
    pred = np.zeros(val_steps)
    for i in range(val_steps):
        s = (1 - alpha) * s + alpha * target
        pred[i] = s
    return pred


def main():
    print("=== V4-06 — Hostile testing del motor edi_engine ===")
    print("500 random walks bajo motor multiescala con sonda genérica AR(1).")
    print()

    n_trials = 500
    n_steps = 200
    results = []
    for i in range(n_trials):
        try:
            obs = gen_random_walk(n_steps, seed=i * 2)
            forcing = gen_neutral_forcing(n_steps, seed=i * 2 + 1)
            r = run_edi(
                case_name=f"trial_{i}",
                scale="hostile",
                observed=obs,
                forcing=forcing,
                sonda_coupled=sonda_generica_coupled,
                sonda_no_ode=sonda_generica_no_ode,
                seed=i,
            )
            results.append({
                "trial": i,
                "edi": r.edi,
                "p_value": r.p_value,
                "overall_pass": r.overall_pass,
                "nivel": r.nivel,
            })
        except Exception as exc:
            pass

    edis = np.array([r["edi"] for r in results if r["edi"] is not None])
    pvals = np.array([r["p_value"] for r in results if r["edi"] is not None])
    ops = np.array([r["overall_pass"] for r in results])

    summary = {
        "n_trials": n_trials,
        "n_valid": int(np.sum(~np.isnan(edis))),
        "edi_mean": float(np.mean(edis)),
        "edi_p99": float(np.percentile(edis, 99)),
        "edi_max": float(np.max(edis)),
        "tasa_overall_pass": float(np.mean(ops)),
        "tasa_p_005": float(np.mean(pvals < 0.05)),
        "tasa_strong_edi": float(np.mean(edis >= 0.30)),
        "tasa_strong_full": float(np.mean((edis >= 0.30) & (pvals < 0.01))),
    }

    print(f"  n_trials: {summary['n_trials']}")
    print(f"  EDI medio bajo nulo: {summary['edi_mean']:+.4f}")
    print(f"  EDI máx bajo nulo: {summary['edi_max']:+.4f}")
    print(f"  EDI p99: {summary['edi_p99']:+.4f}")
    print(f"  Tasa EDI ≥ 0.30 (umbral strong): {summary['tasa_strong_edi']:.4f}")
    print(f"  Tasa overall_pass (gate completo): {summary['tasa_overall_pass']:.4f}")
    print(f"  Tasa p < 0.05: {summary['tasa_p_005']:.4f}")
    print()

    if summary["tasa_overall_pass"] < 0.01:
        verdict = ("Motor edi_engine ROBUSTO bajo random walk: "
                   f"tasa overall_pass = {summary['tasa_overall_pass']:.4f} < 1%. "
                   "Los strong multiescala son verdaderos positivos genuinos.")
    elif summary["tasa_overall_pass"] < 0.05:
        verdict = (f"Motor moderadamente robusto: tasa overall_pass "
                   f"= {summary['tasa_overall_pass']:.4f}. Cautela.")
    else:
        verdict = (f"PROBLEMA en motor: tasa overall_pass "
                   f"= {summary['tasa_overall_pass']:.4f}. Strong multiescala "
                   "pueden contener falsos positivos.")
    print(f"  VEREDICTO: {verdict}")

    out = Path(__file__).parent / "V4_06_resultados.json"
    out.write_text(json.dumps({"summary": summary, "verdict": verdict},
                              indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
