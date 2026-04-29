# Glosario operativo

## Función

Este glosario define todos los términos centrales del manuscrito en su uso operativo. Cada término viene con: definición precisa, capítulo donde se desarrolla, conexión con la métrica empírica EDI cuando aplica.

---

## Términos del núcleo conceptual

### Anti-reificación operativa
Disciplina metodológica que prohíbe inferir ontología fuerte solo por rendimiento predictivo. Nunca afirmamos `X es Y`; afirmamos `bajo el instrumento I, X exhibe cierre operativo de grado G`. Capítulo 02-01.

### Atractor empírico
Estado o región del espacio de fase hacia el cual convergen las trayectorias del sistema bajo perturbación acotada. Operacionalización de **estructura pre-ontológica** y de **patrón estabilizado**. Identificable mediante series temporales con análisis de cuenca de atracción. Capítulo 02-01.

### Cierre operativo
Propiedad medida del trío {fenómeno, sonda ODE, diseño ABM} cuya constricción macro→micro es irreducible y significativa. Cuantificada por EDI. La validación fuerte (Nivel 4) exige además gate completo (`overall_pass=True`). Capítulo 03-04.

### Compresión multiescala
Operación epistemológica que reemplaza una subestructura compleja `G' ⊂ G` por una unidad operativa `n_{G'}` cuando el detalle interno no produce diferencia inferencial relevante para la pregunta `Q`. Operador formal `κ : G → G*`. Capítulo 02-02 (filosófica), 03-04 (empírica vía EDI).

### Dossier de anclaje
Filtro de admisión obligatorio para cualquier categoría candidata. Catorce componentes: pregunta Q fechada, variables operacionalizadas, sustrato instanciante, grafo G, hipergrafo H si procede, compresión κ, atractores identificados, pruebas de validación, predicción discriminante, intervención discriminante, operador ε, traducción B↔L3, limitaciones, comparación rival. Capítulo 03-02.

### EDI (Effective Dependence Index)
Métrica empírica que opera el operador κ. Definición: `EDI = 1 - RMSE_coupled / RMSE_no_ode`. Mide la degradación predictiva al apagar el acoplamiento ODE→ABM manteniendo el forcing exógeno. Significancia por permutación 999, CI por bootstrap 500. Capítulo 03-04.

### Estructura pre-ontológica
Regularidad operativa anterior a la objetualidad sustancial. Ni cosa con esencia, ni ficción lingüística. Identificable como atractor empíricamente robusto de un sistema dinámico acoplado. Núcleo del nombre del proyecto. Capítulo 02-01.

### Irrealismo operativo
Posición filosófica del manuscrito: realismo estructural moderado (en sentido operativo no-Ladyman, ver entrada siguiente) + pluralismo epistemológico + anti-reificación operativa. Ni realismo ingenuo, ni instrumentalismo puro, ni irrealismo radical. Capítulo 02-01.

### Realismo estructural moderado (uso operativo)
Compromiso filosófico de la tesis con la realidad de las estructuras —entendidas aquí como atractores empíricamente identificables sobre sustrato material dinámico— sin reducirla a estructura sin relata. **Declaración explícita de no-importación:** la tesis NO adopta la versión *ontic structural realism* de Ladyman y Ross (2007, *Every Thing Must Go*, §2.4), donde la estructura agota lo real y los relata son eliminables. La tesis exige sustrato material sosteniendo la estructura (cap 02-01 §1.1). Cualquier referencia textual a "realismo estructural moderado" en el cuerpo del manuscrito debe leerse bajo esta convención. Capítulo 02-01 §0.3.

### Self-organization (sentido técnico)
Modelo positivo de la emergencia anclado en la tradición Maturana-Varela (1980, *Autopoiesis and Cognition*) y Haken (1977, *Synergetics*). Designa la estabilización dinámica del sistema acoplado bajo restricciones físicas, informacionales y de tarea, sin postular sustancias nuevas. Causalidad circular upward+downward, ambas materiales. **No es invocación retórica:** cualquier ocurrencia textual no anclada disciplinarmente debe sustituirse por "estabilización dinámica" o "convergencia a atractor". Capítulo 02-04 §4.

