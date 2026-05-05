# F03-04 — Traducción B↔L3 admite trampa: parámetro nombrado sin medición independiente

**Fecha:** 2026-05-05
**Origen:** adversarial-reviewer cap03 (2026-05-05)
**Archivos señalados:**
- `03-formalizacion/04-operacionalizacion-de-kappa.md:106-108` (Patología 3)
- `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:94` (criterio de fallo)
- `03-formalizacion/07-plantilla-dossier-anclaje.md:128-141` (Tabla 3.7.4)
- `03-formalizacion/05-etica-y-gobernanza-de-datos.md:55` (Caso 30, k_g=7.50)

## (a) Verificación de la afirmación adversarial

**Afirmación:** «La traducción B↔L3 admite trampa nominal: basta nombrar un parámetro como "biomecánico" para considerarlo traducido, sin exigir procedimiento de medición independiente del ajuste L3 (Frigg & Hartmann, *Stanford Encyclopedia of Philosophy*, "Models in Science", §2.4 sobre representación y similitud estructural).»

**Verificación textual contra el manuscrito:**

1. Patología 3 (línea 108) define el remedio como «reformular las funciones del sistema en términos de leyes de control con motivación ecológica o biomecánica». **Confirmado:** el criterio operativo es la **motivación** del nombre funcional, no la **medición independiente** del valor del parámetro.

2. El criterio de fallo del dossier (`02-…:94`) dice «algún parámetro de L3 no se traduce a B (formalismo desanclado)» sin especificar qué cuenta como traducción válida. **Confirmado:** la "traducción" no está operacionalizada.

3. Tabla 3.7.4 (`07-…:132-138`) propone columnas `Parámetro de L3 | Variable de B | Unidad | Operacionalización`. La columna "Operacionalización" muestra ejemplos como «medición directa» y «calibración empírica», pero **no exige distinguir entre ambas ni declarar la fuente del valor numérico**. Una calibración por ajuste a los mismos datos que el dossier explica satisface formalmente la columna.

4. Caso 30 (línea 55) declara explícitamente: «Los parámetros (b=3.25, k_g=7.50, c1=0.40, c2=0.40) son los publicados en la fuente original [Fajen y Warren 2003]». Esos parámetros provienen de un ajuste de Fajen-Warren a sus propios datos de captura motora; aunque las variables tienen interpretación biomecánica/informacional, **el valor `k_g=7.50` no proviene de una medición independiente del comportamiento de aproximación-evitación que el modelo explica**. Es ajuste, no medición de B.

**La objeción es válida.** La traducibilidad B↔L3 tal como está formulada en el manuscrito es vulnerable a la "trampa nominal" descrita en Frigg-Hartmann §2.4: la similitud estructural sin protocolo de medición externo no garantiza referencia.

## (b) Propuesta de edición concreta — DRAFT-AI, requiere firma de Jacob

Esta enmienda **toca un criterio definitorio de admisión** del aparato (qué cuenta como L3 anclado). Por CLAUDE.md §3 y §6, la voz autoral filosófica es de Jacob: la asistencia propone, Jacob firma. **`needs_human`** para corte final.

### Edición propuesta 1 — Patología 3 (`04-operacionalizacion-de-kappa.md:106-108`)

> ## Patología 3: el modelo que no se traduce a B
>
> Caso: la dinámica de baja dimensión funciona pero ninguno de sus parámetros se traduce a una variable biomecánica, informacional o de tarea **mediante un procedimiento de medición independiente del ajuste L3**. Diagnóstico: el modelo es L3 desanclado, aun si los nombres de las variables sugieren motivación biomecánica. **No basta con que un parámetro se llame "rigidez de control" o "tasa de aproximación"; se exige que su valor numérico provenga de un protocolo de medición en B (cinemática, fuerza, latencia perceptiva, etc.) que no use los mismos datos que se ajustan en L3.** Remedio: (i) aportar el procedimiento de medición independiente, o (ii) declarar el parámetro como **calibrado por ajuste** y por tanto **no traducido**, lo que degrada el dossier al estatus de descripción nominal en ese parámetro, o (iii) reformular el sistema con leyes cuyos parámetros sí admitan medición externa.

### Edición propuesta 2 — Tabla 3.7.4 (`07-plantilla-dossier-anclaje.md:132-138`)

Añadir columna explícita y desdoblar "Operacionalización" en dos:

