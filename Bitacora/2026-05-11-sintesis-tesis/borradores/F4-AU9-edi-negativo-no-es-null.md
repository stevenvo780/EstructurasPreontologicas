---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 06-cierre/04-versiones-cortas-defensa.md:110 ; 06-cierre/01-conclusion-demostrativa.md:60 ; 05-aplicaciones/07-mapa-aplicaciones-corpus.md:33
hallazgo: Bitacora/2026-05-04-continuous-run/AU-9-edi-negativo-no-es-null.md
tipo: subdivision_categoria + reformulacion_tabla
---

## Diagnóstico

El bloque "8 null" del corpus inter-dominio colapsa tres regímenes empíricamente distintos bajo una sola etiqueta: (i) nulls genuinos con `|EDI|<0.05`; (ii) un caso de EDI negativo moderado donde el modelo acoplado predice **peor** que el reducido (caso 12 Paradigmas, `EDI=-0.144`); (iii) dos casos con `EDI>0` y permutación significativa pero `valid=False` por incumplimiento de C1-C5 (casos 03 Contaminación y 17 Océanos). Englobar los tres regímenes en "null" oculta información discriminante y es exactamente el patrón "categoría que hace que el conteo encaje" prohibido por CLAUDE.md §1. La cifra adversarial "EDI ≤ -0.876" del reporte original no se reproduce: corresponde a los controles 07/08 (correctamente clasificados), no a los nulls.

## Verificación contra fuente primaria

Lectura directa de `phases.{synthetic|real}.edi.value` y `permutation_significant`/`valid` en cada `metrics.json`:

| Caso | EDI | p_perm | valid | Categoría declarada hoy | Sub-régimen propuesto |
|---|---:|---:|:-:|---|---|
| 02 Conciencia | -0.007 | 0.867 | False | Null | Null genuino |
| 03 Contaminación | +0.227 | 0.000 | False | Null | Señal rechazada por gate C1-C5 |
| 12 Paradigmas | -0.144 | 0.787 | False | Null | EDI negativo: sonda macro inadecuada |
| 17 Océanos | +0.149 | 0.000 | False | Null | Señal rechazada por gate C1-C5 |
| 19 Acidificación | +4.3e-5 | 0.001 | False | Null | Null genuino (también afectado por TENG-05) |
| 23 Erosión | -0.019 | 0.975 | False | Null | Null genuino |
| 25 Acuíferos | -0.022 | 0.270 | False | Null | Null genuino |
| 29 IoT | -0.010 | 0.992 | False | Null | Null genuino |

## Texto propuesto (voz autoral filosófica de Jacob)

**Reemplazar la fila única "Null | 8" por tres filas operativamente distinguibles** en las tablas afectadas (`06-cierre/04-versiones-cortas-defensa.md:110`, `06-cierre/01-conclusion-demostrativa.md:60`, `05-aplicaciones/07-mapa-aplicaciones-corpus.md:33`):

> | Sub-régimen | N | Casos | Criterio operativo |
> |---|--:|---|---|
> | Null genuino | 5 | 02, 19, 23, 25, 29 | `|EDI| < 0.05` y `permutation_significant=False` |
> | EDI negativo (sonda macro inadecuada) | 1 | 12 Paradigmas | `EDI ≤ -0.10`: el ABM solo predice mejor que el ABM acoplado al ODE; la sonda macro elegida es activamente inadecuada |
> | Señal rechazada por gate C1-C5 | 2 | 03 Contaminación, 17 Océanos | `EDI > 0` con `p_perm < 0.05` pero `valid=False`: el ranking permutacional cruza el umbral pero la batería compuesta C1-C5 rechaza la admisión |

Y, en prosa, declarar el costo:

> **Costo declarado de la subdivisión.** Lo que el manuscrito presentaba como "8 null" cubre en realidad tres regímenes de no-éxito empíricamente distintos. Los 5 nulls genuinos son el resultado esperado de un aparato que no inventa señal donde no la hay. El caso 12 es más informativo: el ABM acoplado al ODE de paradigmas predice **peor** que el ABM reducido — lo que la tesis lee, honestamente, como prueba de que la sonda macro elegida es **activamente inadecuada** para el dominio histórico-discursivo de los paradigmas científicos (no como prueba de que no haya acoplamiento, sino como prueba de que la sonda no captura el acoplamiento real). Los casos 03 y 17 son del tercer tipo: la dinámica acoplada produce ranking significativo bajo permutación, pero la batería C1-C5 detecta inconsistencias internas (viscosidad, persistencia, no-localidad) que impiden admitir la señal. Esto no es un fracaso del aparato; es la batería operando como filtro adicional al p-valor, exactamente como su diseño requiere. Aceptar la subdivisión refuerza el reclamo de que el aparato discrimina tres modos de no-éxito en lugar de colapsarlos en una etiqueta única; la cifra agregada "señal / no-señal ≈ 50 %" del manuscrito gana matiz y pierde rotundidad.

## Texto a reemplazar

- Borrar la fila única "Null | 8" en los tres loci.
- Recalcular cualquier conteo agregado que dependa de "8 null" (por ejemplo "50 % señal" en cap 06 o en defensas cortas).
- Actualizar el glosario operativo (`00-proyecto/07-glosario-operativo.md`) añadiendo las tres sub-categorías como entradas.

## Acción técnica derivada (B-T)

Para caso 12 (Paradigmas, EDI=-0.144): documentar en `case_config.json` por qué la sonda macro actual es inadecuada y proponer sonda alternativa o reclasificación a "fuera de dominio del aparato".
