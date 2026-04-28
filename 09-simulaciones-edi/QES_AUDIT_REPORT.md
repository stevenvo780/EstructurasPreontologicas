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
| ROBUSTO | 10 |
| DEMOSTRATIVO | 30 |
| PROGRAMÁTICO | 0 |
| PILOTO | 0 |
| INADMISIBLE | 0 |

## Tabla por caso (ordenada de mayor a menor QES)

| Caso | QES | Categoría | Q1 trz | Q2 n | Q3 sonda | Q4 repr | Q5 multi | Q6 LoE | Q7 calib |
|------|----:|-----------|-------:|------:|----------:|--------:|----------:|--------:|----------:|
| 09_caso_finanzas | **0.939** | ROBUSTO | 1.00 | 0.99 | 0.70 | 1.00 | 0.85 | 1.00 | 1.00 |
| 01_caso_clima | **0.924** | ROBUSTO | 1.00 | 0.99 | 0.70 | 1.00 | 0.85 | 1.00 | 0.90 |
| 05_caso_epidemiologia | **0.888** | ROBUSTO | 1.00 | 0.92 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 35_ciclo_celular | **0.885** | ROBUSTO | 1.00 | 0.88 | 0.85 | 1.00 | 0.85 | 0.40 | 1.00 |
| 36_nfkb | **0.885** | ROBUSTO | 1.00 | 0.88 | 0.85 | 1.00 | 0.85 | 0.40 | 1.00 |
| 39_cefeidas_ogle | **0.885** | ROBUSTO | 1.00 | 0.88 | 0.85 | 1.00 | 0.85 | 0.40 | 1.00 |
| 32_espin_orbita | **0.875** | ROBUSTO | 1.00 | 0.82 | 0.85 | 1.00 | 0.85 | 0.40 | 1.00 |
| 37_hrv_cardiaco | **0.875** | ROBUSTO | 1.00 | 0.82 | 0.85 | 1.00 | 0.85 | 0.40 | 1.00 |
| 40_cumulos_globulares | **0.875** | ROBUSTO | 1.00 | 0.82 | 0.85 | 1.00 | 0.85 | 0.40 | 1.00 |
| 11_caso_movilidad | **0.851** | ROBUSTO | 1.00 | 0.41 | 0.70 | 1.00 | 0.85 | 1.00 | 1.00 |
| 15_caso_wikipedia | **0.847** | DEMOSTRATIVO | 1.00 | 0.65 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 07_caso_falsacion_no_estacionariedad | **0.845** | DEMOSTRATIVO | 1.00 | 1.00 | 0.70 | 1.00 | 0.85 | 0.20 | 0.90 |
| 08_caso_falsacion_observabilidad | **0.840** | DEMOSTRATIVO | 1.00 | 0.90 | 0.70 | 1.00 | 0.95 | 0.20 | 0.90 |
| 31_decoherencia_cuantica | **0.840** | DEMOSTRATIVO | 1.00 | 0.73 | 0.70 | 1.00 | 0.85 | 0.40 | 1.00 |
| 34_michaelis_menten | **0.840** | DEMOSTRATIVO | 1.00 | 0.73 | 0.70 | 1.00 | 0.85 | 0.40 | 1.00 |
| 18_caso_urbanizacion | **0.816** | DEMOSTRATIVO | 1.00 | 0.44 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 21_caso_salinizacion | **0.810** | DEMOSTRATIVO | 1.00 | 0.40 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 22_caso_fosforo | **0.810** | DEMOSTRATIVO | 1.00 | 0.40 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 20_caso_kessler | **0.807** | DEMOSTRATIVO | 1.00 | 0.38 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 24_caso_microplasticos | **0.807** | DEMOSTRATIVO | 1.00 | 0.38 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 25_caso_acuiferos | **0.806** | DEMOSTRATIVO | 1.00 | 0.41 | 0.70 | 1.00 | 0.95 | 0.60 | 0.90 |
| 04_caso_energia | **0.804** | DEMOSTRATIVO | 1.00 | 0.36 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 13_caso_politicas_estrategicas | **0.804** | DEMOSTRATIVO | 1.00 | 0.36 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 16_caso_deforestacion | **0.804** | DEMOSTRATIVO | 1.00 | 0.36 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 27_caso_riesgo_biologico | **0.800** | DEMOSTRATIVO | 1.00 | 0.33 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 14_caso_postverdad | **0.799** | DEMOSTRATIVO | 1.00 | 0.32 | 0.70 | 1.00 | 0.85 | 0.60 | 1.00 |
| 28_caso_fuga_cerebros | **0.795** | DEMOSTRATIVO | 1.00 | 0.40 | 0.70 | 1.00 | 0.85 | 0.60 | 0.90 |
| 33_villin_headpiece | **0.795** | DEMOSTRATIVO | 1.00 | 0.88 | 0.70 | 1.00 | 0.85 | 0.40 | 0.55 |
| 23_caso_erosion_dialectica | **0.794** | DEMOSTRATIVO | 1.00 | 0.32 | 0.70 | 1.00 | 0.95 | 0.60 | 0.90 |
| 06_caso_falsacion_exogeneidad | **0.792** | DEMOSTRATIVO | 1.00 | 1.00 | 0.70 | 1.00 | 0.85 | 0.20 | 0.55 |
| 29_caso_iot | **0.792** | DEMOSTRATIVO | 1.00 | 0.38 | 0.70 | 1.00 | 0.85 | 0.60 | 0.90 |
| 38_locomocion_alternativa | **0.785** | DEMOSTRATIVO | 1.00 | 0.82 | 0.70 | 1.00 | 0.85 | 0.40 | 0.55 |
| 02_caso_conciencia | **0.785** | DEMOSTRATIVO | 1.00 | 0.33 | 0.70 | 1.00 | 0.85 | 0.60 | 0.90 |
| 26_caso_starlink | **0.776** | DEMOSTRATIVO | 1.00 | 0.28 | 0.70 | 1.00 | 0.85 | 0.60 | 0.90 |
| 10_caso_justicia | **0.776** | DEMOSTRATIVO | 1.00 | 0.35 | 0.70 | 1.00 | 0.85 | 1.00 | 0.55 |
| 12_caso_paradigmas | **0.757** | DEMOSTRATIVO | 1.00 | 0.35 | 0.70 | 1.00 | 0.85 | 0.60 | 0.70 |
| 19_caso_acidificacion_oceanica | **0.757** | DEMOSTRATIVO | 1.00 | 0.35 | 0.70 | 1.00 | 0.85 | 0.60 | 0.70 |
| 03_caso_contaminacion | **0.750** | DEMOSTRATIVO | 1.00 | 0.35 | 0.70 | 1.00 | 0.85 | 0.60 | 0.65 |
| 17_caso_oceanos | **0.748** | DEMOSTRATIVO | 1.00 | 0.37 | 0.70 | 1.00 | 0.95 | 0.60 | 0.55 |
| 30_caso_behavioral_dynamics | **0.744** | DEMOSTRATIVO | 1.00 | 0.54 | 0.70 | 1.00 | 0.85 | 0.40 | 0.55 |

## Lectura

Esta auditoría es el filtro **anti-paper-science** del aparato V5.3: ningún caso pasa a afirmación demostrativa si su QES < 0.70. Casos en categoría INADMISIBLE deben retirarse, declararse como hipótesis especulativa, o re-implementarse con datos reales y sonda físicamente motivada.

## Lectura cruzada

- `09-simulaciones-edi/common/quality_scorer.py` — implementación del scorer.
- `Anexos/A0-limitaciones-declaradas.md` — limitaciones consolidadas.
- `09-simulaciones-edi/CIERRE_V5_2.md` — síntesis de los ocho bloques V5.2.