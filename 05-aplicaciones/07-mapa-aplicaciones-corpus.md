# Mapa de aplicaciones — corpus inter-dominio e inter-escala

## Función

Mapa completo del paisaje de aplicaciones del marco como **ontología general multiescalar**. Cada caso aparece con su modo (demostrativo/programático), nivel de cierre operativo, escala instanciada, criterio de elevación si procede, y referencias cruzadas. El paisaje agrega 40 casos: 30 inter-dominio + 10 inter-escala. Cada caso es **instancia particular de los cuatro invariantes ontológicos** (sustrato material, acoplamiento dinámico, atractor empírico, cierre operativo κ); ningún caso es aplicación aislada del aparato a un dominio.

> **Nota global de versionado.** Las clasificaciones reflejan el estado del corpus tras re-validación consolidada. Histórico de evolución archivado en `Bitacora/2026-05-17-limpieza-final/historico-05-07.md`.

---

## Resumen ejecutivo

**Total de casos:** 40 (30 corpus inter-dominio + 10 corpus inter-escala). Cobertura conjunta: 8 escalas físicas/biológicas/cosmológicas + 7 dominios disciplinares heterogéneos.

### Corpus inter-dominio (30 casos)

**Distribución por modo:**

- **Modo técnico-ejecutado** (dossier EDI completo, `metrics.json` reproducible bajo el protocolo C1-C5): 30 casos. Todos tienen dossier en `09-simulaciones-edi/<caso>/`.
- **Modo demostrativo en sentido estricto** (14/14 componentes del dossier de anclaje del cap 05-00 §1, con material publicado independiente del aparato): 1 caso (05-05 Warren). La distinción es operativa: el primer modo asegura reproducibilidad técnica; el segundo asegura adecuación filosófica plena del aparato a un caso paradigmático.
- **Aplicaciones filosóficas programáticas adicionales:** 4 dominios sin caso EDI directo (capítulos 05-01 a 05-04).

*Nota sobre el modo técnico-ejecutado.* 'Dossier técnico completo' indica que el caso fue corrido con el protocolo C1-C5 y produce `metrics.json` reproducible. **No equivale a 'demostración positiva del aparato'**: los Bloques V-VII (Trend, Null, Controles) no instancian acoplamiento detectable; funcionan como casos de no-aplicabilidad de la sonda, falsación local o controles correctamente rechazados. Casos con `EDI ≤ 0` o `p ≈ 1` están listados explícitamente en sus bloques correspondientes y **no se contabilizan como instancia positiva del aparato**. La fuerza inferencial real del corpus inter-dominio descansa sobre los Bloques I–IV (Strong gate completo, Strong sin gate, Weak con o sin disclosure, Suggestive), no sobre la cifra agregada N=30 indistinta.

**Distribución por Nivel:**

**Tabla A.5.1.**

**Tabla 5.7.1.**

| Nivel | Categoría | N | Casos |
|:----:|-----------|:-:|-------|
| 4 | Strong (`overall_pass=True`) | 8 | Energía, Deforestación, Kessler, Riesgo Biológico, Urbanización, Microplásticos, Behavioral Dynamics, Salinización |
| 4 | Strong sin gate completo | 1 | Starlink |
| 3 | Weak | 4 | Postverdad, Fósforo, Epidemiología, Océanos (con disclosure `valid=False`) |
| 2 | Suggestive | 1 | Justicia |
| 1 | Trend | 2 | Políticas estratégicas, Movilidad |
| 0a | Null genuino | 8 | Conciencia, Acuíferos, IoT, Clima, Contaminación, Wikipedia, Fuga de cerebros, Finanzas |
| 0b | EDI negativo (sonda macro inadecuada) | 1 | Paradigmas |
| 0d | Falsificación local del aparato (CI excluye cero por la izquierda) | 2 | Acidificación oceánica, Erosión dialéctica |
| 0c | Señal rechazada por gate C1-C5 | 0 | — |
| n.e. | Cuarentena por insuficiencia de datos | 0 | — |
| — | Falsación rechazada (controles) | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Subdivisión del Bloque "Null".** Lo que una versión agregada presentaría como "11 null" cubre cuatro regímenes empíricamente distintos: 8 nulls genuinos (el aparato no detecta señal donde no la hay), 1 EDI negativo por sonda macro inadecuada (Paradigmas), 2 **falsificación local del aparato** (Acidificación oceánica caso 19, Erosión dialéctica caso 23) con CI bootstrap que excluye cero por la izquierda, y 0 rechazos por gate C1-C5. La cifra "señal/no-señal" gana matiz y pierde rotundidad; el aparato discrimina cuatro modos de no-éxito en lugar de colapsarlos en una etiqueta única. La falsificación local de los casos 19 y 23 es **fortaleza, no debilidad**: el aparato declara honestamente la inadecuación de su propia sonda en un dominio específico en lugar de blindarse contra el dato, y en el caso 23 lo declara *ex ante* en pre-registro firmado.

