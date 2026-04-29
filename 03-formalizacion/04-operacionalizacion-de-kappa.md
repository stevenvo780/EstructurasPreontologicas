# Operacionalización del operador de compresión κ

## Por qué hace falta

La tesis define `κ` como operador que reemplaza un subgrafo por un nodo cuando el detalle interno deja de ser inferencialmente relevante para la pregunta Q. Esa definición es ontológicamente correcta y filosóficamente útil. No basta. Una compresión cuya legitimidad sólo se examina con discurso filosófico es vulnerable al mismo error que la tesis denuncia — sustitución nominal, formalismo vacío. Este capítulo cierra el hueco: convierte `κ` en un procedimiento empírico con criterio de admisión, criterio de fallo y test de reapertura.

## Tesis del capítulo

> Una compresión `κ(G) = G*` es legítima respecto de Q si y solo si existe un sistema dinámico de baja dimensión sobre `G*` que (a) reproduce, dentro de tolerancia, las trayectorias observadas, (b) preserva la topología de atractores, repulsores y bifurcaciones empíricamente identificada, (c) predice respuestas a perturbaciones e intervenciones discriminantes, y (d) no oculta una transición que sí ocurre en los datos.

Esto convierte κ en un objeto que cualquier tercero puede auditar.

## Procedimiento operativo

### Paso 1. Definir Q y los observables

Antes de comprimir, hay que fijar:

- la pregunta Q (qué se quiere explicar, predecir o intervenir);
- el conjunto de variables observables `X` y su régimen de medición;
- la tolerancia: qué diferencia entre modelo y datos cuenta como aceptable y cuál no.

Sin esos tres elementos, `κ` no se puede evaluar. Cualquier compresión parece bien o mal según el ojo del lector.

### Paso 2. Construir el grafo G a partir de medidas

Sobre las series temporales medidas se construye `G = (V, E, W, T)` con:

- `V` = variables observadas;
- `E` = dependencias detectadas (causales, de acoplamiento, de restricción);
- `W` = pesos estimados (covarianza condicional, sensibilidad a intervención, exponentes de Lyapunov locales, etc.);
- `T` = reglas de actualización compatibles con la física conocida del sistema.

`G` es el modelo no comprimido: representación más fina disponible bajo las restricciones de medición.

### Paso 3. Estimar la dimensionalidad efectiva

Sobre las series multivariadas se aplica un análisis de dimensionalidad efectiva. Métodos válidos según el caso:

- análisis de componentes principales (PCA) sobre las trayectorias;
- estimación de dimensión de correlación (Grassberger–Procaccia);
- estimación de dimensión intrínseca por vecinos más cercanos;
- truncamiento por varianza explicada acumulada;
- exponentes de Lyapunov para detectar caos versus régimen de baja dimensión.

El resultado es un número `d` (con su intervalo de confianza) que indica cuántas dimensiones bastan para explicar la variabilidad relevante.

Este es el dato decisivo: si el sistema vive en baja dimensión, hay candidato a compresión legítima. Si la dimensionalidad efectiva es alta y no decae, la compresión a nodo único probablemente está mutilando.

### Paso 4. Identificar la topología dinámica

Sobre las trayectorias se identifica:

- atractores (puntos fijos estables, ciclos límite, estados cuasi-estacionarios);
- repulsores (puntos fijos inestables, regiones evitadas);
- bifurcaciones (transiciones cualitativas inducidas por parámetros de control o de tarea);
- regiones de biestabilidad o multiestabilidad.

Esta topología es la que cualquier `κ(G) = G*` debe preservar para ser legítima.

### Paso 5. Ajustar un sistema dinámico de baja dimensión

Sobre las `d` componentes principales (o variables conductuales clave) se ajusta un sistema:

```text
ẋ = f(x; θ)         con x ∈ ℝ^d, θ parámetros
```

Se prefieren formas funcionales con motivación física o ecológica (por ejemplo `mass–spring`, oscilador, ley de control informacional) sobre formas puramente fenomenológicas. La justificación es que las primeras se traducen mejor a B (categorías biomecánicas e informacionales).

### Paso 6. Validar empíricamente

Cuatro pruebas, todas necesarias:

