"""Caso 37 — Variabilidad cardíaca individual bajo estrés (escala 1 m, 1 s).

Sistema: latido cardíaco con regulación autonómica (vagal+simpática).
Variable: intervalos R-R (ms).
Sonda: oscilador no-lineal Mackey-Glass con delay autonómico.
Forcing: nivel de estrés (cortisol/catecolaminas indirecto).
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_hrv(n_steps: int = 250, seed: int = 42):
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    stress = 0.3 + 0.5 * (np.sin(2 * np.pi * t / 70) > 0.5).astype(float) + rng.normal(0, 0.05, n_steps)
    rr = np.zeros(n_steps)
    rr[0] = 800.0
    delay = 5
    for i in range(1, n_steps):
        target = 800 - 200 * stress[i - 1]
        if i > delay:
            modulation = 50 * np.tanh((rr[i - delay] - 800) / 100)
        else:
            modulation = 0
        rr[i] = 0.85 * rr[i - 1] + 0.15 * target - 0.1 * modulation + rng.normal(0, 8.0)
    return rr, stress


def sonda_mackey_glass_coupled(forcing, train_obs, train_steps, val_steps):
    pred = np.zeros(val_steps)
    rr_hist = list(train_obs[-10:])
    delay = 5
    for i in range(val_steps):
        stress = forcing[train_steps + i]
        target = 800 - 200 * stress
        rr_d = rr_hist[-delay] if len(rr_hist) >= delay else 800
        modulation = 50 * np.tanh((rr_d - 800) / 100)
        rr_new = 0.85 * rr_hist[-1] + 0.15 * target - 0.1 * modulation
        rr_hist.append(rr_new)
        pred[i] = rr_new
    return pred


def sonda_no_stress(forcing, train_obs, train_steps, val_steps):
    pred = np.zeros(val_steps)
    rr_hist = list(train_obs[-10:])
    delay = 5
    target = 800 - 200 * 0.5  # stress promedio
    for i in range(val_steps):
        rr_d = rr_hist[-delay] if len(rr_hist) >= delay else 800
        modulation = 50 * np.tanh((rr_d - 800) / 100)
        rr_new = 0.85 * rr_hist[-1] + 0.15 * target - 0.1 * modulation
        rr_hist.append(rr_new)
        pred[i] = rr_new
    return pred


def main():
    print("=== Caso 37 — HRV cardíaco individual (escala individual) ===")
    obs, forcing = gen_hrv(seed=42)
    result = run_edi(
        case_name="Variabilidad cardíaca bajo estrés",
        scale="individual (1 m, 1 s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_mackey_glass_coupled,
        sonda_no_ode=sonda_no_stress,
        notes="Mackey-Glass con delay, parámetros PhysioNet"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
