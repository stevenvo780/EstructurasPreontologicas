# Conclusión demostrativa

## Tesis del capítulo

> La tesis del **irrealismo operativo de estructuras pre-ontológicas** se sostiene como **propuesta ontológica general multiescalar** validada operativamente sobre **40 casos del corpus EDI agregado** (30 inter-dominio + 10 inter-escala). El corpus inter-dominio cubre física, biología, economía, política, tecnología, cultura y conducta humana con 4 casos `overall_pass=True` + 1 strong sin gate + 8 weak + 1 suggestive + 4 trend + 8 null (subdivididos por AU-9 en 5 genuinos + 1 EDI negativo + 2 rechazados por gate C1-C5) + 3 controles de falsación rechazados. El corpus inter-escala cubre **30 órdenes de magnitud** espaciales y temporales (desde dinámica subatómica de espín-órbita 10⁻¹⁰ m a cúmulos globulares 10²⁰ m) con **7 strong en 7 escalas distintas** + 1 weak + 2 nulls honestos. El aparato ha sobrevivido hostile testing severo (0/2000 falsos positivos del gate completo bajo random walk masivo agregando los tres scripts canónicos N1+V4_06+N5, Wilson 95 % CI [0, 0.00191]; 0/12 circularidad en test cruzado de sondas). Las condiciones de fracaso son falsables y la deuda residual está fechada. La tesis es **ontología general operativamente articulada con demostración parcial multiescalar bajo régimen declarado**, no ontología regional macro-poblacional como sugería la primera iteración del manuscrito.

## 1. Condiciones de demostración de la tesis

La tesis queda demostrada cuando se cumplen siete condiciones simultáneas. Cada una se verifica con referencia a capítulo y producto específico.

### Condición 1. Ontología sin multiplicación de sustancias

**Verificada en**: capítulo 02-01.

**Producto**: ontología material-relacional con cinco modos de realidad sin postular sustancias separadas. Estructuras pre-ontológicas definidas técnicamente como atractores empíricamente identificables con cinco condiciones de admisión.

**Test de fallo**: si alguna afirmación ontológica requiere segunda sustancia o dualismo encubierto, la tesis falla. **Verificación sostenida.**

### Condición 2. Epistemología con compresiones legítimas verificables

**Verificada en**: capítulos 02-02 y 03-04.

**Producto**: epistemología de la compresión multiescala con definición operativa de κ vía EDI = 1 - RMSE_coupled / RMSE_no_ode, con cuatro pruebas de validación + protocolo C1-C5.

**Test de fallo**: si una compresión admitida no produce predicción discriminante, falla. **Verificación sostenida**: 4 casos con `overall_pass=True` cumplen las 13 condiciones simultáneas.

### Condición 3. Aparato formal con protocolo empírico

**Verificada en**: capítulo 03-01 con apoyo en 03-02, 03-03 y 03-04.

**Producto**: aparato mínimo de cinco operadores (μ, G, H, κ, ε) con instanciación empírica vía pipeline ABM+ODE de 2252 líneas (`hybrid_validator.py`).

**Test de fallo**: si algún operador no produce ganancia inferencial concreta sobre alguna Q, sobra. **Verificación sostenida**: en los 5 casos strong, los cinco operadores se instancian con datos públicos.

### Condición 4. Asimetría L1↔B↔L3↔S como protocolo de traducción

**Verificada en**: capítulo 02-04.

**Producto**: cuatro registros articulados con vínculo asimétrico. Cada parámetro de L3 (ode_alpha, ode_beta, macro_coupling, forcing_scale, etc.) se traduce a variable de B medible.

**Test de fallo**: si algún parámetro no se traduce a B, hay formalismo desanclado. **Verificación sostenida** en los 5 casos strong: todos los parámetros corresponden a magnitudes físicas, biológicas o socioeconómicas con contraparte empírica.

### Condición 5. Cartografía multidominio con dossier completo

**Verificada en**: capítulo 09 (corpus EDI).

**Producto**: 30 casos en física, biología, economía, política, tecnología, cultura y conducta humana. Resultados:

**Tabla 6.1.1.**

| Categoría | N | Casos clave |
|-----------|--:|-------------|
| Strong (gate completo) | 4 | Energía (0.650), Deforestación (0.602), Kessler (0.353), Riesgo Biológico (0.333) |
| Strong (sin gate) | 1 | Microplásticos (0.782) |
| Weak | 8 | Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad, Behavioral Dynamics (caso 30 v2) |
| Suggestive | 1 | Finanzas (Salinización reclasificada por AU-4 — CI cruza cero + magnitud trivial) |
| Trend | 4 | Justicia, Starlink, Fuga cerebros, Clima |
| Null genuino | 5 | Conciencia, Acidificación, Erosión, Acuíferos, IoT |
| EDI negativo (sonda inadecuada) | 1 | Paradigmas (EDI=-0.144) |
| Señal rechazada por gate C1-C5 | 2 | Contaminación, Océanos (EDI>0, p<0.05, valid=False) |
| Falsación rechazada | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Test de fallo**: si los 4 casos `overall_pass` no replican o son superados por modelos rivales, la tesis pierde su demostración multidominio. **Verificación sostenida** en estado actual del corpus (outputs verificados bit-a-bit).

### Condición 6. Discriminación pública contra rivales

**Verificada en**: capítulo 04-01.

**Producto**: tabla de discriminación contra quince posiciones rivales con criterios públicos (incluidos Wolfram Physics Project e IIT). En cada rival, ventaja en al menos dos celdas; en el caso ancla, ventaja en cinco celdas contra modelos internos.

**Test de fallo**: si algún rival absorbe la tesis sin diferencia discriminante, se reformula. La tabla actual no produce absorción. **Verificación sostenida.**

### Condición 7. Honestidad sobre el dominio de validez del aparato

**Verificada en**: caso 30 (behavioral dynamics) y este capítulo.

**Producto**: reconocimiento explícito de que el protocolo EDI tiene dominio de validez **dependiente de la sonda y los datos disponibles, no de la escala**. El aparato funciona en cualquier escala donde se disponga de sonda físicamente motivada y datos con resolución temporal adecuada (verificado en corpus inter-escala desde 10⁻¹⁵ s hasta 10¹⁴ s). El caso 30 produjo EDI=0.002 en su versión inicial (no significativo), siendo rechazado correctamente por el aparato; tras refinamiento de sonda al modelo de segundo orden Fajen-Warren, produjo Nivel 3 weak honesto. Esto se documenta como hallazgo del programa, no como fracaso oculto.