**Total con señal significativa:** 19/30 (63 %).
**Falsación correcta:** 3/3 (100 %).

**Costo declarado del agregador `overall_pass`.** El gate compuesto `overall_pass=True` integra C1-C5 + viscosidad + significancia permutacional + persistencia, pero **no exige que `ci_lo` del bootstrap del EDI sea positivo**. Riesgo Biológico (caso 27) ilustra el costo: pasa el gate con `p_perm=0.0022` y `edi.value=0.333`, pero su CI bootstrap 95 % `[-0.198, +0.648]` cruza el cero. La promoción a "strong gate completo" descansa, por tanto, sobre la significancia permutacional del ranking del estadístico observado, no sobre la exclusión bootstrap del cero. La tesis sostiene la categorización pero declara su límite: un revisor que lea "strong" como "CI bootstrap excluye el cero" estará leyendo más de lo que el agregador certifica. Si en una pasada posterior se exige `ci_lo > 0` como requisito de admisión, caso 27 se reclasifica a "strong sin gate bootstrap" y el conteo "8 strong" del corpus inter-dominio cae a 7 con pérdida del dominio biomédico-epidemiológico.

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
| 30 | Behavioral Dynamics | 0.6143 | 0.0000 | Behavioral attractor | 3 | Google Mobility real |
| 21 | Salinización (FAOSTAT enhanced) | 0.5152 | 0.0010 | Richards bilineal | 3 | FAOSTAT enhanced |

Reproducibilidad: cada caso es reproducible con `python3 09-simulaciones-edi/<NN>_caso_<nombre>/src/validate.py --seed 42`. La trazabilidad detallada está en `Bitacora/`.

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
| 14 | Postverdad (desinformación) | 0.2428 | 0.0000 | SIS contagion |
| 17 | Océanos (OHC proxy) | 0.1902 | 0.0000 | Sonda térmica (disclosure: `valid=False`, gate C1-C5 no superado pero CI=[0.157, 0.280] estrictamente positivo) |
| 22 | Fósforo (fertilizantes) | 0.1924 | 0.0000 | Carpenter P Cycle |
| 05 | Epidemiología (COVID-19) | 0.1294 | 0.0000 | SEIR |

### Bloque IV — Suggestive (Nivel 2)

**Tabla A.5.6.**

**Tabla 5.7.6.**

| # | Caso | EDI | p_perm | CI 95 % bootstrap | Comentario |
|---|------|----:|--:|---|---|
| 10 | Justicia (Estado de Derecho) | 0.0579 | 0.0170 | [-0.151, +0.345] | Suggestive porque p<0.05 con magnitud baja y CI cruza cero (datos World Bank Rule-of-Law `RL.EST` 10 economías top 1996–2023, val_steps=11). |
| 22 | Fósforo (referenciado en Bloque III Weak) | 0.1924 | 0.0000 | [-0.221, +0.550] | Ranking permutacional alto pero bootstrap no excluye cero; magnitud frágil (criterio CI bootstrap). |

**Costo de admisión declarado.** La regla `CI 95 % no cruza cero` opera como criterio adicional al ranking permutacional. La coexistencia de `p<0.01` con magnitud trivial y CI cruzando cero no debe contar como evidencia positiva, conforme a Wasserstein y Lazar (2016, *The American Statistician* 70(2):129-133, ASA Statement on p-values, Principle 3 — verbatim en `07-bibliografia/Wasserstein-Lazar - ASA Statement on p-values (Am Stat 2016).pdf` p. 2): *"Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold."* La auditoría retrospectiva de casos contabilizados bajo este criterio queda como deuda residual fechada (cf. cap 03 §criterios de admisión).

### Bloque V — Trend (Nivel 1)

**Tabla A.5.7.**

