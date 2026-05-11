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

*Nota sobre el modo técnico-ejecutado.* 'Dossier técnico completo' indica que el caso fue corrido con el protocolo C1-C5 y produce `metrics.json` reproducible. **No equivale a 'demostración positiva del aparato'**: los Bloques V-VII (Trend, Null, Controles) no instancian acoplamiento detectable; funcionan como casos de no-aplicabilidad de la sonda, falsación local o controles correctamente rechazados. Casos con `EDI ≤ 0` o `p ≈ 1` están listados explícitamente en sus bloques correspondientes y **no se contabilizan como instancia positiva del aparato**. La fuerza inferencial real del corpus inter-dominio descansa sobre los Bloques I–IV (Strong, Strong sin gate, Weak, Suggestive — del orden de 15 casos según los conteos vigentes), no sobre la cifra agregada N=30 indistinta.

**Distribución por Nivel:**

**Tabla A.5.1.**

**Tabla 5.7.1.**

| Nivel | Categoría | N | Casos |
|:----:|-----------|:-:|-------|
| 4 | Strong (`overall_pass=True`) | 4 | Energía, Deforestación, Kessler, Riesgo Biológico |
| 4 | Strong sin gate completo | 1 | Microplásticos |
| 3 | Weak | 8 | Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad, Behavioral Dynamics (caso 30) |
| 2 | Suggestive | 1 | Finanzas (Salinización reclasificada por AU-4: CI cruza cero + magnitud trivial) |
| 1 | Trend | 3 | Justicia, Fuga cerebros, Clima |
| 0a | Null genuino | 5 | Conciencia, Acidificación, Erosión, Acuíferos, IoT (`\|EDI\|<0.05` y `p_perm>0.05`) |
| 0b | EDI negativo (sonda macro inadecuada) | 1 | Paradigmas (`EDI=-0.144`: ABM acoplado predice peor que reducido) |
| 0c | Señal rechazada por gate C1-C5 | 2 | Contaminación, Océanos (`EDI>0` con `p_perm<0.05` pero `valid=False`) |
| n.e. | Cuarentena por insuficiencia de datos | 1 | Starlink (val_steps=1) |
| — | Falsación rechazada (controles) | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Subdivisión del Bloque "Null" (AU-9 2026-05-11).** Lo que la versión previa presentaba como "8 null" cubre en realidad tres regímenes empíricamente distintos: 5 nulls genuinos (el aparato no detecta señal donde no la hay), 1 EDI negativo (la sonda macro elegida es activamente inadecuada para el dominio), y 2 rechazos por gate C1-C5 (ranking permutacional cruza el umbral pero la batería compuesta rechaza por incumplimiento de viscosidad/persistencia/no-localidad). La cifra "señal/no-señal ≈ 50 %" gana matiz y pierde rotundidad; el aparato discrimina tres modos de no-éxito en lugar de colapsarlos en una etiqueta única.

**Total con señal significativa:** 15/30 (50%).
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

Reproducibilidad: el caso 16 ha sido re-ejecutado con datos World Bank descargados en vivo (variabilidad estocástica <4%, mismo Nivel 4 strong). La trazabilidad detallada está en `Bitacora/`.

### Bloque II — Strong sin gate completo (Nivel 4*)

**Tabla A.5.4.**

**Tabla 5.7.4.**

| # | Caso | EDI | p | Sonda | Por qué no gate |
|---|------|----:|--:|-------|-----------------|
| 24 | Microplásticos | 0.7819 | 0.0000 | Jambeck Accumulation | Bootstrap CI inestable |

### Bloque III — Weak (Nivel 3)

**Tabla A.5.5.**

**Tabla 5.7.5.**

| # | Caso | EDI | p | Sonda |
|---|------|----:|--:|-------|
| 13 | Políticas estratégicas (gasto militar) | 0.2972 | 0.0015 | Saturation growth |
| 30 | Behavioral Dynamics | 0.2622 | 0.0440 | behavioral_attractor (segundo orden) |
| 14 | Postverdad (desinformación) | 0.2428 | 0.0000 | SIS contagion |
| 18 | Urbanización | 0.2358 | 0.0000 | Logística + atracción |
| 22 | Fósforo (fertilizantes) | 0.1924 | 0.0000 | Carpenter P Cycle |
| 15 | Wikipedia (ediciones) | 0.1916 | 0.0000 | Saturation growth |
| 05 | Epidemiología (COVID-19) | 0.1294 | 0.0000 | SEIR |
| 11 | Movilidad (tráfico aéreo) | 0.1283 | 0.0020 | Bilinear diffusion |

### Bloque IV — Suggestive (Nivel 2)

**Tabla A.5.6.**

**Tabla 5.7.6.**

| # | Caso | EDI | p_perm | CI 95 % bootstrap | Comentario |
|---|------|----:|--:|---|---|
| 09 | Finanzas globales | 0.0813 | 0.0000 | (pendiente reporte en tabla) | Mantenido en suggestive |
| 22 | Fósforo (referenciado en Bloque III Weak) | 0.1924 | 0.0000 | [-0.221, +0.550] | Ranking permutacional alto pero bootstrap no excluye cero; magnitud frágil (AU-4) |

