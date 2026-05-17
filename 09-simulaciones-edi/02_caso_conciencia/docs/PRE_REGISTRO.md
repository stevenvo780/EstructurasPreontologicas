# Pre-registro EDI — caso `02_caso_conciencia`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `02_caso_conciencia` — Conciencia Colectiva (Global Workspace Theory, Baars 1988)
- **Fecha de pre-registro:** `2026-05-17` (firma previa al re-fetch que reemplaza el fallback sintético confirmado en iter 7)
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `c6b3d3b2bbe21b28c8afc0a3e1c740eca55fc3b0`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Null` (con probabilidad secundaria `Trend`; basada en `outputs/metrics.json` actual: EDI_sintético = −0.007, p = 0.867, CI = [−0.125, 0.305])
- **Predicción de cambio sintético → real:** `misma clasificación` (esperado: Null). Subida a Trend posible si la serie OWID real recupera estructura de inercia mediática perdida por el fallback sintético; downgrade adicional improbable porque el sintético ya está cerca de cero.
- **Margen aceptable:** `|ΔEDI_real − (−0.007)| ≤ 0.10`
- **Justificación física breve:** Google Trends OWID mide atención mediática agregada; suicide_rate (driver) actúa con lag multi-anual e inercia institucional. La sonda `logistic_forced` asume respuesta rápida atención↔driver, supuesto cuestionable a escala anual. Se espera magnitud baja porque la atención colectiva se resetea por eventos exógenos (ciclo mediático ~6 meses) que no entran en el driver.

**Sesgo declarado:** la corrida sintética ya está hecha (commit `744724e…`). Este pre-registro congela el protocolo para la primera corrida sobre datos OWID/Google Trends reales y bloquea cualquier modificación de sonda/umbrales. El resultado previo sintético sesga la predicción hacia Null.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `logistic_forced` (definida en `common/ode_models.py`, `ode_key="c"`)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico`
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (Google Trends OWID — search volume agregado tema "mental health"/"suicide", normalizado 0–100)
- **Ventana temporal:** `2004-01-01 a 2023-12-01` (`real_start`/`real_end` de `case_config.json`; Google Trends arranca en 2004)
- **Tratamiento de datos faltantes:** interpolación lineal (pipeline default `src/data.py`)
- **Agregación temporal:** anual (`freq: YS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `https://ourworldindata.org/grapher/google-trends-mental-health.csv` (OWID dataset; reemplaza fallback sintético actual)
- **Indicador específico:** `mental_health_search_index` (Google Trends, normalizado OWID); drivers: `suicide_rate` (`SH.STA.SUIC.P5`, World Bank), `tertiary_enrollment` (`SE.TER.ENRR`, WB)
- **Países / región / agregación:** WLD (agregado global) o promedio OECD si OWID solo expone país-nivel; declarar en `FETCH_MANIFEST.json` la opción tomada **antes** de ver el resultado
- **Fecha de descarga prevista:** `2026-05-18`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/02_caso_conciencia/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; cerrar caso (sería sorpresa: revisar fuga de información) |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; opción de `@multi-probe-runner` (exploratoria) |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia; revisar sonda |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (umbrales, sondas, splits)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario cambiar alguno, se reporta como **análisis exploratorio post-hoc**, no confirmatorio, y se firma un pre-registro nuevo para una segunda corrida con datos independientes.

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza `Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
