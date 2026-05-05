# Diagnóstico de los 8 casos categorizados `null` en el corpus EDI

**Fecha:** 2026-04-29
**Motivo:** El README del corpus afirma "8 casos null con EDI ≤ 0" y describe en una línea que "la sonda específica no captura un acoplamiento dinámico genuino". Esa descripción es honesta pero no diagnóstica. Este documento da el diagnóstico caso por caso (sonda, datos, métricas, brecha sintético→real, lectura) sin re-ejecutar nada.

**Fuente de verdad:** `09-simulaciones-edi/<caso>/outputs/metrics.json` y `case_config.json`. Si la prosa contradice el JSON, gana el JSON (regla 4 de `CLAUDE.md`).

---

## Corrección preliminar al README

La afirmación "8 con EDI ≤ 0" es **falsa**. Los 8 casos en categoría taxonómica `null` se distribuyen así:

- **7 con EDI ≤ 0** (acoplar el ODE *empeora* o no mejora el RMSE): 02, 03, 12, 17, 23, 25, 29.
- **1 con EDI > 0 pero permutación no significativa**: caso 19 (EDI=+0.728, p=0.490). Magnitud aparente sin firma estadística distinguible del null.

La etiqueta `null` viene del Emergentómetro (`emergence_taxonomy.category`), no del signo del EDI. La regla operativa es: **null ≡ no hay evidencia de cierre operativo bajo la sonda elegida**, sea por EDI ≤ 0, sea por EDI positivo no significativo. El README debe corregirse en consecuencia.

---

## Diagnóstico por caso

Formato: **ODE/sonda · drivers · datos · EDI sint→real · p · firma C1-C5+ · lectura**.

### 02 conciencia colectiva — `null`, nivel 0

- **Sonda ODE:** `logistic_forced` (Global Workspace Theory como logística forzada).
- **Drivers exógenos:** suicide_rate, tertiary_enrollment.
- **Datos:** sintéticos derivados de literatura EEG, 20 pasos anuales, `is_synthetic=true`, sin ground truth fenoménico (declarado en `FETCH_MANIFEST.json: limitation`).
- **EDI:** sintético −0.007, real −0.117. Negativo en ambas fases.
- **p-valor permutación real:** 0.92.
- **Correlaciones obs:** ABM 0.44, ODE 0.44 (moderadas).
- **C1-C5+ que fallan:** symploke, no-localidad. C1 absoluto pasa, C1 relativo no.
- **Lectura:** El acoplamiento ABM→ODE no degrada la predicción si se apaga, porque la ODE no añade información que el forzamiento exógeno no aporte ya. Los drivers son proxies sociodemográficos lejanos del fenómeno de interés (consciencia como agregado), y la sonda logística-forzada es genérica, no derivada del modelo GWT que la `Evaluacion_Modelos_Dominio.md` reporta como ideal.
- **Naturaleza del null:** caso piloto declarado, sin observable directo de consciencia. **No falsa la ontología; falsa esta sonda específica para este observable.**
- **Deuda residual:** sustituir drivers por fMRI/MEG agregados con anclaje fisiológico, o reemplazar la sonda por Hopfield/Kuramoto sobre red neural si se quiere defender el caso. Mientras tanto, mantener como null honesto.

### 03 contaminación atmosférica — `null`, nivel 0

- **Sonda ODE:** `mean_reversion` (NO la "Acumulación/Dispersión" que `Evaluacion_Modelos_Dominio.md` declara — disonancia detectada entre doc de modelos y `case_config.json`).
- **Drivers:** gdp_growth, pop_growth.
- **Datos:** AQICN reales, 156 pasos mensuales, panel de 10 ciudades (n_efectivo=1560), `is_synthetic=false`.
- **EDI:** sintético **+0.227 (significativo, p≈0)**, real **−0.090 (p=0.51, no significativo)**.
- **Brecha sintético→real:** ≈0.32. La sonda funciona en el mundo de juguete pero no en datos reales.
- **C1-C5+ que fallan:** emergence_pass, edi_valid. C1 relativo no pasa.
- **Lectura:** La sonda mean-reversion captura una dinámica plausible en sintético calibrado, pero los datos reales de PM2.5 tienen estructura más compleja (factores meteorológicos, regulación, estacionalidad sub-anual) que el panel de drivers macroeconómicos no representa. La brecha sint→real **es la firma del problema**: no es la ontología, es la sonda.
- **Naturaleza del null:** sonda subespecificada para el observable real. Mean-reversion sobre PM2.5 anual con drivers macro no captura la dinámica de mezcla atmosférica.
- **Deuda residual:** reemplazar `mean_reversion` por la sonda dispersión-acumulación que la `Evaluacion_Modelos_Dominio.md` afirma usar; resolver la disonancia entre `case_config.json` y el doc de modelos.

