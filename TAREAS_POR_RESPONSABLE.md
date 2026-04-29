# Tareas por responsable

División operativa de los 34 fallos detectados en `FALLOS_PENDIENTES.md` por quién puede cerrarlos. Cada bloque indica el alcance, las dependencias y el tiempo razonable de cierre.

---

## 1. Tareas que la asistencia computacional puede ejecutar

Tareas de implementación técnica, edición textual y generación de outputs que no requieren decisiones filosóficas de fondo ni intervención institucional.

### 1.1 Cierre de fallos científicos por reescritura técnica

| Fallo | Acción | Tiempo |
|-------|--------|--------|
| F11 | Estandarizar todas las series antes del cómputo de EDI; reportar EDI normalizado vs sin normalizar; añadir nota técnica en cap 03-04 sobre sensibilidad al rango. | 1 sesión |
| F12 | Aplicar FWER Holm-Bonferroni real al corpus completo y escribir los p_adjusted en cada `metrics.json`; reclasificar los casos cuya significancia depende de la corrección. | 1 sesión |
| F14 | Reescribir docstring y cita en `calibration.py` declarando explícitamente "moving block bootstrap, no stationary"; o reimplementar stationary bootstrap auténtico de Politis-Romano. | 1 sesión |
| F15 | Implementar baselines ARIMA, VAR y un modelo de espacio de estados (Kalman) sobre los 5 casos strong; generar tabla comparativa EDI vs baselines en cap 03-04. Sin red neuronal recurrente (requiere PyTorch + GPU + tiempo). | 2-3 sesiones |
| F18 | Reescribir Q0 en `quality_scorer.py` añadiendo gate de significancia: Q0 sólo es alto si EDI > umbral *y* p < 0.05. | 1 sesión |
| F19 | Resolver clasificación dual del caso 30: alinear QES_AUDIT con Anexo A.0 (caso 30 = PILOTO bajo cualquier criterio). | 1 sesión |
| F20 | Documentar honestamente en cada `extend_*.py` que es pseudo-replicación, no replicación independiente; ajustar n_effective con factor de corrección. | 1 sesión |
| F21 | Reformular Q5 para distinguir sonda primaria (motivada teóricamente) de secundaria (de prueba); jerarquizar en lugar de simetrizar. | 1 sesión |
| F22 | Reescribir `preregistration.py` para que sea explícitamente "auditoría criptográfica de cambios" en lugar de "pre-registro". Eliminar el lenguaje de pre-registro del Anexo A.0. | 1 sesión |

### 1.2 Cierre de fallos formales

| Fallo | Acción | Tiempo |
|-------|--------|--------|
| F27 | Eliminar referencias decorativas (Kant, Psillos, van Fraassen, Harman) o insertarlas con cita textual real en el cuerpo. | 1 sesión |
| F28 | Redistribuir interlocutores principales: cap 03-02 podría tener Lakatos como principal, cap 03-03 podría tener Bechtel como principal. | 1 sesión |
| F29 | Estandarizar Chicago author-date: "y" en lugar de "&", "et al." consistente, eliminar "1781/1998" donde no es relevante. | 1-2 sesiones |
| F30 | Consolidar 23 anexos en 7-8: glosario unificado (A.1+A.2), dossier+plantilla (A.3), tabla rivales+aplicaciones (A.4+A.5), defensa+Q&A (A.6+A.6b+A.7), corpus+tablas+visualizaciones (A.8+A.9+A.10+A.12), validación ST (A.11), formalización institucional (B.1). Eliminar B.2-B.9 al moverlos a Bitacora. | 2-3 sesiones |
| F31 | Numerar formalmente todas las tablas (Tabla X.Y por capítulo) y figuras (Figura X.Y). | 1-2 sesiones |
| F33 | Generar visualización del corpus: scatter plot escala espacial vs temporal coloreado por dominio + tabla resumen EDI/p/n por caso + curvas EDI bootstrap CI para los 5 strong. | 2 sesiones |
| F34 | Completar glosario A.1 con los 8-10 términos faltantes. | 1 sesión |

### 1.3 Cierre de inconsistencias filosóficas menores (textuales)

| Fallo | Acción | Tiempo |
|-------|--------|--------|
| F7 | Alinear cap 02-06 (afirma "normas son atractores reales") con cap 04-02 §4 (admite operacionalización pendiente): reescribir cap 02-06 como "afirmación condicional a desarrollo metodológico futuro". | 1 sesión |
| F8 | Resolver inconsistencia "información ecológica": elegir una clasificación ontológica (probablemente realidad fuerte) y propagar la decisión al cap 02-04. | 1 sesión |

**Tiempo total acumulado para tareas computacionales:** 18–25 sesiones de trabajo orientado, equivalente a 2–4 semanas de avance focal.

