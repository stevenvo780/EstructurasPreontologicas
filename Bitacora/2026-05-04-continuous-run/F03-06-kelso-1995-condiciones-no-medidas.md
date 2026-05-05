# F03-06 — Kelso 1995 p.73: vocabulario de "phase transition" sin condiciones operativas

**Fecha:** 2026-05-04
**Origen:** hallazgo adversarial-reviewer cap 03 (2026-05-05)
**Locus:** `03-formalizacion/01-aparato-formal.md:266`
**Estado:** `needs_human` + `needs_biblio`

## 1. Hallazgo

El §12.3 cita a Kelso (1995, *Dynamic Patterns*, cap. 3, p. 73): *"the qualitative change in the form of behavioral patterns is termed a phase transition or bifurcation"* y declara que la tesis adopta el vocabulario **sin modificación**.

El problema no es la cita literal (que es plausible y consistente con el programa kelsoiano), sino el **costo no declarado** de adoptar el vocabulario "sin modificación":

- Kelso ancla "phase transition" en **tres signos operativos medibles**: (a) **critical slowing down** (relajación lenta cerca de la transición), (b) **critical fluctuations** (varianza creciente del parámetro de orden), (c) **hysteresis** (dependencia de trayectoria al variar el parámetro de control en sentidos opuestos). En el experimento HKB clásico, los tres se midieron.
- La tesis importa el vocabulario y lo aplica a casos del corpus EDI (clima, deforestación, VENLab programático, etc.) **sin reportar mediciones de ninguno de los tres signos**. Eso convierte la cita en decorativa por la regla §5 de `CLAUDE.md`: invocación de autoridad sin engagement con el argumento operativo del autor.

## 2. Verificación documental

- PDF de Kelso 1995 *Dynamic Patterns* **no presente** en `07-bibliografia/` (búsqueda `find -iname "*kelso*"` → 0 resultados).
- La paginación p.73 cap.3 no se puede verificar contra fuente primaria desde este harness. Marco la verificación textual como **pendiente** (`needs_biblio`: `/fetch-biblio kelso 1995 dynamic patterns`).
- Aun si la cita literal es correcta, el costo argumentativo (importar vocabulario sin importar protocolo de medición) **persiste con o sin verificación de la página**.

## 3. Propuesta de edición (DRAFT-AI, requiere firma de Jacob)

Sustituir el actual §12.3 segunda oración por dos párrafos que (a) preserven la cita y (b) declaren explícitamente qué del programa kelsoiano la tesis adopta y qué no:

> Kelso (1995, *Dynamic Patterns*, cap. 3, p. 73) extiende el lenguaje al dominio de coordinación: *"the qualitative change in the form of behavioral patterns is termed a phase transition or bifurcation"*. El programa kelsoiano fija tres signos operativos para identificar una transición de fase de coordinación: critical slowing down, critical fluctuations e histéresis bajo barrido del parámetro de control en sentidos opuestos (HKB, cap. 4).
>
> **Qué adoptamos del programa Kelso y qué no.** Adoptamos el vocabulario macro (parámetro de orden, parámetro de control, transición de fase) como descripción de la dinámica acoplada del sustrato. **No adoptamos** la pretensión de que un caso EDI cuente como "transición de fase" sin haber medido al menos uno de los tres signos. En el corpus actual: (i) caso ancla VENLab (cap 05-05) — modo programático, los tres signos están **no medidos**; (ii) caso clima/deforestación — los signos no son aplicables tal cual al diseño ablativo EDI; (iii) corpus inter-escala — pendiente caso a caso. La consecuencia operativa es que el vocabulario kelsoiano se usa aquí en sentido **descriptivo**, no como afirmación de transición de fase comprobada. Cuando la tesis afirme una transición en sentido fuerte (kelsoiano), deberá reportar el signo medido y el protocolo de medición.

Esta edición convierte la cita decorativa en cita con engagement y declara el costo (no se está reclamando "phase transition" en sentido HKB para los casos EDI).

## 4. Costo argumentativo declarado

- **Concesión:** la tesis pierde la asociación retórica "nuestros casos exhiben transiciones de fase à la Kelso". Gana defensibilidad: ya no se le puede objetar que importa el vocabulario sin el protocolo.
- **Riesgo residual:** si Jacob quiere mantener el reclamo fuerte para algún caso, debe diseñar la medición de critical slowing down o histéresis en al menos un caso ancla. Eso es B-T (técnico) o H-J (decisión de alcance).

## 5. Acciones

- `needs_biblio`: recuperar PDF Kelso 1995 *Dynamic Patterns* y verificar literalidad y paginación de la cita p.73 cap.3 (`/fetch-biblio`).
- `needs_human` (H-J): Jacob decide entre (A) aceptar la edición DRAFT-AI §3 (tesis declarativa: vocabulario sin reclamo fuerte), o (B) abrir tarea técnica B-T para medir uno de los tres signos kelsoianos en un caso ancla.
- **No editar Tesis.md** desde la asistencia hasta que Jacob firme la opción.

## 6. Trazabilidad

- Regla §5 CLAUDE.md (cita decorativa = F6).
- Regla §3 CLAUDE.md (concesión honesta declarada).
- Locus único: `03-formalizacion/01-aparato-formal.md:266`.
