# Auditoría doctoral del manuscrito

> Documento de evaluación honesta de lo que separa al manuscrito actual de una tesis doctoral integral defendible ante el comité de la **Universidad de Antioquia**. No es crítica retórica: es identificación de los huecos reales que un comité de evaluación encontraría y que deben cerrarse para superar la auditoría académica.

**Manuscrito evaluado:** *Estructuras Pre-Ontológicas: Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio*. Versión 2026-04-27. Autoría: Jacob Agudelo (concepto y dirección, U. Antioquia) + Steven Vallejo Ortiz (técnica e ingeniería). Ensamblado: `TesisFinal/Tesis.md` (~7,200 líneas, ~430 KB).

**Política de la auditoría:** Cada hueco se reporta con (a) descripción del problema, (b) evidencia en el manuscrito o ausencia de ella, (c) por qué un comité doctoral lo señalaría, (d) qué hace falta producir, (e) prioridad estimada para defensa.

**Niveles de prioridad:**

- **Bloqueante** — sin esto, el comité no aprobará la tesis.
- **Alta** — esto se preguntará en defensa y debe estar resuelto.
- **Media** — esperable en versión final, no bloqueante.
- **Baja** — pulido editorial.

---

## Resumen ejecutivo

El manuscrito tiene **arquitectura argumental sólida**, **aparato empírico funcional con resultados verificables (corpus EDI de 30 casos)**, **discriminación pública contra rivales identificables**, y **trazabilidad de proceso documentada**. Es defendible como **prototipo doctoral avanzado**.

Lo que falta para tesis integral en U. Antioquia se concentra en **diez bloques** ordenados por prioridad:

| # | Bloque | Prioridad | Esfuerzo estimado |
|---|--------|-----------|-------------------|
| 1 | Filiación institucional, comité de tesis y aprobación de protocolo | Bloqueante | trámite |
| 2 | Diálogo bibliográfico real (no asignación de interlocutores) | Alta | 2–3 meses |
| 3 | Capítulo de revisión de literatura sustantivo | Alta | 1–2 meses |
| 4 | Datos humanos reales para caso 30 (elevación a LoE 4) | Alta | 6–12 meses |
| 5 | Programa multi-sonda en al menos 3 casos strong | Alta | 4–6 meses |
| 6 | Comparación con baselines estadísticos (ARIMA, VAR) | Alta | 1–2 meses |
| 7 | Operacionalización de la dimensión normativa | Media | 6–12 meses |
| 8 | Capítulo metodológico con ética de investigación y datos | Media | 3 semanas |
| 9 | Integración formal de citas en cada capítulo | Media | 1–2 meses |
| 10 | Pulido editorial, normas APA/Chicago institucional | Baja | 3 semanas |

El cierre integral exige aproximadamente **12–18 meses adicionales** de trabajo dedicado, asumiendo que el comité quede satisfecho con el alcance regional declarado y la deuda residual nombrada.

---

## 1. Filiación institucional y formalización académica

### Problema

El manuscrito se autodescribe como tesis doctoral en filosofía de la ciencia y ciencias de la complejidad de la U. Antioquia, pero no hay constancia formal en el repositorio de:

- programa doctoral específico (¿filosofía? ¿epistemología? ¿interdisciplinario?);
- director(es) de tesis institucional(es) avalados por el programa;
- comité de evaluación designado;
- aprobación del protocolo de investigación por el comité de ética / facultad;
- avance académico oficial (créditos, exámenes de candidatura, seminarios cumplidos);
- carta de aval del director para depósito.

### Por qué un comité lo señalaría

Una tesis doctoral en Colombia (acuerdos académicos U. Antioquia) requiere registro en SIIU, aprobación de proyecto por el Consejo de Facultad o comité doctoral, asesor formalmente asignado, y cumplimiento del Reglamento Estudiantil de Posgrado. Sin documentación, el manuscrito no puede ser sometido a sustentación pública.

### Qué falta producir