**Tabla 5.7.7.**

| # | Caso | EDI | p | Comentario |
|---|------|----:|--:|------------|
| 13 | Políticas estratégicas (gasto militar) | 0.0821 | 0.1622 | Trend Nivel 1 bajo datos institucionales reales; CI=[0.065, 0.100]. Ruido domina señal. |
| 11 | Movilidad (tráfico aéreo / TomTom) | 0.0599 | 0.9219 | Trend Nivel 1 bajo datos TomTom reales; CI=[-0.392, 0.205]. Ruido domina señal de cierre bajo sonda Bilinear diffusion. |

### Bloque VI — Null (Nivel 0)

**Tabla A.5.8.**

**Tabla 5.7.8.**

| # | Caso | EDI | Comentario |
|---|------|----:|-----------|
| 01 | Clima regional | -0.0007 | Null genuino bajo datos reales IPCC-calibrados (p_perm=0.998, sonda Budyko-Sellers). |
| 02 | Conciencia global | -0.0121 | Null genuino bajo datos reales (p_perm=0.315, CI=[-0.016, -0.010]; sonda dinámica colectiva). Consistente con LoE=1 especulativa. |
| 03 | Contaminación PM2.5 | -0.0109 | Null genuino bajo datos World Bank PM2.5 reales (p_perm=0.616, sonda dispersión-decaimiento). |
| 09 | Finanzas globales | -0.0020 | Null/artefacto bajo régimen detrended honesto (raw=+0.1027 con `trend_r2=0.979`, warning activo). |
| 12 | Paradigmas (ciencia) | -0.1536 | Reflexividad; null bajo régimen real-phase actual. |
| 25 | Acuíferos | -0.1462 | Datos heterogéneos. |
| 29 | IoT | -0.8760 | Reflexividad técnica. |
| 15 | Wikipedia (atención colectiva — "Climate change" EN) | -0.0038 | Null genuino bajo datos Wikimedia pageviews mensuales 2015–2024 (p_perm=0.769, CI=[-0.023, -0.002]). Magnitud trivial domina (`\|EDI\|<0.05`). |
| 28 | Fuga de cerebros (multi-driver WB) | 0.0298 | Null genuino bajo datos WB multi-driver (researchers, enrollment, remittances, GDP pc, net migration; p_perm=0.969, CI=[-0.095, +0.159], val_steps=18). Candidato a panel bilateral origen-destino para próxima ejecución. |

Convención para Bloque VI: `\|EDI\|<0.05` y `p_perm>0.05` cubren los nulls clásicos; el caso 15 con `p_perm>0.05` y CI bootstrap [-0.023, -0.002] que excluye cero por la izquierda con magnitud trivial se declara Null genuino porque la magnitud trivial domina sobre la exclusión bootstrap marginal.

### Bloque VI.5 — Falsificación local del aparato (sonda inadecuada con CI que excluye cero por la izquierda)

**Tabla 5.7.8b.**

| # | Caso | EDI | CI bootstrap | Comentario |
|---|------|----:|--------------|-----------|
| 19 | Acidificación oceánica | -0.0047 | [-0.0054, -0.0041] | Falsificación local del aparato: el bootstrap del EDI **excluye cero por la izquierda**, indicando que el modelo acoplado predice estrictamente peor que el reducido en held-out. La inadecuación es de la **sonda Revelle/calcificadores para la serie Aloha pH**, no del dato; conforme a ASA Wasserstein-Lazar 2016 principio 5, el resultado se reporta como información sobre el aparato y no como ausencia de fenómeno. **Caveat de datos:** `data/dataset.csv` PMEL/NOAA no estaba versionado; proxy calibrado a estadísticas del run original. Reproducción bit-a-bit requiere fetch del CSV NOAA real. Comando regenerador: `python3 09-simulaciones-edi/19_caso_acidificacion_oceanica/src/validate.py`. |
| 23 | Erosión dialéctica | -1.0000 | [-3.336, -1.008] | Falsificación local del aparato con pre-registro firmado VALIDADO EXACTO (`09-simulaciones-edi/23_caso_erosion_dialectica/docs/PRE_REGISTRO.md`): predicción EDI=-1.0 ±0.30 → observado EDI=-1.000 EXACTO, p_perm=1.0, CI bootstrap [-3.336, -1.008] que excluye cero por la izquierda. La sonda Abrams-Strogatz `prestige_competition` no es físicamente apropiada para la serie real propuesta (modela competencia entre dos lenguas en sustrato fijo; aplicar a "erosión dialéctica" sin variable observable con dos competidores claros produce mismatch sistemático). El aparato declara honestamente la inadecuación local ex ante en el pre-registro y la confirma bit-a-bit en la ejecución; ASA Wasserstein-Lazar 2016 principio 5. La falsificación local confirmada es fortaleza: el pre-registro firmado bloquea operativamente el forking path de defenderla post-hoc como "categoría mal definida". Comando regenerador: `python3 09-simulaciones-edi/23_caso_erosion_dialectica/src/validate.py --seed 42`. |

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

