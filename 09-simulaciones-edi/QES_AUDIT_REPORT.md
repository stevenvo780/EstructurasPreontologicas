# Auditoría de calidad de evidencia — corpus completo (40 casos)

Bloque V5.3. Asigna a cada caso un puntaje integral QES ∈ [0,1] que combina trazabilidad de datos, tamaño efectivo, calidad de sonda, reproducibilidad, multi-sonda, LoE y calibración estadística.

## Pesos QES

| Componente | Peso |
|------------|-----:|
| Q1_trazabilidad_datos | 0.20 |
| Q2_tamano_efectivo | 0.15 |
| Q3_calidad_sonda | 0.15 |
| Q4_reproducibilidad | 0.15 |
| Q5_convergencia_multisonda | 0.10 |
| Q6_loe_empirico | 0.10 |
| Q7_calibracion_estadistica | 0.15 |

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
| ROBUSTO | 33 |
| DEMOSTRATIVO | 9 |
| PROGRAMÁTICO | 0 |
| PILOTO | 0 |
| INADMISIBLE | 0 |

## Tabla por caso (ordenada de mayor a menor QES)

| Caso | QES | Categoría | Q1 trz | Q2 n | Q3 sonda | Q4 repr | Q5 multi | Q6 LoE | Q7 calib |
|------|----:|-----------|-------:|------:|----------:|--------:|----------:|--------:|----------:|
| 16_caso_deforestacion | **0.977** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.92 | 1.00 | 1.00 |
| 09_caso_finanzas | **0.973** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 1.00 | 1.00 |
| 18_caso_urbanizacion | **0.973** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 1.00 | 1.00 |
| 05_caso_epidemiologia | **0.968** | ROBUSTO | 1.00 | 1.00 | 1.00 | 1.00 | 0.88 | 0.80 | 1.00 |
| 13_caso_politicas_estrategicas | **0.960** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.95 | 0.80 | 1.00 |
| 24_caso_microplasticos | **0.957** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.92 | 0.80 | 1.00 |
| 27_caso_riesgo_biologico | **0.957** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.92 | 0.80 | 1.00 |
| 42_caso_histeresis_institucional | **0.957** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.92 | 0.80 | 1.00 |
| 22_caso_fosforo | **0.953** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 0.80 | 1.00 |
| 01_caso_clima | **0.938** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 0.80 | 0.90 |
| 04_caso_energia | **0.934** | ROBUSTO | 1.00 | 0.61 | 1.00 | 1.00 | 0.92 | 1.00 | 1.00 |
| 11_caso_movilidad | **0.930** | ROBUSTO | 1.00 | 1.00 | 0.75 | 1.00 | 0.88 | 0.80 | 1.00 |
| 35_ciclo_celular | **0.913** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 0.40 | 1.00 |
| 36_nfkb | **0.913** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 0.40 | 1.00 |
| 39_cefeidas_ogle | **0.913** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 0.40 | 1.00 |
| 21_caso_salinizacion | **0.910** | ROBUSTO | 1.00 | 1.00 | 0.75 | 1.00 | 0.88 | 0.60 | 1.00 |
| 20_caso_kessler | **0.909** | ROBUSTO | 1.00 | 0.62 | 0.90 | 1.00 | 1.00 | 0.80 | 1.00 |
| 40_cumulos_globulares | **0.909** | ROBUSTO | 1.00 | 0.93 | 0.90 | 1.00 | 0.95 | 0.40 | 1.00 |
| 32_espin_orbita | **0.902** | ROBUSTO | 1.00 | 0.93 | 0.90 | 1.00 | 0.88 | 0.40 | 1.00 |
| 37_hrv_cardiaco | **0.902** | ROBUSTO | 1.00 | 0.93 | 0.90 | 1.00 | 0.88 | 0.40 | 1.00 |
| 15_caso_wikipedia | **0.899** | ROBUSTO | 1.00 | 0.79 | 0.75 | 1.00 | 0.88 | 0.80 | 1.00 |
| 25_caso_acuiferos | **0.895** | ROBUSTO | 1.00 | 1.00 | 0.75 | 1.00 | 0.88 | 0.60 | 0.90 |
| 28_caso_fuga_cerebros | **0.895** | ROBUSTO | 1.00 | 1.00 | 0.75 | 1.00 | 0.88 | 0.60 | 0.90 |
| 31_decoherencia_cuantica | **0.891** | ROBUSTO | 1.00 | 0.85 | 0.90 | 1.00 | 0.88 | 0.40 | 1.00 |
| 10_caso_justicia | **0.886** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 0.80 | 0.55 |
| 14_caso_postverdad | **0.876** | ROBUSTO | 1.00 | 0.75 | 0.90 | 1.00 | 0.88 | 0.40 | 1.00 |
| 34_michaelis_menten | **0.875** | ROBUSTO | 1.00 | 0.85 | 0.75 | 1.00 | 0.95 | 0.40 | 1.00 |
| 26_caso_starlink | **0.871** | ROBUSTO | 1.00 | 0.56 | 0.90 | 1.00 | 0.88 | 0.80 | 0.90 |
| 41_caso_wolfram_extendido | **0.870** | ROBUSTO | 1.00 | 1.00 | 0.90 | 1.00 | 0.92 | 0.60 | 0.55 |
| 08_caso_falsacion_observabilidad | **0.863** | ROBUSTO | 1.00 | 1.00 | 0.75 | 1.00 | 0.95 | 0.20 | 0.90 |
| 29_caso_iot | **0.862** | ROBUSTO | 1.00 | 0.62 | 0.90 | 1.00 | 0.88 | 0.60 | 0.90 |
| 07_caso_falsacion_no_estacionariedad | **0.856** | ROBUSTO | 1.00 | 1.00 | 0.75 | 1.00 | 0.88 | 0.20 | 0.90 |
| 17_caso_oceanos | **0.851** | ROBUSTO | 1.00 | 0.90 | 0.90 | 1.00 | 0.88 | 0.60 | 0.55 |
| 33_villin_headpiece | **0.846** | DEMOSTRATIVO | 1.00 | 1.00 | 0.90 | 1.00 | 0.88 | 0.40 | 0.55 |
| 19_caso_acidificacion_oceanica | **0.839** | DEMOSTRATIVO | 1.00 | 0.83 | 0.75 | 1.00 | 0.88 | 0.60 | 0.70 |
| 03_caso_contaminacion | **0.836** | DEMOSTRATIVO | 1.00 | 0.61 | 1.00 | 1.00 | 0.88 | 0.60 | 0.65 |
| 12_caso_paradigmas | **0.829** | DEMOSTRATIVO | 1.00 | 0.61 | 0.90 | 1.00 | 0.88 | 0.60 | 0.70 |
| 23_caso_erosion_dialectica | **0.821** | DEMOSTRATIVO | 1.00 | 0.59 | 0.75 | 1.00 | 0.95 | 0.40 | 0.90 |
| 02_caso_conciencia | **0.815** | DEMOSTRATIVO | 1.00 | 0.60 | 0.75 | 1.00 | 0.88 | 0.40 | 0.90 |
| 38_locomocion_alternativa | **0.812** | DEMOSTRATIVO | 1.00 | 0.93 | 0.75 | 1.00 | 0.88 | 0.40 | 0.55 |
| 30_caso_behavioral_dynamics | **0.804** | DEMOSTRATIVO | 1.00 | 0.73 | 0.90 | 1.00 | 0.88 | 0.40 | 0.55 |
| 06_caso_falsacion_exogeneidad | **0.803** | DEMOSTRATIVO | 1.00 | 1.00 | 0.75 | 1.00 | 0.88 | 0.20 | 0.55 |

## Lectura

Esta auditoría es el filtro **anti-paper-science** del aparato V5.3: ningún caso pasa a afirmación demostrativa si su QES < 0.70. Casos en categoría INADMISIBLE deben retirarse, declararse como hipótesis especulativa, o re-implementarse con datos reales y sonda físicamente motivada.

## Lectura cruzada

- `09-simulaciones-edi/common/quality_scorer.py` — implementación del scorer.
- `Anexos/A0-limitaciones-declaradas.md` — limitaciones consolidadas.
- `09-simulaciones-edi/CIERRE_V5_2.md` — síntesis de los ocho bloques V5.2.