### Sinónimos coloquiales del núcleo conceptual (convención)
Los términos "patrón estabilizado", "regularidad operativa", "estructura operativa" y "cuenca de atracción" (cuando aparece como sinónimo del atractor en lugar de como concepto técnico distinto) se usan en el manuscrito como **registros coloquiales** de los dos términos canónicos: **estructura pre-ontológica** (lectura ontológica) y **atractor empírico** (lectura operacional). El cuerpo argumental privilegia los canónicos cuando la precisión filosófica es decisiva; los coloquiales se admiten para fluidez prosódica, sin valor técnico distinto. Esta convención se documenta aquí para evitar la lectura como cuatro conceptos distintos.

---

## Términos operativos del marco

### Naturalismo metafísico moderado
Compromiso filosófico de partida explícitamente declarado, no conclusión demostrada: el sustrato material dinámico se asume como punto de partida, justificado por continuidad con la ciencia, parsimonia ontológica y capacidad operativa del aparato. Compatible con realismo estructural moderado; rechaza dualismo, idealismo, panpsiquismo, emanacionismo, creacionismo y pluralismo de planos sustanciales. Capítulo 02-01 §0.1.

### Pre-ontológico (sentido genético-epistemológico)
Estructura es pre-ontológica si y sólo si: (a) es regularidad operativa materialmente sostenida; (b) es previa al recorte categorial nominalizante; (c) es génesis de lo individuado (Simondon); (d) es operativamente identificable como atractor empírico. NO significa "anterior temporalmente"; significa "anterior al recorte categorial". Capítulo 02-01 §0.2.

### B-series relacional
Postura ontológica sobre el tiempo: los eventos están ordenados en serie *anterior–simultáneo–posterior* sin presente metafísicamente privilegiado. Eternalismo moderado. La flecha del tiempo es termodinámica, no metafísica. Compatible con relatividad especial y con la generalidad multiescalar requerida por la tesis. Capítulo 02-05 §1.

### Manipulabilidad woodwardiana
Postura sobre la causalidad: X causa Y si y sólo si una intervención sobre X (independiente del resto del sistema) produce un cambio sistemático en Y. Operacionalizada por el aparato EDI vía intervención ablativa (`do(coupling = 0)`). Compatible con el `do`-calculus de Pearl. Capítulo 02-05 §2.

### Constitución descendente (downward constitution)
Relación distinta de causación: X constituye Y si X es parte de la realización material de Y, verificable por manipulabilidad mutua de Craver. La constricción macro→micro del aparato EDI es **constitutiva, no causal**: el atractor macro constituye las restricciones del componente sin causar nuevos eventos por encima del cierre físico. Neutraliza el argumento de exclusión causal de Kim por modus tollens vacuo. Capítulo 02-05 §2.4.

### Atractor normativo
Valor (justicia, libertad, dignidad, verdad, belleza) entendido NO como entidad sustancial separada sino como región del espacio de fase de la conducta colectiva donde el sistema converge bajo perturbación, materialmente sostenido por prácticas, inscripciones, cuerpos en relación, sanciones organizadas y memoria histórica. Capítulo 02-06 §2.

### Complementarismo metodológico (alcance acotado)
Postura sobre la relación entre métodos en tercera persona (aparato EDI) y métodos fenomenológicos en primera persona. La tesis sostiene **co-existencia disciplinada acotada**: reconoce que los métodos fenomenológicos (Husserl, Merleau-Ponty, Thompson, Varela) operan sobre fenómenos ontológicamente continuos con los del aparato, pero **no integra engagement fenomenológico sustantivo** en el cuerpo argumental. La promesa fenomenológica del abstract es **declarativa**, no operativa: el manuscrito declara que el irrealismo operativo es compatible con el complementarismo, sin desarrollar el complementarismo como capítulo. Esta limitación se reconoce explícitamente en cap 05-01 §7 y en el régimen de validez declarado del front matter. Quien busque engagement fenomenológico desarrollado deberá consultar la deuda explícita en cap 06-03 §"Programa de extensiones fenomenológicas".

### Estructuralismo matemático moderado
Postura sobre el estatus de las entidades matemáticas: las estructuras matemáticas (hipergrafos, ODE, espacios de fase) son representaciones formales de patrones reales del sustrato. NO son entidades platónicas independientes; NO son ficciones útiles sin referencia. Su validez depende de homomorfismo parcial con la dinámica material. Capítulo 03-01 §15.

### Inferencialismo brandomiano matizado
Teoría del significado adoptada: el significado de un término es su rol inferencial dentro de prácticas materialmente sostenidas (Brandom 1994). El significado de "atractor", "cierre operativo κ", "estructura pre-ontológica" se constituye por su rol inferencial dentro del aparato y del corpus, no por referencia ostensiva ni por ficción sin referencia. Capítulo 02-02 §3.5.

