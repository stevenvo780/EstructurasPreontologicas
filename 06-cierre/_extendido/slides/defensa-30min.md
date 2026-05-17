---
marp: true
theme: default
paginate: true
header: "Estructuras Pre-Ontológicas — Jacob Agudelo + Steven Vallejo"
footer: "U. de Antioquia · 2026"
---

<!-- STORYBOARD-IA pendiente firma autoral Jacob -->
<!-- Derivado de 06-cierre/_extendido/storyboard-defensa.md (versión 30 min, 25 slides) -->
<!-- Toda cifra es literal contra metrics.json y prosa de cap 06-01 -->

# Irrealismo operativo de estructuras pre-ontológicas

- Ontología, epistemología y metodología generales multiescalares
- Autor principal: Jacob Agudelo (U. Antioquia)
- Colaborador técnico: Steven Vallejo Ortiz
- [PENDIENTE: plantilla institucional H-U2 — logo, tipografía oficial]

<!-- speaker notes: presentar título canónico, autoría y programa doctoral. Mencionar director y jurado. -->

---

# Agradecimientos

- [PENDIENTE: contenido autoral de Jacob — director, jurado, instituciones, equipo]
- IA bajo dirección humana, no co-autora (declaración explícita)

<!-- speaker notes: minuto de agradecimientos; declarar uso de IA como herramienta dirigida. -->

---

# Tesis en una frase

- «Defiendo un irrealismo operativo de estructuras pre-ontológicas como ontología, epistemología y metodología generales aplicables a cualquier escala»
- Tres marcos generales > 40 casos
- Los 40 casos son justificación operativa, no la tesis
- cap 06-01 §0 + cap 03-01 §1 (aparato R→μ→X→G→H→κ→ε)

<!-- speaker notes: anclar que la tesis defiende marcos generales; los casos sirven a esos marcos, no al revés. -->

---

# Condición 1 — Ontología sin segunda sustancia

- Ontología material-relacional con cinco modos de realidad
- Estructuras pre-ontológicas = atractores empíricamente identificables
- Cinco condiciones de admisión (C1-C5)
- Test de fallo: si requiere segunda sustancia, falla
- Estado: sostenida — cap 02-01 + cap 06-01 §1

<!-- speaker notes: distinguir de dualismos encubiertos; cada modo de realidad se ancla en relaciones, no en sustancias adicionales. -->

---

# Condición 2 — Compresión epistémica verificable

- Compresión κ vía **EDI = 1 − RMSE_coupled / RMSE_no_ode**
- 4 casos con `overall_pass=True` cumplen 13 condiciones simultáneas
- Test de fallo: compresión sin predicción discriminante
- cap 02-02 + cap 03-04 + cap 06-01 §1 Condición 2

<!-- speaker notes: EDI no mide ajuste; mide ganancia del modelo acoplado frente al desacoplado bajo ablación. -->

---

# Condición 3 — Aparato formal con protocolo empírico

- Cinco operadores μ, G, H, κ, ε con instanciación empírica
- Pipeline ABM+ODE (`hybrid_validator.py`, 2252 líneas)
- 5 casos strong instancian los 5 operadores con datos públicos
- Figura: `figura_04.svg` (pipeline ABM+ODE)
- cap 03-01..03-04 + cap 06-01 §1

<!-- speaker notes: cada operador tiene contraparte computacional concreta; no es álgebra decorativa. -->

---

# Condición 4 — Asimetría L1↔B↔L3↔S

- Cuatro registros articulados como protocolo operativo
- Cada parámetro de L3 traduce a variable de B
- Test de fallo: parámetro sin traducción a B = formalismo desanclado
- Sostenida en los 5 casos strong
- Figura: `figura_05.svg`

<!-- speaker notes: la asimetría es protocolar, no metafísica; permite auditar dónde se quiebra una traducción. -->

---

# Condición 5 — Cartografía multidominio

- 30 casos: física, biología, economía, política, tecnología, cultura, conducta
- Dossier obligatorio de 14 componentes
- Figura: `figura_03.svg` (dossier 14 componentes)
- cap 02-04 + cap 09 + cap 06-01 §1

<!-- speaker notes: cartografía no es colección; cada caso entra con dossier completo o queda rechazado. -->

---

# Condición 6 — Discriminación contra 15 rivales

- 15 posiciones rivales con criterios públicos
- Ventaja en ≥ 2 celdas contra cada rival
- En caso ancla: ventaja en 5 celdas
- Test de fallo: rival absorbe la tesis sin diferencia
- cap 04-01 + cap 06-01 §1 Condición 6

<!-- speaker notes: Wolfram e IIT incluidos; la discriminación es operativa, no terminológica. -->

---

# Condición 7 — Honestidad sobre dominio de validez

- Caso 30 (behavioral dynamics) rechazado v1 con **EDI=0.002**
- Solo la sonda v2 (Fajen-Warren 2º orden) produjo Nivel 3 weak
- Test de fallo: forzar admisión reformulando datos
- Estado: sostenida — el aparato rechaza honestamente
- Figura: `phase_portrait_caso30.svg`

