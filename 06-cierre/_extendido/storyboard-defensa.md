---
title: "Storyboard estructural — Defensa oral (versión 30 / 15 / 5 min)"
extends: 06-cierre/02-guia-de-defensa.md
created: 2026-05-16
---

# Storyboard estructural — Defensa oral

> **STORYBOARD-IA pendiente firma autoral Jacob.** Este archivo es guion estructural: define qué slide cubre qué condición demostrativa, con cifras canónicas literales y referencias a capítulo/figura del corpus. NO contiene voz visual final ni redacción narrativa: la voz visual final es de Jacob + plantilla institucional H-U2 (pendiente). Cuando llegue la plantilla, el ensamblaje es mecánico. Fuentes consolidadas: `06-cierre/01-conclusion-demostrativa.md`, `06-cierre/02-guia-de-defensa.md`, `06-cierre/_extendido/versiones-cortas-defensa.md`, `figures/`.

## Función del archivo

- Mapear cada slide a (i) qué pieza argumental cubre, (ii) qué capítulo la verifica, (iii) qué cifra canónica o figura usa, (iv) qué test de fallo aplica.
- Reservar la voz visual y la redacción final a Jacob + plantilla institucional.
- Permitir bajada a 15 min y 5 min por compresión, no por reescritura.

## Inventario de figuras disponibles (`figures/`)

- `figures/corpus/corpus_edi_bars.{png,svg}` — barras EDI con CI 95 % (32 casos macro).
- `figures/corpus/corpus_multiescala_scatter.{png,svg}` — escala espacial × temporal (10 casos inter-escala).
- `figures/corpus/corpus_domain_heatmap.{png,svg}` — dominio × banda EDI.
- `figures/corpus/corpus_qes_distribution.{png,svg}` — histograma QES + curva acumulada.
- `figures/corpus/edi_vs_baselines.{png,svg}` — acoplado vs ARIMA/VAR sobre 7 casos.
- `figures/caso30/phase_portrait_caso30.{png,svg}` — espacio de fase del caso 30.
- `figures/mermaid_svg/figura_01.svg` — Historia/Tarea/Agente.
- `figures/mermaid_svg/figura_02.svg` — Aparato R→μ→X→G→H→κ→ε.
- `figures/mermaid_svg/figura_03.svg` — Dossier de anclaje (14 componentes).
- `figures/mermaid_svg/figura_04.svg` — Pipeline ABM+ODE.
- `figures/mermaid_svg/figura_05.svg` — Asimetría L1↔B↔L3↔S.
- `figures/mermaid_svg/figura_06.svg` — Pie distribución corpus 30 casos.
- `figures/mermaid_svg/figura_07.svg` — Arquitectura técnica `case_config → runner`.
- `figures/mermaid_svg/figura_08.svg` — Test multi-sonda primaria vs alternativa.
- `figures/mermaid_svg/figura_09.svg` — Piloto Wolfram Rule 110.

## Versión 30 minutos (defensa estándar tesis doctoral, 25 slides)

### Slide 1 — Portada

- Título: «Irrealismo operativo de estructuras pre-ontológicas».
- Subtítulo: ontología, epistemología y metodología generales multiescalares.
- Autor principal: Jacob Agudelo (U. Antioquia). Colaborador técnico: Steven Vallejo Ortiz.
- Fecha de sustentación, programa doctoral, director.
- [PENDIENTE: plantilla institucional H-U2 — logo, tipografía oficial.]

### Slide 2 — Agradecimientos

- [PENDIENTE: contenido autoral de Jacob — director, jurado, instituciones, equipo.]
- Declaración de uso de IA bajo dirección humana, no co-autora (1 línea).

### Slide 3 — Tesis en una frase + aparato

- Frase canónica: «Defiendo un irrealismo operativo de estructuras pre-ontológicas como ontología, epistemología y metodología generales aplicables a cualquier escala».
- Tres marcos > 40 casos (los 40 casos son justificación operativa, no la tesis).
- Figura: `figures/mermaid_svg/figura_02.svg` (aparato R→μ→X→G→H→κ→ε).
- → cap 06-01 §0 (tesis) + cap 03-01 §1 (aparato).

### Slide 4 — Condición 1: ontología sin multiplicación de sustancias

