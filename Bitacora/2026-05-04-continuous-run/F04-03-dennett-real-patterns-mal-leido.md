# F04-03 — Dennett *Real Patterns* (1991) mal leído como aliado

**Fecha:** 2026-05-04
**Sub-agente:** harness continuous-run
**Archivo objetivo:** `04-debates/04-anticipacion-objeciones-filosoficas.md` §5 (líneas 216-221)
**Acceptance:** §5 declara que "intervención ablativa simulada ≠ intervención woodwardiana sobre sistema físico"; lista de casos donde la diferencia es operativa; cita Dennett *J. Phil.* 88, p. 39.

---

## (a) Verificación textual

### Estado actual del manuscrito (líneas 216-221)

El §5 invoca a Dennett *Real Patterns* (1991, *J. Phil.* 88: 27-51) **paginando p. 32-34** y le atribuye el criterio de "compresión predictiva sin pérdida estructural relevante". Luego añade dos condiciones que la tesis declara como adiciones propias:

1. *Materialmente sostenido* (sustrato dinámico).
2. *Discriminante bajo intervención* (Woodward 2003).

### Lectura directa de Dennett, pp. 38-40 (PDF `07-bibliografia/Dennett - Real Patterns (1991).pdf`)

En **p. 39** Dennett describe el ascenso al *design level* en el Game of Life:

> "[…] their *salience as real things* is considerable, but not guaranteed. To say that their salience is considerable is to say that one can, with some small risk, ascend to this design level, adopt its ontology, and proceed to predict —sketchily and riskily— the behavior of larger configurations or systems of configurations, **without bothering to compute the physical level**." (Dennett 1991, p. 40, primera columna; el inciso clave del *level-ascent* arranca en p. 39 con la nota *"generalizations […] require 'usually' or 'provided nothing encroaches' clauses"*.)

**Lo que Dennett autoriza:** elevar a un nivel ontológico cuyas predicciones sobreviven *en el mismo sustrato simulado* (un autómata determinista cerrado). El riesgo del que habla es el riesgo de que un *encroachment* dentro del autómata rompa el patrón, **no** el riesgo de transitar de un modelo simulado a un sistema físico no simulado.

**Lo que Dennett no autoriza:** transferir el patrón desde una simulación ablada a un sustrato físico re-identificado. En *Real Patterns* la "intervención" es siempre *interna al mismo bit-map* (encroachment de bits ajenos, condiciones iniciales alternativas dentro del mismo Life world). Dennett nunca formula una intervención woodwardiana sobre un sustrato externo a la simulación.

### El golpe contra EDI

El protocolo EDI (cap 09) define la ablación como:

> EDI = 1 − RMSE_coupled / RMSE_no_ode (apagar el acoplamiento ODE→ABM **en el modelo**, manteniendo el forcing exógeno).

Esa ablación es **interna al modelo acoplado**, exactamente como las intervenciones de Dennett dentro del Game of Life. **No es** una intervención woodwardiana sobre el sustrato físico (ecosistema, red eléctrica, paisaje agrícola). La objeción adversarial acierta:

- *Real Patterns* p. 39 puede leerse como aliado **solo si la tesis declara que el régimen empírico del corpus EDI es estructuralmente análogo al Life world**: un sustrato simulado cuyas predicciones se evalúan *internamente*, no un sustrato físico al que se interviene de hecho.
- Si la tesis pretende además que la ablación interna del modelo *equivale* a evidencia woodwardiana sobre el sistema físico real, **eso excede tanto a Dennett como a Woodward**.

La nota actual del manuscrito (línea 221) reconoce que el PDF de Woodward "es escaneo sin capa de texto, lo que impide cita verbatim paginada", pero **no declara la asimetría entre intervención simulada e intervención física**. Ese es el déficit que F04-03 identifica.

---

## (b) Propuesta de edición concreta

**Touches declarados:** ninguno (read-only por regla).
**Estado:** `needs_human` para la firma de Jacob (afecta posición filosófica sustantiva del §5 y reformula el alcance del corpus EDI).

### Borrador propuesto (DRAFT-AI, 90% asistencia / 10% Jacob — pendiente de su voz)

Reemplazar el bloque de líneas 216-221 (sub-sección sobre Dennett) por:

