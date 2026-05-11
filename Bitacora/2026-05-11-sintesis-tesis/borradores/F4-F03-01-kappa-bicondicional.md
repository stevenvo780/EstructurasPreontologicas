---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 03-formalizacion/01-aparato-formal.md:149 ; 03-formalizacion/04-operacionalizacion-de-kappa.md:9
hallazgo: Bitacora/2026-05-04-continuous-run/F03-01-kappa-bicondicional-criterio-d-inverificable.md
tipo: reemplazo_parrafo (legitimidad revisable)
---

## Diagnóstico

La definición canónica de legitimidad de κ en `03-formalizacion/01-aparato-formal.md:149` y su tesis del capítulo en `03-formalizacion/04-operacionalizacion-de-kappa.md:9` están escritas como **bicondicional** ("si y solo si"), con un criterio (d) — "no oculta una transición que sí ocurre en los datos" — que es **operativamente inverificable ex ante**. Saber que una compresión no oculta una transición exige acceso a datos no observados, lo cual es la versión local del *bootstrap problem* de Glymour (1980). El bicondicional confunde criterio de admisión con criterio de fallo: (a)–(c) son auditables sobre los datos disponibles; (d) sólo puede operar como retiro ex post.

## Verificación

Cita textual del manuscrito (`03-formalizacion/01-aparato-formal.md:149`):

> "κ(G) = G* es legítima respecto a Q **si y solo si** existe un sistema dinámico de baja dimensión sobre G* que (a) reproduce las trayectorias observadas dentro de τ, (b) preserva atractores, repulsores y bifurcaciones empíricamente identificadas, (c) predice respuestas a perturbaciones e intervenciones, **(d) no oculta una transición que sí ocurre en los datos**."

Misma formulación, idéntica, en `03-formalizacion/04-operacionalizacion-de-kappa.md:9`.

Glymour 1980, *Theory and Evidence* — discusión del *bootstrap problem* (PDF ausente en `07-bibliografia/`; el argumento operativo no depende de la cita literal; si Jacob acepta inscribirla en el manuscrito, abrir `/fetch-biblio glymour 1980 theory evidence`).

## Texto propuesto (voz autoral filosófica de Jacob)

**Reemplazar en `03-formalizacion/01-aparato-formal.md:149`:**

> "κ(G) = G* es legítima respecto a Q bajo el conjunto de evidencia vigente E si (a) reproduce las trayectorias observadas dentro de τ, (b) preserva atractores, repulsores y bifurcaciones empíricamente identificadas en E, y (c) predice respuestas a perturbaciones e intervenciones discriminantes. La legitimidad es **revisable**: queda **retirada** si nuevos datos E' exhiben una transición no capturada por G*. La cláusula de retiro (antes (d)) opera como criterio de fallo ex post, no como requisito de admisión ex ante: certificar la completitud de la evidencia desde dentro de la evidencia es una versión local del *bootstrap problem* de Glymour."

**Edición espejo en `03-formalizacion/04-operacionalizacion-de-kappa.md:9`**: idéntica reformulación; mover la cláusula (d) a la sección explícita "Criterio de retiro" que ya está implícita en §6.4 del aparato formal, eliminando la duplicación.

**Añadir en el glosario operativo (`00-proyecto/07-glosario-operativo.md`)** la entrada:

> **Legitimidad revisable de κ.** La compresión κ(G) = G* se autoriza provisionalmente por sus propiedades empíricas (a–c) sobre el conjunto de evidencia vigente E. La autorización no es definicional ni bicondicional: es retirada si nuevos datos E' exhiben una transición no capturada por G*. El umbral de E' que obliga a reapertura es deuda residual del cap 03.

## Texto a reemplazar

- El "si y solo si" en ambos loci (cap 03-01:149 y cap 03-04:9).
- La cláusula (d) duplicada en §6.4 del aparato formal: mantener allí como "criterio de fallo / retiro" y eliminar su aparición como requisito de admisión.

## Costo argumentativo declarado

La pretensión modal de κ se debilita de "iff" a "si"; la tesis pierde la promesa de captura completa de la dinámica y gana honestidad operativa. Filosóficamente esto acerca el aparato a una postura falibilista (Lakatos/Popper) y la aleja de un realismo estructural fuerte tipo Ladyman-Ross — coherente con la advertencia del glosario operativo de no importar OSR (cf. F03-07 ya procesado). En el corpus EDI ningún caso depende del bicondicional fuerte; (a)–(c) son lo que `validate.py` audita. El cambio es filosófico, no técnico. Como deuda residual nueva queda fijar un umbral cuantitativo a partir del cual la magnitud de la transición no capturada obliga a reapertura formal del modelo.
