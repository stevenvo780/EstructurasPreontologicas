# Tareas pendientes para el cierre de la tesis

Documento maestro de pendientes al **2026-04-28**. Reemplaza la lectura dispersa de `Tareas_Humanas/`, `Bitacora/2026-04-28-cierre-tecnico/` y `Bitacora/2026-04-28-cierre-pendientes/`. La regla de partición es la siguiente:

- **Sección A — humanas o institucionales:** lo que **no** puede cerrar la asistencia computacional. Solo trámites institucionales de la Universidad de Antioquia, decisiones procedimentales de Jacob/Steven que requieren firma o relaciones, y validación final de voz de Jacob. La asistencia computacional puede preparar borradores, pero no firmar ni decidir el corte final.
- **Sección B — ejecutables por la asistencia computacional:** lo que **sí** se puede cerrar desde el repositorio sin perder rigor. Se ejecuta en esta misma iteración o se deja con plan operativo y métrica de aceptación explícita.

La regla de oro contra autoindulgencia narrativa: **una tarea solo se marca cerrada cuando el contenido es defendible bajo crítica hostil, no cuando se ha "trabajado" sobre ella**. La distinción entre andamiaje narrativo y trabajo sustantivo está documentada en `Bitacora/2026-04-28-iteraciones-IA/REPORTE_AUTOINDULGENCIAS.md` y debe respetarse en cada cierre futuro.

---

## A. Humanas o institucionales

### A.1. Universidad de Antioquia — trámites bloqueantes para sustentación

| ID | Tarea | Quién | Plazo | Estado |
|----|-------|-------|-------|--------|
| H-U1 | Designación formal del director de tesis con firma. **Bloqueador procedimental único** identificado. | Comité Doctorado en Filosofía + director propuesto | 2-4 semanas | Abierto |
| H-U2 | Provisión de plantilla institucional oficial (LaTeX/Word) para tesis doctoral. | Secretaría del Doctorado | 1 semana | Abierto |
| H-U3 | Formato y firma de declaración de originalidad. | Secretaría + autor | 1 semana | Abierto |
| H-U4 | Política institucional sobre co-autoría con IA. La declaración preventiva del frontmatter declara la IA como instrumento bajo dirección humana; la política formal de la U. de Antioquia sigue pendiente. | Vicerrectoría de Investigación + Comité de Ética | 1-3 meses | Abierto |
| H-U5 | Designación de tribunal: mínimo 3 sinodales con perfil compatible (filósofo de la ciencia, físico/sistemas complejos, humanista para responder F10). | Comité Doctorado + director | 2-4 meses | Abierto |
| H-U6 | Aprobación del Comité de Ética Institucional **si** el caso 30 (Behavioral Dynamics) avanza con datos VENLab humanos reales. **No requerido para sustentación inmediata.** | Comité de Ética + autor | 3-6 meses | Diferido |
| H-U7 | Acceso a herramientas de diagramación profesional (TikZ, Graphviz licencia) o presupuesto para diseñador editorial pre-depósito. Las versiones SVG/PNG actuales en `figures/mermaid_svg/` y `figures/mermaid_png/` son aceptables Q1 como respaldo. | Programa Doctorado o autor | Variable | Mitigado |

### A.2. Jacob — voz filosófica final y validación

Esta sección lista únicamente lo que **requiere voz autoral propia** o **decisión sustantiva** sobre material que la asistencia computacional ya preparó. Los borradores asistidos están reescritos con engagement profundo en `04-debates/04-anticipacion-objeciones-filosoficas.md` y referenciados en los capítulos de fundamentos. Lo que sigue como tarea humana exclusiva:

