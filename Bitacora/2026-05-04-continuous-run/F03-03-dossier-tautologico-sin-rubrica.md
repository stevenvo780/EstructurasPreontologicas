# F03-03 — Dossier 14 componentes y matriz 10 criterios sin rúbrica cuantitativa

**Fecha:** 2026-05-05
**Origen:** adversarial-reviewer cap03 (2026-05-05)
**Archivo señalado:** `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md` (líneas 6, 82, y §4 lns 98-129)
**Estado:** `needs_human` (B-T / H-J*)

## (a) Verificación de la afirmación

La objeción es **correcta como auditoría textual**:

1. **Línea 6 (Tesis del capítulo):** afirma que los diez criterios funcionan como *"filtro de admisión cuyo incumplimiento implica retiro de la propuesta"*, pero el filtro depende de un juicio cualitativo no rubricado.
2. **Línea 83 (Criterio de completitud del dossier):** *"Un dossier es admisible si los catorce componentes están presentes con **contenido sustantivo**. Componentes vacíos o decorativos invalidan el dossier."* La frase "contenido sustantivo" carece de rúbrica operativa: ¿qué cuenta como sustantivo y qué como decorativo? El texto no lo dice. Es exactamente el patrón que Hempel (1950, "Problems and Changes in the Empiricist Criterion of Meaning", *Revue Internationale de Philosophie* 4, pp. 41-63) señala: un criterio de significación empírica que no fija condiciones de aplicación reproduce la dificultad que pretende resolver.
3. **§4 Matriz de evaluación (lns 98-129):** define escala 0/1/2 a nivel macro pero **no fija umbrales por criterio**. ¿Cuándo un anclaje material es 1 vs 2? ¿Cuándo una robustez al 10% de ruido es 1 y al 20% es 2? El caso ancla obtiene **20/20** (línea 129). Una matriz que produce 20/20 en su propio caso paradigmático sin rúbrica explícita es **circular**: el caso fue elegido porque cumple, y la matriz fue calibrada para que cumpla.
4. La objeción adversarial coincide con dos problemas internos del propio capítulo:
   - §3.3 (lns 87-94) lista fallos del dossier en términos operacionales (do-test, predicción discriminante en datos públicos, traducción L3→B), pero §3.2 sigue apoyándose en "contenido sustantivo".
   - §4 reaplica una escala 0/1/2 sin mostrar el árbol de decisión que produce el valor.

**Conclusión:** la afirmación adversarial se sostiene textualmente. El capítulo declara un filtro auditable pero deja sin operacionalizar el predicado central ("sustantivo") y los umbrales de la matriz.

## (b) Propuesta de edición

La acceptance pide: *Tabla nueva en cap 03-02 §4 con rúbrica 0/1/2 explícita por criterio (umbrales justificados por dominio); reevaluación caso ancla con rúbrica nueva.*

La acción tiene **dos componentes separables**:

### B1. Rúbrica operativa por criterio (esqueleto, requiere firma de Jacob)

Borrador propuesto para §4 (a insertarse antes de la matriz del caso ancla, lns 108-129). Los umbrales son **propuesta técnica**; la justificación filosófica y la calibración por dominio requieren firma autoral.

| Criterio | 0 | 1 | 2 | Umbral defendible |
|---|---|---|---|---|
| 1. Anclaje material | sustrato no señalado o solo nominal | sustrato señalado pero sin descomposición operativa | sustrato + componentes + interfaces operativas explícitas | requiere lista enumerable de componentes materiales y su régimen de medición |
| 2. Dependencia empírica | sin acceso ni régimen R | acceso indirecto sin cuantificación de error | acceso directo o indirecto con régimen R explícito y error acotado | régimen R fechado, instrumento o protocolo nombrado |
| 3. Fidelidad relacional | la compresión borra dependencias detectadas por intervención | compresión preserva dependencias bajo `do`-test parcial | preserva bajo `do`-test sistemático en variables clave | al menos un `do`-test por arista marcada como crítica |
| 4. Poder inferencial | no permite conclusión nueva sobre la versión sin comprimir | permite conclusión nueva pero sin discriminar contra rival | conclusión nueva discriminante contra rival explícito | tabla comparativa con métrica común |
| 5. Poder predictivo | sin predicción cuantitativa | predicción cumplida en mismas condiciones de entrenamiento | predicción cumplida en condiciones nuevas (out-of-sample o out-of-domain) | error de predicción reportado con CI |
| 6. Poder interventivo | no orienta intervención | orienta intervención cualitativa | orienta intervención cuantitativa con respuesta predicha | predicción de signo y orden de magnitud verificada |
| 7. Robustez | inestable bajo cualquier perturbación | estable bajo perturbación menor (≤5% del rango de la variable) | estable bajo perturbación moderada (≥10%) en variables clave | rango de perturbación reportado con métrica de estabilidad |
| 8. Reversibilidad parcial | sin operador ε definido | ε definido informalmente | ε definido con protocolo y región de aplicación | protocolo de reapertura especificado |
| 9. Economía explicativa | parámetros ≥ datos relevantes | parámetros < datos pero sin ganancia comparativa | parámetros < datos con ganancia inferencial sobre rival | razón parámetros/grados-de-libertad reportada |
| 10. No reificación | la categoría se trata como sustancia independiente | tratamiento mixto, ambigüedad declarativa | la categoría se predica solo del sistema acoplado | revisión explícita de predicados sustantivos |

