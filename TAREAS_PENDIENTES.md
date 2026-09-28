# Tareas pendientes para el cierre de la tesis

Documento maestro de pendientes. Estado consolidado al **2026-07-17** tras auditoría de consistencia inferencial del manuscrito y la web; actualización parcial **2026-09-28** (pasada fix-all: B-T6 cerrada con evidencia pendiente re-verificación post-rebase, B-T-NEW-CLIMA-DATA abierta; B-E1 re-verificar tras rebuild). El histórico previo (con tabla BORRADOR-IA por tipo, notas iter-X y reclasificaciones intermedias) está preservado en `Bitacora/2026-05-17-limpieza-final/historico-tareas-pendientes.md`.

**Partición:**
- **Sección A — humanas o institucionales:** lo que **no** puede cerrar la asistencia computacional. Trámites de la U. de Antioquia, decisiones procedimentales de Jacob/Steven, validación final de voz autoral.
- **Sección B — ejecutables por la asistencia:** lo que **sí** se puede cerrar desde el repositorio sin perder rigor. Cada fila declara métrica de aceptación operativa.

**Regla de oro:** una tarea solo se marca cerrada cuando el contenido es defendible bajo crítica hostil. La discusión está en `Bitacora/2026-04-28-iteraciones-IA/REPORTE_AUTOINDULGENCIAS.md` y `CLAUDE.md §4`.

---

## A. Humanas o institucionales

### A.1. Universidad de Antioquia (H-U*)

| ID | Tarea | Estado |
|----|-------|--------|
| H-U1 | Designación formal del director de tesis con firma. **Bloqueador procedimental único.** | Abierta |
| H-U2 | Plantilla institucional oficial (LaTeX/Word). | Abierta |
| H-U3 | Formato y firma de declaración de originalidad. | Abierta |
| H-U4 | Política institucional sobre co-autoría con IA. | Abierta |
| H-U5 | Designación de tribunal (≥3 sinodales con perfil compatible). | Abierta |
| H-U6 | Aprobación del Comité de Ética **si** caso 30 VENLab humano avanza. | Diferida (H-S4 → post-defensa) |
| H-U7 | Acceso a diagramación profesional o presupuesto editorial. | Mitigada (SVG/PNG actual aceptable Q1) |

### A.2. Jacob — voz filosófica y validación (H-J*), ordenadas por prioridad

| Prio | ID | Tarea | Estado |
|------|----|-------|--------|
| 1 | H-J1 | Firma del cap `04-debates/04` (anticipación de objeciones filosóficas). Sin esta firma los borradores asistidos no son definitivos. | Abierta |
| 1 | H-J7 | Denominador `0/1500 → 0/2000` en defensa argumental. Cálculo verificado bit-a-bit (500+500+1000=2000; Wilson 95% CI [0, 0.00191]). Linter revirtió ediciones por tocar prosa argumental: requiere firma de (a) aceptar 0/2000, (b) mantener 0/1500 con justificación, (c) eliminar el numeral. | Abierta |
| 1 | H-J12 | Reclasificación caso 19 acidificación oceánica como **falsificación local del aparato** (EDI=-0.0047, CI=[-0.0054, -0.0041], p_perm=0.883; CI excluye cero por la izquierda). Cambios ya aplicados en Tabla 6.1.1, 5.7.1, abstracts ES/EN y `Correspondencia_Ricardo/06`; firma autoral pendiente. Caveats declarados: dataset NOAA no versionado, block-perm no implementada en `hybrid_validator.py`. | Abierta |
| 2 | H-J2 | Categoría de "ontología única multiescalar": (a) regulativa kantiana [posición provisional], (b) constitutiva con argumento independiente, (c) conjetura programática abierta. | Abierta |
| 2 | H-J3 | Estatus de la asimetría L1↔B↔L3↔S: ontológica / epistemológica / **procedimental** [posición provisional]. | Abierta |
| 2 | H-J5 | Engagement con Simondon, Gibson, Dennett, Searle, Bunge: ratificar o reformular la lectura preparada. | Abierta |
| 2 | H-J6 | Refutación filosófica de dualismo / idealismo / panpsiquismo (Chalmers, Goff, Strawson). Carga de prueba invertida + naturalismo metodológico no-fuerte preparada. | Abierta |
| 2 | H-J8 | Fusiones grandes de capítulos D.1–D.4 (síntesis 2026-05-11) + decisión intra-D.1: **conteo canónico de escenarios falsables (4 = 3+1)**. Borradores en `Bitacora/2026-05-11-sintesis-tesis/borradores/`. | Abierta |
| 2 | H-J9 | Reconocer baselines ARIMA/VAR ganan en 2/4 casos (Deforestación, Riesgo Biológico): insertar §3.6 + reformular Escenario 1 a 1.a/1.b + deuda baselines no-lineales. Borrador en `borradores/F3-AU3-baselines-superan.md`. | Abierta |
| 2 | H-J10 | Reclasificar Ladyman & Ross como rival eliminativista (verbatim p.130: "There are no things. Structure is all there is."). Reescribir `03-formalizacion/01 §12.2` y `03-formalizacion/03 §10.5`. | Abierta |
| 2 | H-J11 | AUC-ROC=0.886 reformulada como coherencia interna del umbral (no discriminación externa): mismo EDI como label y score, n=8 vs n=12 muestras distintas. Borrador retira "AUC-ROC vs ARIMA" como evidencia discriminativa. | Abierta |
| 3 | H-J4 | Dimensiones omitidas (estética + política agonística): (a) capítulos sustantivos, (b) ampliar declaración de omisión [mínimo defendible], (c) deuda post-defensa. | Abierta |