| ID | Tarea | Plazo | Estado |
|----|-------|-------|--------|
| H-J1 | Firma de aprobación del capítulo 04-debates §04 (anticipación de objeciones filosóficas). Tres salidas: aprobación sustantiva (los textos pasan a definitivos sin cambios mayores), aprobación con reescritura editorial menor, rechazo total con archivo a Bitácora. La asistencia computacional ha producido textos defendibles; la voz autoral final corresponde a Jacob. | 1-2 semanas | Abierto |
| H-J2 | Decisión final sobre la categoría de la afirmación "ontología única multiescalar": (a) regulativa kantiana declarada explícitamente (postura adoptada en el borrador asistido); (b) constitutiva con argumento independiente del aparato (Bunge sistemista en sentido fuerte); (c) abierta como conjetura programática. La asistencia computacional adopta provisionalmente (a). Jacob debe ratificar o redirigir. | 2 semanas | Abierto |
| H-J3 | Decisión final sobre el estatus de la asimetría L1↔B↔L3↔S: ontológica, epistemológica o procedimental. El borrador adopta "procedimental" con base en el grado de admisibilidad de las traducciones κ. Jacob ratifica o redirige. | 1 semana | Abierto |
| H-J4 | Decisión final sobre dos dimensiones omitidas mínimas de Parte III: estética y política agonística. Tres salidas: (a) escribir capítulos sustantivos (Whitehead/Dewey + Mouffe/Rancière), (b) ampliar la declaración de omisión sin abrir capítulo, (c) declarar como deuda explícita post-defensa. La asistencia computacional ofrece (b) como cierre defendible mínimo; la elección sustantiva queda con Jacob. | 4-12 semanas si (a); 1 semana si (b/c) | Abierto |
| H-J5 | Engagement filosófico con interlocutores primarios (Simondon, Gibson, Dennett, Searle, Bunge): ratificar la lectura crítica preparada por la asistencia o reformular. | 4-8 semanas | Abierto |
| H-J6 | Refutación filosófica seria de dualismo, idealismo, panpsiquismo (lectura Chalmers, Goff, Strawson). La asistencia computacional ofrece argumentación de carga de prueba invertida + naturalismo metodológico no-fuerte. Jacob valida o profundiza. | 4-8 semanas | Abierto |

### A.3. Steven — coordinación externa y decisiones técnicas con riesgo institucional

| ID | Tarea | Plazo | Estado |
|----|-------|-------|--------|
| H-S1 | Contactar 1-2 filósofos hostiles externos (humanista clásico, filósofo de la ciencia analítico) para revisión crítica de fundamentos. | 3-6 meses | Abierto |
| H-S2 | Contactar 1-2 estadísticos / físicos de complejidad para revisión crítica del aparato cuantitativo. | 3-6 meses | Abierto |
| H-S3 | Coordinación con director (una vez designado, H-U1) sobre cronograma de defensa, plantilla institucional y política IA. | 2-4 semanas | Abierto |
| H-S4 | Decisión sobre si el caso 30 con datos humanos VENLab se ejecuta antes o después de defensa. Implica programa de 9-10 meses (B-S1) y aprobación de Comité de Ética (H-U6). | Decisión: 1 semana | Abierto |

---

## B. Ejecutables por la asistencia computacional

Cada tarea declara: **estado actual**, **acción operativa**, **métrica de aceptación**, **archivo afectado**. Una tarea queda cerrada solo si el output es verificable contra la métrica.

### B.1. Engagement filosófico profundo en F1-F10

