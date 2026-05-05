# F03-11 — Replicabilidad por tercero: afirmada, no testada

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap03 (2026-05-05)
**Status:** `needs_human` (requiere firma H-J* de Jacob)

## (a) Verificación de la afirmación

Archivo: `03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md:6`

Cita textual:

> "Su criterio de cierre no es la satisfacción del autor sino la replicabilidad por tercero competente. Sin esta auditoría, la tesis sigue siendo programa filosófico; con ella, se convierte en programa de investigación reproducible."

**Hallazgo:** la afirmación es modal-normativa ("criterio de cierre es replicabilidad por tercero") pero **no se ha ejecutado ninguna replicación independiente** del protocolo de nueve fases por un tercero externo al equipo Jacob+Steven. Búsqueda en el repositorio:

- `09-simulaciones-edi/` ejecuta los 40+ casos con seeds fijos. Esto es **auto-replicación con seed = replicación numérica**, no replicación por tercero competente en el sentido de Collins (1985, *Changing Order*: tacit knowledge, experimenter's regress).
- No existe registro en `Bitacora/` de un investigador externo aplicando las nueve fases a una categoría candidata y produciendo una decisión ontológica trazable.
- El "tercero competente" que el texto invoca como criterio de cierre es contrafáctico: el protocolo está **diseñado para admitir replicación**, pero la replicación misma es una promesa, no un hecho.

La objeción de Collins se sostiene: que un protocolo sea reproducible-en-principio no equivale a haber sido reproducido. La asimetría es relevante porque §1 de cap03-03 usa la replicabilidad como **criterio de cierre**, no como aspiración.

## (b) Propuesta de edición

**No edito el manuscrito.** La reescritura toca la tesis del capítulo (línea 6) y el alcance epistémico del protocolo, lo que requiere firma de Jacob. Propuesta concreta para que Jacob revise:

**Reescritura propuesta de §1 (líneas 4–6):**

> "Tesis del capítulo: La auditoría ontológica es un protocolo de nueve fases que examina cualquier categoría candidata bajo el filtro del dossier de anclaje y produce decisión trazable. **El protocolo está construido para admitir replicación por tercero competente —cada fase fija inputs, decisiones y outputs documentables— pero la replicación externa efectiva sobre el corpus de la tesis sigue siendo deuda fechada (ver §Deuda residual).** Sin esta auditoría, la tesis es programa filosófico; con ella, es programa de investigación que reclama reproducibilidad y la somete a verificación, no que la presupone."

**Nueva entrada propuesta para `TAREAS_PENDIENTES.md` Sección A (humanas):**

- `H-J##` — Gestionar replicación externa de **al menos un caso del corpus EDI** (sugerido: caso 16 deforestación o caso clima, por estar mejor documentados) por un investigador independiente del equipo Jacob+Steven. Output esperado: dossier de anclaje regenerado por el tercero + decisión ontológica + comparación con la decisión original. Plazo: antes de la defensa pública. Sin esta replicación, §1 cap03-03 mantiene la marca de deuda.

**Nueva sección "Deuda residual" en cap03-03** (si no existe):

- Replicación externa del protocolo de nueve fases pendiente. La afirmación "criterio de cierre = replicabilidad por tercero competente" se sostiene como criterio normativo del diseño; la verificación empírica de que ese criterio se cumple requiere ejecución por terceros y queda fuera del alcance del manuscrito presente.

## (c) Costo argumentativo declarado

- **Costo retórico:** la tesis del capítulo pierde fuerza performativa. "Se convierte en programa de investigación reproducible" se debilita a "se ofrece como programa que reclama reproducibilidad".
- **Costo metodológico:** se concede a Collins (1985) que el experimenter's regress se aplica también a auditorías ontológicas. La replicabilidad como propiedad del protocolo ≠ replicabilidad como hecho del corpus.
- **Ganancia:** honestidad sobre deuda. La tesis se vuelve menos vulnerable al ataque adversarial directo "ningún tercero ha replicado nada de esto". Pasa a ser un compromiso público fechado, no una afirmación inverificable.
- **Lo que NO se concede:** que la auto-replicación con seeds en `09-simulaciones-edi/` sea irrelevante. Es replicación numérica genuina y documenta determinismo del cómputo. Pero no sustituye replicación de la **decisión ontológica** por un agente con tacit knowledge distinto.

## Acciones requeridas

- [ ] **needs_human (Jacob):** aprobar/modificar la reescritura de §1 cap03-03.
- [ ] **needs_human (Jacob+Steven):** crear entrada `H-J##` en `TAREAS_PENDIENTES.md` Sección A para gestión de replicación externa.
- [ ] **needs_human (Jacob):** decidir si la sección "Deuda residual" del cap03-03 se añade ahora o se difiere al cierre del capítulo.

## Referencias

- Collins, H. M. (1985). *Changing Order: Replication and Induction in Scientific Practice*. SAGE. — Tesis del experimenter's regress y tacit knowledge en replicación.
- `03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md:4-6` — afirmación auditada.
- CLAUDE.md §7 — regla de la deuda residual declarada.
