# Análisis de potencia estadística — corpus completo (40 casos)

Bloque científico B7 (V5.2). Distingue casos null genuinos de casos null por tamaño muestral insuficiente.

## Síntesis

- **No null** (EDI > 0.10): 23
- **Null real** (potencia ≥ 0.80 para detectar weak): 4
- **Null por potencia insuficiente**: 13

## Casos null por potencia insuficiente

Estos casos NO se pueden afirmar como ausencia de cierre operativo; sólo que el corpus actual carece de resolución estadística para detectarlo.

| Caso | EDI | n | Potencia para detectar weak | MDE actual | n necesario |
|------|----:|--:|-----------------------------:|------------:|-------------:|
| 02_caso_conciencia | -0.1165 | 9 | 25.95% | 0.2487 | 124 |
| 03_caso_contaminacion | -0.0038 | 11 | 25.95% | 0.2487 | 124 |
| 08_caso_falsacion_observabilidad | -1.0000 | 97 | 71.13% | 0.1129 | 124 |
| 12_caso_paradigmas | -0.0060 | 11 | 25.95% | 0.2487 | 124 |
| 17_caso_oceanos | -0.0154 | 14 | 25.95% | 0.2487 | 124 |
| 19_caso_acidificacion_oceanica | -0.0002 | 11 | 25.95% | 0.2487 | 124 |
| 21_caso_salinizacion | +0.0184 | 18 | 25.95% | 0.2487 | 124 |
| 23_caso_erosion_dialectica | -1.0000 | 8 | 25.95% | 0.2487 | 124 |
| 25_caso_acuiferos | -0.1462 | 19 | 25.95% | 0.2487 | 124 |
| 28_caso_fuga_cerebros | +0.0249 | 18 | 25.95% | 0.2487 | 124 |
| 29_caso_iot | -0.8760 | 15 | 25.95% | 0.2487 | 124 |
| 33_villin_headpiece | +0.0000 | 90 | 68.31% | 0.1172 | 124 |
| 38_locomocion_alternativa | -1.3412 | 75 | 61.47% | 0.1284 | 124 |

## Tabla completa

| Caso | EDI | n | Potencia | MDE | Clasificación |
|------|----:|--:|---------:|-----:|----------------|
| 01_caso_clima | +0.0111 | 168 | 89.49% | 0.0858 | null_real |
| 02_caso_conciencia | -0.1165 | 9 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 03_caso_contaminacion | -0.0038 | 11 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 04_caso_energia | +0.6503 | 13 | 25.95% | 0.2487 | no_null |
| 05_caso_epidemiologia | +0.1294 | 104 | 73.74% | 0.1091 | no_null |
| 06_caso_falsacion_exogeneidad | +0.0551 | 731 | 100.00% | 0.0411 | null_real |
| 07_caso_falsacion_no_estacionariedad | -0.8819 | 731 | 100.00% | 0.0411 | null_real |
| 08_caso_falsacion_observabilidad | -1.0000 | 97 | 71.13% | 0.1129 | null_por_potencia_insuficiente |
| 09_caso_finanzas | +0.0813 | 168 | 89.49% | 0.0858 | null_real |
| 10_caso_justicia | +0.2274 | 12 | 25.95% | 0.2487 | no_null |
| 11_caso_movilidad | +0.1283 | 19 | 25.95% | 0.2487 | no_null |
| 12_caso_paradigmas | -0.0060 | 11 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 13_caso_politicas_estrategicas | +0.2972 | 13 | 25.95% | 0.2487 | no_null |
| 14_caso_postverdad | +0.2428 | 8 | 25.95% | 0.2487 | no_null |
| 15_caso_wikipedia | +0.1916 | 48 | 46.18% | 0.1605 | no_null |
| 16_caso_deforestacion | +0.5802 | 13 | 25.95% | 0.2487 | no_null |
| 17_caso_oceanos | -0.0154 | 14 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 18_caso_urbanizacion | +0.2358 | 23 | 28.35% | 0.2319 | no_null |
| 19_caso_acidificacion_oceanica | -0.0002 | 11 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 20_caso_kessler | +0.3527 | 15 | 25.95% | 0.2487 | no_null |
| 21_caso_salinizacion | +0.0184 | 18 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 22_caso_fosforo | +0.1924 | 18 | 25.95% | 0.2487 | no_null |
| 23_caso_erosion_dialectica | -1.0000 | 8 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 24_caso_microplasticos | +0.7819 | 15 | 25.95% | 0.2487 | no_null |
| 25_caso_acuiferos | -0.1462 | 19 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 26_caso_starlink | +0.6892 | 1 | 25.95% | 0.2487 | no_null |
| 27_caso_riesgo_biologico | +0.3326 | 9 | 25.95% | 0.2487 | no_null |
| 28_caso_fuga_cerebros | +0.0249 | 18 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 29_caso_iot | -0.8760 | 15 | 25.95% | 0.2487 | null_por_potencia_insuficiente |
| 30_caso_behavioral_dynamics | +0.2622 | 35 | 37.37% | 0.1880 | no_null |
| 31_decoherencia_cuantica | +0.9132 | 60 | 53.47% | 0.1436 | no_null |
| 32_espin_orbita | +0.8251 | 75 | 61.47% | 0.1284 | no_null |
| 33_villin_headpiece | +0.0000 | 90 | 68.31% | 0.1172 | null_por_potencia_insuficiente |
| 34_michaelis_menten | +0.4580 | 60 | 53.47% | 0.1436 | no_null |
| 35_ciclo_celular | +0.1307 | 90 | 68.31% | 0.1172 | no_null |
| 36_nfkb | +0.5874 | 90 | 68.31% | 0.1172 | no_null |
| 37_hrv_cardiaco | +0.5771 | 75 | 61.47% | 0.1284 | no_null |
| 38_locomocion_alternativa | -1.3412 | 75 | 61.47% | 0.1284 | null_por_potencia_insuficiente |
| 39_cefeidas_ogle | +0.9162 | 90 | 68.31% | 0.1172 | no_null |
| 40_cumulos_globulares | +0.4276 | 75 | 61.47% | 0.1284 | no_null |

## Lectura honesta

Esta es la honestidad complementaria a la calibración del Type-I error (B1). Mientras B1 controla falsos positivos por autocorrelación + comparaciones múltiples, B7 controla falsos negativos por tamaño insuficiente.

Los casos clasificados como `null_por_potencia_insuficiente` son particularmente importantes: el manuscrito NO afirma que no tengan cierre operativo; afirma que el aparato actual carece de resolución para detectarlo. La elevación a `n` mayor (mediante series temporales más largas o muestras adicionales) es deuda metodológica priorizada.