### 12 paradigmas científicos — `null`, nivel 0

- **Sonda ODE:** `mean_reversion` (la `Evaluacion_Modelos_Dominio.md` declara "Landau-Ginzburg" — disonancia).
- **Drivers:** journal_articles, patent_residents.
- **Datos:** OWID educación, 60 pasos mensuales, panel de 8 (n_efectivo=480), `is_synthetic=false`, loe_target=3.
- **EDI:** sintético −0.144, real −0.154. Negativo en ambas fases.
- **p-valor real:** 0.50.
- **Correlaciones obs:** ABM −0.96, ODE +0.30 → **ABM anti-correlaciona** con observable. Signo inconsistente entre micro y macro.
- **C1-C5+ que fallan:** C1 (todas las variantes), emergence_pass.
- **Lectura:** La anti-correlación del ABM con el observable es la firma de que la sonda está mal orientada (signo invertido o variable de estado mal mapeada al observable). Mean-reversion sobre indicadores cienciométricos como proxy de "paradigma" tiene una distancia ontológica grande: el observable cienciométrico no es el sustrato dinámico que postularía Kuhn/Lakatos.
- **Naturaleza del null:** sonda y observable no son co-medibles. La taxonomía `ode_quality=poor` lo confirma.
- **Deuda residual:** o se reemplaza la sonda (Landau-Ginzburg como declarado) y se elige un observable cierre-operativo (no cienciometría agregada), o se mantiene como null honesto. La disonancia con `Evaluacion_Modelos_Dominio.md` debe documentarse.

### 17 océanos (temperatura agregada) — `null`, nivel 0

- **Sonda ODE:** `ocean_thermal`.
- **Drivers:** ninguno (forcing endógeno).
- **Datos:** WMO/PMEL, 34 pasos anuales, `is_synthetic=false`, loe_target=4.
- **EDI:** sintético +0.149, real −0.015. Brecha de 0.16 con cambio de signo.
- **p-valor real:** 1.000 (permutación nula al máximo).
- **Correlaciones obs:** ABM −0.79, ODE −0.78 (altas en magnitud, ambas negativas).
- **C1-C5+ que fallan:** C1, emergence_pass.
- **Lectura:** EDI ≈ 0 en real con p=1 indica que apagar el ODE produce predicciones equivalentes. La temperatura oceánica agregada está dominada por el forcing radiativo de gran escala; el acoplamiento ABM-celular no añade información sobre el agregado anual. **Esto es ontológicamente coherente**: el agregado de temperatura no necesita resolución micro para predecirse a esta escala temporal.
- **Naturaleza del null:** observable mal escogido para el aparato — la temperatura agregada anual es macro-suficiente. La ontología ABM↔ODE no es operativamente relevante a esta resolución.
- **Deuda residual:** o se baja la resolución temporal (mensual/diaria) donde la dinámica micro empieza a importar, o se cambia el observable a algo donde el acoplamiento sea no trivial (ej. estratificación, AMOC). Caso 19 (acidificación) usa el mismo dominio físico con resultado distinto.

### 19 acidificación oceánica — `null`, nivel 0 (ANOMALÍA)

