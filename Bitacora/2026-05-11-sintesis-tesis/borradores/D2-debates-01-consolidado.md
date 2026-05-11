---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
reemplazaria: 04-debates/01-debates-con-posiciones-rivales.md
ahorro_lineas_estimado: ~245 (de 491 a ~246)
arquitectura: 01 sintético (discusión por rival con valor argumentativo único) + 03 canónico (tabla síntesis) + _extendido/ (desarrollos extensos por rival con cita primaria)
migra_a_extendido:
  - 04-debates/_extendido/rival-modelos-internos.md
  - 04-debates/_extendido/rival-enactivismo-radical.md
  - 04-debates/_extendido/rival-wolfram-physics-project.md
  - 04-debates/_extendido/rival-mecanicismo-multinivel.md
  - 04-debates/_extendido/rival-cognitivismo-computacional.md
  - 04-debates/_extendido/rival-conductismo-radical.md
  - 04-debates/_extendido/rival-realismo-estructural-informativo.md
relacion_con_03: complementaria, no duplicada. 03 mantiene la tabla síntesis 14×6 + filas A-F + ficha breve por rival. 01 mantiene la confrontación discursiva donde la tesis acepta-rechaza-discrimina con voz argumentativa.
NO_pierde:
  - citas paginadas a Hutto-Myin 2013/2017, Wolfram 2002/2020/2021, Bechtel 2008, Craver 2007, Chemero 2009.
  - el esquema de convergencia EDI ↔ Wolfram (cap 04-01 §14 actual) — se preserva íntegro en _extendido/rival-wolfram.md, referenciado desde 01 §Wolfram.
  - la tabla síntesis final 14 rivales × criterios discriminantes (queda en 03, no en 01).
ELIMINA:
  - 14 micro-tablas tesis/rival (Tabla 4.1.1 a 4.1.14) → ya están en 03 §1 (matriz síntesis).
  - tabla 4.1.15 (síntesis final) → duplica 03 §Tabla 4.3.2.
  - reiteración del "compromiso público" (§17) → 03 ya lo declara en §"Compromiso público".
  - §1 criterios A-F → 03 §"Criterios de discriminación" es canónico (criterio C.4 del reporte 01-redundancia).
---

# Debates con posiciones rivales

## Tesis del capítulo

> La tesis se discrimina de catorce rivales filosófica y empíricamente identificables en al menos dos criterios cada uno. La novedad no es de inventario sino de articulación: **dossier de anclaje + asimetría L1↔B↔L3↔S + cartografía multidominio bajo EDI con controles de falsación rechazados**. Este capítulo confronta cada rival discursivamente; la matriz síntesis 14×6 (criterios A-F) y la ficha breve por rival están en `04-debates/03-tabla-comparativa-rivales.md`. Los desarrollos extensos con citas primarias paginadas viven en `04-debates/_extendido/rival-<X>.md` y se cargan bajo demanda desde la capa web.

## 1. Marco general de la confrontación

Cada rival se evalúa contra la tesis bajo los criterios **A** (anclaje material sin reducción a partículas), **B** (multiescalaridad operativa), **C** (admisión empírica vía dossier de catorce componentes), **D** (traducibilidad asimétrica L1↔B↔L3↔S), **E** (ventaja predictiva discriminante en el caso ancla canónico) y **F** (alcance generalizable). Las definiciones completas y la tabla síntesis 14×6 están en `04-debates/03-tabla-comparativa-rivales.md` §"Criterios de discriminación" y §"Tabla síntesis". Este capítulo asume esa matriz como dado y desarrolla la confrontación discursiva donde la prosa tiene valor argumentativo que la tabla no captura.

## 2. Rivales con discriminación tabular suficiente

Los siguientes ocho rivales se discriminan adecuadamente en la matriz de `04-debates/03` y no requieren desarrollo discursivo adicional aquí. El lector encontrará en `03 §"Confrontación detallada por rival"` la ficha breve (forma fuerte / qué recoge la tesis / qué rechaza / criterios de discriminación) que basta para fijar la posición.

