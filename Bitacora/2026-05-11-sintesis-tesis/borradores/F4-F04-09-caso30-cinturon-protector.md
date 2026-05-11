---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 06-cierre/05-respuestas-tipo-defensa.md:83-87 (P10) ; 06-cierre/02-guia-de-defensa.md:130-132
hallazgo: Bitacora/2026-05-04-continuous-run/F04-09-caso30-v1-v2-cinturon-protector.md
tipo: reemplazo_parrafo
---

## Diagnóstico

La defensa P10 invoca el rechazo del caso 30 v1 (EDI = 0.002, Nivel 0 null) y la posterior elevación de v2 (EDI = 0.262, Nivel 3 weak) como prueba de que el aparato **no es máquina de inmunización**. La historia del repositorio muestra que entre v1 y v2 el equipo **reemplazó la sonda** (de la sonda macro original a la `behavioral_attractor` de segundo orden con forma funcional Fajen-Warren completa) en el mismo commit que ejecuta y reporta el resultado positivo. No hay pre-registro previo a la ejecución de v2. En sentido lakatosiano (1978, *The Methodology of Scientific Research Programmes*, p. 48 sobre el ajuste del cinturón protector; *Proofs and Refutations* 1976 §1 sobre *monster-barring*), v1→v2 es **ajuste del cinturón protector auxiliar tras el fallo**, no test independiente de la teoría. La defensa actual oculta esta estructura.

## Verificación

- `git log -- 09-simulaciones-edi/30_caso_behavioral_dynamics/` muestra el commit **`c6884fb` (2026-04-27 22:01:52 -0500)** como único commit que introduce v2. Mensaje: *"Cerrar tesis: caso 30 v2 a Nivel 3, sonda 2do orden, anexos, manuscrito ensamblado"*. El mismo commit implementa la sonda nueva y reporta el EDI; no existe commit anterior con pre-registro de la sonda v2.
- No hay archivo `pre-registro-caso30-v2.md` en `Bitacora/` previo a 2026-04-27.
- `06-cierre/01-conclusion-demostrativa.md:186` ya declara globalmente que los 40 casos son post-hoc, pero la cláusula no se invoca en P10 donde el caso 30 funciona como ejemplar de disciplina.
- Lakatos 1978, *The Methodology of Scientific Research Programmes*: PDF presente en `07-bibliografia/Lakatos - Methodology of Scientific Research Programmes (1978).pdf`. La cita literal sobre el cinturón protector (*"the protective belt … has to bear the brunt of tests and get adjusted and re-adjusted, or even completely replaced"*) debe verificarse con paginación contra la edición disponible antes de inscribir paginación en el manuscrito (B-T:verify-lakatos-1978-p48).

## Texto propuesto (voz autoral filosófica de Jacob)

**Reemplazar en `06-cierre/05-respuestas-tipo-defensa.md:83-87` (P10) y en `06-cierre/02-guia-de-defensa.md:130-132` la frase:**

> "El aparato rechazó el caso 30 v1 a pesar de la expectativa del equipo: si fuera máquina de inmunización, el rechazo no hubiera ocurrido."

**por:**

> Caso 30 ilustra el riesgo de cinturón protector, no su ausencia. La trayectoria documentada por `git log` es la siguiente: v1 con sonda macro original produjo `EDI = 0.002` (Nivel 0 null); tras ese fallo el equipo introdujo una sonda de segundo orden con forma funcional Fajen-Warren completa (`behavioral_attractor`) **en el mismo commit (`c6884fb`, 2026-04-27)** que ejecutó y reportó el resultado positivo `EDI = 0.262` (Nivel 3 weak). No hubo pre-registro fechado de la sonda v2 anterior a su ejecución. En sentido lakatosiano (1978, *The Methodology of Scientific Research Programmes*, p. 48 — paginación pendiente de verificación contra edición local), esto es **ajuste del cinturón protector auxiliar tras la refutación**, no test independiente de la teoría central. La teoría dura (existe acoplamiento detectable en behavioral dynamics) se preservó modificando el aparato auxiliar (qué ODE cuenta como sonda válida) hasta que el resultado positivo apareció. Que el cambio esté motivado —Fajen-Warren genuinamente es segundo orden— no lo convierte en pre-registro: motivación post-hoc sigue siendo post-hoc.
>
> La defensa contra inmunización no descansa en este caso, sino en (i) la cláusula global de declaración post-hoc de todo el corpus actual (cap 06-01 §límites; `Bitacora/2026-04-28-cierre-pendientes/08-pre-registro-multiescala-honesto.md`), (ii) la prohibición de cambiar la pregunta Q (no la sonda) entre v1 y v2 documentada por commit fechado, (iii) los rechazos del corpus inter-escala donde sí hubo pre-registro mínimo, y (iv) los cuatro escenarios de fracaso falsables del cap 06-01 §3 (con la corrección de F06-04: tres escenarios falsables empíricamente + una condición de prioridad histórica). La falsabilidad efectiva la dan esos escenarios, no la trayectoria del caso 30.
>
> El caso 30 v2 debe leerse como **iteración de diseño documentada**, no como confirmación independiente de la teoría. Aceptar esta lectura es honestidad metodológica explícita (CLAUDE.md §7) y compra falsabilidad futura: pasadas posteriores que pre-registren sondas para casos nuevos antes de ejecutar harán explícito y trazable el patrón "ajustar y luego pre-registrar", en lugar de ocultarlo.

**Añadir nota técnica en cap 06-01 (caso 30) o anexo A.5:**

> Caso 30 v2 no fue pre-registrado; el cambio de sonda v1→v2 ocurrió en commit `c6884fb` (2026-04-27) que también ejecuta y reporta el resultado. Considerar v2 como iteración de diseño, no como confirmación independiente.

## Texto a reemplazar / propagar

- Texto actual en `06-cierre/05-respuestas-tipo-defensa.md:83-87` (P10).
- Texto en `06-cierre/02-guia-de-defensa.md:130-132`.
- `06-cierre/04-versiones-cortas-defensa.md:68`: la afirmación "La versión v2 con sonda mejorada produjo Nivel 3 weak honesto" se mantiene pero con llamada al pie a la nota técnica del párrafo anterior.

## Costo argumentativo declarado

- **Costo retórico.** P10 pierde el caso 30 como ejemplar de disciplina; la defensa contra inmunización queda apoyada en cláusulas más débiles (declaración post-hoc global, falsabilidad por escenarios nombrados).
- **Costo metodológico.** Se admite explícitamente que en al menos un caso del corpus el aparato auxiliar fue ajustado tras el fallo. Esto refuerza la necesidad de pre-registro futuro.
- **Costo recuperable.** La honestidad sobre el cinturón protector hoy compra falsabilidad mañana; ocultarlo deja la objeción Lakatosiana como vector publicable.
- **Lo que no cambia.** `EDI = 0.262` con `CI [0.249, 0.280]` sigue siendo número reproducible vía `python3 09-simulaciones-edi/30_caso_behavioral_dynamics/src/validate.py`. Lo que cambia es su lectura: iteración de diseño documentada, no confirmación independiente.

## Cruza con

- F03-10 (circularidad ODE_gen ≡ ODE_sonda en caso 30).
- F04-11 (novel facts lakatosianos).
- F06-03 (threshold-shopping en 4-strong).
- F06-04 (cinco escenarios falsables, recuento honesto).
