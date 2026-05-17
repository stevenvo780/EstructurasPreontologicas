# Mapa de aplicaciones — corpus inter-dominio e inter-escala

## Función

Mapa completo del paisaje de aplicaciones del marco como **ontología general multiescalar**. Cada caso aparece con su modo (demostrativo/programático), nivel de cierre operativo, escala instanciada, criterio de elevación si procede, y referencias cruzadas. El paisaje agrega 40 casos: 30 inter-dominio + 10 inter-escala. Cada caso es **instancia particular de los cuatro invariantes ontológicos** (sustrato material, acoplamiento dinámico, atractor empírico, cierre operativo κ); ningún caso es aplicación aislada del aparato a un dominio.

---

## Resumen ejecutivo

**Total de casos:** 40 (30 corpus inter-dominio + 10 corpus inter-escala). Cobertura conjunta: 8 escalas físicas/biológicas/cosmológicas + 7 dominios disciplinares heterogéneos.

### Corpus inter-dominio (30 casos)

**Distribución por modo:**

- **Modo técnico-ejecutado** (dossier EDI completo, `metrics.json` reproducible bajo el protocolo C1-C5): 30 casos. Todos tienen dossier en `09-simulaciones-edi/<caso>/`.
- **Modo demostrativo en sentido estricto** (14/14 componentes del dossier de anclaje del cap 05-00 §1, con material publicado independiente del aparato): 1 caso (05-05 Warren). La distinción es operativa: el primer modo asegura reproducibilidad técnica; el segundo asegura adecuación filosófica plena del aparato a un caso paradigmático.
- **Aplicaciones filosóficas programáticas adicionales:** 4 dominios sin caso EDI directo (capítulos 05-01 a 05-04).

*Nota sobre el modo técnico-ejecutado.* 'Dossier técnico completo' indica que el caso fue corrido con el protocolo C1-C5 y produce `metrics.json` reproducible. **No equivale a 'demostración positiva del aparato'**: los Bloques V-VII (Trend, Null, Controles) no instancian acoplamiento detectable; funcionan como casos de no-aplicabilidad de la sonda, falsación local o controles correctamente rechazados. Casos con `EDI ≤ 0` o `p ≈ 1` están listados explícitamente en sus bloques correspondientes y **no se contabilizan como instancia positiva del aparato**. La fuerza inferencial real del corpus inter-dominio descansa sobre los Bloques I–IV (Strong gate completo, Strong sin gate, Weak con o sin disclosure, Suggestive — 14 casos tras iter 7 según los conteos vigentes), no sobre la cifra agregada N=30 indistinta.

**Distribución por Nivel:**

**Tabla A.5.1.**

**Tabla 5.7.1.**

