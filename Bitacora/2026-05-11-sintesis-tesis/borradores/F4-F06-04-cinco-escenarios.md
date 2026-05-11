---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 06-cierre/01-conclusion-demostrativa.md:83-107 (§2 Condiciones de fracaso global)
hallazgo: Bitacora/2026-05-04-continuous-run/F06-04-cinco-escenarios-cuatro-iguales.md
tipo: reemplazo_seccion
---

## Diagnóstico

`06-cierre/01-conclusion-demostrativa.md:83-107` enumera "5 escenarios falsables globales" que la auditoría muestra que **no son cinco condiciones independientes**: los escenarios 1 ("los 4 `overall_pass` se desmoronan") y 2 ("los controles de falsación dejan de rechazarse") son operativamente la misma condición — el corpus deja de discriminar entre señal y ruido — con la misma métrica (EDI + permutación) y los mismos comandos regeneradores. El escenario 5 ("Wolfram absorbe la tesis") tiene criterio de absorción **definido desde dentro del marco** (los 5 criterios de comparación con Wolfram los elige la propia tesis en cap 04-01), por lo que es semi-blindado y reúne las condiciones de inmunización ad hoc por elección de criterio interno (Popper 1959, *LSD* §6). De los 5 escenarios sobreviven **3 falsables empíricamente con criterio externo** + **1 condición de prioridad histórica** (no test crítico).

## Verificación

Las líneas 83-105 listan los cinco escenarios. La verificación detallada del solapamiento entre #1 y #2 (misma métrica, mismo comando regenerador) y del cierre interno del #5 (criterios de comparación con Wolfram diseñados por la tesis) está en F06-04 §A del informe origen. Popper 1959, *LSD* §6 sobre inmunización por elección de criterio interno: PDF presente en `07-bibliografia/Karl Popper - Logica De La Investigacion Cientifica.pdf` y `popper, karl - logica de la investigacion cientifica.pdf` (paginación pendiente de verificación contra edición disponible — B-T:verify-popper-lsd-§6).

## Texto propuesto (voz autoral filosófica de Jacob)

**Reemplazar `06-cierre/01-conclusion-demostrativa.md:83-107` (§2) por:**