- carpeta `00-proyecto/04-formalizacion-institucional.md` con: programa académico, director y co-director, comité de tesis con sus filiaciones, fecha de aprobación del proyecto, número de radicado.
- copia del acta de aprobación del proyecto por el Consejo de Facultad.
- carta de aprobación de protocolo de ética si los datos involucran sujetos humanos (caso 30 elevado a datos reales lo exigirá).
- declaración de propiedad intelectual y de coautoría con IA según política institucional.

### Prioridad

**Bloqueante**. Sin esto, no hay tesis defendible.

---

## 2. Diálogo bibliográfico real

### Problema

El Anexo A bibliográfico lista 90 referencias y asigna interlocutores principales por capítulo. Pero la asignación es nominal: en el cuerpo de los capítulos las citas a estos autores son escasas y mayoritariamente parafrásticas. No hay diálogo textual sostenido — análisis de pasajes específicos, contraste de formulaciones, respuesta a argumentos puntuales.

### Evidencia

Los capítulos 02 (fundamentos), 03 (formalización) y 04 (debates) tienen en promedio **3–5 menciones bibliográficas por capítulo**, casi todas en formato `(Autor, año)` sin cita textual ni paginación. Capítulos 02-04 (nivel B) cita a Warren, Gibson, Maturana-Varela sin extraer sus argumentos. El capítulo de debates trata 14 rivales pero sólo desarrolla en profundidad la confrontación con modelos internos (5 celdas). Wolfram, mecanicismo multinivel y enactivismo radical reciben tratamiento más superficial.

### Por qué un comité lo señalaría

Una tesis doctoral en filosofía exige diálogo sustantivo con la tradición. La mera asignación de interlocutores no demuestra lectura crítica. El comité preguntará en defensa: *¿qué dice exactamente Bunge en el §X de la *Treatise* sobre sistemismo? ¿en qué se diferencia tu posición de la de Ladyman y Ross §6.3? ¿citas a Hoel 2017 pero qué te pareció su crítica a IIT?*. Sin diálogo textual, esas preguntas se contestan vagamente.

### Qué falta producir

- en cada capítulo de fundamentos y debates, **3 pasajes textuales** del interlocutor principal con cita exacta (autor, año, página) y respuesta argumental de la tesis;
- en el capítulo 04-01, expansión de las confrontaciones con Wolfram (al menos 2 referencias específicas a *A New Kind of Science* y al *Wolfram Physics Project*), Bechtel-Craver (capítulos específicos de *Mental Mechanisms*), y enactivismo (al menos un pasaje de *The Embodied Mind*);
- en el capítulo 02-04, citas extensas de Warren (2006) y Gibson (1979/1986) que el manuscrito ya invoca conceptualmente pero no textualmente.

### Prioridad

**Alta**. Esto es lo que distingue una tesis filosófica de un compendio organizado.

---

## 3. Capítulo de revisión de literatura sustantivo

### Problema

El manuscrito carece de un capítulo dedicado a **estado del arte / revisión de literatura**. La discusión de rivales (capítulo 04-01) no la sustituye: confrontación contra rivales no es lo mismo que mapear el campo donde la tesis interviene.

### Por qué un comité lo señalaría

En cualquier programa doctoral colombiano, el capítulo de revisión es estructural. Define el campo, documenta la deuda histórica de la tesis con la tradición, y demuestra dominio del estado del arte. Sin él, la tesis parece flotar en sus propias afirmaciones.

### Qué falta producir

Un capítulo nuevo (sugerencia: `01-diagnostico/03-estado-del-arte.md`) que cubra:

- **subcampo 1:** filosofía de la mente postcognitivista (enactivismo, embodied, extended mind, ecological psychology) con periodización 1991–presente;
- **subcampo 2:** ontología social y del cierre operativo (Bunge, Searle, Bourdieu, Latour, Gilbert);
- **subcampo 3:** filosofía de la complejidad y emergencia computacional (Hoel, Tononi, Seth, Rosas, Klein, Wolfram);
- **subcampo 4:** behavioral dynamics y dinámica de sistemas no lineales (Kelso, Haken, Strogatz, Warren, Fajen, Sternad);
- **subcampo 5:** filosofía latinoamericana de la ciencia (Bunge, Hoyos, Salas), por filiación institucional U. Antioquia;
- **mapa de huecos:** dónde se inserta la tesis en cada subcampo, qué afirmación específica añade, contra quién discrimina.

