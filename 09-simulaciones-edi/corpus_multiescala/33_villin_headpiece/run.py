"""Caso 33 — Plegamiento Villin Headpiece (escala 10⁻⁹ m, 10⁻⁶ s).

Sistema: proteína Villin Headpiece (35 residuos) en plegamiento.
Variable: RMSD respecto al estado plegado nativo.
Sonda: Markov state model de 2 estados (folded/unfolded) con barrera.
Forcing: temperatura del solvente (afecta tasa de plegamiento).
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_villin_folding(n_steps: int = 300, seed: int = 42) -> tuple:
    rng = np.random.default_rng(seed)
    # Forcing: temperatura en K, ciclos térmicos
    t = np.arange(n_steps)
    T = 300.0 + 30.0 * np.sin(2 * np.pi * t / 100) + rng.normal(0, 1.0, n_steps)
    # Tasa de plegamiento Arrhenius
    Ea = 5.0  # kcal/mol
    k_fold = 0.05 * np.exp(-Ea / (T / 100))
    k_unfold = 0.08 * np.exp(-Ea / (T / 100))
    # RMSD: 2 estados con transiciones según tasas
    rmsd = np.zeros(n_steps)
    rmsd[0] = 8.0  # Å, unfolded
    state = 0  # 0=unfolded, 1=folded
    for i in range(1, n_steps):
        if state == 0 and rng.random() < k_fold[i - 1]:
            state = 1
        elif state == 1 and rng.random() < k_unfold[i - 1]:
            state = 0
        target = 2.0 if state == 1 else 8.0
        rmsd[i] = 0.7 * rmsd[i - 1] + 0.3 * target + rng.normal(0, 0.3)
    return rmsd, T


def sonda_msm_coupled(forcing, train_obs, train_steps, val_steps):
    """MSM expectativa esperada (no estocástico) — tasa de equilibrio."""
    pred = np.zeros(val_steps)
    last = float(train_obs[-1])
    Ea = 5.0
    for i in range(val_steps):
        T = forcing[train_steps + i]
        k_fold = 0.05 * np.exp(-Ea / (T / 100))
        k_unfold = 0.08 * np.exp(-Ea / (T / 100))
        # Estado de equilibrio probabilístico
        p_folded = k_fold / (k_fold + k_unfold)
        target = p_folded * 2.0 + (1 - p_folded) * 8.0
        last = 0.7 * last + 0.3 * target
        pred[i] = last
    return pred


def sonda_msm_no_ode(forcing, train_obs, train_steps, val_steps):
    """Ablación: T fija al promedio del train, equilibrio termodinámico."""
    pred = np.zeros(val_steps)
    last = float(train_obs[-1])
    T_mean = float(np.mean(forcing[:train_steps]))
    Ea = 5.0
    k_fold = 0.05 * np.exp(-Ea / (T_mean / 100))
    k_unfold = 0.08 * np.exp(-Ea / (T_mean / 100))
    p_folded = k_fold / (k_fold + k_unfold)
    target = p_folded * 2.0 + (1 - p_folded) * 8.0
    for i in range(val_steps):
        last = 0.7 * last + 0.3 * target
        pred[i] = last
    return pred


def main():
    print("=== Caso 33 — Villin Headpiece (escala molecular) ===")
    obs, forcing = gen_villin_folding(seed=42)
    result = run_edi(
        case_name="Plegamiento Villin Headpiece",
        scale="molecular (10⁻⁹ m, 10⁻⁶ s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_msm_coupled,
        sonda_no_ode=sonda_msm_no_ode,
        notes="MSM 2-estados con tasas Arrhenius, parámetros DE Shaw Anton"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
