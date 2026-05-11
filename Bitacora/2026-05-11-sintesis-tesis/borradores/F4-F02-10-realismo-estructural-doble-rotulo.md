---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 02-fundamentos/02-epistemologia-de-la-compresion.md:93
hallazgo: Bitacora/2026-05-04-continuous-run/F02-10-realismo-estructural-doble-rotulo.md
tipo: reemplazo_parrafo (Opción A)
---

## Diagnóstico

La línea 93 de `02-fundamentos/02-epistemologia-de-la-compresion.md` introduce el rótulo **"realismo estructural representacional"** — un término que aparece **una sola vez en todo el manuscrito**, no figura en el glosario operativo, y no tiene anclaje a literatura primaria que lo autorice (Sellars 1956 §41 y Pearl no usan esa frase exacta). La línea 154 del mismo capítulo retoma el rótulo canónico **"realismo estructural moderado"** (definido en `00-proyecto/07-glosario-operativo.md` líneas 33 y 36 con la cláusula explícita de uso operativo no-Ladyman). Coexisten dos rótulos para una misma posición filosófica, y uno de los dos es invención local sin soporte. Esto duplica la tarea pendiente B-F2 (`TAREAS_PENDIENTES.md:59`) y abre flanco bajo §5 de CLAUDE.md (cita decorativa).

## Verificación

- "Realismo estructural representacional" — `grep` sobre el manuscrito: **1 ocurrencia** (línea 93 de cap 02-02). Sin entrada de glosario.
- "Realismo estructural moderado" — múltiples ocurrencias canónicas en `00-proyecto/07-glosario-operativo.md:33,36`, `02-fundamentos/01-ontologia-material-relacional.md`, `00-proyecto/00-abstract.md` y otros loci.
- Sellars 1956 *Empiricism and the Philosophy of Mind* §41 — PDF disponible en `07-bibliografia/Sellars - Empiricism and the Philosophy of Mind (1956).pdf`; la frase técnica "representación inferencial-funcional" no figura literalmente en §41 (que discute Jones y los reportes neuro-mentalistas), por lo que la cita actual del manuscrito en §3.5.3 invoca a Sellars como autoridad sin reproducir el argumento del autor — patrón F6 según CLAUDE.md §5.

## Texto propuesto (voz autoral filosófica de Jacob) — Opción A (recomendada)

**Reemplazar en `02-fundamentos/02-epistemologia-de-la-compresion.md:93`:**

> "¿Qué es una sonda ODE en relación con el fenómeno que describe? La tesis adopta **realismo estructural representacional**:"

**por:**

> "¿Qué es una sonda ODE en relación con el fenómeno que describe? La tesis lo articula bajo el **realismo estructural moderado** (glosario operativo §"Realismo estructural moderado", uso operativo no-Ladyman) en su faceta representacional. No es copia del fenómeno ni ficción útil: es **homomorfismo parcial bajo `Q`** que preserva las dependencias decisivas para responder la pregunta y declara las que no preserva. La cita a Sellars 1956 §41 y a Pearl funciona como apoyo conceptual (representación inferencial-funcional, estructura mínima suficiente bajo intervención) y no como aval de un rótulo distinto."

## Texto a reemplazar

- Línea 93 actual de `02-fundamentos/02-epistemologia-de-la-compresion.md` y el resto de los bullets de §3.5.3 quedan; sólo cambia la oración introductoria y se retira el rótulo redundante.
- No se toca el glosario (la entrada canónica permanece intacta).
- La cita a Sellars §41 se reformula como apoyo conceptual y no como autoridad del rótulo.

## Costo argumentativo declarado

La tesis pierde el matiz "representacional" como sub-rótulo independiente — matiz que en cualquier caso no estaba autorizado por literatura primaria. Gana adherencia estricta al glosario, cierra B-F2 sin abrir frente nuevo y evita un patrón F6 (cita de Sellars como autoridad de un rótulo que no usa). Si Jacob prefiere preservar el sub-modo representacional (Opción B del informe F02-10), la condición es traer literatura primaria que autorice el rótulo (candidato natural: Bueno & French, *Applying Mathematics*, 2018, *partial structures*; PDF ausente — fetch pendiente).