### Prioridad

**Alta**.

---

## 4. Datos humanos reales para el caso 30

### Problema

El caso 30 (behavioral dynamics) está clasificado como **LoE = 2** porque usa datos sintéticos generados con la ecuación completa de Fajen-Warren. El manuscrito reconoce honestamente que la elevación a LoE = 4 requiere datos humanos reales. Pero deja la elevación como deuda residual.

### Por qué un comité lo señalaría

El comité preguntará: *¿por qué declaras que el caso 30 demuestra cierre operativo significativo si los datos son sintéticos derivados de la teoría que pruebas?* La respuesta actual del manuscrito (los datos provienen del sistema completo, la sonda EDI es la simplificada, no hay circularidad) es defendible pero perfectible. La defensa convencional exige al menos **una prueba sobre datos humanos reales**, aunque sea pequeña.

### Qué falta producir

- adquirir datasets públicos de captura de movimiento humano en tareas de locomoción dirigida (candidatos: VENLab Brown, WALK-MS Boston, OpenLocomotionData, MoCap CMU);
- adaptar el pipeline EDI a la frecuencia temporal de los datos (típicamente 60–120 Hz);
- re-ejecutar el caso 30 con datos reales y reportar EDI nuevo;
- comparar EDI sintético vs EDI real;
- si EDI real ≥ 0.30 con `overall_pass=True`, elevar el caso a Nivel 4 strong;
- si EDI real es comparable al sintético (~0.26), defender la robustez de la conjetura;
- si EDI real es significativamente menor o no significativo, reportar honestamente y discutir las implicaciones.

### Prioridad

**Alta**. Decisión estratégica: si no se logra en plazo razonable, el caso 30 debe quedar explícitamente rebajado a programático en el manuscrito final, no demostrativo.

---

## 5. Programa multi-sonda en al menos 3 casos strong

### Problema

Cada caso del corpus EDI usa **una sola sonda ODE**. La dependencia instrumento-fenómeno se reconoce como condición epistémica honesta, pero el manuscrito no demuestra que el resultado **converge bajo sondas alternativas**.

### Por qué un comité lo señalaría

El comité dirá: *si Energía con Lotka-Volterra da EDI=0.65, ¿qué da con un modelo de balance termodinámico simple? ¿con un AR(1) económico? ¿son convergentes los resultados?*. Sin programa multi-sonda, la objeción de **"el aparato detecta lo que la sonda permite ver"** queda abierta.

### Qué falta producir

Para los **3 casos strong principales** (Energía, Deforestación, Riesgo Biológico):

- implementar al menos una sonda ODE alternativa con motivación teórica distinta;
- re-ejecutar el caso bajo la sonda alternativa;
- reportar tabla de convergencia: ¿el EDI se mantiene en el mismo nivel taxonómico? ¿el `overall_pass` se preserva?;
- discutir interpretación: si convergen, fortalece; si divergen, identifica qué aspecto del fenómeno captura cada sonda.

### Prioridad

**Alta**. Es la única forma de neutralizar la objeción "el resultado depende del instrumento".

---

## 6. Comparación con baselines estadísticos puros

### Problema

El baseline del corpus EDI es **ABM sin ODE con forcing exógeno mantenido**. No se compara contra **modelos puramente estadísticos** (ARIMA, VAR, modelos bayesianos no estructurados). Esta es una limitación que el manuscrito reconoce explícitamente como deuda.

### Por qué un comité lo señalaría

El comité preguntará: *si un ARIMA simple sobre las mismas series predice tan bien como tu ABM+ODE con `overall_pass=True`, ¿qué añade tu marco?*. La respuesta del manuscrito (el marco no busca solo predicción, sino discriminación de cierre operativo bajo intervención) es buena, pero exige **prueba comparativa explícita**.

