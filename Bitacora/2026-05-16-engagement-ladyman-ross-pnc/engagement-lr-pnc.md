# Engagement con Ladyman & Ross, *Every Thing Must Go* (2007) — PNC — DRAFT-IA

**Naturaleza del aporte:** 90% asistencia, 10% Jacob (validación final pendiente, H-J*).
**Requires:** decisión humana entre las tres salidas de §3 (concesión / reformulación / disenso).
**Verificación:** PDF abierto en `07-bibliografia/Ladyman Ross - Every Thing Must Go (2007).pdf`, extraído con `pdftotext -layout` a `/tmp/ladyman-ross.txt` (15.834 líneas), pasajes localizados por grep y verificados verbatim contra paginación impresa.
**Disparador:** adversarial iter 1 marcó la objeción OSR-PNC como **VULNERABLE**; cap 04-04 §1 menciona L&R defensivamente (línea 47: "no en el sentido fuerte de Ladyman y Ross 2007, donde la estructura es lo único que existe sin sustrato") sin engaged el PNC.

---

## §1. El PNC verbatim (Ladyman & Ross 2007, p. 37–38)

> "Any new metaphysical claim that is to be taken seriously at time *t* should be motivated by, and only by, the service it would perform, if true, in showing how two or more specific scientific hypotheses, at least one of which is drawn from fundamental physics, jointly explain more than the sum of what is explained by the two hypotheses taken separately, where this is interpreted by reference to the following terminological stipulations" (Ladyman & Ross 2007, p. 37).

Estipulaciones (p. 38):

> "A 'specific scientific hypothesis' is one that has been directly investigated and confirmed by institutionally bona fide scientific activity prior to *t* or is one that might be investigated at or after *t*, in the absence of constraints resulting from engineering, physiological, or economic restrictions or their combination, as the primary object of attempted verification, falsification, or quantitative refinement, where this activity is part of an objective research project fundable by a bona fide scientific research funding body" (p. 38).

Lectura mínima del PNC: la metafísica no se admite por sí misma; solo en la medida en que **una hipótesis nueva (i)** se conecta con **(ii)** al menos dos hipótesis científicas **específicas y bona fide**, **(iii)** una de las cuales pertenece a **física fundamental**, y **(iv)** produce explicación conjunta **estrictamente superior** a la suma de las explicaciones separadas. Es restricción **eliminativa**, no decorativa: L&R rechazan toda la metafísica analítica del siglo XX que no la satisfaga.

L&R añaden el **Primacy of Physics Constraint** (PPC, p. 39): "special sciences do not relate to physics the way that it relates to them". Y reformulan la motivación de OSR en p. 130: "Ontic Structural Realism (OSR) is the view that the world has an objective modal structure that is ontologically fundamental, in the sense of not supervening on the intrinsic properties of a set of individuals. According to OSR, even the identity and individuality of objects depends on the relational structure of the world. Hence, a first approximation to our metaphysics is: 'There are no things. Structure is all there is.'" (Ladyman & Ross 2007, p. 130).

---

## §2. ¿La tesis cumple el PNC?

Auditoría componente por componente.

### (i) ¿La tesis postula "nueva metafísica"?

Sí. El irrealismo operativo afirma:

- **L1 (sustrato material) ↔ B (atractor estructural) ↔ L3 (formalismo) ↔ S (sentido/uso)** como articulación asimétrica multiescalar invariante.
- "Estructuras pre-ontológicas" como categoría que precede ontológicamente a la fijación L1↔B↔L3↔S por un dossier.

Esto no es metodología neutra: es un compromiso sobre **qué tipo de cosas hay** (sustrato dinámico + patrones reales en sentido cuasi-denneteano + categorías operativas estabilizadas). La cláusula "irrealismo" sobre las categorías no neutraliza el realismo estructural moderado sobre los atractores ni el realismo material sobre el sustrato. **La tesis es metafísica nueva en el sentido PNC.**

### (ii) ¿Conecta ≥2 hipótesis científicas específicas?

Sí, el corpus de 40 casos exhibe articulaciones B↔L3 con sondas ODE concretas (SEIR epidemiológico, P-cycle de Carpenter, Hodgkin–Huxley-like en HRV, Lindblad para decoherencia, etc.). Cada caso conecta al menos una hipótesis empírica de su dominio con la hipótesis estructural del cierre operativo.

### (iii) ¿Al menos una hipótesis es de física fundamental?

**Aquí está la presión.** El corpus tiene dos candidatos:

- **Caso 31 — Decoherencia cuántica de qubit (transmón, parámetros NIST/IBM).** `metrics.json`: `edi=0.913`, `p_value=0`, `nivel=4_strong`. Pero `notes` declara: *"Sintético físicamente realista, parámetros transmón NIST/IBM"*. Es decir: la dinámica Lindblad es real-física, pero el dato del que se calcula EDI es **simulación**, no medida T1/T2 publicada por IBM. La estipulación PNC exige hipótesis "directly investigated and confirmed by institutionally bona fide scientific activity" (p. 38). Lindblad (1976) cumple la estipulación; el cómputo EDI sobre datos sintéticos cumple sólo en sentido débil.
- **Caso 32 — Acoplamiento espín-órbita (Bloch, 2 átomos).** `edi=0.825`, `p_value=0`, `nivel=4_strong`. Misma observación: dinámica fundamental, datos sintéticos.

Caso 41 (Wolfram extendido) y caso 39 (Cefeidas OGLE) involucran física, pero el primero es metafísica especulativa rival, no hipótesis empírica bona fide; el segundo es astrofísica, no fundamental en el sentido de L&R (que reservan "fundamental physics" para QM/QFT/GR; ver p. 39 nota).

**Conclusión parcial:** la tesis tiene **2 anclajes débiles** en física fundamental (cases 31, 32), ambos sobre datos sintéticos calibrados con parámetros reales. El PNC en lectura estricta —"specific scientific hypothesis directly investigated and confirmed"— no se cumple por los datos; se cumple por el modelo Lindblad/Bloch como hipótesis física confirmada en otra parte (literatura de óptica cuántica). Lectura indulgente: pasa. Lectura estricta: deuda.

### (iv) ¿Explicación conjunta > suma de partes?

El argumento de la tesis es que la **invarianza del cierre L1↔B↔L3↔S a través de escalas** (cuántica → atómica → bioquímica → celular → individual → astrofísica) explica algo que ninguna hipótesis de dominio aislada explica: la **co-aplicabilidad** del mismo dossier de admisión sobre 40 sustratos heterogéneos. Esto es **excess content** lakatosiano sobre el agregado.

Pero adversarial iter 1 ya identificó (y `04-debates/03 §H`) que: **predicciones novedosas pre-registradas fuera del corpus de calibración = 0**. Sin novel facts arriesgados, la "explicación conjunta superior" es retrospectiva, no progresiva. PNC no exige novel facts explícitamente, pero L&R sí los exigen en el cap 1 §1.2 vía "consilience" (p. 27). **La tesis no cumple consilience progresiva.**

**Veredicto §2: cumplimiento PARCIAL.** Hay anclaje en física fundamental (debil, sintético); hay conexión multi-hipótesis; hay explicación conjunta; pero no hay novel facts pre-registrados ni hipótesis directamente investigada bona fide en física fundamental con los datos del corpus.

---

## §3. Diagnóstico honesto y tres salidas (elección de Jacob)

### Salida (a) — Concesión

Aceptar que el PNC en lectura estricta no se cumple. Reformular cap 04-04 §1 para declarar: *"La tesis cumple PNC en lectura indulgente (anclaje físico vía Lindblad/Bloch como hipótesis confirmadas en literatura primaria); en lectura estricta, los datos del corpus son sintéticos calibrados, y la deuda H del cap 03 §G (novel facts pre-registrados = 0) impide consilience progresiva. La tesis es PNC-aspirante, no PNC-compliant; lo declara explícitamente."*

**Costo:** L&R quedarían en posición de decir "tu metafísica no debe tomarse seriamente todavía". La tesis pierde fuerza ante audiencia OSR ortodoxa.
**Beneficio:** honestidad estructural; alineada con §H de la Tabla 4.3.3.

### Salida (b) — Reformulación

Sostener que la tesis no propone "nueva metafísica" en el sentido del PNC, sino **metodología de admisión empírica de categorías operativas**. El PNC restringe metafísica; la tesis estaría en otra capa (filtro pre-ontológico). El propio cap 02-01 §0.1 declara naturalismo como "compromiso de partida operativo", no conclusión filosófica demostrada.

**Costo:** dialéctico — L&R podrían replicar (con razón) que toda metodología que decide qué cuenta como categoría real es ya metafísica disfrazada. Además, los compromisos sobre "sustrato material" y "atractores reales" exceden lo metodológico.
**Beneficio:** evita la confrontación directa con PNC en su jurisdicción más fuerte.

### Salida (c) — Disenso