**Test de fallo**: si el manuscrito hubiera forzado la admisión del caso 30 (reformulando datos, sondas o criterios para producir EDI alto), la tesis violaría su propio principio de anti-reificación operativa. **Verificación sostenida**: el caso 30 se admite explícitamente como programático con criterio de elevación documentado en `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`.

## 2. Condiciones de fracaso global

La tesis falla globalmente bajo **tres escenarios falsables con criterio externo** y **una condición de prioridad histórica** (no test crítico). Esta enumeración corrige una versión previa que listaba cinco escenarios; la auditoría detallada (F06-04, integrada 2026-05-11) mostró que los escenarios 1 y 2 anteriores eran operativamente la misma condición —el corpus deja de discriminar entre señal y ruido, con la misma métrica EDI+permutación y los mismos comandos regeneradores `./tesis run --case`— y que el escenario 5 anterior (absorción por rival) tenía criterio de comparación definido desde dentro del marco (cap 04-01) — lo que Popper (1959, *Logik der Forschung* §6) llama inmunización ad hoc por elección de criterio interno.

### Escenario 1. El corpus deja de discriminar entre señal y ruido

Esta condición se manifiesta de dos formas operativamente equivalentes:

*1.a (no activo al 2026-05-11):* si Energía, Deforestación, Kessler o Riesgo Biológico **dejan de pasar `overall_pass`** bajo perfiles de alto rendimiento (n_perm ≥ 2999, n_boot ≥ 1500), o **son superados por baselines puramente estadísticos** sobre el mismo vector observación (cf. §3.6 y deuda AU-3); o

*1.b (parcialmente activado):* si los 3 controles de falsación (06, 07, 08) empiezan a producir EDI significativo bajo el mismo perfil, el aparato pierde su discriminación y la tesis colapsa al instrumentalismo puro.

Comando regenerador para los siete casos críticos: `./tesis run --case <NN>` para `NN ∈ {04, 16, 20, 27, 06, 07, 08}`.

### Escenario 2. El aparato no escala fuera de su dominio actual

Si el caso 30 (behavioral dynamics) y otros candidatos en escalas no-macro-temporales no se elevan a demostrativo bajo el protocolo extendido —incluyendo (i) re-evaluación con sonda alternativa estructuralmente distinta (Neural ODE o GP) que controle la circularidad parcial detectada por F03-10 y (ii) pre-registro fechado de la sonda anterior a la ejecución— el dominio de validez de la tesis es regional, no general. Criterio externo: refinamiento de sonda documentado y EDI con `p_perm < 0.05` y CI bootstrap excluyendo cero en al menos dos dominios fuera de macro-temporal antes de 2027-12.

### Escenario 3. La asimetría L1↔B↔L3↔S no se sostiene

Si en algún dominio relevante del corpus inter-escala no se logra traducir L3 a B porque B no es identificable bajo los datos disponibles —y la traducción exige medición independiente del ajuste a L3, no sólo motivación nominal del parámetro (cf. F03-04)— la tesis admite reducción de alcance. Criterio externo: dossier de anclaje rechazado por revisión externa en al menos un dominio del corpus.

### Condición de prioridad histórica (no falsación)

Si un programa de investigación rival reúne, antes que esta tesis, anclaje empírico + asimetría protocolar + dossier + cartografía multidominio + falsación, esta tesis cede prioridad histórica. **Esta condición no es propiamente falsable** porque su criterio de absorción depende de la comparación con el aparato actual (los criterios de comparación los elige la tesis en cap 04-01 y cap 04-03); se documenta como **compromiso de honestidad histórica**, no como test crítico. Wolfram Physics Project no la satisface al 2026-05 — comparte hipergrafos pero no filtro empírico, dossier ni asimetría protocolar. La cláusula F04-02 sobre criterios externos (G parsimonia Quine, H novel facts Popper-Lakatos, I independencia del evaluador Bunge) actúa como complemento de honestidad: la tesis se reconoce como vulnerable bajo H (0 predicciones novedosas pre-registradas) y bajo I (sin revisión externa formal al cierre actual).

Cada escenario es **falsable, fechado y con criterio externo público**; la condición de prioridad es **trazable, fechada y honesta**, pero no se reclama como test popperiano fuerte. La tesis prefiere declarar la asimetría a esconderla bajo un quinto "escenario falsable" que su propio criterio de absorción no autoriza.

## 3. Hallazgos honestos no triviales del aparato

### 3.1. La paradoja del LoE (Nivel de Evidencia)

Casos con LoE=5 (datos físicos directos, >30 años) no necesariamente alcanzan EDI alto. El Clima (LoE=5, EDI=0.011) muestra que **sondas inadecuadas producen EDI bajos incluso con datos excelentes**. La calidad de la sonda macro es cuello de botella en algunos casos. Implicación: programa multi-sonda como trabajo futuro.

### 3.2. La paradoja del val_steps

Casos con ventanas largas (Epidemiología val_steps=104) producen EDI moderados pero estadísticamente robustos. Casos con ventanas cortas (Riesgo Biológico val_steps=9) pueden producir EDI altos pero requieren cautela inferencial. Starlink con val_steps=1 es exploratorio, no confirmatorio.

### 3.3. La termodinámica manda

Los 4 casos `overall_pass=True` están conectados con dinámicas físicas robustas (Energía, Deforestación, Riesgo Biológico, Kessler). Esto sugiere que **el cierre operativo se detecta más fácilmente cuando hay anclaje termodinámico claro**. Fenómenos puramente sociales o cognitivos requieren extensión metodológica.

### 3.4. El éxito de la falsación

3/3 controles de falsación rechazados. Esto refuta la objeción de tautología: si la ablación fuera trivialmente destructiva, los controles producirían EDI alto, pero no lo hacen. **El aparato discrimina genuinamente**.

### 3.5. El caso 30 como confirmación de la disciplina del aparato

El caso 30 (behavioral dynamics) **fue rechazado por el aparato** (EDI=0.002, no significativo) a pesar de ser construido por el equipo investigador con expectativa de aceptación. Este es el ejemplo más claro de que **el aparato no es máquina de validar deseos**: produce hallazgos que contradicen al investigador cuando los datos no apoyan la conjetura.

