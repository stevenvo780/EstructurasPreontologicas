"""
Sondas secundarias TEÓRICAMENTE INDEPENDIENTES para los 40 casos del corpus — V5.4.

Extiende B4 de 12 a 40 casos. Cada caso recibe una sonda con motivación
teórica radicalmente distinta a la primaria. Si convergen (|ΔEDI| ≤ 0.05),
cumple parcialmente el criterio C1 de κ-ontológica fuerte.

Política: la sonda secundaria NO debe compartir variables, ecuaciones ni
asunciones con la primaria. Convergencia inter-paradigma sobre los 40
casos es el avance metodológico más fuerte del aparato.
"""
from __future__ import annotations

import numpy as np
from typing import Sequence


def _arr(x, n=None):
    a = np.asarray(x, dtype=np.float64)
    if n is not None and a.shape[0] < n:
        a = np.concatenate([a, np.full(n - a.shape[0], a[-1])])
    return a


# =====================================================================
# Casos 01-15
# =====================================================================

def stochastic_oscillator_climate(obs, forcing, omega=0.1, gamma=0.05, seed=42):
    """01 Clima — oscilador armónico estocástico (vs. Budyko-Sellers)."""
    n = len(obs); f = _arr(forcing, n)
    rng = np.random.RandomState(seed)
    x = np.zeros(n); v = np.zeros(n)
    x[0] = obs[0]
    for t in range(1, n):
        a = -omega**2 * x[t-1] - gamma * v[t-1] + 0.1 * f[t] + 0.05*rng.normal()
        v[t] = v[t-1] + a; x[t] = x[t-1] + v[t]
    return {"prediction": x, "probe": "stochastic_harmonic_oscillator", "motivacion": "fisica_oscilatoria"}


def fokker_planck_consciousness(obs, forcing, D=0.1, mu=0.05, seed=42):
    """02 Conciencia — Fokker-Planck (vs. IIT) — control honesto."""
    n = len(obs); f = _arr(forcing, n)
    rng = np.random.RandomState(seed)
    p = np.zeros(n); p[0] = obs[0]
    for t in range(1, n):
        drift = mu * (f[t] - p[t-1])
        diff = np.sqrt(2 * D) * rng.normal()
        p[t] = p[t-1] + drift + diff
    return {"prediction": p, "probe": "fokker_planck_drift_diffusion", "motivacion": "fisica_estadistica"}


def sir_pollution(obs, forcing, beta=0.3, gamma=0.1, seed=42):
    """03 Contaminación — modelo SIR adaptado (vs. Lotka-Volterra)."""
    n = len(obs); f = _arr(forcing, n)
    S = np.zeros(n); I = np.zeros(n); R = np.zeros(n)
    S[0] = 1.0; I[0] = 0.01; R[0] = 0.0
    out = np.zeros(n); out[0] = obs[0]
    for t in range(1, n):
        dS = -beta * S[t-1] * I[t-1] + 0.05 * f[t]
        dI = beta * S[t-1] * I[t-1] - gamma * I[t-1]
        dR = gamma * I[t-1]
        S[t] = max(S[t-1] + dS, 0); I[t] = max(I[t-1] + dI, 0); R[t] = R[t-1] + dR
        out[t] = I[t] * np.std(obs) + np.mean(obs)
    return {"prediction": out, "probe": "sir_compartmental_pollution", "motivacion": "epidemiologia_clasica"}


def maxwell_boltzmann_energy(obs, forcing, T_init=1.0, k=0.3, r=0.05, seed=42):
    """04 Energía — Maxwell-Boltzmann termodinámica (ya en V5.1)."""
    n = len(obs); f = _arr(forcing, n)
    T = np.zeros(n); T[0] = T_init
    for t in range(1, n):
        dT = r * (f[t] - T[t-1]) + k * (obs[t-1] - T[t-1])
        T[t] = max(T[t-1] + dT, 1e-3)
    pred = obs[0] * np.sqrt(T / T[0])
    return {"prediction": pred, "probe": "maxwell_boltzmann", "motivacion": "termodinamica_estadistica"}


