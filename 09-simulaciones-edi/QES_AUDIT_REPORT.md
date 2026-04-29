# Auditoría de calidad de evidencia — corpus completo (40 casos)

Bloque V5.3. Asigna a cada caso un puntaje integral QES ∈ [0,1] que combina trazabilidad de datos, tamaño efectivo, calidad de sonda, reproducibilidad, multi-sonda, LoE y calibración estadística.

## Pesos QES

| Componente | Peso |
|------------|-----:|
| Q0_signo_potencia_edi | 0.10 |
| Q1a_traza_criptografica | 0.10 |
| Q1b_traza_empirica | 0.15 |
| Q2_tamano_efectivo | 0.10 |
| Q3_calidad_sonda | 0.15 |
| Q4_reproducibilidad | 0.10 |
| Q5_multi_sonda_penalizada | 0.10 |
| Q6_loe_empirico | 0.10 |
| Q7_calibracion_estadistica | 0.10 |

## Categorías

| Categoría | Umbral QES | Significado |
|-----------|-----------:|-------------|
| ROBUSTO | ≥ 0.85 | Apto para afirmación demostrativa post-V5.2 |
| DEMOSTRATIVO | 0.70 - 0.85 | Apto para afirmación demostrativa honesta |
| PROGRAMÁTICO | 0.55 - 0.70 | Sólo en modo programático con criterios de elevación |
| PILOTO | 0.40 - 0.55 | Piloto con limitaciones explícitas; no afirmar como demostración |
| INADMISIBLE | < 0.40 | PAPER-SCIENCE: retirar o re-implementar |

## Síntesis

| Categoría | Casos |
|-----------|------:|
| ROBUSTO | 8 |
| DEMOSTRATIVO | 23 |
| PROGRAMÁTICO | 9 |
| PILOTO | 2 |
| INADMISIBLE | 0 |

## Tabla por caso (ordenada de mayor a menor QES)