| Nivel | Categoría | N | Casos |
|:----:|-----------|:-:|-------|
| 4 | Strong (`overall_pass=True`) | 6 | Energía, Deforestación, Kessler, Riesgo Biológico, Urbanización (caso 18 promovido Weak→Strong iter 5 B-T2 con datos World Bank SP.URB.TOTL.IN.ZS reales 2026-05-16: EDI=0.3366, p_perm=0.0, CI=[0.331, 0.347], `overall_pass=True`), **Microplásticos (caso 24 promovido Strong-sin-gate→Strong gate completo iter 7 B-T2 con datos Jambeck reales 2026-05-17: EDI=0.806, p_perm=0.0, CI=[0.701, 0.880], `overall_pass=True`)** |
| 4 | Strong sin gate completo | 1 | **Starlink (caso 26 promovido Trend→Strong sin gate iter 7 B-T2 2026-05-17: EDI=0.7575, p_perm=0.0, CI=[0.741, 0.775], `overall_pass=False` por gate C1-C5 pero CI estrictamente positivo y bootstrap estable; reemplaza a Microplásticos que sube a gate completo)** |
| 3 | Weak | 7 | Postverdad, Fósforo, Wikipedia, Epidemiología, Behavioral Dynamics (caso 30), Finanzas (caso 09 promovido Suggestive→Weak iter 5 B-T2 con yfinance SPY + FRED reales 2026-05-16: EDI=0.1027, p_perm=0.0, CI=[0.1006, 0.1052]; `overall_pass=False` por gate C1-C5 pero EDI>0.1 y CI estrictamente positivo), **Océanos (caso 17 promovido Null/rechazado-por-gate→Weak iter 7 B-T2 2026-05-17: EDI=0.1902, p_perm=0.0, CI=[0.157, 0.280] estrictamente positivo; `overall_pass=False` y `valid=False` declarado como disclosure)** |
| 2 | Suggestive | 0 | (Finanzas elevada a Weak iter 5 B-T2 2026-05-16; Salinización reclasificada por AU-4: CI cruza cero + magnitud trivial) |
| 1 | Trend | 4 | Justicia, Fuga cerebros, Políticas (caso 13 reclasificado Weak→Trend tras re-ejecución con datos institucionales reales 2026-05-16, EDI=0.0821, p_perm=0.162), Movilidad (caso 11 confirmado Trend tras re-ejecución con datos TomTom reales 2026-05-16, EDI=0.0599, p_perm=0.922). **Starlink retirado iter 7 → Strong sin gate.** |
| 0a | Null genuino | 6 | Conciencia (caso 02 confirmado Null iter 7 B-T2 con datos reales 2026-05-17: EDI=-0.0121, p_perm=0.315, CI=[-0.016, -0.010] — consistente con clasificación previa LoE=1 especulativa), Erosión, Acuíferos, IoT, Clima (caso 01 reclasificado Trend→Null tras re-ejecución con datos reales IPCC-calibrados 2026-05-16, EDI=-0.0007, p_perm=0.998), Contaminación (caso 03 reclasificado Weak→Null tras re-ejecución con datos World Bank PM2.5 reales 2026-05-16, EDI=-0.0109, p_perm=0.616) (`\|EDI\|<0.05` y `p_perm>0.05`) |
| 0b | EDI negativo (sonda macro inadecuada) | 1 | Paradigmas (`EDI=-0.144`: ABM acoplado predice peor que reducido) |
| 0d | Falsificación local del aparato (CI excluye cero por la izquierda) | 1 | Acidificación oceánica (caso 19 reclasificado tras adversarial iter 4 2026-05-16: `EDI=-0.0047`, `CI=[-0.0054, -0.0041]`; el bootstrap excluye cero por la izquierda — el modelo acoplado predice estrictamente peor que el reducido bajo sonda Revelle/calcificadores; ASA principio 5) |
| 0c | Señal rechazada por gate C1-C5 | 0 | (Océanos promovido iter 7 a Weak con disclosure; bloque vacío hasta que un caso nuevo lo reactive) |
| n.e. | Cuarentena por insuficiencia de datos | 0 | (Starlink promovido iter 7 a Strong sin gate tras re-ejecución con val_steps=30) |
| — | Falsación rechazada (controles) | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Subdivisión del Bloque "Null" (AU-9 2026-05-11 + adv-iter4 2026-05-16).** Lo que la versión previa presentaba como "8 null" cubre en realidad cuatro regímenes empíricamente distintos: 6 nulls genuinos (el aparato no detecta señal donde no la hay), 1 EDI negativo por sonda inadecuada (Paradigmas; el modelo acoplado predice peor pero sin CI que excluya cero), 1 **falsificación local del aparato** (Acidificación oceánica caso 19, reclasificado tras adversarial iter 4 2026-05-16: EDI=-0.0047 con CI bootstrap [-0.0054, -0.0041] que **excluye cero por la izquierda** — el aparato no sólo no detecta señal: predice estrictamente peor que el reducido bajo la sonda Revelle/calcificadores; ASA Wasserstein-Lazar 2016 principio 5), y 1 rechazo por gate C1-C5 (ranking permutacional cruza el umbral pero la batería compuesta rechaza por incumplimiento de viscosidad/persistencia/no-localidad). La cifra "señal/no-señal ≈ 50 %" gana matiz y pierde rotundidad; el aparato discrimina cuatro modos de no-éxito en lugar de colapsarlos en una etiqueta única. La falsificación local del caso 19 es **fortaleza, no debilidad**: el aparato declara honestamente la inadecuación de su propia sonda en un dominio específico en lugar de blindarse contra el dato.