- **Dualismo** (`03 §1`). Discrimina en A, B, F.
- **Materialismo de partículas** (`03 §2`). Discrimina en B, C, E.
- **Reduccionismo plano** (`03 §3`). Discrimina en B, C, F.
- **Emergentismo fuerte** (`03 §4`). Discrimina en A, C, D.
- **Constructivismo arbitrario** (`03 §5`). Discrimina en C, E.
- **Instrumentalismo puro** (`03 §6`). Discrimina en A, C.
- **Formalismo vacío** (`03 §7`). Discrimina en D, E.
- **Realismo estructural informativo** (`03 §12`). Discrimina en A, C, D. Recordatorio del glosario operativo (`00-proyecto/07-glosario-operativo.md`): "realismo estructural moderado" se usa en sentido **operativo no-Ladyman**; la diferencia con Ladyman-Ross está fijada en `03 §12`.

Donde el lector requiera mayor desarrollo, cada rival anterior cuenta con material extendido cuando exista cita primaria que justifique elaboración: véase listado al pie.

## 3. Rivales con discriminación que requiere prosa argumentativa

Los siguientes seis rivales mantienen desarrollo discursivo en este capítulo porque la matriz tabular no captura el matiz argumentativo o la concesión honesta que la tesis hace.

### 3.1. Modelos internos / control óptimo

El rival representa la posición canónica en behavioral dynamics y control motor (Wolpert et al.; Todorov y Jordan; control engineering aplicado a postura). Sostiene que la conducta adaptativa se explica como solución de un problema de optimización sobre representaciones internas, y que la fidelidad de las representaciones explica la efectividad.

La tesis **recoge** la existencia de procesos internos relevantes para conducta secuencial, anticipatoria, predictiva y estratégica donde la información ocurrente no basta. **No es eliminativista** respecto a estados internos.

La tesis **rechaza** el uso de modelos internos como recurso primario en locomoción, frenado, equilibrio y raqueteo, donde el control directo informacional explica los datos con menos hipótesis y mejor predicción. El caso ancla canónico (`05-aplicaciones/05-...`) muestra cinco discriminaciones operativas concretas: reproducción de Fajen-Warren con r²=0.980 frente a parámetros adicionales no derivados, predicción de degradación al retirar visión en línea, predicción exacta de τ̇=−0.5 en frenado (r²=0.98 Yilmaz-Warren 1995), bifurcación de ruta predicha y observada, y economía paramétrica (4 parámetros vs modelo interno completo). Detalle por celda en `04-debates/_extendido/rival-modelos-internos.md`.

**Restricción honesta:** los modelos internos siguen siendo candidatos legítimos para conducta secuencial, anticipatoria y estratégica que el caso ancla declara fuera de su régimen de validez (`05-aplicaciones/05-...` §casos de presión). La tesis no rechaza modelos internos en abstracto; rechaza su uso como recurso primario donde el control informacional discrimina mejor. Esta es la concesión nuclear: el rival no se elimina, se acota.

### 3.2. Cognitivismo computacional

La tesis **recoge** la existencia de procesos cognitivos no reducibles a respuestas inmediatas a estímulos. **Rechaza** la metáfora computacional como recurso primario donde el acoplamiento dinámico explica los datos sin ella, y rechaza la abstracción del nivel simbólico desligado del nivel B.

La concesión que la matriz no captura: en el caso ancla, cognitivismo computacional pierde en cinco celdas concretas frente al control informacional acoplado. Pero **en mente como dominio programático, la confrontación queda abierta**: la tesis aún no tiene caso demostrativo equivalente para fenómenos cognitivos superiores. Ahí cognitivismo computacional y tesis empatan en modo programático, y la decisión queda para investigación posterior. Esta concesión asimétrica (discriminación en caso ancla, empate en cognición superior) requiere prosa porque ninguna celda tabular puede expresar "discrimina aquí, no discrimina allá, y eso es honestidad estructural del alcance de la tesis".

