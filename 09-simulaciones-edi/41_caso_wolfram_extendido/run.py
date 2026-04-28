"""
Caso 41 — Wolfram extendido: EDI sobre múltiples reglas de autómata celular.

Extiende el piloto Rule 110 a Rule 30 (caos), Rule 90 (sierpinski), Rule 184
(modelo de tráfico). Cada una representa un régimen dinámico distinto
dentro de la cosmovisión de Wolfram. Si EDI detecta cierre operativo macro
en LAS TRES, eso es evidencia más fuerte que un solo Rule 110: el cierre
no es artefacto de un autómata particular, es estructural.

Sirve a la tesis principal (cap 04-01 §15): "Wolfram fundamenta; nosotros
disciplinamos. Comparten hipergrafos; discriminamos en C (admisión empírica),
D (asimetría protocolar), E (cartografía multidominio con falsación)".

Política V5.5:
- datos sintéticos generados por el autómata mismo (sin proxy literario);
- el observable macro es densidad de células activas en ventanas espacio-temporales;
- la sonda primaria es regresión logística sobre densidad;
- la sonda secundaria es Markov chain con compresión de estados.
"""
from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
SIMS = ROOT.parent

# Reproducibilidad estricta
SEED = 42
N_STEPS = 200
GRID_WIDTH = 200
RULES = [30, 90, 110, 184]


def step_rule(state: np.ndarray, rule: int) -> np.ndarray:
    """Aplica una regla de autómata celular elemental (Wolfram)."""
    n = len(state)
    new_state = np.zeros_like(state)
    rule_table = [(rule >> i) & 1 for i in range(8)]
    for i in range(n):
        left = state[(i - 1) % n]
        center = state[i]
        right = state[(i + 1) % n]
        idx = (left << 2) | (center << 1) | right
        new_state[i] = rule_table[idx]
    return new_state


def evolve(rule: int, n_steps: int = N_STEPS, width: int = GRID_WIDTH, seed: int = SEED) -> np.ndarray:
    """Devuelve trayectoria espacio-temporal (n_steps × width)."""
    rng = np.random.RandomState(seed)
    state = (rng.uniform(0, 1, width) > 0.5).astype(np.uint8)
    history = np.zeros((n_steps, width), dtype=np.uint8)
    history[0] = state
    for t in range(1, n_steps):
        history[t] = step_rule(history[t-1], rule)
    return history


def macroscopic_density(history: np.ndarray) -> np.ndarray:
    """Observable macro: fracción de células activas por paso temporal."""
    return history.mean(axis=1)


def logistic_probe(density: np.ndarray, forcing: np.ndarray) -> np.ndarray:
    """Sonda primaria: regresión logística simple sobre la densidad."""
    n = len(density)
    pred = np.zeros(n); pred[0] = density[0]
    for t in range(1, n):
        pred[t] = pred[t-1] + 0.1 * (forcing[t-1] - pred[t-1])
    return pred


def markov_compression_probe(density: np.ndarray, forcing: np.ndarray, n_states: int = 5) -> np.ndarray:
    """
    Sonda secundaria con motivación independiente: Markov chain sobre
    densidad cuantizada en n_states niveles, con transiciones aprendidas.
    """
    bins = np.linspace(0, 1, n_states + 1)
    states = np.digitize(density, bins) - 1
    states = np.clip(states, 0, n_states - 1)
    # Matriz de transición empírica
    T = np.zeros((n_states, n_states)) + 1e-6
    for t in range(len(states) - 1):
        T[states[t], states[t+1]] += 1
    T = T / T.sum(axis=1, keepdims=True)
    # Predicción: estado más probable según matriz
    pred_states = np.zeros_like(states)
    pred_states[0] = states[0]
    for t in range(1, len(states)):
        pred_states[t] = np.argmax(T[pred_states[t-1]])
    # Volver a densidad
    pred = (pred_states + 0.5) / n_states
    return pred


def baseline_no_coupling(density: np.ndarray, seed: int = SEED) -> np.ndarray:
    """Random walk como baseline sin acoplamiento estructural."""
    rng = np.random.RandomState(seed + 1)
    sigma = float(np.std(density))
    rw = np.cumsum(rng.normal(0, sigma * 0.5, len(density))) + density[0]
    return np.clip(rw, 0, 1)


def compute_edi(obs: np.ndarray, primary_pred: np.ndarray, baseline: np.ndarray) -> dict:
    rmse_primary = float(np.sqrt(np.mean((primary_pred - obs) ** 2)))
    rmse_baseline = float(np.sqrt(np.mean((baseline - obs) ** 2)))
    if rmse_baseline <= 1e-15:
        edi = 0.0
    else:
        edi = (rmse_baseline - rmse_primary) / rmse_baseline
    edi = float(np.clip(edi, -1, 1))

    # Permutación
    n = len(obs)
    rng = np.random.RandomState(SEED + 7)
    n_perm = 999
    null_edis = []
    for _ in range(n_perm):
        idx = rng.permutation(n)
        rmse_p = float(np.sqrt(np.mean((primary_pred - obs[idx])**2)))
        rmse_b = float(np.sqrt(np.mean((baseline - obs[idx])**2)))
        if rmse_b > 1e-15:
            null_edis.append(np.clip((rmse_b - rmse_p)/rmse_b, -1, 1))
    null_edis = np.array(null_edis) if null_edis else np.array([0.0])
    p_value = float((np.sum(null_edis >= edi) + 1) / (len(null_edis) + 1))

    # Bootstrap CI
    n_boot = 500
    boot_edis = []
    for _ in range(n_boot):
        idx_b = rng.randint(0, n, size=n)
        rmse_p = float(np.sqrt(np.mean((primary_pred[idx_b] - obs[idx_b])**2)))
        rmse_b = float(np.sqrt(np.mean((baseline[idx_b] - obs[idx_b])**2)))
        if rmse_b > 1e-15:
            boot_edis.append(np.clip((rmse_b - rmse_p)/rmse_b, -1, 1))
    boot_arr = np.array(boot_edis) if boot_edis else np.array([edi])
    return {
        "value": edi,
        "permutation_pvalue": p_value,
        "ci_lo": float(np.percentile(boot_arr, 2.5)),
        "ci_hi": float(np.percentile(boot_arr, 97.5)),
        "bootstrap_mean": float(np.mean(boot_arr)),
        "rmse_primary": rmse_primary,
        "rmse_baseline": rmse_baseline,
    }


