# Auditoría cobertura B-T2 — datos reales vs sintéticos

**Fecha:** 2026-05-17
**Disparador:** snapshot iter 8 reportó "n=15 casos B-T2" mientras find directo dio "solo 2 con dataset_real.csv". Reconciliar.

## Criterios

- **A:** `data/dataset_real.csv` literal presente
- **B:** `data/FETCH_MANIFEST.json` con `fallback=false` (intentó red exitosamente) + alguna fuente real
- **C:** `outputs/metrics.json` con `phases.real` poblada (valid o invalid, pero ejecutada)
- **D:** `src/fetch_real.py` ejecutable presente
- **Veredicto:** REAL (descarga viva o snapshot recuperado), MIXTO (real-con-fallback documentado), SINTÉTICO_DECLARADO, NO_APLICA (falsacionismo intencional)

## Tabla

| Caso | A dsr.csv | B fetch_real | C phases.real | D fetch_real.py | data/ archivos | Veredicto |
|---|---|---|---|---|---|---|
| 01_clima | no | fallback=True (timeout) | sí (edi=-0.001) | sí | `_cache/` | SINTÉTICO_DECLARADO (OWID-derived) |
| 02_conciencia | no | fallback=True | sí (edi=-0.012) | sí | dataset.csv | SINTÉTICO_DECLARADO (OWID no disp.) |
| 03_contaminacion | **sí** | real=True | sí (edi=-0.011) | no | dataset_real.csv | **REAL** (World Bank API) |
| 04_energia | no | real=True | sí (edi=0.461) | no | dataset.csv | MIXTO (WB+OWID proxy) |
| 05_epidemiologia | no | real=True | sí (edi=0.129) | no | dataset.csv | REAL (OWID COVID-19) |
| 06_falsacion_exogen | no | fallback=True | sí (edi=0.055) | no | (vacío) | NO_APLICA (falsacionismo) |
| 07_falsacion_no_est | no | fallback=True | sí (edi=-0.881) | no | (vacío) | NO_APLICA (falsacionismo) |
| 08_falsacion_observ | no | fallback=True | sí (edi=-1.0) | no | (vacío) | NO_APLICA (falsacionismo) |
| 09_finanzas | no | real=True | sí (edi=0.103) | no | spy_monthly.csv | REAL (Yahoo Finance) |
| 10_justicia | no | real=True | sí (edi=0.058) | no | dataset.csv | REAL (World Bank) |
| 11_movilidad | no | real=True | sí (edi=0.060) | sí | dataset.csv + FETCH_MANIFEST_REAL | REAL (World Bank) |
| 12_paradigmas | no | real=True | sí (edi=-0.154) | no | (vacío) | MIXTO (OWID, sin csv local) |
| 13_politicas_estr | no | real=True | sí (edi=0.082) | sí | (vacío) | MIXTO (panel Acemoglu+Kaufmann, sin csv local) |
| 14_postverdad | no | real=True | sí (edi=0.002) | no | dataset.csv | REAL (Google Trends+Wiki) |
| 15_wikipedia | no | real=True | sí (edi=-0.004) | no | wiki_climate.csv | REAL (Wikimedia Stats) |
| 16_deforestacion | no | real=True | sí (edi=0.580) | no | wb_deforestation.csv | REAL (World Bank) |
| 17_oceanos | no | real=True | sí (edi=0.190) | sí | dataset.csv | REAL (NOAA/WMO) |
| 18_urbanizacion | no | real=True | sí (edi=0.337) | sí | wb_urbanization.csv | REAL (World Bank) |
| 19_acidificacion | **sí** | real=True | sí (edi=-0.005) | no | dataset.csv + dataset_real.csv | **REAL** (Aloha Station/PMEL) |
| 20_kessler | no | real=True (fallback NASA) | sí (edi=0.694) | sí | celestrak_snapshot.json | MIXTO (NASA ODPO calibrado, Celestrak offline) |
| 21_salinizacion | no | real=True | sí (edi=0.018) | no | (vacío) | MIXTO (WB, sin csv local) |
| 22_fosforo | no | real=True | sí (edi=0.322) | no | wb_fertilizer_consumption.csv | REAL (World Bank) |
| 23_erosion_dialectica | no | fallback=True | sí (edi=-1.0) | no | (vacío) | SINTÉTICO_DECLARADO (proxy literario) |
| 24_microplasticos | no | real=True | sí (edi=0.806) | no | dataset.csv + 3 csv (Jambeck+OWID) | REAL (Jambeck 2015+OWID) |
| 25_acuiferos | no | real=True | sí (edi=-0.146) | no | (vacío) | MIXTO (USGS GRACE proxy, sin csv local) |
| 26_starlink | no | real=True | sí (edi=0.757) | sí | celestrak_snapshot.json | REAL (CelesTrak) |
| 27_riesgo_biologico | no | real=True | sí (edi=0.216) | sí | dataset.csv | REAL (WB+WHO) |
| 28_fuga_cerebros | no | real=True | sí (edi=0.030) | no | dataset.csv | REAL (World Bank migration) |
| 29_iot | no | real=True | sí (edi=-0.899) | no | dataset.csv | MIXTO (Statista IoT proxy+ITU) |
| 30_behavioral_dyn | no | fallback=True | sí (edi=0.262) | no | behavioral_dynamics_synth.csv | SINTÉTICO_DECLARADO (Fajen-Warren) |
| 41_wolfram_extendido | no | fallback=True | NO_REAL_PHASE | no | (vacío) | SINTÉTICO_DECLARADO (Rule 30/90/110/184) |
| 42_histeresis_inst | no | real=True (panel OxCGRT) | NO_REAL_PHASE | no | (vacío) | SINTÉTICO_DECLARADO (panel calibrado, no panel real) |