**Costo argumentativo declarado** (B1):

- Los umbrales numéricos (≤5%, ≥10%, etc.) son **convenciones por dominio** y heredan el problema de Roberts & Pashler 2000: un umbral que el caso ancla cumple por construcción no es discriminante. Para que la rúbrica sea defendible, **los umbrales deben fijarse antes de evaluar el caso ancla**, no después.
- El criterio 10 (no reificación) sigue siendo cualitativo. No hay forma operativa de detectar "tratamiento mixto" sin lectura interpretativa. Esto es deuda residual del propio criterio, no del rúbrica.
- Pasar de "contenido sustantivo" a una rúbrica operativa **convierte la matriz en un instrumento auditable** pero **no elimina la objeción Hempel**: simplemente la traslada a la justificación de los umbrales. Esto es honesto, no derrota.

### B2. Reevaluación del caso ancla con la nueva rúbrica

La reevaluación de Fajen-Warren 2003 con esta rúbrica **probablemente sigue dando alto puntaje** (8-10 criterios en 2), porque el caso fue elegido precisamente como ancla operativa. Lo informativo no es el total, sino:

- ¿Algún criterio cae a 1 cuando se aplica la rúbrica explícita? Candidato: **criterio 7 (robustez)**, donde el manuscrito declara "10% en variables perceptivas" — cumple el umbral propuesto pero **no se ha probado más allá de 10%**. La honestidad pide reportar como 2 con rango declarado, no como 2 absoluto.
- ¿El criterio 10 (no reificación) admite 2 sin lectura interpretativa? Probablemente sí porque el modelo declara "atractor del sistema acoplado", no del agente; pero esto debería **citarse textualmente** del paper original (Fajen & Warren 2003) y no afirmarse como obvio.

**Sin embargo**, decidir si el ancla baja de 20/20 a 18/20 o se mantiene en 20/20 con rango declarado **es decisión autoral**. La cifra 20/20 publicada en línea 129 funciona como anclaje retórico del capítulo y modificarla cambia el tono de §10 ("La tesis exige dossier publicable"). Esta es una decisión `H-J*`.

## (c) Costo argumentativo declarado

1. **Concesión:** la objeción adversarial es válida. La matriz actual es vulnerable al cargo de circularidad: el caso ancla fue elegido para anclar y obtiene 20/20 sin rúbrica operativa que justifique cada celda.
2. **Costo de aceptar la propuesta B1:** se reconoce que la versión actual del capítulo es **insuficiente sin rúbrica**, lo que obliga a marcar como deuda los demás casos del corpus (40 casos EDI) que no han sido evaluados con la matriz al nivel exigido. Esto es honesto pero implica trabajo adicional.
3. **Costo de no aceptar la propuesta:** mantener "contenido sustantivo" como predicado del filtro de admisión deja al capítulo expuesto a Hempel y a cualquier crítico que acuse al programa de auto-validación. La defensa "los catorce componentes están presentes" se vuelve verificable sólo de forma trivial.
4. **Concesión adicional:** incluso con rúbrica, la matriz hereda el problema de **dependencia de dominio** (un umbral del 10% de ruido para percepción-acción no es trasladable a deforestación o a clima). Por tanto la rúbrica debería **declararse condicional al dominio Q** y publicarse junto al dossier de cada aplicación, no como rúbrica universal.

## Marca de cierre

`needs_human` — la propuesta B1 es esqueleto técnico defendible; los umbrales por dominio y la decisión sobre B2 (mantener o ajustar 20/20 del caso ancla) requieren firma de Jacob, porque tocan tanto la calibración filosófica de los criterios como el anclaje retórico del capítulo. No se edita Tesis.md ni metrics.json.

## Referencias internas

- `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:6,82,98-129`
- Hempel 1950 (criterio de significación empírica)
- Roberts & Pashler 2000 (umbrales fijados ex post)
- Fajen & Warren 2003 (caso ancla)
- Pearl 2009 cap. 3, ya citado en §11.4 del propio capítulo
