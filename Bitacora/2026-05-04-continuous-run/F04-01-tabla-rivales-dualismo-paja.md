# F04-01 — Tabla 4.3.2 fila 1 "Dualismo": hombre de paja

**Fecha:** 2026-05-04
**Tarea:** F04-01-tabla-rivales-dualismo-paja
**Estado:** `needs_human` (requiere firma de Jacob para reformulación de §2 cap 04-01 + cita verbatim de Chalmers 1996)

---

## (a) Verificación de la afirmación

**Hallazgo confirmado.** La Tabla 4.3.2 (`04-debates/03-tabla-comparativa-rivales.md:34`) reporta:

```
| 1 | Dualismo (cartesiano y descendientes) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | A, B, F |
```

Y el cap `04-debates/01-debates-con-posiciones-rivales.md:21-47` trata "dualismo" como bloque monolítico cuya forma fuerte es la postulación de "al menos dos tipos de realidad: material y mental" (línea 25), discriminando en A (sustrato único), B (multiescalaridad sin mundos separados) y F (sin proliferación).

**Problema.** La etiqueta "(cartesiano y descendientes)" es genérica y la confrontación trata sólo el caso fuerte (dualismo de sustancias). Pero el dualismo de propiedades naturalista contemporáneo (Chalmers 1996, *The Conscious Mind*, cap. 4 — "Naturalistic Dualism") **acepta explícitamente**:

- Un único sustrato material (criterio A): no postula sustancia mental separada; las propiedades fenoménicas son propiedades de sistemas físicos.
- Supervenience natural sobre lo físico: las propiedades fenoménicas no varían sin variación física (aunque rechaza supervenience lógica).
- Compatibilidad con la ciencia natural: la posición se presenta como naturalista, no como sobrenaturalismo.

Lo que Chalmers rechaza es **reductibilidad funcional**, no anclaje material. Por tanto, asignarle ✗ en A es **hombre de paja**: la tesis ataca una posición (sustancias separadas) que el dualista de propiedades no defiende.

**Magnitud del costo.** El cap 06-cierre §"discriminación contra catorce rivales" presume que la tesis discrimina en ≥2 criterios contra cada rival. Si dualismo de propiedades acepta A, la fila pasa a (parcial-en-A, ✗-en-B, ✗-en-C, ✗-en-D, ✗-en-E, ✗-en-F). La discriminación sigue siendo ≥2 (B, C, D, E sobreviven), pero **el ✗ en A debe corregirse o queda como cita decorativa F6 contra Chalmers 1996**.

## (b) Propuesta de edición concreta

**Edición 1 — `04-debates/03-tabla-comparativa-rivales.md` línea 34**: separar en dos filas.

```markdown
| 1a | Dualismo de sustancias (Descartes y descendientes) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | A, B, F |
| 1b | Dualismo de propiedades naturalista (Chalmers 1996) | parcial | ✗ | ✗ | ✗ | ✗ | ✗ | B, C, D, E |
```

Justificación de "parcial" en A para 1b: Chalmers acepta sustrato físico único pero postula propiedades fenoménicas que la tesis trata como atractores B-emergentes. El acuerdo es ontológico parcial; la disputa se desplaza al criterio C (dossier de admisión empírica) y D (asimetría L1↔B↔L3↔S aplicada al qualia, sin filtro empírico en Chalmers).

**Edición 2 — `04-debates/01-debates-con-posiciones-rivales.md` §2**: subdividir en §2a (cartesiano) y §2b (propiedades naturalista). El §2b debe:

1. Citar verbatim Chalmers 1996, cap. 4 ("Naturalistic Dualism"), pp. 123-130 — distinción entre supervenience lógica vs. natural y argumento de zombies como motivación de la posición.
2. Reconocer que la tesis recoge más de Chalmers 1996 que del cartesianismo: el rechazo a la reducción funcional es compartido en parte.
3. Discriminar honestamente en C (Chalmers no propone procedimiento empírico de admisión), D (la traducibilidad B↔L3 vía EDI contrasta con la inefabilidad funcional de qualia), E (caso ancla con cartografía multidominio vs. ningún caso operacionalizado en Chalmers).

**Edición 3 — `04-debates/03-tabla-comparativa-rivales.md` línea 67-75 (sección "1. Dualismo")**: reescribir como dos sub-secciones paralelas a 1a/1b, marcando que la discriminación se desplaza de A,B,F (vs. cartesiano) a B,C,D,E (vs. propiedades naturalista).

## (c) Costo argumentativo declarado

- **Pérdida:** la tesis ya no puede afirmar que discrimina contra "el dualismo" en A (anclaje material). Pierde un criterio contra Chalmers 1996.
- **Ganancia:** la confrontación se vuelve defensible. El nuevo lugar de discriminación (C, D, E) es **más fuerte**, porque expone la ausencia de protocolo empírico en Chalmers — un déficit que la tesis convierte en el centro de su programa positivo.
- **Riesgo residual:** si Jacob no acepta dividir la fila, la objeción adversarial (cap04+06 2026-05-05) sobrevive como F6 (cita decorativa de Chalmers como "descendiente cartesiano" cuando no lo es).

## (d) Razón del `needs_human`

1. La cita verbatim de Chalmers 1996, cap. 4 pp. 123-130 **no se puede verificar localmente**: la biblioteca `07-bibliografia/` contiene `Chalmers - Ontological Anti Realism.pdf` y `Chalmers, David (ed) - Metametaphysics.pdf`, pero **no contiene** *The Conscious Mind* (1996). Requiere `@bibliography-fetcher` o adquisición humana del PDF antes de poder cumplir la Acceptance.
2. La división de la fila 1 en 1a/1b modifica la tesis pública sobre "discrimina en ≥2 criterios contra cada rival" — esto es decisión filosófica de Jacob (H-J*), no de la asistencia.
3. La sub-sección §2b requiere voz autoral filosófica (CLAUDE.md §3): es posición declarada con concesión honesta sobre Chalmers, no edición mecánica.

## Acceptance vs. estado real

- ❌ Tabla 4.3.2 con ≥2 filas para dualismo — **no editado** (propuesta lista, espera firma).
- ❌ Chalmers 1996 cap.4 pp.123-130 verbatim en cap 04-01 §2 — **no posible** sin PDF; requiere fetch o entrega humana.

## Acción siguiente sugerida

1. `@bibliography-fetcher` → recuperar Chalmers, D. (1996). *The Conscious Mind*. OUP. Cap. 4.
2. Una vez disponible PDF, `@citation-agent` extrae passages pp. 123-130.
3. Jacob firma división 1a/1b y aprueba la reescritura de §2.