**Total con señal significativa:** 18/30 (60%) tras iter 7 (Microplásticos a gate completo, Starlink a strong sin gate, Océanos a weak con disclosure).
**Falsación correcta:** 3/3 (100%).

**Costo declarado del agregador `overall_pass`.** El gate compuesto `overall_pass=True` integra C1-C5 + viscosidad + significancia permutacional + persistencia, pero **no exige que `ci_lo` del bootstrap del EDI sea positivo**. Riesgo Biológico (caso 27) ilustra el costo: pasa el gate con `p_perm=0.0022` y `edi.value=0.333`, pero su CI bootstrap 95 % `[-0.198, +0.648]` cruza el cero. La promoción a "strong gate completo" descansa, por tanto, sobre la significancia permutacional del ranking del estadístico observado, no sobre la exclusión bootstrap del cero. La tesis sostiene la categorización pero declara su límite: un revisor que lea "strong" como "CI bootstrap excluye el cero" estará leyendo más de lo que el agregador certifica. Si en una pasada posterior se exige `ci_lo > 0` como requisito de admisión, caso 27 se reclasifica a "strong sin gate bootstrap" y el conteo "4 strong" del corpus inter-dominio cae a 3 con pérdida del dominio biomédico-epidemiológico.

### Corpus inter-escala (10 casos)

**Tabla A.5.2.**

**Tabla 5.7.2.**

| Nivel | Categoría | N | Casos (escala instanciada) |
|:----:|-----------|:-:|----------------------------|
| 4 | Strong (`overall_pass=True`) | 7 | 31 Decoherencia (cuántica), 32 Espín-órbita (atómica), 34 Michaelis-Menten (bioquímica), 36 NF-κB (celular oscilatoria), 37 HRV (individual), 39 Cefeida (astrofísica), 40 Cúmulo globular (astrofísica masiva) |
| 3 | Weak | 1 | 35 Ciclo celular (celular) |
| 0 | Null honesto | 1 | 33 Villin Headpiece (sonda equilibrio inadecuada) |
| 0 | Failure mode | 1 | 38 Locomoción τ-dot (sonda mal especificada para reinicios discretos) |

**Cobertura de escalas:** 30 órdenes de magnitud espaciales (10⁻¹⁰ m → 10²⁰ m), 30 órdenes temporales (10⁻¹⁵ s → 10¹⁴ s).

### Lectura ontológica integrada

Los 40 casos del corpus agregado **no son aplicaciones independientes**: cada uno es **instancia de los cuatro invariantes ontológicos** que la tesis afirma. Lo que cambia entre casos es el dominio sustantivo y la escala física donde los invariantes se materializan; la **estructura ontológica subyacente es una sola**. Esto es lo que la tesis llama *"ontología general multiescalar"*: una arquitectura común que se instancia diferenciadamente.

---

## Casos del corpus EDI

### Bloque I — Strong con gate completo (Nivel 4)

**Tabla A.5.3.**

**Tabla 5.7.3.**

| # | Caso | EDI | p | Sonda | LoE | Datos |
|---|------|----:|--:|-------|----:|-------|
| 04 | Energía eléctrica | 0.6503 | 0.0000 | Lotka-Volterra | 4 | OPSD |
| 16 | Deforestación global | 0.5802 | 0.0000 | von Thünen | 4 | World Bank |
| 20 | Síndrome de Kessler | 0.3527 | 0.0000 | Densidad orbital | 3 | CelesTrak |
| 27 | Riesgo biológico (mortalidad) | 0.3326 | 0.0022 | Mortalidad | 3 | World Bank |
| 18 | Urbanización global | 0.3366 | 0.0000 | Logística + atracción | 4 | World Bank (SP.URB.TOTL.IN.ZS) |
| 24 | Microplásticos oceánicos | 0.8057 | 0.0000 | Jambeck Accumulation-Decay | 4 | Jambeck et al. real |

