---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 05-aplicaciones/07-mapa-aplicaciones-corpus.md:109,125 ; 06-cierre/04-versiones-cortas-defensa.md:110
hallazgo: Bitacora/2026-05-04-continuous-run/AU-4-significance-theater-21-22.md
tipo: reformulacion_tabla + reclasificacion
---

## Diagnóstico

Casos 21 (Salinización) y 22 (Fósforo) figuran en bloques "Suggestive" y "Weak" del corpus inter-dominio con `p_perm` significativo, pero sus CI bootstrap 95 % cruzan el cero y, en el caso 21, la magnitud del EDI (0.018) es trivial: la reducción de RMSE asociada al acoplamiento ODE→ABM es del orden del 0.6 %. Esto reúne las dos componentes canónicas del *significance theater* (Wasserstein & Lazar 2016, *The American Statistician* 70(2): 129–133): p-valor que cruza el umbral con magnitud práctica irrelevante y CI que no excluye el cero.

## Verificación contra fuente primaria

`09-simulaciones-edi/21_caso_salinizacion/outputs/metrics.json` (phases.real):

```
edi.value                 = 0.0184
edi.permutation_pvalue    = 0.0028
edi.bootstrap_mean        = 0.0142
edi.ci_lo, edi.ci_hi      = -0.0771, +0.0825
```

`09-simulaciones-edi/22_caso_fosforo/outputs/metrics.json` (phases.real):

```
edi.value                 = 0.1924
edi.permutation_pvalue    = 0.0000
edi.bootstrap_mean        = 0.1989
edi.ci_lo, edi.ci_hi      = -0.2214, +0.5502
```

Cita Wasserstein-Lazar 2016 p.131 (Principle 3): *"Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold."*

**Nota bibliográfica:** PDF de Wasserstein & Lazar 2016 **no está en `07-bibliografia/`**. Si Jacob acepta inscribir la cita, debe abrirse `/fetch-biblio Wasserstein Lazar 2016 ASA p-values`. Hasta entonces la cita queda como **referencia secundaria declarada**; el argumento operativo (CI cruza cero + magnitud trivial → significance theater) no depende de la cita literal.

## Texto propuesto (voz autoral filosófica de Jacob)

**Añadir columna "CI 95 %" a Tablas 5.7.5 (Weak) y 5.7.6 (Suggestive) en `05-aplicaciones/07-mapa-aplicaciones-corpus.md`** y reescribir las filas 21 y 22:

> Caso 22 (Fósforo, Tabla 5.7.5): `EDI = 0.192`, `p_perm = 0.000`, `CI 95 % = [-0.221, +0.550]`. Comentario: el ranking del estadístico observado es alto bajo permutación pero el bootstrap no excluye cero ni magnitudes opuestas; la magnitud es frágil. Se mantiene en "weak" sólo bajo la convención de que el ranking permutacional es criterio admisorio, declarando que el bootstrap no lo respalda.
>
> Caso 21 (Salinización, originalmente en Tabla 5.7.6 Suggestive): `EDI = 0.018`, `p_perm = 0.003`, `CI 95 % = [-0.077, +0.083]`. La magnitud puntual es del orden del 0.6 % de reducción de RMSE; el CI no excluye que el acoplamiento empeore la predicción. **Se reclasifica fuera de "suggestive"** y se reporta en un bloque nuevo "significativos por permutación con magnitud trivial — no contabilizan a favor de la tesis". La tesis declara aquí, como costo, que la coexistencia de `p<0.01` con magnitud trivial y CI cruzando cero no debe contar como evidencia positiva: es exactamente el patrón que Wasserstein y Lazar (2016, p. 131) advierten al recordar que "scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold" (referencia secundaria; pendiente de verificación contra el PDF original, ver tarea B-T:fetch-wasserstein-lazar-2016).

## Texto a reemplazar / modificar

- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:109` (caso 22 en Weak): añadir columna CI; mantener clasificación con nota de fragilidad.
- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:125` (caso 21 en Suggestive): retirar de Suggestive Nivel 2 y mover al bloque nuevo.
- `06-cierre/04-versiones-cortas-defensa.md:110`: el conteo "2 suggestive: Finanzas, Salinización" baja a "1 suggestive: Finanzas" (queda por verificar si Finanzas tiene el mismo problema; auditoría sugerida).

## Costo argumentativo declarado

El conteo del balance "señal / no señal" se debilita marginalmente, pero la regla "CI 95 % que no cruza cero" como criterio adicional a la permutación blinda al manuscrito frente a una crítica adversarial estándar. Esto exige una auditoría retrospectiva de los demás casos contabilizados como significativos: cualquier caso con `p<0.05` y `ci_lo<0` debe quedar señalado o reclasificado. Esa auditoría queda como deuda residual fechada del cap 03-formalización §6 (criterios de admisión).
