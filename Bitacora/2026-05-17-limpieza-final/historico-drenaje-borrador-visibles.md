# Drenaje de marcadores [BORRADOR-IA] visibles — abstract y conclusión

Fecha: 2026-05-24
Operador: orquestador (Claude Opus 4.7) bajo dirección humana.

## Motivación

Para lector externo (Ricardo, revisor académico no co-autor), los marcadores `[BORRADOR-IA]` inline en abstract y conclusión final son ruido visual. La información que comunican ("Jacob debe firmar H-J*") sigue listada en `TAREAS_PENDIENTES.md` y en el bloque global del inicio de `06-cierre/01-conclusion-demostrativa.md` (preservado intacto). Eliminar los marcadores inline no cierra ninguna H-J*.

## Inventario antes (6 marcadores visibles)

1. `00-proyecto/05-resumen-y-abstract.md:31` — `[BORRADOR-IA — pendiente firma autoral H-J5/H-J6/H-J7]`
2. `06-cierre/01-conclusion-demostrativa.md:3` — bloque global "Decisiones autorales pendientes" (**SE PRESERVA**, no se toca)
3. `06-cierre/01-conclusion-demostrativa.md:47` (Condición 4) — `[BORRADOR-IA pendiente firma H-J3]`
4. `06-cierre/01-conclusion-demostrativa.md:75` (Condición 5) — `[BORRADOR-IA pendiente firma H-J5/H-J6/H-J7/H-J12]`
5. `06-cierre/01-conclusion-demostrativa.md:151` (§3.6 baselines) — `[BORRADOR-IA pendiente firma H-J9]`
6. `06-cierre/01-conclusion-demostrativa.md:236` (§5.6 aporte filosófico) — `[BORRADOR-IA pendiente firma H-J5]`

## Snapshots originales (texto exacto antes del drenaje)

### 1. Abstract línea 31

```
> `[BORRADOR-IA — pendiente firma autoral H-J5/H-J6/H-J7]` Reformulación limpia bajo CLAUDE.md §1. Detalle de reclasificaciones por caso en `06-cierre/01-cierre-doctoral.md` §1, §4.5, §5; histórico de versiones previas archivado en `Bitacora/`.
```

### 3. Conclusión línea 47 (Condición 4)

```
**Test de fallo**: si algún parámetro no se traduce a B, hay formalismo desanclado. **Verificación sostenida en sentido pragmático; deuda metodológica declarada para verificación ontológica fuerte (cap 03-04 §Patología 3)**. La verificación actual establece **correspondencia nominal con magnitudes empíricas, no medición independiente de cada parámetro fuera del ajuste**: en los casos con gate completo, ode_alpha/ode_beta y demás parámetros L3 se calibran sobre los mismos datos que los validan, por lo que el dossier sostiene una traducción nominal motivada en B pero no una medición externa al ajuste. La elevación a "verificación sostenida fuerte" requiere medición independiente vía intervención experimental sobre cada parámetro (no calibración sobre el mismo split), conforme al criterio (iii) de la Patología 3 del cap 03-04. `[BORRADOR-IA pendiente firma H-J3]`
```

### 4. Conclusión línea 75 (Condición 5)

```
**Test de fallo**: si los casos que pasan gate completo + block-perm + pre-registro genuino no replican o son superados por modelos rivales bajo el mismo protocolo, la cartografía multidominio pierde su demostración. **Verificación sostenida** en el sentido procesal declarado (defensa por proceso, no por acumulación); deuda B-T2.1 sobre 30 casos en §4. `[BORRADOR-IA pendiente firma H-J5/H-J6/H-J7/H-J12]`
```

### 5. Conclusión línea 151 (§3.6)

```
**Costo argumental asumido.** Deforestación y Riesgo Biológico se reclasifican como casos donde el aparato detecta acoplamiento estructural significativo pero **no exhibe ganancia predictiva frente a modelos estadísticos lineales** bajo la ventana de validación disponible. Esto es **reducción de alcance, no derrota**: la tesis defiende que el acoplamiento ODE→ABM es estructuralmente identificable (sostenido por EDI vs `abm_no_ode`), no que el aparato sea el mejor predictor posible (no sostenido uniformemente). `[BORRADOR-IA pendiente firma H-J9]`
```

### 6. Conclusión línea 236 (§5.6)

```
Establece el **irrealismo operativo** como **operativización del realismo de patrones dennetteano (Dennett 1991) con protocolo de admisión refutable** (dossier de 14 componentes, protocolo C1-C5, métrica EDI por intervención ablativa, gate hostile-tested, pre-registro firmado *ex ante*). El aporte original no es la posición ontológica (compartida con Dennett 1991) sino el aparato de admisión que la operacionaliza públicamente. La distinción entre κ-pragmática y κ-ontológica (véase capítulo 1) es crítica: el manuscrito demuestra κ-pragmática con rigor; la afirmación κ-ontológica fuerte requiere convergencia bajo múltiples sondas y validación inter-grupo. `[BORRADOR-IA pendiente firma H-J5]`
```

## Acción aplicada

- Marcadores 1, 3, 4, 5, 6 → **eliminados inline**. Contenido sustantivo intacto. Las H-J* siguen abiertas en `TAREAS_PENDIENTES.md` y en el bloque global de la conclusión.
- Marcador 2 (bloque global "Decisiones autorales pendientes" línea 3) → **preservado**, es informativo para uso interno.
- En el abstract: el bloque blockquote completo se elimina porque la información ("reformulación limpia bajo CLAUDE.md §1, detalle en cap 06-01") es meta-comentario editorial sin valor para revisor externo; reclasificaciones por caso quedan documentadas en cap 06-01 §3.6 y §4.

## Inventario después

- Abstract: 0 marcadores visibles.
- Conclusión demostrativa: 1 marcador (bloque global línea 3, preservado).
- Total drenado: 5 marcadores inline.

## Garantías

- No se cierran H-J*. Siguen pendientes en `TAREAS_PENDIENTES.md`.
- Contenido filosófico sustantivo intacto: solo se retiran sufijos meta-editoriales.
- Voz autoral de Jacob preservada (no se reescribe argumento, solo se retira marca técnica).
