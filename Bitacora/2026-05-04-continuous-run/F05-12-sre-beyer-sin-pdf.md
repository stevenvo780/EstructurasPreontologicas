# F05-12 — SRE/Beyer 2016 sin PDF: convergencia retórica

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap05 (2026-05-05)
**Archivo objetivo:** `05-aplicaciones/03-sistemas-tecnicos-distribuidos.md:114`
**Estatus:** `needs_human` (firma H-J*)

## (a) Verificación de la afirmación

Lectura literal del párrafo §6.3 (líneas 114–116):

- Cita a Beyer, Jones, Petoff y Murphy (eds., 2016), *Site Reliability Engineering*, O'Reilly, capítulos 3, 4, 15.
- **El propio párrafo declara** que el PDF no está en `07-bibliografia/` y que la lectura no es verbatim paginada (CLAUDE.md §5). Marca la deuda.
- Verificación de la biblioteca local: búsqueda `beyer|sre|site.reli` en `07-bibliografia/` → **0 hits**. La declaración de ausencia es verídica.
- Sin embargo, el párrafo presenta una **tabla implícita de homologías** ("SLO ↔ tolerancia τ", "error budget ↔ región de admisibilidad", "circuit breaker ↔ operador ε", "postmortem ↔ auditoría ontológica") y la cierra como **"fricción productiva: ambas tradiciones desarrollan independientemente la misma estructura operativa"**.

**Tensión detectada.** La declaración de deuda es honesta; la afirmación de convergencia estructural NO es deuda menor: requiere ingeniería conceptual no realizada (¿qué función matemática realiza un error budget en el aparato? ¿bajo qué condición un circuit breaker es operador ε y no mero condicional `if`?). Sin paginación y sin desarrollo, la "convergencia productiva" es **retórica de afinidad terminológica**, no argumento. Cumple el patrón F6 (cita decorativa) aun cuando el autor lo señaliza.

## (b) Propuesta de edición concreta

Dos salidas, con costos distintos. La elección final es de Jacob.

### Salida 1 — Paginar (preserva la tabla de homologías)

Adquirir el PDF de Beyer 2016, depositarlo en `07-bibliografia/`, y citar:
- Cap. 4 "Service Level Objectives" — definición SLO/SLI con páginas.
- Cap. 3 "Embracing Risk" — error budget formalizado.
- Cap. 22 "Addressing Cascading Failures" — circuit breaker/load shedding (NO el cap. 15 como dice el acceptance: el cap. 15 es "Postmortem Culture", el circuit breaker está en cap. 22).
- Cap. 15 — postmortem blameless.

Costo: requiere licencia/adquisición y una pasada de re-lectura. No cierra solo con paginación: la tabla SLO↔τ debe demostrarse operativamente (¿qué predicción del aparato la cita SRE permite verificar?).

### Salida 2 — Reducir a ilustración informal (recomendada por costo/beneficio)

Reescribir §6.3 eliminando el cuadro de homologías y la frase "fricción productiva … misma estructura operativa". Texto propuesto:

> ### 6.3. SRE / práctica de operaciones
>
> La práctica industrial madura de SRE (Site Reliability Engineering, popularizada por Beyer et al. 2016 en O'Reilly; lectura no verificada contra el ejemplar) ha desarrollado vocabulario operativo —SLO, error budgets, circuit breakers, postmortems sin culpa— que, leído desde fuera, sugiere afinidad con varias categorías del aparato (tolerancia, admisibilidad, intervención bajo bifurcación, auditoría retrospectiva). **Esta afinidad es ilustrativa, no argumento de convergencia:** demostrar que un error budget *es* la región de admisibilidad del aparato exigiría reconstruir la matemática del primero, no solo emparejar nombres. Se deja como hipótesis abierta para una pasada futura con el ejemplar físico y desarrollo formal de la homología.

Costo argumentativo declarado: la tesis pierde un argumento de "convergencia con práctica industrial madura" que sonaba fuerte pero no estaba ganado. Lo que conserva es honesto: una hipótesis abierta. La sección 5.3 sigue valiendo por Simondon y Latour (paginados §6.1–6.2).

## (c) Costo argumentativo

- Salida 1 amplía la deuda (adquisición + lectura + formalización de homología); cierra fuerte si se ejecuta, pero no cierra hoy.
- Salida 2 recorta una afirmación no defendible y deja la deuda explícita; consistente con CLAUDE.md §5 (cita decorativa = F6) y §7 (deuda declarada es virtud).
- En ambos casos: **la tabla de homologías SLO↔τ / error budget↔admisibilidad / circuit breaker↔ε / postmortem↔auditoría no se sostiene como afirmación estructural sin desarrollo formal**, paginada o no.

## Acción

`needs_human`. Decisión H-J* para Jacob: ¿Salida 1 (adquirir PDF y paginar + formalizar) o Salida 2 (reducir a ilustración informal)? Recomendación de la asistencia: Salida 2, porque la afirmación de convergencia estructural no estaba ganada y el manuscrito gana en honestidad lo que pierde en retórica.

**Nota técnica al acceptance:** el acceptance pide "cap. 15 (postmortem)" — correcto; pero asocia circuit breaker al cap. 4, cuando en Beyer 2016 el cap. 4 es SLO y los circuit breakers están en cap. 22 ("Addressing Cascading Failures"). Si se elige Salida 1, paginar contra cap. 22, no cap. 4, para circuit breaker.
