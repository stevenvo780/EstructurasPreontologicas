"""
Espacio de fase del caso ancla 30 (behavioral_dynamics, Fajen-Warren). — F33+.

Reproduce la dinámica de heading φ(t) bajo Fajen-Warren de segundo orden y
genera figuras de espacio de fase que muestran:
  1. Trayectoria (φ, φ̇) — atractor convergente cuando d_g > 0
  2. Bifurcación al cambiar la dirección de meta — el atractor se desplaza
  3. Serie temporal de error de heading β_h(t)
  4. Trayectoria contrafactual al perturbar el parámetro k_g (sensibilidad)

Salida: `figures/caso30/phase_portrait_caso30.{png,svg}` (cuatro paneles).

Referencia teórica: Fajen, B. R., & Warren, W. H. (2003). "Behavioral dynamics
of steering, obstacle avoidance, and route selection." Journal of Experimental
Psychology: Human Perception and Performance, 29(2), 343-362.
"""
from __future__ import annotations
import math
import random
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "figures" / "caso30"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def fajen_warren_trajectory(steps: int, b: float = 3.25, k_g: float = 7.50,
                            c1: float = 0.40, c2: float = 0.40, dt: float = 0.05,
                            d_g: float = 4.0,
                            goal_changes: list[tuple[int, float]] | None = None,
                            noise_std: float = 0.05, perceptive_noise: float = 0.02,
                            seed: int = 42) -> dict:
    """Versión instrumentada del simulador de `30_caso_behavioral_dynamics/src/data.py`."""
    random.seed(seed)
    np.random.seed(seed)
    if goal_changes is None:
        goal_changes = []
        n_segments = 8
        seg_len = steps // n_segments
        for i in range(n_segments):
            angle = (-1) ** i * (0.4 + 0.3 * random.random())
            goal_changes.append((i * seg_len, angle))
    phi = 0.0
    phi_dot = 0.0
    psi_g = 0.0
    attract = math.exp(-c1 * d_g) + c2
    goal_dict = dict(goal_changes)

    phi_arr = np.zeros(steps)
    phi_dot_arr = np.zeros(steps)
    psi_g_arr = np.zeros(steps)
    beta_arr = np.zeros(steps)
    for t in range(steps):
        if t in goal_dict:
            psi_g = goal_dict[t]
        psi_g_perceived = psi_g + random.gauss(0, perceptive_noise)
        phi_ddot = -b * phi_dot - k_g * (phi - psi_g_perceived) * attract
        phi_dot = phi_dot + phi_ddot * dt + random.gauss(0, noise_std) * dt
        phi = phi + phi_dot * dt
        phi_arr[t] = phi
        phi_dot_arr[t] = phi_dot
        psi_g_arr[t] = psi_g
        beta_arr[t] = phi - psi_g
    return {
        "phi": phi_arr,
        "phi_dot": phi_dot_arr,
        "psi_g": psi_g_arr,
        "beta": beta_arr,
        "goal_changes": goal_changes,
        "params": {"b": b, "k_g": k_g, "c1": c1, "c2": c2, "d_g": d_g, "dt": dt},
    }


def main() -> int:
    traj = fajen_warren_trajectory(steps=400, seed=42)
    traj_kg_low = fajen_warren_trajectory(steps=400, k_g=4.0, seed=42)
    traj_kg_high = fajen_warren_trajectory(steps=400, k_g=12.0, seed=42)

    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # Panel 1 — espacio de fase (φ, φ̇) con cambios de meta marcados
    ax = axes[0, 0]
    sc = ax.scatter(traj["phi"], traj["phi_dot"], c=np.arange(len(traj["phi"])),
                    cmap="viridis", s=8, alpha=0.6)
    ax.axhline(0, color="#888", linewidth=0.5)
    ax.axvline(0, color="#888", linewidth=0.5)
    for t, ang in traj["goal_changes"]:
        ax.scatter([traj["phi"][t]], [traj["phi_dot"][t]],
                   marker="x", s=80, color="#c0392b", zorder=5,
                   label="cambio de meta" if t == traj["goal_changes"][0][0] else None)
    ax.set_xlabel(r"$\phi$ (heading)")
    ax.set_ylabel(r"$\dot\phi$ (velocidad angular)")
    ax.set_title("Espacio de fase: (φ, φ̇)\ncolor = tiempo, cruces = cambios de meta")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    plt.colorbar(sc, ax=ax, label="t (paso)")

    # Panel 2 — bifurcación: trayectorias para distintos k_g
    ax = axes[0, 1]
    ax.plot(traj_kg_low["phi"], traj_kg_low["phi_dot"], color="#3498db",
            alpha=0.6, linewidth=0.8, label=r"$k_g = 4.0$ (subamortiguado)")
    ax.plot(traj["phi"], traj["phi_dot"], color="#27ae60",
            alpha=0.7, linewidth=0.8, label=r"$k_g = 7.5$ (canónico Fajen-Warren)")
    ax.plot(traj_kg_high["phi"], traj_kg_high["phi_dot"], color="#c0392b",
            alpha=0.6, linewidth=0.8, label=r"$k_g = 12.0$ (sobreamortiguado)")
    ax.set_xlabel(r"$\phi$ (heading)")
    ax.set_ylabel(r"$\dot\phi$")
    ax.set_title("Sensibilidad a $k_g$: forma de la cuenca\ncambia con la rigidez del acoplamiento")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 3 — error de heading β_h(t) con cambios de meta
    ax = axes[1, 0]
    t_axis = np.arange(len(traj["beta"]))
    ax.plot(t_axis, traj["beta"], color="#2c3e50", linewidth=0.9)
    for t, ang in traj["goal_changes"]:
        ax.axvline(t, color="#c0392b", linestyle="--", alpha=0.5, linewidth=0.8)
    ax.axhline(0, color="#27ae60", linestyle="-", alpha=0.5, linewidth=0.8,
               label="meta perfecta β_h=0")
    ax.set_xlabel("t (paso)")
    ax.set_ylabel(r"$\beta_h(t) = \phi(t) - \psi_g(t)$")
    ax.set_title("Error de heading β_h(t)\nlíneas verticales = cambios de meta\nbifurcación de ruta = bajada brusca")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 4 — meta ψ_g(t) y heading φ(t) superpuestos
    ax = axes[1, 1]
    ax.plot(t_axis, traj["psi_g"], color="#c0392b", linewidth=1.4, label=r"$\psi_g(t)$ meta")
    ax.plot(t_axis, traj["phi"], color="#2c3e50", linewidth=1.0, alpha=0.85, label=r"$\phi(t)$ heading")
    ax.set_xlabel("t (paso)")
    ax.set_ylabel("ángulo (rad)")
    ax.set_title("Persecución del agente al objetivo\nseguimiento con latencia y ruido perceptivo")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    fig.suptitle(
        "Caso 30 — Behavioral Dynamics (Fajen-Warren 2003)\n"
        "Trayectorias de espacio de fase del modelo de heading + bifurcación de ruta",
        fontsize=12, y=1.0,
    )
    fig.tight_layout()
    for ext in ("png", "svg"):
        out = OUT_DIR / f"phase_portrait_caso30.{ext}"
        fig.savefig(out, dpi=150)
        print(f"  → {out}")
    plt.close(fig)
    return 0


if __name__ == "__main__":
    sys.exit(main())
