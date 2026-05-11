---
borrador: IA
requires: H-J* + B-T
propuesta_fecha: 2026-05-11
destino: prosa que cite baselines/results.json en cualquier capítulo + 09-simulaciones-edi/common/baselines.py (docstring + campos de output)
hallazgo: Bitacora/2026-05-04-continuous-run/TENG-10-baselines-target-distinto-aparato.md
tipo: edicion_documental_baselines + tarea_B-T_alinear_target
---

## Diagnóstico

`09-simulaciones-edi/common/baselines.py:48-208` ajusta ARIMA/VAR/RW/GP sobre una serie sintética **propia** generada por `_gen_series_with_coupling` (modelo AR1 simple), distinta del proceso generador del aparato (ABM+ODE acoplado del caso). El `rmse_arima` y el `rmse_coupled` que se comparan en el output están definidos sobre **vectores observación distintos**: el primero sobre `val ⊂ series` generada en el módulo de baselines; el segundo sobre el `obs_val` del caso leído desde `metrics.json`. Los ratios `ratio_*_vs_coupled` son aritméticamente válidos pero **inferencialmente nulos**: `_pick_winner` no compara aparato vs baselines en el mismo target. La métrica EDI propia **no se ve afectada** (RMSE_coupled y RMSE_no_ode están sobre el mismo `obs_val` por definición); lo afectado es exclusivamente la comparación externa contra baselines estadísticos.

Esto agrava el hallazgo AU-3 (baselines ARIMA/VAR superan al modelo en 2/4 casos `overall_pass`): la victoria de los baselines en Deforestación y Riesgo Biológico se computa **sobre el target real del aparato** (cuando F3-AU3 reportó el comparativo correcto), no sobre la serie sintética del módulo. Es decir, AU-3 ya usa la comparación correcta; lo que TENG-10 expone es que el `winner` reportado por `baselines.py` en su pipeline canónico **no es esa comparación**, sino otra cuya inferencia es nula.

## Verificación contra código

- `baselines.py:48-67` (`_gen_series_with_coupling`): AR1-acoplado simple distinto de ABM+ODE.
- `baselines.py:166-170`: `series = _gen_series_with_coupling(...); train, val = series[:k], series[k:]` — target de baselines es esta serie sintética propia.
- `baselines.py:178-181`: `rmse_arima = rmse(arima["forecast"], val)` — error contra serie sintética propia.
- `baselines.py:183-184`: `rmse_coupled = syn_phase["errors"]["rmse_abm"]` — leído desde `metrics.json`, calculado sobre **otra** observación.
- `baselines.py:204-212`: ratios y `_pick_winner` operan sobre RMSEs definidos sobre vectores distintos.

## Texto propuesto (voz autoral filosófica de Jacob)

**Edición documental en `09-simulaciones-edi/common/baselines.py` (sin tocar metodología; ejecutable por asistencia):**

- Renombrar campo de salida `winner` → `winner_caveat_distinct_targets` o añadir campo `comparison_target_consistency: false`.
- Añadir campos `baselines_target: "synthetic_regenerated_in_baselines_module"` y `aparato_target: "metrics.json/synthetic/errors.rmse_abm (distinct realization)"`.
- Anteponer en docstring del módulo y de `run_baselines_on_case`:
  > **ADVERTENCIA.** Esta función **NO compara aparato vs baselines sobre el mismo vector observación**. Los `rmse_arima`, `rmse_var`, `rmse_rw`, `rmse_gp` están definidos sobre una serie sintética propia generada por `_gen_series_with_coupling`; el `rmse_coupled` se lee desde `metrics.json` y está definido sobre la observación del caso. Los ratios `ratio_*_vs_coupled` son aritméticamente válidos pero **inferencialmente nulos**. Para comparación válida ver ruta TENG-10 (baselines sobre `primary_arrays.json:obs[val_idx]`).

**Edición en cualquier prosa del manuscrito que cite `baselines/results.json`:**

- Reformular como "ilustrativos, no comparativos".
- **No usar el campo `winner` como evidencia de superioridad del aparato.**
- Mantener AU-3 como referencia: la comparación válida (RMSE del aparato vs RMSE de ARIMA/VAR sobre el mismo target) ya está reportada en `F3-AU3` y en `09-simulaciones-edi/baselines/baselines_report.md`; es esa la que la tesis cita como hallazgo honesto, no `winner` de `baselines.py`.

## Acciones técnicas derivadas (B-T)

- **Ruta 1 — Baselines sobre la observación real (preferible).** Modificar `run_baselines_on_case` para leer `obs` desde `outputs/primary_arrays.json` (ya emitido por `array_dump.py`), particionar `train`/`val` con la frontera del aparato, ajustar ARIMA/VAR/RW/GP sobre `train` y forecast a `val`, computar `rmse_arima = rmse(forecast, val_obs)` y `rmse_coupled = rmse(pred_coupled[val_idx], val_obs)`. Añadir `baselines_target: "primary_arrays.json:obs[val_idx]"` y `aparato_target` igual para auditabilidad.
- **Ruta 2 — Si `primary_arrays.json` no existe en todos los casos.** Modificar `validate.py/hybrid_validator.py` para que la fase synthetic emita `outputs/primary_arrays.json` con `obs_val`, `pred_coupled_val`, `pred_no_ode_val`. Luego aplicar Ruta 1.

## Costo argumentativo declarado

- Si la tesis ha invocado en algún capítulo "el aparato vence a ARIMA/VAR/RW/GP" apoyándose en el campo `winner` de `baselines.py`, esa afirmación debe retirarse o reformularse como ilustrativa hasta que se implemente Ruta 1.
- La métrica EDI propia no se ve afectada: ambos RMSE en su definición están sobre el mismo `obs_val` por construcción.
- La comparación de F3-AU3 (que sí usa el target correcto) se mantiene como referencia honesta: en Deforestación y Riesgo Biológico los baselines ARIMA/VAR ganan en RMSE held-out, lo que activa parcialmente el Escenario 1 declarado por la tesis.
- Coste de honestidad: declarar que la comparación interna del módulo `baselines.py` es metodológicamente vacía es debilitar una línea argumental secundaria, no la tesis principal. Ocultarlo sería F6 según CLAUDE.md §5.
