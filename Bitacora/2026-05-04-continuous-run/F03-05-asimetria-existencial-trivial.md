# F03-05 — Asimetría L1↔B↔L3↔S debilitada de ∀ a ∃: ¿existencial trivial?

**Fecha:** 2026-05-05
**Origen:** hallazgo adversarial-reviewer cap 03 (2026-05-05)
**Archivo objetivo:** `03-formalizacion/08-validacion-logica-st.md` §ST-1 (líneas 21–23)
**Estado:** `needs_human` (requiere firma de Jacob — costo argumentativo filosófico)

---

## (a) Verificación de la afirmación textual

El manuscrito en cap 03-08 §ST-1 (líneas 21–23) sostiene literalmente:

> "Hallazgo ST-1 (V4 conservado): asimetría L1↔B↔L3↔S no es expresable como axiomas universales proposicionales. Refinada a existenciales en lógica de primer orden (cap 02-04 §8.0). Test 5 de la nueva T19 confirma operatividad inter-escala: existen modelos donde B(qubit), B(cumulo), F(qubit), F(cumulo) y S(qubit), S(cumulo) coexisten satisfactoriamente. La asimetría es invariante a la escala bajo la formulación FOL existencial."

**La objeción adversarial es legítima y reproducible:**

1. Una afirmación existencial pura del tipo `∃x (B(x) ∧ F(x) ∧ S(x))` es lógicamente débil: basta exhibir **un** modelo. Cualquier rival (incluido Wolfram, panpsiquismo, dualismo de propiedades) puede satisfacerla con un caso favorable.
2. La fuerza original de la asimetría L1↔B↔L3↔S — si uno lee cap 02-04 — pretendía ser una afirmación sobre el **orden de recortes legítimos**: que el observador no puede invertir L1↔B↔L3↔S sin pérdida operativa. Esa pretensión no es existencial; es contrafáctica/modal sobre clases.
3. Pasar de "para todo recorte legítimo, el orden L1→B→L3→S domina" a "existe al menos un caso donde el orden se cumple" **vacía la tesis discriminativa** frente a rivales (Lakatos, *Proofs and Refutations*, 1976, §1: monster-barring — re-definir el dominio para salvar la generalidad).

**Conclusión de verificación:** la afirmación del manuscrito es formalmente correcta (T19 sí encuentra modelo existencial), pero **el costo argumentativo del paso ∀→∃ no está declarado** en §ST-1. El hallazgo adversarial es válido.

---

## (b) Propuesta de edición concreta (DRAFT-AI, requiere firma Jacob)

Ampliar §ST-1 (líneas 21–23) con una **nota de costo argumentativo** explícita. Borrador propuesto (no aplicado — espera firma):

```markdown
### Hallazgo ST-1 (V4 conservado): asimetría L1↔B↔L3↔S no es expresable como axiomas universales proposicionales

Refinada a existenciales en lógica de primer orden (cap 02-04 §8.0). Test 5 de la nueva T19 confirma operatividad inter-escala: existen modelos donde B(qubit), B(cumulo), F(qubit), F(cumulo) y S(qubit), S(cumulo) coexisten satisfactoriamente. La asimetría es invariante a la escala bajo la formulación FOL existencial.

**Costo argumentativo del paso ∀→∃ (declarado).** El refinamiento a existenciales debilita la pretensión original. La tesis NO afirma ya que "para toda categoría de recorte el orden L1→B→L3→S domina" (axioma universal proposicional, refutado por contramodelos triviales: e.g., recortes contables donde no hay operador B no-trivial). Afirma, en cambio, que **existe una clase no vacía y operativamente discriminable de fenómenos en los que el orden L1→B→L3→S es el mejor recorte por defecto** — donde "mejor" se opera por el corpus EDI multidominio (cap 09) y se discrimina respecto a rivales por dossier de anclaje (cap 05-06).

Esta es una afirmación **defendible pero más modesta**: se reconoce que (i) la asimetría no es teorema universal sino regularidad operativa con contraejemplos documentables; (ii) categorías como agregados estadísticos sin estructura interna, o sistemas puramente sintácticos sin sustrato físico, **violan el orden** y no son monsters a barrar (Lakatos 1976) sino casos legítimos fuera del dominio. La frontera del dominio se define por los criterios operativos del cap 03-04 (existencia de operador B, sonda macro-O, escala S identificable), no por ajuste post-hoc.

Categorías documentadas que violan el orden (a registrar en deuda):
- agregados puramente estadísticos (e.g., distribución de alturas en una población) — no hay B no-trivial;
- objetos formales puros (teoremas, demostraciones) — no hay S material;
- regímenes caóticos sin atractor estable — el orden L1→B se bloquea (cap 02-04 §6).

Frente a Lakatos: esta declaración NO es monster-barring, porque los criterios de pertenencia al dominio se fijan ex ante (cap 03-04) y no se modifican para excluir casos incómodos. Es restricción de alcance, no rescate ad hoc.
```

---

## (c) Costo argumentativo declarado

1. **La tesis pierde universalidad fuerte.** No se afirma ya un teorema sobre toda estructura recortable, sino una regularidad sobre una clase delimitada. El comité puede objetar que esto reduce el aporte ontológico a empírico-clasificatorio.
2. **El criterio de pertenencia al dominio debe cerrarse antes** (cap 03-04). Si el lector encuentra que los criterios de pertenencia se ajustaron después de detectar contraejemplos, la defensa contra Lakatos cae. Verificar fecha de los criterios vs fecha de detección de los contraejemplos — esto es **deuda H-J** (auditoría histórica del manuscrito).
3. **Se gana defensibilidad frente a Wolfram / panpsiquismo.** Estos rivales podrían satisfacer un existencial trivial; el refinamiento a "mejor recorte por defecto en clase delimitada" los discrimina porque obliga a producir el dossier de anclaje (cap 05-06) y la cartografía multidominio (cap 09), no solo un modelo aislado.
4. **Tarea derivada:** registrar las tres categorías de violación en `00-proyecto/07-glosario-operativo.md` o en deuda residual de cap 03-08, no enterrarlas en una nota a pie.

---

## Estado final

- **Verificación:** afirmación adversarial confirmada — el §ST-1 actual no declara el costo del paso ∀→∃.
- **Acción operativa:** edición propuesta en (b), pendiente de firma de Jacob (decisión filosófica sobre cuánto debilitar la pretensión y cómo declarar la frontera del dominio).
- **No editado:** ni `Tesis.md` ni `metrics.json`. Ningún capítulo modificado en esta pasada.
- **Marcador:** `needs_human` — H-J (voz autoral filosófica, cap 03-08 + cap 02-04 §8.0 + cap 03-04).

## Lectura cruzada

- cap 02-04 §8.0 (formulación FOL existencial original).
- cap 03-04 (criterios operativos de pertenencia al dominio — verificar precedencia temporal).
- cap 06-01 §5 (los 40 casos no son la tesis).
- Lakatos, I. (1976). *Proofs and Refutations*, §1 monster-barring. (cita pendiente con paginación si la edición se aprueba.)