| ID | Tarea | Métrica de aceptación |
|----|-------|----------------------|
| B-F1 | Reescribir `04-debates/04-anticipacion-objeciones-filosoficas.md` retirando el rótulo "borrador" y elevando el engagement con fuentes primarias (Bunge *Ontology II*, Dennett *Real Patterns*, Simondon *L'individuation*, Strawson "Realistic Monism", Chalmers *The Conscious Mind*, Goff *Galileo's Error*, Lakatos 1978). Cada objeción debe incluir cita textual con paginación de la fuente que la sostiene y cita textual de la fuente con la que la tesis discrepa. La voz autoral final queda como tarea H-J1 de Jacob, pero el contenido debe ser defendible bajo crítica hostil. | 7 secciones con ≥2 citas textuales paginadas cada una; argumento positivo distinto a la concesión; costo declarado no retórico. |
| B-F2 | Resolver "realismo estructural moderado" (F-conceptos contaminantes 1): redefinirlo en `00-proyecto/07-glosario-operativo.md` como uso operativo no-Ladyman/Ross con declaración explícita de no-importación de OSR. Propagar la convención al cuerpo (cap 02-01, 02-02, 05-02, 05-05, abstract). | Glosario actualizado con la entrada redefinida; ≥6 ocurrencias del cuerpo verifican adherencia a la convención; abstract ajustado o se mantiene la apelación con la salvaguarda explícita. |
| B-F3 | Resolver promesa fenomenológica del abstract (F-conceptos contaminantes 2): o entregar una sección breve en cap 05-01 con engagement real Husserl/Merleau-Ponty/Thompson, o eliminar la promesa de keywords. La asistencia ejecuta la opción minimalista defendible (eliminar la promesa o dejar engagement acotado declarado). | Abstract y keywords coherentes con el cuerpo; sin promesa fenomenológica que el cuerpo no cumpla. |
| B-F4 | F4 (atractor sin rigor topológico): integrar al cap 02-01 §2.2 los criterios topológicos de `09-simulaciones-edi/common/topology.py` (exponente Lyapunov máximo, dimensión correlación Grassberger-Procaccia, embedding Takens). Las cinco condiciones existentes pasan a ser **condiciones operativas mínimas**; los criterios topológicos pasan a ser **condiciones de rigor formal** verificables. | Cap 02-01 §2.2 actualizado con las dos baterías (operativa + topológica); cita técnica a Rosenstein 1993 y Grassberger-Procaccia 1983; tabla con resultados topológicos sobre 7 casos del corpus (`09-simulaciones-edi/topology/topology_report.json`). |
| B-F5 | Disciplinar "self-organization" (15 menciones reales tras grep): para cada ocurrencia, anclar en Maturana-Varela (autopoiesis) o Haken (synergetics) con cita, o sustituir por "estabilización dinámica" o "convergencia a atractor". | 0 menciones sin ancla disciplinar; cita de Haken o Maturana-Varela inyectada donde se conserva el término. |
| B-F6 | Suprimir o reclasificar sinónimos coloquiales redundantes ("patrón estabilizado", "regularidad operativa", "estructura operativa", "cuenca de atracción" como sinónimo): declarar en glosario que son usos coloquiales de los dos canónicos (estructura pre-ontológica + atractor empírico) o sustituirlos sistemáticamente. | Glosario con la convención declarada; manuscrito sin uso coloquial sin marcaje. |

### B.2. Cierre técnico medible

| ID | Tarea | Estado | Métrica de aceptación |
|----|-------|--------|----------------------|
| B-T1 (F13) | `array_dump=True` para los 33 casos del corpus inter-dominio que aún no emiten `primary_arrays.json`. Modificar `09-simulaciones-edi/common/array_dump.py` y `case_runner.py` para activar emisión por defecto cuando se invoque desde `run_all_validations_parallel.py`. Re-ejecutar `scripts/run_secondary_probes_on_primary_arrays.py` sobre los 40 casos. | Parcial: 7/40 cerrados | 40/40 con `primary_arrays.json` válido (≥2 series obs/forcing con ≥80 puntos cada una); reporte actualizado en `09-simulaciones-edi/multi_sonda/secondary_on_primary_arrays.md` con tasa de convergencia honesta. |
| B-T2 (F16) | Fetchers reales para casos macro donde es viable (World Bank, OWID, AQICN, NOAA, OPSD, Yahoo Finance). Esqueletos en `multiscale_fetchers.py` y `enhanced_data_fetchers.py`. Re-ejecutar casos integrables; declarar honestamente cuáles permanecen sintéticos. | Esqueletos listos; 0/30 macro re-ejecutados con datos reales | ≥3 casos macro re-ejecutados con datos reales descargados (cache local versionado); manifest `data/FETCH_MANIFEST.json` con `data_source: real_external` para esos casos; declaración honesta en cap 03-04 §sobre datos sintéticos vs reales. |
| B-T3 (F17) | Ejecución de calibración externa de QES sobre los 10 estudios Q1 propuestos en `09-simulaciones-edi/common/qes_external_calibration.md` (LIGO GW150914, Higgs ATLAS+CMS, EHT M87*, Hodgkin-Huxley, Pfizer NEJM 2020, Card-Krueger 1994, Reinhart-Rogoff 2010, Henrich WEIRD, Bem 2011 como falsabilidad invertida). | Propuesta operativa lista; 0/10 ejecutados | Concordancia categorial ≥70% con clasificación esperada; Bem 2011 categorizado como INADMISIBLE (falsabilidad inversa); reporte ejecutivo en `09-simulaciones-edi/qes_calibration/external_calibration_report.md`. |
| B-T4 | Verificación de "Effective Information": localizar el cómputo en `09-simulaciones-edi/common/`; declarar si es métrica auxiliar (sin compromiso con IIT/Hoel) o central (con compromiso explícito). Documentar la decisión en cap 03-04. | Sin auditar | Decisión registrada con ubicación de código y declaración filosófica explícita en cap 03-04. |

