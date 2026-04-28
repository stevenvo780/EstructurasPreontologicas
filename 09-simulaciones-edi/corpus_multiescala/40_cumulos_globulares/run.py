"""Caso 40 — Dinámica de cúmulos globulares (escala 10¹⁷-10²⁰ m, 10¹⁴ s).

Sistema: cúmulo globular bajo equilibrio gravitacional.
Variable: dispersión de velocidades estelares σ_v (km/s).
Sonda: modelo Plummer reducido con potencial autoconsistente.
Forcing: distancia al centro galáctico (afecta marea).
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_globular_cluster(n_steps: int = 250, seed: int = 42):
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    # Forcing: distancia al centro galáctico (kpc), oscila por órbita
    d_gal = 5.0 + 2.0 * np.sin(2 * np.pi * t / 80) + rng.normal(0, 0.1, n_steps)
    d_gal = np.maximum(d_gal, 1.0)
    # σ_v sigue Plummer con corrección por marea
    M_cluster = 1e5  # M_sol
    r_h = 5.0  # pc, radio medio
    # Plummer: σ² ∝ GM/r_h * f(d_gal)
    sigma_v_base = np.sqrt(M_cluster / r_h * 0.001)  # km/s
    tidal_factor = (5.0 / d_gal) ** 0.3  # marea más fuerte cerca del centro
    sigma_v = sigma_v_base * tidal_factor + rng.normal(0, 0.3, n_steps)
    sigma_v = np.maximum(sigma_v, 0.5)
    return sigma_v, d_gal


def sonda_plummer_coupled(forcing, train_obs, train_steps, val_steps):
    pred = np.zeros(val_steps)
    sigma_base = float(np.mean(train_obs)) * (np.mean(forcing[:train_steps]) / 5.0) ** 0.3
    for i in range(val_steps):
        d = forcing[train_steps + i]
        tidal = (5.0 / d) ** 0.3
        pred[i] = sigma_base / (np.mean(forcing[:train_steps]) / 5.0) ** 0.3 * tidal
    return pred


def sonda_const(forcing, train_obs, train_steps, val_steps):
    return np.full(val_steps, float(np.mean(train_obs)))


def main():
    print("=== Caso 40 — Cúmulo globular (escala astrofísica grande) ===")
    obs, forcing = gen_globular_cluster(seed=42)
    result = run_edi(
        case_name="Cúmulo globular Plummer",
        scale="astrofísica grande (10¹⁷-10²⁰ m, 10¹⁴ s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_plummer_coupled,
        sonda_no_ode=sonda_const,
        notes="Plummer con marea galáctica, parámetros típicos Gaia DR3"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