- Producto: ontología material-relacional, cinco modos de realidad, sin segunda sustancia.
- Estructuras pre-ontológicas = atractores empíricamente identificables (5 condiciones de admisión).
- Test de fallo: si requiere segunda sustancia o dualismo encubierto, falla.
- Estado: verificación sostenida.
- → cap 02-01 + cap 06-01 §1 Condición 1.

### Slide 5 — Condición 2: epistemología con compresiones legítimas verificables

- Producto: compresión κ vía EDI = 1 − RMSE_coupled / RMSE_no_ode.
- 4 casos con `overall_pass=True` cumplen 13 condiciones simultáneas.
- Test de fallo: compresión sin predicción discriminante.
- → cap 02-02 + cap 03-04 + cap 06-01 §1 Condición 2.

### Slide 6 — Condición 3: aparato formal con protocolo empírico

- Cinco operadores μ, G, H, κ, ε con instanciación empírica.
- Pipeline ABM+ODE de 2252 líneas (`hybrid_validator.py`).
- En los 5 casos strong, los 5 operadores se instancian con datos públicos.
- Figura: `figures/mermaid_svg/figura_04.svg` (pipeline ABM+ODE).
- → cap 03-01 + 03-02 + 03-03 + 03-04 + cap 06-01 §1 Condición 3.

### Slide 7 — Condición 4: asimetría L1↔B↔L3↔S como protocolo

- Cuatro registros articulados; cada parámetro de L3 traduce a variable de B.
- Test de fallo: parámetro sin traducción a B = formalismo desanclado.
- Estado: sostenida en los 5 casos strong.
- Figura: `figures/mermaid_svg/figura_05.svg` (asimetría L1↔B↔L3↔S).
- → cap 02-04 + cap 06-01 §1 Condición 4.

### Slide 8 — Condición 5: cartografía multidominio con dossier completo

- 30 casos en física, biología, economía, política, tecnología, cultura, conducta humana.
- Dossier de 14 componentes obligatorios.
- Figura: `figures/mermaid_svg/figura_03.svg` (dossier 14 componentes).
- → cap 02-04 + cap 09 + cap 06-01 §1 Condición 5.

### Slide 9 — Condición 6: discriminación pública contra rivales

- 15 posiciones rivales con criterios públicos (incluidos Wolfram e IIT).
- Ventaja en al menos 2 celdas contra cada rival; en caso ancla, ventaja en 5 celdas.
- Test de fallo: rival absorbe la tesis sin diferencia discriminante.
- → cap 04-01 + cap 06-01 §1 Condición 6.

### Slide 10 — Condición 7: honestidad sobre el dominio de validez

- Caso 30 (behavioral dynamics) rechazado v1 con EDI=0.002.
- Solo la sonda v2 (Fajen-Warren segundo orden) produjo Nivel 3 weak.
- Test de fallo: forzar la admisión reformulando datos/sondas/criterios.
- Estado: sostenida — el aparato rechaza honestamente cuando debe rechazar.
- Figura: `figures/caso30/phase_portrait_caso30.svg`.
- → cap 06-01 §1 Condición 7 + `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`.

### Slide 11 — Cifras agregadas del corpus inter-dominio (Tabla 6.1.1)

- 6 strong con gate completo (post-iter-7 B-T2 2026-05-17): Energía 0.650, Deforestación 0.602, Kessler 0.353, Riesgo Biológico 0.333, Urbanización 0.337 (caso 18 iter 5), Microplásticos 0.806 (caso 24 iter 7).
- 1 strong sin gate: Starlink 0.7575 (caso 26 promovido Trend→Strong-sin-gate iter 7 con CI bootstrap estable [0.741, 0.775]).
- 7 weak con disclosure (incluye Océanos caso 17 promovido Null→Weak iter 7 con `valid=False`), 0 suggestive, 4 trend.
- 6 null genuinos (incluye Conciencia caso 02 confirmado iter 7) + 1 EDI negativo (Paradigmas −0.144) + 1 falsificación local del aparato (Acidificación oceánica caso 19 iter 4) + 0 rechazados por gate C1-C5 (Océanos promovido iter 7).
- 3 controles de falsación rechazados (Exogeneidad, No-estacionariedad, Observabilidad).
- Nota: composición invariante a rejilla de umbrales 0.05-0.15 × 0.20-0.40 (F06-03) bajo régimen sintético; iter 7 consolida los upgrades reales (09 Finanzas, 17 Océanos, 18 Urbanización, 22 Fósforo, 24 Microplásticos, 26 Starlink) frente a downgrades reales (01 Clima, 03 Contaminación, 13 Políticas).
- Figura: `figures/corpus/corpus_edi_bars.svg` + `figures/mermaid_svg/figura_06.svg` (pie 30 casos).
- → cap 06-01 §1 Condición 5 (Tabla 6.1.1) + Tabla.