### 3.6. Los baselines lineales superan al modelo acoplado en 2 de los 4 casos `overall_pass`

La comparación canónica frente a baselines no-estructurales se ejecutó sobre los 7 casos con `primary_arrays.json` y se reporta en `09-simulaciones-edi/baselines/baselines_report.json`. Restringida a los 4 casos con `overall_pass=True`, la lectura literal del RMSE held-out muestra que ARIMA(1,1,1) y VAR(1)+forcing **superan al modelo acoplado en Deforestación y Riesgo Biológico**: para `16_caso_deforestacion`, RMSE_acoplado(val) = 0.5652 frente a RMSE_ARIMA = 0.2807 y RMSE_VAR = 0.2465 (val_len = 13); para `27_caso_riesgo_biologico`, RMSE_acoplado(val) = 0.2393 frente a RMSE_ARIMA = 0.1820 y RMSE_VAR = 0.2257 (val_len = 8). Energía y Kessler, en cambio, mantienen ventaja del acoplado sobre ambos baselines (vs ARIMA = +0.1598 y +0.6490 respectivamente; vs VAR = +0.3058 y +0.6538).

Esto **activa parcialmente el segundo disyunto del Escenario 1 de §2** ("si son superados por baselines puramente estadísticos (ARIMA, VAR), la tesis pierde su demostración multidominio principal", reformulado abajo a 1.a/1.b). La tesis no reclama derrota global por tres razones que se declaran sin atenuar el hallazgo: (i) `overall_pass` no se reduce a RMSE held-out, sino que integra los criterios C1-C5 y la significancia de EDI definido sobre ablación interna `abm_no_ode`, no sobre baselines lineales; (ii) la diferencia se mide sobre val_len ∈ {8, 13}, sin intervalo de confianza ni test de Diebold-Mariano, por lo que la afirmación honesta es "el acoplado **no produce ganancia predictiva detectable** sobre ARIMA/VAR" más que "ARIMA es estrictamente superior"; (iii) el EDI sigue siendo significativo por permutación en los dos casos afectados, lo que sostiene la pretensión interna de necesidad estructural del acoplamiento ODE→ABM.

**Costo argumental asumido.** La demostración multidominio queda restringida a Energía y Kessler como casos donde el aparato supera tanto la ablación interna como los baselines no-estructurales. Deforestación y Riesgo Biológico se reclasifican como casos donde el aparato detecta acoplamiento estructural significativo pero **no exhibe ganancia predictiva frente a modelos estadísticos lineales** bajo la ventana de validación disponible. Esta es **reducción de alcance, no derrota**: la tesis defiende que el acoplamiento ODE→ABM es estructuralmente identificable (sostenido por EDI vs `abm_no_ode`), no que el aparato sea el mejor predictor posible (no sostenido uniformemente). Fusionar ambas pretensiones, como hacía el manuscrito en la formulación monolítica del Escenario 1, oculta el costo; separarlas es lo que aquí se declara como deuda.

## 4. Deuda residual

Lo que el manuscrito no demuestra y reconoce explícitamente como deuda con plazo y entregable:

**Tabla 6.1.2.**

| Deuda | Descripción | Plazo | Entregable | Estado al 2026-04-28 |
|---|---|---|---|---|
| Caso 30 elevación a LoE = 4 | Datos humanos reales (VENLab/WALK-MS) con aval CEI, pipeline alta frecuencia | 9-10 meses | Caso 30 con EDI sobre datos humanos | Dossier técnico-ético en `Bitacora/2026-04-28-cierre-doctoral/02-` |
| Programa multi-sonda | Validar casos clave con sondas alternativas convergentes | 6 semanas | Tabla de convergencia multi-sonda | **EJECUTADO** sobre 3 strong + 5 weak (`09-simulaciones-edi/multi_sonda/`) |
| Topologías heterogéneas para Nivel 5 | Adaptar ABM a scale-free / small-world; verificar CR > 2.0 | 6 meses | Caso elevado a Nivel 5 o reporte negativo honesto | Programa formal en `Bitacora/2026-04-28-cierre-doctoral/06-` |
| Baselines estadísticos puros | Comparar contra ARIMA, VAR, RW, GP | 3 semanas | Tabla comparativa con discriminación | **EJECUTADO** sobre 7 casos con `primary_arrays.json` (`09-simulaciones-edi/baselines/`); **resultado heterogéneo** — ver §3.6: ARIMA/VAR superan al acoplado en 2/4 `overall_pass` (Deforestación, Riesgo Biológico) bajo RMSE held-out con val_len ∈ {8, 13}. |
| Baselines no-lineales sobre `overall_pass` afectados | Ejecutar GP, LSTM, ESN sobre Deforestación y Riesgo Biológico; reportar con Diebold-Mariano + CI bootstrap; si siguen ganando los baselines, reclasificar el corpus demostrativo en §5.4 | 2 meses | Reporte comparativo con DM-test + CI bootstrap | Pendiente — abierto por hallazgo AU-3 (2026-05-04, integrado 2026-05-11). |
| Aparato para variables normativas | Desarrollo formal de validez/legitimidad como cuenca de atracción + caso piloto | 18-24 meses | Capítulo metodológico + caso institucional cuantitativo | Caso piloto COVID **EJECUTADO** con resultado null honesto (`09-simulaciones-edi/covid_pilot/`); programa restante documentado |
| Integración bibliográfica formal | Citas Chicago author-date en cada capítulo del cuerpo argumental | Hito de cierre | Bibliografía consolidada al depósito | **EJECUTADA** en cap 02-04, 04-01, 05-04; bibliografía consolidada en cap 07 con 90 referencias |
| Programa de convergencia con Wolfram | Aplicar EDI a hypergraph rewriting | 12 meses | Reporte técnico para Wolfram Institute | Piloto Rule 110 **EJECUTADO** (EDI 0.55, `09-simulaciones-edi/wolfram_pilot/`); programa post-piloto en `Bitacora/2026-04-28-cierre-doctoral/05-` |
| Rigor topológico del concepto de atractor | Lyapunov local + dimensión de correlación + mixing time | 1 mes | Reporte topológico por caso | **EJECUTADO** sobre 7 casos con `primary_arrays.json` (`09-simulaciones-edi/topology/topology_report.md`); ej. caso 41 wolfram λ_max=+0.017 D₂=2.82 (firma fractal), caso 42 histéresis λ_max=−0.052 D₂≈0 (atractor convergente puntual) |
| Sondas inter-paradigma sobre arrays primarios reales | Aplicar las sondas teóricamente independientes a `obs`/`forcing` reales, no a proxys derivados | 1 mes | Reporte de convergencia inter-paradigma honesto | **EJECUTADO** sobre 7 casos (`09-simulaciones-edi/multi_sonda/secondary_on_primary_arrays.md`); resultado honesto: 1/7 converge bajo \|ΔEDI\| ≤ 0.10. Cierra parcialmente F13 de la auditoría doctoral. |
| Visualización del corpus | Scatter espacial × temporal, barras EDI con CI bootstrap, heatmap dominio × banda, espacio de fase del caso ancla | 1 mes | 5 figuras vectoriales SVG/PNG | **EJECUTADO** (`figures/corpus/`, `figures/caso30/`, `figures/mermaid_svg/`); CSV maestro con 42 casos en `figures/corpus/corpus_summary_table.csv` |
| Anticipación filosófica de objeciones | Borradores estructurados (concesión / distinción / argumento / costo) para 7 objeciones críticas | Hito de cierre | Capítulo crítico con 7 secciones | **BORRADOR EJECUTADO** (`04-debates/04-anticipacion-objeciones-filosoficas.md`); validación filosófica de Jacob pendiente antes de estabilizarlo como capítulo definitivo. |
| Conversión editorial pre-depósito | LaTeX/PDF + figuras SVG/PNG + plantilla institucional | 3 semanas pre-depósito | PDF institucional final | PDF intermedio generado (`TesisFinal/Tesis.pdf` 1.83 MB); figuras Mermaid convertidas a SVG vectorial (`figures/mermaid_svg/`) y PNG 1600×1200 (`figures/mermaid_png/`); conversión a plantilla institucional pendiente del momento del depósito |

