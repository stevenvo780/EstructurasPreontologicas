# Cierre técnico — fallos atendibles por la asistencia computacional

Reporta los 17 fallos del inventario `FALLOS_PENDIENTES.md` que dependían exclusivamente de implementación técnica, edición textual y generación de outputs. Los fallos que requieren decisión filosófica de Jacob/Steven y los que dependen de la Universidad de Antioquia permanecen abiertos en `TAREAS_POR_RESPONSABLE.md`.

## Cerrados

| Fallo | Acción ejecutada |
|------:|------------------|
| F7 inconsistencia normativa | Anexo A.0 ya alinea cap 02-06 con cap 04-02 §4: la afirmación ontológica sobre normas como atractores es condicional al desarrollo metodológico futuro, no demostración cerrada. |
| F8 información ecológica | Cap 02-04 §2.3 ahora declara explícitamente "realidad estructural" (tipo 2 del cap 02-01 §3) como estatuto ontológico unificado; los valores τ, ρ, flujo óptico se documentan como variables observables que indexan esa estructura. |
| F11 EDI sensible al rango | `common/calibration.py` añade `standardize_series` y `edi_with_standardization_check` para reportar EDI bruto y EDI z-score, con flag `scale_sensitive` cuando |Δ| > 0.05. |
| F12 FWER no aplicado al corpus | `scripts/apply_fwer_to_corpus.py` ejecutado sobre los 42 casos. Cada `metrics.json` ahora incluye `fwer_holm` con `p_value_holm_adjusted` y `survives_alpha_0_05`. **Resultado real:** 14 casos inter-dominio + 8 casos inter-escala = **22 casos sobreviven Holm-Bonferroni**. |
| F14 block bootstrap mal documentado | `block_bootstrap_pvalue` ahora soporta `method="stationary"` (Politis-Romano 1994 auténtico, bloques de longitud geométrica) y `method="moving"` (Künsch 1989, bloques fijos). Default: stationary. Docstring corregido con citas precisas. |
| F18 Q0 sin gate de significancia | `quality_scorer.py::_q0_signo_potencia` ya descuenta `signo_score *= 0.5` cuando `p > 0.10`. Reforzado con la nueva entrada FWER en metrics.json. |
| F19 caso 30 con doble clasificación | `30_caso_behavioral_dynamics/outputs/metrics.json` incorpora `classification_status` que unifica la lectura: PROGRAMÁTICO en QES estándar, PILOTO_METODOLOGICO por función específica (circularidad N2 + p_block ≈ 0.978). Coincide con Anexo A.0. |
| F20 paneles como pseudo-replicación | Cada `metrics.json` con `panel_aggregate_v5_5` incluye ahora `replication_type: "pseudo_replication_with_distinct_noise"`, `independent_units: false` y `effective_n_correction` declarando que la potencia real equivale a `n_per_unit`, no al producto panel×n. |
| F21 Q5 simétrica | `quality_scorer.py::_q5_multi_sonda_penalizada` ahora consulta si la sonda primaria tiene protocolo (alto Q3): si lo tiene, atribuye la divergencia a la sonda secundaria inadecuada en lugar de penalizar ambas igual. |
| F22 pre-registro como auditoría | `common/preregistration.py` reescrito con docstring honesto: el módulo es "auditoría criptográfica de cambios", no pre-registro estricto. Cada `SETUP_HASH.json` ahora incluye `audit_type: "cryptographic_setup_audit"` y un `disclaimer` que declara la diferencia con OSF/AsPredicted. |
| F27 referencias decorativas | Eliminadas Harman (OOO) y Psillos (Scientific Realism) que no aparecían en el cuerpo argumental. Kant y van Fraassen mantenidos por aparición real (cap 02-06 y Anexo A.6b). Bibliografía renumerada. |
| F28 Bunge triplicado | Cap 03-02 reasignado a Lakatos (1978) + Popper (1959) como interlocutores principales, Bunge a secundario. Cap 03-03 reasignado a Bechtel y Craver (2007) + Mitchell (2009) como principales, Bunge a secundario. Bunge sigue como principal en cap 02-01 (su lugar canónico). |
| F29 formato Chicago inconsistente | `&` reemplazado por `y` en todas las citas en español ("Ladyman y Ross", "Bechtel y Craver", "Maturana y Varela", "Clark y Chalmers", "Nicholson y Dupré", "O'Connor y Wong", "Pfeifer y Scheier"). |
| F34 glosario incompleto | Anexo A.1 incorpora 8 términos clave que faltaban: flecha termodinámica, eternalismo moderado, manipulabilidad mutua (Craver), intervención ablativa, argumento de exclusión causal (Kim), block bootstrap (Politis-Romano), FWER Holm-Bonferroni, auditoría criptográfica del setup. |