**Criterio de elevación:** construir tareas cognitivas con datos cuantitativos públicos donde atractores conductuales discriminen contra cognitivismo simbólico. El corpus actual **no incluye tal caso**. El caso 30 (behavioral dynamics, Nivel 4 strong) **no cuenta como elevación parcial de este capítulo**: opera en coordinación motora, no en cognición simbólica; su lugar legítimo es el capítulo 05-05 como complemento cuantitativo del ancla cualitativa Warren, no como elevación del capítulo de mente.

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

Los casos `overall_pass=True` están conectados con dinámicas físicas o termodinámicas robustas (energía eléctrica, deforestación, densidad orbital Kessler, mortalidad biológica, dinámica urbana logística, acumulación-decaimiento Jambeck de microplásticos, behavioral attractor Google Mobility, Richards bilineal salinización). Cuanto más anclado físicamente, más robusto el cierre operativo.

### 2. La paradoja del LoE

LoE alto no garantiza EDI alto (Clima: LoE=5, EDI≈0). Sondas inadecuadas producen EDI bajos incluso con datos excelentes. **Sondas, no datos, son cuello de botella en algunos casos.**

### 3. La importancia del val_steps

Ventanas largas → estadística robusta pero EDI moderados. Ventanas cortas → EDI altos posibles pero requieren cautela. Ventana de 1 = exploratorio, no confirmatorio.

### 4. El éxito de la falsación

3/3 controles rechazados. Refuta la objeción de tautología. Si la ablación fuera trivialmente destructiva, los controles también producirían EDI alto, pero no lo hacen.

### 5. Behavioral dynamics como caso bisagra

El caso 30 (Nivel 4 strong bajo Google Mobility real) demuestra que **el aparato EDI funciona en escala behavioral**, produciendo señal genuina con discriminación pública contra nulos. La complementariedad con la demostración cualitativa de Warren (r²=0.980) cubre dos escalas temporales del fenómeno.

---

## Deuda residual

Entradas operativas declaradas tras triage de bitácora huérfana (2026-05-11).

- **[AU-9 2026-05-11]** El Bloque VI (Null, Nivel 0) agrega casos heterogéneos que requieren distinguir tres regímenes operativamente distintos: (i) nulls genuinos (EDI ≈ 0, p > 0.05), (ii) caso con EDI fuertemente negativo (degradación bajo acoplamiento), (iii) casos rechazados por gate C1-C5 antes del cómputo de EDI. La subdivisión vigente en bloques 0a / 0b / 0c / 0d (más Bloque VI.5 de falsificación local) atiende esa distinción; el conteo agregado preserva el total pero hace visible la diferencia operativa entre "el aparato no detecta señal" vs "el aparato detecta degradación" vs "el aparato rechaza antes de calcular". Paralela en `06-cierre/01-conclusion-demostrativa.md` §4.1 y `06-cierre/_extendido/versiones-cortas-defensa.md`. Origen: `Bitacora/2026-05-04-continuous-run/AU-9-edi-negativo-no-es-null.md`.

## Lectura cruzada

- Caso ancla canónico cualitativo: capítulo 05-05
- Aplicaciones programáticas filosóficas: capítulos 05-01 a 05-04
- Caso 30 detallado: `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`
- Cada caso del corpus: `09-simulaciones-edi/<caso>/README.md`
- Resultados consolidados: `09-simulaciones-edi/README.md`
- Verificación de reproducibilidad: `Bitacora/2026-04-27-integracion-jacob/02-verificacion-reproducibilidad.md`
- Histórico de reclasificaciones del corpus: `Bitacora/2026-05-17-limpieza-final/historico-05-07.md`