### Compresión sintáctica vs semántica
Distinción técnica: la compresión sintáctica preserva estructura formal (variables, ecuaciones, dependencias) sin atender al significado; la compresión semántica preserva además el rol inferencial dentro de la práctica disciplinar. La compresión κ del aparato EDI es principalmente sintáctica pero se vuelve semántica cuando la sonda se elige por su rol teórico disciplinar. Capítulo 02-02 §3.5.2.

### Flecha termodinámica
Dirección de aumento de entropía en sistemas cerrados (segunda ley). En la tesis se distingue de la flecha cosmológica (expansión del universo) y de la flecha psicológica (percepción subjetiva pasado–presente–futuro), y se afirma como ontológicamente fundamental: las otras dos son derivadas. La irreversibilidad parcial de κ↔ε (la compresión preserva dependencias decisivas pero la expansión no recobra detalle perfectamente) es manifestación local de esta flecha, no propiedad lógica adicional. Capítulo 02-05 §1.2.

### Eternalismo moderado
Postura ontológica sobre el tiempo: pasado, presente y futuro son igualmente reales en sentido relacional B-series, sin que exista un "presente metafísicamente privilegiado". Compatible con la relatividad especial. La tesis adopta esta postura como mínimo ontológico requerido para que los atractores (objetos definidos por evolución temporal completa) sean coherentes. Capítulo 02-05 §1.1.

### Manipulabilidad mutua (Craver)
Criterio constitutivo (no causal): X es constitutivamente relevante para S si y sólo si manipular X cambia S y manipular S cambia X. Es la operacionalización de la constitución descendente que la tesis usa para neutralizar el argumento de exclusión causal de Kim. Capítulo 02-05 §2.4.

### Intervención ablativa
Operación que apaga el acoplamiento ODE↔ABM manteniendo el forcing exógeno y compara la predicción coupled con la no-coupled. Es la operacionalización woodwardiana de causalidad sobre variables del sistema acoplado y la base de la métrica EDI. Capítulo 03-04 §"EDI".

### Argumento de exclusión causal (Kim)
Argumento de Jaegwon Kim (1998) según el cual, dado el cierre causal del dominio físico y la sobreviniencia de las propiedades macro M sobre las propiedades micro P, M no puede tener poder causal independiente sin sobredeterminación o epifenomenalismo. La tesis responde distinguiendo causación de constitución: el atractor macro constituye restricciones, no produce eventos por encima del cierre físico. Capítulo 02-05 §2.4.

### Block bootstrap (Politis-Romano 1994)
Permutación que preserva la autocorrelación temporal de las series mediante bloques contiguos. La variante stationary bootstrap usa bloques de longitud geométrica aleatoria (parámetro 1/block_size); la variante moving block usa bloques de longitud fija. La implementación canónica del aparato (`common/calibration.py`) provee ambas; el módulo declara explícitamente cuál se usa. Capítulo 03-04 §"Calibración estadística avanzada".

### FWER Holm-Bonferroni
Corrección de family-wise error rate sobre comparaciones múltiples. Aplicada al corpus inter-dominio reduce los casos significativos sin corrección a los que sobreviven α=0.05 tras ajuste secuencial Holm. Sirve como filtro de significancia colectiva; no sustituye la inferencia individual por caso. Capítulo 03-04.

### Información efectiva (uso auxiliar)
Cantidad reportada en `metrics.json::effective_information` definida operacionalmente como `H(residuos_reducido) − H(residuos_completo)` con `H` = entropía diferencial KDE. Se calcula en `09-simulaciones-edi/common/hybrid_validator.py:249`. **No es la Effective Information de Hoel-Albantakis-Tononi** (2013, *PNAS* 110:19790-19795); no implica adopción de IIT. Métrica **auxiliar**, no central: no entra en QES, no entra en `overall_pass`, no entra en la clasificación del paisaje de emergencia. La inferencia central procede por EDI + permutación 999 + bootstrap 500 + FWER Holm. Capítulo 03-04 §"Información efectiva como métrica auxiliar (declaración)".

### Auditoría criptográfica del setup
Cálculo de SHA-256 sobre el código, parámetros y datos de entrada de cada caso, junto con git_commit_sha y timestamp UTC. Permite verificar que el setup actual coincide con el setup que produjo los outputs publicados. NO es pre-registro estricto en plataforma externa (que requeriría depósito previo a ver los datos en OSF u homólogo); es cadena de custodia computacional. Capítulo 03-04 §"Pre-registro criptográfico".

