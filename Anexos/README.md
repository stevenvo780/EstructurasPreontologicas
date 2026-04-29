# Índice temático de anexos

Organización de los 14 archivos de `Anexos/` en 7 grupos temáticos. Cada archivo conserva su identidad citable (`A.N`) por las múltiples referencias cruzadas existentes en el manuscrito (capítulos `02-fundamentos/`, `05-aplicaciones/`, `06-cierre/`, etc.).

---

## Grupo 1 — Lexicón y operadores

| Anexo | Función |
|-------|---------|
| `A1-glosario-operativo.md` | Definiciones técnicas de los términos operativos del marco (estructura pre-ontológica, atractor empírico, operadores μ/G/H/κ/ε, EDI, dossier de anclaje, asimetría L1↔B↔L3↔S, FWER Holm, block bootstrap, etc.). |
| `A2-mapa-operadores.md` | Mapa formal de los cinco operadores: dominio, codominio, signatura, condiciones de admisión. |

**Lectura recomendada:** A1 antes que A2; A2 supone los términos definidos en A1.

---

## Grupo 2 — Anclaje empírico (corpus)

| Anexo | Función |
|-------|---------|
| `A8-tablas-crudas-corpus.md` | Tablas de los 30 casos del corpus inter-dominio (macro): EDI, p-valor, CI bootstrap, val_steps, LoE, coupling, forcing, nivel, overall_pass, métricas C1-C5. |
| `A12-corpus-multiescala-tablas.md` | Tablas de los 10 casos del corpus inter-escala (10⁻¹⁰ m a 10²⁰ m): EDI, p, CI, sondas físicas, datasets candidatos para elevación a LoE 4. |
| `A3-plantilla-dossier.md` | Plantilla canónica del dossier de anclaje de catorce componentes (qué exigir a cualquier nuevo caso candidato). |

**Lectura recomendada:** A3 establece el filtro; A8 lo aplica al corpus macro; A12 lo extiende a otras escalas. La fuente de verdad numérica es `09-simulaciones-edi/<caso>/outputs/metrics.json`.

---

## Grupo 3 — Discriminación y aplicaciones

| Anexo | Función |
|-------|---------|
| `A4-tabla-comparativa-rivales.md` | Tabla 6×14 de la discriminación pública contra catorce posiciones rivales (dualismo, materialismo de partículas, emergentismo fuerte, instrumentalismo, formalismo, modelos internos, conductismo, cognitivismo, enactivismo, realismo estructural, mecanicismo multinivel, Wolfram, etc.). |
| `A5-mapa-aplicaciones.md` | Mapa de aplicaciones del aparato a dominios programáticos. |

---

## Grupo 4 — Falsación y limitaciones

| Anexo | Función |
|-------|---------|
| `A0-limitaciones-declaradas.md` | Inventario público de limitaciones. La tesis declara qué no demuestra; lo declarado es trazable. |
| `A13-anticipacion-objeciones-filosoficas.md` | **Borrador para Jacob** — anticipación estructurada de 7 objeciones filosóficas críticas (F1, F2, F3, F5, F6, F9, F10). Cada sección sigue el esquema objeción/concesión/distinción/argumento/costo. Requiere validación filosófica antes de incorporación al manuscrito. |

---

## Grupo 5 — Validación formal

| Anexo | Función |
|-------|---------|
| `A11-validacion-st.md` | Validación con la suite ST (`@stevenvo780/st-lang`): 24 teorías formalmente verificadas, sound, complete, decidable. Auditoría externa de la consistencia del aparato. |

---

## Grupo 6 — Defensa oral

| Anexo | Función |
|-------|---------|
| `A6-version-corta-defensa.md` | Cuatro presentaciones de duración creciente (30 s, 2 min, 5 min, 15 min) para defensa ante tribunal. |
| `A6b-respuestas-tipo-defensa.md` | Q&A consolidado: 12 preguntas más probables del tribunal con respuestas calibradas en 30 segundos y referencia exacta al capítulo justificador. |
| `A7-abstract-bilingue.md` | Abstract bilingüe (es/en) para portada y depósito. |

---

## Grupo 7 — Apoyo editorial

| Anexo | Función |
|-------|---------|
| `A9-listas-figuras-tablas-abreviaturas.md` | Listas indexadas de figuras, tablas y abreviaturas. |
| `A10-figuras-mermaid.md` | Figuras Mermaid (diagramas de la tesis). Versiones vectoriales en `figures/`. |

---

## Lectura mínima sugerida (si el evaluador tiene 1 hora)

1. **A7** (abstract) — 5 min
2. **A6** (versión 5 min de defensa) — 5 min
3. **A4** (rivales) — 10 min
4. **A8** + **A12** (corpus) — 20 min
5. **A0** (limitaciones) — 10 min
6. **A6b** (Q&A) — 10 min

Esto cubre tesis, anclaje, discriminación, transparencia y preguntas anticipadas en una hora.

---

## Trazabilidad

- Convención de numeración: `A<entero>` para anexos canónicos; `A<entero>b` para anexos derivados (consolidados, no introducen contenido nuevo).
- La fuente de verdad numérica para todo el corpus EDI es `09-simulaciones-edi/<caso>/outputs/metrics.json` (no este directorio).
- Referencias cruzadas: capítulos `02-fundamentos/`, `03-formalizacion/`, `04-confrontacion/`, `05-aplicaciones/`, `06-cierre/`.
