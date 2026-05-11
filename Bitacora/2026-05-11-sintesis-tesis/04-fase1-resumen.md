# Fase 1 — Síntesis de tesis (resumen 2026-05-11)

## Resultado neto

- **Tesis.md**: 9173 (stale) → 9266 líneas tras `build.py` + fix tablas. El stale subestimaba en ~400 líneas; el manuscrito real era ~9570 antes del fix.
- **Reducción real por fix de tablas duplicadas**: **−304 líneas** (de 9570 a 9266) eliminando 96 marcadores `**Tabla X.Y.Z.**` duplicados consecutivos en 33 archivos.
- **Infraestructura `_extendido/` lista**: 6 directorios placeholder + endpoints web + convención canónica.

## F1-A — Web endpoints `_extendido/` (✓ completado)

**Sub-carpetas creadas** (con `README.md` mínimo + `.gitkeep`):
- `00-proyecto/_extendido/` (canonical README)
- `02-fundamentos/_extendido/`
- `03-formalizacion/_extendido/`
- `04-debates/_extendido/`
- `05-aplicaciones/_extendido/`
- `06-cierre/_extendido/`

**Convención** (en `00-proyecto/_extendido/README.md`):
- Cada `<cap>/_extendido/<tema>.md` empieza con frontmatter `--- title: ... extends: <cap>/<archivo>.md ---`.
- NO entran al ensamblado `Tesis.md` (verificado: el `rglob("*.md")` de `_collect_chapter` excluye `_extendido`).
- Web los expone vía `/api/chapters/{slug}/extras` (listado) y `/api/chapters/{slug}/extras/{name}` (contenido completo con TOC).

**Código tocado**:
- `web_tesis/data.py`: funciones nuevas `_parse_extra_frontmatter`, `_collect_chapter_extras`, `resolve_chapter_extra`. `_compute_dataset_mtime` invalida cache si cambian extras.
- `web_tesis/app.py`: 2 endpoints nuevos con defensa contra path-traversal.

**Smoke E2E pasó**: server en puerto 8099 responde 200 a listing, 404 a inexistentes, lista vacía cuando dir vacío. `python3 TesisFinal/build.py` sigue funcionando.

**Bug latente arreglado** (incidental): `_chapter_full_dict` leía `d.get("path")` pero `_collect_chapter` no guardaba `path`. Añadido `"path": rel` al dict del doc.

## F1-B — Bug numeración de tablas (✓ completado)

**Causa raíz**: `scripts/number_tables.py` con regex single-level (`\d+\.\d+`) que no reconocía labels multi-level previos, apilando duplicados en cada corrida.

**Auditoría**: 96 ocurrencias en 33 archivos (60 triplicados + 36 duplicados). Reporte literal en `Bitacora/2026-05-11-sintesis-tesis/03-tabla-numeracion-hits.md`.

**Fix estructural**: añadida `_dedupe_consecutive_labels()` en `scripts/number_tables.py:71-103`. Idempotente: re-ejecutar el script no re-introduce duplicados.

**Edición**: 33 archivos, **312 líneas eliminadas** (2 líneas por label excedente: label + blanco).

**Verificación**:
- `Tesis.md` regenerada: 9266 líneas (−304 vs rebuild stale).
- Numeración monotónica verificada: cero gaps, cero duplicados de numeración.
- `python3 scripts/number_tables.py` idempotente: `Total: 0 tablas + 0 figuras`.

## F1-C — Denominador 0/1500 → 0/2000 (BLOQUEADO por firma Jacob → H-J7)

**Verificación numérica**: confirmada bit-a-bit contra `Bitacora/2026-04-28-cierre-severo/{N1,V4_06,N5}_resultados.json`. Suma real: 500+500+1000 = **2000**, no 1500. Wilson 95% CI con n=2000, k=0: **[0, 0.00191]**.

**7 ubicaciones afectadas** (todas confirman "0/1500"):
- `06-cierre/01-conclusion-demostrativa.md:5,174,246,253`
- `06-cierre/04-versiones-cortas-defensa.md:25,60,114`
- `02-fundamentos/01-ontologia-material-relacional.md:118`

**Estado**: edición aplicada por agente, revertida por linter del harness (correctamente — toca defensa argumental). Registrada como **H-J7** en `TAREAS_PENDIENTES.md`. Tres salidas para Jacob:
- (a) Aceptar la corrección 0/2000 — recomendado por verificación.
- (b) Mantener 0/1500 si hay agregación distinta no detectada.
- (c) Eliminar el numeral y reformular cualitativamente.

## Cosas que NO se hicieron en Fase 1 (deuda explícita)

- Caso 19 metrics.json inconsistente (TENG-05) → re-ejecutar `validate.py` (B-T5, ya en `TAREAS_PENDIENTES.md`).
- AU-3 baselines ARIMA/VAR superan modelo → reconocimiento honesto en `06-cierre/01` §3. Decisión filosófica → Fase 3.
- AU-5 AUC-ROC=0.886 vs ARIMA circular → reformulación → Fase 3.
- F03-07 Ladyman & Ross mal clasificados → reescritura en `03-formalizacion/01:260-262` y `03-formalizacion/03:254-256` → Fase 3.
- Material extendido (e.g., desarrollos rival-por-rival, casos detallados) → migrar a `<cap>/_extendido/` → Fase 2.

## Próximo (Fase 2)

3 fusiones de capítulos identificadas como D.1-D.4 en `01-redundancia-inter-capitulos.md`:
- D.1: `06-cierre/02 + 04 + 05` (triple solapamiento defensa oral) → −200/300 líneas.
- D.2: `04-debates/01 ↔ 03` (tablas tesis/rival duplicadas) → mover detalle rival-por-rival a `04-debates/_extendido/`. −250 líneas.
- D.3: `04-debates/02` subsumido por `04-debates/05` → fusión o reducción a §"Riesgos heredados". −150 líneas.
- D.4: `00-proyecto/01 + 03` (estructura vs plan de capítulos) → revisar solapamiento.

Cada fusión producirá **BORRADOR-IA** con `requires: H-J*` (firma autoral de Jacob).
