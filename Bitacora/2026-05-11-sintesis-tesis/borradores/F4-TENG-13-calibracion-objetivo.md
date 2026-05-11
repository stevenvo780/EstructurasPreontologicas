---
borrador: IA
requires: H-J* + B-T
propuesta_fecha: 2026-05-11
destino: 00-proyecto/07-glosario-operativo.md (entrada "Calibración del ABM") + 03-formalizacion/02-criterios-de-legitimidad-y-metodo.md ó 04-operacionalizacion-de-kappa.md + 06-cierre/Deuda residual
hallazgo: Bitacora/2026-05-04-continuous-run/TENG-13-calibracion-objetivo-no-alineado-con-edi.md
tipo: insercion_glosario + insercion_deuda + tarea_B-T_sensibilidad_calibracion
---

## Diagnóstico

`09-simulaciones-edi/common/hybrid_validator.py:496-549` calibra el ABM minimizando un **score bi-criterio** `score = rmse * max(0.5, 2.0 − corr)` (clamp inferior 0.5). Este objetivo combina RMSE y correlación. La métrica EDI propia, en cambio, depende **sólo** de RMSE (`EDI = 1 − RMSE_coupled / RMSE_no_ode`). Hay desacople entre **objetivo de selección de parámetros** (bi-criterio) y **objetivo de evaluación** (RMSE puro). Dos parametrizaciones con igual RMSE pero distinta correlación pueden ser elegidas por la calibración y comparadas distinto en EDI; el acoplamiento ABM↔ODE finalmente reportado puede no ser el que minimizaría RMSE puro. **El EDI reportado no es "el mejor ajuste predictivo", es "el mejor ajuste predictivo entre los que también correlacionan con la macro-sonda"**. El sesgo puede operar a favor o en contra del EDI según el caso; debe medirse.

## Verificación contra código

- `hybrid_validator.py:496` (docstring `calibrate_abm`): *"Objetivo: minimizar RMSE penalizado por baja correlación."*
- `hybrid_validator.py:508-520` (`_score_single`):
  ```python
  err = float(np.sqrt(np.mean((pred_arr - obs_arr) ** 2)))
  corr = float(np.corrcoef(pred_arr, obs_arr)[0, 1])
  penalty = max(0.5, 2.0 - corr)
  return err * penalty, err
  ```
- `hybrid_validator.py:548-549` (path GPU equivalente):
  ```python
  penalties = cp.clip(2.0 - corrs, 0.5, None)
  scores = errs * penalties
  ```
- La selección de parámetros usa `score`, no `err` limpio; el `err` se devuelve sólo como diagnóstico.

## Texto propuesto (voz autoral filosófica de Jacob)

**Añadir entrada en `00-proyecto/07-glosario-operativo.md`:**

> **Calibración del ABM (objetivo de selección).** El procedimiento `calibrate_abm` en `hybrid_validator.py` selecciona los parámetros del ABM minimizando un objetivo **bi-criterio** `score = RMSE × max(0.5, 2 − corr)` (clamp inferior 0.5 sobre la penalización por baja correlación). El objetivo combina RMSE y correlación temporal entre la predicción y la observación. La métrica EDI, en cambio, se evalúa **sobre RMSE puro** del modelo así seleccionado. Esto introduce una preferencia implícita por modelos cuya dinámica *sigue temporalmente* la observación, no sólo la aproxima en magnitud. Deuda metodológica fechada: la sensibilidad de EDI a la elección del objetivo de calibración (RMSE puro vs RMSE × corr) está pendiente de medición en 3 casos representativos (B-T).

**Añadir párrafo en `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md` o en `03-formalizacion/04-operacionalizacion-de-kappa.md` (donde se describe el protocolo de calibración):**

> **Dependencia metodológica declarada.** El EDI reportado no es exactamente "el mejor ajuste predictivo del ABM acoplado en RMSE", sino "el mejor ajuste predictivo entre los modelos que también correlacionan temporalmente con la sonda macro" (objetivo de calibración `score = RMSE × max(0.5, 2 − corr)`, `hybrid_validator.py:508-520`). La penalización con clamp 0.5 evita explosión bajo regímenes anti-correlacionados, pero introduce un sesgo de selección que la métrica de evaluación (RMSE puro) no anula. El sesgo puede operar en cualquier dirección y se mide caso a caso. Esta dependencia se reconoce como **deuda residual fechada**: sensibilidad pendiente en tres casos pre-acordados (un EDI alto, un medio, un null) re-calibrando con `score = RMSE` puro y reportando `ΔEDI`. Si `|ΔEDI| > 0.05` en algún caso, la deuda escala a corrección estructural del pipeline.

**Insertar deuda en `06-cierre/Deuda residual`:**

> **Deuda residual: calibración bi-criterio vs métrica RMSE-only.** Objetivo de selección `RMSE × max(0.5, 2 − corr)` (cf. glosario "Calibración del ABM"). Sensibilidad pendiente en 3 casos del corpus.

## Acciones técnicas derivadas (B-T)

1. **Declaración por caso:** añadir campo `calibration_objective: "rmse_corr_penalty"` (default actual) en cada `case_config.json` para trazabilidad.
2. **Estudio de sensibilidad en 3 casos pre-acordados** (sugerencia: 16 deforestación con EDI alto, 30 behavioral dynamics con EDI medio, 12 paradigmas con EDI negativo): re-calibrar con `score = RMSE` puro y reportar `ΔEDI`. Si `|ΔEDI| > 0.05` en alguno, declarar deuda explícita en cap 03 §metodología y abrir B-T mayor.
3. **B-T (asistencia tras firma):** implementar flag `--calibration-objective {rmse, rmse_corr}` en `validate.py`, mantener `rmse_corr` como default (compatibilidad hacia atrás) pero documentar el flag y su efecto.
4. Tras decisión de Jacob sobre si el corte conceptual obliga a re-corrida amplia (>40 casos), abrir B-T mayor o cerrar con deuda declarada.

## Costo argumentativo declarado

- **Concesión honesta:** la tesis reporta EDI como "degradación predictiva RMSE al apagar el acoplamiento", pero la búsqueda de parámetros del ABM acoplado prioriza también covariación de fase con la sonda macro. Eso introduce una preferencia implícita por modelos cuya dinámica sigue a la sonda, que puede inflar EDI cuando la sonda comparte estructura temporal con la observación.
- **Defensa razonable:** la penalización con clamp 0.5 evita explosión en regímenes anti-correlacionados; la calibración no es sobre el conjunto de evaluación EDI; aún así, el sesgo no es nulo.
- **Riesgo si no se declara:** un revisor puede calificarlo como p-hacking suave en la calibración. La deuda declarada lo neutraliza; ocultarla lo agrava.