### Slide 12 — Corpus inter-escala (10 casos, 30 órdenes de magnitud)

- 7 strong en 7 escalas distintas: atómica (espín-órbita 10⁻¹⁰ m), cuántica (decoherencia 10⁻⁹ m), bioquímica (Michaelis-Menten 10⁻⁸ m), celular oscilatoria (NF-κB 10⁻⁵ m), individual (HRV cardíaco 1 m), astrofísica (Cefeida 10¹¹ m), astrofísica masiva (cúmulo globular 10²⁰ m).
- 1 weak (ciclo celular Tyson-Novak), 2 nulls honestos (Villin Headpiece, locomoción τ-dot).
- Aclaración Trampa 1: corpus inter-escala = conjetura de aplicabilidad sobre datos sintéticos derivados de parámetros publicados (Lindblad, Bloch, Tyson-Novak, Hoffmann, Mackey-Glass, Leavitt, Plummer); no demostración de generalidad ontológica.
- Figura: `figures/corpus/corpus_multiescala_scatter.svg`.
- → cap 06-01 §0 + cap 02 (versiones-cortas §3.7) + cap 09.

### Slide 13 — Hostile testing severo (gate completo)

- 0/2000 falsos positivos del gate completo bajo random walk masivo.
- Wilson 95 % CI sobre 0/2000 = [0, 0.00191].
- Agregación de tres scripts canónicos: N1_falsos_positivos.py (n=500) + V4_06_hostile_multiescala.py (n=500) + N5_hostile_testing.py (n=1000).
- 3/3 controles de falsación rechazados (06-exoplanetas, 07-noticias-shanghai, 08-observacional-control; EDI ≤ 0.06; gate=false).
- → cap 06-01 §8.1 (L1) + glosario operativo entrada EDI.

### Slide 14 — Hostile testing severo (test cruzado de sondas)

- 0/12 circularidad detectada en test cruzado V4-01 inter-escala.
- Las sondas son específicas: no producen EDI alto sobre datos que no son suyos.
- Sondas secundarias re-aplicadas a arrays primarios reales: 1/7 converge bajo |ΔEDI| ≤ 0.10 (deuda AU-6: descomposición real 1/2 vs reconstruido 0/5 pendiente).
- Figura: `figures/mermaid_svg/figura_08.svg` (multi-sonda primaria vs alternativa).
- → cap 06-01 §3.6 + §4.1 AU-6.

### Slide 15 — Condiciones de fracaso falsables (Escenario 1.a / 1.b)

- Escenario 1.a: si Energía, Deforestación, Kessler o Riesgo Biológico dejan de pasar `overall_pass` bajo perfiles agresivos (n_perm ≥ 2999, n_boot ≥ 1500) o son superados por baselines estadísticos puros.
- Escenario 1.b (parcialmente activado): si los 3 controles de falsación (06, 07, 08) empiezan a producir EDI significativo bajo el mismo perfil.
- Comando regenerador: `./tesis run --case <NN>` para `NN ∈ {04, 16, 20, 27, 06, 07, 08}`.
- → cap 06-01 §2 Escenario 1.

### Slide 16 — Condiciones de fracaso falsables (Escenarios 2 y 3)

- Escenario 2: el aparato no escala fuera del dominio actual; criterio externo: refinamiento de sonda + EDI significativo en ≥ 2 dominios fuera de macro-temporal antes de 2027-12.
- Escenario 3: la asimetría L1↔B↔L3↔S no se sostiene; criterio externo: dossier rechazado por revisión externa en ≥ 1 dominio del corpus.
- Condición de prioridad histórica (no falsación popperiana): si un rival reúne anclaje + asimetría + dossier + cartografía + falsación antes que la tesis, se cede prioridad — Wolfram al 2026-05 no la satisface.
- → cap 06-01 §2 Escenarios 2-3 + condición de prioridad histórica.

### Slide 17 — Deuda residual fechada (críticas para defensa)

