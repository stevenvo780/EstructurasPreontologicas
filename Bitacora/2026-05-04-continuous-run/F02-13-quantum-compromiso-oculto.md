# F02-13 — Compromiso interpretativo oculto en §13.1 cuántico

Fecha: 2026-05-04
Origen: hallazgo adversarial-reviewer cap02 (panel 2026-05-05)
Archivo señalado: `02-fundamentos/01-ontologia-material-relacional.md` líneas 384-405
Estado: **needs_human** (requiere firma H-J* de Jacob + B-T* fetch Wallace 2012)

## (a) Verificación de la afirmación

Se leyó el §13 íntegro (líneas 384-405). El texto dice literalmente:

> "La tesis NO decide entre estas interpretaciones realistas — esa decisión rebasa el alcance del manuscrito" (línea 397).

Y simultáneamente (línea 401):

> "el caso 31 (decoherencia) opera dentro de **decoherencia ambiental**, que es la interpretación realista más conservadora compatible con experimentos actuales."

La objeción adversarial es **parcialmente válida**:

1. El caso 31 (`corpus_multiescala/31_decoherencia_cuantica/`) sí está construido sobre la maquinaria Zurek (einselection, base puntero, supresión de coherencias por acoplamiento ambiental). Esto se confirma por la presencia del directorio y la cita explícita a Zurek 2003 en línea 395.
2. La **decoherencia + einselection sola no resuelve el problema de la medición** (no explica por qué se observa una sola rama). Wallace (2012, *The Emergent Multiverse*, OUP, cap. 2 — *no disponible en `07-bibliografia/`*) argumenta sostenidamente que decoherencia es **el complemento técnico necesario de Everett**, no una posición neutra entre interpretaciones. Quien adopta la maquinaria einselection sin postulado de colapso adicional **ya tomó partido por Everett en la lectura realista canónica**.
3. Bohm requiere que la base puntero coincida con la base de posición (compromiso ontológico distinto). GRW requiere un término de colapso espontáneo que modifica la dinámica unitaria pura sobre la que se construye einselection. **Ninguna de las tres lecturas es trivialmente equivalente respecto al caso 31.**

Lo que es defendible y lo que no:
- **Defendible**: la tesis usa decoherencia *en lectura no-subjetivista* (línea 395: "no de un observador consciente"); esto es genuinamente más débil que comprometerse con Everett-Wallace.
- **No defendible tal cual está**: presentar Everett, Bohm, GRW y decoherencia como si fueran cuatro miembros simétricos de "la familia realista" entre los cuales la tesis no decide — cuando el caso 31 ya implementó la dinámica unitaria + selección ambiental, que es exactamente el armazón Everett-Wallace.

## (b) Propuesta de edición (needs_human)

La acción "Acceptance" pide:
> Párrafo §13.1 declarando compromiso interpretativo efectivo + cita paginada Wallace 2012 *Emergent Multiverse* cap. 2; reconocer que Bohm/GRW exigirían modificación.

**No puede cerrarse desde la asistencia** por dos razones:

1. **Wallace 2012 PDF no está en `07-bibliografia/`** (verificado con `ls`). CLAUDE.md §5 prohíbe citar autor sin paginación verificada → requiere `B-T fetch-biblio Wallace 2012` antes de poder paginar.
2. **El compromiso interpretativo es decisión filosófica de Jacob**, no técnica. La asistencia puede señalar el costo, no firmarlo. Marcar `H-J*`.

Esbozo del párrafo (DRAFT-AI, NO commit hasta firma Jacob + paginación Wallace):

> §13.1bis — Compromiso interpretativo efectivo. La adopción operativa de decoherencia + einselection (Zurek 2003) en el caso 31 no es neutra entre interpretaciones realistas. Wallace (2012, *The Emergent Multiverse*, OUP, cap. 2, pp. XX-YY [PEND]) argumenta que decoherencia ambiental es el complemento técnico que hace coherente a Everett, no una posición independiente. La tesis reconoce, por tanto, un **compromiso efectivo con la familia Everett-Wallace** en su uso operativo de la base puntero, aunque no se compromete con la metafísica de mundos paralelos. Bohm exigiría que la base puntero coincidiera con la base de posición (modificación no trivial); GRW exigiría un término de colapso espontáneo no presente en el modelo (modificación de la dinámica). El caso 31 *podría* reescribirse en clave Bohm o GRW, pero ello requeriría reconstruir la sonda macro, no solo cambiar la lectura interpretativa. **Costo declarado**: la tesis es compatible con Everett-Wallace en uso, no con cualquier interpretación realista en sentido fuerte.

## (c) Costo argumentativo declarado

- **Honestidad ganada**: declarar que el caso 31 está técnicamente comprometido con dinámica unitaria + einselection (lectura Wallace) cierra una evasión que un examinador de filosofía de la física detectaría.
- **Costo perdido**: la tesis pierde la apariencia de neutralidad interpretativa amplia. Solo conserva la compatibilidad genuina con la familia *Everett-decoherentista*; Bohm y GRW pasan a ser "compatibles tras reescritura del caso 31", no "compatibles tal cual".
- **Impacto en monismo material (§0.1)**: ninguno; las tres lecturas realistas son monistas. La objeción no toca el núcleo, solo la exhibición del costo.
- **Riesgo de no editar**: el §13.1 actual contradice operativamente lo que el caso 31 hace; cualquier lector con formación en interpretaciones cuánticas leerá esto como evasión. Es F6 latente (cita decorativa de Bohm/GRW sin engagement).

## Tareas derivadas

- `B-T-F02-13a` (asistencia): fetch Wallace 2012 *The Emergent Multiverse* cap. 2 vía `/fetch-biblio` o sustituto secundario fiable (e.g., Wallace 2010 *Decoherence and ontology* preprint disponible en PhilSci-Archive).
- `H-J-F02-13b` (Jacob): firmar el compromiso "Everett-Wallace en uso, no en metafísica" o rechazarlo y proponer reescritura del caso 31 en clave Zurek-neutral (sin asumir dinámica unitaria pura).
- `B-T-F02-13c` (asistencia, tras H-J): si Jacob firma, redactar §13.1bis con paginación Wallace verificada y registrar deuda de Bohm/GRW como reescrituras pendientes (no realizadas).

RESULT line al final del prompt.
