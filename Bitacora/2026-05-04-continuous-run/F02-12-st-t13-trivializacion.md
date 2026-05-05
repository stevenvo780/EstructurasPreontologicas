# F02-12 — ST T13 "neutraliza" Kim por modus tollens vacuo

**Estado:** `needs_human` (requiere firma filosófica de Jacob).
**Archivo afectado:** `02-fundamentos/05-temporalidad-y-causalidad.md`, §2.4.4, línea 116.
**Origen:** hallazgo de adversarial-reviewer cap02 (2026-05-05).

## (a) Verificación de la afirmación

Texto literal en línea 116:

> "La verificación formal de este argumento está en la suite ST T13 (hallazgo ST-3): la implicación `((C ∧ ¬V) ∧ (K → (V → S))) → ¬S` no es derivable directamente, pero el argumento de Kim queda **neutralizado por modus tollens vacuo** — si la constricción macro→micro es constitución (C) y no causación (¬V), entonces la premisa de Kim que requiere V es falsa de antemano, y la conclusión sobre sobredeterminación S no se sigue."

**El hallazgo adversarial es correcto y la objeción se sostiene en dos niveles:**

1. **Lógico.** "Modus tollens vacuo" no es un nombre estándar. Lo que el párrafo describe es **vacuous truth**: si `V` es falsa, entonces `V → S` es vacuamente verdadera y no permite inferir `S`. Pero eso **no neutraliza** el argumento de Kim; lo declara inaplicable porque se rechaza la premisa de la que parte. Vacuidad ≠ neutralización: una premisa rechazada deja al argumento sin tracción, no "neutralizado". El término "neutralizado" sugiere refutación interna del argumento; lo que ocurre es **evasión por rechazo de premisa**, que es legítimo pero distinto.

2. **Filosófico (más grave).** Rechazar `V` (la cláusula de causación macro→micro) y refugiarse en `C` (constitución) es exactamente la "salida constitutiva" que Kim 2005 (*Physicalism, or Something Near Enough*, cap. 2 "The Mind-Body Problem at the Turn of the Twenty-First Century" y cap. 3 "The Supervenience Argument") identifica como **vía al epifenomenismo**: si los rasgos macro no tienen poder causal propio (¬V), su realidad se vuelve metafísicamente ociosa respecto del cierre causal del nivel físico. Llamar a la macro-pauta "constitutiva" no le devuelve poder causal; le confiere status de pauta supervenente, que Kim diagnostica como epifenomenista *salvo* que se demuestre que la constitución hace trabajo causal independiente — lo que la tesis explícitamente niega en §2.4.3.

El párrafo, por tanto, **declara victoria contra Kim adoptando precisamente la posición que Kim diagnostica como derrota**. La suite ST T13 verifica una tautología trivial (toda implicación con antecedente falso es vacuamente verdadera), no un resultado sustantivo.

**Acceso a Kim 2005:** el PDF no está en `07-bibliografia/`. La tesis no puede citar Kim verbatim sin descargarlo. Esta es deuda bibliográfica adicional.

## (b) Propuesta de edición concreta

**No editable desde la asistencia.** Requiere reescritura filosófica de §2.4.4 + nueva sub-sección de respuesta a Kim 2005 cap. 2 sobre riesgo epifenomenista. Esquema sugerido para Jacob:

1. **Eliminar** la frase "queda neutralizado por modus tollens vacuo" y la apelación a la suite ST T13 como "verificación formal" del argumento contra Kim. La suite verifica vacuidad lógica, no fuerza filosófica.

2. **Reformular** §2.4.4 reconociendo que la salida constitutiva **no neutraliza** a Kim sino que **declina la disputa**: la tesis no defiende `V` (causación macro→micro robusta), defiende `C` (constitución detectable por manipulabilidad mutua). Eso desplaza la carga: la tesis debe ahora responder *por qué* la constitución no colapsa en epifenomenismo.

3. **Añadir respuesta explícita a Kim** en términos no-circulares. Tres opciones para Jacob:
   - **(i)** Asumir el costo epifenomenista parcial: aceptar que la macro-pauta no tiene poder causal *adicional* sobre el cierre físico, pero reivindicar su realidad como **patrón restrictivo detectable** (no como agente causal). El "trabajo" que hace la macro-pauta es **explicativo y predictivo** (vía EDI), no causal en sentido kim-fuerte.
   - **(ii)** Apelar a Craver/Bechtel: la manipulabilidad mutua es un test *sui generis* de relevancia constitutiva que Kim no contempla, y la dicotomía kim-vulnerable causación/epifenomenismo es **falsa dicotomía** porque ignora la categoría constitutiva.
   - **(iii)** Apelar a Hoel/Albantakis (causal emergence): el coarse-graining macro puede tener mayor *información efectiva* que el micro, y eso es trabajo causal medible aunque no satisfaga la noción reductiva de Kim.

4. **Declarar costo argumental:** cualquier salida constitutiva paga el precio de no afirmar "el macro hace algo que el micro no hace". La tesis debe declarar este costo en lugar de borrarlo con "neutralización".

5. **La suite ST T13** puede mantenerse como ilustración formal, pero relabeled: no "neutraliza Kim", sino "muestra que el argumento de Kim presupone V, premisa que la tesis no concede". Eso es **honestidad lógica**, no neutralización.

## (c) Costo argumentativo declarado

- La tesis pierde la pretensión de haber refutado a Kim.
- Gana, a cambio, una posición declaradamente más modesta: rechaza la premisa kim-vulnerable y asume el costo de defender constitución sin colapso epifenomenista por vía independiente (Craver, Hoel, o asunción del costo).
- La suite ST T13, como "verificación formal contra Kim", queda degradada: verifica vacuidad lógica (resultado trivial), no fuerza filosófica.
- Deuda bibliográfica: Kim 2005 cap. 2 y cap. 3 deben descargarse a `07-bibliografia/` y citarse verbatim antes de cerrar §2.4.4.

## Acceptance pendiente

- [ ] §2.4.4 reescrito sin "neutralizado" / "modus tollens vacuo".
- [ ] Respuesta explícita a Kim 2005 cap. 2 (epifenomenismo de la salida constitutiva).
- [ ] Kim 2005 PDF en `07-bibliografia/` con cita verbatim paginada.
- [ ] ST T13 redocumentada como "muestra inaplicabilidad por rechazo de premisa V", no como "neutralización".

Marca: `needs_human` (H-J*: decisión filosófica de Jacob entre las opciones (i)/(ii)/(iii) o combinación).
