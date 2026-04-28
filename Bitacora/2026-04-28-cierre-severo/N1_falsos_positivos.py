"""N1 — Test masivo de falsos positivos del aparato EDI.

Genera 500 series de RANDOM WALK puro (sin estructura macro genuina).
Aplica el aparato EDI (versión simplificada que reproduce coupled vs no_ode).
Reporta tasa empírica de tipo I al umbral declarado (p < 0.05).

Si la tasa empírica > 5%, el aparato tiene calibración rota y los EDI
positivos del corpus son sospechosos.
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "09-simulaciones-edi" / "common"))


def gen_random_walk(steps: int, sigma: float = 0.3, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    increments = rng.normal(0.0, sigma, size=steps)
    return np.cumsum(increments)


def gen_forcing_neutral(steps: int, seed: int = 1) -> np.ndarray:
    """Forcing neutro: ruido blanco sin estructura."""
    rng = np.random.default_rng(seed)
    return rng.normal(0.0, 0.5, size=steps)


def fit_simple_ar1_coupled(forcing: np.ndarray, train: np.ndarray) -> tuple:
    """Ajusta AR(1) con forcing en train."""
    n = len(train)
    if n < 5:
        return 0.0, 0.0, float(np.mean(train))
    diffs = np.diff(train)
    drives = forcing[:n - 1]
    if np.var(drives) < 1e-9:
        beta = 0.0
    else:
        beta = float(np.cov(diffs, drives)[0, 1] / np.var(drives))
    alpha = 0.5
    target = float(np.mean(train))
    return alpha, beta, target


def predict_coupled(forcing, train_obs, alpha, beta, target, val_steps):
    """Predicción coupled (con forcing)."""
    last = train_obs[-1]
    s = float(last)
    n = len(train_obs)
    pred = np.zeros(val_steps)
    for t in range(val_steps):
        s = (1 - alpha) * s + alpha * target + beta * forcing[n + t]
        pred[t] = s
    return pred


def predict_no_ode(forcing, train_obs, alpha, target, val_steps):
    """Predicción sin acoplamiento al forcing (ablación real)."""
    last = train_obs[-1]
    s = float(last)
    pred = np.zeros(val_steps)
    for t in range(val_steps):
        s = (1 - alpha) * s + alpha * target
        pred[t] = s
    return pred


def rmse(a, b):
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))


def edi_with_permutation(observed, modeled, control, val_steps,
                         n_perm=999, seed=42):
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
    null_edis = np.asarray(null_edis)
    pvalue = float(np.mean(null_edis >= edi)) if edi is not None else 1.0
    return edi, pvalue


def run_one_trial(steps: int, val_steps: int, seed: int):
    forcing = gen_forcing_neutral(steps, seed=seed * 2)
    obs = gen_random_walk(steps, seed=seed * 2 + 1)
    train_n = steps - val_steps
    train_obs = obs[:train_n]
    alpha, beta, target = fit_simple_ar1_coupled(forcing, train_obs)
    coupled = predict_coupled(forcing, train_obs, alpha, beta, target, val_steps)
    no_ode = predict_no_ode(forcing, train_obs, alpha, target, val_steps)
    full_coupled = np.concatenate([train_obs, coupled])
    full_no_ode = np.concatenate([train_obs, no_ode])
    edi, p = edi_with_permutation(obs, full_coupled, full_no_ode, val_steps,
                                   seed=seed)
    return {
        "seed": seed,
        "edi": edi,
        "p_value": p,
        "alpha_fit": alpha,
        "beta_fit": beta,
        "rmse_train_obs_std": float(np.std(train_obs)),
    }


def main():
    print("=== N1 — Test de falsos positivos del aparato EDI ===")
    print("500 random walks puros + AR(1) coupled vs no_ode + permutación 999")
    print()
    n_trials = 500
    steps = 60
    val_steps = 20
    results = []
    for i in range(n_trials):
        try:
            r = run_one_trial(steps, val_steps, seed=i)
            results.append(r)
        except Exception as exc:
            print(f"FAIL trial {i}: {exc}")

    edis = [r["edi"] for r in results if r["edi"] is not None]
    pvals = [r["p_value"] for r in results if r["edi"] is not None]
    edis_arr = np.asarray(edis)
    pvals_arr = np.asarray(pvals)

    summary = {
        "n_trials": n_trials,
        "n_valid": len(edis),
        "edi_mean": float(np.mean(edis_arr)),
        "edi_median": float(np.median(edis_arr)),
        "edi_std": float(np.std(edis_arr)),
        "edi_p95": float(np.percentile(edis_arr, 95)),
        "edi_p99": float(np.percentile(edis_arr, 99)),
        "p_value_mean": float(np.mean(pvals_arr)),
        "tipo_I_p_005": float(np.mean(pvals_arr < 0.05)),
        "tipo_I_p_001": float(np.mean(pvals_arr < 0.01)),
        "fraction_edi_above_010": float(np.mean(edis_arr > 0.10)),
        "fraction_edi_above_030": float(np.mean(edis_arr > 0.30)),
        "fraction_edi_positive": float(np.mean(edis_arr > 0)),
    }

    print(f"  n_trials válidos: {summary['n_valid']}/{summary['n_trials']}")
    print(f"  EDI medio bajo nulo: {summary['edi_mean']:+.4f} (esperado ≈ 0)")
    print(f"  EDI mediano: {summary['edi_median']:+.4f}")
    print(f"  EDI std: {summary['edi_std']:.4f}")
    print(f"  EDI p95: {summary['edi_p95']:+.4f}")
    print(f"  EDI p99: {summary['edi_p99']:+.4f}")
    print(f"  p-value medio: {summary['p_value_mean']:.4f}")
    print()
    print(f"  Tasa empírica de tipo I (p < 0.05): {summary['tipo_I_p_005']:.4f}")
    print(f"  Esperado al nivel 0.05: ≤ 0.05")
    print(f"  Tasa empírica de tipo I (p < 0.01): {summary['tipo_I_p_001']:.4f}")
    print(f"  Esperado al nivel 0.01: ≤ 0.01")
    print()
    print(f"  Fracción EDI > 0.10 (umbral weak): {summary['fraction_edi_above_010']:.4f}")
    print(f"  Fracción EDI > 0.30 (umbral strong): {summary['fraction_edi_above_030']:.4f}")
    print(f"  Fracción EDI > 0 (señal positiva espuria): {summary['fraction_edi_positive']:.4f}")
    print()

    if summary["tipo_I_p_005"] > 0.07:
        verdict = ("APARATO CON CALIBRACIÓN ROTA: tasa empírica de tipo I "
                   f"({summary['tipo_I_p_005']:.4f}) > 0.07 (umbral declarado 0.05).")
    elif summary["tipo_I_p_005"] <= 0.06:
        verdict = ("Aparato calibrado correctamente: tasa empírica de tipo I "
                   f"({summary['tipo_I_p_005']:.4f}) ≤ 0.06.")
    else:
        verdict = ("Aparato en zona gris: tasa empírica de tipo I "
                   f"({summary['tipo_I_p_005']:.4f}) entre 0.05 y 0.07.")

    if summary["fraction_edi_above_030"] > 0.05:
        verdict += (f" Adicional: {summary['fraction_edi_above_030']:.4f} de "
                    "trials supera 0.30 (umbral strong) bajo nulo. PREOCUPANTE.")

    print(f"  VEREDICTO: {verdict}")

    out_path = Path(__file__).parent / "N1_resultados.json"
    out_path.write_text(json.dumps({
        "summary": summary,
        "verdict": verdict,
        "trials": results
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  Resultados guardados en: {out_path}")


if __name__ == "__main__":
    main()
