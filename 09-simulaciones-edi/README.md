# Capítulo 09. Corpus EDI: validación empírica inter-dominio + inter-escala

## Función de este capítulo

Este capítulo aloja el **aparato empírico de la tesis**: el motor de simulación híbrido ABM+ODE, los **30 casos del corpus inter-dominio**, los **10 casos del corpus inter-escala** (ver `corpus_multiescala/`), y la infraestructura de ejecución, auditoría y reporte. El corpus inter-dominio cubre física, biología, economía, política, tecnología, cultura y conducta humana con sondas ODE específicas por dominio. El corpus inter-escala cubre **30 órdenes de magnitud** espaciales y temporales, desde dinámica de espín-órbita atómica (10⁻¹⁰ m, 10⁻¹⁵ s) hasta dinámica de cúmulos globulares (10²⁰ m, 10¹⁴ s). Validación canónica unificada en ambos corpus.

## Tesis del capítulo

> El irrealismo operativo de estructuras pre-ontológicas se demuestra como **ontología general multiescalar** mediante cartografía empírica agregada de 40 casos. El motor ABM+ODE acoplado, el protocolo C1-C5 y la métrica EDI calculada por intervención ablativa producen un paisaje de emergencia robusto, discriminante y falsable a través de escalas: corpus inter-dominio con 5 casos strong (4 con `overall_pass=True`), 7 weak, 2 suggestive, 4 trend, 8 null, 3 controles de falsación rechazados; corpus inter-escala con 7 strong en 7 escalas distintas + 1 weak + 2 nulls honestos. El aparato es **invariante a la escala**: opera con la misma metodología desde el qubit superconductor hasta el cúmulo globular, con sondas físicamente motivadas específicas a cada escala.

## Lectura ontológica del corpus: cada caso es instanciación de la misma estructura

Los 40 casos del corpus agregado **no son listado de aplicaciones independientes**: cada caso instancia **los cuatro invariantes ontológicos** que la tesis afirma (cap 02-01). Lo que cambia entre casos es la escala y el dominio donde los invariantes se materializan; la **estructura ontológica subyacente es una sola**.

Para cada caso del corpus, la lectura ontológica articula:

- **Sustrato material:** qué cuerpo material dinámico aloja el fenómeno;
- **Acoplamiento:** qué dos polos interactúan dinámicamente bajo restricciones de la escala;
- **Atractor empírico:** qué región del espacio de fase concentra la convergencia bajo perturbación;
- **Cierre operativo κ:** qué reducción a sistema de baja dimensión preserva las dependencias decisivas, medida por EDI.

Esta lectura no es opcional retórica: es lo que el motor del aparato computa para cada caso. El `metrics.json` de cada caso reporta el cierre operativo κ; los demás invariantes están instanciados en `case_config.json` y la sonda específica.

### Articulación ontológica por familia de casos del corpus inter-dominio

#### Casos strong (4 con `overall_pass=True`): donde la estructura ontológica se manifiesta más nítidamente

| Caso | Sustrato material | Acoplamiento | Atractor | Cierre operativo κ |
|------|-------------------|--------------|----------|---------------------|
| 04 Energía | Red eléctrica + agentes económicos + recursos | F↔R bajo coste y política | Mix energético de equilibrio dinámico | EDI 0.65 (Lotka-Volterra) |
| 16 Deforestación | Frontera agrícola/forestal + agentes humanos + biosfera | Renta agrícola↔distancia al mercado | Patrón espacial de ocupación territorial | EDI 0.60 (von Thünen) |
| 20 Kessler | Densidad orbital + flujo de fragmentos | Densidad↔tasa colisional | Régimen de saturación orbital | EDI 0.35 (densidad orbital) |
| 27 Riesgo Biológico | Población humana + patógenos + sistemas sanitarios | Mortalidad↔presión biológica | Tasa de mortalidad estable bajo régimen | EDI 0.33 (mortalidad) |

