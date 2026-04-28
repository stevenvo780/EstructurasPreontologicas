"""Tests unitarios mínimos para edi_engine.

Política: tests triviales que el motor DEBE pasar. Si fallan, hay bug.
"""

import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from edi_engine import run_edi, rmse


def test_rmse_idempotente():
    """RMSE de una serie consigo misma = 0."""
    a = np.array([1.0, 2.0, 3.0])
    assert abs(rmse(a, a)) < 1e-9, "RMSE(a,a) debería ser 0"
    print("  PASS: rmse_idempotente")


def test_edi_predicciones_identicas():
    """Si coupled y no_ode predicen idéntico, EDI = 0."""
    obs = np.linspace(0, 10, 100) + np.random.default_rng(0).normal(0, 0.1, 100)
    forcing = np.zeros(100)
    def same(forcing, train_obs, train_steps, val_steps):
        return np.full(val_steps, float(np.mean(train_obs)))
    r = run_edi("test", "test", obs, forcing, same, same, n_perm=99, n_boot=50)
    assert abs(r.edi) < 1e-6, f"EDI con sondas idénticas debería ser 0, fue {r.edi}"
    print(f"  PASS: edi_predicciones_identicas (EDI = {r.edi:+.6f})")


def test_edi_perfecto():
    """Si coupled predice perfectamente y no_ode predice mal, EDI ≈ 1."""
    obs = np.array([float(i) for i in range(100)])
    forcing = obs.copy()
    def perfect(forcing, train_obs, train_steps, val_steps):
        return forcing[train_steps:train_steps + val_steps].copy()
    def constant(forcing, train_obs, train_steps, val_steps):
        return np.full(val_steps, 0.0)
    r = run_edi("test", "test", obs, forcing, perfect, constant, n_perm=99, n_boot=50)
    assert r.edi > 0.9, f"EDI con sonda perfecta debería ser > 0.9, fue {r.edi}"
    print(f"  PASS: edi_perfecto (EDI = {r.edi:+.4f})")


def test_edi_random():
    """Sondas que predicen ruido aleatorio: EDI ≈ 0."""
    rng = np.random.default_rng(42)
    obs = rng.normal(0, 1, 100)
    forcing = rng.normal(0, 1, 100)
    def random_pred(forcing, train_obs, train_steps, val_steps):
        return rng.normal(float(np.mean(train_obs)), float(np.std(train_obs)), val_steps)
    r = run_edi("test", "test", obs, forcing, random_pred, random_pred,
                n_perm=99, n_boot=50)
    # En este caso ambas sondas son aleatorias, EDI puede variar pero esperamos cerca de 0
    print(f"  Info: edi_random EDI = {r.edi:+.4f} (variable, esperado ≈ 0)")


def test_clasificacion_nivel():
    """La clasificación de nivel respeta umbrales."""
    # caso strong sintético
    obs = np.linspace(0, 10, 100) + np.random.default_rng(0).normal(0, 0.05, 100)
    forcing = obs.copy()
    def perfect(forcing, train_obs, train_steps, val_steps):
        return forcing[train_steps:train_steps + val_steps].copy()
    def constant(forcing, train_obs, train_steps, val_steps):
        return np.full(val_steps, 0.0)
    r = run_edi("test", "test", obs, forcing, perfect, constant, n_perm=99, n_boot=50)
    assert r.nivel.startswith("4_") or r.nivel.startswith("3_"), \
        f"Sonda perfecta debería ser strong o weak, fue {r.nivel}"
    print(f"  PASS: clasificacion_nivel (nivel = {r.nivel})")


def main():
    print("=== Tests unitarios edi_engine ===")
    print()
    test_rmse_idempotente()
    test_edi_predicciones_identicas()
    test_edi_perfecto()
    test_edi_random()
    test_clasificacion_nivel()
    print()
    print("=== Todos los tests pasaron ===")


if __name__ == "__main__":
    main()