1. **Reproducción**: ¿el sistema reducido reproduce las trayectorias medias observadas con error dentro de la tolerancia? Métrica habitual: proporción de varianza explicada en condiciones similares a las del entrenamiento.
2. **Generalización**: ¿predice trayectorias en condiciones no usadas para ajuste (otras condiciones iniciales, otros parámetros de tarea)?
3. **Topología**: ¿el campo vectorial del sistema reducido tiene los mismos atractores, repulsores y bifurcaciones que los datos?
4. **Intervención**: ¿predice correctamente qué pasa cuando se interviene una variable (perturbación, supresión informacional, cambio de parámetro físico)?

Si las cuatro pruebas pasan, `κ(G) = G*` es legítima respecto de Q. Si alguna falla, la compresión está empíricamente desautorizada.

### Paso 7. Identificar fronteras de validez y reabrir donde haga falta

Una compresión legítima no es legítima en todo el dominio. La práctica obliga a especificar:

- rango de condiciones donde el modelo reducido funciona;
- regiones donde aparecen fenómenos no capturados (típicamente cerca de bifurcaciones, en regímenes ruidosos, fuera del repertorio aprendido);
- variables que deben reabrirse mediante el operador `ε` para esas regiones.

`ε(n) = Gₙ` no es opcional: es la garantía pública de que la compresión no se volvió caja negra.

## Test público de fallo

Una compresión legítima debe poder ser refutada. La tesis exige especificar al menos una **predicción discriminante**: una observación o intervención cuyo resultado favorece al modelo reducido frente a un rival y cuyo resultado contrario lo desautorizaría.

Si una compresión propuesta no admite predicción discriminante, es una nominalización, no un modelo.

## Patología 1: la falsa baja dimensionalidad

Caso: el modelo reducido reproduce trayectorias medias pero falla bajo perturbaciones. Diagnóstico: el modelo capturó una correlación, no la dinámica. Remedio: ampliar `d`, reabrir variables ocultas, o admitir que el régimen no es de baja dimensión.

## Patología 2: el atractor reificado

Caso: el modelo reducido tiene un atractor que no aparece como estabilidad empírica robusta — solo como artefacto del ajuste. Diagnóstico: el atractor es nominal, no real. Remedio: eliminarlo de las clases admitidas o ampliar la base de datos hasta poder confirmar o falsar su existencia.

## Patología 3: el modelo que no se traduce a B

Caso: la dinámica de baja dimensión funciona pero ninguno de sus parámetros se traduce a una variable biomecánica, informacional o de tarea. Diagnóstico: el modelo es L3 desanclado. Remedio: reformular las funciones del sistema en términos de leyes de control con motivación ecológica o biomecánica, o degradar el modelo a estatus de descripción puramente nominal.

## Patología 4: la pregunta no fija tolerancia

Caso: la pregunta Q se enuncia sin tolerancia ni operacionalización. Diagnóstico: el test de fallo no se puede ejecutar; cualquier ajuste se acepta. Remedio: prohibir la admisión hasta que Q tenga criterios de éxito y de fracaso explícitos.

## Relación con el aparato formal previo

El procedimiento aquí descrito no sustituye los operadores `μ`, `G`, `H`, `κ`, `ε` del aparato anterior; los implementa.

- `μ` es el régimen de medición que produce los observables;
- `G` es el grafo construido a partir de esos observables;
- `H` aparece cuando hay relaciones de orden superior (acoplamientos múltiples, restricciones globales, agregaciones de tarea);
- `κ` es el procedimiento de los pasos 3–6;
- `ε` es el procedimiento del paso 7.

La tesis no inventa una matemática nueva — adopta el lenguaje estándar de la dinámica no lineal y le da papel filosófico explícito.

## Qué se gana

1. **Criterio público de admisión**: cualquier aplicación de la tesis puede ser auditada con métodos disponibles en la literatura empírica.
2. **Test público de fallo**: las compresiones admitidas deben poder romperse, lo que protege contra la sustitución nominal.
3. **Reversibilidad operacionalizada**: `ε` deja de ser conceptual y se vuelve protocolo de reapertura para regiones donde la compresión no funciona.
4. **Traducibilidad B ↔ L3**: la exigencia de que los parámetros del sistema reducido se traduzcan a variables biomecánicas, informacionales o de tarea cierra la posibilidad de un L3 flotante.

## Qué se pierde

Se pierde la posibilidad de aplicar la tesis a cualquier dominio sin medidas, sin protocolos de tarea y sin posibilidad de intervención. Eso es una pérdida deseable: marca que el modo demostrativo de la tesis exige fricción empírica real, y reserva el modo programático para los dominios donde esa fricción aún no está disponible.