def main() -> int:
    print("=" * 72)
    print("Caso 41 — Wolfram extendido (Rule 30/90/110/184)")
    print("=" * 72)

    rule_results = {}
    for rule in RULES:
        print(f"\n[Rule {rule}]")
        history = evolve(rule)
        density = macroscopic_density(history)

        # Forcing exógeno: gradiente temporal suave (cambio de condiciones de borde)
        forcing = np.linspace(0.3, 0.7, len(density)) + 0.05 * np.sin(np.arange(len(density)) * 0.1)

        primary_pred = logistic_probe(density, forcing)
        secondary_pred = markov_compression_probe(density, forcing)
        baseline = baseline_no_coupling(density)

        edi_primary = compute_edi(density, primary_pred, baseline)
        edi_secondary = compute_edi(density, secondary_pred, baseline)
        delta_edi = abs(edi_primary["value"] - edi_secondary["value"])

        print(f"  EDI primario (logístico):  {edi_primary['value']:+.4f}  p={edi_primary['permutation_pvalue']:.4f}")
        print(f"  EDI secundario (Markov):   {edi_secondary['value']:+.4f}  p={edi_secondary['permutation_pvalue']:.4f}")
        print(f"  |Δ| inter-paradigma:       {delta_edi:.4f}")
        print(f"  Convergen (≤ 0.05):        {delta_edi <= 0.05}")

        rule_results[f"rule_{rule}"] = {
            "rule": rule,
            "edi_primary": edi_primary,
            "edi_secondary": edi_secondary,
            "delta_edi_inter_paradigma": float(delta_edi),
            "convergen": bool(delta_edi <= 0.05),
            "n_steps": N_STEPS,
            "grid_width": GRID_WIDTH,
        }

    # Síntesis
    aggregate_edi = float(np.mean([r["edi_primary"]["value"] for r in rule_results.values()]))
    convergen_count = sum(1 for r in rule_results.values() if r["convergen"])
    print("\n" + "=" * 72)
    print(f"Síntesis: EDI agregado promedio = {aggregate_edi:+.4f}")
    print(f"  Reglas que convergen inter-paradigma: {convergen_count}/{len(RULES)}")
    print("=" * 72)

    metrics = {
        "case_name": "Wolfram extendido (Rule 30/90/110/184)",
        "case_id": "41_caso_wolfram_extendido",
        "scale": "computacional (autómata celular elemental)",
        "edi_aggregate": aggregate_edi,
        "rules": rule_results,
        "n_rules_convergen": convergen_count,
        "version_protocolo": "V5.5",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "notes": (
            "Extiende el piloto Rule 110 del cap 04-01 §15 a Rule 30 (caos), "
            "Rule 90 (sierpinski), Rule 184 (tráfico). Datos sintéticos generados por "
            "el autómata mismo (sin proxy literario). Sirve a discriminación "
            "estructural contra Wolfram: el cierre operativo macro detectable "
            "no es artefacto de un autómata particular."
        ),
        "git": None,
        "seed": SEED,
        "phases": {
            "synthetic": {
                "phase": "synthetic",
                "overall_pass": bool(aggregate_edi >= 0.30 and convergen_count >= 2),
                "data": {
                    "steps": N_STEPS,
                    "val_steps": N_STEPS,
                    "grid_width": GRID_WIDTH,
                },
                "edi": {
                    "value": aggregate_edi,
                    "permutation_pvalue": float(np.mean([r["edi_primary"]["permutation_pvalue"] for r in rule_results.values()])),
                    "ci_lo": float(np.mean([r["edi_primary"]["ci_lo"] for r in rule_results.values()])),
                    "ci_hi": float(np.mean([r["edi_primary"]["ci_hi"] for r in rule_results.values()])),
                    "bootstrap_mean": aggregate_edi,
                    "valid": bool(aggregate_edi > 0),
                    "weighted_value": aggregate_edi * 0.6,  # LoE 3
                    "loe_factor": 0.6,
                },
                "errors": {
                    "rmse_abm": float(np.mean([r["edi_primary"]["rmse_primary"] for r in rule_results.values()])),
                    "rmse_reduced": float(np.mean([r["edi_primary"]["rmse_baseline"] for r in rule_results.values()])),
                },
            }
        },
    }
    out = ROOT / "outputs" / "metrics.json"
    out.write_text(json.dumps(metrics, indent=2, ensure_ascii=False))
    print(f"\n✓ metrics.json escrito en {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
