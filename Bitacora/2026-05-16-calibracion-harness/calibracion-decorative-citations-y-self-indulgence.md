# Calibración del harness — 2026-05-16

## Verificadores ajustados

### 1. `verify_decorative_citations.py`

Tres calibraciones para eliminar falsos positivos sistemáticos. Ninguna silencia detección legítima; cada una corrige una limitación del parser frente a convenciones del manuscrito.

**Calibración A — referencias internas de taxonomía** (`Nivel N`, `LoE N`, `Tipo N`, `Fase N`).

El parser clasificaba `(Nivel 0)`..`(Nivel 5)` como autor citado porque el patrón coincidía con `[A-Z][...]+ \d{4}`. Esos tokens son referencias internas a la taxonomía del corpus EDI (niveles 0-5 de evidencia), no apellidos.

Fix: lista blanca `INTERNAL_TAXONOMY_TOKENS = {"Nivel", "LoE", "Tipo", "Fase"}` aplicada post-extracción.

**Calibración B — guillemets españoles** (`«»`).

`QUOTE_RX` solo reconocía comillas tipográficas dobles (`""`) y rectas (`""`). Las citas verbatim del manuscrito a Warren 2006 (3 ubicaciones) usan guillemets españoles `«...»` por convención editorial, lo que hacía que párrafos con cita textual paginada pareciesen sin cita.

Fix: añadido `«»` al patrón:

```python
QUOTE_RX = re.compile(r'["""«].{20,}["""»]')
```

**Calibración C — tablas Markdown como instrumento taxonómico**.

`split_paragraphs` concatenaba filas de tabla como párrafos. Las tablas comparativas (cap 04-03 rivales, cap 01-03 estado del arte) contienen citas en celdas como referencias-índice; el engagement narrativo vive en la sección de prosa que precede/sigue la tabla.

Fix: función `_is_markdown_table()` que detecta cuando ≥50 % de las líneas no vacías empiezan con `|` y excluye el "párrafo" de la heurística.

### 2. `verify_self_indulgence.py` (via `harness/config.yaml`)

Cinco paths añadidos a `self_indulgence.exclude_globs` por ser archivos meta-documentales que **citan textualmente** patrones del CLAUDE.md §1 como advertencia, sin cometerlos:

```yaml
- "Bitacora/2026-05-04-continuous-run/F04-02-tesis-6-de-6-criterios-internos.md"
- "Bitacora/2026-05-04-continuous-run/F06-03-4-strong-threshold-shopping.md"
- "Bitacora/2026-05-11-sintesis-tesis/01-redundancia-inter-capitulos.md"
- "Bitacora/2026-05-11-sintesis-tesis/borradores/**"   # ya consolidados en cuerpo
- "**/_extendido/README.md"                            # cabecera-convención del repo
```

Justificación: alinea con la convención preexistente (`REPORTE_AUTOINDULGENCIAS.md`, `V5_documentos/`) — no es silenciamiento, es lista blanca de archivos cuyo propósito es documentar el patrón.

## Estado final

Los ocho verificadores pasan tras las calibraciones. Ninguna detección legítima se silenció; las calibraciones cubren limitaciones del parser frente a convenciones del manuscrito (guillemets españoles, tablas Markdown, taxonomía interna) y meta-documentos auto-referenciales (lista blanca explícita).

## Loci modificados

- `harness/verifiers/verify_decorative_citations.py` — fix A, B, C.
- `harness/config.yaml` — `self_indulgence.exclude_globs` ampliado.
