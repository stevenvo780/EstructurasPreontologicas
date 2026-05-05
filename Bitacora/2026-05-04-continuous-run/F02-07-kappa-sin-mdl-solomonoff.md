# F02-07 — κ sin reconocer la tradición Kolmogorov–MDL

**Fecha:** 2026-05-04
**Origen:** Hallazgo `adversarial-reviewer` cap 02 (2026-05-05).
**Archivo señalado:** `02-fundamentos/02-epistemologia-de-la-compresion.md` §3 (definición de κ desde línea 43).
**Estado:** `needs_human` (decisión filosófica de delimitación + verificación de paginación primaria).

---

## (a) Verificación de la afirmación adversarial

**Afirmación:** la sección §3 ("Compresión") define κ como *"operación que reemplaza una subestructura compleja por una unidad operativa más tratable, cuando el detalle interno no produce diferencia inferencial relevante para la pregunta Q"* (línea 47) y enuncia cuatro condiciones de legitimidad (§3.2, líneas 51-58), pero **no menciona** la tradición formal antecedente:

- **Solomonoff (1964)** — *"A Formal Theory of Inductive Inference"*, Information and Control 7(1): 1-22 y 7(2): 224-254. Inducción universal como mínima descripción algorítmica.
- **Kolmogorov (1965)** — *"Three approaches to the quantitative definition of information"*, Problems of Information Transmission 1(1): 1-7. Complejidad K(x) = longitud del programa más corto.
- **Rissanen (1978)** — *"Modeling by shortest data description"*, Automatica 14(5): 465-471. MDL como criterio de selección de modelo.
- **Grünwald (2007)** — *The Minimum Description Length Principle*, MIT Press, cap. 1.

La definición §3.1 y las condiciones (1)-(2) ("pierde detalle irrelevante", "conserva dependencias decisivas") son **isomorfas** al núcleo MDL: minimizar `L(M) + L(D|M)` preservando información predictiva. La condición (3) ("mejora inferencia/intervención") añade el componente intervencionista pearliano que sí está reconocido en línea 109. La condición (4) (reapertura ε) es genuinamente propia.

**Veredicto:** la objeción adversarial es **válida**. La definición §3.1 se presenta como si fuera estipulación interna de la tesis, sin reconocer que las condiciones (1)-(2) llevan 60 años codificadas en la tradición Solomonoff–Kolmogorov–Rissanen–Grünwald. Esto cumple el criterio F6 (cita decorativa por omisión: invocar implícitamente el contenido de una tradición sin engagement con sus textos).

**Hueco numérico llamativo:** la sección salta de §3.3 (línea 60) a §3.5 (línea 66) — **§3.4 no existe en el archivo**. El reviewer adversarial parece haber identificado correctamente el slot vacío como lugar natural para la delimitación faltante.

## (b) Propuesta de edición concreta

Insertar nueva subsección **§3.4 "Delimitación frente a la tradición Kolmogorov–MDL"** entre líneas 64 y 66 del archivo `02-fundamentos/02-epistemologia-de-la-compresion.md`. Borrador (DRAFT-AI, 90% asistencia / 10% Jacob — corte filosófico final pendiente de Jacob):