Desarrollo con citas primarias en `04-debates/_extendido/rival-cognitivismo-computacional.md`.

### 3.3. Conductismo radical

La tesis **recoge** el recorte correcto del plano observable y la negativa a postular entidades internas no controladas. **Rechaza** la negación de la estructura formal L3 que efectivamente discrimina hipótesis: la tesis añade L3 anclado sin perder anclaje en B.

**Restricción honesta:** el conductismo radical es primo empobrecido del marco propuesto. La tesis se entiende, en este aspecto, como conductismo enriquecido con dinámica y *self-organization* en el sentido técnico anclado en `02-fundamentos/04-anclaje-conductual-ecologico.md` §4 (Maturana y Varela 1980; Haken 1977). Este reconocimiento no es decorativo: marca que la diferencia con conductismo radical es **aditiva** (L3 + dinámica), no **sustractiva**. Lo que el conductismo rechaza (entidades internas no controladas), la tesis también lo rechaza; lo que añade (formalismo L3 acoplado a B), el conductismo lo prohibía como metafísica. La diferencia es de alcance metodológico, no de orientación ontológica.

### 3.4. Enactivismo radical

Hutto y Myin (2013, *Radicalizing Enactivism*, cap. 1, p. 8) sostienen la **REC thesis (Radical Enactive Cognition)**: la cognición básica está constituida por patrones espaciotemporales de interacción dinámica entre organismo y entorno, y no involucra intrínsecamente contenido. Hutto y Myin (2017, *Evolving Enactivism*, cap. 5) extienden el argumento contra cualquier predictive coding que asuma contenido representacional inferencial.

La tesis **recoge** mucho: acoplamiento dinámico (`02-fundamentos/04-...`), dependencia ecológica, centralidad de la tarea, rechazo de la representación interna como recurso primario en niveles básicos. La afirmación de Hutto-Myin (2013, p. 81) de que no hace falta postular intermediarios con contenido entre organismo y entorno para la percepción básica es congruente con la operacionalización del nivel B vía variables informacionales materialmente realizadas (τ, ρ, flujo óptico).

La tesis **rechaza** tres divergencias específicas:

1. **Grado de eliminación.** Hutto-Myin extienden la zero-content thesis a niveles básicos pero conceden contenido en niveles avanzados. La tesis es más cautelosa: admite estados internos como hipótesis cuando la pregunta lo exige (conducta anticipatoria, secuencial, estratégica), pero solo si el dossier de anclaje (`03-formalizacion/02-...`) los justifica empíricamente.
2. **Formalización L3.** La tesis exige aparato formal (μ, G, H, κ, ε) y validación cuantitativa (EDI). El enactivismo radical mantiene la formulación cualitativa. La objeción de Chemero (2009, *Radical Embodied Cognitive Science*, cap. 4) sobre la dificultad de cuantificar dinámica sin recaer en cognitivismo es real, pero el caso 30 del corpus EDI (EDI = 0.262 significativo) muestra que la cuantificación es posible sin volver al cognitivismo.
3. **Alcance multidominio.** El enactivismo radical se concentra en cognición situada; la tesis cubre 30 dominios heterogéneos. La generalización exige aparato formal compartido.

**Reconocimiento:** es el rival con quien la tesis comparte más. La diferencia es de articulación formal y de extensión de dominio, no de orientación filosófica. Esta cercanía es información sustantiva del posicionamiento de la tesis y por eso no se confina a una celda. Citas paginadas extendidas en `04-debates/_extendido/rival-enactivismo-radical.md`.

### 3.5. Wolfram Physics Project (caso especial)

Wolfram (2002, *A New Kind of Science*, cap. 12, p. 737) introduce la tesis de la **irreducibilidad computacional**. En el Wolfram Physics Project (2020, *A Project to Find the Fundamental Theory of Physics*, secciones 1-3) extiende la propuesta al sustrato físico: la realidad fundamental es *hypergraph rewriting*. La conjetura del **Ruliad** (Wolfram 2021, *The Concept of the Ruliad*, sec. 2) sostiene que toda la física observable emerge de la totalidad de reglas computacionales posibles, accedida desde un observador particular.