| Parámetro de L3 | Variable de B | Unidad | **Procedimiento de medición independiente** | **Valor medido independientemente** | Valor usado en L3 | Diferencia |
|-----------------|---------------|--------|---------------------------------------------|-------------------------------------|--------------------|------------|
| ode_alpha | tasa de … | s⁻¹ | [protocolo en B, citado] | [valor + IC] | [valor de ajuste] | [δ relativo] |
| … | … | … | **Si esta celda dice "ajuste a los mismos datos", el parámetro queda marcado como NO TRADUCIDO** | — | … | — |

Regla añadida bajo la tabla: «Un parámetro cuya celda *Procedimiento de medición independiente* esté vacía o coincida con el ajuste de L3 se reporta como **calibrado, no traducido**. Un dossier con ≥1 parámetro central calibrado y no traducido se admite solo en modo programático (no demostrativo) y debe declararlo en §13 Limitaciones.»

### Edición propuesta 3 — Criterio de fallo (`02-criterios-de-legitimidad-y-metodo.md:94`)

> - algún parámetro de L3 no se traduce a B **mediante medición independiente del ajuste L3** (formalismo desanclado **o calibración nominalizada como traducción**);

### Edición propuesta 4 — Caso 30 (`05-etica-y-gobernanza-de-datos.md:55`)

Añadir nota explícita de costo:

> Aclaración de costo: los parámetros `(b, k_g, c1, c2) = (3.25, 7.50, 0.40, 0.40)` provienen del ajuste de Fajen y Warren (2003) a sus datos VENLab, no de medición independiente en variables biomecánicas (rigidez efectiva, viscosidad de control). Por la regla de Patología 3 actualizada, el caso 30 queda **calibrado, no traducido** en sus cuatro parámetros centrales y por tanto opera en **modo programático**, no demostrativo, respecto al criterio D (traducibilidad B↔L3). Esto se asume como deuda residual del caso ancla (§13).

## (c) Costo argumentativo declarado

1. **Pérdida fuerte:** el caso ancla canónico (Fajen-Warren) deja de cumplir el criterio D en sentido estricto. Esto rebaja la matriz 20/20 de Tabla 3.2.1: el criterio "Anclaje material" o "Reversibilidad parcial" debería bajar a 1 (o introducir un criterio nuevo "Traducibilidad estricta" que el ancla cumple en 1, no en 2).
2. **Pérdida programática:** varios casos del corpus EDI que hoy se reportan como "traducidos" porque sus parámetros ODE tienen nombres físicos (k_o, c2, etc.) caerán a "calibrados, no traducidos" hasta que se aporten mediciones independientes. Esto restringe el modo demostrativo a un subconjunto menor del corpus.
3. **Ganancia:** el aparato deja de admitir la trampa nominal Frigg-Hartmann. La traducibilidad B↔L3 se vuelve auditable con un criterio binario (¿hay protocolo de medición externo, sí o no?), no por inspección semántica del nombre del parámetro.
4. **Riesgo abierto:** el criterio "medición independiente del ajuste" puede ser demasiado fuerte en dominios donde toda medición de un parámetro de control involucra el mismo sistema acoplado (e.g. ¿cómo medir `k_g` independientemente de una tarea de aproximación?). Jacob debe decidir si la regla admite **medición indirecta vía intervención discriminante** (manipular `d_g` y observar respuesta de `φ̇`) como sustituto aceptable de medición directa, o si exige medición directa estricta.

## Estado

- **Verificación:** confirmada, la objeción es real.
- **Edición propuesta:** redactada en DRAFT-AI, cuatro puntos de modificación.
- **Cierre:** `needs_human` — Jacob debe firmar (i) la reformulación de Patología 3, (ii) la rebaja del caso ancla a "modo programático" en criterio D, (iii) si admite medición vía intervención como sustituto. Acción técnica de la asistencia detenida hasta ese corte.

## Referencias

- Frigg, R. & Hartmann, S. (2024). "Models in Science", *Stanford Encyclopedia of Philosophy* (Spring 2024 ed.), §2.4 "Representation and similarity". URL: https://plato.stanford.edu/entries/models-science/ — fuente del argumento adversarial. Acceso pendiente de verificación local: PDF no presente en `07-bibliografia/`.
- Fajen, B. R. & Warren, W. H. (2003). "Behavioral dynamics of steering, obstacle avoidance, and route selection", *Journal of Experimental Psychology: Human Perception and Performance*, 29(2), 343-362. (Fuente del ajuste original; valores de `k_g` etc.)
