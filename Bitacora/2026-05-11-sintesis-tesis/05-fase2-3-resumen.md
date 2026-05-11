# Fases 2 y 3 — Síntesis y rescate (resumen 2026-05-11)

## Fase 2 — Fusiones grandes (BORRADORES-IA, requieren firma Jacob)

Cuatro fusiones identificadas por la auditoría de redundancia. Cada una produjo borrador defendible. **NO se editaron los capítulos originales** — solo borradores en `Bitacora/2026-05-11-sintesis-tesis/borradores/`.

### D.1 — Defensa oral (06-cierre/02 + 04 + 05)

**Borrador**: `borradores/D1-defensa-oral-consolidada.md` (281 líneas).
**Arquitectura**: un solo `06-cierre/02-guia-de-defensa.md` (~140 líneas) con tesis canónica de 30s + versión 2min + 7 P&R + 4 trampas + fórmula final; dos extras nuevos: `_extendido/versiones-cortas-defensa.md` (110) y `_extendido/respuestas-tipo-defensa.md` (140).
**Líneas brutas**: 529 → 390 (−139, −26%).
**Sorpresa**: los 3 archivos NO están en `TesisFinal/build.py` PARTS — son satélites de defensa, no parte del manuscrito ensamblado. La fusión es libre del lado del build.
**Decisión clave que requiere firma**: ⚠️ **conteo canónico de escenarios falsables (4/5/6)** — vulnerabilidad de defensa explícita marcada con bloque ⚠️ en el borrador. Recomendación operativa: 5 escenarios.

### D.2 — `04-debates/01` ↔ `03` (rivales)

**Borrador**: `borradores/D2-debates-01-consolidado.md`.
**Arquitectura**: `01` consolidado a 246 líneas (de 491). 14 rivales divididos: 8 con discriminación tabular suficiente (basta `03`), 6 requieren prosa argumentativa. 7 archivos `04-debates/_extendido/rival-<X>.md` propuestos (no escritos todavía).
**Líneas brutas**: 491 → 246 (−245).
**Eliminaciones**: 14 micro-tablas tesis vs rival (Tabla 4.1.1–4.1.14) duplicadas en `03`; tabla 4.1.15 síntesis; §1 criterios; §17 compromiso público.

### D.3 — `04-debates/02` subsumido por `05`

**Borrador**: `borradores/D3-debates-02-decision.md`.
**Salida elegida**: **(b) reducir, NO eliminar**. La auditoría inicial (eliminar) era parcialmente correcta: §1, §4, §6, §8 de `02` están en `05`; pero §3, §7, §9-12 son contenido único filosófico no replicable.
**Líneas brutas**: 200 → ~65 (−135).
**Referencias cruzadas**: 1 en manuscrito vivo (`04-debates/01:429`), 0 bloqueadoras en `build.py`. No hay obstáculo estructural.

### D.4 — `00-proyecto/01` + `03`

**Borrador**: `borradores/D4-proyecto-01-03-decision.md`.
**Salida elegida**: **(a) FUSIÓN total**.
**Justificación**:
1. Ninguno entra al manuscrito ensamblado (`build.py` solo asimila `00`, `05`, `06`, `07` del directorio).
2. `03-plan-de-capitulos.md` describe arquitectura **obsoleta**: 6 capítulos + Intro/Conclusión, cuando la realidad de `build.py` son 5 Partes con 31 capítulos. Hallazgo lateral: `03-plan:108` lista 13 rivales (sin Wolfram).
3. Solapamiento residual ≈60%.
**Líneas brutas**: 371 → ~190 (−175).

### Total Fase 2

| Capítulo | −Líneas | Afecta Tesis.md ensamblada |
|---|--:|---|
| D.1 | −139 | No (satélites) |
| D.2 | −245 | Sí |
| D.3 | −135 | Sí |
| D.4 | −175 | No (no en PARTS) |
| **Total** | **−694** | **−380 en Tesis.md** |

## Fase 3 — Rescate de hallazgos auditables (BORRADORES-IA, requieren firma Jacob)

Tres hallazgos de mayor impacto del triage de bitácora huérfana. Cada uno verificado contra fuente primaria (código, PDF, metrics.json) antes de proponer borrador.

### F3-AU3 — Baselines ARIMA/VAR superan al modelo en 2/4 casos

**Verificación**: contra `09-simulaciones-edi/baselines/baselines_report.json` (canónico 2026-04-29).

| Caso | RMSE acoplado | RMSE ARIMA | RMSE VAR | val_len |
|---|--:|--:|--:|--:|
| 04_caso_energia | 0.4058 | 0.4830 | 0.5846 | 20 |
| 16_caso_deforestacion | **0.5652** | **0.2807** | **0.2465** | 13 |
| 20_caso_kessler | 0.5576 | 1.5887 | 1.6105 | 8 |
| 27_caso_riesgo_biologico | **0.2393** | **0.1820** | 0.2257 | 8 |

ARIMA/VAR ganan en Deforestación y Riesgo Biológico (held-out RMSE). **Activa parcialmente el Escenario 1** declarado en `06-cierre/01:85-87` pero no reconocido en §3.

**Salvedades metodológicas honestas**: (i) RMSE held-out ≠ RMSE de métrica EDI canónica; (ii) val_len ∈ {8,13} es pequeño, sin CI/Diebold-Mariano; (iii) `overall_pass` integra C1-C5 + significancia EDI vs ablación interna, no vs baselines lineales.

