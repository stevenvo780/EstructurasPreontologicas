"""abm.py — Behavioral Dynamics ABM.

Modelo micro: agentes en grilla 40x40 que representan estados de heading
durante locomoción dirigida. Cada agente experimenta:
  - difusión espacial (variabilidad inter-individual);
  - ruido motor (variabilidad intra-individual);
  - acoplamiento al estado macro (flujo óptico + dirección a meta).

Referencias:
  Fajen, B. R., & Warren, W. H. (2003). Behavioral dynamics of steering,
  obstacle avoidance, and route selection. JEP:HPP, 29(2), 343-362.
  Warren, W. H. (2006). The dynamics of perception and action.
  Psychological Review, 113(2), 358-389.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "heading_error"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # Locomoción dirigida tiene gradiente uniforme: el flujo óptico
        # afecta a todos los agentes de manera similar (no hay zona "central"
        # privilegiada como en deforestación).
        p["forcing_gradient_type"] = "uniform"
    if "forcing_gradient_strength" not in p:
        # Gradiente moderado: información ecológica es disponible pero
        # con variabilidad perceptiva entre agentes (cf. Fink y Warren 2002).
        p["forcing_gradient_strength"] = 0.30
    if "heterogeneity_strength" not in p:
        # Variabilidad inter-individual moderada: distintos agentes tienen
        # parámetros biomecánicos ligeramente distintos (longitud de paso,
        # velocidad preferida, sensibilidad perceptiva).
        p["heterogeneity_strength"] = 0.20
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)