## Niveles del paisaje de emergencia (clarificación)

La taxonomía operativa del corpus EDI distingue seis niveles (0–5):

**Tabla 3.4.1.**

| Nivel | Etiqueta | Definición operativa | Ejemplos del corpus |
|------:|----------|----------------------|---------------------|
| 0 | Null | EDI ≤ 0 o sin estructura macro detectable | Conciencia, Acidificación, Erosión |
| 1 | Trend | EDI > 0 sin significancia (p ≥ 0.05) | Justicia, Starlink, Clima |
| 2 | Suggestive | 0.01 ≤ EDI < 0.10, p < 0.05 | Finanzas, Salinización |
| 3 | Weak | 0.10 ≤ EDI < 0.30, p < 0.05 | Epidemiología, Behavioral Dynamics, Wikipedia |
| 4 | Strong | EDI ≥ 0.30, p < 0.01, `overall_pass = True` | Energía, Deforestación, Kessler, Riesgo Bio |
| 5 | Crítico | Convergencia bajo múltiples sondas + LoE = 5 + frontera espacial nítida | **(programa futuro, no alcanzado en el corpus actual)** |

**Aclaración explícita y reiterada del Nivel 5:** el Nivel 5 está definido como **horizonte programático del marco**, no como nivel alcanzado en el corpus actual. Sus condiciones (multi-sonda convergente con resultados consistentes, LoE = 5, topología heterogénea con frontera espacial nítida) son objetivos del programa de elevación documentado en `Bitacora/2026-04-28-cierre-doctoral/03-programa-multi-sonda.md`. El manuscrito no afirma haberlo alcanzado en ningún caso. Esta cláusula se reitera donde sea relevante para evitar la lectura de promesa no cumplida.

## Módulos metodológicos complementarios

La operacionalización de κ se complementa con módulos computacionales que refuerzan la inferencia estadística, la reproducibilidad y la auditabilidad del aparato. Cada módulo es código autocontenido en `09-simulaciones-edi/common/` con pruebas unitarias.

### Calibración estadística avanzada del p-value

La permutación simple con `n_perm=999` produce tasa empírica de tipo I cercana al 24 % bajo autocorrelación temporal. Los umbrales EDI son robustos (0 % de los random walk supera el umbral strong), pero la inferencia formal por p-value requiere calibración. El módulo `common/calibration.py` implementa:

1. **Block bootstrap** (Politis y Romano 1994): permutación por bloques de tamaño √n que preserva la autocorrelación local. El p-value bajo block-bootstrap se reporta junto al p-value naive para cuantificar el shift de calibración.
2. **Newey-West HAC** (Newey y West 1987): error estándar consistente bajo heterocedasticidad y autocorrelación, con kernel de Bartlett y truncamiento adaptativo `floor(4·(n/100)^{2/9})`.
3. **FWER Holm-Bonferroni** (Holm 1979): corrección de family-wise error rate sobre los casos del corpus. Aplicada al corpus completo: **14 casos inter-dominio + 8 casos inter-escala = 22 casos sobreviven Holm-Bonferroni a α=0.05**; los 4 casos macro `overall_pass=True` están entre los sobrevivientes (caso por caso documentado en `metrics.json::fwer_holm`). La clasificación strong sobrevive a la corrección por comparaciones múltiples.

### Replicación robusta sin replicador externo

El AUC-ROC = 0.886 declarado es ranking interno; un crítico podría atribuirlo a sobreajuste del investigador. El módulo `common/replication.py` ofrece tres pruebas que cualquier evaluador externo puede correr sobre los outputs versionados:

1. **`seed_robustness`**: distribución de EDI bajo cambio de semilla. Criterio: `max_drift ≤ 0.05`. Si la varianza inter-seed es alta, hay sobreajuste al ruido pseudoaleatorio.
2. **`holdout_temporal`**: EDI sobre la ventana out-of-sample (último 20 %). Criterio: `|EDI_test − EDI_full| ≤ 0.10`.
3. **`adversarial_probe_swap`**: aplica las sondas de un caso A sobre los datos de otro caso B. Si las sondas son específicas, el EDI cruzado debe ser ≤ 0.05. Extiende al corpus inter-dominio el test cruzado inter-escala que ya reportó 0/12 circularidad.

