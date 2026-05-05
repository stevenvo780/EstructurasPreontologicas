# F02-05 — Brandom 1994: paginación incorrecta y tesis brandomiana ambigua

**Fecha:** 2026-05-04
**Archivo afectado:** `02-fundamentos/02-epistemologia-de-la-compresion.md:72`
**Estado:** `needs_human` (decisión filosófica + verificación de PDF no presente en `07-bibliografia/`)

## (a) Verificación de la afirmación

Cita actual en el manuscrito (línea 72):

> Brandom (1994, *Making it Explicit*, cap. 3, p. 89) lo articula: *"to grasp the meaning of an expression is to grasp its role in inference"*.

Dos problemas detectados:

1. **Paginación fuera de rango.** En la edición Harvard UP 1994 de *Making it Explicit*, el capítulo 3 ("Linguistic Practice and Discursive Commitment") va aproximadamente de p.141 a p.198. La p.89 cae dentro del capítulo 2, no del capítulo 3. La cita "(cap. 3, p. 89)" es internamente inconsistente.
2. **Atribución de la cita literal no verificable localmente.** El PDF de Brandom 1994 NO está en `07-bibliografia/` (`ls 07-bibliografia/ | grep -i brandom` → vacío). La frase *"to grasp the meaning of an expression is to grasp its role in inference"* es una formulación canónica del inferencialismo, pero no he podido confirmar que sea cita textual literal de Brandom 1994 con esa paginación. Brandom suele formularlo en términos de *inferential articulation* / *commitments and entitlements*, no con la fórmula reducida tipo Sellars/Dummett que aquí se le atribuye.

→ Este es exactamente el patrón **F6 — cita decorativa** que CLAUDE.md §5 prohíbe: autor invocado como autoridad sin engagement verificable con el pasaje.

## (b) Problema filosófico independiente del paginado

El adversarial-reviewer señala una tensión más grave que la página: **inferencialismo brandomiano (cap. 8 de MiE, "material inference") contradice el homomorfismo material defendido en §3.5.3** del mismo capítulo de la tesis.

- Brandom-cap.5 (*expresivismo lógico*): el rol del vocabulario lógico es hacer explícitas inferencias materiales ya en juego. Compatible con la postura operativa de la tesis.
- Brandom-cap.8 (*inferencialismo material fuerte*): el contenido conceptual *se agota* en su rol inferencial dentro de prácticas discursivas. Esta lectura es **anti-representacionalista** y choca con cualquier "homomorfismo material" entre estructura del modelo y estructura del fenómeno (que la tesis afirma en §3.5.3).

La tesis dice "inferencialismo brandomiano matizado" sin declarar **qué tesis brandomiana importa**. Sin esa declaración, la sección queda vulnerable a la objeción: "o bien aceptas el inferencialismo material de Brandom y abandonas el realismo estructural moderado de §3.5.3, o bien usas a Brandom decorativamente".

## (c) Propuestas de edición (decisión a Jacob)

Tres salidas posibles, con costo declarado:

**Opción 1 — Corrección mínima (mantener cita, ajustar paginación):**
Sustituir "cap. 3, p. 89" por la paginación correcta tras consulta directa al PDF. Requiere:
- obtener PDF de Brandom 1994 (B-T-*: pendiente bibliografía) — actualmente ausente en `07-bibliografia/`;
- verificar que la frase entrecomillada es literal o reformularla como paráfrasis sin comillas.
- **Costo:** no resuelve la tensión filosófica con §3.5.3.

**Opción 2 — Sustitución por fuente accesible y declarar lectura "expresivista":**
Reemplazar la cita por Brandom (2000, *Articulating Reasons*, Introduction §I) — exposición más breve y citable del inferencialismo —, y añadir frase explícita: *"Importamos de Brandom la tesis expresivista (cap. 5 de MiE / cap. 1 de AR): el vocabulario lógico hace explícitas inferencias materiales sostenidas en práctica. NO importamos la tesis inferencialista material fuerte (cap. 8 de MiE), que sería incompatible con el realismo estructural moderado de §3.5.3."*
- **Costo:** obliga a reescribir §3.5.1 y articular el matiz; requiere PDF de *Articulating Reasons* (también ausente en `07-bibliografia/`).

**Opción 3 — Eliminar la cita decorativa:**
Borrar la cita Brandom y reformular §3.5.1 sin apelar a autoridad: *"el significado operativo de un término se constituye por su rol dentro del aparato (sondas, intervenciones ablativas, predicciones diferenciales). Esta posición es afín al inferencialismo, pero no presupone la tesis brandomiana fuerte de que el contenido conceptual se agote en rol inferencial."*
- **Costo:** se pierde el anclaje en literatura filosófica analítica; gana coherencia interna.

## Recomendación de la asistencia

**Opción 3 como default operativo** (elimina F6 sin compromiso filosófico extra), con **Opción 2 como objetivo si Jacob quiere conservar el ancla brandomiano** y se consigue el PDF.

**No procedo a editar 02-epistemologia-de-la-compresion.md** porque la decisión cruza voz autoral filosófica (CLAUDE.md §3) y requiere firma de Jacob entre las tres opciones.

## Acceptance check

- [x] Paginación verificada como inconsistente (cap.3 ≠ p.89)
- [ ] Paginación corregida → bloqueado (sin PDF local)
- [ ] Declaración explícita de cuál tesis brandomiana se importa → propuesta redactada, pendiente decisión humana
- [x] Marcado `needs_human` y registrado en bitácora

## Nuevas tareas derivadas

- **B-T-bib-brandom:** añadir Brandom 1994 *Making it Explicit* y/o 2000 *Articulating Reasons* a `07-bibliografia/` (vía `/fetch-biblio`).
- **H-J-3.5.1:** Jacob decide entre Opción 1/2/3 para §3.5.1.
