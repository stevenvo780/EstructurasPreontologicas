# F04-11 — Caso 33 Villin Headpiece no es "novel fact" lakatosiano

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap04+06 (2026-05-05)
**Archivo afectado:** `04-debates/04-anticipacion-objeciones-filosoficas.md:138` (§3 argumento positivo (d), "Argumento de progresividad lakatosiana")
**Estado:** `needs_human` (requiere firma de Jacob)

---

## (a) Verificación de la afirmación

Cita textual del manuscrito (línea 138, §3(d)):

> "produjo dos predicciones honestas verificadas a posteriori que satisfacen la cláusula de corroboración: (i) caso 33 Villin Headpiece como null genuino bajo sonda equilibrio (predicción: el aparato debe rechazar honestamente cuando la sonda es físicamente inadecuada; verificada); (ii) caso 38 locomoción τ-dot como failure mode de sonda alternativa (predicción: la circularidad de sonda detectada en N2 no se resuelve sustituyendo la sonda primaria por cualquier otra; verificada). Bajo la métrica lakatosiana literal, el programa es **teóricamente progresivo con corroboración empírica parcial**".

Cita textual de Lakatos (1978, *The Methodology of Scientific Research Programmes*, p. 33) que el propio manuscrito reproduce dos líneas antes:

> *"such a series of theories is theoretically progressive (...) if each new theory has some excess empirical content over its predecessor, that is, if it predicts some novel, hitherto unexpected fact"*.

La objeción adversarial es **válida y operativamente seria**:

1. La predicción atribuida al caso 33 ("el aparato debe rechazar honestamente cuando la sonda es físicamente inadecuada") **no es un hecho novedoso sobre el sustrato Villin Headpiece**. Es una afirmación sobre la **higiene metodológica del aparato** (que sus nulls sean genuinos cuando la sonda no calza). Lakatos exige excess empirical content **sobre el mundo**, no sobre la consistencia interna del programa.
2. Análogamente para caso 38: "la circularidad detectada en una sonda no se resuelve cambiando de sonda" es un teorema metodológico (auto-consistencia de la detección de circularidad), no un hecho novedoso sobre la locomoción τ-dot.
3. En ambos casos el predicado se refiere al *test*, no al *target*. Son corroboraciones de **robustez del método**, no novel facts en sentido lakatosiano-zahariano.
4. Adicionalmente, no hay registro fechado **pre-ejecución** que documente que la predicción se hizo antes del corrido. Sin eso, incluso si fueran hechos sobre sustrato, caerían bajo la objeción de Worrall/Zahar de "ad hoc accommodation": una predicción sólo es novel si fue arriesgada antes de ser verificada.

**Conclusión:** la afirmación de progresividad lakatosiana con corroboración empírica parcial, tal como está formulada en §3(d), **no se sostiene** bajo lectura estricta de Lakatos. El argumento confunde corroboración de la metodología (interna al cinturón protector) con corroboración de novel facts (externa, sobre el dominio).

---

## (b) Propuesta de edición

Tres salidas posibles, ordenadas por costo creciente para la tesis:

**Opción 1 — Eliminar §3(d) y declarar progresividad como deuda abierta (recomendada).**
Sustituir el párrafo (d) por una formulación honesta:

> "(d) **Progresividad lakatosiana como deuda no cerrada.** El cuarto criterio de Lakatos (corroboración empírica de novel facts) requiere predicciones arriesgadas, fechadas pre-ejecución, sobre dominios o sustratos no-vistos por el aparato. La tesis no puede reclamar progresividad lakatosiana plena hasta haber producido al menos un caso 41 con esta estructura: predicción registrada, fechada, arriesgada, sobre sustrato (no sobre el método), verificada con datos posteriores al registro. Esta es la deuda priorizada del cap 06-cierre/03 pasos 1-4. La tesis declara, por tanto, ser teóricamente progresiva en sentido (a)-(b)-(c) — extiende dominio sin reentrenar arquitectura — pero suspende el reclamo de progresividad empírica plena hasta cumplir el protocolo de pre-registro."

Costo declarado: la tesis pierde un argumento de progresividad ya cobrado y lo convierte en programa abierto. Ganancia: alineamiento estricto con Lakatos, defensible bajo crítica filosófica de la ciencia.

**Opción 2 — Reescribir §3(d) con candidatos legítimos a novel fact.**
Buscar en el corpus inter-escala algún caso donde:
- la predicción haya sido formulada antes de la ejecución (registrada en bitácora con fecha);
- la predicción sea sobre el sustrato (no sobre el aparato);
- la verificación use datos posteriores al registro.
Candidato a auditar: si existe registro pre-ejecución de "esperamos EDI > 0.5 con sonda X sobre dominio Y nuevo, antes de correr". Si no existe tal registro, **Opción 2 no es viable** y debe usarse Opción 1.

**Opción 3 — Mantener §3(d) reformulado como progresividad metodológica, no lakatosiana.**
Renombrar el argumento como "argumento de robustez metodológica corroborada" y separarlo explícitamente del criterio de novel facts. Costo: pierde la fuerza del marco lakatosiano y queda como argumento de coherencia interna, ya cubierto por (a) y (b).

**Recomendación:** Opción 1. Es la única que sobrevive a un evaluador filosófico hostil sin cosmética.

---

## (c) Costo argumentativo declarado

- §3(d) actual da una sensación de "criterio cumplido" (programa progresivo con corroboración empírica) que el corpus **no autoriza** bajo Lakatos estricto. Mantenerlo es auto-indulgencia argumentativa (cf. CLAUDE.md §1).
- La eliminación del reclamo no destruye §3: los argumentos (a) discriminación, (b) especificidad cruzada, (c) núcleo duro lakatosiano formal sobreviven y bastan para sostener el carácter regulativo.
- Lo que se pierde: el argumento más optimista del capítulo. Lo que se gana: defensibilidad estricta y honestidad sobre lo que falta (caso 41 con pre-registro).

---

## Acción

`needs_human` — La decisión entre Opciones 1/2/3 es filosófica y reasigna parcialmente la afirmación regulativa del cap 02-01 §0.4. Requiere firma de Jacob. Ningún sub-agente debe editar `04-debates/04-anticipacion-objeciones-filosoficas.md` §3(d) sin esa firma.

Si Jacob elige Opción 1, la edición es directa y puede delegarse a la asistencia. Si elige Opción 2, se requiere búsqueda en bitácora histórica de pre-registros con fecha — alta probabilidad de no encontrarlos, en cuyo caso degrada a Opción 1.

**Sugerencia de tarea derivada para `TAREAS_PENDIENTES.md`:** B-F* "auditar bitácora 2026-04 / 2026-05 buscando pre-registros fechados de predicciones EDI sobre casos 33/38/41; reportar si existen o si Opción 2 es inviable".
