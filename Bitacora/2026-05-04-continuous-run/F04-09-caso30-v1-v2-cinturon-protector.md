# F04-09 — Caso 30 v1→v2: cinturón protector lakatosiano (P10)

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap04+06 (2026-05-05)
**Estado:** `needs_human` (firma Jacob para reformular P10 + nota honesta en cap 06)

---

## (a) Verificación de la afirmación

La objeción adversarial es **correcta**. La defensa P10 actual usa el rechazo de
caso 30 v1 como prueba de no-inmunización, pero la transición v1→v2 reemplazó la
sonda tras el fallo, sin pre-registro previo a la ejecución. Esto encaja con
**monster-barring** y ajuste del **cinturón protector** (Lakatos, *The Methodology
of Scientific Research Programmes*, 1978, p. 48: "the protective belt … has to
bear the brunt of tests and get adjusted and re-adjusted, or even completely
replaced"; cf. Lakatos, *Proofs and Refutations*, 1976, §1: "monster-barring"
redefine el concepto tras el contraejemplo).

### Evidencia documental

1. **Defensa actual** (`06-cierre/05-respuestas-tipo-defensa.md:85`):
   > "El aparato rechazó el caso 30 v1 a pesar de la expectativa del equipo: si
   > fuera máquina de inmunización, el rechazo no hubiera ocurrido."

   Y `06-cierre/04-versiones-cortas-defensa.md:68`:
   > "La versión v2 con sonda mejorada produjo Nivel 3 weak honesto."

2. **Historia git de la sonda v2** (`git log -- 09-simulaciones-edi/30_caso_behavioral_dynamics/`):
   - **`c6884fb`** (2026-04-27 22:01:52 -0500) — *único* commit que introduce v2.
     Mensaje: "Cerrar tesis: caso 30 v2 a Nivel 3, sonda 2do orden, anexos,
     manuscrito ensamblado".
     Bloque 2: implementa nueva sonda `behavioral_attractor` segundo orden +
     reescribe `data.py` + actualiza `case_config.json` + `ode.py`.
     Bloque 3: re-ejecuta y reporta `EDI=0.262, p=0.044`.

   **El mismo commit** introduce el cambio de sonda **y** el resultado positivo.
   No existe commit anterior que registre la sonda v2 antes de su ejecución.
   No hay archivo `pre-registro-caso30-v2.md` ni equivalente en `Bitacora/`
   previo a 2026-04-27.

3. **Reconocimiento ya existente en el manuscrito**
   (`06-cierre/01-conclusion-demostrativa.md:186`):
   > "los 40 casos son post-hoc (no pre-registrados; tabla de depuración
   > multiescala en `Bitacora/2026-04-28-cierre-pendientes/08-pre-registro-multiescala-honesto.md`)".

   Esto es honesto a nivel global, pero **no se invoca en P10**, donde la
   retórica usa caso 30 como ejemplo de disciplina.

### Diagnóstico

Lo que ocurrió secuencialmente:

1. v1 con sonda macro original → EDI=0.002, Nivel 0 null.
2. El equipo reemplaza la sonda por `behavioral_attractor` segundo orden
   (forma funcional Fajen-Warren completa, ver F03-10).
3. v2 con la nueva sonda → EDI=0.262, Nivel 3 weak.
4. v2 entra al manuscrito como caso "weak"; v1 se reinterpreta retroactivamente
   como "prueba de disciplina del aparato".

**Esto es exactamente lo que P10 niega.** El protocolo prohíbe cambiar Q tras el
fallo, pero la sonda ODE *es parte de Q* (define qué nivel macro se considera
"correcto" para la pregunta). Cambiar la sonda tras un null es un movimiento de
cinturón protector: la teoría central (existe acoplamiento detectable) se
preserva ajustando el aparato auxiliar (qué ODE cuenta como sonda válida) hasta
que el resultado positivo aparece.

La defensa "el aparato rechazó v1" es engañosa: el aparato rechazó v1, y en
respuesta el equipo cambió el aparato hasta que v2 pasó. Que el cambio esté
*motivado* (Fajen-Warren genuinamente es segundo orden) no lo convierte en
pre-registro: la motivación post-hoc sigue siendo post-hoc.

---