- **Sonda ODE:** `acidification` (Revelle factor según `Evaluacion_Modelos_Dominio.md`).
- **Datos:** PMEL/NOAA pH proxy, 31 pasos anuales, panel 8 (n_efectivo=2880), `is_synthetic=false`, loe_target=3.
- **EDI:** sintético +0.00004 (≈0), real **+0.728**.
- **p-valor real:** **0.490** (no significativo).
- **Correlaciones obs:** ABM −0.67, ODE −0.93 (altas).
- **C1-C5+ que fallan:** C1, C2 robustez, emergence_pass.
- **Lectura:** EDI alto en magnitud pero permutación no rechaza H0 → la diferencia RMSE coupled vs no-coupled está dentro del rango de la distribución nula. C2 (robustez) falla → probable sobreajuste a la ventana de validación. El sintético produce EDI ≈ 0 (la sonda calibrada no genera señal): si el caso real produce EDI=0.73, **el resultado es dudoso, no falsable, no celebrable**.
- **Naturaleza del null:** **anomalía estadística**, no null por sonda inadecuada. El aparato es honesto al clasificarlo `null` a pesar del EDI alto: la falta de significancia + falta de robustez → no hay evidencia de cierre operativo defendible.
- **Deuda residual prioritaria:** investigar por qué el sintético produce EDI≈0 mientras el real produce 0.73. Hipótesis: el sintético no reproduce la deriva temporal del pH real, y la sonda Revelle real está aprovechando una correlación espuria con la tendencia. Re-ejecutar con `n_perm=2999` y bloque-permutación temporal antes de cualquier afirmación. **Este caso no debe usarse como evidencia ni positiva ni negativa hasta resolverlo.**

### 23 erosión dialéctica — `null`, nivel 0

- **Sonda ODE:** `prestige_competition` (Abrams-Strogatz según `Evaluacion_Modelos_Dominio.md`).
- **Datos:** sintéticos de proxy literario, 19 pasos anuales, `is_synthetic=true`, loe_target=1, **limitación declarada**: "Erosión dialéctica no tiene observable directo; piloto conceptual".
- **EDI:** sintético −0.019, real **−1.000** (tope inferior numérico).
- **p-valor real:** 1.000.
- **Correlaciones obs:** ABM 0.99, ODE 0.99 (ambas casi perfectas, **lo cual es sospechoso**).
- **C1-C5+ que pasan:** todos excepto edi_valid y cr_valid.
- **Lectura:** EDI=−1.0 es el extremo: `RMSE_coupled` es muchísimo peor que `RMSE_no_ode`. Pero ambas correlaciones son ≈0.99 — ABM y ODE replican el observable con casi perfecta correspondencia, simultáneamente. Esto es marca de **sintético sobre-ajustado**: cuando los datos son construidos a partir de la sonda, todo correlaciona, pero la intervención ablativa expone que el ODE no aporta información estructural — lo que ya estaba dicho en la limitación del manifest.
- **Naturaleza del null:** caso piloto conceptual sin observable real. **Es honesto. No celebrar, no descartar — declarar como deuda explícita.**
- **Deuda residual:** sin observable directo de "erosión dialéctica", el caso no puede subir de loe=1. Mantener como ejemplo de sonda sin datos.

### 25 acuíferos — `null`, nivel 0

- **Sonda ODE:** `aquifer_darcy` (Darcy-Theis según `Evaluacion_Modelos_Dominio.md`).
- **Datos:** USGS GRACE proxy, 21 pasos anuales con cobertura **0.51** (la mitad de los puntos faltan), val_steps=19, `is_synthetic=false`, loe_target=3.
- **EDI:** sintético −0.022, real −0.146.
- **p-valor real:** 1.000.
- **Correlaciones obs:** ABM 0.99, ODE 0.96 (altas).
- **C1-C5+ que fallan:** C2 robustez, emergence_pass.
- **Lectura:** Cobertura de datos al 51% es el factor dominante: con la mitad de los puntos imputados/faltantes, la calibración converge pero no es robusta (C2 fail). EDI ligeramente negativo + p=1 → el ODE no añade información sobre el observable agregado a esta resolución. Combinado con cobertura baja, el null es razonable.
- **Naturaleza del null:** **datos insuficientes** + sonda dimensionada para resolución mensual operando sobre datos anuales con huecos. No hay evidencia de cierre operativo, pero tampoco de su ausencia firme.
- **Deuda residual:** re-correr con datos GRACE mensuales completos (cobertura ≈100%) antes de declarar el null cerrado. Mientras tanto, null por insuficiencia de datos, no por inadecuación de sonda.

### 29 IoT (Internet of Things) — `null`, nivel 0

