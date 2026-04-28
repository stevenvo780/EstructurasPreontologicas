# Programa de adquisición de datos humanos para el caso 30

## Función

Documento que especifica la ruta concreta de elevación del caso 30 (behavioral dynamics) desde LoE = 2 (datos sintéticos) a LoE = 4 (datos humanos reales) bajo control ético institucional. La existencia de este documento responde a la deuda residual nombrada en el manuscrito y al bloque 4 de la auditoría doctoral interna (`04-auditoria-doctoral-v1.md`).

## 1. Estado actual del caso 30

- **EDI = 0.2622 (p = 0.044)** bajo perfil canónico (n_perm = 999, n_boot = 500).
- **Bootstrap CI = [0.2494, 0.2798]**, estrecho, no incluye cero.
- **Verificado bajo perfil agresivo** (n_perm = 2999, n_boot = 1500): EDI = 0.2623 idéntico.
- **Clasificación:** Nivel 3 (weak), `overall_pass = False` por diseño (no alcanza umbral strong).
- **LoE = 2:** datos sintéticos generados con la ecuación completa de Fajen-Warren (no con la sonda EDI simplificada, evitando circularidad ABM ≡ ODE).

La señal es genuina, robusta y honesta. Falta cerrar la pregunta legítima: ¿se mantiene con datos humanos reales?

## 2. Hipótesis a verificar

| Hipótesis | Enunciado |
|-----------|-----------|
| H30R.1 | EDI sobre datos humanos reales ≥ 0.20 con p < 0.05 |
| H30R.2 | EDI real es comparable (banda ±0.05) al EDI sintético |
| H30R.3 | Si H30R.2 falla, identificar qué aspecto del fenómeno captura el sintético que el real no, o viceversa |

Tres escenarios cualitativos:

- **Escenario A (favorable):** EDI real ≥ 0.30, `overall_pass = True`. El caso 30 se eleva a Nivel 4 (strong).
- **Escenario B (esperado):** EDI real comparable al sintético (~0.26), Nivel 3 weak confirmado. El caso 30 se mantiene como demostrativo cuantitativo de behavioral dynamics weak con datos humanos verificados.
- **Escenario C (adverso):** EDI real significativamente menor o no significativo. La tesis lo reportaría honestamente; el caso 30 se rebajaría a programático y la conjetura se discutiría con detalle. La tesis general no depende de un único caso strong adicional.

## 3. Datasets candidatos

### 3.1. VENLab (Brown University)

**Lab:** Warren Lab, Department of Cognitive Linguistic and Psychological Sciences, Brown University.

**Descripción:** captura de movimiento óptica de alta frecuencia (60–120 Hz) en tareas de locomoción dirigida, esquiva de obstáculos, seguimiento de líderes. Es el laboratorio de origen de Fajen-Warren 2003 y Warren 2006. Ofrece la coincidencia teórica más estrecha con la sonda `behavioral_attractor`.

**Acceso:** previa solicitud académica al PI (William H. Warren). Se redactará carta institucional firmada por el director(a) de tesis cuando esté designado.

**Ventaja:** los datos se generaron con la teoría que se está probando, lo que permite la calibración más limpia.

**Desventaja:** requiere gestión académica directa, sin garantía de respuesta.

### 3.2. WALK-MS Boston

**Institución:** Boston University Movement Science Lab.

**Descripción:** captura de locomoción humana en interiores, con metas variables, en sujetos sanos y patológicos. Frecuencia 100–200 Hz.

**Acceso:** abierto académico, registro previo.

**Ventaja:** disponibilidad inmediata.

**Desventaja:** menor coincidencia teórica con Fajen-Warren; requiere adaptación de la sonda.

### 3.3. OpenLocomotionData

**Consorcio:** consorcio académico multi-institucional 2020–presente.

**Descripción:** repositorio agregado de datasets de locomoción dirigida con metadatos estandarizados.

**Acceso:** Open Access bajo CC BY 4.0.

**Ventaja:** licencia permisiva, disponibilidad inmediata, múltiples laboratorios.

**Desventaja:** heterogeneidad en protocolos requiere selección cuidadosa.

### 3.4. CMU MoCap

**Institución:** Carnegie Mellon University.

**Descripción:** captura de movimiento humana general, no específica de locomoción dirigida pero amplia.

**Acceso:** académico, disponible.

**Ventaja:** cantidad masiva de datos.

**Desventaja:** la mayoría no es locomoción dirigida con meta variable; requiere filtrado intensivo.

### 3.5. Decisión

Estrategia secuencial:

1. **Fase 1:** OpenLocomotionData (acceso inmediato, ejecutar adaptación de pipeline).
2. **Fase 2:** WALK-MS Boston (registro académico, complementar con datos clínicamente caracterizados).
3. **Fase 3:** VENLab (gestión académica con Warren Lab para el contraste teórico estricto).
4. **Fase 4 (opcional):** CMU MoCap si las anteriores resultan insuficientes.

## 4. Adaptación del pipeline EDI

**Cambios técnicos requeridos:**

- adaptación de la ventana de validación de mensual (val_steps = 35 en versión sintética) a la frecuencia natural del dataset (60–120 Hz);
- reescalado de los parámetros de Fajen-Warren al dominio temporal real (b = 3.25 sigue siendo dimensionalmente coherente, pero requiere verificación);
- ajuste del ruido motor del ABM al espectro empírico observado;
- decisión sobre tamaño de muestra y agregación inter-sujetos.

**Costo computacional estimado:** factor 10–100 sobre la versión sintética por la mayor frecuencia. Hardware disponible (2 GPUs, 32 hilos CPU, 123 GB RAM) lo soporta sin problema.

## 5. Procedimiento ético

| Paso | Acción | Responsable |
|------|--------|-------------|
| 1 | Solicitud formal al PI / dataset host con uso académico secundario declarado | autor técnico + carta del director |
| 2 | Verificación de consentimiento informado del estudio original | autor técnico |
| 3 | Radicación de protocolo de investigación en CEI Universidad de Antioquia | director(a) + autor principal |
| 4 | Aval explícito del CEI documentado | CEI |
| 5 | Anonimización adicional si procede (verificar que dataset original no permite re-identificación) | autor técnico |
| 6 | Cumplimiento Ley 1581/2012 (Colombia) | autor principal |
| 7 | Re-ejecución del caso 30 con datos reales | autor técnico |
| 8 | Reporte de resultados en `09-simulaciones-edi/30_caso_behavioral_dynamics/outputs/metrics_real.json` | autor técnico |
| 9 | Actualización del README del caso 30 con escenario A/B/C | ambos autores |
| 10 | Archivado de documentación del proceso ético en `Procesos/` | autor técnico |

**Bloqueante:** sin aval CEI documentado, no se ejecuta el paso 7.

## 6. Cronograma estimado

| Mes | Hito |
|-----|------|
| 0–1 | Diseño detallado, redacción de protocolo CEI |
| 1–2 | Solicitudes a datasets, registro académico |
| 2–3 | Adaptación del pipeline EDI a alta frecuencia |
| 3–4 | Aval CEI obtenido |
| 4–5 | Re-ejecución sobre OpenLocomotionData |
| 5–6 | Re-ejecución sobre WALK-MS |
| 6–8 | Re-ejecución sobre VENLab (si acceso obtenido) |
| 8–9 | Análisis comparativo y reporte |
| 9–10 | Actualización del manuscrito y de la conclusión demostrativa |

Total: 9–10 meses de dedicación parcial (compatible con el ciclo doctoral declarado en el capítulo 06-03).

## 7. Decisión condicional sobre el caso 30 en el manuscrito final

**Mientras la elevación no se complete:**

- el caso 30 se reporta como **demostrativo Nivel 3 weak con LoE = 2**;
- la tesis declara explícitamente que la elevación a Nivel 4 strong con LoE = 4 es deuda residual del programa;
- la conjetura ontológica (behavioral dynamics como dominio donde el aparato EDI funciona) se sostiene con la señal weak verificada;
- la complementariedad con la demostración cualitativa de Warren 2006 (capítulo 05-05) cubre la dimensión temporal corta.

**Al cierre de la elevación:**

- según escenario A/B/C, se actualizan las cifras del corpus, las tablas del Anexo A.5, la conclusión demostrativa (capítulo 06-01), y la guía de defensa (06-02).

## 8. Compromiso público

Este programa se asume como **compromiso firme** del autor técnico (Steven Vallejo) en coordinación con el autor principal (Jacob Agudelo). Su ejecución se documenta en `Procesos/`, sus resultados se publican en el repositorio, y su no-ejecución (si por motivos institucionales no procede) se reporta también con honestidad.

## 9. Lectura cruzada

- Caso 30 actual: `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`.
- Política ética y de gobernanza de datos: `03-formalizacion/05-etica-y-gobernanza-de-datos.md`.
- Auditoría que motivó este programa: `Procesos/2026-04-27-integracion-jacob/04-auditoria-doctoral-v1.md` §4.
- Hoja de ruta general: `06-cierre/03-hoja-de-ruta-para-tesis-final.md`.
