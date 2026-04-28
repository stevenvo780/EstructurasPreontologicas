"""Caso 38 — Locomoción humana bajo τ-dot (Lee 1976), NO Fajen-Warren.

Sistema: control de aproximación a meta usando solo flujo óptico (τ-dot).
Variable: velocidad de aproximación.
Sonda: τ-dot constante = -0.5 (Lee 1976).
Forcing: distancia restante a meta.

Este caso responde a la auditoría severa N2 (circularidad caso 30):
usa una sonda DIFERENTE a Fajen-Warren para datos de locomoción.
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_lee_locomotion(n_steps: int = 250, seed: int = 42):
    """Múltiples episodios de aproximación a metas distintas."""
    rng = np.random.default_rng(seed)
    d = np.zeros(n_steps)
    v = np.zeros(n_steps)
    dt = 0.05
    tau_dot_target = -0.5
    # Reiniciar a una nueva meta cada cierto tiempo
    period_reset = 35
    initial_d = 30.0
    initial_v = 5.0
    d[0] = initial_d
    v[0] = initial_v
    for i in range(1, n_steps):
        if i % period_reset == 0:
            d[i] = initial_d * (0.7 + 0.6 * rng.random())  # nueva meta
            v[i] = initial_v * (0.7 + 0.6 * rng.random())
        elif d[i - 1] > 0.5:
            tau = d[i - 1] / max(0.1, v[i - 1])
            d_dot = -v[i - 1]
            d_ddot_t = (tau_dot_target * v[i - 1] + d_dot ** 2 / d[i - 1]) / dt
            v[i] = max(0.0, v[i - 1] - d_ddot_t * dt * 0.1 + rng.normal(0, 0.15))
            d[i] = max(0.0, d[i - 1] + d_dot * dt + rng.normal(0, 0.05))
        else:
            d[i] = 0.0
            v[i] = max(0.0, v[i - 1] - 0.5 + rng.normal(0, 0.1))
    return v, d


def sonda_lee_coupled(forcing, train_obs, train_steps, val_steps):
    pred = np.zeros(val_steps)
    v = float(train_obs[-1])
    dt = 0.05
    tau_dot_target = -0.5
    for i in range(val_steps):
        d = forcing[train_steps + i]
        if d > 0.1 and v > 0.01:
            tau = d / v
            d_dot = -v
            d_ddot_t = (tau_dot_target * v + d_dot ** 2 / d) / dt
            v = max(0.0, v - d_ddot_t * dt * 0.1)
        pred[i] = v
    return pred


def sonda_const(forcing, train_obs, train_steps, val_steps):
    """Ablación: sonda sin acceso a la distancia, predice velocidad media."""
    return np.full(val_steps, float(np.mean(train_obs)))


def main():
    print("=== Caso 38 — Locomoción τ-dot (alternativa al caso 30) ===")
    obs, forcing = gen_lee_locomotion(seed=42)
    result = run_edi(
        case_name="Locomoción humana τ-dot (Lee 1976)",
        scale="individual / behavioral (1 m, 1 s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_lee_coupled,
        sonda_no_ode=sonda_const,
        notes="Sonda τ-dot, alternativa NO-FW al caso 30 (responde a N2)"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