---

## Operadores formales

### μ (operador de medición)
`μ : R → X`. Recorta el dominio efectivo de realidad `R` en variables observables `X` con régimen de medición `R` especificado. Capítulo 03-01.

### G (grafo basal)
`G = (V, E, W, T)`. Representa dependencias entre variables: V nodos, E aristas, W pesos, T reglas dinámicas. Cada arista pasa criterio de admisión por intervención (`do`-test). Capítulo 03-01.

### H (hipergrafo)
`H = (V, 𝓔)`. Hiperaristas conectan conjuntos de nodos cuando la dependencia conjunta no se reduce sin pérdida a relaciones binarias. Capítulo 03-01.

### κ (compresión)
`κ : G → G*`. Reemplaza subestructuras complejas por unidades operativas. Operacionalizado empíricamente vía EDI. Capítulo 03-01 + 03-04.

### ε (expansión)
`ε : n → G_n`. Abre un nodo comprimido cuando la pregunta exige más detalle. Garantiza reversibilidad de κ. Capítulo 03-01.

### Q (pregunta paramétrica)
`Q = (φ, τ, R)`. Triple fechado: formulación φ, tolerancia τ, régimen de medición R. Cambiar Q después del fallo invalida el ciclo. Capítulo 03-01.

---

## Niveles del paisaje de emergencia

### Nivel 0 (null)
EDI ≤ 0. Sin cierre operativo detectable. 8 casos del corpus.

### Nivel 1 (trend)
EDI > 0, p ≥ 0.05. Indicios sin significancia. 4 casos.

### Nivel 2 (suggestive)
EDI > 0.01, p < 0.05. Constricción débil. 2 casos.

### Nivel 3 (weak)
0.10 ≤ EDI < 0.30, p < 0.05. Componente funcional con significancia. Análogo al ribosoma: tiene función pero no es organismo autónomo. 8 casos (incluido caso 30 v2).

### Nivel 4 (strong)
0.30 ≤ EDI ≤ 0.90, p < 0.05 (con `overall_pass=True` para gate completo). Cierre operativo alto. **En el corpus inter-dominio:** 5 casos (4 con gate + 1 sin gate). **En el corpus inter-escala:** 7 casos en 7 escalas distintas (atómica, cuántica, bioquímica, celular oscilatoria, individual, astrofísica, astrofísica masiva).

### Nivel 5 (cierre operativo fuerte)
Strong + convergencia bajo múltiples sondas independientes + LoE = 5 (datos físicos directos) + frontera espacial nítida verificada. Programa futuro. Ningún caso del corpus actual lo alcanza, en ninguna escala. Definido con criterios operativos explícitos en cap 03-04 §"Niveles del paisaje" para evitar lectura como promesa no cumplida.

---

## Registros de descripción (asimetría L1↔B↔L3↔S)

### L1 (psicológico/ordinario)
Categorías heredadas del lenguaje ordinario. Fija qué pregunta importa pero no responde por sí sola. Vínculo indirecto y restrictivo con L3. Capítulo 02-04.

### B (conductual-biológico, físico-ecológico, técnico-institucional)
Nivel material-instanciante. Ancla la respuesta. Variables: organismo + entorno + información + tarea + historia (en dominio biológico-conductual); o componentes físicos, técnicos, institucionales según dominio. Vínculo directo y traduccional con L3. Capítulo 02-04.

### L3 (estructural-relacional formal)
Modelos dinámicos, grafos, hipergrafos, leyes de control. Reconstruye formalmente las dependencias detectadas en B. Capítulo 02-04.

### S (semántica revisada)
Categorías que sobreviven a la auditoría. Se gana solo a posteriori. Capítulo 02-04.

---

## Protocolo C1-C5

### C1 Convergencia
`RMSE_coupled < RMSE_no_ode`. Sin mejora respecto a baseline, no hay señal.

### C2 Robustez
Clasificación estable bajo ±20% de perturbación de parámetros.

### C3 Determinismo aleatorio
Semilla fija (`seed=42`). Reproducibilidad bit-a-bit.

### C4 Consistencia de dominio
Trayectorias respetan restricciones físicas (no-negatividad, conservación). Direccionalidad coherente con la teoría del dominio. Magnitudes plausibles según literatura.