**Lo que NO puedo hacer:** ninguno de los fallos filosóficos de fondo (F1–F6, F9–F10) requiere decisión filosófica humana sobre cómo reformular argumentos, qué tradiciones profundizar, qué dimensiones omitidas incorporar. Y ninguno de los fallos institucionales centrales (F23–F26) puede ejecutarse sin intervención humana o institucional.

---

## 2. Tareas que solo Steven o Jacob pueden ejecutar

Tareas que requieren decisiones filosóficas de fondo, escritura sustantiva, validación con director de tesis, contacto con interlocutores externos.

### 2.1 Reformulación filosófica de fondo

| Fallo | Acción | Quién | Tiempo |
|-------|--------|-------|--------|
| F1 | Refundir la distinción κ-pragmática / κ-ontológica con criterios externos no operativos (e.g., compromiso con realismo de Ladyman-Ross, criterios de invariancia bajo cambio de modelo, predicción ex-ante no observada en entrenamiento). | Jacob (concepto), Steven (formalización) | 2–4 semanas |
| F2 | Reformular teoría de identidad sin caer en circularidad: o se adopta criterio externo (Locke, Parfit, Strawson) o se reconoce honestamente que la "cuenca persistente" es metáfora, no explicación. | Jacob | 1–2 semanas |
| F3 | Aceptar honestamente que la "ontología única multiescalar" es conjetura, no demostración. Reescribir el cap 02-01 §1 como "programa de unificación ontológica" con condiciones de fracaso explícitas. Alternativa: defender la unidad ontológica con argumento independiente del aparato (e.g., Bunge sistémico riguroso, no solo invocado). | Jacob (filosofía), Steven (estructura) | 3–4 semanas |
| F4 | Decidir si se importa rigor topológico estándar (espectro de Lyapunov, dimensión de correlación) o se acepta que "atractor empírico" es categoría operativa, no formal. La primera opción requiere reescritura del cap 02-01 §2 con literatura de sistemas dinámicos no-lineales. | Steven (formalismo) | 2–3 semanas |
| F5 | Escribir refutación filosófica seria de dualismo, idealismo, panpsiquismo. Esto requiere lectura sustantiva de Chalmers (panpsiquismo), Goff, Strawson. Sin esto, el naturalismo queda como petición de principio. | Jacob | 4–8 semanas |
| F6 | Profundizar diálogo con Simondon, Gibson, Dennett, Searle, Bunge. Para cada uno: leer la obra primaria, identificar la objeción real al programa de la tesis, responder con argumento. Trabajo de meses. | Jacob | 8–16 semanas |
| F9 | Decidir si la asimetría L1↔B↔L3↔S es ontológica (defenderla con criterio independiente del lenguaje), epistemológica (modos de acceso), o terminológica (plurilingüismo). Reescribir cap 02-04 §8 con la decisión. | Jacob | 2–3 semanas |
| F10 | Incluir tratamiento de al menos dos dimensiones omitidas: estética y política son las más urgentes. Mereología, género y descolonialidad pueden quedar como deuda explícita. | Jacob | 6–12 semanas |

### 2.2 Decisiones sobre el corpus y la metodología

| Fallo | Acción | Quién | Tiempo |
|-------|--------|-------|--------|
| F13 | Decidir si se modifica `edi_engine.py` para emitir arrays primarios y se re-ejecuta el corpus completo (≈3 semanas), o se acepta que el primer criterio de κ-ontológica fuerte queda como deuda explícita. | Steven | 3 semanas si se ejecuta |
| F16 | Implementar fetch real desde fuentes públicas para los casos donde es posible (World Bank, OWID, AQICN, NOAA, OPSD, Yahoo Finance). Re-ejecutar esos casos con datos reales. Declarar honestamente cuáles permanecen sintéticos. | Steven | 3–6 semanas |
| F17 | Validar QES contra criterios externos (GRADE, AMSTAR) o aceptar honestamente que es métrica interna del proyecto. Documentar la elección de pesos con justificación filosófica, no solo operativa. | Jacob (filosofía), Steven (implementación) | 2 semanas |

### 2.3 Contacto con interlocutores externos

| Fallo asociado | Acción | Quién | Tiempo |
|----------------|--------|-------|--------|
| F1, F2, F3, F5, F6, F9, F10 | Contactar 1–2 filósofos hostiles externos (humanista clásico) para revisión crítica de los fundamentos. | Steven o Jacob | 3–6 meses (depende del calendario del revisor) |
| F11–F22 | Contactar 1–2 estadísticos/físicos de complejidad para revisión crítica del aparato. | Steven | 3–6 meses |
| F23, F24, F26 | Coordinar con director de tesis y secretaría del Doctorado en Filosofía. | Steven | 2–4 semanas |

---

## 3. Tareas que solo la Universidad de Antioquia puede ejecutar

Tareas procedimentales que dependen de la estructura institucional y no pueden cerrarse desde el repositorio.

