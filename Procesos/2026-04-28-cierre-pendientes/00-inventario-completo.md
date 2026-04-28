# Inventario completo de pendientes — 2026-04-28

## Función

Registro consolidado del estado de actividades pendientes al cierre del manuscrito doctoral (versión 2026-04-28). Su propósito es **no modificar archivos canónicos** dejando referencia única en `Procesos/` con marca de tiempo.

Este inventario clasifica los pendientes en cuatro categorías por tipo de cierre:

- **A.** Ejecutado en esta versión (no es pendiente; se documenta para registro).
- **B.** Documentado con dossier técnico-ético, ejecución supeditada a recurso externo.
- **C.** Programa futuro con esquema declarado.
- **D.** Mega-tareas estratégicas (Backlog/) movidas a archivo histórico.

---

## A. Pendientes ejecutados en esta versión (registro)

| Ítem | Fecha de ejecución | Resultado | Archivo |
|------|--------------------|-----------|---------|
| Programa multi-sonda (Energía, Deforestación, Riesgo Bio) | 2026-04-28 | 1 convergencia fuerte + 2 moderadas | `09-simulaciones-edi/multi_sonda/` |
| Baselines ARIMA + VAR + RW (8 casos) | 2026-04-28 | HB.1-HB.4 verificadas con interpretación dimensional | `09-simulaciones-edi/baselines/` |
| Tres sondas ODE alternativas implementadas | 2026-04-28 | `thermo_balance`, `spatial_logistic`, `seir_demographic` | `09-simulaciones-edi/common/ode_models.py` |
| Auditoría doctoral v2 con verificación de cierre | 2026-04-28 | 10 bloques + 8 puntos menores cerrados o ejecutados | `Auditoria_Doctoral.md` |
| Capítulos institucionales y estado del arte | 2026-04-28 | `00-04`, `01-03`, `03-05` | sus respectivos archivos |
| Anexos A.8 (tablas crudas) y A.9 (listas editoriales) | 2026-04-28 | Disponibles | `Anexos/` |

**Diagnóstico:** ya no son pendientes. Aparecen aquí únicamente para que la trazabilidad histórica del cierre quede en un único registro consultable.

---

## B. Pendientes con dossier técnico-ético, ejecución supeditada a recurso externo

### B.1. Elevación del caso 30 con datos humanos a LoE = 4

- **Estado:** dossier completo en `Procesos/2026-04-28-cierre-doctoral/02-programa-datos-humanos-caso30.md`.
- **Ruta:** OpenLocomotionData → WALK-MS Boston → VENLab Brown.
- **Cronograma:** 9–10 meses de dedicación parcial.
- **Bloqueante operativo:** acceso a datasets externos + aval de Comité de Ética.
- **Decisión de manuscrito:** caso 30 permanece como Nivel 3 weak con LoE = 2; cualquier resultado posterior se reportará en escenarios A/B/C ya documentados en el mismo dossier.

### B.2. Caso piloto COVID-19 (dimensión normativa)

- **Estado:** justificación y candidatos en `05-aplicaciones/04-instituciones-mercado-y-estado.md` §7.1.
- **Datos candidatos:** Oxford COVID-19 Government Response Tracker (Hale et al. 2021).
- **Cronograma:** 3–6 meses.
- **Adaptación técnica requerida:** pipeline EDI para series institucionales con índices ordinales (stringency).
- **Decisión de manuscrito:** capítulo 05-04 declarado en modo programático acotado (Ruta A); el caso piloto es Ruta B documentada para trabajo futuro.

---

## C. Programas futuros con esquema declarado

### C.1. Convergencia EDI con Wolfram Physics Project

- **Estado:** esquema en 6 pasos en `04-debates/01-debates-con-posiciones-rivales.md` §14 (sección "Convergencia productiva posible").
- **Cronograma estimado:** 12–18 meses.
- **Pasos:** selección de regla → simulaciones → sonda macro → aplicación EDI → hipótesis → lectura.
- **Estado actual:** propuesta concreta no ejecutada.

### C.2. Verificación masiva del corpus completo bajo perfil agresivo

- **Estado:** mencionado en `Anexos/A8-tablas-crudas-corpus.md` Tabla A.8.3.
- **Realizado hasta ahora:** Deforestación y Behavioral Dynamics verificados.
- **Pendiente:** los otros 28 casos del corpus.
- **Esfuerzo:** 1–2 días de cómputo bajo el perfil agresivo (n_perm = 2999, n_boot = 1500) sobre las GPUs disponibles.

