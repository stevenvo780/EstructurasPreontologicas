# Pre-registro EDI — caso `22_caso_fosforo`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `22_caso_fosforo` — Ciclo del Fósforo (Carpenter 2005; sonda bilinear runoff×concentración)
- **Fecha de pre-registro:** `2026-05-17` (firma previa al **re-fetch con FAOSTAT granular**; reemplaza WB `AG.CON.FERT.ZS` agregado por país-cultivo)
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `c6b3d3b2bbe21b28c8afc0a3e1c740eca55fc3b0`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Weak` (basada en `outputs/metrics.json` actual: EDI = 0.192, p = 0.014, CI = [0.161, 0.239], permutation_significant=true; `valid:false` por LoE=0.6 que descuenta el weighted_value a 0.115)
- **Predicción de cambio sintético → real:** `misma clasificación` (Weak) con probabilidad alta; `upgrade a borderline Strong` posible si FAOSTAT granular reduce ruido agregativo; `downgrade a Trend` improbable porque la señal sintética ya cruza el umbral p<0.05 con CI estrecho.
- **Margen aceptable:** `|ΔEDI_real − 0.192| ≤ 0.10`
- **Justificación física breve:** Carpenter (2005) predice acumulación irreversible de fósforo reactivo con dinámica bilineal F·P. La sonda `bilinear` captura precisamente ese término; FAOSTAT granular (RP — Reactive Phosphorus por país×cultivo) reduce el ruido del agregado WB `AG.CON.FERT.ZS` (kg/ha mezclando N+P+K). Se espera señal modesta pero significativa.

**Sesgo declarado:** el sintético ya está hecho (commit `88a58df…`) con EDI=0.192, p=0.014. Este pre-registro congela el protocolo para la re-corrida con datos FAOSTAT más granulares y bloquea cualquier modificación de sonda/umbrales. El resultado previo sesga hacia Weak.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `bilinear` (definida en `common/ode_models.py`, `ode_key="ph"`)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico` (perfil agresivo `n_perm=2999, n_boot=1500` queda como auditoría secundaria opcional, **post**-corrida confirmatoria)
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (concentración P reactiva agregada o consumo P inferido vía fertilizer-use balance)
- **Ventana temporal:** `1966-01-01 a 2022-01-01` (`real_start`/`real_end` de `case_config.json`; ventana extensa porque FAOSTAT cubre desde 1961)
- **Tratamiento de datos faltantes:** interpolación lineal sobre serie agregada (FAOSTAT reporta gaps por país pre-1980)
- **Agregación temporal:** anual (`freq: YS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `https://faostatservices.fao.org/api/v1/en/data/RFN?elements=5157&items=3103&year=1961-2022` (FAOSTAT Inputs / Fertilizers by Nutrient, P2O5 específicamente, granularidad país×año; reemplaza WB `AG.CON.FERT.ZS` actual que agrega NPK)
- **Indicadores específicos:**
  - FAOSTAT `RFN`: item 3103 (Phosphate fertilizers, P2O5), element 5157 (agricultural use, tonnes)
  - Fallback secundario: FAOSTAT `RT` (Fertilizers Trade) para validación cruzada producción↔consumo
- **Países / región / agregación:** WLD (agregado global FAOSTAT) como serie principal; opción de top-10 productores (CHN, IND, USA, BRA, RUS, FRA, DEU, CAN, AUS, IDN) como cross-check
- **Fecha de descarga prevista:** `2026-05-19`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/22_caso_fosforo/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; cerrar caso; revisar si la granularidad reduce ruido tan agresivamente que sugiere correlación espuria país-nivel |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso (resultado esperado) |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; revisar mismatch sonda↔dataset |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia |

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
