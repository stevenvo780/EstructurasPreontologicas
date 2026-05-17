# Pre-registro EDI — caso `28_caso_fuga_cerebros`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `28_caso_fuga_cerebros` — Fuga de Cerebros Global (Docquier-Rapoport)
- **Fecha de pre-registro:** `2026-05-17`
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `744724e565f6027b7f29eae919c32e8aaf2f197d`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Null` (basada en `outputs/metrics.json` previo: EDI_real ≈ 0.025, p ≈ 0.997, CI [-0.154, 0.187] cruza cero → null inequívoco)
- **Predicción de cambio sintético → real:** `misma clasificación` (sintético: EDI≈-0.006 null; real: EDI≈0.025 null). El multi-driver WB (researchers, enrollment, remittances, GDP pc, net migration) no genera coupling detectable por la sonda `brain_drain` declarada.
- **Margen aceptable:** `|ΔEDI_real_v2 − 0.025| ≤ 0.08`
- **Justificación física breve:** la fuga de cerebros es proceso multi-país con heterogeneidad fuerte origen-destino (Docquier-Rapoport 2012); el agregado WLD pierde la señal bilateral. La sonda agregada `brain_drain` con `ode_drain_threshold=1.5` modela switch en un solo proxy (`rd_gdp` = R&D % PIB), perdiendo la asimetría migratoria. Predicción: null hasta que el caso se desdoble a panel bilateral (origen, destino).

**Sesgo declarado:** primera corrida ya ejecutada y arrojó null. Este pre-registro congela el protocolo agregado para reportar honestamente la limitación y deja la reformulación bilateral como pre-registro futuro independiente.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `brain_drain` (definida en `common/ode_models.py`, `ode_key="fc"`, params `ode_alpha=0.06, ode_beta=0.02, ode_gamma_forcing=0.08, ode_delta_drain=0.015, ode_drain_threshold=1.5`)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico`
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (`GB.XPD.RSDV.GD.ZS` — gasto en I+D como % del PIB, World Bank WLD agregado)
- **Drivers multivariados:** `researchers` (SP.POP.SCIE.RD.P6), `enrollment` (SE.TER.ENRR), `remittances` (BX.TRF.PWKR.DT.GD.ZS), `gdp_pc` (NY.GDP.PCAP.KD), `net_migration` (SM.POP.NETM)
- **Ventana temporal:** `1980-01-01 a 2022-01-01` (campo `real_start`/`real_end` de `case_config.json`)
- **Tratamiento de datos faltantes:** interpolación lineal (`limit_direction="both"`, ya implementado en `src/data.py`)
- **Agregación temporal:** anual (`freq: YS`)

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `https://api.worldbank.org/v2/country/WLD/indicator/GB.XPD.RSDV.GD.ZS?format=json&per_page=500` (+ 5 indicadores adicionales vía `worldbank_universal_fetcher.fetch_worldbank_indicator`)
- **Indicadores específicos (códigos WB):** `GB.XPD.RSDV.GD.ZS`, `SP.POP.SCIE.RD.P6`, `SE.TER.ENRR`, `BX.TRF.PWKR.DT.GD.ZS`, `NY.GDP.PCAP.KD`, `SM.POP.NETM`
- **Países / región / agregación:** WLD (agregado mundial); deuda declarada: el agregado oculta asimetría bilateral origen-destino
- **Fecha de descarga prevista:** `2026-05-18`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/28_caso_fuga_cerebros/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; investigar overfitting (sorpresa fuerte) |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; opción de reformular a panel bilateral en pre-registro nuevo |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (umbrales, sondas, splits)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario reformular a panel bilateral (Docquier-Rapoport completo), se trata como **caso nuevo** (`28b_caso_fuga_cerebros_bilateral`), no como re-especificación post-hoc; requiere pre-registro nuevo.

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza `Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