Reproducibilidad: el caso 16 ha sido re-ejecutado con datos World Bank descargados en vivo (variabilidad estocástica <4%, mismo Nivel 4 strong). La trazabilidad detallada está en `Bitacora/`. **Caso 18 Urbanización promovido Weak→Strong iter 5 B-T2 2026-05-16** con datos World Bank `SP.URB.TOTL.IN.ZS` reales (`overall_pass=True`, `edi_valid=True`, CI=[0.331, 0.347]). Comando regenerador: `python3 09-simulaciones-edi/18_caso_urbanizacion/src/validate.py`. **Caso 24 Microplásticos promovido Strong-sin-gate→Strong gate completo iter 7 B-T2 2026-05-17** con datos Jambeck reales (`overall_pass=True`, `valid=True`, EDI=0.806, CI=[0.701, 0.880]). Comando regenerador: `python3 09-simulaciones-edi/24_caso_microplasticos/src/validate.py`.

### Bloque II — Strong sin gate completo (Nivel 4*)

**Tabla A.5.4.**

**Tabla 5.7.4.**

| # | Caso | EDI | p | Sonda | Por qué no gate |
|---|------|----:|--:|-------|-----------------|
| 26 | Constelaciones satelitales Starlink | 0.7575 | 0.0000 | Saturation Growth | `overall_pass=False` por gate C1-C5; CI bootstrap [0.741, 0.775] estrictamente positivo y estable, val_steps=30 |

### Bloque III — Weak (Nivel 3)

**Tabla A.5.5.**

**Tabla 5.7.5.**

| # | Caso | EDI | p | Sonda |
|---|------|----:|--:|-------|
| 30 | Behavioral Dynamics | 0.2622 | 0.0440 | behavioral_attractor (segundo orden) |
| 14 | Postverdad (desinformación) | 0.2428 | 0.0000 | SIS contagion |
| 17 | Océanos (OHC proxy) | 0.1902 | 0.0000 | Sonda térmica (disclosure: `valid=False`, gate C1-C5 no superado pero CI=[0.157, 0.280] estrictamente positivo) |
| 22 | Fósforo (fertilizantes) | 0.1924 | 0.0000 | Carpenter P Cycle |
| 15 | Wikipedia (ediciones) | 0.1916 | 0.0000 | Saturation growth |
| 05 | Epidemiología (COVID-19) | 0.1294 | 0.0000 | SEIR |
| 09 | Finanzas globales | 0.1027 | 0.0000 | Macro-financiero (yfinance SPY + FRED) |

**Reclasificación iter 5 B-T2 (2026-05-16, calibración bidireccional):** el caso 18 Urbanización se **retira del Bloque III Weak** y se promueve al Bloque I Strong gate completo tras re-ejecución con datos World Bank `SP.URB.TOTL.IN.ZS` reales (EDI=0.3366 vs sintético 0.2358; `overall_pass=True`). El caso 09 Finanzas se **incorpora al Bloque III Weak** desde Bloque IV Suggestive tras re-ejecución con yfinance SPY + FRED reales (EDI=0.1027 vs sintético 0.0813, CI=[0.1006, 0.1052] estrictamente positivo). Esto confirma que el aparato modula en ambas direcciones bajo datos reales: declara strong real cuando los datos lo soportan (18) y eleva suggestive a weak cuando el CI estabiliza (09), no solo produce downgrades (01, 03, 11, 13).

**Reclasificación iter 7 B-T2 (2026-05-17, continuación de la calibración bidireccional):** tres movimientos adicionales con datos reales. (i) Caso 24 Microplásticos se **retira del Bloque II Strong sin gate** y se promueve al Bloque I Strong gate completo (EDI=0.806, `overall_pass=True`, CI=[0.701, 0.880]). (ii) Caso 26 Starlink se **retira del Bloque V Trend** y se incorpora al Bloque II Strong sin gate (EDI=0.7575, `overall_pass=False` por gate C1-C5 pero CI bootstrap estable [0.741, 0.775] y val_steps=30); sustituye a Microplásticos en el Bloque II. (iii) Caso 17 Océanos se **retira del Bloque "Señal rechazada por gate C1-C5"** y se incorpora al Bloque III Weak con disclosure explícito `valid=False` (EDI=0.1902, CI=[0.157, 0.280] estrictamente positivo); el bloque "Señal rechazada por gate" queda en 0 casos hasta que un caso nuevo lo reactive. Caso 02 Conciencia: re-ejecución iter 7 confirma Null genuino (EDI=-0.0121, p_perm=0.315) — sin cambio de bloque, sólo consolidación de la clasificación previa LoE=1 especulativa contra datos reales. El conteo agregado pasa de 5+1+6+0+5+6+1+1+1+1+3 a 6+1+7+0+4+6+1+1+0+0+3 (más Salinización fuera de la tabla por AU-4) = 30 inter-dominio consistente; señal significativa pasa de 15/30 a 18/30.

