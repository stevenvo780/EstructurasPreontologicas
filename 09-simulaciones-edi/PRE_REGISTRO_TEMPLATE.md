# Pre-registro EDI — caso `<NN>_caso_<nombre>`

> Plantilla de pre-registro pre-ejecución (B-T2). Bloquea el "garden of forking paths" (Gelman & Loken 2014) fijando hipótesis, especificación analítica y criterios de cierre **antes** de ver los datos reales. Compatible con Open Science Framework (OSF).

## 1. Header

- **Caso:** `<NN>_caso_<nombre>`
- **Fecha de pre-registro:** `YYYY-MM-DD` (anterior a primera ejecución sobre datos reales)
- **Pre-registrador:** `<Nombre> (<rol: Jacob / Steven / asistencia>)`
- **Commit del repo en el momento del registro:** `<git rev-parse HEAD>`

## 2. Hipótesis y predicciones

- **H0 (clasificación predicha):** `<Strong | Weak | Trend | Null>` (basada en sintético previo o teoría)
- **Predicción de cambio sintético → real:** `<misma clasificación | downgrade | upgrade>`
- **Margen aceptable:** `|ΔEDI_real − EDI_sintético| ≤ <X>`
- **Justificación física breve (≤ 3 líneas):** `<por qué se predice esa clasificación>`

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `<idéntica a la usada en sintético; nombre exacto en `common/ode_models.py`>`
- **Hiperparámetros:**
  - `n_perm = 999`, `n_boot = 500` (canónico) **o** `n_perm = 2999`, `n_boot = 1500` (agresivo) — declarar: `<canónico | agresivo>`
  - `seed = 42`
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` **o** `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` **o** `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Variable de observación (indicador empírico):** `<nombre exacto de la columna / serie>`
- **Ventana temporal:** `<YYYY-MM-DD a YYYY-MM-DD>` (default: 1990-01-01 a 2022-12-31)
- **Tratamiento de datos faltantes:** `<interpolación lineal | forward fill | exclusión de registro>` (declarar uno solo)
- **Agregación temporal:** `<diaria | mensual | anual>`

## 4. Fuente de datos (API / dataset público)

- **URL exacta:** `<https://…>`
- **Indicador específico (código API):** `<p. ej. EN.ATM.CO2E.KT>`
- **Países / región / agregación:** `<lista ISO-3 o región>`
- **Fecha de descarga prevista:** `YYYY-MM-DD`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; registrar aquí en commit posterior>`

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/<NN>_caso_<nombre>/src/validate.py --seed 42`:

| Resultado observado | Clasificación | Acción |
|---|---|---|
| `EDI ∈ [0.33, 0.65]` con `p < 0.05` | **Strong** | Reportar; cerrar caso |
| `EDI ∈ [0.10, 0.33)` con `p < 0.05` | **Weak** | Reportar; cerrar caso |
| `EDI ∈ [0.05, 0.10)` o `p ∈ [0.05, 0.10)` | **Trend** | Reportar; declarar deuda de potencia |
| `EDI < 0.05` o `p ≥ 0.10` con CI cruzando cero | **Null genuino** | Reportar como null; opción de `@multi-probe-runner` (declarada como exploratoria, no confirmatoria) |
| `EDI < 0` con CI excluyendo cero por la izquierda | **Falsificación local del aparato** | Reportar como contraevidencia; revisar sonda en sección crítica |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución sobre datos reales **no se modifica**:

- `case_config.json` (ni umbrales, ni sondas, ni splits)
- `src/data.py` (pipeline de ingesta y limpieza)
- `src/ode.py`, `src/abm.py` (modelos)
- Hiperparámetros declarados en §3

Si tras ver el resultado se considera necesario cambiar alguno, se reporta como **análisis exploratorio post-hoc**, no como resultado confirmatorio, y se firma un pre-registro nuevo para una segunda corrida con datos independientes.

Si el resultado no coincide con la predicción de §2, se reporta honestamente como **contraevidencia** en `outputs/report.md` y se actualiza la clasificación del caso en `09-simulaciones-edi/Evaluacion_Modelos_Dominio.md`.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `YYYY-MM-DD`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `YYYY-MM-DD`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): `<modelo + versión>`
