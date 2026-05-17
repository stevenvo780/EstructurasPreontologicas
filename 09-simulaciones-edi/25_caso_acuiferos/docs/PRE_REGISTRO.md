# Pre-registro EDI — caso `25_caso_acuiferos`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `25_caso_acuiferos` — Depleción de Acuíferos (Theis 1935; balance Darcy-Theis con saturación de extracción)
- **Fecha de pre-registro:** `2026-05-17` (firma previa a B-T2 con cobertura GRACE/USGS ampliada; corrida previa con cobertura 0.51 declarada)
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `c6b3d3b2bbe21b28c8afc0a3e1c740eca55fc3b0`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Null` (con cola hacia `Falsificación local`; basada en `outputs/metrics.json` sintético actual: EDI = −0.061, p = 0.302, CI = [−0.100, −0.047])
- **Predicción de cambio sintético → real:** `upgrade a Trend o Weak` posible si GRACE GWSA con cobertura ampliada (>0.80) captura mejor la tendencia secular de depleción; `downgrade a Falsificación local` posible porque el CI sintético ya excluye cero por la izquierda, sugiriendo mismatch estructural sonda↔serie.
- **Margen aceptable:** `|ΔEDI_real − (−0.061)| ≤ 0.15` (margen amplio porque la cobertura previa 0.51 es muy baja; un re-fetch a cobertura >0.80 puede alterar la calibración significativamente)
- **Justificación física breve:** GRACE mide TWS (Total Water Storage) con resolución ~300 km y inercia mensual; la sonda `aquifer_darcy` modela un acuífero único con recarga α=0.08/año y extracción saturada logísticamente. La agregación global puede mezclar acuíferos en distintos estados (acumulación monzónica vs. depleción permanente en Ogallala/Indo-Gangético), diluyendo la señal de cierre operativo. Se espera magnitud baja.

**Sesgo declarado:** el sintético ya está hecho (commit `c6b3d3b…`, mismo HEAD que este pre-registro porque la corrida con cobertura 0.51 está en outputs). Este pre-registro congela el protocolo para la corrida con cobertura ampliada y bloquea cambios de sonda. El resultado previo (EDI=−0.06, CI excluye cero negativamente) sesga la predicción hacia Null/Falsificación.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `aquifer_darcy` (definida en `common/ode_models.py`, `ode_key="aq"`)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico`
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (anomalía GWSA — Groundwater Storage Anomaly — derivada de GRACE TWS con corrección de soil moisture; cm equivalente agua)
- **Ventana temporal:** `1980-01-01 a 2020-12-01` (`real_start`/`real_end` de `case_config.json`; GRACE disponible desde 2002, pre-2002 se llena con reconstrucciones USGS o se acorta la ventana — declarar la opción en `FETCH_MANIFEST.json` **antes** de ver el resultado)
- **Tratamiento de datos faltantes:** interpolación lineal sobre serie anualizada (GRACE tiene gap 2017-2018 entre misiones GRACE/GRACE-FO)
- **Agregación temporal:** anual (`freq: YS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC_L3_CSR_RL06_LND_v04` (GRACE Tellus Mascon, JPL) + `https://waterservices.usgs.gov/nwis/site/?siteOutput=expanded&siteType=GW` (USGS NWIS groundwater levels para validación cruzada)
- **Indicadores específicos:**
  - GRACE: `lwe_thickness` (Liquid Water Equivalent, cm) — equivalente agua almacenada
  - Conversión a GWSA: restar soil moisture (NOAH GLDAS) y snow water equivalent
  - USGS: `gwsa_avg` (promedio anomalía pozos en US para sanity check)
- **Países / región / agregación:** WLD (mascon agregado global, con peso de área); alternativa: top-5 acuíferos estresados (Ogallala, North China Plain, Indo-Gangético, California Central Valley, Arabia Saudí) — declarar en `FETCH_MANIFEST.json`
- **Fecha de descarga prevista:** `2026-05-20`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/25_caso_acuiferos/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; cerrar caso (sorpresa fuerte: auditar leakage temporal pre/post-2002) |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia (ventana corta GRACE) |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; opción de `@multi-probe-runner` con sonda multi-reservorio (exploratoria) |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia; documentar mismatch agregación global ↔ acuíferos heterogéneos |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (umbrales, sondas, splits)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario cambiar alguno, se reporta como **análisis exploratorio post-hoc**, no confirmatorio, y se firma un pre-registro nuevo para una corrida adicional con datos independientes.

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza `Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
