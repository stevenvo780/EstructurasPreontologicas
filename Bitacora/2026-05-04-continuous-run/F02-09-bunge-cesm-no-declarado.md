# F02-09 — Bunge CESM importado sin declarar costo

**Fecha:** 2026-05-04
**Origen:** Hallazgo de adversarial-reviewer cap02 (2026-05-05).
**Archivo afectado:** `02-fundamentos/01-ontologia-material-relacional.md` §1.3, línea 189.
**Estado:** `needs_human` (decisión filosófica de qué se asume / qué no de CESM corresponde a Jacob).

---

## (a) Verificación de la afirmación

Texto actual (línea 189):

> **Bunge.** En *Treatise on Basic Philosophy* vol. 3 (1977, *Ontology I: The Furniture of the World*, p. 27), Bunge enuncia el principio que la tesis recoge: *"to be is to be a system or a component of one"*. El sustrato dinámico de la tesis encarna esta consigna sin reducirla a inventario: cada componente es a su vez sistema con composición, entorno, estructura y mecanismo (Bunge 1979, vol. 4, p. 4-5). La diferencia operativa con Bunge es el filtro empírico: Bunge define qué cuenta como sistema; la tesis añade el procedimiento (dossier de 14 componentes + EDI) para admitir sistemas concretos en cada caso de estudio.

**Hechos verificables:**
- En `07-bibliografia/` **NO** existen los volúmenes 3 (1977) ni 4 (1979) del *Treatise*. Disponibles: *La investigación científica* (2, 3, 4), *La ciencia, su método y su filosofía*, *Buscar la filosofía en las ciencias sociales*, *Ser, Saber, Hacer*, *Estudio de las interpretaciones de la mecánica cuántica*.
- Las paginaciones reportadas (vol.3 p.27; vol.4 pp.4-5) **no son verificables localmente**. Esto cae bajo CLAUDE.md §5: cita textual con paginación. Marcar como deuda de verificación bibliográfica (B-T*).
- El slogan "to be is to be a system or a component of one" es atribución estándar a Bunge (vol.3 *Ontology I*, cap.1), pero la página exacta (27) requiere comprobación contra el PDF original — pendiente.

**Hallazgo adversarial central:** la línea 189 **invoca** CESM (composición, entorno, estructura, mecanismo) como si fuese decoración terminológica del slogan, pero **no declara**:

1. Qué *exactamente* la tesis adopta de la cuádrupla CESM (¿solo composición+estructura? ¿también mecanismo?).
2. Qué *no* asume del aparato bungeano: específicamente, **el realismo causal-mecanicista fuerte** que Bunge defiende en *Treatise* vol.4 cap.3 (la noción de "mecanismo" como proceso causal específico que produce el comportamiento del sistema). La tesis trabaja con dependencias detectadas por intervención y covarianza condicional (§1.2), que es más débil que mecanismo bungeano.
3. La referencia a "Bunge 1977 cap.3 pp.110-120" del acceptance del adversarial corresponde, según el contexto temático, a la elaboración de "system" en *Ontology I* — paginación a verificar contra PDF.

**Costo no declarado:** importar el slogan sin disociarlo del CESM completo crea ambigüedad sobre si la tesis se compromete con (i) materialismo sistémico bungeano (mecanismo causal específico requerido para cada sistema) o (ii) una versión más débil (dependencias multi-tipo, no necesariamente mecánicas). El capítulo 02 sostiene (ii) en §1.2, pero §1.3 sugiere (i) sin negarlo.

## (b) Propuesta de edición concreta — DRAFT-AI, requiere firma Jacob

Reescritura propuesta de §1.3 párrafo Bunge:

> **Bunge.** En *Treatise on Basic Philosophy* vol. 3 (1977, *Ontology I: The Furniture of the World*), Bunge enuncia un principio que la tesis recoge en versión restringida: *"to be is to be a system or a component of one"*. La tesis adopta de Bunge **dos** elementos del esquema CESM (composición-entorno-estructura-mecanismo, *Treatise* vol. 4, 1979): la **composición** (un sistema tiene partes identificables) y la **estructura** (relaciones entre las partes y con el entorno). **No adopta** el compromiso bungeano fuerte con el **mecanismo** como proceso causal específico productor del comportamiento — la tesis trabaja con un repertorio plural de dependencias (mecánicas, funcionales, históricas, semióticas, §1.2), detectadas por intervención y covarianza condicional, que es estrictamente más débil que el "mecanismo" de Bunge 1979 cap.3. Tampoco se importa el realismo materialista monista de Bunge en su totalidad: la tesis es realismo estructural moderado en sentido operativo (glosario §"realismo estructural moderado"), no materialismo sistémico bungeano. La diferencia operativa con Bunge, una vez declarado el costo, es el filtro empírico: Bunge define qué cuenta como sistema por estipulación ontológica; la tesis añade el procedimiento (dossier de 14 componentes + EDI) que decide caso por caso. **Deuda bibliográfica:** paginación exacta de las citas del *Treatise* vol.3 y vol.4 pendiente — los PDFs no están en `07-bibliografia/` (B-T pendiente).

**Costo argumentativo declarado:**

- Se gana: claridad sobre qué se importa (C+E del CESM) y qué no (M en sentido fuerte + materialismo bungeano).
- Se pierde: la apariencia de respaldo total de un autor canónico. Bunge no firmaría esta versión "blanda" — la tesis no debería aparentar que sí.
- Se gana en honestidad metodológica (CLAUDE.md §3): el costo declarado es virtud.

## (c) Decisión

`needs_human` — Jacob debe firmar:
1. ¿Confirmar adopción restringida (solo C+E)? ¿O sí adopta también una versión debilitada de mecanismo?
2. Verificar paginaciones contra los volúmenes originales (acceso institucional U. Antioquia).
3. Aprobar reescritura propuesta o ajustar.

Tareas operativas derivadas:
- **B-T (pendiente):** descargar/digitalizar *Treatise* vol.3 y vol.4 a `07-bibliografia/` para verificar paginación.
- **H-J (decisión filosófica):** firma sobre alcance del préstamo CESM.

NO se edita Tesis.md ni `02-fundamentos/01-ontologia-material-relacional.md` desde este reporte. La edición queda como propuesta DRAFT-AI hasta firma de Jacob.