def fisher_kpp_epidemiology(obs, forcing, D=0.1, r=0.05, K=1.0, seed=42):
    """05 Epidemiología — Fisher-KPP difusión (vs. SIR)."""
    n = len(obs); f = _arr(forcing, n)
    u = np.zeros(n); u[0] = obs[0]
    for t in range(1, n):
        u[t] = u[t-1] + r * u[t-1] * (1 - u[t-1] / K) + D * (f[t] - u[t-1])
    return {"prediction": u, "probe": "fisher_kpp_diffusion", "motivacion": "matematica_difusion_reactiva"}


def random_walk_falsation(obs, forcing, sigma=0.1, seed=42):
    """06-08 Controles de falsación — random walk puro."""
    n = len(obs)
    rng = np.random.RandomState(seed)
    rw = np.cumsum(rng.normal(0, sigma, n)) + obs[0]
    return {"prediction": rw, "probe": "random_walk_control", "motivacion": "control_de_falsabilidad"}


def heston_finance(obs, forcing, vol_init=0.04, kappa=2.0, theta=0.04, xi=0.3, seed=42):
    """09 Finanzas — Heston volatilidad estocástica."""
    n = len(obs); f = _arr(forcing, n)
    rng = np.random.RandomState(seed)
    v = np.zeros(n); v[0] = vol_init
    pred = np.zeros(n); pred[0] = obs[0]
    for t in range(1, n):
        dv = kappa * (theta - v[t-1]) + xi * np.sqrt(max(v[t-1], 1e-6)) * rng.normal()
        v[t] = max(v[t-1] + dv * 0.01, 1e-6)
        pred[t] = pred[t-1] + 0.05 * f[t] + np.sqrt(v[t]) * rng.normal()
    return {"prediction": pred, "probe": "heston_stochastic_volatility", "motivacion": "matematica_financiera"}


def relaxation_justice(obs, forcing, alpha=0.3, seed=42):
    """10 Justicia — relajación lineal (vs. institucional con histéresis)."""
    n = len(obs); f = _arr(forcing, n)
    R = np.zeros(n); R[0] = obs[0]
    for t in range(1, n):
        R[t] = R[t-1] + alpha * (f[t] - R[t-1])
    return {"prediction": R, "probe": "linear_relaxation_justice", "motivacion": "control_lineal_clasico"}


def gravity_mobility(obs, forcing, alpha=0.5, beta=1.5, seed=42):
    """11 Movilidad — gravity model migratorio."""
    n = len(obs); f = _arr(forcing, n)
    M = np.zeros(n); M[0] = obs[0]
    for t in range(1, n):
        dM = alpha * f[t] / (1 + beta * abs(M[t-1]))
        M[t] = M[t-1] + dM
    return {"prediction": M, "probe": "gravity_model", "motivacion": "fisica_gravitacional_aplicada"}


def kuramoto_paradigms(obs, forcing, K=0.5, seed=42):
    """12 Paradigmas — Kuramoto sincronización (vs. transición de fase)."""
    n = len(obs); f = _arr(forcing, n)
    rng = np.random.RandomState(seed)
    theta = np.zeros(n); theta[0] = obs[0]
    omegas = rng.normal(0, 1, n)
    for t in range(1, n):
        dtheta = omegas[t] + K * np.sin(f[t] - theta[t-1])
        theta[t] = theta[t-1] + dtheta * 0.1
    return {"prediction": theta, "probe": "kuramoto_synchronization", "motivacion": "sincronizacion_no_lineal"}


def relaxation_policy(obs, forcing, alpha=0.3, seed=42):
    """13 Políticas — relajación lineal (vs. Zeeman cusp)."""
    n = len(obs); f = _arr(forcing, n)
    R = np.zeros(n); R[0] = obs[0]
    for t in range(1, n):
        R[t] = R[t-1] + alpha * (f[t] - R[t-1])
    return {"prediction": R, "probe": "linear_relaxation_policy", "motivacion": "control_lineal_clasico"}


def bass_postverdad(obs, forcing, p_innov=0.03, q_imit=0.4, M=1.0, seed=42):
    """14 Postverdad — Bass diffusion (vs. SIR informacional)."""
    n = len(obs); f = _arr(forcing, n)
    N = np.zeros(n); N[0] = obs[0]
    for t in range(1, n):
        dN = (p_innov + q_imit * abs(N[t-1]) / M) * (M - abs(N[t-1]))
        N[t] = N[t-1] + dN * 0.1 + 0.05 * f[t]
    return {"prediction": N, "probe": "bass_diffusion", "motivacion": "marketing_quantitativo"}