### C.3. Extensión multi-sonda a casos weak con p < 0.001

- **Estado:** declarado como deuda secundaria en `09-simulaciones-edi/multi_sonda/README.md`.
- **Casos candidatos:** Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología.
- **Esfuerzo:** análogo al multi-sonda en strong (1 sonda alternativa por caso), 4–6 semanas.

### C.4. Comparación contra modelos no lineales

- **Estado:** declarado como deuda futura en `09-simulaciones-edi/baselines/README.md` §"Limitaciones".
- **Modelos candidatos:** LSTM, Transformer, Gaussian Process no estacionario.
- **Esfuerzo:** 4–8 semanas según modelo.

### C.5. Discriminación cuantitativa fina mente-memoria

- **Estado:** mencionado en `05-aplicaciones/01-mente-memoria-yo.md` línea 101.
- **Naturaleza:** confrontación cuantitativa modelo dinámico vs. modelo Atkinson-Shiffrin sobre datos de interferencia/forgetting/reconsolidación.
- **Esfuerzo:** depende del dataset; 3–6 meses.

### C.6. Revisión exhaustiva por dominio del corpus

- **Estado:** declarado en `01-diagnostico/03-estado-del-arte.md` §8.
- **Naturaleza:** mini-revisión específica por cada uno de los 30 dominios del corpus.
- **Esfuerzo:** 6–12 meses, distribuible entre ítems.

### C.7. Conversión a LaTeX/PDF con plantilla institucional

- **Estado:** declarado en bloque 10 de la auditoría v2.
- **Naturaleza:** trámite editorial pre-depósito.
- **Esfuerzo:** 3 semanas, ejecutable cuando la plantilla institucional esté disponible.

### C.8. Conversión de figuras ASCII a SVG/PNG

- **Estado:** declarado en `Anexos/A9-listas-figuras-tablas-abreviaturas.md` §A.9.1.
- **Naturaleza:** trámite editorial pre-depósito.
- **Esfuerzo:** 1–2 semanas con Mermaid o equivalente.

---

## D. Mega-tareas estratégicas (movidas a archivo histórico)

La carpeta `Backlog/` (originalmente `Tareas/`) contiene siete documentos de **mega-tareas estratégicas** que son trabajo posterior al manuscrito doctoral. Para mantener limpio el árbol del manuscrito sin destruir contenido, se mueven al archivo de procesos como referencia histórica:

- `00-critica-radical-de-la-tesis.md`
- `01-pasos-no-negociables.md`
- `02-mega-tarea-programa-cientifico-general.md`
- `03-mega-tarea-traduccion-y-reconstruccion-canonica.md`
- `04-mega-tarea-operacionalizacion-y-validacion.md`
- `05-mega-tarea-benchmark-rivales.md`
- `06-mega-tarea-corpus-st-y-plataforma.md`
- `90-tareas-documentales-delegables-a-ia.md`
- `README.md`

**Destino:** `Procesos/2026-04-28-cierre-pendientes/mega-tareas-archivadas/`.

**Diagnóstico:** son hojas de ruta de programa científico de largo plazo, no tareas pendientes del manuscrito doctoral. Se preservan tal cual, sin modificación, para que cualquier extensión posterior del programa pueda invocarlas.

---

## Resumen final

Al cierre del 2026-04-28:

- **0 pendientes ejecutables internamente** sin gestión externa.
- **2 pendientes con dossier técnico-ético** y bloqueante de recurso externo (caso 30 humano, caso piloto COVID).
- **8 programas futuros con esquema declarado** (convergencia Wolfram, perfil agresivo masivo, multi-sonda en weak, baselines no lineales, mente-memoria fina, revisión por dominio, LaTeX/PDF, figuras formales).
- **8 mega-tareas estratégicas** archivadas como referencia histórica.

**El manuscrito está limpio de pendientes activos para sustentación de fondo.** Lo que queda es trabajo posterior con cronograma honesto o trabajo dependiente de recurso externo.

## Lectura cruzada

- Procesos del 2026-04-27: `Procesos/2026-04-27-integracion-jacob/`.
- Procesos del 2026-04-28 (programas técnico-éticos): `Procesos/2026-04-28-cierre-doctoral/`.
- Auditorías: `Procesos/2026-04-27-integracion-jacob/04-auditoria-doctoral-v1.md` y `Auditoria_Doctoral.md` (v2).
- Mega-tareas archivadas: `Procesos/2026-04-28-cierre-pendientes/mega-tareas-archivadas/`.