Estos cuatro casos, aunque pertenecen a dominios heterogéneos (energético, ecológico, espacial, sanitario), instancian la **misma estructura ontológica**. La diferencia entre ellos es de escala temporal (años en Energía vs décadas en Deforestación) y de dominio sustantivo (recursos vs biosfera vs órbita vs salud), no de **forma ontológica**. Cada uno es atractor empírico de un sistema material acoplado con cierre operativo medible.

#### Caso strong sin gate completo: estructura ontológica detectada con cautela inferencial

| Caso | Sustrato material | Acoplamiento | Atractor | Cierre operativo κ |
|------|-------------------|--------------|----------|---------------------|
| 24 Microplásticos | Hidrosfera + materiales sintéticos + ecosistemas marinos | Generación↔acumulación | Concentración acumulada estable | EDI 0.78 (Jambeck) |

EDI muy alto pero CI bootstrap inestable. Estructura ontológica plausible pero la inferencia estadística requiere refinamiento.

#### Casos weak (8 con p < 0.05 y EDI ≥ 0.10): estructura ontológica detectable pero atenuada

Cada uno instancia los invariantes con **componente exógeno dominante** o **acoplamiento parcial**:

- **05 Epidemiología, 18 Urbanización, 22 Fósforo, 13 Políticas, 14 Postverdad, 15 Wikipedia, 11 Movilidad** — sustratos sociotecnoecológicos con acoplamientos identificables, atractores parciales, cierre operativo modesto pero significativo.
- **30 Behavioral Dynamics** — caso bisagra entre dimensión individual y poblacional; sustrato organismo-entorno-tarea; acoplamiento informacional vía τ; atractor de control de heading; κ medido bajo Fajen-Warren con circularidad detectada por N2 (limita la fuerza ontológica del caso individual).

#### Casos null (8 con EDI ≤ 0): instancias donde el aparato detecta correctamente ausencia de cierre operativo bajo la sonda elegida

Estos casos **no refutan la ontología general**: muestran que **no toda regularidad superficial es atractor de cierre operativo**. Conciencia global, contaminación PM2.5, paradigmas científicos, océanos como temperatura agregada, acidificación, erosión dialéctica, acuíferos, IoT — en cada uno, la sonda específica no captura un acoplamiento dinámico genuino. La ontología sí se afirma: el aparato distingue entre cierre operativo real y ausencia de él.

#### Controles de falsación (3 rechazados): la prueba inversa de la ontología

Los 3 controles (exogeneidad, no-estacionariedad, observabilidad) están construidos para que el aparato **DEBA fallar**. El rechazo correcto de los tres confirma que el cierre operativo detectado en los strong/weak no es artefacto del aparato: si fuera artefacto, los controles también producirían EDI alto. **No lo hacen.** Esto es prueba operativa de que la ontología no es vacía.

### Articulación ontológica del corpus inter-escala

Los 10 casos del corpus inter-escala (`corpus_multiescala/`) instancian los mismos cuatro invariantes en escalas físicas distintas. Ver `09-simulaciones-edi/corpus_multiescala/README.md` y `Anexos/A12-corpus-multiescala-tablas.md` para la tabla detallada. Lo importante para esta sección: los 7 strong en 7 escalas distintas (atómica, cuántica, bioquímica, celular oscilatoria, individual, astrofísica, astrofísica masiva) **no son aplicación nominal del aparato a otros dominios**: cada uno verifica los cuatro invariantes ontológicos en su escala, con sondas físicamente motivadas y test cruzado de especificidad (V4-01: 0/12 circularidad).

### Síntesis filosófica del corpus agregado

Los 40 casos del corpus, leídos ontológicamente, **dicen lo mismo**: hay un sustrato material dinámico que se acopla en pares (o más) bajo restricciones, produce atractores empíricos, y admite descripción comprimida cuando el detalle local no afecta la dependencia decisiva. Esta es **una sola ontología**, no una colección. Los dominios y las escalas cambian; los invariantes permanecen.

