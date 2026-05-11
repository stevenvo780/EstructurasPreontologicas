---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 05-aplicaciones/00-criterios-de-admision.md (§1) ; 05-aplicaciones/07-mapa-aplicaciones-corpus.md:11,17
hallazgo: Bitacora/2026-05-04-continuous-run/F05-08-criterios-admision-post-hoc.md
tipo: insercion_nota_circularidad + correccion_extension (coordinada con F4-F05-09)
---

## Diagnóstico

Los 14 componentes del *dossier de anclaje* (cap 05-00 §1, vv. 1-14) coinciden punto por punto con los elementos que cap 05-05 (Warren 2006) ya provee, en el mismo orden y con la misma granularidad. La auditoría muestra que cada criterio del cap 05-00 §1 tiene correspondencia textual exacta en una sección del cap 05-05; por construcción, el caso ancla satisface el criterio. Aplicación a 5 casos EDI muestreados (16, 04, 05, 23, 30) confirma que ninguno alcanza más de 6/14 con contenido sustantivo; el caso ancla obtiene 13/14 — la distancia es sistemática y se concentra en los criterios donde Warren tiene material publicado independiente del aparato. Esto es **ad hoc rescue tipo 3** (Lakatos 1970). Además existe contradicción interna entre cap 05-00 (un único demostrativo: 05-05) y cap 05-07 línea 17 (30 casos como "Modo demostrativo con dossier completo").

## Verificación

- Mapeo uno-a-uno entre 14 criterios de cap 05-00 y secciones del cap 05-05 documentado en F05-08 §A.
- Aplicación de los 14 criterios a 5 casos EDI: conteos 6/14 (16, 04, 30), 4/14 (05), 3/14 (23) vs 13/14 del caso ancla. La distancia se concentra en los criterios 4, 7, 9, 10, 12 — donde Warren provee material publicado.
- Contradicción 05-00 vs 05-07:
  - `05-aplicaciones/00-criterios-de-admision.md:67-71`: único caso demostrativo = 05-05.
  - `05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md:5`: "el único caso del manuscrito que entra en modo demostrativo".
  - `05-aplicaciones/07-mapa-aplicaciones-corpus.md:17`: "30 casos Modo demostrativo (con dossier completo)".
- Lakatos 1970, *Falsification and the Methodology of Scientific Research Programmes*, sobre ad hoc rescue: PDF de Lakatos 1978 presente en `07-bibliografia/Lakatos - Methodology of Scientific Research Programmes (1978).pdf`; la paginación literal de la clasificación de ad hoc₁/ad hoc₂/ad hoc₃ debe verificarse contra la edición disponible (B-T:verify-lakatos-ad-hoc-tipo-3).

## Texto propuesto (voz autoral filosófica de Jacob)

**Insertar en `05-aplicaciones/00-criterios-de-admision.md` §1 (al inicio de la enumeración de los 14 componentes) un párrafo de costo declarado:**

> **Nota sobre la genealogía de los 14 componentes.** Los catorce componentes que organizan este dossier fueron extraídos como **abstracción del caso ancla** (cap 05-05, Warren 2006). La adecuación del caso ancla a estos criterios es por construcción y no constituye evidencia independiente de la potencia del marco. La asistencia técnica que redactó borradores y la dirección filosófica de la tesis han verificado este punto: cada componente del dossier tiene correspondencia textual en una sección del cap 05-05 (la auditoría detallada está en `Bitacora/2026-05-04-continuous-run/F05-08-criterios-admision-post-hoc.md`). Lakatos (1978, *The Methodology of Scientific Research Programmes*) llamaría a esto **ad hoc rescue tipo 3**: una rejilla evaluativa diseñada para que sólo el caso paradigmático la satisfaga. La tesis declara el costo y opta por la salida más honesta operativamente: los demás casos del corpus entran en **modo programático** (dossier técnico ejecutado y reproducible) no porque sean ontológicamente menos firmes, sino porque carecen de un caso paradigmático con las catorce dimensiones desarrolladas independientemente. Los catorce componentes funcionan, por tanto, como **agenda regulativa para futuros casos paradigmáticos**, no como medida de adecuación ontológica de los 30 casos ejecutados.

**Corregir en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:11,17` la equivocidad léxica (coordinado con F4-F05-09):**

> *Antes (línea 17):* "Modo demostrativo (con dossier completo): 30 casos"
>
> *Después:* "**Modo técnico-ejecutado** (dossier EDI completo, `metrics.json` reproducible bajo el protocolo C1-C5): 30 casos. **Modo demostrativo en sentido estricto** (14/14 componentes del dossier de anclaje del cap 05-00 §1, con material publicado independiente del aparato): 1 caso (05-05 Warren). La distinción es operativa: el primer modo asegura reproducibilidad técnica, el segundo asegura adecuación filosófica plena del aparato a un caso paradigmático."

Y añadir nota bajo la Tabla 5.7.1:

> 'Modo técnico-ejecutado' indica que el caso fue corrido con el protocolo C1-C5 y produce `metrics.json` reproducible. **No equivale a 'demostración positiva del aparato'**: los Bloques V-VII (Trend, Null, Controles) no instancian acoplamiento detectable; funcionan como casos de no-aplicabilidad, falsación local o controles correctamente rechazados.

## Texto a reemplazar / propagar

- Inserción del bloque "Nota sobre la genealogía de los catorce componentes" en `05-aplicaciones/00-criterios-de-admision.md` §1.
- Sustitución textual en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:11,17` (coordinada con F4-F05-09: la edición textual mínima propuesta allí se solapa con esta; aplicar como una sola pasada).
- Recalcular cualquier conteo agregado que se apoye en "30 demostrativos" (especialmente cap 06 y defensas cortas).

## Costo argumentativo declarado

- La tesis pasa de "30 demostrativos en 7 dominios" a "1 demostrativo + 30 técnico-ejecutados + n programáticos". La cifra retórica baja, la honestidad sube.
- El único demostrativo es además circular por construcción; la nota declara la circularidad explícitamente y la convierte en agenda regulativa, no en evidencia.
- La defensa oral debe explicitar que el aparato EDI (validate.py + C1-C5) **no equivale al dossier de anclaje filosófico** — son dos verificaciones distintas con dos extensiones distintas: la técnica cubre 30 casos, la filosófica plena cubre 1.
- Sin la nota: F05-08 queda como vector publicable de objeción Lakatosiana directa. Con la nota: la tesis transforma una vulnerabilidad oculta en concesión declarada (CLAUDE.md §3 y §7).

## Tarea derivada

- Si Jacob escoge la **Opción C del informe origen** (reducir los 14 a un subconjunto verdaderamente discriminante de ~5-7 criterios derivados de filosofía de la ciencia, no de Warren), abrir tarea B-F separada con el subconjunto candidato; el presente borrador asume la salida **Opción A** (asumir y declarar el ad hoc).