### Qué falta producir

Para los 5 casos strong y los 3 controles de falsación:

- ajustar ARIMA(p,d,q) o VAR según corresponda;
- reportar RMSE de validación;
- comparar contra RMSE_coupled del ABM+ODE;
- discutir: ¿hay caso donde ARIMA gana? ¿en qué casos el marco aporta algo que ARIMA no?;
- documentar la conclusión en un sub-anexo del capítulo 09 o como apéndice del corpus.

### Prioridad

**Alta**. El comité preguntará esto explícitamente.

---

## 7. Operacionalización de la dimensión normativa

### Problema

Los capítulos 05-04 (instituciones, mercado, Estado) y 02-03 (categorías) reconocen que la dimensión normativa (validez, legitimidad, efectividad de normas) requiere desarrollo formal pendiente. El manuscrito conjetura que validez = cuenca de atracción del cumplimiento, efectividad = tasa de retorno, legitimidad = anchura de la cuenca. Pero no hay operacionalización empírica de esto en ningún caso.

### Por qué un comité lo señalaría

Si la tesis aspira a ser ontología y epistemología generales, la dimensión normativa no puede quedar en conjetura. Bourdieu, Searle y Latour son interlocutores principales del capítulo 05-04 y exigen confrontación operativa.

### Qué falta producir

Una de tres rutas:

- **Ruta A (mínima):** declarar explícitamente que la dimensión normativa queda fuera del alcance demostrativo de esta tesis y se trata sólo conceptualmente; mover el capítulo 05-04 a modo programático sin ambigüedad.
- **Ruta B (media):** construir un caso operativo acotado: por ejemplo, dinámica de adopción de medidas COVID-19 por estados como cuenca de atracción institucional bajo perturbación. Datos disponibles, sonda construible.
- **Ruta C (ambiciosa):** desarrollar capítulo metodológico sobre **EDI normativo** con formalización propia y al menos un caso construible.

### Prioridad

**Media**. Si el alcance se acota explícitamente (Ruta A), no es bloqueante.

---

## 8. Capítulo metodológico de ética de investigación y gobernanza de datos

### Problema

El manuscrito no incluye un capítulo metodológico que cubra:

- protocolo de manejo de datos en cada caso del corpus;
- consideraciones éticas específicas (caso 30 con datos humanos exige consentimiento informado del dataset original; casos institucionales pueden involucrar datos sensibles);
- gobernanza de datos abiertos vs. propietarios;
- política de reproducibilidad y disponibilidad de código y datos;
- aspectos éticos de la co-autoría con IA: cómo se declaró, qué decisiones humanas la limitaron, qué política institucional aplica.

### Por qué un comité lo señalaría

Las tesis doctorales en U. Antioquia exigen aval del Comité de Ética cuando hay sujetos humanos. Aún sin sujetos directos, exigen capítulo metodológico. Y la co-autoría con IA es un punto sensible que la institución empieza a regular formalmente (2024–2026).

### Qué falta producir

Capítulo nuevo (sugerencia: `03-formalizacion/05-etica-y-gobernanza-de-datos.md`):

- política por caso del corpus;
- consideraciones éticas y aval de comité (si aplica);
- declaración de co-autoría con IA según marco institucional vigente;
- compromiso público de disponibilidad de código (`09-simulaciones-edi/` ya en repositorio) y datos cacheables;
- limitaciones de los datos públicos usados (World Bank, OWID, etc.) y su trazabilidad.

### Prioridad

**Media**. Se puede redactar en 3 semanas.

---

## 9. Integración formal de citas en cada capítulo

### Problema

Las citas a la bibliografía formal del Anexo A son escasas en los capítulos del cuerpo argumental. La asignación de interlocutores por capítulo (en el Anexo de bibliografía) no se ha vertido en cada capítulo como diálogo activo.

### Por qué un comité lo señalaría

