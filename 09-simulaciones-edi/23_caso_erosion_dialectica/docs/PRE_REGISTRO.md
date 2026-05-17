# Pre-registro EDI — caso `23_caso_erosion_dialectica`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `23_caso_erosion_dialectica` — Erosión Dialéctica (Abrams-Strogatz Prestige Competition)
- **Fecha de pre-registro:** `2026-05-17`
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `744724e565f6027b7f29eae919c32e8aaf2f197d`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Falsificación local del aparato` (basada en `outputs/metrics.json` previo: EDI_real = −1.0, CI [-3.09, -0.68] excluye cero por la izquierda → contraevidencia explícita)
- **Predicción de cambio sintético → real:** `downgrade severo` (sintético: EDI≈-0.019 null; real: EDI=-1.0 falsificación). La sonda `prestige_competition` no es físicamente apropiada para la serie real propuesta — predicción honesta de fallo.
- **Margen aceptable:** `|ΔEDI_real_v2 − (−1.0)| ≤ 0.30`
- **Justificación física breve:** Abrams-Strogatz (2003) modela competencia lingüística con dos lenguas en sustrato fijo; aplicarla a "erosión dialéctica" sin una variable de observación con dos competidores claros (e.g. share de idiomas en Wikipedia, citas científicas idioma A vs B) produce mismatch sistemático. Predicción: la falsificación se replicará hasta que se especifique mejor la variable observable.

**Sesgo declarado:** primera corrida ya ejecutada y arrojó falsificación local. Este pre-registro **congela el protocolo defectuoso para reportarlo como contraevidencia honesta**, no para esconderlo. Si se reformula la variable observable, requiere pre-registro nuevo (caso renombrado o desdoblado).

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `prestige_competition` (definida en `common/ode_models.py`, `ode_key="ed"`, params `ode_alpha=0.03, ode_beta=1.0, ode_prestige=0.008, ode_amplification=0.3`)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico`
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (serie unidimensional declarada en `data/dataset.csv`; ver `src/data.py` — actualmente proxy genérico desde `data_universal.fetch_case_data` con fallback sintético)
- **Ventana temporal:** `2005-01-01 a 2023-12-01` (campo `real_start`/`real_end` de `case_config.json`)
- **Tratamiento de datos faltantes:** exclusión de registro (default)
- **Agregación temporal:** anual (`freq: YS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** declarada en `common/data_universal.py` para clave `23_caso_erosion_dialectica` (revisar antes de descarga; si no hay fuente real específica → fallback sintético declarado como deuda)
- **Indicador específico:** **pendiente de especificar fuente real** — candidato: share Wikipedia por idioma (EN vs ES vs ZH) o proporción de citas científicas idioma dominante (Web of Science)
- **Países / región / agregación:** global agregado
- **Fecha de descarga prevista:** `2026-05-18`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

**Deuda declarada:** la fuente real del caso está sub-especificada (`data_universal` falla → fallback sintético). El pre-registro reconoce esto como límite metodológico; cualquier reclasificación requiere primero arreglar la fuente real, luego firmar pre-registro nuevo.

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/23_caso_erosion_dialectica/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; investigar overfitting (sorpresa fuerte respecto a predicción) |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; verificar contra predicción |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar; activar `@multi-probe-runner` (exploratorio) |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como **contraevidencia esperada**; documentar en sección crítica del manuscrito como evidencia de honestidad del aparato |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (umbrales, sondas, splits)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario cambiar la sonda o la variable observable, se trata como **caso reformulado** (renombrado o desdoblado), no como re-especificación post-hoc; requiere pre-registro nuevo.

Si el resultado no coincide con la predicción de §2 (p. ej. EDI sube a Weak), se reporta honestamente y se investiga overfitting / data leakage antes de aceptar como Weak genuino.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
