# F02-10 — Doble rótulo "realismo estructural" en cap 02-02

**Fecha:** 2026-05-04
**Sub-agente:** harness headless (auditoría F02-10)
**Estado:** `needs_human` (firma Jacob requerida — toca voz filosófica)

## (a) Verificación de la afirmación

Confirmado el doble rótulo en `02-fundamentos/02-epistemologia-de-la-compresion.md`:

- **Línea 93 (§3.5.3 "La sonda como representación"):**
  > "¿Qué es una sonda ODE en relación con el fenómeno que describe? La tesis adopta **realismo estructural representacional**:"
  Bullets: NO copia / NO ficción útil / sí homomorfismo parcial preservando dependencias decisivas bajo `Q`. Apoyo: Sellars 1956 §41 (representación inferencial-funcional) + Pearl (estructura mínima suficiente).

- **Línea 154 (§6 "Por qué esto no es constructivismo arbitrario"):**
  > "Por eso la tesis defiende **realismo estructural moderado**: los recortes son construidos, pero algunos son mejores porque siguen mejor la estructura real."

### Auditoría de canonicidad

- **Rótulo canónico:** "realismo estructural moderado" está definido en `00-proyecto/07-glosario-operativo.md` líneas 33 y 36, con la cláusula explícita de uso **operativo no-Ladyman** (no-importación de OSR de Ladyman & Ross 2007). Aparece en abstract, plan de capítulos, ontología (cap 02-01), aplicaciones (05-02, 05-05), introducción (00).
- **Rótulo no-canónico:** "realismo estructural representacional" aparece **solo una vez en todo el manuscrito** — en cap 02-02 §3.5.3 línea 93. No hay entrada de glosario, ni anclaje a literatura primaria que use ese término técnico (Sellars no usa la frase; Pearl tampoco). Es una invención local del párrafo.

### Diagnóstico

El §3.5.3 introduce un segundo rótulo filosófico que:
1. duplica funcionalmente "realismo estructural moderado" (los bullets — homomorfismo parcial, dependencias decisivas, tolerancia explícita — son exactamente la posición moderada operativa del glosario);
2. carece de soporte primario (Sellars/Pearl no autorizan la frase exacta);
3. confunde al lector porque dentro del mismo capítulo §6 retoma el rótulo canónico sin advertir la sinonimia o diferencia.

Esto **duplica B-F2** (TAREAS_PENDIENTES.md línea 59), que pide propagar la convención del rótulo canónico al cuerpo.

## (b) Propuesta de edición

**Opción A (recomendada — mínima invasión, alinea con B-F2):**
Reemplazar en línea 93:

```diff
- ¿Qué es una sonda ODE en relación con el fenómeno que describe? La tesis adopta **realismo estructural representacional**:
+ ¿Qué es una sonda ODE en relación con el fenómeno que describe? La tesis lo articula bajo el **realismo estructural moderado** (glosario §"realismo estructural moderado", uso operativo no-Ladyman) en su faceta representacional:
```

Justificación: el contenido operativo del párrafo (NO copia / NO ficción / sí homomorfismo parcial bajo `Q`) ya está cubierto por la posición canónica; basta señalar que aquí se enfoca su faceta representacional sin acuñar un rótulo nuevo. Resultado: 0 ocurrencias del no-canónico, glosario intacto, B-F2 progresa sin volver a abrirse.

**Opción B (si Jacob quiere preservar la distinción):**
Mantener ambos rótulos pero (i) añadir entrada de glosario que distinga "realismo estructural moderado" (posición filosófica global de la tesis) vs. "realismo estructural representacional" (sub-modo aplicado a sondas ODE), (ii) declarar literatura primaria que autorice este último (candidato: Bueno & French 2018 *Applying Mathematics*, *partial structures* — no es Sellars). Costo: introduce un término técnico nuevo que requiere defensa adicional en defensa oral; profesor podría preguntar "¿qué autor sostiene esto exactamente?".

**Opción C (radical):**
Reemplazar §3.5.3 por subsumirlo en cap 02-01 §13 (donde ya se discute realismo estructural). Costo: rompe la lógica local del cap 02-02 (3.5.1 sintáctica/semántica → 3.5.3 sonda-como-representación → 3.5.4 prohibición de sustitución nominal).

## (c) Costo argumentativo declarado

- **Si se adopta A:** se pierde el matiz "representacional" como sub-rótulo; se gana adherencia estricta al glosario y a B-F2. La tesis no pierde contenido — los cuatro bullets siguen ahí — solo el adjetivo redundante.
- **Si se adopta B:** la tesis carga un término técnico extra que debe defenderse con literatura primaria explícita. Si no se trae Bueno-French o equivalente, la cita de Sellars+Pearl no autoriza el rótulo y queda como cita decorativa (F6 según CLAUDE.md §5).
- **Riesgo común:** §3.5.3 invoca Sellars 1956 §41 con paginación implícita ("§41"); B-F5 ya audita citas decorativas, conviene verificar que Sellars §41 efectivamente autoriza "representación inferencial-funcional" antes de cualquier elección.

## Marca

`needs_human` — Jacob debe elegir entre A/B/C. La asistencia recomienda A por ser la opción que cierra B-F2 sin abrir frentes nuevos.

## Acceptance check

- [ ] Un único rótulo en cap 02-02 → pendiente de elección Jacob
- [ ] Entrada de glosario distinguiendo ambos (solo si B) → pendiente
- [ ] 0 ocurrencias de "realismo estructural representacional" → actualmente 1 (línea 93)
