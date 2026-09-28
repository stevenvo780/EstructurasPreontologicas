"""Self-test de Fix M4/M6 (gate C1) — 2026-09-28.

Regresión contra ronda adversarial red-team-motor-datos:
  M4a. c1_relative aceptaba mejoras ~1e-14 (`> 0 # cualquier mejora cuenta`).
  M4b. corr_threshold era parámetro muerto (rama B hardcodeaba corr > 0.3).
  M4c/M6. Rama (B) aprobaba C1 sin exigir aporte ODE (ahora diagnóstica).

Ejecutar (requiere numpy, usar venv del corpus):
  09-simulaciones-edi/.venv/bin/python 09-simulaciones-edi/common/test_gate_fixes.py
"""
from __future__ import annotations

import sys
from pathlib import Path

COMMON = Path(__file__).resolve().parent
if str(COMMON) not in sys.path:
    sys.path.insert(0, str(COMMON))

import numpy as np

from hybrid_validator import evaluate_c1

PASS = []


def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def t_epsilon_ignora_ruido():
    obs = np.zeros(10)
    reduced = np.full(10, 1.0)          # err = 1.0
    abm_noise = np.full(10, 1.0 - 1e-14)  # mejora 1e-14 (ruido float)
    c1, d = evaluate_c1(abm_noise, abm_noise, obs, 1.0, reduced_val=reduced)
    check("T1a mejora 1e-14 no aprueba relativa", d["c1_relative"] is False)
    abm_real = np.full(10, 0.99)        # mejora 0.01 (real)
    c1b, db = evaluate_c1(abm_real, abm_real, obs, 1.0, reduced_val=reduced)
    check("T1b mejora 0.01 sí aprueba relativa", db["c1_relative"] is True)


def t_corr_threshold_vivo():
    obs = np.arange(10, dtype=float)
    abm = obs + 0.1  # corr == 1.0 exacta, err pequeño
    _, d_lo = evaluate_c1(abm, abm, obs, float(obs.std()), corr_threshold=0.999999,
                           reduced_val=obs + 5.0)
    _, d_hi = evaluate_c1(abm, abm, obs, float(obs.std()), corr_threshold=1.0,
                           reduced_val=obs + 5.0)
    check("T2a threshold bajo corr alta -> absoluta True", d_lo["c1_absolute"] is True)
    # Con el bug (hardcode 0.3) AMBAS serían True; threshold=1.0 debe dar False.
    check("T2b threshold 1.0 con corr 1.0 -> absoluta False (param vivo)",
          d_hi["c1_absolute"] is False)
    check("T2c detail reporta threshold usado", d_hi["corr_threshold_used"] == 1.0)


def t_sin_fallback_silencioso():
    obs = np.arange(10, dtype=float)
    abm = obs + 0.1
    c1, d = evaluate_c1(abm, abm, obs, float(obs.std()), reduced_val=None)
    check("T3a sin reduced_val C1 falla", c1 is False)
    check("T3b absoluta sigue reportada", d["c1_absolute"] is True)
    check("T3c flag via_absolute_only", d["c1_via_absolute_only"] is True)


def t_rama_b_no_aprueba_gate():
    obs = np.arange(10, dtype=float)
    abm = obs + 0.1                      # buen ajuste absoluto
    reduced = obs.copy()                 # reducido perfecto -> relativa False
    c1, d = evaluate_c1(abm, abm, obs, float(obs.std()), reduced_val=reduced)
    check("T4a relativa False cuando reducido gana", d["c1_relative"] is False)
    check("T4b gate C1 False aunque absoluta pase (M6)", c1 is False)
    check("T4c flag via_absolute_only True", d["c1_via_absolute_only"] is True)


def t_keys_nuevas():
    obs = np.zeros(5)
    _, d = evaluate_c1(obs, obs, obs, 1.0, reduced_val=np.ones(5))
    check("T5 keys M4 presentes",
          "corr_threshold_used" in d and "c1_via_absolute_only" in d)


if __name__ == "__main__":
    t_epsilon_ignora_ruido()
    t_corr_threshold_vivo()
    t_sin_fallback_silencioso()
    t_rama_b_no_aprueba_gate()
    t_keys_nuevas()
    fails = [n for n, ok in PASS if not ok]
    print(f"\n{len(PASS) - len(fails)}/{len(PASS)} pass")
    if fails:
        print("FALLAS:", fails)
        sys.exit(1)
    print("TODOS LOS TESTS PASAN")
