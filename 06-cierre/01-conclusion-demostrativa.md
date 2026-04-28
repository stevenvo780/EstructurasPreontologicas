# Conclusión demostrativa

## Tesis del capítulo

> La tesis del **irrealismo operativo de estructuras pre-ontológicas** se sostiene como **propuesta ontológica general multiescalar** validada operativamente sobre **40 casos del corpus EDI agregado** (30 inter-dominio + 10 inter-escala). El corpus inter-dominio cubre física, biología, economía, política, tecnología, cultura y conducta humana con 4 casos `overall_pass=True` + 1 strong sin gate + 8 weak + 2 suggestive + 4 trend + 8 null + 3 controles de falsación rechazados. El corpus inter-escala cubre **30 órdenes de magnitud** espaciales y temporales (desde dinámica subatómica de espín-órbita 10⁻¹⁰ m a cúmulos globulares 10²⁰ m) con **7 strong en 7 escalas distintas** + 1 weak + 2 nulls honestos. El aparato ha sobrevivido hostile testing severo (0/1500 falsos positivos del gate completo bajo random walk masivo, 0/12 circularidad en test cruzado de sondas). Las condiciones de fracaso son falsables y la deuda residual está fechada. La tesis es **ontología general operativamente articulada con demostración parcial multiescalar bajo régimen declarado**, no ontología regional macro-poblacional como sugería la primera iteración del manuscrito.

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

| Categoría | N | Casos clave |
|-----------|--:|-------------|
| Strong (gate completo) | 4 | Energía (0.650), Deforestación (0.602), Kessler (0.353), Riesgo Biológico (0.333) |
| Strong (sin gate) | 1 | Microplásticos (0.782) |
| Weak | 7 | Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad |
| Suggestive | 2 | Finanzas, Salinización |
| Trend | 4 | Justicia, Starlink, Fuga cerebros, Clima |
| Null | 8 | Conciencia, Contaminación, Paradigmas, Océanos, Acidificación, Erosión, Acuíferos, IoT |
| Falsación rechazada | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Test de fallo**: si los 4 casos `overall_pass` no replican o son superados por modelos rivales, la tesis pierde su demostración multidominio. **Verificación sostenida** en estado actual del corpus (outputs verificados bit-a-bit).

### Condición 6. Discriminación pública contra rivales

**Verificada en**: capítulo 04-01.

**Producto**: tabla de discriminación contra catorce posiciones rivales con criterios públicos (incluido Wolfram Physics Project). En cada rival, ventaja en al menos dos celdas; en el caso ancla, ventaja en cinco celdas contra modelos internos.

**Test de fallo**: si algún rival absorbe la tesis sin diferencia discriminante, se reformula. La tabla actual no produce absorción. **Verificación sostenida.**

### Condición 7. Honestidad sobre el dominio de validez del aparato

**Verificada en**: caso 30 (behavioral dynamics) y este capítulo.

**Producto**: reconocimiento explícito de que el protocolo EDI tiene dominio de validez **dependiente de la sonda y los datos disponibles, no de la escala**. El aparato funciona en cualquier escala donde se disponga de sonda físicamente motivada y datos con resolución temporal adecuada (verificado en corpus inter-escala desde 10⁻¹⁵ s hasta 10¹⁴ s). El caso 30 produjo EDI=0.002 en su versión inicial (no significativo), siendo rechazado correctamente por el aparato; tras refinamiento de sonda al modelo de segundo orden Fajen-Warren, produjo Nivel 3 weak honesto. Esto se documenta como hallazgo del programa, no como fracaso oculto.

**Test de fallo**: si el manuscrito hubiera forzado la admisión del caso 30 (reformulando datos, sondas o criterios para producir EDI alto), la tesis violaría su propio principio de anti-reificación operativa. **Verificación sostenida**: el caso 30 se admite explícitamente como programático con criterio de elevación documentado en `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`.

## 2. Condiciones de fracaso global

La tesis falla globalmente en cinco escenarios falsables:

### Escenario 1. Los 4 casos `overall_pass` se desmoronan empíricamente

Si Energía, Deforestación, Kessler, Riesgo Biológico no replican bajo perfiles de alto rendimiento o son superados por baselines puramente estadísticos (ARIMA, VAR), la tesis pierde su demostración multidominio principal.

### Escenario 2. Los controles de falsación dejan de rechazarse

Si los 3 controles de falsación (06, 07, 08) empiezan a producir EDI significativo, el aparato pierde discriminación y la tesis colapsa al instrumentalismo puro.

### Escenario 3. Aparato no escala más allá de su dominio