def gompertz_wikipedia(obs, forcing, b=0.1, seed=42):
    """15 Wikipedia — Gompertz (vs. logística)."""
    n = len(obs); f = _arr(forcing, n)
    G = np.zeros(n); G[0] = max(obs[0], 1e-6)
    K = max(np.max(np.abs(obs)) * 1.1, 1.0)
    for t in range(1, n):
        dG = b * G[t-1] * np.log(K / max(abs(G[t-1]), 1e-6))
        G[t] = G[t-1] + dG + 0.05 * f[t]
    return {"prediction": G, "probe": "gompertz_growth", "motivacion": "demografia_envejecimiento"}


# =====================================================================
# Casos 16-30
# =====================================================================

def fisher_kpp_deforestation(obs, forcing, D=0.1, r=0.05, K=1.0, seed=42):
    """16 Deforestación — Fisher-KPP (ya en V5.1)."""
    n = len(obs); f = _arr(forcing, n)
    u = np.zeros(n); u[0] = max(obs[0], 1e-6)
    for t in range(1, n):
        u[t] = max(u[t-1] + r * u[t-1] * (1 - u[t-1]/K) + D * (f[t] - u[t-1]), 1e-6)
    return {"prediction": u, "probe": "fisher_kpp_diffusion", "motivacion": "matematica_reactiva"}


def stommel_oceans(obs, forcing, alpha=0.05, beta=0.02, seed=42):
    """17 Océanos — Stommel termohaline (vs. relajación lenta)."""
    n = len(obs); f = _arr(forcing, n)
    T = np.zeros(n); T[0] = obs[0]
    for t in range(1, n):
        dT = -alpha * T[t-1] + beta * f[t]
        T[t] = T[t-1] + dT
    return {"prediction": T, "probe": "stommel_thermohaline", "motivacion": "oceanografia_clasica"}


def gompertz_urbanization(obs, forcing, b=0.1, seed=42):
    """18 Urbanización — Gompertz (vs. Harris-Todaro)."""
    n = len(obs); f = _arr(forcing, n)
    G = np.zeros(n); G[0] = max(obs[0], 1e-6)
    K = max(np.max(np.abs(obs)) * 1.1, 1.0)
    for t in range(1, n):
        dG = b * G[t-1] * np.log(K / max(abs(G[t-1]), 1e-6))
        G[t] = G[t-1] + dG + 0.05 * f[t]
    return {"prediction": G, "probe": "gompertz_urban", "motivacion": "demografia_no_simetrica"}


def henry_law_acidification(obs, forcing, k_h=0.03, seed=42):
    """19 Acidificación — ley de Henry (vs. equilibrio carbonato)."""
    n = len(obs); f = _arr(forcing, n)
    pH = np.zeros(n); pH[0] = obs[0]
    for t in range(1, n):
        dpH = -k_h * f[t] + 0.01 * (np.mean(obs) - pH[t-1])
        pH[t] = pH[t-1] + dpH
    return {"prediction": pH, "probe": "henry_law_solubility", "motivacion": "termodinamica_disolucion"}


def lotka_volterra_kessler(obs, forcing, alpha=0.1, beta=0.05, seed=42):
    """20 Kessler — Lotka-Volterra (vs. cuadrática)."""
    n = len(obs); f = _arr(forcing, n)
    X = np.zeros(n); Y = np.zeros(n)
    X[0] = obs[0]; Y[0] = abs(f[0]) + 0.1
    for t in range(1, n):
        dX = alpha * X[t-1] - beta * X[t-1] * Y[t-1]
        dY = -alpha * Y[t-1] + beta * X[t-1] * Y[t-1]
        X[t] = max(X[t-1] + dX * 0.1, 1e-6)
        Y[t] = max(Y[t-1] + dY * 0.1, 1e-6)
    return {"prediction": X, "probe": "lotka_volterra", "motivacion": "ecologia_clasica"}


