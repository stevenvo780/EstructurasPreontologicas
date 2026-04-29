# Tareas humanas pendientes

Tareas que **NO pueden cerrarse desde el repositorio**. Requieren decisión filosófica de Jacob, ejecución técnica con criterio humano de Steven, o trámite institucional de la Universidad de Antioquia.

> **Estado al 2026-04-28:** todos los fallos atendibles por la asistencia computacional están cerrados; la auditoría histórica completa está archivada en `Bitacora/2026-04-28-cierre-tecnico/`. Aquí solo permanece lo que requiere intervención humana.

---

## 1. Jacob — fundamentos filosóficos

Decisiones de fondo del marco. Cada una requiere lectura sustantiva y escritura argumentativa, no edición técnica.

### `01-jacob-fundamentos-filosoficos.md`

| Tarea | Origen | Tiempo estimado |
|-------|--------|-----------------|
| **Reformular distinción κ-pragmática / κ-ontológica con criterios externos no operativos** (compromiso con realismo de Ladyman-Ross, criterios de invariancia bajo cambio de modelo, predicción ex-ante). | F1 | 2-4 semanas |
| **Reformular teoría de identidad sin caer en circularidad**: o adoptar criterio externo (Locke, Parfit, Strawson), o reconocer que la "cuenca persistente" es metáfora. | F2 | 1-2 semanas |
| **Aceptar que la "ontología única multiescalar" es conjetura, no demostración**. Reescribir cap 02-01 §1 como "programa de unificación ontológica" con condiciones de fracaso explícitas; o defenderla con argumento independiente del aparato (Bunge sistémico riguroso). | F3 | 3-4 semanas |
| **Refutación filosófica seria de dualismo, idealismo, panpsiquismo**. Lectura de Chalmers, Goff, Strawson. Sin esto, el naturalismo es petición de principio. | F5 | 4-8 semanas |
| **Profundizar diálogo con Simondon, Gibson, Dennett, Searle, Bunge**: para cada uno, leer obra primaria, identificar la objeción real al programa, responder con argumento. | F6 | 8-16 semanas |
| **Decidir si la asimetría L1↔B↔L3↔S es ontológica, epistemológica o terminológica**. Reescribir cap 02-04 §8 con la decisión. | F9 | 2-3 semanas |
| **Incluir tratamiento de al menos dos dimensiones omitidas**: estética y política. Mereología, género y descolonialidad pueden quedar como deuda explícita. | F10 | 6-12 semanas |
| **Validar borradores filosóficos del Anexo A.13** (anticipación de objeciones): aceptar/reescribir/rechazar las 7 secciones. Si Jacob aprueba, las secciones se promueven a `04-debates/03-anticipacion-objeciones.md`. | A.13 | 1-2 semanas |
| **Decidir destino de "realismo estructural moderado"**: redefinir como uso operativo no-Ladyman, o reemplazar por "anti-reificación operativa con compromiso estructural local". | conceptos contaminantes | 1 semana |
| **Resolver promesa fenomenológica del abstract**: o entregar engagement real (Husserl, Merleau-Ponty, Thompson) en cap 05-01, o eliminar la promesa de A.7. | conceptos contaminantes | 2-3 semanas |

---

## 2. Steven — decisiones técnicas con criterio humano

### `02-steven-decisiones-tecnicas.md`

| Tarea | Origen | Tiempo estimado |
|-------|--------|-----------------|
| **Decidir si se modifica `edi_engine.py` para emitir arrays primarios y se re-ejecuta el corpus completo** (≈3 semanas). Hoy solo 7/40 casos tienen `primary_arrays.json`. Cierra completamente F13. | F13 | 3 semanas si se ejecuta |
| **Implementar fetch real desde fuentes públicas** (World Bank, OWID, AQICN, NOAA, OPSD, Yahoo Finance) para casos del corpus inter-dominio. Re-ejecutar con datos reales. Declarar honestamente cuáles permanecen sintéticos. Esqueletos ya provistos en `09-simulaciones-edi/multiscale_fetchers.py` y `enhanced_data_fetchers.py`. | F16 | 3-6 semanas |
| **Ejecutar la calibración externa de QES** sobre los 10 estudios Q1 propuestos en `09-simulaciones-edi/common/qes_external_calibration.md` (LIGO, Higgs, EHT, Hodgkin-Huxley, Pfizer, Card-Krueger, Reinhart-Rogoff, Henrich, Bem). Métrica de aceptación: concordancia categorial ≥ 70%. | F17 | 3-5 sesiones focales |
| **Verificar que "Effective Information" (EI) en métricas no implica compromiso oculto con IIT/Hoel**. Si es métrica auxiliar, declarar uso operativo. Si es central, declarar el compromiso. | conceptos contaminantes | 1 sesión |
| **Disciplinar uso de "self-organization"** (21 menciones): o anclar bajo Maturana-Varela, o sustituir por "estabilización dinámica". | conceptos contaminantes | 1-2 sesiones |
| **Suprimir o declarar equivalencia** entre los sinónimos "patrón estabilizado", "regularidad operativa", "estructura operativa" (los tres redundan con "estructura pre-ontológica" + "atractor empírico"). | conceptos contaminantes | 1 sesión |