## (b) Propuesta de edición

**No edito `Tesis.md` ni `metrics.json`** (regla harness §4). Propuestas a Jacob:

### B1. Reformular P10 — reconocer cinturón protector honestamente

En `06-cierre/05-respuestas-tipo-defensa.md:83-87` y
`06-cierre/02-guia-de-defensa.md:130-132`, sustituir la frase:

> "El aparato rechazó el caso 30 v1 a pesar de la expectativa del equipo: si
> fuera máquina de inmunización, el rechazo no hubiera ocurrido."

por algo del tenor:

> "Caso 30 ilustra el riesgo, no su ausencia: v1 fue rechazado (EDI=0.002), y
> tras el fallo el equipo introdujo una sonda de segundo orden (Fajen-Warren
> completa) sin pre-registro previo a la ejecución, obteniendo v2 weak
> (EDI=0.262). En sentido lakatosiano, esto es ajuste del cinturón protector
> auxiliar, no test de la teoría dura. La defensa contra inmunización no
> descansa en este caso, sino en (i) la cláusula global de declaración post-hoc
> del corpus (cap 06-01 §límites; *Bitacora 2026-04-28*), (ii) la prohibición
> de cambiar Q (no la sonda) entre v1 y v2 documentada por commit fechado, y
> (iii) los rechazos del corpus inter-escala donde sí hubo pre-registro. La
> falsabilidad efectiva la dan los cuatro escenarios de fracaso del cap 06-01
> §3, no la trayectoria del caso 30."

### B2. Nota técnica en cap 06-01 (caso 30) y/o anexo A.5

Añadir línea: "Caso 30 v2 no fue pre-registrado; el cambio de sonda v1→v2
ocurrió en commit `c6884fb` (2026-04-27) que también ejecuta y reporta el
resultado. Considerar v2 como iteración de diseño, no como confirmación
independiente."

### B3. (opcional, alto costo) Pre-registro retrospectivo + replicación

Si Jacob quiere recuperar la fuerza retórica de P10, la única salida limpia es:
(i) congelar v2 como "iteración de diseño", (ii) pre-registrar v3 con sonda
fijada antes de re-ejecutar, (iii) re-ejecutar sobre datos nuevos / split
ciego. Esto excede el alcance de cierre técnico actual.

**Acceptance del task**: opción tomada = **B (reconocer cinturón protector sin
garantía de pre-registro)**. La opción A (commit + fecha de pre-registro de v2
antes de su ejecución) es inalcanzable: tal commit no existe.

---

## (c) Costo argumentativo declarado

- **Costo retórico:** P10 pierde el caso 30 como ejemplar de disciplina. La
  defensa contra inmunización queda apoyada en cláusulas más débiles
  (declaración post-hoc global, falsabilidad por escenarios nombrados).
- **Costo metodológico:** se admite explícitamente que en al menos un caso del
  corpus el aparato auxiliar fue ajustado tras el fallo. Esto refuerza la
  necesidad de pre-registro futuro y debilita la pretensión de "hostile
  testing" sobre el corpus actual.
- **Costo recuperable:** si pasadas futuras pre-registran sondas para casos
  nuevos antes de ejecutar, el patrón "ajuste y luego pre-registro" se vuelve
  explícito y trazable, no oculto. La honestidad sobre el cinturón protector
  hoy compra falsabilidad mañana.
- **Lo que NO cambia:** EDI=0.262 con CI [0.249, 0.280] sigue siendo el número
  reproducible vía `09-simulaciones-edi/30_caso_behavioral_dynamics/src/validate.py`.
  Lo que cambia es su lectura: iteración de diseño documentada, no
  confirmación independiente.

---

## Acción solicitada

`needs_human` — Jacob: aprobar/modificar redacción B1 + B2. Tras firma,
sub-agente puede aplicar edits en `06-cierre/05-respuestas-tipo-defensa.md` y
`06-cierre/02-guia-de-defensa.md` (no tocan `TesisFinal/Tesis.md` directo;
re-ensamblado por `python3 TesisFinal/build.py`).

Cruza con: F03-10 (circularidad ODE_gen ≡ ODE_sonda en caso 30), F04-11
(novel facts lakatosianos), F06-03 (threshold-shopping en 4-strong).