La diferencia entre 5 strong, 8 weak, 2 suggestive, 4 trend, 8 null, 3 controles rechazados (corpus inter-dominio) y 7 strong + 1 weak + 2 null (corpus inter-escala) **no es diferencia ontológica**: es diferencia de **calidad de la sonda y de los datos** disponibles para verificar la estructura común. Donde la sonda es físicamente adecuada y los datos preservan la dinámica, el cierre operativo aparece. Donde la sonda no captura el acoplamiento o los datos son ruido sin estructura, el aparato lo reporta honestamente.

**Esto es lo que significa "ontología general operativamente articulada":** una sola estructura ontológica, multiescalar e inter-dominio, validada caso por caso por su capacidad de discriminar genuinamente entre presencia y ausencia de cierre operativo bajo intervención ablativa controlada.

## Estructura del corpus

```
09-simulaciones-edi/
├── README.md                          ← este archivo
├── tesis                              ← CLI principal (./tesis demo, audit, build...)
├── run_demo.sh                        ← demo rápido
├── requirements.txt                   ← dependencias
├── .venv/                             ← entorno aislado
├── common/                            ← validador canónico, ABM, ODE, GPU backend
│   ├── hybrid_validator.py            ← 2252 líneas, núcleo del Emergentómetro
│   ├── abm_core.py + abm_core_gpu.py  ← ABM CPU/GPU
│   ├── ode_models.py                  ← sondas macro (Lotka-Volterra, von Thünen, etc.)
│   ├── case_runner.py                 ← orquestador de cada caso
│   ├── gpu_backend.py                 ← detección CUDA/CuPy/PyTorch
│   └── ...
├── 01_caso_clima/ ... 30_caso_behavioral_dynamics/  ← 30 casos del corpus EDI
│   └── src/{abm,ode,data,validate}.py
│   └── outputs/metrics.json + report.md
│   └── case_config.json
├── docker/                            ← entorno reproducible con GPU
└── scripts_orquestacion/              ← auditoría, evaluación, build
```

## Resultados consolidados

### Tabla maestra (30 casos, fase real, outputs verificados)

| # | Caso | Sonda macro | EDI | p-value | overall | Nivel | LoE | val_steps |
|---|------|-------------|----:|--------:|:-------:|:-----:|----:|----------:|
| 04 | Energía eléctrica | Lotka-Volterra | **0.6503** | 0.0000 | ✓ | **4** | 4 | 13 |
| 16 | Deforestación global | von Thünen | **0.6020** | 0.0000 | ✓ | **4** | 4 | 13 |
| 20 | Síndrome de Kessler | Densidad orbital | **0.3527** | 0.0000 | ✓ | **4** | 3 | 15 |
| 27 | Riesgo biológico | Mortalidad | **0.3326** | 0.0022 | ✓ | **4** | 3 | 9 |
| 24 | Microplásticos | Jambeck Accumulation | **0.7819** | 0.0000 | – | 4* | 4 | 15 |
| 13 | Políticas estratégicas | Gasto militar | 0.2972 | 0.0015 | – | 3 | 3 | 13 |
| 14 | Postverdad | SIS Desinformación | 0.2428 | 0.0000 | – | 3 | 2 | 8 |
| 18 | Urbanización | Logística + Atracción | 0.2358 | 0.0000 | – | 3 | 4 | 23 |
| 22 | Fósforo | Carpenter P Cycle | 0.1924 | 0.0000 | – | 3 | 4 | 18 |
| 15 | Wikipedia | Crecimiento social | 0.1916 | 0.0000 | – | 3 | 3 | 48 |
| 05 | Epidemiología | SIR/SEIR | 0.1294 | 0.0000 | – | 3 | 4 | 104 |
| 11 | Movilidad | Difusión aérea | 0.1283 | 0.0020 | – | 3 | 3 | 19 |
| 09 | Finanzas globales | Pricing factor | 0.0813 | 0.0000 | – | 2 | 4 | 168 |
| 21 | Salinización | Balance hídrico | 0.0184 | 0.0028 | – | 2 | 3 | 18 |
| 10 | Justicia | – | 0.2274 | 0.4775 | – | 1 | 2 | 12 |
| 26 | Starlink | Densidad orbital | 0.6892 | 1.0000 | – | 1* | 3 | 1 |
| 28 | Fuga de cerebros | Docquier-Rapoport | 0.0249 | 0.9975 | – | 1 | 3 | 18 |
| 01 | Clima regional | Budyko-Sellers | 0.0111 | 0.9990 | – | 1 | 5 | 168 |
| 02 | Conciencia global | Fallback | -0.1165 | 0.9239 | – | 0 | 1 | 9 |
| 03 | Contaminación PM2.5 | – | -0.0038 | 0.8699 | – | 0 | 3 | 11 |
| 12 | Paradigmas (ciencia) | – | -0.0060 | 0.0000 | – | 0 | 2 | 11 |
| 17 | Océanos (temperatura) | – | -0.0154 | 1.0000 | – | 0 | 3 | 14 |
| 19 | Acidificación oceánica | – | -0.0002 | 0.0000 | – | 0 | 3 | 11 |
| 23 | Erosión dialéctica | – | -1.0000 | 1.0000 | – | 0 | 1 | 8 |
| 25 | Acuíferos | – | -0.1462 | 1.0000 | – | 0 | 3 | 19 |
| 29 | IoT | – | -0.8760 | 1.0000 | – | 0 | 3 | 15 |
| 06 | **Falsación exogeneidad** | Ruido puro | 0.0551 | 1.0000 | – | – | 1 | 731 |
| 07 | **Falsación no-estacionariedad** | Random walk | -0.8819 | 1.0000 | – | – | 1 | 731 |
| 08 | **Falsación observabilidad** | Estado oculto | -1.0000 | 1.0000 | – | – | 1 | 97 |