- Caso 30 elevación a LoE = 4 (datos humanos VENLab/WALK-MS, 9-10 meses, aval CEI).
- Baselines no-lineales sobre `overall_pass` afectados (GP, LSTM, ESN sobre Deforestación y Riesgo Biológico con DM-test + CI bootstrap, 2 meses) — abierto por hallazgo AU-3.
- Topologías heterogéneas para Nivel 5 (scale-free / small-world, 6 meses).
- Datos reales abiertos en corpus inter-escala (IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3; 6-12 meses).
- → cap 06-01 §4 Tabla 6.1.2.

### Slide 18 — Deuda residual técnica del aparato

- AU-4 significance theater: Salinización reclasificada (CI cruza cero + magnitud trivial).
- TENG-01 permutación iid bajo dependencia temporal: implementar block-permutation `ℓ ∝ n^{1/3}`.
- TENG-02 bootstrap percentil simple en pocas muestras: implementar BCa con `bca_z0`, `bca_a`.
- TENG-04 invariancia CPU/GPU de C2: unificar a `seed=seed_base`.
- TENG-08 C1 disyuntivo permite EDI<0: reclasificar `c1_absolute` como `c1_fallback`.
- TENG-10 baselines sobre target distinto: ejecutar baselines sobre `primary_arrays.json:obs[val_idx]`.
- TENG-12 hash MD5 no detecta inconsistencia interna: implementar `verify_internal_consistency.py`.
- TENG-13 calibración bi-criterio vs RMSE-only: estudio de sensibilidad con `ΔEDI`.
- B-T-NEW-AUC-METH: methodology canónica del AUC-ROC = 0.886 ausente.
- → cap 06-01 §4.2.

### Slide 19 — Discriminación contra rivales (síntesis tabla cap 04)

- 15 rivales discriminados en ≥ 2 criterios cada uno.
- Wolfram Physics Project: comparte hipergrafos; discrimina en C (admisión empírica), D (asimetría protocolar), E (cartografía multidominio con falsación). Piloto Rule 110 ejecutado: EDI=0.55.
- IIT (Tononi-Boly-Massimini-Koch 2016): comparte métrica computable sobre estructura de dependencias; discrimina en C, D, F + tratabilidad (Φ intratable más allá de ~10-12 nodos).
- Figura: `figures/mermaid_svg/figura_09.svg` (piloto Wolfram Rule 110).
- → cap 04-01 + cap 04-03 (tabla síntesis).

### Slide 20 — Aporte ontológico

- Estructuras pre-ontológicas a cualquier escala donde el aparato opera con sonda físicamente motivada.
- Cuatro invariantes (sustrato, acoplamiento, atractor, κ) operativamente medibles desde qubit a cúmulo globular.
- Distinción κ-pragmática vs κ-ontológica con criterios operativos.
- → cap 02-01 §Nota sobre κ + cap 06-01 §5.1.

### Slide 21 — Aporte epistemológico

- Conocimiento como compresión disciplinada bajo intervención ablativa.
- Misma teoría del conocimiento en cualquier escala; lo que cambia es la sonda específica.
- Limitación reconocida: p-value declarado con tasa empírica de tipo I = 24 %; umbrales EDI sí robustos (0.6 % supera weak, 0 % supera strong bajo random walk).
- → cap 02-02 + cap 06-01 §5.2.

### Slide 22 — Aporte metodológico (general, no regional)

- Protocolo replicable de 9 fases con dossier de 14 componentes.
- Motor `edi_engine` invariante a la escala (qubit → cúmulo globular sin reentrenar arquitectura).
- Determinismo `seed=42` con `requirements-locked.txt` para reproducibilidad inter-instalación.
- Ejecutable: cualquier tercero puede correr el motor sobre datos nuevos.
- Figura: `figures/mermaid_svg/figura_07.svg` (arquitectura técnica `case_config → runner`).
- → cap 03-01 + cap 06-01 §5.3.

### Slide 23 — Limitaciones declaradas (parte 1)

- p-value mal calibrado (24 % empírico) aunque umbrales EDI robustos.
- Caso 30 con circularidad parcial detectada por sonda alternativa (block bootstrap p ≈ 0.978).
- Depuración post-hoc del corpus inter-escala (no pre-registrado).
- Datos sintéticos en corpus inter-escala pendientes de elevación a LoE 4-5.
- Escalas como etiquetas nominales basadas en parámetros publicados.
- → cap 06-01 §8.2 + cap 04-05 (consolidación L1-L20).

### Slide 24 — Limitaciones declaradas (parte 2)

