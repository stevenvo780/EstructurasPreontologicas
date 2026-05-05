# F03-08 — `do`-test confundido con ablación de modelo

**Fecha:** 2026-05-05
**Origen:** hallazgo adversarial-reviewer cap03 (2026-05-05)
**Estado:** `needs_human` (requiere firma H-J* — modifica reclamo teórico central)

---

## (a) Verificación de la afirmación

### Lo que dice la tesis hoy

- **`03-formalizacion/01-aparato-formal.md:91-101` (§4.3-4.4)** establece que una arista `(v_i, v_j) ∈ E` es admisible si "es robusta a intervenciones específicas (`do(v_i)` cambia `v_j`)" y que el grafo se exige consistente "con intervención".
- **`03-formalizacion/01-aparato-formal.md:256-258` (§12.1)** afirma textualmente:
  > "La métrica EDI es **operacionalización directa de un do-test**: ablación del acoplamiento ODE con preservación del forcing exógeno, comparada contra coupled completo."
- **`03-formalizacion/06-mapa-operadores-formales.md:138` (Tabla 3.6.2, fila E)** glosa las aristas como "dependencias detectadas que pasan do-test"; fila W como "covarianza condicional, sensibilidad a intervención"; criterio de admisión "aristas robustas a intervenciones específicas".

### Lo que dice Pearl (fuente primaria)

Pearl 2009, *Causality* 2.ª ed. cap. 3 (p. 23 y p. 70):
> "the action `do(X = x)` represents an experiment in which the variable X is set to value x by an outside intervention, while the rest of the model remains unchanged"

La cita textual está bien copiada en §12.1. El problema **no es la cita**: es la equivalencia que la tesis postula entre esa operación y la métrica EDI.

### El error operativo

Pearl distingue tres niveles (asociación / intervención / contrafáctico). `do(X=x)` es **intervención sobre el sistema real** (o sobre una SCM que se postula como modelo causal verdadero del sistema real), no manipulación interna de un modelo que ya se admitió que es aproximación.

En 29 de los 30 casos del corpus macro:

1. La construcción de aristas en `G` se hace por **detección de covarianza condicional** sobre series temporales observadas (datos públicos no-experimentales: clima, deforestación, epidemiología, mercado, etc.). No hay intervención exógena sobre el sistema real.
2. El **EDI es una ablación dentro del simulador**: apaga el término de acoplamiento ODE→ABM y mide degradación predictiva. Esa operación no se ejecuta sobre el sistema real; se ejecuta sobre el modelo híbrido construido por los autores.
3. La inferencia "si la ablación degrada predicción, entonces hay dependencia causal en el sistema real" requiere supuestos identificadores extra (modularidad, fiel-Markov, no confounders) que la tesis **no declara ni testea**.

El único caso donde la apelación a `do` tiene tracción literal es **VENLab (caso 30, locomoción Fajen-Warren)** porque ahí sí hay manipulación experimental directa de la posición de la meta y de los obstáculos sobre sujetos reales — es el único locus donde la admisión de aristas se ancla en intervención pearliana genuina (y aun ahí la cita Warren 2006 documenta el dispositivo, no el grafo de aristas de la tesis).

### Diagnóstico

La afirmación "EDI es operacionalización directa de un do-test" es **metafóricamente sugerente pero técnicamente incorrecta**. EDI es una **ablación de modelo** que sirve como evidencia indirecta de dependencia (en el sentido de "si apago este término, mi modelo predice peor"), no una intervención causal sobre el sistema-blanco. Confundir ambas cosas es importar la fuerza epistémica del do-calculus sin pagar el costo de los supuestos identificadores.

Costo declarado: §4.3-4.4 y §12.1 venden más fuerza causal de la que el aparato realmente tiene. Es la objeción F03-08 del adversarial.

---

## (b) Propuesta de edición concreta — `needs_human`

Estas reescrituras tocan reclamos teóricos centrales (qué *es* exactamente EDI y qué fuerza tiene la admisión de aristas). **No las cierro yo**. Quedan como propuesta para Jacob.

### Propuesta para §4.3 (`01-aparato-formal.md:91-97`)

Reemplazar:

```
- es robusta a intervenciones específicas (`do(v_i)` cambia `v_j`);
```

