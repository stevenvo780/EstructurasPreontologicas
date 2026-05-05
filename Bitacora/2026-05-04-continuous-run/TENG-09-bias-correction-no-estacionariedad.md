# TENG-09 — Bias Correction y no-estacionariedad

**Fecha:** 2026-05-04
**Origen:** process-verifier engine, 2026-05-05
**Archivos auditados:** `09-simulaciones-edi/common/hybrid_validator.py:1560-1681`

## (a) Verificación de la afirmación

La afirmación es **correcta y se reproduce textualmente en el código**:

1. Líneas 1579–1589: las estadísticas de BC se calculan exclusivamente sobre el segmento `[:val_start]`:
   - `ode_train_seg = ode_arr_full[:val_start]`
   - `obs_train_seg = np.asarray(obs[:val_start], …)`
   - `ode_m, ode_s, obs_m_bc, obs_s_bc` derivados solo del train.
2. Líneas 1594–1604: la transformación afín se aplica a **toda la serie ODE** (`for v in ode_series`), no solo al segmento de train. Es decir, los parámetros estimados en train se proyectan al horizonte completo, incluyendo `[val_start:]`.
3. Bajo no-estacionariedad (cambio de media/varianza entre train y val: tendencia, régimen, intervención exógena), el shift+scale calibrado en train introduce un sesgo sistemático en val que no está acotado por la guarda actual.

La **guarda de reversión** (líneas 1664–1680) compara `err_abm` (ABM acoplado con BC) contra `err_abm_no_ode` (ABM sin ODE). Solo dispara el rerun si el BC degrada el ABM acoplado **por debajo del baseline sin acoplamiento**. No detecta:
- Casos donde el BC mejora marginalmente sobre `no_ode` pero queda dominado por sesgo de no-estacionariedad (BC subóptimo, no catastrófico).
- Casos donde la mejora aparente del BC se debe a fuga indirecta de información (ode_series ajustada a la media-train mientras la val tiene drift).

Por tanto, el riesgo identificado es **real y no mitigado** por las guardas vigentes.

## (b) Propuesta de edición

**needs_human (B-T*):** la corrección toca el pipeline numérico canónico y altera la métrica EDI declarada. No cierro desde asistencia.

Borrador propuesto para revisión de Jacob/Steven:

1. Tras computar `ode_series_bc`, calcular un test de estacionariedad sobre el **residuo** `ode_series_bc[val_start:] - ode_series[val_start:]` (la "huella" introducida por BC en val):
   - Test ADF (`statsmodels.tsa.stattools.adfuller`) sobre el residuo.
   - Si `p > 0.05` (no se puede rechazar raíz unitaria) **y** `len(val) ≥ 12`, marcar `bc_stationarity_warning = true` en `metrics.json`.
2. Como diagnóstico complementario (más barato y sin nueva dependencia obligatoria), añadir un check Welch sobre means/var:
   - `mean_train` vs `mean_val` de `obs`; si `|Δmean| > 2·obs_train_std` o ratio de varianzas fuera de [0.5, 2.0], emitir el mismo warning.
3. **No alterar la decisión de BC**: solo emitir warning. La modificación de la lógica (p.ej. BC rolling o BC bloqueado bajo no-estacionariedad) es una decisión H-J* que requiere firma porque cambia EDI reportados.
4. Persistir el warning en todos los casos con `bc_mode in {"full", "bias_only"}` (los `none` y `reverted` no aplican).

Ubicación sugerida del parche: bloque inmediatamente posterior a la guarda de reversión (~línea 1681), antes de calcular `edi_val`.

Acceptance test propuesto (alineado con el solicitado):
- Unit test sintético con serie `obs` que tiene drift lineal (p.ej. `obs_train ~ N(0,1)`, `obs_val = obs_train + 0.05·t`) y ODE estacionaria. Verificar que `bc_stationarity_warning == True` tras correr `validate.py`.
- Auditoría retroactiva: ejecutar `./tesis audit` con un script que recorra todos los `metrics.json` y reporte cuántos casos `bc_mode != none/reverted` carecen del campo nuevo (objetivo: 0 tras backfill).

## (c) Costo argumentativo declarado

- **Costo 1:** la introducción del warning **no corrige** el sesgo, solo lo declara. Los EDI ya reportados de casos con BC activo siguen siendo válidos como cifra reproducible, pero deben leerse con la advertencia explícita de que en presencia de no-estacionariedad pueden estar sesgados (dirección del sesgo no determinable sin el caso concreto). Esto es coherente con CLAUDE.md §7 (deuda declarada) pero amplía la deuda residual de capítulo 03/05.
- **Costo 2:** si la auditoría retroactiva muestra que >30% del corpus (≥12 casos) levanta `bc_stationarity_warning`, la afirmación de "EDI multidominio robusto" del capítulo 06 requiere matización: el efecto medido podría tener componente de sesgo BC × no-estacionariedad inseparable sin re-ejecución con BC alternativo.
- **Costo 3:** la solución "correcta" (BC rolling sobre ventanas, o re-fit por bloque, o renunciar a BC bajo no-estacionariedad) cambia EDI reportados — es decisión H-J* que no puedo ejecutar.
- **Costo 4 (concesión filosófica):** este hallazgo da munición legítima a la objeción de Cartwright/Hacking sobre "modelos que se ajustan al laboratorio pero proyectan mal al campo". El manuscrito debería reconocerlo en cap. 04-debates §limitaciones técnicas.

## Estado

`needs_human` — propuesta de B-T* (test ADF + campo nuevo en metrics.json) y posible H-J* (decisión sobre cambiar la lógica de BC). No se edita código ni `metrics.json` desde esta pasada.

RESULT: complete | TENG-09-bias-correction-no-estacionariedad | needs_human B-T*+H-J*
