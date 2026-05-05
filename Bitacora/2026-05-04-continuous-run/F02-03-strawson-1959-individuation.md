# F02-03 — Strawson 1959 citado decorativamente

**Fecha:** 2026-05-04
**Archivo señalado:** `02-fundamentos/03-categorias-objetos-propiedades-e-identidad.md:202`
**Origen del hallazgo:** adversarial-reviewer cap.02 (2026-05-05)

## (a) Verificación de la afirmación

Cita actual en línea 202:

> **Strawson** (1959, *Individuals*) defiende re-identificación a través del cuerpo. La tesis recoge: el cuerpo es el **acoplador material continuo** que sostiene la cuenca.

**Diagnóstico CLAUDE.md §5 — cita decorativa:**

1. **Sin paginación.** Solo año y título; ningún capítulo, sección ni página.
2. **Sin cita textual.** Strawson 1959 es invocado como autoridad sin reproducir su argumento.
3. **Reducción problemática del contenido de Strawson.** *Individuals* (cap. 1 "Bodies" y cap. 3 "Persons") sostiene una tesis MÁS FUERTE que "re-identificación a través del cuerpo": que **persona** es un *primitive concept* — un tipo lógico irreductible al que se atribuyen tanto P-predicates (estados de conciencia) como M-predicates (corporales) — precisamente para bloquear el dualismo cartesiano y el reduccionismo materialista. Reducir Strawson a "el cuerpo es el acoplador material continuo" es **colapsar su tesis del primitivismo lógico a una tesis corporalista** que él explícitamente rechaza (cap.3 §"Persons", la conciencia no es atribuible a un cuerpo *qua* cuerpo, sino a la persona como tipo primitivo).
4. **Objeción de circularidad de Lowe (1998, *The Possibility of Metaphysics*, cap. 6) no respondida.** Lowe argumenta que individuación corporal presupone criterios de identidad sortales que ya implican el tipo de objeto que se quiere individuar — la tesis usa la cuenca de atractor para individuar al sistema acoplado, pero el atractor mismo se define sobre componentes ya tipificados (cuerpo, memoria, relación). Riesgo: circularidad operativa.

## (b) Acceso a fuentes

Verificado con `ls 07-bibliografia/ | grep -iE "strawson|lowe"`: **ni Strawson 1959 ni Lowe 1998 están en la biblioteca local.** No es posible producir cita textual paginada desde este sub-agente sin acceso a los PDFs.

## (c) Propuesta de edición — needs_human + bibliography-fetch

**Acción 1 (operativa, ejecutable por asistencia):** invocar `/fetch-biblio` para obtener:
- Strawson, P. F. (1959). *Individuals: An Essay in Descriptive Metaphysics*. Methuen. Cap. 3 "Persons".
- Lowe, E. J. (1998). *The Possibility of Metaphysics: Substance, Identity, and Time*. OUP. Cap. 6.

**Acción 2 (filosófica, requiere firma Jacob — H-J):** decidir entre dos salidas, ambas con costo declarado:

- **Salida A — concesión:** retirar la cita a Strawson y reformular sin él. Costo: pérdida del único anclaje analítico clásico para identidad personal corporal en el capítulo; queda solo Locke/Parfit como interlocutores anglófonos.

- **Salida B — engagement honesto:** mantener Strawson pero reescribir el pasaje reconociendo (i) que Strawson defiende **persona como tipo primitivo lógico, no reducible a cuerpo**, (ii) que la tesis de la cuenca-atractor *converge* con Strawson en rechazar tanto cartesianismo como reduccionismo psicológico pero *diverge* en que la tesis ofrece un **mecanismo dinámico** (atractor) donde Strawson solo afirma primitividad lógica. Costo: la tesis se compromete a mostrar que el atractor no recae en el corporalismo que Strawson rechaza — debe responder por qué la cuenca-de-atractor del sistema acoplado no es solo "cuerpo extendido + memoria" (lo que Strawson llamaría una mezcla cartesiana disimulada). Y debe responder a Lowe sobre circularidad de los sortales individuantes.

**Borrador propuesto para Salida B (DRAFT-AI, requiere firma Jacob):**

> **Strawson** (1959, *Individuals*, cap. 3 "Persons", §1, [pp. ~_pendiente_]) defiende que **persona** es un concepto primitivo: un tipo lógico al que se atribuyen tanto P-predicates (conciencia) como M-predicates (corporalidad) sin reducción de unos a otros. La tesis converge con Strawson en rechazar tanto el alma cartesiana como el reduccionismo psicológico, pero *añade* un mecanismo dinámico: la primitividad strawsoniana se expresa operativamente como **cuenca persistente del atractor del sistema acoplado**. Concesión: la cuenca-atractor no debe leerse como "cuerpo extendido", o se colapsa al corporalismo que Strawson rechaza; lo primitivo es el sistema acoplado completo bajo perturbación, no su sustrato material. Objeción pendiente (Lowe 1998, *The Possibility of Metaphysics*, cap. 6, [pp. ~_pendiente_]): la individuación operativa por cuenca presupone tipos sortales (cuerpo, memoria, relación) que ya están individuados — riesgo de circularidad. Respuesta provisional: la circularidad es virtuosa si los sortales son revisables empíricamente bajo el aparato (cap. 04 §debates), no viciosa.

## Costo argumentativo declarado

- Salida A: pérdida de profundidad analítica; cap. 02-03 §8.bis queda con menos densidad bibliográfica.
- Salida B: la tesis se compromete a sostener bajo crítica que (i) atractor ≠ corporalismo, (ii) la circularidad de individuación es revisable y no viciosa. Esa carga es real.

## Estado

`needs_human` — la elección entre Salida A y B es decisión filosófica (H-J). La verificación paginada requiere `/fetch-biblio` para Strawson 1959 y Lowe 1998 (no presentes en `07-bibliografia/`).