### C5 Reporte de incertidumbre
CI bootstrap, modos de fallo, LoE, val_steps reportados con su implicación inferencial.

---

## Niveles de Evidencia (LoE)

**Tabla A.1.1.**

| LoE | Descripción | Ejemplos |
|----:|-------------|----------|
| 1 | Especulativo | Proxies indirectos, encuestas subjetivas, datos sintéticos sin ground truth |
| 2 | Débil | Datos digitales traza con alto ruido semántico (caso 30 cae aquí) |
| 3 | Medio | Datos estructurados pero incompletos o de corto plazo (<5 años) |
| 4 | Fuerte | Series temporales consistentes, múltiples fuentes, >10 años |
| 5 | Robusto | Datos físicos directos (sensores), estandarizados, >30 años |

---

## Modos de admisión de aplicaciones

### Modo demostrativo
Caso paradigmático trabajado a fondo: dossier completo de catorce componentes, datos públicos, ecuaciones ajustadas, predicciones cumplidas, intervenciones documentadas, comparación rival con discriminación verificable. Capítulo 05-00.

### Modo programático
Conjetura articulada con criterio explícito de elevación: qué datos faltan, qué rival se enfrentaría, qué predicción discriminante se buscaría. La marca `MODO PROGRAMÁTICO` es obligatoria. Capítulo 05-00.

---

## Otros términos del aparato

### overall_pass
Gate completo de validación: 13 condiciones simultáneas (C1-C5 + 8 adicionales). Estado más fuerte de admisión.

### val_steps
Tamaño de la ventana de validación. Restricción inferencial: ≥24 mensual / ≥10 anual = inferencia estándar; <5 = exploratorio.

### Symploké CR (Cohesion Ratio)
Indicador de frontera funcional. CR > 2.0 sugiere frontera espacial nítida (programa de Nivel 5).

### Sonda macro (ODE)
Instrumento computacional que genera la señal macro candidata. No agota el fenómeno; estima su grado de cierre operativo mediante el acoplamiento con el nivel micro. Ejemplos: Budyko-Sellers (clima), von Thünen (deforestación), Jambeck (microplásticos), behavioral_attractor (Fajen-Warren).

### Paisaje de emergencia
Conjunto ordenado de fenómenos clasificados por su grado de cierre operativo. Resultado principal de la tesis, no solo los Nivel 4.

### Brecha instrumento-fenómeno
Cláusula epistemológica: cada resultado describe el trío {fenómeno, instrumento, pregunta}. Reconocida explícitamente como condición epistémica honesta, no como debilidad.

### Programa multi-sonda
Trabajo futuro: validar 3-5 casos clave con sondas ODE alternativas. La convergencia inter-sonda fortalecería cada resultado.

### ABM (Agent-Based Modeling)
Simulación micro: retícula 40×40 de agentes con difusión espacial y acoplamiento al estado macro. Implementación CPU/GPU disponible.

### ODE (Ordinary Differential Equation)
Sonda macro: ecuación diferencial domain-specific que genera la señal macro candidata.

### Acoplamiento bidireccional
Coupling ABM↔ODE: la sonda macro afecta a la dinámica micro y viceversa cuando hay feedback configurado.

---

## Términos de la teoría conductual (caso 30 y caso ancla)

### Behavioral dynamics
Marco teórico de Warren (2006): comportamiento adaptativo orientado a meta sin postular controlador centralizado. La organización emerge de la interacción agente-entorno bajo restricciones físicas, informacionales y de tarea.

### Variable τ (tau)
Razón entre tamaño angular óptico y su tasa de cambio. Especifica tiempo hasta contacto (Lee 1976).

### Variable τ_bal
`θ/θ̇`. Razón entre ángulo del palo y velocidad angular. Especifica tiempo hasta vertical (Foo, Kelso, Guzman 2000).

### Información ecológica
Patrones detectables del flujo óptico, acústico y háptico que estructuran el entorno. Materialmente real, no representación interna. Capítulo 02-04.

### Heading φ
Dirección de marcha actual. Variable conductual clave en locomoción (Fajen y Warren 2003).

### Error de heading β_h
`(φ - ψ_g)`. Ángulo entre heading actual y dirección de meta. Observable principal del caso 30.

---

## Cierre

Cada término del glosario se usa de manera consistente en todos los capítulos del manuscrito. Cuando un capítulo introduce un término nuevo, se añade aquí con su definición operativa y referencia cruzada.