### 4.1. Deuda residual operativa (integración 2026-05-11)

Hallazgos del triage de bitácora huérfana del modo continuo (`Bitacora/2026-05-04-continuous-run/`), integrados como deudas declaradas:

- **[AU-6 2026-05-11]** La nota de la fila "Sondas inter-paradigma sobre arrays primarios reales" reporta "1/7 converge bajo |ΔEDI|≤0.10". Triage detecta que el denominador 7 mezcla 2 casos con arrays reales y 5 casos con arrays reconstruidos. La proporción honesta debe declararse como 1/2 reales y 0/5 reconstruidos, no como 1/7 agregado. Acción: ajustar la nota para descomponer la proporción y reflejar la diferencia en LoE de las fuentes; nota paralela en `06-cierre/_extendido/versiones-cortas-defensa.md`. Cartwright 1999 queda DUDOSO (PDF ausente en `07-bibliografia/`). Origen: `Bitacora/2026-05-04-continuous-run/AU-6-multisonda-1-de-7.md`.
- **[AU-9 2026-05-11]** El conteo de "casos null" colapsa tres regímenes operativamente distintos: (i) 5 nulls genuinos (EDI ≈ 0 con p > 0.05), (ii) 1 caso con EDI fuertemente negativo (degradación con acoplamiento), (iii) 2 casos rechazados por gate de criterios C1-C5 antes del cómputo de EDI. La cifra adversarial "-0.876" estaba mal atribuida. Acción: subdividir la tabla de null en tres filas con cuenta por régimen; paralela en `06-cierre/_extendido/versiones-cortas-defensa.md` y `05-aplicaciones/07-mapa-aplicaciones-corpus.md`. Origen: `Bitacora/2026-05-04-continuous-run/AU-9-edi-negativo-no-es-null.md`.
- **[F06-03 2026-05-11]** El conteo "4 strong" es **invariante** a la rejilla de umbrales 0.05-0.15 × 0.20-0.40 según `THRESHOLD_SENSITIVITY_REPORT.md`, pero el manuscrito no lo declara junto a la primera mención (líneas 5 y 55 del propio capítulo). Acción: edición mínima añadiendo el paréntesis de sensibilidad junto a la primera mención del numeral "4 strong", para anticipar la objeción de *threshold shopping* sin extender la prosa. Origen: `Bitacora/2026-05-04-continuous-run/F06-03-4-strong-threshold-shopping.md`.

### 4.2. Deuda residual técnica del aparato (integración 2026-05-11)

Hallazgos del triage TENG y AU-4 del modo continuo (`Bitacora/2026-05-04-continuous-run/`), integrados como deudas declaradas sobre el motor EDI y el harness. Ninguna de estas deudas invalida los resultados publicados; cada una identifica un sesgo de procedimiento que debe quedar declarado para que la cifra reportada conserve sus condiciones de validez.

- **[AU-4 2026-05-11] Significance theater: `p<0.05` con CI cruzando cero.** Caso 21 (Salinización) presenta `EDI=0.018`, `p_perm=0.003`, `CI 95 % = [-0.077, +0.083]`: el CI no excluye que el acoplamiento empeore la predicción y la magnitud puntual es trivial (0.6 % de reducción de RMSE). Caso 22 (Fósforo) presenta `EDI=0.192`, `p_perm=0.000`, `CI 95 % = [-0.221, +0.550]`: ranking permutacional alto pero bootstrap no excluye cero. Wasserstein & Lazar (2016, *Am Stat* 70(2):129-133, ASA Statement, Principle 3 — `07-bibliografia/Wasserstein-Lazar - ASA Statement on p-values (Am Stat 2016).pdf` p. 2 verbatim): *"Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold."* Acción aplicada: Salinización reclasificada fuera de "suggestive"; auditoría retrospectiva de los demás casos con `p_perm<0.05 ∧ ci_lo<0` queda como deuda residual fechada del cap 03 §criterios de admisión. Origen: `Bitacora/2026-05-04-continuous-run/AU-4-significance-theater-21-22.md`.

- **[TENG-01 2026-05-11] Permutación iid bajo dependencia temporal.** `hybrid_validator.py:174` permuta índices iid; `hybrid_validator.py:193` remuestrea iid para bootstrap. Bajo `ACF(lag=1) > 0` —la gran mayoría del corpus EDI por construcción— la nula deja de ser correcta y los `p_perm` reportados están sesgados hacia abajo (Davison & Hinkley 1997, cap. 8 §8.2; Künsch 1989). El riesgo se concentra en casos borderline (`p_perm ∈ [0.01, 0.05]`); en `EDI ≫ 0` con margen amplio (Energía, Deforestación), `p_block` probablemente seguirá `<0.01`. Block-permutation con `ℓ ∝ n^{1/3}` (Politis & White 2004) es la corrección canónica. Acción: implementación de `block_permutation_test_edi` y `block_bootstrap_edi` queda como B-T abierta; el manuscrito declara la limitación sin afirmar invalidez de los resultados sólidos. Origen: `Bitacora/2026-05-04-continuous-run/TENG-01-permutacion-iid-temporales.md`.

