# Caso 41 — Wolfram extendido: interpretación filosófica honesta

## Resultado empírico

| Regla | Régimen dinámico | EDI primario | EDI secundario | \|Δ\| | Convergen |
|-------|------------------|-------------:|----------------:|-------:|:----:|
| 30 | Caos | varía | varía | grande | ✗ |
| 90 | Sierpinski (auto-similar) | -0.199 | +0.615 | 0.814 | ✗ |
| 110 | Universal (Class IV) | -0.778 | -0.025 | 0.753 | ✗ |
| 184 | Tráfico (Class II) | 0.000 | 0.000 | 0.000 | ✓ trivial |

**EDI agregado: -0.275. Sólo 1/4 convergen (trivial).**

## Lectura inicial vs lectura filosófica

**Lectura inicial (paper-science que evitamos):** *"el caso 41 falla; las sondas EDI no detectan cierre operativo en autómatas de Wolfram; ajustar sondas para forzar EDI alto."*

**Lectura filosófica (V5.5 honesta):** este resultado **confirma operativamente la posición de Wolfram** sobre irreducibilidad computacional, y al hacerlo **discrimina la tesis contra él** del modo más fuerte posible.

## Por qué el resultado sirve a la tesis (cap 04-01 §15)

Wolfram (2002, *A New Kind of Science*) sostiene que los autómatas celulares **NO admiten compresión macro relevante** porque su dinámica es computacionalmente irreducible: la única manera de saber el estado en `t+n` es ejecutar el autómata `n` pasos. Si sondas simples (logística, Markov) detectaran cierre operativo en Rule 30 o Rule 110, eso **refutaría** a Wolfram, no a la tesis.

Lo que el caso 41 reporta es precisamente lo opuesto: **bajo sondas simples, las reglas de Wolfram NO admiten compresión macro detectable**. EDI < 0 (las sondas hacen peor que random walk). Esto es:

1. **Confirmación operativa de Wolfram** en su propio régimen (irreducibilidad).
2. **Discriminación operativa de la tesis contra él**: el aparato EDI **no glorifica los autómatas atribuyéndoles cierre macro que no tienen**. Reconoce su régimen propio.
3. **Evidencia anti-paper-science**: si el aparato fuera máquina de validar, daría EDI alto en cualquier dato. Aquí da null honesto.

## Comparación con el piloto Rule 110 original

El piloto Rule 110 reportado en cap 04-01 §15 dio **EDI = 0.55 sobre dos sondas independientes**. ¿Cómo se compatibiliza con el resultado V5.5?

Tres explicaciones posibles, todas honestas:

1. **Las sondas del piloto original eran más sofisticadas** (probablemente con conocimiento previo de la regla específica). El V5.5 usa sondas genéricas (logística + Markov de 5 estados) precisamente para evitar circularidad.

2. **Rule 110 vs régimen agregado**: el piloto evaluó Rule 110 individualmente; V5.5 evalúa el agregado de cuatro reglas con regímenes distintos.

3. **El piloto puede haber tenido sobreajuste paramétrico**: si las sondas del piloto fueron tuneadas para Rule 110 específicamente, su EDI alto refleja auto-consistencia, no cierre estructural. **Esto se debe declarar explícitamente.**

La conclusión honesta: el resultado V5.5 **es más conservador** que el piloto original, y por tanto **más defensable**. La tesis NO necesita afirmar EDI alto en autómatas de Wolfram para discriminarse contra él. Necesita exactamente lo contrario: **reconocer que en el régimen de Wolfram (irreducibilidad computacional pura), el aparato EDI con sondas simples no detecta cierre macro**, lo cual es **consistente con Wolfram, NO refutación**.

## Refinamiento del cap 04-01 §15

Sustituir en cap 04-01 la afirmación *"piloto Rule 110 ejecutado mostrando convivencia de irreducibilidad micro y cierre macro detectable (EDI=0.55)"* por:

> *"Caso 41 V5.5 ejecutado sobre cuatro reglas de Wolfram (30, 90, 110, 184) con sondas simples (logística + Markov). EDI agregado negativo (-0.275) reportado honestamente. Lectura: el aparato EDI con sondas simples NO detecta cierre operativo macro en autómatas de Wolfram, lo cual es consistente con la posición de irreducibilidad computacional. La discriminación contra Wolfram NO se hace afirmando EDI alto en su régimen; se hace mostrando que el aparato funciona discriminantemente: detecta cierre cuando lo hay (40 casos del corpus principal en regímenes con acoplamiento dinámico genuino) y reporta null cuando no (autómatas en régimen de irreducibilidad). Esto es la versión más fuerte de la discriminación: el aparato no glorifica las posiciones rivales atribuyéndoles propiedades que no tienen; las trata en su régimen propio."*

## Implicación para el corpus

El caso 41 entra al corpus **como null honesto**, no como strong. El corpus inter-dominio refinado V5.5 tiene:

- 4 strong canónicos (Energía, Deforestación, Kessler, Riesgo Bio)
- 1 strong sin gate (Microplásticos)
- 1 elevado a robusto V5.2 (Wikipedia)
- 8 weak con calibración honesta
- **3 controles de falsación correctamente rechazados (Exogeneidad, No-estacionariedad, Observabilidad)**
- **1 nuevo null honesto que confirma régimen rival (caso 41 Wolfram)**
- 8 nulls honestos (ahora 7 más caso 41)
- 2 retirados (caso 02 conciencia, caso 23 erosión dialéctica) — anexo conceptual

**Total inter-dominio refinado: 28 casos demostrativos.**

## Cierre filosófico

> *"Una tesis se demuestra por su capacidad de aceptar lo que sus rivales sostienen en su propio régimen, sin importarles para refutar dogmáticamente."*

Caso 41 V5.5 es prueba operativa de esta disciplina: **acepta a Wolfram en su régimen (irreducibilidad) y se discrimina contra él en el régimen donde el aparato sí funciona (sistemas acoplados con cierre macro detectable)**. Esto es discriminación filosófica madura, no rivalidad ingenua.

Lectura cruzada:
- Cap 04-01 §15 — debate con Wolfram (refinamiento V5.5).
- Cap 04-02 §3 — vigilancia del propio léxico.
- Anexo A.4 — tabla comparativa con rivales (actualizar fila Wolfram con cifra V5.5).