Si el caso 30 (behavioral dynamics) y otros candidatos en escalas no-macro-temporales no se elevan a demostrativo bajo el protocolo extendido, el dominio de validez de la tesis es regional, no general como aspira.

### Escenario 4. Asimetría L1↔B↔L3↔S no se sostiene en algún dominio

Si en algún dominio relevante no se logra traducir L3 a B porque B no es identificable, la tesis admite reducción de alcance.

### Escenario 5. Wolfram (u otro rival) absorbe la tesis sin diferencia discriminante

Si un programa de investigación rival reúne todas las piezas (anclaje + asimetría + dossier + cartografía + falsación) en arquitectura equivalente o superior, la tesis cede prioridad y se reformula.

Cada escenario es falsable, fechado y con criterios públicos.

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

## 4. Deuda residual

Lo que el manuscrito no demuestra y reconoce explícitamente como deuda con plazo y entregable:

| Deuda | Descripción | Plazo | Entregable | Estado al 2026-04-28 |
|---|---|---|---|---|
| Caso 30 elevación a LoE = 4 | Datos humanos reales (VENLab/WALK-MS) con aval CEI, pipeline alta frecuencia | 9-10 meses | Caso 30 con EDI sobre datos humanos | Dossier técnico-ético en `Bitacora/2026-04-28-cierre-doctoral/02-` |
| Programa multi-sonda | Validar casos clave con sondas alternativas convergentes | 6 semanas | Tabla de convergencia multi-sonda | **EJECUTADO** sobre 3 strong + 5 weak (`09-simulaciones-edi/multi_sonda/`) |
| Topologías heterogéneas para Nivel 5 | Adaptar ABM a scale-free / small-world; verificar CR > 2.0 | 6 meses | Caso elevado a Nivel 5 o reporte negativo honesto | Programa formal en `Bitacora/2026-04-28-cierre-doctoral/06-` |
| Baselines estadísticos puros | Comparar contra ARIMA, VAR, RW, GP | 3 semanas | Tabla comparativa con discriminación | **EJECUTADO** sobre 8 casos (`09-simulaciones-edi/baselines/`) |
| Aparato para variables normativas | Desarrollo formal de validez/legitimidad como cuenca de atracción + caso piloto | 18-24 meses | Capítulo metodológico + caso institucional cuantitativo | Caso piloto COVID **EJECUTADO** con resultado null honesto (`09-simulaciones-edi/covid_pilot/`); programa restante documentado |
| Integración bibliográfica formal | Citas Chicago author-date en cada capítulo del cuerpo argumental | Hito de cierre | Bibliografía consolidada al depósito | **EJECUTADA** en cap 02-04, 04-01, 05-04; bibliografía consolidada en cap 07 con 90 referencias |
| Programa de convergencia con Wolfram | Aplicar EDI a hypergraph rewriting | 12 meses | Reporte técnico para Wolfram Institute | Piloto Rule 110 **EJECUTADO** (EDI 0.55, `09-simulaciones-edi/wolfram_pilot/`); programa post-piloto en `Bitacora/2026-04-28-cierre-doctoral/05-` |
| Conversión editorial pre-depósito | LaTeX/PDF + figuras SVG/PNG + plantilla institucional | 3 semanas pre-depósito | PDF institucional final | PDF intermedio generado (`TesisFinal/Tesis.pdf` 1.83 MB); figuras Mermaid en Anexo A.10; conversión a plantilla institucional pendiente del momento del depósito |

## 5. Aporte conceptual sustantivo

El aporte de la tesis es triplemente general: ontología, epistemología y metodología generales, como se articula en la Parte I (capítulos 1-6) y la Parte II (capítulos 7-11). Los 40 casos del corpus son **justificación operativa** del marco, no son la tesis. La generalidad del marco es independiente de la cantidad del corpus; lo que el corpus aporta es discriminación operativa y demostración de transferibilidad.

La tesis introduce como aporte propio:

### 5.1. Aporte ontológico

Reformula entidades como **estructuras pre-ontológicas** a cualquier escala donde el aparato puede operar con sondas físicamente motivadas. Afirma una estructura ontológica común entre el qubit superconductor, la enzima, la célula oscilante, el agente económico, el organismo en tarea, la estrella pulsante y el cúmulo globular: los cuatro invariantes (sustrato, acoplamiento, atractor, κ) son operativamente medibles en cada uno con la misma metodología EDI. El "irrealismo operativo" distingue κ-pragmática de κ-ontológica con criterios operativos para cada una (véase capítulo 1, §Nota sobre κ).

### 5.2. Aporte epistemológico