**Reclasificación AU-4 (2026-05-11):** el caso 21 (Salinización) se **retira del Bloque IV Suggestive** y se reubica en un bloque nuevo de "significativos por permutación con magnitud trivial — no contabilizan a favor de la tesis". Sus métricas son `EDI = 0.0184`, `p_perm = 0.0028`, `CI 95 % bootstrap = [-0.0771, +0.0825]`: el CI no excluye que el acoplamiento empeore la predicción y la magnitud puntual es del orden del 0.6 % de reducción de RMSE. Este es exactamente el patrón que Wasserstein y Lazar (2016, *The American Statistician* 70(2):129-133, ASA Statement on p-values, Principle 3 — verbatim en `07-bibliografia/Wasserstein-Lazar - ASA Statement on p-values (Am Stat 2016).pdf` p. 2) advierten: *"Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold."* La coexistencia de `p<0.01` con magnitud trivial y CI cruzando cero no debe contar como evidencia positiva. La tesis declara aquí, como costo, que **la regla `CI 95 % no cruza cero` debe operar como criterio adicional al ranking permutacional** en pasadas subsiguientes; la auditoría retrospectiva de los demás casos contabilizados como significativos queda como deuda residual fechada (cf. cap 03 §criterios de admisión).

### Bloque V — Trend (Nivel 1)

**Tabla A.5.7.**

**Tabla 5.7.7.**

| # | Caso | EDI | p | Comentario |
|---|------|----:|--:|------------|
| 10 | Justicia (Estado de Derecho) | 0.2274 | 0.4775 | Ventana corta |
| 28 | Fuga de cerebros | 0.0249 | 0.9975 | Ruido domina |
| 01 | Clima regional | 0.0111 | 0.9990 | Sonda Budyko-Sellers insuficiente |

**Casos en cuarentena por insuficiencia de datos.** Caso 26 (Starlink) se removió del Bloque V tras auditoría de `metrics.json` (phases.real): `val_steps = 1`, `ci_lo = ci_hi = edi.value = 0.6892` (CI bootstrap colapsado), `permutation_pvalue = 1.0`, `correlations.abm_obs = 0.0`. Con un único punto de validación el bootstrap colapsa y la permutación carece de grados de libertad: el EDI=0.689 es **artefacto numérico, no medición**. El caso 19 (Acidificación oceánica) compartió esa patología en versiones previas (cf. línea correspondiente en Bloque VI con `metrics.json` re-ejecutado a EDI≈0.00044, p_perm=0.43). La tesis declara estos casos en cuarentena/null por insuficiencia de datos hasta que el dataset admita un `val_steps ≥ 8` o se decida su reclasificación definitiva. Comando regenerador: `python3 09-simulaciones-edi/26_caso_starlink/src/validate.py`. El epíteto "exploratorio" no salva la clasificación como Trend; el caso queda reubicado en bloque de cuarentena.

### Bloque VI — Null (Nivel 0)

**Tabla A.5.8.**

**Tabla 5.7.8.**

| # | Caso | EDI | Comentario |
|---|------|----:|-----------|
| 02 | Conciencia global | -0.1165 | Datos especulativos LoE=1 |
| 03 | Contaminación PM2.5 | -0.0901 | Sin estructura macro detectable bajo régimen real-phase actual |
| 12 | Paradigmas (ciencia) | -0.1536 | Reflexividad; null bajo régimen real-phase actual |
| 17 | Océanos (temperatura) | -0.0154 | Sin sonda específica |
| 19 | Acidificación oceánica | 0.00044 | **Null genuino tras re-ejecución canónica 2026-05-11** (EDI=0.00044, p_perm=0.433, CI=[0.00023, 0.00065], n_perm=2999). El `metrics.json` previo (`edi.value=0.7278`) era inconsistente internamente (TENG-05): mezclaba dos ejecuciones; los `errors` almacenados implicaban `computed_edi=-0.000191`. La re-ejecución coherente clasifica el caso como null. **Caveat de datos:** `data/dataset.csv` PMEL/NOAA no estaba versionado; se usó proxy sintético calibrado a estadísticas del run original. Reproducción bit-a-bit requiere fetch del CSV NOAA real. Block-permutation no implementada (i.i.d. Phipson-Smyth); con EDI≈0 y p=0.43 el resultado null tiene margen amplio. Detalle en `Bitacora/2026-05-11-sintesis-tesis/F5-A-caso19-reejecucion.md`. |
| 23 | Erosión dialéctica | -1.0000 | Categoría mal definida |
| 25 | Acuíferos | -0.1462 | Datos heterogéneos |
| 29 | IoT | -0.8760 | Reflexividad técnica |

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

Los 4 casos `overall_pass=True` están conectados con dinámicas físicas o termodinámicas robustas. Cuanto más anclado físicamente, más robusto el cierre operativo.

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
