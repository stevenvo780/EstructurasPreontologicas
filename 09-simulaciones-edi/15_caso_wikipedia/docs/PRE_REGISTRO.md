# Pre-registro EDI — caso `15_caso_wikipedia`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `15_caso_wikipedia` — Wikipedia: atención mensual a "Climate change" (Wikimedia pageviews)
- **Fecha de pre-registro:** `2026-05-17`
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `744724e565f6027b7f29eae919c32e8aaf2f197d`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Weak` (basada en `outputs/metrics.json` previo: EDI_real ≈ 0.192, p ≈ 0.000 → estadísticamente significativo, magnitud moderada)
- **Predicción de cambio sintético → real:** `misma clasificación` (sintético: EDI≈0.197 Weak significativo; real: EDI≈0.192 Weak significativo — estabilidad alta).
- **Margen aceptable:** `|ΔEDI_real_v2 − 0.192| ≤ 0.08`
- **Justificación física breve:** la atención colectiva a artículos controvertidos sigue una dinámica de Yasseri (consensus-controversy) bien capturada por `mean_reversion` con shocks externos (eventos climáticos mediáticos); CI bootstrap [0.12, 0.51] indica magnitud incierta pero signo consistente.

**Sesgo declarado:** primera corrida ya ejecutada; este pre-registro congela el protocolo para una segunda re-ejecución con descarga refrescada de pageviews (extensión hasta 2025-12).

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `mean_reversion` (definida en `common/ode_models.py`, `ode_key="w"`)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico`
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (atención mensual ≈ pageviews log-normalizados del artículo "Climate change" en EN Wikipedia)
- **Ventana temporal:** `2015-07-01 a 2024-12-01` (campo `real_start`/`real_end` de `case_config.json`)
- **Tratamiento de datos faltantes:** exclusión de registro (CSV pre-limpiado)
- **Agregación temporal:** mensual (`freq: MS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/Climate_change/monthly/2015070100/2024120100`
- **Indicador específico:** pageviews mensuales (artículo "Climate change", EN Wikipedia, all-access, all-agents)
- **Países / región / agregación:** EN Wikipedia global (lectores anglófonos mundiales)
- **Fecha de descarga prevista:** `2026-05-18`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/15_caso_wikipedia/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; cerrar caso |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; opción de `@multi-probe-runner` (exploratoria) |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (umbrales, sondas, splits)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario cambiar alguno, se reporta como **análisis exploratorio post-hoc**, no confirmatorio, y se firma un pre-registro nuevo para una tercera corrida con datos independientes (p. ej., artículo distinto o idioma distinto).

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza `Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