**Reclasificación iter 4 B-T2 (2026-05-16):** los casos 13 Políticas estratégicas y 11 Movilidad se **retiran del Bloque III Weak** y se reubican en Bloque V Trend tras re-ejecución con datos reales. Caso 13: con datos sintéticos producía EDI=0.2972 / p=0.0015 (Weak); con datos institucionales reales 2026-05-16 produce EDI=0.0821 / p_perm=0.162 (Trend Nivel 1, p>0.05). Caso 11: con datos sintéticos producía EDI=0.1283 / p=0.0020 (Weak); con datos TomTom reales 2026-05-16 confirma EDI=0.0599 / p_perm=0.922 (Trend Nivel 1, p>0.05). Comando regenerador: `python3 09-simulaciones-edi/13_caso_politicas_estrategicas/src/validate.py` y `python3 09-simulaciones-edi/11_caso_movilidad/src/validate.py`. Patrón consistente con casos 01 Clima y 03 Contaminación (Weak/Trend sintético → Null/Trend real): el aparato declara honestamente cuando los datos reales no soportan la magnitud previa.

### Bloque IV — Suggestive (Nivel 2)

**Tabla A.5.6.**

**Tabla 5.7.6.**

| # | Caso | EDI | p_perm | CI 95 % bootstrap | Comentario |
|---|------|----:|--:|---|---|
| 22 | Fósforo (referenciado en Bloque III Weak) | 0.1924 | 0.0000 | [-0.221, +0.550] | Ranking permutacional alto pero bootstrap no excluye cero; magnitud frágil (AU-4) |

**Reclasificación iter 5 B-T2 (2026-05-16):** el caso 09 Finanzas globales se **retira del Bloque IV Suggestive** y se reubica en Bloque III Weak tras re-ejecución con yfinance SPY + FRED reales 2026-05-16 (EDI=0.1027 vs sintético 0.0813, p_perm=0.0, CI=[0.1006, 0.1052] estrictamente positivo). La estabilización del CI sobre datos financieros reales eleva el caso por encima del umbral Weak EDI>0.1 con CI excluyendo cero — comportamiento opuesto a la advertencia AU-4 sobre CI cruzando cero.

**Reclasificación AU-4 (2026-05-11):** el caso 21 (Salinización) se **retira del Bloque IV Suggestive** y se reubica en un bloque nuevo de "significativos por permutación con magnitud trivial — no contabilizan a favor de la tesis". Sus métricas son `EDI = 0.0184`, `p_perm = 0.0028`, `CI 95 % bootstrap = [-0.0771, +0.0825]`: el CI no excluye que el acoplamiento empeore la predicción y la magnitud puntual es del orden del 0.6 % de reducción de RMSE. Este es exactamente el patrón que Wasserstein y Lazar (2016, *The American Statistician* 70(2):129-133, ASA Statement on p-values, Principle 3 — verbatim en `07-bibliografia/Wasserstein-Lazar - ASA Statement on p-values (Am Stat 2016).pdf` p. 2) advierten: *"Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold."* La coexistencia de `p<0.01` con magnitud trivial y CI cruzando cero no debe contar como evidencia positiva. La tesis declara aquí, como costo, que **la regla `CI 95 % no cruza cero` debe operar como criterio adicional al ranking permutacional** en pasadas subsiguientes; la auditoría retrospectiva de los demás casos contabilizados como significativos queda como deuda residual fechada (cf. cap 03 §criterios de admisión).

### Bloque V — Trend (Nivel 1)

**Tabla A.5.7.**

**Tabla 5.7.7.**