> Sobre **Dennett** en *Real Patterns* (1991, *Journal of Philosophy* 88: 27-51): la lectura fuerte (pp. 38-40, especialmente p. 39, donde Dennett describe el ascenso al *design level* en el Game of Life) ofrece una analogía exacta con el régimen empírico del corpus EDI, pero con un costo que conviene declarar antes de invocarla.
>
> Dennett autoriza elevar a un nivel ontológico cuyas predicciones sobreviven *con cierto riesgo* (p. 39: "generalizations […] require 'usually' or 'provided nothing encroaches' clauses") **dentro del mismo sustrato simulado**. La intervención que Dennett contempla es interna al bit-map: encroachment de configuraciones vecinas, condiciones iniciales alternativas dentro del mismo Life world. No es una intervención woodwardiana sobre un sustrato físico externo a la simulación.
>
> El protocolo EDI hereda esa estructura: la ablación EDI = 1 − RMSE_coupled / RMSE_no_ode apaga el acoplamiento ODE→ABM **en el modelo acoplado**, no en el sistema físico que el modelo abstrae. La intervención es modelo-interna y simulada, no woodwardiana sobre el sustrato. **La tesis declara explícitamente esta asimetría: intervención ablativa simulada ≠ intervención woodwardiana sobre sistema físico.** El corpus EDI ofrece evidencia de que cierto patrón es real *en el sentido denneteano de p. 39* (sobrevive el filtro de compresión predictiva interna), no evidencia de que el patrón sobreviva manipulación física directa del sustrato.
>
> Casos donde la diferencia es operativamente decisiva:
>
> - **Caso 16 deforestación (von Thünen, EDI≈0.58-0.60).** La ablación apaga el acoplamiento von Thünen→agentes en el simulador, no se tala ni se reforesta el paisaje real. La evidencia woodwardiana sobre el paisaje real exigiría experimentos cuasi-naturales (cortes de carretera, expropiaciones, moratorias).
> - **Caso 04 energía (Lotka-Volterra, EDI=0.65).** La ablación es del acoplamiento red↔demanda en el modelo; la intervención woodwardiana exigiría apagar líneas reales y medir efectos en consumo.
> - **Caso 20 Kessler (densidad orbital, EDI=0.35).** La ablación cierra el feedback fragmentación→colisión en el simulador; ninguna agencia interviene físicamente la densidad orbital.
> - **Caso 27 riesgo biológico (mortalidad, EDI=0.33).** La ablación apaga el acoplamiento patógeno→demografía en el modelo; los datos físicos provienen de eventos epidémicos no manipulados experimentalmente.
> - **Caso 30 v1 VENLab (Fajen-Warren).** Aquí la asimetría se invierte: el caso *sí* tiene intervención experimental real sobre sujetos humanos en el VENLab, y por eso la sonda alternativa pudo detectar circularidad. El contraste con el resto del corpus muestra que *cuando la intervención woodwardiana existe, opera como filtro adicional al EDI*, no como su sinónimo.
>
> La tesis recoge entonces el criterio denneteano de patrón real (compresión predictiva interna) como criterio **necesario pero no suficiente** para la realidad woodwardiana del patrón. Donde el corpus tiene además acceso a manipulación física (caso 30 v1), la condición woodwardiana opera como filtro adicional. Donde el corpus solo tiene ablación interna del modelo (la mayoría del corpus), la tesis afirma realidad denneteana del patrón, no realidad woodwardiana fuerte. Esa modestia es el costo declarado de operar mayoritariamente con datos observacionales sobre los que no se interviene físicamente.

### Mover la cita en línea de §5

Actualizar la línea 221 cambiando el rango paginado citado de "pp. 32-34" (compresión) a "pp. 32-34, 38-40 (esp. p. 39)" para incluir el pasaje del *design level* y los *encroachment clauses* que dan el contenido sustantivo del argumento.

---

## (c) Costo argumentativo declarado

1. **La tesis pierde la lectura cómoda de Dennett como aliado universal.** *Real Patterns* p. 39 sostiene la realidad denneteana del patrón ablado en el modelo, pero **no** sostiene que esa realidad implique manipulabilidad woodwardiana del sustrato físico. La tesis paga el costo de declararlo: el corpus EDI ofrece evidencia denneteana en la mayoría de los casos, evidencia woodwardiana solo donde la intervención experimental existió de hecho (caso 30 v1).
2. **Modestia metodológica frente a un comité hostil.** Quien lea la tesis como afirmando manipulabilidad causal sobre los sustratos físicos del corpus desde los EDI internos, podrá objetar que la tesis confunde simulación con experimento. La edición propuesta corta esa objeción declarando la asimetría.
3. **El §5 deja de ser solo respuesta a F6 (citas decorativas) para asumir además F4 (ablación como evidencia limitada).** Esa expansión afecta otras secciones (cap 03-03 §criterios-admision; cap 09 narrativa de cada caso) que pueden necesitar revisión consistente.
4. **Riesgo:** si Jacob prefiere mantener la lectura más fuerte (Dennett + Woodward fusionados como evidencia conjunta), la edición propuesta debilita posición. La decisión es filosófica, no técnica — `H-J*`.

---

## Estatus

- **Verificación textual:** completa. Dennett 1991 p. 39 leído directamente; el paginado citado actualmente (p. 32-34) es correcto pero insuficiente para la afirmación que el §5 quiere apoyar.
- **Edición:** `needs_human` (afecta posición filosófica sustantiva).
- **Recomendación operativa:** abrir tarea **H-J F04-03** en `TAREAS_PENDIENTES.md` Sección A para la firma de Jacob sobre el borrador propuesto.

RESULT: complete | F04-03-dennett-real-patterns-mal-leido | borrador needs_human, p.39 verificada
