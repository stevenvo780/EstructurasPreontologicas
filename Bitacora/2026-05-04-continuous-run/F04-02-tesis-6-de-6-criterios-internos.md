# F04-02 — Tesis 6/6 en criterios internos: circularidad criterio-evaluador

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap04+06 (2026-05-05)
**Archivo señalado:** `04-debates/03-tabla-comparativa-rivales.md:59` (Tabla 4.3.3)
**Estado:** `needs_human` (requiere firma de Jacob — afecta arquitectura discriminativa del cap 04)

---

## (a) Verificación de la afirmación

**Afirmación auditada:** La tesis, en `04-debates/03-tabla-comparativa-rivales.md:59`, se autoadjudica `✓ ✓ ✓ ✓ ✓ ✓` sobre los seis criterios A-F definidos en el mismo capítulo (líneas 15-22). Los criterios fueron diseñados por la propia tesis (anclaje material, multiescalaridad, dossier de catorce componentes, asimetría L1↔B↔L3↔S, cartografía con falsación, alcance programático). Resultado: 6/6 contra 14 rivales que oscilan entre 0/6 y 4/6.

**Verificación textual:** confirmado. Línea 59: `| **Tesis** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** |`. Línea 61: *"La tesis cumple los seis criterios. Ninguna posición rival cumple los seis."* La nota mitigante *"La novedad no es de inventario […] sino de articulación"* reconoce que cada criterio aislado existe en algún rival, pero **no neutraliza el problema metodológico**: el conjunto-criterio fue construido para que solo la tesis lo satisfaga.

**Diagnóstico (Lakatos 1970 / Bunge 1977 vol. 3):**

- **Lakatos**, *Falsification and the Methodology of Scientific Research Programmes* (en *Criticism and the Growth of Knowledge*, Cambridge UP, 1970, pp. 116-122): un programa que se inmuniza redefiniendo sus condiciones de éxito comete una *ad hoc₃ rescue* — el cinturón protector se ajusta para que las predicciones del núcleo siempre se confirmen. El criterio C ("dossier de **catorce** componentes") y el D ("asimetría L1↔B↔L3↔S") son tan específicos que **ningún rival podía satisfacerlos por construcción**, pues están definidos a partir del aparato propio.
- **Bunge**, *Treatise on Basic Philosophy*, vol. 3 *Ontology I: The Furniture of the World* (Reidel, 1977), §1.3 sobre criterios de adecuación de sistemas ontológicos: exige que los criterios de evaluación sean **independientes** del sistema evaluado o, al menos, que se aplique además un panel de criterios externos no diseñados por el sistema mismo. La Tabla 4.3.3 incumple esta exigencia.

**Conclusión:** la afirmación adversarial es **correcta**. La tabla, tal como está, no constituye discriminación pública sino auto-evaluación con vara propia.

---

## (b) Propuesta de edición concreta

**No edito el capítulo** (afecta tesis sustantiva → `needs_human` Jacob). Propuesta para revisión:

### B.1 — Insertar §"Reconocimiento de circularidad criterio-evaluador" (tras línea 22)

Sugerencia de prosa (≤ 8 líneas, voz Jacob):

> **Reconocimiento de circularidad.** Los criterios A-F fueron formulados desde el aparato de la propia tesis. Que la tesis los satisfaga 6/6 no es virtud, sino tautología si se lee como discriminación pública. La función real de la tabla es doble: (i) explicitar las dimensiones que la tesis considera relevantes para que el lector pueda contestarlas, y (ii) mostrar que ningún rival las satisface conjuntamente —lo que es informativo solo en la medida en que el lector acepte previamente la pertinencia del conjunto-criterio. Para mitigar la circularidad, §"Criterios externos" somete la tesis a tres criterios no diseñados por ella.

### B.2 — Añadir §"Evaluación contra criterios externos" con ≥1 ✗ o parcial

Propuesta de tres criterios externos donde la tesis **no** se autoadjudica ✓:

| Código | Criterio externo (fuente) | Tesis |
|---|---|---|
| **G** | Parsimonia ontológica estricta (Quine, *On What There Is*, 1948): preferir el menor número de tipos de entidad. La tesis postula sustrato + estructura emergente + categorías operativas → **más tipos que el materialismo de partículas**. | **parcial** |
| **H** | Predictividad novedosa cuantitativa fuera del corpus de calibración (Popper, *LSD* §85; Lakatos 1970 p.118: *"novel facts"*). El corpus EDI fue diseñado y los casos null (8/40) se reanalizaron post-hoc; predicciones novedosas pre-registradas: 0. | **✗** |
| **I** | Independencia del evaluador (Bunge 1977 vol.3 §1.3): el sistema debe ser evaluable por criterios no construidos por sus proponentes. La presente tabla es interna; no hay revisión externa formal todavía. | **✗** (al cierre actual; muta a parcial tras defensa pública) |

