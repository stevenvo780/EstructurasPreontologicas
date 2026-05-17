# Pre-registro EDI — caso `21_caso_salinizacion`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `21_caso_salinizacion` — Salinización de Suelos (proxy: irrigated land % World Bank)
- **Fecha de pre-registro:** `2026-05-17`
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `744724e565f6027b7f29eae919c32e8aaf2f197d`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Null` (basada en `outputs/metrics.json` previo: EDI_real ≈ 0.018, p ≈ 0.003 → p significativo pero magnitud trivial, CI [-0.077, 0.083] cruza cero → null genuino)
- **Predicción de cambio sintético → real:** `misma clasificación` (sintético: EDI≈-0.002 null; real: EDI≈0.018 null — la sonda bilineal no captura dinámica relevante en serie WB anual de irrigated land).
- **Margen aceptable:** `|ΔEDI_real_v2 − 0.018| ≤ 0.05`
- **Justificación física breve:** la salinización es proceso de escala decadal-centenaria con causalidad acumulativa (Qadir 2014); el proxy WB de irrigated land es indicador estructural lento (~0.05%/año), no responde a forzantes anuales modelables por `bilinear`. Predicción: null genuino esperado; candidato a `@multi-probe-runner` con sonda de acumulación o Richards modificada.

**Sesgo declarado:** primera corrida ya ejecutada y arrojó null. Este pre-registro congela protocolo para segunda re-ejecución y formaliza el null como predicción explícita (no como falla post-hoc).

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `bilinear` (definida en `common/ode_models.py`, `ode_key="sl"`, params `ode_alpha=0.05, ode_beta=1.0, ode_gamma=0.02`)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico`
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (`AG.LND.IRIG.AG.ZS` — irrigated land % of agricultural land, World Bank)
- **Ventana temporal:** `1961-01-01 a 2022-01-01` (campo `real_start`/`real_end` de `case_config.json`)
- **Tratamiento de datos faltantes:** interpolación lineal (pipeline WB)
- **Agregación temporal:** anual (`freq: YS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `https://api.worldbank.org/v2/country/WLD/indicator/AG.LND.IRIG.AG.ZS?format=json&per_page=500&date=1961:2022`
- **Indicadores específicos (códigos WB):** `AG.LND.IRIG.AG.ZS` (irrigated land %), `ER.H2O.FWTL.ZS` (freshwater withdrawal % de recursos internos)
- **Países / región / agregación:** WLD (agregado mundial World Bank)
- **Fecha de descarga prevista:** `2026-05-18`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/21_caso_salinizacion/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; cerrar caso (improbable según predicción) |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; activar `@multi-probe-runner` con sonda de acumulación (declarada exploratoria) |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (umbrales, sondas, splits)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario cambiar alguno, se reporta como **análisis exploratorio post-hoc**, no confirmatorio, y se firma un pre-registro nuevo para una tercera corrida.

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza `Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
