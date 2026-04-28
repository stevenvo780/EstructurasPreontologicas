"""N2 — Test de circularidad en caso 30.

Genera 100 series con sistemas dinámicos ALTERNATIVOS (NO Fajen-Warren)
y aplica la sonda behavioral_attractor (segundo orden Fajen-Warren).

Si la sonda detecta cierre (EDI > 0.20) sobre datos no Fajen-Warren,
la sonda solo funciona en su propio dominio generativo y el caso 30
NO demuestra cierre operativo de behavioral dynamics — solo demuestra
auto-consistencia paramétrica.

Sistemas alternativos probados:
  A) Random walk con drift (no atractor)
  B) Mass-spring lineal (otra dinámica de segundo orden, Hogan-style)
  C) AR(2) puro estocástico
  D) Constante con ruido (controlador trivial)
"""

from __future__ import annotations
import json
import sys
import math
from pathlib import Path
import numpy as np

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "09-simulaciones-edi" / "common"))

from ode_models import simulate_ode_model  # noqa: E402


def gen_random_walk(steps: int, sigma: float = 0.4, drift: float = 0.0,
                    seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    inc = rng.normal(drift, sigma, size=steps)
    return np.cumsum(inc)


def gen_mass_spring(steps: int, omega: float = 0.4, damping: float = 0.2,
                    forcing: np.ndarray | None = None, seed: int = 0,
                    noise: float = 0.05) -> np.ndarray:
    """Oscilador armónico amortiguado (no Fajen-Warren)."""
    rng = np.random.default_rng(seed)
    x = 0.0
    v = 0.0
    series = np.zeros(steps)
    dt = 0.1
    for t in range(steps):
        f = forcing[t] if forcing is not None else 0.0
        a = -omega ** 2 * x - damping * v + f * 0.3
        v = v + a * dt + rng.normal(0, noise) * dt
        x = x + v * dt
        series[t] = x
    return series


def gen_ar2(steps: int, phi1: float = 0.6, phi2: float = -0.2,
            sigma: float = 0.3, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    series = np.zeros(steps)
    series[0] = rng.normal(0, sigma)
    series[1] = rng.normal(0, sigma)
    for t in range(2, steps):
        series[t] = phi1 * series[t - 1] + phi2 * series[t - 2] + rng.normal(0, sigma)
    return series


def gen_constant_noise(steps: int, sigma: float = 0.3, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.normal(0, sigma, size=steps)


def gen_forcing_oscillator(steps: int, period: float = 25, amp: float = 0.5,
                           seed: int = 1) -> np.ndarray:
    rng = np.random.default_rng(seed)
    t = np.arange(steps)
    return amp * np.sin(2 * np.pi * t / period) + rng.normal(0, 0.05, size=steps)


def predict_with_fajen_warren(forcing: np.ndarray, train_obs: np.ndarray,
                              steps: int) -> np.ndarray:
    """Aplica behavioral_attractor (Fajen-Warren) como sonda."""
    params = {
        "fw_b": 3.25, "fw_k_g": 7.50, "fw_c1": 0.40, "fw_c2": 0.40,
        "fw_d_g": 4.0, "fw_dt": 0.05,
        "phi0": float(train_obs[0]) if len(train_obs) > 0 else 0.0,
        "phi_dot0": 0.0,
        "model": "behavioral_attractor",
        "ode_key": "y",
        "forcing_series": forcing.tolist(),
    }
    out = simulate_ode_model(params, steps, seed=42)
    return np.asarray(out["y"], dtype=float)


def rmse(a, b):
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))


def edi_test(observed, modeled, control_no_ode):
    rmse_mod = rmse(observed, modeled)
    rmse_ctrl = rmse(observed, control_no_ode)
    return 1.0 - rmse_mod / rmse_ctrl if rmse_ctrl > 1e-9 else None, rmse_mod, rmse_ctrl


def run_trial(generator_name: str, generator_fn, n_trials: int = 100):
    edis = []
    rng_master = np.random.default_rng(123)
    for i in range(n_trials):
        steps = 80
        val_steps = 25
        train_n = steps - val_steps
        forcing = gen_forcing_oscillator(steps, seed=int(rng_master.integers(0, 1e9)))
        try:
            obs = generator_fn(steps, forcing, seed=int(rng_master.integers(0, 1e9)))
        except TypeError:
            obs = generator_fn(steps, seed=int(rng_master.integers(0, 1e9)))
        modeled = predict_with_fajen_warren(forcing, obs[:train_n], steps)
        forcing_zero = np.zeros_like(forcing)
        control = predict_with_fajen_warren(forcing_zero, obs[:train_n], steps)
        edi, rm, rc = edi_test(obs[-val_steps:], modeled[-val_steps:],
                                control[-val_steps:])
        if edi is not None and not np.isnan(edi):
            edis.append(edi)
    edis_arr = np.asarray(edis)
    return {
        "generator": generator_name,
        "n_valid": len(edis),
        "edi_mean": float(np.mean(edis_arr)) if len(edis) else None,
        "edi_median": float(np.median(edis_arr)) if len(edis) else None,
        "edi_std": float(np.std(edis_arr)) if len(edis) else None,
        "edi_p95": float(np.percentile(edis_arr, 95)) if len(edis) else None,
        "fraction_above_010": float(np.mean(edis_arr > 0.10)) if len(edis) else None,
        "fraction_above_020": float(np.mean(edis_arr > 0.20)) if len(edis) else None,
        "fraction_above_030": float(np.mean(edis_arr > 0.30)) if len(edis) else None,
        "fraction_positive": float(np.mean(edis_arr > 0)) if len(edis) else None,
    }


def main():
    print("=== N2 — Circularidad caso 30 ===")
    print("Sonda Fajen-Warren aplicada a sistemas ALTERNATIVOS no-FW")
    print()

    generators = [
        ("random_walk_drift",
         lambda steps, forcing=None, seed=0: gen_random_walk(steps, sigma=0.3, drift=0.05, seed=seed)),
        ("mass_spring_oscilador",
         lambda steps, forcing=None, seed=0: gen_mass_spring(steps, omega=0.4, damping=0.2,
                                                              forcing=forcing, seed=seed)),
        ("ar2_estocastico",
         lambda steps, forcing=None, seed=0: gen_ar2(steps, phi1=0.6, phi2=-0.2, seed=seed)),
        ("constante_ruido",
         lambda steps, forcing=None, seed=0: gen_constant_noise(steps, sigma=0.3, seed=seed)),
    ]

    results = []
    for name, fn in generators:
        r = run_trial(name, fn, n_trials=100)
        results.append(r)
        print(f"  {r['generator']:30s}  n={r['n_valid']:3d}  "
              f"EDI mean={r['edi_mean']:+.4f}  p95={r['edi_p95']:+.4f}  "
              f"frac>0.10={r['fraction_above_010']:.3f}  "
              f"frac>0.30={r['fraction_above_030']:.3f}")

    print()
    referencia_caso30 = 0.2622
    print(f"  Referencia caso 30 publicado: EDI = {referencia_caso30:+.4f}")
    print()

    max_above_020 = max(r["fraction_above_020"] or 0 for r in results)
    max_mean = max(r["edi_mean"] or -1 for r in results)
    if max_above_020 > 0.10:
        verdict = ("CIRCULARIDAD DETECTADA: la sonda Fajen-Warren produce "
                   f"EDI > 0.20 en >10% de trials sobre datos no-FW. "
                   "El caso 30 puede estar midiendo auto-consistencia paramétrica.")
    elif max_mean > 0.10:
        verdict = ("CIRCULARIDAD PARCIAL: EDI medio bajo nulo > 0.10 "
                   "en al menos un generador alternativo. Cautela.")
    elif max_mean > 0.05:
        verdict = ("Sesgo leve detectado: la sonda tiene tendencia "
                   "a producir EDI ligeramente positivo bajo nulo, "
                   "pero por debajo del umbral weak.")
    else:
        verdict = ("La sonda Fajen-Warren produce EDI ≈ 0 sobre datos "
                   "no-FW. El caso 30 publicado (EDI=0.262) no es "
                   "auto-consistencia trivial.")

    print(f"  VEREDICTO: {verdict}")

    out = Path(__file__).parent / "N2_resultados.json"
    out.write_text(json.dumps({
        "results_by_generator": results,
        "verdict": verdict,
        "case30_reference_edi": referencia_caso30,
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  Resultados: {out}")


if __name__ == "__main__":
    main()
