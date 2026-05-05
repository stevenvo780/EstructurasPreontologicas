# TENG-10 — baselines.py: target distinto del aparato ABM+ODE

**Fecha:** 2026-05-04
**Origen:** process-verifier engine 2026-05-05
**Archivo:** `09-simulaciones-edi/common/baselines.py:141` (`run_baselines_on_case`)
**Tipo:** Hallazgo metodológico (afecta toda comparación baseline↔aparato)

## (a) Verificación de la afirmación

**Afirmación:** baselines.py genera una serie sintética propia con
`_gen_series_with_coupling` (modelo AR simple) que es **distinto** del proceso
generador del aparato (ABM+ODE acoplado del caso); por tanto el `rmse_arima`
(y VAR/RW/GP) y el `rmse_coupled_aparato` que se comparan en el output **no
están definidos sobre el mismo vector observación**, y los ratios
`ratio_*_vs_coupled` son aritméticamente válidos pero **inferencialmente
nulos**.

**VERIFICADA.** Lectura literal del módulo:

- `baselines.py:48-67` — `_gen_series_with_coupling(forcing, params, seed)` es
  un AR1-acoplado simple `y_{t+1} = damping*y_t + alpha*(beta*forcing_t - y_t)
  + N(0,σ)`. No es el ABM+ODE del caso ni una sonda C1-C5; es un modelo
  generador propio del módulo de baselines.
- `baselines.py:166-170` — `forcing = _gen_forcing(...)`, `series =
  _gen_series_with_coupling(forcing, tparams, seed)`, `train = series[:k]`,
  `val = series[k:]`. **El target val al que se ajusta ARIMA/VAR/RW/GP es
  esta `series` sintética del propio módulo, no la observación real del
  caso.**
- `baselines.py:178-181` — `rmse_arima = rmse(arima["forecast"], val)`, etc.
  Todos los RMSE de baselines miden error contra `val ⊂ series` generado por
  `_gen_series_with_coupling`.
- `baselines.py:183-184` — `rmse_coupled = syn_phase["errors"]["rmse_abm"]`
  leído desde `outputs/metrics.json`, donde el `rmse_abm` fue calculado por
  el aparato (ABM+ODE acoplado) **contra la observación de ese caso** (sea
  data/ real o la fase synthetic propia del aparato), que es un vector
  distinto del `val` generado aquí.
- `baselines.py:204-208` — los ratios `rmse_arima / rmse_coupled` se reportan
  como veredicto comparativo y `_pick_winner` (línea 212) elige "ABM+ODE
  coupled" vs "ARIMA"/"VAR"/"RW"/"GP" usando RMSEs **definidos sobre vectores
  observación distintos**.

El docstring del módulo (líneas 4-7) admite que opera sobre la "fase
synthetic", pero la implementación **no recupera la serie val de la fase
synthetic del aparato** (no la lee de `outputs/`); en su lugar **regenera
una serie con un modelo distinto** parametrizado nominalmente igual. Aun
asumiendo que `_gen_series_with_coupling` aproximase el ABM+ODE, las
realizaciones estocásticas con seed=42 producen vectores distintos, y la
comparación de RMSE entre forecast→val_baselines vs aparato→val_aparato
no es métrica equivalente.

**Consecuencia operativa:** `winner = "ABM+ODE coupled"` reportado por
`_pick_winner` no implica superioridad predictiva del aparato sobre los
baselines: implica que el aparato tuvo menor RMSE contra **su** observación
y los baselines tuvieron RMSE contra **otra** observación. La afirmación
"el aparato aporta algo más que un modelo estadístico genérico" (docstring
línea 9-10) **no está sostenida por este pipeline**.

## (b) Propuesta de edición

La corrección de fondo requiere decisión metodológica de Jacob+Steven
(qué cuenta como observación común). Dejo dos rutas:

**Ruta 1 — Baselines sobre la observación real del caso (preferible).**
Para cada caso, `validate.py` ya emite (vía `array_dump.py`) un
`outputs/primary_arrays.json` con los vectores observación (`obs`) y
predicción del aparato (`pred_coupled`, `pred_no_ode`). `run_baselines_on_case`
debería:

1. Leer `obs` desde `outputs/primary_arrays.json` (no regenerar).
2. Particionar `obs` en `train`/`val` con la misma frontera que usó el
   aparato (también en `primary_arrays.json` o `metrics.json`).
3. Ajustar ARIMA/VAR/RW/GP sobre `train` y forecast a `val`.
4. Computar `rmse_arima = rmse(forecast, val_obs)`.
5. Recalcular `rmse_coupled_sobre_val_obs = rmse(pred_coupled[val_idx],
   val_obs)` (ya disponible o reproducible) y compararlo contra los
   baselines en el **mismo** vector.
6. Añadir al output `baselines_target: "primary_arrays.json:obs[val_idx]"`
   y `aparato_target: "<idem>"` para auditabilidad.

**Ruta 2 — Si `primary_arrays.json` no existe para todos los casos.**
Modificar `validate.py`/`hybrid_validator.py` para que la fase synthetic
emita `outputs/primary_arrays.json` con `obs_val`, `pred_coupled_val`,
`pred_no_ode_val`. Luego aplicar Ruta 1.

**Mientras tanto:** marcar en cualquier prosa del manuscrito que cite
`baselines/results.json` que los ratios `ratio_*_vs_coupled` son
**ilustrativos, no comparativos**, y NO usar `winner` como evidencia de
superioridad del aparato.

**Edición concreta sugerible (sin tocar metodología, sólo honestidad
documental) en `baselines.py`:**

- Renombrar campo de salida `winner` → `winner_caveat_distinct_targets`.
- Añadir campo `baselines_target: "synthetic_regenerated_in_baselines_module"`
  y `aparato_target: "metrics.json/synthetic/errors.rmse_abm (distinct
  realization)"`.
- Anteponer en docstring del módulo y de `run_baselines_on_case`: "ADVERTENCIA:
  esta función NO compara aparato vs baselines en el mismo vector observación.
  Para comparación válida ver Ruta 1 en TENG-10."

Esta edición documental puede hacerla la asistencia. La Ruta 1/2 (cambio
metodológico) **needs_human** porque modifica cómo se reporta el mérito
empírico del aparato — decisión de Jacob+Steven.

## (c) Costo argumentativo declarado

- Si la tesis ha invocado en algún capítulo "el aparato vence a ARIMA/VAR/RW/GP"
  apoyándose en `baselines.py`, esa afirmación **debe retirarse o reformularse
  como ilustrativa** hasta que se implemente Ruta 1/2.
- La métrica EDI propia (definida intra-aparato como `1 - RMSE_coupled/RMSE_no_ode`,
  CLAUDE.md §4) **no se ve afectada** por este hallazgo: ambos RMSE en la
  definición de EDI están sobre el mismo vector obs del caso. La afectada es
  exclusivamente la **comparación externa contra baselines estadísticos**.
- Costo de honestidad: declarar abiertamente que la comparación
  baseline↔aparato actual es metodológicamente vacía es debilitar una línea
  argumental secundaria, no la tesis principal. Ocultarlo sería F6 según
  CLAUDE.md §5 (afirmación sin sustento auditable).

## Estado

`needs_human` para Ruta 1/2 (decisión metodológica Jacob+Steven, B-T*).
La edición documental (renombre de campo + ADVERTENCIA en docstrings)
puede ejecutarla la asistencia previa autorización. No edita Tesis.md ni
metrics.json.

RESULT: complete | TENG-10-baselines-target-distinto-aparato | claim verificada; needs_human Ruta 1/2