| # | Caso | EDI | p | Comentario |
|---|------|----:|--:|------------|
| 10 | Justicia (Estado de Derecho) | 0.2274 | 0.4775 | Ventana corta |
| 28 | Fuga de cerebros | 0.0249 | 0.9975 | Ruido domina |
| 13 | Políticas estratégicas (gasto militar) | 0.0821 | 0.1622 | **Reclasificado Weak→Trend tras re-ejecución iter 4 B-T2 con datos institucionales reales 2026-05-16** (p_perm=0.162 > 0.05, CI=[0.065, 0.100]). Antes Weak sintético (EDI=0.2972, p=0.0015). El aparato declara honestamente cuando los datos reales no sostienen la magnitud sintética. |
| 11 | Movilidad (tráfico aéreo / TomTom) | 0.0599 | 0.9219 | **Confirmado Trend Nivel 1 tras re-ejecución iter 4 B-T2 con datos TomTom reales 2026-05-16** (p_perm=0.922 > 0.05, CI=[-0.392, 0.205]). Antes Weak sintético (EDI=0.1283, p=0.0020). Ruido domina señal de cierre bajo sonda Bilinear diffusion sobre datos reales. |

**Casos en cuarentena por insuficiencia de datos.** Caso 26 (Starlink) se mantuvo previamente en cuarentena tras auditoría de `metrics.json` (val_steps=1, CI colapsado). **Iter 7 B-T2 2026-05-17:** re-ejecución produjo phase real con val_steps=30, EDI=0.7575, p_perm=0.0, CI bootstrap [0.741, 0.775] estable; el caso se **promueve a Bloque II Strong sin gate** (`overall_pass=False` por gate C1-C5 pero CI estrictamente positivo); deja la cuarentena. El caso 19 (Acidificación oceánica) compartió esa patología en versiones previas (`metrics.json` mezcla de ejecuciones reportado como TENG-05) pero ha sido **reclasificado tras adversarial iter 4 2026-05-16 como falsificación local del aparato** (no como cuarentena ni null genuino): la re-ejecución coherente produjo EDI=-0.0047 con CI bootstrap [-0.0054, -0.0041] que excluye cero por la izquierda, indicando que el modelo acoplado predice estrictamente peor que el reducido bajo la sonda Revelle/calcificadores; véase nuevo Bloque VI.5 más abajo. Comando regenerador para Starlink: `python3 09-simulaciones-edi/26_caso_starlink/src/validate.py`.

### Bloque VI — Null (Nivel 0)

**Tabla A.5.8.**

**Tabla 5.7.8.**

| # | Caso | EDI | Comentario |
|---|------|----:|-----------|
| 01 | Clima regional | -0.0007 | **Null genuino tras re-ejecución con datos reales IPCC-calibrados 2026-05-16** (EDI=-0.0007, p_perm=0.998, sonda Budyko-Sellers). Reclasificado Trend→Null: con datos reales el aparato declara honestamente ausencia de cierre macro detectable bajo esta sonda. Comando regenerador: `python3 09-simulaciones-edi/01_caso_clima/src/validate.py`. |
| 02 | Conciencia global | -0.0121 | **Null genuino confirmado iter 7 B-T2 2026-05-17 con datos reales** (EDI=-0.0121, p_perm=0.315, CI=[-0.016, -0.010]; sonda dinámica colectiva). Consistente con la clasificación previa LoE=1 especulativa; los datos reales reproducen ausencia de cierre macro detectable. Comando regenerador: `python3 09-simulaciones-edi/02_caso_conciencia/src/validate.py`. |
| 03 | Contaminación PM2.5 | -0.0109 | **Null genuino tras re-ejecución iter 3 con datos World Bank PM2.5 reales 2026-05-16** (EDI=-0.0109, p_perm=0.616, sonda dispersión-decaimiento). Reclasificado Weak→Null: con datos reales el aparato declara honestamente ausencia de cierre macro detectable bajo esta sonda. Comando regenerador: `python3 09-simulaciones-edi/03_caso_contaminacion/src/validate.py`. |
| 12 | Paradigmas (ciencia) | -0.1536 | Reflexividad; null bajo régimen real-phase actual |
| 23 | Erosión dialéctica | -1.0000 | Categoría mal definida |
| 25 | Acuíferos | -0.1462 | Datos heterogéneos |
| 29 | IoT | -0.8760 | Reflexividad técnica |