Las normas APA / Chicago exigen que cada afirmación sustantiva tenga su referencia. Hoy hay capítulos enteros sin una sola cita formal. El comité hará la pregunta: *¿en qué texto de Bunge se basa esta afirmación?*.

### Qué falta producir

- inyectar citas formales (autor, año, página cuando proceda) en cada capítulo, sustituyendo las paráfrasis;
- estilo unificado: Chicago author-date para todo el manuscrito (ya elegido en el Anexo bibliográfico);
- bibliografía consolidada al final de `TesisFinal/Tesis.md` con todas las referencias citadas en el cuerpo.

### Prioridad

**Media**. Trabajo continuo durante la redacción final.

---

## 10. Pulido editorial y cumplimiento normativo institucional

### Problema

El manuscrito está en formato Markdown sin las exigencias de presentación de la U. Antioquia:

- portada institucional según plantilla oficial;
- agradecimientos;
- dedicatoria (opcional pero esperada);
- listado de figuras y tablas;
- listado de abreviaturas y símbolos;
- numeración de capítulos según convención;
- normas tipográficas institucionales (espaciado, márgenes, fuentes);
- versión PDF compilada con LaTeX o Word según exigencia del programa.

### Por qué un comité lo señalaría

Es trámite, pero sin él el documento no entra a sustentación.

### Qué falta producir

- plantilla institucional de la U. Antioquia obtenida del programa doctoral;
- conversión Markdown → LaTeX/Word según exigencia (Pandoc lo facilita);
- generación de listados automáticos (figuras, tablas, abreviaturas);
- revisión editorial profesional (si presupuesto lo permite).

### Prioridad

**Baja**. Trabajo de las últimas 3 semanas antes de depósito.

---

## Otros puntos menores que conviene atender

### A. Cobertura de figuras y diagramas

El manuscrito menciona figuras (mapas de operadores, diagramas de flujo) pero las representa solo en ASCII art. Una tesis doctoral suele incluir figuras formales. Recomendación: convertir los diagramas ASCII a SVG/PNG con herramientas (mermaid ya está en el manuscrito previo, pero no se renderiza en PDF). Prioridad media.

### B. Anexo de tablas crudas de outputs

Los `metrics.json` por caso son la fuente de verdad. Conviene producir un anexo tabular consolidado (`Anexos/A8-resultados-corpus.md` o similar) con las cifras exactas verificadas por el comité, no sólo distribución por nivel. Prioridad media.

### C. Capa ST (`08-consistencia-st/`)

Existe una capa de validación lógica con ST que el manuscrito menciona pero no integra activamente en los capítulos. Decidir: o se elimina del manuscrito (queda como herramienta interna de control), o se desarrolla un sub-capítulo que la presente al lector con resultados de cobertura. Prioridad media-baja.

### D. Glosario operativo del Anexo A.1

El glosario es bueno, pero no aparece referenciado activamente en el cuerpo del manuscrito. Conviene introducir referencias cruzadas en los capítulos donde se introduce cada término (por ejemplo, primera mención de κ debe tener "(ver Glosario A.1)"). Prioridad baja.

### E. Nomenclatura de niveles

El paisaje de emergencia tiene 6 niveles (0–5), pero la tesis sólo demuestra hasta Nivel 4. La cláusula "Nivel 5 = programa futuro" debe reforzarse en cada lugar donde aparece para no dar la impresión de promesa no cumplida. Prioridad baja.

### F. Convergencia con Wolfram como trabajo futuro

El capítulo 04-01 propone aplicar EDI a fenómenos derivados de hypergraph rewriting de Wolfram como trabajo futuro. Esto es una propuesta concreta pero no desarrollada. Si se va a presentar, conviene producir al menos un esquema de cómo se haría, qué dataset experimental se usaría, qué predicción se buscaría. Prioridad baja.

### G. Tono y voz del manuscrito

El manuscrito alterna entre voz académica formal y voz más ensayística (especialmente en cierres de capítulo y conclusiones). La voz ensayística es legítima pero conviene revisarla para asegurar que no introduce afirmaciones sin sustento. Prioridad baja.

