# Shortlist H-S2: Estadísticos / Físicos de complejidad — revisores hostiles

Tesis objetivo: aparato EDI = ABM+ODE acoplado, permutación (n=999), bootstrap (n=500), criterios C1-C5.
Fecha de compilación: 2026-05-16.

---

## Bloque E — Validación de ABM / simulaciones (hostilidad metodológica a simulaciones sin validación externa)

| # | Nombre | Afiliación | Publicaciones recientes pertinentes | Ángulo de ataque esperado | Confidence |
|---|--------|------------|-------------------------------------|--------------------------|------------|
| E1 | **Bruce Edmonds** | Manchester Metropolitan University (Director, Centre for Policy Modelling; Professor of Social Simulation) | (1) "The practice and rhetoric of prediction – the case in agent-based modelling", *International Journal of Social Research Methodology* 26(2), 2023; (2) "An introduction to the themed section on 'Using agent-based simulation for integrating qualitative and quantitative evidence'", *IJSRM*, 2022; (3) "Different Modelling Purposes", *Simulating Social Complexity*, Springer, 2017 (referencia estándar en ABM) | Atacará si EDI no ha sido validado contra datos empíricos externos (fuera del modelo): "post-truth drift" en simulaciones — sostendrá que un índice derivado enteramente del comportamiento del modelo no puede ser evidencia de estructura en el mundo | HIGH |
| E2 | **Flaminio Squazzoni** | University of Milan (Professor of Sociology, Dept. Social & Political Sciences); ex-presidente European Social Simulation Association | (1) "Social Simulation in the Social Sciences" (con Jager & Edmonds), *Social Science Computer Review* 32(3), 2014 (base); (2) *Agent-Based Computational Sociology*, Wiley, 2012 (base); Google Scholar activo 2020-2024 | Atacará desde la sociología computacional: pedirá validación de face, output y predictiva de los 40 casos del corpus; cuestionará si la acoplación ABM+ODE respeta supuestos sobre actores sociales heterogéneos | MEDIUM |

---

## Bloque F — Inferencia por permutación y bootstrap (hostilidad técnica estadística)

| # | Nombre | Afiliación | Publicaciones recientes pertinentes | Ángulo de ataque esperado | Confidence |
|---|--------|------------|-------------------------------------|--------------------------|------------|
| F1 | **Dimitris N. Politis** | UC San Diego (Distinguished Professor of Mathematics; Associate Director, Halicioglu Data Science Institute; Endowed Chair desde 2022) | (1) "Local Block Bootstrap for Inhomogeneous Poisson Marked Point Processes", *Bernoulli* 24(1):592-615, 2018; (2) Lista completa en mathweb.ucsd.edu/~politis (2018-2024 verificada); (3) Trabajo fundacional en subsampling y bootstrap para series temporales y datos dependientes | Atacará si el test de permutación asume intercambiabilidad cuando los datos del ABM tienen dependencia temporal o espacial; preguntará si n=999 es suficiente para la dimensión del espacio de parámetros del modelo acoplado; cuestionará si bootstrap de n=500 es calibrado para la estructura de error del ODE | HIGH |
| F2 | **Sander Greenland** | UCLA (Emeritus Prof. Epidemiology & Statistics; Clarivate Highly Cited Researcher 2019-2025) | (1) "Divergence vs. decision P-values: A distinction worth making in theory and keeping in practice", *Scandinavian Journal of Statistics*, 2023; (2) "Analysis goals, error-cost sensitivity, and analysis hacking: essential considerations in hypothesis testing", *Pediatric & Perinatal Epidemiology*, 2021; (3) "The causal foundations of applied probability and statistics", en *Probabilistic and Causal Inference: Works of Judea Pearl*, 2022 | Atacará el uso de umbrales de permutación como criterio decisional binario (C1-C5); pedirá intervalos de compatibilidad en lugar de p < 0.05 para cada criterio; cuestionará si la función de pérdida implícita en los criterios EDI está declarada explícitamente | HIGH |
| F3 | **Valentin Amrhein** (con Sander Greenland) | University of Basel (Zoology & Evolution) | (1) "Scientists rise up against statistical significance" (con Greenland & McShane, 854 co-signatarios), *Nature* 567:305-307, 2019; (2) "Discuss practical importance of results based on interval estimates and p-value functions, not only on point estimates and null p-values" (con Greenland), *Journal of Information Science*, 2022; (3) "Statistical significance gives bias a free pass", *Eur. Journal of Clinical Investigation*, 2019 | Firme del manifiesto "Moving to a World Beyond p < 0.05" (*The American Statistician*, 2019); atacará cualquier umbral de significancia binaria en los criterios C1-C5 del EDI; pedirá curvas de p-valor (p-value functions) en lugar de decisiones discretas | HIGH |

---

## Bloque G — Física de sistemas complejos (hostilidad por ausencia de fundamento físico)

| # | Nombre | Afiliación | Publicaciones recientes pertinentes | Ángulo de ataque esperado | Confidence |
|---|--------|------------|-------------------------------------|--------------------------|------------|
| G1 | **Mark E. J. Newman** | University of Michigan (Anatol Rapoport Distinguished University Prof. of Physics; external faculty, Santa Fe Institute) | (1) "Luck, skill, and depth of competition in games and social hierarchies" (con Jerdee), *Science Advances* 10: eadn2654, 2024; (2) "Efficient computation of rankings from pairwise comparisons", *JMLR* 24:238, 2023; (3) *Networks* (2nd ed.), OUP, 2018 | Atacará si el modelo de acoplamiento ABM+ODE no respeta principios de escalado conocidos en redes complejas; pedirá comparación de EDI con métricas de integración de red (modularidad, índice de pequeño mundo); cuestionará si "dependencia inter-nivel" captura algo diferente a la correlación cruzada en series temporales acopladas | HIGH |
| G2 | **John P. A. Ioannidis** | Stanford (Prof. Medicine, Epidemiology & Population Health, Statistics, Biomedical Data Science; Director Stanford Prevention Research Center; co-director Meta-Research Innovation Center) | (1) "Transparency, bias, and reproducibility across science: a meta-research view", *JCI* / AAP Presidential Address, 2024; (2) "Assessment of transparency indicators across the biomedical literature", *PLoS Biology*, 2021; (3) "Hundreds of thousands of zombie randomised trials", *Anaesthesia*, 2021 | Desde la perspectiva de la meta-investigación atacará: ¿los 40 casos son una muestra representativa o seleccionada por conveniencia (cherry-picking)? ¿El protocolo de simulación fue pre-registrado? ¿Los resultados EDI son reproducibles por terceros independientes? Pedirá protocolo de pre-registro y análisis de sesgo de selección del corpus | HIGH |

---

## Notas de uso

- Politis es el especialista técnico más preciso en bootstrap/permutación para datos con dependencia; su objeción sería la más difícil de responder si los datos del ABM tienen autocorrelación temporal.
- Greenland + Amrhein son el dúo más directamente relevante para los umbrales discretos C1-C5: su objeción es que toda decisión binaria encubre pérdida de información continua.
- Ioannidis es el más peligroso para la integridad del corpus: preguntará si los 40 casos son una muestra o una antología, y si existe sesgo de confirmación en la selección.
- Newman atacará desde la física: pedirá que EDI sea comparable con medidas estándar de complejidad / acoplamiento de red.

