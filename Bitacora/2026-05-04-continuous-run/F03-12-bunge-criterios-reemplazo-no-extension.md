# F03-12 — Bunge: criterios de la tesis sustituyen, no extienden

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap 03 (2026-05-05)
**Archivo señalado:** `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:230` (§11.1)
**Naturaleza:** auditoría textual + verificación de mapeo conceptual

---

## (a) Verificación de la afirmación

### A.1 Cita actual en §11.1 (línea 232)

> "Bunge (1967, *La investigación científica*, vol. 2, p. 32) formula los criterios de cientificidad de un constructo: *'claridad, falsabilidad, contrastabilidad, no contradicción interna, compatibilidad con el grueso del conocimiento previo, capacidad explicativa y predictiva'*. Los diez criterios de este capítulo **extienden** esa lista al dominio multiescala con énfasis en compresión y reversibilidad, dos exigencias adicionales que Bunge no operacionaliza con la misma especificidad pero que la tesis vuelve verificables."

### A.2 Verificación de paginación contra PDF local

`07-bibliografia/Bunge Mario - 2 - La Investigacion Cientifica.PDF` tiene 27 páginas (scan parcial Canon, sin OCR detectable mediante `pdftotext`). Los volúmenes 3 y 4 también son fragmentos (34 y 31 páginas respectivamente). **No se puede verificar localmente la cita literal de p.32 vol.2** desde los PDFs disponibles.

→ **needs_human:** acceso a edición completa de Bunge 1967 (Ariel) para confirmar si la enumeración textual es literal o paráfrasis no marcada como tal.

### A.3 Verificación del mapeo conceptual (sí auditable)

Lista bungeana enumerada en la tesis (7 criterios):
1. Claridad
2. Falsabilidad
3. Contrastabilidad
4. No contradicción interna
5. Compatibilidad con el conocimiento previo
6. Capacidad explicativa
7. Capacidad predictiva

Diez criterios de la tesis (§2.1–§2.10):
1. Anclaje material
2. Dependencia empírica
3. Fidelidad relacional
4. Poder inferencial
5. Poder predictivo
6. Poder interventivo
7. Robustez
8. Reversibilidad parcial
9. Economía explicativa
10. No reificación

**Mapeo honesto:**

| Bunge | Tesis | Estado |
|---|---|---|
| Claridad | — | **no aparece como criterio** |
| Falsabilidad | (en §3.3 dossier failure, vía `do`-test) | **desplazada de criterio a sub-cláusula** |
| Contrastabilidad | Dependencia empírica (§2.2) | mapeo parcial |
| No contradicción interna | — | **no aparece** |
| Compatibilidad con conocimiento previo | — | **no aparece** |
| Capacidad explicativa | Poder inferencial (§2.4) | mapeo aceptable |
| Capacidad predictiva | Poder predictivo (§2.5) | mapeo directo |

**Conclusión del mapeo:** de los 7 criterios bungeanos invocados, solo 2 (capacidad explicativa→inferencial; capacidad predictiva→predictivo) y media (contrastabilidad→dependencia empírica, parcial) reaparecen entre los 10. Cuatro criterios (claridad, falsabilidad, no contradicción, compatibilidad con saber previo) **no figuran** como criterios de admisión. Falsabilidad se relega a §3.3 como condición de fallo del dossier, no como criterio positivo.

**El verbo "extienden" en línea 232 es incorrecto:** los 10 criterios **sustituyen** la lista bungeana en su mayoría (4 de 7 desaparecen, falsabilidad se desplaza). Lo que sí añaden es: anclaje material, fidelidad relacional, poder interventivo, robustez, reversibilidad parcial, economía explicativa, no reificación (7 nuevos). La afirmación de que "compresión y reversibilidad" son las "dos exigencias adicionales" subreporta el grado real de divergencia.

El hallazgo del adversarial-reviewer queda **confirmado** en su núcleo: el cap 03 invoca a Bunge como ancla legitimadora pero la lista resultante reordena el campo, no lo extiende.

---

## (b) Propuesta de edición concreta para §11.1

Reemplazar el párrafo actual (línea 232) por:

> Bunge (1967, *La investigación científica*, vol. 2, p. 32) formula siete criterios de cientificidad de un constructo: claridad, falsabilidad, contrastabilidad, no contradicción interna, compatibilidad con el grueso del conocimiento previo, capacidad explicativa y predictiva. **Los diez criterios de este capítulo no extienden esa lista sino que la reorganizan**: conservan capacidad explicativa (como poder inferencial, §2.4), capacidad predictiva (§2.5) y contrastabilidad (subsumida en dependencia empírica, §2.2); **desplazan falsabilidad** del estatuto de criterio positivo al de condición de fallo del dossier (§3.3), donde se opera mediante `do`-test e intervención discriminante; y **omiten como criterios independientes** claridad, no contradicción interna y compatibilidad con el saber previo, asumiéndolas como precondiciones de admisión a discusión, no como filtros operativos. La tesis añade, en cambio, **siete exigencias materialistas y operativas** ausentes en la lista bungeana: anclaje material (§2.1), fidelidad relacional (§2.3), poder interventivo (§2.6), robustez (§2.7), reversibilidad parcial (§2.8), economía explicativa (§2.9) y no reificación (§2.10). El costo de esta reorganización se declara: una propuesta puede satisfacer los diez criterios sin haberse sometido a un test de falsabilidad popperiano clásico, siempre que su dossier admita intervención discriminante. La tesis sostiene que esta sustitución es ganancia operativa; queda como pregunta abierta para el lector si el desplazamiento de la falsabilidad a sub-cláusula del dossier le resta fuerza normativa.

**Cambios clave respecto del texto actual:**
- "extienden" → "no extienden esa lista sino que la reorganizan"
- mapeo explícito Bunge↔diez (no opaco)
- declaración del **costo argumentativo** del desplazamiento de falsabilidad
- pregunta abierta declarada (no cerrada con bravata)

**Alternativa menos invasiva:** mantener los 10 criterios pero añadir explícitamente como **§2.11 No contradicción interna** y **§2.12 Compatibilidad con conocimiento previo**, llevando la lista a 12 y permitiendo la palabra "extienden" en sentido literal. Esta vía tiene el costo de inflar la matriz de evaluación (§4) y obligar a re-puntuar los casos del corpus.

---

## (c) Costo argumentativo declarado

1. **Filosófico:** desplazar falsabilidad de criterio a sub-cláusula expone la tesis a la crítica popperiana clásica (Lakatos 1970, en cap §11.2, ya intenta amortiguarla). La concesión honesta es: el filtro EDI/`do`-test es funcionalmente equivalente a falsabilidad **solo en dominios donde la intervención es factible**; en dominios histórico-sociales o cosmológicos donde no hay `do`-test, el filtro pierde mordida. La tesis no resuelve esto; declara la limitación.

2. **Bibliográfico:** la cita de Bunge p.32 vol.2 **no es verificable con los PDFs locales** (scans parciales). El texto literal entrecomillado debería marcarse como paráfrasis hasta que un agente humano confirme contra edición física. → ítem `needs_human`.

3. **Estructural:** si Jacob acepta la opción "ampliar a 12", se invalidan las matrices de evaluación de los 40 casos del corpus que puntúan sobre 10 criterios. Costo de re-trabajo no trivial.

---

## Acceptance status

- ✓ §11.1 propuesta reescrita en sentido "sustituyen, no extienden"
- ✓ Mapeo Bunge↔10 criterios documentado
- ✗ Verificación literal de p.32 vol.2 → **needs_human (B-T*: acceso a edición completa Bunge 1967 Ariel)**
- ⊙ Decisión final entre opción A (reescribir §11.1) vs opción B (ampliar a 12 criterios) → **needs_human (H-J*: firma de Jacob)**

## Próximos pasos

1. Jacob decide: reescribir §11.1 (opción A) o ampliar a 12 criterios (opción B).
2. Verificar contra Bunge 1967 vol.2 p.32 edición física: confirmar si la enumeración entrecomillada es cita literal o paráfrasis.
3. Si opción B: re-puntuar matrices §4 de los 40 casos sobre 12 criterios.
