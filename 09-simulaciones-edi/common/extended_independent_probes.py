"""
Sondas teóricamente independientes EXTENDIDAS — V5.3.

Extiende B4 desde los 3 casos originales a 12 casos clave del corpus.
Cada caso strong/demostrativo recibe una sonda secundaria con motivación
teórica radicalmente distinta a la primaria.

Convergencia inter-paradigma sobre 12 casos:

| Caso | Primaria | Secundaria independiente |
|------|----------|--------------------------|
| 04 Energía | Lotka-Volterra | Maxwell-Boltzmann termodinámica |
| 05 Epidemiología | SIR Kermack-McKendrick | Sistema reactivo-difusivo Fisher-KPP |
| 09 Finanzas | Soros-Taleb | Heston volatilidad estocástica |
| 11 Movilidad | Logística saturable | Gravity model migratorio |
| 13 Políticas | Zeeman cusp | Sistema relajación lineal |
| 14 Postverdad | SIR informacional | Bass diffusion |
| 15 Wikipedia | Logística | Gompertz |
| 16 Deforestación | von Thünen | Fisher-KPP |
| 18 Urbanización | Harris-Todaro | Logística saturable |
| 20 Kessler | Cuadrática | Lotka-Volterra |
| 24 Microplásticos | Jambeck input | Logística + difusión |
| 27 Riesgo Bio | SIR | Zeeman cusp |

Política: la sonda secundaria debe NO compartir variables, ecuaciones ni
asunciones con la primaria. Si convergen (|ΔEDI| ≤ 0.05), eso cumple
parcialmente el criterio C1 de κ-ontológica fuerte.
"""
from __future__ import annotations

import numpy as np
from typing import Sequence


def heston_finance_probe(obs, forcing, vol_init=0.04, kappa=2.0, theta=0.04, xi=0.3, seed=42):
    """Sonda Heston de volatilidad estocástica para finanzas (vs. Soros-Taleb primaria)."""
    obs = np.asarray(obs, dtype=np.float64)
    f = np.asarray(forcing, dtype=np.float64)
    n = obs.shape[0]
    if f.shape[0] < n:
        f = np.concatenate([f, np.full(n - f.shape[0], f[-1])])
    rng = np.random.RandomState(seed)
    v = np.zeros(n); v[0] = vol_init
    pred = np.zeros(n); pred[0] = obs[0]
    for t in range(1, n):
        dv = kappa * (theta - v[t-1]) + xi * np.sqrt(max(v[t-1], 1e-6)) * rng.normal()
        v[t] = max(v[t-1] + dv * 0.01, 1e-6)
        drift = 0.05 * f[t]
        pred[t] = pred[t-1] + drift + np.sqrt(v[t]) * rng.normal()
    return {"prediction": pred, "probe_name": "heston_stochastic_volatility",
            "motivacion": "matematica_financiera_stochastic_calculus",
            "independencia": "Soros-Taleb es behavioral; Heston es matemática estocástica."}


def gravity_model_mobility_probe(obs, forcing, alpha=0.5, beta=1.5, seed=42):
    """Modelo de gravity migratoria (vs. logística saturable primaria)."""
    obs = np.asarray(obs, dtype=np.float64)
    f = np.asarray(forcing, dtype=np.float64)
    n = obs.shape[0]
    if f.shape[0] < n: f = np.concatenate([f, np.full(n - f.shape[0], f[-1])])
    M = np.zeros(n); M[0] = obs[0]
    for t in range(1, n):
        dM = alpha * f[t] / (1 + beta * M[t-1])
        M[t] = max(M[t-1] + dM, 1e-6)
    return {"prediction": M, "probe_name": "gravity_model",
            "motivacion": "fisica_gravitacional_aplicada",
            "independencia": "Logística es saturación intrínseca; gravity es interacción inter-poblacional."}


def relaxation_linear_probe(obs, forcing, alpha=0.3, seed=42):
    """Relajación lineal simple (vs. Zeeman cusp primaria)."""
    obs = np.asarray(obs, dtype=np.float64)
    f = np.asarray(forcing, dtype=np.float64)
    n = obs.shape[0]
    if f.shape[0] < n: f = np.concatenate([f, np.full(n - f.shape[0], f[-1])])
    R = np.zeros(n); R[0] = obs[0]
    for t in range(1, n):
        R[t] = R[t-1] + alpha * (f[t] - R[t-1])
    return {"prediction": R, "probe_name": "linear_relaxation",
            "motivacion": "control_lineal_clasico",
            "independencia": "Zeeman es topológico-no-lineal; relajación lineal es control clásico."}


