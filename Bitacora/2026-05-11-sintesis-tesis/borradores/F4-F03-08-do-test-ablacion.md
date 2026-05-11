---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 03-formalizacion/01-aparato-formal.md:91-101,256-258 ; 03-formalizacion/06-mapa-operadores-formales.md:138
hallazgo: Bitacora/2026-05-04-continuous-run/F03-08-do-test-confundido-con-ablacion.md
tipo: reemplazo_parrafo + reformulacion_tabla
---

## Diagnóstico

El cap 03-01 §4.3-4.4 admite aristas del grafo G como "robustas a `do(v_i)` pearliano" y §12.1 afirma que "EDI es operacionalización directa de un do-test". Esto importa la fuerza epistémica del do-calculus sin pagar el costo de sus supuestos identificadores. Pearl (2009, *Causality* 2.ª ed., p. 23) define `do(X=x)` como intervención exógena sobre el sistema real; la métrica EDI, en cambio, es **ablación interna del modelo acoplado** (apagar el término ODE→ABM en el simulador), no intervención sobre el sustrato físico. La equivalencia "EDI = do-test" sólo tiene tracción literal en el caso 30 VENLab (Fajen-Warren), donde hay manipulación experimental real; en los 29 casos observacionales restantes, la inferencia "ablación degrada → dependencia causal en el sistema real" exige supuestos identificadores (modularidad, fidelidad, no-confounders) que la tesis hoy no declara.

## Verificación

- `03-formalizacion/01-aparato-formal.md:91-101` (§4.3-4.4): aristas admisibles si "robustas a `do(v_i)`".
- `03-formalizacion/01-aparato-formal.md:256-258` (§12.1): "EDI es operacionalización directa de un do-test".
- `03-formalizacion/06-mapa-operadores-formales.md:138` Tabla 3.6.2 fila E: aristas como "dependencias detectadas que pasan do-test".
- Pearl, *Causality* (2009), cap. 3, p. 23: *"the action do(X = x) represents an experiment in which the variable X is set to value x by an outside intervention, while the rest of the model remains unchanged"* (verificable contra PDF local: `07-bibliografia/Pearl - Causality (2009).pdf`).

## Texto propuesto (voz autoral filosófica de Jacob)

**Reescribir `03-formalizacion/01-aparato-formal.md:91-97` (§4.3, criterio de admisión de aristas):**

> Una arista `(v_i, v_j) ∈ E` es admisible si:
> - es robusta a una intervención análoga al `do(v_i)` pearliano **cuando hay acceso experimental al sistema** (caso ancla VENLab);
> - en los casos observacionales (29/30 del corpus inter-dominio) la admisión se reduce a **ablación dentro del modelo híbrido** —apagar el término de acoplamiento ODE→ABM degrada la predicción— bajo supuestos identificadores explícitamente declarados en §12.1.
>
> La consistencia con ablación de modelo **no equivale** a la consistencia con `do` pearliano genuino: la primera es afirmación sobre la estructura del modelo que mejor predice; la segunda exige intervención sobre el sustrato.

**Reescribir `03-formalizacion/01-aparato-formal.md:256-258` (§12.1):**

> La métrica EDI **no es un `do`-test pearliano sobre el sistema real**, excepto en el caso ancla VENLab, donde el dispositivo experimental permite manipulación exógena directa de los obstáculos y la meta. En los 29 casos observacionales restantes del corpus inter-dominio, EDI es una **ablación de modelo**: se apaga el término de acoplamiento ODE→ABM dentro del simulador híbrido y se mide la degradación predictiva. La inferencia de un EDI alto a una dependencia causal en el sistema real exige supuestos identificadores adicionales que la tesis declara como costo: (i) **fidelidad** del simulador al sistema, (ii) **modularidad** del acoplamiento (apagar el término ODE no rompe otros mecanismos no modelados), (iii) **ausencia de confounders** no incluidos. Lo que EDI sí establece sin estos supuestos es que el término ODE **no es decorativo en el modelo**: si fuera decorativo, su ablación no degradaría la predicción. La inferencia más fuerte —que esa dependencia se preserva en el sustrato físico— exige justificación adicional caso a caso, y se declara como deuda residual del cap 03 cuando no es defendible.
>
> Pearl (2009, *Causality* 2.ª ed., p. 23) define `do(X=x)` como intervención exógena que deja "the rest of the model unchanged"; EDI realiza algo análogo dentro del modelo acoplado, no sobre el sustrato. La métrica preserva su fuerza epistémica como filtro contra términos decorativos y como evidencia indirecta de dependencia bajo supuestos declarados; pierde la fuerza causal directa que el rótulo "do-test" sugería.

**Reescribir Tabla 3.6.2 (`03-formalizacion/06-mapa-operadores-formales.md:138`):**

> | Campo | Especificación |
> |-------|----------------|
> | E (aristas) | dependencias detectadas que pasan `do`-test (VENLab) o ablación de modelo (corpus observacional) bajo supuestos identificadores declarados |
> | W (pesos) | covarianza condicional + sensibilidad a ablación del término ODE en el modelo híbrido |
> | Criterio de admisión | aristas robustas a intervención experimental cuando es accesible; en caso observacional, robustas a ablación bajo supuestos identificadores §12.1 |
> | Criterio de fallo | apagar v_i no cambia v_j en el modelo → arista decorativa, eliminar |

## Texto a reemplazar / propagar

- Modificar también `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md` y `03-formalizacion/07-plantilla-dossier-anclaje.md:45` (donde el dossier dice "dependencias detectadas que pasan do-test") para usar la formulación dual.
- Añadir en la sección de "Deuda residual" del cap 03 los tres supuestos identificadores (fidelidad, modularidad, no-confounders) con plan o reconocimiento de irreductibilidad por caso.

## Costo argumentativo declarado

La tesis pierde la fórmula vendible "EDI = do-test" y debe sostener una formulación más austera ("EDI = ablación de modelo + supuestos identificadores → indicador indirecto de dependencia causal"). Filosóficamente esto refuerza el realismo estructural moderado operativo del glosario: las aristas son afirmaciones sobre la estructura del modelo que mejor predice, no afirmaciones directas sobre la causalidad del sistema real. La tesis queda mejor blindada: ya no promete intervención pearliana donde no la hay.