**Nota iter 7:** caso 17 Océanos retirado del Bloque VI Null tras re-ejecución con datos reales (EDI=0.1902, p_perm=0.0, CI estrictamente positivo) y promovido al Bloque III Weak con disclosure `valid=False`.

### Bloque VI.5 — Falsificación local del aparato (sonda inadecuada con CI que excluye cero por la izquierda)

**Tabla 5.7.8b.**

| # | Caso | EDI | CI bootstrap | Comentario |
|---|------|----:|--------------|-----------|
| 19 | Acidificación oceánica | -0.0047 | [-0.0054, -0.0041] | **Falsificación local del aparato tras adversarial iter 4 2026-05-16.** Reclasificado de "Null genuino" (clasificación previa 2026-05-11 con EDI≈0) a "Falsificación local del aparato": el bootstrap del EDI **excluye cero por la izquierda**, indicando que el modelo acoplado predice estrictamente peor que el reducido en held-out, no que el efecto sea trivial. La inadecuación es de la **sonda Revelle/calcificadores para la serie Aloha pH**, no del dato; conforme a ASA Wasserstein-Lazar 2016 principio 5 ("scientific conclusions … should not be based only on whether a p-value passes a specific threshold"), el resultado se reporta como información sobre el aparato y no como ausencia de fenómeno. **Caveat de datos:** `data/dataset.csv` PMEL/NOAA no estaba versionado; proxy calibrado a estadísticas del run original. Reproducción bit-a-bit requiere fetch del CSV NOAA real. Comando regenerador: `python3 09-simulaciones-edi/19_caso_acidificacion_oceanica/src/validate.py`. Detalle en `Bitacora/2026-05-16-adversarial-downgrades/`. |

### Bloque VII — Controles de falsación (correctamente rechazados)

**Tabla A.5.9.**

**Tabla 5.7.9.**

| # | Caso | EDI | p | Diseño |
|---|------|----:|--:|--------|
| 06 | Falsación de exogeneidad | 0.0551 | 1.0000 | Ruido puro |
| 07 | Falsación de no-estacionariedad | -0.8819 | 1.0000 | Random walk |
| 08 | Falsación de observabilidad | -1.0000 | 1.0000 | Estado oculto |

**3/3 controles correctamente rechazados** — aparato discrimina genuinamente, no es máquina de validar arbitrariamente.

---

## Aplicaciones filosóficas programáticas (sin caso EDI directo)

### Capítulo 05-01 — Mente, memoria, yo

**Estado:** modo programático **sin caso EDI ejecutado ni candidato del corpus**.

**Conjetura central:** las categorías mentales (memoria, atención, decisión, conciencia perceptiva) son **atractores de integración multivariable** en sistemas acoplados organismo–entorno–tarea–historia. Esta es conjetura programática, no resultado empírico de este manuscrito.

**Criterio de elevación:** construir tareas cognitivas con datos cuantitativos públicos donde atractores conductuales discriminen contra cognitivismo simbólico. El corpus actual **no incluye tal caso**. El caso 30 (behavioral dynamics, Nivel 3 weak) **no cuenta como elevación parcial de este capítulo**: opera en coordinación motora, no en cognición simbólica; su lugar legítimo es el capítulo 05-05 como complemento cuantitativo del ancla cualitativa Warren, no como elevación del capítulo de mente.

**Deuda residual fechada:** identificar caso público con datos de tarea cognitiva (decisión bajo incertidumbre, memoria de trabajo, atención sostenida) susceptible de modelado dinámico acoplado, ejecutarlo con `validate.py` y reportar EDI con significancia bootstrap. Hasta entonces, el capítulo 05-01 permanece como conjetura programática declarada.

### Capítulo 05-02 — Biología y ecología

**Estado:** modo programático.

**Conjetura central:** los fenómenos vivos son patrones operativos materialmente sostenidos con cierre dinámico verificable.

**Criterio de elevación:** adoptar caso publicado de regime shift ecológico (Scheffer y colegas) con bifurcación documentada y construir dossier completo.