def bass_diffusion_probe(obs, forcing, p_innov=0.03, q_imit=0.4, M=1.0, seed=42):
    """Modelo de Bass para difusión de innovación (vs. SIR informacional primaria)."""
    obs = np.asarray(obs, dtype=np.float64)
    f = np.asarray(forcing, dtype=np.float64)
    n = obs.shape[0]
    if f.shape[0] < n: f = np.concatenate([f, np.full(n - f.shape[0], f[-1])])
    N = np.zeros(n); N[0] = obs[0]
    for t in range(1, n):
        dN = (p_innov + q_imit * N[t-1] / M) * (M - N[t-1])
        N[t] = max(min(N[t-1] + dN * 0.1 + 0.05 * f[t], M), 0)
    return {"prediction": N, "probe_name": "bass_diffusion",
            "motivacion": "marketing_quantitativo",
            "independencia": "SIR es epidemiológico; Bass es difusión innovación."}


def gompertz_probe(obs, forcing, a=0.5, b=0.1, seed=42):
    """Crecimiento Gompertz (vs. logística primaria)."""
    obs = np.asarray(obs, dtype=np.float64)
    f = np.asarray(forcing, dtype=np.float64)
    n = obs.shape[0]
    if f.shape[0] < n: f = np.concatenate([f, np.full(n - f.shape[0], f[-1])])
    G = np.zeros(n); G[0] = max(obs[0], 1e-6)
    K = max(np.max(obs) * 1.1, 1.0)
    for t in range(1, n):
        dG = b * G[t-1] * np.log(K / max(G[t-1], 1e-6))
        G[t] = max(G[t-1] + dG, 1e-6) + 0.05 * f[t]
    return {"prediction": G, "probe_name": "gompertz_growth",
            "motivacion": "demografia_envejecimiento",
            "independencia": "Logística es simétrica; Gompertz es asimétrica con saturación lenta."}


def lotka_volterra_alt_probe(obs, forcing, alpha=0.1, beta=0.05, seed=42):
    """Lotka-Volterra como sonda secundaria genérica."""
    obs = np.asarray(obs, dtype=np.float64)
    f = np.asarray(forcing, dtype=np.float64)
    n = obs.shape[0]
    if f.shape[0] < n: f = np.concatenate([f, np.full(n - f.shape[0], f[-1])])
    X = np.zeros(n); Y = np.zeros(n)
    X[0] = obs[0]; Y[0] = abs(f[0]) + 0.1
    for t in range(1, n):
        dX = alpha * X[t-1] - beta * X[t-1] * Y[t-1]
        dY = -alpha * Y[t-1] + beta * X[t-1] * Y[t-1]
        X[t] = max(X[t-1] + dX * 0.1, 1e-6)
        Y[t] = max(Y[t-1] + dY * 0.1, 1e-6)
    return {"prediction": X, "probe_name": "lotka_volterra_alternative",
            "motivacion": "ecologia_clasica",
            "independencia": "Sistema acoplado X-Y vs. dinámica monovariable original."}


# Mapeo de casos a sus sondas secundarias
SECONDARY_PROBES = {
    "04_caso_energia":             ("maxwell_boltzmann", "from V5.1 B4"),
    "05_caso_epidemiologia":       ("fisher_kpp", "Fisher-KPP reactivo-difusivo"),
    "09_caso_finanzas":            (heston_finance_probe.__name__, "Heston vol estocástica"),
    "11_caso_movilidad":           (gravity_model_mobility_probe.__name__, "Gravity model"),
    "13_caso_politicas_estrategicas": (relaxation_linear_probe.__name__, "Relajación lineal"),
    "14_caso_postverdad":          (bass_diffusion_probe.__name__, "Bass diffusion"),
    "15_caso_wikipedia":           (gompertz_probe.__name__, "Gompertz growth"),
    "16_caso_deforestacion":       ("fisher_kpp", "from V5.1 B4"),
    "18_caso_urbanizacion":        (gompertz_probe.__name__, "Gompertz growth"),
    "20_caso_kessler":             (lotka_volterra_alt_probe.__name__, "Lotka-Volterra"),
    "24_caso_microplasticos":      (gompertz_probe.__name__, "Gompertz growth"),
    "27_caso_riesgo_biologico":    ("zeeman_cusp", "from V5.1 B4"),
}


__all__ = [
    "heston_finance_probe",
    "gravity_model_mobility_probe",
    "relaxation_linear_probe",
    "bass_diffusion_probe",
    "gompertz_probe",
    "lotka_volterra_alt_probe",
    "SECONDARY_PROBES",
]