**(*)** Microplásticos: EDI alto (0.78) sin gate completo por inestabilidad del bootstrap. Starlink: ventana de validación insuficiente (val_steps=1).

### Distribución del paisaje de emergencia

| Categoría | Conteo | Porcentaje |
|-----------|-------:|-----------:|
| Strong (Nivel 4) — gate completo | 4 | 14% |
| Strong (Nivel 4) — sin gate | 1 | 3% |
| Weak (Nivel 3) | 7 | 24% |
| Suggestive (Nivel 2) | 2 | 7% |
| Trend (Nivel 1) | 4 | 14% |
| Null (Nivel 0) | 8 | 28% |
| Falsación rechazada | 3 | 10% |

**Total:** 30 casos del corpus EDI. **Selectividad:** 15/30 con significancia (p<0.05 y EDI>0.01). **Falsación correcta:** 3/3.

### Métricas globales de robustez

| Métrica | Valor | Interpretación |
|---------|------:|----------------|
| Estabilidad numérica | 29/29 | Pipeline numéricamente sólido |
| Persistencia temporal | 28/29 | Ventanas de validación adecuadas |
| Determinismo (seed=42) | 29/29 | Reproducibilidad bit-a-bit |
| Coupling > 0.10 | 21/29 | Mayoría con acoplamiento no epifenoménico |

## Análisis transversal

### Patrón 1. La termodinámica manda

Los cuatro casos con `overall_pass=True` están conectados con dinámicas físicas o termodinámicas robustas (Energía, Deforestación, Riesgo Biológico, Kessler). Esto es coherente con la hipótesis: cuanto más anclado físicamente está un fenómeno, más robusto es su cierre operativo.

### Patrón 2. La paradoja de los datos (LoE)

Los casos con LoE 5 (datos físicos directos) no necesariamente alcanzan los EDI más altos. El Clima (LoE=5, EDI=0.011) muestra que sondas inadecuadas producen EDI bajos incluso con datos excelentes. Sondas, no datos, son el cuello de botella en algunos casos.

### Patrón 3. La importancia del val_steps

Casos con ventanas largas (Epidemiología 104, Finanzas 168, Clima 168) producen estadística robusta pero EDI moderados. Casos con ventanas cortas (Riesgo Biológico 9, Postverdad 8) pueden producir EDI altos pero requieren cautela inferencial. Starlink (val_steps=1) es exploratorio, no confirmatorio.