### Pre-registro criptográfico

La composición del corpus es post-hoc. El pre-registro en bitácora podría cuestionarse por modificación retroactiva. El módulo `common/preregistration.py` calcula SHA-256 sobre el setup completo de cada caso (excluyendo outputs y caches), junto con `git_commit_sha`, `git_dirty` y timestamp UTC. Cada caso conserva su `SETUP_HASH.json` y el corpus completo agrega su hash en `HASHES_PRE_EJECUCION.json`. La verificación reproducible está disponible vía `verify_setup_hash(case_id)`.

Esto no produce pre-registro retroactivo (lógicamente imposible); produce pre-registro mecánico de cualquier ejecución futura y garantía criptográfica de la coincidencia setup–código–resultado.

### Sondas teóricamente independientes

Ningún caso del corpus actual cumple los tres criterios de κ-ontológica fuerte simultáneamente. El primer criterio —convergencia bajo sondas con motivación teórica distinta— es el único alcanzable sin replicación inter-grupo externa. El módulo `common/full_secondary_probes.py` implementa una sonda secundaria por cada caso del corpus, con motivación radicalmente distinta a la primaria.

**Tabla 3.4.2.**

| Caso | Sonda primaria | Sonda secundaria |
|------|----------------|------------------|
| 04 Energía | Lotka-Volterra ecológico | Maxwell-Boltzmann termodinámico |
| 16 Deforestación | von Thünen económico-espacial | Fisher-KPP difusión reactiva |
| 27 Riesgo biológico | SIR epidemiológico | Catastrophe theory de Zeeman |
| 09 Finanzas | Soros-Taleb reflexividad | Heston volatilidad estocástica |
| 41 Wolfram | Logística sobre densidad | Markov compression cuantizada |
| 42 Histéresis institucional | Cusp de Zeeman | Bisección de threshold por panel |

Cuando los `metrics.json` no exponen los arrays primarios `obs/abm/forcing`, las sondas se evalúan sobre proxys derivados del EDI publicado. La verificación definitiva del primer criterio κ-ontológica requiere re-ejecutar el corpus con dump de arrays. Es deuda metodológica fechada, no deuda externa indefinida.

### Análisis de sensibilidad a umbrales

El módulo `common/threshold_sensitivity.py` barre la grilla `weak_low ∈ {0.05, 0.075, 0.10, 0.125, 0.15} × strong_low ∈ {0.20, 0.25, 0.30, 0.35, 0.40}` y reporta para cada caso la clasificación invariante. Los casos siempre strong bajo toda la grilla razonable (Energía, Deforestación, Microplásticos) tienen clasificación independiente de la elección de umbrales. La declaración del cap 06-01 §5.4 sobre sensibilidad de la composición a la elección de umbrales queda mecanizada y verificable.

### Análisis de potencia estadística

El módulo `common/power_analysis.py` distingue `null_real` (potencia ≥ 0.80 para detectar EDI weak) de `null_por_potencia_insuficiente` (n insuficiente para alcanzar potencia 0.80). De los 17 casos null en el corpus actual, 4 son null reales y 13 son null por potencia insuficiente; estos últimos requieren n ≥ 124 vs n actual entre 8 y 19. El manuscrito, en consecuencia, no afirma ausencia de cierre operativo en esos 13 casos: afirma falta de resolución estadística para detectarlo bajo el régimen actual.

### Información efectiva como métrica auxiliar (declaración)

El módulo `09-simulaciones-edi/common/hybrid_validator.py:249` implementa una función `effective_information(obs, full_pred, reduced_pred) = H(residuos_reducido) − H(residuos_completo)`, donde `H` es entropía diferencial estimada por KDE gaussiana. El valor se persiste en `metrics.json::effective_information` para cada caso del corpus.

**Estatuto declarado:** esta cantidad es **métrica auxiliar reportada por convención**, no métrica central del aparato. La tesis hace explícitas tres aclaraciones para evitar confusión con la tradición IIT:

1. **No es la "Effective Information" de Hoel-Albantakis-Tononi** (2013, *PNAS* 110:19790-19795) ni de Tononi (2008, *Biological Bulletin* 215:216-242). Aquellas se calculan sobre matrices de transición discretas con intervención uniforme `do(C = c)` y miden información mutua entre causa y efecto bajo ese ensemble. La función del aparato calcula diferencia de entropía de residuos predictivos; son cantidades **conceptualmente distintas**.
2. **No hay compromiso con IIT.** La tesis no afirma que el sistema acoplado tenga "phi", "experiencia integrada" o cualquier propiedad protoconsciente de la familia IIT. La discusión filosófica con causal emergence (Hoel 2017) en cap 02-05 §2.5 se mantiene como diálogo conceptual, no como adopción operativa.
3. **No es árbitro.** La métrica central del aparato es **EDI** (cap 03-04 §"EDI") y la inferencia procede por permutación 999 + bootstrap 500 + C1-C5 + FWER Holm-Bonferroni. La información efectiva auxiliar se reporta como descriptor adicional para evaluadores que la pidan, nunca como justificación de admisión.

**Decisión documentada:** la función se mantiene en el código por trazabilidad histórica (estaba presente en el pipeline desde la primera versión) y como descriptor opcional. Su valor no entra en QES, no entra en `overall_pass`, no entra en la clasificación del paisaje de emergencia. Si una pasada futura del aparato decidiera elevarla a métrica central, requeriría rediseño explícito documentado en bitácora con calibración contra IIT estándar.

### Auditoría de calidad de evidencia (QES)

El módulo `common/quality_scorer.py` asigna a cada caso siete puntajes Qi ∈ [0, 1]:

- **Q1** trazabilidad de datos (FETCH_MANIFEST con SHA-256 y URL).
- **Q2** tamaño efectivo (n y potencia para detectar EDI weak).
- **Q3** calidad de sonda (protocolo con ecuación y cita disciplinar).
- **Q4** reproducibilidad mecanizada (SETUP_HASH, git_commit, seed).
- **Q5** convergencia multi-sonda con motivación independiente.
- **Q6** Level of Evidence (escala 1–5).
- **Q7** calibración estadística (block bootstrap, FWER, Newey-West).

QES total es media ponderada con pesos justificados. Las categorías de admisión son: ROBUSTO (QES ≥ 0.85), DEMOSTRATIVO (0.70–0.85), PROGRAMÁTICO (0.55–0.70), PILOTO (0.40–0.55), INADMISIBLE (< 0.40). El umbral inferior funciona como filtro contra paper-science: ningún caso del corpus actual cae bajo 0.40.

Algunos casos tienen funciones específicas que justifican categorías ROBUSTO especializadas: los controles de falsación son robustos cuando, por diseño, no sobreviven el FWER; los casos límite del aparato (consciencia, erosión dialéctica) son robustos como documentación operativa de los límites declarados; el caso Wolfram extendido es robusto cuando, por diseño, no converge inter-paradigma sobre datos de irreducibilidad computacional. La uniformización forzada de estos casos como ROBUSTO genérico sería ella misma paper-science, dado que su rol filosófico exige clasificaciones específicas.

### Pipeline ejecutable

`09-simulaciones-edi/scripts/run_full_pipeline.py` orquesta las etapas (generación de FETCH_MANIFEST → SETUP_HASH → protocolos → enrichment → sondas independientes → análisis de potencia → sensibilidad a umbrales → auditoría QES) en una invocación única reproducible. Cualquier evaluador externo puede correr el pipeline sobre el repositorio congelado bajo el commit declarado y obtener bit-a-bit los mismos resultados.

## Cierre

La operación κ deja de ser un acto interpretativo y se convierte en un protocolo reproducible. Esto permite mostrar cómo Warren (2006) ya implementó, sin nombrarla así, esta misma operacionalización: identificó variables conductuales clave, midió series, ajustó sistemas dinámicos de baja dimensión, validó atractores, predijo bifurcaciones, e indicó las regiones donde el modelo se queda corto. Esa coincidencia no es accidente; es la confirmación de que la tesis y la práctica investigadora más rigurosa de percepción–acción comparten el mismo esqueleto operativo.

Los módulos complementarios reducen seis de las limitaciones declaradas en el capítulo de limitaciones consolidadas (calibración del p-value, replicación inter-grupo simulada, pre-registro mecanizado, sensibilidad a umbrales, control del error de tipo II, primer criterio de κ-ontológica) sin reabrir debate conceptual ni re-ejecutar el corpus completo. Las deudas restantes (datos reales en el corpus inter-escala, validación inter-grupo externa, datos VENLab para el caso 30) están fechadas como deuda externa explícita en ese capítulo.