### A.3. Steven — coordinación externa (H-S*)

| ID | Tarea | Estado |
|----|-------|--------|
| H-S1 | Contactar 1-2 filósofos hostiles externos. Shortlist en `Bitacora/2026-05-16-shortlist-revisores/`. | En preparación |
| H-S2 | Contactar 1-2 estadísticos / físicos de complejidad. Shortlist en `Bitacora/2026-05-16-shortlist-revisores/`. | En preparación |
| H-S3 | Coordinación con director (una vez designado H-U1): cronograma, plantilla, política IA. | Abierta |
| H-S4 | Caso 30 VENLab con datos humanos antes/después de defensa → **post-defensa** (deuda externa; EDI=0.002 honesto declarado). | Cerrada |

---

## B. Ejecutables por la asistencia computacional

### B.1. Engagement filosófico (B-F*)

| ID | Tarea | Estado |
|----|-------|--------|
| B-F1 | Cap `04-debates/04` cubre F1–F10 con concesión/distinción/argumento/costo + paginación Lakatos 1978 pp.33-34, 48, 49. | Núcleo cumplido; firma final en H-J1 |
| B-F2 | Redefinir "realismo estructural moderado" en glosario como uso operativo no-Ladyman/Ross. | Cerrada técnicamente; firma filosófica absorbida por H-J2/H-J10 |
| B-F3 | Promesa fenomenológica del abstract: entregar sección breve en `05-01` o eliminar del keyword. | Cerrada: promesa retirada del resumen y alcance declarado como programático |
| B-F4 | Atractor con rigor topológico (cap `02-01 §2.2.1-3` + Tabla 2.1.6 sobre 7 casos, paginación Rosenstein 1993 pp.117-134, Grassberger-Procaccia 1983 pp.189-208). Extensión a 33 casos = B-T1. | Cerrada (firma de validación con Jacob, no bloquea) |
| B-F5 | Disciplinar "self-organization" — 0 menciones del cuerpo sin ancla en cap `02-04 §4` (Maturana-Varela 1980, Haken 1977 pp.191-204). | Cerrada |
| B-F6 | Sinónimos coloquiales del núcleo conceptual declarados en glosario como convención global. | Cerrada |

### B.2. Cierre técnico (B-T*)