### Patrón 4. El éxito de la falsación

3 de 3 controles de falsación rechazados correctamente. Esto refuta la objeción de tautología: si la ablación fuera trivialmente destructiva, los controles también producirían EDI alto, pero no lo hacen.

## Cómo ejecutar

### Setup (una vez)

```bash
cd /datos/repos/EstructurasPreontologicas/09-simulaciones-edi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Ejecución básica

```bash
source .venv/bin/activate
./tesis demo               # ejecuta caso clima
./tesis audit              # auditoría rápida (sin re-ejecutar)
./tesis metrics            # regenera tablas
./tesis build              # ensambla tesis
```

### Ejecución de un caso específico

```bash
cd 16_caso_deforestacion/src
python3 validate.py        # perfil canónico (n_perm=999, n_boot=500)
```

### Re-ejecución masiva con perfiles agresivos (GPU)

```bash
./tesis run --gpu --case clima
HYPER_N_PERM=2999 HYPER_N_BOOT=1500 ./tesis run --case deforest
```

## Sondas macro implementadas

| Caso | Sonda ODE | Referencia teórica |
|------|-----------|--------------------|
| Clima | Budyko-Sellers | Budyko 1969, Sellers 1969 |
| Energía | Lotka-Volterra | Lotka 1925, Volterra 1926 |
| Deforestación | von Thünen frontier | von Thünen 1826 |
| Microplásticos | Jambeck Accumulation | Jambeck et al. 2015 |
| Epidemiología | SIR/SEIR | Kermack-McKendrick 1927 |
| Urbanización | Logística + Atracción | Pearl-Reed 1920 |
| Fósforo | Carpenter P Cycle | Carpenter 2005 |
| Kessler | Densidad orbital | Kessler-Cour-Palais 1978 |
| Fuga cerebros | Docquier-Rapoport | Docquier-Rapoport 2012 |
| Behavioral Dynamics (caso 30) | Atractor de heading (segundo orden) | Fajen y Warren 2003, Warren 2006 |

## Limitaciones reconocidas

1. **Una sonda por caso:** la dependencia instrumental es limitación; programa multi-sonda como trabajo futuro.
2. **Ventanas cortas en algunos casos:** Riesgo Biológico (val_steps=9), Postverdad (8), Starlink (1) requieren cautela inferencial.
3. **Topología de retícula homogénea:** la condición de Nivel 5 (frontera espacial nítida) requeriría topologías heterogéneas (scale-free) ya implementadas en `common/topology_generator.py` pero no aplicadas masivamente.
4. **Baseline solo ABM-sin-ODE:** comparación con ARIMA/VAR como trabajo futuro.

## Conexión con el resto del manuscrito

- **Posición filosófica que justifica este corpus:** capítulo 02 (fundamentos);
- **Aparato formal del que κ es operacionalizado vía EDI:** capítulo 03;
- **Discriminación pública contra rivales (incluido Wolfram):** capítulo 04-01;
- **Caso ancla canónico (caso 30, behavioral dynamics):** capítulo 05-05 + `30_caso_behavioral_dynamics/`;
- **Conclusión demostrativa con condiciones de fracaso:** capítulo 06-01.

## Trazabilidad

La trazabilidad histórica del crecimiento del corpus, las decisiones metodológicas y el desarrollo del caso behavioral dynamics está documentada en `Bitacora/`. La fuente de verdad del manuscrito son los `outputs/metrics.json` versionados en cada caso.

## Cierre

Este corpus es la prueba empírica del irrealismo operativo. No es ilustración de la tesis: es su demostración bajo intervención controlada con datos públicos, semillas fijas, controles de falsación rechazados, y discriminación entre fenómenos con y sin cierre operativo. Lo que el aparato formal del capítulo 03 promete operativamente, este corpus lo entrega cuantitativamente sobre 30 dominios heterogéneos.