### `03-steven-coordinacion-externa.md`

| Tarea | Origen | Tiempo estimado |
|-------|--------|-----------------|
| **Contactar 1-2 filósofos hostiles externos** (humanista clásico) para revisión crítica de los fundamentos (F1, F2, F3, F5, F6, F9, F10). | F1-F10 | 3-6 meses |
| **Contactar 1-2 estadísticos / físicos de complejidad** para revisión crítica del aparato (F11-F22). | F11-F22 | 3-6 meses |
| **Coordinar con director de tesis y secretaría del Doctorado en Filosofía**. | F23, F24, F26 | 2-4 semanas |

---

## 3. Universidad de Antioquia — trámites institucionales

### `04-universidad-tramites.md`

| Tarea | Quién | Tiempo |
|-------|-------|--------|
| **Designación formal del director de tesis con firma**. | Comité del Doctorado en Filosofía + director | 2-4 semanas |
| **Provisión de la plantilla institucional oficial** para tesis doctoral. | Secretaría del Doctorado | 1 semana |
| **Requisitos formales de declaración de originalidad**: formato y firma. | Secretaría del Doctorado | 1 semana |
| **Política institucional sobre co-autoría con IA**: la U. de Antioquia debe tener (o emitir) una política. Zona gris que puede ser problema en la sustentación. | Vicerrectoría de Investigación + Comité de Ética | 1-3 meses |
| **Designación de tribunal**: mínimo 3 sinodales con perfil compatible (filósofo de la ciencia, físico/sistemas complejos, humanista). | Comité del Doctorado + director | 2-4 meses |
| **Aprobación del proyecto por Comité de Ética Institucional** si el caso 30 (Behavioral Dynamics) avanza con datos VENLab humanos reales. | Comité de Ética | 3-6 meses |
| **Acceso a herramientas de diagramación profesional** (TikZ, Graphviz licencia) o presupuesto para diseñador editorial. | Programa de Doctorado o autor | Variable |

---

## Mapa de prioridades

### Prioridad 1: bloqueadores de sustentación (próximas 2-6 semanas)

- F23 (director declarado) → Universidad + Steven
- F24, F25, F26 (portada, originalidad, política IA) → Universidad provee plantilla, Steven la ajusta
- A.13 validación filosófica de borradores → Jacob

### Prioridad 2: cierre filosófico para defensa fuerte (próximos 4-12 meses)

- F1, F2, F3 (circularidad κ-ontológica, identidad-cuenca, salto inductivo) → Jacob
- F5 (refutación filosófica de alternativas) → Jacob
- F6, F9, F10 (engagement con interlocutores, asimetría, dimensiones omitidas) → Jacob
- Conceptos contaminantes (realismo estructural, fenomenología prometida, EI, self-organization, sinónimos) → Jacob + Steven

### Prioridad 3: cierre técnico opcional pre-defensa (próximos 2-3 meses)

- F13 (re-ejecutar corpus con `array_dump=True`) → Steven
- F16 (fetch real para casos macro) → Steven
- F17 (calibración externa QES) → Steven

### Prioridad 4: deuda externa post-defensa (6-24 meses)

- Tribunal completo y revisión externa → Universidad + revisores hostiles
- Programas de extensión multiescala con datos reales → Steven

---

## Origen y trazabilidad

- Auditoría doctoral original: `Bitacora/2026-04-28-cierre-tecnico/FALLOS_PENDIENTES_HISTORICO.md` (34 fallos detectados con tres lentes: filosófica, científica, formal/institucional).
- División de responsabilidades original: `Bitacora/2026-04-28-cierre-tecnico/TAREAS_POR_RESPONSABLE_HISTORICO.md`.
- Reporte de cierre técnico (lo que sí pudo ejecutar la asistencia computacional): `Bitacora/2026-04-28-cierre-tecnico/REPORTE_CIERRE_TECNICO.md`.
- Borradores filosóficos asistidos pendientes de validación de Jacob: `Anexos/A13-anticipacion-objeciones-filosoficas.md`.
- Propuesta operativa de calibración externa de QES: `09-simulaciones-edi/common/qes_external_calibration.md`.

Esta carpeta `Tareas_Humanas/` solo lista trabajo no automatizable. Los entregables técnicos cerrados están versionados en sus directorios canónicos del repositorio (`figures/`, `09-simulaciones-edi/baselines/`, `09-simulaciones-edi/topology/`, `09-simulaciones-edi/multi_sonda/`, etc.).