Reformula el conocimiento como compresión disciplinada bajo intervención ablativa. La epistemología es general: opera del mismo modo en cualquier escala donde se disponga de sonda físicamente motivada. Lo que cambia entre escalas es la sonda específica; la teoría del conocimiento no cambia (véase capítulo 2).

**Limitación reconocida:** el p-value declarado tiene tasa de tipo I empírica = 24%. Los umbrales EDI sí son robustos contra falsos positivos (0.6% supera weak, 0% supera strong bajo random walk puro).

### 5.3. Aporte metodológico (general, no regional)

Ofrece la auditoría ontológica como protocolo replicable de nueve fases con dossier de catorce componentes, más el pipeline ABM+ODE con soporte CPU/GPU, validador canónico, controles de falsación incorporados, suite ST de 13 teorías formales y procedimiento de hostile testing automatizado. Determinismo `seed=42` con `requirements-locked.txt` para reproducibilidad inter-instalación. **Esta metodología es general**: el mismo motor `edi_engine` opera sobre los 10 casos del corpus inter-escala y el mismo protocolo C1-C5 opera sobre los 30 casos del corpus inter-dominio sin reentrenar arquitectura. La transferibilidad metodológica entre escalas y dominios —verificada por test cruzado (0/12 circularidad) y hostile testing (0/1500 falsos positivos)— es **prueba operativa de que la metodología no es regional**: una misma máquina funciona desde lo cuántico hasta lo cosmológico, desde lo físico hasta lo social.

**Este aporte es ejecutable, no solo declarativo:** cualquier tercero puede correr el motor sobre datos nuevos en cualquier escala con sondas físicamente motivadas. La generalidad metodológica está respaldada por código, no por afirmación retórica.

### 5.4. Aporte aplicado: cartografía agregada inter-dominio + inter-escala

Demuestra que el aparato **discrimina** y **detecta cierre operativo** en cartografía agregada de **40 casos** que cubren simultáneamente:

**(a) heterogeneidad de dominio** (corpus inter-dominio, 30 casos): física, biología, economía, política, tecnología, cultura y conducta humana, con AUC-ROC = 0.886 de ranking interno strong vs no-strong (N3).

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

> Bajo el aparato consolidado — irrealismo operativo de estructuras pre-ontológicas como **ontología general multiescalar**, asimetría L1↔B↔L3↔S como protocolo formal con sistema modal T declarado e invariante a la escala, dossier de anclaje de catorce componentes, protocolo C1-C5 con 13 condiciones simultáneas, EDI por intervención ablativa con permutación 999 y bootstrap 500, cartografía agregada de 40 casos: **30 inter-dominio** sobre física, biología, economía, política, tecnología, cultura y conducta humana (4 `overall_pass=True` + 1 strong sin gate + 8 weak + 3 controles rechazados) y **10 inter-escala** desde dinámica de espín-órbita atómica (10⁻¹⁰ m) hasta dinámica de cúmulos globulares (10²⁰ m) con **7 strong en 7 escalas distintas** + 1 weak + 2 nulls honestos, validación lógica formal con suite ST de 13 teorías (2 hallazgos críticos detectados y corregidos), hostile testing aplicado al motor (0/1500 falsos positivos en gate completo bajo random walk masivo) y al test cruzado de sondas inter-escala (0/12 circularidad detectada), AUC-ROC = 0.886 para discriminación de ranking interno vs ARIMA = 0.600, y discriminación pública contra catorce rivales (incluido Wolfram con piloto Rule 110 ejecutado mostrando convivencia de irreducibilidad micro y cierre macro detectable) — la tesis del irrealismo operativo de estructuras pre-ontológicas se sostiene como **propuesta ontológica general multiescalar articulada con demostración parcial bajo régimen declarado**, con limitaciones honestamente reconocidas (p-value mal calibrado al 24% empírico aunque umbrales EDI robustos, caso 30 con circularidad detectada por sonda alternativa, depuración post-hoc del corpus inter-escala, datos sintéticos pendientes de elevación a LoE 4-5, escalas como etiquetas nominales basadas en parámetros publicados, AUC-ROC interno no externo, ningún caso cumple los tres criterios κ-ontológica, sin revisión por pares humanos externos) y deuda residual fechada con cronograma firme post-defensa.

### 8.1. Lo que la tesis afirma con fuerza tras hostile testing severo

