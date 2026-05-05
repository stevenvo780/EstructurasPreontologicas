# F06-04 — Cinco escenarios falsables, ¿cuántos son genuinamente independientes?

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap04+06 (2026-05-05)
**Archivo señalado:** `06-cierre/01-conclusion-demostrativa.md`, §2 "Condiciones de fracaso global", líneas 83–107.

## (a) Verificación de la afirmación

**Afirmación adversarial:** los "5 escenarios falsables globales" no son cinco condiciones independientes; 4 son variaciones del mismo evento ("el corpus deja de discriminar") y el #5 (Wolfram absorbe la tesis) está blindado por el criterio interno definido en F04-02.

**Lectura literal de los cinco escenarios** (líneas 87–105):

| # | Etiqueta | Variable falsable | Criterio externo |
|---|----------|--------------------|-------------------|
| 1 | 4 casos `overall_pass` se desmoronan | distribución EDI de los 4 casos demostrativos | sí (re-ejecución bajo perfiles altos / superación por baselines) |
| 2 | Controles de falsación dejan de rechazarse | EDI de casos 06/07/08 | sí (re-ejecución) |
| 3 | Aparato no escala más allá de su dominio | EDI del caso 30 + candidatos no-macro | sí (refinamiento de sonda) |
| 4 | Asimetría L1↔B↔L3↔S no se sostiene | identificabilidad de B en algún dominio | parcial (depende de quién declara "no identificable") |
| 5 | Wolfram (u otro rival) absorbe la tesis | existencia de programa rival con arquitectura equivalente | **interno** (la tesis define qué cuenta como "absorción" — F04-02) |

**Hallazgo:** la afirmación adversarial es **parcialmente correcta**, no totalmente.

- Escenarios **1 y 2** son operativamente la misma condición desde el punto de vista del aparato: el EDI deja de separar señal de ruido en el corpus actual. Si los 4 demostrativos caen, o si los 3 controles suben, **el corpus deja de discriminar**. Son dos caras del mismo fallo de discriminación, con la misma métrica (EDI + p_perm) y el mismo comando regenerador (`./tesis run --case <NN>`). Declararlos como dos escenarios independientes infla el conteo sin agregar discriminación.
- Escenario **3** sí es independiente: pone a prueba la pretensión de **generalidad de escala**, no de discriminación. Un corpus que discrimina pero solo en macro-temporal cumple 1 y 2 pero falla 3.
- Escenario **4** es independiente en principio (es estructural-formal, no empírico-EDI), pero su criterio de fallo es ambiguo: "no se logra traducir L3 a B" depende de juicio del autor, no de un test público. Necesita afilarse o pasa a ser semi-blindado.
- Escenario **5** es el más problemático: su criterio de fallo ("rival reúne todas las piezas en arquitectura equivalente o superior") es **definible solo desde dentro del marco**. Wolfram comparte hipergrafos pero no comparte filtro empírico, dossier ni asimetría L1↔B↔L3↔S — y esos cinco criterios de comparación son los que la tesis misma elige (cap 04-01, fila Wolfram). Por construcción, ningún rival puede cumplirlos sin volverse la tesis. Esto es lo que Popper (1959, *Logic of Scientific Discovery* §6) llama **inmunización ad hoc por elección de criterio**: la tesis decide qué cuenta como "absorción" y luego declara que el rival no absorbe.

**Conclusión de la auditoría:** de los 5 escenarios, **3 son genuinamente independientes con criterio externo** (1+2 colapsados como "discriminación falla", 3 "escalabilidad falla", 4 "asimetría falla con criterio reforzado"). El #5 requiere reescritura para externalizar el criterio o ser declarado como **condición de prioridad histórica** (no de falsación).

## (b) Propuesta de edición concreta — `needs_human` (firma de Jacob)

La reescritura toca el núcleo retórico del cierre y debe firmarla Jacob. Borrador propuesto para considerar:

> ## 2. Condiciones de fracaso global
>
> La tesis falla globalmente bajo tres escenarios falsables empíricamente y una condición de prioridad histórica:
>
> ### Escenario 1. El corpus deja de discriminar
>
> Esta condición se manifiesta de dos formas operativamente equivalentes: (a) los 4 casos `overall_pass` no replican bajo perfiles de alto rendimiento o son superados por baselines puramente estadísticos; (b) los 3 controles de falsación (06, 07, 08) empiezan a producir EDI significativo. En cualquiera de las dos formas, el aparato pierde su capacidad discriminante y la tesis colapsa al instrumentalismo puro. Comando regenerador: `./tesis run --case <NN>` para los siete casos críticos (01, 16, 26, 28, 06, 07, 08).
>
> ### Escenario 2. El aparato no escala fuera de su dominio actual
>
> Si el caso 30 (behavioral dynamics) y otros candidatos en escalas no-macro-temporales no se elevan a demostrativo bajo el protocolo extendido, el dominio de validez de la tesis es regional. Criterio externo: refinamiento de sonda documentado y EDI con p_perm<0.05 en al menos dos dominios fuera de macro-temporal antes de 2027-12.
>
> ### Escenario 3. La asimetría L1↔B↔L3↔S no se sostiene
>
> Si en algún dominio relevante (definido públicamente como dominio incluido en el corpus inter-escala) no se logra traducir L3 a B porque B no es identificable bajo los datos disponibles, la tesis admite reducción de alcance. Criterio externo: dossier de anclaje rechazado por revisión externa en al menos un dominio.
>
> ### Condición de prioridad histórica (no falsación)
>
> Si un programa de investigación rival reúne, antes que esta tesis, anclaje empírico + asimetría protocolar + dossier + cartografía multidominio + falsación, esta tesis cede prioridad. **Esta condición no es propiamente falsable porque su criterio depende de la comparación con el aparato actual; se documenta como compromiso de honestidad histórica, no como test crítico.** Wolfram Physics Project no la satisface al 2026-05 (cap 04-01).

## (c) Costo argumentativo declarado

- **Costo retórico:** la tesis pasa de "5 escenarios falsables" a "3 escenarios falsables + 1 condición de prioridad". El número baja, la honestidad sube.
- **Costo conceptual:** se reconoce explícitamente que la cláusula Wolfram es asimétrica (la tesis define los criterios de comparación) y se reclasifica como compromiso de prioridad histórica, no como test de falsación. Esto **debilita la apariencia de robustez popperiana** pero **fortalece la coherencia metodológica**: Popper rechaza la inmunización por elección de criterio interno (1959, §6).
- **Costo defensivo:** un revisor podría argumentar que aún 3 escenarios siguen siendo "lo mismo" (todos dependen del aparato EDI). Respuesta: 1 testea discriminación, 2 testea generalidad de escala, 3 testea estructura formal. Son tests con métricas distintas (EDI vs identificabilidad de sonda vs identificabilidad de B). La independencia es operativa, no solo nominal.
- **Costo de cierre:** F04-02 (criterio público de absorción rival) debe revisarse en paralelo. Si esta tarea reescribe Wolfram como condición de prioridad histórica, F04-02 debe declarar explícitamente que la cláusula de absorción no es falsable en sentido popperiano fuerte.

## Estado

`needs_human` — firma de Jacob requerida para reescritura del §2 del cap 06-cierre.
Propuesta lista para revisión. NO se editó `Tesis.md` ni `06-cierre/01-conclusion-demostrativa.md`.

RESULT: complete | F06-04-cinco-escenarios-cuatro-iguales | 3 escenarios independientes + 1 condición de prioridad