La tesis **recoge**: centralidad de los hipergrafos como instrumento formal (`03-formalizacion/01-...`), rechazo de la lista plana de partículas, importancia de la multiescalaridad sin emergentismo fuerte, espíritu de exploración computacional sistemática.

La tesis **rechaza** cuatro divergencias precisas:

1. **Ambición ontológica:** Wolfram busca ontología fundamental (la física *es* hypergraph rewriting). La tesis es ontología y epistemología generales integradoras, no fundacionales. No reduce todo a hipergrafos; articula registros heterogéneos bajo dossier de admisión.
2. **Procedimiento de admisión empírica:** Wolfram propone reglas computacionales pero no especifica filtro empírico de admisión para constructos macro. La tesis exige dossier de catorce componentes + protocolo C1-C5 + EDI con prueba de permutación + controles de falsación rechazados.
3. **Asimetría L1↔B↔L3↔S:** Wolfram opera en un solo registro (sustrato computacional). La tesis distingue cuatro registros con vínculos asimétricos y prohíbe la sustitución nominal.
4. **Cartografía empírica multidominio:** Wolfram propone simulaciones internas pero no validación discriminante sobre datos reales en dominios heterogéneos con controles de falsación. La tesis valida 30 casos en física, biología, economía, política, tecnología, cultura y conducta humana, con 3 controles de falsación correctamente rechazados.

**Reconocimiento de fortalezas:** el Wolfram Physics Project tiene mayor profundidad técnica en hypergraph rewriting, exploración computacional masiva con visualizaciones avanzadas, conjeturas con potencial unificador en física fundamental, y comunidad investigadora activa. La tesis es **complementaria, no rival sustituta**. El esquema de **convergencia productiva** (aplicar EDI a fenómenos derivados de hypergraph rewriting, con piloto Rule 110 ya ejecutado en `09-simulaciones-edi/wolfram_pilot/` reportando EDI=0.55 sobre dos sondas independientes) se conserva íntegramente en `04-debates/_extendido/rival-wolfram-physics-project.md` con sus seis pasos y la condición de discriminación (cierre operativo confirma puente; ausencia de cierre fortalece la tesis de irreducibilidad de Wolfram en el régimen específico). La frase eslogan "Wolfram fundamenta; la tesis disciplina" se conserva como síntesis pero no como respuesta a la pregunta filosófica nuclear, que sigue siendo: ¿qué constructos macro de hypergraph rewriting admiten dossier completo? Deuda residual H-J*: declarar complementariedad asimétrica modal (cf. `Bitacora/2026-05-11-sintesis-tesis/02-triage-bitacora-huerfana.md` F04-06).

### 3.6. Mecanicismo multinivel (Bechtel-Craver)

Bechtel (2008, *Mental Mechanisms*, cap. 1, p. 13) define mecanismo como estructura que realiza una función en virtud de sus partes componentes, sus operaciones y su organización. Craver (2007, *Explaining the Brain*, cap. 4, p. 152) elabora la tesis de la integración multinivel: los niveles son ontológicamente reales si y solo si las relaciones constitutivas entre ellos son *mutually manipulable*. Bechtel y Richardson (1993, *Discovering Complexity*, cap. 2) sistematizan la heurística de descomposición y localización.

La tesis **recoge casi todo**: es el aliado más fuerte en la articulación multinivel y en el realismo de mecanismos. La definición bechteliana de mecanismo coincide con la noción de **patrón materialmente sostenido con organización específica** del cap `02-fundamentos/01-...`. El criterio de *mutual manipulability* de Craver coincide con el criterio empírico de cierre operativo κ vía intervención ablativa.

La tesis **añade** tres aportes específicos al programa mecanicista:

1. **Filtro de admisión cuantitativo.** Bechtel-Craver aceptan que los niveles son legítimos cuando las relaciones constitutivas son mutuamente manipulables, pero no especifican una métrica única para decidir el grado de manipulabilidad. La tesis ofrece la métrica EDI con permutación + bootstrap + protocolo C1-C5 como instrumento operativo.
2. **Procedimiento empírico de κ vía baja dimensionalidad.** El mecanicismo deja la legitimidad de niveles relativamente abierta; la tesis la cierra con criterios verificables (`03-formalizacion/04-...`).
3. **Cartografía multidominio.** Bechtel-Craver trabajan principalmente en neurobiología y ciencias biomédicas; la tesis extiende la lógica a 30 dominios heterogéneos con controles de falsación rechazados.

La objeción específica de Glennan (2017, *The New Mechanical Philosophy*) sobre si la dinámica acoplada continua admite descripción mecanicista discreta queda como punto de presión legítimo y se trata en `04-debates/05-limitaciones-declaradas-consolidacion.md` §3 (deuda L11 sobre κ-ontológica; cf. nota de migración D.3 sobre el destino de los riesgos heredados previamente alojados en `04-debates/02`).

**Reconocimiento:** el mecanicismo multinivel es el aliado teórico principal de este capítulo. La tesis se entiende mejor como **mecanicismo multinivel disciplinado por dossier de anclaje y asimetría L1↔B↔L3↔S**. Citas extendidas en `04-debates/_extendido/rival-mecanicismo-multinivel.md`.

## 4. Lectura cruzada

- Tabla síntesis 14×6 + ficha breve por rival: `04-debates/03-tabla-comparativa-rivales.md`.
- Anticipación de objeciones filosóficas (F1-F10, distinto de discriminación rival): `04-debates/04-anticipacion-objeciones-filosoficas.md`.
- Limitaciones declaradas con plazos y entregables: `04-debates/05-limitaciones-declaradas-consolidacion.md`.
- Caso ancla canónico (donde se opera la discriminación contra modelos internos): `05-aplicaciones/05-...`.
- Convergencia con Wolfram (programa futuro): `Bitacora/2026-04-28-cierre-doctoral/05-programa-convergencia-wolfram.md` y `06-cierre/01-conclusion-demostrativa.md`.

## 5. Cierre

La tesis ocupa un punto difícil pero filosóficamente fértil: austera como el materialismo, sin ser de partículas; sensible a la organización como el emergentismo, sin postular sustancias; cuidadosa con las mediaciones como el constructivismo, sin caer en arbitrariedad; rigurosa en su modelización como el formalismo, sin ser vacía; empíricamente comprometida como el *behavioral dynamics*, con extensión filosófica general; mecanicista multinivel disciplinada por filtros de admisión que el mecanicismo deja abiertos.

> La realidad no exige más sustancias, pero sí mejores recortes, dossier completo y predicción discriminante.

El compromiso público de discriminación (que la tesis muestre ventaja en al menos dos celdas contra cada rival, bajo pena de admitir absorción y reformularse) está fijado y declarado en `04-debates/03-tabla-comparativa-rivales.md` §"Compromiso público". Este capítulo no lo duplica.

---

## Anexo: archivos `_extendido/` que se crearían

Boceto de contenido por archivo (una línea por rival). Cada archivo lleva frontmatter `extends: 04-debates/01-debates-con-posiciones-rivales.md`.

