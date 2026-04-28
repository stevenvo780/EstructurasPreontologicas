"""Caso 39 — Cefeidas pulsantes (escala 10¹¹ m, 10⁵ s = días).

Sistema: estrella variable Cefeida con pulsación radial.
Variable: magnitud aparente.
Sonda: oscilador no-lineal con relación período-luminosidad (Leavitt 1912).
Forcing: fase del ciclo de pulsación.
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_cepheid(n_steps: int = 300, seed: int = 42):
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps) * 0.1  # días
    period = 5.0  # días
    phase = (t % period) / period
    # asimetría típica de Cefeidas (más rápido en bajada)
    signal = -0.4 * np.sin(2 * np.pi * phase) - 0.1 * np.sin(4 * np.pi * phase)
    M_mean = 12.0  # magnitud media
    mag = M_mean + signal + rng.normal(0, 0.02, n_steps)
    return mag, phase


def sonda_pulsation_coupled(forcing, train_obs, train_steps, val_steps):
    pred = np.zeros(val_steps)
    M_mean = float(np.mean(train_obs))
    for i in range(val_steps):
        phase = forcing[train_steps + i]
        signal = -0.4 * np.sin(2 * np.pi * phase) - 0.1 * np.sin(4 * np.pi * phase)
        pred[i] = M_mean + signal
    return pred


def sonda_const(forcing, train_obs, train_steps, val_steps):
    return np.full(val_steps, float(np.mean(train_obs)))


def main():
    print("=== Caso 39 — Cefeidas pulsantes (escala astrofísica) ===")
    obs, forcing = gen_cepheid(seed=42)
    result = run_edi(
        case_name="Cefeida pulsante",
        scale="astrofísica (10¹¹ m, 10⁵ s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_pulsation_coupled,
        sonda_no_ode=sonda_const,
        notes="Modelo Leavitt P-L, parámetros típicos OGLE survey"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