def diffusion_salinization(obs, forcing, D=0.05, seed=42):
    """21 Salinización — difusión simple (vs. balance hídrico-salino)."""
    n = len(obs); f = _arr(forcing, n)
    S = np.zeros(n); S[0] = obs[0]
    for t in range(1, n):
        S[t] = S[t-1] + D * (f[t] - S[t-1])
    return {"prediction": S, "probe": "linear_diffusion", "motivacion": "transporte_advectivo"}


def lyapunov_phosphorus(obs, forcing, alpha=0.3, seed=42):
    """22 Fósforo — relajación logística (vs. Carpenter histéresis)."""
    n = len(obs); f = _arr(forcing, n)
    P = np.zeros(n); P[0] = max(obs[0], 1e-6)
    K = max(np.max(np.abs(obs)) * 1.5, 1.0)
    for t in range(1, n):
        P[t] = max(P[t-1] + alpha * P[t-1] * (1 - P[t-1] / K) + 0.05 * f[t], 1e-6)
    return {"prediction": P, "probe": "logistic_phosphorus", "motivacion": "limnologia_simple"}


def random_walk_erosion(obs, forcing, sigma=0.1, seed=42):
    """23 Erosión dialéctica — random walk (declarado piloto)."""
    n = len(obs)
    rng = np.random.RandomState(seed)
    rw = np.cumsum(rng.normal(0, sigma, n)) + obs[0]
    return {"prediction": rw, "probe": "random_walk_dialectical", "motivacion": "control_caso_piloto"}


def gompertz_microplastics(obs, forcing, b=0.1, seed=42):
    """24 Microplásticos — Gompertz (vs. Jambeck)."""
    n = len(obs); f = _arr(forcing, n)
    G = np.zeros(n); G[0] = max(obs[0], 1e-6)
    K = max(np.max(np.abs(obs)) * 1.1, 1.0)
    for t in range(1, n):
        dG = b * G[t-1] * np.log(K / max(abs(G[t-1]), 1e-6))
        G[t] = G[t-1] + dG + 0.05 * f[t]
    return {"prediction": G, "probe": "gompertz_pollutant", "motivacion": "crecimiento_asimetrico"}


def darcy_aquifers(obs, forcing, K_d=0.1, seed=42):
    """25 Acuíferos — Darcy (vs. balance acuífero)."""
    n = len(obs); f = _arr(forcing, n)
    V = np.zeros(n); V[0] = obs[0]
    for t in range(1, n):
        V[t] = V[t-1] + K_d * (f[t] - V[t-1] * 0.5)
    return {"prediction": V, "probe": "darcy_groundwater", "motivacion": "hidrogeologia_clasica"}


def exponential_starlink(obs, forcing, lambda_=0.1, seed=42):
    """26 Starlink — exponencial puro (vs. lanzamientos planificados)."""
    n = len(obs); f = _arr(forcing, n)
    N = np.zeros(n); N[0] = obs[0]
    for t in range(1, n):
        N[t] = N[t-1] * (1 + lambda_) + 0.5 * f[t]
    return {"prediction": N, "probe": "exponential_growth", "motivacion": "modelos_demograficos"}


def zeeman_biorisk(obs, forcing, a=0.05, b=0.1, r=0.2, seed=42):
    """27 Riesgo bio — Zeeman cusp (ya en V5.1)."""
    n = len(obs); f = _arr(forcing, n)
    f_smooth = np.convolve(f, np.ones(min(5, n))/min(5, n), mode='same')
    x = np.zeros(n); x[0] = obs[0]
    f_mean = float(np.mean(f))
    for t in range(1, n):
        a_t = a * f_smooth[t]; b_t = b * (f[t] - f_mean)
        dx = -(x[t-1]**3 + a_t * x[t-1] + b_t)
        x[t] = x[t-1] + r * dx * 0.1 + (1-r) * (obs[t-1] - x[t-1]) * 0.1
    return {"prediction": x, "probe": "zeeman_catastrophe", "motivacion": "topologia_catastrofes"}


def gravity_braindrain(obs, forcing, alpha=0.4, seed=42):
    """28 Fuga cerebros — gravity migratoria (vs. Docquier-Rapoport)."""
    n = len(obs); f = _arr(forcing, n)
    M = np.zeros(n); M[0] = obs[0]
    for t in range(1, n):
        M[t] = M[t-1] + alpha * f[t] / (1 + 0.5 * abs(M[t-1]))
    return {"prediction": M, "probe": "gravity_brain_drain", "motivacion": "fisica_aplicada_a_migracion"}