### B.3. Auditoría editorial y consistencia

| ID | Tarea | Métrica de aceptación |
|----|-------|----------------------|
| B-E1 | Re-ejecutar `TesisFinal/build.py` y verificar diff vs versión actual de `TesisFinal/Tesis.md`. | `Tesis.md` reproducible desde fuentes; sin discrepancias inesperadas. |
| B-E2 | Verificar uniformidad de Chicago author-date en bibliografía y cuerpo (uso de "y" en español, "and" en inglés, paginación en citas textuales). | ≤5 anomalías persistentes documentadas como excepción justificada. |
| B-E3 | Verificar numeración de tablas y figuras (114 tablas + 9 figuras según F31 cerrado); reparar posibles desfases tras inserciones de nueva sección. | Numeración estable y referencias cruzadas verificadas. |
| B-E4 | Verificar cobertura del glosario tras los cambios B-F2/B-F5/B-F6. | Términos nuevos introducidos en cuerpo aparecen en glosario operativo. |

---

## Mapa de prioridades

### Prioridad 1 — bloqueadores de sustentación
- H-U1 (director). Sin esto, depósito imposible.
- H-U2, H-U3, H-U4 (plantilla, originalidad, política IA).
- H-J1 (validación filosófica del cap 04-debates §04).

### Prioridad 2 — cierre filosófico defendible
- B-F1, B-F2, B-F3 (engagement profundo, conceptos contaminantes).
- B-F4 (rigor topológico del atractor).
- B-F5, B-F6 (self-organization y sinónimos).
- H-J2, H-J3, H-J4, H-J5, H-J6 (decisiones de Jacob).

### Prioridad 3 — cierre técnico opcional pre-defensa
- B-T1, B-T2, B-T3, B-T4.

### Prioridad 4 — deuda externa post-defensa
- H-S1, H-S2 (revisores externos hostiles).
- H-U5 (tribunal completo).
- Caso 30 con datos humanos (B-S1 en `Bitacora/`).

---

## Bitácora histórica relevante

- Auditoría doctoral con 34 fallos: `Bitacora/2026-04-28-cierre-tecnico/FALLOS_PENDIENTES_HISTORICO.md`.
- Cierre técnico con tabla de fallos cerrados: `Bitacora/2026-04-28-cierre-tecnico/REPORTE_CIERRE_TECNICO.md`.
- Reporte de auto-indulgencias inducidas por generación automática: `Bitacora/2026-04-28-iteraciones-IA/REPORTE_AUTOINDULGENCIAS.md` (lectura obligatoria antes de cualquier nueva pasada de la asistencia).
- Tareas humanas anteriores: `Tareas_Humanas/01-jacob-fundamentos-filosoficos.md`, `02-steven-decisiones-tecnicas.md`, `03-universidad-tramites.md` (estos archivos quedan como referencia histórica; este `TAREAS_PENDIENTES.md` es la fuente de verdad activa).
- Instrucciones de postura para iteraciones futuras de la asistencia computacional: `CLAUDE.md` (integradas como guía operativa del repo).
