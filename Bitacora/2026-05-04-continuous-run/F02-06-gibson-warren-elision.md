# F02-06 — Elisión Gibson → Warren (omite tradición dinamicista 1981–1992)

**Fecha:** 2026-05-05
**Origen:** adversarial-reviewer cap02 2026-05-05
**Archivo afectado:** `02-fundamentos/04-anclaje-conductual-ecologico.md` §10.1 (línea 207) y §10.5 (línea 229)
**Estado:** `needs_human` (B-F* / requiere bibliografía no disponible localmente)

---

## (a) Verificación de la afirmación crítica

El adversarial señala que el §10 ("Diálogo con interlocutores") salta de **Gibson (1979)** directamente a **Warren (2006)**, omitiendo ~25 años de programación dinamicista que media históricamente entre ambos:

- **Turvey & Shaw (1981)**, "The primacy of perceiving: An ecological reformulation of perception for understanding memory", en Nilsson (ed.), *Perspectives on Memory Research*.
- **Kugler & Turvey (1987)**, *Information, Natural Law and the Self-Assembly of Rhythmic Movement*. Erlbaum.
- **Turvey (1992)**, "Affordances and prospective control: An outline of the ontology", *Ecological Psychology* 4(3):173-187.

Lectura del archivo (líneas 205-233) **confirma la elisión**: §10.1 cierra con "Donde Gibson queda en la formulación cualitativa de la affordance, la tesis avanza al sistema dinámico acoplado vía Warren-Fajen". El "vía Warren-Fajen" salta el puente histórico-conceptual donde Turvey-Shaw-Kugler convirtieron las affordances de Gibson en un programa dinamicista (constraint-based, self-assembly, leyes naturales sin agente computacional). Warren 2006 es **heredero explícito** de ese programa, no de Gibson directamente.

El costo de la elisión es doble:

1. **Histórico**: hace parecer que el salto de "información ecológica cualitativa" a "ecuaciones acopladas con r²=0.98" lo da la tesis o Warren, cuando lo dio Kugler-Turvey 1987 con la ontología de constraints + self-assembly.
2. **Argumental**: la tesis usa "atractor", "ley de control", "dinámica intrínseca" como vocabulario propio del nivel B (línea 233) — pero ese vocabulario fue acuñado/operacionalizado precisamente por Turvey 1992 y Kugler-Turvey 1987 para el dominio ecológico. Sin citarlos, la genealogía queda incorrecta.

**Conclusión**: la objeción adversarial es válida. No es un fallo F6 (cita decorativa) porque Warren sí está engaged con cita paginada verificada (línea 231-233), pero **es una elisión genealógica** que debilita el anclaje histórico del programa.

---

## (b) Acción operativa propuesta — needs_human

**Bloqueador**: los PDFs de Turvey 1992, Kugler-Turvey 1987 y Turvey-Shaw 1981 **no están en `07-bibliografia/`** (verificado: `ls | grep -iE "turvey|kugler|shaw"` → vacío). Sin acceso a fuente primaria, **no puedo proponer cita textual paginada** sin violar §5 de `CLAUDE.md` ("cita textual con paginación o no cita").

**Propuesta concreta de §10.1.bis** (DRAFT-AI estructural; el contenido textual paginado lo debe completar Jacob o un fetch bibliográfico):

```markdown
### 10.1.bis. Turvey, Shaw, Kugler — programa dinamicista ecológico

Entre Gibson (1979) y Warren (2006) media un cuarto de siglo de
programación dinamicista que la tesis hereda y que conviene declarar
explícitamente. Turvey y Shaw (1981) reformulan la percepción como
"primacía del percibir" sin recurso representacional. Kugler y Turvey
(1987, *Information, Natural Law and the Self-Assembly of Rhythmic
Movement*) operacionalizan la coordinación motora como auto-ensamblaje
bajo restricciones físicas e informacionales, introduciendo el
vocabulario de "constraint" y "self-assembly" que la tesis usa en B.
Turvey (1992, "Affordances and prospective control", *Ecological
Psychology* 4(3):173-187, pp. [PAGINACIÓN PENDIENTE]) ofrece la
ontología de affordances como propiedades disposicionales del par
animal-entorno, base directa del operador μ tal como se define aquí.

**Qué toma la tesis de cada uno:**

- De Turvey-Shaw 1981: el rechazo del "doble registro" representacional
  (información en el mundo + copia en la mente).
- De Kugler-Turvey 1987: la noción operativa de **constraint** como
  reductor de dimensionalidad — base conceptual de la compresión κ.
- De Turvey 1992: la lectura de affordance como propiedad disposicional
  verificable por intervención, no como cualidad fenomenológica.

Warren (§10.5) hereda este programa y le añade la formalización
acoplada de segundo orden con validación empírica cuantitativa. La
tesis se sitúa explícitamente en esa línea: Gibson → Turvey-Shaw-Kugler
→ Warren-Fajen → corpus EDI.
```

**Tareas que esto genera:**

1. **B-T?** (técnica/bibliográfica): `bibliography-fetcher` debe recuperar PDFs de:
   - Turvey 1992, *Ecological Psychology* 4(3):173-187.
   - Kugler & Turvey 1987 (libro Erlbaum, puede no estar en open access — alternativa: capítulo extraído).
   - Turvey & Shaw 1981 (capítulo en compilación Nilsson).
2. **H-J?** (Jacob): firmar la versión final del §10.1.bis con cita paginada y decisión de cuánta extensión darle (¿párrafo o subsección completa?).
3. **B-F?** (asistencia, post-fetch): redactar las citas textuales paginadas una vez disponibles los PDFs.

---

## (c) Costo argumentativo declarado

- **Costo de NO añadir §10.1.bis**: la tesis presenta a Warren como heredero directo de Gibson, ocultando la mediación dinamicista. Un examinador con formación en psicología ecológica (Turvey, Carello, Richardson, Chemero) detectaría la elisión inmediatamente y la leería como **desconocimiento del programa**, no como brevedad. Riesgo de F6 implícito.
- **Costo de añadir §10.1.bis sin paginación**: violación directa de §5 (`CLAUDE.md`). Inaceptable.
- **Costo de añadirlo con paginación verificada**: ~400-600 palabras adicionales en el cap 02-04, una concesión genealógica honesta, fortalece el anclaje histórico. Beneficio neto positivo.
- **Decisión recomendada**: bloquear cierre del cap 02-04 hasta obtener PDFs de Turvey 1992 / Kugler-Turvey 1987 vía `/fetch-biblio`.

---

## Marca

`needs_human` — requiere (i) fetch bibliográfico de Turvey/Kugler/Shaw, (ii) firma de Jacob sobre alcance del §10.1.bis, (iii) decisión sobre si la elisión genealógica afecta también al cap 05-05 (caso 30 EDI).