> ## 2. Condiciones de fracaso global
>
> La tesis falla globalmente bajo **tres escenarios falsables con criterio externo** y **una condición de prioridad histórica** (no test crítico). Esta enumeración corrige una versión previa que listaba cinco escenarios; la auditoría detallada (F06-04) mostró que los escenarios 1 y 2 anteriores eran operativamente la misma condición y que el escenario 5 (absorción por rival) tenía criterio definido desde dentro del marco — lo que Popper (1959, *LSD* §6 — paginación pendiente de verificación) llama inmunización ad hoc por elección de criterio interno.
>
> ### Escenario 1. El corpus deja de discriminar entre señal y ruido
>
> Esta condición se manifiesta de dos formas operativamente equivalentes:
> (a) los 4 casos `overall_pass` (04 Energía, 16 Deforestación, 20 Kessler, 27 Riesgo Biológico) no replican bajo perfiles de alto rendimiento `HYPER_N_PERM=2999 HYPER_N_BOOT=1500` o son superados por baselines puramente estadísticos cuando éstos se computan sobre el mismo vector observación (cf. F4-AU3 y TENG-10);
> (b) los 3 controles de falsación (06, 07, 08) empiezan a producir EDI significativo bajo el mismo perfil.
> En cualquiera de las dos formas, el aparato pierde su capacidad discriminante y la tesis colapsa al instrumentalismo puro. Comando regenerador para los siete casos críticos: `./tesis run --case <NN>` para `NN ∈ {04, 16, 20, 27, 06, 07, 08}`.
>
> ### Escenario 2. El aparato no escala fuera de su dominio actual
>
> Si el caso 30 (behavioral dynamics) y otros candidatos en escalas no-macro-temporales no se elevan a demostrativo bajo el protocolo extendido —incluyendo (i) re-evaluación con sonda alternativa estructuralmente distinta (Neural ODE o GP) que controle la circularidad parcial detectada por F03-10 y (ii) pre-registro fechado de la sonda anterior a la ejecución— el dominio de validez de la tesis es regional, no general. Criterio externo: refinamiento de sonda documentado y EDI con `p_perm < 0.05` y CI bootstrap excluyendo cero en al menos dos dominios fuera de macro-temporal antes de 2027-12.
>
> ### Escenario 3. La asimetría L1↔B↔L3↔S no se sostiene
>
> Si en algún dominio relevante (definido públicamente como dominio incluido en el corpus inter-escala) no se logra traducir L3 a B porque B no es identificable bajo los datos disponibles —y la traducción exige medición independiente del ajuste a L3, no sólo motivación nominal del parámetro (cf. F03-04)— la tesis admite reducción de alcance. Criterio externo: dossier de anclaje rechazado por revisión externa en al menos un dominio del corpus.
>
> ### Condición de prioridad histórica (no falsación)
>
> Si un programa de investigación rival reúne, antes que esta tesis, anclaje empírico + asimetría protocolar + dossier + cartografía multidominio + falsación, esta tesis cede prioridad histórica. **Esta condición no es propiamente falsable** porque su criterio de absorción depende de la comparación con el aparato actual (los criterios de comparación los elige la tesis en cap 04-01 y cap 04-03); se documenta como **compromiso de honestidad histórica**, no como test crítico. Wolfram Physics Project no la satisface al 2026-05 — comparte hipergrafos pero no filtro empírico, dossier ni asimetría protocolar. La cláusula F04-02 sobre criterios externos (G parsimonia Quine, H novel facts Popper-Lakatos, I independencia del evaluador Bunge) actúa como complemento de honestidad: la tesis se reconoce como vulnerable bajo H (0 predicciones novedosas pre-registradas) y bajo I (sin revisión externa formal al cierre actual).
>
> Cada escenario es **falsable, fechado y con criterio externo público**; la condición de prioridad es **trazable, fechada y honesta**, pero no se reclama como test popperiano fuerte. La tesis prefiere declarar la asimetría a esconderla bajo un quinto "escenario falsable" que su propio criterio de absorción no autoriza.

## Texto a reemplazar

- Sección §2 completa (líneas 83-107).
- En cap 04-01 y 04-03 (cláusulas sobre Wolfram), revisar coherencia: la reclasificación como "condición de prioridad histórica" obliga a ajustar la presentación del rival Wolfram (no es "rival al que la tesis vence", es "programa con el que la tesis convive bajo asimetría declarada"). Cf. F04-06 (no procesado aún en este lote por DEUDA RESIDUAL clasificación).
- Lectura cruzada con F4-F04-02 (criterios externos G-I, donde la tesis muestra ✗) y F4-F04-11 (progresividad lakatosiana como deuda).

## Costo argumentativo declarado

- **Costo retórico.** La tesis pasa de "5 escenarios falsables" a "3 escenarios falsables + 1 condición de prioridad". El número baja, la honestidad sube.
- **Costo conceptual.** Se reconoce explícitamente que la cláusula Wolfram es asimétrica (la tesis define los criterios de comparación) y se reclasifica como compromiso de prioridad histórica, no como test de falsación. Esto debilita la apariencia de robustez popperiana y fortalece la coherencia metodológica: Popper rechaza la inmunización por elección de criterio interno.
- **Costo defensivo.** Un revisor podría argumentar que aún los 3 escenarios dependen del aparato EDI. Respuesta: cada escenario testea un eje distinto (discriminación, generalidad de escala, estructura formal de la asimetría) con métricas distintas (EDI vs identificabilidad de sonda alternativa vs identificabilidad de B). La independencia es operativa, no sólo nominal.
- **Costo de cierre.** La cláusula de honestidad histórica conecta con F4-F04-02 (criterios externos G-I): la tesis se declara vulnerable bajo H e I al cierre actual, con plan de mitigación post-defensa (pre-registro de predicciones novedosas; sometimiento a revisión externa).