**Lectura honesta:** introducir la columna externa rebaja el puntaje a **3/9** o **4/9** (según se cuente "parcial"), no a 6/6. Esto **no destruye la tesis** — destruye la lectura tautológica de la tabla. La defensa real de la tesis no descansa en el conteo, sino en la articulación dossier+asimetría+cartografía y en los 32/40 casos EDI con `p_perm < 0.05` (cifra que sí es independiente del aparato evaluativo).

### B.3 — Reescribir la nota mitigante (línea 61)

Cambiar:
> *"La tesis cumple los seis criterios. Ninguna posición rival cumple los seis."*

Por algo del orden de:
> *"La tesis satisface los seis criterios internos por construcción; este hecho es informativo solo si el lector acepta el conjunto-criterio. La discriminación sustantiva contra rivales se sostiene en (a) las celdas individuales donde rivales no satisfacen criterios que ellos mismos reconocerían como deseables (p.ej. enactivismo radical reconoce la ausencia de filtro formal) y (b) los criterios externos G-I de §siguiente, donde la tesis muestra al menos un ✗."*

### B.4 — Tachar "compromiso público" línea 222 si no se incorpora B.2

La frase actual *"Si en algún rival la tesis no muestra ventaja en al menos dos celdas, la tesis admite haber sido absorbida"* es un compromiso vacío mientras las celdas las dibuje la tesis. Reescribir o eliminar.

---

## (c) Costo argumentativo declarado

**Costo de aceptar la edición:**

1. **Pérdida retórica:** el "6/6 vs ningún rival 6/6" es visualmente fuerte y queda desactivado. La tabla pasa de ser "prueba de superioridad" a "mapa de auto-ubicación + reconocimiento de límites". Es la lectura honesta, pero más austera.
2. **Apertura de vector crítico:** introducir el criterio H ("predicciones novedosas pre-registradas: 0") expone deuda real frente a Popper-Lakatos. Esto puede explotarse en defensa. Mitigación: declararlo como deuda explícita en cap 06 §Deuda residual con plan post-defensa de pre-registro de ≥3 predicciones novedosas en dominios no calibrados.
3. **Coherencia con CLAUDE.md §1 y §7:** la edición *aumenta* la defensibilidad porque elimina un patrón de auto-indulgencia ("6/6 verdes" — exactamente el anti-patrón listado en CLAUDE.md §1 contra "8/8 verdes, 42/42 ROBUSTO como totem de completud") y declara deuda en lugar de ocultarla.

**Costo de no aceptar la edición:**

- Vulnerabilidad alta en defensa: cualquier evaluador con formación en Lakatos o Bunge identifica la tautología en < 5 minutos. El adversarial-reviewer ya lo hizo en una pasada. Es **F6 latente** (citas/argumentos decorativos: aquí el argumento estructural es decorativo respecto de la discriminación que pretende ejecutar).

**Recomendación:** aceptar B.1+B.2+B.3 antes de cierre doctoral. B.4 opcional.

---

## Marca de estado

- `needs_human` — Jacob debe firmar la reescritura del §"Criterios de discriminación" y la inclusión de criterios externos G-I (decisión filosófica, no técnica).
- No se editó `Tesis.md` ni `metrics.json` (regla CLAUDE.md §4 + harness hooks).
- Pendiente derivado: si Jacob acepta criterio H (predicciones novedosas), abrir tarea B-T para diseñar pre-registro de ≥3 predicciones EDI en dominios fuera del corpus actual.

---

## Lectura cruzada

- CLAUDE.md §1 (auto-indulgencia: "8/8 verdes" — directamente aplicable).
- CLAUDE.md §7 (deuda declarada como virtud).
- Lakatos 1970, *Criticism and the Growth of Knowledge*, pp. 116-122 (ad hoc rescues).
- Bunge 1977, *Treatise on Basic Philosophy* vol.3, §1.3 (independencia del evaluador).
- Quine 1948, *On What There Is*, *Review of Metaphysics* 2(5), pp. 21-38 (parsimonia).
- Popper 1934/1959, *Logik der Forschung* / *Logic of Scientific Discovery*, §85 (predicciones novedosas).