**Borrador**: `borradores/F3-AU3-baselines-superan.md` — insertar §3.6 en `06-cierre/01` reconociendo el hallazgo + reformular Escenario 1 a 1.a/1.b + crear deuda residual de baselines no-lineales (GP, LSTM, ESN) a 2 meses.

### F3-F03-07 — Ladyman & Ross como rivales (no aliados)

**Verificación**: cita "*There are no things. Structure is all there is.*" — **verbatim en p.130** del PDF en `07-bibliografia/Ladyman Ross - Every Thing Must Go (2007).pdf` (página 143 del PDF). Auto-descripción explícita "*our view is eliminative*" en p.131.

**Discrepancia de paginación corregida**: las ubicaciones reales son `03-formalizacion/01:256-258` (no 260-262) y `03-formalizacion/03:248-250` (no 254-256). Triage previo usaba paginación stale.

**Borradores** (dos archivos):
- `borradores/F3-F03-07-aparato-formal-LR.md`: reescritura §12.2 con L&R como rival eliminativista. Cita verbatim p.130 + nuance p.131 (concesión: L&R no niegan que existan objetos discursivos, niegan natura intrínseca/individualidad). Frontera filosófica: la tesis preserva ontología de cosas en cada estrato; L&R la elimina en cualquier estrato.
- `borradores/F3-F03-07-auditoria-ontologica-LR.md`: reescritura §10.5 adaptada al contexto de auditoría ontológica + Rainforest Realism (p.191) sobre ciencias especiales.

### F3-AU5 — AUC-ROC=0.886 reformulada como coherencia interna

**Verificación de los 3 sub-claims (todos CONFIRMADOS leyendo código primario)**:
1. Mismo EDI como label y como score: `Bitacora/2026-04-28-cierre-severo/N3_auc_roc_discriminacion.py:51-68`. `label_strong=1` si EDI≥0.33 (umbral declarado); luego AUC computado con mismo EDI como score. AUC≠1.0 solo por `26_starlink` (EDI=0.6892, label=0 por gate=false) — mide **inconsistencia umbral residual**, no discriminación.
2. n=8 vs n=12: líneas 60-63 del script — 4 casos null tienen `rmse_arima: None`; filtro para ARIMA → n=8. Comparación 0.886 vs 0.600 sobre muestras distintas.
3. `09-simulaciones-edi/auc_roc/methodology.md` AUSENTE. Solo existe `baselines/README.md:91-99` con disclaimer parcial.

**Salida elegida**: **(b) reformular**, NO eliminar. La cifra es honesta como coherencia interna; lo deshonesto es presentarla como discriminación externa.

**Borrador**: `borradores/F3-AU5-auc-roc.md` — reformular líneas 230, 235, 237 de `06-cierre/01` retirando "AUC-ROC 0.886 vs ARIMA 0.600" como evidencia discriminativa y sustituyendo por "coherencia interna del umbral EDI (AUC-ROC=0.886, n=12)" con declaración explícita. Trasladar peso evidencial al 0/2000 FP del gate y los 3/3 controles de falsación rechazados. Deuda B-T-NEW-AUC-METH: crear `methodology.md` con CI bootstrap.

## Decisiones que requieren firma de Jacob (H-J8 a H-J11)

| Tarea | Borrador | Decisión clave |
|---|---|---|
| H-J8 | D.1-D.4 (4 borradores) | (a) Aprobar arquitectura `_extendido/` como convención; (b) Conteo canónico escenarios falsables (4/5/6); (c) División 8 tabulares + 6 discursivos para rivales; (d) Salida (b) sobre `04-debates/02` |
| H-J9 | F3-AU3 | (a) Aprobar §3.6 con reconocimiento honesto; (b) Reformular Escenario 1 a 1.a/1.b; (c) Plazo baselines no-lineales |
| H-J10 | F3-LR-A + F3-LR-B | (a) Reclasificar L&R como rival eliminativista; (b) Mantener nuance p.131 vs eliminar por dilución; (c) Actualizar glosario `00-proyecto/07:36` |
| H-J11 | F3-AU5 | (a) Salida (b) reformular vs (a) eliminar; (b) Aprobar redacción exacta; (c) Crear `methodology.md` como deuda bloqueante |

## Próximos pasos (después de firma)

1. **Aplicar borradores** Fase 2 a los capítulos: −694 líneas brutas total, −380 en Tesis.md.
2. **Aplicar correcciones** Fase 3 a los pasajes verificados: 4 párrafos reescritos en `06-cierre/01` y `03-formalizacion/{01,03}`.
3. **Crear los 7 `04-debates/_extendido/rival-<X>.md`** propuestos en D.2 (no escritos todavía).
4. **Reordenar `build.py` PARTS** según D.3 (si Jacob aprueba reordenar `02` post `05`).

## Costo declarado

- Tokens consumidos: ~3.5M (3 agentes Fase 1 + 3 agentes Fase 2 + 3 agentes Fase 3 + auditoría inicial).
- Tiempo: ~3 horas de trabajo coordinado.
- IA bajo dirección humana (CLAUDE.md §1). Voz autoral filosófica de Jacob NO suplantada.
