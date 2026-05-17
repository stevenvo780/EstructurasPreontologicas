# Pre-registro EDI — caso `10_caso_justicia`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `10_caso_justicia` — Justicia Algorítmica (Rule of Law WGI, World Bank)
- **Fecha de pre-registro:** `2026-05-17` (firma previa a la **segunda** re-ejecución; ver sesgo declarado en §2)
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `744724e565f6027b7f29eae919c32e8aaf2f197d`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Weak` (basada en `outputs/metrics.json` previo: EDI_real ≈ 0.227, p ≈ 0.48 → no significativo)
- **Predicción de cambio sintético → real:** `upgrade` esperable si el detrend captura la tendencia secular de Rule of Law; `downgrade a Null` si el ruido institucional satura.
- **Margen aceptable:** `|ΔEDI_real_v2 − 0.227| ≤ 0.10`
- **Justificación física breve:** Rule of Law es serie lenta (anual, n≈28), gobernada por inercia institucional y shocks políticos no modelados (sonda `mean_reversion`); se espera magnitud baja pero no nula porque PIB pc y desempleo correlacionan con calidad institucional (Acemoglu-Robinson 2012).

**Sesgo declarado:** la primera corrida ya se ejecutó (commit previo); este pre-registro congela el protocolo para una **segunda re-ejecución con datos refrescados (WB API, fetch nuevo)** y bloquea cualquier modificación de sonda/umbrales en la defensa. El resultado previo (EDI=0.227, p=0.48) se reconoce como información que sesga la predicción hacia Weak/Null.

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
- **Variable de observación:** `value` (Rule of Law Estimate WGI, promedio top-10 economías)
- **Ventana temporal:** `1996-01-01 a 2023-01-01` (campo `real_start`/`real_end` de `case_config.json`)
- **Tratamiento de datos faltantes:** interpolación lineal (default WB pipeline)
- **Agregación temporal:** anual (`freq: YS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `https://api.worldbank.org/v2/country/USA;GBR;DEU;FRA;JPN;CAN;AUS;BRA;IND;CHN/indicator/RL.EST`
- **Indicadores específicos (códigos WB):** `RL.EST` (Rule of Law Estimate), `NY.GDP.PCAP.KD` (GDP pc), `SL.UEM.TOTL.ZS` (desempleo)
- **Países / región / agregación:** ISO-3 top-10: USA, GBR, DEU, FRA, JPN, CAN, AUS, BRA, IND, CHN (promedio simple anual); drivers WLD
- **Fecha de descarga prevista:** `2026-05-18`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/10_caso_justicia/src/validate.py --seed 42`:

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

Si tras ver el resultado se considera necesario cambiar alguno, se reporta como **análisis exploratorio post-hoc**, no confirmatorio, y se firma un pre-registro nuevo para una tercera corrida con datos independientes.

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza `Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
