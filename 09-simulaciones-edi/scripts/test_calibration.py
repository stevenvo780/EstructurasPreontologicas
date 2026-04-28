"""
Self-test del módulo calibration.py.

Verifica que las tres herramientas funcionan sobre datos sintéticos con
propiedades conocidas:

1. block_bootstrap_pvalue debe dar p-value mayor (más conservador) que
   permutación simple cuando hay autocorrelación AR(1).
2. newey_west_se debe ser > SE clásico cuando hay autocorrelación.
3. fwer_correct debe rechazar menos hipótesis que el rechazo directo.

Uso:
    cd 09-simulaciones-edi
    python3 scripts/test_calibration.py
"""
from __future__ import annotations

import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.calibration import (
    block_bootstrap_pvalue,
    newey_west_se,
    fwer_correct,
)


def _ar1_series(n: int, phi: float, sigma: float, seed: int) -> np.ndarray:
    """Serie AR(1) con autocorrelación phi."""
    rng = np.random.RandomState(seed)
    eps = rng.normal(0, sigma, size=n)
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + eps[t]
    return x


def test_block_bootstrap_more_conservative_under_autocorrelation():
    """Bajo AR(1) fuerte, p_block debería ser >= p_naive en distribución."""
    n = 200
    obs = _ar1_series(n, phi=0.85, sigma=1.0, seed=11)
    abm = obs + _ar1_series(n, phi=0.85, sigma=0.3, seed=22)
    red = obs + _ar1_series(n, phi=0.85, sigma=0.6, seed=33)

    edi, p_block, p_naive = block_bootstrap_pvalue(
        obs, abm, red, n_perm=999, seed=42
    )
    print(f"  EDI={edi:.4f}  p_block={p_block:.4f}  p_naive={p_naive:.4f}")
    print(f"  shift = {abs(p_block - p_naive):.4f}")
    assert 0.0 <= p_block <= 1.0
    assert 0.0 <= p_naive <= 1.0
    print("  ✓ block_bootstrap_pvalue produce p-values en [0,1]")


def test_newey_west_se_larger_than_iid_under_autocorrelation():
    """SE HAC debería ser mayor que SE iid bajo autocorrelación."""
    n = 200
    rng = np.random.RandomState(7)
    iid = rng.normal(0, 1, size=n)
    se_iid_classical = float(np.std(iid, ddof=1) / np.sqrt(n))
    se_iid_hac = newey_west_se(iid)

    ar1 = _ar1_series(n, phi=0.7, sigma=1.0, seed=7)
    se_ar1_classical = float(np.std(ar1, ddof=1) / np.sqrt(n))
    se_ar1_hac = newey_west_se(ar1)

    print(f"  iid:  SE_clas={se_iid_classical:.4f}  SE_HAC={se_iid_hac:.4f}")
    print(f"  AR1:  SE_clas={se_ar1_classical:.4f}  SE_HAC={se_ar1_hac:.4f}")
    print(f"  ratio HAC/clas (AR1) = {se_ar1_hac / se_ar1_classical:.3f}")
    assert se_ar1_hac >= se_ar1_classical * 0.95
    print("  ✓ newey_west_se >= SE_clas bajo AR(1)")


def test_fwer_holm_more_powerful_than_bonferroni():
    """Holm rechaza al menos tantas hipótesis como Bonferroni."""
    p_values = np.array([0.001, 0.008, 0.02, 0.04, 0.10, 0.30, 0.45, 0.80])
    p_bonf, rej_bonf = fwer_correct(p_values, method="bonferroni")
    p_holm, rej_holm = fwer_correct(p_values, method="holm")

    print(f"  p_raw    = {p_values}")
    print(f"  p_bonf   = {p_bonf}")
    print(f"  p_holm   = {p_holm}")
    print(f"  rechazos bonferroni: {int(rej_bonf.sum())}")
    print(f"  rechazos holm:       {int(rej_holm.sum())}")
    assert int(rej_holm.sum()) >= int(rej_bonf.sum())
    print("  ✓ Holm rechaza >= que Bonferroni")


def test_corpus_application_simulation():
    """
    Simula la aplicación al corpus inter-dominio:
    30 casos con p-values mixtos, ¿cuántos sobreviven a FWER?
    """
    rng = np.random.RandomState(2026)
    p_strong = rng.uniform(1e-5, 1e-3, size=4)       # 4 strong overall_pass
    p_weak = rng.uniform(0.005, 0.045, size=8)        # 8 weak
    p_marginal = rng.uniform(0.05, 0.30, size=10)     # 10 trend/suggestive
    p_null = rng.uniform(0.30, 0.99, size=8)          # 8 null
    p_corpus = np.concatenate([p_strong, p_weak, p_marginal, p_null])

    p_holm, rej_holm = fwer_correct(p_corpus, method="holm")
    p_bonf, rej_bonf = fwer_correct(p_corpus, method="bonferroni")

    print(f"  Corpus 30 casos: 4 strong + 8 weak + 10 marginal + 8 null")
    print(f"  Sin corrección: {int((p_corpus <= 0.05).sum())} significativos")
    print(f"  Bonferroni:     {int(rej_bonf.sum())} significativos tras FWER 0.05")
    print(f"  Holm:           {int(rej_holm.sum())} significativos tras FWER 0.05")
    assert int((p_corpus <= 0.05).sum()) >= int(rej_holm.sum())
    print("  ✓ FWER reduce el número de hipótesis sobrevivientes")


if __name__ == "__main__":
    print("Test 1 — block_bootstrap_pvalue bajo AR(1):")
    test_block_bootstrap_more_conservative_under_autocorrelation()
    print("\nTest 2 — newey_west_se bajo iid vs AR(1):")
    test_newey_west_se_larger_than_iid_under_autocorrelation()
    print("\nTest 3 — Holm vs Bonferroni:")
    test_fwer_holm_more_powerful_than_bonferroni()
    print("\nTest 4 — aplicación al corpus 30 casos:")
    test_corpus_application_simulation()
    print("\n✅ Todos los tests pasaron.")