| ID | Tarea | Estado | Métrica de aceptación |
|----|-------|--------|----------------------|
| B-T1 | Corpus efectivo = 32 casos (30 numerados + 41 Wolfram + 42 histéresis) con `primary_arrays.json`. | Cerrada | 32/32 verificado vía `find 09-simulaciones-edi -name "primary_arrays.json" -path "*/outputs/*"` |
| B-T2 | Fetchers reales en `multiscale_fetchers.py`. Piloto caso 16 Deforestación; resto de macros como deuda post-defensa. | Piloto en ejecución | Caso 16 con `data_source: real_external` en `data/FETCH_MANIFEST.json`; declaración honesta en cap `03-04` |
| **B-T2.1** | **Pre-registro genuino ex ante ampliado**. Iter 17 ejecutó 3 casos (04 valida weak, 20 falsifica, 24 falsifica colapsando de robusto declarado a EDI=-1.0). **Resultado:** 0 strong robustos puros sobreviven. Falta extender a casos 16/17/18/21 (los 4 reclasificados con datos refrescados — ver `Bitacora/2026-05-17-process-verifier-final/audit.md` R5). | **Abierta** | Pre-registros versionados en `docs/PRE_REGISTRO_B_T2_1*.md` con commit hash pre-firma; `metrics.json` regenerado; tabla comparativa B-T2 vs B-T2.1 en `09-simulaciones-edi/Evaluacion_Modelos_Dominio.md` |
| B-T3 | Calibración externa QES (10/10 estudios, concordancia loose 100%, estricta 50%, Bem 2011 INADMISIBLE). | Cerrada | `09-simulaciones-edi/qes_calibration/external_calibration_report.md` |
| B-T4 | Información efectiva como métrica auxiliar (sin compromiso IIT/Hoel) declarada en `03-formalizacion/04` §líneas 205-215 + glosario `:99`. | Cerrada | Ubicación de código `hybrid_validator.py:249` + declaración filosófica explícita |
| B-T5 | Reclasificación caso 19 a falsificación local (ver H-J12 para firma). | Cerrada (firma en H-J12) | `metrics.json` regenerado; Tablas 6.1.1 / 5.7.1 / Bloque VI.5 actualizadas |
| B-T6 | Disonancia doc↔config sondas ODE casos 03/12/29 (doc declaraba Acumulación/Landau-Ginzburg/Difusión+Metcalfe; configs ejecutan `mean_reversion`/`mean_reversion`/`bilinear`). | Cerrada 2026-09-28 | Opción (b) ya aplicada en el doc (filas tabla reconcilian a configs); verificado con diente: `verify_consistency_doc_config.py` (bug precedencia corregido + patrón tabla) → 3 doc × 30 configs, 0 disonancias. Falsador: re-correr el verificador. |
| B-T7 | Caso 25 acuíferos con cobertura 0.51 dominado por datos faltantes. Bloqueado por B-T2. | Bloqueada | `metrics.json` con cobertura ≥0.95; null/no-null reasignado |
| **B-T2.4** | **Re-verificación inter-escala con datos reales por escala**. Generalidad multiescalar bajo aparato post-fix (`detrended_edi` corregido iter 13 + block-perm propagada). Posición filosófica en `Bitacora/2026-05-17-cierre-loop/posicion-filosofica-final.md`; H-J6 decide si es deuda fechada o condición de defensa. | **Abierta** | Casos inter-escala (31/32) re-ejecutados bajo aparato corregido con datos por escala; tabla comparativa pre/post |
| **B-T-NEW-AUC-METH** | **Crear `09-simulaciones-edi/auc_roc/methodology.md` + script regenerador** con CI bootstrap (B≥2000) y comando declarado. La cifra se conserva solo como consistencia interna del umbral, no como validación externa. | **Cerrada técnicamente; afirmación discriminativa retirada** | `methodology.md` y `compute_auc_ci.py` reproducen AUC=0.8857, CI=[0.6571, 1.0000]; H-J11 firma la interpretación |
| **B-T-NEW-CLIMA-DATA** | **Rescate de datos caso 01**: `outputs/metrics.json` commiteado (2026-07-16, EDI=0.258) usó CSV post-procesado indocumentado (408 filas, media≈0, std≈0.01); reproducción bit-idéntica bloqueada. Vía real restaurada (`src/data.py` + meteostat 2.x; revalidación 2026-09-28: EDI=0.0030, misma conclusión pass=False). | **Abierta** | Receta documentada + bit-repro, o re-corrida fresca aceptada + prosa que cite EDI=0.258 actualizada |

