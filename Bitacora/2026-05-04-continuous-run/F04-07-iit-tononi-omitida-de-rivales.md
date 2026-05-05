# F04-07 — IIT (Tononi) omitida de la lista de 14 rivales

**Fecha:** 2026-05-04
**Origen:** hallazgo de adversarial-reviewer cap04+06 (2026-05-05).
**Files señalados:** `04-debates/01-debates-con-posiciones-rivales.md:6`, `04-debates/03-tabla-comparativa-rivales.md:32`.

## (a) Verificación de la afirmación

**La afirmación adversarial es correcta y verificable.**

1. La tesis del cap 04-01 (línea 6) declara públicamente que se discrimina contra **catorce rivales filosófica y empíricamente identificables** y los enumera. La lista NO contiene IIT (Integrated Information Theory de Tononi y colaboradores).
2. La tabla 4.3.2 (`04-debates/03-tabla-comparativa-rivales.md:32-47`) repite las catorce filas. Ninguna corresponde a IIT.
3. Búsqueda `Tononi|IIT|Integrated Information` en `04-debates/`: **0 matches**. Confirmado: IIT está ausente del capítulo de debates.
4. La tesis SÍ menciona IIT en otro capítulo: `02-fundamentos/05-temporalidad-y-causalidad.md:132` declara que la afinidad con causal emergence (Hoel, Albantakis, Tononi 2013) "no implica adopción de IIT como marco; la tesis usa la noción de información efectiva como métrica comparable, no como ontología de la consciencia".
5. Existe el PDF `07-bibliografia/Tononi - Integrated Information Theory (2016).pdf` (Scholarpedia entry, accesible localmente).

**Diagnóstico:** la tesis menciona IIT lateralmente en cap 02-05 §2.5 para distanciarse, pero NO la declara como rival explícito en cap 04, pese a que IIT:

- ofrece una métrica formal (Φ, integrated information) que es **el competidor más natural de EDI** en el discurso 2008-2024 sobre métricas operativas de organización causal/integración;
- es el marco teórico de referencia mundial para el caso 02 (consciencia) del corpus EDI — que la tesis ejecuta y reporta;
- comparte con la tesis el rechazo del reduccionismo plano y la apuesta por una métrica computable definida sobre estructura de dependencias.

La omisión NO es trivial: hace la lista de "14 rivales" **selectivamente parcial** en exactamente el dominio donde la tesis tiene un caso ejecutado (caso 02 conciencia). Un evaluador hostil que conozca la literatura — cualquier filósofo de la mente o teórico de la consciencia post-2010 — leerá la omisión como evasión.

## (b) Propuesta de edición concreta — `needs_human` (Jacob)

Tres salidas posibles, **todas requieren firma de Jacob** porque (i) modifican una afirmación pública central ("catorce rivales"), (ii) requieren posición filosófica sustantiva sobre la relación EDI↔Φ, (iii) afectan la defensibilidad del caso 02.

### Opción 1 — Añadir IIT como rival #15 (recomendada técnicamente)

- Cambiar "catorce rivales" → "quince rivales" en `04-debates/01-debates-con-posiciones-rivales.md:6` y en `03-tabla-comparativa-rivales.md` (cabecera "14 rivales").
- Añadir §15 en cap 04-01 con cita verbatim de **Tononi (2008, "Consciousness as Integrated Information: a Provisional Manifesto", *Biological Bulletin* 215(3):216-242)** — definición de Φ — y **Oizumi, Albantakis & Tononi (2014, "From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0", *PLoS Comput Biol* 10(5):e1003588)** — formalización IIT 3.0.
- Añadir fila 15 en tabla 4.3.2 con criterios discriminantes propuestos:
  - **A** ✓ (IIT acepta sustrato físico) → no discrimina.
  - **B** parcial (IIT define Φ a una sola escala maximizante; EDI multiescala explícita).
  - **C** ✗ (IIT carece de dossier de catorce componentes para admisión empírica de categorías).
  - **D** ✗ (IIT no tiene asimetría L1↔B↔L3↔S; trabaja sobre matriz de transición única).
  - **E** parcial (IIT predice correlatos perceptuales pero Φ es **computacionalmente intratable** >10-12 nodos; EDI escalable a cientos).
  - **F** ✗ (IIT específicamente diseñado para consciencia; EDI multidominio).
  - **Discrimina en:** C, D, F (intratabilidad computacional de Φ + monodominio + ausencia de dossier).

**Costo argumentativo declarado:**
- la tesis pierde la cifra redonda "14 rivales" que aparece en múltiples capítulos y bitácoras (cambio en cascada);
- requiere defender que EDI y Φ son **comparables pero no equivalentes** (riesgo: lectura como "IIT-light");
- exige posición sobre IIT 3.0 vs IIT 4.0 (Albantakis et al. 2023) — la tesis tendría que escoger versión y justificar;
- el caso 02 conciencia (consciencia) ya reportado debe contestar: ¿por qué EDI=X y no Φ?

