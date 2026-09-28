# Auditoría de Simulaciones

Criterios: consistencia documental, presencia de métricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | p-perm | sig | CR | C1 | Categoría | Nivel | NS | Per | Pass | Hallazgos |
| :--- | ---: | ---: | :---: | ---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01_caso_clima | 0.258 | 1.000 | ❌ | 1.036 | ✅ | trend | 1 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 02_caso_conciencia | -0.012 | 0.315 | ❌ | 0.803 | ❌ | null | 0 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 03_caso_contaminacion | -0.011 | 0.616 | ❌ | 1.096 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 04_caso_energia | 0.157 | 0.006 | ✅ | 1.001 | ✅ | weak | 3 | ✅ | ✅ | ❌ | OK |
| 05_caso_epidemiologia | 0.129 | 0.000 | ✅ | 1.009 | ✅ | weak | 3 | ✅ | ✅ | ❌ | OK |
| 06_caso_falsacion_exogeneidad | 0.055 | 1.000 | ❌ | 1.006 | ✅ | falsification | — | ✅ | ✅ | ❌ | OK |
| 07_caso_falsacion_no_estacionariedad | -0.882 | 1.000 | ❌ | 1.005 | ❌ | falsification | — | ✅ | ✅ | ❌ | OK |
| 08_caso_falsacion_observabilidad | -1.000 | 1.000 | ❌ | 1.005 | ❌ | falsification | — | ✅ | ✅ | ❌ | OK |
| 09_caso_finanzas | 0.103 | 0.000 | ✅ | 2.652 | ✅ | weak | 3 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 10_caso_justicia | 0.058 | 0.017 | ✅ | 1.001 | ✅ | suggestive | 2 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 11_caso_movilidad | 0.060 | 0.922 | ❌ | 1.001 | ✅ | trend | 1 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 12_caso_paradigmas | -0.172 | 1.000 | ❌ | 1.000 | ✅ | null | 0 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 13_caso_politicas_estrategicas | 0.082 | 0.162 | ❌ | 1.000 | ✅ | trend | 1 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 14_caso_postverdad | 0.002 | 0.985 | ❌ | 1.009 | ✅ | trend | 1 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 15_caso_wikipedia | -0.004 | 0.769 | ❌ | 1.022 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 16_caso_deforestacion | 0.580 | 0.000 | ✅ | 1.023 | ✅ | strong | 4 | ✅ | ✅ | ✅ | docs/ incompleto (4 faltantes) |
| 17_caso_oceanos | 0.190 | 0.000 | ✅ | 1.000 | ✅ | weak | 3 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 18_caso_urbanizacion | 0.337 | 0.000 | ✅ | 1.003 | ✅ | strong | 4 | ✅ | ✅ | ✅ | docs/ incompleto (4 faltantes) |
| 19_caso_acidificacion_oceanica | -0.005 | 0.868 | ❌ | 1.352 | ❌ | null | 0 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 20_caso_kessler | -1.000 | 1.000 | ❌ | 1.005 | ✅ | null | 0 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 21_caso_salinizacion | 0.515 | 0.000 | ✅ | 1.001 | ✅ | strong | 4 | ✅ | ✅ | ✅ | docs/ incompleto (4 faltantes) |
| 22_caso_fosforo | 0.322 | 0.000 | ✅ | 1.003 | ✅ | strong | 4 | ✅ | ✅ | ✅ | docs/ incompleto (4 faltantes) |
| 23_caso_erosion_dialectica | -1.000 | 1.000 | ❌ | 1.001 | ✅ | null | 0 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 24_caso_microplasticos | -1.000 | 1.000 | ❌ | 1.001 | ✅ | null | 0 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 25_caso_acuiferos | 0.004 | 0.186 | ❌ | 1.067 | ✅ | trend | 1 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 26_caso_starlink | 0.757 | 0.079 | ❌ | ∞ | ✅ | trend | 1 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes); CR=∞ (ext≈0) |
| 27_caso_riesgo_biologico | 0.216 | 0.956 | ❌ | 0.999 | ✅ | trend | 1 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 28_caso_fuga_cerebros | 0.030 | 0.969 | ❌ | 1.006 | ✅ | trend | 1 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 29_caso_iot | -0.899 | 1.000 | ❌ | 1.006 | ❌ | null | 0 | ✅ | ❌ | ❌ | docs/ incompleto (4 faltantes) |
| 30_caso_behavioral_dynamics | 0.262 | 0.044 | ✅ | 1.090 | ✅ | weak | 3 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 41_caso_wolfram_extendido | -0.275 | 0.574 | ❌ | n/a | ❌ | ? | 0 | ❌ | ❌ | ❌ | README.md faltante; outputs/report.md faltante; docs/ incompleto (4 faltantes); CR no disponible |
| 42_caso_histeresis_institucional | 0.777 | 0.001 | ❌ | n/a | ❌ | ? | 0 | ❌ | ❌ | ✅ | README.md faltante; outputs/report.md faltante; docs/ incompleto (4 faltantes); CR no disponible |

## Resumen

| Métrica | Valor |
| :--- | :--- |
| Total de casos | 32 |
| overall_pass (EDI∈[0.30,0.90]) | 5/32 |
| Significancia (p<0.05 + EDI>0.01) | 10/32 |
| Estabilidad numérica | 30/32 |
| Persistencia (std_ratio<5) | 29/32 |

### Distribución por categoría

| Categoría | Nivel | Casos |
| :--- | :---: | ---: |
| strong | 4 | 4 |
| weak | 3 | 5 |
| suggestive | 2 | 1 |
| trend | 1 | 8 |
| null | 0 | 9 |
| falsification | — | 3 |
| ? | ? | 2 |

## Recomendaciones

- Si EDI o CR es n/a, revisar el pipeline de cálculo y los datos fuente.
- CR=∞ indica acoplamiento externo nulo: la macro no recibe señal del entorno.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
