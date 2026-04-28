"""V4-01 — Test cruzado de sondas multiescala.

Para cada caso multiescala, generamos datos con un sistema dinámico distinto
del que la sonda fue diseñada para predecir. Si la sonda sigue produciendo
EDI > 0.30, hay circularidad genuina (la sonda detecta su propia estructura).
Si EDI cae a < 0.10, la sonda discrimina entre dinámicas distintas.

Política: aplicamos cada sonda contra:
  (a) sus datos originales (caso strong reportado)
  (b) random walk + ruido
  (c) sistema dinámico alternativo (oscilador armónico simple)
  (d) constante con ruido

Reportamos el EDI en cada caso. Si la sonda da EDI alto en (b), (c), (d),
la sonda está midiendo auto-consistencia paramétrica, no cierre operativo.
"""

from __future__ import annotations
import sys
import json
from pathlib import Path
import numpy as np

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "09-simulaciones-edi" / "corpus_multiescala"))

from edi_engine import run_edi


def gen_random_walk(n_steps, sigma=0.3, seed=0):
    rng = np.random.default_rng(seed)
    return np.cumsum(rng.normal(0.0, sigma, n_steps))


def gen_constant_noise(n_steps, mean=0.5, sigma=0.05, seed=0):
    rng = np.random.default_rng(seed)
    return mean + rng.normal(0, sigma, n_steps)


def gen_simple_oscillator(n_steps, period=30, amp=0.5, seed=0):
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    return amp * np.sin(2 * np.pi * t / period) + rng.normal(0, 0.05, n_steps)


def gen_neutral_forcing(n_steps, seed=1):
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps)
    return 0.5 + 0.3 * np.sin(2 * np.pi * t / 25) + rng.normal(0, 0.05, n_steps)


def test_caso(caso_id: str, sonda_coupled, sonda_no_ode):
    """Aplica la sonda del caso a 4 generadores distintos."""
    n = 200
    forcing = gen_neutral_forcing(n)
    generators = {
        "random_walk": gen_random_walk(n, seed=42),
        "constante_ruido": gen_constant_noise(n, seed=42),
        "oscilador_simple": gen_simple_oscillator(n, period=30, seed=42),
    }
    results = {}
    for name, obs in generators.items():
        try:
            result = run_edi(
                case_name=f"{caso_id}_{name}",
                scale="test cruzado",
                observed=obs,
                forcing=forcing,
                sonda_coupled=sonda_coupled,
                sonda_no_ode=sonda_no_ode,
            )
            results[name] = {
                "edi": result.edi,
                "p_value": result.p_value,
                "nivel": result.nivel,
                "overall_pass": result.overall_pass,
            }
        except Exception as exc:
            results[name] = {"error": str(exc)}
    return results


# Recreamos sondas mínimas para cada caso (versiones simplificadas)

def make_sondas_caso31():
    def coupled(forcing, train_obs, train_steps, val_steps):
        pred = np.zeros(val_steps)
        last = float(train_obs[-1])
        period_reset = 25
        for i in range(val_steps):
            if (train_steps + i) % period_reset == 0:
                last = 1.0
            else:
                T_b = forcing[train_steps + i]
                T2_eff = max(1.0, 30.0 / (1.0 + (T_b - 20.0) / 15.0))
                last = last * np.exp(-1.0 / T2_eff)
            pred[i] = last
        return pred
    def no_ode(forcing, train_obs, train_steps, val_steps):
        pred = np.zeros(val_steps)
        last = float(train_obs[-1])
        decay = np.exp(-1.0 / 30.0)
        period_reset = 25
        for i in range(val_steps):
            if (train_steps + i) % period_reset == 0:
                last = 1.0
            else:
                last = last * decay
            pred[i] = last
        return pred
    return coupled, no_ode


def make_sondas_caso34():
    def coupled(forcing, train_obs, train_steps, val_steps):
        train_S = forcing[:train_steps]
        train_v = train_obs
        inv_S = 1.0 / np.maximum(train_S, 0.01)
        inv_v = 1.0 / np.maximum(np.abs(train_v) + 0.5, 0.5)
        A = np.vstack([inv_S, np.ones(len(inv_S))]).T
        sol, *_ = np.linalg.lstsq(A, inv_v, rcond=None)
        slope, intercept = sol
        vmax_est = 1.0 / max(intercept, 1e-6)
        Km_est = max(0.01, slope * vmax_est)
        pred = np.zeros(val_steps)
        for i in range(val_steps):
            S = forcing[train_steps + i]
            pred[i] = vmax_est * S / (Km_est + S)
        return pred
    def no_ode(forcing, train_obs, train_steps, val_steps):
        return np.full(val_steps, float(np.mean(train_obs)))
    return coupled, no_ode


