"""
Self-test del módulo replication.py.
"""
from __future__ import annotations

import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.replication import (
    seed_robustness,
    holdout_temporal,
    adversarial_probe_swap,
    replication_robustness_summary,
)


def test_seed_robustness():
    """Simulamos un caso 'estable' donde EDI casi no cambia con seed."""
    def fake_run(seed: int, base_edi: float = 0.65) -> dict:
        rng = np.random.RandomState(seed)
        return {"edi": base_edi + rng.normal(0, 0.005)}

    result = seed_robustness(
        fake_run, base_kwargs={"base_edi": 0.65}, seeds=[1, 7, 13, 17, 23, 42]
    )
    print(f"  EDIs: {[f'{e:.4f}' for e in result['edis']]}")
    print(f"  mean={result['mean']:.4f}  std={result['std']:.5f}")
    print(f"  max_drift={result['max_drift']:.4f}  robust={result['robust']}")
    assert result["robust"], "caso estable debería ser robusto"
    print("  ✓ caso estable detectado como robust")


def test_seed_robustness_fail():
    """Caso 'inestable' debería fallar criterio."""
    def fake_run(seed: int) -> dict:
        rng = np.random.RandomState(seed)
        return {"edi": 0.30 + rng.normal(0, 0.10)}  # alta varianza

    result = seed_robustness(fake_run, base_kwargs={}, seeds=[1, 7, 13])
    print(f"  EDIs: {[f'{e:.4f}' for e in result['edis']]}")
    print(f"  max_drift={result['max_drift']:.4f}  robust={result['robust']}")
    if not result["robust"]:
        print("  ✓ caso inestable detectado como NO robust")


def test_holdout_temporal():
    n = 100
    rng = np.random.RandomState(42)
    obs = np.cumsum(rng.normal(0, 1, n))
    abm = obs + rng.normal(0, 0.5, n)
    red = obs + rng.normal(0, 1.5, n)

    result = holdout_temporal(obs, abm, reduced=red, train_frac=0.8)
    print(f"  edi_full={result['edi_full']:.4f}")
    print(f"  edi_train={result['edi_train']:.4f}")
    print(f"  edi_test={result['edi_test']:.4f}")
    print(f"  Δ={result['delta_test_vs_full']:.4f}  sin_leakage={result['sin_leakage']}")
    print("  ✓ holdout_temporal ejecutado")


def test_adversarial_swap():
    n = 100
    rng = np.random.RandomState(11)
    obs_b = np.cumsum(rng.normal(0, 1, n))

    # Sonda A: una transformación específica que NO captura obs_b
    def probe_specific(forcing):
        return np.cumsum(forcing) * 0.001  # casi cero

    result = adversarial_probe_swap(
        probe_predict_fn_A=probe_specific,
        obs_data_B=obs_b,
        expected_low=True,
    )
    print(f"  edi_cruzado={result['edi_cruzado']:.4f}")
    print(f"  especifica={result['especifica']}  cumple={result['cumple_expectativa']}")
    print("  ✓ adversarial_probe_swap ejecutado")


def test_summary_integration():
    seed_dict = {"robust": True, "max_drift": 0.02}
    holdout_dict = {"sin_leakage": True, "delta_test_vs_full": 0.03}
    adversarial = [
        {"cumple_expectativa": True, "edi_cruzado": 0.01},
        {"cumple_expectativa": True, "edi_cruzado": -0.05},
    ]
    summary = replication_robustness_summary(seed_dict, holdout_dict, adversarial)
    print(f"  tests_pasados: {summary['tests_pasados']}/{summary['tests_ejecutados']}")
    print(f"  inferencia_robusta: {summary['inferencia_robusta_replicacion']}")
    assert summary["inferencia_robusta_replicacion"]
    print("  ✓ summary integra los tres tests correctamente")


if __name__ == "__main__":
    print("Test 1 — seed_robustness (caso estable):")
    test_seed_robustness()
    print("\nTest 1b — seed_robustness (caso inestable):")
    test_seed_robustness_fail()
    print("\nTest 2 — holdout_temporal:")
    test_holdout_temporal()
    print("\nTest 3 — adversarial_probe_swap:")
    test_adversarial_swap()
    print("\nTest 4 — summary integration:")
    test_summary_integration()
    print("\n✅ Todos los tests pasaron.")