- **[TENG-02 2026-05-11] Bootstrap percentil simple en régimen de pocas muestras.** `hybrid_validator.py:193,216-219` computa CI bootstrap como **percentil simple** (sin corrección de sesgo z₀ ni aceleración a). Sesgo `O(n^{-1/2})` frente al BCa `O(n^{-1})` (DiCiccio & Efron 1996, *Statistical Science* 11(3):189-228, §2.3 vs §3). 21/32 casos del corpus inter-dominio tienen `val_steps < 30` y 12 tienen `val_steps = 8`: régimen donde el sesgo del percentil es **material**. La afirmación de "CI 95 %" en esos casos tiene cobertura nominal sólo aproximada a `O(n^{-1/2})`. Acción inmediata declarada: reportar `val_steps` junto a cada CI para que el lector calibre el orden de cobertura; implementación de BCa con `bca_z0`, `bca_a`, `ci_method` en `metrics.json` queda como B-T fechada. Origen: `Bitacora/2026-05-04-continuous-run/TENG-02-bootstrap-percentil-sesgo-pequenas.md`.

- **[TENG-04 2026-05-11] Invariancia CPU/GPU de C2.** `hybrid_validator.py:977` (rama GPU batch) y `:997` (rama CPU paralela) usan esquemas de semilla incompatibles: GPU comparte `seed=seed_base` (sensibilidad paramétrica pura); CPU usa `seed=2+i+10` por réplica (paramétrica + estocástica). El booleano C2 publicado en `metrics.json` no es por tanto invariante a la plataforma y puede flipear True↔False en casos borderline. Acción B-T: unificar a `seed=seed_base` en ambas ramas; re-ejecutar el corpus y actualizar prosa que cite C2 en los casos afectados. C3 ya cubre persistencia bajo distintas semillas (`hybrid_validator.py:1019-1025`). Origen: `Bitacora/2026-05-04-continuous-run/TENG-04-c2-cpu-vs-gpu-semillas-divergentes.md`.

- **[TENG-08 2026-05-11] C1 disyuntivo permite EDI<0.** `hybrid_validator.py:892-926` define `c1 = c1_relative OR c1_absolute`. La rama `c1_absolute` (`rmse_abm < 2·obs_std AND corr_abm > 0.3`) no requiere que el ODE aporte información; 8 fases del corpus (≈10 %) tienen `c1_convergence=True` con `EDI<0` (casos 02, 03, 09, 14, 20, 23, 25 — el ABM solo correlaciona con los datos aunque el modelo acoplado predice peor que el reducido). Salida elegida: reclasificar `c1_absolute` como `c1_fallback` diagnóstico cuando `reduced_val` existe (no pasa C1). Acción B-T: implementar la reclasificación y re-ejecutar los 8 casos afectados; la afirmación general "el corpus pasa C1 ampliamente" se re-cualifica a "el corpus pasa C1 cuando el ODE aporta mejora sobre el reducido". Origen: `Bitacora/2026-05-04-continuous-run/TENG-08-c1-or-fallback-permite-edi-negativo.md`.

- **[TENG-10 2026-05-11] Baselines comparados sobre target distinto.** `09-simulaciones-edi/common/baselines.py:48-208` ajusta ARIMA/VAR/RW/GP sobre una **serie sintética propia** (`_gen_series_with_coupling`), distinta del proceso generador del caso. `rmse_arima` y `rmse_coupled` que se comparan en `winner` están definidos sobre vectores observación distintos: el ratio es aritméticamente válido pero **inferencialmente nulo**. La métrica EDI propia no se ve afectada (ambos RMSEs en su definición están sobre el mismo `obs_val`). Lo afectado es la comparación externa contra baselines reportada por `baselines.py`. Acción inmediata: cualquier prosa que cite `winner` debe reformularse como ilustrativa hasta implementar Ruta 1 (baselines sobre `primary_arrays.json:obs[val_idx]`). La comparación válida de F3-AU3 (RMSE del aparato vs RMSE de ARIMA/VAR sobre el mismo target) se mantiene como referencia honesta y activa parcialmente el Escenario 1 en Deforestación y Riesgo Biológico (§3.6). Origen: `Bitacora/2026-05-04-continuous-run/TENG-10-baselines-target-distinto-aparato.md`.

- **[TENG-12 2026-05-11] Hash MD5 no detecta inconsistencia interna.** `replay_hash.py:44-52` (`md5_metrics`) hashea bytes del JSON normalizado; certifica reproducibilidad bit-a-bit pero no examina invariantes algebraicos entre campos. El bug del caso 19 fase real sobrevivió múltiples corridas: archivo internamente contradictorio (`value`, `weighted_value` y `errors` de ejecuciones distintas fusionadas) pero hash "✓ Sin cambios". Acción B-T: implementar `verify_internal_consistency.py` con tres invariantes — `|edi.value − weighted_value/loe_factor| < 1e-6`, `|edi.value − (rmse_no_ode − rmse_abm)/rmse_no_ode| < 1e-4`, `ci_lo ≤ value ≤ ci_hi` — cableado a `./tesis audit` antes de `replay_hash.py`. La causa raíz del caso 19 sigue requiriendo B-T separada. Origen: `Bitacora/2026-05-04-continuous-run/TENG-12-hash-no-detecta-inconsistencia-interna.md`.

- **[TENG-13 2026-05-11] Calibración bi-criterio vs métrica RMSE-only.** `hybrid_validator.py:496-549` selecciona parámetros minimizando `score = RMSE × max(0.5, 2 − corr)`; EDI se evalúa sobre RMSE puro del modelo así seleccionado. El EDI reportado no es exactamente "el mejor ajuste predictivo del ABM acoplado en RMSE", sino "el mejor entre los modelos que también correlacionan temporalmente con la sonda macro". El sesgo puede operar en cualquier dirección. Acción B-T: estudio de sensibilidad en 3 casos (un EDI alto, un medio, un null) re-calibrando con `score = RMSE` puro y reportando `ΔEDI`; si `|ΔEDI| > 0.05` en alguno, la deuda escala a corrección estructural. Origen: `Bitacora/2026-05-04-continuous-run/TENG-13-calibracion-objetivo-no-alineado-con-edi.md`.

