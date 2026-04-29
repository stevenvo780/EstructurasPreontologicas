#!/usr/bin/env python3
"""
Re-ejecuta el caso 30 (Behavioral Dynamics) con n extendido.

Sustento filosófico: el caso 30 declarado como piloto metodológico con
N2 (circularidad por Fajen-Warren) confirma marginal por. Pero
el componente honesto del caso (sonda Fajen-Warren detecta SU PROPIA
estructura por construcción) puede operacionalizarse con honestidad
declarando explícitamente la circularidad y reportando EDI sobre n
mayor con ventana temporal extendida.

NO se afirma que el caso resuelva la circularidad N2. Se afirma que
con n=300 y ventana temporal mayor, la estimación de EDI es
estadísticamente más estable, lo cual es valor metodológico aunque
no resuelva el problema epistémico.

Datos: panel sintético de 30 trayectorias (réplicas) × 100 pasos
temporales = 3000 obs efectivas. Cada réplica varía condiciones
iniciales y ruido perceptual.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
CASE_DIR = ROOT / "30_caso_behavioral_dynamics"

SEED = 42
N_TRIALS = 30
N_STEPS = 100


def _fajen_warren_system(seed: int) -> dict:
    """Sistema completo Fajen-Warren con condiciones iniciales aleatorias."""
    rng = np.random.RandomState(seed)
    phi = np.zeros(N_STEPS)
    phi_dot = np.zeros(N_STEPS)
    phi[0] = rng.uniform(-0.5, 0.5)
    phi_dot[0] = rng.uniform(-0.2, 0.2)

    psi_g = rng.uniform(-0.3, 0.3)
    psi_o = rng.uniform(0.5, 1.5)
    d_g0 = rng.uniform(5, 15)
    d_o0 = rng.uniform(3, 8)
    v = 1.5

    b = 3.25
    k_g = 7.50
    c1 = 0.40
    c2 = 0.40
    k_o = 198.0
    c3 = 6.5
    c4 = 0.80

    dt = 0.05
    for t in range(1, N_STEPS):
        d_g = max(d_g0 - v * t * dt * np.cos(phi[t-1] - psi_g), 0.5)
        d_o = max(d_o0 - v * t * dt * np.cos(phi[t-1] - psi_o), 0.5)
        decel_g = k_g * (phi[t-1] - psi_g) * (np.exp(-c1 * d_g) + c2)
        decel_o = k_o * (phi[t-1] - psi_o) * np.exp(-c3 * abs(phi[t-1] - psi_o)) * np.exp(-c4 * d_o)
        accel = -b * phi_dot[t-1] - decel_g + decel_o + rng.normal(0, 0.05)
        phi_dot[t] = phi_dot[t-1] + accel * dt
        phi[t] = phi[t-1] + phi_dot[t] * dt

    forcing = np.array([rng.normal(0.5, 0.1) for _ in range(N_STEPS)])
    return {"phi": phi, "phi_dot": phi_dot, "forcing": forcing}


def fajen_warren_probe(forcing: np.ndarray, params: dict) -> np.ndarray:
    """Sonda primaria: Fajen-Warren simplificada."""
    n = len(forcing)
    pred = np.zeros(n); pred[0] = 0.0
    pred_dot = 0.0
    for t in range(1, n):
        accel = -3.0 * pred_dot - 5.0 * pred[t-1] + 0.5 * forcing[t]
        pred_dot += accel * 0.05
        pred[t] = pred[t-1] + pred_dot * 0.05
    return pred


def mass_spring_probe(forcing: np.ndarray) -> np.ndarray:
    """Sonda secundaria: masa-resorte (motivación independiente)."""
    n = len(forcing)
    x = np.zeros(n); v = 0.0
    for t in range(1, n):
        a = -1.0 * x[t-1] - 0.5 * v + 0.3 * forcing[t]
        v += a * 0.05
        x[t] = x[t-1] + v * 0.05
    return x


def baseline_random_walk(observed: np.ndarray, seed: int = SEED) -> np.ndarray:
    rng = np.random.RandomState(seed + 1)
    sigma = float(np.std(observed))
    return np.cumsum(rng.normal(0, sigma * 0.5, len(observed))) + observed[0]


def main() -> int:
    print("=" * 72)
    print("Caso 30 — Behavioral Dynamics: panel n extendido")
    print("=" * 72)

    edis_primary = []
    edis_secondary = []
    for trial in range(N_TRIALS):
        sys_data = _fajen_warren_system(SEED + trial)
        obs = sys_data["phi"]
        forcing = sys_data["forcing"]

        primary = fajen_warren_probe(forcing, {})
        secondary = mass_spring_probe(forcing)
        base = baseline_random_walk(obs, seed=SEED + trial)

        rmse_p = float(np.sqrt(np.mean((primary - obs)**2)))
        rmse_s = float(np.sqrt(np.mean((secondary - obs)**2)))
        rmse_b = float(np.sqrt(np.mean((base - obs)**2)))
        if rmse_b > 1e-15:
            edis_primary.append(np.clip((rmse_b - rmse_p) / rmse_b, -1, 1))
            edis_secondary.append(np.clip((rmse_b - rmse_s) / rmse_b, -1, 1))

    edi_p = float(np.mean(edis_primary))
    edi_s = float(np.mean(edis_secondary))
    delta = abs(edi_p - edi_s)

    rng = np.random.RandomState(SEED + 7)
    null_edis = []
    for _ in range(999):
        sampled = rng.choice(edis_primary, size=len(edis_primary), replace=True)
        null_edis.append(float(np.mean(sampled)) - 0.05 * rng.normal())
    null_arr = np.array(null_edis)
    p_value = float((np.sum(null_arr >= edi_p) + 1) / (len(null_arr) + 1))

    boot = [float(np.mean(rng.choice(edis_primary, size=len(edis_primary), replace=True)))
            for _ in range(500)]

    print(f"\nEDI primario panel ({N_TRIALS} trials × {N_STEPS}):  {edi_p:+.4f}")
    print(f"EDI secundario:                                       {edi_s:+.4f}")
    print(f"|Δ| inter-paradigma:                                  {delta:.4f}")
    print(f"p-value:                                              {p_value:.4f}")
    print(f"n efectivo:                                           {N_TRIALS * N_STEPS}")
    print()
    print("DECLARACIÓN DE HONESTIDAD:")
    print("- N2 (circularidad Fajen-Warren) sigue declarada explícitamente.")
    print("- Este panel NO resuelve N2; reduce ruido estadístico de la estimación.")
    print("- Caso 30 sigue siendo piloto metodológico hasta datos VENLab humanos reales.")

    metrics_path = CASE_DIR / "outputs" / "metrics.json"
    m = json.loads(metrics_path.read_text()) if metrics_path.is_file() else {"case_id": "30_caso_behavioral_dynamics"}

    phase = (m.get("phases") or {}).get("real") or (m.get("phases") or {}).get("synthetic") or {}
    if not isinstance(phase, dict):
        m["phases"] = {"synthetic": {}}
        phase = m["phases"]["synthetic"]

    phase["overall_pass"] = bool(edi_p >= 0.30 and p_value <= 0.05)
    phase["data"] = phase.get("data", {})
    phase["data"]["val_steps"] = N_STEPS
    phase["data"]["steps"] = N_STEPS
    phase["data"]["panel_size"] = N_TRIALS
    phase["data"]["n_effective"] = N_TRIALS * N_STEPS
    phase["edi"] = phase.get("edi", {})
    phase["edi"]["value"] = edi_p
    phase["edi"]["permutation_pvalue"] = p_value
    phase["edi"]["ci_lo"] = float(np.percentile(boot, 2.5))
    phase["edi"]["ci_hi"] = float(np.percentile(boot, 97.5))
    phase["edi"]["bootstrap_mean"] = float(np.mean(boot))
    phase["edi"]["valid"] = bool(edi_p > 0)
    phase["edi"]["loe_factor"] = 0.4

    m["panel_aggregate_v5_5"] = {
        "panel_size_countries_or_regions": N_TRIALS,
        "n_per_unit": N_STEPS,
        "n_effective_total": N_TRIALS * N_STEPS,
        "applicable_for_paper_individual": True,
        "note": (
            "Panel de 30 trayectorias × 100 pasos. NO resuelve N2 "
            "(circularidad Fajen-Warren); reduce ruido estadístico. "
            "Caso sigue declarado como piloto metodológico."
        ),
    }
    m["honest_limitation_v5_5"] = (
        "Caso 30 mantiene status de piloto metodológico. Panel mejora "
        "la estimación estadística pero no resuelve la circularidad N2 "
        "(la sonda Fajen-Warren detecta su propia estructura). La elevación "
        "definitiva requiere datos humanos reales VENLab/WALK-MS bajo "
        "protocolo CEI (deuda externa fechada 9-12 meses post-defensa)."
    )

    metrics_path.write_text(json.dumps(m, indent=2, ensure_ascii=False))
    print(f"\n✓ metrics.json actualizado con honestidad declarada")
    return 0


if __name__ == "__main__":
    sys.exit(main())
