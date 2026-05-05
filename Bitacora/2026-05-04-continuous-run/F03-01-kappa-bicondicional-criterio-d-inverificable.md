# F03-01 — κ bicondicional con criterio (d) inverificable

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap03 (2026-05-05)
**Estado:** `needs_human` (H-J*) — requiere firma filosófica de Jacob.

## (a) Verificación de la afirmación

Verificada literalmente en dos sitios.

- `03-formalizacion/01-aparato-formal.md:149`:

  > κ(G) = G* es legítima respecto a Q **si y solo si** existe un sistema dinámico de baja dimensión sobre G* que (a) reproduce las trayectorias observadas dentro de τ, (b) preserva atractores, repulsores y bifurcaciones empíricamente identificadas, (c) predice respuestas a perturbaciones e intervenciones, **(d) no oculta una transición que sí ocurre en los datos**.

- `03-formalizacion/04-operacionalizacion-de-kappa.md:9`: tesis del capítulo idéntica, también bicondicional ("si y solo si") y con criterio (d) en los mismos términos.

La objeción del adversarial-reviewer es correcta:

1. **Inverificabilidad operativa de (d).** Saber si una compresión "oculta una transición que sí ocurre en los datos" exige un oráculo del sistema verdadero (o un conjunto de datos no observado todavía); es la versión local del *bootstrap problem* (Glymour 1980): no se puede certificar la completitud de la evidencia desde dentro de la evidencia. (a)–(c) son auditables sobre los datos disponibles; (d) sólo se puede *desautorizar* ex post (refutación) cuando aparecen los datos que la exhiben, no *autorizar* ex ante.
2. **Asimetría lógica con el bicondicional.** Como bicondicional, la cláusula exige que para declarar κ legítima se verifique (d), lo cual es imposible operativamente. Como condicional necesario para retirar legitimidad (refutación ex post), (d) es perfectamente sano. La forma actual confunde criterio de admisión con criterio de fallo, y por eso §6.4 ya tiene que repetir (d) como "criterio de fallo" — duplicación sintomática.
3. **Coherencia con CLAUDE.md §4.** "Distinción operativamente verificable" es la regla; un bicondicional con cláusula no auditable la viola.

## (b) Propuesta de edición — DRAFT-AI, requiere firma de Jacob

**Costo argumentativo declarado:** debilita la pretensión modal de κ (de "iff" a "si"); la tesis pierde la promesa de *captura completa* de la dinámica y gana honestidad operativa. Es exactamente el tipo de concesión que CLAUDE.md §3 pide declarar.

**Edición propuesta en `03-formalizacion/01-aparato-formal.md:149`:**

> κ(G) = G* es legítima respecto a Q bajo el conjunto de evidencia vigente E si (a) reproduce las trayectorias observadas dentro de τ, (b) preserva atractores, repulsores y bifurcaciones empíricamente identificadas en E, y (c) predice respuestas a perturbaciones e intervenciones discriminantes. La legitimidad es **revisable**: queda **retirada** si nuevos datos E' exhiben una transición no capturada por G*. La cláusula de retiro (antes (d)) es criterio de fallo ex post, no requisito de admisión ex ante.

**Edición espejo en `03-formalizacion/04-operacionalizacion-de-kappa.md:9`:** misma reformulación; mover (d) de "tesis del capítulo" a una sección explícita "Criterio de retiro" que ya está implícita en §6.4 del aparato formal.

**Implicaciones que arrastra (Jacob debe valorar):**

- En 03-formalizacion/01-aparato-formal.md §6.4 ("Criterio de fallo"): mantener (d) ahí con redacción de fallo, eliminar la duplicación.
- En 03-04 §"Tesis del capítulo": ajustar el "si y solo si" a "si … sujeta a retiro …".
- En el corpus EDI: ningún caso depende del bicondicional fuerte; (a)–(c) ya son lo que validate.py audita. El cambio es filosófico, no técnico.
- Glosario operativo (`00-proyecto/07-glosario-operativo.md`): añadir entrada "legitimidad revisable de κ" para fijar el uso.

## (c) Costo argumentativo

- **Pierde:** la pretensión de definición *iff* — κ ya no se "define" por sus propiedades empíricas, se *autoriza provisionalmente* por ellas. Filosóficamente esto acerca la tesis a una postura falibilista (Lakatos/Popper) y la aleja de un realismo estructural fuerte tipo Ladyman-Ross — coherente con la advertencia del glosario operativo de no importar OSR.
- **Gana:** verificabilidad operativa estricta; consistencia con §6.4; elimina la objeción Glymour-bootstrap; honra CLAUDE.md §4 (operativo > terminológico) y §7 (deuda declarada en lugar de oculta).
- **No resuelve:** la pregunta de cuán grande puede ser E' antes de exigir reapertura del modelo (umbral de retiro). Esto es deuda residual nueva — declarar en cap 03-04.

## Acción

`needs_human` — la edición propuesta cambia la fuerza modal de un criterio central del aparato formal (operador κ). No es una edición de prosa; es una decisión filosófica que debe firmar Jacob. El draft de arriba está listo para revisión humana; no se ha tocado ningún archivo de la tesis ni `metrics.json`.

RESULT: complete | F03-01-kappa-bicondicional-criterio-d-inverificable | needs_human, draft listo
