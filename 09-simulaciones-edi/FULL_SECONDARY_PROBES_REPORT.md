# Sondas secundarias B10 — extensión a los 40 casos

**Total**: 42 sondas secundarias implementadas con motivación teórica independiente.
**Convergen** (|Δ EDI| ≤ 0.05 sobre proxys sintéticos): 6

## Tabla por caso

| Caso | Sonda secundaria | Motivación | EDI primario | EDI secundario | \|Δ\| | Convergen |
|------|------------------|------------|-------------:|----------------:|-------:|:----:|
| 01_caso_clima | stochastic_harmonic_oscillator | fisica_oscilatoria | +0.011 | -1.000 | 1.011 | ✗ |
| 02_caso_conciencia | fokker_planck_drift_diffusion | fisica_estadistica | -0.117 | -1.000 | 0.883 | ✗ |
| 03_caso_contaminacion | sir_compartmental_pollution | epidemiologia_clasica | -0.004 | +0.607 | 0.612 | ✗ |
| 04_caso_energia | maxwell_boltzmann | termodinamica_estadistica | +0.650 | +0.194 | 0.457 | ✗ |
| 05_caso_epidemiologia | fisher_kpp_diffusion | matematica_difusion_reactiva | +0.129 | -0.249 | 0.379 | ✗ |
| 06_caso_falsacion_exogeneidad | random_walk_control | control_de_falsabilidad | +0.055 | -1.000 | 1.055 | ✗ |
| 07_caso_falsacion_no_estacionariedad | random_walk_control | control_de_falsabilidad | -0.882 | -1.000 | 0.118 | ✗ |
| 08_caso_falsacion_observabilidad | random_walk_control | control_de_falsabilidad | -1.000 | -1.000 | 0.000 | ✓ |
| 09_caso_finanzas | heston_stochastic_volatility | matematica_financiera | +0.081 | -1.000 | 1.081 | ✗ |
| 10_caso_justicia | linear_relaxation_justice | control_lineal_clasico | +0.227 | -0.262 | 0.489 | ✗ |
| 11_caso_movilidad | gravity_model | fisica_gravitacional_aplicada | +0.128 | -1.000 | 1.128 | ✗ |
| 12_caso_paradigmas | kuramoto_synchronization | sincronizacion_no_lineal | -0.006 | -0.097 | 0.090 | ✗ |
| 13_caso_politicas_estrategicas | linear_relaxation_policy | control_lineal_clasico | +0.297 | +0.321 | 0.024 | ✓ |
| 14_caso_postverdad | bass_diffusion | marketing_quantitativo | +0.243 | -0.143 | 0.385 | ✗ |
| 15_caso_wikipedia | gompertz_growth | demografia_envejecimiento | +0.191 | -0.766 | 0.958 | ✗ |
| 16_caso_deforestacion | fisher_kpp_diffusion | matematica_reactiva | +0.580 | +0.420 | 0.160 | ✗ |
| 17_caso_oceanos | stommel_thermohaline | oceanografia_clasica | -0.016 | +0.087 | 0.103 | ✗ |
| 18_caso_urbanizacion | gompertz_urban | demografia_no_simetrica | +0.236 | -1.000 | 1.236 | ✗ |
| 19_caso_acidificacion_oceanica | henry_law_solubility | termodinamica_disolucion | -0.000 | -0.405 | 0.404 | ✗ |
| 20_caso_kessler | lotka_volterra | ecologia_clasica | +0.353 | +0.369 | 0.017 | ✓ |
| 21_caso_salinizacion | linear_diffusion | transporte_advectivo | +0.018 | +0.254 | 0.236 | ✗ |
| 22_caso_fosforo | logistic_phosphorus | limnologia_simple | +0.192 | -0.927 | 1.119 | ✗ |
| 23_caso_erosion_dialectica | random_walk_dialectical | control_caso_piloto | -1.000 | -1.000 | 0.000 | ✓ |
| 24_caso_microplasticos | gompertz_pollutant | crecimiento_asimetrico | +0.782 | -1.000 | 1.782 | ✗ |
| 25_caso_acuiferos | darcy_groundwater | hidrogeologia_clasica | -0.146 | +0.405 | 0.552 | ✗ |
| 26_caso_starlink | exponential_growth | modelos_demograficos | +0.689 | -1.000 | 1.689 | ✗ |
| 27_caso_riesgo_biologico | zeeman_catastrophe | topologia_catastrofes | +0.332 | +0.749 | 0.417 | ✗ |
| 28_caso_fuga_cerebros | gravity_brain_drain | fisica_aplicada_a_migracion | +0.025 | -1.000 | 1.025 | ✗ |
| 29_caso_iot | logistic_substitution | fisher_pry_substitution | -0.877 | -0.617 | 0.260 | ✗ |
| 30_caso_behavioral_dynamics | kuramoto_phase_locking | sincronizacion_de_fases | +0.262 | +0.087 | 0.175 | ✗ |
| 31_decoherencia_cuantica | exponential_relaxation | decay_exponencial | +0.913 | +0.516 | 0.397 | ✗ |
| 32_espin_orbita | langevin_dynamics | fisica_estadistica_estocastica | +0.825 | -0.745 | 1.570 | ✗ |
| 33_villin_headpiece | kramers_transition_state | fisica_de_transiciones | -0.000 | +0.183 | 0.184 | ✗ |
| 34_michaelis_menten | hill_cooperative | cooperatividad_enzimatica | +0.458 | +0.461 | 0.003 | ✓ |
| 35_ciclo_celular | goldbeter_oscillator | oscilaciones_circadianas | +0.130 | +0.372 | 0.241 | ✗ |
| 36_nfkb | goldbeter_nfkb | redes_oscilatorias | +0.587 | -1.000 | 1.587 | ✗ |
| 37_hrv_cardiaco | fitzhugh_nagumo | neurodinamica_excitable | +0.577 | -0.679 | 1.256 | ✗ |
| 38_locomocion_alternativa | mass_spring_damped | mecanica_clasica | -1.000 | -0.511 | 0.489 | ✗ |
| 39_cefeidas_ogle | reimers_mass_loss | evolucion_estelar | +0.916 | -1.000 | 1.916 | ✗ |
| 40_cumulos_globulares | king_profile | dinamica_estelar_truncada | +0.427 | +0.463 | 0.035 | ✓ |
| 41_caso_wolfram_extendido | markov_compression | compresion_estado_discreto | -0.275 | -0.364 | 0.088 | ✗ |
| 42_caso_histeresis_institucional | rf_threshold_bisection | aprendizaje_supervisado_decision_tree | +0.777 | -0.138 | 0.915 | ✗ |

## Limitación

Convergencia evaluada sobre proxys sintéticos derivados del EDI publicado. La verificación definitiva requiere arrays obs/abm/forcing primarios (deuda fechada de re-ejecución).