| Fallo | Acción | Quién en la institución | Tiempo |
|-------|--------|------------------------|--------|
| F23 | Designación formal del director de tesis con firma. | Comité del Doctorado en Filosofía + director | 2–4 semanas |
| F24 | Provisión de la plantilla institucional oficial para tesis doctoral (RES de la U. de Antioquia). | Secretaría del Doctorado | 1 semana |
| F25 | Requisitos formales de declaración de originalidad: formato y firma. | Secretaría del Doctorado | 1 semana |
| F26 | Política institucional sobre co-autoría con IA: la U. de Antioquia debe tener (o emitir) una política. Si no la hay, esto es zona gris que puede convertirse en problema en la sustentación. | Vicerrectoría de Investigación + Comité de Ética | 1–3 meses |
| (asociado a F23) | Designación de tribunal: mínimo 3 sinodales con perfil compatible (filósofo de la ciencia, físico/sistemas complejos, humanista). | Comité del Doctorado + director | 2–4 meses |
| (asociado a F25) | Aprobación del proyecto por Comité de Ética Institucional si el caso 30 (Behavioral Dynamics) avanza con datos VENLab humanos reales. | Comité de Ética | 3–6 meses |
| (asociado a F32) | Acceso a herramientas de diagramación profesional (TikZ, Graphviz licencia) si el programa lo provee, o presupuesto para diseñador editorial. | Programa de Doctorado o autor | Variable |

---

## 4. Mapa de prioridades

### Prioridad 1: bloqueadores de sustentación (próximas 2–6 semanas)

- F23 (director declarado) → Universidad + Steven
- F24, F25, F26 (portada, originalidad, conflicto de interés) → Universidad provee plantilla, Steven la ajusta
- F12 (aplicar FWER al corpus) → Asistencia técnica
- F18 (Q0 con gate de significancia) → Asistencia técnica
- F19 (resolver clasificación dual del caso 30) → Asistencia técnica
- F22 (reescribir lenguaje de pre-registro como auditoría) → Asistencia técnica
- F30 (consolidar 23 anexos en 7–8) → Asistencia técnica
- F31 (numerar tablas y figuras) → Asistencia técnica
- F34 (glosario completo) → Asistencia técnica

### Prioridad 2: bloqueadores de Q1 (próximos 2–4 meses)

- F11, F14 (calibración estadística honesta) → Asistencia técnica + revisor estadístico
- F13 (verificación inter-paradigma sobre arrays primarios) → Steven con apoyo computacional
- F15 (baselines competitivos: ARIMA, VAR, Kalman) → Asistencia técnica
- F16 (datos reales fetcheados verificables) → Steven con apoyo computacional
- F20 (corregir pseudo-replicación en paneles) → Asistencia técnica
- F33 (visualizaciones del corpus) → Asistencia técnica
- F32 (figuras Q1-quality) → Steven o asistencia técnica con TikZ

### Prioridad 3: cierre filosófico para defensa fuerte (próximos 4–12 meses)

- F1, F2, F3 (circularidad κ-ontológica, identidad-cuenca, salto inductivo) → Jacob
- F4, F5 (atractor topológico, refutación de alternativas filosóficas) → Steven + Jacob
- F6, F9, F10 (engagement real con interlocutores, asimetría L1↔B↔L3↔S, dimensiones omitidas) → Jacob
- F7, F8 (alinear inconsistencias normativa e información ecológica) → Asistencia técnica con guía de Jacob
- F17 (validar QES contra GRADE) → Jacob + Steven
- F27, F28, F29 (bibliografía depurada y consistente) → Asistencia técnica con revisión humana

### Prioridad 4: deuda externa post-defensa (6–24 meses)

- F23 con tribunal completo y revisión externa → Universidad + revisores hostiles
- F26 (política institucional sobre IA) → Universidad
- (asociado a F30) datos VENLab para caso 30 → Comité de Ética + laboratorio externo

---

## 5. Resumen ejecutivo

| Quién | Cuántos fallos puede cerrar directamente | Tiempo razonable |
|-------|------------------------------------------|------------------|
| Asistencia computacional (yo) | ~17 fallos (técnicos, formales, inconsistencias menores) | 2–4 semanas de trabajo focal |
| Steven o Jacob | ~13 fallos (filosóficos de fondo, decisiones metodológicas, contacto con revisores) | 4–6 meses con focalización |
| Universidad de Antioquia | ~6 fallos (portada institucional, director, tribunal, política IA, ética) | 1–6 meses con gestión activa |
| Solapamiento (varios responsables) | ~8 fallos requieren coordinación | — |

**Recomendación operativa:** atacar primero los 17 que puedo cerrar yo (Prioridades 1 y 2 en su parte técnica) en paralelo con la gestión institucional de F23–F26. Los fallos filosóficos de fondo (F1–F10) requieren intervención de Jacob y se atacan secuencialmente, con revisor humanista externo cuando esté disponible.

Esta división **NO es promesa de cierre**, sino diagnóstico de quién puede tocar qué. Cada fallo cerrado debe verificarse con criterio externo siempre que sea posible.
