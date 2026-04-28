# Anexo A.1. Glosario operativo

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

### Hiperobjeto (operativo)
Constructo del entendimiento que designa un fenómeno de cualquier escala con cierre operativo alto (Nivel 4+) que excede la captura intuitiva inmediata. No restringido a gran escala temporal o espacial: aplica desde decoherencia cuántica (caso 31) hasta cúmulos globulares (caso 40), pasando por dinámica social macro. No implica existencia metafísica adicional. Heurística de candidatura inspirada en Morton (2013) pero usada en sentido operativo y multiescalar. Capítulo 02-01.

### Irrealismo operativo
Posición filosófica del manuscrito: realismo estructural moderado + pluralismo epistemológico + anti-reificación operativa. Ni realismo ingenuo, ni instrumentalismo puro, ni irrealismo radical. Capítulo 02-01.

### Self-organization
Modelo positivo de la emergencia. Estabilización dinámica del sistema acoplado bajo restricciones físicas, informacionales y de tarea, sin postular sustancias nuevas. Causalidad circular upward+downward, ambas materiales. Capítulo 02-04.

---

## Términos introducidos en V5 (2026-04-28)

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

### Complementarismo metodológico
Postura sobre la relación entre métodos en tercera persona (aparato EDI) y métodos fenomenológicos en primera persona (Husserl, Merleau-Ponty, Thompson, Varela). Son métodos diferentes para fenómenos distintos pero ontológicamente continuos. La tesis no elimina ninguno por reducción al otro; sostiene co-existencia disciplinada. Capítulo 05-01 §7.

### Estructuralismo matemático moderado
Postura sobre el estatus de las entidades matemáticas: las estructuras matemáticas (hipergrafos, ODE, espacios de fase) son representaciones formales de patrones reales del sustrato. NO son entidades platónicas independientes; NO son ficciones útiles sin referencia. Su validez depende de homomorfismo parcial con la dinámica material. Capítulo 03-01 §15.

### Inferencialismo brandomiano matizado
Teoría del significado adoptada: el significado de un término es su rol inferencial dentro de prácticas materialmente sostenidas (Brandom 1994). El significado de "atractor", "cierre operativo κ", "estructura pre-ontológica" se constituye por su rol inferencial dentro del aparato y del corpus, no por referencia ostensiva ni por ficción sin referencia. Capítulo 02-02 §3.5.

### Compresión sintáctica vs semántica
Distinción técnica: la compresión sintáctica preserva estructura formal (variables, ecuaciones, dependencias) sin atender al significado; la compresión semántica preserva además el rol inferencial dentro de la práctica disciplinar. La compresión κ del aparato EDI es principalmente sintáctica pero se vuelve semántica cuando la sonda se elige por su rol teórico disciplinar. Capítulo 02-02 §3.5.2.

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