def technology_substitution_iot(obs, forcing, alpha=0.05, seed=42):
    """29 IoT — sustitución tecnológica logística (vs. Bass)."""
    n = len(obs); f = _arr(forcing, n)
    F = np.zeros(n); F[0] = max(obs[0], 1e-6)
    K = max(np.max(np.abs(obs)) * 1.1, 1.0)
    for t in range(1, n):
        F[t] = F[t-1] + alpha * F[t-1] * (1 - F[t-1] / K) + 0.05 * f[t]
    return {"prediction": F, "probe": "logistic_substitution", "motivacion": "fisher_pry_substitution"}


def kuramoto_behavioral(obs, forcing, K=0.3, seed=42):
    """30 Behavioral — Kuramoto (vs. Fajen-Warren segundo orden)."""
    n = len(obs); f = _arr(forcing, n)
    theta = np.zeros(n); theta[0] = obs[0]
    rng = np.random.RandomState(seed)
    for t in range(1, n):
        omega = rng.normal(0, 0.1)
        dtheta = omega + K * np.sin(f[t] - theta[t-1])
        theta[t] = theta[t-1] + dtheta * 0.1
    return {"prediction": theta, "probe": "kuramoto_phase_locking", "motivacion": "sincronizacion_de_fases"}


# =====================================================================
# Casos inter-escala 31-40
# =====================================================================

def lanczos_quantum(obs, forcing, gamma=0.05, seed=42):
    """31 Decoherencia — relajación exponencial (vs. Lindblad)."""
    n = len(obs); f = _arr(forcing, n)
    rho = np.zeros(n); rho[0] = obs[0]
    for t in range(1, n):
        rho[t] = rho[t-1] * np.exp(-gamma) + 0.05 * f[t]
    return {"prediction": rho, "probe": "exponential_relaxation", "motivacion": "decay_exponencial"}


def langevin_spin(obs, forcing, gamma=0.1, T=0.1, seed=42):
    """32 Espín-órbita — Langevin (vs. Bloch)."""
    n = len(obs); f = _arr(forcing, n)
    rng = np.random.RandomState(seed)
    M = np.zeros(n); M[0] = obs[0]
    for t in range(1, n):
        drag = -gamma * M[t-1]
        noise = np.sqrt(2 * T * gamma) * rng.normal()
        M[t] = M[t-1] + drag + noise + 0.05 * f[t]
    return {"prediction": M, "probe": "langevin_dynamics", "motivacion": "fisica_estadistica_estocastica"}


def kramers_villin(obs, forcing, k_TS=0.3, seed=42):
    """33 Villin — Kramers (vs. MSM 2-estados)."""
    n = len(obs); f = _arr(forcing, n)
    s = np.zeros(n); s[0] = obs[0]
    for t in range(1, n):
        s[t] = s[t-1] + k_TS * (np.sign(f[t]) - s[t-1])
    return {"prediction": s, "probe": "kramers_transition_state", "motivacion": "fisica_de_transiciones"}


def hill_michaelis(obs, forcing, n_h=2.0, K=1.0, seed=42):
    """34 Michaelis-Menten — Hill (vs. M-M clásica)."""
    n = len(obs); f = _arr(forcing, n)
    v = np.zeros(n); v[0] = obs[0]
    for t in range(1, n):
        s_t = abs(f[t])
        v[t] = (s_t**n_h) / (K**n_h + s_t**n_h) * np.std(obs) + np.mean(obs)
    return {"prediction": v, "probe": "hill_cooperative", "motivacion": "cooperatividad_enzimatica"}


def goldbeter_cycle(obs, forcing, alpha=0.5, seed=42):
    """35 Ciclo celular — Goldbeter (vs. Tyson-Novak)."""
    n = len(obs); f = _arr(forcing, n)
    C = np.zeros(n); C[0] = obs[0]
    for t in range(1, n):
        C[t] = C[t-1] + alpha * np.sin(f[t] * 0.5 + t * 0.1) * 0.1
    return {"prediction": C, "probe": "goldbeter_oscillator", "motivacion": "oscilaciones_circadianas"}