### B.3. Auditoría editorial (B-E*)

| ID | Tarea | Estado |
|----|-------|--------|
| B-E1 | Re-ejecutar `TesisFinal/build.py`, regenerar PDF y verificar diff/render. | Cerrada 2026-07-17: MD 7.159 líneas y 75.792 palabras; PDF 204 páginas; 0 páginas con texto recortado. Re-verificar tras rebuild post-rebase 2026-09-28 (prosa origin + sellos deuda) |
| B-E2 | Uniformidad Chicago author-date (≤5 anomalías documentadas). | Abierta |
| B-E3 | Numeración tablas/figuras tras inserciones recientes. | Abierta |
| B-E4 | Cobertura glosario tras B-F2/B-F5/B-F6. | Abierta |
| B-E5 | Re-ejecución canónica caso 30 (EDI=0.2622, CI=[0.2494, 0.2798], p_perm=0.0440). | Cerrada |
| B-E6 | Sincronización prosa↔JSON 30 casos macro + 2 inter-escala. 28/30 directos; 3 casos (03, 12, 19) con divergencia declarada por datos externos. Cierre completo requiere B-T2. | Parcial |
| B-E7 | Re-ejecutar perfil canónico (n_perm=999, n_boot=500) caso 16 Deforestación (target EDI=0.6020, CI=[0.5872, 0.6168] de Tabla A.8.1). | Abierta |

---

## BORRADOR-IA — resumen consolidado

El conteo de marcadores debe regenerarse tras esta pasada. La introducción, las preguntas, el resumen, el mapa del corpus y la conclusión contienen nuevos marcadores **BORRADOR-IA · requires: H-J2/H-J8** porque la reducción explícita de alcance requiere voz y firma autoral. **Ningún H-J* se cierra por consolidación de marcadores.**

---

## Mapa de prioridades

**Prioridad 1 — bloqueadores de sustentación:** H-U1, H-U2, H-U3, H-U4 + H-J1, H-J7, H-J12.

**Prioridad 2 — cierre filosófico defendible:** H-J2, H-J3, H-J5, H-J6, H-J8, H-J9, H-J10, H-J11.

**Prioridad 3 — cierre técnico pre-defensa:** B-T2 piloto, B-T2.1 ampliado (4 casos restantes), B-T-NEW-CLIMA-DATA, B-E2–E4 y B-E6–E7 (B-T6 cerrada 2026-09-28 pendiente re-verificación post-rebase; B-E1 cerrada 2026-07-17, re-verificar tras rebuild).

**Prioridad 4 — deuda externa post-defensa:** H-S1, H-S2, H-U5, B-T2 resto, B-T2.4 inter-escala, B-T7 acuíferos, caso 30 VENLab (H-S4 decidida).

---

## Bitácora histórica relevante

- `Bitacora/2026-05-17-limpieza-final/historico-tareas-pendientes.md` — versión previa de este archivo.
- `Bitacora/2026-05-17-loop-nocturno/REPORTE_EJECUTIVO_FINAL_v4.md` — cierre del loop iter 1–18.
- `Bitacora/2026-05-17-cierre-loop/posicion-filosofica-final.md` — posición Lakatos sobre B-T2.4.
- `Bitacora/2026-04-28-cierre-tecnico/REPORTE_CIERRE_TECNICO.md` — tabla histórica de fallos cerrados.
- `Bitacora/2026-04-28-iteraciones-IA/REPORTE_AUTOINDULGENCIAS.md` — lectura obligatoria antes de pasadas futuras.
- `Tareas_Humanas/01-jacob-fundamentos-filosoficos.md`, `02-steven-decisiones-tecnicas.md`, `03-universidad-tramites.md` — referencia histórica; este archivo es la fuente de verdad activa.