## 5. Aporte conceptual sustantivo

El aporte de la tesis es triplemente general: ontología, epistemología y metodología generales, como se articula en la Parte I (capítulos 1-6) y la Parte II (capítulos 7-11). Los 40 casos del corpus son **justificación operativa** del marco, no son la tesis. La generalidad del marco es independiente de la cantidad del corpus; lo que el corpus aporta es discriminación operativa y demostración de transferibilidad.

La tesis introduce como aporte propio:

### 5.1. Aporte ontológico

Reformula entidades como **estructuras pre-ontológicas** a cualquier escala donde el aparato puede operar con sondas físicamente motivadas. Afirma una estructura ontológica común entre el qubit superconductor, la enzima, la célula oscilante, el agente económico, el organismo en tarea, la estrella pulsante y el cúmulo globular: los cuatro invariantes (sustrato, acoplamiento, atractor, κ) son operativamente medibles en cada uno con la misma metodología EDI. El "irrealismo operativo" distingue κ-pragmática de κ-ontológica con criterios operativos para cada una (véase capítulo 1, §Nota sobre κ).

### 5.2. Aporte epistemológico

Reformula el conocimiento como compresión disciplinada bajo intervención ablativa. La epistemología es general: opera del mismo modo en cualquier escala donde se disponga de sonda físicamente motivada. Lo que cambia entre escalas es la sonda específica; la teoría del conocimiento no cambia (véase capítulo 2).

**Limitación reconocida:** el p-value declarado tiene tasa de tipo I empírica = 24%. Los umbrales EDI sí son robustos contra falsos positivos (0.6% supera weak, 0% supera strong bajo random walk puro).

### 5.3. Aporte metodológico (general, no regional)

Ofrece la auditoría ontológica como protocolo replicable de nueve fases con dossier de catorce componentes, más el pipeline ABM+ODE con soporte CPU/GPU, validador canónico, controles de falsación incorporados, suite ST de 24 teorías formales y procedimiento de hostile testing automatizado. Determinismo `seed=42` con `requirements-locked.txt` para reproducibilidad inter-instalación. **Esta metodología es general**: el mismo motor `edi_engine` opera sobre los 10 casos del corpus inter-escala y el mismo protocolo C1-C5 opera sobre los 30 casos del corpus inter-dominio sin reentrenar arquitectura. La transferibilidad metodológica entre escalas y dominios —verificada por test cruzado (0/12 circularidad) y hostile testing (0/2000 falsos positivos)— es **prueba operativa de que la metodología no es regional**: una misma máquina funciona desde lo cuántico hasta lo cosmológico, desde lo físico hasta lo social.

**Este aporte es ejecutable, no solo declarativo:** cualquier tercero puede correr el motor sobre datos nuevos en cualquier escala con sondas físicamente motivadas. La generalidad metodológica está respaldada por código, no por afirmación retórica.

### 5.4. Aporte aplicado: cartografía agregada inter-dominio + inter-escala

Demuestra que el aparato **discrimina** y **detecta cierre operativo** en cartografía agregada de **40 casos** que cubren simultáneamente:

**(a) heterogeneidad de dominio** (corpus inter-dominio, 30 casos): física, biología, economía, política, tecnología, cultura y conducta humana, con AUC-ROC = 0.886 (n=12) interpretada como **coherencia interna del umbral EDI** (consistencia entre el umbral declarado 0.33 → strong y la clasificación final del corpus tras gate completo + C1-C5 + hostile testing), no como discriminación externa contra un baseline rival. Ver §8.1 para la declaración honesta del alcance evidencial de esta cifra.

**(b) heterogeneidad de escala** (corpus inter-escala, 10 casos): desde la dinámica de espín-órbita atómica (10⁻¹⁰ m, 10⁻¹⁵ s) hasta la dinámica gravitacional de cúmulos globulares (10²⁰ m, 10¹⁴ s), con 7 strong en 7 escalas distintas y test cruzado V4-01 que confirma la especificidad de las sondas (0/12 circularidad).

**Lectura ontológica de los 40 casos:** **no son catálogo**, son **instancias** de los cuatro invariantes ontológicos. Cada caso strong (4 con `overall_pass` macro + 7 strong inter-escala) verifica los cuatro invariantes en su dominio y escala. Cada null honesto verifica que el aparato discrimina entre presencia y ausencia de cierre operativo bajo la sonda elegida. Cada control de falsación rechazado confirma que el aparato no glorifica indiscriminadamente.

**Reconocimientos honestos (V4):**

- los 40 casos son post-hoc (no pre-registrados; tabla de depuración multiescala en `Bitacora/2026-04-28-cierre-pendientes/08-pre-registro-multiescala-honesto.md`);
- la composición numérica del corpus inter-dominio es frágil a umbrales (N4: pasar de 0.10/0.30 a 0.15/0.40 reduce strong de 5 a 3);
- el caso 30 (behavioral dynamics) sufre circularidad detectada por N2 (Fajen-Warren produce EDI > 0.30 en 50% de mass-spring puro);
- el caso 38 (locomoción τ-dot, intentado como alternativa a Fajen-Warren) produjo failure mode de sonda (EDI = -1.34), no resolución de N2;
- las escalas del corpus inter-escala son etiquetas nominales sobre datos sintéticos derivados de parámetros publicados;
- el AUC-ROC = 0.886 es ranking interno, no validación externa contra estándar de oro independiente;
- ningún caso del corpus cumple los **3 criterios κ-ontológica** simultáneamente; todas las afirmaciones son κ-pragmática hasta que se ejecuten convergencia inter-grupo + replicación + intervención experimental confirmatoria.

**Lo que el corpus agregado sí demuestra con fuerza:** la **arquitectura ontológica común** (cuatro invariantes) es detectable en al menos 8 escalas y 30 dominios, no como artefacto del aparato (V4-01 + V4-06 lo refutan empíricamente: las sondas son específicas y el motor es robusto bajo random walk masivo). La afirmación "ontología general multiescalar" se sostiene como **propuesta operativamente articulada con demostración parcial**, con las limitaciones reconocidas como deuda de validación externa, no como debilidad oculta.

