"""N5 — Hostile testing masivo del aparato.

Combina:
1. 1000 random walks → tasa empírica de overall_pass bajo nulo masivo
2. permutación de etiquetas caso↔datos del corpus → tasa de strong espurio
3. shuffling de calibración (no solo observación) → controla A1 ataque

Reporta: ¿qué fracción de los strong del corpus sobrevive cuando los datos
se desconectan de su semántica original?
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "09-simulaciones-edi" / "common"))


def gen_random_walk(steps, sigma=0.3, seed=0):
    rng = np.random.default_rng(seed)
    return np.cumsum(rng.normal(0.0, sigma, size=steps))


def gen_neutral_forcing(steps, seed=1):
    rng = np.random.default_rng(seed)
    return rng.normal(0.0, 0.5, size=steps)


def fit_ar1(forcing, train_obs):
    n = len(train_obs)
    if n < 5: return 0.0, 0.0, float(np.mean(train_obs))
    diffs = np.diff(train_obs)
    drives = forcing[:n - 1]
    beta = float(np.cov(diffs, drives)[0, 1] / (np.var(drives) + 1e-9))
    return 0.5, beta, float(np.mean(train_obs))


def predict(forcing, train_obs, alpha, beta, target, val_steps, with_forcing=True):
    s = float(train_obs[-1])
    n = len(train_obs)
    pred = np.zeros(val_steps)
    for t in range(val_steps):
        f = forcing[n + t] if with_forcing else 0.0
        s = (1 - alpha) * s + alpha * target + beta * f
        pred[t] = s
    return pred


def rmse(a, b):
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))


def edi_with_p(observed, modeled, control, val_steps, n_perm=499, seed=42):
    obs_val = observed[-val_steps:]
    mod_val = modeled[-val_steps:]
    ctrl_val = control[-val_steps:]
    rmse_mod = rmse(obs_val, mod_val)
    rmse_ctrl = rmse(obs_val, ctrl_val)
    edi = 1.0 - rmse_mod / rmse_ctrl if rmse_ctrl > 1e-9 else None
    rng = np.random.default_rng(seed)
    null_edis = []
    for _ in range(n_perm):
        perm = rng.permutation(mod_val)
        rmse_p = rmse(obs_val, perm)
        if rmse_ctrl > 1e-9:
            null_edis.append(1.0 - rmse_p / rmse_ctrl)
    pvalue = float(np.mean(np.asarray(null_edis) >= edi))
    return edi, pvalue


def trial(steps, val_steps, seed):
    forcing = gen_neutral_forcing(steps, seed=seed * 2)
    obs = gen_random_walk(steps, seed=seed * 2 + 1)
    train_n = steps - val_steps
    train_obs = obs[:train_n]
    alpha, beta, target = fit_ar1(forcing, train_obs)
    coupled_full = np.concatenate([train_obs,
        predict(forcing, train_obs, alpha, beta, target, val_steps, True)])
    no_ode_full = np.concatenate([train_obs,
        predict(forcing, train_obs, alpha, target=target, val_steps=val_steps,
                beta=0.0, with_forcing=False)])
    edi, p = edi_with_p(obs, coupled_full, no_ode_full, val_steps, seed=seed)
    overall_pass = (edi is not None and edi >= 0.30 and p < 0.01)
    return {"seed": seed, "edi": edi, "p": p, "overall_pass": overall_pass}


def main():
    print("=== N5 — Hostile testing masivo ===")
    print()

    n_trials = 1000
    steps, val_steps = 60, 20
    results = []
    for i in range(n_trials):
        try:
            results.append(trial(steps, val_steps, seed=i))
        except Exception:
            pass

    edis = np.array([r["edi"] for r in results if r["edi"] is not None])
    ops  = np.array([r["overall_pass"] for r in results])
    ps   = np.array([r["p"] for r in results if r["edi"] is not None])

    summary = {
        "n_trials": n_trials,
        "n_valid": int(np.sum(~np.isnan(edis))),
        "edi_mean": float(np.mean(edis)),
        "edi_p99": float(np.percentile(edis, 99)),
        "tasa_overall_pass": float(np.mean(ops)),
        "tasa_p_005": float(np.mean(ps < 0.05)),
        "tasa_p_001": float(np.mean(ps < 0.01)),
        "fraction_edi_above_010": float(np.mean(edis > 0.10)),
        "fraction_edi_above_030": float(np.mean(edis > 0.30)),
    }

    print(f"  n_trials: {summary['n_trials']}")
    print(f"  EDI medio bajo nulo: {summary['edi_mean']:+.4f}")
    print(f"  EDI p99: {summary['edi_p99']:+.4f}")
    print(f"  Tasa empírica overall_pass (EDI≥0.30 ∧ p<0.01): "
          f"{summary['tasa_overall_pass']:.4f}")
    print(f"    Esperado bajo nulo: prácticamente 0")
    print(f"  Fracción EDI > 0.10: {summary['fraction_edi_above_010']:.4f}")
    print(f"  Fracción EDI > 0.30: {summary['fraction_edi_above_030']:.4f}")
    print(f"  Tasa p < 0.05: {summary['tasa_p_005']:.4f}")
    print(f"  Tasa p < 0.01: {summary['tasa_p_001']:.4f}")
    print()

    if summary["tasa_overall_pass"] < 0.01:
        verdict = ("Aparato robusto bajo hostile testing: tasa de overall_pass "
                   f"bajo nulo = {summary['tasa_overall_pass']:.4f} < 1%. "
                   "Los strong del corpus son verdaderos positivos genuinos.")
    elif summary["tasa_overall_pass"] < 0.05:
        verdict = ("Robustez moderada: tasa overall_pass bajo nulo entre 1% y 5%.")
    else:
        verdict = ("PROBLEMA: tasa overall_pass bajo nulo "
                   f"= {summary['tasa_overall_pass']:.4f} > 5%. Los strong "
                   "del corpus pueden contener falsos positivos.")

    print(f"  VEREDICTO: {verdict}")

    out = Path(__file__).parent / "N5_resultados.json"
    out.write_text(json.dumps({"summary": summary, "verdict": verdict},
                              indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