- **Sonda ODE:** `bilinear` (declarado log_transform=true).
- **Datos:** Statista IoT proxy + ITU, 33 pasos anuales, cobertura 0.87, `is_synthetic=false`, loe_target=3.
- **EDI:** sintético −0.010, real **−0.876** (cerca del tope inferior).
- **p-valor real:** 1.000.
- **Correlaciones obs:** ABM 0.94, ODE 0.94.
- **C1-C5+ que fallan:** C1, C2 robustez, persistence_pass.
- **Lectura:** EDI=−0.88 con correlaciones altas en ambas variantes indica que el ODE bilineal, una vez aplicado en log-espacio, **degrada activamente** la predicción del ABM. La adopción IoT real tiene saltos exponenciales y discontinuidades (Metcalfe + difusión Bass) que un modelo bilineal genérico no acomoda. La transformación logarítmica enmascara el problema en sintético (donde la curva es suave) pero lo amplifica en real (donde hay saltos).
- **Naturaleza del null:** **sonda mal especificada** para la dinámica observada. Bilinear log-transformado no es la familia funcional adecuada para difusión tecnológica con efectos de red.
- **Deuda residual:** sustituir por Bass diffusion explícito (caso 13 lo usa con éxito) o por una difusión con saturación. La `Evaluacion_Modelos_Dominio.md` declara "Difusión Tecnológica + Network Effects (Metcalfe)" como modelo ideal — disonancia con el `bilinear` del `case_config.json`.

---

## Síntesis: por qué cada null es null

| Caso | Causa dominante del null |
|------|--------------------------|
| 02 conciencia | Datos sintéticos sin ground truth + drivers proxy + sonda logística genérica |
| 03 contaminación | Sonda mean-reversion subespecificada para PM2.5 panel; brecha sint→real grande |
| 12 paradigmas | Anti-correlación ABM-obs → sonda y observable no co-medibles |
| 17 océanos | Observable agregado anual macro-suficiente (no necesita micro) |
| **19 acidificación** | **Anomalía: EDI alto sin significancia ni robustez (no clasificable, requiere reanálisis)** |
| 23 erosión dialéctica | Caso piloto sin observable real (declarado en manifest) |
| 25 acuíferos | Cobertura de datos al 51% (insuficiencia, no inadecuación) |
| 29 IoT | Sonda bilineal mal especificada para difusión tecnológica con saltos |

**Lectura general:** los 8 nulls **no son una falla del aparato** ni evidencia contra la ontología general. Son la firma operativa de tres condiciones distintas:

1. **Sonda inadecuada para el observable** (02, 03, 12, 17, 29).
2. **Datos insuficientes o sintéticos sin anclaje** (02, 23, 25).
3. **Anomalía estadística sin resolver** (19).

El aparato distingue cierre operativo genuino (strong/weak con p<0.05 y C1-C5+ que pasan) de su ausencia. Lo que estos 8 casos demandan es **deuda declarada por caso**, no defensa retórica de la categoría agregada.

---

## Disonancias detectadas entre `Evaluacion_Modelos_Dominio.md` y `case_config.json`

Tres casos null tienen sondas declaradas en el doc de evaluación que **no coinciden** con la sonda ejecutada:

| Caso | Doc declara | `case_config.json` ejecuta |
|------|-------------|---------------------------|
| 03 contaminación | Acumulación/Dispersión | mean_reversion |
| 12 paradigmas | Landau-Ginzburg | mean_reversion |
| 29 IoT | Difusión + Metcalfe | bilinear |

Esto es **deuda independiente** de los nulls: o el doc se actualiza para reflejar lo que el repo ejecuta, o los `case_config.json` se actualizan para usar la sonda declarada. La afirmación del doc "100% modelos personalizados" no se sostiene en estos tres casos.

---

## Acciones siguientes

1. **README §Casos null:** corregir el conteo ("8 con EDI ≤ 0" → "7 con EDI ≤ 0 + 1 anómalo con EDI alto sin significancia") y reemplazar la línea genérica por la tabla de causas.
2. **TAREAS_PENDIENTES.md:** añadir entradas de deuda para (a) anomalía caso 19 prioritaria, (b) disonancias doc↔config en 03/12/29, (c) re-ejecución con datos completos en 25.
3. **No tocar `metrics.json` ni etiquetas taxonómicas.** Los nulls son honestos. Lo que cambia es la prosa que los explica.
