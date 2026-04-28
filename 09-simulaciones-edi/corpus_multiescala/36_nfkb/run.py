"""Caso 36 — Oscilaciones NF-κB (escala 10⁻⁵ m, 10²-10³ s).

Sistema: oscilaciones nucleares de NF-κB en respuesta a TNF.
Variable: concentración nuclear NF-κB.
Sonda: modelo Hoffmann reducido (NF-κB / IκBα feedback).
Forcing: pulsos de TNF.
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from edi_engine import run_edi, save_result


def gen_nfkb(n_steps: int = 300, seed: int = 42):
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    tnf = 0.0 * np.ones(n_steps)
    tnf[50:] = 1.0
    tnf[150:160] = 0.0
    tnf = tnf + rng.normal(0, 0.02, n_steps)
    nfkb_n = np.zeros(n_steps)
    ikb = np.zeros(n_steps)
    nfkb_n[0] = 0.1
    ikb[0] = 1.0
    dt = 0.1
    for i in range(1, n_steps):
        kdeg = 0.5 * tnf[i - 1]
        ksyn = 1.0 * nfkb_n[i - 1]
        dnfkb = (kdeg * ikb[i - 1]) - 0.3 * nfkb_n[i - 1]
        dikb = ksyn - kdeg * ikb[i - 1] - 0.05 * ikb[i - 1]
        nfkb_n[i] = max(0, nfkb_n[i - 1] + dnfkb * dt + rng.normal(0, 0.005))
        ikb[i] = max(0, ikb[i - 1] + dikb * dt + rng.normal(0, 0.005))
    return nfkb_n, tnf


def sonda_hoffmann_coupled(forcing, train_obs, train_steps, val_steps):
    pred = np.zeros(val_steps)
    nfkb = float(train_obs[-1])
    ikb = 1.0
    dt = 0.1
    for i in range(val_steps):
        tnf = forcing[train_steps + i]
        kdeg = 0.5 * tnf
        ksyn = 1.0 * nfkb
        dn = kdeg * ikb - 0.3 * nfkb
        di = ksyn - kdeg * ikb - 0.05 * ikb
        nfkb = max(0, nfkb + dn * dt)
        ikb = max(0, ikb + di * dt)
        pred[i] = nfkb
    return pred


def sonda_no_tnf(forcing, train_obs, train_steps, val_steps):
    pred = np.zeros(val_steps)
    nfkb = float(train_obs[-1])
    ikb = 1.0
    dt = 0.1
    tnf = 0.0
    for i in range(val_steps):
        kdeg = 0.5 * tnf
        ksyn = 1.0 * nfkb
        dn = kdeg * ikb - 0.3 * nfkb
        di = ksyn - kdeg * ikb - 0.05 * ikb
        nfkb = max(0, nfkb + dn * dt)
        ikb = max(0, ikb + di * dt)
        pred[i] = nfkb
    return pred


def main():
    print("=== Caso 36 — NF-κB (escala celular, oscilaciones) ===")
    obs, forcing = gen_nfkb(seed=42)
    result = run_edi(
        case_name="Oscilaciones NF-κB",
        scale="celular oscilatoria (10⁻⁵ m, 10²-10³ s)",
        observed=obs, forcing=forcing,
        sonda_coupled=sonda_hoffmann_coupled,
        sonda_no_ode=sonda_no_tnf,
        notes="Hoffmann reducido, parámetros Tay Lab ETH"
    )
    print(f"  EDI = {result.edi:+.4f}, p = {result.p_value:.4f}, "
          f"CI = [{result.ci_95[0]:.3f}, {result.ci_95[1]:.3f}], "
          f"Nivel = {result.nivel}")
    save_result(result, Path(__file__).parent / "outputs")


if __name__ == "__main__":
    main()
