# Pre-registro EDI — caso `12_caso_paradigmas`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `12_caso_paradigmas` — Paradigmas Científicos / R&D (Kuhn 1962; Landau-Ginzburg como sonda macro)
- **Fecha de pre-registro:** `2026-05-17` (firma previa a la primera corrida sobre OpenAlex/WB reales; sintético actual declarado)
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `c6b3d3b2bbe21b28c8afc0a3e1c740eca55fc3b0`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Null` (probabilidad alta) con cola en `Falsificación local`; basada en `outputs/metrics.json` sintético actual: EDI = −0.144, p = 0.787, CI = [−0.207, −0.107]
- **Predicción de cambio sintético → real:** `upgrade a Null/Trend` posible si OpenAlex (journal articles, patents) captura mejor la dinámica de transición de fase que el sintético `mean_reversion`. `Downgrade a Falsificación local` improbable pero no descartable porque el sintético ya cruza cero.
- **Margen aceptable:** `|ΔEDI_real − (−0.144)| ≤ 0.15` (margen amplio porque el sintético está mal calibrado: la sonda `mean_reversion` no captura la estructura de doble pozo del modelo Landau-Ginzburg descrito en el README; este pre-registro reconoce esa tensión)
- **Justificación física breve:** la producción científica anual (journal articles, patents) tiene tendencia secular dominante (crecimiento exponencial) que la sonda `mean_reversion` no modela. Se espera que el detrend canónico no recupere señal de cierre operativo porque el "paradigma dominante" opera en escala generacional (~30 años), excediendo la ventana 1996–2022.

**Sesgo declarado:** el sintético ya está hecho (commit `ed2571b…`) con EDI negativo. Este pre-registro reconoce que la sonda actual (`mean_reversion`) probablemente está mal especificada respecto a la teoría declarada (Landau-Ginzburg), pero **no la modifica antes de ver los datos reales** — eso sería garden of forking paths. Si tras la corrida real se considera cambiar a una sonda con doble pozo, se declara explícitamente como análisis exploratorio post-hoc en un pre-registro nuevo.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `mean_reversion` (definida en `common/ode_models.py`, `ode_key="j"`)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico`
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (índice compuesto journal_articles + patents, log-normalizado; ver `src/data.py`)
- **Ventana temporal:** `1996-01-01 a 2022-01-01` (`real_start`/`real_end` de `case_config.json`)
- **Tratamiento de datos faltantes:** interpolación lineal
- **Agregación temporal:** anual (`freq: YS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `https://api.openalex.org/works?filter=publication_year:1996-2022&group_by=publication_year` (volumen anual de publicaciones, ya scaffold en `data/fetch_openalex.py`)
- **Indicadores específicos:**
  - OpenAlex: `works_count` por año (todos los campos, sin filtro de concepto)
  - World Bank: `IP.JRN.ARTC.SC` (Scientific and technical journal articles), `IP.PAT.RESD` (Patent applications, residents)
- **Países / región / agregación:** WLD (agregado mundial) para OpenAlex; WLD para WB
- **Fecha de descarga prevista:** `2026-05-19`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/12_caso_paradigmas/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; cerrar caso (sorpresa fuerte: auditar leakage) |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; opción de `@multi-probe-runner` con sonda doble-pozo (exploratoria) |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia; documentar mismatch sonda↔teoría |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (umbrales, sondas, splits)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario cambiar la sonda a una con doble pozo (consistente con el README Landau-Ginzburg), se reporta como **análisis exploratorio post-hoc**, no confirmatorio, y se firma un pre-registro nuevo para una segunda corrida con datos independientes.

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza `Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
