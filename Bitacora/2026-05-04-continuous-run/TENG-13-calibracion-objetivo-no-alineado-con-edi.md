# TENG-13 — Calibración con objetivo no alineado con EDI

**Fecha:** 2026-05-04
**Origen:** Hallazgo de `process-verifier` engine 2026-05-05.
**Modo:** auditoría read-only; sin tocar `Tesis.md` ni `metrics.json`.

## (a) Verificación de la afirmación

**Afirmación:** la calibración del ABM minimiza un objetivo bi-criterio
`score = rmse * max(0.5, 2.0 − corr)`, no alineado con la métrica EDI que
sólo depende de RMSE (`EDI = 1 − RMSE_coupled / RMSE_no_ode`). Es una
dependencia oculta no declarada en metodología.

**Verificación textual** (`09-simulaciones-edi/common/hybrid_validator.py`):

- L496 (docstring de `calibrate_abm`):
  > "Objetivo: minimizar RMSE penalizado por baja correlación."
- L508–520 (`_score_single`):
  ```python
  err = float(np.sqrt(np.mean((pred_arr - obs_arr) ** 2)))
  ...
  corr = float(np.corrcoef(pred_arr, obs_arr)[0, 1])
  ...
  penalty = max(0.5, 2.0 - corr)
  return err * penalty, err
  ```
- L548–549 (path GPU equivalente):
  ```python
  penalties = cp.clip(2.0 - corrs, 0.5, None)
  scores = errs * penalties
  ```

La afirmación se confirma textualmente: el score de selección es producto
RMSE×(2−corr) (clamp inferior 0.5), mientras que EDI sólo lee RMSE en
`validate.py`. La función devuelve además `err` "limpio", pero el
ranking/selección de parámetros se hace por `score`, no por `err`.

**Por qué importa:** dos parametrizaciones con igual RMSE pero distinta
correlación pueden ser elegidas por la calibración y rechazadas en EDI, o
viceversa. El acoplamiento ABM↔ODE finalmente reportado puede no ser el
que minimizaría RMSE puro. Esto es relevante para la lectura del EDI:
no es "el mejor ajuste predictivo", es "el mejor ajuste predictivo entre
los que también correlacionan con la macro-sonda".

Este sesgo puede operar a favor o en contra del EDI según el caso, por lo
que no es un *signo* declarable a priori; debe medirse.

## (b) Propuesta de edición

Esta tarea **requiere firma humana** (`needs_human`) por dos razones:

1. La elección entre RMSE-only vs RMSE×corr no es ortográfica: cambia el
   sentido operativo de "EDI calibrado" en todo el corpus. El corte
   conceptual lo firma Jacob.
2. Re-calibrar 3 casos con RMSE-only y reportar |ΔEDI| está en el alcance
   de la asistencia, pero re-correr el corpus completo (>40 casos) es
   decisión humana.

**Acciones propuestas (escalonadas):**

1. **Declaración inmediata en glosario** (low-risk, sin re-correr nada):
   añadir en `00-proyecto/07-glosario-operativo.md` entrada
   "Calibración del ABM" indicando que el objetivo de selección es
   bi-criterio `score = RMSE · max(0.5, 2 − corr)` y que EDI se evalúa
   sobre RMSE puro del modelo así seleccionado. Marcar como dependencia
   metodológica declarada.
2. **Declaración por caso** en `case_config.json` (campo
   `calibration_objective`: `"rmse_corr_penalty"`). No requiere re-correr.
3. **Estudio de sensibilidad** en 3 casos pre-acordados (sugerencia:
   uno con EDI alto, uno medio, uno null) re-calibrando con
   `score = RMSE` puro y reportando `ΔEDI`. Si `|ΔEDI| > 0.05` en alguno,
   declarar deuda explícita en cap. 03 §metodología.
4. **B-T nueva (asistencia ejecuta tras firma):** implementar flag
   `--calibration-objective {rmse,rmse_corr}` en `validate.py` y mantener
   `rmse_corr` como default (compat hacia atrás), pero documentado.

**Edición concreta sugerida (no aplicada):**

- `00-proyecto/07-glosario-operativo.md`: nueva entrada "Calibración del
  ABM (objetivo de selección)" — cita literal del score y aclaración del
  desacople con la métrica de evaluación.
- `03-formalizacion/04-operacionalizacion-de-kappa.md` o
  `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md`: párrafo
  declarando dependencia oculta antes-de-deuda.
- `06-cierre/` "Deuda residual": ítem "calibración bi-criterio vs métrica
  RMSE-only — sensibilidad pendiente en 3 casos".

No se edita aquí ningún archivo del manuscrito ni de configuración por
política de la pasada.

## (c) Costo argumentativo declarado

- **Concesión honesta:** la tesis reporta EDI como "degradación predictiva
  RMSE al apagar el acoplamiento", pero la búsqueda de parámetros del
  ABM acoplado prioriza también covariación de fase con la sonda macro.
  Eso introduce una preferencia implícita por modelos cuya dinámica
  *sigue* a la sonda, lo que puede inflar EDI cuando la sonda comparte
  estructura temporal con la observación.
- **Defensa razonable:** la penalización con clamp 0.5 evita explosión
  en regímenes anti-correlacionados y la calibración no es sobre el
  conjunto de evaluación EDI; aún así, el sesgo no es nulo y debe
  medirse, no asumirse pequeño.
- **Riesgo si no se declara:** un revisor hostil puede calificar esto como
  *p-hacking suave* en la calibración (selección que favorece narrativa
  de acoplamiento). La deuda declarada lo neutraliza; ocultarla lo
  agrava.

## Estado

- Verificación textual: **OK** (línea 508-520, 548-549).
- Propuesta concreta: redactada, **no aplicada**.
- Marca: `needs_human` para corte conceptual y para re-corrida amplia;
  acciones (1) y (2) podrían ejecutarse por asistencia tras firma de
  Jacob como B-T.

RESULT: complete | TENG-13-calibracion-objetivo-no-alineado-con-edi | verificado L508-520; needs_human para corte
