"""
Anima un caso EDI usando el motor ABM real del framework
(common/abm_core.simulate_abm_core): campo espacial heterogeneo con
gradiente de forzamiento radial, heterogeneidad parametrica por celda
y un evento de perturbacion (shock) a mitad de la corrida.

Muestra como el sistema absorbe y relaja un shock localizado — la
dinamica de histeresis/resiliencia que el indice EDI cuantifica.

-> estructuras-caso-anim.mp4
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import animation

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "common"))
from abm_core import simulate_abm_core  # motor ABM real del framework EDI

ASSETS = "/workspace/INeedMoney/docs/03-perfil-y-marca/publicaciones/assets"
os.makedirs(ASSETS, exist_ok=True)

BG = "#0e1117"; FG = "#e6e6e6"; TEAL = "#1f8a8a"; GOLD = "#d4a017"
plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": FG, "axes.labelcolor": FG,
    "xtick.color": FG, "ytick.color": FG,
    "axes.edgecolor": "#3a3f4b", "font.size": 12,
})

STEPS = 200
N = 70
SHOCK = 90
t_arr = np.arange(STEPS)
forcing = (0.5 * np.sin(2 * np.pi * t_arr / 30.0) + 0.01 * t_arr).tolist()

params = {
    "grid_size": N,
    "diffusion": 0.16,
    "noise": 0.05,
    "macro_coupling": 0.06,
    "forcing_scale": 0.10,
    "damping": 0.025,
    "forcing_series": forcing,
    "forcing_gradient_type": "radial",     # heterogeneidad espacial real
    "forcing_gradient_strength": 0.7,
    "heterogeneity_strength": 0.35,        # parametros por celda
    "heterogeneity_seed": 11,
    "perturbation_event": {"step": SHOCK, "magnitude": 3.5},  # shock localizado
    "init_range": 0.6,
    "_store_grid": True,
    "macro_mode": "mean",
}

print("[EDI] corriendo motor ABM real (gradiente radial + heterogeneidad + shock)...")
res = simulate_abm_core(params, STEPS, seed=5, series_key="tbar")
grids = np.array(res["grid"])     # (STEPS, N, N)
macro = np.array(res["tbar"])
print(f"[EDI] grids {grids.shape}  rango=[{grids.min():.2f},{grids.max():.2f}]  "
      f"shock en paso {SHOCK}")

# Autoescalado por frame para resaltar la textura espacial
lo = np.array([np.percentile(g, 4) for g in grids])
hi = np.array([np.percentile(g, 96) for g in grids])

fig, (axf, axm) = plt.subplots(
    1, 2, figsize=(11, 5.2), gridspec_kw={"width_ratios": [1.2, 1.0]})
fig.subplots_adjust(left=0.04, right=0.95, top=0.85, bottom=0.12, wspace=0.30)

im = axf.imshow(grids[0], cmap="viridis", vmin=lo[0], vmax=hi[0],
                interpolation="bilinear", animated=True)
axf.set_title("Campo EDI  (70 x 70, gradiente radial)", color=GOLD, fontsize=13, pad=10)
axf.set_xticks([]); axf.set_yticks([])
cbar = fig.colorbar(im, ax=axf, fraction=0.046, pad=0.02)
cbar.set_label("estado local (relativo)", color=FG)
plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color=FG)

axm.set_title("Respuesta macro al shock", color=TEAL, fontsize=13, pad=10)
axm.set_xlim(0, STEPS)
mpad = (macro.max() - macro.min()) * 0.15 + 1e-6
axm.set_ylim(macro.min() - mpad, macro.max() + mpad)
axm.set_xlabel("paso temporal")
line, = axm.plot([], [], color=GOLD, lw=2.2)
dot, = axm.plot([], [], "o", color=TEAL, ms=7)
shock_line = axm.axvline(SHOCK, color="#e25822", ls="--", lw=1.4, alpha=0.0)
axm.grid(alpha=0.15)

sup = fig.suptitle("", color=FG, fontsize=11, y=0.95)


def update(t):
    im.set_array(grids[t])
    im.set_clim(lo[t], hi[t])
    line.set_data(t_arr[:t + 1], macro[:t + 1])
    dot.set_data([t], [macro[t]])
    if t >= SHOCK:
        shock_line.set_alpha(0.7)
    estado = "absorbiendo shock" if SHOCK <= t < SHOCK + 25 else (
        "relajacion / histeresis" if t >= SHOCK + 25 else "regimen base")
    sup.set_text(f"Estructuras preontologicas - caso EDI  |  paso {t+1}/{STEPS}  |  {estado}")
    return im, line, dot, shock_line, sup


anim = animation.FuncAnimation(fig, update, frames=STEPS, blit=False)
out = os.path.join(ASSETS, "estructuras-caso-anim.mp4")
writer = animation.FFMpegWriter(fps=25, codec="libx264",
                                extra_args=["-pix_fmt", "yuv420p"], bitrate=2800)
anim.save(out, writer=writer, dpi=120)
plt.close(fig)
print(f"[EDI] guardado -> {out}")
