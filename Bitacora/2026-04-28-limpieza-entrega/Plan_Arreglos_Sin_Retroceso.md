# Plan de arreglos sin retroceso

> Lista cerrada de cambios que mejoran el manuscrito **sin** abrir nuevas iteraciones conceptuales. Cada arreglo es local, mecánico o aditivo. Nada de re-escritura de capítulos, nada de re-ejecución de corpus, nada de re-arquitectura.
>
> **Regla de oro:** si un arreglo requiere re-decidir algo conceptual, NO entra acá. Va al director.

**Fecha:** 2026-04-28.
**Tiempo total estimado:** 12–18 horas de trabajo distribuibles en 4–6 días.

---

## Criterio de admisión de cada arreglo

Cada item de esta lista cumple las cuatro condiciones:

1. **Local:** afecta máximo 1–2 archivos.
2. **Aditivo o mecánico:** añade contenido o corrige forma; no reabre debate conceptual.
3. **Verificable:** se puede confirmar que está hecho con un check binario.
4. **Sin dependencia de input externo:** no requiere esperar al director, ni a revisor externo, ni a re-cómputo masivo.

Lo que **NO** entra: añadir capítulos, re-ejecutar corpus, cambiar definiciones nucleares, profundizar argumentos filosóficos sustantivos (eso es V6 disfrazada).

---

## Bloque A — Higiene de formato (3–4 horas, 0 riesgo)

Estos son arreglos puramente mecánicos. Cero retroceso conceptual.

### A.1. Renumerar secciones 12bis / 12ter del cap 02-01

`02-fundamentos/01-ontologia-material-relacional.md`: las secciones `12bis` (observador cuántico) y `12ter` (evolución conceptual) deben pasar a §13 y §14 respectivamente. Renumerar referencias cruzadas si las hay.

**Verificación:** `grep -n "12bis\|12ter"` devuelve vacío.

### A.2. Cerrar viñetas residuales del cap 02-01

Al final de §"Criterios operativos para distinguir κ-pragmática de κ-ontológica", tras la tabla y la "Implicación operacional", quedan tres bullets fragmentados (`- la corrección de los umbrales...`, `- lo que NO es revisable...`) que parecen continuación del párrafo anterior. Reordenar o reabsorber en el párrafo.

**Verificación:** lectura visual del cap; no debe haber bullets huérfanos sin encabezado claro.

### A.3. Completar §10 ausente del cap 06-01

`06-cierre/01-conclusion-demostrativa.md` salta de §9 ("Forma corta de la tesis demostrada") a §11 ("Cierre del cierre"). O se renumera §11 → §10, o se añade §10 con contenido mínimo (e.g., "Síntesis ejecutiva en una página"). **Recomendado:** renumerar.

**Verificación:** numeración consecutiva.

### A.4. Unificar viñetas y guiones largos en bibliografía

`07-bibliografia/01-bibliografia-orientativa.md`: revisar que todas las entradas usen el mismo separador (`,` vs `.`) entre autor y año. Mecánico, 30 minutos.

**Verificación:** grep por inconsistencias de puntuación.

### A.5. Frontmatter del manuscrito ensamblado

`TesisFinal/Tesis.md`: el frontmatter dice "Universidad de Antioquia" pero **falta línea para director de tesis**. Añadir placeholder explícito:

```
**Director de tesis:** [pendiente de declaración formal — bloqueador procedimental, ver Anexo B.1]
```

Esto evita que el comité piense que se omitió por descuido. Lo declaras como bloqueador conocido.

**Verificación:** línea presente en frontmatter.

---

## Bloque B — Refuerzos textuales mínimos (4–6 horas, riesgo bajo)

Estos son micro-añadidos de 1–3 párrafos cada uno que cierran flancos de defensa oral sin reabrir debates.

### B.1. Sub-sección sobre Kim en cap 02-05 §2.4

La respuesta actual (modus tollens vacuo) ocupa ~4 renglones. Expandir a sub-sección de **medio página** con:

- enunciado preciso del argumento de Kim (3 líneas);
- distinción constitución/causación con cita de Craver paginada (5–6 líneas);
- aplicación al aparato EDI: por qué la intervención ablativa es woodwardiana sobre variables, no sobre eventos micro (5–6 líneas);
- por qué esto no diluye la tesis (3–4 líneas).

**Material ya existe** en T13 de la suite ST y en el §2.4 actual. Sólo es expandir, no re-pensar.

**Verificación:** §2.4 tiene al menos 25 líneas y cita textual de Kim 1998 + Craver 2007 con paginación.