<!-- speaker notes: la tesis acepta perder; el caso 30 es prueba de que el aparato no protege resultados. -->

---

# Corpus inter-dominio — Tabla 6.1.1

- 4 strong con gate: Energía **0.650**, Deforestación **0.602**, Kessler **0.353**, Riesgo Biológico **0.333**
- 1 strong sin gate: Microplásticos **0.782**
- 8 weak · 1 suggestive · 4 trend · 5 null genuinos
- 1 EDI negativo (Paradigmas −0.144) + 2 rechazados por C1-C5
- 3 controles de falsación rechazados
- Composición invariante a rejilla 0.05-0.15 × 0.20-0.40 (F06-03)
- Figura: `corpus_edi_bars.svg` + `figura_06.svg`

<!-- speaker notes: subrayar que la composición no depende de los umbrales elegidos; F06-03 documenta la invariancia. -->

---

# Corpus inter-escala — 30 órdenes de magnitud

- 7 strong en 7 escalas: atómica (10⁻¹⁰ m), cuántica (10⁻⁹ m), bioquímica (10⁻⁸ m), celular oscilatoria (10⁻⁵ m), individual (1 m), Cefeida (10¹¹ m), cúmulo globular (10²⁰ m)
- 1 weak (Tyson-Novak) · 2 nulls honestos (Villin, locomoción τ-dot)
- Trampa 1: corpus inter-escala = conjetura de aplicabilidad sobre datos sintéticos derivados de parámetros publicados
- NO es demostración de generalidad ontológica
- Figura: `corpus_multiescala_scatter.svg`

<!-- speaker notes: declarar explícitamente la limitación de datos sintéticos; pendiente elevación a LoE 4-5. -->

---

# Hostile testing — gate completo

- **0/2000** falsos positivos del gate bajo random walk masivo
- Wilson 95 % CI = **[0, 0.00191]**
- Agregación: N1 (n=500) + V4_06_hostile (n=500) + N5_hostile (n=1000)
- 3/3 controles de falsación rechazados (06, 07, 08): EDI ≤ 0.06, gate=false
- cap 06-01 §8.1 (L1) + glosario operativo EDI

<!-- speaker notes: la combinación gate + permutación + bootstrap controla falsos positivos a tasa empírica nula bajo random walk. -->

---

# Hostile testing — test cruzado de sondas

- **0/12** circularidad detectada en test cruzado V4-01 inter-escala
- Sondas específicas: no producen EDI alto sobre datos ajenos
- Sondas secundarias re-aplicadas: 1/7 converge bajo |ΔEDI| ≤ 0.10
- Deuda AU-6: descomposición real 1/2 vs reconstruido 0/5 pendiente
- Figura: `figura_08.svg` (multi-sonda primaria vs alternativa)

<!-- speaker notes: el test cruzado demuestra que la sonda no puede explotar estructura espuria de otro dominio. -->

---

# Escenario 1.a / 1.b — Falsadores activos

- Escenario 1.a: si Energía, Deforestación, Kessler o Riesgo Biológico dejan de pasar `overall_pass` bajo perfiles agresivos (n_perm ≥ 2999, n_boot ≥ 1500)
- O si son superados por baselines puros
- Escenario 1.b (parcialmente activado): si los 3 controles (06, 07, 08) producen EDI significativo bajo el mismo perfil
- Comando: `./tesis run --case <NN>` para NN ∈ {04, 16, 20, 27, 06, 07, 08}

<!-- speaker notes: cada escenario es ejecutable; cualquier tercero puede reproducir el falsador. -->

---

# Escenarios 2 y 3 + prioridad histórica

- Escenario 2: aparato no escala fuera del dominio actual — criterio: refinamiento + EDI significativo en ≥ 2 dominios fuera de macro-temporal antes de 2027-12
- Escenario 3: la asimetría L1↔B↔L3↔S no se sostiene — criterio: dossier rechazado por revisión externa en ≥ 1 dominio
- Prioridad histórica: si un rival reúne anclaje + asimetría + dossier + cartografía + falsación antes que la tesis, se cede prioridad
- Wolfram al 2026-05 no la satisface

<!-- speaker notes: la prioridad histórica no es falsación popperiana; es honestidad académica sobre primacía. -->

---

# Deuda residual fechada — críticas

- Caso 30 elevación a LoE = 4: datos humanos VENLab/WALK-MS (9-10 meses, aval CEI)
- Baselines no-lineales sobre `overall_pass`: GP, LSTM, ESN sobre Deforestación y Riesgo Biológico con DM-test + CI bootstrap (2 meses) — abierto por AU-3
- Topologías heterogéneas Nivel 5: scale-free / small-world (6 meses)
- Datos reales abiertos inter-escala: IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3 (6-12 meses)
- cap 06-01 §4 Tabla 6.1.2

<!-- speaker notes: deuda declarada con fecha y comando; no se oculta. -->