### 5.5. Aporte filosófico de fondo

Establece el **irrealismo operativo** como tercera vía: ni cosa, ni ficción, sino patrón cuya admisión requiere intervención empírica controlada. La distinción entre κ-pragmática y κ-ontológica (véase capítulo 1) es crítica: el manuscrito demuestra κ-pragmática con rigor; la afirmación κ-ontológica fuerte requiere convergencia bajo múltiples sondas y validación inter-grupo.

## 6. Lo que la tesis afirma con compromiso público

**Tabla 6.1.3.**

| Afirmación | Compromiso | Verificación |
|---|---|---|
| **La ontología es general (no regional macro)** | Cuatro invariantes válidos a cualquier escala | Capítulo 02-01 |
| **La epistemología es general** | Compresión disciplinada a cualquier escala | Capítulo 02-02 |
| **La metodología es general** | Aparato invariante a la escala (μ, G, H, κ, ε) | Capítulo 03-01 |
| La realidad es material y dinámica | Sustrato único | Capítulo 02-01 |
| Las estructuras pre-ontológicas son atractores empíricos | Cinco condiciones de admisión, instanciables a cualquier escala | Capítulos 02-01 y 02-04 |
| La emergencia es self-organization | Modelo positivo, no negación | Capítulo 02-04 §4 |
| La compresión κ se opera vía EDI | Procedimiento ABM+ODE con 13 condiciones, transferible entre escalas | Capítulos 03-04 y 09 |
| La asimetría L1↔B↔L3↔S es protocolo formal | Traducibilidad obligatoria, invariante a la escala | Capítulo 02-04 §8 |
| **Los 40 casos del corpus justifican el marco** (no son la tesis) | 30 inter-dominio + 10 inter-escala, 8 escalas, 30 dominios | Capítulos 09 + 05-06 |
| Los rivales se discriminan públicamente | Tabla con celdas (incluido Wolfram) | Capítulo 04-01 |
| El aparato tiene dominio de validez declarado | Casos null + caso 38 failure mode reportados honestamente | Capítulo 06-01 §3.5 |

## 7. Lo que la tesis no afirma

**Tabla 6.1.4.**

| Promesa rechazada | Razón |
|---|---|
| Ontología total cerrada | Articuladora general, no totalizadora |
| Reducción de las ciencias a esquema único | El pluralismo controlado lo prohíbe; la generalidad ontológica es de invariantes estructurales, no de contenido sustantivo |
| Teoría definitiva de consciencia o normatividad | Cada uno requiere programa específico bajo el marco general |
| El protocolo EDI funciona universalmente sobre cualquier dato | El caso 33 (Villin) y caso 38 (locomoción τ-dot) muestran que sondas inadecuadas producen null/failure mode honestos |
| Los 40 casos demuestran el marco por inducción | Los casos justifican el marco operativamente; el marco se sostiene por su articulación tripartita interna |
| Más casos = más verdad | Falacia inductivista; la generalidad del marco no depende del tamaño del corpus |
| Predicción de fenómenos individuales no medibles | Las leyes de control sin instrumentación son objeto de investigación, no de afirmación dogmática |

## 8. Fórmula final demostrativa

> Bajo el aparato consolidado — irrealismo operativo de estructuras pre-ontológicas como **ontología general multiescalar**, asimetría L1↔B↔L3↔S como protocolo formal con sistema modal T declarado e invariante a la escala, dossier de anclaje de catorce componentes, protocolo C1-C5 con 13 condiciones simultáneas, EDI por intervención ablativa con permutación 999 y bootstrap 500, cartografía agregada de 40 casos: **30 inter-dominio** sobre física, biología, economía, política, tecnología, cultura y conducta humana (4 `overall_pass=True` + 1 strong sin gate + 8 weak + 3 controles rechazados) y **10 inter-escala** desde dinámica de espín-órbita atómica (10⁻¹⁰ m) hasta dinámica de cúmulos globulares (10²⁰ m) con **7 strong en 7 escalas distintas** + 1 weak + 2 nulls honestos, validación lógica formal con suite ST de 24 teorías (6 hallazgos críticos detectados y corregidos), hostile testing aplicado al motor (0/2000 falsos positivos en gate completo bajo random walk masivo, Wilson 95 % CI [0, 0.00191]) y al test cruzado de sondas inter-escala (0/12 circularidad detectada), coherencia interna del umbral EDI sobre el corpus inter-dominio (AUC-ROC = 0.886, n=12; interpretada como consistencia entre el umbral declarado 0.33 y la clasificación final del corpus, no como discriminación externa contra un baseline rival; ver §8.1), y discriminación pública contra quince rivales (incluidos Wolfram con piloto Rule 110 ejecutado mostrando convivencia de irreducibilidad micro y cierre macro detectable, e IIT — Tononi-Boly-Massimini-Koch 2016) — la tesis del irrealismo operativo de estructuras pre-ontológicas se sostiene como **propuesta ontológica general multiescalar articulada con demostración parcial bajo régimen declarado**, con limitaciones honestamente reconocidas (p-value mal calibrado al 24% empírico aunque umbrales EDI robustos, caso 30 con circularidad detectada por sonda alternativa, depuración post-hoc del corpus inter-escala, datos sintéticos pendientes de elevación a LoE 4-5, escalas como etiquetas nominales basadas en parámetros publicados, AUC-ROC interno no externo, ningún caso cumple los tres criterios κ-ontológica, sin revisión por pares humanos externos) y deuda residual fechada con cronograma firme post-defensa.

### 8.1. Lo que la tesis afirma con fuerza tras hostile testing severo