por:

```
- es robusta a una intervención análoga al `do(v_i)` pearliano cuando hay
  acceso experimental al sistema (caso ancla VENLab); en los casos
  observacionales (29/30 del corpus macro) la admisión se reduce a
  ablación dentro del modelo híbrido (apagar el término de acoplamiento
  ODE→ABM degrada la predicción), bajo supuestos identificadores
  declarados en §12.1;
```

Y añadir una línea al final de §4.4 declarando explícitamente que la consistencia con ablación de modelo **no equivale** a la consistencia con `do` pearliano genuino.

### Propuesta para §12.1 (`01-aparato-formal.md:256-258`)

Reemplazar:

> "La métrica EDI es **operacionalización directa de un do-test**: ablación del acoplamiento ODE con preservación del forcing exógeno, comparada contra coupled completo."

por:

> "La métrica EDI **no** es un `do`-test pearliano sobre el sistema real (excepto en el caso ancla VENLab, donde el dispositivo experimental sí permite manipulación exógena). En los 29 casos observacionales del corpus macro, EDI es una **ablación de modelo**: se apaga el término de acoplamiento ODE→ABM dentro del simulador híbrido y se mide la degradación predictiva. La inferencia de EDI a dependencia causal en el sistema real exige supuestos identificadores adicionales (fidelidad del simulador al sistema, modularidad del acoplamiento, ausencia de confounders no modelados) que la tesis declara como costo. Lo que EDI sí establece sin estos supuestos es que el término ODE no es decorativo *en el modelo*: si fuera decorativo, su ablación no degradaría la predicción."

### Propuesta para Tabla 3.6.2 (`06-mapa-operadores-formales.md:138-141`)

Reemplazar:

| Campo | Especificación |
|-------|----------------|
| E (aristas) | dependencias detectadas que pasan do-test |
| W (pesos) | covarianza condicional, sensibilidad a intervención |
| Criterio de admisión | aristas robustas a intervenciones específicas |
| Criterio de fallo | manipular v_i no cambia v_j según predicción → eliminar arista |

por:

| Campo | Especificación |
|-------|----------------|
| E (aristas) | dependencias detectadas que pasan do-test (VENLab) o ablación de modelo (corpus observacional) |
| W (pesos) | covarianza condicional + sensibilidad a ablación del término ODE en el modelo híbrido |
| Criterio de admisión | aristas robustas a intervención experimental cuando es accesible; en caso observacional, robustas a ablación bajo supuestos identificadores declarados (§12.1) |
| Criterio de fallo | apagar v_i no cambia v_j en el modelo → arista decorativa, eliminar |

Y propagación obligatoria a `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md` y `03-formalizacion/07-plantilla-dossier-anclaje.md:45` (donde el dossier dice "dependencias detectadas que pasan do-test").

---

## (c) Costo argumentativo declarado

1. **Pérdida retórica:** la tesis ya no puede decir "EDI = do-test"; debe decir "EDI = ablación de modelo + supuestos identificadores → indicador indirecto de dependencia causal". Es menos vendible pero defendible.
2. **Costo filosófico:** se refuerza el realismo **estructural moderado operativo** (§glosario): las aristas son afirmaciones sobre la estructura del modelo que mejor predice, no afirmaciones directas sobre la causalidad del sistema real. Esto es coherente con el resto del aparato (irrealismo metodológico) pero hay que decirlo.
3. **Beneficio:** desactiva la objeción adversarial F03-08 sin pagar fragilidad: la tesis queda mejor blindada porque ya no promete intervención pearliana donde no la hay.
4. **Deuda derivada:** los supuestos identificadores (fidelidad, modularidad, no-confounders) que ahora se declaran como costo de §12.1 deben quedar listados como **deuda residual** del cap. 03 con plan o reconocimiento de irreductibilidad.

---

## Marca

`needs_human` — H-J* (Jacob debe firmar la reescritura porque modifica el reclamo central sobre qué *es* EDI epistémicamente). No tocado: `Tesis.md`, `metrics.json`. Touches efectivos: ninguno (solo bitácora).

RESULT: complete | F03-08-do-test-confundido-con-ablacion | needs_human, propuesta de reescritura §4.3/§12.1/T.3.6.2