| Caso | QES | Categoría | Q0 EDI | Q1a crp | Q1b emp | Q2 n | Q3 sonda | Q4 repr | Q5 multi | Q6 LoE | Q7 calib |
|------|----:|-----------|-------:|--------:|--------:|-----:|---------:|--------:|---------:|-------:|---------:|
| 16_caso_deforestacion | **0.922** | ROBUSTO | 1.00 | 1.00 | 1.00 | 1.00 | 0.85 | 1.00 | 0.45 | 1.00 | 1.00 |
| 13_caso_politicas_estrategicas | **0.912** | ROBUSTO | 0.70 | 1.00 | 1.00 | 1.00 | 0.85 | 1.00 | 0.85 | 0.80 | 1.00 |
| 24_caso_microplasticos | **0.882** | ROBUSTO | 1.00 | 1.00 | 1.00 | 1.00 | 0.85 | 1.00 | 0.25 | 0.80 | 1.00 |
| 27_caso_riesgo_biologico | **0.882** | ROBUSTO | 1.00 | 1.00 | 1.00 | 1.00 | 0.85 | 1.00 | 0.25 | 0.80 | 1.00 |
| 05_caso_epidemiologia | **0.875** | ROBUSTO | 0.70 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.25 | 0.80 | 1.00 |
| 18_caso_urbanizacion | **0.872** | ROBUSTO | 0.70 | 1.00 | 1.00 | 1.00 | 0.85 | 1.00 | 0.25 | 1.00 | 1.00 |
| 20_caso_kessler | **0.853** | ROBUSTO | 0.63 | 1.00 | 1.00 | 0.38 | 0.85 | 1.00 | 0.95 | 0.80 | 1.00 |
| 22_caso_fosforo | **0.852** | ROBUSTO | 0.70 | 1.00 | 1.00 | 1.00 | 0.85 | 1.00 | 0.25 | 0.80 | 1.00 |
| 40_cumulos_globulares | **0.840** | DEMOSTRATIVO | 0.56 | 1.00 | 1.00 | 0.82 | 0.85 | 1.00 | 0.85 | 0.40 | 1.00 |
| 42_caso_histeresis_institucional | **0.833** | DEMOSTRATIVO | 1.00 | 0.50 | 1.00 | 1.00 | 0.85 | 1.00 | 0.25 | 0.80 | 1.00 |
| 09_caso_finanzas | **0.831** | DEMOSTRATIVO | 0.30 | 1.00 | 1.00 | 0.99 | 0.85 | 1.00 | 0.25 | 1.00 | 1.00 |
| 04_caso_energia | **0.823** | DEMOSTRATIVO | 0.62 | 1.00 | 1.00 | 0.36 | 1.00 | 1.00 | 0.25 | 1.00 | 1.00 |
| 11_caso_movilidad | **0.822** | DEMOSTRATIVO | 0.70 | 1.00 | 1.00 | 1.00 | 0.65 | 1.00 | 0.25 | 0.80 | 1.00 |
| 34_michaelis_menten | **0.802** | DEMOSTRATIVO | 0.56 | 1.00 | 1.00 | 0.73 | 0.65 | 1.00 | 0.85 | 0.40 | 1.00 |
| 39_cefeidas_ogle | **0.787** | DEMOSTRATIVO | 0.56 | 1.00 | 1.00 | 0.88 | 0.85 | 1.00 | 0.25 | 0.40 | 1.00 |
| 01_caso_clima | **0.786** | DEMOSTRATIVO | 0.15 | 1.00 | 1.00 | 0.99 | 0.85 | 1.00 | 0.25 | 0.80 | 0.90 |
| 21_caso_salinizacion | **0.782** | DEMOSTRATIVO | 0.30 | 1.00 | 1.00 | 1.00 | 0.65 | 1.00 | 0.45 | 0.60 | 1.00 |
| 37_hrv_cardiaco | **0.780** | DEMOSTRATIVO | 0.56 | 1.00 | 1.00 | 0.82 | 0.85 | 1.00 | 0.25 | 0.40 | 1.00 |
| 12_caso_paradigmas | **0.772** | DEMOSTRATIVO | 0.00 | 1.00 | 1.00 | 1.00 | 0.85 | 1.00 | 0.65 | 0.60 | 0.70 |
| 10_caso_justicia | **0.772** | DEMOSTRATIVO | 0.35 | 1.00 | 1.00 | 1.00 | 0.85 | 1.00 | 0.25 | 0.80 | 0.55 |
| 15_caso_wikipedia | **0.772** | DEMOSTRATIVO | 0.55 | 1.00 | 1.00 | 0.65 | 0.65 | 1.00 | 0.25 | 0.80 | 1.00 |
| 31_decoherencia_cuantica | **0.772** | DEMOSTRATIVO | 0.56 | 1.00 | 1.00 | 0.73 | 0.85 | 1.00 | 0.25 | 0.40 | 1.00 |
| 14_caso_postverdad | **0.753** | DEMOSTRATIVO | 0.52 | 1.00 | 1.00 | 0.58 | 0.85 | 1.00 | 0.25 | 0.40 | 1.00 |
| 19_caso_acidificacion_oceanica | **0.753** | DEMOSTRATIVO | 0.50 | 1.00 | 1.00 | 1.00 | 0.65 | 1.00 | 0.25 | 0.60 | 0.70 |
| 03_caso_contaminacion | **0.750** | DEMOSTRATIVO | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.25 | 0.60 | 0.65 |
| 28_caso_fuga_cerebros | **0.737** | DEMOSTRATIVO | 0.15 | 1.00 | 1.00 | 1.00 | 0.65 | 1.00 | 0.25 | 0.60 | 0.90 |
| 17_caso_oceanos | **0.737** | DEMOSTRATIVO | 0.00 | 1.00 | 1.00 | 0.79 | 0.85 | 1.00 | 0.65 | 0.60 | 0.55 |
| 26_caso_starlink | **0.728** | DEMOSTRATIVO | 0.28 | 1.00 | 1.00 | 0.28 | 0.85 | 1.00 | 0.25 | 0.80 | 0.90 |
| 25_caso_acuiferos | **0.712** | DEMOSTRATIVO | 0.00 | 1.00 | 1.00 | 0.90 | 0.65 | 1.00 | 0.25 | 0.60 | 0.90 |
| 36_nfkb | **0.712** | DEMOSTRATIVO | 0.56 | 1.00 | 0.50 | 0.88 | 0.85 | 1.00 | 0.25 | 0.40 | 1.00 |
| 29_caso_iot | **0.710** | DEMOSTRATIVO | 0.00 | 1.00 | 1.00 | 0.38 | 0.85 | 1.00 | 0.45 | 0.60 | 0.90 |
| 35_ciclo_celular | **0.685** | PROGRAMÁTICO | 0.39 | 1.00 | 0.30 | 0.88 | 0.85 | 1.00 | 0.45 | 0.40 | 1.00 |
| 32_espin_orbita | **0.675** | PROGRAMÁTICO | 0.56 | 1.00 | 0.30 | 0.82 | 0.85 | 1.00 | 0.25 | 0.40 | 1.00 |
| 30_caso_behavioral_dynamics | **0.648** | PROGRAMÁTICO | 0.35 | 1.00 | 0.30 | 1.00 | 0.85 | 1.00 | 0.45 | 0.40 | 0.55 |
| 08_caso_falsacion_observabilidad | **0.628** | PROGRAMÁTICO | 0.00 | 1.00 | 0.30 | 0.90 | 0.65 | 1.00 | 0.85 | 0.20 | 0.90 |
| 07_caso_falsacion_no_estacionariedad | **0.617** | PROGRAMÁTICO | 0.00 | 1.00 | 0.30 | 1.00 | 0.65 | 1.00 | 0.65 | 0.20 | 0.90 |
| 41_caso_wolfram_extendido | **0.602** | PROGRAMÁTICO | 0.00 | 0.50 | 0.30 | 1.00 | 0.85 | 1.00 | 0.65 | 0.60 | 0.55 |
| 33_villin_headpiece | **0.601** | PROGRAMÁTICO | 0.00 | 1.00 | 0.30 | 0.88 | 0.85 | 1.00 | 0.45 | 0.40 | 0.55 |
| 23_caso_erosion_dialectica | **0.590** | PROGRAMÁTICO | 0.00 | 1.00 | 0.30 | 0.32 | 0.65 | 1.00 | 0.85 | 0.40 | 0.90 |
| 02_caso_conciencia | **0.561** | PROGRAMÁTICO | 0.00 | 1.00 | 0.50 | 0.33 | 0.65 | 1.00 | 0.25 | 0.40 | 0.90 |
| 38_locomocion_alternativa | **0.544** | PILOTO | 0.00 | 1.00 | 0.30 | 0.82 | 0.65 | 1.00 | 0.25 | 0.40 | 0.55 |
| 06_caso_falsacion_exogeneidad | **0.542** | PILOTO | 0.15 | 1.00 | 0.20 | 1.00 | 0.65 | 1.00 | 0.25 | 0.20 | 0.55 |

## Lectura

QES es métrica ad-hoc del proyecto, no estándar reconocido en literatura externa (no es GRADE ni AMSTAR). Sirve como filtro interno: la categoría ROBUSTO requiere QES ≥ 0.85 *y* Q0 ≥ 0.60 (EDI positivo con potencia razonable) *y* Q1b ≥ 0.50 (trazabilidad empírica suficiente). Sin ambas precondiciones, un caso con infraestructura adecuada pero contenido empírico nulo o sintético ad-hoc clasifica como DEMOSTRATIVO o inferior.

## Lectura cruzada

- `09-simulaciones-edi/common/quality_scorer.py` — implementación del scorer.
- `Anexos/A0-limitaciones-declaradas.md` — limitaciones consolidadas.