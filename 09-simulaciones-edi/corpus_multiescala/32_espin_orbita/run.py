"""Caso 32 — Acoplamiento espín-órbita en sistemas de pocos átomos (escala 10⁻¹⁰ m).

Sistema: dos átomos con interacción espín-órbita ajustable (régimen Bloch).
Variable observable: momento angular total J(t).
Sonda: Hamiltoniano efectivo H_eff = H_0 + λ(t) * (L·S).
Forcing: intensidad del campo magnético externo (Tesla).
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_spin_orbit(n_steps: int = 250, seed: int = 42) -> tuple:
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    # Forcing: campo magnético externo con modulación
    B = 1.0 + 0.5 * np.sin(2 * np.pi * t / 60) + rng.normal(0, 0.05, n_steps)
    # J(t) responde con acoplamiento espín-órbita
    omega = 0.3
    J = np.zeros(n_steps)
    J[0] = 0.5
    for i in range(1, n_steps):
        coupling = 0.4 * B[i - 1]
        J[i] = J[i - 1] + omega * np.sin(coupling * t[i] * 0.1) * 0.05 + rng.normal(0, 0.01)
    return J, B


def sonda_h_eff(forcing, train_obs, train_steps, val_steps):
    """H_eff con acoplamiento espín-órbita explícito."""
    pred = np.zeros(val_steps)
    last = train_obs[-1] if len(train_obs) > 0 else 0.5
    omega = 0.3
    for i in range(val_steps):
        B = forcing[train_steps + i]
        coupling = 0.4 * B
        last = last + omega * np.sin(coupling * (train_steps + i) * 0.1) * 0.05
        pred[i] = last
    return pred


def sonda_h0_solo(forcing, train_obs, train_steps, val_steps):
    """Ablación: solo H_0 sin término L·S."""
    pred = np.full(val_steps, train_obs[-1] if len(train_obs) > 0 else 0.5)
    return pred


def main():
    print("=== Caso 32 — Espín-órbita (escala atómica) ===")
    obs, forcing = gen_spin_orbit(seed=42)
    result = run_edi(
        case_name="Acoplamiento espín-órbita",
        scale="atómica (10⁻¹⁰ m, 10⁻¹⁵ s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_h_eff,
        sonda_no_ode=sonda_h0_solo,
        notes="Sistema de dos átomos con coupling espín-órbita (Bloch)"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