- `04-debates/_extendido/rival-modelos-internos.md` — desarrollo celda-por-celda de las cinco discriminaciones en el caso ancla (Fajen-Warren r²=0.980, degradación al retirar visión con cita pendiente a Wallis et al. 2002 y Hildreth et al. 2000, τ̇=−0.5 en frenado, bifurcación de ruta, economía paramétrica); restricción honesta sobre el régimen donde modelos internos siguen siendo candidatos.
- `04-debates/_extendido/rival-cognitivismo-computacional.md` — citas primarias a Fodor, Pylyshyn, Putnam sobre realización múltiple; análisis de por qué en cognición superior cognitivismo y tesis empatan en modo programático; lista de fenómenos cognitivos donde la tesis aún no tiene caso demostrativo.
- `04-debates/_extendido/rival-conductismo-radical.md` — desarrollo Skinner (1953, 1974) versus la versión enriquecida con L3 + Maturana-Varela 1980 + Haken 1977; análisis de la concesión "primo empobrecido"; relación con Chomsky 1959 review de Skinner.
- `04-debates/_extendido/rival-enactivismo-radical.md` — citas paginadas a Hutto y Myin 2013 (cap. 1, p. 8; cap. 4, p. 81), 2017 (cap. 5); Chemero 2009 cap. 4 sobre cuantificación; Thompson 2007 *Mind in Life*; análisis del caso 30 EDI=0.262 como evidencia de que la cuantificación no requiere recaer en cognitivismo.
- `04-debates/_extendido/rival-realismo-estructural-informativo.md` — Ladyman y Ross 2007 *Every Thing Must Go*, cap. 2-3; distinción operativa con el "realismo estructural moderado" del glosario; razón por la que la tesis no flota la estructura sin sustrato; relación con Worrall 1989.
- `04-debates/_extendido/rival-mecanicismo-multinivel.md` — Bechtel 2008 cap. 1 p. 13; Craver 2007 cap. 4 p. 152; Bechtel y Richardson 1993 cap. 2; Glennan 2017 objeción sobre dinámica continua; análisis de por qué la tesis se posiciona como mecanicismo multinivel disciplinado.
- `04-debates/_extendido/rival-wolfram-physics-project.md` — Wolfram 2002 cap. 12 p. 737 (irreducibilidad computacional); Wolfram Physics Project 2020 secs. 1-3; Wolfram 2021 *The Concept of the Ruliad* sec. 2; piloto Rule 110 (`09-simulaciones-edi/wolfram_pilot/`) con EDI=0.55 sobre dos sondas; programa de convergencia con seis pasos operativos para aplicar EDI a hypergraph rewriting; tratamiento de la asimetría modal Ruliad↔dossier (deuda F04-06).

**Nota de gobernanza `_extendido/`:** la convención (`00-proyecto/_extendido/README.md`) prohíbe alojar contenido único de un argumento en `_extendido/`. Cada uno de los siete archivos anteriores aloja **elaboración** (citas paginadas, desarrollo celda-por-celda, derivaciones) cuyo núcleo argumentativo ya está en el capítulo principal. Si la elaboración desaparece, la discriminación rival sobrevive. Verificable antes de migración.

## Política de cierre del borrador

Este borrador **no** decide la migración. La fusión final requiere firma H-J*. En particular requieren decisión humana:

1. **Confirmar la división rivales tabulares (§2) vs rivales discursivos (§3).** El criterio aplicado fue: si la matriz 14×6 de `03` captura la discriminación, no se desarrolla aquí. Si hay concesión asimétrica, restricción honesta, citas primarias clave, o reconocimiento de cercanía con la tesis, se desarrolla. Jacob puede mover rivales entre §2 y §3 según criterio editorial.
2. **Confirmar la lista de siete archivos `_extendido/rival-<X>.md`.** Solo se crean si Jacob valida que el material extendido aporta valor de elaboración (citas paginadas no presentes en el capítulo principal, derivaciones técnicas). Si alguno se considera elaboración prescindible, no se crea.
3. **Decidir si la frase eslogan "Wolfram fundamenta; la tesis disciplina" se conserva o se reemplaza.** La auditoría F04-06 (`Bitacora/2026-05-11-sintesis-tesis/02-triage-bitacora-huerfana.md`) marca esta frase como manierismo que oculta asimetría modal. Este borrador la conserva como síntesis sintetizadora (no como respuesta a la pregunta filosófica nuclear) pero la decisión final es H-J*.
4. **Decidir si `01` mantiene su lugar en `TesisFinal/build.py` PARTS (capítulo 25) o se reordena.** El borrador asume orden actual.