Argumentar que el PNC mismo es **demasiado restrictivo y crypto-eliminativista**. L&R están cerca del eliminativismo sobre objetos (p. 130: *"There are no things. Structure is all there is."*) y exigen que toda metafísica tribute a física fundamental. La tesis disiente: la materialidad como **proceso dinámico instanciado** (cap 04-04 §6.2) es sustrato no-puramente-estructural y por tanto no puede absorberse en OSR. La tesis adopta una versión **debilitada del PNC** ("aspirante a anclaje físico, no obligado a fundación física"), siguiendo la línea de Floridi (2003), a quien L&R citan y rechazan (p. 191).

**Costo:** la tesis se separa de Ladyman-Ross públicamente; pierde la posibilidad de presentarse como "OSR-aliado". Asume el rol de **rival respetuoso** declarado.
**Beneficio:** posición filosóficamente articulada; consistente con cap 04-04 §6 (sustrato material como relato del relata, contra Goff).

---

## §4. Argumento OSR fuerte vs. irrealismo operativo

OSR fuerte (p. 130): la estructura modal objetiva es ontológicamente fundamental y no superviene en propiedades intrínsecas de individuos. Los objetos son **dispositivos pragmáticos** para orientar agentes en regiones del espacio-tiempo (p. 130: "objects are pragmatic devices used by agents to orient themselves in regions of spacetime").

Irrealismo operativo (cap 02-01 §0.3): las categorías son **fijaciones operativas** sobre patrones reales en sustrato material dinámico; los patrones reales se admiten vía dossier C1–C5; el sustrato material es real, dinámico, no-puramente-estructural.

**Punto de fricción exacto:** L&R sostienen que **estructura es todo lo que hay**; la tesis sostiene que **estructura es patrón real sobre sustrato material dinámico**. Si el sustrato material dinámico es a su vez puramente estructural, la tesis colapsa en OSR. Si no lo es, la tesis es OSR + materialismo dinámico, lo que L&R rechazarían como ontología duplicada (violación implícita de su parsimonia estructural).

L&R adoptan a Dennett ("Real Patterns" 1991) como **incompleto pero correcto en dirección**, y lo completan con OSR (p. 202–203). La tesis adopta a Dennett en versión más fuerte (cap 04-04 §6 cita Dennett 1991 p. 39) **sin** completarlo con OSR — usa el sustrato material como ese complemento. Es divergencia explícita.

**¿La tesis es OSR debilitado o posición distinta?** Es posición distinta: el sustrato dinámico instanciado no es eliminable como "dispositivo pragmático". La tesis es **realismo estructural moderado anclado en materialidad dinámica**, no OSR.

---

## §5. Recomendación operativa para Jacob

Recomendación: combinar **salida (c) + parte de (a)**. Concretamente:

1. Reescribir cap 04-04 §1 (línea 47) para que la mención defensiva de L&R 2007 se convierta en confrontación articulada al PNC con cita verbatim p. 37–38 y declaración del disenso. Texto sugerido (BORRADOR-IA): *"La tesis no cumple el PNC en lectura estricta (datos sintéticos en casos 31–32, novel facts pre-registrados = 0). Tampoco lo acepta como criterio único: el PNC privilegia física fundamental sobre toda otra hipótesis bona fide, posición que la tesis considera demasiado restrictiva. Adopta en cambio una versión debilitada — anclaje aspirante, no fundación obligada — consistente con la materialidad dinámica del cap 04-04 §6."*

2. Actualizar `04-debates/03-tabla-comparativa-rivales.md` rival 12: explicitar que la discriminación en A es **sustantiva y declarada**, no terminológica; añadir cita p. 130 ("There are no things. Structure is all there is.") como contraste verbatim.

3. Abrir entrada en `TAREAS_PENDIENTES.md` H-J* con: *"Decidir entre salidas (a), (b), (c) del engagement Ladyman-Ross PNC; sin decisión, la objeción OSR queda VULNERABLE en defensa pública."*

**Costo real declarado:** la tesis cede que (i) el PNC en lectura estricta no se cumple por el corpus, (ii) novel facts = 0 impide consilience progresiva, (iii) L&R queda como rival, no como aliado.

---

## §6. Lo que este DRAFT-IA no resuelve

- No es decisión filosófica; es material de decisión.
- No reescribe cap 04-04 §1 (regla §3: voz autoral de Jacob).
- No verifica si caso 31 puede usar datos reales IBM Quantum (parece factible según `corpus_multiescala/README.md` línea: *"31 | IBM Quantum Experience (T1, T2 públicos) | abierto | 2-3 meses"*) — si esto se ejecuta, la salida (a) se debilita y la (c) se fortalece.
- No agota el cap 5 de L&R (Rainforest Realism); el engagement con RR queda pendiente como bitácora separada (es donde L&R hacen el trabajo más cercano a la tesis y donde la discrepancia es más fina).