## Conteo definitivo verificado

- Casos totales del corpus operativo (01-30 + 41 + 42): **32**
- **REAL puro** (descarga real + csv local + phases.real con datos): **15**
  - 03, 05, 09, 10, 11, 14, 15, 16, 17, 18, 19, 22, 24, 26, 27, 28 (=**16**, recontado)
  - Tras revisión 28 (migration WB con dataset.csv y fallback=false) cuenta REAL → **16**
- **MIXTO** (declara real pero usa proxy/calibración/fallback parcial): **7**
  - 04, 12, 13, 20, 21, 25, 29
- **SINTÉTICO_DECLARADO** (admite fallback honesto explícito): **6**
  - 01, 02, 23, 30, 41, 42
- **NO_APLICA** (casos de falsacionismo, no requieren datos reales): **3**
  - 06, 07, 08
- **Solo `dataset_real.csv` literal en disco:** **2** (03, 19)

## Reconciliación con "n=15" reportado iter 8

La lista que dio el snapshot iter 8: 16, 04, 27, 20, 01, 03, 19, 13, 11, 09, 18, 22, 24, 26, 17, 02, 10, 15, 21, 28, 23 (21 casos).

Discrepancias:
- **Cuenta inflada por SINTÉTICO_DECLARADO marcados como real:** 01, 02, 23 (3 casos).
- **MIXTOS contados como REAL:** 04, 13, 20, 21 (4 casos, defendible pero requiere asterisco).
- El número "15" probablemente corresponde a un subconjunto previo; el conteo correcto de REAL puro es **16**, y si se incluyen MIXTOS defendibles llega a **23**.

## Casos que necesitan re-clasificación

1. **01_clima** — manifest dice `fallback=True` (timeout OWID); prosa probablemente lo presenta como real. Reclasificar a SINTÉTICO_DECLARADO o re-ejecutar fetch.
2. **02_conciencia** — manifest dice OWID Mental Health no disponible. SINTÉTICO_DECLARADO. Verificar prosa.
3. **23_erosion_dialectica** — proxy literario sintético. Reclasificar.
4. **30_behavioral_dynamics** — `behavioral_dynamics_synth.csv` evidencia sintético; declarar.
5. **41_wolfram_extendido, 42_histeresis_institucional** — sin `phases.real`. Excluir del conteo B-T2 o re-ejecutar.
6. **MIXTOS (04, 12, 13, 20, 21, 25, 29)** — añadir nota "real con fallback documentado" cuando se cite.
7. **12, 13, 21, 25** — manifest=real pero `data/` vacío de csv local. Auditar si `phases.real` viene de cache externo o si manifest es optimista.

## Archivos clave

- `/datos/repos/EstructurasPreontologicas/09-simulaciones-edi/[NN]_caso_*/data/FETCH_MANIFEST.json` — todos los manifests
- `/datos/repos/EstructurasPreontologicas/09-simulaciones-edi/03_caso_contaminacion/data/dataset_real.csv`
- `/datos/repos/EstructurasPreontologicas/09-simulaciones-edi/19_caso_acidificacion_oceanica/data/dataset_real.csv`