### Opción 2 — Declarar IIT "rival no-discriminado, fuera de alcance" con costo

- Mantener "14 rivales" pero añadir nota en cap 04-01 §1: "IIT (Tononi 2008, Oizumi-Albantakis-Tononi 2014) se reconoce como métrica adyacente a EDI en el dominio consciencia, pero **no se confronta como rival** porque (i) IIT es ontología-de-la-consciencia, no marco general multidominio, y (ii) la cuestión IIT↔EDI exige tratamiento monográfico que excede el alcance de esta tesis. Se declara como deuda residual."
- Añadir entrada en `06-cierre/` deuda residual: "Confrontación detallada IIT vs EDI sobre caso 02 — pendiente para trabajo posterior".

**Costo argumentativo:** declarar abiertamente que el rival más obvio en el dominio del caso 02 queda fuera de la confrontación. Es honesto pero **debilita la pretensión de exhaustividad** ("filosófica y empíricamente identificables") en el dominio consciencia. Lectura hostil: "convenientemente fuera de alcance".

### Opción 3 — Reformular la lista como "rivales centrales" sin pretensión exhaustiva

- Cambiar línea 6 cap 04-01: "catorce rivales filosófica y empíricamente identificables" → "catorce posiciones rivales centrales seleccionadas como representativas de los espacios principales de oposición filosófica y metodológica; otras posiciones (notablemente IIT/Tononi en el dominio consciencia, predictive processing/Friston, free-energy principle) se discuten en capítulos específicos donde su pertinencia es máxima".
- Mantener tabla 4.3.2 con 14 filas; añadir nota al pie con la lista de rivales reconocidos pero no tabulados.

**Costo argumentativo:** abandona la pretensión de cierre exhaustivo del espacio rival. Es la salida más honesta epistemológicamente pero **rebaja una afirmación que la tesis ha defendido públicamente** ("la tabla no produce absorción"). Requiere reescritura de `01-debates-con-posiciones-rivales.md:6` y de bitácoras que repiten "14 rivales".

## (c) Costo argumentativo global y recomendación

**Costo de no actuar:** un evaluador familiarizado con teorías formales de consciencia detectará la omisión en minutos. La tesis pierde credibilidad asimétricamente — mucho más en el dominio consciencia que en otros — porque ejecuta el caso 02 y reporta cifras EDI sin contrastarlas con la métrica de referencia (Φ) de la literatura.

**Costo de actuar (cualquier opción):** trabajo filosófico sustantivo sobre IIT que Jacob debe firmar. La asistencia técnica puede preparar el material (cita verbatim Tononi 2008, formalización Oizumi 2014, lectura crítica de la intratabilidad de Φ) pero NO puede decidir cuál de las tres opciones adopta la tesis — eso es decisión filosófica autorial.

**Recomendación operativa (no decisional):** Opción 1 si Jacob acepta el costo de defender EDI vs Φ frontalmente (recomendada porque elimina la objeción de raíz); Opción 2 si el calendario no permite trabajo monográfico (honesta pero defensiva); Opción 3 si Jacob considera que la pretensión exhaustiva es indefendible en cualquier hipótesis (la más conservadora).

## Estado

- `needs_human` — decisión filosófica que requiere firma de Jacob Agudelo. La asistencia puede preparar borrador de §15 con citas verbatim Tononi 2008 y Oizumi-Albantakis-Tononi 2014 en cuanto Jacob escoja opción.
- Tarea sugerida para `TAREAS_PENDIENTES.md` Sección A (humanas): **H-J-IIT-01** "Decidir si IIT entra como rival #15 (Opción 1), como rival declarado fuera de alcance (Opción 2) o si la lista se reformula como no-exhaustiva (Opción 3)".
- Tarea sugerida Sección B (ejecutable post-decisión Jacob): **B-IIT-02** "Preparar borrador de §IIT (cap 04-01) y fila 15 (tabla 4.3.2) con citas verbatim paginadas a partir de PDF `07-bibliografia/Tononi - Integrated Information Theory (2016).pdf` + descarga de Tononi 2008 *Biol Bull* y Oizumi 2014 *PLoS Comput Biol*".

## Acceptance check

- [ ] §IIT en cap 04-01 con cita verbatim Tononi 2008 o Oizumi-Albantakis-Tononi 2014 — **no realizado** (requiere Jacob).
- [ ] Tabla 4.3.2 fila 15 IIT con criterios discriminación EDI vs Φ — **no realizado** (requiere Jacob).
- [x] O declarar rival no-discriminado con costo — **propuesto como Opción 2 con costo declarado**, pendiente decisión Jacob.