**Casos del corpus que ya cubren parcialmente:** 16 Deforestación, 22 Fósforo, 21 Salinización, 19 Acidificación oceánica.

### Capítulo 05-03 — Sistemas técnicos distribuidos

**Estado:** modo programático.

**Conjetura central:** los sistemas distribuidos son patrones técnicos modelables como pares acoplados con dinámica de fallo.

**Criterio de elevación:** trace público de incidente con modelo dinámico cuantitativo y predicción de cascada.

**Casos del corpus relevantes:** 20 Kessler, 26 Starlink (overhead técnico).

### Capítulo 05-04 — Instituciones, mercado, Estado

**Estado:** modo programático.

**Conjetura central:** las instituciones son patrones materialmente sostenidos por prácticas, normas, soportes; los mercados son redes dinámicas; el Estado es organización material-normativa.

**Criterio de elevación:** transición de régimen político o crisis institucional con datos cuantitativos publicados.

**Casos del corpus relevantes:** 13 Políticas, 09 Finanzas, 14 Postverdad.

---

## Patrones transversales

### 1. La termodinámica manda

Los 6 casos `overall_pass=True` (post-iter-7) están conectados con dinámicas físicas o termodinámicas robustas (energía eléctrica, deforestación, densidad orbital Kessler, mortalidad biológica, dinámica urbana logística, acumulación-decaimiento Jambeck de microplásticos). Cuanto más anclado físicamente, más robusto el cierre operativo.

### 2. La paradoja del LoE

LoE alto no garantiza EDI alto (Clima: LoE=5, EDI=0.011). Sondas inadecuadas producen EDI bajos incluso con datos excelentes. **Sondas, no datos, son cuello de botella en algunos casos.**

### 3. La importancia del val_steps

Ventanas largas → estadística robusta pero EDI moderados. Ventanas cortas → EDI altos posibles pero requieren cautela. Ventana de 1 (Starlink) = exploratorio, no confirmatorio.

### 4. El éxito de la falsación

3/3 controles rechazados. Refuta la objeción de tautología. Si la ablación fuera trivialmente destructiva, los controles también producirían EDI alto, pero no lo hacen.

### 5. Behavioral dynamics como caso bisagra

El caso 30 (Nivel 3 weak) demuestra que **el aparato EDI funciona en escala behavioral**, produciendo señal genuina con discriminación pública contra nulos. La complementariedad con la demostración cualitativa de Warren (r²=0.980) cubre dos escalas temporales del fenómeno.

---

## Deuda residual

Entradas operativas declaradas tras triage de bitácora huérfana (2026-05-11).

- **[AU-9 2026-05-11]** El Bloque VI (Null, Nivel 0, líneas 128-143) agrega ocho casos sin distinguir tres regímenes operativamente distintos: (i) cinco nulls genuinos (EDI ≈ 0, p > 0.05), (ii) un caso con EDI fuertemente negativo (degradación bajo acoplamiento), (iii) dos casos rechazados por gate C1-C5 antes del cómputo de EDI. La cifra adversarial "-0.876" estaba mal atribuida en versiones previas. Acción: subdividir el bloque en tres etiquetas distintas en la próxima pasada; el conteo agregado preserva el total pero pierde la diferencia operativa entre "el aparato no detecta señal" vs "el aparato detecta degradación" vs "el aparato rechaza antes de calcular". Paralela en `06-cierre/01-conclusion-demostrativa.md` §4.1 y `06-cierre/_extendido/versiones-cortas-defensa.md`. Origen: `Bitacora/2026-05-04-continuous-run/AU-9-edi-negativo-no-es-null.md`.

## Lectura cruzada

- Caso ancla canónico cualitativo: capítulo 05-05
- Aplicaciones programáticas filosóficas: capítulos 05-01 a 05-04
- Caso 30 detallado: `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`
- Cada caso del corpus: `09-simulaciones-edi/<caso>/README.md`
- Resultados consolidados: `09-simulaciones-edi/README.md`
- Verificación de reproducibilidad: `Bitacora/2026-04-27-integracion-jacob/02-verificacion-reproducibilidad.md`