### B.2. Tres citas textuales con paginación de Husserl o Merleau-Ponty en cap 05-01

`05-aplicaciones/01-mente-memoria-yo.md`: añadir un párrafo de "Diálogo con tradición fenomenológica" con tres citas textuales paginadas (Husserl *Ideas I*, Merleau-Ponty *Fenomenología de la percepción*, Thompson *Mind in Life*). Reconocer que el aparato no agota el problema fenomenológico y que el complementarismo metodológico se sostiene operativamente.

**No re-discutir qualia, no abrir nuevas posiciones**. Sólo poner el texto que demuestra lectura.

**Verificación:** sub-sección presente con tres citas paginadas.

### B.3. Tres citas textuales con paginación de Hoyos Vásquez

`02-fundamentos/01-ontologia-material-relacional.md` §0.3: las tres líneas actuales sobre Hoyos están sin cita textual paginada. Añadir tres citas de *Borradores para una fenomenología* (1996) o *Ética para ciudadanos* (1996) que articulen continuidad/discontinuidad con la asimetría L1↔B↔L3↔S.

**Verificación:** §0.3 tiene tres citas paginadas.

### B.4. Recordatorio de honestidad sobre p-value en cap 06-02

`06-cierre/02-guia-de-defensa.md` (versión 15 minutos): añadir un punto explícito sobre cómo responder a la pregunta del p-value miscalibrado al 24%. Tres líneas: "los umbrales EDI sí son robustos (0% strong bajo random walk puro); la inferencia se basa en umbrales, no en p-value; la calibración es deuda metodológica fechada".

Esto te ahorra improvisar en defensa.

**Verificación:** versión 15 min tiene parágrafo sobre p-value.

### B.5. Cierre explícito de "datos sintéticos" en cap 06-01

`06-cierre/01-conclusion-demostrativa.md` ya lo declara, pero conviene añadir **una línea visible** en el §8.2 ("Lo que la tesis NO afirma") con formulación clara: *"No afirma que los 7 strong del corpus inter-escala estén validados sobre datos experimentales independientes; los datos son sintéticos derivados de parámetros publicados, y la elevación a OGLE/IBM Quantum/BRENDA es deuda priorizada."*

Material ya está; sólo unificarlo en una línea citable.

**Verificación:** línea presente, citable de memoria en defensa.

---

## Bloque C — Cierres de consistencia formal (3–4 horas, riesgo bajo)

### C.1. Extender suite ST de modal.k a modal.kt

El sistema modal **declarado** en cap 02-01 es T (KT). La suite ST verifica T22 sobre `modal.k` (sin axioma T). Esta inconsistencia es notable. Solución mínima: añadir teoría T23 que repita los tests críticos de T22 bajo perfil `modal.kt` y verifique que `□P → P` se valida bajo el sistema declarado.

**No requiere re-pensar la tesis.** Es un test adicional. El framework `@stevenvo780/st-lang` ya soporta modal.kt según T11.

**Verificación:** `08-consistencia-st/theories/23-modal-kt.st` existe y `npm run st:check` pasa.

### C.2. Glosario A.1 — verificar que cubre términos V5

`Anexos/A1-glosario-operativo.md`: verificar que incluye entradas para los términos introducidos en V5: *naturalismo metafísico moderado*, *constitución descendente*, *B-series relacional*, *manipulabilidad woodwardiana*, *atractor normativo*, *complementarismo metodológico*, *estructuralismo matemático moderado*, *inferencialismo brandomiano matizado*, *pre-ontológico (sentido genético-epistemológico)*.

Si falta alguno, añadir definición de 2–3 líneas. Mecánico.

**Verificación:** los 9 términos aparecen en el glosario.

### C.3. Asignación bibliográfica — entradas V5 nuevas

`07-bibliografia/01-bibliografia-orientativa.md`: la tabla de "Asignación de interlocutores por capítulo" no incluye los **nuevos capítulos 02-05 y 02-06**. Añadir dos filas:

| Capítulo | Interlocutor principal | Secundarios |
|----------|------------------------|-------------|
| 02-05 (temporalidad y causalidad) | Woodward (2003), Mellor (1998) | Craver, Pearl, McTaggart, Kim, Bunge, Bergson, Whitehead, Hoel |
| 02-06 (dimensión normativa) | Bunge (1989, vol. VIII) | Searle, MacIntyre, Foot, Mackie |

Verificar que las referencias correspondientes estén en la bibliografía nuclear; si no, añadirlas.

**Verificación:** filas presentes y referencias en bibliografía.

### C.4. Anexo A.4 — añadir fila para Wolfram con piloto Rule 110