```markdown
### 3.4. Delimitación frente a la tradición Kolmogorov–MDL

Las condiciones §3.2(1)-(2) — pérdida de detalle irrelevante con
preservación de dependencias decisivas — no son originales de esta
tesis. Son la formulación operativa, en lenguaje del aparato EDI,
del núcleo de una tradición de seis décadas:

- **Solomonoff (1964)** define la inducción universal como búsqueda
  del programa más corto que reproduce los datos observados.
- **Kolmogorov (1965)** formaliza la complejidad K(x) como longitud
  mínima de descripción algorítmica.
- **Rissanen (1978, Automatica 14: 465-471)** introduce el principio
  MDL: el mejor modelo es el que minimiza L(M) + L(D|M),
  i.e. descripción del modelo más descripción de los datos dado el
  modelo. La condición §3.2(1) ("pierde detalle irrelevante") es
  exactamente el término L(M) bajo presión a la baja; la §3.2(2)
  ("conserva dependencias decisivas") es L(D|M) acotado.
- **Grünwald (2007, *The Minimum Description Length Principle*,
  MIT Press, cap. 1)** sintetiza MDL refinado y su relación con
  inferencia bayesiana y selección de modelos.

**Qué aporta esta tesis sobre esa tradición** (delimitación honesta):

1. La condición §3.2(3) **intervencionista** — la compresión debe
   mejorar predicción *o intervención* — no está en MDL clásico, que
   es puramente predictivo-descriptivo. Procede de Pearl (cap §3.6) y
   se operacionaliza en EDI como ablación del acoplamiento ODE→ABM.
2. La condición §3.2(4) **reapertura ε** — operador inverso explícito
   bajo cambio de pregunta Q — añade la dimensión pragmática
   peirceano-brandomiana ausente en MDL.
3. El **acoplamiento de κ con sondas físicas dimensionadas** (no con
   códigos algorítmicos arbitrarios) introduce una restricción
   material que MDL clásico, agnóstico al sustrato, no impone.

**Qué NO aporta esta tesis sobre esa tradición** (concesión honesta):

- el núcleo formal "comprimir preservando lo decisivo" es Rissanen
  1978, no esta tesis;
- la noción de "mínima descripción suficiente" es Kolmogorov 1965,
  no esta tesis;
- la búsqueda inductiva del modelo más simple compatible con los
  datos es Solomonoff 1964, no esta tesis.

El aporte original de κ está en (1)-(3) arriba, no en la idea misma
de comprimir-conservando.
```

## (c) Costo argumentativo declarado

Esta delimitación **debilita** retóricamente la sección 3 (κ deja de leerse como innovación conceptual y queda como reformulación operativa de MDL + extensiones intervencionistas). El costo es real y debe asumirse:

- **Costo retórico:** un lector apresurado puede concluir "esto es solo MDL en jerga propia". La defensa frente a esa lectura está en (1)-(3) de la propuesta: el componente intervencionista, la reapertura ε, y el acoplamiento con sondas físicas dimensionadas son originales y operativamente verificables.
- **Costo de continuidad:** las menciones a κ en cap 03-04 y cap 05 no requieren ajuste estructural, pero conviene revisar si en algún punto del manuscrito se afirma "κ es novedad conceptual" — esa frase, si existe, debe atemperarse.
- **Beneficio compensatorio:** la honestidad metodológica (CLAUDE.md §1, §5) gana. Citar la tradición con paginación cierra una vía de ataque adversarial recurrente y alinea el capítulo con los estándares de §5 (cita textual con paginación o no cita).

## Bloqueo: paginación primaria

**Crítico antes de cerrar:** los PDFs de Rissanen 1978, Grünwald 2007, Solomonoff 1964 y Kolmogorov 1965 **NO están en `07-bibliografia/`** (verificado: `ls 07-bibliografia/ | grep -iE "rissanen|grunwald|solomonoff|kolmogorov|mdl"` = vacío). Las páginas citadas (Automatica 14:465-471, Grünwald cap 1) son referencias bibliográficas estándar verificables, pero **CLAUDE.md §5 exige cita textual con paginación verificada en PDF**. Antes de hacer la edición:

1. ejecutar `/fetch-biblio rissanen-1978-mdl` y `/fetch-biblio grunwald-2007-mdl-principle` para incorporar los PDFs;
2. extraer cita literal de Rissanen 1978 sobre minimización conjunta y cita literal de Grünwald 2007 cap. 1 sobre la formulación moderna de MDL;
3. solo entonces sustituir en el borrador las referencias parafrásticas por citas literales paginadas.

## Acción para el daemon / siguiente pasada

1. **Tarea derivada `B-T-fetch-mdl`** (ejecutable por el harness):
   `/fetch-biblio` para Rissanen 1978 y Grünwald 2007 → depositar en `07-bibliografia/`.
2. **Tarea derivada `B-E-cita-mdl`** (ejecutable tras (1)):
   extraer cita literal con `@citation-agent` desde los PDFs descargados.
3. **Tarea `H-J-delim-kappa`** (`needs_human`, firma de Jacob):
   aprobar el corte filosófico de §3.4 — concretamente la lista de aportes (1)-(3) y la lista de no-aportes. Ningún sub-agente cierra esa decisión.

**Estado final:** `needs_human` — propuesta lista, edición bloqueada por paginación primaria pendiente y por firma filosófica de Jacob sobre la delimitación.