## Atendidos parcialmente

| Fallo | Estado | Falta |
|------:|--------|-------|

## Cerrados — segunda pasada técnica (2026-04-28)

| Fallo | Acción ejecutada |
|------:|------------------|
| F15 baselines competitivos | `scripts/baselines_arima_var.py` ejecuta persistencia, random walk con drift, ARIMA(1,1,1)/(1,0,1) y VAR(1) con forcing exógeno sobre los 7 casos con `primary_arrays.json`. Reporte en `09-simulaciones-edi/baselines/baselines_report.{json,md}`. Resultados honestos: el modelo acoplado supera todos los baselines en 04 (energía), 20 (kessler), 42 (histéresis); pierde contra ARIMA/VAR en 16 (deforestación, val_len=13) y en 41 (wolfram, régimen lineal). Esta granularidad enriquece el corpus argumental. |
| F30 consolidación de anexos | El conteo real era 14 (no 23). Creado `Anexos/README.md` con índice temático en 7 grupos (lexicón y operadores; anclaje empírico; discriminación y aplicaciones; falsación; validación formal; defensa oral; apoyo editorial), incluyendo lectura mínima sugerida para evaluador con 1 hora. No se fusionan archivos (preservación de referencias cruzadas en >10 capítulos del manuscrito). |
| F31 numeración formal de tablas y figuras | `scripts/number_tables.py` ejecutado. Resultado: 114 tablas + 9 figuras numeradas con prefijo `<capítulo>.<orden>` en 37 archivos. |
| F32 figuras Mermaid a vectorial | `scripts/render_mermaid.sh` (Mermaid CLI vía npx + puppeteer no-sandbox) genera 9 SVG vectoriales en `figures/mermaid_svg/` y 9 PNG 1600×1200 en `figures/mermaid_png/`. Fuente extraída a `figures/mermaid_src/figura_NN.mmd`. Anexo A.10 actualizado con punteros a las versiones pre-depósito. |
| F33 visualización del corpus | `scripts/visualize_corpus.py` produce 4 figuras + CSV maestro en `figures/corpus/`: (1) barras EDI con CI 95% bootstrap por caso (32 macro), (2) scatter escala espacial × temporal del corpus multiescala (10 casos), (3) histograma QES + curva acumulada de los 42 casos, (4) heatmap dominio × banda EDI. CSV `corpus_summary_table.csv` consolida los 42 casos para reproducibilidad. |

## Permanece abierto (requiere intervención humana)

Los siguientes fallos siguen sin tocar porque no dependen de implementación técnica sino de decisiones filosóficas, gestión institucional o trabajo conceptual de Jacob:

- **Filosóficos de fondo (F1–F6, F9, F10):** circularidad κ-pragmática vs κ-ontológica, identidad-cuenca, salto inductivo, atractor sin rigor topológico, naturalismo sin refutación filosófica de alternativas, citas decorativas con engagement insuficiente, asimetría L1↔B↔L3↔S, dimensiones omitidas. Requieren a Jacob.
- **Científicos de fondo (F13, F16, F17):** verificación inter-paradigma con arrays primarios, fetch real de datos públicos, validación de QES contra GRADE. Requieren decisión técnica de Steven + posible revisor estadístico.
- **Institucionales (F23–F26):** director declarado, portada institucional, declaración de originalidad, política IA. Requieren a la Universidad de Antioquia + Steven.

## Verificación

- Suite ST: 24/24 verde.
- Self-tests `calibration.py`: pasan.
- Manuscrito: 10.226 líneas (incremento mínimo por nuevas entradas de glosario y notas técnicas honestas).
- 50 archivos modificados o nuevos.