- AUC-ROC = 0.886 mide coherencia interna del umbral EDI, no discriminación contra baseline externo.
- ARIMA/VAR superan al acoplado en RMSE held-out en 2/4 `overall_pass` (Deforestación, Riesgo Biológico). Reducción de alcance, no derrota.
- Ningún caso del corpus cumple los 3 criterios κ-ontológica simultáneamente: todas las afirmaciones son κ-pragmática.
- Sin revisión por pares humanos externos al cierre actual.
- → cap 06-01 §3.6 + §8.2 + cap 04-05.

### Slide 25 — Cierre + Q&A

- Fórmula final: «Mínima en sustancias, rica en relaciones, controlada en sus recortes, anclada en cartografía empírica multidominio con discriminación pública contra rivales, abierta en su programa de extensión, disciplinada por anti-reificación operativa, y honesta en sus rechazos».
- «La diferencia entre tesis demostrada y manifiesto bien escrito es que la tesis acepta perder y especifica cómo.»
- Apertura formal a Q&A.
- → cap 06-01 §9 + §10.

## Versión 15 minutos (defensa media, 13 slides)

Compresiones respecto a la versión 30 min:

- **Conservar:** Slides 1 (portada), 3 (tesis + aparato), 8 (cartografía con dossier), 11 (Tabla 6.1.1 inter-dominio), 12 (corpus inter-escala), 13 (hostile testing gate), 15 (Escenario 1.a/1.b), 17 (deuda residual crítica), 19 (rivales — Wolfram + IIT), 22 (aporte metodológico general), 23 (limitaciones parte 1), 24 (limitaciones parte 2), 25 (cierre + Q&A).
- **Fundir:** Slides 4-10 (7 condiciones individuales) → 1 slide tabla resumen «7 condiciones × capítulo verificador × estado»; Slides 20-21-22 (3 aportes) → 1 slide tríptico ontología/epistemología/metodología.
- **Eliminar:** Slide 2 (agradecimientos comprimido a línea en Slide 1), Slide 14 (test cruzado de sondas absorbido por Slide 13 como bullet), Slide 16 (Escenarios 2-3 absorbidos en Slide 15), Slide 18 (deuda técnica TENG absorbida como bullet en Slide 17).

Estructura final 15 min (13 slides): portada+agradecimientos / tesis+aparato / tabla 7 condiciones / dossier-cartografía / Tabla 6.1.1 inter-dominio / corpus inter-escala / hostile testing agregado / escenarios falsables / deuda residual / rivales (Wolfram+IIT) / aporte tripartito / limitaciones / cierre.

## Versión 5 minutos (defensa corta, 9 slides)

Selección mínima de piezas no comprimibles:

- **Slide 1** — Portada con tesis en una frase + autor/director (Slide 1+3 fundidos).
- **Slide 2** — Aparato (figura `figura_02.svg` + 5 operadores μ, G, H, κ, ε + EDI = 1 − RMSE_coupled / RMSE_no_ode).
- **Slide 3** — 7 condiciones de demostración en una tabla (capítulo verificador + estado).
- **Slide 4** — Cifras canónicas inter-dominio (post-iter-7 2026-05-17): 6 strong gate completo (Energía 0.650, Deforestación 0.602, Kessler 0.353, Riesgo Biológico 0.333, Urbanización 0.337, Microplásticos 0.806) + 1 strong sin gate (Starlink 0.7575) + 3 controles rechazados (figura `corpus_edi_bars.svg`).
- **Slide 5** — Corpus inter-escala: 7 strong en 7 escalas + 30 órdenes de magnitud + aclaración de datos sintéticos (figura `corpus_multiescala_scatter.svg`).
- **Slide 6** — Hostile testing: 0/2000 (Wilson 95 % CI [0, 0.00191]) + 0/12 circularidad + 3/3 controles rechazados.
- **Slide 7** — 5 escenarios falsables canónicos (1.a, 1.b, 2, 3, prioridad histórica) en una sola viñeta cada uno.
- **Slide 8** — Aporte tripartito (ontología + epistemología + metodología) + limitaciones críticas (p=24 %, AUC interno, κ-pragmática solamente).
- **Slide 9** — Cierre con fórmula final + apertura Q&A.

## Cierre del storyboard

Estructura final: 25 / 13 / 9 slides para 30 / 15 / 5 minutos. Toda cifra es literal contra `metrics.json` y prosa de cap 06-01. Toda figura existe en `figures/`. Voz visual y redacción narrativa pendientes de Jacob + plantilla institucional H-U2.
