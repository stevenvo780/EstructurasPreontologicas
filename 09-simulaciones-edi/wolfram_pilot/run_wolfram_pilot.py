"""Piloto EDI sobre hipergrafo de Wolfram (regla simple).

Implementa el esquema de 6 pasos del capítulo 04-01 §14: aplicar EDI a una
serie macro derivada de hypergraph rewriting. Usamos un autómata celular
elemental como proxy 1D de hypergraph rewriting (Wolfram 2002 cap. 3 trata
los CA como caso especial de los sistemas de reescritura). Regla 110 está
documentada como Turing-completa y produce estructura emergente compleja
(Cook 2004); la usamos como sustrato de prueba.

  Paso 1: regla = 110 (CA elemental con irreducibilidad computacional probada).
  Paso 2: 200 ejecuciones con condiciones iniciales perturbadas.
  Paso 3: sonda macro = densidad de celdas activas + curvatura discreta de
          la frontera entre regiones.
  Paso 4: EDI = 1 - rmse_coupled / rmse_no_ode con permutación 999 + bootstrap 500.
  Paso 5: hipótesis: EDI ≥ 0.30 → cierre operativo macro detectable;
          EDI < 0.10 → irreducibilidad computacional macro confirmada.
  Paso 6: lectura.

Salida: outputs/metrics_wolfram_pilot.json
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def evolve_rule(rule: int, init: np.ndarray, steps: int) -> np.ndarray:
    """Evolución determinística de un CA elemental con condición de borde periódica."""
    n = init.size
    table = np.array([(rule >> b) & 1 for b in range(8)], dtype=np.int8)
    cur = init.astype(np.int8).copy()
    history = np.zeros((steps, n), dtype=np.int8)
    history[0] = cur
    for t in range(1, steps):
        left = np.roll(cur, 1)
        right = np.roll(cur, -1)
        idx = (left << 2) | (cur << 1) | right
        cur = table[idx]
        history[t] = cur
    return history


def macro_density(history: np.ndarray) -> np.ndarray:
    """Sonda macro 1: densidad temporal de celdas activas (proxy de carga del hipergrafo)."""
    return history.mean(axis=1)


def macro_boundary_curvature(history: np.ndarray) -> np.ndarray:
    """Sonda macro 2: número de fronteras 0→1 en cada paso (proxy de curvatura discreta)."""
    diffs = np.diff(history.astype(np.int16), axis=1)
    boundaries = np.abs(diffs).sum(axis=1)
    return boundaries / history.shape[1]


def edi_proxy(observed: np.ndarray, modeled: np.ndarray, control: np.ndarray) -> dict:
    """EDI = 1 - rmse_modeled/rmse_control + permutación + bootstrap."""
    val_steps = max(10, observed.size // 3)
    obs_val = observed[-val_steps:]
    mod_val = modeled[-val_steps:]
    ctrl_val = control[-val_steps:]
    rmse_mod = float(np.sqrt(np.mean((obs_val - mod_val) ** 2)))
    rmse_ctrl = float(np.sqrt(np.mean((obs_val - ctrl_val) ** 2)))
    edi = 1.0 - rmse_mod / rmse_ctrl if rmse_ctrl > 1e-9 else None
    rng = np.random.default_rng(42)
    n_perm = 999
    null_edis = []
    for _ in range(n_perm):
        perm = rng.permutation(mod_val)
        rmse_p = float(np.sqrt(np.mean((obs_val - perm) ** 2)))
        e_p = 1.0 - rmse_p / rmse_ctrl if rmse_ctrl > 1e-9 else 0.0
        null_edis.append(e_p)
    null_edis = np.array(null_edis)
    pvalue = float(np.mean(null_edis >= edi)) if edi is not None else None
    n_boot = 500
    boot_edis = []
    for _ in range(n_boot):
        idx = rng.integers(0, val_steps, size=val_steps)
        b_obs = obs_val[idx]
        b_mod = mod_val[idx]
        b_ctrl = ctrl_val[idx]
        rmse_m = np.sqrt(np.mean((b_obs - b_mod) ** 2))
        rmse_c = np.sqrt(np.mean((b_obs - b_ctrl) ** 2))
        if rmse_c > 1e-9:
            boot_edis.append(1.0 - rmse_m / rmse_c)
    boot_edis = np.array(boot_edis)
    ci = (float(np.percentile(boot_edis, 2.5)), float(np.percentile(boot_edis, 97.5))) if len(boot_edis) > 0 else None
    return {
        "edi": edi,
        "p_value": pvalue,
        "ci_95": ci,
        "rmse_modeled": rmse_mod,
        "rmse_control": rmse_ctrl,
        "val_steps": val_steps,
    }


def fit_macro_dynamics(macro: np.ndarray) -> np.ndarray:
    """Modela la sonda macro con AR(1) sobre la mitad train."""
    n = macro.size
    train_n = n // 2
    train = macro[:train_n]
    if train.size < 2:
        return np.zeros_like(macro)
    a = float(np.cov(train[:-1], train[1:])[0, 1] / (np.var(train[:-1]) + 1e-9))
    b = float(np.mean(train) * (1 - a))
    pred = np.zeros_like(macro)
    pred[0] = train[0]
    for t in range(1, n):
        pred[t] = a * (pred[t - 1] if t < train_n else macro[t - 1]) + b
    return pred


def run_pilot(rule: int = 110, n_runs: int = 200, n_cells: int = 64,
              steps: int = 200, seed: int = 42) -> dict:
    rng = np.random.default_rng(seed)
    edis_density = []
    edis_curvature = []
    for run in range(n_runs):
        init = rng.integers(0, 2, size=n_cells).astype(np.int8)
        history = evolve_rule(rule, init, steps)
        density = macro_density(history)
        curvature = macro_boundary_curvature(history)

        # modelo macro: AR(1) ajustado en train
        mod_d = fit_macro_dynamics(density)
        mod_c = fit_macro_dynamics(curvature)

        # control: serie aleatoria reescalada al mismo rango (proxy "no_ode")
        ctrl_d = rng.uniform(density.min(), density.max(), size=density.size)
        ctrl_c = rng.uniform(curvature.min(), curvature.max(), size=curvature.size)

        e_d = edi_proxy(density, mod_d, ctrl_d)
        e_c = edi_proxy(curvature, mod_c, ctrl_c)
        if e_d["edi"] is not None:
            edis_density.append(e_d["edi"])
        if e_c["edi"] is not None:
            edis_curvature.append(e_c["edi"])

    out = {
        "rule": rule,
        "n_runs": n_runs,
        "n_cells": n_cells,
        "steps": steps,
        "density_probe": {
            "edi_mean": float(np.mean(edis_density)) if edis_density else None,
            "edi_std": float(np.std(edis_density)) if edis_density else None,
            "edi_median": float(np.median(edis_density)) if edis_density else None,
            "n_valid": len(edis_density),
        },
        "curvature_probe": {
            "edi_mean": float(np.mean(edis_curvature)) if edis_curvature else None,
            "edi_std": float(np.std(edis_curvature)) if edis_curvature else None,
            "edi_median": float(np.median(edis_curvature)) if edis_curvature else None,
            "n_valid": len(edis_curvature),
        },
    }

    # Veredicto cualitativo
    edi_d = out["density_probe"]["edi_mean"]
    edi_c = out["curvature_probe"]["edi_mean"]
    verdicts = []
    for name, edi in [("densidad", edi_d), ("curvatura", edi_c)]:
        if edi is None:
            verdicts.append((name, "indeterminado"))
        elif edi >= 0.30:
            verdicts.append((name, "cierre operativo macro detectable"))
        elif edi >= 0.10:
            verdicts.append((name, "señal macro débil"))
        else:
            verdicts.append((name, "irreducibilidad computacional macro confirmada"))
    out["verdicts"] = verdicts
    return out


if __name__ == "__main__":
    print("=== Piloto EDI sobre Wolfram CA Rule 110 ===")
    result = run_pilot(rule=110, n_runs=200, n_cells=64, steps=200, seed=42)
    out_path = OUT / "metrics_wolfram_pilot.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nResults written to: {out_path}")