---

# Deuda residual técnica del aparato

- AU-4 significance theater: Salinización reclasificada (CI cruza cero)
- TENG-01: implementar block-permutation `ℓ ∝ n^{1/3}`
- TENG-02: BCa con `bca_z0`, `bca_a`
- TENG-04: unificar `seed=seed_base` para invariancia CPU/GPU
- TENG-08: reclasificar `c1_absolute` como `c1_fallback`
- TENG-10: baselines sobre `primary_arrays.json:obs[val_idx]`
- TENG-12: `verify_internal_consistency.py`
- TENG-13: estudio de sensibilidad bi-criterio vs RMSE-only
- B-T-NEW-AUC-METH: methodology del AUC-ROC = **0.886** ausente
- cap 06-01 §4.2

<!-- speaker notes: enumerar deuda técnica; cada item tiene ticket y dueño. -->

---

# Discriminación contra rivales — síntesis

- 15 rivales discriminados en ≥ 2 criterios
- **Wolfram Physics Project**: comparte hipergrafos; discrimina en C (admisión empírica), D (asimetría protocolar), E (cartografía multidominio). Piloto Rule 110: **EDI=0.55**
- **IIT** (Tononi-Boly-Massimini-Koch 2016): comparte métrica computable; discrimina en C, D, F + tratabilidad (Φ intratable más allá de ~10-12 nodos)
- Figura: `figura_09.svg` (piloto Wolfram Rule 110)
- cap 04-01 + cap 04-03

<!-- speaker notes: dos rivales fuertes; ambos discriminados por celdas específicas, no por descalificación. -->

---

# Aporte ontológico

- Estructuras pre-ontológicas a cualquier escala donde el aparato opera
- Cuatro invariantes operativamente medibles: sustrato, acoplamiento, atractor, κ
- Desde qubit hasta cúmulo globular
- Distinción κ-pragmática vs κ-ontológica con criterios operativos
- cap 02-01 §Nota sobre κ + cap 06-01 §5.1

<!-- speaker notes: la ontología es general porque los invariantes se miden con el mismo aparato en cualquier escala. -->

---

# Aporte epistemológico

- Conocimiento como compresión disciplinada bajo intervención ablativa
- Misma teoría del conocimiento en cualquier escala; cambia la sonda
- Limitación reconocida: p-value con tasa empírica de tipo I = **24 %**
- Umbrales EDI sí robustos: **0.6 %** supera weak, **0 %** supera strong bajo random walk
- cap 02-02 + cap 06-01 §5.2

<!-- speaker notes: el p mal calibrado se compensa con umbrales EDI robustos; declarar ambos. -->

---

# Aporte metodológico general

- Protocolo replicable de 9 fases con dossier de 14 componentes
- Motor `edi_engine` invariante a la escala (qubit → cúmulo globular sin reentrenar)
- Determinismo `seed=42` con `requirements-locked.txt`
- Ejecutable por terceros sobre datos nuevos
- Figura: `figura_07.svg` (arquitectura `case_config → runner`)
- cap 03-01 + cap 06-01 §5.3

<!-- speaker notes: el motor no es prototipo; está congelado con hashes y versiones bloqueadas. -->

---

# Limitaciones declaradas — parte 1

- p-value mal calibrado (24 % empírico)
- Caso 30: circularidad parcial detectada por sonda alternativa (block bootstrap p ≈ 0.978)
- Depuración post-hoc del corpus inter-escala (no pre-registrado)
- Datos sintéticos pendientes de elevación a LoE 4-5
- Escalas como etiquetas nominales basadas en parámetros publicados
- cap 06-01 §8.2 + cap 04-05

<!-- speaker notes: cada limitación tiene cap y consolidación L1-L20. -->

---

# Limitaciones declaradas — parte 2

- AUC-ROC = **0.886** mide coherencia interna del umbral EDI, NO discriminación contra baseline externo
- ARIMA/VAR superan al acoplado en RMSE held-out en **2/4** `overall_pass` (Deforestación, Riesgo Biológico) — reducción de alcance, no derrota
- Ningún caso cumple los 3 criterios κ-ontológica simultáneamente: todas las afirmaciones son κ-pragmática
- Sin revisión por pares humanos externos al cierre actual
- cap 06-01 §3.6 + §8.2 + cap 04-05

<!-- speaker notes: declarar los costos; la fortaleza está en hacerlos visibles. -->

---

# Cierre + Q&A

- «Mínima en sustancias, rica en relaciones, controlada en sus recortes, anclada en cartografía empírica multidominio con discriminación pública contra rivales, abierta en su programa de extensión, disciplinada por anti-reificación operativa, y honesta en sus rechazos»
- «La diferencia entre tesis demostrada y manifiesto bien escrito es que la tesis acepta perder y especifica cómo»
- Apertura formal a Q&A
- cap 06-01 §9 + §10

<!-- speaker notes: cierre con fórmula final; abrir Q&A invitando preguntas hostiles sobre falsadores activos. -->
