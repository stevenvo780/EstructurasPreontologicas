---
borrador: IA
requires: H-J* + B-T
propuesta_fecha: 2026-05-11
destino: 04-debates/05-limitaciones-declaradas-consolidacion.md + 00-proyecto/07-glosario-operativo.md (entrada C1)
hallazgo: Bitacora/2026-05-04-continuous-run/TENG-08-c1-or-fallback-permite-edi-negativo.md
tipo: deuda + tarea_B-T_c1_fallback_diagnostico (Salida 2)
---

## Diagnóstico

`evaluate_c1` en `hybrid_validator.py:892-926` aprueba C1 si se cumple AL MENOS UNA de dos condiciones (`c1_relative OR c1_absolute`). La rama (B) `c1_absolute` exige sólo `rmse_abm < 2·obs_std AND corr_abm > 0.3`, **sin requerir que el ODE aporte información**. Resultado: 8 fases del corpus tienen `c1_convergence=True` con `EDI < 0` (el ABM acoplado predice peor que el ABM reducido — pero pasa C1 por correlación temporal del ABM con los datos). Caso 23 (erosión dialéctica, fase real) es ejemplar: `c1_convergence=True, c1_relative=False (rel_improvement=-0.237), c1_absolute=True (corr_abm=0.994), edi.value=-1.0`. El falso positivo de convergencia es sistemático (8/80 fases ≈ 10 %), no anomalía aislada.

## Verificación contra código

- `hybrid_validator.py:913-926`:
  ```python
  if reduced_val is not None:
      err_reduced = rmse(reduced_val, obs_val)
      relative_improvement = err_reduced - err_abm
      c1_relative = relative_improvement > 0
  c1_absolute = (err_abm < 2.0 * threshold and corr_abm > 0.3)
  c1 = c1_relative or c1_absolute
  ```
- Lista de 8 fases con C1=True y EDI<0 verificada en F4-TENG-08 origen §"Casos del corpus": 02 (synthetic, real), 03 (real), 09 (synthetic), 14 (synthetic), 20 (synthetic), 23 (real, EDI=-1.0), 25 (real, rel_improv=-2.858).

## Texto propuesto (voz autoral filosófica de Jacob) — Salida 2 (c1_fallback diagnóstico)

**Añadir entrada en `00-proyecto/07-glosario-operativo.md` (sección C1-C5+):**

> **C1 (convergencia ABM+ODE → datos).** Mide si el modelo acoplado se aproxima a las observaciones. Implementación actual (`hybrid_validator.py:evaluate_c1`): disyunción `c1 = c1_relative OR c1_absolute`, donde `c1_relative` exige mejora del coupled sobre el reducido y `c1_absolute` admite ajuste absoluto del ABM aun sin aporte del ODE.
>
> Deuda técnica abierta: la disyunción permite que C1 pase con `EDI < 0` (8 fases del corpus actualmente — el ABM acoplado predice peor que el reducido pero el ABM solo correlaciona temporalmente con los datos). La salida 2 propuesta (B-T abierta) reclasifica `c1_absolute` como **diagnóstico `c1_fallback` que NO contribuye a `overall_pass` cuando `reduced_val` existe**:
>
> ```python
> if reduced_val is not None:
>     c1 = c1_relative          # estricto: ODE debe aportar
>     c1_fallback = c1_absolute # diagnóstico, no pasa C1
> else:
>     c1 = c1_absolute          # único disponible
>     c1_fallback = None
> ```
>
> El cambio actualiza `overall_pass` y la prosa de cap 03/09 que cite C1 = True en los 8 casos afectados.

**Insertar en `04-debates/05-limitaciones-declaradas-consolidacion.md` o "Deuda residual" del cap 06:**

> **Deuda residual: 8 fases con C1 = True bajo EDI < 0.** La implementación actual de C1 admite que el modelo acoplado pase la convergencia por la rama absoluta (`c1_absolute`, basada en RMSE del ABM y correlación temporal) sin requerir que el ODE aporte información. Esto produce 8 fases del corpus (casos 02, 03, 09, 14, 20, 23, 25) donde `c1_convergence = True` coexiste con `EDI < 0` — el modelo acoplado predice peor que el reducido pero el ABM solo correlaciona con los datos. El caso 25 (acuíferos, real) es el más severo: `relative_improvement = -2.858` (el ODE catastróficamente empeora la predicción), aún reportado como `C1 = True`. Casos como 23 (erosión, real, `EDI = -1.0`) están ya declarados como null en el manuscrito; reclasificar C1 refuerza esa lectura, no la contradice. La afirmación general "el corpus pasa C1 ampliamente" debe re-cualificarse tras la corrección.
>
> La salida elegida es **Salida 2** (reclasificar `c1_absolute` como `c1_fallback` diagnóstico cuando `reduced_val` existe). La salida 1 (C1 estricto, AND) es más invasiva y rompe casos legítimos sin reducido; la salida 3 (guardia anti-EDI-negativo) acopla C1 a EDI invirtiendo el orden lógico del pipeline.

## Acciones técnicas derivadas (B-T)

- Implementar la salida 2 en `hybrid_validator.py:892-926`.
- Actualizar el agregador `overall_pass` y la prosa de §03/§09 que cite C1 = True en las 8 fases afectadas.
- Re-ejecutar los 8 casos afectados y reportar diff en `metrics.json`.
- Documentar la salida 2 como cambio metodológico fechado en CHANGELOG del harness.

## Costo argumentativo declarado

- 8 fases (≈10 % del corpus por fase) cambiarán C1 = True → C1 = False bajo la salida 2.
- La afirmación general "el corpus pasa C1 ampliamente" debe re-cualificarse a "el corpus pasa C1 cuando el ODE aporta mejora sobre el reducido; en ~10 % de las fases el ajuste absoluto del ABM aprueba C1 sin aporte del ODE — esos casos se reportan ahora como `c1_fallback`, no como C1 estricto".
- Sin la corrección: la cifra de "robust convergence" del aparato es inflada por estos falsos positivos; con la corrección queda alineada con la semántica fuerte de "convergencia ABM + ODE".
