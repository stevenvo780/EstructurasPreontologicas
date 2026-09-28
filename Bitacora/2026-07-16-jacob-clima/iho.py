#!/usr/bin/env python3
"""IHO - Indice de Hiperobjetividad Operativa (prototipo).

Turns Morton's hyperobject into a measurable OPERATIVE profile over the EDI apparatus.
Reported as a VECTOR (V,N,T,P,I), never collapsed to a scalar (that would re-reify).
Computes P, I, approx T from live case metrics.json, and now also V (viscosity,
via 01_caso_clima/alt_probes/V_dispersion.json) and N (non-locality, via
_coupling/N_coupling.json) when those stub programs have been run; falls back
to PENDIENTE per axis if either json is missing.
Run from 09-simulaciones-edi/.  Source of truth: each case outputs/metrics.json.
"""
import json, statistics, sys

AGGREGATE = '01_caso_clima'                      # Morton's flagship hyperobject: the whole
SUBSTRUCTURES = [                                # candidate pre-ontological structures of 'climate'
    '16_caso_deforestacion','17_caso_oceanos','18_caso_urbanizacion',
    '19_caso_acidificacion_oceanica','21_caso_salinizacion','22_caso_fosforo',
    '25_caso_acuiferos','03_caso_contaminacion','04_caso_energia',
]

def load(case):
    d = json.load(open(f'{case}/outputs/metrics.json'))
    ph = d['phases'].get('real') or d['phases'].get('synthetic')
    e = ph.get('edi', {})
    cal = ph.get('calibration', {})
    a, b = cal.get('ode_alpha'), cal.get('ode_beta')
    tau = (1.0/(a*b)) if (a and b) else None       # approx response time-constant (months)
    return dict(case=case, edi=e.get('value'), sig=bool(e.get('permutation_significant')),
                p=e.get('permutation_pvalue'), passed=bool(ph.get('overall_pass')), tau=tau)

V_DISPERSION_PATH = '01_caso_clima/alt_probes/V_dispersion.json'
N_COUPLING_PATH = '_coupling/N_coupling.json'


def load_axis(path, key):
    """Lee V_dispersion.json o N_coupling.json si existen; None si aun no corrieron."""
    try:
        d = json.load(open(path))
    except FileNotFoundError:
        return None, None
    return d.get(key), d


agg = load(AGGREGATE)
subs = [load(c) for c in SUBSTRUCTURES]
V, V_detail = load_axis(V_DISPERSION_PATH, 'V_axis')
N, N_detail = load_axis(N_COUPLING_PATH, 'N_axis')

# P - Fasing/Retiro: whole withdraws (low aggregate) while parts manifest (high, gated components)
gated = [s['edi'] for s in subs if s['passed']]
P = (statistics.mean(gated) - agg['edi']) if gated else None
# I - Interobjetividad: density of co-active (significant) structures in the mesh
I = sum(s['sig'] for s in subs) / len(subs)
# T - Ondulacion temporal (APPROX): median response time-constant across structures
taus = [s['tau'] for s in subs if s['tau']]
T_months = statistics.median(taus) if taus else None

print('== IHO / sub-corpus CLIMA (live metrics.json) ==')
print(f"AGREGADO  {agg['case']:32s} EDI={agg['edi']:+.3f} sig={agg['sig']} pass={agg['passed']}")
for s in subs:
    print(f"  sub     {s['case']:32s} EDI={s['edi']:+.3f} sig={str(s['sig']):5s} pass={s['passed']}")
print()
print('PERFIL IHO (vector, NO colapsar a escalar):')
print(f"  P Fasing/Retiro   = {P:+.3f}   (media componentes-con-gate {statistics.mean(gated):+.3f} - agregado {agg['edi']:+.3f})")
print(f"  I Interobjetiv.   = {I:.2f}    ({sum(s['sig'] for s in subs)}/{len(subs)} subestructuras significativas)")
print(f"  T Ondulacion~     = {T_months:.1f} meses (approx, mediana tau ODE)" if T_months else '  T = n/d')
if V is not None:
    n_probes = len(V_detail.get('probes', []))
    print(f"  V Viscosidad      = {V:.4f}  (stdev EDI entre {n_probes} sondas, spread={V_detail.get('edi_spread'):.4f}; {V_DISPERSION_PATH})")
else:
    print( '  V Viscosidad      = PENDIENTE (correr 01_caso_clima/alt_probes/run_probes.py)')
if N is not None:
    n_pairs = len(N_detail.get('pairs', []))
    print(f"  N No-localidad    = {N:+.4f}  (media edi_coupling de {n_pairs} pares, proxy RMSE OLS AR1; {N_COUPLING_PATH})")
else:
    print( '  N No-localidad    = PENDIENTE (correr _coupling/run_pairs.py)')
print()
print(f"LECTURA: agregado 'clima' NO pasa gate (sig={agg['sig']}), pero {len(gated)} subestructuras SI ")
print( "        -> P alto = firma de RETIRO del hiperobjeto: el todo se retira, las partes se manifiestan.")
