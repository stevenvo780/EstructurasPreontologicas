# Pre-registro EDI — caso `30_caso_behavioral_dynamics`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con OSF.

## 1. Header

- **Caso:** `30_caso_behavioral_dynamics` — Locomoción dirigida (Fajen & Warren 2003; sonda `behavioral_attractor` de segundo orden)
- **Fecha de pre-registro:** `2026-05-17` (firma previa al B-T2 que reemplaza el sintético basado en ecuación publicada por captura de movimiento humano real)
- **Pre-registrador:** asistencia IA bajo dirección de Steven Vallejo
- **Commit del repo en el momento del registro:** `c6b3d3b2bbe21b28c8afc0a3e1c740eca55fc3b0`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `Weak` (con cola hacia `Null`; basada en `outputs/metrics.json` sintético actual: EDI = 0.133, p = 0.354, CI = [−0.164, 0.364]; p no significativo, CI cruza cero, pero el README declara EDI=0.262 p=0.044 bajo perfil agresivo)
- **Predicción de cambio sintético → real:** `downgrade probable` (de Weak sintético a Trend o Null sobre datos reales); fundamento: el sintético usa la **ecuación completa de segundo orden** (datos generados con `b=3.25, k_g=7.5, c1=0.4, c2=0.4, d_g=4.0` exactos), mientras que datos humanos reales (VENLab, OpenLocomotionData) incluyen ruido perceptivo no-Gaussiano, diferencias inter-individuales fuertes y estrategias de control mixtas que la sonda `behavioral_attractor` no captura. `Upgrade a Strong` improbable.
- **Margen aceptable:** `|ΔEDI_real − 0.133| ≤ 0.15` (margen amplio por la transición sintético→humano y el ruido perceptivo declarado en Fajen-Warren 2003)
- **Justificación física breve:** Fajen & Warren (2003) reportan que el modelo de heading captura ~70% de la varianza inter-trial en VENLab pero deja residuos sistemáticos en trayectorias con metas múltiples. El cierre operativo medible vía EDI depende de que el ABM 40×40 con difusión 0.15 y ruido motor 0.005 sea representativo de la variabilidad inter-sujeto real, supuesto fuerte.

**Sesgo declarado:** el sintético ya está hecho (commit `55c5287…`) con EDI=0.133 canónico y EDI=0.262 reportado bajo perfil agresivo en README. Este pre-registro congela el protocolo (incluyendo el perfil **canónico** como confirmatorio, no el agresivo) y bloquea cambios de sonda. La tensión entre EDI canónico/agresivo en el README es información que sesga la predicción hacia Weak/Trend.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `behavioral_attractor` (definida en `common/ode_models.py`, `ode_key="heading_error"`); ecuación de segundo orden con `b=3.25, k_g=7.5, c1=0.4, c2=0.4, d_g=4.0, dt=0.05` (parámetros publicados Fajen-Warren 2003)
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` — declarar: `canónico` (el perfil agresivo `n_perm=2999, n_boot=1500` queda como auditoría secundaria opcional, **post**-corrida confirmatoria; no como criterio de cierre)
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación:** `value` (heading_error φ, ángulo entre heading instantáneo y vector hacia meta, en radianes)
- **Ventana temporal:** `2000-01-01 a 2010-01-01` nominal (mapeo abstracto; datos humanos reales se re-mapean al rango temporal por trial; ver `src/data.py`)
- **Tratamiento de datos faltantes:** exclusión de registro (trials con frame-drop >5% se descartan, política estándar VENLab)
- **Agregación temporal:** mensual nominal (`freq: MS`); 121 puntos por dataset agregado

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** Datasets de captura de movimiento humano públicos. Opciones (declarar la elegida en `FETCH_MANIFEST.json` **antes** de la corrida):
  - VENLab Brown University: `https://www.brown.edu/research/labs/perception-action-lab/` (requiere request de acceso a Warren lab; LoE=4 si concedido)
  - OpenLocomotionData: `https://github.com/UM-LoCoLab/OpenLocomotionData` (público, treadmill + overground; LoE=3)
  - WALK-MS dataset (Mendeley Data, doi:10.17632/wsvhfjxd33.1; LoE=3)
- **Indicadores específicos:** trayectorias x(t), y(t), heading θ(t) muestreadas a ≥60 Hz; cálculo de heading_error φ(t) = θ(t) − atan2(goal_y − y, goal_x − x)
- **Países / región / agregación:** sujetos pooled del dataset elegido (≥20 sujetos, ≥10 trials cada uno); declarar criterio de inclusión exacto en `FETCH_MANIFEST.json`
- **Fecha de descarga prevista:** `2026-05-22`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/30_caso_behavioral_dynamics/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; cerrar caso; auditar si la sonda `behavioral_attractor` no está sobre-ajustando a la estructura de la captura |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso (resultado más probable según predicción) |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; opción de `@multi-probe-runner` con sonda informacional (exploratoria) |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (umbrales, sondas, splits, parámetros `fw_b, fw_k_g, fw_c1, fw_c2, fw_d_g, fw_dt`)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario cambiar alguno, se reporta como **análisis exploratorio post-hoc**, no confirmatorio, y se firma un pre-registro nuevo para una corrida adicional con datos independientes (sujetos distintos del primer fetch).

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza `Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context)