`Anexos/A4-tabla-comparativa-rivales.md`: si la fila de Wolfram no incluye ya el resultado del piloto Rule 110 (EDI=0.55), añadir columna o nota de pie con el resultado y referencia a `09-simulaciones-edi/wolfram_pilot/`.

**Verificación:** fila Wolfram menciona piloto ejecutado con cifra.

---

## Bloque D — Materiales de defensa (2–3 horas, alto valor)

### D.1. Hoja de respuestas tipo (Q&A) — anexo nuevo de defensa

Crear `Anexos/A6b-respuestas-tipo-defensa.md` (o sección al final de A.6) con las 7 preguntas anticipadas del veredicto + respuesta lista en 3–5 líneas cada una, con referencia exacta al capítulo donde está la justificación completa.

Esto NO es contenido nuevo. Es **mapeo** de contenido existente a formato Q&A para defensa oral. Riesgo cero, valor alto.

**Verificación:** anexo existe con 7 Q&A.

### D.2. Lista de errores conocidos y declarados

Crear `Anexos/A0-limitaciones-declaradas.md` (o ampliar A.6): lista de una página con todas las limitaciones que la tesis declara (p-value 24%, datos sintéticos, post-hoc, AUC interno, sin revisión externa, ningún caso κ-ontológica, etc.) en formato cerrado con plazo y entregable.

Material ya está disperso en cap 06-01 §8.2 y README. Es **consolidación**, no nueva crítica.

**Verificación:** anexo existe con tabla cerrada.

---

## Bloque E — Lo que NO se debe tocar

Para evitar bucles, fijar explícitamente lo que queda fuera:

| Tentación | Por qué no |
|-----------|------------|
| Añadir capítulo nuevo sobre fenomenología profunda | V6 disfrazada; si el director lo pide, se añade después |
| Re-ejecutar corpus inter-escala con datos reales | 6–12 meses, post-defensa |
| Re-pensar la respuesta a Kim desde cero | Ya verificada por ST T13; expandir sí, re-pensar no |
| Añadir más casos al corpus inter-dominio | Composición ya post-hoc declarada; añadir empeora la objeción |
| Cambiar la definición de "pre-ontológico" | Cerrada en cap 02-01 §0.2; tocar reabre todo |
| Re-calibrar el p-value | Refinamiento metodológico; deuda fechada |
| Pulir narrativa global con re-escritura | Trabajo de plantilla institucional pre-depósito |
| Añadir más rivales al cap 04-01 | 14 ya cubren el espacio; más es ruido |
| Mejorar la suite ST con teorías nuevas más allá de C.1 | 23 teorías con 6 hallazgos ya es defendible |

---

## Orden de ejecución recomendado

**Día 1 (2–3 h):** Bloque A completo. Higiene mecánica primero porque no contamina conceptualmente y deja el manuscrito presentable.

**Día 2 (3–4 h):** B.1 + B.4 + B.5. Refuerzos defensivos sobre los puntos que más pueden empujar.

**Día 3 (2–3 h):** B.2 + B.3. Diálogos textuales fenomenológico y latinoamericano. Riesgo de abrirse a re-pensar — disciplina: tres citas, tres párrafos, cierre.

**Día 4 (2–3 h):** Bloque C completo. Cierres de consistencia formal.

**Día 5 (2–3 h):** Bloque D completo. Anexos de defensa.

**Día 6 (1 h):** revisión final + commit con mensaje claro tipo "V5.1: arreglos sin retroceso pre-envío a director".

---

## Criterio de cierre

Se considera completado cuando:

1. Todos los items de A–D están con check binario verificado.
2. La suite ST sigue pasando completa (`npm run st:check` verde).
3. Ningún capítulo cambió de tesis nuclear; sólo añadidos textuales o de forma.
4. Commit final hecho.
5. Después de eso: **se envía al director y se para hasta tener su feedback**.

---

## Lo que esto produce

- **Manuscrito visualmente más profesional** (Bloque A).
- **Defensa oral más blindada** (B.4, D.1, D.2).
- **Flancos filosóficos más respetables** (B.1, B.2, B.3).
- **Consistencia formal interna mayor** (C.1, C.2, C.3, C.4).
- **Sin tocar tesis nuclear, sin re-ejecutar nada, sin reabrir debates.**

Tiempo total: **12–18 horas reales** distribuidas en 4–6 días. Después: stop, commit, director.

> Si te encontrás haciendo algo que no está en esta lista, parar y preguntarse: *¿esto es V5.1 o es V6?* Si es V6, archivar la idea para después del director.