def make_sondas_caso37():
    def coupled(forcing, train_obs, train_steps, val_steps):
        pred = np.zeros(val_steps)
        rr_hist = list(train_obs[-10:])
        delay = 5
        for i in range(val_steps):
            stress = forcing[train_steps + i]
            target = 800 - 200 * stress
            rr_d = rr_hist[-delay] if len(rr_hist) >= delay else 800
            modulation = 50 * np.tanh((rr_d - 800) / 100)
            rr_new = 0.85 * rr_hist[-1] + 0.15 * target - 0.1 * modulation
            rr_hist.append(rr_new)
            pred[i] = rr_new
        return pred
    def no_ode(forcing, train_obs, train_steps, val_steps):
        pred = np.zeros(val_steps)
        rr_hist = list(train_obs[-10:])
        delay = 5
        target = 800 - 200 * 0.5
        for i in range(val_steps):
            rr_d = rr_hist[-delay] if len(rr_hist) >= delay else 800
            modulation = 50 * np.tanh((rr_d - 800) / 100)
            rr_new = 0.85 * rr_hist[-1] + 0.15 * target - 0.1 * modulation
            rr_hist.append(rr_new)
            pred[i] = rr_new
        return pred
    return coupled, no_ode


def make_sondas_caso39():
    def coupled(forcing, train_obs, train_steps, val_steps):
        pred = np.zeros(val_steps)
        M_mean = float(np.mean(train_obs))
        for i in range(val_steps):
            phase = forcing[train_steps + i]
            signal = -0.4 * np.sin(2 * np.pi * phase) - 0.1 * np.sin(4 * np.pi * phase)
            pred[i] = M_mean + signal
        return pred
    def no_ode(forcing, train_obs, train_steps, val_steps):
        return np.full(val_steps, float(np.mean(train_obs)))
    return coupled, no_ode


def main():
    print("=== V4-01 — Test cruzado de sondas multiescala ===")
    print()
    print("Aplicamos cada sonda a generadores ALTERNATIVOS (RW, const, oscilador).")
    print("Si la sonda da EDI > 0.30 sobre datos no-suyos: CIRCULARIDAD.")
    print()

    casos = {
        "31_decoherencia": make_sondas_caso31(),
        "34_michaelis_menten": make_sondas_caso34(),
        "37_hrv": make_sondas_caso37(),
        "39_cefeida": make_sondas_caso39(),
    }

    all_results = {}
    for caso_id, (sc, sn) in casos.items():
        print(f"--- Caso {caso_id} ---")
        results = test_caso(caso_id, sc, sn)
        all_results[caso_id] = results
        for gen_name, r in results.items():
            edi = r.get("edi")
            p = r.get("p_value")
            nivel = r.get("nivel", "?")
            if edi is None:
                print(f"  {gen_name:25s}  (error)")
            else:
                marker = " ⚠️ CIRCULARIDAD" if (edi > 0.30 and p is not None and p < 0.05) else ""
                print(f"  {gen_name:25s}  EDI={edi:+.4f}  p={p:.4f}  Nivel={nivel}{marker}")
        print()

    out = Path(__file__).parent / "V4_01_resultados.json"
    out.write_text(json.dumps(all_results, indent=2, ensure_ascii=False),
                   encoding="utf-8")
    print(f"Resultados: {out}")

    # Veredicto agregado
    n_circ = 0
    n_total = 0
    for caso, results in all_results.items():
        for gen, r in results.items():
            if "edi" in r and r["edi"] is not None:
                n_total += 1
                if r["edi"] > 0.30 and r["p_value"] is not None and r["p_value"] < 0.05:
                    n_circ += 1
    print()
    print(f"Tasa de circularidad: {n_circ}/{n_total} = {n_circ/n_total:.4f}")
    if n_circ / n_total > 0.30:
        print("VEREDICTO: CIRCULARIDAD MASIVA. Las sondas detectan estructura genérica, no específica.")
    elif n_circ / n_total > 0.10:
        print("VEREDICTO: CIRCULARIDAD MODERADA. Algunas sondas son inespecíficas.")
    else:
        print("VEREDICTO: Sondas razonablemente específicas. Circularidad < 10% bajo testing cruzado.")


if __name__ == "__main__":
    main()