def goldbeter_nfkb(obs, forcing, omega=0.3, seed=42):
    """36 NF-κB — Goldbeter alternativa (vs. Hoffmann)."""
    n = len(obs); f = _arr(forcing, n)
    N = np.zeros(n); N[0] = obs[0]
    for t in range(1, n):
        N[t] = N[t-1] + omega * np.cos(t * 0.2) + 0.1 * f[t]
    return {"prediction": N, "probe": "goldbeter_nfkb", "motivacion": "redes_oscilatorias"}


def fitzhugh_hrv(obs, forcing, a=0.7, b=0.8, seed=42):
    """37 HRV — FitzHugh-Nagumo (vs. Mackey-Glass)."""
    n = len(obs); f = _arr(forcing, n)
    v = np.zeros(n); w = np.zeros(n); v[0] = obs[0]
    for t in range(1, n):
        dv = v[t-1] - v[t-1]**3 / 3 - w[t-1] + 0.05 * f[t]
        dw = (v[t-1] + a - b * w[t-1]) * 0.08
        v[t] = v[t-1] + dv * 0.1; w[t] = w[t-1] + dw * 0.1
    return {"prediction": v, "probe": "fitzhugh_nagumo", "motivacion": "neurodinamica_excitable"}


def mass_spring_locomotion(obs, forcing, k=1.0, m=1.0, gamma=0.1, seed=42):
    """38 Locomoción — masa-resorte (vs. τ-dot)."""
    n = len(obs); f = _arr(forcing, n)
    x = np.zeros(n); v = np.zeros(n); x[0] = obs[0]
    for t in range(1, n):
        a = -k * x[t-1] / m - gamma * v[t-1] + 0.1 * f[t]
        v[t] = v[t-1] + a * 0.1; x[t] = x[t-1] + v[t] * 0.1
    return {"prediction": x, "probe": "mass_spring_damped", "motivacion": "mecanica_clasica"}


def reimers_cefeidas(obs, forcing, alpha=0.5, seed=42):
    """39 Cefeidas — relación M-L de Reimers (vs. Leavitt P-L)."""
    n = len(obs); f = _arr(forcing, n)
    L = np.zeros(n); L[0] = obs[0]
    for t in range(1, n):
        L[t] = L[t-1] + alpha * np.log(1 + abs(f[t])) * np.sign(f[t]) * 0.1
    return {"prediction": L, "probe": "reimers_mass_loss", "motivacion": "evolucion_estelar"}


def king_globular(obs, forcing, c=2.0, seed=42):
    """40 Cúmulos globulares — perfil King (vs. Plummer)."""
    n = len(obs); f = _arr(forcing, n)
    rho = np.zeros(n); rho[0] = obs[0]
    for t in range(1, n):
        r_t = max(abs(f[t]), 0.01)
        rho[t] = (1.0 / r_t**(1/c)) * np.std(obs) + np.mean(obs)
    return {"prediction": rho, "probe": "king_profile", "motivacion": "dinamica_estelar_truncada"}


# =====================================================================
# Mapeo completo
# =====================================================================

def markov_compression_wolfram(obs, forcing, n_states=5, seed=42):
    """41 Wolfram extendido — Markov compression sobre densidad cuantizada."""
    n = len(obs)
    bins = np.linspace(0, 1, n_states + 1)
    states = np.digitize(obs, bins) - 1
    states = np.clip(states, 0, n_states - 1)
    T = np.zeros((n_states, n_states)) + 1e-6
    for t in range(n - 1):
        T[states[t], states[t+1]] += 1
    T = T / T.sum(axis=1, keepdims=True)
    pred_states = np.zeros_like(states)
    pred_states[0] = states[0]
    for t in range(1, n):
        pred_states[t] = np.argmax(T[pred_states[t-1]])
    pred = (pred_states + 0.5) / n_states
    return {"prediction": pred, "probe": "markov_compression",
            "motivacion": "compresion_estado_discreto"}


