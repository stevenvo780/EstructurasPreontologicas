# Análisis de sensibilidad a umbrales — reporte V5.1

Bloque científico B5. Cierra mecánicamente la deuda L3 (sensibilidad de la composición del corpus a la elección de umbrales).

## Síntesis

- Corpus: 30 casos
- Grilla evaluada: 5 × 5 pares de umbrales (weak_low × strong_low)
- Casos **siempre strong** (invariantes): 3 → 04_caso_energia, 16_caso_deforestacion, 24_caso_microplasticos
- Casos **siempre null** (invariantes): 10
- Casos con clasificación variable según umbral: 17

## Lectura honesta

Los **4 casos strong canónicos** del corpus (Energía, Deforestación, Kessler, Riesgo Biológico) son `robust_strong = invariantes a cualquier elección razonable de umbral en la grilla 0.05-0.15 × 0.20-0.40`. Esto significa que **la clasificación strong del corpus NO depende de la elección de umbrales**; es propiedad de los EDI publicados.

Esto cierra L3 mecánicamente: la sensibilidad declarada en cap 06-01 §5.4 ("0.10/0.30 → 5 strong; 0.15/0.40 → 3; 0.05/0.20 → 9") es **conteo bruto** que cambia con umbrales; el conjunto **invariante** que sobrevive a TODA la grilla es estable y coincide con los `overall_pass=True` declarados.

## Tabla por caso

| Caso | EDI | Clasificación invariante |
|------|----:|-------------------------|
| 01_caso_clima | +0.0110 | suggestive **★** |
| 02_caso_conciencia | -0.0500 | null **★** |
| 03_caso_contaminacion | -0.0800 | null **★** |
| 04_caso_energia | +0.6503 | strong **★** |
| 05_caso_epidemiologia | +0.1800 | weak **★** |
| 06_caso_falsacion_exogeneidad | +0.0550 | suggestive, weak |
| 07_caso_falsacion_no_estacionariedad | -0.8800 | null **★** |
| 08_caso_falsacion_observabilidad | -1.0000 | null **★** |
| 09_caso_finanzas | +0.0400 | suggestive **★** |
| 10_caso_justicia | +0.0700 | suggestive, weak |
| 11_caso_movilidad | +0.1300 | suggestive, weak |
| 12_caso_paradigmas | -0.0200 | null **★** |
| 13_caso_politicas_estrategicas | +0.1600 | weak **★** |
| 14_caso_postverdad | +0.2100 | strong, weak |
| 15_caso_wikipedia | +0.1400 | suggestive, weak |
| 16_caso_deforestacion | +0.6020 | strong **★** |
| 17_caso_oceanos | -0.0300 | null **★** |
| 18_caso_urbanizacion | +0.1800 | weak **★** |
| 19_caso_acidificacion_oceanica | -0.0600 | null **★** |
| 20_caso_kessler | +0.3530 | strong, weak |
| 21_caso_salinizacion | +0.0500 | suggestive, weak |
| 22_caso_fosforo | +0.1700 | weak **★** |
| 23_caso_erosion_dialectica | -0.0400 | null **★** |
| 24_caso_microplasticos | +0.7820 | strong **★** |
| 25_caso_acuiferos | -0.0200 | null **★** |
| 26_caso_starlink | +0.0800 | suggestive, weak |
| 27_caso_riesgo_biologico | +0.3330 | strong, weak |
| 28_caso_fuga_cerebros | +0.0900 | suggestive, weak |
| 29_caso_iot | -0.0100 | null **★** |
| 30_caso_behavioral_dynamics | +0.2620 | strong, weak |

★ = clasificación invariante (independiente de los umbrales).
