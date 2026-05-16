---
paths:
  - "00-proyecto/**/*.md"
  - "01-marcos/**/*.md"
  - "02-fundamentos/**/*.md"
  - "03-corpus/**/*.md"
  - "04-debates/**/*.md"
  - "05-aplicaciones/**/*.md"
  - "06-cierre/**/*.md"
  - "08-anexos/**/*.md"
  - "TesisFinal/**/*.md"
---

# Edición de prosa de la tesis

Estás editando prosa filosófica del manuscrito. Cargas reglas que solo aplican aquí.

## La voz es de Jacob

Tu rol técnico no sustituye su voz. Si redactas prosa filosófica final, márcala como `BORRADOR-IA` con `requires: H-J*` para firma humana. Para engagement sustantivo con autor primario (Bunge, Dennett, Simondon, etc.) delega a `@philosophical-reader` que produce DRAFT-AI con cita verbatim paginada.

## Antes de cerrar una sección

Tres preguntas hostiles que debe sobrevivir:

1. Si retiras el adjetivo ("brutalmente honesto", "anti-paper-science", "decisivo"), ¿sobrevive la oración?
2. ¿Cada autor citado aparece con cita textual paginada contra PDF en `07-bibliografia/`? Si no → es cita decorativa = fallo F6.
3. ¿Cada cifra que la prosa menciona se reproduce con `python3 09-simulaciones-edi/<caso>/src/validate.py`? Si la prosa contradice `metrics.json`, gana el JSON.

## Antipatrones a borrar del propio output

- **Versionología:** "V_FINAL", "8/8 verdes", "42/42 ROBUSTO" como totem de completud.
- **Manierismo:** "brutalmente honesto", "honestidad simétrica", "anti-paper-science".
- **Plantillas spam:** mismas tres líneas repetidas en >3 archivos.
- **Categorías inventadas** para forzar que las cifras cuadren.
- **Documentos meta** que duplican en prosa los outputs JSON.

Si reconoces alguno en tu output, **bórralo antes de mostrar**. No lo defiendas.

## Tres marcos > 40 casos

La tesis defiende ontología, epistemología, metodología. Los 40 casos del corpus son **justificación operativa**, no la tesis. No escribir como si los 40 casos fueran la tesis. Si una sección invierte esa relación, recortarla.

## Concesiones explícitas

Cada vez que el manuscrito hace una concesión filosófica (e.g., "esto no se aplica a casos cuánticos", "la métrica EDI no captura X"), déjala visible. La fortaleza está en declarar los costos; ocultarlos es debilidad.

## Glosario operativo

`00-proyecto/07-glosario-operativo.md` define términos centrales. Antes de renombrar "realismo estructural moderado", "self-organization", "preontológico", "EDI", "C1-C5": verificar el glosario. En particular:

- "realismo estructural moderado" se usa en sentido **operativo no-Ladyman** (NO importar OSR de Ladyman & Ross).
- "self-organization" debe anclarse en Maturana-Varela o Haken o sustituirse por "estabilización dinámica".