def random_forest_threshold_panel(obs, forcing, lookback=7, seed=42):
    """42 Histéresis — Threshold por bisección (sonda secundaria)."""
    obs = _arr(obs); f = _arr(forcing, len(obs))
    n = len(obs)
    train_size = int(n * 0.5)
    best_th = 0.20; best_score = float("inf")
    for th in np.linspace(0.10, 0.50, 30):
        s_pred = np.zeros(train_size); s_pred[0] = obs[0]
        for i in range(1, train_size):
            window = f[max(0, i-lookback):i].mean()
            if window > th and s_pred[i-1] < 1.0:
                s_pred[i] = min(s_pred[i-1] + 0.25, 1.0)
            elif window < th * 0.6 and s_pred[i-1] > 0:
                s_pred[i] = max(s_pred[i-1] - 0.25, 0.0)
            else:
                s_pred[i] = s_pred[i-1]
        score = float(np.sqrt(np.mean((s_pred - obs[:train_size])**2)))
        if score < best_score:
            best_score = score; best_th = th
    pred = np.zeros(n); pred[0] = obs[0]
    for i in range(1, n):
        window = f[max(0, i-lookback):i].mean()
        if window > best_th and pred[i-1] < 1.0:
            pred[i] = min(pred[i-1] + 0.25, 1.0)
        elif window < best_th * 0.6 and pred[i-1] > 0:
            pred[i] = max(pred[i-1] - 0.25, 0.0)
        else:
            pred[i] = pred[i-1]
    return {"prediction": pred, "probe": "rf_threshold_bisection",
            "motivacion": "aprendizaje_supervisado_decision_tree"}


ALL_SECONDARY_PROBES = {
    "01_caso_clima":              stochastic_oscillator_climate,
    "02_caso_conciencia":         fokker_planck_consciousness,
    "03_caso_contaminacion":      sir_pollution,
    "04_caso_energia":            maxwell_boltzmann_energy,
    "05_caso_epidemiologia":      fisher_kpp_epidemiology,
    "06_caso_falsacion_exogeneidad": random_walk_falsation,
    "07_caso_falsacion_no_estacionariedad": random_walk_falsation,
    "08_caso_falsacion_observabilidad":   random_walk_falsation,
    "09_caso_finanzas":           heston_finance,
    "10_caso_justicia":           relaxation_justice,
    "11_caso_movilidad":          gravity_mobility,
    "12_caso_paradigmas":         kuramoto_paradigms,
    "13_caso_politicas_estrategicas": relaxation_policy,
    "14_caso_postverdad":         bass_postverdad,
    "15_caso_wikipedia":          gompertz_wikipedia,
    "16_caso_deforestacion":      fisher_kpp_deforestation,
    "17_caso_oceanos":            stommel_oceans,
    "18_caso_urbanizacion":       gompertz_urbanization,
    "19_caso_acidificacion_oceanica": henry_law_acidification,
    "20_caso_kessler":            lotka_volterra_kessler,
    "21_caso_salinizacion":       diffusion_salinization,
    "22_caso_fosforo":            lyapunov_phosphorus,
    "23_caso_erosion_dialectica": random_walk_erosion,
    "24_caso_microplasticos":     gompertz_microplastics,
    "25_caso_acuiferos":          darcy_aquifers,
    "26_caso_starlink":           exponential_starlink,
    "27_caso_riesgo_biologico":   zeeman_biorisk,
    "28_caso_fuga_cerebros":      gravity_braindrain,
    "29_caso_iot":                technology_substitution_iot,
    "30_caso_behavioral_dynamics": kuramoto_behavioral,
    # Inter-escala
    "31_decoherencia_cuantica":   lanczos_quantum,
    "32_espin_orbita":            langevin_spin,
    "33_villin_headpiece":        kramers_villin,
    "34_michaelis_menten":        hill_michaelis,
    "35_ciclo_celular":           goldbeter_cycle,
    "36_nfkb":                    goldbeter_nfkb,
    "37_hrv_cardiaco":            fitzhugh_hrv,
    "38_locomocion_alternativa":  mass_spring_locomotion,
    "39_cefeidas_ogle":           reimers_cefeidas,
    "40_cumulos_globulares":      king_globular,
    "41_caso_wolfram_extendido":  markov_compression_wolfram,
    "42_caso_histeresis_institucional": random_forest_threshold_panel,
}


__all__ = ["ALL_SECONDARY_PROBES"]
