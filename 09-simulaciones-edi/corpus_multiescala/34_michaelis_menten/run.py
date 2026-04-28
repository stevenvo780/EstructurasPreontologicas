"""Caso 34 — Cinética enzimática Michaelis-Menten (escala 10⁻⁸ m, 10⁻³ s).

Sistema: enzima β-galactosidasa con sustrato variable.
Variable: tasa de turnover (s⁻¹).
Sonda: ecuación MM v = vmax·[S]/(Km+[S]).
Forcing: concentración de sustrato (mM).
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_michaelis_menten(n_steps: int = 200, seed: int = 42) -> tuple:
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    # Forcing: [S] mM con escalonado experimental
    S = 0.5 + 0.4 * np.abs(np.sin(2 * np.pi * t / 50)) + rng.normal(0, 0.02, n_steps)
    S = np.maximum(S, 0.01)
    # MM: v = vmax * S / (Km + S)
    vmax = 20.0  # s^-1
    Km = 0.3  # mM
    v = vmax * S / (Km + S) + rng.normal(0, 0.4, n_steps)
    return v, S


def sonda_mm_coupled(forcing, train_obs, train_steps, val_steps):
    """MM con vmax y Km estimados de train (Lineweaver-Burk)."""
    train_S = forcing[:train_steps]
    train_v = train_obs
    # Lineweaver-Burk: 1/v = (Km/vmax)*(1/S) + 1/vmax
    inv_S = 1.0 / np.maximum(train_S, 0.01)
    inv_v = 1.0 / np.maximum(train_v, 0.5)
    A = np.vstack([inv_S, np.ones(len(inv_S))]).T
    sol, *_ = np.linalg.lstsq(A, inv_v, rcond=None)
    slope, intercept = sol
    vmax_est = 1.0 / max(intercept, 1e-6)
    Km_est = max(0.01, slope * vmax_est)
    pred = np.zeros(val_steps)
    for i in range(val_steps):
        S = forcing[train_steps + i]
        pred[i] = vmax_est * S / (Km_est + S)
    return pred


def sonda_mm_no_ode(forcing, train_obs, train_steps, val_steps):
    """Ablación: tasa media de train sin acoplamiento a [S]."""
    return np.full(val_steps, float(np.mean(train_obs)))


def main():
    print("=== Caso 34 — Michaelis-Menten (escala bioquímica) ===")
    obs, forcing = gen_michaelis_menten(seed=42)
    result = run_edi(
        case_name="Cinética Michaelis-Menten",
        scale="bioquímica (10⁻⁸ m, 10⁻³ s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_mm_coupled,
        sonda_no_ode=sonda_mm_no_ode,
        notes="β-galactosidasa, parámetros publicados Yang Lab Berkeley"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