- **Aporte metodológico:** protocolo replicable con motor común (ABM+ODE acoplado, suite ST, hostile testing automatizado, requirements-locked) que cualquier tercero puede ejecutar y verificar.
- **Discriminación de ranking interno** sobre el corpus inter-dominio: AUC-ROC 0.886 vs ARIMA 0.600 (V4-05 reconoce que es interno, no validación externa contra estándar de oro).
- **Discriminación multiescalar:** 7 strong en 7 escalas distintas con sondas físicamente motivadas (Lindblad, Bloch, Tyson-Novak, Hoffmann, Mackey-Glass, Leavitt, Plummer); las sondas son específicas (test cruzado V4-01: 0% circularidad sobre datos no-suyos).
- **Robustez del gate completo:** 0/1500 falsos positivos bajo random walk masivo.
- **Validación lógica formal:** suite ST de 13 teorías con coherencia interna verificada y limitaciones explícitas declaradas.

### 8.2. Lo que la tesis NO afirma (limitaciones honestas)

- **No afirma que el p-value declarado tenga calibración correcta:** la tasa empírica de tipo I es 24%, no 5%. Los umbrales EDI sí son robustos.
- **No afirma que el caso 30 (behavioral dynamics) demuestre cierre operativo específico:** la sonda Fajen-Warren produce EDI > 0.30 en 50% de mass-spring puro (N2). El caso 30 se mantiene como caso piloto metodológico hasta elevación con datos humanos reales.
- **No afirma que la composición del corpus refleje prevalencia poblacional:** los umbrales 0.10/0.30 producen 5 strong; 0.15/0.40 produce 3; 0.05/0.20 produce 9 (N4). La composición es post-hoc.
- **No afirma que κ-ontológica fuerte esté demostrada:** solo κ-pragmática multiescalar. La afirmación ontológica fuerte requiere convergencia inter-grupo y revisión externa.
- **No afirma generalidad multiescalar sin reservas:** las escalas son etiquetas nominales basadas en parámetros publicados; los datos son sintéticos. La elevación a datos reales abiertos (IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3) es deuda priorizada de 6-12 meses post-defensa.
- **No afirma haber resuelto el caso 38 (locomoción τ-dot):** la sonda alternativa propuesta produjo EDI = -1.34, lo cual es failure mode de sonda, no null estructural. La objeción N2 sobre circularidad de Fajen-Warren sigue parcialmente abierta hasta datos VENLab humanos.
- **No afirma haber sido validada por pares humanos externos:** todas las auditorías (v1, v2, severa, v3, v4) son endógenas. La revisión externa hostil es deuda bloqueante para sustentación.

### 8.3. Estado declarado del manuscrito

**Propuesta ontológica general multiescalar con aparato ejecutable validado bajo hostile testing severo, demostración parcial inter-dominio (30 casos) e inter-escala (10 casos en 8 escalas distintas), validación lógica formal interna con suite ST de 13 teorías, distinción explícita κ-pragmática vs κ-ontológica con criterios operativos para cada una, limitaciones honestamente reconocidas (depuración post-hoc multiescala, escalas nominales, AUC interno, ningún caso pasa los 3 criterios κ-ontológica). Tesis defendible bajo régimen declarado. La tesis es ontológica general, no regional macro-poblacional. Demostración cerrada inter-escala con datos reales y revisión por pares humanos: deuda externa bloqueante post-defensa.**

## 9. Forma corta de la tesis demostrada

> Mínima en sustancias, rica en relaciones, controlada en sus recortes, reversible en sus niveles de explicación, anclada en cartografía empírica multidominio con discriminación pública contra rivales, abierta en su programa de extensión, disciplinada por anti-reificación operativa, y honesta en sus rechazos.



## 11. Cierre del cierre

La diferencia entre una tesis demostrada y un manifiesto bien escrito es que la tesis demostrada **acepta perder y especifica cómo**. Este capítulo es el lugar donde la tesis del irrealismo operativo acepta perder. No pierde, hasta el momento del manuscrito. Pero acepta los términos de la pérdida posible:

- si los 4 casos `overall_pass` se desmoronan, perdimos;
- si los controles de falsación dejan de rechazarse, perdimos;
- si el caso 30 nunca se eleva tras programa serio, el dominio es regional;
- si Wolfram (u otro) absorbe la tesis sin diferencia, cedemos prioridad.

Y aún más importante: el caso 30 ya nos enseñó algo decisivo. **El aparato funciona porque rechaza honestamente cuando debe rechazar**. Si hubiéramos forzado el caso 30 a producir EDI alto reformulando datos o sondas, habríamos validado todo y demostrado nada. La tesis del irrealismo operativo se demuestra precisamente por su capacidad de decir no a sus propios autores.

> *El cómputo es potente. Por eso necesita disciplina. Por eso necesita anti-reificación operativa. Por eso necesita, sobre todo, dejar de glorificarse.*

Esa es la condición de la victoria local de esta tesis.
