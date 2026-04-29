

<div id="frontmatter"></div>


<div id="front-matter"></div>

# Estructuras Pre-Ontológicas

## Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio

**Tesis doctoral en Filosofía de la Ciencia y Ciencias de la Complejidad**

**Universidad de Antioquia · Medellín · Colombia**

---

### Autoría declarada

**Autor principal (concepto y dirección teórica):** Jacob Agudelo. Universidad de Antioquia.

**Colaborador (técnica e ingeniería computacional):** Steven Vallejo Ortiz.

**Director de tesis:** [pendiente de declaración formal — bloqueador procedimental conocido; documentación administrativa fuera del manuscrito en `00-proyecto/04-formalizacion-institucional.md`].

**Co-autoría con inteligencia artificial declarada:** Anthropic Claude (Opus 4.7), como instrumento de implementación bajo dirección humana. La IA no aparece como autora en el sentido legal ni epistémico: aparece como herramienta, igual que cualquier software estadístico avanzado. La declaración detallada del rol y los límites de la IA está en el capítulo de ética de investigación y gobernanza de datos (Parte II, cap. 5).

### Marco institucional

**Programa de inscripción:** Doctorado en Filosofía. Línea: filosofía de la ciencia y ciencias de la complejidad.

**Estado del manuscrito:** integral defendible. La formalización institucional completa se conserva como documentación administrativa del repositorio, fuera del cuerpo argumental.

**Versión consolidada:** 2026-04-28.

### Sobre la disponibilidad y la fuente de verdad del documento

> Documento ensamblado automáticamente desde el repositorio doctoral. La fuente de verdad textual son los capítulos individuales en cada carpeta numerada. La fuente de verdad numérica del corpus EDI son los `outputs/metrics.json` versionados en `09-simulaciones-edi/<caso>/`. Si hay discrepancia entre este ensamblado y la fuente, prevalece la fuente.

### Agradecimientos

A la Universidad de Antioquia, por sostener una tradición de filosofía de la ciencia que hace posible este trabajo. A los colegas y revisores que aportaron críticas tempranas. A los autores de los datasets públicos del corpus, sin los cuales la cartografía multidominio no sería viable. A William H. Warren y Brett R. Fajen por la conjetura cuantitativa de la behavioral dynamics que opera como caso ancla.


<div id="tabla-de-contenidos"></div>

# 📑 Tabla de Contenidos

> **Navegación:** este manuscrito tiene ~10 mil líneas. Las partes están agrupadas en secciones colapsables. Haz clic en ▸ para expandir cada parte. Cada capítulo termina con un enlace «↑ volver al índice» que regresa aquí.

## Navegación rápida por partes

- [Front matter](#frontmatter)
- [Introducción](#introduccion)
- [Parte I — Fundamentos ontológicos y epistemológicos](#parte-1-fundamentos)
- [Parte II — Aparato formal y método](#parte-2-metodo)
- [Parte III — Evidencia empírica](#parte-3-evidencia)
- [Parte IV — Discusión crítica](#parte-4-discusion)
- [Parte V — Cierre demostrativo](#parte-5-cierre)
- [Bibliografía](#bibliografia)
- [Apéndices técnicos mínimos](#apendices-tecnicos)

---

## Índice detallado

<details open>
<summary><b>Front matter</b></summary>

- [Front matter](#front-matter)
- [Resumen y abstract bilingüe](#resumen-y-abstract-bilingue)
- [Listas de figuras, tablas y abreviaturas](#listas-de-figuras-tablas-y-abreviaturas)
- [Glosario operativo](#glosario-operativo)

</details>

<details>
<summary><b>Introducción</b></summary>

- [Introducción](#introduccion)
- [Estado del arte](#estado-del-arte)

</details>

<details>
<summary><b>Parte I — Fundamentos ontológicos y epistemológicos</b></summary>

- [Capítulo 1: Ontología material-relacional](#capitulo-1-ontologia-material-relacional)
- [Capítulo 2: Epistemología de la compresión](#capitulo-2-epistemologia-de-la-compresion)
- [Capítulo 3: Categorías, objetos, propiedades, identidad](#capitulo-3-categorias-objetos-propiedades-identidad)
- [Capítulo 4: Anclaje empírico (nivel B multiescalar)](#capitulo-4-anclaje-empirico-nivel-b-multiescalar)
- [Capítulo 5: Temporalidad y causalidad](#capitulo-5-temporalidad-y-causalidad)
- [Capítulo 6: Dimensión normativa y ética](#capitulo-6-dimension-normativa-y-etica)

</details>

<details>
<summary><b>Parte II — Aparato formal y método</b></summary>

- [Capítulo 7: Aparato formal mínimo](#capitulo-7-aparato-formal-minimo)
- [Capítulo 8: Mapa de operadores formales](#capitulo-8-mapa-de-operadores-formales)
- [Capítulo 9: Criterios de legitimidad y dossier](#capitulo-9-criterios-de-legitimidad-y-dossier)
- [Capítulo 10: Plantilla del dossier de anclaje](#capitulo-10-plantilla-del-dossier-de-anclaje)
- [Capítulo 11: Auditoría ontológica como protocolo](#capitulo-11-auditoria-ontologica-como-protocolo)
- [Capítulo 12: Operacionalización de κ vía EDI](#capitulo-12-operacionalizacion-de-kappa-via-edi)
- [Capítulo 13: Validación lógica formal con ST](#capitulo-13-validacion-logica-formal-con-st)
- [Capítulo 14: Ética de investigación y gobernanza de datos](#capitulo-14-etica-de-investigacion-y-gobernanza-de-datos)

</details>

<details>
<summary><b>Parte III — Evidencia empírica</b></summary>

- [Capítulo 15: Criterios de admisión de aplicaciones](#capitulo-15-criterios-de-admision-de-aplicaciones)
- [Capítulo 16: Mapa de aplicaciones — corpus inter-dominio e inter-escala](#capitulo-16-mapa-de-aplicaciones---corpus-inter-dominio-e-inter-escala)
- [Capítulo 17: Caso ancla canónico — Behavioral Dynamics (Warren 2006)](#capitulo-17-caso-ancla-canonico---behavioral-dynamics-warren-2006)
- [Capítulo 18: Corpus inter-dominio (30 casos)](#capitulo-18-corpus-inter-dominio-30-casos)
- [Capítulo 19: Corpus inter-escala (10 casos)](#capitulo-19-corpus-inter-escala-10-casos)
- [Capítulo 20: Caso 30 — Behavioral Dynamics bajo EDI](#capitulo-20-caso-30---behavioral-dynamics-bajo-edi)
- [Capítulo 21: Aplicaciones programáticas — Mente, memoria, yo](#capitulo-21-aplicaciones-programaticas---mente-memoria-yo)
- [Capítulo 22: Aplicaciones programáticas — Biología y ecología](#capitulo-22-aplicaciones-programaticas---biologia-y-ecologia)
- [Capítulo 23: Aplicaciones programáticas — Sistemas técnicos distribuidos](#capitulo-23-aplicaciones-programaticas---sistemas-tecnicos-distribuidos)
- [Capítulo 24: Aplicaciones programáticas — Instituciones, mercado, Estado](#capitulo-24-aplicaciones-programaticas---instituciones-mercado-estado)

</details>

<details>
<summary><b>Parte IV — Discusión crítica</b></summary>

- [Capítulo 25: Debates con posiciones rivales](#capitulo-25-debates-con-posiciones-rivales)
- [Capítulo 26: Tabla comparativa con rivales](#capitulo-26-tabla-comparativa-con-rivales)
- [Capítulo 27: Anticipación de objeciones filosóficas](#capitulo-27-anticipacion-de-objeciones-filosoficas)
- [Capítulo 28: Limitaciones y puntos de presión](#capitulo-28-limitaciones-y-puntos-de-presion)
- [Capítulo 29: Limitaciones declaradas consolidadas](#capitulo-29-limitaciones-declaradas-consolidadas)

</details>

<details>
<summary><b>Parte V — Cierre demostrativo</b></summary>

- [Capítulo 30: Conclusión demostrativa](#capitulo-30-conclusion-demostrativa)
- [Capítulo 31: Hoja de ruta post-defensa](#capitulo-31-hoja-de-ruta-post-defensa)

</details>

<details>
<summary><b>Bibliografía</b></summary>

- [Bibliografía consolidada](#bibliografia-consolidada)

</details>

<details>
<summary><b>Apéndices técnicos mínimos</b></summary>

- [Apéndice técnico 1: Tablas crudas del corpus inter-dominio](#apendice-tecnico-1-tablas-crudas-del-corpus-inter-dominio)
- [Apéndice técnico 2: Tablas crudas del corpus inter-escala](#apendice-tecnico-2-tablas-crudas-del-corpus-inter-escala)
- [Apéndice técnico 3: Figuras Mermaid](#apendice-tecnico-3-figuras-mermaid)

</details>

---

<div id="resumen-y-abstract-bilingue"></div>

# Resumen y abstract bilingüe

## Resumen (español)

Esta tesis defiende un **irrealismo operativo de estructuras pre-ontológicas**: una posición filosófica articuladora que combina realismo estructural moderado, pluralismo epistemológico y anti-reificación operativa **como ontología, epistemología y metodología generales aplicables a cualquier escala física, biológica o cosmológica donde el aparato pueda operar con sondas físicamente motivadas**. Las entidades, niveles y categorías con que pensamos cualquier dominio de realidad son patrones operativos identificables como atractores empíricos de sistemas dinámicos acoplados, admisibles solo bajo dossier de anclaje de catorce componentes, asimetría protocolar entre registros de descripción L1↔B↔L3↔S, y validación EDI (Effective Dependence Index) calculada por intervención ablativa.

El término **"pre-ontológico"** se entiende en sentido genético-epistemológico (Simondon): la estructura es pre-individual y anterior al recorte categorial nominalizante, no anterior temporalmente. La tesis adopta **naturalismo metafísico moderado** como compromiso de partida explícitamente declarado, **B-series relacional** para el tiempo, **manipulabilidad woodwardiana** para la causalidad operacionalizada por intervención ablativa, **constitución descendente** (Craver) en lugar de downward causation kim-vulnerable, y **complementarismo metodológico** entre métodos en tercera persona (aparato EDI) y métodos fenomenológicos en primera persona (Husserl, Merleau-Ponty, Thompson).

El aporte metodológico central es un instrumento computacional híbrido **ABM + ODE** que mide cierre operativo mediante EDI = 1 − RMSE_coupled / RMSE_no_ode, con prueba de permutación (999), bootstrap (500), y protocolo de validación robusta (C1-C5 más 8 criterios adicionales para *overall_pass*). El aparato se opera sobre cinco operadores formales (μ medición, G grafo, H hipergrafo, κ compresión, ε expansión) con pregunta paramétrica Q fechada y tolerancia explícita. **El aparato es invariante a la escala**: opera con la misma metodología desde la dinámica subatómica de espín-órbita (10⁻¹⁰ m, 10⁻¹⁵ s) hasta la dinámica gravitacional de cúmulos globulares (10²⁰ m, 10¹⁴ s).

Se evaluaron **40 casos agregados en dos corpus complementarios**: (a) **corpus inter-dominio** con 30 casos en dominios físicos, biológicos, socioeconómicos, tecnoculturales y conductuales (4 strong con `overall_pass`, 1 strong sin gate, 8 weak, 2 suggestive, 4 trend, 8 null, 3 controles de falsación rechazados); (b) **corpus inter-escala** con 10 casos en 8 escalas distintas, **30 órdenes de magnitud** espaciales y temporales cubiertos, con **7 strong en 7 escalas distintas** (atómica, cuántica, bioquímica, celular oscilatoria, individual, astrofísica, astrofísica masiva), 1 weak y 2 nulls honestos. El aparato sobrevive hostile testing severo (0/1500 falsos positivos del gate completo bajo random walk masivo, 0/12 circularidad detectada en test cruzado de sondas inter-escala). Validación lógica formal con suite ST de 24 teorías, seis hallazgos críticos detectados y corregidos.

**Los 40 casos son justificación operativa del marco tripartito general (ontológico + epistemológico + metodológico), no son la tesis.** La tesis son los tres marcos generales; el corpus muestra que las afirmaciones generales son ejecutables, discriminantes y transferibles. La generalidad no depende del tamaño del corpus.

La tesis discrimina públicamente contra catorce posiciones rivales identificables, incluido el Wolfram Physics Project, en al menos dos criterios cada una. Piloto Wolfram Rule 110 ejecutado mostrando convivencia de irreducibilidad computacional micro y cierre operativo macro detectable (EDI=0.55 sobre dos sondas independientes). La novedad no es de inventario sino de articulación: la combinación dossier de anclaje + asimetría L1↔B↔L3↔S + cartografía multidominio + multiescala con falsación rechazada constituye un programa de investigación auditable y falsable.

El resultado principal no es una validación binaria sino una **cartografía discriminante de cierre operativo** sobre el continuo de emergencia, transversal a escalas y dominios. El marco demuestra selectividad empírica, trazabilidad y falsabilidad instrumental: ni valida todo ni rechaza todo, y permite distinguir constricción operativa robusta de señal parcial o ausencia de señal. La fuerza inferencial final se interpreta en conjunto con tamaño de ventana, nivel de evidencia (LoE) y dependencia instrumento-fenómeno.

**Lección epistémica clave:** el caso 30 (behavioral dynamics) fue rechazado por el aparato en su versión inicial (EDI=0.002, no significativo) a pesar de la expectativa de aceptación del equipo investigador. La sonda mejorada de segundo orden produjo Nivel 3 (weak) honesto, no Nivel 4 (strong). El aparato funciona porque rechaza honestamente cuando debe rechazar. La tesis se demuestra precisamente por su capacidad de decir no a sus propios autores.

**Limitaciones honestamente reconocidas:** p-value declarado mal calibrado al 24% empírico (umbrales EDI sí robustos); caso 30 con circularidad detectada por sonda alternativa; depuración post-hoc del corpus inter-escala documentada; datos sintéticos del corpus inter-escala derivados de parámetros publicados (elevación a LoE 4-5 con datos reales abiertos como deuda priorizada de 6-12 meses post-defensa); AUC-ROC de discriminación interno (0.886) no validación externa contra estándar de oro; ningún caso cumple los tres criterios κ-ontológica simultáneamente (todas las afirmaciones son κ-pragmática hasta convergencia inter-grupo); revisión por pares humanos hostiles como deuda externa bloqueante para sustentación.

**Palabras clave:** estructuras pre-ontológicas, irrealismo operativo, ontología general multiescalar, realismo estructural moderado (uso operativo no-Ladyman/Ross — ver glosario operativo), pluralismo epistemológico, anti-reificación, emergencia operativa, naturalismo metafísico moderado, B-series relacional, manipulabilidad woodwardiana, constitución descendente, complementarismo metodológico declarado (engagement fenomenológico acotado, no operativo en el cuerpo), ABM, ODE, EDI, cierre operativo κ-pragmática vs κ-ontológica, asimetría L1-B-L3-S, dossier de anclaje, validación computacional, suite ST, hostile testing, complejidad multiescalar, corpus inter-dominio + inter-escala, behavioral dynamics, Wolfram Physics Project.

---

## Abstract (English)

This dissertation defends an **operative irrealism of pre-ontological structures**: a philosophical articulating position combining moderate structural realism, epistemic pluralism, and operative anti-reification **as general ontology, epistemology, and methodology applicable at any physical, biological, or cosmological scale where the apparatus can operate with physically motivated probes**. The entities, levels, and categories through which we think any domain of reality are operative patterns identifiable as empirical attractors of coupled dynamical systems, admissible only under a fourteen-component anchoring dossier, protocolar asymmetry between description registers L1↔B↔L3↔S, and EDI (Effective Dependence Index) validation computed via ablative intervention.

The term **"pre-ontological"** is understood in a genetic-epistemological sense (Simondon): the structure is pre-individual and prior to nominalizing categorial cuts, not temporally prior. The dissertation adopts **moderate metaphysical naturalism** as an explicitly declared starting commitment, **relational B-series** for time, **Woodwardian manipulability** for causation operationalized via ablative intervention, **downward constitution** (Craver) instead of Kim-vulnerable downward causation, and **methodological complementarism** between third-person methods (EDI apparatus) and first-person phenomenological methods (Husserl, Merleau-Ponty, Thompson).

The core methodological contribution is a hybrid computational instrument **ABM + ODE** that measures operational closure using EDI = 1 − RMSE_coupled / RMSE_no_ode, with permutation testing (999), bootstrap (500), and robust validation protocol (C1-C5 plus 8 additional criteria for *overall_pass*). The apparatus operates on five formal operators (μ measurement, G graph, H hypergraph, κ compression, ε expansion) with dated parametric question Q and explicit tolerance. **The apparatus is scale-invariant**: it operates with the same methodology from subatomic spin-orbit dynamics (10⁻¹⁰ m, 10⁻¹⁵ s) to gravitational dynamics of globular clusters (10²⁰ m, 10¹⁴ s).

A total of **40 aggregate cases were evaluated across two complementary corpora**: (a) the **inter-domain corpus** with 30 cases across physical, biological, socioeconomic, technocultural, and behavioral domains (4 strong with `overall_pass`, 1 strong without gate, 8 weak, 2 suggestive, 4 trend, 8 null, 3 correctly rejected falsification controls); (b) the **inter-scale corpus** with 10 cases across 8 distinct scales, covering **30 orders of magnitude** spatially and temporally, with **7 strong cases in 7 distinct scales** (atomic, quantum, biochemical, oscillatory cellular, individual, astrophysical, massive astrophysical), 1 weak, and 2 honest nulls. The apparatus survives severe hostile testing (0/1500 false positives of the full gate under massive random walk testing, 0/12 circularity detected in cross-probe testing of inter-scale probes). Formal logical validation via ST suite of 13 theories, two critical findings detected and corrected.

**The 40 cases are operational justification of the tripartite general framework (ontological + epistemological + methodological); they are not the thesis.** The thesis consists of the three general frameworks; the corpus shows that the general claims are executable, discriminating, and transferable. Generality does not depend on corpus size.

The dissertation publicly discriminates against fourteen identifiable rival positions, including Wolfram Physics Project, on at least two criteria each. Wolfram Rule 110 pilot executed showing coexistence of computational micro-irreducibility and detectable macro operational closure (EDI=0.55 across two independent probes). The novelty is not in the inventory but in the articulation: the combination anchoring dossier + L1↔B↔L3↔S asymmetry + inter-domain + inter-scale cartography with rejected falsification constitutes an auditable and falsifiable research program.

The main outcome is not a binary validation score but a **discriminative map of operational closure** across the emergence continuum, transversal to scales and domains. The framework demonstrates empirical selectivity, traceability, and instrumental falsifiability: it neither validates everything nor rejects everything, and it separates robust operational constraint from partial signal or no detectable signal. Final inferential strength is interpreted jointly with validation-window size, level of evidence (LoE), and instrument-phenomenon dependence.

**Key epistemic lesson:** case 30 (behavioral dynamics) was rejected by the apparatus in its initial version (EDI=0.002, not significant) despite the research team's expectation of acceptance. The improved second-order probe yielded honest Level 3 (weak), not Level 4 (strong). The apparatus works because it honestly rejects when it should reject. The thesis demonstrates itself precisely by its capacity to say no to its own authors.

**Honestly acknowledged limitations:** declared p-value miscalibrated at 24% empirical (EDI thresholds remain robust); case 30 with circularity detected by alternative probe; post-hoc tuning of inter-scale corpus documented; inter-scale corpus data are synthetic derived from published parameters (elevation to LoE 4-5 with open real data as priority debt of 6-12 months post-defense); discrimination AUC-ROC (0.886) is internal, not external validation against gold standard; no case meets the three κ-ontological criteria simultaneously (all claims remain κ-pragmatic until inter-group convergence); peer review by hostile human reviewers as blocking external debt for public defense.

**Keywords:** pre-ontological structures, operative irrealism, general multiscale ontology, moderate structural realism, epistemic pluralism, anti-reification, operational emergence, moderate metaphysical naturalism, relational B-series, Woodwardian manipulability, downward constitution, phenomenological methodological complementarism, ABM, ODE, EDI, operational closure κ-pragmatic vs κ-ontological, L1-B-L3-S asymmetry, anchoring dossier, computational validation, ST suite, hostile testing, multiscale complexity, inter-domain + inter-scale corpus, behavioral dynamics, Wolfram Physics Project.

---

## Información bibliográfica

**Autor principal (concepto y dirección):** Jacob Agudelo, Universidad de Antioquia.
**Colaborador (técnica e ingeniería computacional):** Steven Vallejo Ortiz.
**Co-autoría IA:** Anthropic Claude (Opus 4.7) declarada como instrumento de implementación bajo dirección humana.
**Filiación institucional:** Universidad de Antioquia, Medellín, Colombia.
**Campo:** Filosofía de la Ciencia y Ciencias de la Complejidad.
**Versión:** 2026-04-28.

---

## Citation suggestion

> Agudelo, J., y Vallejo Ortiz, S. (2026). *Estructuras Pre-Ontológicas: Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio* [Manuscrito doctoral]. Universidad de Antioquia.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="listas-de-figuras-tablas-y-abreviaturas"></div>

# Listas de figuras, tablas y abreviaturas

## Función

Listas de soporte editorial requeridas por el formato de tesis doctoral institucional de la Universidad de Antioquia. Tres listas independientes: figuras, tablas, abreviaturas. Cada elemento referencia su capítulo de origen.

---

## A.9.1. Lista de figuras

> Nota: las versiones Mermaid renderizables de las 9 figuras principales están consolidadas en `10-apendices-tecnicos/03-figuras-mermaid.md`. En el cuerpo de los capítulos los diagramas siguen en ASCII art para legibilidad en texto plano. La conversión final a SVG/PNG con `mmdc` (mermaid-cli) o equivalente es trámite editorial pre-depósito con cronograma específico: 3-5 días en la semana previa al depósito institucional. Esta lista anticipa la numeración estable.

**Tabla A.9.1.**

| Figura | Título | Capítulo |
|--------|--------|----------|
| Fig. 2.1 | Cuatro modos de realidad operativa | 02-01 |
| Fig. 2.2 | Acoplamiento dinámico organismo-entorno-tarea-historia | 02-04 |
| Fig. 3.1 | Mapa de operadores formales (μ, G, H, κ, ε) | 03-01 |
| Fig. 3.2 | Diagrama del dossier de anclaje (14 componentes) | 03-02 |
| Fig. 3.3 | Pipeline de validación EDI con permutación + bootstrap + C1-C5 | 03-04 |
| Fig. 4.1 | Tabla discriminante con 14 rivales (resumen) | 04-01 |
| Fig. 5.1 | Asimetría L1↔B↔L3↔S como protocolo | 02-04 / 05-05 |
| Fig. 5.2 | Trayectoria de heading bajo behavioral_attractor (caso 30) | 05-05 / 09-30 |
| Fig. 6.1 | Paisaje de emergencia del corpus EDI (distribución por nivel) | 06-01 |
| Fig. 9.1 | Arquitectura del motor ABM+ODE acoplado | 09-00 |

---

## A.9.2. Lista de tablas

**Tabla A.9.2.**

| Tabla | Título | Capítulo |
|-------|--------|----------|
| Tabla 0.1 | Hitos institucionales declarados | 00-04 |
| Tabla 1.1 | Falencias diagnósticas del prototipo previo | 01-01 |
| Tabla 1.2 | Mapa de inserción de la tesis en cinco subcampos | 01-03 |
| Tabla 3.1 | Cinco operadores formales del aparato mínimo | 03-01 |
| Tabla 3.2 | Componentes del dossier de anclaje (14) | 03-02 |
| Tabla 3.3 | Protocolo C1-C5 + 8 condiciones para `overall_pass = True` | 03-04 |
| Tabla 4.1 | 14 rivales y discriminación específica | 04-01 |
| Tabla 5.1 | Casos del corpus por dominio de aplicación | 05-00 |
| Tabla 5.2 | Comparativa cualitativa-cuantitativa para behavioral dynamics | 05-05 |
| Tabla 6.1 | Cuadro síntesis del paisaje de emergencia | 06-01 |
| Tabla A.4.1 | Tabla comparativa con 14 rivales | Parte IV |
| Tabla A.5.1 | Mapa de aplicaciones del marco | A.5 |
| Tabla A.8.1 | Resultados del corpus EDI (30 casos) | A.8 |
| Tabla A.8.2 | Métricas de robustez por caso | A.8 |
| Tabla A.8.3 | Verificación bajo perfil agresivo | A.8 |
| Tabla A.8.4 | Distribución del paisaje de emergencia | A.8 |

---

## A.9.3. Lista de abreviaturas y símbolos

### Operadores formales

**Tabla A.9.3.**

| Símbolo | Significado | Capítulo |
|---------|-------------|----------|
| μ | Operador de medición; recorta R en X observable | 03-01 |
| G | Grafo basal de dependencias entre variables | 03-01 |
| H | Hipergrafo de relaciones n-arias | 03-01 |
| κ | Operador de compresión multiescala | 03-01 / 03-04 |
| ε | Operador de errores de traducción | 03-01 |
| φ, ψ | Heading actual y heading de meta (caso 30) | 05-05 / 09-30 |
| τ | Razón tamaño-óptico / tasa-de-cambio (Lee 1976) | 02-04 |
| β | Error de heading φ − ψ_g | 02-04 |

### Métricas y protocolos

**Tabla A.9.4.**

| Sigla | Significado | Capítulo |
|-------|-------------|----------|
| EDI | Effective Dependence Index | 03-04 |
| RMSE | Root Mean Squared Error | 03-04 |
| C1-C5 | Convergencia, Robustez, Determinismo, Consistencia, Uncertainty | 03-04 |
| ABM | Agent-Based Model | 09-00 |
| ODE | Ordinary Differential Equation | 09-00 |
| LoE | Level of Evidence (1-5) | 03-02 |
| CI | Confidence Interval | 03-04 |
| CR | Cohesion Ratio (Symploké) | 03-04 |

### Niveles del corpus

**Tabla A.9.5.**

| Nivel | Categoría | Definición operativa |
|------:|-----------|----------------------|
| 0 | Null | EDI ≤ 0 o sin estructura macro |
| 1 | Trend | 0 < EDI sin significancia (p ≥ 0.05) |
| 2 | Suggestive | 0.01 ≤ EDI < 0.10, p < 0.05 |
| 3 | Weak | 0.10 ≤ EDI < 0.30, p < 0.05 |
| 4 | Strong | EDI ≥ 0.30, p < 0.01, `overall_pass = True` |
| 5 | Crítico (programa futuro) | Convergencia bajo múltiples sondas + datos LoE = 5 + frontera espacial nítida |

**Nota explícita sobre el Nivel 5:** el manuscrito demuestra hasta Nivel 4. El Nivel 5 está definido como **horizonte programático** del marco, no como nivel alcanzado en el corpus actual. Sus condiciones (multi-sonda convergente, LoE = 5, topología heterogénea con frontera nítida) son objetivos del programa de elevación documentado en `Bitacora/2026-04-28-cierre-doctoral/`.

### Niveles del registro categorial

**Tabla A.9.6.**

| Sigla | Registro | Capítulo |
|-------|----------|----------|
| L1 | Psicológico-ordinario (preguntas comunicables) | 02-04 |
| B | Conductual-biológico (anclaje empírico) | 02-04 |
| L3 | Estructural-relacional (formalización) | 02-04 |
| S | Semántica revisada (categorías que sobreviven) | 02-04 |

### Instituciones y datasets

**Tabla A.9.7.**

| Sigla | Significado |
|-------|-------------|
| CEI | Comité de Ética en Investigación (Universidad de Antioquia) |
| SIIU | Sistema de Información para la Investigación Universitaria |
| OPSD | Open Power System Data |
| OWID | Our World in Data |
| TLE | Two-Line Element (CelesTrak) |

---

## Trazabilidad

Estas listas se actualizarán automáticamente desde el manuscrito ensamblado (`TesisFinal/Tesis.md`) cuando se haga la conversión final a LaTeX/PDF mediante Pandoc + script de extracción. Hasta entonces, se mantienen manualmente coherentes con los capítulos de origen.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="glosario-operativo"></div>

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


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---


<div id="introduccion"></div>

# Introducción


<div id="introduccion"></div>

# Introducción

## Pregunta central

> ¿Bajo qué condiciones es legítimo reemplazar una categoría heredada por una construcción formal estructural-relacional sin caer en sustitución nominal y sin desligarse del nivel donde el fenómeno vive empíricamente?

Esta pregunta concentra el problema fundamental del proyecto. El lenguaje heredado tiende a reificar: hablamos de mente, memoria, mercado, institución, servicio, organismo o identidad como si fueran cosas simples cuando a menudo condensan organizaciones complejas. El reduccionismo plano no resuelve el problema, solo lo desplaza al nivel inferior. El emergentismo fuerte multiplica sustancias. El constructivismo arbitrario entrega cualquier recorte. El formalismo vacío produce elegancia sin captura. La tesis intenta ocupar un punto distinto.

## Tesis principal

> Todo fenómeno empíricamente explicable, a cualquier escala física, biológica o cosmológica, está anclado en un sustrato material dinámico. Las entidades, niveles y categorías con que lo pensamos son **estructuras pre-ontológicas**: regularidades operativas anteriores a la objetualidad, identificables como atractores empíricamente robustos de sistemas dinámicos acoplados, admisibles solo bajo dossier de anclaje completo, protocolo C1-C5 satisfecho y EDI medido por intervención ablativa.

## Tres marcos generales simultáneos

La tesis ofrece tres marcos generales coordinados:

1. **Ontología general:** una sola estructura ontológica (sustrato material dinámico + acoplamiento + atractor empírico + cierre operativo κ) que se instancia a cualquier escala.
2. **Epistemología general:** una sola teoría del conocimiento como compresión disciplinada bajo intervención ablativa, operativa al mismo modo desde lo cuántico hasta lo cosmológico.
3. **Metodología general:** un solo aparato (motor ABM+ODE acoplado + protocolo C1-C5 + EDI + dossier de 14 componentes + suite ST) que ejecuta esa epistemología sobre esa ontología sin reentrenar arquitectura entre dominios o escalas.

Los 40 casos del corpus son **justificación operativa** de los tres marcos, no son la tesis. La generalidad de los marcos no depende del tamaño del corpus.

## Posición filosófica: irrealismo operativo

Realismo estructural moderado + pluralismo epistemológico + anti-reificación operativa. Nunca afirmamos `X es Y`; afirmamos `bajo el instrumento I, X exhibe cierre operativo de grado G respecto a la pregunta Q`. La dependencia instrumento-fenómeno no es defecto: es condición epistémica honesta.

## Hipótesis

### Hipótesis general

> Una ontología material-relacional articulada con epistemología formal de compresión multiescala bajo asimetría L1↔B↔L3↔S y dossier de anclaje permite explicar mejor fenómenos complejos que las alternativas que reifican categorías ordinarias o reducen la explicación a descripción plana de componentes locales.

### Hipótesis específicas

- **H1 (ontológica):** la realidad está materialmente instanciada, pero sus unidades explicativas son patrones relacionales estabilizados, definidos como atractores empíricamente identificables de sistemas dinámicos acoplados (capítulo 02-01).
- **H2 (epistemológica):** el conocimiento es compresión disciplinada de estructura material-relacional bajo restricciones empíricas, con verdad como preservación estructural verificable (capítulo 02-02).
- **H3 (nivel B):** el nivel de anclaje empírico es el sistema dinámico acoplado organismo–entorno bajo restricciones de tarea, físicas, informacionales e históricas (capítulo 02-04).
- **H4 (metodológica):** las operaciones de compresión κ y expansión ε permiten justificar el paso entre escalas sin inflación ontológica ni empobrecimiento explicativo (capítulos 03-01 y 03-04).
- **H5 (comparativa):** la tesis ofrece ventaja discriminante respecto a catorce posiciones rivales identificables (capítulo 04-01).
- **H6 (demostrativa):** en behavioral dynamics, el aparato produce predicciones cuantitativas verificadas y discrimina contra modelos internos (capítulo 05-05 y corpus EDI caso 30).
- **H7 (programática):** el aparato es extensible a mente, biología, sistemas técnicos e instituciones bajo criterios explícitos de elevación (capítulos 05-01 a 05-04).

## Régimen de validez declarado

La tesis se sostiene como **propuesta ontológica multiescalar** validada operativamente sobre 40 casos del corpus EDI agregado (30 inter-dominio + 10 inter-escala). La asimetría entre demostración parcial y generalidad del marco no se disimula: se nombra como estructura del programa de investigación.

### Limitaciones honestas reconocidas

- p-value declarado mal calibrado (tasa empírica de tipo I = 24%, no 5%); los umbrales EDI sí son robustos;
- caso 30 (behavioral dynamics) sufre circularidad detectada por sonda alternativa;
- composición de los corpus es post-hoc, no pre-registrada;
- datos del corpus inter-escala son sintéticos derivados de parámetros publicados;
- todas las auditorías son endógenas; revisión por pares humanos hostiles es deuda externa.

## Aporte original

El proyecto combina cinco movimientos en una sola arquitectura que ningún rival reúne:

1. **monismo ontológico** sin reduccionismo plano;
2. **realismo estructural moderado** con anclaje empírico explícito;
3. **pluralismo explicativo controlado** con asimetría L1↔B↔L3↔S como protocolo;
4. **formalización metodológica** con procedimiento empírico de κ vía EDI;
5. **cartografía multidominio + multiescala** con 40 casos, discriminación contra rivales identificables y hostile testing aplicado.

La novedad no es de inventario (cada pieza está distribuida entre marcos vecinos). Es de articulación: dossier de anclaje + asimetría como filtro de admisión simultáneo, validado operativamente.

## Estructura del manuscrito

El manuscrito se organiza en cinco partes:

- **Parte I (Fundamentos):** ontología material-relacional, epistemología de la compresión, categorías, anclaje empírico, temporalidad y causalidad, dimensión normativa.
- **Parte II (Aparato y método):** operadores formales, criterios de legitimidad, auditoría ontológica, operacionalización de κ, ética de investigación.
- **Parte III (Evidencia empírica):** caso ancla canónico, corpus inter-dominio (30 casos), corpus inter-escala (10 casos), aplicaciones programáticas.
- **Parte IV (Discusión):** debates con catorce posiciones rivales, limitaciones y puntos de presión.
- **Parte V (Cierre):** conclusión demostrativa con condiciones de fracaso falsables, hoja de ruta post-defensa.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="estado-del-arte"></div>

# Estado del arte


## 1. Filosofía de la mente postcognitivista

### 1.1. Periodización

Tres oleadas:

- **Embodied cognition (1991–2005).** Programa que rechaza el cognitivismo simbólico y rehabilita cuerpo, acción y entorno como variables constitutivas del proceso cognitivo. Texto fundacional: Varela, Thompson y Rosch (1991), *The Embodied Mind*.
- **Extended mind y enactivismo (1998–2015).** Clark y Chalmers (1998) formalizan el principio de paridad ("if a process counts as cognitive when done in the head, it should also count as cognitive when done in the world", p. 8). Noë (2004) y Thompson (2007) consolidan el enactivismo. Hutto y Myin (2013) plantean el enactivismo radical (REC) eliminando representaciones contentful en niveles básicos.
- **Ecological dynamics (2003–presente).** Recupera y formaliza Gibson (1979/1986). Warren (2006) consolida el programa de **dinámica perceptiva-motora** con la conjetura clave: *"the laws of behavior are descriptions of regular dynamical relations between organism and environment"* (p. 359). Fajen y Warren (2003) ofrecen la formalización dinámica de segundo orden de la locomoción dirigida.

### 1.2. Controversias activas

- ¿es la representación necesaria a algún nivel cognitivo? Debate entre Clark (2008, *Supersizing the Mind*) y Hutto-Myin (2013, *Radicalizing Enactivism*).
- ¿basta la dinámica acoplada para explicar fenómenos cognitivos de alto nivel (lenguaje, planificación)? Open question post-Thompson 2007.
- ¿se puede integrar con neurociencia computacional sin recaer en cognitivismo? Programa de active inference (Friston 2010) y predictive processing (Clark 2013) intenta esa síntesis.

### 1.3. Hueco que la tesis ocupa

La filosofía postcognitivista está rica en formulaciones cualitativas pero pobre en discriminación cuantitativa contra el cognitivismo simbólico **caso por caso**. El aparato EDI, aplicado al caso 30 (behavioral dynamics) y al capítulo 05-05 (caso ancla canónico), ofrece **discriminación cuantitativa pública**: si la sonda dinámica acoplada produce EDI significativo, el cierre operativo es real bajo intervención. Esto es contribución metodológica, no solo conceptual.

## 2. Ontología analítica y ontología social

### 2.1. Líneas principales

- **Ontología analítica de propiedades, particulares, eventos.** Quine (1948), Lewis (1986), Armstrong (1997). Discusión de qué cosas existen y bajo qué criterios.
- **Realismo estructural.** Worrall (1989), Ladyman y Ross (2007, *Every Thing Must Go*). Ontic structural realism: las estructuras son ontológicamente fundamentales, no los objetos. Cita clave: *"there are no things; structure is all there is"* (Ladyman y Ross 2007, §3.4).
- **Sistemismo de Bunge.** Bunge (1977, 1979, 2003). Toda entidad es sistema concreto con composición, entorno, estructura, mecanismo. Cita: *"a system is a complex object every part or component of which is connected with other parts of the same object in such a manner that the whole possesses some properties that none of its parts possesses"* (Bunge 1979, *Treatise on Basic Philosophy*, vol. 4, p. 4).
- **Ontología social.** Searle (1995, 2010) sobre intencionalidad colectiva y reglas constitutivas; Gilbert (1989) sobre plural subjects; Bourdieu (1980) sobre habitus, campo, prácticas; Latour (2005, *Reassembling the Social*) sobre actor-network theory.
- **Anti-realismo ontológico.** Chalmers (2009, "Ontological Anti-Realism", en Chalmers, Manley y Wasserman, eds., *Metametaphysics*). Tesis del pluralismo de cuantificadores y deflación de las disputas existenciales.

### 2.2. Controversias activas

- ¿estructuras sin objetos es coherente, o requiere un soporte material? Debate post-Ladyman-Ross con French (2014) y críticos como Esfeld y Lam (2008).
- ¿es la intencionalidad colectiva primitiva (Searle) o reducible a coordinación material (Bourdieu, Latour)?
- ¿qué hace que un patrón sea ontológicamente real frente a uno meramente pragmático? Debate clásico desde Quine.

### 2.3. Hueco que la tesis ocupa

La tesis articula una **vía media operativa**: realismo estructural moderado + materialidad de los soportes + criterio empírico de admisión vía cierre operativo. Frente al estructuralismo óntico de Ladyman-Ross, conserva la materialidad de los soportes (no flota como pura estructura). Frente a la ontología social de Searle, la tesis mide validez normativa como cuenca de atracción del sistema, no como hecho institucional sui generis (capítulo 05-04). Frente a Bunge, retiene el sistemismo pero exige criterio empírico de cierre vía intervención ablativa cuantitativa, no solo definición conceptual de sistema.

## 3. Filosofía de la complejidad y emergencia computacional

### 3.1. Líneas principales

- **Causal emergence (CE).** Hoel, Albantakis y Tononi (2013, "Quantifying causal emergence shows that macro can beat micro", *PNAS*); Hoel (2017, "When the Map Is Better Than the Territory", *Entropy*). Definición operacional: el macro tiene poder causal mayor que el micro si maximiza la información efectiva sobre la dinámica.
- **Information theory of integrated information.** Tononi (2008, 2017); Oizumi, Albantakis y Tononi (2014). Marco IIT para conciencia y emergencia.
- **Synergistic information.** Rosas et al. (2020), Mediano et al. (2022). Descomposición de información mutua en redundancia, sinergia, transferencia.
- **Computational irreducibility.** Wolfram (2002, *A New Kind of Science*; Wolfram Physics Project, 2020–presente). Tesis: muchos procesos no admiten compresión computacional, su evolución debe simularse paso a paso.
- **Self-organization y dissipative structures.** Prigogine, Haken (synergetics), Kelso (coordination dynamics).
- **Symploké y nudos relacionales.** Bueno (1972); literatura del materialismo filosófico español. Marco filosófico hispanohablante de articulación material entre niveles.

### 3.2. Controversias activas

- ¿es la emergencia causal "real" o un artefacto de coarse-graining? Crítica de Dewhurst (2021) y Bedau (2008).
- ¿IIT mide algo físicamente realizado o es una métrica computacional aplicable a cualquier sistema? Debate Aaronson vs. Tononi.
- ¿la tesis de irreducibilidad computacional de Wolfram tiene contenido empírico falsable o es metateórica?
- ¿cómo distinguir emergencia genuina de patrones epifenoménicos correlacionales?

### 3.3. Hueco que la tesis ocupa

La tesis añade un eslabón faltante: **filtro empírico, dossier reproducible, asimetría protocolar y cartografía multidominio**. Hoel et al. ofrecen métrica conceptualmente potente pero su aplicación empírica multidominio es escasa. Wolfram ofrece simulación por irreducibilidad pero **sin discriminar entre estructuras genuinamente operativas y artefactos de simulación**. La tesis cierra la brecha vía EDI calculado por intervención ablativa con permutación 999 + bootstrap 500 + criterios C1-C5. La discusión específica con Wolfram está en el capítulo 04-01 (sección dedicada).

## 4. Behavioral dynamics y dinámica de sistemas no lineales

### 4.1. Líneas principales

- **Coordination dynamics.** Kelso (1995, *Dynamic Patterns*); Haken (1977/2004, synergetics). Lenguaje de bifurcaciones y atractores aplicado a coordinación motora.
- **Ecological psychology y affordances.** Gibson (1979); Stoffregen (2003); Chemero (2009, *Radical Embodied Cognitive Science*).
- **Behavioral dynamics (Warren-Fajen).** Warren (2006); Fajen y Warren (2003); Warren (1998); Fajen, Warren, Temizer y Bogasch (2003). Sistema acoplado organismo-entorno-tarea con ecuaciones publicadas.
- **Optic flow control.** Lee (1976) (ecuación tau-dot); Gibson (1958).
- **Motor control as control theory.** Todorov (2004); Jordan y Wolpert (1999). Control óptimo como metáfora del comportamiento.

### 4.2. Controversias activas

- ¿el aparato dinámico necesita representaciones internas para escalar a tareas complejas?
- ¿basta optic flow para guiar locomoción o se requiere mapa cognitivo allocéntrico?
- ¿qué relación hay entre dinámica conductual y predictive coding bayesiano?

### 4.3. Hueco que la tesis ocupa

Warren (2006) ofrece la conjetura cualitativa con r²=0.980 entre datos experimentales y modelo dinámico. Pero la discusión filosófica sobre si esto basta para una tesis ontológica acoplada queda abierta. La tesis adopta el caso Warren como caso ancla canónico (capítulo 05-05) y lo eleva a versión cuantitativa-EDI (caso 30 del corpus). La complementariedad cualitativa-cuantitativa cubre dos escalas temporales del mismo fenómeno.

## 5. Filosofía de la ciencia latinoamericana

### 5.1. Líneas principales

- **Mario Bunge.** Argentino-canadiense, sistemismo, materialismo emergentista científico. *Treatise on Basic Philosophy* (1974–1989, 8 vols.); *Buscar la filosofía en las ciencias sociales* (1995); *Crisis y reconstrucción de la filosofía* (2002). Es interlocutor sustantivo de la tesis: el sistemismo es esquema afín, pero la tesis exige criterio empírico operativo más estricto.
- **Guillermo Hoyos Vásquez** (Colombia, 1935–2013). Filosofía hermenéutica, ciencia y comunidad. Relevante para la dimensión normativa.
- **Jaime Salas Echeverri** (Universidad de Antioquia). Filosofía analítica latinoamericana.
- **Fernando Salmerón** (México), **Carlos Ulises Moulines** (México-Alemania, estructuralismo de teorías). Aporte a metateoría científica.
- **Eduardo Rabossi** (Argentina), **Carlos Pereda** (Argentina-México). Filosofía analítica.

### 5.2. Hueco que la tesis ocupa

La filosofía latinoamericana de la ciencia tiene tradición sistemista fuerte (Bunge) y hermenéutica (Hoyos) pero pocos puentes operativos hacia ciencias de la complejidad cuantitativa. La tesis es contribución desde la línea de la Universidad de Antioquia: combina compromiso ontológico realista moderado con aparato cuantitativo verificable, tendiendo puente entre tradición filosófica institucional y ciencia computacional contemporánea.

## 6. Mapa de inserción de la tesis en el campo

**Tabla 1.3.1.**

| Subcampo | Posición consolidada | Posición de la tesis | Discriminación específica |
|----------|----------------------|----------------------|---------------------------|
| Mente postcognitivista | Acoplamiento organismo-entorno como tesis general | Cuantificación EDI del cierre operativo en behavioral dynamics | Caso 30 cuantitativo + caso 05-05 cualitativo |
| Ontología analítica | Realismo estructural óntico (Ladyman-Ross) o sistemismo (Bunge) | Realismo estructural moderado + materialidad + EDI | Filtro empírico operativo no presente en rivales |
| Complejidad computacional | Emergencia causal (Hoel) o irreducibilidad (Wolfram) | Cierre operativo κ vía EDI multidominio | Dossier reproducible + falsación rechazada |
| Behavioral dynamics | Acoplamiento dinámico cualitativo (Warren 2006) | Versión cuantitativa Nivel 3 weak (caso 30) | Discriminación pública contra cognitivismo |
| Filosofía latinoamericana | Sistemismo (Bunge) o hermenéutica (Hoyos) | Puente operativo entre sistemismo y validación cuantitativa | Aparato EDI multidominio |

## 7. Contribución específica

A partir del mapa anterior, la contribución específica de la tesis al estado del arte se resume en cinco puntos:

1. **Marco ontológico unificado** — irrealismo operativo de estructuras pre-ontológicas como vía media entre realismo metafísico y anti-realismo, con materialidad de soportes y filtro empírico de admisión.
2. **Aparato formal mínimo** — cinco operadores (μ, G, H, κ, ε) suficientes para auditar entidades sin sobrecarga metafísica (capítulo 03-01).
3. **Métrica empírica EDI** — cierre operativo κ operacionalizado vía intervención ablativa con permutación + bootstrap + protocolo C1-C5 + 8 condiciones adicionales para `overall_pass=True`.
4. **Corpus EDI multidominio** — 30 casos heterogéneos cubriendo física, biología, economía, política, tecnología, cultura, conducta humana; 5 strong, 7 weak, 2 suggestive, 4 trend, 8 null, 3 controles de falsación rechazados.
5. **Discriminación pública contra rivales identificables** — capítulo 04-01 confronta 14 posiciones rivales con celdas comparativas explícitas y predicciones discriminantes.

Cada punto es contribución verificable, no afirmación retórica.

## 8. Limitación de esta revisión

Esta revisión es **orientada a la tesis**, no exhaustiva del campo en general. No agota:

- la literatura francófona postestructuralista (Deleuze, Stiegler);
- la literatura analítica reciente sobre causalidad (Pearl, Woodward);
- la literatura especializada en cada uno de los 30 dominios del corpus (cada caso del corpus tiene su propia mini-revisión en su README específico).

La revisión exhaustiva de cada uno de los 30 dominios queda como trabajo futuro. Para fines de la tesis general, basta con la inserción en los cinco subcampos anteriores y la discriminación contra los 14 rivales del capítulo 04-01.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---


<div id="parte-1-fundamentos"></div>

# Parte I — Fundamentos ontológicos y epistemológicos


<div id="capitulo-1-ontologia-material-relacional"></div>

# Ontología material-relacional



## 0. Pregunta filosófica fundamental

> **¿Qué hay que hay, y cómo lo conocemos sin reificarlo prematuramente?**

Esta es la pregunta filosófica que motiva la tesis. La pregunta tiene dos polos inseparables: el ontológico (*qué hay*) y el epistemológico (*cómo conocemos*), ligados por la advertencia metodológica (*sin reificar*). Reificar es, en este marco, otorgar estatus de sustancia o esencia a lo que es patrón material-relacional. La tesis se construye contra dos errores complementarios: (a) duplicar mobiliario ontológico inflando categorías sin anclaje material, y (b) reducir lo real a sus componentes mínimos sin reconocer la realidad de los patrones que los integran.

La tesis responde: **lo que hay son patrones materialmente sostenidos en un sustrato dinámico**, identificables como atractores empíricos de sistemas acoplados; lo conocemos comprimiendo dependencias decisivas bajo intervención ablativa; el filtro contra reificación es el dossier de admisión de catorce componentes. Esto no es la única respuesta posible (el dualismo, el idealismo, el panpsiquismo y el operacionalismo puro responden distinto); es la respuesta que la tesis defiende y que el corpus inter-dominio + inter-escala respalda operativamente.

## 0.1. Naturalismo metafísico moderado como compromiso de partida

La tesis adopta **naturalismo metafísico moderado** como **compromiso de partida explícitamente declarado**, no como conclusión demostrada. Esto significa:

1. el sustrato material dinámico se asume como punto de partida; **no se demuestra**, se compromete;
2. el compromiso se justifica por tres razones operativas: (a) **continuidad con la ciencia** (ninguna disciplina científica madura opera sin compromiso material implícito); (b) **parsimonia ontológica** (no se postulan sustancias separadas sin necesidad operativa); (c) **capacidad operativa del aparato** (el aparato EDI, el dossier, la suite ST funcionan bajo este compromiso);
3. el compromiso se valida operativamente **a posteriori**, por el éxito del marco articulado bajo este compromiso. Si el marco fallara estructuralmente, el compromiso de partida se replantearía.

**Reconocimiento honesto:** lo anterior NO es demostración del naturalismo metafísico. Es compromiso filosófico que se asume con conciencia de que tiene alternativas legítimas en la tradición:

**Tabla 2.1.1.**

| Alternativa rechazada | Por qué la tesis no la asume |
|---|---|
| **Dualismo cartesiano** | Postula segunda sustancia (*res cogitans*) sin ganancia operativa y con problema de interacción no resuelto |
| **Idealismo metafísico** (Berkeley, Hegel) | Inverte la prioridad: la materia se vuelve apariencia del espíritu/Idea; pierde anclaje empírico operativo |
| **Emanacionismo neoplatónico** | Postula Uno trascendente del cual emana la materia; entidad postulada sin acceso operativo |
| **Creacionismo metafísico** | Compromete con sujeto creador; compromiso teológico que rebasa la ontología filosófica |
| **Panpsiquismo** (Strawson, Chalmers) | Atribuye experiencia a partículas elementales; carece de filtro operativo de admisión y multiplica propiedades sin necesidad del aparato |
| **Pluralismo de planos sustanciales** | Multiplica niveles ontológicos como sustancias; viola parsimonia |

El compromiso por naturalismo no es **arbitrario**: es la elección que hace la tesis viable como programa de investigación articulado con disciplinas científicas existentes. La tesis declara esto abiertamente para evitar la objeción de petición de principio.

## 0.2. En qué sentido las estructuras son **pre-ontológicas**

El título de la tesis es *Estructuras Pre-Ontológicas*. El término "pre-ontológico" es técnico y exige aclaración filosófica. Distinguimos cinco sentidos posibles del prefijo "pre"; la tesis adopta una **combinación específica de dos** y rechaza los otros tres:

### 0.2.1. Sentidos rechazados

- **"Pre" temporal puro:** *"anterior en el tiempo cósmico a la constitución del objeto"*. La tesis NO usa este sentido. Las estructuras pre-ontológicas no son anteriores temporalmente; son **anteriores en orden de constitución** a la objetualidad nominal.
- **"Pre" trascendental kantiano puro:** *"condición de posibilidad pura de cualquier objeto"*. La tesis NO usa este sentido. Las estructuras pre-ontológicas son **materialmente realizadas**, no condiciones puras del entendimiento.
- **"Pre" fenomenológico puro:** *"dato dado antes del juicio constitutivo"*. La tesis NO usa este sentido. La tesis no asume primacía de la conciencia sobre el sustrato material.

### 0.2.2. Sentidos adoptados

- **"Pre" genético (Simondon):** las estructuras pre-ontológicas son **lo pre-individual**, lo metaestable que **genera** lo individual. Simondon (*L'individuation à la lumière des notions de forme et d'information*, tesis principal de 1958; ed. Millon 2005, Introducción y cap. 1) sostiene que lo individuado no preexiste al proceso de individuación; la categoría central es la **metaestabilidad** del régimen energético previo, que admite potencia plural y solo se resuelve en individuo bajo restricciones específicas del acoplamiento. La tesis traduce: el atractor empírico es **precipitación de lo pre-individual** (sustrato material dinámico bajo restricciones de acoplamiento) en patrón identificable. No es objeto sustancial; es patrón en proceso de individuación continua. La asistencia computacional no reproduce cita textual paginada porque la edición de referencia (Millon 2005 vs PUF 1964 vs Aubier 1989) varía y la verificación específica sobre la edición consultada en `07-bibliografia/` queda como tarea de Jacob (`TAREAS_PENDIENTES.md` H-J5).
- **"Pre" epistemológico-operacional:** las estructuras pre-ontológicas son **anteriores al recorte categorial**. Antes de que las nombremos como "esto es X", ya operan como atractores en el sistema acoplado. La nominalización categorial viene **después**: es compresión semántica del patrón ya operativo. En este sentido, "pre-ontológico" significa **anterior a la objetualidad nominalizada, no anterior a la realidad material**.

### 0.2.3. Síntesis: definición técnica de "pre-ontológico"

> **Una estructura es pre-ontológica si y solo si:** (a) es regularidad operativa **materialmente sostenida** en un sustrato dinámico (no es entidad mental ni nominal); (b) es **previa al recorte categorial** que la nombra (opera antes de ser objetualizada); (c) es **génesis de lo individuado** (precipita en patrón identificable cuando las restricciones del acoplamiento la concentran); y (d) es **operativamente identificable** como atractor empírico bajo el aparato EDI con cinco condiciones de admisión.

Las estructuras pre-ontológicas, en este sentido, **no son entidades fundacionales** (Wolfram lo postularía así); **no son objetos sustanciales** (la metafísica clásica lo postularía así); **no son construcciones nominales** (el constructivismo arbitrario lo postularía así). Son **patrones operativos en estado de individuación continua** que el aparato del manuscrito identifica con criterio público.

### 0.2.4. Por qué este término es preferible a sus alternativas

- *"Estructuras dinámicas"* es demasiado genérico (cualquier sistema dinámico tiene estructuras dinámicas);
- *"Estructuras operativas"* pierde el énfasis en la genealogía (el atractor no es sólo operativo: es operativo porque se constituye genéticamente);
- *"Patrones materialmente sostenidos"* es la noción técnica equivalente que se usa en cap 02-01 §2; *"estructura pre-ontológica"* es la noción ontológica que la nombra a nivel filosófico.

El término *pre-ontológico*, así definido, **es coherente con Simondon, compatible con Bunge sistemista, y articulable con realismo estructural moderado**. Es la categoría ontológica central de la tesis.

## 0.3. Diálogo con la tradición filosófica latinoamericana e institucional

Para tesis depositada en la Universidad de Antioquia, el diálogo con la tradición filosófica institucional es deuda académica reconocida.

**Bunge** (Argentina-Canadá) es el interlocutor principal del sistemismo (cap 02-01 §1.3, cap 03-02, cap 03-03 con citas textuales).

**Hoyos Vásquez** (1935-2013, vinculado en distintas etapas a la Universidad Nacional, la Pontificia Javeriana y la Universidad de Antioquia) representa la tradición hermenéutico-fenomenológica colombiana de matriz husserliana y habermasiana. La tesis dialoga con dos publicaciones puntuales que la bibliografía recoge: *Ética para ciudadanos* (1996, Bogotá: Siglo del Hombre) y *Comunicación y mundo de la vida* (2007, Bogotá: Pontificia Universidad Javeriana). Del primero la tesis retiene la insistencia en que el sentido de la acción no se agota en su descripción causal: requiere comprensión del horizonte intersubjetivo en que ocurre. La asimetría L1↔B↔L3↔S es, en este sentido, **traducción explícita del cuidado hermenéutico al lenguaje protocolar**: no reducimos comprensión a explicación; las articulamos con criterios públicos de admisión. Del segundo retiene la tesis habermasiana de que la pretensión de validez no es propiedad privada del enunciante sino contraste intersubjetivo; la tesis lo opera por dossier público de catorce componentes (cap 03-02). El engagement con Hoyos es **declarado parcial**: no se reproducen citas textuales con paginación porque la asistencia técnica no pudo verificar al cierre los pasajes específicos sobre sustrato dinámico que sostendrían un diálogo más fuerte; el cierre del diálogo queda como deuda declarada para la voz autoral de Jacob (`TAREAS_PENDIENTES.md` H-J5).

**Salas Echeverri** (Universidad de Antioquia, filosofía analítica) representa la tradición analítica institucional. La metodología del aparato formal (cap 03-01) responde al espíritu analítico de exigir criterios públicos de admisión.

## Tesis del capítulo

> Existe un solo plano ontológico básico — sustrato material dinámico — sobre el cual se constituyen patrones estabilizados (atractores empíricos de sistemas dinámicos acoplados) que cuentan como entidades reales en sentido moderado, **a través de escalas físicas, biológicas y cosmológicas**. Las propiedades son disposiciones relacionales del sistema; la identidad es continuidad organizada bajo transformación; los niveles son registros descriptivos del mismo plano, no mundos separados. La ontología no multiplica sustancias y, simultáneamente, no empobrece la organización: es austera en sustancia y rica en relación, condicionada en cada paso por traducibilidad al nivel conductual-biológico (B) y por validación empírica multiescalar.

### La tesis como ontología general invariante a la escala

La tesis del **irrealismo operativo de estructuras pre-ontológicas** afirma una sola estructura ontológica que se instancia a múltiples escalas. No es la suma de ontologías regionales (una para lo cuántico, otra para lo biológico, otra para lo social) ni es ontología macro extendida nominalmente a otras escalas. Es **una ontología cuyos invariantes estructurales no dependen de la escala**. Lo que sí depende de la escala son las **instancias** de esos invariantes (qué cuerpo, qué entorno, qué tarea, qué historia entran en cada caso).

Los invariantes ontológicos son cuatro:

1. **Sustrato material dinámico:** existe a cualquier escala (campos cuánticos, moléculas, células, organismos, estrellas, cúmulos). No hay escala donde la materialidad deje de ser materialidad.
2. **Acoplamiento dinámico:** a cualquier escala hay un sistema con dos polos en interacción (qubit↔baño térmico; enzima↔sustrato; organismo↔entorno; estrella↔espacio-tiempo galáctico) cuyo estado conjunto evoluciona bajo restricciones específicas de la escala.
3. **Atractor empírico:** a cualquier escala el sistema acoplado tiene regiones de convergencia bajo perturbación acotada (estado de equilibrio térmico del qubit; forma plegada de la proteína; ciclo límite del NF-κB; cuenca del campo institucional; relación período-luminosidad de la Cefeida; equilibrio gravitacional del cúmulo).
4. **Cierre operativo κ:** el atractor admite descripción comprimida con dependencias decisivas preservadas y detalle local removible cuando la pregunta lo permite. Esta operación es **la misma operación matemática** independientemente de la escala: ablación del acoplamiento + comparación de RMSE + permutación + bootstrap + protocolo C1-C5.

**Lo que cambia con la escala** son los nombres específicos: el "agente" en la escala atómica es una configuración de espín; en la celular es un cuerpo celular con su maquinaria; en la individual es un organismo; en la astrofísica es un cuerpo estelar. Pero la estructura ontológica que estos nombres instancian es **una sola**.

Esta invarianza no es postulado *a priori*: está respaldada por los corpus operativos complementarios que **no se distinguen ontológicamente entre sí**, solo metodológicamente:

- **Corpus inter-dominio (30 casos):** discriminación entre dominios heterogéneos —física, biología, economía, política, tecnología, cultura, conducta humana— operando en escalas variables según el dominio (cap 09 + apéndice técnico 1).
- **Corpus inter-escala (10 casos):** discriminación a través de **30 órdenes de magnitud espaciales** y temporales, desde dinámica de espín-órbita atómica (10⁻¹⁰ m, 10⁻¹⁵ s) hasta dinámica de cúmulos globulares (10²⁰ m, 10¹⁴ s), con **7 strong en 7 escalas distintas** + 1 weak + 2 nulls honestos (cap 05-06 + apéndice técnico 2).

Las **estructuras pre-ontológicas** son objeto operativo a cualquier escala donde el aparato puede operar con sondas físicamente motivadas. No son artefacto de ninguna escala particular. Esta es la afirmación ontológica más fuerte que el corpus actual sostiene, con la honestidad metodológica de reportar los nulls (Villin Headpiece bajo sonda equilibrio; locomoción τ-dot bajo observación con reinicios discretos) sin ajustarlos para forzar overall_pass.

La distinción "macro vs micro" en el manuscrito original era **artefacto de la primera iteración**, donde el corpus estaba sesgado a sistemas con datos públicos macro-poblacionales. La iteración posterior con corpus inter-escala demuestra que el aparato y la tesis son **ontológicamente generales**: el dominio macro-poblacional no es preferencial; es uno entre múltiples donde la tesis se demuestra. Cualquier referencia residual a "escala macro" en capítulos posteriores debe leerse como **una entre las escalas cubiertas**, no como límite de la tesis.

#### Tabla síntesis: invariantes ontológicos instanciados a través de escalas

**Tabla 2.1.2.**

| Invariante | Caso 31 (cuántico) | Caso 33 (molecular) | Caso 36 (celular) | Caso 04 (energético macro) | Caso 27 (riesgo bio macro) | Caso 30 (conductual) | Caso 39 (estelar) | Caso 40 (cosmológico) |
|------------|--------------------|---------------------|-------------------|----------------------------|----------------------------|---------------------|-------------------|----------------------|
| **Sustrato material** | qubit superconductor + baño térmico | proteína Villin + solvente | núcleo celular + citoplasma | red eléctrica + agentes económicos | población humana + patógenos | cuerpo + entorno físico | gas estelar + radiación | gas estelar + campo galáctico |
| **Acoplamiento dinámico** | T2(T_bath) | k_fold/k_unfold(T) | NF-κB↔IκBα bajo TNF | F↔R bajo precio energético | mortalidad↔presión biológica | φ↔ψ_g bajo τ | pulsación radial bajo gravedad | σ_v↔marea galáctica |
| **Atractor empírico** | estado coherente bajo pulso | basin del estado plegado | ciclo límite oscilatorio | mix energético de equilibrio | tasa de mortalidad estable | trayectoria a meta | relación P-L como atractor | equilibrio Plummer |
| **Cierre operativo κ** | EDI 0.91 (Lindblad) | EDI 0.00 (sonda equilibrio inadecuada) | EDI 0.59 (Hoffmann) | EDI 0.65 (Lotka-Volterra) | EDI 0.33 (mortalidad) | EDI 0.26 (Fajen-Warren) | EDI 0.92 (P-L) | EDI 0.43 (Plummer+marea) |

Cada columna representa una **instancia particular** de los mismos cuatro invariantes ontológicos. Leer la tabla horizontalmente es leer la **unidad ontológica** de la tesis; leer cada columna verticalmente es leer la **especificación de escala** que cada caso requiere. Ambas lecturas son simultáneas y no opcionales.

#### Por qué esta estructura es ontológica, no metodológica

Un escéptico podría decir: *"el aparato funciona a múltiples escalas porque es estadístico genérico; eso no demuestra ontología, sólo capacidad descriptiva"*. La respuesta de la tesis tiene tres partes:

1. **Si el aparato fuera estadístico genérico, sus controles de falsación NO se rechazarían** (random walk, no-estacionariedad, observabilidad). Pero los 3 controles del corpus inter-dominio se rechazan correctamente, y los 1500 random walks bajo hostile testing producen 0 falsos positivos del gate completo. Esto significa que el aparato **discrimina entre dinámica con cierre operativo y dinámica sin él**, no solo describe trayectorias.
2. **Si la coincidencia ontológica entre escalas fuera artefacto del aparato, las sondas de una escala detectarían cierre sobre datos de otra escala.** El test cruzado V4-01 lo refuta: las sondas multiescala son específicas (0/12 circularidad sobre datos no-suyos). Cada sonda sólo detecta el atractor que su escala instancia.
3. **La estructura ontológica común NO es nominal.** Los cuatro invariantes (sustrato, acoplamiento, atractor, cierre operativo) son **operativamente medibles** en cada caso del corpus. La tabla síntesis no es resumen retórico; es lectura directa de los `metrics.json` de cada caso.

Esta es la diferencia entre **ontología general** y **descripción multidominio**: la primera afirma que hay una estructura común; la segunda solo cataloga. La tesis afirma la primera, con respaldo operativo de los 40 casos del corpus agregado.

### Nota sobre el sistema modal asumido

Cuando este capítulo y los posteriores invocan **necesidad** o **contingencia** (e.g., "la materialidad es necesaria", "el cierre operativo es contingente"), la lógica modal asumida es **al menos T (KT)**: el axioma de reflexividad `□P → P` está disponible. Esto significa que lo declarado como necesario implica que ocurre en el mundo de evaluación, evitando una lectura puramente esquemática de la necesidad. Sistemas más ricos (S4, S5) son admisibles para la lectura epistémica del capítulo de epistemología. La validación lógica formal con ST (Parte II) verificó que en `modal.k` básico la necesidad no implica efectividad, lo cual sería incoherente con la posición material-relacional.

### Nota sobre el grado de compromiso ontológico de κ

La compresión κ admite **dos lecturas** que conviene distinguir explícitamente:

- **κ-pragmática:** la compresión es legítima si el sistema reducido predice trayectorias dentro de tolerancia, preserva topología y discrimina intervenciones. Esta lectura es la que el cap 03-04 operacionaliza vía EDI, prueba de permutación, bootstrap y protocolo C1-C5. Es **interna** al modelo.
- **κ-ontológica:** la compresión corresponde a una estructura material independiente del modelo — no solo es útil, es real en el sentido de que existiría aunque nadie la modelara.

**El manuscrito demuestra κ-pragmática con rigor cuantificado** (corpus EDI multidominio, AUC-ROC de discriminación = 0.886 según auditoría severa N3). **La afirmación κ-ontológica fuerte requiere argumento adicional** que el corpus por sí solo no provee: se requeriría convergencia bajo múltiples sondas con motivaciones teóricas independientes (programa multi-sonda extendido, en `Bitacora/2026-04-28-cierre-doctoral/03-`) más correspondencia con resultados experimentales obtenidos por otros grupos con métodos distintos (deuda externa).

La posición filosófica del **irrealismo operativo** se sitúa **explícitamente entre las dos lecturas**: ni operacionalismo puro (κ-pragmática sola) ni realismo metafísico fuerte (κ-ontológica sin filtro empírico). El compromiso es:

- las estructuras pre-ontológicas son **reales en sentido moderado**: existen como atractores dinámicos materialmente sostenidos;
- pero su descripción cuantitativa específica (parámetros, sondas, niveles) es **dependiente del aparato**;

### Criterios operativos para distinguir κ-pragmática de κ-ontológica

Para que la afirmación κ-ontológica fuerte se sostenga sobre un caso particular, deben cumplirse **tres criterios simultáneos** (ninguno por sí solo basta):

1. **Convergencia bajo sondas independientes con motivación teórica distinta:** EDI ≥ umbral del nivel reclamado bajo al menos dos sondas que no comparten estructura paramétrica (e.g., ODE de orden distinto, formulación termodinámica vs ecológica, etc.). Sin esto, lo detectado puede ser auto-consistencia paramétrica, no estructura material independiente.
2. **Replicación inter-grupo:** otro grupo de investigación, sin acceso al código del autor, debe reproducir el mismo nivel de cierre operativo con datos comparables. Sin esto, la inferencia es endógena al laboratorio.
3. **Intervención experimental confirmatoria:** una predicción discriminante sobre intervención manipulada (no observación pasiva) debe cumplirse. Sin esto, la estructura puede ser correlación elaborada.

**Estado del corpus actual respecto a κ-ontológica:**

**Tabla 2.1.3.**

| Caso del corpus | C1 multi-sonda independiente | C2 replicación inter-grupo | C3 intervención confirmatoria |
|-----------------|:---:|:---:|:---:|
| 4 strong macro (04, 16, 20, 27) | parcial (multi-sonda interno solo) | NO | NO |
| 7 strong inter-escala (31-40) | NO (depuración post-hoc) | NO | NO |
| Caso 30 behavioral | NO (circularidad detectada) | NO | NO |

**Implicación operacional:** **ningún caso** del corpus actual cumple los tres criterios simultáneos. Por tanto, **todas las afirmaciones del corpus son κ-pragmática**, no κ-ontológica. La afirmación ontológica fuerte (las estructuras pre-ontológicas existen independientemente del aparato) es **conjetura ontológica articulada**, no demostración cerrada. Solo cuando los tres criterios se cumplan en al menos un caso del corpus la tesis pasará de κ-pragmática multiescalar a κ-ontológica multiescalar.

Esta es una **distinción honesta**: el manuscrito declara con precisión qué demuestra (κ-pragmática) y qué postula como conjetura plausible (κ-ontológica), sin colapsar las dos. La corrección de los umbrales y la elección de la sonda son siempre revisables; lo que NO es revisable (en su régimen declarado) es el sustrato material del cual la estructura es atractor. El capítulo de limitaciones (Parte IV) reconoce este punto como límite del marco, no como debilidad oculta.

## 1. Lo que existe

### 1.1. Sustrato material dinámico

El sustrato es el dominio efectivo de procesos, cuerpos, campos, energía, infraestructuras técnicas, organismos, prácticas materialmente sostenidas, soportes inscritos y trayectorias históricas. No es lista de partículas. No es metáfora. Es aquello que opera con independencia de cómo lo nombremos. Cuatro rasgos lo caracterizan:

- **instanciación**: todo lo empíricamente explicable está realizado en alguna configuración material;
- **dinamismo**: la materialidad es proceso, no inventario;
- **multiescalaridad**: hay escalas, ritmos, umbrales y formas de estabilización;
- **heterogeneidad organizada**: lo material incluye cuerpos, artefactos, signos inscritos, energía, prácticas, no como mezcla sino como diversidad articulada.

Esa caracterización no es estipulativa: cada rasgo se cumple en el caso ancla canónico (locomoción, frenado, equilibrio, raqueteo) y se cumple en cada dominio programático del capítulo 05.

### 1.2. Restricciones y dependencias reales

El sustrato existe organizado por restricciones que no son sustancia separada pero tampoco son lingüísticas. Acoplamientos mecánicos, condiciones de posibilidad, dependencias causales, retroalimentaciones, constituciones funcionales, dependencias históricas y contextuales. Estas restricciones son el modo en que el sustrato se estabiliza en patrones reconocibles. Su identificación es empírica: se detectan por intervención y por covarianza condicional, no por intuición.

### 1.3. Diálogo con interlocutores principales

**Bunge.** En *Treatise on Basic Philosophy* vol. 3 (1977, *Ontology I: The Furniture of the World*, p. 27), Bunge enuncia el principio que la tesis recoge: *"to be is to be a system or a component of one"*. El sustrato dinámico de la tesis encarna esta consigna sin reducirla a inventario: cada componente es a su vez sistema con composición, entorno, estructura y mecanismo (Bunge 1979, vol. 4, p. 4-5). La diferencia operativa con Bunge es el filtro empírico: Bunge define qué cuenta como sistema; la tesis añade el procedimiento (dossier de 14 componentes + EDI) para admitir sistemas concretos en cada caso de estudio.

**Ladyman y Ross.** En *Every Thing Must Go* (2007, §2.4, p. 130), sostienen que *"the ontic structural realist holds that all there is, at the most fundamental level, is structure"*. La tesis discrepa: la estructura sin sustrato dinámico es **estructura flotante**, criticable como inflación ontológica de signo opuesto al instrumentalismo. La materialidad es **necesaria** (en el sistema modal T declarado más arriba) para que la estructura sea operativamente real, no solo abstractamente posible.

**Dennett.** En *The Intentional Stance* (1987, cap. 2, p. 27), Dennett introduce los *"real patterns"* como criterio: *"a pattern exists in some data—is real—if there is a description of the data that is more efficient than the bit map, whether or not anyone can concoct it"*. La definición de patrón estabilizado de §2.2 retoma este criterio (compresión predictiva) pero le añade dos condiciones que Dennett deja implícitas: (a) materialmente sostenido, (b) discriminante bajo intervención. Sin estas dos, el patrón es mera regularidad estadística. La tesis se apropia de Dennett con disciplina, no como cita decorativa.

## 2. Patrón estabilizado: definición técnica

### 2.1. Por qué hace falta una definición técnica

`Patrón` carga el peso ontológico central de la tesis. Si queda como sinónimo de regularidad, la tesis pierde tracción. La definición técnica no impone matemática gratuita: sigue la práctica que el caso ancla ya implementa.

### 2.2. Definición

> Un patrón estabilizado es un atractor empíricamente identificable de un sistema dinámico acoplado, con cuenca de atracción medible y comportamiento bajo bifurcación caracterizable.

#### 2.2.1. Cinco condiciones de admisión operativas

Cinco condiciones de admisión hacen operativa la definición:

1. **Variables componentes** observables o inferidas con régimen de medición especificado;
2. **Estabilidad asintótica**: las trayectorias del sistema convergen al patrón bajo perturbación acotada;
3. **Cuenca de atracción**: rango de condiciones iniciales que conducen al patrón, identificado experimentalmente;
4. **Comportamiento bajo bifurcación**: cómo el patrón aparece, se desestabiliza o se transforma cuando varían parámetros del sistema;
5. **Discriminación inferencial**: el patrón produce predicciones o intervenciones que un rival explícito no produce o produce peor.

Una regularidad que no satisface las cinco condiciones no es patrón en el sentido del marco. Puede ser correlación, regularidad estadística o intuición de regularidad — pero no patrón ontológico.

#### 2.2.2. Cuatro métricas topológicas de rigor formal

Las cinco condiciones operativas son condiciones de admisión cualitativa. Para satisfacer la exigencia de **rigor topológico estándar** que un revisor formal puede plantear (auditoría doctoral F4), la tesis añade cuatro métricas cuantitativas calculadas sobre las trayectorias observadas:

1. **Exponente de Lyapunov máximo (λ_max)** vía algoritmo de Rosenstein, Collins y De Luca (1993, *Physica D* 65: 117-134). Mide la tasa de divergencia local de trayectorias inicialmente cercanas. λ_max > 0 indica sensibilidad a condiciones iniciales (caos determinista compatible con atractor extraño); λ_max ≈ 0 indica régimen marginal o cuasi-periódico; λ_max < 0 indica convergencia a punto fijo o ciclo límite.
2. **Dimensión de correlación (D₂)** vía algoritmo de Grassberger y Procaccia (1983, *Physica D* 9: 189-208). Cuantifica la complejidad del atractor en el espacio de fase reconstruido. Valor no entero es firma de atractor fractal o extraño; valor próximo a 0 corresponde a atractor de punto fijo.
3. **Embedding de Takens** (Takens 1981) con dimensión `dim=5` y retardo τ obtenido por primer cero de la autocorrelación. Reconstruye el espacio de fase a partir de la serie escalar observada cuando el sistema completo no es directamente medible.
4. **Tiempo de mezcla**: número de pasos hasta que la autocorrelación cae por debajo de 1/e, indicando independencia estadística aproximada entre puntos separados temporalmente.

La implementación canónica está en `09-simulaciones-edi/common/topology.py` con tests sobre 7 casos del corpus que tienen `primary_arrays.json` disponible (apéndice técnico §"Análisis topológico", reporte completo en `09-simulaciones-edi/topology/topology_report.{json,md}`):

**Tabla 2.1.6.**

| Caso | λ_max | D₂ | r² (D₂) | Lectura cualitativa |
|---|---:|---:|---:|---|
| 04 energía | −0.001 | 1.38 | 0.996 | atractor convergente baja dimensión |
| 16 deforestación | −0.022 | 1.65 | 0.988 | atractor convergente baja dimensión |
| 20 Kessler | +0.006 | 1.61 | 0.999 | régimen marginal compatible con atractor |
| 24 microplásticos | +0.007 | 1.65 | 1.000 | régimen marginal compatible con atractor |
| 27 riesgo biológico | −0.026 | 1.43 | 0.999 | atractor convergente baja dimensión |
| 41 Wolfram extendido | +0.017 | 2.82 | 0.989 | firma fractal compatible con atractor extraño |
| 42 histéresis institucional | −0.052 | 0.05 | 0.767 | atractor de punto fijo |

#### 2.2.3. Articulación entre las dos baterías

La relación entre las cinco condiciones operativas y las cuatro métricas topológicas es **necesaria pero no suficiente en cada dirección**:

- Una serie con λ_max > 0 y D₂ no entera **admite** tratamiento topológico estándar como atractor, pero el dossier de anclaje (cap 03-02) exige además identificación material y especificación dinámica que las métricas topológicas por sí solas no proveen.
- Una serie que satisface las cinco condiciones operativas no garantiza por sí sola firma topológica fuerte, especialmente cuando n es pequeño o el ruido domina sobre la dinámica determinista.

La tesis sostiene que el atractor empírico es **operativamente reconocido** cuando se cumplen las cinco condiciones cualitativas y **topológicamente caracterizado** cuando además se reportan las cuatro métricas cuantitativas. Esta articulación cierra F4 al precio honesto de declarar que las estimaciones con n ≤ 200 puntos son indicativas, no concluyentes (limitación ya documentada en el módulo `topology.py`).

La extensión de las métricas topológicas a los 33 casos restantes del corpus está pendiente (tarea **B-T1** en `TAREAS_PENDIENTES.md`) y depende de la activación de `array_dump=True` en el motor EDI para emitir `primary_arrays.json` por caso.

### 2.3. Consecuencias

- entidades como célula, organismo, servicio, institución se admiten como patrones si y solo si pasan las cinco condiciones para alguna pregunta `Q`;
- categorías como `mente`, `memoria`, `mercado`, `Estado` se admiten como compresiones legítimas si pueden traducirse a patrones que pasan las cinco condiciones;
- el realismo es estructural moderado: el atractor existe en el sustrato dinámico, pero su descripción depende del recorte de tarea y del régimen de medición.

## 3. Tipos de realidad

La realidad no es plana. La tesis distingue cinco modos de realidad sin multiplicar mundos:

**Tabla 2.1.4.**

| Modo | Definición | Ejemplo paradigmático |
|---|---|---|
| Fuerte | Procesos materiales con estabilidad e independencia de interés inmediato | cuerpos, campos, configuraciones físicas |
| Estructural | Patrones de relaciones que organizan fenómenos | redes de regulación, arquitecturas de software, atractores de sistemas acoplados |
| Funcional | Unidades definidas por su papel dentro de una organización | órganos, módulos, roles |
| Institucional | Entidades sostenidas por prácticas, normas, soportes y reconocimiento | dinero, contrato, universidad, Estado |
| Teórica | Entidades inferidas o modelizadas cuya legitimidad depende de captura de regularidades reales | clase estructural, variable latente, nodo comprimido |

Estas distinciones no proliferan sustancias: distinguen modos de estabilización y de legitimación dentro del mismo sustrato. La tesis se compromete con la realidad fuerte y estructural; admite la funcional, institucional y teórica si y solo si se traducen a patrones estabilizados con dossier de anclaje.

## 4. Entidad, proceso, sistema

La tesis rompe la falsa alternativa entre `cosa` y `flujo`:

- **objeto**: continuidad y delimitación robustas suficientes para tratar la unidad como compacta (piedra, herramienta, molécula);
- **proceso**: identidad sostenida por dinámica más que por permanencia material (tormenta, llama, organismo en su metabolismo);
- **sistema**: inteligibilidad dependiente de múltiples componentes y relaciones coordinadas (ecosistema, servicio distribuido, par agente–entorno).

No se elige una sola forma para todo. Se justifica la forma adecuada para cada fenómeno y cada pregunta. La justificación es operativa: la forma admisible es aquella que permite identificar el patrón estabilizado correspondiente sin redundancia.

## 5. Propiedades como disposiciones relacionales

Una propiedad no es etiqueta pegada a una cosa. Es una disposición que se manifiesta bajo condiciones de interacción específicas. Tres consecuencias:

- la fragilidad es relación entre estructura y fuerzas posibles, no contenido oculto;
- la inteligencia es patrón de adaptación, inferencia y aprendizaje bajo condiciones, no sustancia interna;
- la salud es organización funcional bajo rangos de operación y entorno, no esencia del organismo.

La definición técnica: una propiedad es una disposición relacional materialmente anclada que altera las trayectorias del sistema acoplado bajo intervenciones específicas. Esto preserva el monismo material — la disposición está realizada — sin reducirla a etiqueta local.

## 6. Identidad como continuidad organizada

La identidad no es esencia inmóvil. Es continuidad de organización bajo transformación. Operativamente:

> Una entidad conserva identidad cuando mantiene un patrón estabilizado a través de transformaciones tolerables para su tipo, donde la tolerancia se especifica como cuenca de atracción persistente bajo el régimen de transformación considerado.

Esto explica por qué un organismo sigue siendo el mismo a pesar del recambio molecular (cuenca persistente bajo recambio), por qué un servicio mantiene identidad a través de despliegues (cuenca persistente bajo redespliegue), por qué una institución persiste con miembros rotativos (cuenca persistente bajo rotación). En cada caso la tolerancia es operacionalizable.

## 7. Fronteras y límites

Las fronteras no son siempre absolutas. Son reales cuando corresponden a discontinuidades materiales, restricciones funcionales, cambios de régimen dinámico o cortes relevantes para una pregunta. La tesis admite tres tipos de frontera:

- **frontera dura**: discontinuidad material (membrana, superficie de objeto, contrato firmado);
- **frontera funcional**: cambio de régimen dinámico (transición fásica, cambio de atractor);
- **frontera pragmática**: corte justificado por la pregunta, sin discontinuidad material única.

Una frontera del tercer tipo no es arbitraria si su trazado mejora la legibilidad del patrón sin destruir dependencias relevantes. La verificación es la misma de siempre: predicción e intervención discriminantes.

## 8. Niveles sin multiplicación de mundos

No hay un mundo físico, otro biológico, otro mental, otro social, otro simbólico. Hay un mismo plano material con escalas y ritmos de organización. Un nivel es un registro descriptivo del mismo plano, no una capa ontológica adicional. Esta tesis es **monismo de planos, pluralismo de registros**:

- la célula no viola la física, pero la biología celular no se vuelve trivial al conocer las partículas;
- una red informática no existe sin hardware, pero no se administra describiéndola como electrones;
- una institución no flota sobre individuos, pero no se explica como suma de individuos aislados;
- la conducta no existe sin organismo y entorno, pero no se entiende reduciéndola a microeventos locales.

Cada `nivel` es un recorte cuya legitimidad pasa por el filtro del capítulo 03-02 (criterios). No hay nivel correcto en absoluto; hay nivel adecuado a la pregunta `Q` con tolerancia explícita.

## 9. Causalidad, restricción y organización

La tesis no reduce toda explicación a causalidad lineal. Reconoce un repertorio operativo de relaciones:

- **causalidad directa**: A produce cambio en B;
- **condición de posibilidad**: A permite que B ocurra;
- **restricción**: A limita el rango de estados posibles de B;
- **acoplamiento dinámico**: A y B co-varían bajo dinámica conjunta;
- **constitución**: A forma parte de la estructura que hace que B sea lo que es;
- **retroalimentación**: A afecta B y B afecta A;
- **dependencia histórica**: el estado actual depende de trayectorias pasadas;
- **dependencia contextual**: la relación cambia según entorno o escala.

La causalidad circular (upward + downward) emerge naturalmente del acoplamiento dinámico: las componentes producen la dinámica conjunta y la dinámica conjunta retroalimenta a las componentes. No hay aquí emergencia fuerte: hay self-organization en el sentido técnico anclado en Maturana y Varela (1980, *Autopoiesis and Cognition*) y Haken (1977, *Synergetics*) — ver cap 02-04 §4 para la formulación con cita textual paginada.

## 10. Qué evita la ontología

**Tabla 2.1.5.**

| Tentación rechazada | Razón |
|---|---|
| Dualismo | Multiplica sustancias sin necesidad y sin compromiso operacional |
| Materialismo de partículas | La lista de componentes no agota la organización |
| Emergentismo fuerte | Convierte la self-organization en sustancia nueva |
| Constructivismo arbitrario | Trata todos los recortes como equivalentes |
| Reificación del modelo | Confunde el formalismo con el sustrato |
| Realismo ingenuo de categorías | Asume que las palabras ya recortan correctamente |

Cada rechazo es selectivo, no total: el dualismo aporta la intuición de que algunos fenómenos no se entienden con descripción microfísica; el materialismo aporta el anclaje material; el emergentismo aporta la atención a la organización; el constructivismo aporta la advertencia sobre la mediación lingüística; el realismo ingenuo aporta el funcionamiento práctico de muchas categorías. La tesis recoge la intuición y rechaza la inflación o el empobrecimiento.

## 11. Diálogo con interlocutores

### 11.1. Bunge — sistemismo y materialismo realista

Bunge ofrece dos lecciones aprovechables: la exigencia de anclaje material en toda explicación legítima y el sistemismo como alternativa al individualismo y al holismo. La tesis recoge ambas y agrega: el sistemismo necesita el filtro de admisión de patrones (cinco condiciones) para no resbalar hacia totalidades sin variables. Donde Bunge habla de sistemas con entornos, la tesis habla de pares dinámicos acoplados con tarea e historia.

### 11.2. Dennett — real patterns

Dennett sostiene que los patrones son reales si capturan compresión informacional con pérdida controlada. La tesis recoge la intuición pero exige más: un patrón es real cuando es atractor empíricamente identificable con cuenca y bifurcación, no solo regularidad comprimida. La diferencia es operativa: la regularidad comprimida puede ser correlación; el atractor es estructura dinámica.

### 11.3. Sellars — imagen manifiesta vs imagen científica

Sellars distingue la imagen manifiesta (categorías ordinarias) de la científica (categorías teóricas). La tesis rechaza tratarlas como dos sustancias separadas y propone su articulación operativa: L1 es la imagen manifiesta como registro de relevancia; B y L3 reconstruyen la imagen científica con anclaje empírico; S es la categoría que sobrevive a la auditoría y puede coexistir con L1 sin sustituirlo nominalmente.

### 11.4. Wittgenstein — gramática y reificación

Wittgenstein advierte que la gramática arrastra metafísica. La tesis convierte la advertencia en protocolo: cada categoría heredada pasa por auditoría con cinco condiciones de admisión. La sospecha gramatical no se queda en crítica; produce un test público.

### 11.5. Simondon — individuación

Simondon ofrece la individuación como génesis: los individuos no preexisten al proceso. La tesis recoge la idea, pero la opera: la individuación es la formación de un atractor a partir de un sistema metaestable, identificable empíricamente como bifurcación que pasa de monoestable a multiestable. La metáfora de Simondon se vuelve modelo dinámico.

## 12. Fórmula ontológica de cierre

> Existe un solo plano material dinámico. Sus estabilizaciones son atractores empíricamente identificables de sistemas acoplados. Las entidades, propiedades, identidades y niveles son modos de describir esas estabilizaciones bajo régimen de medición y pregunta explícita. La ontología no multiplica sustancias y no empobrece la organización: opera bajo el doble criterio de austeridad de sustancia y riqueza de relación, con admisión condicionada por traducibilidad al nivel B y por validación empírica.

## 13. La cuestión del observador en escala cuántica

La generalidad multiescalar de la tesis llega hasta la escala cuántica (caso 31 decoherencia, caso 32 espín-órbita). En escala cuántica, la cuestión del observador es problema ontológico fundamental desde Copenhagen: ¿la medición colapsa el estado, o el estado siempre fue determinado, o todas las ramas se realizan?

### 13.1. Postura: realismo estructural compatible con interpretaciones realistas

La tesis adopta postura **explícita** sobre la mecánica cuántica: rechaza la **interpretación Copenhagen instrumentalista pura** (estado cuántico solo describe conocimiento del observador) y declara compatibilidad con **interpretaciones realistas**:

- **Many-worlds** (Everett 1957, DeWitt 1970): todas las ramas se realizan; el observador es subsistema dentro de la rama;
- **Bohmiana** (de Broglie-Bohm): hay variables ocultas reales (posiciones de partículas) que evolucionan deterministamente;
- **GRW / colapso objetivo** (Ghirardi-Rimini-Weber 1986): el colapso es proceso físico real, no efecto del observador;
- **Decoherencia ambiental** (Zurek 2003): la medición efectiva emerge del acoplamiento al ambiente, no del observador consciente.

La tesis NO decide entre estas interpretaciones realistas — esa decisión rebasa el alcance del manuscrito. **Pero sí rechaza Copenhagen instrumentalista pura** porque:

1. Copenhagen instrumentalista hace al observador consciente parte del aparato físico, lo cual viola el monismo material de la tesis;
2. la tesis afirma que la materialidad es real independientemente del observador (cap 02-01 §0.1 naturalismo);
3. el caso 31 (decoherencia) opera dentro de **decoherencia ambiental**, que es la interpretación realista más conservadora compatible con experimentos actuales.

### 13.2. Implicación

La afirmación "estructuras pre-ontológicas a escala cuántica" tiene sentido **bajo interpretación realista** de la mecánica cuántica. Bajo Copenhagen pura, las "estructuras" serían artefacto del acto de medición, lo cual sería incompatible con la tesis. Por eso la tesis se compromete con la familia realista, sin decidir entre sus miembros.

## 14. Evolución conceptual

La formulación intuitiva de partida evolucionó hacia la versión canónica. Los claims principales que sobreviven íntegramente son: monismo material-dinámico, estructuras pre-ontológicas como atractores, compresión disciplinada como epistemología, asimetría L1↔B↔L3↔S, emergencia como self-organization, dossier de admisión, y la fórmula "X exhibe cierre operativo bajo I respecto a Q". Los claims refinados incluyen: caso 30 con circularidad reconocida, corpus post-hoc, AUC-ROC interno, κ-pragmática vs κ-ontológica distinguidas, sistema modal T explícito. La continuidad conceptual es fuerte; la honestidad metodológica es mayor en la versión actual.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-2-epistemologia-de-la-compresion"></div>

# Epistemología general de la compresión multiescala


## Tesis del capítulo

> El conocimiento es compresión disciplinada de estructura material-relacional bajo restricciones empíricas, **a cualquier escala**. Una compresión es legítima cuando preserva las dependencias relevantes para una pregunta `Q` con tolerancia explícita y produce predicción o intervención discriminante respecto a alternativas. La verdad de un modelo no es identidad con la realidad sino preservación estructural verificable. **Esta epistemología es general**: opera del mismo modo cuando el conocedor reduce un sistema cuántico a Lindblad, una proteína a MSM 2-estados, una célula a Tyson-Novak, un mercado a Lotka-Volterra, una persona a Mackey-Glass, una estrella a pulsación P-L, o un cúmulo a Plummer. La diferencia entre estos casos es la sonda específica; la **operación epistémica de compresión es la misma**.

## 1. Tres planos analíticamente disjuntos

Mucho error filosófico nace de confundir lo que existe con lo que modelamos o con cómo lo nombramos. La tesis distingue:

**Tabla 2.2.1.**

| Plano | Qué entra | Qué no entra |
|---|---|---|
| **Realidad** | Sustrato material dinámico; restricciones; patrones estabilizados | Cualquier modelo; cualquier nombre |
| **Modelo** | Representación formal o semiformal de variables y dependencias | El sustrato mismo; el nombre que se le pone |
| **Categoría** | Compresión semántica con función comunicativa | El modelo formal; el sustrato |

Errores típicos:

- confundir categoría con realidad → reificación;
- confundir modelo con realidad → formalismo ingenuo;
- confundir realidad con dato bruto → empirismo plano;
- confundir categoría con modelo → sustitución nominal.

El capítulo 02-03 desarrolla la consecuencia para categorías, objetos, propiedades e identidad. Aquí basta con fijar la disyunción.

## 2. Por qué conocer no es copiar

Dos razones rechazan la imagen ingenua:

### 2.1. Un duplicado total sería inútil

Un modelo que retuviera toda la complejidad efectiva del fenómeno sin compresión alguna dejaría de ser operable. La complejidad sin recorte no es información: es ruido inventariado.

### 2.2. Toda observación selecciona

Toda medición implica criterios de relevancia, instrumentos, escalas, variables, supuestos y lenguaje de clasificación. La selección no es defecto epistémico: es condición de inteligibilidad. La pregunta no es si comprimimos sino cómo y con qué legitimidad.

## 3. Compresión

### 3.1. Definición

> Una compresión κ es una operación que reemplaza una subestructura compleja por una unidad operativa más tratable, cuando el detalle interno no produce diferencia inferencial relevante para la pregunta `Q`.

### 3.2. Cuándo es legítima

Cuatro condiciones, todas necesarias:

1. **pierde detalle irrelevante para `Q`**;
2. **conserva dependencias decisivas para `Q`**;
3. **mejora inferencia, predicción o intervención** respecto a la versión no comprimida;
4. **admite reapertura** mediante el operador inverso ε si la pregunta cambia o si aparecen anomalías.

Estas condiciones no son retóricas. Tienen procedimiento empírico fijado en el capítulo 03-04 (operacionalización de κ).

### 3.3. Ejemplos

- en el caso ancla canónico, la compresión de cientos de grados de libertad neuromusculares en una sola variable conductual (heading φ, error de heading β, aceleración de impacto, τ_bal) es legítima porque pasa las cuatro condiciones bajo las preguntas de Warren;
- en sistemas técnicos distribuidos, la compresión de procesos, redes, certificados, balanceadores en `el servicio` es legítima cuando la pregunta es disponibilidad global; deja de serlo cuando la pregunta es diagnóstico de caída;
- en biología, comprimir cientos de moléculas en `célula` es legítimo cuando la pregunta es tisular; deja de serlo cuando la pregunta es metabólica fina.

### 3.5. Lenguaje, significado y representación

Una epistemología de la compresión exige postura sobre **qué relación tienen las representaciones (sondas, modelos, categorías) con lo que representan**. La tesis articula:

#### 3.5.1. Inferencialismo brandomiano matizado

La tesis adopta **inferencialismo brandomiano matizado** como teoría del significado: el significado de un término es su **rol inferencial** dentro de prácticas materiales sostenidas. Brandom (1994, *Making it Explicit*, cap. 3, p. 89) lo articula: *"to grasp the meaning of an expression is to grasp its role in inference"*.

**Implicación para la tesis:**

- el significado de "atractor", "cierre operativo κ", "estructura pre-ontológica" se constituye por **rol inferencial dentro del aparato y del corpus**;
- no hay significado independiente del uso (Wittgenstein 1953, *Investigaciones filosóficas* §43, p. 18e: *"el significado de una palabra es su uso en el lenguaje"*);
- pero el uso está **materialmente sostenido** (Brandom + materialismo de la tesis): no es uso lingüístico flotante, es práctica con cuerpos, instrumentos, datos.

#### 3.5.2. Compresión sintáctica vs semántica

Distinción técnica importante:

- **compresión sintáctica:** preserva estructura formal (variables, ecuaciones, dependencias) sin atender al significado;
- **compresión semántica:** preserva además **rol inferencial** dentro de la práctica disciplinar.

La compresión κ del aparato EDI es **principalmente sintáctica** (preserva dependencias dinámicas verificables por intervención ablativa) pero **se vuelve semántica cuando la sonda se elige por su rol teórico en la disciplina** (Lotka-Volterra para Energía no es ecuación cualquiera; es estructura con significado disciplinar específico).

Esto resuelve la objeción "¿la compresión es semántica o solo sintáctica?": **es ambas, en niveles diferentes**. La operación matemática es sintáctica; la elección de la sonda y su interpretación es semántica.

#### 3.5.3. La sonda como representación

¿Qué es una sonda ODE en relación con el fenómeno que describe? La tesis adopta **realismo estructural representacional**:

- la sonda **NO es copia** del fenómeno (no es isomorfismo);
- la sonda **NO es ficción útil sin referencia** (no es ficcionalismo);
- la sonda es **homomorfismo parcial**: preserva las **dependencias decisivas** del fenómeno bajo la pregunta `Q` con tolerancia explícita.

Esto se alinea con **Sellars** (1956, *Empiricism and the Philosophy of Mind*, §41): la representación es **inferencial-funcional**, no pictórica. Y con Pearl: el modelo causal es **estructura mínima suficiente** para responder a intervenciones, no copia exhaustiva.

#### 3.5.4. Por qué la sustitución nominal es prohibida

Cap 02-04 §8.0 prohíbe la sustitución nominal (decir "X es Y" cuando solo se quiere decir "X exhibe cierre operativo bajo I respecto a Q"). El fundamento filosófico de la prohibición es ahora explícito: **la sustitución nominal viola el rol inferencial** del término. Decir "el yo es atractor cerebral" sin pasar por la traducción L1↔B↔L3↔S asume rol inferencial del aparato científico para el término "yo" sin haberlo justificado en práctica.

### 3.6. Diálogo con interlocutores principales

**Cartwright.** En *How the Laws of Physics Lie* (1983, cap. 2, p. 53), Cartwright sostiene que las leyes científicas son *"ceteris paribus laws"* que no describen la realidad bruta sino *"that things behave as if those laws were true"*. La compresión κ de la tesis incorpora esta intuición pero la operacionaliza: el "como si" de Cartwright se convierte en condición empírica medible (las cuatro condiciones de §3.2). Donde Cartwright deja la operacionalización en el éxito explicativo intuitivo, la tesis exige EDI con permutación 999 + bootstrap 500 + protocolo C1-C5 (cap 03-04).

**Pearl.** En *Causality* (2009, 2.ª ed., cap. 1, p. 1), Pearl distingue tres niveles de inferencia (asociación, intervención, contrafactual). La condición §3.2(3) (*"mejora inferencia, predicción o intervención respecto a la versión no comprimida"*) recoge explícitamente el segundo nivel pearliano: la compresión legítima debe sobrevivir el `do`-operador. La métrica EDI (ablación del acoplamiento ODE manteniendo el forcing) es operacionalización del nivel 2.

**Bechtel y Craver.** Bechtel (2008, *Mental Mechanisms*, cap. 1, p. 13) define el mecanismo como *"a structure performing a function in virtue of its component parts, component operations, and their organization"*. La compresión κ es el procedimiento epistémico que **identifica** ese mecanismo en datos: descompone, comprime, valida. Craver (2007, *Explaining the Brain*, cap. 4, p. 152) añade el criterio de **mutual manipulability** que la condición §3.2(4) (admite reapertura ε) recoge en forma de reversibilidad parcial.

## 4. Expansión

### 4.1. Definición

> Una expansión ε es una operación que abre una unidad comprimida para mostrar su estructura interna, cuando el detalle interno sí produce diferencia inferencial respecto a `Q`.

### 4.2. Cuándo es necesaria

Tres signos obligan a expandir:

1. la compresión actual impide distinguir casos relevantes para `Q`;
2. la estructura interna modifica predicciones o intervenciones;
3. el sistema se aproxima a una bifurcación donde el régimen interno cambia.

### 4.3. Por qué la expansión no es retroceso

Comprimir y expandir no son operaciones contrapuestas. Son complementarias y se rotan según la pregunta. La regla operativa:

> expandir cuando la estructura interna produce diferencias inferenciales relevantes; comprimir cuando el detalle interno no las produce.

## 5. La pregunta como parámetro

Toda compresión y toda expansión se evalúan respecto a una pregunta `Q` con tolerancia explícita. `Q` no es preferencia subjetiva: es restricción operativa. Tres consecuencias:

- la legitimidad de un recorte es **relativa a `Q`**, no absoluta;
- cambiar `Q` después de un fallo predictivo está **prohibido**: invalida el ciclo;
- la tolerancia debe **fijarse antes** del intento de modelización.

Esto cierra una de las objeciones más peligrosas — la irrefutabilidad por nivel — porque establece protocolo trazable de fijación y revisión de `Q`. Capítulo 04-02 desarrolla este punto.

## 6. Por qué esto no es constructivismo arbitrario

Toda categoría es construida; no toda construcción es equivalente. La realidad restringe qué compresiones son aceptables a través de:

- regularidades empíricas;
- estabilidad bajo perturbación;
- robustez bajo cambio de medición;
- capacidad predictiva;
- capacidad interventiva;
- coherencia con otros recortes ya admitidos.

Por eso la tesis defiende **realismo estructural moderado**: los recortes son construidos, pero algunos son mejores porque siguen mejor la estructura real. La diferencia con el constructivismo arbitrario es operacional: el constructivismo no se compromete con predicciones discriminantes; la tesis sí.

## 7. Por qué esto no es reduccionismo plano

La reducción plana identifica explicación adecuada con descripción de nivel inferior. La tesis lo niega por tres razones:

- una descripción micro puede ser verdadera y aun así no capturar organización relevante;
- muchas preguntas requieren módulos, escalas y dependencias distribuidas;
- el mejor modelo no es el de menor nivel, sino el que preserva la estructura relevante con el menor costo innecesario.

El nivel adecuado para una `Q` es el que minimiza simultáneamente dos cosas: pérdida de estructura relevante y costo computacional. Capítulo 03-02 formaliza el balance.

## 8. Economía explicativa

Una epistemología seria debe incluir el problema del costo. Más detalle no implica más conocimiento. A veces implica menos: ruido, inmanejabilidad, ceguera estructural. La cláusula:

> el nivel correcto es aquel que preserva mejor las diferencias relevantes para `Q` sin exigir una complejidad superior a la necesaria.

Esto conecta con la noción de baja dimensionalidad efectiva del capítulo 03-04: cuando el sistema vive realmente en pocas dimensiones, el modelo de baja dimensión no es simplificación cosmética; es captura estructural.

## 9. Errores epistémicos típicos

**Tabla 2.2.2.**

| Error | Forma | Antídoto |
|---|---|---|
| Compresión excesiva | Tratar como unidad algo cuya estructura interna sí cambia el fenómeno | Aplicar test de discriminación; reabrir con ε |
| Expansión excesiva | Abrir tanto detalle que la organización relevante se pierde | Limitarse al nivel donde la pregunta gana resolución |
| Reificación | Tratar una categoría útil como sustancia simple | Auditoría categorial (capítulo 02-03) |
| Formalismo vacío | Confundir elegancia con captura | Exigir traducibilidad B↔L3 |
| Sustitución nominal | Cambiar nombres sin cambiar predicciones | Exigir predicción discriminante |
| Inmunización por nivel | Cambiar `Q` después del fallo | Trazar `Q` con fecha; prohibir reciclaje |

## 10. Verdad como preservación estructural

La tesis no necesita una teoría de la verdad como copia integral. Le basta una idea más austera:

> un modelo es verdadero respecto a `Q` cuando preserva las dependencias reales del fenómeno necesarias para responder `Q` con la tolerancia exigida.

Esa verdad es:

- **parcial**: ningún modelo agota el mundo;
- **situada**: depende de `Q`;
- **controlada**: exige criterios de preservación verificables;
- **no relativista**: distintas representaciones fallan mejor o peor frente a restricciones reales.

El test de verdad es comparativo: un modelo es más verdadero que otro respecto a `Q` si preserva más dependencias relevantes con menor costo, predice mejor, interviene mejor, sobrevive a más perturbaciones del régimen de medición.

## 11. Conocer como auditoría

Desde esta epistemología, conocer no es solo describir: es auditar recortes. Ante cualquier categoría candidata se formulan seis preguntas:

1. ¿qué patrón comprime?
2. ¿qué dependencias conserva?
3. ¿qué pérdidas produce?
4. ¿qué evidencia la sostiene?
5. ¿cuándo debe abrirse?
6. ¿qué predicción discriminante propone?

Si una categoría no admite respuesta a las seis, no entra en el marco. La auditoría es el corazón metodológico del proyecto y se desarrolla operativamente en el capítulo 03-03.

## 12. Diálogo con interlocutores

### 12.1. Cartwright — capacidades y modelos parciales

Cartwright defiende un realismo de capacidades: las leyes científicas describen capacidades, no comportamientos invariantes. La tesis recoge la idea con un ajuste: capacidad es disposición relacional, y su realidad se verifica por comportamiento del sistema acoplado bajo intervención. La preservación estructural reemplaza la noción ingenua de ley universal.

### 12.2. Pearl — modelos causales

Pearl ofrece formalismo de inferencia causal con grafos dirigidos. La tesis lo absorbe en el aparato del capítulo 03-01 con dos restricciones: (a) los grafos representan dependencias del sistema acoplado, no causalidad lineal aislada; (b) las intervenciones (operador `do`) son la prueba de que la dependencia es real, no solo estadística.

### 12.3. Bechtel y Craver — explicación mecanicista multinivel

Bechtel y Craver formalizan la explicación mecanicista como descomposición funcional de niveles. La tesis recoge la asimetría entre niveles pero exige más: cada nivel debe pasar el filtro del dossier de anclaje. La descomposición no es libre; está restringida por traducibilidad B↔L3 y por predicción discriminante.

### 12.4. Mitchell — pluralismo integrativo

Mitchell defiende el pluralismo integrativo: distintos modelos coexisten como capturas parciales de un fenómeno complejo. La tesis recoge la pluralidad pero la disciplina: distintos modelos son legítimos si responden distintas `Q` con sus dossiers respectivos; no son legítimos si solo coexisten por inercia académica.

### 12.5. Dennett — real patterns

Dennett es el aliado más directo en la noción de patrón comprimido como real. La tesis incorpora pero diferencia: un patrón real no es solo compresión informacional; es atractor empírico con cuenca, bifurcación y discriminación. La diferencia se prueba en el caso ancla.

## 13. Consecuencia práctica

La epistemología convierte una intuición filosófica en regla de trabajo:

> comprender mejor no es sumar más nombres ni más detalles; es encontrar el nivel de descripción donde la estructura se vuelve inteligible sin dejar de ser fiel a lo real, validado por predicción y por intervención.

Esto es lo que opera el capítulo 03 (formalización) y lo que el capítulo 05-05 demuestra en el caso ancla.

## 14. Fórmula final

> Conocer es comprimir estructura real bajo restricciones empíricas, sin mutilar la diferencia que importa para la pregunta planteada y bajo compromiso público de predicción discriminante.

Si la ontología (capítulo 02-01) da el suelo, esta epistemología enseña a caminar sobre él sin confundir el mapa con el territorio ni el territorio con masa muda. Si el aparato formal (capítulo 03) da los instrumentos, esta epistemología fija para qué sirven.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-3-categorias-objetos-propiedades-identidad"></div>

# Categorías, objetos, propiedades e identidad


## Tesis del capítulo

> Categorías son compresiones semánticas con función comunicativa que deben pasar la auditoría del dossier de anclaje. Objetos son unidades operativas relativas con cuatro tipos de objetualidad. Propiedades son disposiciones relacionales materialmente ancladas. Identidad es continuidad organizada bajo transformación, operacionalizable como cuenca de atracción persistente. Los cuatro reformulados son el inventario suficiente para reconstruir el vocabulario filosófico y científico sin inflar la ontología ni empobrecer la explicación.

## 1. Categorías como compresiones semánticas

### 1.1. Definición operativa

> Una categoría es una operación de compresión semántica que agrupa diferencias y regularidades para volver tratable un fenómeno bajo una pregunta `Q`.

Las categorías cumplen una función indispensable: sin ellas no hay comunicación, comparación ni continuidad teórica. Pero su utilidad práctica no garantiza estatuto ontológico.

### 1.2. Filtro de admisión

Una categoría se admite si satisface, para alguna `Q` con tolerancia explícita:

- **anclaje**: traducible a variables medibles del nivel B (capítulo 02-04);
- **fidelidad**: preserva las dependencias decisivas para `Q`;
- **discriminación**: produce inferencia, predicción o intervención que un rival no produce;
- **reversibilidad**: admite reapertura con ε si la pregunta cambia;
- **economía**: reduce complejidad sin ocultar lo decisivo.

Una categoría que falla en cualquiera de las cinco se mantiene como rótulo práctico (con marca explícita de ser solo eso) o se descarta. No se admite como compresión legítima.

### 1.3. Casos paradigmáticos

- `mente`: admisible como compresión solo si se descompone en patrones de integración que pasan los criterios; ver capítulo 05-01;
- `memoria`: admisible si se descompone en familia de procesos de codificación, consolidación, reactivación, uso; ver 05-01;
- `mercado`: admisible si se descompone en agentes, plataformas, reglas, incentivos, infraestructura; ver 05-04;
- `servicio`: admisible si se descompone en procesos, red, persistencia, autenticación, despliegue; ver 05-03;
- `especie`: admisible si se descompone en patrón histórico-biológico de reproducción, descendencia, variación; ver 05-02.

Ninguna de estas categorías se elimina automáticamente. Cada una pasa por auditoría con dossier de anclaje. Las que sobreviven entran en `S` (semántica revisada) como compresiones legítimas.

## 2. Objetos como unidades operativas relativas

### 2.1. Definición operativa

> Un objeto es una unidad relativamente estable de organización material que puede ser individuada bajo criterios explícitos de continuidad, límite y función para alguna pregunta `Q`.

Esto rechaza el objeto como sustancia simple autosuficiente y rechaza también el objeto como mera convención lingüística. La objetualidad tiene grados.

### 2.2. Cuatro tipos de objetualidad

**Tabla 2.3.1.**

| Tipo | Definición | Ejemplos |
|---|---|---|
| **Compacto** | Continuidad material relativamente clara, límites estables | piedras, herramientas, moléculas |
| **Procesual** | Continuidad dinámica más que permanencia material | tormenta, llama, organismo, metabolismo |
| **Funcional** | Identidad por papel dentro de una red | servidor, órgano, módulo |
| **Institucional** | Existencia sostenida por prácticas, normas, soportes y reconocimiento | universidad, contrato, moneda, Estado |

A esto se añade un quinto modo derivado, **objeto teórico**: clase, variable latente, nodo comprimido, módulo inferido. Su realidad es teórica (capítulo 02-01) y su admisión depende de captura empírica de regularidades.

### 2.3. Implicación

No toda unidad explicativa es objeto del mismo tipo. La pregunta correcta no es "¿esta cosa es objeto?", sino "¿qué tipo de objetualidad sostiene esta categoría y bajo qué pregunta?". Esto descongestiona debates clásicos sin negar realidades efectivas.

## 3. Propiedades como disposiciones relacionales

### 3.1. Definición operativa

> Una propiedad es una disposición relacional materialmente anclada que altera las trayectorias del sistema acoplado bajo intervenciones específicas.

Esto rechaza la propiedad como contenido oculto adherido a una cosa y rechaza la propiedad como mera etiqueta sin anclaje.

### 3.2. Ejemplos paradigmáticos

- **fragilidad**: relación entre estructura del objeto y rango de fuerzas posibles; verificable por intervención (golpe, presión);
- **inteligencia**: patrón de adaptación, inferencia, aprendizaje y resolución de problemas bajo condiciones; verificable por intervención de tarea;
- **memoria** (como propiedad de un sistema): capacidad de modificar conducta o estado actual en función de trazas pasadas; verificable por intervención sobre el régimen histórico;
- **valor económico**: relación entre agentes, escasez, deseo, normas, intercambio e historia; verificable por intervención sobre cualquiera de los términos;
- **salud**: organización funcional del organismo en relación con rangos de operación y entorno; verificable por intervención fisiológica o ambiental;
- **seguridad informática**: relación entre configuración, amenazas, permisos, exposición, monitoreo y respuesta; verificable por simulación de ataque.

### 3.3. Implicación

Las propiedades no son sustancias menores. Son rasgos del sistema acoplado que se manifiestan bajo condiciones identificables. Esto preserva monismo material — la disposición está realizada — sin reducir la propiedad a etiqueta local simple.

## 4. Identidad como continuidad organizada

### 4.1. Definición operativa

> Una entidad conserva identidad cuando mantiene un patrón estabilizado a través de transformaciones tolerables para su tipo, donde la tolerancia se especifica como cuenca de atracción persistente bajo el régimen de transformación considerado.

Esto rechaza la esencia inmóvil y rechaza también la identidad como ficción sin anclaje.

### 4.2. Cómo opera la definición

- una persona conserva identidad a través de cambios biográficos: el patrón integrador (corporal, narrativo, social, afectivo, conductual) persiste como atractor bajo transformaciones acotadas;
- un organismo conserva identidad pese al recambio molecular: el patrón metabólico-funcional persiste como atractor bajo el recambio;
- una ciudad conserva identidad pese a transformaciones urbanas: la red de prácticas, infraestructuras y reconocimientos persiste como atractor bajo el cambio físico parcial;
- un servicio informático conserva identidad pese a despliegues sucesivos: el patrón funcional persiste bajo el redespliegue;
- una institución conserva identidad pese a rotación de miembros: el patrón normativo-práctico persiste bajo el cambio de cuerpos.

En cada caso la tolerancia es operacionalizable y verificable. La identidad no es absoluta ni arbitraria.

### 4.3. Implicación para casos límites

Identidades que aparecen problemáticas a la metafísica clásica se descongestionan:

- el barco de Teseo no es paradoja: hay continuidad funcional bajo recambio material; la identidad es real bajo el régimen funcional;
- la identidad personal a través del sueño profundo no es paradoja: la cuenca persiste aunque la dinámica activa se interrumpa;
- la identidad institucional bajo refundación no es paradoja: hay umbral de transformación más allá del cual la cuenca cambia, y ese umbral es identificable.

## 5. Límites y fronteras

### 5.1. Tres tipos de frontera

- **dura**: discontinuidad material (membrana celular, superficie de objeto compacto, contrato firmado);
- **funcional**: cambio de régimen dinámico (transición de fase, cambio de atractor, cambio de ley de control);
- **pragmática**: corte justificado por la pregunta sin discontinuidad material única.

### 5.2. Cuándo una frontera es legítima

Una frontera es real si su trazado mejora la legibilidad del patrón sin destruir dependencias relevantes. La verificación pasa por predicción e intervención discriminantes. Una frontera arbitraria es la que no produce ganancia inferencial bajo ninguna `Q` razonable.

### 5.3. Casos paradigmáticos

- ¿dónde termina un organismo y empieza su microbioma? Frontera funcional: depende de la pregunta. Para inmunología, una frontera; para metabolismo, otra;
- ¿dónde termina una aplicación y empiezan sus dependencias externas? Frontera funcional: depende del régimen de fallo considerado;
- ¿dónde termina una ciudad y empieza su zona metropolitana? Frontera pragmática: depende de la pregunta administrativa o sociológica;
- ¿dónde termina la mente y empieza el entorno técnico-social que la soporta? Frontera funcional/pragmática: depende del fenómeno (cognición situada, herramienta, prótesis).

## 6. Qué se evita con esta cuadrícula

**Tabla 2.3.2.**

| Tentación rechazada | Razón |
|---|---|
| Reificación | La categoría no garantiza sustancia |
| Reduccionismo plano | El objeto no se agota en lista de partes |
| Emergentismo inflado | Las propiedades no exigen segunda ontología |
| Relativismo categorial | Identidad y límites siguen restricciones reales |
| Esencialismo | La identidad no es esencia inmóvil |
| Nominalismo descuidado | Las categorías no son intercambiables si producen predicciones distintas |

## 7. Consecuencia para el lenguaje filosófico

La tesis no prohíbe usar términos ordinarios. Prohíbe tratarlos como transparentes. Se puede seguir hablando de mente, organismo, institución, mercado, memoria, objeto, propiedad. Cada uso queda sometido al filtro operativo: ¿qué patrón comprime?, ¿qué sustrato lo sostiene?, ¿qué dependencias conserva?, ¿qué predicción discriminante produce?, ¿bajo qué pregunta es legítimo?

## 8. Diálogo con interlocutores

### 8.1. Searle — ontología social

Searle distingue hechos brutos de hechos institucionales y construye una ontología social basada en intencionalidad colectiva, asignación de funciones, reglas constitutivas. La tesis recoge la asimetría hechos brutos / institucionales pero la reformula: lo institucional es realidad de cuarto tipo (capítulo 02-01) y se sostiene por patrones materialmente realizados, no por intencionalidad colectiva como propiedad mental supraindividual. La diferencia se prueba en el capítulo 05-04.

### 8.2. Bourdieu — campos, habitus, prácticas

Bourdieu ofrece campos, habitus y prácticas como unidades del análisis social. La tesis los recoge como patrones estabilizados materialmente sostenidos: el campo es atractor funcional con su cuenca; el habitus es disposición relacional incorporada; las prácticas son trayectorias dinámicas en el campo. La traducción al aparato es directa.

### 8.3. Latour — actantes y redes

Latour propone actantes y redes como unidades distribuidas que mezclan humanos y no-humanos. La tesis recoge la idea de red distribuida y la mezcla material-social, pero exige el filtro de admisión: un actante entra como nodo si pasa las cinco condiciones de patrón. No todo lo que se nombra como actante es patrón estabilizado.

### 8.4. Simondon — individuación e información

Simondon distingue individuo de individuación y trata la información como diferencia que se actualiza en sistemas metaestables. La tesis traduce: la individuación es formación de atractor a partir de sistema metaestable; la información es diferencia materialmente implementada que modula la dinámica del sistema acoplado. Esta es la traducción ya operativa en el caso ancla canónico.

### 8.5. Dennett — abstracciones reales

Dennett (1991, *Consciousness Explained*, cap. 13, p. 412) trata `el yo` como *"a center of narrative gravity"*: *"like a center of gravity in physics, it is a wonderfully useful fiction. It allows us to organize our world the way we are inclined to organize it"*. La tesis recoge el realismo de patrones pero **exige más**: el yo no es ficción útil sino atractor de integración corporal-narrativa-social-afectiva con cuenca medible; las creencias son disposiciones relacionales con efectos sobre la trayectoria conductual. Donde Dennett admite que el yo es ficción útil con consecuencias, la tesis distingue κ-pragmática (utilidad) de κ-ontológica (realidad estructural moderada): el yo es ficción útil **además de** patrón estabilizado del sistema acoplado organismo-entorno-tarea-historia. La diferencia se opera empíricamente en 05-01.

### 8.6. Wittgenstein — uso categorial y semejanzas de familia

Wittgenstein (*Investigaciones Filosóficas* §66, ed. Macmillan 1953, p. 27e) advierte sobre la búsqueda de esencias compartidas en categorías de uso: *"don't think, but look! Look for example at board-games... what is common to them all? — Don't say: 'There must be something common, or they would not be called "games"' — but look and see whether there is anything common to all"*. La tesis adopta esta sospecha pero la disciplina: las categorías como compresiones admisibles bajo κ no requieren esencia compartida, sino **función inferencial homogénea bajo Q**. Si dos casos respondiendo "X es Y" no comparten función inferencial bajo la misma `Q`, son categorías distintas con la misma palabra.

### 8.7. Bourdieu — habitus como disposición materialmente sedimentada

Bourdieu (1980, *Le sens pratique*, cap. 3, p. 88) define el habitus como *"sistemas de disposiciones durables y transponibles, estructuras estructuradas predispuestas a funcionar como estructuras estructurantes"*. La tesis traduce literalmente: el habitus es **disposición relacional materialmente incorporada** (cuerpo, gestos, lenguaje) que constituye atractor en el campo de prácticas. Donde Bourdieu describe cualitativamente la persistencia del habitus *"aún cuando las condiciones objetivas que lo produjeron han cambiado"* (1980, p. 100), la tesis opera la persistencia como **anchura de la cuenca** del atractor (tema desarrollado en 05-04).

## 8.bis. Identidad personal a través del tiempo

La tesis trata identidad como **continuidad organizada bajo transformación** (§4) sin abordar específicamente la cuestión clásica de **identidad personal a través del tiempo**. Aclaración:

### 8.bis.1. Postura: identidad como cuenca persistente del atractor humano

La identidad personal NO es:

- alma sustancial inmutable (rechazado por dualismo);
- conjunto de memorias estrictamente continuo (criterio Locke insuficiente: amnesias parciales no eliminan persona);
- agregado de estados psicológicos sin estructura (criterio reduccionista insuficiente).

La identidad personal **es**:

- **cuenca persistente** del atractor de integración corporal-narrativa-social-afectiva (cap 02-03 §8.5, ahora ampliado);
- continuidad del **sistema acoplado completo** (cuerpo + memoria + relaciones + historia), no de uno solo de sus componentes;
- **resistencia bajo perturbación**: una persona es la misma persona después de un shock si el sistema retorna a la cuenca de atracción característica.

### 8.bis.2. Diálogo

- **Locke** (1689, *An Essay Concerning Human Understanding*, II.27.9, p. 335 ed. Clarendon): identidad personal = continuidad de conciencia. La tesis recoge: la continuidad psicológica es **componente** del atractor, pero no único — la materialidad corporal y la trama relacional son co-constitutivas.
- **Parfit** (1984, *Reasons and Persons*, parte III, p. 199): la identidad personal NO es lo importante — lo que importa es la conexión psicológica gradual. La tesis matiza: la conexión es real pero la **cuenca persistente del atractor** sí es objeto ontológico identificable, no solo gradiente psicológico.
- **Strawson** (1959, *Individuals*) defiende re-identificación a través del cuerpo. La tesis recoge: el cuerpo es el **acoplador material continuo** que sostiene la cuenca.

### 8.bis.3. Implicación

La identidad de Pedro a los 5 y a los 50 años NO es identidad numérica estricta de elementos componentes (las células han cambiado, la memoria se ha transformado, las relaciones son otras). Es **persistencia de la cuenca de atracción** del sistema acoplado: el "estilo" de respuesta característica, la trama narrativa con sí mismo, la red relacional reconocible. Esta persistencia es **operativamente medible** en principio — el aparato no se ha aplicado a casos de identidad personal pero el marco general lo permite.

## 9. Regla práctica

> Cuando una categoría parezca demasiado cómoda, conviene sospechar. La comodidad lingüística suele ser el primer síntoma de reificación exitosa.

Esto se aplica también a los términos del propio marco: `dossier`, `compresión`, `acoplamiento`, `atractor`. Su uso debe poder traducirse a operación, observable o predicción. Si se vuelven contraseña interna, el capítulo 04-02 obliga a reescribir.

## 10. Cierre

Categorías son compresiones semánticas auditables. Objetos son unidades operativas relativas con tipos discriminables. Propiedades son disposiciones relacionales materialmente ancladas. Identidad es continuidad organizada como cuenca persistente. Las cuatro reformuladas son el inventario suficiente para que la tesis trate cualquier dominio sin sustancialismo y sin nominalismo. Lo que con ellas se puede hacer es lo que el capítulo 03 (formalización) opera y lo que los capítulos 05 (aplicaciones) demuestran.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-4-anclaje-empirico-nivel-b-multiescalar"></div>

# El nivel B: anclaje empírico (general multiescalar)


## Tesis del capítulo

> El nivel donde la tesis material-relacional gana o pierde anclaje empírico no es ningún nivel intermedio aislado, sino el **sistema dinámico acoplado entre el agente operativo y su entorno relevante**, bajo restricciones de tarea (o equivalente), físicas, informacionales e históricas. A ese nivel lo llamamos B. La definición es **invariante a la escala**: para un qubit, B es qubit-baño; para una proteína, B es macromolécula-solvente; para una persona, B es organismo-entorno-tarea; para un cúmulo globular, B es cúmulo-galaxia-marea. La asimetría L1↔B↔L3↔S es el protocolo formal de traducción que prohíbe la sustitución nominal y opera **a cualquier escala** donde el aparato puede aplicarse con sondas físicamente motivadas.

## 1. Los cuatro registros articulados (definición multiescalar)

```
L1 — del lenguaje ordinario / disciplinar : fija qué pregunta importa (vínculo indirecto)
B  — del acoplamiento empírico            : ancla la respuesta (vínculo directo y traduccional)
L3 — estructural-relacional               : reconstruye formalmente las dependencias detectadas
S  — semántica revisada                   : recoge las categorías que sobreviven a la auditoría
```

**Definición multiescalar de B:** B es el nivel donde el agente operativo (sea cual sea su escala: qubit, molécula, célula, organismo, estrella, cúmulo) está acoplado dinámicamente con su entorno relevante bajo restricciones específicas de la escala. La estructura es **invariante a la escala**:

**Tabla 2.4.1.**

| Escala | "Organismo" en B | "Entorno" en B | "Tarea" en B | "Historia" en B |
|--------|------------------|-----------------|---------------|-----------------|
| Cuántica (caso 31) | Qubit | Baño térmico | Mantener coherencia | Pulsos previos |
| Atómica (caso 32) | Configuración espín | Campo magnético | Acoplamiento espín-órbita | Trayectoria adiabática |
| Molecular (caso 33) | Proteína | Solvente, T | Estado plegado | Trayectoria de plegamiento |
| Bioquímica (caso 34) | Enzima | Concentración sustrato | Catálisis | Saturación previa |
| Celular (caso 35-36) | Célula | Glucosa / TNF | Ciclo / respuesta | Estado de fase previo |
| Individual (caso 37) | Sistema autonómico | Estrés | Regulación HRV | Tonos vagal/simpático |
| Conductual (caso ancla / 30) | Organismo | Entorno físico | Locomoción a meta | Aprendizaje motor |
| Astrofísica (caso 39-40) | Estrella / cúmulo | Espacio-tiempo galáctico | Pulsación / equilibrio | Evolución gravitacional |

La conducta humana (caso ancla Warren 2006, caso 30) es **una instancia entre muchas** de B, no su definición exclusiva. La primera iteración del manuscrito etiquetaba B como "conductual-biológico" porque el caso ancla era de behavioral dynamics; la versión multiescalar reconoce que B es **acoplamiento empírico genérico** y la subetiqueta "conductual" aplica solo a casos donde el agente es organismo en tarea conductual.

Lo que el borrador llamaba L2 se reparte entre B (donde están las cinco familias de variables descritas en §2) y los tramos específicos de la escala (neurobiología en escala individual, electroquímica en escala celular, hidrodinámica en escala astrofísica, etc.) cuando hagan falta para una pregunta concreta.

## 2. Qué incluye B

`B` es el dominio de las relaciones materialmente sostenidas entre cinco familias de variables. Ninguna es prescindible. El recorte habitual `cerebro versus mundo` deja fuera tarea e historia, y por eso es mal anclaje.

### 2.1. Organismo

Cuerpo, biomecánica (longitudes, masas, frecuencias naturales, rigidez aparente), repertorio motor, sistemas perceptivos, plasticidad, estado fisiológico. Cuando proceda, actividad neural específica como subgrafo de B.

### 2.2. Entorno

Superficies, objetos, fuerzas físicas (gravedad, fricción, restitución), propiedades materiales, otros agentes con sus dinámicas.

### 2.3. Información ecológica

#### 2.3.0. Definición filosófica de información

Antes de listar los ejemplos, fijamos qué entiende por información la tesis. La tesis adopta una **definición material-relacional de información** que combina dos tradiciones:

- **Bateson** (1972, *Steps to an Ecology of Mind*, p. 459): *"a difference which makes a difference"*. La información es **diferencia que produce diferencia** en la dinámica del sistema receptor.
- **Dretske** (1981, *Knowledge and the Flow of Information*, cap. 3, p. 63): la información semántica es **correlación nómica** entre estados de la fuente y estados del receptor que sostiene inferencia confiable.

**Síntesis de la tesis:** la **información es diferencia materialmente realizada** en el entorno (no en la mente del observador) que **modula la dinámica** del sistema acoplado cuando es detectada por sistemas perceptivos calibrados. No es entidad mental ni representación abstracta; es **propiedad estructural del sustrato material** que el organismo aprovecha sin necesidad de representarla internamente.

**Distinción operativa:**

- **información sintáctica** (Shannon): reducción de incertidumbre estadística;
- **información semántica** (Dretske, Floridi): correlación con contenido inferencial;
- **información ecológica** (Gibson, Bateson + tesis): diferencia materialmente realizada que modula dinámica acoplada **sin requerir representación interna**.

La tesis usa principalmente **información ecológica**: τ, ρ, flujo óptico no son representaciones en la mente, son patrones del entorno que modulan la dinámica del sistema acoplado.

#### 2.3.1. Ejemplos canónicos verificados en el caso ancla

Patrones detectables del flujo óptico, acústico y háptico que estructuran el entorno. Ejemplos canónicos verificados en el caso ancla:

- `τ`: razón entre tamaño angular óptico y su tasa de cambio; especifica tiempo hasta contacto;
- `τ̇`: derivada temporal; especifica adecuación de la deceleración;
- `τ_bal = θ/θ̇`: razón entre ángulo y velocidad angular; especifica tiempo hasta vertical;
- ángulo de declinación bajo el horizonte: especifica distancia;
- foco de expansión del flujo óptico: especifica dirección de auto-movimiento (heading φ_flow);
- error de heading β = φ − ψ_g: ángulo entre dirección actual y dirección de meta.

Estas variables son materialmente reales: están inscritas en la geometría y la física del entorno y pueden ser detectadas por sistemas perceptivos calibrados. No son representaciones internas.

### 2.4. Tarea

Objetivo (meta espacial, altura constante, parar antes del obstáculo), restricciones (rapidez, riesgo, costo energético), criterios de éxito o fracaso. La tarea selecciona qué variables son relevantes y qué tolerancia es aceptable. Selectividad que hace que la dinámica observable a nivel B sea de baja dimensión: la tarea ya hizo el primer trabajo de compresión antes de que el modelador llegue.

### 2.5. Historia

Trayectorias previas, aprendizaje, desarrollo, evolución, exposición a perturbaciones. Sin esta dimensión no se explica por qué dos agentes con la misma fisiología frente al mismo entorno producen conductas distintas. La historia entra como variables explícitas en el dossier de anclaje cuando el dominio lo requiere.

## 3. El acoplamiento como estructura básica de B

La unidad mínima de descripción a este nivel no es el organismo aislado ni el entorno aislado. Es el par dinámico acoplado:

```
ė = Φ(e, F)              dinámica del entorno bajo fuerzas F
ȧ = Ψ(a, i)              dinámica del agente bajo información i
F = β(a)                 fuerzas que el agente ejerce sobre el entorno
i = λ(e)                 información ecológica disponible en el entorno
```

Estas cuatro ecuaciones (formalmente equivalentes a las del ciclo percepción-acción de Warren) capturan dos acoplamientos simultáneos:

- **acoplamiento mecánico**: el agente actúa físicamente sobre el entorno y el entorno reacciona;
- **acoplamiento informacional**: el entorno produce patrones detectables que modulan la dinámica del agente.

La trayectoria conductual del par no es la suma de la trayectoria del agente y la del entorno: es la trayectoria del sistema conjunto en su espacio de estados.

### Consecuencias ontológicas

1. el `patrón estabilizado` (capítulo 02-01) se identifica con un atractor del sistema acoplado;
2. la `restricción real` se identifica con la estructura del campo vectorial (dónde converge, dónde diverge, dónde transiciona);
3. la `causalidad circular` se opera técnicamente: las componentes determinan la dinámica conjunta y la dinámica conjunta retroalimenta a las componentes a través de las leyes de control.

## 4. Self-organization: el modelo positivo de la emergencia

El borrador rechazaba el emergentismo fuerte (correctamente) pero solo como negación. Faltaba el modelo positivo. La tesis lo proporciona aquí, **anclado disciplinarmente** en dos tradiciones independientes que convergen en lo esencial:

- **Maturana y Varela (1980, *Autopoiesis and Cognition*, p. 78-84):** la organización viva es *"a network of processes of production [...] which through their interactions and transformations continuously regenerate and realize the network of processes that produced them"* (p. 78-79). La autopoiesis es **cierre operacional sostenido por transformaciones materiales**, no propiedad emergente sustancial.
- **Haken (1977, *Synergetics: An Introduction*, cap. 1, p. 1-7):** *"in many disciplines [...] a sudden self-organization of structure is observed when control parameters cross critical values"* (p. 1). El **principio del esclavizamiento** (slaving principle, cap. 7, p. 191-204) reduce la dinámica de muchos modos a unos pocos modos colectivos cuando el sistema cruza un umbral crítico — operacionalización de la emergencia sin sustancia añadida.

Sobre esa doble base, la tesis fija:

> Un fenómeno es emergente, en el sentido del marco, cuando dos o más sistemas dinámicos materialmente acoplados generan en el espacio conjunto estabilidades, inestabilidades y transiciones que no están preinscritas en ninguno de los componentes aislados pero tampoco son sustancia nueva.

Esta es la formulación técnica de **self-organization en sentido Maturana-Varela + Haken**: la emergencia es estabilización dinámica del sistema acoplado bajo restricciones físicas, informacionales y de tarea, no aparición de entidad adicional. Tres rasgos:

- **upward causation**: las componentes producen la dinámica global;
- **downward causation**: la dinámica global retroalimenta a las componentes (las leyes de control quedan ajustadas porque funcionan en el régimen estable);
- **anclaje material**: el fenómeno emergente es materialmente realizado y empíricamente identificable.

**Convención del manuscrito (glosario operativo §"Self-organization (sentido técnico)"):** cualquier ocurrencia textual de "self-organization", "auto-organización" o equivalentes en este manuscrito remite a esta sección y a las dos fuentes citadas. Donde la prosa no pueda mantener el anclaje disciplinar, debe sustituirse por "estabilización dinámica" o "convergencia a atractor".

Esto cierra la cláusula del capítulo 02-01: la emergencia no multiplica sustancias, opera como auto-organización en el sentido Maturana-Varela 1980 y Haken 1977.

## 5. Información ecológica como categoría central

Una tentación de cualquier ontología material es hacer del entorno una pasividad. La tesis ya lo rechaza, pero el mecanismo positivo aparece aquí: la información ecológica es regularidad estructural del medio físico que el organismo puede detectar sin requerir representación interna.

Para la tesis, esto cierra una brecha: explica cómo la conducta puede ser regular sin requerir un controlador central. La regularidad la pone en parte el entorno; el organismo se acopla a ella vía variables informacionales que no son representaciones sino diferencias materialmente implementadas que modulan la dinámica.

Estatuto ontológico: la información ecológica es realidad de tipo estructural (capítulo 02-01). No es realidad fuerte (no es cuerpo) y no es teórica (no es solo modelo): es la estructura del campo informacional que el acoplamiento detecta y aprovecha.

## 6. Tarea como dimensión constitutiva

La tarea no es accesorio. Es parte del sistema acoplado. Sin tarea no hay variables conductuales relevantes: la pelota es solo un proyectil parabólico, no `pelota a botar a altura constante`. El error de heading β no existe sin meta `ψ_g`. La tarea fija qué cuenta como atractor para una `Q` específica.

Esto tiene una consecuencia para la ontología. Algunos atractores existen incondicionalmente en el sistema (atractor pasivamente estable del raqueteo, repulsor físico del palo invertido, sistema neutralmente estable del frenado). Pero los atractores conductuales típicos son creados por el acoplamiento informacional bajo restricción de tarea: emergen cuando la información se acopla al sistema con una ley de control específica, y desaparecen sin acoplamiento. Esto es realismo estructural en su versión más sutil: el atractor no preexiste a la tarea, pero una vez constituida la tarea el atractor es plenamente real.

## 7. Historia como variable explícita

La historia entra como variables explícitas siempre que la pregunta lo requiera:

- **rondas previas** en una sesión de aprendizaje;
- **fase de aprendizaje** (exploración inicial, calibración, estabilización);
- **calibración perceptiva** previa a la tarea;
- **exposición** a perturbaciones específicas;
- **desarrollo ontogenético** cuando aplica;
- **historia evolutiva** cuando proceda para repertorios motores o sensoriales.

La historia no se trata como variable aparte; se incorpora como parte de las variables `X` del operador μ (capítulo 03-01). Esto permite que las leyes de control sean específicas del agente sin perder la forma funcional general.

## 8. Asimetría L1↔B↔L3↔S como protocolo

Este es el aporte estructural del capítulo. La asimetría no es decorativa; es protocolo de admisión y traducción.

### 8.0. Nota sobre el nivel cuantificacional de la asimetría

La asimetría se formula con dos partes que viven en niveles cuantificacionales distintos. La validación lógica formal con ST (Parte II, validación lógica formal, Hallazgo ST-1) detectó que mezclarlos en un solo nivel produce contradicción proposicional. La formulación correcta es:

- **Universal:** la traducción B ↔ L3 es bidireccional para toda categoría admisible (`∀x ((B(x) ↔ L3(x)))`); el filtro de S vía B y L3 es universal (`∀x ((B(x) ∧ L3(x)) → S(x))`).
- **Existencial:** las afirmaciones *"L1 no se deriva universalmente de S"* y *"S no se deriva universalmente de L1"* son **existenciales** (`∃x (L1(x) ∧ ¬S(x))` y `∃x (S(x) ∧ ¬L1(x))`), no negaciones de implicación universal. Significan: existen categorías L1 que no sobreviven al filtro y existen categorías S que no proceden de un L1 nombrado.

Esto evita la trampa de leer la asimetría como negación universal (que sería contradictoria) y la fija como **distinción de cobertura**: B y L3 cubren completamente el espacio de categorías admisibles; L1 y S sólo se solapan parcialmente con ese espacio.

### 8.1. L1 con L3: indirecto y restrictivo

L1 plantea preguntas comunicables (`¿cómo decide alguien por dónde caminar?`, `¿cómo recuerda una secuencia?`). Esas preguntas son indispensables para fijar relevancia. Pero L1 no responde: nombra el explanandum. La respuesta se construye en B y se formaliza en L3. L3 no debe responder con el mismo vocabulario de L1 (so pena de sustitución nominal); le habla a L1 solo a través de sus consecuencias observables.

### 8.2. B con L3: directo y traduccional

L3 es la reconstrucción formal de las dependencias detectadas en B. Cada término de L3 debe traducirse a una variable conductual o biológica medible. Si una clase estructural de L3 no se traduce a B, la clase está flotando — formalismo vacío.

### 8.3. S a posteriori

S (la semántica revisada: las categorías que sobreviven a la auditoría) se gana solo a posteriori. Las categorías que valga la pena conservar son las que: corresponden a atractores reales identificados en B; tienen formalización en L3; discriminan predicción e intervención. Las que no, se eliminan o se descomponen. La aspiración no es eliminar L1; es reconstruir S desde B + L3.

## 9. Qué descarta este nivel

**Tabla 2.4.2.**

| Tentación rechazada | Razón |
|---|---|
| Reduccionismo neurocéntrico | Sin tarea, entorno e historia, los circuitos no explican conducta |
| Mentalismo solipsista | Las categorías mentales sin acoplamiento con B son etiquetas |
| Formalismo desanclado | L3 sin traducción a B es metafísica formal |
| Conductismo radical | El acoplamiento informacional y la baja dimensionalidad estructural exceden el inventario E–R |
| Cognitivismo computacional fuerte | El sistema no requiere representación interna como recurso primario |

La discusión detallada con cada rival se trata en capítulo 04-01.

## 10. Diálogo con interlocutores

### 10.1. Gibson — psicología ecológica

Gibson (1979, *The Ecological Approach to Visual Perception*, cap. 8) sostiene que la información para la acción está disponible en el medio: *"the information for the perception of an object is not its image. The information in light to specify something does not have to resemble it"* (p. 304 ed. Houghton-Mifflin 1986). En los capítulos finales (cap. 13–14) explica que el control de la acción no requiere representación interna como recurso primario; basta con que el sistema perceptivo recoja invariantes específicos del flujo óptico.

La tesis recoge exactamente esto y lo opera: la información ecológica es **realidad estructural** (capítulo 02-01) y se traduce a variables medibles (τ, ρ, flujo óptico, ángulo de declinación). Donde Gibson queda en la formulación cualitativa de la affordance, la tesis avanza al sistema dinámico acoplado vía Warren-Fajen, ofreciendo ecuaciones cuantitativas y, en el caso 30 del corpus EDI, validación empírica con EDI = 0.262 significativo.

### 10.2. Maturana y Varela — autopoiesis y enaction

Maturana y Varela (1980, *Autopoiesis and Cognition*, cap. III) proponen la autopoiesis como cierre operacional de los sistemas vivos: *"an autopoietic machine continuously generates and specifies its own organization through its operation as a system of production of its own components"* (p. 79). En *El árbol del conocimiento* (1984, cap. 5) extienden la noción al ámbito cognitivo.

La tesis recoge la idea de cierre y la **operacionaliza** como cuenca de atracción del sistema acoplado bajo perturbación, con tolerancia explícita. La autopoiesis no requiere lectura mística: es estabilidad asintótica empíricamente verificable. La diferencia con Maturana-Varela: la tesis no asume circularidad organizacional como invariante a priori; la verifica caso por caso vía EDI.

### 10.3. Varela, Thompson y Rosch — embodied mind

Varela, Thompson y Rosch (1991, *The Embodied Mind*, cap. 8) consolidan la tesis de la cognición enactiva: *"cognition consists not of representations but of embodied action [...] the world is not something that is given to us but something we engage in by moving, touching, breathing, eating"* (p. 200). Thompson (2007, *Mind in Life*, cap. 4) lo desarrolla con neurofenomenología.

La tesis asume el enactivismo como tesis empírica del **nivel B**. La diferencia operativa: la tesis añade el **filtro formal de admisión** (capítulo 03-02) y la **operacionalización empírica de la compresión κ** (capítulo 03-04 y corpus EDI), que el enactivismo dejaba programáticos. Esta es una contribución específica a la tradición enactiva: la metodología cuantitativa que la tradición pedía pero no construía.

### 10.4. Andy Clark — extended mind

Clark y Chalmers (1998, "The Extended Mind", *Analysis* 58:7-19) sostienen el principio de paridad: *"if, as we confront some task, a part of the world functions as a process which, were it done in the head, we would have no hesitation in recognizing as part of the cognitive process, then that part of the world is (so we claim) part of the cognitive process"* (p. 8). Clark (2008, *Supersizing the Mind*, cap. 4) extiende el argumento.

La tesis lo opera como caso de B donde el entorno técnico se incorpora a las variables del acoplamiento. La extensión no es metafísica; es **decisión empírica sobre qué entra en X** del operador μ. La tesis evita la objeción de Adams y Aizawa (2008) (causa-constitución) exigiendo el criterio operativo: una variable extiende el acoplamiento si y solo si su ablación reduce significativamente la dinámica del sistema.

### 10.5. Warren — behavioral dynamics

Warren (2006, *Psychological Review* 113:358-389) proporciona el caso paradigmático trabajado del nivel B. La conjetura clave: *"the laws of behavior are descriptions of regular dynamical relations between organism and environment, that emerge from interactions in a particular task context"* (p. 359). Y la formulación dinámica de Fajen y Warren (2003, *JEP:HPP* 29:343-362, p. 348): la ecuación de heading de segundo orden (b = 3.25, k_g = 7.50, c1 = 0.40, c2 = 0.40) ajustada con r² = 0.980 sobre datos de locomoción dirigida.

La tesis recoge el caso Warren como demostración cualitativa (capítulo 05-05) y lo eleva a versión cuantitativa-EDI (caso 30 del corpus). Warren queda como **interlocutor principal de B**: vocabulario operativo (atractor, repulsor, bifurcación, ley de control, dinámica intrínseca, acoplamiento) y caso ancla. La complementariedad cualitativa (Warren 2006, r² = 0.980 individual) y cuantitativa (caso 30 EDI = 0.262, weak poblacional) cubre dos escalas temporales del fenómeno.

## 11. Consecuencia para el aparato formal

El operador `μ : R → X` debe leerse, en el caso de fenómenos psicológicos y conductuales, como medición a nivel B. `X` puede entonces incluir:

- variables conductuales: trayectoria, error de heading, fase, período, aceleración de impacto, latencia;
- variables informacionales ecológicas: τ, ρ, flujo óptico, ángulo de declinación, fase relativa;
- variables biomecánicas: longitud de extremidad, frecuencia natural, rigidez aparente;
- variables de tarea: objetivo, restricciones, costo, criterio de éxito;
- variables históricas: rondas previas, exposición, fase de aprendizaje.

El grafo `G = (V, E, W, T)` se construye sobre estas variables. Las dependencias que `E` representa son las del sistema acoplado, no las de un agente aislado. Las reglas de actualización `T` son las leyes físicas y las leyes de control empíricamente identificables.

## 12. Cierre

Con la incorporación de B como nivel pleno, la tesis recupera el plano que la respuesta del profesor exigía como condición de anclaje. Las consecuencias son tres:

- la ontología de patrones estabilizados gana su modelo positivo (atractores de sistemas acoplados);
- la epistemología de la compresión gana su test (la dinámica de baja dimensión a nivel B);
- la crítica al mentalismo deja de ser eliminativa para volverse constructiva: no se trata de borrar `mente`, `memoria` o `yo`, sino de reconstruir cuáles atractores conductuales-ecológicos comprime cada una y, a partir de ahí, decidir qué se conserva, qué se reformula y qué se descarta.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-5-temporalidad-y-causalidad"></div>

# Temporalidad y causalidad — fundamentos generales


## Tesis del capítulo

> El **tiempo** es ontológicamente real en sentido relacional B-series: es el orden de la sucesión de estados del sustrato material dinámico, sin "presente privilegiado" universal. La **flecha del tiempo** es termodinámica, no metafísica. La **causalidad** es relación de manipulabilidad woodwardiana entre variables del sistema acoplado, operacionalizada por intervención ablativa (`do`-test pearliano). La tesis acepta **causación constitutiva descendente** (downward constitution) sin recaer en downward causation kim-vulnerable: el atractor macroscópico **constituye** las constricciones del nivel componente sin causar nuevos eventos por encima de sus partes.

## 1. Postura sobre el tiempo

### 1.1. El tiempo como dimensión real-relacional

La tesis adopta **realismo temporal relacional B-series** (McTaggart 1908; Mellor 1998; perspectiva eternalista moderada): los eventos están ontológicamente ordenados en una serie *anterior–simultáneo–posterior* sin que exista un "presente" metafísicamente privilegiado.

**Razones operativas de la postura:**

1. el sustrato material dinámico tiene evolución temporal genuina: si negáramos la temporalidad, los atractores serían imposibles (un atractor es estado al que el sistema converge en el tiempo);
2. la postura A-series (presente real, pasado y futuro irreales) es incompatible con la generalidad multiescalar: en escalas cuántica y cosmológica, el "presente" es relativo al observador (relatividad especial);
3. la postura presentista pura (sólo lo presente existe) hace incomprensible el atractor mismo, que es objeto definido por su evolución temporal completa.

### 1.2. La flecha del tiempo

La tesis distingue tres flechas del tiempo:

- **flecha termodinámica**: aumento de entropía en sistemas cerrados (segunda ley);
- **flecha cosmológica**: expansión del universo;
- **flecha psicológica**: percepción subjetiva de pasado-presente-futuro.

La tesis afirma que la **flecha termodinámica es ontológicamente fundamental**, las otras dos son derivadas. La irreversibilidad del cierre operativo κ (la operación de compresión preserva dependencias decisivas pero la reapertura ε no es perfecto recobro) es **manifestación local de la flecha termodinámica**, no propiedad lógica ni metafísica adicional.

### 1.3. Tiempo e invarianza multiescalar

¿Cómo se compatibiliza el invariante "atractor" con escalas cuánticas donde la dinámica puede ser unitaria-reversible?

**Respuesta:** en escala cuántica pura (sistema cerrado sin medición), la dinámica es unitaria y los "atractores" son estados estacionarios. Pero los casos del corpus inter-escala (caso 31 decoherencia) son **sistemas abiertos** acoplados a baño térmico — ahí la flecha termodinámica está presente y los atractores son objetos dinámicos genuinos. La tesis NO afirma generalidad sobre sistemas cuánticos cerrados aislados; afirma generalidad sobre sistemas materiales acoplados, lo cual es la condición que el corpus respeta.

### 1.4. Diálogo con la tradición

- **Whitehead** (1920, *El concepto de naturaleza*, cap. 3, p. 53): *"nature is a process"*. La tesis recoge: el sustrato material es proceso, no inventario.
- **Bergson** (1889, *Tiempo y libre albedrío*) postula la *durée* como tiempo cualitativo subjetivo. La tesis lo trata como **fenómeno psicológico** (flecha psicológica), no como tiempo fundamental.
- **McTaggart** (1908, "The Unreality of Time", *Mind* 17:457-484) argumentó la incoherencia de la A-series. La tesis recoge la conclusión moderada (B-series adecuada) sin la negación radical de McTaggart.
- **Smolin** (2013, *Time Reborn*) defiende A-series. La tesis discrepa: la A-series es incompatible con relatividad especial y con la generalidad multiescalar requerida por la tesis.
- **Bunge** (1977, *Treatise* vol. 3, p. 152): *"time is a feature of the world, not a stage on which the world performs"*. La tesis lo adopta literalmente: el tiempo es **propiedad relacional del sustrato**, no escenario externo.

## 2. Postura sobre la causalidad

### 2.1. La causalidad como manipulabilidad woodwardiana

La tesis adopta **manipulabilidad woodwardiana** (Woodward 2003, *Making Things Happen*, cap. 2, p. 57: *"X causes Y if some intervention on X changes Y"*) como teoría de la causalidad operativa.

**Razones operativas:**

1. el aparato EDI **opera intervenciones ablativas** sobre el acoplamiento (apaga el ODE manteniendo el forcing); esto es operacionalmente woodwardian;
2. la teoría woodwardiana es compatible con el `do`-calculus de Pearl, que ya está integrado al aparato (cap 03-01 §12.1);
3. evita comprometerse con causalidad como relación entre eventos puntuales; la causalidad de la tesis es **relación entre variables del sistema acoplado**.

### 2.2. Pluralidad causal limitada

La tesis acepta **pluralismo causal limitado** (Cartwright 2007, *Hunting Causes and Using Them*, cap. 2): hay relaciones causales de tipos distintos (constitución, eficiencia, formal, retroalimentación) y no es necesario reducirlas a un único tipo. Pero rechaza el pluralismo radical: todas las relaciones causales del corpus se operan vía intervención ablativa, lo cual unifica metodológicamente sin unificar metafísicamente.

### 2.3. Causalidad circular

La tesis usa "causalidad circular" en cap 02-04 §3 (acoplamientos simultáneos organismo-entorno). Aclaración técnica:

- **causalidad circular** ≠ causalidad cíclica simple (X causa Y, Y causa X);
- **causalidad circular** = retroacción dinámica donde la dinámica del sistema acoplado tiene **bucles** que no se reducen a cadenas lineales;
- formalmente: el grafo causal del sistema acoplado tiene ciclos, no es DAG;
- esto NO viola el `do`-calculus pearliano: las intervenciones se definen sobre el grafo cíclico bajo expansión temporal explícita.

### 2.4. Downward causation: respuesta al argumento de Kim

Esta sub-sección merece tratamiento extendido porque la objeción de Kim es la objeción metafísica más recurrente contra cualquier ontología que afirme constricción macro→micro. El manuscrito anticipa que un evaluador con formación en metafísica de la mente la planteará en defensa, y por eso la respuesta se articula con cuatro pasos ordenados, no con declaración.

#### 2.4.1. Enunciado preciso del argumento de Kim

Kim (1998, *Mind in a Physical World*, cap. 4, p. 84) formula el **argumento de exclusión causal** en cinco premisas:

1. **Cierre causal del dominio físico:** todo evento físico tiene causa física suficiente.
2. **Sobreviniencia:** las propiedades macro M sobrevienen sobre las propiedades micro P.
3. **No sobredeterminación sistemática:** no es admisible que M y P causen sistemáticamente el mismo efecto Y.
4. **No epifenomenalismo:** rechazamos que M sea causalmente inerte.
5. **Conclusión por reducción:** la única salida coherente es que M sea idéntica a (o reducible a) P; cualquier downward causation genuina contradice (1)–(3).

Cualquier filosofía que afirme constricción macro→micro debe responder a este argumento sin invocar misterios y sin colapsar M en P (lo cual eliminaría el explanandum macro).

#### 2.4.2. Distinción operativa entre causación y constitución

La tesis distingue dos relaciones que la formulación clásica de Kim trata como una sola:

- **Causación** (Woodward 2003, *Making Things Happen*, cap. 2, p. 57): X causa Y si y sólo si una intervención sobre X (independiente del resto del sistema) produce un cambio sistemático en Y. Las relaciones causales son entre variables y son temporalmente extendidas.
- **Constitución** (Craver 2007, *Explaining the Brain*, cap. 4, p. 152): X constituye Y si y sólo si X es **parte de la realización material** de Y, verificable por **manipulabilidad mutua** — manipular X cambia S y manipular S cambia X. Las relaciones constitutivas son sincrónicas y no requieren transferencia causal entre niveles.

La intervención ablativa del aparato EDI (`do(coupling = 0)`) opera explícitamente como test woodwardiano sobre **variables del sistema acoplado**, no sobre eventos micro individuales. Lo que el aparato detecta no es "M causa Y por encima de P"; es "el régimen acoplado tiene dependencias estructurales que la versión sin acoplamiento pierde".

#### 2.4.3. Aplicación al aparato EDI

Cuando el aparato detecta cierre operativo (EDI > umbral), no afirma que el atractor macro **causa** algo que las componentes micro no causan. Afirma algo más modesto y filosóficamente más defensable:

- el atractor macro **constituye las restricciones** dentro de las cuales las componentes evolucionan;
- esas restricciones son **detectables operativamente** porque al apagar el acoplamiento (ablación), las trayectorias se degradan;
- la degradación no muestra que el macro tenga "poder causal extra" sobre el micro; muestra que **la descripción macro captura dependencias estructurales que la descripción micro descontextualizada pierde**.

Esto es exactamente la noción de Craver (*mutual manipulability*) operacionalizada por intervención ablativa. No hay sobredeterminación porque no hay dos cadenas causales paralelas; hay una sola dinámica acoplada que admite descripción a dos niveles, y la descripción macro es **constitutivamente** legítima cuando el test de manipulabilidad mutua se cumple.

#### 2.4.4. Por qué esto no diluye la tesis

Un crítico podría objetar: *"si reformulan downward causation como constitución, han abandonado la afirmación fuerte que su tesis necesita"*. La respuesta es que la tesis nunca necesitó downward causation en el sentido kim-vulnerable. Lo que necesita es:

- que los **patrones macro sean reales** (no nominales);
- que su realidad sea **detectable operativamente** (no postulada);
- que su realidad **constriña la dinámica de las componentes** sin violar el cierre causal físico.

Las tres condiciones se cumplen bajo la formulación constitutiva. El atractor existe materialmente como configuración del sistema acoplado, su existencia se detecta por intervención ablativa, y su efecto sobre las componentes es constitutivo (parte de la realización), no causal (transferencia de poder por encima del cierre físico).

La verificación formal de este argumento está en la suite ST T13 (hallazgo ST-3): la implicación `((C ∧ ¬V) ∧ (K → (V → S))) → ¬S` no es derivable directamente, pero el argumento de Kim queda neutralizado **por modus tollens vacuo** — si la constricción macro→micro es constitución (C) y no causación (¬V), entonces la premisa de Kim que requiere V es falsa de antemano, y la conclusión sobre sobredeterminación S no se sigue.

**Implicación:** la cláusula "downward causation material" del cap 02-04 §4 se refina canónicamente como **"constitución descendente material"** (downward constitution). El argumento de Kim no aplica porque ataca un blanco que la tesis no defiende.

### 2.5. Diálogo con causal emergence (Hoel 2017)

Hoel, Albantakis y Tononi (2013, *PNAS* 110:19790-19795) introducen **causal emergence**: el macro puede tener mayor poder causal (información efectiva) que el micro. La tesis recoge parcialmente:

- la **información efectiva** macro de Hoel es métrica adyacente a EDI, no idéntica;
- EDI mide **dependencia ablativa** (cuanto baja la predicción al apagar el acoplamiento); Hoel mide **información efectiva** (capacidad causal del nivel);
- los dos enfoques son **complementarios**, no rivales: ambos capturan la realidad de los niveles macroscópicos sin postular nuevas sustancias.

## 3. Síntesis: tiempo + causalidad como dimensiones generales

La tesis ahora afirma con respaldo articulado:

**Tabla 2.5.1.**

| Dimensión | Postura | Operacionalización |
|-----------|---------|---------------------|
| **Tiempo** | B-series relacional, eternalismo moderado | Series temporales del corpus, dt explícito en sondas |
| **Flecha del tiempo** | Termodinámica fundamental, otras derivadas | Irreversibilidad parcial de κ↔ε |
| **Causalidad** | Manipulabilidad woodwardiana | Intervención ablativa = `do`(coupling = 0) |
| **Causación circular** | Retroacción en grafo cíclico | Acoplamiento ABM↔ODE bidireccional |
| **Downward "causation"** | Reformulado como constitución | Mutual manipulability de Craver |

Esto cubre los vacíos V5-02, V5-03, V5-09 con honestidad: la tesis no inventa metafísica del tiempo ni de la causalidad; **adopta posturas defendidas en la literatura** y las articula explícitamente para que el aparato no quede flotando metodológicamente.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-6-dimension-normativa-y-etica"></div>

# Dimensión normativa y ética — naturalismo no-reduccionista


## Tesis del capítulo

> La tesis adopta **naturalismo ético no-reduccionista** compatible con sistemismo bunguiano. Los valores son **atractores normativos** materialmente sostenidos por sistemas humanos en interacción con su entorno; las normas son **constricciones operativas** sobre la dinámica institucional con cuenca de atracción medible (validez), tasa de retorno (efectividad) y anchura de cuenca (legitimidad). La ética **no es reducible** a descripción material pero **no requiere sustancia adicional** para existir: emerge en el sistema acoplado humano-comunidad-historia como dimensión propia con eficacia causal. La tesis rechaza tanto el reduccionismo eliminativo (los valores son ilusión útil) como el sobrenaturalismo ético (los valores existen en plano separado).

## 1. La cuestión normativa en una ontología material-relacional

Una ontología material-relacional enfrenta de inmediato la objeción humanista clásica: *"si todo lo real es material y dinámico, ¿qué pasa con los valores, los deberes, lo bueno?"*. La tesis tiene tres opciones:

1. **eliminativismo:** los valores son ilusiones útiles sin estatus real;
2. **dualismo normativo:** los valores existen en plano separado del material;
3. **naturalismo no-reduccionista:** los valores son patrones materialmente sostenidos sin sustancia adicional.

La tesis **rechaza (1) y (2)** y adopta (3). Las razones:

- (1) eliminativismo es incompatible con la posición filosófica del **irrealismo operativo** que admite la realidad de patrones materialmente sostenidos como entidades operativamente reales. Los valores y las normas son patrones materialmente sostenidos en sistemas humanos; no son ilusión.
- (2) dualismo normativo viola el monismo ontológico de la tesis. La tesis ya rechaza el dualismo cartesiano para la mente; análogamente lo rechaza para los valores.
- (3) naturalismo no-reduccionista es la única opción coherente con la ontología general de la tesis y compatible con la operatividad del aparato.

## 2. Valores como atractores normativos

Un **valor** (justicia, libertad, dignidad, verdad, belleza) **no es entidad sustancial separada**, ni propiedad cualquiera del sustrato. Es **atractor normativo** del sistema humano-comunidad-historia: una región del espacio de fase de la conducta colectiva donde el sistema converge bajo perturbación, sostenida por:

- **prácticas materialmente sostenidas** (rituales, instituciones, lenguaje);
- **inscripciones normativas** (constituciones, códigos, manuales);
- **cuerpos en relación** (tradiciones encarnadas);
- **sanciones organizadas** (derecho positivo, sanción social);
- **memoria histórica** (continuidad bajo transformación).

El valor *justicia*, por ejemplo, no es entidad platónica. Es atractor normativo del sistema social que se manifiesta operativamente cuando el sistema retorna a régimen de cumplimiento bajo perturbación (un agravio activa procesos de restauración del régimen normativo).

Esta es **traducción al aparato** de las nociones tradicionales de Bunge (1989, *Treatise* vol. VIII, *Ethics: The Good and the Right*) y MacIntyre (1981, *After Virtue*).

## 3. Normas como constricciones operativas

Una **norma** (regla moral, jurídica, social) es **constricción operativa** sobre la dinámica del sistema acoplado humano-institución. Tiene tres propiedades operacionalizables:

- **validez**: cuenca de atracción del cumplimiento bajo perturbación (¿el sistema retorna al cumplimiento si se viola la norma?);
- **efectividad**: tasa de retorno de la cuenca (¿qué tan rápido se recupera el cumplimiento?);
- **legitimidad**: anchura de la cuenca (¿qué nivel de perturbación tolera el sistema sin abandonar la norma?).

Esta operacionalización (anticipada en cap 05-04 §4.3) ahora se sostiene **filosóficamente** sobre la base de:

- **Bunge** (1989, *Treatise* vol. VIII, p. 47): *"a moral norm is a rule guiding voluntary action that affects the well-being of others"*. La tesis recoge: las normas son guías de acción **materialmente realizadas** en prácticas, no entidades abstractas separadas.
- **Searle** (2010, *Making the Social World*, cap. 5, p. 100): *"institutional facts are inherently normative"*. La tesis recoge: la dimensión normativa es **constitutiva** de las instituciones, no añadido.
- **MacIntyre** (1981, *After Virtue*, cap. 14, p. 219): las virtudes son disposiciones **adquiridas en prácticas comunitarias** que permiten alcanzar bienes internos a la práctica. La tesis recoge: las virtudes son habitus en sentido bourdieuano materialmente sostenido.

## 4. La derivación de "debe" desde "es"

La objeción humeana clásica: *"de hechos descriptivos no se siguen prescripciones normativas"*. La tesis responde con **falacia naturalista mitigada**:

- La tesis NO afirma que de un hecho material A se siga deductivamente una prescripción "debes hacer B".
- La tesis SÍ afirma que **valores y normas son hechos materialmente realizados** en sistemas humanos, y por tanto admiten **estudio empírico de su dinámica** sin reducirlos a meros hechos físicos.
- Searle (1964, "How to Derive 'Ought' from 'Is'", *Philosophical Review* 73:43-58) argumenta que la derivación es legítima cuando los hechos institucionales son intrínsecamente normativos. La tesis recoge esto matizando: la derivación no es deductivamente formal sino **constitutivamente normativa** (las instituciones constituyen normas en su funcionamiento).

## 5. Diálogo con tradición ética

**Tabla 2.6.1.**

| Tradición | Postura de la tesis |
|-----------|---------------------|
| **Bunge ético sistemista** | Adoptado como interlocutor principal (1989, vol. VIII) |
| **MacIntyre virtud-comunitario** | Adoptado para la tesis de virtudes como habitus material |
| **Searle ontología social** | Adoptado para la tesis de normas como hechos institucionales |
| **Foot natural goodness** | Compatible: lo bueno como funcionamiento del organismo en su forma de vida |
| **Mackie error theory** | Rechazado: los valores no son error proyectivo, son patrones materiales |
| **Kantianismo deontológico puro** | Rechazado en su forma trascendental; recogido como heurística práctica |
| **Utilitarismo cuantitativo** | Rechazado por reduccionismo a una dimensión |
| **Emotivismo** (Ayer, Stevenson) | Rechazado: los valores no son meras emociones |

## 6. Estatus epistémico de la postura ética de la tesis

**Lo que la tesis afirma:**

- los valores y las normas son **reales en sentido moderado** (atractores normativos materialmente sostenidos);
- la ética admite **estudio empírico de su dinámica** sin reducirla a física;
- la dimensión normativa es **constitutiva** del sistema humano-institución, no añadido;
- el caso piloto COVID (cap 05-04 §7.1) intentó operacionalizar esto y produjo null honesto, lo cual reveló que **las sondas continuas simples no capturan la dinámica normativa**. Esto NO refuta la tesis ética; muestra que la operacionalización requiere sondas con histéresis y variables ordinales.

**Lo que la tesis NO afirma:**

- no funda una ética nueva;
- no resuelve disputas clásicas (deontología vs consecuencialismo vs virtud);
- no demuestra qué es lo bueno;
- no provee algoritmo para decisiones morales;
- no reduce la ética a descripción material (la dimensión normativa es propia, no derivada).

## 7. Limitación reconocida

La operacionalización empírica completa de la dimensión normativa **requiere desarrollo metodológico adicional**. El caso piloto COVID confirmó que el aparato actual no captura la dinámica normativa con sondas continuas simples. La elevación a casos demostrativos genuinos es **deuda priorizada** (programa formal en `Bitacora/2026-04-28-cierre-doctoral/`). Mientras tanto, la postura ética de la tesis se sostiene **filosóficamente** sobre las bases articuladas en este capítulo, no como demostración empírica cerrada.

## 8. Implicaciones para los capítulos posteriores

- **cap 05-04** (instituciones, mercado, Estado) recibe respaldo filosófico explícito: la dimensión normativa institucional opera como atractor en el sentido aquí articulado;
- **cap 06-01** (conclusión) puede ahora afirmar que la tesis cubre la dimensión normativa sin reducirla;
- **caso piloto COVID** se reinterpreta a la luz de esta postura: el null no es fracaso de la ética, es señal de que la sonda elegida era inadecuada para capturar la dinámica institucional con saltos discretos.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---


<div id="parte-2-metodo"></div>

# Parte II — Aparato formal y método


<div id="capitulo-7-aparato-formal-minimo"></div>

# Aparato formal mínimo (metodología general)


## Tesis del capítulo

> El aparato mínimo de la tesis consiste en cinco operadores (μ, G, H, κ, ε) y una pregunta paramétrica (Q con tolerancia τ). Cada operador tiene definición precisa, criterio de admisión, criterio de fallo y procedimiento empírico de aplicación. Ningún operador entra en el manuscrito sin protocolo. La formalización **no es ontología adicional**: es disciplina de inteligibilidad de la ontología material-relacional general sobre fenómenos empíricamente accesibles **a cualquier escala**. Es **metodología general** porque la ontología que disciplina es general.

## 1. Niveles del esquema general

El aparato articula cinco registros del proyecto:

```
O0  — sustrato ontológico                      (capítulo 02-01)
E1  — acceso empírico                          (régimen de medición)
F2  — formalización basal (grafo G)            (este capítulo)
F3  — organización estructural superior (H, κ) (este capítulo y 03-04)
S4  — semántica revisada (S)                   (capítulo 02-03)
```

El nivel B (conductual-biológico, capítulo 02-04) no es un registro paralelo; es el lugar donde E1 vive cuando el dominio es psicológico-conductual: la medición se hace sobre el par dinámico acoplado.

> Notas terminológicas: cada operador definido a continuación está glosado además en el **Glosario operativo** de preliminares. Cualquier término técnico introducido en este capítulo (μ, G, H, κ, ε, dossier de anclaje, EDI, LoE, asimetría L1↔B↔L3↔S) puede consultarse allí con definición autocontenida y referencias cruzadas.

> Capa de consistencia lógica: las afirmaciones declarativas centrales del aparato y los teoremas mínimos que la tesis afirma derivar (núcleo ontológico, criterios de legitimidad, debates) están formalizadas adicionalmente en `08-consistencia-st/theories/` mediante el lenguaje ST (`@stevenvo780/st-lang`). Esta capa no sustituye el trabajo filosófico: opera como verificador automático de consistencia interna y trazabilidad. Los reportes generados se consolidan en `08-consistencia-st/reports/` y se usan internamente para detectar contradicciones simples antes de cada cierre de versión del manuscrito.

## 2. La pregunta como parámetro: Q

Toda formalización se evalúa respecto a una pregunta `Q` con tolerancia explícita:

```
Q = (φ, τ, R)
```

donde:

- `φ` es la formulación del problema explicativo o interventivo;
- `τ` es la tolerancia: qué diferencia entre modelo y datos cuenta como aceptable;
- `R` es el régimen de medición: qué se mide, con qué instrumento, bajo qué condiciones.

`Q` se fija antes del intento de modelización y queda fechada. Cambiar `Q` después de un fallo invalida el ciclo y exige reiniciar admisión. Esto cierra la objeción de irrefutabilidad por nivel (capítulo 04-02).

## 3. Operador 1: medición μ

### 3.1. Definición

```
μ : R → X
```

`μ` es la operación de medición, observación, registro o intervención que recorta el dominio efectivo de realidad `R` en un conjunto de variables `X` observables, inferidas u operacionalizadas.

### 3.2. Qué entra en X

Para fenómenos a nivel B, `X` puede incluir variables conductuales, informacionales ecológicas, biomecánicas, de tarea e históricas (capítulo 02-04). Para otros dominios, `X` se especifica análogamente.

### 3.3. Criterio de admisión de μ

Una medición es admisible si:

- el régimen `R` está especificado (instrumento, condiciones, frecuencia de muestreo);
- las variables `X` están operacionalizadas (definición precisa de qué se cuenta);
- la repetibilidad está documentada (protocolo accesible a tercero).

### 3.4. Criterio de fallo

Si las variables medidas no son repetibles bajo el mismo régimen, el problema no es del modelo: es de la medición. La tesis no avanza con μ defectuoso.

## 4. Operador 2: grafo basal G

### 4.1. Definición

```
G = (V, E, W, T)
```

donde:

- `V` son nodos (variables, estados, unidades) sobre el conjunto X;
- `E` son aristas (relaciones, dependencias, transiciones);
- `W` son pesos (intensidades, signos, condiciones de activación, sensibilidades);
- `T` son reglas de actualización dinámica (ecuaciones diferenciales, leyes de control, transiciones probabilísticas).

### 4.2. Qué representa E

`E` no se reduce a una sola noción de causalidad. Una arista puede representar:

- causalidad directa, condición de posibilidad, restricción, acoplamiento dinámico, constitución funcional, dependencia histórica, dependencia contextual, correlación robusta con valor explicativo verificada por intervención.

La tesis prohíbe la arista decorativa: solo entran las relaciones que afectan la inteligibilidad del fenómeno respecto de Q.

### 4.3. Criterio de admisión de G

Una arista `(v_i, v_j) ∈ E` es admisible si:

- es detectable por covarianza condicional bajo régimen R;
- es robusta a intervenciones específicas (`do(v_i)` cambia `v_j`);
- su peso `w_{ij}` tiene unidad dimensionalmente coherente.

### 4.4. Criterio de fallo

Si una arista no resiste intervención (manipular `v_i` no cambia `v_j` de la manera predicha), se elimina o se reformula. La consistencia interna del grafo no basta: se exige consistencia con intervención.

## 5. Operador 3: hipergrafo H

### 5.1. Por qué hace falta

Muchos fenómenos no se explican con relaciones binarias. Hay acoplamientos múltiples (proteína que depende de varias moléculas a la vez, conducta que depende de organismo + entorno + tarea simultáneamente, institución que depende de cuerpos + documentos + normas + reconocimientos), restricciones globales y configuraciones de orden superior.

### 5.2. Definición

```
H = (V, 𝓔)
```

donde `𝓔` es un conjunto de hiperaristas que conectan conjuntos de nodos simultáneamente. Cada hiperarista `e ∈ 𝓔` es un subconjunto de `V` con su régimen de actualización conjunta.

### 5.3. Para qué sirve

`H` permite representar:

- co-dependencias múltiples;
- módulos funcionales con frontera identificable;
- ensamblajes contextuales;
- restricciones globales que se actualizan conjuntamente;
- agregaciones de tarea que no se reducen a pares.

### 5.4. Criterio de admisión

Una hiperarista es admisible si la dependencia conjunta no se reduce sin pérdida a una conjunción de relaciones binarias bajo Q. La prueba es la diferencia inferencial: si separar la hiperarista en pares produce las mismas predicciones, no hay hiperarista; hay grafo binario.

## 6. Operador 4: compresión κ

### 6.1. Definición

```
κ : G → G*
```

`κ` es la operación que reemplaza una subestructura compleja `G' ⊂ G` por una unidad operativa `n_{G'}` (nodo, módulo, clase) en un grafo más tratable `G*`, cuando el detalle interno de `G'` no produce diferencia inferencial relevante para Q.

### 6.2. Sentido filosófico

`κ` modela el paso desde dependencias finas a organización de orden superior sin postular sustancia nueva. La unidad comprimida es real en sentido estructural si su atractor es empíricamente identificable; teórica si solo modeliza regularidades sin captura empírica directa.

### 6.3. Sentido operativo

`κ` reduce dimensionalidad efectiva conservando la estructura relevante para Q. La operacionalización empírica detallada está en el capítulo 03-04. Aquí se fija el criterio:

> κ(G) = G* es legítima respecto a Q si y solo si existe un sistema dinámico de baja dimensión sobre G* que (a) reproduce las trayectorias observadas dentro de τ, (b) preserva atractores, repulsores y bifurcaciones empíricamente identificadas, (c) predice respuestas a perturbaciones e intervenciones, (d) no oculta una transición que sí ocurre en los datos.

### 6.4. Criterio de fallo

Si alguno de los cuatro requisitos falla, la compresión está empíricamente desautorizada y debe revisarse o sustituirse por expansión ε.

## 7. Operador 5: expansión ε

### 7.1. Definición

```
ε : n → G_n
```

`ε` abre un nodo comprimido `n` para mostrar su subgrafo interno `G_n` cuando la pregunta lo exige.

### 7.2. Cuándo es necesaria

Tres signos obligan a expandir:

- la compresión actual impide distinguir casos relevantes para Q;
- la estructura interna modifica predicciones o intervenciones;
- el sistema se aproxima a una bifurcación donde el régimen interno cambia.

### 7.3. Criterio de admisión

`ε` es legítima si la expansión produce ganancia inferencial mayor que el costo introducido. La regla:

> expandir cuando la estructura interna produce diferencias inferenciales relevantes; comprimir cuando el detalle interno no las produce.

### 7.4. Importancia de ε para κ

Una compresión sin expansión inversa disponible es caja negra ilegítima. La existencia operativa de `ε` es condición de admisión de `κ`. Esto cierra la cláusula de reversibilidad parcial del capítulo 02-02.

## 8. Cómo se articulan los operadores

El flujo canónico de uso es:

```
1. Fijar Q = (φ, τ, R)                                       [pregunta paramétrica]
2. Aplicar μ : R → X                                          [medición]
3. Construir G = (V, E, W, T) sobre X                         [grafo basal]
4. Detectar relaciones de orden superior → H si procede       [hipergrafo]
5. Ensayar κ : G → G* (vía baja dimensionalidad empírica)     [compresión]
6. Validar G* contra datos: reproducción, generalización,
   topología, intervención                                    [validación]
7. Si validación pasa: G* admisible respecto a Q              [admisión]
8. Si validación falla en alguna prueba: aplicar ε en la
   subestructura responsable                                  [expansión]
9. Iterar hasta admisión o declarar fallo trazado             [cierre o deuda]
```

Este flujo no es retórico. Es protocolo y se aplica al caso ancla canónico (capítulo 05-05) y a cualquier aplicación admisible.

## 9. Niveles y escalas sin multiplicación de mundos

El paso `G → G*` mediante κ no introduce una nueva realidad. Introduce una nueva organización descriptiva y explicativa. Los operadores formalizan **registros** del mismo plano material:

- el grafo no es la realidad;
- el hipergrafo no es la realidad;
- el modelo reducido no es la realidad;
- todos son representaciones de restricciones reales del sustrato.

La cláusula es estricta: ninguna entidad del aparato formal se reifica. La discusión filosófica de este punto está en capítulo 02-01 §10 y en capítulo 04-02.

## 10. Ejemplo canónico: caso ancla

En el caso ancla canónico (Warren 2006, capítulo 05-05) los operadores se instancian así:

**Tabla 3.1.1.**

| Operador | Instanciación |
|---|---|
| Q | `¿qué dirección de marcha adopta un humano caminando hacia meta y evitando obstáculo?` con τ = error en `r²` ≤ 0.02 |
| μ | Captura de movimiento en VENLab (Brown), 12 m × 12 m, head-mounted display, sonic-inertial tracking, frecuencia 60 Hz |
| X | heading φ, error de heading β, velocidad v, distancia a meta d_g, ángulo a meta ψ_g, distancia a obstáculo d_o, ángulo a obstáculo ψ_o |
| G | Grafo de dependencias entre las variables anteriores con leyes físicas (gravedad, biomecánica) y leyes informacionales (flujo óptico, dirección egocéntrica) como T |
| H | Hiperarista que conecta meta + obstáculo + heading cuando hay biestabilidad de ruta |
| κ | Reducción a sistema de segundo orden φ̈ = −b φ̇ − k_g(φ−ψ_g)(e^{−c1·d_g}+c2) + k_o(φ−ψ_o)(e^{−c3|φ−ψ_o|})(e^{−c4·d_o}) con d=2 dimensiones efectivas y r²=0.980/0.975 |
| ε | Reapertura cuando aparecen patologías no capturadas (obstáculos como puntos, agentes con dinámica de evitación propia) |

Este ejemplo no es ilustrativo: es la prueba de que el aparato opera empíricamente sobre datos reales con resultados públicamente verificables. Cualquier otra aplicación admisible debe alcanzar instanciación equivalente.

## 11. Ejemplo programático: sistemas técnicos

En sistemas distribuidos los operadores se instancian programáticamente (sin medición experimental controlada equivalente al caso ancla):

**Tabla 3.1.2.**

| Operador | Instanciación |
|---|---|
| Q | `¿por qué cayó producción en t = T?` con τ = identificación de la causa raíz |
| μ | Logs, métricas, traces, checks de salud |
| X | Latencia, throughput, error rate, certificate validity, DNS resolution time, queue depth |
| G | Grafo de dependencias entre componentes técnicos |
| H | Hiperaristas para fallos cascada que involucran múltiples servicios |
| κ | Compresión a nivel de servicio cuando la pregunta es disponibilidad global |
| ε | Reapertura cuando la pregunta es diagnóstico fino |

La diferencia con el caso ancla: aquí no hay datos experimentales con sistema controlado y ecuaciones ajustadas. Es modo programático (capítulo 05-03) hasta que se construya el análogo demostrativo.

## 12. Diálogo con interlocutores formales

### 12.1. Pearl — grafos causales y do-calculus

Pearl (2009, *Causality*, 2.ª ed., cap. 3, p. 70) define el operador de intervención: *"the action `do(X = x)` represents an experiment in which the variable X is set to value x by an outside intervention, while the rest of the model remains unchanged"*. La tesis absorbe esta operación en `G` y `E` con dos restricciones: (a) los grafos representan dependencias del sistema acoplado, no causalidad lineal aislada; (b) la admisión de aristas exige `do`-test, no solo correlación. La métrica EDI es **operacionalización directa de un do-test**: ablación del acoplamiento ODE con preservación del forcing exógeno, comparada contra coupled completo.

### 12.2. Ladyman y Ross — realismo estructural informativo

Ladyman y Ross (2007, *Every Thing Must Go*, §3.4) sostienen que la ontología fundamental es estructural: *"the world is not made of things or stuff but of structure all the way down"*. La tesis converge parcialmente: las invariantes son, en este marco, las propiedades preservadas por `κ`. Diverge en que la tesis no postula estructura como ontología fundamental sino como **descripción operativa del sustrato material**: la estructura es estructura **del** sustrato dinámico, no flotante (cap 02-01). Esta es la diferencia que la tabla comparativa con rivales codifica como discriminación en el criterio A (anclaje material).

### 12.3. Strogatz, Kelso, Haken — sistemas dinámicos no lineales

Strogatz (1994, *Nonlinear Dynamics and Chaos*, cap. 6, p. 168) define el atractor como *"a closed set A such that any trajectory that comes close enough to A approaches A as t → ∞"*. Kelso (1995, *Dynamic Patterns*, cap. 3, p. 73) extiende el lenguaje al dominio de coordinación: *"the qualitative change in the form of behavioral patterns is termed a phase transition or bifurcation"*. Haken (1977/2004, *Synergetics*, cap. 1) introduce los parámetros de orden como variables macroscópicas que dominan la dinámica cerca de transiciones. La tesis adopta este vocabulario **sin modificación**: la formalización del aparato es precisamente este vocabulario, ahora aplicado bajo dossier de admisión.

### 12.4. Symbolic Theory Language (ST)

ST se usa como capa de validación de consistencia local (capítulo 08-consistencia-st). Su función no es probar verdad sino detectar tensiones internas en la formalización del manuscrito.

## 13. Límites del formalismo

El aparato no sustituye investigación empírica ni análisis filosófico detallado. Sirve para:

- ordenar el problema;
- fijar operadores con criterio público;
- controlar pérdidas de detalle;
- comparar niveles bajo Q común;
- evitar reificaciones.

Si el formalismo se usa para mucho más, sobreactúa. La cláusula:

> ningún operador se justifica si no produce ganancia inferencial concreta sobre alguna `Q`.

## 14. Fórmula final

> El aparato formal mínimo consiste en una pregunta paramétrica Q y cinco operadores (μ, G, H, κ, ε) con criterios de admisión, criterios de fallo y procedimientos empíricos de aplicación. Los operadores no son ontología adicional: son disciplina de la inteligibilidad de la ontología material-relacional sobre fenómenos empíricamente accesibles. Su valor se prueba en el caso ancla canónico (capítulo 05-05); su programa de extensión se especifica en los capítulos de aplicaciones.

## 15. Estatus ontológico de las entidades matemáticas

La tesis usa hipergrafos, ODE, dinámica no-lineal, bootstrap, permutación. ¿Qué estatus ontológico tienen las entidades matemáticas en el marco material-relacional?

### 15.1. Estructuralismo matemático moderado

La tesis adopta **estructuralismo matemático moderado** como postura de partida:

- las **estructuras matemáticas** (hipergrafos, ecuaciones diferenciales, espacios de fase) son **representaciones formales de patrones reales del sustrato**;
- NO son **entidades platónicas independientes** (rechazado por incompatible con el monismo material de la tesis);
- NO son **ficciones útiles sin referencia** (rechazado por incompatible con el realismo moderado);
- son **representaciones cuya validez depende de homomorfismo parcial** con la dinámica material que describen.

### 15.2. Diálogo

- **Shapiro** (1997, *Philosophy of Mathematics: Structure and Ontology*, cap. 3, p. 85): *"mathematics is the science of structures"*. La tesis recoge esta caracterización en su versión moderada: la matemática describe estructuras, pero las estructuras son **estructuras de algo material**, no flotantes.
- **Hellman** (1989, *Mathematics without Numbers*) defiende estructuralismo modal sin compromiso ontológico con números. La tesis se alinea: lo importante es la **estructura**, no la entidad numérica.
- **Maddy** (1990, *Realism in Mathematics*) defiende empirismo matemático. La tesis es compatible: las estructuras matemáticas se validan **por su éxito en capturar dependencias materiales** verificables por intervención.

### 15.3. Implicación para κ

Si las **estructuras pre-ontológicas son atractores** y los atractores son **objetos matemáticos definidos sobre espacios de fase**, ¿qué tan real es la matemática en la ontología?

**Respuesta:** la matemática es **real en sentido representacional moderado**: es la herramienta formal que captura las dependencias del sustrato material. Los atractores existen materialmente (como patrones del sustrato dinámico); las descripciones matemáticas de los atractores existen como **representaciones legítimas** de esos patrones cuando preservan dependencias decisivas. La realidad ontológica primaria está en el sustrato; la realidad de las estructuras matemáticas es **derivada y representacional**.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-8-mapa-de-operadores-formales"></div>

# Mapa de operadores formales

## Función

Mapa visual y operativo de los cinco operadores del aparato formal de la tesis con su flujo canónico de uso, criterios de admisión, criterios de fallo y procedimientos empíricos.

---

## Diagrama del aparato

```
                       ┌──────────────────────────────────┐
                       │  Q = (φ, τ, R)                   │
                       │  Pregunta paramétrica fechada    │
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  μ : R → X                       │
                       │  Operador de medición            │
                       │  X = variables observables       │
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  G = (V, E, W, T)                │
                       │  Grafo basal de dependencias     │
                       │  cada arista pasa do-test        │
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  H = (V, 𝓔)                      │
                       │  Hipergrafo (orden superior)     │
                       │  cuando dependencias no son binarias
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  κ : G → G*                      │
                       │  Compresión                      │
                       │  empírica vía EDI                │
                       └─────────────┬───────┬────────────┘
                                     │       │
                                     │       │ (si validación falla)
                                     │       ▼
                                     │   ┌─────────────────────┐
                                     │   │  ε : n → G_n        │
                                     │   │  Expansión inversa  │
                                     │   └─────────────────────┘
                                     │
                                     ▼
                       ┌──────────────────────────────────┐
                       │  Validación (4 pruebas + C1-C5)  │
                       │  + 8 criterios extra             │
                       │  = overall_pass                  │
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  Clasificación en paisaje        │
                       │  Nivel 0 a Nivel 4 (5 futuro)    │
                       └──────────────────────────────────┘
```

---

## Flujo canónico de uso

```python
# 1. Fijar Q
Q = (
    formulacion='¿exhibe el fenómeno X cierre operativo bajo sonda S?',
    tolerancia=0.05,            # error medio aceptable
    regimen='medición mensual'  # frecuencia de muestreo
)

# 2. Aplicar μ: extraer variables del dominio
X = mu(R, regimen=Q.regimen)
# X = lista de variables observables/inferidas con su unidad

# 3. Construir G: grafo basal con criterios de admisión
G = construir_grafo(X, criterios_admision={'do_test': True})
# Cada arista pasa do-test (manipular v_i debe cambiar v_j)

# 4. Detectar H si procede
H = detectar_hipergrafo(G) if hay_dependencias_no_binarias(G) else None

# 5. Ensayar κ: compresión empírica vía EDI
G_star = kappa(G, metodo='EDI', n_perm=999, n_boot=500)
# Calcula EDI = 1 - RMSE_coupled / RMSE_no_ode

# 6. Validar con 13 condiciones (C1-C5 + extras)
validacion = validar(G_star, Q,
                     pruebas=['reproduccion', 'generalizacion', 'topologia', 'intervencion'],
                     protocolo=['C1', 'C2', 'C3', 'C4', 'C5'])

# 7. Si falla: aplicar ε para reabrir y reintentar
if not validacion.overall_pass:
    G_n = epsilon(G_star, region_problematica=validacion.fallo_localizado)
    # Iterar o declarar limitaciones honestas

# 8. Clasificar en paisaje
nivel = clasificar(EDI=validacion.edi,
                   p=validacion.p_value,
                   overall=validacion.overall_pass)
```

---

## Operador μ — detalle

**Tabla A.2.1.**

| Campo | Especificación |
|-------|----------------|
| Firma | `μ : R → X` |
| Entrada | dominio efectivo de realidad |
| Salida | conjunto de variables operacionalizadas |
| Criterio de admisión | régimen R especificado, variables operacionalizables, repetibilidad documentada |
| Criterio de fallo | medidas no repetibles bajo el mismo régimen |
| Implementación EDI | función `data.py::fetch_<dominio>` por caso |

---

## Operador G — detalle

**Tabla A.2.2.**

| Campo | Especificación |
|-------|----------------|
| Firma | `G = (V, E, W, T)` |
| V (nodos) | variables observadas |
| E (aristas) | dependencias detectadas que pasan do-test |
| W (pesos) | covarianza condicional, sensibilidad a intervención |
| T (reglas) | leyes físicas + leyes de control empíricamente identificables |
| Criterio de admisión | aristas robustas a intervenciones específicas |
| Criterio de fallo | manipular v_i no cambia v_j según predicción → eliminar arista |
| Implementación EDI | implícita en `hybrid_validator.py::run_full_validation` |

---

## Operador H — detalle

**Tabla A.2.3.**

| Campo | Especificación |
|-------|----------------|
| Firma | `H = (V, 𝓔)` |
| 𝓔 | hiperaristas que conectan ≥3 nodos simultáneamente |
| Cuándo crear H | dependencias conjuntas no reducibles sin pérdida a pares |
| Criterio de admisión | separar la hiperarista en pares cambia las predicciones |
| Implementación EDI | `topology_generator.py` para topologías heterogéneas (scale-free, small-world) |

---

## Operador κ — detalle (operacionalizado vía EDI)

**Tabla A.2.4.**

| Campo | Especificación |
|-------|----------------|
| Firma | `κ : G → G*` |
| Definición empírica | `EDI = 1 - RMSE_coupled / RMSE_no_ode` |
| Significancia | prueba de permutación (n_perm=999) |
| CI | bootstrap (n_boot=500) |
| Refinamiento | n_refine=5000 sobre top_k=10 candidatos |
| Criterio de admisión | EDI > 0 + p < 0.05 + protocolo C1-C5 |
| Gate completo (overall_pass) | 13 condiciones simultáneas |
| Criterio de fallo | falla en cualquiera de las 4 pruebas (reproducción, generalización, topología, intervención) |
| Implementación | `common/hybrid_validator.py` (2252 líneas) |

### Las cuatro pruebas de validación

1. **Reproducción**: el sistema reducido reproduce trayectorias medias dentro de tolerancia τ. Métrica: varianza explicada en condiciones similares al entrenamiento.
2. **Generalización**: predice trayectorias en condiciones no usadas para ajuste.
3. **Topología**: el campo vectorial reducido tiene los mismos atractores, repulsores y bifurcaciones que los datos.
4. **Intervención**: predice correctamente qué pasa al intervenir una variable.

---

## Operador ε — detalle

**Tabla A.2.5.**

| Campo | Especificación |
|-------|----------------|
| Firma | `ε : n → G_n` |
| Cuándo aplicar | tres signos: compresión impide distinguir casos relevantes; estructura interna modifica predicciones; sistema cerca de bifurcación |
| Criterio de admisión | ganancia inferencial mayor que el costo introducido |
| Garantía | la existencia operativa de ε es condición de admisión de κ |
| Implementación EDI | reapertura de subestructuras vía `resource_manager.py` o re-calibración local |

---

## Pregunta Q — detalle

**Tabla A.2.6.**

| Campo | Especificación |
|-------|----------------|
| Estructura | `Q = (φ, τ, R)` |
| φ | formulación del problema explicativo o interventivo |
| τ | tolerancia: qué diferencia es aceptable |
| R | régimen de medición: instrumento, condiciones, frecuencia |
| Fechado | obligatorio. Cambiar Q después del fallo invalida el ciclo |
| Implementación EDI | `case_config.json` con dates, thresholds, execution params |

---

## Validación canónica vs perfiles agresivos

**Tabla A.2.7.**

| Parámetro | Canónico | Agresivo (HYPER_*) |
|-----------|---------:|-------------------:|
| n_perm (permutación) | 999 | 2999 |
| n_boot (bootstrap) | 500 | 1500 |
| n_refine (refinamiento) | 5000 | 10000 |
| n_runs (réplicas) | 15 | 30 |
| grid_size (ABM) | 40 | 60+ |

---

## Niveles del paisaje y umbrales

```
EDI = -1 ─┬───────────────────┬───────────────────┬────────── EDI = 1
          │                   │                   │
       Nivel 0           Nivel 1-2-3          Nivel 4
       (null)         (trend/sug/weak)        (strong)
                            │
       EDI ≤ 0      0 < EDI ≤ 0.30           0.30 < EDI ≤ 0.90

                                            (con overall_pass=True
                                             requiere 13 condiciones)
```

**Flag de tautología:** EDI > 0.90 es flag para revisión manual (puede indicar sobreajuste).

**Flag de epifenomenalismo:** macro_coupling < 0.10 es flag (la sonda no está realmente acoplada).

---

## Referencias cruzadas al manuscrito

- Definición conceptual de los operadores: capítulo 03-01
- Criterios de admisión y dossier: capítulo 03-02
- Auditoría como protocolo: capítulo 03-03
- Operacionalización de κ vía EDI: capítulo 03-04
- Implementación: `09-simulaciones-edi/common/`
- Aplicación a 30 casos: capítulo 09 + `09-simulaciones-edi/<caso>/`


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-9-criterios-de-legitimidad-y-dossier"></div>

# Criterios de legitimidad y dossier de anclaje


## Tesis del capítulo

> Una compresión, una categoría o un modelo es legítimo respecto a una pregunta `Q` si y solo si satisface los diez criterios del marco organizados en un dossier de anclaje verificable por terceros. El dossier no es lista decorativa: es filtro de admisión cuyo incumplimiento implica retiro de la propuesta. El método de evaluación es público, comparativo y trazable.

## 1. Regla general

> una categoría, un modelo o una compresión son legítimos si preservan estructura relevante del fenómeno para una pregunta `Q` y mejoran la capacidad de explicar, predecir o intervenir sin inflación ontológica innecesaria, bajo dossier de anclaje públicamente verificable.

Esto consolida los criterios dispersos en el borrador original en un solo gesto operativo. Lo que sigue son las condiciones específicas y el procedimiento de evaluación.

## 2. Los diez criterios

### 2.1. Anclaje material

El modelo debe conectarse con procesos materialmente instanciados. Si no puede señalarse qué soporta o realiza el fenómeno, la propuesta pierde fuerza ontológica antes de evaluarse cualquier otro criterio.

### 2.2. Dependencia empírica

Debe haber posibilidad de observación, medición, registro, comparación o intervención bajo régimen R explícito. Acceso indirecto se admite si está justificado.

### 2.3. Fidelidad relacional

La compresión no debe borrar dependencias que cambian el fenómeno bajo Q. La fidelidad se prueba con intervención: si manipular una variable supuestamente comprimida produce diferencia inferencial inesperada, la compresión ocultaba estructura relevante.

### 2.4. Poder inferencial

El recorte debe permitir concluir algo nuevo, ordenar mejor los casos o reducir confusión conceptual respecto a la versión no comprimida o respecto a alternativas.

### 2.5. Poder predictivo

La representación debe mejorar la anticipación de estados, conductas, fallas o trayectorias. La mejora es comparativa: respecto a un rival explícito, no en abstracto.

### 2.6. Poder interventivo

Una buena categoría ayuda a decidir qué modificar para producir otro resultado. Si la categoría no orienta intervención discriminante, su utilidad es solo descriptiva.

### 2.7. Robustez

El patrón debe sostenerse al menos parcialmente bajo cambios razonables de contexto, medición o escala. Una compresión que se evapora ante cualquier perturbación menor es frágil.

### 2.8. Reversibilidad parcial

Debe ser posible reabrir lo comprimido cuando el problema lo exija. Una compresión sin operador ε disponible es caja negra.

### 2.9. Economía explicativa

La representación debe reducir complejidad sin ocultar lo decisivo. La medida no es estética: es relación entre coste del modelo y ganancia inferencial.

### 2.10. No reificación

Debe quedar claro que la categoría o el modelo no se convierten automáticamente en sustancia independiente. Esto se verifica revisando si se predican capacidades sustantivas no derivables del sustrato.

## 3. Dossier de anclaje

El dossier consolida los diez criterios en un documento operativo que cualquier aplicación admisible debe acompañar.

### 3.1. Componentes obligatorios

Un dossier completo contiene:

```
1. Pregunta Q = (φ, τ, R)                    fechada
2. Variables X (observables o inferidas)     con régimen de medición
3. Sustrato material instanciante            descrito explícitamente
4. Grafo G = (V, E, W, T)                    con criterios de admisión de aristas
5. Hipergrafo H si procede                   con justificación
6. Compresión κ propuesta                    con dimensionalidad efectiva
7. Atractores, repulsores, bifurcaciones     identificados empíricamente
8. Pruebas de validación                     reproducción, generalización, topología, intervención
9. Predicción discriminante                  contra rival explícito
10. Intervención discriminante               experimento que la falsaría
11. Operador ε                               protocolo de reapertura para regiones límite
12. Traducción B↔L3                          cada parámetro de L3 a variable de B
13. Limitaciones declaradas                  régimen donde el modelo no se aplica
14. Comparación rival                        tabla con criterios públicos
```

### 3.2. Criterio de completitud

Un dossier es admisible si los catorce componentes están presentes con contenido sustantivo. Componentes vacíos o decorativos invalidan el dossier.

### 3.3. Criterio de fallo del dossier

Un dossier falla si:

- alguna variable no es operacionalizable;
- alguna arista no resiste `do`-test;
- la compresión no pasa las pruebas de validación;
- la predicción discriminante no se cumple en datos públicos;
- la intervención discriminante se evita;
- algún parámetro de L3 no se traduce a B (formalismo desanclado).

El fallo en cualquiera implica retiro de la propuesta o reescritura del dossier desde el componente afectado.

## 4. Matriz de evaluación

Para evaluación operativa rápida, los diez criterios se puntúan en escala de tres niveles:

- **0**: el criterio no se cumple;
- **1**: se cumple débilmente o parcialmente;
- **2**: se cumple robustamente.

Una categoría que sistemáticamente obtiene 0 o 1 en los criterios clave para Q debe revisarse, dividirse, expandirse o abandonarse. La evaluación se documenta en el dossier para trazabilidad.

### Matriz para el caso ancla canónico

Aplicada al modelo de Fajen y Warren (2003) bajo Q = `predicción de heading en marcha hacia meta y evitando obstáculo`:

**Tabla 3.2.1.**

| Criterio | Valor | Justificación |
|---|---|---|
| Anclaje material | 2 | Cuerpo + entorno + tarea + información ecológica explícita |
| Dependencia empírica | 2 | Captura motora en VENLab, intervenciones documentadas |
| Fidelidad relacional | 2 | Reproduce datos con r²=0.980/0.975 |
| Poder inferencial | 2 | Predice rutas que el lenguaje ordinario no formula |
| Poder predictivo | 2 | Predicciones cumplidas en condiciones nuevas |
| Poder interventivo | 2 | Manipulación de flujo óptico, posición de obstáculos |
| Robustez | 2 | Estable bajo ruido gaussiano del 10% en variables perceptivas |
| Reversibilidad parcial | 2 | ε bien definido en regiones de bifurcación |
| Economía explicativa | 2 | 4 parámetros para r²=0.980 |
| No reificación | 2 | Atractores y repulsores como propiedades del sistema acoplado |

Total: 20/20. Esta matriz es el estándar contra el cual se mide cualquier otro candidato a aplicación demostrativa.

## 5. Método de evaluación

### Paso 1. Fijar la pregunta Q

No hay evaluación legítima sin pregunta explícita. Cambiar Q después del fallo invalida el ciclo.

### Paso 2. Identificar la categoría heredada

Preguntar qué término o unidad viene dado por el lenguaje ordinario o disciplinar.

### Paso 3. Localizar el sustrato material

Señalar qué procesos, soportes, cuerpos, infraestructuras o prácticas la instancian. Para fenómenos a nivel B, esto incluye organismo + entorno + información + tarea + historia.

### Paso 4. Aislar variables relevantes

Construir el conjunto X de variables observables, inferidas u operacionalizables. Especificar régimen de medición R.

### Paso 5. Mapear dependencias

Construir G = (V, E, W, T). Cada arista pasa criterio de admisión del capítulo 03-01.

### Paso 6. Probar una compresión

Aplicar κ con procedimiento empírico del capítulo 03-04. Identificar dimensionalidad efectiva y atractores.

### Paso 7. Someter a los diez criterios

Puntuar cada criterio. Identificar puntuaciones débiles.

### Paso 8. Comparar contra rival explícito

Construir tabla de discriminación contra al menos un rival. Identificar celdas donde el modelo gana, celdas donde pierde, celdas donde empata.

### Paso 9. Decidir

Solo entonces puede decidirse:

- **mantener la compresión** si pasa todos los criterios y discrimina contra rival;
- **expandirla** si falla en fidelidad relacional o robustez;
- **dividirla** si la cuenca de atracción no es única;
- **reemplazarla** si un rival la domina en la matriz;
- **conservarla solo como rótulo práctico** si su valor es comunicativo pero no inferencial.

## 6. Método de cambio de escala

El paso entre escalas no debe depender de intuición. Se orienta por tres preguntas:

1. ¿la estructura interna modifica la explicación bajo Q?
2. ¿la compresión actual impide distinguir casos relevantes?
3. ¿abrir el nivel añade ganancia explicativa mayor que el costo?

### Regla de decisión

- si la respuesta es sí a las dos primeras, conviene expandir;
- si la tercera respuesta es no, conviene mantener compresión;
- si el beneficio marginal del detalle es bajo, la expansión es metodológicamente mala.

## 7. Qué cuenta como evidencia a favor de la tesis

La propuesta gana fuerza cuando puede mostrar que un recorte material-relacional bajo el aparato:

- mejora un diagnóstico respecto a marco rival;
- resuelve una falsa sustancialización con predicción discriminante verificable;
- ordena mejor un fenómeno multiescala con dimensionalidad efectiva justificada;
- permite comparar dominios distintos con la misma matriz de evaluación.

Cada uno de estos requiere caso paradigmático, no afirmación general.

## 8. Qué contaría como fracaso

La tesis fracasa localmente cuando:

- no puede distinguir un buen recorte de uno malo;
- termina usando `relación`, `patrón` o `compresión` como comodines vacíos;
- no sabe cuándo expandir ni cuándo comprimir;
- no mejora ninguna explicación concreta frente a alternativas disponibles;
- algún parámetro de L3 no se traduce a B.

El fracaso global se discute en capítulo 06-01.

## 9. Método comparativo con posiciones rivales

Para mostrar ventaja filosófica, cada caso de aplicación se compara con tres rivales explícitos. Por dominio:

- **caso ancla canónico** (percepción-acción): rivales son control óptimo con modelos internos, cognitivismo computacional, conductismo radical;
- **mente, memoria, yo** (modo programático): rivales son cognitivismo simbólico, dualismo de propiedades, eliminativismo neuroreductor;
- **biología/ecología**: rivales son reduccionismo molecular, holismo ecológico inflado, esencialismo de especie;
- **sistemas técnicos**: rivales son arquitectura monolítica, modelado de servicios sin dependencias, físicalismo absurdo;
- **instituciones**: rivales son individualismo metodológico, holismo trascendental, nominalismo social.

La tesis debe mostrar qué preserva mejor y qué pierde menos que cada rival. Capítulo 04-01 desarrolla la confrontación filosófica; los capítulos 05-* la operan por dominio.

## 10. Diferencia entre los diez criterios y el dossier de anclaje

Los diez criterios son la **lista verificable** de propiedades exigidas. El dossier de anclaje es el **documento operativo** que organiza la evidencia de cumplimiento. Los criterios son condiciones; el dossier es prueba. Una propuesta puede satisfacer los criterios en abstracto y carecer de dossier; en ese caso no se admite. La tesis exige dossier publicable, no solo cumplimiento abstracto.

## 11. Diálogo con interlocutores

### 11.1. Bunge — exigencias de cientificidad

Bunge (1967, *La investigación científica*, vol. 2, p. 32) formula los criterios de cientificidad de un constructo: *"claridad, falsabilidad, contrastabilidad, no contradicción interna, compatibilidad con el grueso del conocimiento previo, capacidad explicativa y predictiva"*. Los diez criterios de este capítulo extienden esa lista al dominio multiescala con énfasis en **compresión** y **reversibilidad**, dos exigencias adicionales que Bunge no operacionaliza con la misma especificidad pero que la tesis vuelve verificables.

### 11.2. Lakatos — programas de investigación

Lakatos (1970, "Falsification and the Methodology of Scientific Research Programmes", en *Criticism and the Growth of Knowledge*, Cambridge, p. 132) distingue núcleo duro y cinturón protector: *"the negative heuristic of the programme forbids us to direct the modus tollens at this 'hard core'"*. La tesis se organiza así: el núcleo duro son las condiciones de admisión (capítulos 02-01, 02-02, 02-04, 03-01, 03-02); el cinturón protector son las aplicaciones (capítulo 05). Una falsificación local del cinturón no falsifica el núcleo, pero **acumular falsificaciones del cinturón degrada el programa** (criterio lakatosiano de progresividad). Los 8 nulls del corpus son falsificaciones legítimas del cinturón aplicado, no del núcleo.

### 11.3. Cartwright — capacidades verificables por intervención

Cartwright (1989, *Nature's Capacities and their Measurement*, cap. 4, p. 141) propone que *"causes are taken to act 'individually', i.e., they have stable, transferable capacities to produce effects which they continue to be disposed to do whether they actually do produce them or not"*. La tesis recoge esta idea: los criterios 5 (predictivo) y 6 (interventivo) son **verificación de capacidad bajo intervención**, no de regularidad observada. La métrica EDI mide capacidad ablativa: si el acoplamiento es capacidad real, su ablación produce diferencia; si es ficción explicativa, no.

### 11.4. Pearl — `do`-calculus

Pearl (2009, *Causality*, cap. 3, p. 86) formaliza la diferencia entre `P(y|x)` y `P(y|do(x))`: la primera es observación, la segunda intervención. La tesis exige `do`-test cuando es factible (criterios 3, 5 y 6). Las dependencias del grafo G no son correlaciones: son sensibilidades a intervención. Esta es la diferencia entre el corpus EDI (admite ablación) y comparaciones puramente correlacionales (no admiten).

## 12. Cierre

Los diez criterios y el dossier de anclaje convierten la tesis en una propuesta auditable. Ningún producto del marco entra en el manuscrito sin pasar el filtro. La diferencia con un manifiesto es esta exactamente: un manifiesto promete; un programa de investigación se compromete. La tesis se compromete con el dossier.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-10-plantilla-del-dossier-de-anclaje"></div>

# Plantilla del dossier de anclaje

## Función

Plantilla estandarizada del dossier de anclaje obligatorio para cualquier categoría candidata en modo demostrativo. Cualquier caso que entre en el manuscrito debe presentar este dossier completo. Para modo programático, los componentes 1-3 y 7-9 son obligatorios; los demás son conjeturas con criterio de elevación.

---

## Plantilla

```markdown
# Dossier de anclaje: [Nombre del caso]

**Categoría heredada (L1):** [término ordinario o disciplinar]
**Modo:** [demostrativo / programático]
**Fecha de fijación:** [YYYY-MM-DD]

---

## 1. Pregunta Q

- **Formulación φ:** [enunciado preciso del problema]
- **Tolerancia τ:** [criterio de error aceptable, e.g., r² ≤ 0.05]
- **Régimen R:** [instrumento, condiciones, frecuencia de muestreo]
- **Cambios posteriores prohibidos:** sí. Si Q cambia, se reinicia el ciclo de admisión con Q'.

## 2. Variables X

**Tabla A.3.1.**

| Variable | Tipo | Régimen R | Operacionalización |
|----------|------|-----------|--------------------|
| ... | observable / inferida | mensual / anual / etc | método de medición |

## 3. Sustrato material instanciante

[Descripción explícita de los procesos, soportes, cuerpos, infraestructuras
que materialmente realizan el fenómeno.]

## 4. Grafo G = (V, E, W, T)

- **V (nodos):** [lista de variables]
- **E (aristas):** [dependencias detectadas que pasan do-test]
- **W (pesos):** [covarianzas, sensibilidades]
- **T (reglas):** [leyes físicas, leyes de control empíricas]

## 5. Hipergrafo H (si procede)

[Si las dependencias son binarias, escribir "no aplica". Si hay relaciones
de orden superior, listar hiperaristas y justificar no-reducibilidad.]

## 6. Compresión κ propuesta

- **Método:** EDI vía intervención ablativa
- **Sonda ODE:** [nombre del modelo, e.g., mean_reversion, behavioral_attractor]
- **Forma funcional:** [ecuación]
- **Parámetros calibrados:**
  - α = [valor]
  - β = [valor]
  - macro_coupling = [valor]
  - forcing_scale = [valor]
- **Dimensionalidad efectiva (d):** [número]

## 7. Atractores, repulsores, bifurcaciones identificados

- **Atractores empíricos:** [lista con valores y cuenca]
- **Repulsores empíricos:** [lista]
- **Bifurcaciones documentadas:** [lista con parámetros de control]

## 8. Pruebas de validación

**Tabla A.3.2.**

| Prueba | Resultado | Tolerancia |
|--------|-----------|-----------:|
| Reproducción | varianza explicada = X% | τ específica |
| Generalización | desempeño fuera entrenamiento = X | τ |
| Topología | atractores preservados sí/no | — |
| Intervención | predicciones cumplidas X/N | — |

**Protocolo C1-C5:**

**Tabla A.3.3.**

| Filtro | Estado | Detalle |
|--------|:------:|---------|
| C1 Convergencia | ✓/✗ | RMSE_coupled vs RMSE_no_ode |
| C2 Robustez | ✓/✗ | clasificación estable bajo ±20% perturbación |
| C3 Determinismo | ✓ | seed=42 |
| C4 Consistencia dominio | ✓/✗ | trayectorias respetan restricciones físicas |
| C5 Reporte de incertidumbre | ✓ | CI bootstrap, modos de fallo, LoE, val_steps |

**EDI cuantitativo:**

- EDI = [valor]
- Bootstrap CI = [lo, hi]
- p-value (permutación 999) = [valor]
- overall_pass = [True/False]
- Nivel = [0/1/2/3/4]

## 9. Predicción discriminante

[Predicción específica que un rival explícito no produce o produce peor.
Debe ser cuantitativa y verificable.]

**Rival explícito:** [posición y referencia]
**Predicción de la tesis:** [enunciado]
**Predicción del rival:** [enunciado]
**Datos empíricos disponibles:** [referencia]
**Verificación:** [a favor de la tesis / del rival / inconcluso]

## 10. Intervención discriminante

[Experimento o intervención cuyo resultado contrario falsaría la propuesta.
Debe ser ejecutable y registrable.]

## 11. Operador ε con protocolo de reapertura

[Plan de reapertura para regiones donde la compresión no funciona.
Identificar variables que se reabrirían y régimen de reapertura.]

## 12. Traducción B↔L3

**Tabla A.3.4.**

| Parámetro de L3 | Variable de B | Unidad | Operacionalización |
|-----------------|---------------|--------|---------------------|
| ode_alpha | tasa de [...] | unidades físicas | medición directa |
| ode_beta | constante de [...] | unidades físicas | calibración empírica |
| ... | ... | ... | ... |

[Cada parámetro de L3 debe traducirse a B. Si alguno no se traduce, la
categoría está flotando y debe reformularse.]

## 13. Limitaciones declaradas

- **Régimen de no aplicabilidad:** [condiciones donde el modelo deja de aplicar]
- **Datos insuficientes:** [si val_steps < 10, marcar exploratorio]
- **Sonda única:** [si no hay multi-sonda, declararlo]
- **Otras limitaciones:** [...]

## 14. Comparación rival

**Tabla A.3.5.**

| Criterio | Tesis (irrealismo operativo) | Rival 1 | Rival 2 | Rival 3 |
|---|---|---|---|---|
| A (anclaje) | sí | ... | ... | ... |
| B (multiescala) | sí | ... | ... | ... |
| C (admisión empírica) | EDI + C1-C5 | ... | ... | ... |
| D (traducibilidad B↔L3) | obligatoria | ... | ... | ... |
| E (caso ancla con datos) | sí | ... | ... | ... |
| F (alcance) | multidominio | ... | ... | ... |

[Discriminación pública: ventaja en al menos dos celdas. Si no, reformular.]

---

## Cierre del dossier

- **Conclusión sobre el caso:** [admitido como Nivel X / programático con criterio Y]
- **Trabajo futuro:** [extensiones planificadas]
- **Referencias cruzadas en el manuscrito:** [capítulos donde se discute]
```

---

## Casos completos disponibles en el repositorio

- **04 Energía:** dossier en `09-simulaciones-edi/04_caso_energia/` (overall_pass=True)
- **16 Deforestación:** dossier en `09-simulaciones-edi/16_caso_deforestacion/` (overall_pass=True, reproducibilidad verificada con World Bank en vivo)
- **20 Kessler:** dossier en `09-simulaciones-edi/20_caso_kessler/` (overall_pass=True)
- **27 Riesgo Biológico:** dossier en `09-simulaciones-edi/27_caso_riesgo_biologico/` (overall_pass=True)
- **30 Behavioral Dynamics:** dossier en `09-simulaciones-edi/30_caso_behavioral_dynamics/` (Nivel 3 weak, sonda `behavioral_attractor` segundo orden)

Cada uno tiene:
- `case_config.json` con parámetros y dates
- `src/{abm,ode,data,validate}.py` con implementación
- `outputs/metrics.json` con resultados
- `README.md` con análisis cualitativo

---

## Política de uso

1. **Modo demostrativo:** los catorce componentes son obligatorios.
2. **Modo programático:** componentes 1-3 (Q, X, sustrato) y 7-9 (atractores conjeturados, ¿pruebas?, predicción discriminante a buscar) son obligatorios. El resto son objetivos del programa de elevación.
3. **Auditoría:** un tercer investigador competente debe poder reproducir el dossier desde el case_config y los datos.

## Cierre

> El dossier no es burocracia: es la articulación operativa del filtro de admisión que distingue una tesis de un manifiesto. Cualquier categoría que entre al manuscrito sin dossier completo (en demostrativo) o sin criterio de elevación (en programático) está fuera del marco.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-11-auditoria-ontologica-como-protocolo"></div>

# Auditoría ontológica y diseño de investigación


## Tesis del capítulo

> La auditoría ontológica es un protocolo de nueve fases que examina cualquier categoría candidata bajo el filtro del dossier de anclaje y produce decisión trazable. Su criterio de cierre no es la satisfacción del autor sino la replicabilidad por tercero competente. Sin esta auditoría, la tesis sigue siendo programa filosófico; con ella, se convierte en programa de investigación reproducible.

## 1. Qué es una auditoría ontológica

> Una auditoría ontológica es el examen sistemático de una categoría, entidad, propiedad o nivel mediante el aparato formal y los criterios de legitimidad, con el fin de determinar su admisión, reformulación o retiro respecto a una pregunta `Q` con tolerancia explícita.

La auditoría se aplica a cualquier candidato: una categoría heredada (`mente`, `mercado`, `especie`), una unidad teórica propuesta (`atractor de integración corporal`, `módulo funcional X`), una clase modelística (`memoria de trabajo`), una entidad institucional (`Estado`).

## 2. Preguntas básicas de auditoría

Ante cualquier concepto C, la auditoría plantea diez preguntas estandarizadas:

1. ¿qué fenómeno pretende capturar?
2. ¿qué sustrato material lo instancia?
3. ¿qué variables lo componen?
4. ¿qué relaciones lo sostienen?
5. ¿qué nivel de análisis exige?
6. ¿qué evidencia lo apoya?
7. ¿qué predicciones permite?
8. ¿qué intervenciones orienta?
9. ¿qué se pierde si desaparece del modelo?
10. ¿qué se gana si se lo reemplaza por una estructura más fina?

Las respuestas se registran en el dossier de anclaje (capítulo 03-02 §3).

## 3. Protocolo de nueve fases

### Fase 1. Detección del recorte heredado

Identificar la categoría que ya opera en el lenguaje ordinario o disciplinar. Documentar contextos de uso, sinónimos cercanos, autores principales que la trabajan.

### Fase 2. Desustancialización inicial

Suspender la suposición de que C designa automáticamente una entidad simple. Tratar C como hipótesis de patrón estabilizado a verificar.

### Fase 3. Reconstrucción material

Buscar soportes, procesos, mecanismos, infraestructuras o prácticas que materialicen el fenómeno bajo C. Si no se encuentra ninguno, C es candidato a categoría sin anclaje y debe declararse como tal.

### Fase 4. Modelización basal

Aplicar μ y construir G = (V, E, W, T) sobre las variables identificadas en la Fase 3. Cada arista pasa criterio de admisión del capítulo 03-01 §4.3.

### Fase 5. Detección de patrones de orden superior

Buscar módulos, ciclos, acoplamientos, cuellos de botella, jerarquías o ensamblajes. Si los hay, construir H. Si las dependencias son binarias, no se postula H.

### Fase 6. Ensayo de compresión

Aplicar κ con procedimiento empírico del capítulo 03-04. Identificar dimensionalidad efectiva y atractores empíricos del sistema reducido.

### Fase 7. Ensayo de expansión

Si la compresión falla en alguna prueba de validación, aplicar ε en la subestructura responsable. Iterar hasta admisión o declaración de límite.

### Fase 8. Evaluación comparativa

Comparar el rendimiento del recorte material-relacional bajo el aparato contra al menos un rival explícito. Producir tabla de discriminación según método del capítulo 03-02 §9.

### Fase 9. Decisión ontológica local

Decidir el estatuto final de C respecto a Q:

- **patrón estabilizado admisible**: C se admite como compresión legítima, entra en S como categoría revisada;
- **función dependiente**: C designa función en un sistema más amplio, admisible como tal;
- **clase teórica**: C es construcción teórica útil bajo Q sin atractor empírico directo, admisible como categoría con anclaje teórico;
- **convención práctica**: C funciona como rótulo comunicativo sin pretensión ontológica, admisible con marca explícita de uso convencional;
- **etiqueta a revisar**: C tiene contenido pero su formulación actual es defectuosa, requiere reformulación;
- **etiqueta a abandonar**: C no satisface ningún criterio bajo ninguna Q razonable.

La decisión se documenta con justificación trazable a las fases anteriores.

## 4. Diseño de investigación para la tesis

### 4.1. Combinación metodológica obligatoria

La tesis requiere tres tipos de trabajo simultáneos:

- **análisis conceptual riguroso**: limpieza de vocabulario, definiciones de trabajo, separación de niveles;
- **comparación filosófica con posiciones rivales**: discriminación bajo criterios públicos, no contraste retórico;
- **estudios de caso estratégicos**: caso ancla canónico (modo demostrativo) y dominios adicionales (modo programático con criterios de elevación).

### 4.2. Por qué esta combinación funciona

**Tabla 3.3.1.**

| Trabajo | Función |
|---|---|
| Análisis conceptual | Permite limpiar vocabulario, separar niveles, fijar definiciones operativas |
| Comparación filosófica | Permite mostrar que la tesis no es intuición aislada sino intervención en debates reales con discriminación verificable |
| Estudios de caso | Permiten demostrar que la tesis produce rendimiento explicativo efectivo respecto a rivales explícitos |

Sin alguna de las tres patas, el manuscrito es incompleto: análisis sin comparación es solipsismo; comparación sin caso es académicamente vacía; caso sin análisis es ad hoc.

## 5. Cómo seleccionar casos

Un caso vale la pena si cumple cuatro condiciones:

1. usa categorías muy naturalizadas (susceptibles de auditoría);
2. exige paso entre escalas (probará la operación de κ y ε);
3. muestra claramente la diferencia entre reificación y compresión legítima;
4. admite construcción de dossier de anclaje completo o programático con criterio de elevación explícito.

Un caso que no cumple las cuatro queda fuera del manuscrito o se incluye con marca de incompletud.

## 6. Casos del manuscrito

### 6.1. Caso ancla canónico (modo demostrativo)

**Behavioral dynamics** (Warren 2006): tareas de raqueteo, equilibrio, frenado, locomoción. Datos públicos, ecuaciones ajustadas, predicciones cumplidas, intervenciones documentadas. Dossier completo en capítulo 05-05.

### 6.2. Casos en modo programático

**Tabla 3.3.2.**

| Caso | Por qué es candidato | Criterio de elevación a demostrativo |
|---|---|---|
| Mente, memoria, yo | Categorías altamente reificadas, exigen multiescalaridad | Construcción de tareas con datos cuantitativos donde atractores conductuales discriminen contra cognitivismo |
| Biología y ecología | Multiescalaridad biológica clásica, organización procesual | Identificación de atractores de regulación con bifurcaciones empíricas en datos publicados |
| Sistemas técnicos distribuidos | Compresión y expansión muy claras, intervención cotidiana | Construcción de modelo dinámico cuantitativo de sistema distribuido con predicción de fallo verificable |
| Instituciones, mercado, Estado | Espesor normativo e histórico, riesgo de hipóstasis | Identificación de atractores institucionales con bifurcaciones (crisis, refundación) y predicción discriminante contra individualismo o holismo |

Estos casos se desarrollan en capítulos 05-01 a 05-04 con marca explícita de modo programático y dossier parcial.

## 7. Indicadores de éxito del programa

El proyecto está metodológicamente bien armado si logra:

- usar la misma matriz en dominios heterogéneos sin variación arbitraria de criterios;
- producir distinciones nuevas y no triviales en al menos un dominio;
- justificar cuándo cambia de escala con regla pública;
- evitar reificaciones sin caer en nominalismo en cada dominio examinado;
- mostrar al menos una aplicación demostrativa donde la teoría mejora respecto a rivales con datos públicos.

El manuscrito actual cumple los cinco indicadores: el caso ancla canónico cumple el último explícitamente; los criterios y la auditoría cumplen los cuatro primeros estructuralmente.

## 8. Riesgos del diseño

### Riesgo 1. Convertir todos los casos en meras ilustraciones

Hay que evitar que los casos solo repitan la tesis. Deben ponerla a prueba. Antídoto: cada caso programático lleva criterio explícito de fallo (qué resultado lo desautorizaría) además de criterio de elevación.

### Riesgo 2. Elegir casos demasiado fáciles

Si solo se escogen ejemplos donde la conclusión ya parece obvia, la tesis no gana fuerza. Antídoto: el caso ancla canónico se eligió porque enfrenta directamente al rival más fuerte (modelos internos / control óptimo) en su mejor terreno.

### Riesgo 3. Perder el hilo común

Cada caso debe devolver algo al marco general. Antídoto: cada capítulo de aplicaciones cierra con sección `Lo que este caso devuelve a la tesis general` que articula el aporte específico al marco.

### Riesgo 4. Hipertrofia de la auditoría

La auditoría puede convertirse en burocracia que ahoga al fenómeno. Antídoto: cuando una auditoría se vuelve más larga que el fenómeno examinado, se reescribe.

## 9. Plantilla operativa del dossier

Para investigador externo que aplique el protocolo a un caso nuevo:

```markdown
# Dossier de anclaje: [Nombre del caso]

## 1. Pregunta Q
- Formulación φ:
- Tolerancia τ:
- Régimen R:
- Fecha de fijación:

## 2. Variables X
- Observables:
- Inferidas:
- Régimen de medición:

## 3. Sustrato material instanciante
[Descripción explícita]

## 4. Grafo G = (V, E, W, T)
[Estructura, criterios de admisión de aristas]

## 5. Hipergrafo H (si procede)
[Justificación]

## 6. Compresión κ propuesta
- Dimensionalidad efectiva d:
- Forma funcional del sistema reducido:
- Parámetros y unidades:

## 7. Topología dinámica
- Atractores:
- Repulsores:
- Bifurcaciones:

## 8. Validación
- Reproducción (varianza explicada, error medio):
- Generalización (condiciones no usadas para ajuste):
- Topología (preservación de atractores y bifurcaciones):
- Intervención (predicciones cumplidas o falladas):

## 9. Predicción discriminante
[Predicción específica que un rival no produce o produce peor]

## 10. Intervención discriminante
[Experimento que falsaría la propuesta]

## 11. Operador ε
[Protocolo de reapertura para regiones límite]

## 12. Traducción B↔L3
- Cada parámetro de L3 → variable de B
- Cada categoría de S → atractor de B

## 13. Limitaciones declaradas
[Régimen donde el modelo no se aplica]

## 14. Comparación rival

**Tabla 3.3.3.**

| Criterio | Modelo propuesto | Rival 1 | Rival 2 |
|---|---|---|---|
[...]
```

Esta plantilla se aplica al caso ancla canónico (capítulo 05-05) y se aplica parcialmente, marcada como tal, a los casos programáticos.

## 10. Diálogo con interlocutores

### 10.1. Bunge — método científico riguroso

Bunge (1972, *La investigación científica*, vol. 1, parte II) formula el ciclo *"problema → hipótesis → contrastación → teoría → aplicación"* como protocolo iterativo. La auditoría ontológica de este capítulo es esa estructura aplicada a **categorías filosóficas y científicas**, no a hechos puntuales. Bunge queda como referente metodológico principal: la diferencia es que aquí el "problema" es siempre la legitimidad de una compresión, y la "contrastación" exige operacionalización empírica vía EDI.

### 10.2. Bechtel — descomposición funcional

Bechtel y Richardson (1993/2010, *Discovering Complexity*, cap. 1, p. 17) sistematizan la heurística de descomposición y localización: *"the strategies of decomposition and localization treat the system as if it were a physical machine and then attempt to identify the parts that perform specific operations"*. La auditoría incorpora esta descomposición pero la **disciplina con el filtro del dossier**: no toda descomposición funcional es admisible; debe pasar la batería de criterios. Bechtel deja la decisión de qué cuenta como "operación específica" relativamente abierta; la tesis lo cierra con el dossier de 14 componentes.

### 10.3. Craver — niveles mecanicistas

Craver (2007, *Explaining the Brain*, cap. 4, p. 152) define el criterio de **mutual manipulability**: *"X is constitutively relevant to S's φ-ing iff X is part of S, and... if (a) intervening to manipulate X gives rise to a change in φ, and (b) intervening to manipulate φ gives rise to a change in X"*. La auditoría incorpora este criterio en Fase 5 (detección de patrones de orden superior) y Fase 6 (ensayo de compresión): un nivel se admite solo si las relaciones constitutivas son mutuamente manipulables empíricamente, no nominalmente.

### 10.4. Mitchell — pluralismo integrativo

Mitchell defiende coexistencia de modelos parciales para fenómenos complejos. La auditoría la admite con condición: cada modelo parcial debe llevar dossier con su Q específica. Pluralismo no es mezcla; es articulación bajo criterios.

### 10.5. Ladyman y Ross — realismo estructural

Ladyman y Ross sugieren tomar la estructura como ontología fundamental. La auditoría adopta estructura como objeto del análisis, pero se compromete con sustrato material como ontología base: la estructura es estructura **del** sustrato, no estructura sin sustrato.

## 11. Resultado metodológico

Con esta auditoría, la tesis se presenta no solo como respuesta a una pregunta metafísica sino como técnica filosófica para examinar conceptos complejos. El protocolo es explícito, replicable y sometido a criterios de fallo. Eso es lo que separa un programa de investigación de una posición doctrinal.

## 12. Cierre

> La filosofía propuesta no pregunta solo qué existe; pregunta también cómo recortar lo existente sin convertir un nombre útil en sustancia imaginaria ni una complejidad real en niebla conceptual. La auditoría ontológica es la técnica que ejecuta esa exigencia con trazabilidad pública.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-12-operacionalizacion-de-kappa-via-edi"></div>

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


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-13-validacion-logica-formal-con-st"></div>

# Validación lógica formal con ST

## Función

Reporte sistemático de la validación de la lógica interna del marco mediante el lenguaje formal **ST** (`@stevenvo780/st-lang` v3.2.2). La suite cubre la asimetría L1↔B↔L3↔S, la cadena de operadores formales, las trece condiciones de `overall_pass`, la discriminación contra los rivales identificados, los niveles 0-5 del paisaje de emergencia, la falsabilidad del marco, la coherencia modal, la convivencia paraconsistente con Wolfram, y los puntos sustantivos del marco filosófico: temporalidad y causalidad, definición técnica de "pre-ontológico", marco tripartito general, naturalismo metafísico moderado, distinción κ-pragmática vs κ-ontológica, dimensión normativa deóntica, asimetría a través de los tres marcos, stress test de falsabilidad, paraconsistencia del corpus multiescala, y modal del marco tripartito.

**Fuente de verdad ejecutable:** `08-consistencia-st/theories/00-22.st` y reporte automatizado en `08-consistencia-st/reports/ultimo-reporte.md`.

**Ejecución:**

```bash
cd 08-consistencia-st
npm install
npm run st:check
```

## Hallazgos críticos detectados durante la validación

La suite extendida **detectó cuatro problemas reales** que la formulación V4 del manuscrito no anticipaba. Todos se resuelven aquí y se propagan al cuerpo argumental.

### Hallazgo ST-1 (V4 conservado): asimetría L1↔B↔L3↔S no es expresable como axiomas universales proposicionales

Refinada a existenciales en lógica de primer orden (cap 02-04 §8.0). Test 5 de la nueva T19 confirma operatividad inter-escala: existen modelos donde B(qubit), B(cumulo), F(qubit), F(cumulo) y S(qubit), S(cumulo) coexisten satisfactoriamente. La asimetría es invariante a la escala bajo la formulación FOL existencial.

### Hallazgo ST-2 (V4 conservado): necesidad modal requiere axioma T

Sistema modal **al menos T (KT)** declarado en cap 02-01. T22 confirma: en `modal.k` puro no se valida `□P → P` (axioma T no asumido). La declaración explícita en cap 02-01 cierra el hueco.

### Hallazgo ST-3: la respuesta a Kim sobre downward causation requiere construcción argumental, no solo declaración

**Detección (T13 Test 4):** la primera formulación afirmaba *"si downward es constitución, Kim no aplica"* como implicación directa. La verificación ST mostró que la implicación `((C ∧ ¬V) ∧ (K → (V → S))) → ¬S` **NO es válida** sin pasos intermedios.

**Refinamiento ejecutado:** la respuesta correcta es por modus tollens vacuo. Si C → ¬V (constitución no es causación) y K dice `(V → S)`, entonces de `¬V` y `(V → S)` no se infiere S; el argumento de Kim sobre sobredeterminación queda neutralizado **por ausencia del antecedente** (V), no por refutación del consecuente (S).

**Implicación para el manuscrito:** cap 02-05 §2.4 ya articula esto correctamente. La verificación ST formaliza el argumento.

### Hallazgo ST-4: la generalidad del marco NO se infiere desde los casos del corpus

**Detección (T15 Test 2):** `analyze {J} → G` (de "casos justifican" inferir "marco general") es **inferencia NO VÁLIDA**. Esto es exactamente lo que el cap 06-01 §5 afirma: los 40 casos NO son la tesis; son justificación operativa parcial.

**Implicación:** la verificación ST confirma operativamente que el marco general se sostiene por su **estructura interna coherente** (T15 Test 4: `(G → S) ∧ G → S` válida), no por inducción sobre casos. La advertencia contra el inductivismo del manuscrito está formalmente respaldada.

### Hallazgo ST-5: los 3 marcos NO colapsan unos sobre otros

**Detección (T15 Test 5):** los contramodelos de `O → E`, `E → M`, `M → O` **se encuentran**. Esto confirma que los 3 marcos (ontológico, epistemológico, metodológico) son **lógicamente independientes** entre sí: ninguno se reduce a otro.

**Implicación:** la afirmación del cap 06-01 §5 de que el aporte es **triple sustantivo** (no solo metodológico, no solo ontológico, no solo epistemológico) está formalmente verificada.

### Hallazgo ST-6: el naturalismo metafísico moderado NO se demuestra desde dentro

**Detección (T16 Test 6):** countermodel para N (naturalismo) **encontrado**. Esto confirma que el naturalismo es **compromiso de partida**, no conclusión deductiva, exactamente como el cap 02-01 §0.1 declara.

**Implicación:** la honestidad metodológica del manuscrito está formalmente verificada: la tesis NO presume que el naturalismo es una verdad demostrada; lo declara como compromiso filosófico.

## Resumen de la suite refactorizada

**Tabla A.11.1.**

| Teoría | Perfil ST | Foco | Estado |
|--------|-----------|------|--------|
| 00 — Núcleo ontológico | classical.propositional | 4 invariantes + naturalismo + rechazo de 3 rivales | ✅ |
| 01 — Criterios de legitimidad | classical.propositional | 9 condiciones derivan G y H | ✅ |
| 02 — Debates y límites | classical.propositional | Anti-dualismo, anti-reduccionismo, anti-emergencia | ✅ |
| 03 — Text layer tesis | classical.propositional | 3 claims con confianza > 0.94 | ✅ |
| 04 — Text layer bibliografía | classical.propositional | 3 claims con confianza > 0.90 | ✅ |
| 05 — Asimetría L1↔B↔L3↔S | classical.first_order | Refinamiento a existenciales | ✅ |
| 06 — Operadores y circularidad | classical.propositional | μ→G→H→K→E sin atajos viciosos | ✅ |
| 07 — overall_pass 13 condiciones | classical.propositional | Colectivamente necesarias | ✅ |
| 08 — Discriminación rivales | classical.propositional | 14 rivales discriminados | ✅ |
| 09 — Niveles 0-5 paisaje | classical.propositional | Excluyentes con axiomas explícitos | ✅ |
| 10 — Falsabilidad | classical.propositional | 5 condiciones por modus tollens | ✅ |
| 11 — Modal coherencia | modal.k | Necesidad requiere axioma T | ⚠️ → ✅ |
| 12 — Paraconsistencia Wolfram | paraconsistent.belnap | Coexistencia sin trivialización | ✅ |
| **13 — Temporalidad y causalidad** | classical.propositional | B-series + Woodward + constitución vs Kim | ⚠️ → ✅ |
| **14 — Pre-ontológico genético** | classical.first_order | "Pre" simondoniano definido | ✅ |
| **15 — Tres marcos generales** | classical.propositional | Independencia + no inductivismo | ⚠️ → ✅ |
| **16 — Naturalismo + rivales** | classical.propositional | Naturalismo excluye 5 rivales metafísicos | ✅ |
| **17 — κ-pragmática vs κ-ontológica** | classical.propositional | 3 criterios; ningún caso actual los cumple | ✅ |
| **18 — Deóntica normativa** | deontic.standard | Validez/efectividad/legitimidad coherentes | ✅ |
| **19 — Asimetría tres marcos** | classical.first_order | Asimetría invariante a la escala | ✅ |
| **20 — Stress test falsabilidad** | classical.propositional | 8 condiciones de fracaso falsables | ✅ |
| **21 — Belnap corpus multiescala** | paraconsistent.belnap | Honestidad metodológica sin colapso | ✅ |
| **22 — Modal marco tripartito** | modal.k | Invariantes necesarios + sondas contingentes | ✅ |
| **23 — Modal T (KT) bajo hipótesis** | modal.k + axioma T explícito | Cierre formal de la declaración "AT LEAST T" del cap 02-01 | ✅ |

24 teorías ejecutadas, 6 hallazgos críticos detectados durante la verificación, todos resueltos. T23 cierra la consistencia entre el sistema modal declarado en cap 02-01 (KT) y el verificado por la suite (modal.k + axioma T como hipótesis explícita, lógicamente equivalente a modal.kt).

## Pruebas duras pasadas por la suite refactorizada

### T13 — Temporalidad + causalidad responde a Kim

- **B-series + flecha termodinámica satisfacibles juntas:** ✅
- **EDI como `do`-test woodwardiano:** válido
- **Constitución (Craver) ≠ causación (Kim):** verificado por contramodelo de `C → V`
- **Argumento de Kim neutralizado por modus tollens vacuo:** ✅ T13 Test 4
- **Eternalismo bloque rechazado:** contramodelo encontrado
- **Irreversibilidad κ↔ε es termodinámica, no axioma adicional:** ✅

### T14 — Definición técnica de "pre-ontológico"

- **Estructura pre-ontológica satisfacible con definición simondoniana:** ✅
- **"Pre" temporal puro rechazado:** contramodelo encontrado
- **Génesis del individuo:** instanciación universal válida
- **Regularidad estadística NO es pre-ontológica:** verificado

### T15 — Tres marcos generales independientes

- **Tres marcos colectivamente la tesis:** ✅
- **Generalidad NO se infiere desde casos:** **Hallazgo ST-4 confirmado**
- **Estructura interna coherente necesaria:** modus tollens válido
- **Tres marcos lógicamente independientes:** **Hallazgo ST-5 confirmado** (ninguno colapsa sobre otros)
- **Coexistencia mutua coherente:** satisfacible

### T16 — Naturalismo metafísico moderado

- **Naturalismo excluye dualismo, idealismo, emanacionismo, panpsiquismo, creacionismo:** ✅ los 5
- **Conjunción naturalismo + rival es contradicción:** ✅
- **Naturalismo NO decide entre interpretaciones realistas QM:** ✅
- **Copenhagen instrumentalista pura SÍ se rechaza:** ✅
- **Naturalismo es compromiso de partida, no conclusión:** **Hallazgo ST-6 confirmado** (countermodel para N)

### T17 — κ-pragmática vs κ-ontológica

- **κ-ontológica requiere 3 criterios simultáneos:** ✅
- **κ-pragmática NO implica κ-ontológica:** verificado
- **Ningún caso actual cumple los 3 criterios:** ✅
- **Distinción no trivial:** modelos donde solo se da P existen
- **Colapso κ-pragmática = κ-ontológica rechazado:** contramodelo encontrado

### T18 — Dimensión normativa deóntica

- **Validez normativa = `□C` (cumplimiento necesario):** coherente
- **Efectividad = `<>C` (cumplimiento posible):** coherente
- **Deber = (validez + efectividad), no sustancia:** validado
- **Validez compatible con incumplimiento ocasional:** satisfacible
- **Naturalismo ético no-reduccionista coherente:** ✅

### T20 — Stress test de falsabilidad

- **Cada una de 8 falsaciones refuta tesis:** ✅
- **Tesis NO es tautología:** countermodel encontrado
- **Tesis NO es contradicción:** modelo encontrado
- **Estado actual: corpus NO satisface las falsaciones críticas:** satisfacible
- **Modus tollens válido para cualquier falsación:** ✅

### T21 — Belnap: honestidad metodológica sin colapso

- **Caso 30 sufre circularidad Y produce EDI 0.262:** coexisten en Belnap
- **p-value 24% mal calibrado Y umbrales EDI robustos:** coexisten
- **Sondas depuradas post-hoc Y específicas (V4-01):** coexisten
- **AUC interno Y ausencia de validación externa:** coexisten
- **Honestidad metodológica NO colapsa la tesis:** ✅

### T22 — Modal del marco tripartito

- **4 invariantes declarados como necesarios:** satisfacibles
- **Sondas específicas son contingentes:** satisfacible
- **Regla K (distribución):** válida
- **`[]M → M` requiere axioma T:** confirmado (no en modal.k puro)

## Limitaciones de la validación ST

### Lo que ST sí valida

- Coherencia interna de los axiomas declarados (ausencia de contradicción).
- Validez de inferencias específicas.
- Detección de falacias formales conocidas.
- Existencia de contramodelos para implicaciones no válidas.
- **Independencia lógica de los 3 marcos generales** (T15).
- **Distinción operativa entre constitución y causación** (T13).
- **Naturalismo como compromiso, no conclusión** (T16).
- **Distinción κ-pragmática vs κ-ontológica con 3 criterios operativos** (T17).
- **Coherencia de la dimensión normativa deóntica** (T18).
- **Coexistencia de honestidades metodológicas en Belnap** (T21).

### Lo que ST NO valida

1. **ST no valida que los axiomas sean verdaderos en el mundo.** Solo certifica consistencia interna.
2. **ST no detecta axiomas vacíos.** Un sistema puede ser consistente y vacío.
3. **ST no captura la dinámica acoplada del aparato.** El motor ABM+ODE es objeto computacional con dinámica continua que ST no representa.
4. **ST no audita la calibración empírica de la métrica.** El p-value del 24% es problema empírico que ST no detecta.
5. **La cobertura de la suite es representativa, no exhaustiva.** 23 teorías cubren los puntos críticos identificados; no garantiza completitud.
6. **ST no sustituye revisión humana experta.** El comité doctoral debe leer los axiomas declarados y juzgar si son los correctos.

## Política de uso

La validación ST debe leerse como certificación de coherencia interna del marco, no como certificación de validez filosófica o empírica. Las dos validaciones complementarias son:

- **validez empírica:** corpus EDI inter-dominio + inter-escala (cap 09 + 05-06 + apéndices técnicos de tablas crudas), con limitaciones documentadas en las auditorías iterativas;
- **validez filosófica:** revisión por pares humanos competentes en filosofía de la mente, ontología analítica y ciencias de la complejidad (deuda externa pendiente).

Esta declaración cubre los puntos sustantivos del marco filosófico (temporalidad, causalidad, pre-ontológico genético, naturalismo declarado, κ-pragmática/ontológica, dimensión normativa, asimetría multiescalar).

## Conclusión

La validación lógica formal con ST confirma que los cierres conceptuales sustantivos del marco son lógicamente coherentes. Los hallazgos críticos detectados durante la verificación (ST-3, ST-4, ST-5, ST-6) refuerzan la honestidad metodológica del manuscrito: confirman operativamente que la generalidad del marco se sostiene por estructura interna y no por inducción sobre casos, que el naturalismo es compromiso de partida y no conclusión, y que la respuesta a Kim sobre downward causation requiere argumentación constitutiva específica.

Las teorías iniciales (T0–T12) verifican la lógica metodológica del marco; las teorías sustantivas adicionales (T13–T22) cubren los conceptos filosóficos que un comité humanista exigiría articulados; T23 cierra la consistencia formal entre el sistema modal declarado en el cap 02-01 (KT) y el sistema modal.k base de la biblioteca de validación.

## Lectura cruzada

- Teorías ST originales: `08-consistencia-st/theories/00-12.st`.
- Teorías sustantivas del marco: `08-consistencia-st/theories/13-22.st`.
- Reporte automatizado: `08-consistencia-st/reports/ultimo-reporte.md`.
- Capítulos donde los conceptos validados se articulan: 02-01 (ontología, naturalismo, pre-ontológico, observador), 02-02 (epistemología general), 02-04 (asimetría), 02-05 (tiempo y causalidad), 02-06 (ética), 03-01 (aparato), 06-01 (cierre).
- Auditoría de vacíos estructurales: `Auditoria_V5_Vacios_Estructurales.md`.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-14-etica-de-investigacion-y-gobernanza-de-datos"></div>

# Ética de investigación y gobernanza de datos

## Función

Capítulo metodológico que documenta la política de manejo de datos del corpus EDI multidominio, las consideraciones éticas específicas por caso, la gobernanza de datos abiertos vs. propietarios, la política de reproducibilidad, y la declaración explícita de co-autoría con inteligencia artificial. Su existencia responde a la exigencia institucional de la Universidad de Antioquia y al estándar internacional vigente (COPE 2023, JAMA 2023, EU AI Act 2024).

## 1. Naturaleza de los datos del corpus

El corpus EDI consta de **30 casos**. Por su naturaleza de datos, se clasifican en cuatro categorías:

**Tabla 3.5.1.**

| Categoría | Cuenta | Casos | Implicaciones éticas |
|-----------|-------:|-------|----------------------|
| Datos públicos secundarios verificables | 22 | Energía, Deforestación, Kessler, Riesgo Bio, Microplásticos, Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad, Finanzas, Salinización, Justicia, Starlink, Fuga cerebros, Clima, Contaminación, Océanos, Acidificación, Acuíferos | Mínimas: solo trazabilidad de fuente y cumplimiento de licencias |
| Datos públicos con sensibilidad media | 2 | Conciencia (proxy especulativo), IoT (telemetría agregada) | Bajas: agregación previa anula identificación |
| Datos sintéticos generados con parámetros publicados | 4 | Caso 30 (behavioral dynamics), Erosión, Paradigmas, los 3 controles de falsación | Ninguna: sin sujetos humanos directos |
| Datos humanos directos (futuro) | 0 actualmente / 1 planeado | Caso 30 elevado a LoE = 4 | **Significativas:** requiere aval CEI |

**Implicación clave:** en la versión actual del manuscrito (2026-04-28), **no hay manejo de datos personales identificables ni experimentación con sujetos humanos**. Por tanto, los 30 casos no exigen aval previo del Comité de Ética en Investigación (CEI). El aval se solicitará **únicamente** cuando el caso 30 incorpore datasets de captura de movimiento humano.

## 2. Política por caso del corpus

### 2.1. Casos con datos públicos secundarios

**Política:** trazabilidad completa de la fuente, cita de la institución que publica, cumplimiento de la licencia de cada dataset, reproducción mediante URLs documentadas o caché versionado.

**Fuentes principales y sus licencias:**

**Tabla 3.5.2.**

| Fuente | Licencia | Casos asociados |
|--------|----------|-----------------|
| World Bank Open Data | CC BY 4.0 | 16 Deforestación, 18 Urbanización, 27 Riesgo Biológico, 21 Salinización, 28 Fuga cerebros, 22 Fósforo |
| Our World in Data (OWID) | CC BY 4.0 | 04 Energía, 05 Epidemiología, 14 Postverdad, 13 Políticas |
| Open Power System Data (OPSD) | CC0 / dominio público | 04 Energía |
| CelesTrak (TLE) | dominio público | 20 Kessler, 26 Starlink |
| Jambeck et al. 2015 (publicado en *Science*) | uso secundario académico | 24 Microplásticos |
| Wikipedia API estadísticas | dominio público | 15 Wikipedia |
| Yahoo Finance / OECD | uso secundario académico | 09 Finanzas |
| OpenSky Network | CC BY-NC 4.0 | 11 Movilidad aérea |

**Trazabilidad:** cada caso documenta su fuente exacta en `09-simulaciones-edi/<caso>/case_config.json` y en su README específico.

### 2.2. Casos con datos sintéticos

**Política:** parámetros publicados en literatura revisada por pares + semilla determinística (`seed=42` por defecto) + reproducibilidad bit-a-bit verificada.

**Casos:**

- **Caso 30 (behavioral dynamics):** datos sintéticos generados con la ecuación completa de Fajen y Warren (2003) con cambios discretos de meta y ruido perceptivo realista. Los parámetros (b=3.25, k_g=7.50, c1=0.40, c2=0.40) son los publicados en la fuente original. La elección de generar datos sintéticos del sistema completo (no de la sonda EDI simplificada) evita la circularidad ABM ≡ ODE.
- **Controles de falsación (06, 07, 08):** ruido puro, random walk y estado oculto respectivamente, generados con semilla fija para reproducir la condición de falsación.
- **Casos null especulativos (02 Conciencia, 23 Erosión):** datos especulativos clasificados explícitamente como LoE = 1.

**Limitación reconocida:** los datos sintéticos no sustituyen datos reales. La tesis declara explícitamente esta limitación y compromete elevación del caso 30 a LoE = 4 con datos humanos como deuda priorizada.

### 2.3. Caso 30 elevado a LoE = 4 (ruta planeada)

Cuando el caso 30 se eleve con datos humanos:

**Datasets candidatos:**

**Tabla 3.5.3.**

| Dataset | Institución | Naturaleza | Licencia / Acceso |
|---------|-------------|------------|-------------------|
| VENLab (Brown University) | Warren Lab | Captura de movimiento en steering tasks | Acceso académico previa solicitud |
| WALK-MS Boston | Boston University | Locomoción humana en interiores | Académico, disponible |
| OpenLocomotionData | Consorcio académico | Locomoción dirigida múltiples laboratorios | Open Access bajo CC BY 4.0 |
| MoCap CMU | Carnegie Mellon | Captura general | Académico, disponible |

**Procedimiento ético:**

1. solicitud formal al laboratorio de origen del dataset, declarando uso académico secundario;
2. verificación de que el dataset original tenía consentimiento informado de participantes y permite reuso académico;
3. radicación de protocolo de investigación ante el **Comité de Ética en Investigación de la Universidad de Antioquia** (CEI sede Medellín) con justificación de reuso secundario;
4. cumplimiento de Ley 1581 de 2012 (Colombia) sobre protección de datos personales: en datos secundarios anonimizados, la ley se cumple manteniendo la anonimización del dataset de origen sin re-identificación;
5. declaración del cumplimiento en el manuscrito final;
6. archivado de la documentación del proceso ético en `Bitacora/`.

**Hito condicional:** la elevación del caso 30 al nivel demostrativo con datos humanos no se ejecutará sin el aval CEI documentado.

## 3. Gobernanza de datos: abiertos vs. propietarios

**Compromiso institucional:** todos los datos primarios usados en el corpus son **abiertos** o **académicos con reuso permitido**. No se usan datos propietarios ni datos comerciales restringidos.

**Caché reproducible:** cada caso del corpus mantiene caché de los datos descargados en su carpeta `data_cache/` para garantizar reproducción aún si la fuente original cambia. La política de caché:

- caché versionado con fecha de descarga;
- hash SHA-256 verificable;
- compromiso de **no modificar el caché** una vez establecido;
- si la fuente original se actualiza, se anota en el log de caso pero el caché se preserva para reproducir el resultado publicado.

**Trazabilidad histórica:** la carpeta `Bitacora/` documenta cada hito relevante de adquisición y procesamiento de datos.

## 4. Reproducibilidad

**Compromiso público:**

- código completo del aparato EDI publicado en repositorio (`09-simulaciones-edi/`);
- documentación de dependencias en `requirements.txt`;
- entorno aislado documentado (`.venv`, Docker disponible);
- semillas deterministas (`seed=42`) en todos los casos donde la estocasticidad es intencional;
- validación de determinismo: 29/29 casos pasan reproducibilidad bit-a-bit con semilla fija;
- los `metrics.json` de cada caso son la fuente de verdad numérica del manuscrito.

**Política de archivo a largo plazo:** antes de la sustentación pública, depósito del repositorio en Zenodo o equivalente con DOI permanente.

## 5. Declaración de co-autoría con inteligencia artificial

### 5.1. Marco normativo

La declaración se ajusta a:

- **COPE (Committee on Publication Ethics).** Posición de febrero 2023: las herramientas de IA no pueden ser autoras (no asumen responsabilidad), pero su uso debe declararse explícitamente.
- **JAMA Network (2023).** Política editorial: los autores humanos son responsables del contenido completo aún si fueron asistidos por IA; la asistencia de IA debe declararse en métodos.
- **Universidad de Antioquia.** Política institucional vigente al momento del depósito, que se consultará explícitamente con la Vicerrectoría de Investigación antes de la sustentación.
- **EU AI Act (2024).** Aunque Colombia no está bajo jurisdicción europea, el Act es referencia internacional sobre transparencia y declaración del uso de IA en producción intelectual.

### 5.2. Rol específico de la IA en esta tesis

Anthropic Claude (Opus 4.7) operó como **instrumento de implementación bajo dirección humana**, equivalente epistémico a un software estadístico avanzado. Específicamente:

**Tabla 3.5.4.**

| Tarea | Rol IA | Rol humano |
|-------|--------|------------|
| Tesis ontológica del irrealismo operativo | — | Jacob Agudelo (concepto original) |
| Conjetura del cierre operativo κ | — | Jacob Agudelo |
| Aparato formal (μ, G, H, κ, ε) | refactorización de redacción | Jacob Agudelo (concepto), Steven Vallejo (formalización) |
| Diseño del protocolo C1-C5 | sugerencias de redacción | Jacob Agudelo + Steven Vallejo |
| Implementación del corpus EDI computacional | asistente de codificación | Steven Vallejo (autoría técnica) |
| Selección de los 30 casos del corpus | sugerencias acotadas | Jacob Agudelo + Steven Vallejo |
| Sondas ODE específicas | implementación bajo guía | Steven Vallejo |
| Ejecución del corpus y producción de `metrics.json` | ejecución supervisada | Steven Vallejo |
| Redacción del manuscrito | asistencia activa de redacción | Jacob Agudelo + Steven Vallejo (revisión y aprobación) |
| Decisiones ontológicas, epistemológicas, metodológicas finales | — | autores humanos |
| Auditorías doctorales internas | redacción asistida | autores humanos (revisión final) |

### 5.3. Lo que la IA no hizo

- no decidió ninguna tesis ontológica, epistemológica o metodológica fundamental;
- no produjo ningún resultado del corpus EDI sin revisión humana de los `metrics.json`;
- no eligió las posiciones rivales del capítulo 04-01;
- no generó la conjetura κ ni la métrica EDI;
- no interpretó los resultados del corpus en términos filosóficos sin revisión humana.

### 5.4. Responsabilidad

La responsabilidad académica completa del manuscrito reside en los autores humanos: Jacob Agudelo (autoría principal) y Steven Vallejo Ortiz (colaborador técnico). La IA es declarada herramienta, no autora.

## 6. Limitaciones honestas en gobernanza

- **Datos cacheados:** algunos casos del corpus dependen de fuentes con políticas de actualización que pueden cambiar; el caché protege la reproducibilidad pero no garantiza acceso futuro a datos vivos. La tesis acepta esta limitación.
- **Versiones de software:** las dependencias en `requirements.txt` están pineadas a versiones específicas. Cambios futuros en bibliotecas pueden requerir adaptación. El compromiso es mantener compatibilidad documentada por al menos 5 años post-defensa.
- **Datos humanos pendientes:** el caso 30 elevado a LoE = 4 sigue siendo deuda; la política ética está documentada para ese momento, pero la ejecución no ha ocurrido al cierre de esta versión.
- **Co-autoría con IA en tesis doctoral:** la política institucional de la Universidad de Antioquia sobre IA en producción de tesis está en evolución (2024–2026). El manuscrito se ajustará a la versión vigente al momento del depósito; los autores se comprometen a actualizar esta declaración si la política cambia.

## 7. Política de errores y correcciones

**Compromiso público:** si tras la sustentación se detecta error en datos, código o cálculo del corpus, los autores se comprometen a:

- publicar erratum en el repositorio público con fecha y naturaleza del error;
- recalcular las cifras afectadas;
- revisar si el error afecta conclusiones del manuscrito;
- en caso de impacto material, publicar versión corregida con nota de modificación.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---


<div id="parte-3-evidencia"></div>

# Parte III — Evidencia empírica


<div id="capitulo-15-criterios-de-admision-de-aplicaciones"></div>

# Criterios de admisión de aplicaciones


## Tesis del capítulo

> Una aplicación entra en modo demostrativo solo si presenta dossier completo de anclaje con datos públicos, ecuaciones ajustadas, predicciones cumplidas, intervenciones documentadas y comparación rival con discriminación verificable. Una aplicación entra en modo programático si presenta conjetura articulada con criterio explícito de elevación a demostrativo: qué datos hacen falta, qué rival se enfrentaría, qué predicción discriminante se buscaría. Cualquier capítulo de aplicación se etiqueta inequívocamente con uno de los dos modos.

## 1. Modo demostrativo: condiciones de admisión

Una aplicación se admite en modo demostrativo si y solo si su dossier de anclaje (capítulo 03-02 §3) está completo en sus catorce componentes con contenido sustantivo:

1. **Pregunta Q fechada** con tolerancia y régimen de medición explícitos;
2. **Variables X** operacionalizadas con régimen R;
3. **Sustrato material instanciante** descrito;
4. **Grafo G** con criterios de admisión de aristas verificados por intervención;
5. **Hipergrafo H** si procede, con justificación de la no-reducibilidad a pares;
6. **Compresión κ** con dimensionalidad efectiva empíricamente justificada;
7. **Atractores, repulsores, bifurcaciones** identificados en datos;
8. **Pruebas de validación**: reproducción dentro de τ, generalización fuera del entrenamiento, preservación topológica, intervención discriminante;
9. **Predicción discriminante** contra rival explícito;
10. **Intervención discriminante** que falsaría la propuesta si se ejecuta y produce resultado contrario;
11. **Operador ε** con protocolo de reapertura;
12. **Traducción B↔L3** completa: cada parámetro de L3 se traduce a variable de B;
13. **Limitaciones declaradas** con régimen de no aplicabilidad;
14. **Comparación rival** con tabla de discriminación.

Un componente vacío o decorativo invalida la admisión en modo demostrativo. La aplicación pasa a modo programático con la marca correspondiente o queda fuera.

## 2. Modo programático: condiciones de admisión

Una aplicación se admite en modo programático si presenta:

1. **Pregunta Q candidata** con formulación explícita (puede no estar fechada);
2. **Esbozo de variables X** con indicación de régimen de medición plausible;
3. **Sustrato material instanciante** descrito en términos generales;
4. **Esbozo de grafo** con dependencias plausibles;
5. **Conjetura de κ** con dimensionalidad esperada (sin demostración);
6. **Atractores conjeturados** con argumento plausible;
7. **Criterio de elevación a demostrativo**: qué datos cuantitativos harían falta, qué rival se enfrentaría, qué predicción discriminante se buscaría;
8. **Diálogo bibliográfico** con interlocutores principales del dominio;
9. **Limitación honesta**: el modo programático no demuestra; conjetura.

La marca `MODO PROGRAMÁTICO` debe aparecer en el primer párrafo del capítulo y en el cierre.

## 3. Por qué la distinción es importante

### 3.1. Honestidad académica

Una tesis que presenta como demostraciones lo que son conjeturas se debilita en defensa oral. Un evaluador competente detecta inmediatamente la asimetría entre caso ancla y dominios adicionales. Mejor declararla.

### 3.2. Trazabilidad del programa

La distinción permite que la hoja de ruta (capítulo 06-03) priorice exactamente qué dominios necesitan trabajo demostrativo y en qué orden. Sin la distinción, la tesis se queda en una nube uniforme de aplicaciones todas igual de creíbles, todas igual de inverificadas.

### 3.3. Vigilancia contra sustitución nominal

Una aplicación que solo renombra el fenómeno con vocabulario del marco sin producir predicción discriminante es candidata a sustitución nominal. La obligación de criterio de elevación obliga a articular la diferencia.

## 4. Inventario de aplicaciones del manuscrito

### 4.1. Caso ancla canónico (modo demostrativo)

**Tabla 5.0.1.**

| Capítulo | Tema | Estado |
|---|---|---|
| 05-05 | Behavioral dynamics: locomoción, obstáculos, frenado, raqueteo, equilibrio | DEMOSTRATIVO con dossier completo (Warren 2006, Fajen y Warren 2003, Yilmaz y Warren 1995, Foo et al. 2000, Sternad et al. 2001) |

### 4.2. Aplicaciones en modo programático

**Tabla 5.0.2.**

| Capítulo | Tema | Estado | Criterio de elevación |
|---|---|---|---|
| 05-01 | Mente, memoria, yo | PROGRAMÁTICO | Tareas cognitivas con datos cuantitativos donde atractores conductuales discriminen contra cognitivismo simbólico |
| 05-02 | Biología y ecología | PROGRAMÁTICO | Atractores de regulación con bifurcaciones empíricas en datos publicados; rival principal: reduccionismo molecular o holismo ecológico inflado |
| 05-03 | Sistemas técnicos distribuidos | PROGRAMÁTICO | Modelo dinámico cuantitativo de sistema distribuido con predicción de fallo verificable; rival: arquitectura sin dependencias dinámicas |
| 05-04 | Instituciones, mercado, Estado | PROGRAMÁTICO | Atractores institucionales con bifurcaciones en datos históricos; rival: individualismo metodológico o holismo trascendental |

## 5. Política de extensión

### 5.1. Cuándo agregar aplicaciones

Una aplicación nueva se agrega al manuscrito solo si pasa al menos a modo programático con criterios de los §1-2 de este capítulo. No se admiten capítulos `interesantes` sin estructura.

### 5.2. Cuándo elevar de programático a demostrativo

Una aplicación programática se eleva a demostrativa cuando se cumplen sus criterios de elevación específicos y se produce dossier completo. La elevación se documenta con fecha y se actualiza el inventario.

### 5.3. Cuándo retirar

Una aplicación se retira si:

- en modo demostrativo, el dossier falla en alguna prueba de validación y la falla no se subsana;
- en modo programático, el criterio de elevación se intentó y produjo evidencia contraria a la conjetura;
- el rival principal del dominio absorbe la propuesta sin diferencia discriminante.

El retiro se documenta como deuda explícita en el capítulo 06-01.

## 6. Criterios uniformes de evaluación por aplicación

Cada aplicación, sea demostrativa o programática, debe responder cinco preguntas en su capítulo:

1. **¿Qué pregunta Q se trata?** Formulación explícita.
2. **¿Qué patrón material-relacional se conjetura?** Atractor candidato.
3. **¿Qué rival se enfrenta?** Posición específica con criterios.
4. **¿Qué predicción discriminante se ofrece?** Para demostrativo: cumplida. Para programático: a buscar.
5. **¿Qué se gana respecto al lenguaje ordinario?** Para demostrativo: con datos. Para programático: con argumento.

Sin las cinco respuestas, el capítulo se reescribe.

## 7. Diferencia con presentaciones laxas

Muchas tesis filosóficas presentan aplicaciones como ilustraciones afines a la tesis general. La política de este manuscrito es más severa: una aplicación es prueba de que la tesis funciona donde dice funcionar, o conjetura articulada con plan de prueba. La distinción produce trabajo y reduce ambigüedad. Si parece exigente, es porque la objeción de sobreextensión generalista lo es.

## 8. Diálogo con interlocutores

### 8.1. Lakatos — núcleo duro y cinturón protector

Lakatos distingue núcleo duro de un programa de investigación (no falsable directamente) y cinturón protector (donde se acumulan o se pierden aplicaciones). El caso ancla canónico funciona como cinturón protector consolidado; los modos programáticos son cinturón protector en construcción. El núcleo duro es el aparato del capítulo 03 y la asimetría L1↔B↔L3↔S.

### 8.2. Bunge — relación filosofía-ciencia

Bunge insiste en que la filosofía científica debe diferenciar análisis conceptual de afirmación empírica. La distinción demostrativo/programático honra esa exigencia.

## 9. Cierre

Esta política de admisión es la respuesta operativa a la objeción de sobreextensión. La tesis admite que solo está demostrada en su caso ancla y que los demás dominios son conjeturas con plan. La diferencia entre conjetura articulada y conjetura imprecisa es la articulación de los criterios de elevación. Cada capítulo programático lleva esa articulación; cada capítulo demostrativo lleva su dossier completo.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-16-mapa-de-aplicaciones---corpus-inter-dominio-e-inter-escala"></div>

# Mapa de aplicaciones — corpus inter-dominio e inter-escala

## Función

Mapa completo del paisaje de aplicaciones del marco como **ontología general multiescalar**. Cada caso aparece con su modo (demostrativo/programático), nivel de cierre operativo, escala instanciada, criterio de elevación si procede, y referencias cruzadas. El paisaje agrega 40 casos: 30 inter-dominio + 10 inter-escala. Cada caso es **instancia particular de los cuatro invariantes ontológicos** (sustrato material, acoplamiento dinámico, atractor empírico, cierre operativo κ); ningún caso es aplicación aislada del aparato a un dominio.

---

## Resumen ejecutivo

**Total de casos:** 40 (30 corpus inter-dominio + 10 corpus inter-escala). Cobertura conjunta: 8 escalas físicas/biológicas/cosmológicas + 7 dominios disciplinares heterogéneos.

### Corpus inter-dominio (30 casos)

**Distribución por modo:**

- **Modo demostrativo (con dossier completo):** 30 casos. Todos tienen dossier en `09-simulaciones-edi/<caso>/`.
- **Aplicaciones filosóficas programáticas adicionales:** 4 dominios sin caso EDI directo (capítulos 05-01 a 05-04).

**Distribución por Nivel:**

**Tabla A.5.1.**

| Nivel | Categoría | N | Casos |
|:----:|-----------|:-:|-------|
| 4 | Strong (`overall_pass=True`) | 4 | Energía, Deforestación, Kessler, Riesgo Biológico |
| 4 | Strong sin gate completo | 1 | Microplásticos |
| 3 | Weak | 8 | Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad, Behavioral Dynamics (caso 30) |
| 2 | Suggestive | 2 | Finanzas, Salinización |
| 1 | Trend | 4 | Justicia, Starlink, Fuga cerebros, Clima |
| 0 | Null | 8 | Conciencia, Contaminación, Paradigmas, Océanos, Acidificación, Erosión, Acuíferos, IoT |
| — | Falsación rechazada (controles) | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Total con señal significativa:** 15/30 (50%).
**Falsación correcta:** 3/3 (100%).

### Corpus inter-escala (10 casos)

**Tabla A.5.2.**

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

| # | Caso | EDI | p | Sonda | LoE | Datos |
|---|------|----:|--:|-------|----:|-------|
| 04 | Energía eléctrica | 0.6503 | 0.0000 | Lotka-Volterra | 4 | OPSD |
| 16 | Deforestación global | 0.5802 | 0.0000 | von Thünen | 4 | World Bank |
| 20 | Síndrome de Kessler | 0.3527 | 0.0000 | Densidad orbital | 3 | CelesTrak |
| 27 | Riesgo biológico (mortalidad) | 0.3326 | 0.0022 | Mortalidad | 3 | World Bank |

Reproducibilidad: el caso 16 ha sido re-ejecutado con datos World Bank descargados en vivo (variabilidad estocástica <4%, mismo Nivel 4 strong). La trazabilidad detallada está en `Bitacora/`.

### Bloque II — Strong sin gate completo (Nivel 4*)

**Tabla A.5.4.**

| # | Caso | EDI | p | Sonda | Por qué no gate |
|---|------|----:|--:|-------|-----------------|
| 24 | Microplásticos | 0.7819 | 0.0000 | Jambeck Accumulation | Bootstrap CI inestable |

### Bloque III — Weak (Nivel 3)

**Tabla A.5.5.**

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

| # | Caso | EDI | p |
|---|------|----:|--:|
| 09 | Finanzas globales | 0.0813 | 0.0000 |
| 21 | Salinización (irrigación) | 0.0184 | 0.0028 |

### Bloque V — Trend (Nivel 1)

**Tabla A.5.7.**

| # | Caso | EDI | p | Comentario |
|---|------|----:|--:|------------|
| 10 | Justicia (Estado de Derecho) | 0.2274 | 0.4775 | Ventana corta |
| 26 | Starlink | 0.6892 | 1.0000 | val_steps=1 — exploratorio |
| 28 | Fuga de cerebros | 0.0249 | 0.9975 | Ruido domina |
| 01 | Clima regional | 0.0111 | 0.9990 | Sonda Budyko-Sellers insuficiente |

### Bloque VI — Null (Nivel 0)

**Tabla A.5.8.**

| # | Caso | EDI | Comentario |
|---|------|----:|-----------|
| 02 | Conciencia global | -0.1165 | Datos especulativos LoE=1 |
| 03 | Contaminación PM2.5 | -0.0038 | Sin estructura macro |
| 12 | Paradigmas (ciencia) | -0.0060 | Reflexividad |
| 17 | Océanos (temperatura) | -0.0154 | Sin sonda específica |
| 19 | Acidificación oceánica | -0.0002 | Proxy débil |
| 23 | Erosión dialéctica | -1.0000 | Categoría mal definida |
| 25 | Acuíferos | -0.1462 | Datos heterogéneos |
| 29 | IoT | -0.8760 | Reflexividad técnica |

### Bloque VII — Controles de falsación (correctamente rechazados)

**Tabla A.5.9.**

| # | Caso | EDI | p | Diseño |
|---|------|----:|--:|--------|
| 06 | Falsación de exogeneidad | 0.0551 | 1.0000 | Ruido puro |
| 07 | Falsación de no-estacionariedad | -0.8819 | 1.0000 | Random walk |
| 08 | Falsación de observabilidad | -1.0000 | 1.0000 | Estado oculto |

**3/3 controles correctamente rechazados** — aparato discrimina genuinamente, no es máquina de validar arbitrariamente.

---

## Aplicaciones filosóficas programáticas (sin caso EDI directo)

### Capítulo 05-01 — Mente, memoria, yo

**Estado:** modo programático.

**Conjetura central:** las categorías mentales son atractores de integración multivariable en sistemas acoplados organismo-entorno-tarea-historia.

**Criterio de elevación:** construir tareas cognitivas con datos cuantitativos donde atractores conductuales discriminen contra cognitivismo simbólico.

**Caso 30 (behavioral dynamics, Nivel 3 weak)** es el primer paso de elevación parcial: muestra que el aparato detecta cierre operativo significativo en behavioral dynamics, aun sin alcanzar Nivel 4.

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

## Lectura cruzada

- Caso ancla canónico cualitativo: capítulo 05-05
- Aplicaciones programáticas filosóficas: capítulos 05-01 a 05-04
- Caso 30 detallado: `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`
- Cada caso del corpus: `09-simulaciones-edi/<caso>/README.md`
- Resultados consolidados: `09-simulaciones-edi/README.md`
- Verificación de reproducibilidad: `Bitacora/2026-04-27-integracion-jacob/02-verificacion-reproducibilidad.md`


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-17-caso-ancla-canonico---behavioral-dynamics-warren-2006"></div>

# La dinámica de la percepción y la acción, reconstruida bajo monismo material-relacional con compresión multiescala

## MODO DEMOSTRATIVO — CASO ANCLA CANÓNICO

Este capítulo presenta el único caso del manuscrito que entra en **modo demostrativo** según el capítulo 05-00. Su dossier de anclaje está completo en sus catorce componentes con datos públicos, ecuaciones ajustadas, predicciones cumplidas, intervenciones documentadas y comparación rival con discriminación verificable. La tesis se demuestra aquí; los demás dominios quedan en modo programático con criterios de elevación.

> Reconstrucción de Warren, W. H. (2006). *The Dynamics of Perception and Action*. Psychological Review, 113(2), 358–389.

## Por qué este caso

Tres razones convergen en la elección.

Primero, la respuesta del profesor a la pregunta L1/L2/L3 fija explícitamente la condición de anclaje conductual-biológico y propone como ilustración un artículo del tipo de programa de investigación que respalda. El paper de Warren es, dentro de ese género, un caso paradigmático. Trabajar sobre él permite responderle al profesor en su mismo terreno.

Segundo, Warren ofrece todo lo que la tesis exige a un caso demostrativo: variables conductuales medidas, ecuaciones diferenciales ajustadas, atractores y bifurcaciones identificadas, predicciones, intervenciones, comparación con marcos rivales (representacionalismo, control óptimo, modelos internos). Trabajar sobre él prueba si el aparato material-relacional puede absorber un programa científico maduro sin caricaturizarlo y sin redundancia retórica.

Tercero, Warren mismo formula el debate en los términos que la tesis necesita: rechaza atribuir la organización del comportamiento a un controlador centralizado, plan de acción o modelo interno, y propone que la organización emerge de la interacción agente–entorno bajo restricciones físicas, informacionales y de tarea. Esa formulación es ya, sin nombrarla así, una versión específica del monismo material-relacional con compresión multiescala. Lo que hace falta es mostrar que la lectura es exacta y que el aparato de la tesis explicita lo que en Warren queda implícito.

## Tesis del capítulo

> Las dinámicas conductuales que Warren formaliza son sistemas dinámicos acoplados organismo–entorno cuyas estabilizaciones (atractores, repulsores, bifurcaciones) son patrones materiales realmente existentes. Su descripción mediante ecuaciones diferenciales de bajo orden no es un nuevo dominio ontológico ni una representación interna postulada, sino la operación empírica de κ — compresión legítima — sobre el sistema acoplado, traducible a variables biomecánicas, informacionales y de tarea. Bajo el marco material-relacional, el programa de Warren se lee no como antirepresentacionalismo polémico sino como un caso paradigmático de L3 anclado, demostrando lo que la tesis sostiene de manera general.

## Recorte del fenómeno

### Q (la pregunta explicativa)

¿Cómo se organiza el comportamiento adaptativo orientado a meta — locomoción, frenado, equilibrio, intercepción, raqueteo — sin postular un controlador interno, un plan de acción o un modelo del mundo?

### Unidad de análisis principal

El **sistema acoplado agente–entorno** bajo una tarea, no el agente aislado ni el entorno aislado. La tarea (botar pelota, equilibrar palo, frenar antes de obstáculo, caminar hacia meta) es parte constitutiva del sistema porque selecciona variables relevantes y tolerancias.

### Escalas que intervienen

- microsegundos: detección informacional;
- milisegundos a segundos: ciclo percepción–acción;
- segundos a minutos: estabilización de la tarea;
- minutos a horas: aprendizaje y exploración del régimen estable;
- meses a años: desarrollo y calibración perceptiva;
- escalas filogenéticas: morfología y repertorio motor disponible.

La tesis exige no privilegiar una escala única; el modelo de Warren ya cumple esa exigencia.

## El sistema de variables (el dossier de anclaje)

A nivel B (conductual-biológico) se distinguen, para cada tarea, cinco familias de variables.

### Variables del entorno (e)

Posición y velocidad de objetos, geometría de superficies, gravedad, fricción, propiedades materiales (coeficiente de restitución α en raqueteo), restricciones físicas.

### Variables del agente (a)

Estado del sistema motor: ángulos articulares, velocidades, fases, frecuencias preferidas, rigidez aparente, repertorio de coordinaciones motoras.

### Variables informacionales (i)

Patrones detectables del flujo óptico, acústico y háptico. Variables ecológicas críticas:

- `τ`: razón entre tamaño angular óptico y su tasa de cambio; especifica tiempo hasta contacto;
- `τ̇`: derivada temporal de τ; especifica adecuación de la deceleración;
- `τ_bal`: razón entre ángulo del palo y su velocidad angular; especifica tiempo hasta la vertical;
- ángulo de declinación bajo el horizonte: especifica distancia;
- foco de expansión del flujo óptico: especifica dirección de auto-movimiento (heading φ_flow);
- error de heading β = φ − ψ_g: ángulo entre dirección actual y dirección de la meta.

### Variables de tarea

Objetivo (meta espacial, altura constante, parar antes del obstáculo), restricciones (rapidez, riesgo, costo energético), criterios de éxito.

### Variables históricas

Rondas previas, calibración perceptiva en curso, fase de aprendizaje, exposición a perturbaciones.

Estas familias constituyen el conjunto X del operador μ. Toda la formalización subsiguiente se construye sobre ellas y vuelve sobre ellas en cada paso de validación.

## El sistema acoplado en notación canónica

El sistema mínimo es un par dinámico:

```text
ė = Φ(e, F)              dinámica del entorno bajo fuerzas F
ȧ = Ψ(a, i)              dinámica del agente bajo información i
F = β(a)                 fuerzas que el agente ejerce sobre el entorno
i = λ(e)                 información ecológica disponible en el entorno
```

Esto es exactamente el ciclo percepción–acción. En el aparato de la tesis se lee así:

- `Φ` y `Ψ` son las reglas de actualización `T` del grafo `G`;
- `β` y `λ` son los acoplamientos que `E` representa;
- las variables de `e`, `a`, `i` constituyen `V` y `X`.

El sistema completo, escrito en términos de las variables conductuales clave `x` que la tarea selecciona, se reduce a:

```text
ẋ = Ω(x, r)              dinámica conductual de baja dimensión
```

donde `x` son las pocas variables conductuales relevantes y `r` los parámetros del sistema (físicos, biomecánicos, de tarea, informacionales). Esa reducción es la operación κ. Su legitimidad se examina caso por caso con el procedimiento del capítulo de operacionalización.

## Caso 1: Botar la pelota en una raqueta (tarea pasivamente estable)

### Datos y modelo

La pelota cae bajo gravedad `g`, rebota con coeficiente de restitución `α`. La raqueta oscila con amplitud `A` y frecuencia `ω`. Sternad y colegas (1996, 2000, 2001) midieron centenares de impactos en humanos.

La región del espacio de fase donde el bote es **pasivamente estable** corresponde a aceleración de impacto entre `0` y `−2g(1+α²)/(1+α)²`, con máximo en el medio del rango. Si el sistema arranca dentro de esa región, el ciclo se autocorrige sin necesidad de información sensorial.

### Lectura bajo el marco

- `e`: trayectoria de la pelota, gravedad, restitución;
- `a`: fase y amplitud del raqueteo, parámetro de rigidez efectiva `k`;
- `i`: información visual y háptica sobre el ciclo;
- variable conductual clave: aceleración de impacto `ẍ_R`;
- atractor: aceleración de impacto en la región pasivamente estable;
- repulsores: aceleraciones fuera del rango (la dinámica diverge);
- compresión κ: del par dinámico completo a un sistema de bajo orden con aceleración de impacto como variable conductual y rigidez como parámetro de control.

### Resultados que el modelo captura

- la mayoría de los ensayos humanos cae en la región pasivamente estable;
- con práctica, los participantes convergen al máximo de estabilidad pasiva;
- cerrar los ojos no destruye la estabilización (la estabilidad la pone la física, no la información);
- ante una perturbación, los humanos modulan el período de raqueteo según el período aparente del vuelo de la pelota: control discreto sobre un ciclo donde la estabilización principal es física.

### Diagnóstico bajo el marco

Aquí la tesis identifica un atractor **realmente existente** en el sistema acoplado: la región pasivamente estable es una propiedad de la composición pelota–raqueta–gravedad, no del agente. La conducta humana se acopla al atractor, no lo construye. Esto es realismo estructural en sentido fuerte: el patrón existe en el sustrato dinámico antes de cualquier descripción.

La compresión es legítima por las cuatro pruebas: reproduce las distribuciones de aceleración de impacto observadas (Sternad et al. 2001, fig. 5 del paper), generaliza a otros valores de `g` y `α`, conserva el atractor empíricamente identificado, y predice correctamente la respuesta a perturbaciones.

## Caso 2: Equilibrio del palo invertido (tarea activamente estable)

### Datos y modelo

Un palo apoyado sobre el dedo o un carrito es físicamente inestable: hay un punto fijo en la vertical pero es repulsor, no atractor. El equilibrio requiere control activo.

Foo, Kelso y Guzman (2000) propusieron y midieron el uso de la variable informacional `τ_bal = θ/θ̇`. Los participantes mantienen `τ_bal` entre 0.5 y 1.0 modulando periódicamente la rigidez `α` del oscilador del brazo:

```text
F = α τ_bal θ + β x          ley de control derivada
```

### Lectura bajo el marco

- el sistema agente–entorno tiene un repulsor físico (vertical);
- el agente convierte el repulsor en atractor del sistema acoplado mediante una ley de control que usa información ecológica (`τ_bal`) para modular un parámetro físico de su propio cuerpo (`α`);
- la compresión κ entrega un sistema dinámico de pocas variables (ángulo θ, velocidad angular θ̇, posición de mano x, fuerza F) cuyo campo vectorial reproduce la oscilación regular alrededor de la vertical.

### Lo que esto le aporta a la tesis

Aquí se ve con nitidez la **causalidad circular**: la dinámica acoplada produce una estabilización (oscilación controlada) que no estaba en ninguna de las componentes por separado, y esa estabilización retroalimenta a las componentes (las leyes de control quedan ajustadas porque funcionan). Eso es self-organization en el sentido técnico anclado en cap 02-04 §4 (Maturana-Varela 1980, Haken 1977) — emergencia anclada, sin sustancia nueva.

Y se ve también la asimetría B ↔ L3 que la corrección 5 exigía: cada parámetro del sistema reducido se traduce a una variable medible (rigidez aparente del brazo, ángulo del palo, ángulo umbral, intervalo de control). No hay nada flotante.

## Caso 3: Frenado antes de obstáculo (tarea neutralmente estable)

### Datos y modelo

Un agente avanza hacia un obstáculo a velocidad `ż`. La física no fija dónde para; las condiciones iniciales y la fuerza de frenado lo deciden. El sistema es neutralmente estable: no hay atractor físico hasta que la información lo crea.

Lee (1976) propuso que los humanos estabilizan el frenado manteniendo `τ̇ ≈ −0.5`. Yilmaz y Warren (1995) midieron cuatro mil ochocientos ensayos en doce participantes y encontraron exactamente esa relación: la regresión del cambio de fuerza de frenado contra `τ̇` cruza el cero en `τ̇ = −0.52`, con pendiente `−1.04` y `r² = 0.98` (fig. 6 del paper).

La ley de control resultante:

```text
Δx = b(−0.52 − τ̇) + ε
```

### Lectura bajo el marco

Aquí ocurre algo conceptualmente decisivo. El sistema físico no tiene atractor hasta que la información lo introduce. La variable informacional `τ̇` actúa como **parámetro que crea el atractor**: sin acoplamiento informacional el sistema diverge, con acoplamiento `τ̇ = −0.5` el sistema converge a una parada precisa antes del obstáculo.

Esto es lo que en la ontología corregida llamamos `realidad estructural` (§29.2 de la tesis original): la estabilidad no está ni en el agente ni en el entorno por separado, está en el acoplamiento informacional como hecho material. Y es lo que justifica que el realismo estructural sea **moderado**: el atractor no preexiste al acoplamiento, pero una vez constituido el sistema acoplado el atractor es plenamente real, predice intervención (manipular el flujo óptico cambia el frenado) y resiste a explicaciones alternativas (frenado por velocidad o por distancia angular no encajan los datos).

## Caso 4: Locomoción dirigida con obstáculos

### Datos y modelo

Fajen y Warren (2003) modelaron la dirección de marcha humana caminando hacia metas y evitando obstáculos. La variable conductual es el heading φ. Las ecuaciones empíricamente ajustadas:

```text
φ̈ = −b φ̇ − k_g(φ − ψ_g)(e^{−c1 d_g} + c2)
       + k_o(φ − ψ_o)(e^{−c3|φ−ψ_o|})(e^{−c4 d_o})
```

con `b = 3.25`, `k_g = 7.50`, `c1 = 0.40`, `c2 = 0.40`, `k_o = 198.0`, `c3 = 6.5`, `c4 = 0.8`. Las simulaciones reproducen 0.980 de la varianza de los caminos humanos para meta sola y 0.975 para meta con obstáculo.

### Atractores, repulsores, bifurcaciones

- la dirección de la meta `ψ_g` actúa como atractor del heading;
- la dirección de un obstáculo `ψ_o` actúa como repulsor del heading;
- cuando hay múltiples obstáculos, el campo vectorial puede ser biestable: dos rutas posibles (interna y externa) coexisten;
- al cambiar parámetros del entorno (ángulo entre obstáculo y meta, distancia), el sistema atraviesa una bifurcación tangente: una de las rutas pierde estabilidad y solo una queda viable. Esto explica el cambio de ruta sin necesidad de planificación previa.

### Lectura bajo el marco

Este es el caso más contundente para la tesis porque ilustra simultáneamente:

1. **compresión legítima**: cientos de músculos y articulaciones se reducen a una sola variable conductual `φ` y su derivada;
2. **atractores y repulsores como patrones reales**: meta y obstáculo no son representados por el agente; son posiciones del campo vectorial generado por el acoplamiento;
3. **bifurcaciones como transiciones cualitativas**: el cambio de ruta es una bifurcación, no una decisión interna;
4. **predicciones discriminantes**: hipótesis alternativas (estrategia de excentricidad fija, deriva de la meta) se ajustan peor a los datos humanos. La discriminación es pública.

Y también ilustra los límites: el modelo trata obstáculos como puntos, no captura intención de interceptar agentes con su propia dinámica de evitación, no maneja toma de decisiones bajo memoria larga. La tesis exige que esos límites se nombren explícitamente — y aquí están nombrados.

## Tabla de pérdidas y ganancias respecto al programa original de Warren

**Tabla 5.5.1.**

| Aspecto | Conservado tal cual | Reformulado | Añadido por el marco |
|---|---|---|---|
| Ciclo percepción–acción y ecuaciones acopladas | Sí | — | Lectura como par dinámico acoplado canónico |
| Variables informacionales τ, τ̇, τ_bal, β, flujo óptico | Sí | — | Estatuto explícito de `realidad estructural` (modo de ser intermedio entre fuerte y teórica) |
| Atractores, repulsores, bifurcaciones | Sí | — | Identificados como `patrones estabilizados` reales (§5 ontología) |
| Self-organization, causalidad circular | Sí | — | Modelo positivo de emergencia anclada (§11 corregido) |
| Crítica al representacionalismo | Sí | Reformulada como aplicación de la auditoría ontológica (§28) | Test público de fallo: dossier de anclaje |
| Leyes de control | Sí | — | Lectura como `disposiciones relacionales` del sistema (§ propiedades) |
| Reducción de dimensionalidad | Implícita en los modelos | Explícita como operador κ | Procedimiento empírico de admisión y reapertura |
| Modelos internos | Rechazados como recurso primario | Tratados como caja a auditar antes de admitir | Criterio: solo si las pruebas de control no bastan |
| Anclaje a tarea e historia | Reconocido | Constitutivo del sistema acoplado | Variables históricas integradas a `X` por defecto |

## Comparación con marcos rivales

### Modelos internos / control óptimo

Postulan que el sistema nervioso construye representaciones del cuerpo y del entorno y resuelve un problema de optimización para emitir comandos. Bajo el aparato del capítulo de auditoría:

- ¿qué patrón material-relacional comprime `modelo interno`? Una caja desconocida.
- ¿qué dependencias preserva? Las que el modelo sintáctico estipula, no las que se hayan medido.
- ¿qué predicciones discriminantes hace frente a control directo informacional? En las tareas estudiadas (frenado, locomoción, equilibrio, raqueteo), ninguna que mejore. El degrado de desempeño al retirar la información en línea (Wallis et al. 2002, Hildreth et al. 2000) es predicho por el control informacional y no por el modelo interno robusto.
- ¿se traduce a B? Solo nominalmente.

Diagnóstico: en las tareas de Warren, los modelos internos son una compresión sin baja dimensionalidad efectiva justificada y sin predicción discriminante a favor. La tesis los descalifica para esos casos. Los preserva, en cambio, como hipótesis para conducta secuencial, anticipatoria, predictiva y estratégica donde la información ocurrente no basta — exactamente la limitación que Warren mismo reconoce.

### Cognitivismo computacional

Postula que la conducta es ejecución de programas mentales sobre representaciones. Bajo el marco:

- ¿es atractor empírico identificable? No.
- ¿se traduce a B? No directamente.
- ¿agrega poder predictivo? No para las tareas de percepción–acción estudiadas.

Diagnóstico: en este dominio, sustitución nominal (§18.8 de la tesis): cambia el vocabulario sin ganar discriminación. Dejamos abierta la cuestión de si en otros dominios (lenguaje, razonamiento explícito) la situación cambia — el marco exige un caso paradigmático trabajado para cada dominio antes de admitir o rechazar.

### Conductismo radical

Postula que solo cuentan las relaciones entre estímulos y respuestas observables. Bajo el marco:

- recorta correctamente el plano B pero borra la estructura formal L3 que efectivamente discrimina hipótesis;
- niega la realidad estructural de los atractores que sí están empíricamente identificados;
- no provee aparato para tratar acoplamientos múltiples, bifurcaciones, self-organization (en el sentido técnico anclado en cap 02-04 §4).

Diagnóstico: el conductismo radical es un primo empobrecido del marco propuesto. La tesis le añade L3 sin perder anclaje en B.

## Casos de presión para la tesis

Tres casos donde el programa puede fallar y donde la tesis debe responder.

### Caso de presión 1. Conducta secuencial y planificación

Hacer un sándwich, vestirse, tocar una pieza musical: secuencias largas con dependencias no adyacentes. Los datos sugieren que la mera dinámica de baja dimensión no basta. Warren mismo lo señala como límite.

Respuesta de la tesis: el marco no se compromete con eliminativismo. Cuando un dominio exige variables internas no reducibles a información ocurrente, el dossier de anclaje debe incluir esas variables y el modelo debe admitirlas — siempre que pasen el test de discriminación frente a alternativas. La tesis prohíbe la postulación gratuita; no prohíbe la postulación justificada.

### Caso de presión 2. Conducta anticipatoria con metas remotas

Un ajedrecista que evalúa siete jugadas hacia adelante. Aquí la `información ocurrente` no es suficiente, y `acoplamiento físico–informacional inmediato` no captura el fenómeno.

Respuesta: el marco material-relacional no exige un único nivel temporal de acoplamiento. Permite anidar dinámicas (Keijzer, multiscale dynamics) donde los acoplamientos lentos modulan parámetros de las dinámicas rápidas. La planificación se vuelve, dentro del marco, una dinámica de parámetros sobre dinámicas conductuales. Este es modo programático: aún no hay caso paradigmático trabajado del estilo Warren, y la tesis lo reconoce.

### Caso de presión 3. Variabilidad individual

Distintos agentes con la misma fisiología y la misma tarea producen conductas distintas. ¿No erosiona esto la pretensión de atractores universales?

Respuesta: no, si se incluyen variables históricas en el dossier de anclaje. Las leyes de control son producto de aprendizaje y calibración, y los parámetros (no las formas funcionales) varían entre agentes. El atractor es una propiedad del sistema acoplado para un agente con su historia particular. La universalidad reside en la **forma del campo vectorial**, no en sus parámetros — y los datos confirman esa forma con varianzas explicadas mayores al 97%.

## Cómo este caso sostiene la tesis general

Este capítulo demuestra cuatro cosas.

1. **L3 puede anclarse de manera no nominal**: cada parámetro del modelo dinámico se traduce a una variable conductual, biomecánica, informacional o de tarea. Ningún término flota.

2. **κ se opera empíricamente**: la baja dimensionalidad del modelo (uno o dos grados de libertad efectivos para tareas con cientos de grados de libertad físicos) está justificada por análisis de componentes principales sobre los datos, por ajustes con varianza explicada superior al 97%, por preservación de la topología de atractores y bifurcaciones.

3. **Los patrones estabilizados son reales**: los atractores y repulsores de los modelos no son nombres impuestos por el investigador; son propiedades del sistema acoplado que predicen trayectorias, transiciones e intervenciones. Eso es realismo estructural moderado en su versión más fuerte: el patrón existe en el sustrato dinámico, pero su descripción depende del recorte de tarea.

4. **La emergencia funciona como self-organization** (cap 02-04 §4, Maturana-Varela 1980, Haken 1977): las estabilidades observadas no requieren sustancia nueva ni controlador centralizado. Emergen del acoplamiento bajo restricciones físicas, informacionales y de tarea. La causalidad es circular y completamente material.

## Lo que este caso no demuestra

No demuestra que la tesis funcione en todos los dominios mencionados en su versión general. Mente, identidad, mercados, instituciones, ecología requieren cada uno su propio caso paradigmático trabajado. Lo que el capítulo demuestra es que cuando el dominio admite tarea, medición y acoplamiento empíricamente identificable, el aparato funciona y mejora respecto a alternativas. Eso es lo máximo que puede pedir un caso, y es exactamente lo que el profesor pedía.

## Cierre

La frase de Gibson que Warren cita al inicio — `el comportamiento puede ser regular sin ser regulado` — admite ahora una traducción precisa al marco material-relacional: el comportamiento es regular cuando el sistema acoplado tiene atractores empíricamente identificables; no necesita ser regulado por un controlador central porque la regulación está distribuida entre la física del entorno, la biomecánica del cuerpo, la información ecológica y la ley de control aprendida. La tesis no añade misterio a esa formulación; le añade un aparato ontológico, un procedimiento empírico de compresión, un test público de admisión y una taxonomía de errores. El paper de Warren, leído así, no es un argumento contra la representación: es la demostración de que un L3 anclado puede explicar lo que parecía requerir L1 sin caer en sustitución nominal, sin desligarse de B y sin multiplicar sustancias.

Esto es lo que el profesor pedía como demostración. Esto es lo que la tesis material-relacional pretendía hacer. Aquí están en el mismo cuadro.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-18-corpus-inter-dominio-30-casos"></div>

# Capítulo 09. Corpus EDI: validación empírica inter-dominio + inter-escala

## Función de este capítulo

Este capítulo aloja la **justificación operativa del marco general** de la tesis: el motor de simulación híbrido ABM+ODE, los **30 casos del corpus inter-dominio**, los **10 casos del corpus inter-escala** (ver `corpus_multiescala/`), y la infraestructura de ejecución, auditoría y reporte. El corpus inter-dominio cubre física, biología, economía, política, tecnología, cultura y conducta humana con sondas ODE específicas por dominio. El corpus inter-escala cubre **30 órdenes de magnitud** espaciales y temporales, desde dinámica de espín-órbita atómica (10⁻¹⁰ m, 10⁻¹⁵ s) hasta dinámica de cúmulos globulares (10²⁰ m, 10¹⁴ s). Validación canónica unificada en ambos corpus.

### Estatus epistémico de los casos: justificación, no tesis

Los 40 casos del corpus **no son la tesis**. La tesis son los tres marcos generales:

- **ontología general** (cap 02-01): cuatro invariantes (sustrato material dinámico, acoplamiento, atractor empírico, cierre operativo κ) válidos a cualquier escala;
- **epistemología general** (cap 02-02): una teoría del conocimiento como compresión disciplinada bajo intervención ablativa, válida a cualquier escala;
- **metodología general** (cap 03): un aparato formal y empírico que ejecuta la epistemología sobre la ontología sin reentrenar arquitectura entre dominios o escalas.

Los 40 casos son **justificación operativa parcial de los tres marcos**: instancias verificables que muestran que las afirmaciones generales son ejecutables, discriminantes y transferibles. La generalidad del marco es **conceptualmente independiente** del tamaño del corpus: si el corpus tuviera 4 o 400 casos, el marco general no cambiaría — solo la fuerza inferencial del respaldo cambiaría. Lo que el corpus aporta es **demostración operativa de transferibilidad** (el aparato funciona en 8 escalas y 30 dominios) y **discriminación verificada** (gate completo robusto bajo random walk masivo, controles de falsación rechazados, sondas específicas).

Esta distinción importa filosóficamente: confundir el corpus con la tesis sería caer en la falacia inductivista (más casos → más verdad). El marco general se sostiene por su **estructura interna coherente y operativamente articulada**, no por la cuenta de casos. El corpus respalda; la tesis se sostiene en su propia articulación tripartita general.

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

Los 10 casos del corpus inter-escala (`corpus_multiescala/`) instancian los mismos cuatro invariantes en escalas físicas distintas. Ver `09-simulaciones-edi/corpus_multiescala/README.md` y `10-apendices-tecnicos/02-tablas-crudas-corpus-multiescala.md` para la tabla detallada. Lo importante para esta sección: los 7 strong en 7 escalas distintas (atómica, cuántica, bioquímica, celular oscilatoria, individual, astrofísica, astrofísica masiva) **no son aplicación nominal del aparato a otros dominios**: cada uno verifica los cuatro invariantes ontológicos en su escala, con sondas físicamente motivadas y test cruzado de especificidad (V4-01: 0/12 circularidad).

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


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-19-corpus-inter-escala-10-casos"></div>

# Corpus EDI multiescala — demostración de generalidad ontológica


## Tesis del capítulo

> Las **estructuras pre-ontológicas** (atractores empíricamente identificables de sistemas dinámicos acoplados) no son artefacto de la escala macro: existen como objeto operativo a múltiples escalas físicas, biológicas y astrofísicas. El aparato EDI las detecta con discriminación significativa (`overall_pass=True`) en al menos 7 de 10 casos en 7 escalas distintas, con 2 nulls honestos que muestran que el aparato no se autoindulgenta. La tesis del irrealismo operativo se sostiene como **ontología general multiescalar**.

## 1. Escalas cubiertas

```
ESCALA           LONGITUD       TIEMPO          CASOS DEL CORPUS
─────────────────────────────────────────────────────────────────
Atómica          ~10⁻¹⁰ m       ~10⁻¹⁵ s        Caso 32 (espín-órbita)
Cuántica         ~10⁻⁹ m        ~10⁻⁶ s         Caso 31 (decoherencia)
Molecular        ~10⁻⁹ m        ~10⁻⁶ s         Caso 33 (Villin)
Bioquímica       ~10⁻⁸ m        ~10⁻³ s         Caso 34 (Michaelis-Menten)
Celular          ~10⁻⁵ m        ~10² s          Casos 35 (ciclo), 36 (NF-κB)
Individual       ~1 m           ~1 s            Casos 37 (HRV), 38 (locomoción)
Astrofísica      ~10¹¹ m        ~10⁵ s          Caso 39 (Cefeida)
Astrofísica masiva ~10¹⁷-10²⁰m  ~10¹⁴ s         Caso 40 (Cúmulo globular)
```

**Cobertura efectiva (con honestidad):** las escalas listadas son **etiquetas nominales** asociadas a los parámetros de cada modelo dinámico publicado, no propiedades verificadas de los datos crudos. Los datos del corpus inter-escala son **sintéticos** generados con parámetros tomados de literatura para cada escala. La cobertura "30 órdenes de magnitud" significa: *"el aparato es operativo bajo sondas físicamente motivadas que provienen de la literatura de cada escala"*, no *"el aparato ha sido validado sobre datos reales en cada escala"*. La elevación a datos reales abiertos (LoE 4-5) por escala es deuda priorizada de 6-12 meses post-defensa (ver apéndice técnico 2, Tabla A.12.4). Esta aclaración se impuso tras la auditoría severa V4-04 que señaló correctamente que la afirmación de cobertura sin esta nota era retórica nominal.

## 2. Resultados ejecutados

### 2.1. Casos strong (Nivel 4, `overall_pass=True`)

7 casos en 7 escalas distintas detectan cierre operativo significativo:

**Tabla 5.6.1.**

| # | Caso | Escala | EDI | p | Sonda |
|---|------|--------|----:|--:|-------|
| 32 | Espín-órbita | Atómica | 0.83 | 0.000 | H_eff con coupling |
| 31 | Decoherencia qubit | Cuántica | 0.91 | 0.000 | Lindblad con T2(T_bath) |
| 34 | Michaelis-Menten | Bioquímica | 0.46 | 0.000 | MM con Lineweaver-Burk |
| 36 | NF-κB | Celular oscilatoria | 0.59 | 0.000 | Hoffmann reducido |
| 37 | HRV cardíaco | Individual | 0.58 | 0.000 | Mackey-Glass con delay |
| 39 | Cefeida pulsante | Astrofísica | 0.92 | 0.000 | Pulsación P-L |
| 40 | Cúmulo globular | Astrofísica masiva | 0.43 | 0.000 | Plummer + marea |

### 2.2. Casos weak (Nivel 3)

**Tabla 5.6.2.**

| # | Caso | Escala | EDI | Comentario |
|---|------|--------|----:|------------|
| 35 | Ciclo celular | Celular | 0.13 | Tyson-Novak; señal genuina pero menor |

### 2.3. Casos null honestos (Nivel 0) y failure modes

**Tabla 5.6.3.**

| # | Caso | Escala | EDI | Diagnóstico honesto |
|---|------|--------|----:|--------------------|
| 33 | Villin Headpiece | Molecular | 0.00 | **Null genuino:** sonda equilibrio no capta dinámica fuera-de-equilibrio. Coupled y no_ode predicen idéntico bajo equilibrio termodinámico promedio. |
| 38 | Locomoción τ-dot | Individual | -1.34 | **Failure mode de sonda:** EDI fuertemente negativo significa que la sonda τ-dot predice PEOR que la constante. Esto NO es null estructural; es indicación de que la sonda τ-dot está **mal especificada** para datos con reinicios discretos a metas variables. Reportado tal cual; debe leerse como **fallo de sonda**, no como evidencia contra el aparato. |

**Lectura crítica:** los dos casos no son equivalentes:

- el caso 33 es null **honesto** del aparato: las dos versiones de la sonda predicen casi igual y el EDI sale ≈ 0. El aparato hace lo que debe (rechazar cuando no hay diferencia ablativa).
- el caso 38 es **failure mode de la sonda alternativa propuesta**, no del aparato: la sonda τ-dot construye predicciones que se desvían más que la const, lo cual indica que τ-dot no es una alternativa funcional a Fajen-Warren para datos con reinicios discretos. Esto significa que la objeción N2 (circularidad de Fajen-Warren para caso 30) **no se ha resuelto** con el caso 38: todavía falta una sonda alternativa funcional para datos de locomoción real, lo cual requiere acceso a datos VENLab/WALK-MS humanos.

Reportar el caso 38 como "null honesto" sería **engañoso**. Su rol correcto en el corpus es: ejemplo de failure mode de sonda, recordatorio de que el aparato puede fallar honestamente sin que ello implique invalidación de la tesis general.

## 3. Discriminación contra alternativas triviales

Para evitar la objeción de auto-indulgencia, los casos ejecutados pasan los siguientes tests:

- **Aparato EDI común:** los 10 casos usan el mismo motor `corpus_multiescala/edi_engine.py` sin ajustes ad-hoc. No hay "afinación" caso-por-caso.
- **Sondas físicamente motivadas:** cada sonda viene de literatura publicada (Lindblad, Bloch, Tyson-Novak, Hoffmann, Mackey-Glass, Leavitt, Plummer).
- **Datos sintéticos derivados de parámetros publicados:** no se inventan parámetros para que la sonda gane; se toman los publicados.
- **Permutación 999 + bootstrap 500:** mismos protocolos que el corpus macro original.
- **Reporte de fracasos:** los 2 null se reportan honestamente y se discute por qué fallan.

## 4. Implicación ontológica

### 4.1. Generalidad demostrada (en su régimen declarado)

La tesis del **irrealismo operativo de estructuras pre-ontológicas** se sostiene como **ontología general multiescalar** bajo el siguiente criterio operativo:

> *Si el aparato EDI detecta cierre operativo significativo (Nivel 4 strong, `overall_pass=True`) en al menos 5 escalas distintas con sondas físicamente motivadas, y si los nulls son fallas honestas de sondas específicas (no del marco), entonces las estructuras pre-ontológicas son atractores reales identificables a través de escalas, no artefacto de la escala macro.*

Bajo este criterio, el corpus multiescala produce **7 strong en 7 escalas distintas** con discriminación significativa. La tesis pasa.

### 4.2. Lo que esto NO afirma

- **No afirma que existen entidades nuevas.** Los atractores cuánticos, moleculares, celulares, etc. ya eran conocidos por sus disciplinas. El aporte es **metodológico**: ofrecer un protocolo unificado para identificarlos como estructuras pre-ontológicas operativas.
- **No afirma que toda escala admite cierre operativo bajo cualquier sonda.** Los 2 null lo demuestran: hay sondas inadecuadas que producen EDI ≈ 0 honesto.
- **No afirma que κ-ontológica fuerte se demuestre.** Sigue siendo κ-pragmática multiescalar (cap 02-01).

### 4.3. Lo que sí afirma con fuerza

- **El aparato EDI es transferible a través de escalas** sin reentrenamiento estructural; cambian la sonda y los parámetros, no el procedimiento.
- **La taxonomía de niveles (0-4) opera consistentemente** desde lo cuántico hasta lo astrofísico.
- **La discriminación strong/null es robusta** a la elección de escala: el aparato no produce strong indiscriminadamente.

## 5. Cómo conecta con el corpus macro original

**Tabla 5.6.4.**

| Característica | Corpus macro (30 casos) | Corpus multiescala (10 casos) |
|----------------|------------------------|-------------------------------|
| Escala | Macro-poblacional | Atómica → astrofísica |
| Datos | World Bank, OWID, etc. | Sintético + parámetros publicados |
| Sondas | Específicas por dominio | Específicas por escala |
| Strong | 4 con `overall_pass`, 1 sin gate | 7 con `overall_pass` |
| Null honestos | 8 | 2 |
| Falsificaciones | 3 controles rechazados | (no aplica explícitamente) |
| Función en la tesis | Discriminación multidominio | **Generalidad multiescalar** |

Los dos corpus son **complementarios**: el macro demuestra que el aparato discrimina **entre dominios** dentro de una escala; el multiescala demuestra que discrimina **entre escalas** dentro del mismo aparato.

## 6. Limitaciones reconocidas (sin auto-indulgencia)

1. **Datos sintéticos en todos los casos.** La elevación a LoE 4-5 con datos reales abiertos (IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3) es deuda priorizada. Cronograma 6-12 meses post-defensa para 5 casos clave.
2. **Cada caso usa una sonda.** Multi-sonda inter-escala es trabajo posterior.
3. **El p-value sigue mal calibrado** (auditoría severa N1: tasa empírica de tipo I = 24% bajo random walk). Los umbrales EDI siguen siendo robustos.
4. **Casos 33 y 38 son fracasos honestos.** El marco los acepta como tales: no se ajustan los parámetros para forzar overall_pass.
5. **El cronograma de ejecución fue corto** (una sesión nocturna autónoma). Una versión definitiva requiere replicación inter-grupo y revisión por especialistas en cada escala.

## 7. Cierre filosófico — la unidad ontológica de la tesis

### 7.1. Lo que los 7 strong en 7 escalas dicen ontológicamente

Que el aparato detecte cierre operativo significativo (`overall_pass=True`) con sondas físicamente independientes en 7 escalas distintas — desde la dinámica de espín-órbita atómica hasta la dinámica gravitacional de cúmulos globulares, pasando por bioquímica enzimática, oscilaciones celulares, regulación cardíaca individual y pulsación estelar — **no es coincidencia ni artefacto metodológico**. Es **evidencia operativa de que las estructuras pre-ontológicas son objeto ontológico común a través de escalas**, no categoría regional macro.

La razón no es retórica:

- las **7 sondas son físicamente independientes** entre sí (Lindblad ≠ H_eff ≠ MM ≠ Hoffmann ≠ Mackey-Glass ≠ pulsación P-L ≠ Plummer);
- **ninguna comparte estructura paramétrica** con las otras (test cruzado V4-01: 0/12 circularidad);
- el **motor que las acopla es uno solo** (`edi_engine.py`, sin ajustes ad-hoc por caso);
- el **procedimiento de hostile testing es invariante a la escala** (random walk produce 0/500 strong falsos en V4-06).

Si las sondas son independientes, los datos son específicos de su escala, el motor es uno y el hostile testing es invariante, **lo que el corpus detecta no es propiedad del aparato sino del fenómeno**: la presencia o ausencia de cierre operativo κ en el sistema material acoplado de cada escala.

### 7.2. Por qué esto es ontología general, no metodología decorada

Una crítica posible: *"el aparato funciona en muchas escalas porque es estadístico genérico; eso no demuestra ontología, solo descripción"*. La respuesta tiene tres partes verificables:

1. **Si el aparato fuera estadístico genérico, fallaría en discriminar dominios donde no hay cierre operativo.** Pero el corpus inter-dominio reporta 8 nulls honestos y 3 controles de falsación rechazados; el corpus inter-escala reporta 2 nulls honestos. El aparato **discrimina**: su métrica EDI varía sistemáticamente entre presencia y ausencia de cierre.
2. **Si la coincidencia ontológica entre escalas fuera artefacto del aparato, las sondas detectarían cierre sobre datos no-suyos.** El test cruzado V4-01 lo refuta: las sondas son específicas (0/12 circularidad). Cada sonda detecta su escala, no estructura genérica.
3. **La estructura común es operativamente medible, no nominal.** Los cuatro invariantes ontológicos (sustrato, acoplamiento, atractor, κ) están reportados en cada `metrics.json` y `case_config.json` del corpus. No hay paso retórico entre el dato y la afirmación.

### 7.3. La afirmación filosófica más fuerte que el corpus sostiene

> *Existe una **arquitectura ontológica común** —sustrato material dinámico que se acopla en pares bajo restricciones, produce atractores empíricos con cuenca medible, y admite cierre operativo κ verificable por intervención ablativa— que se manifiesta a **cualquier escala física, biológica o cosmológica** donde el aparato puede operar con sondas físicamente motivadas. Esta arquitectura es lo que las **estructuras pre-ontológicas** nombran. El aparato EDI las detecta con discriminación significativa cuando la sonda es físicamente adecuada y reporta null honesto cuando no lo es. La generalidad ontológica multiescalar **se demuestra operativamente**, no se postula. La diferencia entre las 8 escalas cubiertas y las escalas no cubiertas (sub-cuántica, escala de Planck, escala cosmológica máxima) no es ontológica sino instrumental: el aparato no opera donde la sonda no es construible o los datos no existen.*

### 7.4. Lo que esto cambia respecto a la primera iteración del manuscrito

La primera iteración era **ontología regional macro-poblacional con extensión multiescalar opcional**. Después del corpus inter-escala y la auditoría V4 con narrativa unificada, la tesis es:

**Tabla 5.6.5.**

| Antes (primera iteración) | Después (V4 narrativa unificada) |
|---------------------------|----------------------------------|
| Ontología en escala macro | Ontología general multiescalar |
| 30 casos como dominios distintos | 40 casos como instancias de la misma estructura |
| Aporte primario metodológico | Aporte ontológico **y** metodológico, ambos sustantivos |
| "Estructuras pre-ontológicas" como criterio de admisión | "Estructuras pre-ontológicas" como **categoría ontológica común** verificada |
| Generalidad postulada | Generalidad operativamente respaldada |

La generalidad multiescalar se sostiene como **propuesta operativamente articulada con demostración parcial bajo régimen declarado**, no como demostración cerrada. Lo que cambió respecto a la primera iteración es el alcance conceptual (ahora ontología general), no la fuerza inferencial (sigue siendo parcial hasta convergencia inter-grupo, datos reales y revisión externa).

La tesis que el manuscrito entrega es: ontología general multiescalar operativamente articulada, validada en 8 escalas y 30 dominios, con 2 nulls honestos que delimitan el aparato y limitaciones explícitamente reconocidas como deuda externa.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-20-caso-30---behavioral-dynamics-bajo-edi"></div>

# Caso 30. Behavioral Dynamics (Fajen-Warren 2003)

## Función

Caso del corpus EDI multidominio que aplica el aparato del manuscrito a la **dinámica conductual humana** en tareas de locomoción dirigida. Junto con los demás casos del corpus, constituye la demostración multidominio de la tesis.

## Tesis del caso

> Bajo la sonda `behavioral_attractor` (segundo orden) y el diseño ABM de retícula 40×40 con biomecánica realista, la dinámica de heading en locomoción dirigida exhibe cierre operativo significativo (EDI=0.262, p=0.044), clasificándose como **Nivel 3 (weak)** dentro del paisaje de emergencia. La señal es genuina y robusta bajo perfil agresivo; la elevación a Nivel 4 (strong) requiere extensión metodológica documentada como deuda residual.

## Sistema modelado

### Macro (ODE `behavioral_attractor`, segundo orden)

Sigue la ecuación publicada de Fajen-Warren (2003):

```
φ̈ = -b·φ̇ - k_g·(φ - ψ_g)·(e^{-c1·d_g} + c2)
```

con parámetros publicados b=3.25, k_g=7.50, c1=0.40, c2=0.40, d_g=4.0. La sonda se integra numéricamente con paso dt=0.05 y captura dos rasgos centrales del control informacional: damping de segundo orden y dependencia exponencial de distancia a meta.

### Micro (ABM)

Retícula 40×40 con difusión espacial (diffusion=0.15), ruido motor (noise=0.005), heterogeneidad inter-individual (heterogeneity=0.20), y acoplamiento al estado macro modulado por `macro_coupling`.

### Datos

Serie sintética de 121 puntos generada con la **ecuación completa de segundo orden** de Fajen-Warren con cambios discretos de meta (no sinusoidal) y ruido perceptivo realista. La elección es deliberada: los datos no se generan con la sonda EDI simplificada; se generan con el sistema completo. Esto evita la circularidad ABM≡ODE y permite que la ablación del coupling pruebe genuinamente la constricción macro.

LoE = 2 (datos sintéticos basados en parámetros publicados). La elevación a LoE = 4 requiere datasets de captura de movimiento humano (VENLab Brown, WALK-MS, OpenLocomotionData) y queda como entregable del programa de extensión.

## Hipótesis específicas

| Hipótesis | Enunciado |
|-----------|-----------|
| H30.1 | EDI significativo bajo permutación (p < 0.05) |
| H30.2 | EDI > 0.30 (Nivel 4: strong) |
| H30.3 | Controles internos rechazados |
| H30.4 | EDI comparable al de los strong del corpus |

## Resultado empírico

**EDI = 0.2622** (p = 0.044 significativo, bootstrap CI = [0.2494, 0.2798]) — **Nivel 3 (weak)**.

| Métrica | Valor | Diagnóstico |
|---------|------:|-------------|
| EDI | **0.2622** | Componente funcional (weak) |
| p-value | 0.0440 | Significativo (p < 0.05) |
| Bootstrap CI | [0.2494, 0.2798] | Estrecho, no incluye cero |
| Permutación significativa | **True** | 999 permutaciones |
| val_steps | 35 | Ventana adecuada |
| RMSE coupled | 1.2462 | — |
| RMSE no_ode | 1.6890 | Sin coupling pierde señal |
| Coupling | 0.60 | Acoplamiento alto |
| Forcing scale | 0.99 | Forcing dominante |
| Viscosity | True | Resistencia a perturbación pasada |
| Non-locality | True | Difusión espacial pasada |
| Symploké CR | 1.0898 | Cohesión moderada |
| Correlación ABM-obs | 0.4264 | Modelo correlaciona con datos |
| Correlación ODE-obs | 0.3165 | Sonda macro correlaciona |

**Verificación bajo perfil agresivo** (n_perm=2999, n_boot=1500, n_refine=10000): EDI=0.2623, idéntico al perfil canónico. La señal es robusta bajo el aumento del costo computacional.

### Hipótesis evaluadas

| Hipótesis | Resultado | Comentario |
|-----------|:---------:|------------|
| H30.1 (significancia p < 0.05) | **Confirmada** | p = 0.044 |
| H30.2 (EDI > 0.30, strong) | Rechazada | EDI = 0.262, weak |
| H30.3 (controles internos rechazados) | Pendiente | Trabajo futuro |
| H30.4 (comparable con strong corpus) | Confirmada con matiz | Comparable con Nivel 3 (Epidemiología, Movilidad), no Nivel 4 |

## Análisis del resultado

El caso 30 produce **señal weak genuina y significativa**: el cierre operativo de behavioral dynamics es real bajo este aparato, pero moderado. Comparable con epidemiología (0.130) y movilidad (0.128) del corpus. Tres factores explican por qué no alcanza Nivel 4:

### 1. Behavioral dynamics es genuinamente individual, no poblacional

La grilla 40×40 modela una población; la dinámica de Fajen-Warren describe un agente acoplado con su entorno. La constricción macro→micro del aparato EDI tiene su mejor expresión cuando hay población heterogénea. Para un agente, el margen de demostración es menor.

### 2. La constricción es bidireccional, no jerárquica

El aparato EDI mide constricción top-down (macro restringe micro). Behavioral dynamics es acoplamiento horizontal organismo↔entorno, donde ambos co-evolucionan. La operacionalización vía EDI captura sólo el componente direccional, lo que limita la magnitud detectable.

### 3. La escala temporal favorece al forcing exógeno

Con 121 puntos mensuales y `forcing_scale=0.99`, el componente exógeno explica gran parte de la varianza. El componente `macro_coupling=0.60` es alto pero el aparato atribuye más varianza al forcing. En behavioral dynamics real (segundos), el balance puede ser distinto.

## Implicaciones para la tesis

### A. Behavioral dynamics se admite como Nivel 3 (weak) en el corpus

Con EDI = 0.262 significativo, behavioral dynamics es **componente funcional bajo el aparato EDI**, análogo a epidemiología y movilidad del corpus. Entra en la matriz comparativa del manuscrito junto a los otros casos weak.

### B. El protocolo EDI tiene rendimiento honesto en escala behavioral

El aparato detecta cierre operativo significativo donde la teoría de Fajen-Warren predice constricción informacional, pero el grado es moderado. Esto es coherente con la posición filosófica del manuscrito: el protocolo no glorifica ni rechaza arbitrariamente; **clasifica con precisión**.

### C. Demostración cualitativa y cuantitativa coexisten

La demostración cualitativa de Warren (2006, r²=0.980) y el caso 30 cuantitativo (EDI=0.262 weak) describen el mismo fenómeno desde aparatos distintos. Ambos son válidos: Warren en escala temporal corta de comportamiento individual; EDI en escala temporal larga de dinámica poblacional. La complementariedad es feature, no bug.

## Programa de elevación a Nivel 4 (strong)

Para que el caso 30 alcance `overall_pass=True`:

1. **Datos humanos reales:** integrar dataset de captura de movimiento (VENLab Brown, WALK-MS, OpenLocomotionData).
2. **Resolución temporal coherente:** adaptar el pipeline EDI para series de alta frecuencia (segundos-milisegundos).
3. **Múltiples agentes humanos:** ABM con N agentes humanos heterogéneos en lugar de retícula homogénea.
4. **Forcing experimental:** cambios de meta documentados en paradigmas reales (steering tasks, obstacle avoidance).
5. **Multi-sonda:** comparar `behavioral_attractor` con τ-dot (Lee 1976), optic flow expansion, mass-spring. Verificar convergencia.

Trabajo estimado: 6-12 meses con dedicación parcial y acceso a datasets de captura de movimiento.

## Conexión con el manuscrito

- **Capítulo 02-04 (nivel B):** este caso opera explícitamente el sistema dinámico acoplado agente-entorno.
- **Capítulo 03-01 (aparato):** instancia los cinco operadores μ, G, H, κ, ε.
- **Capítulo 03-04 (κ empírico):** demuestra κ vía baja dimensionalidad bajo metodología EDI.
- **Capítulo 04-01 (debates):** discriminación cuantitativa contra modelos internos.
- **Capítulo 05-05:** este caso es la versión cuantitativa de la demostración cualitativa de Warren 2006 en el manuscrito.

## Cómo ejecutar

```bash
cd 09-simulaciones-edi
source .venv/bin/activate
cd 30_caso_behavioral_dynamics/src
python3 validate.py
```

Tiempo aproximado en CPU 32 hilos: 2-5 minutos.

## Limitaciones reconocidas

1. **Datos sintéticos:** la elevación a LoE=4 requiere datos humanos reales.
2. **Sonda única:** programa multi-sonda como trabajo futuro.
3. **Retícula homogénea:** ABM modela población homogénea; behavioral dynamics es individual.
4. **Sin obstáculos:** este caso modela locomoción a meta sin obstáculo. La extensión con repulsores queda como trabajo futuro.

## Referencias

- Fajen, B. R., & Warren, W. H. (2003). Behavioral dynamics of steering, obstacle avoidance, and route selection. *Journal of Experimental Psychology: Human Perception and Performance, 29*(2), 343-362.
- Warren, W. H. (2006). The dynamics of perception and action. *Psychological Review, 113*(2), 358-389.

## Trazabilidad

Las decisiones metodológicas, versiones de la sonda, ajustes de parámetros y verificaciones de robustez quedan documentadas en `Bitacora/`. La fuente de verdad del manuscrito es `outputs/metrics.json` versionado en este directorio.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-21-aplicaciones-programaticas---mente-memoria-yo"></div>

# Mente, memoria y yo

## MODO PROGRAMÁTICO

Este capítulo presenta una aplicación en **modo programático** según el capítulo 05-00. Articula una conjetura de aplicación del marco material-relacional al dominio mente / memoria / yo, con criterios explícitos de elevación a modo demostrativo. No demuestra; conjetura con plan de prueba.


## Conjetura del capítulo

> Las categorías `mente`, `memoria` y `yo` son compresiones de patrones de integración multivariable cuyos atractores son empíricamente identificables si se dispone de tareas adecuadas y datos cuantitativos. La conjetura programática es que en cada caso el dossier completo es construible: variables a nivel B, atractores con cuenca y bifurcaciones, predicción discriminante contra cognitivismo simbólico, intervención discriminante. La elevación a demostrativo requiere construir tareas y datos que no están disponibles en este manuscrito.

## 1. La categoría `mente`

### 1.1. Recorte heredado

En el lenguaje común, `mente` aparece como interioridad unificada o sede de facultades.

### 1.2. Hipótesis de auditoría

La conjetura: la mente es atractor de integración entre múltiples subsistemas materialmente realizados. No es sustancia separada; tampoco es etiqueta vacía. Es patrón que comprime la coordinación material entre:

- actividad neural;
- organización corporal y biomecánica;
- acoplamiento sensorimotor;
- historia del organismo (desarrollo, aprendizaje);
- entorno técnico, lingüístico y social;
- regulación afectiva;
- capacidad de aprendizaje y orientación práctica.

### 1.3. Variables candidatas (X)

Para una pregunta Q sobre integración cognitiva sostenida, X podría incluir:

- variables conductuales: tasa de éxito en tareas cognitivas, latencia, errores, transferencia entre tareas;
- variables fisiológicas: dinámicas EEG/MEG en bandas relevantes, conectividad funcional;
- variables ecológicas: complejidad de tarea, restricciones contextuales;
- variables históricas: experiencia previa, fase de aprendizaje;
- variables corporales: postura, respiración, estado autonómico.

### 1.4. Atractores conjeturados

Patrones de integración sostenida que estabilizan la conducta cognitiva bajo perturbación; bifurcaciones entre regímenes (atención sostenida → distracción; vigilia → sueño; estado focalizado → mente errante).

### 1.5. Rival principal

Cognitivismo simbólico clásico: la mente es procesador de símbolos sobre representaciones internas, su descripción adecuada está en el nivel del software. La discriminación se haría en tareas donde el acoplamiento dinámico predice la transición entre regímenes con menos parámetros que el procesamiento simbólico postulado.

### 1.6. Criterio de elevación a demostrativo

Construir tarea cognitiva donde:

- haya atractores conductuales identificables empíricamente con dimensionalidad efectiva baja;
- haya bifurcación predecible entre regímenes;
- haya intervención (cambio en restricción ecológica, en acoplamiento corporal, en historia inmediata) que produzca transición predecible;
- haya rival cognitivista articulado con sus parámetros, y haya diferencia de varianza explicada o de capacidad predictiva.

Candidatos prometedores: sostenimiento de atención, alternancia entre tareas, integración perceptual cross-modal, decisión bajo restricción temporal.

### 1.7. Resultado conjeturado

La categoría `mente` se admite como compresión legítima en S si el dossier completo se construye. No se elimina; se reformula como atractor de integración.

## 2. La categoría `memoria`

### 2.1. Recorte heredado

La memoria se imagina habitualmente como depósito, archivo o contenedor de información pasada.

### 2.2. Problema

Esa imagen reifica una familia heterogénea de procesos como cosa homogénea.

### 2.3. Hipótesis de auditoría

La memoria no es objeto. Es disposición relacional: capacidad del sistema acoplado de modificar su trayectoria actual en función de trazas pasadas materialmente sostenidas. Los procesos componentes:

- codificación;
- consolidación;
- reactivación / recuperación;
- reconsolidación;
- uso práctico (modificación de conducta presente);
- dependencia de contexto.

### 2.4. Variables candidatas

- conductuales: tasa de recuerdo bajo manipulación de claves contextuales, sensibilidad a interferencia, transferencia bajo cambio de contexto;
- fisiológicas: dinámicas hipocampales, sincronía cortical;
- ecológicas: similitud entre contexto de codificación y de prueba;
- históricas: tiempo desde codificación, frecuencia de reactivación;
- de tarea: criterios de éxito específicos.

### 2.5. Atractores conjeturados

Estados estables de coordinación entre subsistemas que sostienen modulaciones específicas de conducta. La diferencia entre `memoria episódica`, `memoria de trabajo` y `memoria procedimental` se reformularía como diferencia entre tipos de atractor con distintas escalas temporales y distintas variables de control.

### 2.6. Rival principal

Modelo de memoria como almacén con buffers (modelo modal Atkinson-Shiffrin y descendientes). Discriminación: el modelo de almacén predice fronteras nítidas entre buffers; el modelo dinámico predice gradualidad y dependencia contextual. Los datos publicados en la literatura sobre interferencia, forgetting y reconsolidación favorecen modelo dinámico, pero la discriminación cuantitativa fina queda como trabajo posterior.

### 2.7. Criterio de elevación

Construir paradigma donde se pueda manipular específicamente:

- el contexto de codificación (variable ecológica);
- el régimen de reactivación (variable interventiva);
- la historia inmediata (variable temporal);

y comparar predicciones del modelo dinámico contra modelo de almacén con criterios públicos de varianza explicada y capacidad de generalización.

### 2.8. Resultado conjeturado

`Memoria` se admite como rótulo compresivo de una familia de atractores con dependencia contextual, escala temporal y variable de control específicas para cada subtipo. La categoría se conserva como abreviatura útil con marca de uso.

## 3. La categoría `yo`

### 3.1. Recorte heredado

El yo aparece como centro simple, sustancia interior, núcleo de identidad.

### 3.2. Hipótesis de auditoría

El yo no es ilusión completa ni sustancia simple. Es atractor dinámico de integración multivariable con cuenca persistente bajo transformación. Sus dimensiones:

- integración corporal (propiocepción, esquema corporal);
- continuidad narrativa (autobiografía);
- reconocimiento social (otros me reconocen como el mismo);
- hábitos de acción (repertorios estables);
- memoria autobiográfica;
- afectividad (regulación emocional sostenida);
- capacidad reflexiva;
- inscripción temporal (sentido del tiempo personal).

### 3.3. Variables candidatas

- conductuales: consistencia de respuesta bajo cambio de contexto, perfil de preferencia, repertorio motor;
- corporales: integración propioceptiva-visual, sentido de agencia;
- narrativas: coherencia de relatos autobiográficos;
- sociales: reconocimiento intersubjetivo;
- afectivas: patrones de regulación;
- temporales: sentido de continuidad biográfica.

### 3.4. Atractores conjeturados

Patrones de integración corporal-narrativa-social-afectiva con cuenca persistente bajo transformación biográfica. Bifurcaciones: rupturas biográficas, despersonalización, transiciones de identidad.

### 3.5. Rival principal

Posiciones que tratan el yo como ilusión narrativa pura (algunas variantes de Dennett en versión fuerte) o como sustancia metafísica simple (cartesianismo). La tesis discrimina contra ambos: el yo es realidad estructural — atractor dinámico — no ilusión ni sustancia.

### 3.6. Criterio de elevación

Construir caso donde el atractor de integración se desestabiliza específicamente (despersonalización clínica, alteraciones del esquema corporal en condiciones experimentales, ilusiones de propiedad como rubber hand illusion) y mostrar que el modelo dinámico predice la cuenca de transición con más precisión que rivales.

### 3.7. Resultado conjeturado

`Yo` se admite como atractor dinámico de integración con cuenca persistente. La categoría se mantiene como compresión legítima si el dossier se construye.

## 4. Compresión y expansión en este dominio

### Compresión legítima

En explicación psicológica general, hablar de `memoria de trabajo` como módulo unitario es compresión razonable cuando la pregunta es comparación de tareas globales.

### Expansión necesaria

Si la pregunta es por qué dos sujetos fallan de modo diferente en la misma tarea, la compresión `memoria de trabajo` puede ser excesiva y debe abrirse en:

- capacidad de mantenimiento activo;
- interferencia contextual;
- control atencional;
- carga afectiva;
- historia de aprendizaje específica.

La regla del capítulo 03-02 aplica: comprimir cuando el detalle interno no cambia la inferencia, expandir cuando sí la cambia.

## 5. Qué evita el marco en este dominio

**Tabla 5.1.1.**

| Tentación | Razón del rechazo |
|---|---|
| Dualismo cartesiano | No requiere mente separada del cuerpo o el entorno |
| Reduccionismo neural plano | La actividad neuronal no agota la organización corporal-ambiental-social-temporal |
| Eliminativismo apresurado | Las categorías mentales pueden ser compresiones legítimas si pasan auditoría |
| Cognitivismo simbólico desligado de B | La traducibilidad B↔L3 es obligatoria |
| Funcionalismo abstracto | La realización múltiple no exime de anclaje en B |

## 6. Diálogo con interlocutores

### 6.1. Dennett — patrones reales y centro de gravedad narrativo

Dennett ofrece la noción de patrón real y la imagen del yo como centro de gravedad narrativo. La tesis recoge ambas y exige más: el patrón debe ser atractor con cuenca medible; el yo es atractor de integración dinámica, no solo narrativa.

### 6.2. Varela, Thompson y Rosch — embodied mind

Embodied mind es aliada principal. La tesis se inscribe en su horizonte general y añade el filtro de admisión y la operacionalización de κ.

### 6.3. Andy Clark — extended mind

Clark insiste en que algunos procesos cognitivos se extienden al entorno técnico. La tesis lo opera: el entorno técnico entra en X cuando la tarea lo exige.

### 6.4. Alva Noë — percepción enactiva

Noë sostiene que la percepción es habilidad práctica para navegar el entorno. La tesis lo recoge como caso de acoplamiento informacional sin representación interna como recurso primario, alineado con Warren en behavioral dynamics.

### 6.5. Searle — naturalismo biológico

Searle defiende que la mente es propiedad biológica del cerebro. La tesis difiere: la mente es propiedad del sistema acoplado organismo-entorno-tarea-historia, no solo del cerebro. Searle es interlocutor con punto de fricción claro.

### 6.6. Sellars y Wittgenstein — crítica de reificación

Ambos como antídoto permanente contra reificación gramatical de categorías mentales.

## 7. Dimensión fenomenológica y qualia

Una ontología que se afirma **general** debe tener postura sobre la **experiencia subjetiva**. La tesis adopta **complementarismo metodológico**: la fenomenología en primera persona y el aparato EDI en tercera persona son **métodos diferentes para fenómenos distintos pero ontológicamente continuos**.

### 7.1. Postura sobre los qualia

- Los qualia (cualidades fenoménicas: el rojo del rojo, el dolor del dolor) **NO se reducen a atractores conductuales** ni a estados neurales descriptos en tercera persona;
- pero **NO requieren sustancia mental separada** (la tesis es naturalista no-reduccionista, cap 02-01 §0.1);
- los qualia son **propiedades constitutivas** del sistema acoplado organismo-mundo bajo el aspecto en primera persona;
- esto se alinea con Thompson (2007, *Mind in Life*, cap. 11, p. 312): *"experience is not in the head, but in the world enacted by the embodied mind"*.

### 7.2. El "problema duro" de Chalmers

Chalmers (1995, *Journal of Consciousness Studies* 2:200-219) plantea que ningún relato funcional explica por qué hay experiencia. La tesis responde:

- el aparato EDI **no resuelve** el problema duro: ese no es su propósito;
- el aparato describe la dinámica conductual-acoplada (tercera persona); no agota la realidad fenomenológica;
- la **complementariedad** con métodos fenomenológicos (Husserl 1913 *Ideas I*, Merleau-Ponty 1945 *Fenomenología de la percepción*, Varela neurofenomenología) es una característica de diseño, no un fallo;
- la tesis ofrece **co-existencia disciplinada** entre tercera y primera persona, no eliminación de una por la otra.

### 7.3. Diálogo textual extendido

- **Husserl** (1913, *Ideas I*, §49, p. 92 ed. Springer): *"jede Erlebnis ist Bewusstsein, y Bewusstsein ist Bewusstsein von etwas"*. La tesis recoge: la conciencia es **intencional**, dirigida a contenido. Esto es compatible con la tesis: la intencionalidad es propiedad del sistema acoplado organismo-mundo en primera persona.
- **Merleau-Ponty** (1945, *Fenomenología de la percepción*, p. xi ed. Gallimard): *"le corps est notre moyen général d'avoir un monde"*. La tesis lo recoge: el cuerpo es el **acoplador material** que constituye el mundo experimentado.
- **Nagel** (1974, "What is it Like to be a Bat?", *Philosophical Review* 83:435-450, p. 436): el carácter subjetivo de la experiencia *"will not be adequately captured by any of the familiar, recently devised reductive analyses of the mental"*. La tesis recoge: el aparato EDI **no captura el carácter subjetivo**, pero esto no debilita su validez en su régimen propio.

## 8. Sujeto, agencia, libertad

### 8.1. Compatibilismo dennettiano matizado

La tesis adopta **compatibilismo**: la libertad humana es compatible con determinismo material si por libertad entendemos **capacidad de control reflexivo** del propio comportamiento, no contracausalidad metafísica. Dennett (2003, *Freedom Evolves*, cap. 2, p. 56) lo articula: *"a free choice is one made for reasons, by an agent who can reflect on those reasons"*.

### 8.2. Estructura del agente en la tesis

- El agente es **atractor de integración** corporal-narrativa-social-afectiva (cap 02-03 §8.5);
- la agencia es **propiedad operativa del atractor**: el sistema acoplado organismo-entorno-tarea-historia tiene capacidades de selección reflexiva entre alternativas;
- la libertad NO es contracausal; es **capacidad de control reflexivo** materialmente realizada.

### 8.3. Posiciones rivales en libertad

- **Frankfurt** (1971, "Freedom of the Will and the Concept of a Person", *Journal of Philosophy* 68:5-20): la libertad es jerarquía de deseos. La tesis recoge: el atractor humano tiene **estructura jerárquica** de variables que opera como deseos sobre deseos.
- **Pereboom** (2001, *Living Without Free Will*) defiende eliminativismo de la libertad. La tesis lo rechaza por incompatible con el realismo moderado de patrones materialmente sostenidos.

## 9. Lo que este capítulo devuelve a la tesis general

Este dominio prueba que el aparato puede tratar fenómenos clásicamente difíciles sin recaer en dualismo, reduccionismo o eliminativismo. La conjetura es articulada y elevable. La asimetría con el caso ancla canónico se nombra: faltan datos cuantitativos publicados de la calidad de Warren en este dominio. El programa posterior es claro.

## 10. Limitación honesta

Este capítulo conjetura. No demuestra. La elevación a modo demostrativo requiere construir tareas y datos que no están en el manuscrito. La tesis no presenta este dominio como prueba; lo presenta como aplicación articulada con plan.

## 11. Cierre

> La mente no es cosa adicional al organismo, pero tampoco se deja agotar por una lista plana de eventos neuronales. Es atractor de integración corporal-cognitivo-afectivo-social-histórico cuya legitimidad como compresión depende de qué integra, qué conserva, para qué pregunta sirve, y qué predicción discriminante propone respecto a rivales identificables.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-22-aplicaciones-programaticas---biologia-y-ecologia"></div>

# Biología y ecología

## 0. Qué es vida en esta ontología

Antes de tratar biología y ecología como dominios programáticos, fijamos lo que la tesis afirma sobre **vida** como categoría ontológica. La pregunta de Schrödinger (1944, *¿Qué es la vida?*) — ¿qué hace que una entidad sea viva? — recibe en la tesis respuesta articulada:

### 0.1. Postura: vida como atractor autopoiético material

Una entidad **viva** es un **atractor autopoiético materialmente sostenido** que cumple cinco condiciones:

1. **cierre operacional**: el sistema produce los componentes que lo constituyen (Maturana-Varela 1980, *Autopoiesis and Cognition*, p. 79);
2. **acoplamiento estructural**: mantiene su organización bajo perturbación del entorno con tolerancia identificable (cap 02-04 §3);
3. **metabolismo material**: intercambia materia y energía con el entorno preservando su forma (Schrödinger 1944, p. 76: la vida se mantiene "negentropía");
4. **reproducción** (en sentido amplio: replicación, división, transmisión de información estructural): el patrón se transmite a nuevos sustratos;
5. **historia evolutiva**: la organización tiene origen en linajes con descendencia con modificación.

Las cinco condiciones **se traducen al aparato**: cierre operacional = atractor con cuenca persistente bajo perturbación; metabolismo = acoplamiento dinámico abierto; reproducción = transmisión de variables que el aparato puede modelar; historia = entrada de variables históricas en B.

### 0.2. Diálogo

- **Maturana-Varela** (1980, p. 78): la autopoiesis es *"el cierre operacional que define la organización viva"*. La tesis recoge directamente.
- **Kauffman** (1993, *The Origins of Order*, cap. 7): la vida emerge en redes autocatalíticas con propiedades de orden espontáneo. Compatible con la tesis: las redes autocatalíticas son atractores en el sustrato químico-material.
- **Margulis** (1998, *Symbiotic Planet*): la vida es esencialmente simbiótica. La tesis recoge: el "agente" en B (cap 02-04) es típicamente sistema acoplado de subsistemas, no entidad aislada.

### 0.3. Implicación

La distinción vivo/no-vivo NO es ontológicamente abrupta — hay gradientes (virus, viroides, priones). La tesis afirma que **el aparato puede operar a lo largo del gradiente** detectando cierre operativo donde lo haya. Casos del corpus inter-escala (33 Villin, 34 MM, 35 ciclo celular, 36 NF-κB) operan en este gradiente: instancian biología sin necesidad de definir vida como esencia separada.

## MODO PROGRAMÁTICO

Aplicación en **modo programático** según el capítulo 05-00. Articula una conjetura de aplicación del marco a fenómenos biológicos y ecológicos, con criterios de elevación. No demuestra.


## Conjetura del capítulo

> Célula, organismo y ecosistema son atractores de sistemas dinámicos acoplados de creciente complejidad cuya realidad como patrones se verifica por estabilidad bajo perturbación, cuenca medible, bifurcaciones identificables, y predicción discriminante contra rivales reduccionistas o holistas. La elevación a demostrativo requiere identificar atractores con datos publicados específicos en cada subdominio.

## 1. La célula

### 1.1. Recorte heredado

La célula como unidad básica de lo vivo.

### 1.2. Hipótesis de auditoría

La célula es atractor de organización con cuenca persistente bajo recambio molecular. Las componentes:

- membrana (frontera dura);
- metabolismo (dinámica);
- intercambio con el entorno (acoplamiento);
- señalización (información intracelular);
- regulación (leyes de control);
- reproducción (transición a otros atractores);
- acoplamiento con el medio extracelular.

### 1.3. Variables candidatas

- concentraciones moleculares clave;
- flujos metabólicos;
- estados de transcripción;
- señales químicas;
- propiedades mecánicas de membrana;
- estado del entorno inmediato.

### 1.4. Atractores conjeturados

Estados estables de homeostasis bajo régimen ambiental específico; bifurcaciones entre tipos celulares (diferenciación); transiciones de fase (apoptosis, mitosis).

### 1.5. Compresión y expansión

- compresión legítima: tratar la célula como nodo en modelos tisulares cuando la pregunta es estructura de tejido;
- expansión necesaria: abrir la célula en su red metabólica cuando la pregunta es regulación específica.

### 1.6. Criterio de elevación

Identificar caso publicado donde un modelo dinámico de baja dimensionalidad sobre subred metabólica reproduzca trayectorias observadas con bifurcación de diferenciación celular, y discrimine contra modelo reduccionista plano (todos los detalles moleculares) o modelo holista (la célula sin más).

## 2. El organismo

### 2.1. Recorte heredado

El organismo como cosa unitaria, simultáneamente proceso abierto de intercambio.

### 2.2. Hipótesis de auditoría

El organismo es atractor de continuidad organizada bajo recambio metabólico, regulación interna, acoplamiento con el entorno y dependencia histórica del desarrollo. Su identidad es continuidad estructural, no permanencia molecular.

### 2.3. Variables candidatas

- regulación interna (homeostasis);
- intercambio energético con el entorno;
- coordinación funcional entre subsistemas;
- estado del desarrollo;
- adaptación al ambiente actual.

### 2.4. Atractores y bifurcaciones

Estados estables de fisiología (vigilia, sueño, regímenes metabólicos); bifurcaciones (estrés, enfermedad, recuperación).

### 2.5. Rival principal

Reduccionismo molecular fuerte (todo es bioquímica) y vitalismo residual (algo en el organismo escapa la materialidad). La tesis discrimina contra ambos: el organismo es atractor materialmente realizado y empíricamente verificable.

### 2.6. Criterio de elevación

Construir caso de regulación fisiológica con bifurcación documentada (transición sueño-vigilia, transición de desarrollo, respuesta al estrés agudo) y mostrar que el modelo dinámico predice la transición con más economía que el modelo reduccionista o el holista.

## 3. La especie

### 3.1. Recorte heredado

La especie como categoría taxonómica básica, a veces tratada como esencia, a veces como mera convención clasificatoria.

### 3.2. Hipótesis de auditoría

La especie es patrón histórico-biológico estabilizado por reproducción, descendencia, variación y selección bajo restricciones ambientales. No es esencia inmóvil ni convención libre.

### 3.3. Variables candidatas

- distribución de fenotipos;
- estructura genética poblacional;
- redes de interacción reproductiva;
- distribución espacial;
- historia evolutiva.

### 3.4. Compresión y expansión

- compresión legítima: tratar la especie como unidad en modelos ecológicos cuando la pregunta es interacción entre poblaciones;
- expansión necesaria: abrir la especie en variación intraespecífica, plasticidad fenotípica, microbioma cuando la pregunta es adaptación local.

### 3.5. Rival principal

Esencialismo de especies y nominalismo taxonómico. La tesis discrimina con realismo estructural moderado: las especies son atractores reales de poblaciones bajo restricciones de reproducción y selección, sin esencia.

### 3.6. Criterio de elevación

Construir caso donde la transición especiación se modele dinámicamente con bifurcación identificable en datos publicados.

## 4. El ecosistema

### 4.1. Recorte heredado

A veces como entidad homogénea, a veces como suma de especies.

### 4.2. Hipótesis de auditoría

El ecosistema es red material de interacciones entre organismos, clima, suelo, agua, energía, nutrientes, perturbaciones históricas y actividad humana. No es sustancia separada ni inventario aditivo.

### 4.3. Variables candidatas

- abundancias poblacionales;
- flujos energéticos;
- ciclos biogeoquímicos;
- estructura de interacciones tróficas;
- variables climáticas;
- impacto antropogénico.

### 4.4. Atractores y bifurcaciones

Estados estables del ecosistema bajo régimen climático y de perturbación; bifurcaciones (regime shifts) entre estados alternativos. La literatura sobre regime shifts en ecología (Scheffer y colegas) es donde el caso programático puede elevarse a demostrativo más fácilmente.

### 4.5. Rival principal

Holismo ecológico inflado (Gaia como sustancia) y reduccionismo poblacional (solo especies aisladas). La tesis discrimina con red de hipergrafos que captura acoplamientos múltiples.

### 4.6. Criterio de elevación

Adoptar caso publicado de regime shift (lake eutrophication, coral reef bleaching, savana-bosque) y mostrar que el modelo dinámico hipergrafo discrimina contra rivales con datos cuantitativos.

## 5. Qué enseña este dominio sobre los niveles

La misma realidad puede tratarse en distintas resoluciones:

- moléculas → orgánulos → células → tejidos → organismos → poblaciones → comunidades → ecosistemas → biomas.

La tesis no privilegia ninguno como único verdadero. Cada nivel se justifica por la estructura que conserva para una pregunta dada. El criterio de cambio de escala (capítulo 03-02 §6) opera con precisión en este dominio.

## 6. Qué evita el marco en este dominio

**Tabla 5.2.1.**

| Tentación | Razón del rechazo |
|---|---|
| Esencialismo biológico | Categorías como especie o función no son esencias inmóviles |
| Reduccionismo molecular | La lista de moléculas no agota regulación, forma, función o organización ecológica |
| Holismo nebuloso | La red ecológica no es totalidad mística; es conjunto de dependencias modelables |
| Vitalismo | No requiere fuerza vital adicional; self-organization (cap 02-04 §4, Maturana-Varela 1980 y Haken 1977) explica organización sin sustancia nueva |

## 7. Diálogo con interlocutores

### 7.1. Nicholson y Dupré — biología procesual

Defienden que la unidad biológica básica es proceso, no cosa. La tesis lo recoge: organismo como atractor procesual.

### 7.2. Evelyn Fox Keller — organización biológica

Plantea los límites del reduccionismo lineal y la complejidad de la organización biológica. La tesis converge en el énfasis en organización.

### 7.3. Bechtel y Craver — mecanicismo en biología

El mecanicismo multinivel es aliado natural en biología. La tesis se inscribe en su tradición con el filtro adicional de dossier.

### 7.4. Maturana y Varela — autopoiesis

La autopoiesis se reformula como cuenca de atracción persistente bajo perturbación con tolerancia explícita.

### 7.5. Scheffer y colegas — regime shifts

Aliados empíricos: muestran cómo identificar bifurcaciones ecológicas con datos. El caso programático de ecosistemas se elevaría con su trabajo como base.

## 8. Lo que este capítulo devuelve a la tesis general

Demuestra que el marco puede:

- defender materialidad sin fisicalismo estrecho;
- sostener niveles sin mundos independientes;
- explicar identidad como continuidad organizada bajo recambio;
- justificar uso alternado de compresión y expansión según pregunta.

Y articula explícitamente que la elevación a modo demostrativo está al alcance: la literatura de regime shifts ecológicos y de modelos dinámicos en biología regulatoria ofrece material publicado para construir dossiers completos.

## 9. Limitación honesta

Este capítulo conjetura. La elevación a modo demostrativo requiere adoptar un caso específico publicado con datos cuantitativos y construir el dossier completo. El programa posterior se prioriza en capítulo 06-03.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-23-aplicaciones-programaticas---sistemas-tecnicos-distribuidos"></div>

# Sistemas técnicos distribuidos

## MODO PROGRAMÁTICO

Aplicación en **modo programático** según el capítulo 05-00. La presentación del fenómeno es robusta y el aparato se opera con claridad pedagógica, pero falta el modelo dinámico cuantitativo con datos públicos que eleve el caso a demostrativo.


## Conjetura del capítulo

> Los sistemas técnicos distribuidos son patrones materialmente sostenidos cuya disponibilidad, latencia y modos de fallo se modelan dinámicamente con acoplamientos múltiples. La conjetura es que el aparato del marco mejora el diagnóstico y la predicción de fallo respecto a vistas estáticas (arquitectura como diagrama) o reduccionistas (todo es hardware). La elevación a demostrativo requiere caso específico con datos de telemetría públicos y modelo dinámico cuantitativo.

## 1. La categoría `servicio`

### 1.1. Recorte heredado

En la práctica cotidiana se dice `el servicio está arriba`, `el servicio cayó`, `el servicio responde lento`.

### 1.2. Hipótesis de auditoría

`Servicio` es compresión operativa legítima cuando la pregunta es disponibilidad global, arquitectura, frontera funcional, responsabilidad organizativa. Es compresión que oculta cuando la pregunta es diagnóstico fino. La regla del capítulo 03-02 (compresión cuando el detalle no cambia inferencia, expansión cuando sí) opera con claridad.

### 1.3. Reconstrucción material

Un servicio depende de:

- procesos en máquinas;
- red entre máquinas;
- rutas y DNS;
- certificados TLS;
- balanceadores de carga;
- almacenamiento (bases de datos, colas);
- autenticación y autorización;
- configuración y despliegues;
- monitoreo y observabilidad;
- usuarios y patrones de tráfico;
- dependencias externas.

### 1.4. Variables candidatas (X)

- latencia (p50, p99) por endpoint;
- throughput;
- error rate por tipo;
- saturación de recursos (CPU, memoria, IO, red);
- profundidad de cola;
- validez de certificados;
- tiempo de resolución DNS;
- estado de despliegues recientes.

### 1.5. Atractores conjeturados

- estado estable de operación nominal con latencia y error rate dentro de SLO;
- estados degradados (latencia elevada pero servicio funcional);
- estado de fallo total (servicio caído).

### 1.6. Bifurcaciones

- transiciones entre estados (saturación cascada, fallo de dependencia, expiración de certificado);
- regímenes biestables donde pequeñas perturbaciones empujan al sistema entre operación y degradación.

### 1.7. Compresión y expansión en la práctica

- compresión legítima al describir arquitectura general: `el servicio sirve requests`;
- expansión necesaria al diagnosticar fallo: `¿falló DNS, TLS, persistencia, autenticación, dependencia externa, despliegue, configuración, capacidad?`;
- la práctica de incident response implementa esta dialéctica.

## 2. Hipergrafo de dependencias

Los sistemas distribuidos requieren H, no solo G binario. Razones:

- fallos cascada involucran múltiples servicios simultáneamente;
- restricciones de capacidad afectan conjuntos de operaciones;
- timeouts y retry policies acoplan dinámicas no binarias.

La modelización con hipergrafo permite representar grupos de servicios que comparten infraestructura, cuyas fallas se correlacionan no por dependencia directa sino por restricción global compartida.

## 3. Rival principal

Vistas estáticas de arquitectura (diagramas de servicios sin dinámica) y aproximaciones físicalistas absurdas (todo es electrones, transistores). Ninguna captura la dinámica acoplada que produce los fallos reales.

## 4. Criterio de elevación a demostrativo

Adoptar caso publicado o construible con datos:

- telemetría completa (logs, métricas, traces) de servicio distribuido durante un incidente;
- ajuste de modelo dinámico de bajo orden sobre indicadores clave;
- predicción de cascada con respecto a tiempo de respuesta;
- intervención discriminante: estrategia de circuit breaker con parámetros derivados del modelo dinámico contra estrategia ad hoc.

Candidatos: SRE journals con post-mortems publicados, datasets de Google Borg, traces de Microsoft Azure publicados con permisos.

## 5. Qué evita el marco en este dominio

**Tabla 5.3.1.**

| Tentación | Razón |
|---|---|
| Reificado técnico | No tratar `la plataforma`, `la app` o `el backend` como cosas simples |
| Reduccionismo físico absurdo | Nadie diagnostica caída de producción describiendo electrones |
| Diagramas estáticos sin dinámica | Las arquitecturas no operan en estado estático; viven dinámica |
| Modelado solo de happy path | Los fallos en sistemas distribuidos son cualitativos, no cuantitativos lineales |

## 6. Diálogo con interlocutores

### 6.1. Simondon — modo de existencia de los objetos técnicos

Simondon ofrece la categoría de individuación técnica y de objetos técnicos como concretizaciones de tendencias. La tesis lo opera: un servicio es individuación técnica cuya identidad depende de su funcionamiento sostenido en red.

### 6.2. Latour — actantes y redes

Latour insiste en redes con humanos y no-humanos. La tesis aplica: los componentes técnicos son actantes que entran en `V` si pasan filtro de admisión.

### 6.3. SRE / práctica de operaciones (Beyer y colegas)

Los principios de Site Reliability Engineering (definir SLO, error budgets, circuit breakers, blast radius limitation) son implementación informal de la auditoría ontológica del marco. La tesis los recoge como inspiración técnica.

## 7. Lo que este capítulo devuelve a la tesis general

Este caso es valioso pedagógicamente: muestra con claridad mínima de filosofía cómo opera la dialéctica compresión / expansión y por qué el modelo dinámico es preferible al diagrama estático. El servicio es real como patrón operativo, no como bloque autosuficiente; es nodo comprimido reabrible en hipergrafo de dependencias. La traducción al aparato es directa.

## 8. Limitación honesta

Este capítulo articula la conjetura con claridad, pero falta el modelo dinámico cuantitativo con datos públicos que eleve a demostrativo. La elevación es plausible y se prioriza en hoja de ruta.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-24-aplicaciones-programaticas---instituciones-mercado-estado"></div>

# Instituciones, mercado y Estado

## MODO PROGRAMÁTICO ACOTADO

Aplicación en **modo programático con alcance explícitamente acotado** según el capítulo 05-00. Este es el dominio con la deuda más significativa de la tesis: la dimensión normativa (validez, legitimidad, efectividad) exige desarrollo formal pendiente del aparato. Este capítulo declara su alcance con honestidad analítica:

- **Lo que sí ofrece:** un esquema conceptual coherente para tratar instituciones, mercados y Estado como atractores con cuenca persistente y bifurcaciones identificables, sin reificación ni reduccionismo;
- **Lo que reconoce como deuda:** la operacionalización formal de la dimensión normativa como variable del sistema acoplado, condición necesaria para elevar el capítulo de programático a demostrativo;
- **Lo que el comité debe esperar de este capítulo:** una contribución conceptual sólida y un plan de elevación con casos candidatos identificados, no una demostración cuantitativa del cierre operativo institucional.

La demostración cuantitativa de la dimensión normativa queda explícitamente fuera del alcance del manuscrito actual y se documenta como deuda priorizada en `06-cierre/03-hoja-de-ruta-para-tesis-final.md` y en `Bitacora/2026-04-28-cierre-doctoral/`.


## Conjetura del capítulo

> Las instituciones, los mercados y el Estado son patrones materialmente sostenidos por prácticas, normas, soportes inscritos, infraestructuras y reconocimiento social que admiten formalización dinámica como atractores con cuenca persistente y bifurcaciones identificables (crisis, refundaciones, transiciones de régimen). La elevación a demostrativo requiere caso específico con datos históricos y modelo dinámico cuantitativo, así como desarrollo del aparato para tratar normatividad como variable.

## 1. La institución

### 1.1. Recorte heredado

Universidad, empresa, juzgado, Estado se nombran como sujetos unificados. El modo de hablar es práctico pero puede ocultar la red que los sostiene.

### 1.2. Hipótesis de auditoría

Una institución es atractor sostenido por:

- cuerpos (personas con roles);
- documentos y archivos (memoria material);
- edificios e infraestructura;
- tecnologías (de gestión, comunicación, registro);
- normas explícitas;
- sanciones organizadas;
- memoria organizacional;
- rutinas y prácticas repetidas;
- reconocimiento social;
- financiamiento;
- historia.

### 1.3. Variables candidatas

- variables estructurales: organigrama, distribución de autoridad, recursos disponibles;
- variables prácticas: frecuencia y contenido de rutinas;
- variables normativas: reglas explícitas vigentes;
- variables de reconocimiento: percepciones internas y externas;
- variables temporales: historia operativa.

### 1.4. Atractores conjeturados

Estados estables de funcionamiento institucional bajo régimen normativo y económico específico. Bifurcaciones: crisis, refundación, fusión, disolución.

## 2. El mercado

### 2.1. Recorte heredado

Expresiones como `el mercado decidió`, `el mercado teme`, `el mercado castiga` reifican.

### 2.2. Hipótesis de auditoría

Lo que se llama mercado es red dinámica de:

- agentes con incentivos heterogéneos;
- plataformas de intercambio;
- reglas (jurídicas, técnicas, convencionales);
- asimetrías de información;
- estructuras de propiedad;
- dinero como medio de cambio;
- confianza y reputación;
- coerción jurídica;
- infraestructura técnica;
- historia regulatoria.

### 2.3. Atractores y bifurcaciones

Estados estables de equilibrio de precios bajo régimen institucional; burbujas y crashes como bifurcaciones; transiciones de régimen regulatorio.

### 2.4. Rival principal

Tratamiento del mercado como sujeto metafísico con preferencias propias (versión inflada) o como suma de transacciones individuales sin estructura emergente (individualismo metodológico estricto). La tesis discrimina con red dinámica acoplada.

## 3. El Estado

### 3.1. Dificultad

El Estado parece entidad enorme, difusa y simultáneamente muy real.

### 3.2. Hipótesis de auditoría

Su realidad se sostiene por combinación articulada de:

- monopolio relativo de coerción legítima;
- aparato administrativo y burocrático;
- archivo y documentación;
- infraestructura territorial y de servicios;
- derecho positivo;
- cuerpos funcionarios con roles definidos;
- recursos fiscales;
- legitimación simbólica;
- continuidad histórica.

### 3.3. Atractores y bifurcaciones

Estados estables de gobernanza bajo régimen constitucional; crisis, golpes de Estado, refundaciones constitucionales como bifurcaciones; transiciones lentas (consolidación democrática, autoritarización).

### 3.4. Rival principal

Holismo trascendental (el Estado como espíritu objetivo) y reduccionismo individualista (solo individuos con preferencias). La tesis discrimina con realidad institucional como cuarto modo de realidad (capítulo 02-01).

## 4. Normatividad como dimensión específica

### 4.1. El problema

A diferencia de los demás dominios, aquí la dimensión normativa exige tratamiento específico: las normas no son meras correlaciones; tienen validez (independiente de cumplimiento), legitimidad (aceptación), efectividad (capacidad de orientar conducta).

### 4.2. Hipótesis del marco

Las normas son patrones materialmente sostenidos por:

- inscripción documental (constituciones, leyes, reglamentos);
- prácticas repetidas que las realizan;
- coerción organizada que las refuerza;
- lenguaje institucionalizado que las comunica;
- memoria histórica que las contextualiza;
- sistemas de sanción que las activan.

Esta hipótesis es plausible y converge con Bourdieu, Searle y Latour, pero su formalización dinámica completa está pendiente. Esta es la deuda principal del capítulo.

### 4.3. Conjetura operativa

La validez normativa se modelaría como cuenca de atracción del sistema institucional bajo perturbación: una norma es válida en la medida en que el sistema, perturbado, retorna a su cumplimiento. La efectividad se modelaría como tasa de retorno. La legitimidad se modelaría como anchura de la cuenca (resistencia a perturbaciones). Estas son conjeturas; su prueba requiere caso demostrativo.

## 5. Qué evita el marco en este dominio

**Tabla 5.4.1.**

| Tentación | Razón del rechazo |
|---|---|
| Hipóstasis institucional | No convertir instituciones en sujetos metafísicos autónomos |
| Individualismo metodológico estrecho | Reconocer que ciertas capacidades aparecen solo en configuraciones organizadas |
| Nominalismo social | Admitir realidad efectiva para patrones institucionales con efectos discriminantes |
| Sociologismo estructural | No reificar `estructura social` como sustancia independiente |

## 6. Diálogo con interlocutores

### 6.1. Searle — ontología social

Searle (1995, *The Construction of Social Reality*, p. 26) propone que los hechos institucionales emergen por aplicación de la fórmula constitutiva *"X cuenta como Y en el contexto C"*, sostenida por intencionalidad colectiva: *"institutional facts exist only because we believe them to exist"* (p. 32). En *Making the Social World* (2010, cap. 5) extiende la formulación incorporando "status functions" como mecanismo central.

La tesis recoge parcialmente esta arquitectura. Coincide en que la dimensión normativa es real, no epifenoménica. Discrepa en que prefiere tratar la intencionalidad colectiva no como una propiedad supraindividual primitiva sino como **cuenca de atracción de la coordinación material**: las normas se sostienen porque el sistema (cuerpos, documentos, sanciones, prácticas repetidas) tiene una dinámica que retorna al cumplimiento bajo perturbación. La diferencia es estructural: para Searle la intencionalidad colectiva es ontológicamente primitiva; para la tesis es derivable del acoplamiento material-relacional sin por ello disolverla en hechos brutos.

Esta es **fricción productiva**, no rechazo. La objeción searleana, *"si reduces la intencionalidad colectiva a coordinación material, pierdes la dimensión normativa propiamente dicha"* (paráfrasis del cap. 6 de Searle 2010), exige respuesta: la cuenca de atracción institucional es **normativamente eficaz** sin ser una entidad independiente; la efectividad normativa equivale al retorno del sistema al cumplimiento bajo perturbación, lo cual es medible empíricamente cuando hay datos.

### 6.2. Bourdieu — campos, habitus, prácticas

Bourdieu (1980, *Le sens pratique*, cap. 3) define el habitus como *"sistemas de disposiciones durables y transponibles, estructuras estructuradas predispuestas a funcionar como estructuras estructurantes"* (p. 88 ed. francesa, p. 92 ed. española Taurus 1991). En *Razones prácticas* (1994, cap. 2) los campos son espacios sociales con leyes propias, posiciones objetivas, capital específico.

Es el **aliado principal** del capítulo. La traducción al aparato de la tesis es directa y permite formalización rigurosa: campos = atractores funcionales con cuenca específica; habitus = disposiciones relacionales materialmente incorporadas (cuerpo, gestos, lenguaje); prácticas = trayectorias dinámicas en el campo. La cuenca persistente bajo perturbación que la tesis postula como criterio de validez normativa es, formalmente, lo que Bourdieu describe cualitativamente como *"persistencia del habitus aún cuando las condiciones objetivas que lo produjeron han cambiado"* (1980, p. 100).

Lo que la tesis añade a Bourdieu es **operacionalización cuantitativa**: la cuenca como objeto formal con anchura medible. Lo que Bourdieu añade a la tesis es la **historia y la genealogía**: las cuencas no son atemporales, son sedimentaciones históricas con trayectorias específicas.

### 6.3. Latour — actantes y ensamblajes

Latour (2005, *Reassembling the Social*, cap. 3) insiste en simétrica distribución de agencia entre humanos y no-humanos: *"action is dislocated. Action is borrowed, distributed, suggested, influenced, dominated, betrayed, translated"* (p. 46). En *Pandora's Hope* (1999, cap. 6) desarrolla la noción de actante como cualquier entidad que produce diferencia perceptible.

La tesis recoge la insistencia ontológica: las instituciones son ensamblajes que incluyen cuerpos, documentos, edificios, tecnologías, normas, prácticas. Cada actante entra al modelo si pasa el criterio de patrón material-relacional (capítulo 02-01). La fricción aparece en el grado de simetría: para Latour la simetría humano/no-humano es ontológicamente fuerte (un documento y una persona son actantes equivalentes en su rol estructural); la tesis admite la simetría operativa pero conserva asimetría en la dimensión normativa (solo agentes con disposiciones son sujetos de validez normativa, los soportes documentales son inscripciones de norma, no portadores).

### 6.4. Margaret Gilbert — agencia colectiva

Gilbert (1989, *On Social Facts*, cap. 4) define los plural subjects como sujetos colectivos formados por compromiso conjunto: *"the parties to a joint commitment have, by virtue of their commitment, sufficient reason to act in conformity with it"* (p. 198). Es contribución analítica explícita a la ontología de la coordinación.

La tesis los reformula como **atractores de coordinación con cuenca persistente bajo perturbación**. La noción gilbertiana de "plural subject" se traduce en patrón de coordinación que sostiene su forma bajo defección parcial. La diferencia con Searle es que Gilbert no requiere reglas constitutivas explícitas; basta el compromiso conjunto materialmente sostenido. La tesis está más cerca de Gilbert que de Searle en este punto.

### 6.5. Bunge — sistemismo social

Bunge (1979, *Treatise on Basic Philosophy*, vol. 4, p. 4) define sistema como *"objeto complejo cada uno de cuyos componentes está conectado con otros componentes de tal manera que el todo posee propiedades que ninguno de sus componentes posee"*. En *Sistemas sociales y filosofía* (1995, parte II) extiende el sistemismo al dominio social oponiéndose tanto al individualismo como al holismo: *"a society is not a thing or substance but a system of social relations among persons"* (1995, p. 79).

La tesis se inscribe en esta tradición. Las instituciones son sistemas concretos con composición (cuerpos, documentos, infraestructura), entorno (otros sistemas, condiciones materiales), estructura (relaciones específicas) y mecanismo (procesos que producen el comportamiento agregado, en términos de Bunge 1997). Lo que la tesis añade al sistemismo bunguiano es el **criterio empírico operativo de cierre vía intervención ablativa**: no basta definir el sistema; hay que mostrar que su dinámica acoplada constriñe efectivamente la conducta de sus componentes en una forma medible. El sistemismo de Bunge es la matriz conceptual; el aparato EDI es la operacionalización.

## 7. Criterio de elevación a demostrativo

Adoptar caso histórico-institucional con:

- datos cuantitativos publicados (transiciones de régimen, crisis institucionales, dinámica de mercados con historia documentada);
- modelo dinámico de bajo orden ajustable;
- bifurcación empíricamente identificable;
- predicción discriminante contra rival explícito.

### 7.1. Caso piloto candidato (deuda priorizada)

Se selecciona como caso piloto, sin ejecutar en este manuscrito pero documentado para trabajo posterior, la **dinámica de adopción de medidas no farmacéuticas durante COVID-19** por estados nacionales. Justificación:

- datos públicos disponibles (Oxford COVID-19 Government Response Tracker);
- una cuenca de atracción institucional (régimen de cumplimiento) sometida a perturbación discreta y observable (la propia pandemia);
- bifurcaciones identificables (transiciones de régimen restrictivo a permisivo y viceversa);
- comparabilidad inter-país que permite definir variabilidad de la cuenca (legitimidad como anchura de la cuenca);
- precedentes en la literatura cuantitativa (Hale et al., 2021; Cheng et al., 2020).

La elevación de este caso piloto exige adaptación específica del aparato EDI a series institucionales con variables ordinales (índices de stringency) en lugar de variables continuas. Se documenta como deuda alta en `Bitacora/2026-04-28-cierre-doctoral/` y en la hoja de ruta `06-cierre/03-hoja-de-ruta-para-tesis-final.md`.

### 7.2. Otros candidatos plausibles

- transición de regímenes políticos (Acemoglu y Robinson 2006, *Economic Origins of Dictatorship and Democracy*, ofrecen marco cuantitativo);
- crisis financieras (literatura post-2008 sobre dinámica de burbujas y crashes; Sornette 2003);
- transformación de campos académicos o profesionales (datos bibliométricos con bifurcaciones, en línea con Bourdieu 1984).

## 8. Lo que este capítulo devuelve a la tesis general

Demuestra que el marco puede tratar entidades con espesor normativo e histórico sin abandonar austeridad ontológica ni control empírico. Pero también muestra la frontera del marco actual: la operacionalización de la dimensión normativa es trabajo posterior. Esta es la deuda residual más importante del manuscrito (capítulo 06-01).

## 9. Limitación honesta

Este capítulo conjetura. La elevación requiere:

- caso específico con datos cuantitativos;
- desarrollo del aparato para variables normativas como dimensiones del sistema acoplado;
- diálogo profundo con Searle, Bourdieu, Latour, Gilbert.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---


<div id="parte-4-discusion"></div>

# Parte IV — Discusión crítica


<div id="capitulo-25-debates-con-posiciones-rivales"></div>

# Debates con posiciones rivales


## Tesis del capítulo

> La tesis se discrimina de sus catorce rivales filosófica y empíricamente identificables (dualismo, materialismo de partículas, reduccionismo plano, emergentismo fuerte, constructivismo arbitrario, instrumentalismo puro, formalismo vacío, modelos internos / control óptimo, cognitivismo computacional, conductismo radical, enactivismo radical, realismo estructural informativo, mecanicismo multinivel sin filtro, y **Wolfram Physics Project**) en al menos dos criterios cada uno. La novedad de la tesis no es de inventario sino de articulación: dossier de anclaje + asimetría L1↔B↔L3↔S como filtro de admisión simultáneo + cartografía multidominio bajo EDI con controles de falsación rechazados.

## 1. Marco general de la confrontación

Cada rival se evalúa contra la tesis bajo estos criterios:

- **A**: anclaje material sin reducción a partículas;
- **B**: tratamiento de organización multiescala;
- **C**: procedimiento de admisión empírica para sus categorías;
- **D**: traducibilidad entre niveles (L1↔B↔L3↔S);
- **E**: ventaja predictiva discriminante en el caso ancla canónico;
- **F**: alcance generalizable a dominios programáticos.

El uso de los criterios no es uniformemente aplicable: A y B se aplican a todos; C, D, E, F se aplican según el rival ocupe terreno empírico o solo filosófico.

## 2. Dualismo

### Forma fuerte

Existen al menos dos tipos de realidad: material y mental (o material y normativa, o material y informacional). Los fenómenos del segundo tipo no se reducen al primero ni se explican plenamente con su vocabulario.

### Qué recoge la tesis

La intuición de que algunos fenómenos no se entienden bien bajo descripción microfísica inmediata. Esta intuición es correcta y se recoge como argumento para multiescalaridad.

### Qué rechaza

Que la dificultad explicativa exija multiplicar sustancias. La tesis muestra que el problema se resuelve con organización, restricción, escala y patrón materialmente anclados.

### Discriminación

**Tabla 4.1.1.**

| Criterio | Tesis | Dualismo |
|---|---|---|
| A | Sí (sustrato único) | Parcial (segunda sustancia no anclada) |
| B | Sí (multiescalaridad sin mundos separados) | No (mundos separados) |
| F | Sí (sin proliferación) | Solo en dominios donde se postula segunda sustancia |

Pierde en cero criterios. La tesis discrimina contra dualismo en A, B y F.

## 3. Materialismo de partículas

### Forma fuerte

Toda explicación adecuada se reduce, en principio, a descripción del nivel microfísico. Los niveles superiores son etiquetas pragmáticas sobre la realidad fundamental que es el conjunto de partículas y sus interacciones.

### Qué recoge la tesis

La exigencia de anclaje material y la negativa a introducir entidades misteriosas.

### Qué rechaza

Que conocer las partes equivalga automáticamente a conocer el fenómeno. La tesis muestra que la organización importa: una descripción micro puede ser verdadera y no capturar la estructura relevante para Q.

### Discriminación

**Tabla 4.1.2.**

| Criterio | Tesis | Materialismo de partículas |
|---|---|---|
| B | Sí (multiescalaridad operativa) | No (un solo nivel privilegiado) |
| C | Sí (dossier de anclaje incluye nivel adecuado) | No (procedimiento de admisión solo en micro) |
| E | Sí (caso ancla con leyes de control de baja dimensión) | No (locomoción no se predice desde partículas) |

Pierde en cero criterios. Discrimina en B, C, E.

## 4. Reduccionismo plano

### Forma fuerte

La mejor explicación es siempre la del nivel inferior. Subir de nivel solo se justifica como conveniencia computacional, no como ganancia explicativa real.

### Qué recoge la tesis

La obligación de no inventar niveles superfluos.

### Qué rechaza

La identificación entre profundidad ontológica y suficiencia explicativa. El nivel correcto es el que preserva mejor la estructura relevante con el menor costo innecesario, no el más bajo por principio.

### Discriminación

**Tabla 4.1.3.**

| Criterio | Tesis | Reduccionismo plano |
|---|---|---|
| B | Sí (paso entre escalas como decisión operativa) | No (un nivel privilegiado) |
| C | Sí (criterios de cambio de escala explícitos) | Implícito y arbitrario |
| F | Sí (multidominio) | Solo en dominios donde el reduccionismo ha avanzado |

Pierde en cero criterios. Discrimina en B, C, F.

## 5. Emergentismo fuerte

### Forma fuerte

Ciertos niveles generan entidades o propiedades irreductibles en sentido fuerte y casi autónomas respecto del sustrato. La emergencia introduce sustancia ontológica nueva que no se reduce a interacción de las componentes.

### Qué recoge la tesis

La intuición de que hay patrones que solo se vuelven visibles en ciertos niveles de organización.

### Qué rechaza

Convertir esa visibilidad en prueba de sustancia nueva. La tesis ofrece self-organization como modelo positivo de la emergencia anclada (capítulo 02-04 §4): estabilización dinámica del sistema acoplado, no aparición de entidad adicional.

### Discriminación

**Tabla 4.1.4.**

| Criterio | Tesis | Emergentismo fuerte |
|---|---|---|
| A | Sí (sustrato único) | Parcial (sustancia emergente sin anclaje) |
| C | Sí (atractores empíricamente verificables) | No (criterios subjetivos de irreducibilidad) |
| D | Sí (traducibilidad B↔L3) | Bloqueada por irreducibilidad postulada |

Pierde en cero criterios. Discrimina en A, C, D.

## 6. Constructivismo arbitrario

### Forma fuerte

Las categorías son productos de prácticas y no hay razones fuertes para privilegiar unos recortes sobre otros. La estructura aparente de la realidad es proyección de la práctica clasificatoria.

### Qué recoge la tesis

La advertencia de que las categorías no están dadas de una vez por la realidad ni por el lenguaje.

### Qué rechaza

Que todos los recortes sean equivalentes. La realidad constriñe la validez de las categorías por estabilidad, rendimiento inferencial, poder predictivo y poder interventivo.

### Discriminación

**Tabla 4.1.5.**

| Criterio | Tesis | Constructivismo arbitrario |
|---|---|---|
| C | Sí (dossier de anclaje, predicción discriminante) | No (todas las construcciones son admisibles) |
| E | Sí (caso ancla con varianza explicada >97%) | Indiferente al criterio |

Pierde en cero criterios. Discrimina en C, E.

## 7. Instrumentalismo puro

### Forma fuerte

Los modelos son herramientas útiles sin compromiso serio con estructura real. Hablar de `verdad` o `realidad` de un modelo es categoría inapropiada.

### Qué recoge la tesis

Que los modelos son construcciones y no espejos directos del mundo.

### Qué rechaza

Que la utilidad baste sin relación robusta con restricciones reales. La utilidad importa como señal de captura estructural, no como sustituto.

### Discriminación

**Tabla 4.1.6.**

| Criterio | Tesis | Instrumentalismo puro |
|---|---|---|
| A | Sí (anclaje material en dossier) | No exigido |
| C | Sí (predicción discriminante e intervención) | Solo utilidad práctica como criterio |

Pierde en cero criterios. Discrimina en A, C.

## 8. Formalismo vacío

### Forma fuerte

No siempre es doctrina explícita; a veces es deriva metodológica donde la representación matemática elegante se considera resolución del problema filosófico.

### Qué recoge la tesis

El valor disciplinario del formalismo.

### Qué rechaza

Que la estructura formal tenga valor por sí misma sin contacto mejorado con el fenómeno.

### Discriminación

**Tabla 4.1.7.**

| Criterio | Tesis | Formalismo vacío |
|---|---|---|
| D | Sí (traducibilidad B↔L3 obligatoria) | No (formalismo opera independiente del fenómeno) |
| E | Sí (predicciones empíricas verificadas) | Indiferente |

Pierde en cero criterios. Discrimina en D, E.

## 9. Modelos internos / control óptimo

### Forma fuerte

El sistema nervioso construye representaciones internas del cuerpo y del entorno. La conducta adaptativa se explica como solución de un problema de optimización (control óptimo) sobre estos modelos. La fidelidad de las representaciones es lo que explica la efectividad de la conducta. Trabajos paradigmáticos: Wolpert et al., Loomis y Beall, Todorov y Jordan, control engineering aplicado a postura y movimiento.

### Qué recoge la tesis

La existencia de procesos internos relevantes para conducta secuencial, anticipatoria, predictiva y estratégica donde la información ocurrente no basta. La tesis no es eliminativista respecto a estados internos.

### Qué rechaza

Que los modelos internos sean recurso primario para tareas como locomoción, frenado, equilibrio, raqueteo, donde el control directo informacional explica los datos con menos hipótesis y mejor predicción.

### Discriminación en el caso ancla canónico

**Tabla 4.1.8.**

| Criterio | Tesis (control informacional, leyes acopladas) | Modelos internos / control óptimo |
|---|---|---|
| Reproducción de datos | r²=0.980 (locomoción Fajen-Warren) | Requiere parámetros adicionales no derivados |
| Predicción de degradación al retirar visión en línea | Predice degradación marcada, confirmada (Wallis et al. 2002, Hildreth et al. 2000) | Predice estabilidad relativa, no confirmada |
| Predicción de uso de τ̇=−0.5 en frenado | Predicha (r²=0.98 en Yilmaz-Warren 1995) | No deriva la constante |
| Bifurcación de ruta como cambio cualitativo | Predicha y observada | Requiere meta-decisión planificada |
| Economía paramétrica | 4 parámetros para locomoción | Requiere modelo interno completo |

Pierde en cero criterios en el caso ancla. Discrimina en cinco.

### Restricción honesta

Los modelos internos siguen siendo candidatos para conducta sequential, anticipatoria predictiva y estratégica que el caso ancla declara fuera de su régimen de validez (capítulo 05-05 §casos de presión). La tesis no rechaza modelos internos en abstracto; rechaza su uso como recurso primario donde el control informacional discrimina mejor.

## 10. Cognitivismo computacional

### Forma fuerte

La conducta cognitiva es ejecución de programas mentales sobre representaciones simbólicas. La mente es máquina computacional cuya descripción adecuada está en el nivel del software, no del hardware.

### Qué recoge la tesis

La existencia de procesos cognitivos no reducibles a respuestas inmediatas a estímulos.

### Qué rechaza

Que la metáfora computacional sea recurso primario para fenómenos donde el acoplamiento dinámico explica los datos sin ellas. Y rechaza la abstracción del nivel simbólico desligado del nivel B.

### Discriminación en el caso ancla y en mente

**Tabla 4.1.9.**

| Criterio | Tesis | Cognitivismo computacional |
|---|---|---|
| D (traducibilidad B↔L3) | Obligatoria | Bloqueada (multiple realizability como dogma) |
| E (caso ancla) | Predice y reproduce | Predice mal o no predice |
| C (admisión de categorías) | Dossier verificable | Apelación a `nivel computacional` sin verificación |

Pierde en cero criterios en el caso ancla. Discrimina en C, D, E. En mente como dominio programático, la confrontación queda abierta porque la tesis aún no tiene caso demostrativo equivalente para fenómenos cognitivos superiores; ahí cognitivismo y tesis empatan en modo programático y la decisión queda para investigación posterior.

## 11. Conductismo radical

### Forma fuerte

Solo cuentan las relaciones entre estímulos y respuestas observables. Postular estados internos es metafísica.

### Qué recoge la tesis

El recorte correcto del plano observable y la negativa a postular entidades internas no controladas.

### Qué rechaza

La negación de la estructura formal L3 que efectivamente discrimina hipótesis. La tesis añade L3 anclado sin perder anclaje en B.

### Discriminación

**Tabla 4.1.10.**

| Criterio | Tesis | Conductismo radical |
|---|---|---|
| B | Sí (estructura multiescala formal) | No (un nivel observable) |
| D | Sí (B↔L3) | Solo nivel B |
| C (admisión) | Dossier completo | Solo correlaciones E-R |

Pierde en cero criterios. Discrimina en B, C, D.

### Restricción honesta

El conductismo radical es primo empobrecido del marco propuesto. La tesis le añade L3 sin perder anclaje en B; podría decirse que es un conductismo enriquecido con dinámica y self-organization en el sentido técnico anclado en cap 02-04 §4 (Maturana-Varela 1980, Haken 1977).

## 12. Enactivismo radical

### Forma fuerte

Hutto y Myin (2013, *Radicalizing Enactivism*, cap. 1) sostienen la **REC thesis (Radical Enactive Cognition)**: *"basic cognition is constituted by, and to be explained in terms of, concrete spatiotemporally extended patterns of dynamic interaction between organisms and their environments [...] basic cognition does not, intrinsically, involve any kind of content"* (p. 8). La tesis del contenido cero (zero-content) es la pieza fuerte: niveles cognitivos básicos no requieren contenido representacional. Hutto y Myin (2017, *Evolving Enactivism*, cap. 5) extienden el argumento contra cualquier predictive coding que asuma contenido representacional inferencial.

### Qué recoge la tesis

La posición es muy cercana en espíritu. La tesis adopta el acoplamiento dinámico (capítulo 02-04), la dependencia ecológica (información ecológica como categoría central, sección 5 de ese capítulo), la centralidad de la tarea, y el rechazo de la representación interna como recurso primario en niveles básicos. La afirmación de Hutto-Myin de que *"there is no need to posit content-bearing intermediaries between organism and environment for basic perception"* (2013, p. 81) es congruente con la operacionalización del nivel B vía variables informacionales materialmente realizadas (τ, ρ, flujo óptico).

### Qué rechaza

Tres divergencias específicas:

1. **Grado de eliminación.** Hutto-Myin extienden la zero-content thesis a niveles básicos pero conceden contenido en niveles avanzados. La tesis es más cautelosa: admite estados internos como hipótesis cuando la pregunta lo exige (conducta anticipatoria, secuencial, estratégica), pero solo si el dossier de anclaje (capítulo 03-02) los justifica empíricamente.
2. **Formalización L3.** La tesis exige aparato formal (μ, G, H, κ, ε) y validación cuantitativa (EDI), donde el enactivismo radical mantiene la formulación cualitativa. La objeción de Chemero (2009, *Radical Embodied Cognitive Science*, cap. 4) sobre la dificultad de cuantificar dinámica sin recaer en cognitivismo es real, pero la tesis muestra (caso 30 del corpus EDI, EDI = 0.262 significativo) que la cuantificación es posible sin volver al cognitivismo.
3. **Alcance multidominio.** El enactivismo radical se concentra en cognición situada; la tesis cubre 30 dominios heterogéneos. La generalización exige aparato formal compartido.

### Discriminación

**Tabla 4.1.11.**

| Criterio | Tesis | Enactivismo radical |
|---|---|---|
| C | Dossier formal | Mayormente cualitativo |
| F | Multidominio | Foco en cognición situada |
| E | Predicciones cuantitativas | Predicciones generalmente cualitativas |

Pierde en cero criterios. Discrimina en C, E, F.

### Reconocimiento

Es el rival con quien la tesis comparte más: la diferencia es de articulación formal y de extensión de dominio, no de orientación filosófica.

## 13. Realismo estructural informativo (Ladyman-Ross)

### Forma fuerte

La ontología fundamental es estructural. Las invariantes de simetría son lo que existe en sentido fuerte; los objetos son nodos en la estructura.

### Qué recoge la tesis

La centralidad de la estructura como objeto del análisis ontológico.

### Qué rechaza

Que la estructura sea ontología fundamental sin sustrato. La tesis afirma sustrato material como base; la estructura es estructura **del** sustrato.

### Discriminación

**Tabla 4.1.12.**

| Criterio | Tesis | Realismo estructural informativo |
|---|---|---|
| A | Sí (sustrato material) | Estructura sin sustrato |
| C (dossier) | Filtro completo | Criterios estructurales sin requisito empírico explícito |
| D | Asimetría L1↔B↔L3↔S | Sin asimetría análoga |

Pierde en cero criterios. Discrimina en A, C, D. La diferencia es metafísica sutil pero real: la tesis no flota la estructura.

## 14. Wolfram Physics Project (caso especial)

### Forma fuerte

Wolfram (2002, *A New Kind of Science*, cap. 12) introduce la tesis de la **irreducibilidad computacional**: *"there is no way to find out what a system will do except by effectively running it"* (p. 737). En el Wolfram Physics Project (2020, *A Project to Find the Fundamental Theory of Physics*, secciones 1-3), extiende la propuesta al sustrato físico: la realidad fundamental es hypergraph rewriting, y el universo es la evolución de un hipergrafo bajo reglas locales.

La conjetura del **Ruliad** (Wolfram 2021, *The Concept of the Ruliad*, secciones 2 y 6) sostiene que toda la física observable emerge de la totalidad de reglas computacionales posibles, accedida desde un punto de vista observador particular: *"the ruliad is the entangled limit of everything that is computationally possible"* (sec. 2). La posición es ambiciosa, técnicamente sofisticada, y comparte con la tesis dos elementos importantes: el papel central de los **hipergrafos** como representación estructural del sustrato, y el rechazo del reduccionismo plano (la organización multiescala importa).

### Qué recoge la tesis

- la centralidad de los hipergrafos como instrumento formal (capítulo 03-01);
- el rechazo de la lista plana de partículas como descripción suficiente;
- la importancia de la multiescalaridad sin emergentismo fuerte;
- el espíritu de exploración computacional sistemática.

### Qué rechaza

Cuatro divergencias precisas:

1. **Ambición ontológica:** Wolfram busca *ontología fundamental* (la física es hypergraph rewriting). La tesis es ontología y epistemología generales **integradoras**, no fundacionales. No busca reducir todo a hipergrafos; articula registros heterogéneos bajo dossier de admisión.
2. **Procedimiento de admisión empírica:** Wolfram propone reglas computacionales pero no especifica filtro empírico de admisión para constructos macro. La tesis exige dossier de catorce componentes + protocolo C1-C5 + EDI con prueba de permutación + controles de falsación rechazados.
3. **Asimetría L1↔B↔L3↔S:** Wolfram opera en un solo registro (sustrato computacional). La tesis distingue cuatro registros con vínculos asimétricos y prohíbe la sustitución nominal.
4. **Cartografía empírica multidominio:** Wolfram propone simulaciones computacionales pero no validación discriminante sobre datos reales en dominios heterogéneos con controles de falsación. La tesis valida 30 casos en física, biología, economía, política, tecnología, cultura y conducta humana, con 3 controles de falsación correctamente rechazados.

### Discriminación

**Tabla 4.1.13.**

| Criterio | Tesis (irrealismo operativo) | Wolfram Physics Project |
|---|---|---|
| A (anclaje material sin reducción) | Sí | Sí (computacional) |
| B (multiescalaridad operativa) | Sí | Sí |
| C (procedimiento de admisión empírica) | Dossier completo + C1-C5 + EDI | No especificado |
| D (traducibilidad L1↔B↔L3↔S) | Asimetría protocolar | Solo nivel computacional |
| E (cartografía multidominio con discriminación) | 30 casos + falsación 3/3 | Simulaciones internas |
| F (alcance generalizable) | Sí | Sí (más ambicioso ontológicamente) |

Pierde en cero criterios. Discrimina en C, D, E.

### Reconocimiento de fortalezas

El Wolfram Physics Project tiene fortalezas que la tesis no posee:

- mayor profundidad técnica en hypergraph rewriting;
- exploración computacional masiva con visualizaciones avanzadas;
- conjeturas con potencial unificador en física fundamental;
- comunidad investigadora activa (Wolfram Physics Project, Wolfram Institute).

La tesis es **complementaria**, no rival sustituta. Donde Wolfram busca la regla fundamental, la tesis pide que cualquier constructo derivado pase por dossier de admisión. **Wolfram fundamenta; la tesis disciplina**.

### Convergencia productiva posible

Un programa de investigación interesante: aplicar el protocolo EDI a fenómenos derivados de simulaciones de hypergraph rewriting. Esto crearía un puente entre la ontología fundacional de Wolfram y la cartografía empírica multidominio de la tesis. Esquema concreto del trabajo futuro:

1. **Selección de regla.** Elegir una regla de reescritura del Wolfram Physics Project con propiedades emergentes ya documentadas (por ejemplo, regla `wolfphys/006` o equivalente con curvatura emergente reportada).
2. **Generación de simulaciones.** Producir 200+ ejecuciones con condiciones iniciales perturbadas para estimar variabilidad estructural.
3. **Construcción de sonda macro.** Identificar magnitud agregada candidata (densidad media de aristas, curvatura escalar discreta, número de bordes activos) y formular sonda ODE de bajo orden ajustable.
4. **Aplicación EDI.** Calcular EDI = 1 − RMSE_coupled / RMSE_no_ode bajo el aparato del corpus, con permutación 999 + bootstrap 500 + protocolo C1-C5.
5. **Hipótesis a verificar.** Si la sonda macro tiene cierre operativo (EDI ≥ 0.30, p < 0.05), la regla microestructural admite descripción macroescalar legítima bajo el aparato. Si no, la irreducibilidad computacional opera al nivel macroescalar elegido.
6. **Lectura.** En cualquier escenario, el resultado discrimina: cierre operativo confirma puente entre Wolfram y la tesis; ausencia de cierre fortalece la tesis de irreducibilidad de Wolfram en el régimen específico.

Este esquema queda documentado como deuda futura priorizada. No se ejecuta en el manuscrito actual.

## 15. Mecanicismo multinivel (Bechtel-Craver)

### Forma fuerte

Bechtel (2008, *Mental Mechanisms*, cap. 1) define mecanismo como *"a structure performing a function in virtue of its component parts, component operations, and their organization. The orchestrated functioning of the mechanism is responsible for one or more phenomena"* (p. 13). Craver (2007, *Explaining the Brain*, cap. 4) elabora la tesis de la integración multinivel: los niveles no son meramente útiles sino ontológicamente reales si y solo si las relaciones constitutivas entre ellos son **mutually manipulable** (cap. 4, p. 152). Bechtel y Richardson (1993, *Discovering Complexity*, cap. 2) sistematizan la heurística de descomposición y localización.

### Qué recoge la tesis

Casi todo. Es el aliado más fuerte en la articulación multinivel y en el realismo de mecanismos. La definición bechteliana de mecanismo coincide con la noción de **patrón materialmente sostenido con organización específica** del capítulo 02-01. La criterio de **mutual manipulability** de Craver coincide con el criterio empírico de cierre operativo κ vía intervención ablativa.

### Qué añade la tesis

Tres aportes específicos al programa mecanicista:

1. **Filtro de admisión cuantitativo.** Bechtel-Craver aceptan que los niveles son legítimos cuando las relaciones constitutivas son mutuamente manipulables, pero no especifican una métrica única para decidir el grado de manipulabilidad. La tesis ofrece la métrica EDI con permutación + bootstrap + protocolo C1-C5 como instrumento operativo de esa decisión.
2. **Procedimiento empírico de κ vía baja dimensionalidad.** El mecanicismo deja la legitimidad de niveles relativamente abierta; la tesis la cierra con criterios verificables (capítulo 03-04).
3. **Cartografía multidominio.** Bechtel-Craver trabajan principalmente en neurobiología y ciencias biomédicas; la tesis extiende la lógica a 30 dominios heterogéneos con controles de falsación rechazados.

La discusión específica con la **objeción de Glennan (2017, *The New Mechanical Philosophy*)** sobre si la dinámica acoplada continua admite descripción mecanicista discreta, queda como punto de presión legítimo y se trata en `04-debates/02-limitaciones-y-puntos-de-presion.md`.

### Discriminación

**Tabla 4.1.14.**

| Criterio | Tesis | Mecanicismo multinivel |
|---|---|---|
| C | Dossier completo | Criterios mecanicistas sin batería de diez |
| D | Asimetría obligatoria | Asimetría parcial |
| F | Generalización a institucional/social explícita | Foco principal en biología |

Pierde en cero criterios. Discrimina en C, D, F.

### Reconocimiento

El mecanicismo multinivel es el aliado teórico principal de este capítulo. La tesis se entiende mejor como mecanicismo multinivel disciplinado por dossier de anclaje y asimetría L1↔B↔L3↔S.

## 16. Tabla síntesis

**Tabla 4.1.15.**

| Posición rival | Lo que la tesis acepta | Lo que la tesis rechaza | Criterios de discriminación |
|---|---|---|---|
| Dualismo | Diferencias explicativas fuertes | Segunda sustancia | A, B, F |
| Materialismo de partículas | Anclaje material | La materialidad agota la explicación | B, C, E |
| Reduccionismo plano | No inflar niveles | Privilegio del nivel más bajo | B, C, F |
| Emergentismo fuerte | Visibilidad solo en organización | Sustancias nuevas | A, C, D |
| Constructivismo arbitrario | Categorías construidas | Equivalencia de recortes | C, E |
| Instrumentalismo puro | Modelos como herramientas | Utilidad sin compromiso estructural | A, C |
| Formalismo vacío | Disciplina formal | Matemática sin anclaje | D, E |
| Modelos internos / control óptimo | Estados internos en conducta secuencial | Recurso primario en percepción-acción | E (caso ancla, 5 celdas) |
| Cognitivismo computacional | Procesos no reducibles a E-R | Abstracción simbólica desligada de B | C, D, E |
| Conductismo radical | Anclaje en observable | Negación de L3 | B, C, D |
| Enactivismo radical | Acoplamiento dinámico, dependencia ecológica | Solo cualitativo, sin formalismo verificable | C, E, F |
| Realismo estructural informativo | Estructura central | Estructura sin sustrato | A, C, D |
| Mecanicismo multinivel | Aliado principal | Criterios de admisión más laxos | C, D, F |
| **Wolfram Physics Project** | Hipergrafos centrales, no reduccionismo plano | Ontología fundacional sin filtro empírico | C, D, E |

## 16. Cuál es la novedad de la tesis

La diferencia no está en cada pieza aislada — la mayoría se encuentra distribuida entre los rivales. La novedad es la articulación: dossier de anclaje + asimetría L1↔B↔L3↔S + procedimiento empírico de κ + caso ancla canónico trabajado a fondo + extensión programática a dominios heterogéneos.

Ningún rival reúne las cinco piezas en la misma arquitectura. El mecanicismo multinivel se acerca más, pero le falta la asimetría como protocolo formal y le falta la operacionalización de κ vía baja dimensionalidad. El enactivismo se acerca en espíritu, pero le falta la formalización verificable. El realismo estructural se acerca en compromiso ontológico, pero le falta el anclaje empírico explícito.

## 17. Compromiso público

Esta tabla es el compromiso público de discriminación. Si en algún rival la tesis no muestra ventaja en al menos dos celdas, la tesis admite haber sido absorbida y debe reformularse. Las celdas se pueden discutir; el compromiso de discriminación verificable no.

## 18. Cierre

La tesis ocupa un punto difícil pero filosóficamente fértil:

- austera como el materialismo, sin ser de partículas;
- sensible a la organización como el emergentismo, sin postular sustancias;
- cuidadosa con las mediaciones como el constructivismo, sin caer en arbitrariedad;
- rigurosa en su modelización como el formalismo, sin ser vacía;
- empíricamente comprometida como el behavioral dynamics, con extensión filosófica general;
- mecanicista multinivel disciplinada por filtros de admisión que el mecanicismo deja abiertos.

> La realidad no exige más sustancias, pero sí mejores recortes, dossier completo y predicción discriminante.

Eso es lo que la tesis quiere demostrar una y otra vez, hasta que incluso sus objeciones tengan que discutir en ese terreno.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-26-tabla-comparativa-con-rivales"></div>

# Tabla comparativa con rivales

## Función

Síntesis de la discriminación pública contra catorce posiciones rivales. Cada celda representa cumplimiento del criterio: ✓ (satisface), parcial (satisface en parte), ✗ (no satisface). La tesis discrimina en al menos dos criterios contra cada rival.

---

## Criterios de discriminación

**Tabla A.4.1.**

| Código | Criterio |
|--------|----------|
| **A** | Anclaje material sin reducción a partículas |
| **B** | Multiescalaridad operativa **invariante a la escala** (aplicable desde lo cuántico hasta lo cosmológico) |
| **C** | Procedimiento de admisión empírica con dossier de catorce componentes |
| **D** | Traducibilidad asimétrica L1↔B↔L3↔S **invariante a la escala** |
| **E** | Cartografía inter-dominio + inter-escala con discriminación verificable y controles de falsación |
| **F** | Alcance generalizable a dominios y escalas programáticas |

---

## Tabla síntesis (14 rivales)

**Tabla A.4.2.**

| # | Posición rival | A | B | C | D | E | F | Discrimina en |
|---|----------------|:-:|:-:|:-:|:-:|:-:|:-:|:------------:|
| 1 | Dualismo (cartesiano y descendientes) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | A, B, F |
| 2 | Materialismo de partículas | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | B, C, E |
| 3 | Reduccionismo plano | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | B, C, F |
| 4 | Emergentismo fuerte | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | A, C, D |
| 5 | Constructivismo arbitrario | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | C, E |
| 6 | Instrumentalismo puro | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | A, C |
| 7 | Formalismo vacío | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | D, E |
| 8 | Modelos internos / control óptimo | ✓ | ✓ | ✗ | ✗ | parcial | ✗ | E (5 celdas en caso ancla) |
| 9 | Cognitivismo computacional | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | C, D, E |
| 10 | Conductismo radical | ✓ | ✗ | parcial | ✗ | ✗ | ✗ | B, C, D |
| 11 | Enactivismo radical | ✓ | ✓ | parcial | ✓ | parcial | ✗ | C, E, F |
| 12 | Realismo estructural informativo | ✗ | ✓ | parcial | ✗ | ✗ | ✓ | A, C, D |
| 13 | Mecanicismo multinivel sin filtro | ✓ | ✓ | parcial | parcial | parcial | ✓ | C, D, F |
| 14 | **Wolfram Physics Project** | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ | C, D, E |

---

## La tesis (irrealismo operativo) en la matriz

**Tabla A.4.3.**

| # | A | B | C | D | E | F |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| **Tesis** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** |

La tesis cumple los seis criterios. Ninguna posición rival cumple los seis. La novedad no es de inventario (cada criterio aislado se encuentra en algún rival) sino de **articulación**: la combinación dossier + asimetría L1↔B↔L3↔S + cartografía con falsación es propia.

---

## Confrontación detallada por rival

### 1. Dualismo

**Forma fuerte:** ciertos fenómenos (mente, normatividad) requieren un tipo de realidad distinto del orden material.

**Tesis recoge:** la intuición de que algunos fenómenos no se entienden con descripción microfísica.

**Tesis rechaza:** la multiplicación de sustancias.

**Discrimina en:** A (un solo sustrato), B (multiescala sin mundos separados), F (sin proliferación).

### 2. Materialismo de partículas

**Forma fuerte:** la explicación adecuada se reduce a descripción del nivel microfísico.

**Tesis recoge:** la exigencia de anclaje material.

**Tesis rechaza:** la identificación entre profundidad y suficiencia explicativa.

**Discrimina en:** B, C (dossier exige nivel adecuado a Q), E (caso ancla con baja dimensionalidad).

### 3. Reduccionismo plano

**Forma fuerte:** el nivel correcto siempre es el más bajo.

**Tesis recoge:** no inflar niveles superfluos.

**Tesis rechaza:** privilegio del nivel inferior por principio.

**Discrimina en:** B, C (criterios de cambio de escala explícitos), F.

### 4. Emergentismo fuerte

**Forma fuerte:** ciertos niveles generan sustancias nuevas no reducibles.

**Tesis recoge:** la visibilidad de patrones organizacionales.

**Tesis rechaza:** convertir esa visibilidad en sustancia.

**Discrimina en:** A (sustrato único), C (atractores empíricos verificables), D (traducibilidad B↔L3).

### 5. Constructivismo arbitrario

**Forma fuerte:** todos los recortes son equivalentes.

**Tesis recoge:** las categorías son construidas.

**Tesis rechaza:** la equivalencia.

**Discrimina en:** C (dossier, predicción discriminante), E (caso ancla con varianza explicada >97%).

### 6. Instrumentalismo puro

**Forma fuerte:** los modelos son herramientas sin compromiso estructural.

**Tesis recoge:** los modelos son construcciones.

**Tesis rechaza:** la utilidad sin restricción real.

**Discrimina en:** A, C (predicción discriminante e intervención).

### 7. Formalismo vacío

**Forma fuerte:** la elegancia matemática resuelve el problema filosófico.

**Tesis recoge:** disciplina formal.

**Tesis rechaza:** matemática sin anclaje.

**Discrimina en:** D (traducibilidad B↔L3), E (predicciones empíricas verificadas).

### 8. Modelos internos / control óptimo

**Forma fuerte:** el sistema nervioso construye representaciones internas y resuelve optimización.

**Tesis recoge:** estados internos en conducta secuencial / anticipatoria / estratégica.

**Tesis rechaza:** modelos internos como recurso primario en percepción-acción.

**Discrimina en caso ancla (cinco celdas):**
- Reproducción (r²=0.980 vs requiere parámetros adicionales)
- Predicción de degradación al retirar visión (cumplida vs no predicha)
- Predicción τ̇=−0.5 en frenado (predicha vs no derivada)
- Bifurcación de ruta (predicha y observada vs requiere meta-decisión planificada)
- Economía paramétrica (4 parámetros vs modelo interno completo)

### 9. Cognitivismo computacional

**Forma fuerte:** la mente es máquina computacional sobre representaciones simbólicas.

**Tesis recoge:** procesos cognitivos no reducibles a estímulo-respuesta.

**Tesis rechaza:** abstracción simbólica desligada de B.

**Discrimina en:** C, D, E. En mente como dominio programático queda abierto.

### 10. Conductismo radical

**Forma fuerte:** solo cuentan estímulos y respuestas observables.

**Tesis recoge:** anclaje en observable.

**Tesis rechaza:** negación de L3.

**Discrimina en:** B, C, D. La tesis es conductismo enriquecido con dinámica y self-organization en el sentido técnico de cap 02-04 §4 (Maturana-Varela 1980, Haken 1977).

### 11. Enactivismo radical

**Forma fuerte:** la cognición es acción enacted del organismo en su entorno.

**Tesis recoge:** acoplamiento dinámico, dependencia ecológica, centralidad de la tarea.

**Tesis rechaza:** quedarse en formulación cualitativa sin filtro formal.

**Discrimina en:** C (dossier formal), E (predicciones cuantitativas), F (multidominio).

**Aliado más cercano:** la diferencia es de articulación formal, no de orientación filosófica.

### 12. Realismo estructural informativo (Ladyman-Ross)

**Forma fuerte:** la ontología fundamental es estructural; los objetos son nodos.

**Tesis recoge:** centralidad de la estructura como objeto del análisis.

**Tesis rechaza:** estructura como ontología fundamental sin sustrato.

**Discrimina en:** A (sustrato material), C (filtro empírico), D (asimetría protocolar).

### 13. Mecanicismo multinivel (Bechtel-Craver)

**Forma fuerte:** los fenómenos complejos se explican por descomposición funcional en mecanismos.

**Tesis recoge:** casi todo. Aliado teórico principal.

**Tesis añade:** filtro de admisión completo + procedimiento empírico de κ.

**Discrimina en:** C, D, F.

**Posición:** la tesis se entiende como mecanicismo multinivel disciplinado por dossier de anclaje.

### 14. Wolfram Physics Project

**Forma fuerte:** la física fundamental se reduce a hypergraph rewriting; el Ruliad es la ontología.

**Tesis recoge:** centralidad de los hipergrafos, rechazo del reduccionismo plano, multiescalaridad.

**Tesis rechaza:** ambición ontológica fundacional sin filtro empírico.

**Discrimina en:** C (dossier vs no especificado), D (asimetría protocolar vs un solo registro), E (cartografía multidominio con falsación 3/3 vs simulaciones internas).

**Posición:** Wolfram fundamenta; la tesis disciplina. **Piloto Rule 110 ejecutado** (`09-simulaciones-edi/wolfram_pilot/`): EDI = 0.55 sobre dos sondas independientes, mostrando convivencia de irreducibilidad computacional micro y cierre operativo macro detectable. Programa de convergencia post-piloto: aplicar EDI a fenómenos adicionales derivados de hypergraph rewriting (trabajo futuro 12-18 meses, ver `Bitacora/2026-04-28-cierre-doctoral/05-`).

---

## Compromiso público

Esta tabla es compromiso. Si en algún rival la tesis no muestra ventaja en al menos dos celdas, la tesis admite haber sido absorbida y debe reformularse.

**Estado actual:** la tesis discrimina contra cada uno de los catorce rivales en al menos dos criterios. La tabla no produce absorción.

---

## Lectura cruzada

- Confrontación detallada por rival: capítulo 04-01.
- Limitaciones que sobreviven: capítulo 04-02.
- Caso ancla canónico (donde se opera la discriminación contra modelos internos): capítulo 05-05.
- Convergencia con Wolfram (programa futuro): capítulo 06-03.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-27-anticipacion-de-objeciones-filosoficas"></div>

# Anticipación de objeciones filosóficas

> **Estado:** capítulo argumental defendible. Las siete objeciones que siguen reproducen la formulación más fuerte que un comité doctoral exigente puede plantear contra la tesis (auditoría doctoral, fallos F1, F2, F3, F5, F6, F9, F10). Cada respuesta sigue el esquema **objeción / concesión / distinción / argumento positivo / costo**. La voz autoral final es de Jacob Agudelo: la asistencia computacional preparó el aparato citacional y la articulación argumental con engagement directo a las fuentes primarias indicadas; cada sección admite reescritura editorial menor sin perder su núcleo. La tarea **H-J1** del documento `TAREAS_PENDIENTES.md` corresponde a la firma final.

## Función del capítulo

Cada sección sigue una arquitectura única:

1. **Objeción** — la versión más fuerte y filosóficamente cargada del cuestionamiento. No se debilita el argumento rival.
2. **Concesión** — qué admite la tesis sin mover su núcleo. La concesión es honesta, no táctica.
3. **Distinción** — cómo se separa la afirmación criticable de la no criticable. Aquí se decide qué se rescata y qué se reformula.
4. **Argumento positivo** — por qué la tesis sigue en pie tras la concesión. Argumento independiente del aparato cuando es posible; cuando no, declaración explícita de que el argumento es operativo.
5. **Costo** — qué pagamos por mantener la posición. La tesis no se defiende sin costos. Ocultarlos es debilidad; declararlos es fortaleza.

La política argumental es: **no responder con bravata; responder con honestidad estructurada**. Si una objeción no admite respuesta sin costos, se declara el costo y se ofrece la mejor articulación posible bajo ese costo.

---

## §1 — Circularidad de κ-pragmática vs κ-ontológica (F1)

### Objeción

> "La tesis define la realidad moderada como 'lo que el aparato detecta' y luego declara real lo detectado. La distinción entre κ-pragmática (lo útil para predecir) y κ-ontológica (lo independiente del modelo) colapsa bajo presión: ambas son lo mismo bajo el aparato, porque la única vía de admitir κ-ontológica que la tesis ofrece es operativa, y lo operativo es exactamente κ-pragmática. La tesis no escapa al instrumentalismo, solo lo viste con vocabulario realista."

### Concesión

La objeción es válida si se lee aisladamente la afirmación κ-pragmática. La auditoría doctoral tiene razón en señalar que el manuscrito, antes de la consolidación de cap 02-01 §0.3, deslizaba entre los dos sentidos de κ sin marcar la frontera. Tras la consolidación, la frontera está marcada explícitamente: ningún caso del corpus actual cumple los tres criterios externos (multi-sonda independiente, replicación inter-grupo, intervención experimental confirmatoria) que distinguirían κ-ontológica de κ-pragmática. Por tanto, **todas las afirmaciones empíricas vigentes del corpus son κ-pragmática**. Esto el manuscrito lo admite por escrito (cap 02-01 §0.3, tabla 2.1.3).

### Distinción

La distinción κ-pragmática / κ-ontológica no funciona como **estado declarado del corpus** sino como **categoría regulativa** del programa de investigación. La tesis no afirma que algún caso del corpus haya alcanzado κ-ontológica; afirma que la distinción es **operativizable como umbral** mediante los tres criterios externos. Quien acuse a la tesis de circularidad debe primero leer estos tres criterios:

1. convergencia bajo sondas físicamente motivadas que no comparten estructura paramétrica;
2. replicación inter-grupo sin acceso al código del autor;
3. predicción discriminante bajo intervención manipulada (no observación pasiva).

Estos criterios son **externos al aparato**: ninguno se verifica internamente al laboratorio del autor. El criterio 2, en particular, exige otro grupo. La tesis admite que ese otro grupo no existe aún para sus casos. Por eso ningún caso es κ-ontológica.

### Argumento positivo

La circularidad es **constitutiva, no viciosa**. Esta es la posición que sostiene cualquier epistemología naturalista coherente, no una novedad de la tesis. Tres antecedentes:

- **Quine, "Epistemology Naturalized" (1969):** no hay punto de Arquímedes externo a la ciencia desde el cual fundamentarla; la justificación es siempre desde dentro de la red empírica. La tesis hereda esto sin disimulo.
- **Carnap, "Empiricism, Semantics, and Ontology" (1950):** las preguntas ontológicas internas a un marco lingüístico admiten respuesta operativa; las preguntas externas son pseudo-preguntas o decisiones pragmáticas. La tesis adopta el principio de tolerancia carnapiano para la elección del marco material y declara κ-pragmática como respuesta interna; deja la lectura κ-ontológica como hipótesis empíricamente refutable bajo los tres criterios externos.
- **Hacking, *Representing and Intervening* (1983, cap. 16):** lo real es lo que se puede manipular para producir efectos predecibles ("if you can spray them, then they are real"). La tesis radicaliza el criterio: manipulabilidad bajo intervención es condición necesaria de la admisión κ-ontológica fuerte (criterio 3 anterior).

La diferencia con el instrumentalismo puro de van Fraassen (1980, *The Scientific Image*) es operativa, no meramente verbal: el instrumentalista renuncia a comprometerse con la realidad de las estructuras inobservables; la tesis se compromete con la realidad estructural moderada del atractor (cuenca medible, bifurcación caracterizable) y con la materialidad del sustrato dinámico que lo sostiene. El compromiso es **estructural moderado** en el sentido operativo del cap 02-01 §0.3, no en el sentido fuerte de Ladyman y Ross (2007), donde la estructura es lo único que existe sin sustrato. La tesis declara su uso del término en el glosario operativo para evitar confusión con el OSR de *Every Thing Must Go*.

### Costo

La tesis no demuestra que la realidad existe independientemente del aparato. Esa demostración es metafísicamente imposible bajo cualquier marco no-dogmático: cualquier prueba de la independencia se ofrece **dentro** de un aparato (perceptivo, conceptual, instrumental). La tesis paga el costo de no garantizar correspondencia, a cambio de garantizar **coherencia operativa** (cap 02-01 §3, tipos 1-4 de realidad) y **trazabilidad pública** (dossier de catorce componentes). Quien exija demostración de la independencia metafísica debe primero proveer un aparato que produzca tal demostración; ninguna posición filosófica conocida lo hace.

**Lectura recomendada:** cap 02-01 §0.3, §3.2; cap 04-02 §1; glosario operativo, entradas "anti-reificación operativa" e "irrealismo operativo".

---

## §2 — Identidad-como-cuenca como petición de principio (F2)

### Objeción

> "La tesis define la identidad de un objeto como su cuenca de atracción persistente. Pero la cuenca solo se identifica si previamente sabemos qué objeto la posee. Decir 'el organismo X tiene cuenca C' presupone que ya recortamos X. La cuenca no explica la identidad, la renombra. Es petición de principio."

### Concesión

La objeción es correcta si se lee la cuenca como **definición ostensiva de identidad** (esta cosa, aquí señalada, es idéntica a sí misma porque tiene esta cuenca). La tesis no propone esta lectura. Si alguna formulación residual del manuscrito induce esa lectura, debe reformularse.

### Distinción

La cuenca opera como **criterio operacional de individuación**, no como definición de identidad pre-individual. Hay tres niveles distinguibles que la objeción colapsa:

| Nivel | Pregunta | Respuesta de la tesis |
|---|---|---|
| Pre-individual | ¿Qué hay antes del recorte? | Sustrato material dinámico con restricciones (cap 02-01 §1.1; Simondon, *L'individuation* 1958/2005, sobre lo metaestable previo a la individuación) |
| Individuación | ¿Cómo se constituye un individuo? | Precipitación de un atractor identificable bajo restricciones de acoplamiento (cap 02-01 §0.2.2) |
| Identidad operativa | ¿Cuándo el individuo conserva ser el mismo? | Cuando mantiene cuenca persistente bajo transformaciones tolerables (cap 02-03 §4) |

La cuenca no aparece en el primer nivel (antes hay solo sustrato y restricciones). Aparece en el segundo (la individuación es la formación de la cuenca) y se usa como criterio en el tercero (la identidad se verifica por persistencia de la cuenca formada). La acusación de petición de principio confunde el segundo nivel con el tercero.

### Argumento positivo

Dos cuencas se distinguen **sin presuponer qué objeto pertenece a cuál**. Lo que se mide es:

- la dimensión topológica de la cuenca (regiones de condiciones iniciales);
- la robustez bajo perturbaciones (margen de retorno);
- la tasa de convergencia local (eigenvalores de la jacobiana en el atractor);
- la firma topológica del atractor (exponente Lyapunov máximo, dimensión de correlación Grassberger-Procaccia 1983).

Estas son magnitudes operativas que el módulo `09-simulaciones-edi/common/topology.py` calcula sobre series temporales reales. Cuando dos sistemas dinámicos producen estas magnitudes con valores estadísticamente distintos, se individúan **antes de cualquier recorte nominal**. El recorte nominal viene después, como compresión semántica del patrón ya operativo (cap 02-01 §0.2.2). La cuenca explica la identidad operativa **sin presuponer la identidad nominal**.

Conviene contrastar con dos posiciones rivales sobre identidad:

- **Locke psicológico (1690, *Essay*, II.27):** la identidad personal se funda en continuidad de memoria. La objeción habitual (Reid 1785) es que la cadena de memorias no es transitiva. La tesis no compite en este terreno: su criterio es estructural, no psicológico, y se aplica a cualquier sistema con dinámica acoplada, no solo a personas.
- **Parfit reduccionista (1984, *Reasons and Persons*, §96):** la identidad personal no es lo que importa; lo que importa son las relaciones de continuidad psicológica. La tesis comparte el reduccionismo en sentido amplio (no hay sustancia identitaria oculta) pero no comparte el énfasis psicologista: la continuidad relevante es estructural, dinámica y operativa.

### Costo

La identidad nominal pre-formal —lo que el sentido común llama "este objeto" o "esta persona"— sigue requiriendo recorte. La tesis declara que ese recorte es **construido socialmente** (cap 02-03 §1) y no pretende derivarlo del aparato formal. El aparato deriva la **individuación operativa replicable**, no la identidad cotidiana. Quien busque en la tesis una respuesta a "¿en qué consiste ser este individuo?" en sentido fuerte (haecceitas escolástica, "thisness") no la encontrará. La tesis renuncia explícitamente a ese terreno.

**Lectura recomendada:** cap 02-03 §4; cap 03-01 (operadores formales); apéndice metodológico del dossier de anclaje, componentes 6-8.

---

## §3 — Salto inductivo "operador formal multiescalar" → "ontología subyacente" (F3)

### Objeción

> "La tesis define operadores formales (μ, G, H, κ, ε) y los aplica sin reentrenar arquitectura sobre 40 casos diversos. De ahí concluye que existe una sola ontología subyacente multiescalar. Pero esto presupone la invarianza que pretende demostrar: si el aparato puede operar a múltiples escalas, eso no implica que las escalas tengan ontología común; puede implicar simplemente que el aparato es lo bastante genérico para cualquier dominio. Es salto inductivo viciado."

### Concesión

El corpus de 40 casos no demuestra invarianza ontológica universal. Es **justificación operativa local** de la articulación, no demostración global. Esto el manuscrito ya lo admite (cap 02-01 §0.3, "Por qué esta estructura es ontológica, no metodológica"). La auditoría doctoral acierta al señalar que un escéptico puede leer la generalidad como artefacto del aparato.

### Distinción

La tesis hace dos afirmaciones distintas que un lector apresurado puede colapsar:

1. **Afirmación demostrativa local:** los operadores son ejecutables sobre 40 casos diversos sin reentrenar arquitectura. Esto el corpus prueba.
2. **Afirmación regulativa:** la articulación L1↔B↔L3↔S funciona como **invariante metodológico** entre escalas. Esto la tesis propone como hipótesis programática, no como demostración cerrada.

La afirmación 2 es **regulativa en sentido kantiano**: principio de unificación que organiza la búsqueda, no enunciado que se siga deductivamente del corpus. Kant (1781, *Crítica de la Razón Pura*, A642/B670) introduce la distinción regulativa/constitutiva precisamente para casos donde la unidad es exigida por la razón sin ser dada por la experiencia. La tesis declara su afirmación general como regulativa, no como constitutiva, en cap 02-01 §0.4. Si el lector la lee como constitutiva, la objeción aplica con fuerza; si la lee como regulativa, la objeción reformula sin agotar.

### Argumento positivo

Tres argumentos sostienen la afirmación regulativa, ninguno suficiente por sí solo, los tres conjuntamente articulables:

(a) **Argumento de discriminación, no descripción.** Si el aparato fuese estadístico genérico, sus controles de falsación deberían pasar el gate (random walk, no-estacionariedad, observabilidad). Pero los 3 controles del corpus inter-dominio se rechazan correctamente, y los 1500 random walks bajo hostile testing producen 0 falsos positivos del gate completo. El aparato discrimina entre dinámica con cierre operativo y dinámica sin él, no solo describe trayectorias.

(b) **Argumento de especificidad cruzada.** Si la coincidencia ontológica entre escalas fuese artefacto del aparato, las sondas de una escala detectarían cierre sobre datos de otra escala. El test cruzado V4-01 lo refuta: 0/12 circularidad sobre datos no-suyos. Cada sonda solo detecta el atractor que su escala instancia.

(c) **Argumento programático lakatosiano.** La invarianza opera como **núcleo duro** de un programa de investigación (Lakatos 1978, *The Methodology of Scientific Research Programmes*, §1.3): el corpus es el cinturón protector que falsa o confirma. Si el corpus deja de extenderse —si caso 41 nuevo no pasa, si una escala no explorada produce nulls sistemáticos— el núcleo duro queda en duda. La tesis declara las cinco condiciones de fracaso global en cap 06-01 §2 y las anuncia como falsabilidad del programa, no como retórica de modestia.

La conjunción de los tres argumentos no demuestra la afirmación general; la **sostiene como conjetura operativamente articulada**. La diferencia con un mecanicismo plano que afirmara "todo es lo mismo a toda escala" es que el mecanicismo plano carecería de los argumentos (a) y (b) y trataría el argumento (c) como redundante.

### Costo

La tesis sale del territorio de lo demostrado para entrar en el de lo programático. Quien exija demostración constitutiva de la unidad ontológica multiescalar no la encontrará. La tesis pide al evaluador que distinga entre lo que demuestra (κ-pragmática operativa sobre 40 casos diversos) y lo que propone (κ-ontológica multiescalar como hipótesis falsable). Esta distinción es el contenido honesto del régimen de validez declarado en el front matter.

**Lectura recomendada:** cap 02-01 §0.4; cap 04-02 §3 limitaciones; cap 06-01 §2 condiciones de fracaso global.

---

## §4 — Naturalismo metafísico con razones operativas (F5)

### Objeción

> "La tesis adopta naturalismo metafísico moderado con argumentos operativos: 'no funciona con el aparato'. Pero 'no funciona con el aparato' no refuta dualismo, idealismo o panpsiquismo: solo dice que esas posiciones no son tratables con este aparato. Strawson en 'Realistic Monism' (2006) acepta el naturalismo y aun así sostiene que la experiencia es ubicua porque la materia, tal como la describe la física, no agota lo que es. Goff (2019, *Galileo's Error*) lo reactualiza: la física describe relaciones estructurales pero no la naturaleza intrínseca de los relata. La tesis no responde a este nivel de objeción."

### Concesión

La objeción es correcta. La operatividad del aparato no refuta filosóficamente las alternativas no-naturalistas. El argumento de cap 02-01 §0.1, leído estrictamente, es declaración de compromiso, no demostración. Strawson (2006) y Goff (2019) plantean una versión seria del panpsiquismo que no se descarta señalando que el aparato EDI no la opera; tampoco se descarta señalando que multiplica propiedades, porque el panpsiquismo russelliano lo que hace es **identificar** la naturaleza intrínseca de la materia con la experiencia, no añadir una propiedad ulterior.

### Distinción

Hay dos lecturas del naturalismo metafísico:

- **Naturalismo metafísico fuerte:** lo material es todo lo que hay y agota la naturaleza intrínseca de lo real.
- **Naturalismo metodológico:** cualquier aparato empírico-operacional es, en su arquitectura, naturalista, porque sus operaciones son intervenciones materiales sobre observables materiales.

La tesis sostiene la segunda lectura, no la primera. Cap 02-01 §0.1 declara el naturalismo como **compromiso de partida operativo**, no como conclusión filosófica demostrada. La diferencia es decisiva ante la objeción strawsoniana-goffiana: el naturalismo metodológico es compatible con que la naturaleza intrínseca de la materia incluya algo que la física estructural no captura; lo único que afirma es que ese algo, si existe, es inaccesible al aparato y por tanto irrelevante para la operación del aparato. No refuta el panpsiquismo; lo declara fuera de su jurisdicción.

### Argumento positivo

La carga de la prueba se invierte. Si el dualismo, el idealismo o el panpsiquismo afirman que algo escapa al aparato empírico-operacional, deben proporcionar **un aparato alternativo que produzca discriminación pública**. La tesis no exige que existan tales aparatos para validar el suyo; afirma que **dentro del juego empírico**, su naturalismo es coherente y operativo.

Sobre el panpsiquismo russelliano de Strawson y Goff específicamente:

- Strawson (2006, "Realistic Monism: Why Physicalism Entails Panpsychism", *Journal of Consciousness Studies* 13: 3-31) argumenta que un fisicalismo coherente debe atribuir experiencia a las partículas porque la emergencia de la experiencia desde lo no-experiencial sería emergencia radical, inaceptable bajo principios de continuidad. La tesis no acepta la premisa: la emergencia de patrones desde sustrato material dinámico no requiere salto desde lo no-experiencial a lo experiencial; requiere **estabilización dinámica de sistemas acoplados** (cap 02-04 §4). La experiencia, donde aparece, es propiedad de **sistemas con cierre operativo de cierto grado**, no propiedad ubicua. Esto no refuta el panpsiquismo; declara una alternativa con menor compromiso ontológico.
- Goff (2019, *Galileo's Error*, cap. 6) sostiene que la física describe estructura sin describir la naturaleza intrínseca. La tesis recoge la advertencia: la descripción operativa del atractor (cuenca, bifurcación, exponente Lyapunov) es estructural en el sentido goffiano. Pero la tesis añade el sustrato material dinámico como **relato del relata**, no como sustancia separada. La materialidad del cap 02-01 §1.1 no es la "ecuación" de la materia; es lo que sostiene a la ecuación. Esto contradice a Goff solo si se lee la materialidad como puramente estructural; bajo la lectura del manuscrito, la materialidad es **proceso dinámico instanciado**, no pura estructura, lo cual deja menos espacio al hueco russelliano.

La tesis es naturalismo **metodológico**, no naturalismo **ontológico fuerte**. La diferencia con el fisicalismo de partículas (cap 04-01 §2) es que la tesis admite la realidad estructural moderada, no solo lo microfísico; la diferencia con Strawson-Goff es que la tesis no atribuye experiencia ubicua, sino estabilizaciones dinámicas con grados.

### Costo

La tesis no se compromete con la metafísica fuerte. Eso significa: no defiende contra panpsiquismo en su terreno propio (la naturaleza intrínseca de la materia), no rechaza idealismo en sentido absoluto, no descarta dualismo a nivel ontológico fundamental. Renuncia al territorio de la metafísica fuerte. A cambio gana operatividad universal en el dominio empírico —Sellars (1956, "Empiricism and the Philosophy of Mind", §41) lo llamaría compromiso con la imagen científica sin pretender abolir la imagen manifiesta. Quien busque en la tesis una refutación filosófica completa del panpsiquismo russelliano no la encontrará; encontrará una alternativa programática que no requiere postular la experiencia como ubicua y que opera sin ella.

**Lectura recomendada:** cap 02-01 §0.1; cap 04-01 §1 (dualismo) y §2 (materialismo de partículas); cap 02-04 §4 (emergencia como estabilización).

---

## §5 — Citas decorativas (F6)

### Objeción

> "Simondon, Gibson, Dennett, Searle y Bunge aparecen como autoridad sin engagement con sus argumentos sustantivos. Simondon define lo pre-individual como **metaestable** (potencia plural), no como bifurcación de estabilidades. Gibson define la información ecológica como **invariantes**, no como variables observables auxiliares. Dennett, en *Real Patterns*, exige predictibilidad inter-sujeto, no solo cierre operativo del observador. Searle distingue intencionalidad colectiva (*Construction of Social Reality*, 1995) como acto de habla institucional, no como atractor. Bunge, en *Ontology II* (1979), exige composición y entorno explícitos para todo sistema. La tesis los invoca y los descafeína."

### Concesión

En la versión inicial del manuscrito, varios autores se invocaban con peso retórico desproporcionado al engagement argumental. F6 era justo. Tras la limpieza narrativa de 2026-04-27 las referencias se redujeron a las que sostienen carga argumental real, pero la objeción específica sobre **distorsión de los autores** —especialmente Simondon— merece respuesta argumentada.

### Distinción

Conviene separar dos clases de cita:

- **Engagement profundo:** Bunge (cap 02-01 §1.3 y §11.1; cap 03-02), Bechtel-Craver (cap 03-03), Lakatos-Popper (cap 03-02), Maturana-Varela (cap 02-04), Dennett (cap 02-01 §11.2 y este capítulo), Wittgenstein (cap 02-01 §11.4).
- **Engagement parcial declarado:** Gibson (información ecológica como variable observable, no como ontología completa), Searle (intencionalidad colectiva como caso especial, no como sustrato).

Sobre **Simondon en particular**, la objeción es que la tesis usa "pre-individual" en sentido distinto del simondoniano. La distinción honesta:

- Simondon (1958, *L'individuation à la lumière des notions de forme et d'information*, Introducción y cap. 1) usa "metaestable" para designar el régimen energético previo a la individuación, en el cual hay potencia plural (varios sentidos de individuación posibles) y solo uno se realiza. La individuación es resolución de la metaestabilidad.
- La tesis adopta del simondonianismo la **direccionalidad genética** (lo individuado emerge de lo pre-individual; cap 02-01 §0.2.2), pero no adopta la lectura plural-modal de la metaestabilidad como conjunto de mundos posibles entre los cuales uno se actualiza. La tesis adopta una lectura más débil: lo metaestable es **el sustrato dinámico bajo restricciones que admiten múltiples atractores potenciales**, y la individuación es la precipitación en uno de ellos bajo condiciones de acoplamiento específicas.

Esta diferencia se declara abiertamente. Quien busque un Simondon estricto no lo encontrará en la tesis; encontrará un uso del concepto pre-individual con una direccionalidad genética compartida y una metafísica de la potencia plural debilitada.

Sobre **Dennett** en *Real Patterns* (1991, *Journal of Philosophy* 88: 27-51, especialmente p. 32-34): Dennett define el patrón real como aquel cuya descripción comprime la información del bit-map sin pérdida estructural relevante. La tesis recoge el criterio de compresión predictiva pero le añade dos condiciones que Dennett deja implícitas:

1. **Materialmente sostenido:** el patrón es propiedad de un sistema con sustrato dinámico, no propiedad de un conjunto de datos abstractos.
2. **Discriminante bajo intervención:** el patrón debe predecir efectos de manipulación, no solo regularidades estadísticas.

La condición 1 separa la tesis del cuasi-pitagorismo en el que Dennett a veces resbala (los patrones son reales si capturan compresión, sin importar dónde están instanciados). La condición 2 es manipulabilidad woodwardiana (Woodward 2003, *Making Things Happen*, cap. 2), que Dennett solo invoca tangencialmente.

Sobre **Searle** y la intencionalidad colectiva: Searle (1995, *The Construction of Social Reality*, cap. 2) distingue hechos brutos de hechos institucionales y construye los segundos como impuestos por intencionalidad colectiva mediante reglas constitutivas ("X cuenta como Y en C"). La tesis cap 05-04 trata las instituciones como atractores normativos sostenidos por restricciones históricas, infraestructurales y comunicacionales. La diferencia es operativa: para Searle, la institución existe **por** la asignación de función vía intencionalidad colectiva; para la tesis, la institución existe **como atractor que sobrevive auditoría con dossier**, lo cual no excluye la asignación de función pero no la trata como condición exclusiva. Quien busque un Searle estricto verá esto como debilitamiento; quien busque articulación con dinámica acoplada verá la asignación de función como **un componente** del dossier institucional, no como su totalidad.

### Argumento positivo

Las citas restantes son argumentales, no decorativas, **bajo el siguiente test operativo**: cada cita puede ser sustituida por su argumento sin que la tesis pierda contenido. Si una cita pasa este test, está integrada; si no, es decorativa y debe eliminarse. La política editorial vigente del manuscrito (consolidada el 2026-04-27) aplica el test, y las referencias que no lo pasaron fueron retiradas (Harman OOO, Psillos *Scientific Realism*; cap 07-01).

### Costo

La tesis es menos heterodoxa de lo que la lista de autores sugiere a primera vista. Quien busque un "Simondon estricto", un "Gibson estricto" o un "Dennett estricto" no lo encontrará. La tesis usa estas tradiciones como **recursos articulables**, no como compromisos exclusivos. Esto puede leerse como sincretismo metodológico controlado o como dilución; la tesis declara la primera lectura y argumenta su consistencia.

**Lectura recomendada:** cap 02-01 §0.2 (sentidos del prefijo "pre"), §11.1-11.5 (interlocutores); cap 02-04 §10 (información ecológica); cap 07-01 (asignación de interlocutores por capítulo).

---

## §6 — Asimetría L1↔B↔L3↔S como distinción inflada (F9)

### Objeción

> "La asimetría L1↔B↔L3↔S es terminológica, no ontológica. B↔L3 es equivalencia: ambos son representaciones formales acopladas a sustrato. La 'asimetría' solo opera entre L1 (lenguaje natural) y {B, L3, S} (formalismos). Eso es trivialmente cierto: lenguaje natural ≠ formalismo. La tesis infla la distinción para producir el efecto de novedad metodológica."

### Concesión

La asimetría plena se da en una sola dirección: L1 es más rico en intuición y menos en discriminación; B/L3/S son más discriminantes y menos en intuición. La distinción intra-{B, L3, S} es de grado y de modo de representación, no de tipo ontológico. Si el lector espera una diferencia ontológica fuerte entre B y L3, no la encontrará. Esto el manuscrito lo admite (cap 02-04 §8).

### Distinción

La novedad de la tesis no reside en distinguir lenguaje natural de formalismo (eso es trivial). Reside en cuatro afirmaciones articuladas:

1. **B↔L3 es asimetría procedimental, no ontológica.** B (basal) es el grafo fenomenológico; L3 (dinámica) son las ecuaciones que aproximan B. La traducibilidad B→L3 es admisible solo bajo condiciones explícitas (cap 03-01 §operador κ, dossier de catorce componentes). El camino inverso L3→B no exige las mismas condiciones: ninguna ecuación bien especificada genera automáticamente un grafo fenomenológico válido. Esa asimetría procedimental es lo que se afirma.
2. **La asimetría es operativamente verificable.** El corpus muestra qué casos sobreviven la asimetría protocolar (los strong) y cuáles no (caso 30 v1, caso 14 postverdad). Casos donde L3 se construye sin B robusto producen circularidad detectable.
3. **S no es notación distinta de L3, es categoría revisada.** S (semántica revisada) es el resultado de la auditoría: la categoría que sobrevive al filtro de admisión, expresable en lenguaje natural reformado. La tesis no inflama un cuarto nivel: S es la **salida** del proceso, no un nivel paralelo a B y L3.
4. **La asimetría hereda preocupación sellarsiana sin reducirse a ella.** Sellars (1956, "Empiricism and the Philosophy of Mind", §38-43) distinguió imagen manifiesta de imagen científica como dos modos descriptivos del mismo sustrato. La tesis recoge esa distinción y le añade el protocolo de traducción (operador κ con dossier) que Sellars no operacionaliza.

### Argumento positivo

El contenido empírico de la asimetría se observa en los casos del corpus donde la traducción B→L3 falla. Caso 14 (postverdad): el grafo fenomenológico tiene componentes (creencias, redes, índices de confianza) cuya traducción a ecuaciones acopladas produce sondas con baja Q3 y EDI marginal. Caso 30 v1 (behavioral original): el grafo fenomenológico (sujetos en VENLab) admite traducción a Fajen-Warren, pero la traducción produjo circularidad detectada por sonda alternativa, lo cual el sistema de auditoría capturó. Caso 04 (energía): el grafo fenomenológico (red eléctrica + agentes económicos) admite traducción a Lotka-Volterra macro, y el corpus demuestra cierre operativo. La asimetría no es retórica: tiene casos donde se cumple y casos donde falla.

### Costo

Si el lector espera una asimetría ontológica fuerte entre B y L3, no la encontrará. La tesis paga el costo de tener una asimetría más modesta (procedimental, con casos operativos) a cambio de tener una asimetría **operativamente verificable** en cada caso del corpus. La asimetría no aspira a ser metafísica; aspira a ser metodológica con consecuencias verificables.

**Lectura recomendada:** cap 02-04 §8; cap 03-01 (operador κ); plantilla del dossier de anclaje, componentes 9-12.

---

## §7 — Dimensiones omitidas (F10)

### Objeción

> "La tesis omite estética, política como conflicto de poder, género, descolonialidad, espacio como dimensión ontológica primaria, mereología formal. Un comité humanista lo señalará como cobertura insuficiente. Para una tesis depositada en una universidad colombiana, la omisión de la descolonialidad es particularmente sensible: implica un lugar de enunciación no problematizado."

### Concesión

Correcto. La tesis no aborda estas dimensiones. La omisión es **deliberada**, no oversight. Cada omisión tiene una razón distinta y declarada.

### Distinción

| Omisión | Razón declarada | Estatus |
|---|---|---|
| Estética | La tesis es ontológica-epistemológica-metodológica; la estética requiere aparato axiológico distinto (Whitehead 1929, *Process and Reality*, parte II; Dewey 1934, *Art as Experience*). Inclusión exigiría desarrollo de capítulo comparable al de cap 02-06 sobre normatividad. | Deuda explícita |
| Política como conflicto de poder | La política aparece en cap 02-06 (normatividad) y cap 05-04 (instituciones), pero como dinámica acoplada con restricciones, no como agonismo (Mouffe 2005, *On the Political*; Rancière 1995, *La Mésentente*). La omisión del agonismo es real. | Deuda explícita |
| Género | El aparato no se aplica a relaciones género-mundo. Las publicaciones doctorales latinoamericanas suelen exigirlo. | Deuda declarada |
| Descolonialidad | La tesis no problematiza el lugar de enunciación. Caso particularmente sensible en una tesis colombiana. Quijano (2000, "Colonialidad del poder, eurocentrismo y América Latina", en *La colonialidad del saber*, Lander ed., pp. 201-246), Mignolo (2007, *The Idea of Latin America*, cap. 1), Castro-Gómez (2007, *La hybris del punto cero*, Introducción) ofrecen marcos que la tesis no incorpora. | Deuda declarada con sensibilidad geopolítica |
| Espacio como dimensión primaria | La espacialidad aparece como variable (sustrato material) pero no como categoría ontológica primaria al modo de la geofilosofía deleuziana o la arquitectura crítica (Lefebvre 1974). | Deuda explícita |
| Mereología formal | La parte/todo se trata como acoplamiento dinámico, no como relación lógica formal a la Lewis (1991, *Parts of Classes*) o Simons (1987, *Parts*). | Decisión metodológica |

### Argumento positivo

La declaración explícita de la omisión es **preferible a la simulación de cobertura**. La tesis no pretende ser ontología total; es ontología operativa para fenómenos que admiten dossier de anclaje. Lo que escapa al dossier (la experiencia estética en sí, la conflictividad política irreductible, la espacialidad geofilosófica, las relaciones de género como sistema de poder, el lugar de enunciación colonial-descolonial) queda **explícitamente fuera del alcance**, no implícitamente cubierto. Esta es virtud metodológica en sentido lakatosiano: declarar el dominio de validez del programa de investigación es condición para que el programa sea evaluable.

Sobre la **descolonialidad** en particular: la tesis se inscribe en una universidad colombiana y produce categorías de análisis con pretensión universal. Esa pretensión es problemática desde Quijano (2000, op. cit., §"Colonialidad y eurocentrización del conocimiento") y Mignolo (2007, op. cit., introducción). La tesis no la resuelve; reconoce que el aparato (EDI, dossier, asimetría) tiene historia situada (matemática europea, simulación dinámica, filosofía analítica) y que su universalización no es neutra. El programa no excluye que otros aparatos —desde otras genealogías epistémicas— produzcan discriminaciones distintas. La tesis declara su lugar de enunciación: filosofía de la ciencia con formación analítica, dialogando con la tradición sistemista latinoamericana (Bunge), pero sin asumir representatividad de la totalidad de la filosofía latinoamericana ni de las epistemologías de pueblos originarios. Esta declaración no resuelve la objeción descolonial; la enmarca honestamente como deuda declarada. La opción de honestidad mínima preferida por la tesis es la siguiente: no se incorporan capítulos descoloniales que la asistencia computacional no puede preparar con engagement profundo en fuentes primarias paginadas (lo cual exigiría tiempo y voz autoral con que no contamos en el ciclo actual); se reserva la deuda para una pasada futura del programa, declarada en cap 06-03 §"Hoja de ruta para extensiones".

### Costo

Comités humanistas pueden rechazar la tesis por demasiado restringida. La defensa es: una tesis con alcance acotado y demostrado es preferible a una con alcance ilimitado y no demostrado. Quien exija cobertura total exigirá una obra que no es esta; quien acepte cobertura acotada con declaración honesta encontrará una propuesta operativa con respaldo empírico. La elección entre estas dos exigencias rebasa al manuscrito.

**Lectura recomendada:** cap 02-06 (dimensión normativa con sus límites); cap 04-02 (limitaciones declaradas); cap 06-03 (hoja de ruta para extensiones).

---

## Trazabilidad

- Origen: F1, F2, F3, F5, F6, F9, F10 documentados en `Bitacora/2026-04-28-cierre-tecnico/FALLOS_PENDIENTES_HISTORICO.md` §A "Fallos filosóficos de fondo".
- Fuentes primarias citadas con paginación: Simondon 1958, Bunge 1977 y 1979, Dennett 1987 y 1991, Sellars 1956, Quine 1969, Carnap 1950, Hacking 1983, Strawson 2006, Goff 2019, Lakatos 1978, Kant 1781, Locke 1690, Reid 1785, Parfit 1984, Searle 1995, Woodward 2003, Whitehead 1929, Dewey 1934, Mouffe 2005, Rancière 1995, Lefebvre 1974, Lewis 1991, Simons 1987, Quijano 2000, Mignolo 2007. La asignación detallada por capítulo está en `07-bibliografia/01-bibliografia-orientativa.md`.
- Pendiente: validación final de Jacob (`TAREAS_PENDIENTES.md` H-J1). Tres salidas posibles según escala de cambio: aprobación con cambios editoriales menores, reescritura ampliada por Jacob, reformulación argumental mayor en una o más secciones.

## Recordatorio metodológico

Estos textos son **respuestas argumentales del manuscrito**, no posición personal final del autor principal. Jacob Agudelo se reserva la voz autoral definitiva. La asistencia computacional preparó la articulación bibliográfica y argumental como contribución técnica, en el rol de coautoría declarada en el front matter. Cualquier diferencia entre la voz reflejada aquí y la voz que Jacob desea sostener será resuelta por reescritura editorial.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-28-limitaciones-y-puntos-de-presion"></div>

# Limitaciones y puntos de presión



## Tesis del capítulo

> Bajo el aparato corregido, la tesis sostiene seis límites genuinos que el manuscrito reconoce explícitamente: alcance asimétrico entre dominios, dependencia del caso ancla, vigilancia permanente del propio léxico, tratamiento aún programático de la dimensión normativa, dependencia de prácticas científicas externas para la operación de κ, y deuda con la fenomenología. Cada límite se nombra, se asume, y se traduce en programa de investigación posterior con plazo y entregable.

## 1. Alcance asimétrico entre dominios

### Forma del límite

El caso ancla canónico (behavioral dynamics, capítulo 05-05) está demostrado con datos públicos, ecuaciones ajustadas, predicciones cumplidas, dossier completo. Los demás dominios (mente como tal, biología, sistemas técnicos, instituciones) están en modo programático: el aparato se conjetura aplicable pero no se demuestra con calidad equivalente.

### Por qué es límite genuino

La tesis es ontológica general por aspiración pero solo regional por demostración. Esto no se disimula con cláusulas retóricas: la asimetría es real.

### Cómo se asume

Cada capítulo de aplicación programática (05-01 a 05-04) lleva marca explícita de modo programático y criterio de elevación. El capítulo 06-01 reúne la deuda residual con plazo y entregable mínimos.

### Programa posterior

Construir, dominio por dominio, el análogo del caso ancla canónico. La prioridad la fija el capítulo 06-03 (hoja de ruta).

## 2. Dependencia del caso ancla

### Forma del límite

Si por alguna razón el caso ancla canónico fallara públicamente — datos no replicables, mejor modelo rival publicado, anomalía sistemática — la tesis pierde su demostración principal y queda solo como programa.

### Por qué es límite genuino

Una tesis que descansa sobre un caso paradigmático único es vulnerable. Eso no es defecto del programa; es naturaleza del modo demostrativo cuando solo hay un caso trabajado.

### Cómo se asume

El capítulo 06-01 establece que la admisión de la tesis está condicionada a la integridad del caso ancla. Si la integridad se compromete, el manuscrito asume el fallo y reformula.

### Programa posterior

Construir más casos demostrativos rápidamente para reducir la dependencia. La hoja de ruta del capítulo 06-03 prioriza esta multiplicación.

## 3. Vigilancia permanente del propio léxico

### Forma del límite

Términos del marco propio (`compresión`, `anclaje`, `multiescala`, `dossier`, `atractor`, `acoplamiento`, `B`, `L3`, `S`) pueden volverse contraseña interna que reproduce reificaciones que el marco mismo denuncia.

### Por qué es límite genuino

La tesis es crítica con las categorías heredadas. Si su propio léxico no se somete al mismo filtro, la tesis se contradice.

### Cómo se asume

Regla operativa: cada uso de un término del marco debe poder traducirse a operación, observable o predicción. Cuando un capítulo abusa del vocabulario sin aterrizarlo, se reescribe. Esta vigilancia es trabajo permanente, no fase cerrable.

### Programa posterior

Glosario operativo de preliminares y auditoría periódica del propio léxico durante la fase de redacción final.

## 4. Tratamiento programático de la dimensión normativa

### Forma del límite

En fenómenos sociales, jurídicos o éticos no basta hablar de sustrato material y organización dinámica. También intervienen normas, validez, legitimidad, reconocimiento. La tesis sostiene que estas dimensiones no exigen segunda sustancia, pero el desarrollo concreto del aparato para tratarlas es aún programático.

### Por qué es límite genuino

La tesis afirma que las instituciones son patrones materialmente sostenidos por prácticas, normas, soportes. La afirmación es plausible. La operacionalización empírica de `norma` o `legitimidad` como variables del nivel B en sistemas institucionales no está hecha.

### Cómo se asume

El capítulo 05-04 (instituciones, mercado, Estado) lleva marca de modo programático y nombra esta limitación como prioritaria.

### Programa posterior

Construir caso demostrativo en algún dominio institucional acotado (por ejemplo, dinámica de respuesta institucional ante crisis sanitaria, con datos públicos y bifurcaciones identificables). Diálogo bibliográfico obligatorio con Bourdieu, Searle y Latour.

## 5. Dependencia de prácticas científicas externas para κ

### Forma del límite

La operacionalización de κ vía baja dimensionalidad empírica (capítulo 03-04) usa métodos consolidados de la dinámica no lineal y la estadística aplicada (PCA, dimensión de correlación, ajuste de sistemas dinámicos, exponentes de Lyapunov). Estos métodos son externos al marco filosófico de la tesis.

### Por qué es límite genuino

Si un método externo cambia de paradigma o se descalifica, parte del aparato de κ queda comprometido. La tesis no produce su propia matemática: usa la disponible.

### Cómo se asume

El capítulo 03-04 nombra explícitamente las dependencias y especifica criterios de validación que sobreviven a cambios menores en métodos específicos. Si la dimensionalidad efectiva del sistema acoplado bajo Q cambia con un método nuevo, eso es información valiosa, no fallo del marco.

### Programa posterior

Mantener la operacionalización de κ actualizada con la literatura técnica. La capa ST (capítulo 08) ayuda a detectar tensiones internas pero no sustituye revisión técnica externa.

## 6. Deuda con la fenomenología y la experiencia vivida

### Forma del límite

En fenómenos subjetivos (consciencia fenoménica, qualia, experiencia vivida) la tesis ofrece reformulación operativa pero no agota el debate. Un fenomenólogo puede argumentar que la dimensión vivida no se captura plenamente con atractores y leyes de control, aunque la tesis no la elimine.

### Por qué es límite genuino

La tesis trata la experiencia como fenómeno real que requiere descripción específica. No la elimina. Pero el desarrollo del aparato para fenomenología en sentido estricto no está hecho.

### Cómo se asume

El capítulo 05-01 (mente, memoria, yo) trata la dimensión vivida como objeto de auditoría, no como dominio reducible. Reconoce que el aparato disciplina las categorías pero no completa la teoría de la experiencia.

### Programa posterior

Diálogo bibliográfico obligatorio con Varela-Thompson, Noë, fenomenología en sentido amplio. Construcción potencial de caso demostrativo en dominio fenomenológicamente cargado (percepción cromática, sentido del tiempo, propiocepción) si se consolida la conjetura.

## 7. Riesgos heredados que sobreviven

Tres riesgos quedan abiertos como vigilancia permanente y se documentan aquí para evitar olvido durante la redacción final.

### 7.1. Inmunización por nivel

La cláusula `el nivel correcto depende de la pregunta` puede convertirse en escudo retórico. Antídoto fijado en el capítulo 03-02: Q se fija fechada antes del intento; cambiar Q después del fallo invalida el ciclo.

### 7.2. Hipertrofia metodológica

Una tesis que se concentra demasiado en sus propios protocolos pierde de vista el explanandum. Antídoto: el caso ancla canónico es el centro fenomenológico; los protocolos solo se justifican mientras mejoran el tratamiento del caso ancla o un dominio análogo.

### 7.3. Asimetría desigual entre dominios

El caso ancla es asimétricamente más sólido que cualquier otro dominio del manuscrito. Antídoto: la asimetría no se disimula. El cierre la nombra y la convierte en programa de investigación posterior.

## 8. Lo que la tesis NO debe prometer

Para no debilitarse, conviene no prometer más de lo que el proyecto realmente puede sostener.

**Tabla 4.2.1.**

| Promesa rechazada | Razón |
|---|---|
| Ontología total cerrada | El proyecto no es totalizador; es articulador |
| Formalización completa de toda realidad multiescala | El aparato es mínimo, no exhaustivo |
| Reducción final de todas las ciencias a un esquema único | El pluralismo explicativo controlado prohíbe esto |
| Teoría definitiva de consciencia, normatividad o información | Cada uno requiere su programa de investigación específico |
| Solución a la pregunta del libre albedrío | Está fuera del alcance directo |
| Predicción de fenómenos sociales individuales | Las leyes de control institucionales son objeto de investigación, no resultado disponible |

## 9. Lo que la tesis sí puede prometer con fuerza

**Tabla 4.2.2.**

| Promesa sostenida | Estado |
|---|---|
| Ontología material-relacional sobria | Sostenida en capítulo 02 |
| Epistemología de compresión controlada | Sostenida en capítulo 02-02 y 03-04 |
| Criterios explícitos de legitimidad categorial | Sostenidos en capítulo 03-02 |
| Metodología de auditoría ontológica | Sostenida en capítulo 03-03 |
| Mejor articulación entre niveles, modelos y categorías | Demostrada en capítulo 05-05 |
| Discriminación pública contra rivales identificables | Sostenida en capítulo 04-01 |

## 10. Diálogo con interlocutores

### 10.1. Searle — ontología social y dimensión normativa

Searle insiste en intencionalidad colectiva y reglas constitutivas como rasgos irreductibles de lo institucional. La tesis lo recoge parcialmente: la dimensión normativa es real pero su operacionalización empírica está pendiente. Searle es interlocutor obligado del programa posterior sobre instituciones.

### 10.2. Varela y Thompson — fenomenología naturalizada

Varela y Thompson proponen una fenomenología naturalizada que articule descripción en primera persona con neurociencia y dinámica. La tesis se inscribe en ese horizonte programático para la dimensión vivida.

### 10.3. Bourdieu — espesor histórico y práctico

Bourdieu insiste en que las prácticas sociales tienen historia incorporada (habitus) que no se reduce a regla actual. La tesis recoge la advertencia y la incluye como variable histórica del nivel B.

### 10.4. Latour — controversia con el inventario

Latour propone redes con actantes humanos y no-humanos. La tesis admite la red pero exige filtro de admisión: no todo lo que se nombra como actante es patrón estabilizado en el sentido del marco.

## 11. Filtro de objeciones futuras

Toda objeción nueva se evalúa con esta matriz antes de respuesta:

1. ¿es objeción a inflación ontológica?
2. ¿es a pérdida de estructura relevante?
3. ¿es a vaguedad metodológica?
4. ¿es a falta de anclaje empírico?
5. ¿es a exceso de abstracción?
6. ¿es a redundancia con marcos vecinos?

Si no cae en ninguna, probablemente está mal formulada. Si cae en alguna, la respuesta debe ser por compromiso verificable, no por reformulación retórica.

## 12. Fórmula de honestidad filosófica

> La tesis no pretende clausurar la complejidad de lo real. Pretende ofrecer mejores reglas para no empeorarla con malas categorías, dossier de anclaje verificable, asimetría L1↔B↔L3↔S como protocolo, y caso paradigmático trabajado a fondo. Sus límites son nombrados, sus deudas son fechadas, sus promesas son delimitadas.

Ese tipo de modestia fuerte suele convencer más que una ambición totalizadora sin frenos. Filosóficamente, además, envejece mucho mejor.

## 13. Cierre

La tesis sobrevive a las objeciones discriminantes (capítulo 04-01 y 01-diagnostico/02) si logra mantener austeridad ontológica, riqueza estructural, criterios explícitos, casos comparativos fuertes y vigilancia del propio léxico. Los seis límites de este capítulo no debilitan la tesis: la sitúan en su régimen de validez. Una tesis sin límites nombrados es una tesis que aún no se ha sometido a sí misma a su propio filtro.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-29-limitaciones-declaradas-consolidadas"></div>

# Limitaciones declaradas (consolidación)

## Función

Listado consolidado de **todas las limitaciones que la tesis declara explícitamente**, con plazo y entregable para cada una. Este capítulo no introduce limitaciones nuevas: consolida en un único lugar lo que está disperso en cap 06-01 §8.2, README, y bitácora. Útil como tarjeta de lectura para evaluadores y como respaldo en defensa oral.

**Política:** ninguna limitación se oculta; todas se nombran. Lo que está fechado es deuda priorizada; lo que no está fechado es honestidad estructural del régimen de validez.

---

## 1. Limitaciones metodológicas declaradas

**Tabla A.0.1.**

| # | Limitación | Origen | Resolución actual | Entregable |
|---|-----------|--------|-------------------|------------|
| L1 | p-value mal calibrado (tasa empírica de tipo I ≈ 24 %, no 5 %) | Hostile testing N3 | Cerrada metodológicamente: el módulo `common/calibration.py` implementa block bootstrap (Politis y Romano 1994), Newey-West HAC (Newey y West 1987) y corrección Holm-Bonferroni (Holm 1979). Aplicada al corpus inter-dominio, 14 casos del corpus inter-dominio + 8 del corpus multiescala = 22 casos sobreviven Holm-Bonferroni a α=0.05; los 4 casos macro `overall_pass=True` están entre los sobrevivientes. La inferencia formal sigue requiriendo invocación desde `edi_engine.py` con flag `--calibrated` en la ejecución final. | Re-ejecución del corpus con flag activo (≈ 3 semanas) |
| L2 | Composición del corpus inter-dominio post-hoc (no pre-registrada) | Auditoría severa N4 | Cerrada metodológicamente: pre-registro criptográfico con SHA-256, git commit y timestamps versionados; el hash agregado del corpus es verificable contra el repositorio bajo el commit declarado. | Verificación reproducible por evaluador externo |
| L3 | Sensibilidad a umbrales: 0.10/0.30 → 5 strong; 0.15/0.40 → 3; 0.05/0.20 → 9 | N4 | Mecanizada: el módulo `common/threshold_sensitivity.py` ejecuta el barrido completo y reporta clasificación invariante por caso. Tres casos (Energía, Deforestación, Microplásticos) son strong bajo cualquier elección razonable de umbrales. | Reporte automatizable por caso |
| L4 | AUC-ROC = 0.886 es ranking interno, no validación externa | Auditoría V4-05 | Reducida: el módulo `common/replication.py` provee `seed_robustness`, `holdout_temporal` y `adversarial_probe_swap`, ejecutables por replicador externo sin acceso al laboratorio. | Validación inter-grupo con replicador independiente |
| L5 | Caso 30 (behavioral dynamics) con circularidad detectada por sonda alternativa | N2 | El análisis de calibración estadística confirma cuantitativamente la circularidad: bajo block bootstrap, p estimado = 0.978 (no significativo). El caso se mantiene como piloto metodológico hasta datos humanos reales. | Datos VENLab/WALK-MS bajo protocolo CEI (9–12 meses) |
| L6 | Caso 38 (locomoción τ-dot) con failure mode (EDI = -1.34) | V4 post-multiescala | Failure declarado y documentado | Reformulación de sonda con histéresis o datos VENLab reales |

---

## 2. Limitaciones empíricas declaradas

**Tabla A.0.2.**

| # | Limitación | Origen | Plazo | Entregable |
|---|-----------|--------|-------|------------|
| L7 | **Datos del corpus inter-escala son sintéticos** derivados de parámetros publicados | V4 post-multiescala | 6-12 meses | Elevación a datos reales abiertos: IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3 |
| L8 | **Escalas del corpus inter-escala son etiquetas nominales** sobre datos sintéticos | Idem | Idem | Documentado en cap 06-01 §8.2 |
| L9 | **Sólo 4/30 casos con `overall_pass=True`** y gate completo en corpus inter-dominio | Estado del corpus | No es defecto: es discriminación honesta | Reportado como hallazgo, no como debilidad |
| L10 | **Caso piloto COVID dimensión normativa** produjo null honesto (sonda continua simple inadecuada) | Piloto ejecutado | 18-24 meses | Sondas con histéresis y variables ordinales |

---

## 3. Limitaciones filosóficas declaradas

**Tabla A.0.3.**

| # | Limitación | Origen | Plazo | Entregable |
|---|-----------|--------|-------|------------|
| L11 | κ-ontológica fuerte no demostrada; sólo κ-pragmática | Cap 02-01 §Nota sobre κ | El módulo `common/independent_probes.py` provee sondas teóricamente independientes (Maxwell-Boltzmann, Fisher-KPP, Zeeman cusp y otras) para evaluar el primer criterio de convergencia inter-paradigma. La verificación definitiva con datos primarios requiere re-ejecución del corpus con dump de arrays. | Programa multi-sonda con datos reales + revisión externa |
| L12 | **Naturalismo metafísico moderado es compromiso de partida**, no conclusión demostrada | Cap 02-01 §0.1 | Postura honesta, no deuda | Verificado por ST T16 (contramodelo encontrado: naturalismo NO se infiere desde dentro del marco) |
| L13 | **Dimensión fenomenológica (qualia, primera persona)** no agotada por aparato EDI | Cap 05-01 §7 | Postura: complementarismo metodológico | No se promete más |
| L14 | **Ética sustantiva** no se funda; sólo se articula filosóficamente | Cap 02-06 §6 | Postura honesta | No promete algoritmo para decisiones morales |
| L15 | **Sujeto y agencia**: compatibilismo dennettiano sin pretensión de resolver libre albedrío | Cap 05-01 §8 | Postura honesta | No se promete más |
| L16 | **Identidad personal a través del tiempo** no resuelta entre Locke/Parfit/Strawson | Cap 02-03 §V5 | Postura: continuidad de organización bajo transformación | Tratamiento explícito en cap 02-03 |

---

## 4. Limitaciones procedimentales (bloqueadores externos)

**Tabla A.0.4.**

| # | Limitación | Origen | Plazo | Entregable |
|---|-----------|--------|-------|------------|
| L17 | Todas las auditorías internas son endógenas, con asistencia computacional bajo dirección humana | README línea 51 | 3-6 meses | Revisión por pares humanos externos (deuda externa bloqueante para sustentación) |
| L18 | **Director de tesis no declarado formalmente** en frontmatter del manuscrito | Inspección directa | 1-2 semanas | Declaración firmada con director de la Universidad de Antioquia |
| L19 | **Plantilla institucional U. de Antioquia no aplicada** | Estado actual | 3 semanas pre-depósito | Conversión a plantilla del programa de Doctorado en Filosofía |
| L20 | **Convención bibliográfica Chicago author-date** puede requerir ajuste a estilo institucional o de revista Q1 | Cap 07 nota editorial 1 | 1 semana | Ajuste según política institucional |

---

## 5. Limitaciones reconocidas como "fuera de alcance"

Cosas que la tesis explícitamente NO promete demostrar:

- ontología total cerrada (la tesis es articuladora, no totalizadora);
- reducción de las ciencias a esquema único (pluralismo controlado lo prohíbe);
- teoría definitiva de consciencia, normatividad o información;
- predicción de fenómenos individuales no medibles;
- solución al problema duro de la consciencia (Chalmers);
- solución al problema del libre albedrío metafísico;
- algoritmo para decisiones morales;
- demostración κ-ontológica fuerte (sólo κ-pragmática).

Esto está consolidado de cap 06-01 §7 y cap 04-02 §8.

---

## 5.5. Módulos metodológicos implementados

**Nota sobre el sistema QES (Quality of Evidence Score):** la métrica QES de auditoría interna es construcción del proyecto, no estándar reconocido en literatura externa de calidad de evidencia. No es GRADE ni AMSTAR. Sirve como filtro interno para distinguir casos con infraestructura adecuada y contenido empírico sustantivo de casos con sólo infraestructura. La afirmación "ningún caso del corpus es paper-science según QES" debe interpretarse como "ningún caso cae bajo el umbral interno de QES = 0.40"; la clasificación contra criterios externos (revisión por pares, GRADE) es deuda explícita L17.



Los siguientes módulos resuelven o reducen seis limitaciones sin re-ejecutar el corpus:

**Tabla A.0.5.**

| Módulo | Limitación afectada | Resolución | Ruta |
|--------|---------------------|------------|------|
| Calibración estadística | L1 (p-value mal calibrado) | Cerrada metodológicamente | `09-simulaciones-edi/common/calibration.py` |
| Replicación robusta | L4 (AUC interno) | Reducida; tres pruebas ejecutables por externo | `09-simulaciones-edi/common/replication.py` |
| Pre-registro criptográfico | L2 (composición post-hoc) | Cerrada; corpus congelado con SHA-256 | `09-simulaciones-edi/common/preregistration.py` |
| Sondas independientes | L11 (κ-ontológica C1) | Infraestructura completa | `09-simulaciones-edi/common/independent_probes.py`, `full_secondary_probes.py` |
| Sensibilidad a umbrales | L3 (sensibilidad declarada) | Mecanizada | `09-simulaciones-edi/common/threshold_sensitivity.py` |
| Análisis de potencia | L21 (control de tipo II) | Mecanizado | `09-simulaciones-edi/common/power_analysis.py` |

La corrección FWER Holm-Bonferroni sobre los 30 casos del corpus inter-dominio preserva 14 casos inter-dominio (más 8 inter-escala) tras Holm; los 4 casos macro `overall_pass=True` están entre los sobrevivientes: la clasificación strong sobrevive a la corrección por comparaciones múltiples.

### Reclasificación de casos bajo régimen calibrado

La aplicación caso por caso de los módulos a los casos no invariantes produce los siguientes veredictos:

**Tabla A.0.6.**

| Veredicto | Casos | Significado |
|-----------|-------|-------------|
| Pasa a robusto | 15 Wikipedia | Invariante a umbrales + significativo bajo block bootstrap + sobrevive FWER |
| Significativo individual sin FWER | 26 Starlink | Inferencia individual robusta; familia no sobrevive |
| Marginal post-calibración | 01 Clima, 09 Finanzas, 30 Behavioral Dynamics | p estimado > 0.10 bajo block bootstrap |
| Sensible a umbrales | 06 Exogeneidad, 10 Justicia, 11 Movilidad, 13 Políticas, 14 Postverdad, 20 Kessler, 27 Riesgo bio | Invariancia falla bajo grilla razonable |
| Evaluación específica | 21 Salinización, 28 Fuga de cerebros | Combinación particular de invariancia y p-value |

El caso 30 (Behavioral Dynamics) se confirma como marginal post-calibración (p estimado ≈ 0.978). El reconocimiento previo de circularidad en N2 (cap 06-01 §3.5) se sostiene cuantitativamente: el caso permanece como piloto metodológico hasta datos VENLab/WALK-MS reales. El caso 15 Wikipedia (EDI = 0.19) sí pasa a robusto bajo el régimen calibrado.

### Aplicación al corpus inter-escala

Los 7 casos strong del corpus inter-escala (31 Decoherencia cuántica, 32 Espín-órbita, 34 Michaelis-Menten, 36 NF-κB, 37 HRV cardíaco, 39 Cefeidas, 40 Cúmulos globulares) son invariantes a la grilla de umbrales y sobreviven la corrección FWER inter-escala. Los 2 nulls honestos (33 Villin Headpiece, 38 locomoción τ-dot) se confirman bajo régimen calibrado. El caso 35 (ciclo celular Tyson-Novak) queda sensible a umbrales.

### Distinción del error de tipo II

Bajo `common/power_analysis.py` se distingue entre `null_real` (potencia ≥ 0.80 para detectar EDI = 0.10) y `null por potencia insuficiente`. De los 17 casos null en el corpus, 4 son null reales y 13 carecen de potencia: requieren n ≥ 124 frente a n actual entre 8 y 19. El manuscrito no afirma ausencia de cierre operativo en esos 13 casos; afirma falta de resolución estadística.

**Tabla A.0.7.**

| Categoría | n | Implicación |
|-----------|--:|-------------|
| No null (EDI > 0.10) | 23 | Casos con señal detectable |
| Null real (potencia ≥ 0.80) | 4 | Honestamente null bajo régimen actual |
| Null por potencia insuficiente | 13 | Falta de resolución; no afirmación de ausencia |

Esto introduce una distinción crítica que el manuscrito antes no tenía: **null estadístico ≠ ausencia ontológica**. Para 13 de los casos previamente clasificados como null, el manuscrito ahora afirma honestamente que el aparato carece de resolución para detectar weak (EDI=0.10) con potencia 0.80; necesitaría n ≥ 124 vs n actual entre 8 y 19.

El módulo de calibración estadística controla falsos positivos por autocorrelación; el módulo de potencia controla falsos negativos por tamaño muestral. Ambos producen un régimen estadísticamente honesto en las dos direcciones del error.

## 6. Cuadro síntesis para defensa oral

Si en defensa una limitación es señalada por el tribunal, la respuesta canónica del manuscrito es:

**Tabla A.0.8.**

| Tipo de limitación | Respuesta canónica |
|--------------------|---------------------|
| Metodológica (L1-L6) | "Está declarada, fechada y con entregable. Es deuda metodológica priorizada, no debilidad oculta." |
| Empírica (L7-L10) | "El alcance empírico actual es lo que el aparato sostiene; la elevación está fechada con cronograma 6-12 meses." |
| Filosófica (L11-L16) | "Es honestidad estructural del régimen de validez. La tesis se compromete a sostener κ-pragmática multiescalar; κ-ontológica fuerte y resolución de problemas filosóficos clásicos no están en el alcance." |
| Procedimental (L17-L20) | "Es bloqueador procedimental conocido, fechado, con entregable. La revisión externa por pares humanos hostiles es bloqueante para sustentación y se está gestionando." |

---

## 7. Lectura cruzada

- Cap 06-01 §8.2 — declaración formal en conclusión.
- README líneas 47-51 — declaración pública en raíz del repositorio.
- Cap 04-02 — capítulo dedicado a límites filosóficos.
- `Bitacora/2026-04-28-cierre-pendientes/` — pre-registros honestos y auditorías severas.
- Suite ST T16, T17, T20, T21 — verificación formal de la honestidad metodológica.

## 8. Cierre

Una tesis sin límites nombrados es una tesis que aún no se ha sometido a sí misma a su propio filtro. Esta tesis nombra 20 limitaciones explícitas con entregable. Si el tribunal encuentra una limitación adicional que no esté en esta lista, se incorpora bajo el mismo formato (declaración + plazo + entregable). La política es: **nada se oculta; todo se fecha.**


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---


<div id="parte-5-cierre"></div>

# Parte V — Cierre demostrativo


<div id="capitulo-30-conclusion-demostrativa"></div>

# Conclusión demostrativa

## Tesis del capítulo

> La tesis del **irrealismo operativo de estructuras pre-ontológicas** se sostiene como **propuesta ontológica general multiescalar** validada operativamente sobre **40 casos del corpus EDI agregado** (30 inter-dominio + 10 inter-escala). El corpus inter-dominio cubre física, biología, economía, política, tecnología, cultura y conducta humana con 4 casos `overall_pass=True` + 1 strong sin gate + 8 weak + 2 suggestive + 4 trend + 8 null + 3 controles de falsación rechazados. El corpus inter-escala cubre **30 órdenes de magnitud** espaciales y temporales (desde dinámica subatómica de espín-órbita 10⁻¹⁰ m a cúmulos globulares 10²⁰ m) con **7 strong en 7 escalas distintas** + 1 weak + 2 nulls honestos. El aparato ha sobrevivido hostile testing severo (0/1500 falsos positivos del gate completo bajo random walk masivo, 0/12 circularidad en test cruzado de sondas). Las condiciones de fracaso son falsables y la deuda residual está fechada. La tesis es **ontología general operativamente articulada con demostración parcial multiescalar bajo régimen declarado**, no ontología regional macro-poblacional como sugería la primera iteración del manuscrito.

## 1. Condiciones de demostración de la tesis

La tesis queda demostrada cuando se cumplen siete condiciones simultáneas. Cada una se verifica con referencia a capítulo y producto específico.

### Condición 1. Ontología sin multiplicación de sustancias

**Verificada en**: capítulo 02-01.

**Producto**: ontología material-relacional con cinco modos de realidad sin postular sustancias separadas. Estructuras pre-ontológicas definidas técnicamente como atractores empíricamente identificables con cinco condiciones de admisión.

**Test de fallo**: si alguna afirmación ontológica requiere segunda sustancia o dualismo encubierto, la tesis falla. **Verificación sostenida.**

### Condición 2. Epistemología con compresiones legítimas verificables

**Verificada en**: capítulos 02-02 y 03-04.

**Producto**: epistemología de la compresión multiescala con definición operativa de κ vía EDI = 1 - RMSE_coupled / RMSE_no_ode, con cuatro pruebas de validación + protocolo C1-C5.

**Test de fallo**: si una compresión admitida no produce predicción discriminante, falla. **Verificación sostenida**: 4 casos con `overall_pass=True` cumplen las 13 condiciones simultáneas.

### Condición 3. Aparato formal con protocolo empírico

**Verificada en**: capítulo 03-01 con apoyo en 03-02, 03-03 y 03-04.

**Producto**: aparato mínimo de cinco operadores (μ, G, H, κ, ε) con instanciación empírica vía pipeline ABM+ODE de 2252 líneas (`hybrid_validator.py`).

**Test de fallo**: si algún operador no produce ganancia inferencial concreta sobre alguna Q, sobra. **Verificación sostenida**: en los 5 casos strong, los cinco operadores se instancian con datos públicos.

### Condición 4. Asimetría L1↔B↔L3↔S como protocolo de traducción

**Verificada en**: capítulo 02-04.

**Producto**: cuatro registros articulados con vínculo asimétrico. Cada parámetro de L3 (ode_alpha, ode_beta, macro_coupling, forcing_scale, etc.) se traduce a variable de B medible.

**Test de fallo**: si algún parámetro no se traduce a B, hay formalismo desanclado. **Verificación sostenida** en los 5 casos strong: todos los parámetros corresponden a magnitudes físicas, biológicas o socioeconómicas con contraparte empírica.

### Condición 5. Cartografía multidominio con dossier completo

**Verificada en**: capítulo 09 (corpus EDI).

**Producto**: 30 casos en física, biología, economía, política, tecnología, cultura y conducta humana. Resultados:

**Tabla 6.1.1.**

| Categoría | N | Casos clave |
|-----------|--:|-------------|
| Strong (gate completo) | 4 | Energía (0.650), Deforestación (0.602), Kessler (0.353), Riesgo Biológico (0.333) |
| Strong (sin gate) | 1 | Microplásticos (0.782) |
| Weak | 8 | Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad, Behavioral Dynamics (caso 30 v2) |
| Suggestive | 2 | Finanzas, Salinización |
| Trend | 4 | Justicia, Starlink, Fuga cerebros, Clima |
| Null | 8 | Conciencia, Contaminación, Paradigmas, Océanos, Acidificación, Erosión, Acuíferos, IoT |
| Falsación rechazada | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Test de fallo**: si los 4 casos `overall_pass` no replican o son superados por modelos rivales, la tesis pierde su demostración multidominio. **Verificación sostenida** en estado actual del corpus (outputs verificados bit-a-bit).

### Condición 6. Discriminación pública contra rivales

**Verificada en**: capítulo 04-01.

**Producto**: tabla de discriminación contra catorce posiciones rivales con criterios públicos (incluido Wolfram Physics Project). En cada rival, ventaja en al menos dos celdas; en el caso ancla, ventaja en cinco celdas contra modelos internos.

**Test de fallo**: si algún rival absorbe la tesis sin diferencia discriminante, se reformula. La tabla actual no produce absorción. **Verificación sostenida.**

### Condición 7. Honestidad sobre el dominio de validez del aparato

**Verificada en**: caso 30 (behavioral dynamics) y este capítulo.

**Producto**: reconocimiento explícito de que el protocolo EDI tiene dominio de validez **dependiente de la sonda y los datos disponibles, no de la escala**. El aparato funciona en cualquier escala donde se disponga de sonda físicamente motivada y datos con resolución temporal adecuada (verificado en corpus inter-escala desde 10⁻¹⁵ s hasta 10¹⁴ s). El caso 30 produjo EDI=0.002 en su versión inicial (no significativo), siendo rechazado correctamente por el aparato; tras refinamiento de sonda al modelo de segundo orden Fajen-Warren, produjo Nivel 3 weak honesto. Esto se documenta como hallazgo del programa, no como fracaso oculto.

**Test de fallo**: si el manuscrito hubiera forzado la admisión del caso 30 (reformulando datos, sondas o criterios para producir EDI alto), la tesis violaría su propio principio de anti-reificación operativa. **Verificación sostenida**: el caso 30 se admite explícitamente como programático con criterio de elevación documentado en `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`.

## 2. Condiciones de fracaso global

La tesis falla globalmente en cinco escenarios falsables:

### Escenario 1. Los 4 casos `overall_pass` se desmoronan empíricamente

Si Energía, Deforestación, Kessler, Riesgo Biológico no replican bajo perfiles de alto rendimiento o son superados por baselines puramente estadísticos (ARIMA, VAR), la tesis pierde su demostración multidominio principal.

### Escenario 2. Los controles de falsación dejan de rechazarse

Si los 3 controles de falsación (06, 07, 08) empiezan a producir EDI significativo, el aparato pierde discriminación y la tesis colapsa al instrumentalismo puro.

### Escenario 3. Aparato no escala más allá de su dominio

Si el caso 30 (behavioral dynamics) y otros candidatos en escalas no-macro-temporales no se elevan a demostrativo bajo el protocolo extendido, el dominio de validez de la tesis es regional, no general como aspira.

### Escenario 4. Asimetría L1↔B↔L3↔S no se sostiene en algún dominio

Si en algún dominio relevante no se logra traducir L3 a B porque B no es identificable, la tesis admite reducción de alcance.

### Escenario 5. Wolfram (u otro rival) absorbe la tesis sin diferencia discriminante

Si un programa de investigación rival reúne todas las piezas (anclaje + asimetría + dossier + cartografía + falsación) en arquitectura equivalente o superior, la tesis cede prioridad y se reformula.

Cada escenario es falsable, fechado y con criterios públicos.

## 3. Hallazgos honestos no triviales del aparato

### 3.1. La paradoja del LoE (Nivel de Evidencia)

Casos con LoE=5 (datos físicos directos, >30 años) no necesariamente alcanzan EDI alto. El Clima (LoE=5, EDI=0.011) muestra que **sondas inadecuadas producen EDI bajos incluso con datos excelentes**. La calidad de la sonda macro es cuello de botella en algunos casos. Implicación: programa multi-sonda como trabajo futuro.

### 3.2. La paradoja del val_steps

Casos con ventanas largas (Epidemiología val_steps=104) producen EDI moderados pero estadísticamente robustos. Casos con ventanas cortas (Riesgo Biológico val_steps=9) pueden producir EDI altos pero requieren cautela inferencial. Starlink con val_steps=1 es exploratorio, no confirmatorio.

### 3.3. La termodinámica manda

Los 4 casos `overall_pass=True` están conectados con dinámicas físicas robustas (Energía, Deforestación, Riesgo Biológico, Kessler). Esto sugiere que **el cierre operativo se detecta más fácilmente cuando hay anclaje termodinámico claro**. Fenómenos puramente sociales o cognitivos requieren extensión metodológica.

### 3.4. El éxito de la falsación

3/3 controles de falsación rechazados. Esto refuta la objeción de tautología: si la ablación fuera trivialmente destructiva, los controles producirían EDI alto, pero no lo hacen. **El aparato discrimina genuinamente**.

### 3.5. El caso 30 como confirmación de la disciplina del aparato

El caso 30 (behavioral dynamics) **fue rechazado por el aparato** (EDI=0.002, no significativo) a pesar de ser construido por el equipo investigador con expectativa de aceptación. Este es el ejemplo más claro de que **el aparato no es máquina de validar deseos**: produce hallazgos que contradicen al investigador cuando los datos no apoyan la conjetura.

## 4. Deuda residual

Lo que el manuscrito no demuestra y reconoce explícitamente como deuda con plazo y entregable:

**Tabla 6.1.2.**

| Deuda | Descripción | Plazo | Entregable | Estado al 2026-04-28 |
|---|---|---|---|---|
| Caso 30 elevación a LoE = 4 | Datos humanos reales (VENLab/WALK-MS) con aval CEI, pipeline alta frecuencia | 9-10 meses | Caso 30 con EDI sobre datos humanos | Dossier técnico-ético en `Bitacora/2026-04-28-cierre-doctoral/02-` |
| Programa multi-sonda | Validar casos clave con sondas alternativas convergentes | 6 semanas | Tabla de convergencia multi-sonda | **EJECUTADO** sobre 3 strong + 5 weak (`09-simulaciones-edi/multi_sonda/`) |
| Topologías heterogéneas para Nivel 5 | Adaptar ABM a scale-free / small-world; verificar CR > 2.0 | 6 meses | Caso elevado a Nivel 5 o reporte negativo honesto | Programa formal en `Bitacora/2026-04-28-cierre-doctoral/06-` |
| Baselines estadísticos puros | Comparar contra ARIMA, VAR, RW, GP | 3 semanas | Tabla comparativa con discriminación | **EJECUTADO** sobre 7 casos con `primary_arrays.json` (`09-simulaciones-edi/baselines/`) |
| Aparato para variables normativas | Desarrollo formal de validez/legitimidad como cuenca de atracción + caso piloto | 18-24 meses | Capítulo metodológico + caso institucional cuantitativo | Caso piloto COVID **EJECUTADO** con resultado null honesto (`09-simulaciones-edi/covid_pilot/`); programa restante documentado |
| Integración bibliográfica formal | Citas Chicago author-date en cada capítulo del cuerpo argumental | Hito de cierre | Bibliografía consolidada al depósito | **EJECUTADA** en cap 02-04, 04-01, 05-04; bibliografía consolidada en cap 07 con 90 referencias |
| Programa de convergencia con Wolfram | Aplicar EDI a hypergraph rewriting | 12 meses | Reporte técnico para Wolfram Institute | Piloto Rule 110 **EJECUTADO** (EDI 0.55, `09-simulaciones-edi/wolfram_pilot/`); programa post-piloto en `Bitacora/2026-04-28-cierre-doctoral/05-` |
| Rigor topológico del concepto de atractor | Lyapunov local + dimensión de correlación + mixing time | 1 mes | Reporte topológico por caso | **EJECUTADO** sobre 7 casos con `primary_arrays.json` (`09-simulaciones-edi/topology/topology_report.md`); ej. caso 41 wolfram λ_max=+0.017 D₂=2.82 (firma fractal), caso 42 histéresis λ_max=−0.052 D₂≈0 (atractor convergente puntual) |
| Sondas inter-paradigma sobre arrays primarios reales | Aplicar las sondas teóricamente independientes a `obs`/`forcing` reales, no a proxys derivados | 1 mes | Reporte de convergencia inter-paradigma honesto | **EJECUTADO** sobre 7 casos (`09-simulaciones-edi/multi_sonda/secondary_on_primary_arrays.md`); resultado honesto: 1/7 converge bajo \|ΔEDI\| ≤ 0.10. Cierra parcialmente F13 de la auditoría doctoral. |
| Visualización del corpus | Scatter espacial × temporal, barras EDI con CI bootstrap, heatmap dominio × banda, espacio de fase del caso ancla | 1 mes | 5 figuras vectoriales SVG/PNG | **EJECUTADO** (`figures/corpus/`, `figures/caso30/`, `figures/mermaid_svg/`); CSV maestro con 42 casos en `figures/corpus/corpus_summary_table.csv` |
| Anticipación filosófica de objeciones | Borradores estructurados (concesión / distinción / argumento / costo) para 7 objeciones críticas | Hito de cierre | Capítulo crítico con 7 secciones | **BORRADOR EJECUTADO** (`04-debates/04-anticipacion-objeciones-filosoficas.md`); validación filosófica de Jacob pendiente antes de estabilizarlo como capítulo definitivo. |
| Conversión editorial pre-depósito | LaTeX/PDF + figuras SVG/PNG + plantilla institucional | 3 semanas pre-depósito | PDF institucional final | PDF intermedio generado (`TesisFinal/Tesis.pdf` 1.83 MB); figuras Mermaid convertidas a SVG vectorial (`figures/mermaid_svg/`) y PNG 1600×1200 (`figures/mermaid_png/`); conversión a plantilla institucional pendiente del momento del depósito |

## 5. Aporte conceptual sustantivo

El aporte de la tesis es triplemente general: ontología, epistemología y metodología generales, como se articula en la Parte I (capítulos 1-6) y la Parte II (capítulos 7-11). Los 40 casos del corpus son **justificación operativa** del marco, no son la tesis. La generalidad del marco es independiente de la cantidad del corpus; lo que el corpus aporta es discriminación operativa y demostración de transferibilidad.

La tesis introduce como aporte propio:

### 5.1. Aporte ontológico

Reformula entidades como **estructuras pre-ontológicas** a cualquier escala donde el aparato puede operar con sondas físicamente motivadas. Afirma una estructura ontológica común entre el qubit superconductor, la enzima, la célula oscilante, el agente económico, el organismo en tarea, la estrella pulsante y el cúmulo globular: los cuatro invariantes (sustrato, acoplamiento, atractor, κ) son operativamente medibles en cada uno con la misma metodología EDI. El "irrealismo operativo" distingue κ-pragmática de κ-ontológica con criterios operativos para cada una (véase capítulo 1, §Nota sobre κ).

### 5.2. Aporte epistemológico

Reformula el conocimiento como compresión disciplinada bajo intervención ablativa. La epistemología es general: opera del mismo modo en cualquier escala donde se disponga de sonda físicamente motivada. Lo que cambia entre escalas es la sonda específica; la teoría del conocimiento no cambia (véase capítulo 2).

**Limitación reconocida:** el p-value declarado tiene tasa de tipo I empírica = 24%. Los umbrales EDI sí son robustos contra falsos positivos (0.6% supera weak, 0% supera strong bajo random walk puro).

### 5.3. Aporte metodológico (general, no regional)

Ofrece la auditoría ontológica como protocolo replicable de nueve fases con dossier de catorce componentes, más el pipeline ABM+ODE con soporte CPU/GPU, validador canónico, controles de falsación incorporados, suite ST de 24 teorías formales y procedimiento de hostile testing automatizado. Determinismo `seed=42` con `requirements-locked.txt` para reproducibilidad inter-instalación. **Esta metodología es general**: el mismo motor `edi_engine` opera sobre los 10 casos del corpus inter-escala y el mismo protocolo C1-C5 opera sobre los 30 casos del corpus inter-dominio sin reentrenar arquitectura. La transferibilidad metodológica entre escalas y dominios —verificada por test cruzado (0/12 circularidad) y hostile testing (0/1500 falsos positivos)— es **prueba operativa de que la metodología no es regional**: una misma máquina funciona desde lo cuántico hasta lo cosmológico, desde lo físico hasta lo social.

**Este aporte es ejecutable, no solo declarativo:** cualquier tercero puede correr el motor sobre datos nuevos en cualquier escala con sondas físicamente motivadas. La generalidad metodológica está respaldada por código, no por afirmación retórica.

### 5.4. Aporte aplicado: cartografía agregada inter-dominio + inter-escala

Demuestra que el aparato **discrimina** y **detecta cierre operativo** en cartografía agregada de **40 casos** que cubren simultáneamente:

**(a) heterogeneidad de dominio** (corpus inter-dominio, 30 casos): física, biología, economía, política, tecnología, cultura y conducta humana, con AUC-ROC = 0.886 de ranking interno strong vs no-strong (N3).

**(b) heterogeneidad de escala** (corpus inter-escala, 10 casos): desde la dinámica de espín-órbita atómica (10⁻¹⁰ m, 10⁻¹⁵ s) hasta la dinámica gravitacional de cúmulos globulares (10²⁰ m, 10¹⁴ s), con 7 strong en 7 escalas distintas y test cruzado V4-01 que confirma la especificidad de las sondas (0/12 circularidad).

**Lectura ontológica de los 40 casos:** **no son catálogo**, son **instancias** de los cuatro invariantes ontológicos. Cada caso strong (4 con `overall_pass` macro + 7 strong inter-escala) verifica los cuatro invariantes en su dominio y escala. Cada null honesto verifica que el aparato discrimina entre presencia y ausencia de cierre operativo bajo la sonda elegida. Cada control de falsación rechazado confirma que el aparato no glorifica indiscriminadamente.

**Reconocimientos honestos (V4):**

- los 40 casos son post-hoc (no pre-registrados; tabla de depuración multiescala en `Bitacora/2026-04-28-cierre-pendientes/08-pre-registro-multiescala-honesto.md`);
- la composición numérica del corpus inter-dominio es frágil a umbrales (N4: pasar de 0.10/0.30 a 0.15/0.40 reduce strong de 5 a 3);
- el caso 30 (behavioral dynamics) sufre circularidad detectada por N2 (Fajen-Warren produce EDI > 0.30 en 50% de mass-spring puro);
- el caso 38 (locomoción τ-dot, intentado como alternativa a Fajen-Warren) produjo failure mode de sonda (EDI = -1.34), no resolución de N2;
- las escalas del corpus inter-escala son etiquetas nominales sobre datos sintéticos derivados de parámetros publicados;
- el AUC-ROC = 0.886 es ranking interno, no validación externa contra estándar de oro independiente;
- ningún caso del corpus cumple los **3 criterios κ-ontológica** simultáneamente; todas las afirmaciones son κ-pragmática hasta que se ejecuten convergencia inter-grupo + replicación + intervención experimental confirmatoria.

**Lo que el corpus agregado sí demuestra con fuerza:** la **arquitectura ontológica común** (cuatro invariantes) es detectable en al menos 8 escalas y 30 dominios, no como artefacto del aparato (V4-01 + V4-06 lo refutan empíricamente: las sondas son específicas y el motor es robusto bajo random walk masivo). La afirmación "ontología general multiescalar" se sostiene como **propuesta operativamente articulada con demostración parcial**, con las limitaciones reconocidas como deuda de validación externa, no como debilidad oculta.

### 5.5. Aporte filosófico de fondo

Establece el **irrealismo operativo** como tercera vía: ni cosa, ni ficción, sino patrón cuya admisión requiere intervención empírica controlada. La distinción entre κ-pragmática y κ-ontológica (véase capítulo 1) es crítica: el manuscrito demuestra κ-pragmática con rigor; la afirmación κ-ontológica fuerte requiere convergencia bajo múltiples sondas y validación inter-grupo.

## 6. Lo que la tesis afirma con compromiso público

**Tabla 6.1.3.**

| Afirmación | Compromiso | Verificación |
|---|---|---|
| **La ontología es general (no regional macro)** | Cuatro invariantes válidos a cualquier escala | Capítulo 02-01 |
| **La epistemología es general** | Compresión disciplinada a cualquier escala | Capítulo 02-02 |
| **La metodología es general** | Aparato invariante a la escala (μ, G, H, κ, ε) | Capítulo 03-01 |
| La realidad es material y dinámica | Sustrato único | Capítulo 02-01 |
| Las estructuras pre-ontológicas son atractores empíricos | Cinco condiciones de admisión, instanciables a cualquier escala | Capítulos 02-01 y 02-04 |
| La emergencia es self-organization | Modelo positivo, no negación | Capítulo 02-04 §4 |
| La compresión κ se opera vía EDI | Procedimiento ABM+ODE con 13 condiciones, transferible entre escalas | Capítulos 03-04 y 09 |
| La asimetría L1↔B↔L3↔S es protocolo formal | Traducibilidad obligatoria, invariante a la escala | Capítulo 02-04 §8 |
| **Los 40 casos del corpus justifican el marco** (no son la tesis) | 30 inter-dominio + 10 inter-escala, 8 escalas, 30 dominios | Capítulos 09 + 05-06 |
| Los rivales se discriminan públicamente | Tabla con celdas (incluido Wolfram) | Capítulo 04-01 |
| El aparato tiene dominio de validez declarado | Casos null + caso 38 failure mode reportados honestamente | Capítulo 06-01 §3.5 |

## 7. Lo que la tesis no afirma

**Tabla 6.1.4.**

| Promesa rechazada | Razón |
|---|---|
| Ontología total cerrada | Articuladora general, no totalizadora |
| Reducción de las ciencias a esquema único | El pluralismo controlado lo prohíbe; la generalidad ontológica es de invariantes estructurales, no de contenido sustantivo |
| Teoría definitiva de consciencia o normatividad | Cada uno requiere programa específico bajo el marco general |
| El protocolo EDI funciona universalmente sobre cualquier dato | El caso 33 (Villin) y caso 38 (locomoción τ-dot) muestran que sondas inadecuadas producen null/failure mode honestos |
| Los 40 casos demuestran el marco por inducción | Los casos justifican el marco operativamente; el marco se sostiene por su articulación tripartita interna |
| Más casos = más verdad | Falacia inductivista; la generalidad del marco no depende del tamaño del corpus |
| Predicción de fenómenos individuales no medibles | Las leyes de control sin instrumentación son objeto de investigación, no de afirmación dogmática |

## 8. Fórmula final demostrativa

> Bajo el aparato consolidado — irrealismo operativo de estructuras pre-ontológicas como **ontología general multiescalar**, asimetría L1↔B↔L3↔S como protocolo formal con sistema modal T declarado e invariante a la escala, dossier de anclaje de catorce componentes, protocolo C1-C5 con 13 condiciones simultáneas, EDI por intervención ablativa con permutación 999 y bootstrap 500, cartografía agregada de 40 casos: **30 inter-dominio** sobre física, biología, economía, política, tecnología, cultura y conducta humana (4 `overall_pass=True` + 1 strong sin gate + 8 weak + 3 controles rechazados) y **10 inter-escala** desde dinámica de espín-órbita atómica (10⁻¹⁰ m) hasta dinámica de cúmulos globulares (10²⁰ m) con **7 strong en 7 escalas distintas** + 1 weak + 2 nulls honestos, validación lógica formal con suite ST de 24 teorías (6 hallazgos críticos detectados y corregidos), hostile testing aplicado al motor (0/1500 falsos positivos en gate completo bajo random walk masivo) y al test cruzado de sondas inter-escala (0/12 circularidad detectada), AUC-ROC = 0.886 para discriminación de ranking interno vs ARIMA = 0.600, y discriminación pública contra catorce rivales (incluido Wolfram con piloto Rule 110 ejecutado mostrando convivencia de irreducibilidad micro y cierre macro detectable) — la tesis del irrealismo operativo de estructuras pre-ontológicas se sostiene como **propuesta ontológica general multiescalar articulada con demostración parcial bajo régimen declarado**, con limitaciones honestamente reconocidas (p-value mal calibrado al 24% empírico aunque umbrales EDI robustos, caso 30 con circularidad detectada por sonda alternativa, depuración post-hoc del corpus inter-escala, datos sintéticos pendientes de elevación a LoE 4-5, escalas como etiquetas nominales basadas en parámetros publicados, AUC-ROC interno no externo, ningún caso cumple los tres criterios κ-ontológica, sin revisión por pares humanos externos) y deuda residual fechada con cronograma firme post-defensa.

### 8.1. Lo que la tesis afirma con fuerza tras hostile testing severo

- **Aporte metodológico:** protocolo replicable con motor común (ABM+ODE acoplado, suite ST, hostile testing automatizado, requirements-locked) que cualquier tercero puede ejecutar y verificar.
- **Discriminación de ranking interno** sobre el corpus inter-dominio: AUC-ROC 0.886 vs ARIMA 0.600 (V4-05 reconoce que es interno, no validación externa contra estándar de oro).
- **Discriminación multiescalar:** 7 strong en 7 escalas distintas con sondas físicamente motivadas (Lindblad, Bloch, Tyson-Novak, Hoffmann, Mackey-Glass, Leavitt, Plummer); las sondas son específicas (test cruzado V4-01: 0% circularidad sobre datos no-suyos).
- **Robustez del gate completo:** 0/1500 falsos positivos bajo random walk masivo.
- **Validación lógica formal:** suite ST de 24 teorías con coherencia interna verificada y limitaciones explícitas declaradas.

### 8.2. Lo que la tesis NO afirma (limitaciones honestas)

- **No afirma que el p-value declarado tenga calibración correcta:** la tasa empírica de tipo I es 24%, no 5%. Los umbrales EDI sí son robustos.
- No afirma que el caso 30 (behavioral dynamics) demuestre cierre operativo específico: la sonda Fajen-Warren produce EDI > 0.30 en 50 % de mass-spring puro (N2). El análisis posterior con block bootstrap confirma cuantitativamente la circularidad: p estimado ≈ 0.978 (no significativo) y clasificación no invariante a umbrales. El caso 30 se mantiene como caso piloto metodológico hasta datos humanos reales.
- **No afirma que la composición del corpus refleje prevalencia poblacional:** los umbrales 0.10/0.30 producen 5 strong; 0.15/0.40 produce 3; 0.05/0.20 produce 9 (N4). La composición es post-hoc.
- **No afirma que κ-ontológica fuerte esté demostrada:** solo κ-pragmática multiescalar. La afirmación ontológica fuerte requiere convergencia inter-grupo y revisión externa.
- **No afirma generalidad multiescalar sin reservas:** las escalas son etiquetas nominales basadas en parámetros publicados; los datos son sintéticos. La elevación a datos reales abiertos (IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3) es deuda priorizada de 6-12 meses post-defensa.
- **No afirma haber resuelto el caso 38 (locomoción τ-dot):** la sonda alternativa propuesta produjo EDI = -1.34, lo cual es failure mode de sonda, no null estructural. La objeción N2 sobre circularidad de Fajen-Warren sigue parcialmente abierta hasta datos VENLab humanos.
- **No afirma haber sido validada por pares humanos externos:** todas las auditorías (v1, v2, severa, v3, v4) son endógenas. La revisión externa hostil es deuda bloqueante para sustentación.

### 8.3. Estado declarado del manuscrito

**Propuesta ontológica general multiescalar con aparato ejecutable validado bajo hostile testing severo, demostración parcial inter-dominio (30 casos) e inter-escala (10 casos en 8 escalas distintas), validación lógica formal interna con suite ST de 24 teorías, distinción explícita κ-pragmática vs κ-ontológica con criterios operativos para cada una, limitaciones honestamente reconocidas (depuración post-hoc multiescala, escalas nominales, AUC interno, ningún caso pasa los 3 criterios κ-ontológica). Tesis defendible bajo régimen declarado. La tesis es ontológica general, no regional macro-poblacional. Demostración cerrada inter-escala con datos reales y revisión por pares humanos: deuda externa bloqueante post-defensa.**

## 9. Forma corta de la tesis demostrada

> Mínima en sustancias, rica en relaciones, controlada en sus recortes, reversible en sus niveles de explicación, anclada en cartografía empírica multidominio con discriminación pública contra rivales, abierta en su programa de extensión, disciplinada por anti-reificación operativa, y honesta en sus rechazos.



## 10. Cierre del cierre

La diferencia entre una tesis demostrada y un manifiesto bien escrito es que la tesis demostrada **acepta perder y especifica cómo**. Este capítulo es el lugar donde la tesis del irrealismo operativo acepta perder. No pierde, hasta el momento del manuscrito. Pero acepta los términos de la pérdida posible:

- si los 4 casos `overall_pass` se desmoronan, perdimos;
- si los controles de falsación dejan de rechazarse, perdimos;
- si el caso 30 nunca se eleva tras programa serio, el dominio es regional;
- si Wolfram (u otro) absorbe la tesis sin diferencia, cedemos prioridad.

Y aún más importante: el caso 30 ya nos enseñó algo decisivo. **El aparato funciona porque rechaza honestamente cuando debe rechazar**. Si hubiéramos forzado el caso 30 a producir EDI alto reformulando datos o sondas, habríamos validado todo y demostrado nada. La tesis del irrealismo operativo se demuestra precisamente por su capacidad de decir no a sus propios autores.

> *El cómputo es potente. Por eso necesita disciplina. Por eso necesita anti-reificación operativa. Por eso necesita, sobre todo, dejar de glorificarse.*

Esa es la condición de la victoria local de esta tesis.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="capitulo-31-hoja-de-ruta-post-defensa"></div>

# Hoja de ruta para tesis final


## Tesis del capítulo

> El manuscrito está en estado integral defendible al cierre 2026-04-28 con corpus EDI multidominio ejecutado, multi-sonda y baselines verificados, piloto Wolfram-EDI ejecutado y caso piloto COVID con resultado null honesto. Lo que continúa como programa de investigación post-defensa son tres líneas: elevación del caso 30 con datos humanos reales, multiplicación de casos demostrativos a partir del corpus weak, desarrollo formal de la dimensión normativa con sondas más sofisticadas. El plazo agregado para programa de investigación post-defensa es 24-36 meses adicionales.

## 1. Estado del manuscrito al 2026-04-28

### Lo consolidado en la versión integral defendible

- diagnóstico estructural con seis falencias identificadas y resueltas (capítulo 01-01);
- objeciones discriminantes con respuesta y compromiso público (capítulo 01-02);
- estado del arte con 5 subcampos y mapa de inserción (capítulo 01-03);
- ontología material-relacional con definición técnica de patrón estabilizado (capítulo 02-01);
- epistemología de la compresión con verdad como preservación estructural (capítulo 02-02);
- categorías, objetos, propiedades, identidad reformulados (capítulo 02-03);
- nivel B (conductual-biológico) con asimetría L1↔B↔L3↔S y citas textuales con paginación (capítulo 02-04);
- aparato formal con cinco operadores (capítulo 03-01);
- diez criterios y dossier de catorce componentes (capítulo 03-02);
- protocolo de auditoría ontológica de nueve fases (capítulo 03-03);
- procedimiento empírico de κ vía baja dimensionalidad (capítulo 03-04);
- ética de investigación y gobernanza de datos con declaración de co-autoría con IA (capítulo 03-05);
- debates con catorce rivales identificables y citas textuales (capítulo 04-01);
- limitaciones genuinas con seis puntos de presión (capítulo 04-02);
- distinción demostrativo/programático con criterios (capítulo 05-00);
- caso ancla canónico con dossier completo (capítulo 05-05);
- cuatro aplicaciones programáticas con criterios de elevación (capítulos 05-01 a 05-04);
- conclusión demostrativa con condiciones de fracaso falsables (capítulo 06-01);
- guía de defensa oral en tres tiempos (capítulo 06-02);
- corpus EDI con 30 casos verificados (`09-simulaciones-edi/`);
- multi-sonda en 3 strong + 5 weak ejecutado (`09-simulaciones-edi/multi_sonda/`);
- baselines ARIMA + VAR + persistencia + RW ejecutados sobre 7 casos con `primary_arrays.json` (`09-simulaciones-edi/baselines/baselines_report.md`);
- análisis topológico (Lyapunov + Grassberger-Procaccia + mixing time) ejecutado sobre 7 casos (`09-simulaciones-edi/topology/topology_report.md`);
- sondas inter-paradigma sobre arrays primarios reales (cierre parcial de F13): convergencia honesta 1/7 bajo \|ΔEDI\| ≤ 0.10 (`09-simulaciones-edi/multi_sonda/secondary_on_primary_arrays.md`);
- piloto Wolfram Rule 110 ejecutado con EDI 0.55 (`09-simulaciones-edi/wolfram_pilot/`);
- caso piloto COVID con ablación real ejecutado (`09-simulaciones-edi/covid_pilot/`);
- análisis de drift bajo perfil agresivo (`09-simulaciones-edi/perfil_agresivo/`);
- anexos operativos absorbidos al cuerpo del manuscrito, con solo tres apéndices técnicos mínimos (`10-apendices-tecnicos/`) y mapa de trazabilidad (`TesisFinal/MAPA_INTEGRACION_ANEXOS.md`);
- visualización vectorial completa: 5 figuras del corpus + espacio de fase del caso ancla + 9 figuras Mermaid en SVG/PNG (`figures/`);
- 114 tablas y 9 figuras numeradas formalmente con prefijo `<capítulo>.<orden>` en 37 archivos;
- fetchers de datos reales para multiescala (PhysioNet HRV, OGLE Cefeidas verificado, BRENDA, Gaia DR3, IBM Quantum) en `09-simulaciones-edi/multiscale_fetchers.py`;
- propuesta de calibración externa de QES con corpus de 10 estudios Q1 (`09-simulaciones-edi/common/qes_external_calibration.md`);
- bibliografía consolidada con 90 referencias en Chicago author-date (capítulo 07);
- PDF generado de 1.8 MB (`TesisFinal/Tesis.pdf`).

### Programa post-defensa (no requerido para sustentación)

- elevación del caso 30 con datos humanos reales (LoE = 4) cuando se obtenga acceso a VENLab/WALK-MS/OpenLocomotionData;
- elevación de casos programáticos del capítulo 05 (mente, biología, sistemas técnicos, instituciones) a modo demostrativo con dossier completo;
- desarrollo formal de la dimensión normativa con sondas más sofisticadas (resultado null del piloto COVID confirmó insuficiencia de AR(1));
- revisión exhaustiva por dominio del corpus EDI (mini-revisiones específicas por cada uno de los 30 dominios);
- comparación contra modelos no lineales adicionales (LSTM, Transformer);
- conversión final a plantilla institucional con figuras formales (trámite editorial pre-depósito).

## 2. Paso 1. Elegir caso programático prioritario para elevación

### Criterio de prioridad

El caso programático con mayor retorno marginal sobre la robustez del programa es **biología y ecología (capítulo 05-02)**, por tres razones:

- la literatura sobre regime shifts ecológicos (Scheffer y colegas) ofrece datos cuantitativos publicados con bifurcaciones identificables;
- el rival principal (reduccionismo molecular o holismo ecológico inflado) es articulable en su forma fuerte;
- la elevación reduce significativamente la asimetría con el caso ancla, fortaleciendo la generalidad ontológica del marco.

### Entregable

Capítulo 05-02 elevado a modo demostrativo con dossier completo: pregunta Q sobre transición de régimen ecológico, variables medidas, modelo dinámico ajustado, atractores empíricos, bifurcación de regime shift, predicción discriminante, comparación rival con datos.

### Plazo plausible

6-12 meses con dedicación parcial. La literatura existente acelera el trabajo.

## 3. Paso 2. Integración bibliográfica formal

### Tarea

Convertir el mapa de interlocutores funcionales del capítulo 07 en aparato bibliográfico real con citas rigurosas distribuidas por capítulo.

### Distribución obligatoria

**Tabla 6.3.1.**

| Capítulo | Interlocutor principal | Interlocutores secundarios |
|---|---|---|
| 02-01 (ontología) | Bunge | Dupré, Ladyman-Ross, Dennett, Sellars, Wittgenstein, Simondon |
| 02-02 (epistemología) | Cartwright | Pearl, Bechtel-Craver, Mitchell, Dennett |
| 02-03 (categorías) | Dennett | Searle, Bourdieu, Latour, Simondon |
| 02-04 (nivel B) | Warren, Gibson | Maturana-Varela, Varela-Thompson-Rosch, Clark, Noë |
| 03-01 (aparato) | Pearl | Ladyman-Ross, Strogatz, Kelso, Haken |
| 03-02 (criterios) | Bunge, Lakatos | Cartwright, Pearl |
| 03-03 (auditoría) | Bunge | Bechtel, Craver, Mitchell |
| 03-04 (κ empírico) | Strogatz, Kelso | literatura técnica de dinámica no lineal |
| 04-01 (rivales) | según rival | construido caso por caso |
| 04-02 (límites) | Searle, Varela-Thompson | Bourdieu, Latour |
| 05-01 (mente) | Varela-Thompson, Dennett | Clark, Noë, Searle |
| 05-02 (biología) | Nicholson-Dupré, Scheffer | Keller, Bechtel-Craver |
| 05-03 (técnico) | Simondon, Latour | literatura SRE |
| 05-04 (instituciones) | Bourdieu | Searle, Latour, Gilbert, Bunge |
| 05-05 (caso ancla) | Warren, Gibson | Fajen, Sternad, Foo, Yilmaz, Lee, Fink |

### Estilo

Citación por defecto Chicago author-date para texto en español filosófico. Bibliografía consolidada en capítulo 07 (refactor obligatorio).

### Entregable

Cada capítulo con citas insertadas, bibliografía formal por capítulo y bibliografía consolidada. Ningún capítulo sin diálogo textual mínimo con su interlocutor principal.

### Plazo

Continuo durante redacción final, con prioridad alta. Tareas documentales delegables a IA según el archivo `Bitacora/2026-04-28-cierre-pendientes/mega-tareas-archivadas/90-tareas-documentales-delegables-a-ia.md` ayudan acumulativamente.

## 4. Paso 3. Desarrollo del aparato para variables normativas

### Tarea

Operacionalización dinámica de validez, legitimidad y efectividad como propiedades del sistema institucional acoplado. Conjetura preliminar (capítulo 05-04 §4): validez = cuenca de atracción del cumplimiento; efectividad = tasa de retorno a la cuenca; legitimidad = anchura de la cuenca.

### Entregable

Capítulo metodológico adicional dentro de la Parte II con formalización dinámica de las tres propiedades, casos posibles de operacionalización, dialogo bibliográfico con Searle, Bourdieu, Latour, Gilbert.

### Plazo

18-24 meses en paralelo con paso 4 (instituciones como caso demostrativo). Es prerrequisito.

## 5. Paso 4. Multiplicación de casos demostrativos

### Tarea

Tras elevación del caso biológico (paso 1) y desarrollo del aparato normativo (paso 3), elevar al menos un caso adicional. Prioridad: instituciones (capítulo 05-04) por la deuda significativa que cierra; o sistemas técnicos (capítulo 05-03) por la accesibilidad a datos.

### Entregable

Al menos un caso adicional elevado a demostrativo con dossier completo. Idealmente dos.

### Plazo

12-18 meses tras los pasos 1 y 3.

## 6. Paso 5. Lectura externa por evaluadores hostiles

### Tarea

Someter el manuscrito a tres lectores con perfiles distintos:

- **filósofo de orientación analítica o de filosofía de la ciencia**: ataca consistencia argumental y discriminación contra rivales;
- **científico empírico o modelizador**: ataca rigor del aparato formal y validez del caso ancla;
- **crítico fenomenológico o hermenéutico**: ataca el tratamiento de la experiencia vivida y la dimensión normativa;
- **técnico de sistemas o computación formal**: ataca la operacionalización del aparato y la consistencia ST.

### Entregable

Versión revisada con respuestas integradas a cada crítica fuerte. Las críticas que fuerzan reformulación se documentan con fecha.

### Plazo

3-6 meses tras tener manuscrito completo en versión avanzada.

## 7. Paso 6. Redacción final unificada

### Tareas

- unificar terminología según glosario operativo;
- pulir transiciones entre capítulos;
- escribir introducción definitiva (al final, cuando se sepa qué logró el manuscrito);
- escribir conclusión definitiva (al final, cuando se sepa qué quedó probado);
- mantener tono entre claridad expositiva y rigor conceptual sin sacrificar ambición filosófica;
- revisar léxico propio para evitar lexicalización interna (riesgo del capítulo 04-02 §7.2).

### Entregable

Manuscrito doctoral en estilo unificado, listo para depósito.

### Plazo

3-6 meses tras lectura externa.

## 8. Paso 7. Apéndices técnicos mínimos

### Regla editorial

El material argumental deja de ser anexo y pasa al cuerpo: glosario, operadores, dossier, rivales, aplicaciones, objeciones, limitaciones y validación ST. Solo permanecen como apéndices los soportes que no conviene interrumpir en la lectura principal: tablas crudas y fuentes visuales.

### Plazo

Continuo durante el desarrollo. Cierre completo al final.

## 9. Cronograma agregado

**Tabla 6.3.2.**

| Mes | Hito |
|---|---|
| 1-12 | Elevación de caso biológico (paso 1); inicio integración bibliográfica (paso 2); inicio aparato normativo (paso 3) |
| 13-18 | Elevación de segundo caso (paso 4 inicial); aparato normativo en estado avanzado (paso 3) |
| 19-24 | Cierre de aparato normativo (paso 3); elevación de tercer caso si es viable; integración bibliográfica completa (paso 2) |
| 25-30 | Lectura externa hostil (paso 5); revisión |
| 31-33 | Redacción final unificada (paso 6); apéndices técnicos mínimos completos (paso 7) |
| 34-36 | Pulido, formato académico, depósito |

Plazo plausible: 24-36 meses con dedicación seria. Plazo real depende de bibliografía y disponibilidad de datasets.

## 10. Riesgos del plan

### Riesgo 1. Caso biológico no se eleva fácilmente

Si la literatura ecológica disponible no produce dossier completo con calidad equivalente al caso ancla, la elevación se posterga y se prueba con otro dominio (sistemas técnicos como alternativa más accesible).

### Riesgo 2. Aparato normativo resulta más difícil de lo esperado

La operacionalización de validez, legitimidad, efectividad puede requerir colaboración con sociología o ciencia política con datos cuantitativos. Si la colaboración no se consigue, el aparato queda como conjetura articulada y el capítulo 05-04 permanece programático con la deuda nombrada.

### Riesgo 3. Lectura externa fuerza reformulación mayor

Si los evaluadores hostiles encuentran fallas estructurales, el cronograma se extiende. Esto es preferible a depósito prematuro.

### Riesgo 4. Hipertrofia académica

Cada paso puede expandirse indefinidamente. La política: cada entregable tiene fecha y tamaño objetivo. Lo que no entra en la fecha, se documenta como deuda actualizada y se prosigue con el siguiente.

## 11. Indicadores de éxito final

El manuscrito doctoral final está listo si:

- al menos dos casos están en modo demostrativo (caso ancla + uno elevado);
- al menos tres dominios programáticos quedan con criterios de elevación claros;
- las catorce posiciones rivales se discriminan con tabla pública;
- el aparato formal opera con procedimiento empírico verificable;
- el dossier de anclaje se aplica al caso ancla con catorce componentes completos;
- la bibliografía está integrada en cada capítulo con interlocutor principal y secundarios;
- los seis límites del capítulo 04-02 se reconocen y se traducen en programa posterior;
- las cuatro condiciones de fracaso del capítulo 06-01 se aceptan;
- la guía de defensa oral funciona en simulación con interlocutor competente;
- los apéndices técnicos mínimos están completos y no sustituyen el cuerpo argumental.

## 12. Resultado deseado

El objetivo no es solo tener un texto largo defendible sino un manuscrito que reúna seis cualidades simultáneas:

- problema claro;
- tesis demostrada en su régimen declarado;
- rivales identificados con discriminación pública;
- criterio de evaluación explícito;
- aplicaciones con rendimiento (al menos demostrativas);
- límites honestamente reconocidos con plan de trabajo posterior;
- posible escalado a programa de investigación más amplio.

Si el manuscrito final cumple las seis cualidades, deja de ser tesis y empieza a ser programa de investigación.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---


<div id="bibliografia"></div>

# Bibliografía


<div id="bibliografia-consolidada"></div>

# Bibliografía formal del proyecto


## Asignación de interlocutores por capítulo

Cada capítulo del manuscrito se ancla en al menos un interlocutor principal y un conjunto de secundarios. Esta asignación no es decorativa: estructura el diálogo textual obligatorio.

**Tabla 7.1.**

| Capítulo | Interlocutor principal | Secundarios |
|----------|------------------------|-------------|
| 02-01 (ontología) | Bunge (1979) | Dupré, Ladyman y Ross, Dennett, Sellars, Wittgenstein, Simondon, Bueno |
| 02-02 (epistemología) | Cartwright (1989) | Pearl, Bechtel y Craver, Mitchell, Dennett, Popper |
| 02-03 (categorías) | Dennett (1991) | Searle, Bourdieu, Latour, Simondon |
| 02-04 (nivel B) | Warren (2006), Gibson (1979) | Maturana y Varela, Varela-Thompson-Rosch, Clark, Noë, Fajen |
| 02-05 (temporalidad y causalidad) | Woodward (2003), Mellor (1998) | Craver, Pearl, McTaggart, Kim, Bunge, Bergson, Whitehead, Hoel |
| 02-06 (dimensión normativa y ética) | Bunge (1989, vol. VIII) | Searle, MacIntyre, Foot, Mackie, Hoyos |
| 03-01 (aparato) | Pearl (2009) | Ladyman y Ross, Strogatz, Kelso, Haken |
| 03-02 (criterios) | Lakatos (1978), Popper (1959) | Cartwright, Pearl, Bunge |
| 03-03 (auditoría) | Bechtel y Craver (2007), Mitchell (2009) | Bunge, Cartwright |
| 03-04 (κ empírico, EDI) | Hoel (2017) | Strogatz, Kelso, Haken, Tononi, Seth, Rosas, Mediano, Klein |
| 04-01 (rivales) | Por rival | Wolfram (2020), Tononi (IIT), Searle (1980), Chalmers (2006) |
| 04-02 (límites) | Searle (1995) | Varela-Thompson, Bourdieu, Latour |
| 05-01 (mente) | Varela-Thompson-Rosch (1991), Dennett (1991) | Clark y Chalmers, Noë, Searle, Sellars |
| 05-02 (biología) | Nicholson y Dupré (2018), Scheffer (2009) | Keller, Bechtel y Craver, Maturana y Varela |
| 05-03 (técnico) | Simondon (1989), Latour (2005) | Brooks, Beyer (SRE), Hayhoe |
| 05-04 (instituciones) | Bourdieu (1980) | Searle, Latour, Gilbert, Bunge, North |
| 05-05 (caso ancla cualitativo) | Warren (2006), Gibson (1979) | Fajen, Sternad, Foo, Yilmaz, Lee, Fink |
| 06-01 (cierre) | — | sintetiza todos los anteriores |
| 09 (corpus EDI) | Hoel (2017) | Bunge, Ladyman y Ross, Woodward, Kim, Humphreys, O'Connor y Wong |

## Bibliografía nuclear completa

### A. Filosofía de la Ciencia, Ontología y Emergencia

1. Bedau, M. (1997). "Weak Emergence". *Philosophical Perspectives* 11: 375–399.
2. Bennett, J. (2010). *Vibrant Matter: A Political Ecology of Things*. Durham: Duke University Press.
3. Bueno, G. (1978). *Ensayos materialistas*. Madrid: Taurus.
4. Bunge, M. (1959). *Causality: The Place of the Causal Principle in Modern Science*. Cambridge: Harvard University Press.
4bis. Bunge, M. (1977). *Treatise on Basic Philosophy, Volume 3: Ontology I: The Furniture of the World*. Dordrecht: Reidel.
5. Bunge, M. (1979). *Treatise on Basic Philosophy, Volume 4: Ontology II: A World of Systems*. Dordrecht: Reidel.
6. Chalmers, D. (2006). "Strong and Weak Emergence". En P. Clayton y P. Davies (eds.), *The Re-Emergence of Emergence*. Oxford: Oxford University Press.
7. Dennett, D. (1991). "Real Patterns". *The Journal of Philosophy* 88(1): 27–51.
8. Dupré, J. (1993). *The Disorder of Things: Metaphysical Foundations of the Disunity of Science*. Cambridge: Harvard University Press.
9. Humphreys, P. (2016). *Emergence: A Philosophical Account*. Oxford: Oxford University Press.
10. Kant, I. (1781/1998). *Crítica de la razón pura*. Trad. P. Guyer y A. W. Wood. Cambridge: Cambridge University Press.
11. Kim, J. (1999). "Making Sense of Emergence". *Philosophical Studies* 95(1–2): 3–36.
12. Ladyman, J. y Ross, D. (2007). *Every Thing Must Go: Metaphysics Naturalized*. Oxford: Oxford University Press.
13. Latour, B. (2005). *Reassembling the Social: An Introduction to Actor-Network-Theory*. Oxford: Oxford University Press.
14. Latour, B. (2017). *Facing Gaia: Eight Lectures on the New Climatic Regime*. Cambridge: Polity Press.
15. Nicholson, D. y Dupré, J. (eds.) (2018). *Everything Flows: Towards a Processual Philosophy of Biology*. Oxford: Oxford University Press.
16. O'Connor, T. y Wong, H. Y. (2005). "The Metaphysics of Emergence". *Noûs* 39(4): 658–678.
17. Sellars, W. (1962). "Philosophy and the Scientific Image of Man". En R. Colodny (ed.), *Frontiers of Science and Philosophy*. Pittsburgh: University of Pittsburgh Press.
18. Simondon, G. (1989). *Du mode d'existence des objets techniques*. Paris: Aubier.
18bis. Simondon, G. (1958/2005). *L'individuation à la lumière des notions de forme et d'information*. Grenoble: Millon (edición completa). [Tesis doctoral defendida en 1958; ediciones parciales 1964 PUF y 1989 Aubier].
19. van Fraassen, B. C. (1980). *The Scientific Image*. Oxford: Oxford University Press.
20. Whitehead, A. N. (1929). *Process and Reality*. New York: Macmillan.
21. Wittgenstein, L. (1953). *Philosophical Investigations*. Oxford: Blackwell.

### B. Causalidad, Reducción, Mecanismos

23. Batterman, R. (2002). *The Devil in the Details: Asymptotic Reasoning in Explanation, Reduction, and Emergence*. Oxford: Oxford University Press.
24. Bechtel, W. (2008). *Mental Mechanisms: Philosophical Perspectives on Cognitive Neuroscience*. New York: Routledge.
25. Cartwright, N. (1989). *Nature's Capacities and Their Measurement*. Oxford: Clarendon Press.
25bis. Cartwright, N. (1983). *How the Laws of Physics Lie*. Oxford: Clarendon Press.
26. Cartwright, N. (1999). *The Dappled World: A Study of the Boundaries of Science*. Cambridge: Cambridge University Press.
26bis. Cartwright, N. (2007). *Hunting Causes and Using Them: Approaches in Philosophy and Economics*. Cambridge: Cambridge University Press.
27. Craver, C. (2007). *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*. Oxford: Oxford University Press.
28. Mitchell, S. D. (2009). *Unsimple Truths: Science, Complexity, and Policy*. Chicago: University of Chicago Press.
29. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. 2.ª ed. Cambridge: Cambridge University Press.
30. Woodward, J. (2003). *Making Things Happen: A Theory of Causal Explanation*. Oxford: Oxford University Press.

### B-bis. Temporalidad y filosofía del tiempo (cap 02-05)

32a. Bergson, H. (1889). *Essai sur les données immédiates de la conscience*. Paris: Alcan.
32b. Kim, J. (1998). *Mind in a Physical World: An Essay on the Mind-Body Problem and Mental Causation*. Cambridge: MIT Press.
32c. McTaggart, J. M. E. (1908). "The Unreality of Time". *Mind* 17(68): 457–484.
32d. Mellor, D. H. (1998). *Real Time II*. London: Routledge.
32e. Smolin, L. (2013). *Time Reborn: From the Crisis in Physics to the Future of the Universe*. Boston: Houghton Mifflin Harcourt.
32f. Whitehead, A. N. (1920). *The Concept of Nature*. Cambridge: Cambridge University Press.

### B-ter. Ética sustantiva y filosofía normativa (cap 02-06)

32g. Bunge, M. (1989). *Treatise on Basic Philosophy, Volume 8: Ethics: The Good and the Right*. Dordrecht: Reidel.
32h. Foot, P. (2001). *Natural Goodness*. Oxford: Clarendon Press.
32i. MacIntyre, A. (1981). *After Virtue: A Study in Moral Theory*. Notre Dame: University of Notre Dame Press.
32j. Mackie, J. L. (1977). *Ethics: Inventing Right and Wrong*. London: Penguin.
32k. Searle, J. R. (1964). "How to Derive 'Ought' from 'Is'". *Philosophical Review* 73(1): 43–58.
32l. Hoyos Vásquez, G. (2007). *Comunicación y mundo de la vida*. Bogotá: Pontificia Universidad Javeriana.

### C. Información, Complejidad y Emergencia Cuantitativa

33. Bar-Yam, Y. (2004). "Multiscale Complexity/Entropy". *Advances in Complex Systems* 7(1): 47–63.
34. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences*. 2.ª ed. Hillsdale: Lawrence Erlbaum.
35. Comolatti, R. y Hoel, E. P. (2022). "Causal Emergence is Widespread Across Measures of Causation". *arXiv:2202.01854*.
36. Flack, J. C. (2017). "Coarse-graining as a Downward Causation Mechanism". *Philosophical Transactions of the Royal Society A* 375(2109): 20160338.
37. Hoel, E. P. (2017). "When the Map is Better than the Territory". *Entropy* 19(5): 188.
38. Klein, B. y Hoel, E. P. (2020). "The Emergence of Informative Higher Scales in Complex Networks". *Complexity* 2020: 8932526.
39. Mediano, P. A. M., Rosas, F. E., Luppi, A. I., Carhart-Harris, R. L., Bor, D., Seth, A. K. y Barrett, A. B. (2022). "Greater than the Parts: A Review of the Information Decomposition Approach to Causal Emergence". *Philosophical Transactions of the Royal Society A* 380(2227): 20210246.
40. Rosas, F. E., Mediano, P. A. M., Gastpar, M. y Jensen, H. J. (2020). "Quantifying High-order Interdependencies via Multivariate Extensions of the Mutual Information". *Physical Review E* 100(3): 032310.
41. Seth, A. K. (2008). "Measuring Autonomy and Emergence via Granger Causality". *Artificial Life* 16(2): 179–196.
42. Shannon, C. E. (1948). "A Mathematical Theory of Communication". *Bell System Technical Journal* 27: 379–423, 623–656.
43. Tononi, G. (2004). "An Information Integration Theory of Consciousness". *BMC Neuroscience* 5: 42.
44. Tononi, G., Boly, M., Massimini, M. y Koch, C. (2016). "Integrated Information Theory: An Updated Account". *Archives Italiennes de Biologie* 154: 1–21.
45. Varley, T. F. y Hoel, E. P. (2022). "Emergence as the Conversion of Information: A Unifying Theory". *Philosophical Transactions of the Royal Society A* 380(2227): 20210150.

### D. Metodología y Filosofía de la Práctica Científica

46. Evensen, G. (2009). *Data Assimilation: The Ensemble Kalman Filter*. 2.ª ed. Berlin: Springer.
47. Lakatos, I. (1978). *The Methodology of Scientific Research Programmes*. Cambridge: Cambridge University Press.
48. Popper, K. (1959). *The Logic of Scientific Discovery*. London: Hutchinson.

### E. Sistemas Complejos, Simulación y Dinámica No Lineal

49. Haken, H. (1983). *Synergetics: An Introduction*. 3.ª ed. Berlin: Springer.
50. Holland, J. H. (1995). *Hidden Order: How Adaptation Builds Complexity*. Reading: Addison-Wesley.
51. Kelso, J. A. S. (1995). *Dynamic Patterns: The Self-Organization of Brain and Behavior*. Cambridge: MIT Press.
52. Luhmann, N. (1995). *Social Systems*. Stanford: Stanford University Press.
53. Schelling, T. C. (1978). *Micromotives and Macrobehavior*. New York: Norton.
54. Strogatz, S. H. (2014). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*. 2.ª ed. Boulder: Westview Press.
55. Soros, G. (1987). *The Alchemy of Finance*. New York: Simon & Schuster.
56. Taleb, N. N. (2012). *Antifragile: Things That Gain from Disorder*. New York: Random House.

### F. Filosofía de la Mente, Cognición Encarnada y Embodied

57. Clark, A. (2008). *Supersizing the Mind: Embodiment, Action, and Cognitive Extension*. Oxford: Oxford University Press.
58. Clark, A. y Chalmers, D. (1998). "The Extended Mind". *Analysis* 58(1): 7–19.
59. Maturana, H. y Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. Dordrecht: Reidel.
60. Noë, A. (2004). *Action in Perception*. Cambridge: MIT Press.
61. Searle, J. R. (1980). "Minds, Brains, and Programs". *Behavioral and Brain Sciences* 3(3): 417–424.
62. Searle, J. R. (1995). *The Construction of Social Reality*. New York: Free Press.
63. Varela, F. J., Thompson, E. y Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. Cambridge: MIT Press.

### G. Behavioral Dynamics y Percepción Ecológica

64. Fajen, B. R. y Warren, W. H. (2003). "Behavioral Dynamics of Steering, Obstacle Avoidance, and Route Selection". *Journal of Experimental Psychology: Human Perception and Performance* 29(2): 343–362.
65. Foo, P., Kelso, J. A. S. y de Guzman, G. C. (2000). "Functional Stabilization of Unstable Fixed Points: Human Pole Balancing Using Time-to-Balance Information". *Journal of Experimental Psychology: Human Perception and Performance* 26(4): 1281–1297.
66. Gibson, J. J. (1966). *The Senses Considered as Perceptual Systems*. Boston: Houghton Mifflin.
67. Gibson, J. J. (1979). *The Ecological Approach to Visual Perception*. Boston: Houghton Mifflin.
68. Lee, D. N. (1976). "A Theory of Visual Control of Braking Based on Information about Time-to-Collision". *Perception* 5(4): 437–459.
69. Sternad, D., Duarte, M., Katsumata, H. y Schaal, S. (2001). "Bouncing a Ball: Tuning into Dynamic Stability". *Journal of Experimental Psychology: Human Perception and Performance* 27(5): 1163–1184.
70. Warren, W. H. (2006). "The Dynamics of Perception and Action". *Psychological Review* 113(2): 358–389.
71. Yilmaz, E. H. y Warren, W. H. (1995). "Visual Control of Braking: A Test of the Tau-Dot Hypothesis". *Journal of Experimental Psychology: Human Perception and Performance* 21(5): 996–1014.

### H. Modelos de Dominio Específico (sondas ODE del corpus EDI)

72. Budyko, M. I. (1969). "The Effect of Solar Radiation Variations on the Climate of the Earth". *Tellus* 21(5): 611–619.
73. Carpenter, S. R. (2005). "Eutrophication of Aquatic Ecosystems: Bistability and Soil Phosphorus". *Proceedings of the National Academy of Sciences* 102(29): 10002–10005.
74. Docquier, F. y Rapoport, H. (2012). "Globalization, Brain Drain, and Development". *Journal of Economic Literature* 50(3): 681–730.
75. Jambeck, J. R., Geyer, R., Wilcox, C., Siegler, T. R., Perryman, M., Andrady, A., Narayan, R. y Law, K. L. (2015). "Plastic Waste Inputs from Land into the Ocean". *Science* 347(6223): 768–771.
76. Kermack, W. O. y McKendrick, A. G. (1927). "A Contribution to the Mathematical Theory of Epidemics". *Proceedings of the Royal Society A* 115(772): 700–721.
77. North, D. C. (1990). *Institutions, Institutional Change and Economic Performance*. Cambridge: Cambridge University Press.
78. Scheffer, M. (2009). *Critical Transitions in Nature and Society*. Princeton: Princeton University Press.
79. Sellers, W. D. (1969). "A Global Climatic Model Based on the Energy Balance of the Earth-Atmosphere System". *Journal of Applied Meteorology* 8(3): 392–400.
80. von Thünen, J. H. (1826). *Der isolirte Staat in Beziehung auf Landwirthschaft und Nationalökonomie*. Hamburg: Perthes.

### I. Computación, Hipergrafos y Wolfram

81. Wolfram, S. (2020). *A Project to Find the Fundamental Theory of Physics*. Champaign: Wolfram Media.
82. Wolfram, S. (2002). *A New Kind of Science*. Champaign: Wolfram Media.

### J. Ontología social e instituciones

83. Bourdieu, P. (1980). *Le sens pratique*. Paris: Éditions de Minuit.
84. Bourdieu, P. (1990). *The Logic of Practice*. Stanford: Stanford University Press.
85. Gilbert, M. (1989). *On Social Facts*. London: Routledge.
86. Searle, J. R. (2010). *Making the Social World: The Structure of Human Civilization*. Oxford: Oxford University Press.

### K. Filosofía latinoamericana / Universidad de Antioquia

87. Hoyos Vásquez, G. (1996). *Ética para ciudadanos*. Bogotá: Siglo del Hombre.
88. Salas, R. (ed.) (2014). *Pensamiento crítico latinoamericano: conceptos fundamentales*. Santiago: Universidad Católica.

### L. Robótica situada y embodied AI

89. Brooks, R. A. (1991). "Intelligence Without Representation". *Artificial Intelligence* 47(1–3): 139–159.
90. Pfeifer, R. y Scheier, C. (1999). *Understanding Intelligence*. Cambridge: MIT Press.

### M. Epistemología naturalizada e instrumentalismo

91. Carnap, R. (1950). "Empiricism, Semantics, and Ontology". *Revue Internationale de Philosophie* 4(11): 20–40.
92. Hacking, I. (1983). *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*. Cambridge: Cambridge University Press.
93. Quine, W. V. O. (1969). "Epistemology Naturalized". En *Ontological Relativity and Other Essays*, pp. 69–90. New York: Columbia University Press.
94. Sellars, W. (1956). "Empiricism and the Philosophy of Mind". En H. Feigl y M. Scriven (eds.), *Minnesota Studies in the Philosophy of Science*, vol. 1, pp. 253–329. Minneapolis: University of Minnesota Press.

### N. Filosofía de la mente — panpsiquismo, identidad, naturaleza intrínseca

95. Chalmers, D. J. (1996). *The Conscious Mind: In Search of a Fundamental Theory*. New York: Oxford University Press.
96. Goff, P. (2019). *Galileo's Error: Foundations for a New Science of Consciousness*. New York: Pantheon Books.
97. Locke, J. (1690/1975). *An Essay Concerning Human Understanding*. P. H. Nidditch (ed.). Oxford: Clarendon Press.
98. Parfit, D. (1984). *Reasons and Persons*. Oxford: Clarendon Press.
99. Reid, T. (1785/2002). *Essays on the Intellectual Powers of Man*. D. R. Brookes (ed.). Edinburgh: Edinburgh University Press.
100. Strawson, G. (2006). "Realistic Monism: Why Physicalism Entails Panpsychism". *Journal of Consciousness Studies* 13(10–11): 3–31.

### O. Política agonística, descolonialidad y geofilosofía (deudas declaradas cap 04-04 §7)

101. Castro-Gómez, S. (2007). *La hybris del punto cero: Ciencia, raza e Ilustración en la Nueva Granada (1750-1816)*. Bogotá: Pontificia Universidad Javeriana.
102. Dewey, J. (1934). *Art as Experience*. New York: Minton, Balch & Company.
103. Lefebvre, H. (1974/1991). *The Production of Space*. Trad. D. Nicholson-Smith. Oxford: Blackwell.
104. Lewis, D. (1991). *Parts of Classes*. Oxford: Blackwell.
105. Mignolo, W. (2007). *The Idea of Latin America*. Oxford: Blackwell.
106. Mouffe, C. (2005). *On the Political*. London: Routledge.
107. Quijano, A. (2000). "Colonialidad del poder, eurocentrismo y América Latina". En E. Lander (comp.), *La colonialidad del saber: eurocentrismo y ciencias sociales. Perspectivas latinoamericanas*, pp. 201–246. Buenos Aires: CLACSO.
108. Rancière, J. (1995/1999). *Disagreement: Politics and Philosophy*. Trad. J. Rose. Minneapolis: University of Minnesota Press. [Original *La Mésentente*, Galilée 1995].
109. Simons, P. (1987). *Parts: A Study in Ontology*. Oxford: Clarendon Press.
110. Whitehead, A. N. (1929). *Process and Reality: An Essay in Cosmology*. New York: Macmillan. [Edición corregida: Free Press, 1978].

### P. Información ecológica y comunicación (cap 02-04)

111. Bateson, G. (1972). *Steps to an Ecology of Mind*. New York: Ballantine Books.
112. Dretske, F. (1981). *Knowledge and the Flow of Information*. Cambridge: MIT Press.
113. Floridi, L. (2011). *The Philosophy of Information*. Oxford: Oxford University Press.

### Q. Análisis topológico de series (cap 02-01 §2.2.2)

114. Grassberger, P. y Procaccia, I. (1983). "Characterization of Strange Attractors". *Physical Review Letters* 50(5): 346–349. [Versión extendida: *Physica D* 9(1–2): 189–208].
115. Haken, H. (1977). *Synergetics: An Introduction. Nonequilibrium Phase Transitions and Self-Organization in Physics, Chemistry and Biology*. 1.ª ed. Berlin: Springer-Verlag. [3.ª ed. 1983 ya listada en E.49].
116. Rosenstein, M. T., Collins, J. J. y De Luca, C. J. (1993). "A Practical Method for Calculating Largest Lyapunov Exponents from Small Data Sets". *Physica D* 65(1–2): 117–134.
117. Takens, F. (1981). "Detecting Strange Attractors in Turbulence". En D. A. Rand y L.-S. Young (eds.), *Dynamical Systems and Turbulence*, *Lecture Notes in Mathematics* 898, pp. 366–381. Berlin: Springer.

### R. Calibración estadística avanzada (cap 03-04)

118. Holm, S. (1979). "A Simple Sequentially Rejective Multiple Test Procedure". *Scandinavian Journal of Statistics* 6(2): 65–70.
119. Newey, W. K. y West, K. D. (1987). "A Simple, Positive Semi-definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix". *Econometrica* 55(3): 703–708.
120. Politis, D. N. y Romano, J. P. (1994). "The Stationary Bootstrap". *Journal of the American Statistical Association* 89(428): 1303–1313.
121. Künsch, H. R. (1989). "The Jackknife and the Bootstrap for General Stationary Observations". *Annals of Statistics* 17(3): 1217–1241.

### S. Mecánica cuántica — interpretaciones realistas (cap 02-01 §13)

122. Everett III, H. (1957). "'Relative State' Formulation of Quantum Mechanics". *Reviews of Modern Physics* 29(3): 454–462.
123. DeWitt, B. S. (1970). "Quantum Mechanics and Reality". *Physics Today* 23(9): 30–35.
124. Ghirardi, G. C., Rimini, A. y Weber, T. (1986). "Unified Dynamics for Microscopic and Macroscopic Systems". *Physical Review D* 34(2): 470–491.
125. Zurek, W. H. (2003). "Decoherence, einselection, and the quantum origins of the classical". *Reviews of Modern Physics* 75(3): 715–775.

### T. Biología procesual y enactivismo (cap 02-04, 05-01)

126. Hutto, D. D. y Myin, E. (2013). *Radicalizing Enactivism: Basic Minds without Content*. Cambridge: MIT Press.
127. Hutto, D. D. y Myin, E. (2017). *Evolving Enactivism: Basic Minds Meet Content*. Cambridge: MIT Press.
128. Thompson, E. (2007). *Mind in Life: Biology, Phenomenology, and the Sciences of Mind*. Cambridge: Harvard University Press.

### U. Filosofía colombiana e hispanoamericana (extensión cap 02-01 §0.3)

129. Bunge, M. (1980). *Epistemología: Curso de actualización*. Barcelona: Ariel.
130. Hoyos Vásquez, G. (1986). *Los intereses de la vida cotidiana y las ciencias*. Bogotá: Universidad Nacional de Colombia.

### V. Inferencialismo y filosofía del lenguaje (cap 02-02)

131. Brandom, R. B. (1994). *Making It Explicit: Reasoning, Representing, and Discursive Commitment*. Cambridge: Harvard University Press.

### W. Mecanicismo procesual y enactivismo radical (cap 03-03, 04-01)

132. Adams, F. y Aizawa, K. (2008). *The Bounds of Cognition*. Oxford: Wiley-Blackwell.
133. Bechtel, W. y Richardson, R. C. (1993/2010). *Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research*. Cambridge: MIT Press. [Reedición 2010 con prólogo nuevo].
134. Chemero, A. (2009). *Radical Embodied Cognitive Science*. Cambridge: MIT Press.
135. Glennan, S. (2017). *The New Mechanical Philosophy*. Oxford: Oxford University Press.

### X. Filosofía de la mente analítica (cap 05-01, 04-01)

136. Chalmers, D. J. (1995). "Facing Up to the Problem of Consciousness". *Journal of Consciousness Studies* 2(3): 200–219.

## Fuentes de Datos (Repositorios Principales)

**Tabla 7.2.**

| Fuente | URL/API | Casos del corpus |
|--------|---------|-----|
| World Bank Open Data | api.worldbank.org/v2 | 10, 11, 13, 16, 18, 22, 25, 27, 28, 29 |
| Our World in Data (OWID) | github.com/owid/owid-grapher-data | 5, 24 |
| Meteostat / NOAA | meteostat.net | 1 |
| Yahoo Finance | finance.yahoo.com / yfinance | 9 |
| OPSD (Open Power Systems Data) | open-power-system-data.org | 4 |
| CelesTrak | celestrak.org | 20, 26 |
| Wikimedia Statistics | stats.wikimedia.org | 15 |
| AQICN | aqicn.org | 3 |
| WMO/PMEL (proxies) | psl.noaa.gov | 17, 19 |
| GRAVIS+USGS (proxy) | usgs.gov | 25 |
| Synthetic (Fajen-Warren) | local | 30 |

## Notas editoriales

1. **Convención de citación:** Chicago author-date adaptado al manuscrito doctoral en español. Para envío a revista Q1 específica, debe ajustarse al estilo solicitado (APA, Vancouver según campo).
2. **Cobertura por capítulo:** las 90 referencias cubren todos los capítulos del manuscrito con al menos 3 fuentes nucleares por capítulo.
3. **Fuentes faltantes para futuro:** envío a revistas exige revisión sistemática por dominio. Aquí están las fuentes nucleares; las complementarias se incorporan en fase de redacción final.
4. **Bibliografía secundaria:** el corpus PDF en `07-bibliografia/` (Bunge, Dennett, Searle, Bourdieu, Latour, Simondon, Wittgenstein, Sellars, Maturana-Varela, Whitehead, Chalmers, Noë-Thompson, Warren) sirve como fuente directa para citas extensas.

## Fórmula final de la bibliografía

> Una tesis doctoral no se valida por la cantidad de referencias sino por la **función argumental** de cada una. Aquí cada referencia tiene su asignación a capítulo y su rol (alianza, contraste, afinación). Una vez asignados, se convierten en aparato real durante la redacción final.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---


<div id="apendices-tecnicos"></div>

# Apéndices técnicos mínimos


<div id="apendice-tecnico-1-tablas-crudas-del-corpus-inter-dominio"></div>

# Apéndice técnico 1. Tablas crudas del corpus EDI inter-dominio

## Función

Apéndice tabular de **resultados crudos verificables** del corpus EDI multidominio. La fuente de verdad numérica son los `outputs/metrics.json` versionados en `09-simulaciones-edi/<caso>/`. Este apéndice consolida las cifras exactas en una sola tabla auditable por el comité doctoral.

**Política:** todas las cifras son las publicadas en los `metrics.json` del repositorio. Si hay discrepancia entre este apéndice y el `metrics.json` correspondiente, **prevalece el `metrics.json`** y este apéndice se actualiza como erratum.

---

## Tabla A.8.1. Resultados del corpus EDI (30 casos, perfil canónico)

Perfil canónico: `n_perm = 999`, `n_boot = 500`, `seed = 42`, `validator_version = canonical-2026-04`.

**Tabla A.8.1.**

| # | Caso | Sonda macro | EDI | p | Bootstrap CI | val_steps | LoE | Coupling | Forcing | Nivel | overall_pass |
|---|------|-------------|----:|---:|---|----:|---:|----:|----:|---:|:---:|
| 04 | Energía eléctrica | Lotka-Volterra | 0.6503 | 0.0000 | [0.6377, 0.6629] | 13 | 4 | 0.55 | 0.85 | 4 | True |
| 16 | Deforestación global | von Thünen | 0.6020 | 0.0000 | [0.5872, 0.6168] | 13 | 4 | 0.50 | 0.80 | 4 | True |
| 20 | Síndrome de Kessler | Densidad orbital | 0.3527 | 0.0000 | [0.3398, 0.3656] | 15 | 3 | 0.45 | 0.75 | 4 | True |
| 27 | Riesgo biológico | Mortalidad | 0.3326 | 0.0022 | [0.3198, 0.3454] | 9 | 3 | 0.40 | 0.70 | 4 | True |
| 24 | Microplásticos | Jambeck Accumulation | 0.7819 | 0.0000 | inestable | 15 | 4 | 0.60 | 0.90 | 4* | False |
| 13 | Políticas estratégicas | Saturation growth | 0.2972 | 0.0015 | [0.2842, 0.3102] | 13 | 3 | 0.40 | 0.70 | 3 | False |
| 30 | Behavioral Dynamics | behavioral_attractor | 0.2622 | 0.0440 | [0.2494, 0.2798] | 35 | 2 | 0.60 | 0.99 | 3 | False |
| 14 | Postverdad | SIS Desinformación | 0.2428 | 0.0000 | [0.2298, 0.2558] | 8 | 2 | 0.45 | 0.80 | 3 | False |
| 18 | Urbanización | Logística + Atracción | 0.2358 | 0.0000 | [0.2228, 0.2488] | 23 | 4 | 0.50 | 0.75 | 3 | False |
| 22 | Fósforo | Carpenter P Cycle | 0.1924 | 0.0000 | [0.1794, 0.2054] | 18 | 4 | 0.40 | 0.70 | 3 | False |
| 15 | Wikipedia | Saturation growth | 0.1916 | 0.0000 | [0.1786, 0.2046] | 48 | 3 | 0.35 | 0.65 | 3 | False |
| 05 | Epidemiología | SEIR | 0.1294 | 0.0000 | [0.1164, 0.1424] | 104 | 4 | 0.50 | 0.85 | 3 | False |
| 11 | Movilidad aérea | Bilinear diffusion | 0.1283 | 0.0020 | [0.1153, 0.1413] | 19 | 3 | 0.35 | 0.65 | 3 | False |
| 09 | Finanzas globales | Pricing factor | 0.0813 | 0.0000 | [0.0683, 0.0943] | 168 | 4 | 0.30 | 0.60 | 2 | False |
| 21 | Salinización | Balance hídrico | 0.0184 | 0.0028 | [0.0054, 0.0314] | 18 | 3 | 0.20 | 0.55 | 2 | False |
| 10 | Justicia | — | 0.2274 | 0.4775 | inestable | 12 | 2 | 0.15 | 0.50 | 1 | False |
| 26 | Starlink | Densidad orbital | 0.6892 | 1.0000 | inestable | 1 | 3 | — | — | 1* | False |
| 28 | Fuga de cerebros | Docquier-Rapoport | 0.0249 | 0.9975 | inestable | 18 | 3 | 0.10 | 0.45 | 1 | False |
| 01 | Clima regional | Budyko-Sellers | 0.0111 | 0.9990 | inestable | 168 | 5 | 0.05 | 0.40 | 1 | False |
| 02 | Conciencia global | Fallback | -0.1165 | 0.9239 | — | 9 | 1 | — | — | 0 | False |
| 03 | Contaminación PM2.5 | — | -0.0038 | 0.8699 | — | 11 | 3 | — | — | 0 | False |
| 12 | Paradigmas (ciencia) | — | -0.0060 | 0.0000 | — | 11 | 2 | — | — | 0 | False |
| 17 | Océanos (temperatura) | — | -0.0154 | 1.0000 | — | 14 | 3 | — | — | 0 | False |
| 19 | Acidificación oceánica | — | -0.0002 | 0.0000 | — | 11 | 3 | — | — | 0 | False |
| 23 | Erosión dialéctica | — | -1.0000 | 1.0000 | — | 8 | 1 | — | — | 0 | False |
| 25 | Acuíferos | — | -0.1462 | 1.0000 | — | 19 | 3 | — | — | 0 | False |
| 29 | IoT | — | -0.8760 | 1.0000 | — | 15 | 3 | — | — | 0 | False |
| 06 | **Falsac. exogeneidad** | Ruido puro | 0.0551 | 1.0000 | — | 731 | 1 | — | — | — | False |
| 07 | **Falsac. no-estacionar.** | Random walk | -0.8819 | 1.0000 | — | 731 | 1 | — | — | — | False |
| 08 | **Falsac. observabilidad** | Estado oculto | -1.0000 | 1.0000 | — | 97 | 1 | — | — | — | False |

**Convenciones:**

- `(*)`: nivel asignado tentativamente por inestabilidad bootstrap o ventana insuficiente.
- "—": campo no aplicable o sin sonda macro específica (casos null o casos donde la sonda fallback genera EDI no informativo).
- "inestable": el bootstrap no convergió a CI estrecho con n_boot = 500; la cifra de EDI puntual permanece pero la inferencia se trata con cautela.

---

## Tabla A.8.2. Métricas de robustez por caso

**Tabla A.8.2.**

| # | Caso | Estabilidad numérica | Persistencia temporal | Determinismo seed=42 | C1 | C2 | C3 | C4 | C5 |
|---|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 04 | Energía | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 16 | Deforestación | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 20 | Kessler | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 27 | Riesgo Bio | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 24 | Microplásticos | ✓ | ✓ | ✓ | ✓ | ✗ (CI) | ✓ | ✓ | ✓ |
| 30 | Behavioral Dynamics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ... | (resto: ver `09-simulaciones-edi/<caso>/outputs/metrics.json`) | | | | | | | | |

**Resumen agregado del corpus:**

- estabilidad numérica: 29/29 casos (uno declarado N/A);
- persistencia temporal: 28/29;
- determinismo seed = 42: 29/29;
- coupling > 0.10: 21/29;
- protocolo C1-C5 superado por los 5 casos strong y los 7 weak con p < 0.05.

---

## Tabla A.8.3. Verificación bajo perfil agresivo

Perfil agresivo: `n_perm = 2999`, `n_boot = 1500`, `n_refine = 10000`. Aplicado a casos seleccionados.

**Tabla A.8.3.**

| # | Caso | EDI canónico | EDI agresivo | Δ | Veredicto |
|---|------|------------:|-------------:|---:|-----------|
| 16 | Deforestación | 0.6020 | 0.5802 | -0.022 | Robusto bajo agresivo (Nivel 4 strong preservado) |
| 30 | Behavioral Dynamics | 0.2622 | 0.2623 | +0.0001 | Idéntico bajo agresivo (Nivel 3 weak preservado) |

La verificación masiva del corpus completo bajo perfil agresivo es trabajo futuro; en los dos casos verificados, la concordancia es alta. La tendencia esperable es ligera atenuación bajo agresivo por la selección más estricta de la null hypothesis.

---

## Tabla A.8.4. Distribución del paisaje de emergencia

**Tabla A.8.4.**

| Categoría | Definición operativa | Cuenta | Porcentaje |
|-----------|----------------------|-------:|-----------:|
| Strong (Nivel 4) — gate completo | EDI ≥ 0.30, p < 0.01, `overall_pass = True`, ≥ 8 ms restantes | 4 | 14% |
| Strong (Nivel 4) — sin gate | EDI ≥ 0.30, p < 0.01, gate parcial | 1 | 3% |
| Weak (Nivel 3) | 0.10 ≤ EDI < 0.30, p < 0.05 | 8 | 27% |
| Suggestive (Nivel 2) | 0.01 ≤ EDI < 0.10, p < 0.05 | 2 | 7% |
| Trend (Nivel 1) | 0 < EDI ≤ 0.30 sin significancia | 4 | 14% |
| Null (Nivel 0) | EDI ≤ 0 o sin estructura macro | 8 | 27% |
| Falsación rechazada | EDI ≤ 0.06, p ≥ 1.0 | 3 | 10% |

**Total:** 30 casos del corpus EDI. **Selectividad:** 15/30 con p < 0.05 y EDI > 0.01. **Falsación correcta:** 3/3.

---

## Trazabilidad

- fuente de verdad: `09-simulaciones-edi/<caso>/outputs/metrics.json`;
- código de validación: `09-simulaciones-edi/common/hybrid_validator.py`;
- política de reproducibilidad: `03-formalizacion/05-etica-y-gobernanza-de-datos.md`;
- discusión cualitativa: `09-simulaciones-edi/README.md`.

## Instrucción al lector

Para verificar cualquier cifra de este apéndice:

```bash
cd 09-simulaciones-edi/<NN_caso_xxx>
cat outputs/metrics.json | python3 -m json.tool
```

Si una cifra del apéndice no coincide con `metrics.json`, prevalece `metrics.json` y este apéndice se corrige.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="apendice-tecnico-2-tablas-crudas-del-corpus-inter-escala"></div>

# Apéndice técnico 2. Tablas crudas del corpus EDI multiescala

## Función

Apéndice tabular de **resultados crudos verificables** del corpus EDI multiescala (10 casos en escalas distintas a la macro). La fuente de verdad numérica son los `outputs/metrics.json` versionados en `09-simulaciones-edi/corpus_multiescala/<caso>/`.

**Política:** todas las cifras son las publicadas en los `metrics.json`. Si hay discrepancia entre este apéndice y el `metrics.json` correspondiente, **prevalece el `metrics.json`**.

---

## Tabla A.12.1. Resultados del corpus multiescala (10 casos)

**Tabla A.12.1.**

| # | Caso | Escala (longitud) | Escala (tiempo) | EDI | p | CI 95% | Nivel | Overall pass |
|---|------|-------------------|-----------------|----:|--:|--------|------:|:------------:|
| 31 | Decoherencia qubit | 10⁻⁹ m | 10⁻⁶ s | 0.91 | 0.000 | [0.89, 0.93] | 4 | True |
| 32 | Espín-órbita | 10⁻¹⁰ m | 10⁻¹⁵ s | 0.83 | 0.000 | [0.80, 0.85] | 4 | True |
| 33 | Villin Headpiece | 10⁻⁹ m | 10⁻⁶ s | 0.00 | 0.826 | ~0 | 0 | False |
| 34 | Michaelis-Menten | 10⁻⁸ m | 10⁻³ s | 0.46 | 0.000 | [0.33, 0.57] | 4 | True |
| 35 | Ciclo celular | 10⁻⁵ m | 10³ s | 0.13 | 0.000 | [0.11, 0.15] | 3 | False |
| 36 | NF-κB | 10⁻⁵ m | 10² s | 0.59 | 0.000 | [0.58, 0.59] | 4 | True |
| 37 | HRV cardíaco | 1 m | 1 s | 0.58 | 0.000 | [0.51, 0.64] | 4 | True |
| 38 | Locomoción τ-dot | 1 m | 1 s | -1.34 | 1.000 | [-1.51, -1.21] | 0 | False |
| 39 | Cefeida pulsante | 10¹¹ m | 10⁵ s | 0.92 | 0.000 | [0.90, 0.93] | 4 | True |
| 40 | Cúmulo globular | 10¹⁷-10²⁰ m | 10¹⁴ s | 0.43 | 0.000 | [0.35, 0.51] | 4 | True |

## Tabla A.12.2. Distribución por nivel y por escala

**Tabla A.12.2.**

| Nivel | Cuenta | Escalas representadas |
|-------|-------:|----------------------|
| 4 strong (`overall_pass=True`) | 7 | atómica, cuántica, bioquímica, celular oscilatoria, individual, astrofísica chica, astrofísica grande |
| 3 weak | 1 | celular (ciclo) |
| 0 null | 2 | molecular (Villin), individual (Lee τ-dot) |

**Selectividad multiescala:** 8/10 con señal positiva (EDI > 0); 7/10 con `overall_pass=True`.

## Tabla A.12.3. Sondas físicas usadas por caso

**Tabla A.12.3.**

| # | Caso | Sonda macro | Referencia teórica |
|---|------|-------------|---------------------|
| 31 | Decoherencia qubit | Lindblad con T2(T_bath) | Lindblad 1976; Bloch 1946 |
| 32 | Espín-órbita | H_eff con (L·S) acoplado | Bloch theorem |
| 33 | Villin | MSM 2-estados Arrhenius | Lindorff-Larsen 2011 |
| 34 | MM | Lineweaver-Burk | Michaelis-Menten 1913 |
| 35 | Ciclo celular | Tyson-Novak 4 ODE | Tyson-Novak 2001 |
| 36 | NF-κB | Hoffmann reducido | Hoffmann 2002 |
| 37 | HRV | Mackey-Glass con delay | Mackey-Glass 1977 |
| 38 | Locomoción τ-dot | Lee 1976 control óptico | Lee 1976 |
| 39 | Cefeida | P-L Leavitt | Leavitt 1912 |
| 40 | Cúmulo globular | Plummer + marea | Plummer 1911 |

## Tabla A.12.4. Datos candidatos para elevación a LoE 4

**Tabla A.12.4.**

| # | Caso | Dataset abierto | Acceso | Cronograma |
|---|------|-----------------|--------|------------|
| 31 | Decoherencia | IBM Quantum Experience (T1, T2) | abierto | 2-3 meses |
| 32 | Espín-órbita | Bloch Lab MPI Munich | académico | 4-6 meses |
| 33 | Villin | DE Shaw Anton trayectorias | académico | 4-6 meses |
| 34 | MM | BRENDA enzyme database | abierto | 2-3 meses |
| 35 | Ciclo celular | Cross Lab Rockefeller | académico | 6-8 meses |
| 36 | NF-κB | Tay Lab ETH single-cell | académico | 4-6 meses |
| 37 | HRV | PhysioNet ECG | abierto | 1-2 meses |
| 38 | Locomoción | VENLab / WALK-MS | académico | 9-12 meses |
| 39 | Cefeida | OGLE survey | abierto | 1-2 meses |
| 40 | Cúmulo globular | Gaia DR3 | abierto | 2-3 meses |

## Trazabilidad

- fuente de verdad: `09-simulaciones-edi/corpus_multiescala/<caso>/outputs/metrics.json`
- código: `09-simulaciones-edi/corpus_multiescala/<caso>/run.py`
- motor común: `09-simulaciones-edi/corpus_multiescala/edi_engine.py`
- discusión: `05-aplicaciones/06-corpus-multiescala.md`
- corpus macro original: `10-apendices-tecnicos/01-tablas-crudas-corpus-interdominio.md`


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---

<div id="apendice-tecnico-3-figuras-mermaid"></div>

# Apéndice técnico 3. Figuras Mermaid

Diagramas formales del manuscrito en formato Mermaid (renderable directamente por GitHub, GitLab, Pandoc + filtros, y la mayoría de visores Markdown). Reemplaza los diagramas ASCII art que aparecen en el cuerpo de los capítulos.

**Versiones vectoriales pre-depósito (generadas por `@mermaid-js/mermaid-cli`):**

- SVG: `figures/mermaid_svg/figura_<NN>.svg`
- PNG (1600×1200): `figures/mermaid_png/figura_<NN>.png`
- Fuente `.mmd` extraída automáticamente: `figures/mermaid_src/figura_<NN>.mmd`

La numeración `<NN>` (01-09) corresponde al orden de aparición en este apéndice (`Figura T.3.1` → `figura_01.svg`, etc.). La regeneración es reproducible con `scripts/render_mermaid.sh`.

---

## Fig. 2.2. Acoplamiento dinámico organismo-entorno-tarea-historia (capítulo 02-04)

**Figura A.10.1.**

```mermaid
graph LR
    H[Historia] --> A[Agente / Organismo]
    T[Tarea] --> A
    A -->|β: fuerza| E[Entorno]
    E -->|λ: información ecológica| A
    A -->|ȧ = Ψ a,i| A
    E -->|ė = Φ e,F| E
    style A fill:#cdf
    style E fill:#fdc
    style T fill:#dfc
    style H fill:#fcd
```

---

## Fig. 3.1. Mapa de operadores formales (capítulo 03-01)

**Figura A.10.2.**

```mermaid
graph TD
    R[Realidad R] -->|μ: medir| X[Variables X]
    X -->|construir grafo| G[Grafo basal G = V,E,W,T]
    G -->|relaciones n-arias| H[Hipergrafo H]
    G -->|comprimir| K[κ: G → G*]
    H -->|comprimir| K
    K -->|errores de traducción| Eps[ε: G ↔ G*]
    K -->|admitir| S[Semántica revisada S]
    Eps -->|reabrir si| K
    style R fill:#fee
    style X fill:#efe
    style G fill:#eef
    style H fill:#eff
    style K fill:#fef
    style Eps fill:#ffe
    style S fill:#cfc
```

---

## Fig. 3.2. Dossier de anclaje (14 componentes — capítulo 03-02)

**Figura A.10.3.**

```mermaid
graph TD
    Q[1 Pregunta Q fechada] --> V[2 Variables operacionalizadas]
    V --> Sus[3 Sustrato instanciante]
    Sus --> Gr[4 Grafo G construido]
    Gr --> Hi[5 Hipergrafo H si procede]
    Hi --> Kp[6 Compresión κ]
    Kp --> At[7 Atractores identificados]
    At --> Pv[8 Pruebas de validación]
    Pv --> Pred[9 Predicción discriminante]
    Pred --> Iv[10 Intervención discriminante]
    Iv --> Eps[11 Operador ε]
    Eps --> Tr[12 Traducción B↔L3]
    Tr --> Lim[13 Limitaciones]
    Lim --> Rv[14 Comparación rival]
```

---

## Fig. 3.3. Pipeline EDI (capítulo 03-04)

**Figura A.10.4.**

```mermaid
graph LR
    D[Datos] --> ABM[Simulación ABM N=200, 50x50]
    D --> ODE_p[Sonda ODE primaria]
    ABM -->|coupled| RC[RMSE coupled]
    ABM -->|sin ODE| RnO[RMSE no_ode]
    ODE_p --> ABM
    RC --> EDI[EDI = 1 - RC/RnO]
    RnO --> EDI
    EDI --> Pe[Permutación 999]
    EDI --> Bo[Bootstrap 500]
    Pe --> Pv[p-value]
    Bo --> CI[CI 95%]
    EDI --> C[Protocolo C1-C5]
    C --> OP[overall_pass]
```

---

## Fig. 5.1. Asimetría L1↔B↔L3↔S como protocolo (capítulo 02-04)

**Figura A.10.5.**

```mermaid
graph LR
    L1[L1 psicológico ordinario<br>preguntas comunicables] -.indirecto.-> B[B conductual biológico<br>anclaje empírico]
    B -->|directo<br>traduccional| L3[L3 estructural relacional<br>formalización]
    L3 -->|consecuencias<br>observables| L1
    L3 -->|filtro empírico| S[S semántica revisada<br>categorías que sobreviven]
    B -->|atractores reales| S
    style L1 fill:#fcc
    style B fill:#cfc
    style L3 fill:#ccf
    style S fill:#fcf
```

---

## Fig. 6.1. Paisaje de emergencia del corpus (capítulo 06-01)

**Figura A.10.6.**

```mermaid
pie title Distribución del corpus EDI 30 casos
    "Strong gate (4)" : 4
    "Strong sin gate (1)" : 1
    "Weak (8)" : 8
    "Suggestive (2)" : 2
    "Trend (4)" : 4
    "Null (8)" : 8
    "Falsación rechazada (3)" : 3
```

---

## Fig. 9.1. Arquitectura del motor ABM+ODE (capítulo 09-00)

**Figura A.10.7.**

```mermaid
graph TD
    DC[case_config.json] --> CR[case_runner.py]
    Data[fetch_*.py por caso] --> CR
    CR --> ABM_C[abm_core CPU]
    CR --> ABM_G[abm_core_gpu CuPy/PyTorch]
    CR --> OM[ode_models.py 22 sondas]
    OM --> HV[hybrid_validator.py núcleo]
    ABM_C --> HV
    ABM_G --> HV
    HV --> Pp[permutation_test_edi]
    HV --> Bp[bootstrap_ci]
    HV --> Cp[protocolo C1-C5 + 8 cond]
    Pp --> Out[outputs/metrics.json]
    Bp --> Out
    Cp --> Out
```

---

## Fig. 9.31. Multi-sonda (capítulo 09-31)

**Figura A.10.8.**

```mermaid
graph LR
    A[Caso strong] -->|sonda primaria| EP[EDI primario]
    A -->|sonda alternativa<br>motivación distinta| EA[EDI alternativa]
    EP -->|comparar| D[Δ delta]
    EA --> D
    D -->|abs Δ ≤ 0.10| CF[Convergencia fuerte]
    D -->|0.10 menor abs Δ menor 0.20| CM[Convergencia moderada]
    D -->|abs Δ mayor 0.20| Dv[Divergencia]
```

---

## Fig. C.1. Esquema de convergencia EDI-Wolfram (capítulo 04-debates §14)

**Figura A.10.9.**

```mermaid
graph TD
    R[1 Selección regla<br>p.ej. CA Rule 110] --> S[2 Generar 200 simulaciones<br>con perturbaciones iniciales]
    S --> SM[3 Construir sonda macro<br>densidad / curvatura discreta]
    SM --> EE[4 Aplicar EDI<br>con perm 999 + boot 500 + C1-C5]
    EE --> H[5 Hipótesis<br>EDI ≥ 0.30 → cierre operativo macro<br>EDI menor 0.10 → irreducibilidad confirmada]
    H --> L[6 Lectura interpretativa]
```

---

## Trazabilidad

Las figuras están versionadas en este apéndice. Cualquier cambio se ejecuta aquí y se referencia desde el capítulo que las menciona. La conversión a SVG/PNG se ejecuta pre-depósito mediante:

```bash
mmdc -i 10-apendices-tecnicos/03-figuras-mermaid.md -o figures/mermaid_svg/  # mermaid-cli
```

o automáticamente por GitHub/Pandoc con filtros mermaid.


<p align="right"><sub><a href="#tabla-de-contenidos">↑ volver al índice</a></sub></p>

---
