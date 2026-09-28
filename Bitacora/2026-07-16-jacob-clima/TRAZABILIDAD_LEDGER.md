# Ledger de trazabilidad de datos — corpus EDI (tesis pre-ontológicas + precursora hiperobjetos)

_Auditoría determinista sobre `/workspace/EstructurasPreontologicas/09-simulaciones-edi`._

## Resumen

- **n_cases**: 42
- **n_excluidos_subprobe_template**: 8
- **integridad_REAL_VERIFICADO**: 26
- **integridad_REAL_con_FALLBACK**: 3
- **integridad_SINTETICO_DECLARADO**: 12
- **integridad_INDETERMINADO**: 1
- **n_con_manifest**: 42
- **n_sin_manifest**: 0
- **n_sha_tbd**: 8
- **n_sinteticos**: 12
- **n_reales**: 29
- **n_syn_indeterminado**: 0
- **n_sin_fase_real**: 12
- **n_sin_setup_hash**: 0
- **n_sin_cmd_repro**: 41

Convención tabla: EDI`*` = permutación significativa · `✓` = gate completo (overall_pass) · `·` = no pasa.

## Corpus interdominio (32 casos)

| Caso | Nombre | Integridad | LoE | EDI synth | EDI real | Fuente | SHA | Flags |
|---|---|---|---|---|---|---|---|---|
| 01_caso_clima | Clima Regional (CONUS) | 🟠 sint | 5 | 0.069* · | 0.269 · | Realistic synthetic (OWID-derived, d | tbd | SHA256_TBD,SYN@LoE≥4 |
| 02_caso_conciencia | Conciencia Colectiva | 🟠 sint | 3 | -0.007 · | -0.012 · | Sintético fallback (OWID Mental Heal | ok | SIN_CMD_REPRO |
| 03_caso_contaminacion | Contaminación PM2.5 | 🟢 real | 3 | 0.227* · | -0.011 · | World Bank Open Data API | ok | SIN_CMD_REPRO |
| 04_caso_energia | Energía (Consumo Per Cáp | 🟡 real?fb | 3 | 0.330* ✓ | 0.157* · | Real energy data (synthetic proxy to | tbd | FB,SHA256_TBD,SIN_CMD_REPRO |
| 05_caso_epidemiologia | Epidemiología (COVID-19  | 🟢 real | 3 | 0.328* ✓ | 0.129* · | OWID COVID-19 | ok | SIN_CMD_REPRO |
| 06_caso_falsacion_exogeneidad | Falsación: Exogeneidad | 🟠 sint | 1 | — | 0.055 · | Random walk sintético | ok | SIN_CMD_REPRO |
| 07_caso_falsacion_no_estacionariedad | Falsación: No-Estacionar | 🟠 sint | 1 | — | -0.882 · | Random walk con drift sintético | ok | SIN_CMD_REPRO |
| 08_caso_falsacion_observabilidad | Falsación: Observabilida | 🟠 sint | 1 | — | -1.000 · | Sistema con variable latente sintéti | ok | SIN_CMD_REPRO |
| 09_caso_finanzas | Finanzas (SPY) | 🟢 real | 5 | -0.665 · | 0.103* · | Yahoo Finance | ok | SIN_CMD_REPRO |
| 10_caso_justicia | Justicia Algorítmica | 🟢 real | 5 | 0.045 · | 0.058* · | World Bank Open Data | ok | SIN_CMD_REPRO |
| 11_caso_movilidad | Movilidad Urbana (Vehícu | 🟢 real | 5 | 0.363 · | 0.060 · | World Bank Open Data | ok | SIN_CMD_REPRO |
| 12_caso_paradigmas | Paradigmas Científicos ( | 🟢 real | 3 | -0.144 · | -0.172 · | Semantic Scholar API (cached empiric | tbd | SHA256_TBD,SIN_CMD_REPRO |
| 13_caso_politicas_estrategicas | Políticas Estratégicas ( | 🟢 real | 3 | -0.015 · | 0.082 · | Multi-country institutional effectiv | ok | SIN_CMD_REPRO |
| 14_caso_postverdad | Postverdad (SIS Infodemi | 🟢 real | 3 | -0.012 · | 0.002 · | Google Trends + Wikipedia stats | ok | SIN_CMD_REPRO |
| 15_caso_wikipedia | Wikipedia (Conocimiento  | 🟢 real | 3 | 0.196* · | -0.004 · | Wikimedia Statistics | ok | SIN_CMD_REPRO |
| 16_caso_deforestacion | Deforestación Global (vo | 🟢 real | 3 | 0.040 · | 0.580* ✓ | World Bank Open Data forest area | ok | SIN_CMD_REPRO |
| 17_caso_oceanos | Océanos (OHC proxy) | 🟢 real | 3 | 0.137* · | 0.190* · | WMO/PMEL | ok | SIN_CMD_REPRO |
| 18_caso_urbanizacion | Urbanización Global | 🟢 real | 3 | 0.833* ✓ | 0.337* ✓ | World Bank Open Data | ok | SIN_CMD_REPRO |
| 19_caso_acidificacion_oceanica | Acidificación Oceánica | 🟢 real | 3 | 0.000 · | -0.005 · | NOAA PMEL/Aloha HOT-DOGS | tbd | SHA256_TBD,SIN_CMD_REPRO |
| 20_caso_kessler | Kessler (Debris Orbital) | 🟡 real?fb | 3 | -0.139 · | -1.000 · | NASA ODPO calibrated (fallback from  | tbd | FB,SHA256_TBD,SIN_CMD_REPRO |
| 21_caso_salinizacion | Salinización de Suelos ( | 🟢 real | 3 | -0.003 · | 0.515* ✓ | World Bank irrigated land | ok | SIN_CMD_REPRO |
| 22_caso_fosforo | Ciclo del Fósforo (Carpe | 🟢 real | 3 | 0.192* · | 0.322* ✓ | World Bank - Fertilizer consumption  | ok | SIN_CMD_REPRO |
| 23_caso_erosion_dialectica | Erosión Dialéctica (Abra | ⚪ ? | 3 | -0.019 · | -1.000 · | OpenAlex API | tbd | SHA256_TBD,SIN_CMD_REPRO |
| 24_caso_microplasticos | Microplásticos Oceánicos | 🟢 real | 3 | 0.076 · | -1.000 · | Jambeck 2015 et al. + OWID | ok | SIN_CMD_REPRO |
| 25_caso_acuiferos | Depleción de Acuíferos ( | 🟡 real?fb | 3 | -0.061 · | 0.004 · | USGS GRACE proxy | ok | FB,SIN_CMD_REPRO |
| 26_caso_starlink | Constelaciones Satelital | 🟢 real | 3 | -0.425 · | 0.757 · | CelesTrak | ok | SIN_CMD_REPRO |
| 27_caso_riesgo_biologico | Riesgo Biológico Global  | 🟢 real | 3 | -0.003 · | 0.216 · | World Bank mortality + WHO | ok | SIN_CMD_REPRO |
| 28_caso_fuga_cerebros | Fuga de Cerebros Global  | 🟢 real | 3 | -0.007 · | 0.030 · | World Bank net migration tertiary | ok | SIN_CMD_REPRO |
| 29_caso_iot | Ecosistema IoT Global (B | 🟢 real | 3 | -0.009 · | -0.899 · | World Bank Open Data API | ok | SIN_CMD_REPRO |
| 30_caso_behavioral_dynamics | Behavioral Dynamics — Lo | 🟠 sint | 2 | 0.133 · | 0.262* · | Sintético generado por sistema compl | ok | SIN_CMD_REPRO |
| 41_caso_wolfram_extendido | 41_caso_wolfram_extendid | 🟠 sint | 3 | -0.275 · | — | Sintético — autómatas celulares Rule | tbd | SHA256_TBD,SIN_FASE_REAL,SIN_CMD_REPRO |
| 42_caso_histeresis_institucional | 42_caso_histeresis_insti | 🟢 real | 4 | 0.777 ✓ | — | Panel sintético calibrado OxCGRT (Ha | tbd | SHA256_TBD,SIN_FASE_REAL,SIN_CMD_REPRO |

## Corpus multiescala (10 casos)

| Caso | Nombre | Integridad | LoE | EDI synth | EDI real | Fuente | SHA | Flags |
|---|---|---|---|---|---|---|---|---|
| corpus_multiescala/31_decoherencia_cuantica | corpus_multiescala/31_de | 🟢 real | 4 | — | — | Sintético Lindblad — parámetros tran | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/32_espin_orbita | corpus_multiescala/32_es | 🟠 sint | 3 | — | — | Sintético Bloch — parámetros NV-cent | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/33_villin_headpiece | corpus_multiescala/33_vi | 🟠 sint | 3 | — | — | Sintético MSM 2-estados — Anton 2 Sh | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/34_michaelis_menten | corpus_multiescala/34_mi | 🟢 real | 3 | — | — | Sintético MM — parámetros BRENDA | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/35_ciclo_celular | corpus_multiescala/35_ci | 🟠 sint | 3 | — | — | Sintético Tyson-Novak | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/36_nfkb | corpus_multiescala/36_nf | 🟠 sint | 3 | — | — | Sintético Hoffmann — parámetros lite | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/37_hrv_cardiaco | corpus_multiescala/37_hr | 🟢 real | 3 | — | — | Sintético Mackey-Glass — parámetros  | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/38_locomocion_alternativa | corpus_multiescala/38_lo | 🟠 sint | 2 | — | — | Sintético τ-dot — Lee 1976 modelo si | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/39_cefeidas_ogle | corpus_multiescala/39_ce | 🟢 real | 4 | — | — | Sintético Leavitt P-L — parámetros O | ok | SIN_FASE_REAL,SIN_CMD_REPRO |
| corpus_multiescala/40_cumulos_globulares | corpus_multiescala/40_cu | 🟢 real | 4 | — | — | Sintético Plummer — parámetros Gaia  | ok | SIN_FASE_REAL,SIN_CMD_REPRO |

## Huecos de trazabilidad priorizados

- **REAL declarado pero con fallback/proxy sintético (contradicción a resolver)** (3): 04_caso_energia, 20_caso_kessler, 25_caso_acuiferos
- **Sin FETCH_MANIFEST (provenance ausente)** (0): —
- **SHA256 = 'tbd' (integridad no verificable)** (8): 01_caso_clima, 04_caso_energia, 12_caso_paradigmas, 19_caso_acidificacion_oceanica, 20_caso_kessler, 23_caso_erosion_dialectica, 41_caso_wolfram_extendido, 42_caso_histeresis_institucional
- **Sintético pese a LoE≥4 (deuda dato-real)** (1): 01_caso_clima
- **Sin fase real (solo corrida sintética)** (12): 41_caso_wolfram_extendido, 42_caso_histeresis_institucional, corpus_multiescala/31_decoherencia_cuantica, corpus_multiescala/32_espin_orbita, corpus_multiescala/33_villin_headpiece, corpus_multiescala/34_michaelis_menten, corpus_multiescala/35_ciclo_celular, corpus_multiescala/36_nfkb, corpus_multiescala/37_hrv_cardiaco, corpus_multiescala/38_locomocion_alternativa, corpus_multiescala/39_cefeidas_ogle, corpus_multiescala/40_cumulos_globulares
- **Sin SETUP_HASH** (0): —
- **Sin comando de reproducción declarado** (41): 02_caso_conciencia, 03_caso_contaminacion, 04_caso_energia, 05_caso_epidemiologia, 06_caso_falsacion_exogeneidad, 07_caso_falsacion_no_estacionariedad, 08_caso_falsacion_observabilidad, 09_caso_finanzas, 10_caso_justicia, 11_caso_movilidad, 12_caso_paradigmas, 13_caso_politicas_estrategicas, 14_caso_postverdad, 15_caso_wikipedia, 16_caso_deforestacion, 17_caso_oceanos, 18_caso_urbanizacion, 19_caso_acidificacion_oceanica, 20_caso_kessler, 21_caso_salinizacion, 22_caso_fosforo, 23_caso_erosion_dialectica, 24_caso_microplasticos, 25_caso_acuiferos, 26_caso_starlink, 27_caso_riesgo_biologico, 28_caso_fuga_cerebros, 29_caso_iot, 30_caso_behavioral_dynamics, 41_caso_wolfram_extendido, 42_caso_histeresis_institucional, corpus_multiescala/31_decoherencia_cuantica, corpus_multiescala/32_espin_orbita, corpus_multiescala/33_villin_headpiece, corpus_multiescala/34_michaelis_menten, corpus_multiescala/35_ciclo_celular, corpus_multiescala/36_nfkb, corpus_multiescala/37_hrv_cardiaco, corpus_multiescala/38_locomocion_alternativa, corpus_multiescala/39_cefeidas_ogle, corpus_multiescala/40_cumulos_globulares