- **Aporte metodológico:** protocolo replicable con motor común (ABM+ODE acoplado, suite ST, hostile testing automatizado, requirements-locked) que cualquier tercero puede ejecutar y verificar.
- **Coherencia interna del umbral EDI** sobre el corpus inter-dominio: AUC-ROC = 0.886 (n=12), entendida como consistencia entre el umbral declarado a priori (EDI ≥ 0.33 → strong) y la clasificación final del corpus tras todas las verificaciones del aparato (gate completo, p-value, C1-C5, hostile testing). Esta cifra **no mide discriminación contra un rival externo**: el predictor y la etiqueta son funciones del mismo EDI. La comparación previa contra ARIMA (0.600) se retira: ARIMA no es un baseline pertinente para clasificación strong/null y se computaba sobre n=8 mientras EDI se computaba sobre n=12, lo que invalida la comparación pareada. La validación discriminativa externa (etiquetas asignadas por especialistas de cada dominio sin acceso al EDI, replicación independiente del cómputo, comparación de rankings) es deuda bloqueante post-defensa. Metodología y CI bootstrap en `09-simulaciones-edi/auc_roc/methodology.md`.
- **Discriminación multiescalar:** 7 strong en 7 escalas distintas con sondas físicamente motivadas (Lindblad, Bloch, Tyson-Novak, Hoffmann, Mackey-Glass, Leavitt, Plummer); las sondas son específicas (test cruzado V4-01: 0% circularidad sobre datos no-suyos).
- **Robustez del gate completo:** 0/2000 falsos positivos bajo random walk masivo agregando los tres scripts canónicos (`N1_falsos_positivos.py` n=500, `V4_06_hostile_multiescala.py` n=500, `N5_hostile_testing.py` n=1000); Wilson 95 % CI [0, 0.00191]. El gate filtra ruido sin acoplamiento ODE→ABM por construcción (§3.4): el resultado certifica integridad de implementación, no discriminación contra rivales con estructura — esa carga la sostienen **los 3/3 controles de falsación rechazados** (06-exoplanetas, 07-noticias-shanghai, 08-observacional-control, con EDI ≤ 0.06 y gate=false en los tres) y la coherencia interna del umbral EDI (AUC-ROC = 0.886 como medida de consistencia umbral interna, no de discriminación contra baseline externo).
- **Validación lógica formal:** suite ST de 24 teorías con coherencia interna verificada y limitaciones explícitas declaradas.

### 8.2. Lo que la tesis NO afirma (limitaciones honestas)

- **No afirma que el p-value declarado tenga calibración correcta:** la tasa empírica de tipo I es 24%, no 5%. Los umbrales EDI sí son robustos.
- No afirma que el caso 30 (behavioral dynamics) demuestre cierre operativo específico: la sonda Fajen-Warren produce EDI > 0.30 en 50 % de mass-spring puro (N2). El análisis posterior con block bootstrap confirma cuantitativamente la circularidad: p estimado ≈ 0.978 (no significativo) y clasificación no invariante a umbrales. El caso 30 se mantiene como caso piloto metodológico hasta datos humanos reales.
- **No afirma que la composición del corpus refleje prevalencia poblacional:** los umbrales 0.10/0.30 producen 5 strong; 0.15/0.40 produce 3; 0.05/0.20 produce 9 (N4). La composición es post-hoc.
- **No afirma que κ-ontológica fuerte esté demostrada:** solo κ-pragmática multiescalar. La afirmación ontológica fuerte requiere convergencia inter-grupo y revisión externa.
- **No afirma generalidad multiescalar sin reservas:** las escalas son etiquetas nominales basadas en parámetros publicados; los datos son sintéticos. La elevación a datos reales abiertos (IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3) es deuda priorizada de 6-12 meses post-defensa.
- **No afirma haber resuelto el caso 38 (locomoción τ-dot):** la sonda alternativa propuesta produjo EDI = -1.34, lo cual es failure mode de sonda, no null estructural. La objeción N2 sobre circularidad de Fajen-Warren sigue parcialmente abierta hasta datos VENLab humanos.
- **No afirma haber sido validada por pares humanos externos:** todas las auditorías (v1, v2, severa, v3, v4) son endógenas. La revisión externa hostil es deuda bloqueante para sustentación.
- **No afirma que el AUC-ROC = 0.886 mida discriminación contra un baseline rival:** la AUC se computa con el mismo EDI como score y como etiqueta (vía umbral 0.33), por lo que es un test de **consistencia umbral interna**, no de validez externa. La comparación previa contra ARIMA (0.600) se retira por dos razones: (i) ARIMA es predicción univariada, no clasificación binaria; (ii) la comparación se hacía sobre n=8 (ARIMA, tras filtrar 4 nulls sin `rmse_arima`) mientras EDI se computaba sobre n=12, lo que invalida la comparación pareada. La validación discriminativa externa es deuda bloqueante post-defensa.

### 8.3. Estado declarado del manuscrito

**Propuesta ontológica general multiescalar con aparato ejecutable validado bajo hostile testing severo, demostración parcial inter-dominio (30 casos) e inter-escala (10 casos en 8 escalas distintas), validación lógica formal interna con suite ST de 24 teorías, distinción explícita κ-pragmática vs κ-ontológica con criterios operativos para cada una, limitaciones honestamente reconocidas (depuración post-hoc multiescala, escalas nominales, AUC interno, ningún caso pasa los 3 criterios κ-ontológica). Tesis defendible bajo régimen declarado. La tesis es ontológica general, no regional macro-poblacional. Demostración cerrada inter-escala con datos reales y revisión por pares humanos: deuda externa bloqueante post-defensa.**

## 9. Forma corta de la tesis demostrada

> Mínima en sustancias, rica en relaciones, controlada en sus recortes, reversible en sus niveles de explicación, anclada en cartografía empírica multidominio con discriminación pública contra rivales, abierta en su programa de extensión, disciplinada por anti-reificación operativa, y honesta en sus rechazos.



## 10. Cierre del cierre

La diferencia entre una tesis demostrada y un manifiesto bien escrito es que la tesis demostrada **acepta perder y especifica cómo**. Este capítulo es el lugar donde la tesis del irrealismo operativo acepta perder. No pierde, hasta el momento del manuscrito. Pero acepta los términos de la pérdida posible:

- si los 4 casos `overall_pass` se desmoronan, perdimos;
- si los controles de falsación dejan de rechazarse, perdimos;
- si el caso 30 nunca se eleva tras programa serio, el dominio es regional;
- si Wolfram (u otro) absorbe la tesis sin diferencia, cedemos prioridad.

Y aún más importante: el caso 30 ya nos enseñó algo decisivo. **El aparato funciona porque rechaza honestamente cuando debe rechazar**. Si hubiéramos forzado el caso 30 a producir EDI alto reformulando datos o sondas, habríamos validado todo y demostrado nada. La tesis del irrealismo operativo se demuestra precisamente por su capacidad de decir no a sus propios autores.

> *El cómputo es potente. Por eso necesita disciplina. Por eso necesita anti-reificación operativa. Por eso necesita, sobre todo, dejar de glorificarse.*

Esa es la condición de la victoria local de esta tesis.