### H. Tareas/ y backlog del proyecto

La carpeta `Tareas/` contiene mega-tareas estratégicas (programa científico general, traducción de obras, benchmark de rivales, etc.) que son trabajo posterior al manuscrito. Conviene mover esa carpeta a `Procesos/Tareas/` o renombrarla a `Backlog/` para que no se confunda con material del manuscrito final. Prioridad baja.

---

## Cuadro síntesis de huecos por capítulo

| Capítulo | Huecos detectados | Prioridad |
|----------|-------------------|-----------|
| Front matter | Falta filiación institucional formal (ver §1) | Bloqueante |
| 00-proyecto | Falta capítulo de protocolo institucional aprobado | Bloqueante |
| 01-diagnostico | Falta capítulo de revisión de literatura (ver §3) | Alta |
| 02-fundamentos | Faltan citas textuales sostenidas con interlocutores (ver §2) | Alta |
| 03-formalizacion | Falta capítulo de ética y gobernanza de datos (ver §8) | Media |
| 04-debates | Confrontación con Wolfram, Bechtel-Craver, enactivismo está superficial (ver §2) | Alta |
| 05-aplicaciones | Caso 30 necesita datos humanos reales (ver §4); caso 05-04 (instituciones) necesita decisión de alcance (ver §7) | Alta |
| 06-cierre | Coherente, pero conviene actualizar conclusión con resultados de §4–§6 cuando se completen | Media |
| 07-bibliografia | Citas formales no integradas al cuerpo (ver §9) | Media |
| 09-simulaciones-edi | Falta multi-sonda (ver §5) y baselines estadísticos (ver §6) | Alta |
| Anexos | Convertir ASCII art a figuras formales; añadir A.8 tablas crudas | Media |

---

## Plan de cierre auditable

Si la dirección del proyecto acepta esta auditoría, la trayectoria mínima de cierre es:

**Mes 0 (presente)** — manuscrito en este estado.

**Mes 1–2** — capítulo de revisión de literatura; integración de citas; capítulo metodológico ético.

**Mes 3–4** — programa multi-sonda en 3 casos strong; comparación con baselines estadísticos.

**Mes 5–10** — adquisición e integración de datos humanos reales para caso 30; re-ejecución y reporte.

**Mes 11–12** — pulido editorial; conversión LaTeX; portada institucional; depósito.

**Mes 12+** — sustentación pública.

Esto asume **dedicación parcial** y **disponibilidad de datasets**. En condiciones de dedicación completa con acceso prioritario a recursos, el ciclo se reduce a 6–9 meses.

---

## Conclusión de la auditoría

El manuscrito **no necesita ser reformulado**. Necesita ser **completado** en los diez bloques anteriores. La arquitectura argumental, el aparato empírico, la posición filosófica y el corpus EDI están en estado **suficiente para sostener una defensa exigente**. Lo que falta es:

1. **Trámite institucional** (bloqueante).
2. **Diálogo bibliográfico real** (alta).
3. **Datos humanos para caso 30 + multi-sonda + baselines estadísticos** (alta).
4. **Capítulos auxiliares** (revisión de literatura, ética de datos) (media).
5. **Pulido editorial** (baja).

Una tesis doctoral en U. Antioquia con esta línea de cierre es **defendible en 12–18 meses**. La señal positiva es que el manuscrito ya tiene los elementos no replicables (concepto, aparato, demostración empírica multidominio); lo que queda es trabajo metodológico, bibliográfico y administrativo, todo ejecutable.

> *Una tesis se aprueba cuando el comité no encuentra preguntas que el manuscrito no anticipe. Esta auditoría es el listado de las preguntas que aún no anticipa con suficiente cuidado.*

---

**Auditor metodológico:** preparado por la asistencia IA bajo dirección humana.
**Fecha:** 2026-04-27.
**Para discusión con:** comité doctoral, director de tesis, y autores.
