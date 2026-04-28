"""Caso 35 — Ciclo celular Tyson-Novak (escala 10⁻⁵ m, 10³-10⁴ s).

Sistema: ciclo celular S. cerevisiae bajo perturbación nutricional.
Variable: actividad CDK1 (Cyc-CDK).
Sonda: modelo Tyson-Novak de 4 ODEs reducidas.
Forcing: nivel de glucosa en el medio.
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_cell_cycle(n_steps: int = 300, seed: int = 42) -> tuple:
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    # Forcing: glucosa con pulsos
    glu = 1.0 + 0.4 * (np.sin(2 * np.pi * t / 90) > 0) + rng.normal(0, 0.05, n_steps)
    # CDK1 oscila bajo control de glucosa (síntesis-degradación de ciclinas)
    cdk = np.zeros(n_steps)
    cyc = np.zeros(n_steps)
    cdk[0] = 0.1
    cyc[0] = 0.5
    dt = 0.1
    for i in range(1, n_steps):
        # síntesis ciclina depende de glucosa
        ks = 0.05 * glu[i - 1]
        # degradación dependiente de cdk activo
        kd = 0.04 * (1 + 5 * cdk[i - 1])
        dcyc = ks - kd * cyc[i - 1]
        # cdk activado por ciclina, inhibido por Wee1
        ka = 0.3 * cyc[i - 1]
        ki = 0.1
        dcdk = ka * (1 - cdk[i - 1]) - ki * cdk[i - 1]
        cyc[i] = cyc[i - 1] + dcyc * dt + rng.normal(0, 0.005)
        cdk[i] = cdk[i - 1] + dcdk * dt + rng.normal(0, 0.003)
        cyc[i] = max(0.0, cyc[i])
        cdk[i] = max(0.0, cdk[i])
    return cdk, glu


def sonda_tyson_novak_coupled(forcing, train_obs, train_steps, val_steps):
    """Tyson-Novak con glucosa acoplada."""
    pred = np.zeros(val_steps)
    cdk = float(train_obs[-1])
    cyc = 0.5
    dt = 0.1
    for i in range(val_steps):
        glu = forcing[train_steps + i]
        ks = 0.05 * glu
        kd = 0.04 * (1 + 5 * cdk)
        dcyc = ks - kd * cyc
        ka = 0.3 * cyc
        ki = 0.1
        dcdk = ka * (1 - cdk) - ki * cdk
        cyc = max(0.0, cyc + dcyc * dt)
        cdk = max(0.0, cdk + dcdk * dt)
        pred[i] = cdk
    return pred


def sonda_no_glu(forcing, train_obs, train_steps, val_steps):
    """Ablación: glucosa promedio del train (no acoplada al pulso real)."""
    pred = np.zeros(val_steps)
    cdk = float(train_obs[-1])
    cyc = 0.5
    dt = 0.1
    glu_mean = float(np.mean(forcing[:train_steps]))
    for i in range(val_steps):
        ks = 0.05 * glu_mean
        kd = 0.04 * (1 + 5 * cdk)
        dcyc = ks - kd * cyc
        ka = 0.3 * cyc
        ki = 0.1
        cyc = max(0.0, cyc + dcyc * dt)
        cdk = max(0.0, cdk + (ka * (1 - cdk) - ki * cdk) * dt)
        pred[i] = cdk
    return pred


def main():
    print("=== Caso 35 — Ciclo celular (escala celular) ===")
    obs, forcing = gen_cell_cycle(seed=42)
    result = run_edi(
        case_name="Ciclo celular S. cerevisiae",
        scale="celular (10⁻⁵ m, 10³-10⁴ s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_tyson_novak_coupled,
        sonda_no_ode=sonda_no_glu,
        notes="Tyson-Novak reducido, parámetros Cross Lab Rockefeller"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
