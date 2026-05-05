# F05-04 — Instituciones sin North/Ostrom/Williamson

**Fecha:** 2026-05-05
**Capítulo afectado:** `05-aplicaciones/04-instituciones-mercado-y-estado.md`
**Disparador:** hallazgo de `adversarial-reviewer` (cap 05, 2026-05-05): el capítulo de instituciones, mercado y Estado dialoga con Searle, Bourdieu, Latour, Gilbert y Bunge, pero **omite** a los tres autores canónicos de la economía institucional (North 1990) y la gobernanza de bienes comunes (Ostrom 1990) y costos de transacción (Williamson 1985). El engagement institucional queda truncado a "sistemismo bunguiano + sociología francesa".

---

## (a) Verificación de la afirmación adversarial

### Omisión confirmada

Búsqueda en `05-aplicaciones/04-instituciones-mercado-y-estado.md`:

- **North** — 0 menciones. No aparece en §1 (institución), §6 (diálogo con interlocutores), §7 (caso piloto OxCGRT), ni en §9 (limitación honesta).
- **Ostrom** — 0 menciones. No aparece en §1.4 (atractores institucionales), §4 (normatividad), ni en §7 (caso piloto), pese a que sus 8 principios de diseño de instituciones para bienes comunes son el referente cuantitativo más citado para el tipo de afirmación que el capítulo hace (cuenca de cumplimiento, validez, efectividad).
- **Williamson** — 0 menciones. No aparece en §2 (mercado) pese a que la reformulación del mercado como "red dinámica con costos de transacción" sin invocar a Williamson es difícilmente defendible ante un comité con formación en economía institucional.

### Disponibilidad bibliográfica local

```
07-bibliografia/North - Institutions Institutional Change (1990).pdf  ← presente, 6.6 MB
07-bibliografia/Ostrom*.pdf                                            ← AUSENTE
07-bibliografia/Williamson*.pdf                                        ← AUSENTE
```

North 1990 está físicamente en el repo; **omitirlo es injustificable**. Ostrom 1990 y Williamson 1985 deben ser recuperados (B-T: solicitar a `bibliography-fetcher`).

### Severidad de la omisión

Esto **no** es un hallazgo cosmético. North 1990 cap. 1 establece la distinción **institución / organización** que el capítulo necesita explícitamente:

- §1.1–§1.4 de la tesis lista cuerpos, documentos, infraestructura, normas, etc. **dentro del mismo concepto "institución"**, sin la separación northiana entre *rules of the game* (institución) y *players* (organizaciones). Para North esta separación es metodológicamente prerrequisito (1990, p. 4: *"a crucial distinction in this study is made between institutions and organizations"*; p. 5: *"What must be clearly differentiated are the rules from the players"*).
- §6 menciona Searle ("X cuenta como Y") pero no contrasta con la formulación operativa de North (1990, p. 3): *"Institutions are the rules of the game in a society or, more formally, are the humanly devised constraints that shape human interaction"* — formulación más cercana al espíritu **deflacionario operativo** de la tesis que la searleana, y por tanto un aliado natural omitido.
- §7.1 (caso piloto OxCGRT) describe las medidas COVID como "cuenca de cumplimiento" sin notar que el OxCGRT mide precisamente lo que North llamaría **formal constraints** (cap. 6, "Formal constraints", pp. 46–53) y su efectividad de enforcement (cap. 7, pp. 54–60). El stringency index es, en términos northianos, una operacionalización ordinal del *formal-rule layer*, mientras que la tesis quiere medir la **cuenca dinámica completa** (formal + informal + enforcement). Sin esta distinción, el caso piloto pierde su discriminante explícito frente a una lectura institucionalista pura.

**Conclusión de verificación:** la afirmación adversarial es correcta. La omisión es operativamente significativa, no decorativa.

---

## (b) Propuesta de edición concreta

### Edit-1 — §1.2 "Hipótesis de auditoría" (línea 24-38)

Insertar al final de §1.2, tras la lista de soportes materiales:

> Esta caracterización converge parcialmente con la tradición neoinstitucional. North (1990, p. 3) define instituciones como *"the rules of the game in a society or, more formally, [...] the humanly devised constraints that shape human interaction"*, y propone como prerrequisito metodológico la separación entre *institución* (las reglas) y *organización* (los jugadores que operan bajo esas reglas; cap. 1, pp. 4–5: *"What must be clearly differentiated are the rules from the players"*). La tesis recoge la distinción operativa pero la subordina a su esquema material-relacional: las "reglas" northianas se realizan como cuenca de atracción del sistema acoplado (cuerpos + documentos + sanciones + prácticas repetidas), no como entidad independiente del soporte que las inscribe. Esto preserva la utilidad analítica de North (separar el régimen normativo de los agentes que lo operan) sin importar su realismo de reglas como entidades discretas.

**Costo argumentativo declarado:** la tesis pierde el aire de "ontología social novedosa" y se reposiciona como **refinamiento materialista** de la tradición northiana; ganancia: defensibilidad ante comité con formación en economía institucional.

### Edit-2 — §6 nuevo subepígrafe "6.6 North — economía neoinstitucional"

Insertar como §6.6 (antes del cierre del bloque 6):

> ### 6.6. North — economía neoinstitucional
>
> North (1990, *Institutions, Institutional Change and Economic Performance*, cap. 1, p. 3) define instituciones como restricciones humanamente diseñadas que estructuran la interacción, y separa metodológicamente reglas (instituciones) y jugadores (organizaciones; pp. 4–5). En cap. 5 (*Informal constraints*, pp. 36–45) y cap. 6 (*Formal constraints*, pp. 46–53) descompone el régimen institucional en tres capas operacionalmente distinguibles: restricciones informales (convenciones, códigos de conducta), restricciones formales (reglas escritas, derecho positivo) y enforcement (cap. 7, pp. 54–60).
>
> Es **el aliado más cercano del capítulo en la tradición económica**, complementario a Bourdieu en el lado sociológico. La traducción al aparato es directa: las tres capas northianas son tres dimensiones del estado del sistema institucional acoplado; la cuenca de atracción que la tesis postula como criterio de validez normativa es el **agregado dinámico** de las tres. Donde North se queda en *constraints* como restricciones del problema de elección racional, la tesis añade que las restricciones tienen **realidad efectiva como atractor** verificable por intervención ablativa.
>
> Fricción honesta: North trata las reglas como entidades cuya existencia es independiente del soporte que las inscribe (un código permanece código aunque el archivo se queme y nadie recuerde su contenido); la tesis sostiene que sin soporte material y memoria operante el patrón normativo deja de existir. Esta es divergencia ontológica genuina, no malentendido. La tesis paga el costo: pierde el "realismo de reglas" típico del institucionalismo y debe sostener que toda norma vive en su sustrato.

### Edit-3 — §7.1 reformulación del caso piloto OxCGRT

Reemplazar el bloque actual de §7.1 (líneas 192–200) por una formulación que **explicite el discriminante northiano**:

> Se selecciona como caso piloto la **dinámica de adopción de medidas no farmacéuticas durante COVID-19** por estados nacionales (Oxford COVID-19 Government Response Tracker; Hale et al. 2021, *Nature Human Behaviour* 5: 529–538, citado como fuente secundaria sobre el diseño del dataset, no auditado contra PDF en `07-bibliografia/`).
>
> El OxCGRT operacionaliza un índice ordinal de *stringency* (0–100) agregado por país y día desde indicadores de cierres, restricciones de movilidad y políticas sanitarias. **En la lectura northiana esto es exclusivamente la capa de *formal constraints* (North 1990, cap. 6, pp. 46–53):** reglas escritas con enforcement nominal. La adaptación EDI requiere demostrar que el índice ordinal de stringency es **insuficiente** para predecir el comportamiento agregado sin acoplar simultáneamente (i) restricciones informales (cumplimiento social, confianza institucional como proxy) y (ii) efectividad real de enforcement, y que la cuenca dinámica completa —no la regla aislada— es lo que retorna al cumplimiento bajo perturbación (la propia pandemia).
>
> El **discriminante explícito** frente a una lectura institucionalista pura es: para North, la stringency es la institución; para la tesis, la stringency es solo la inscripción de la institución, y la institución vive en el sistema acoplado completo. La predicción contrastable es que países con stringency comparable pero distinta cuenca informal/enforcement mostrarán divergencias en EDI medibles, no derivables del índice ordinal.

**Costo argumentativo declarado:** el caso piloto pasa de "candidato general" a "candidato con un compromiso predictivo específico". Si los datos OxCGRT no muestran esa divergencia entre stringency y cuenca completa, el caso refuta la utilidad institucional añadida de la tesis. Esto es deuda asumida, no debilidad.

### Edits pendientes que requieren bibliografía no local

- **Ostrom 1990** (gobernanza de bienes comunes, 8 principios de diseño): debe entrar en §4 (normatividad) y §7.2 (otros candidatos plausibles, sustituyendo o complementando Sornette 2003 con Ostrom como referente cuantitativo en estudios de comunes — pesquerías, sistemas de irrigación). **Bloqueado:** PDF ausente. → B-T: invocar `bibliography-fetcher` para `Ostrom (1990) Governing the Commons` (Cambridge UP).
- **Williamson 1985** (*The Economic Institutions of Capitalism*, costos de transacción): debe entrar en §2 (mercado) como referente que la tesis recoge y reformula. **Bloqueado:** PDF ausente. → B-T: invocar `bibliography-fetcher` para `Williamson (1985) The Economic Institutions of Capitalism` (Free Press).

---

## (c) Costo argumentativo declarado y status

**Naturaleza del aporte de esta bitácora:** 90% asistencia (lectura PDF North + propuesta), 10% Jacob (decisión final de integración y firma de fricciones ontológicas con North).

**Estado:** `needs_human` para integración final.

**Razón:** los tres edits propuestos modifican el **posicionamiento del capítulo dentro de tradiciones intelectuales** (lo reposiciona como refinamiento materialista del neoinstitucionalismo, no como ontología social novedosa). Esa decisión de posicionamiento es filosófica y autoral, no técnica; corresponde a Jacob aprobar o ajustar la fricción declarada con North (Edit-2 último párrafo) y el compromiso predictivo específico (Edit-3) que se asume como deuda. La asistencia no firma reposicionamientos de tradición.

**Acciones técnicas pre-firma que sí pueden ejecutarse:**

1. Recuperar Ostrom 1990 y Williamson 1985 vía `bibliography-fetcher` (no editado en esta pasada).
2. Verificar que las páginas citadas de North (pp. 3, 4, 5, 36–45, 46–53, 54–60) coinciden con la edición Cambridge 1990 disponible en `07-bibliografia/` — **verificado en esta pasada**, paginación de la edición física confirmada contra el PDF en pp. 3–9 (cap. 1).
3. Si Jacob aprueba los edits-1, 2 y 3, ejecutar inserción y luego `python3 TesisFinal/build.py`.

**Deuda residual asumida si los edits se aceptan:**

- Operacionalización formal del compromiso predictivo de §7.1 (divergencia EDI entre stringency y cuenca completa) sigue pendiente, marcada como deuda alta en `06-cierre/03-hoja-de-ruta-para-tesis-final.md`.
- Engagement con Ostrom y Williamson queda pendiente hasta que sus PDFs ingresen al repo — la honestidad exige no citarlos hasta poder traer página y cita literal (CLAUDE.md §5).

---

## Verificaciones formales

- Citas literales North 1990: extraídas directamente del PDF `07-bibliografia/North - Institutions Institutional Change (1990).pdf`, pp. 3–5, lectura propia en esta pasada.
- Paginación: verificada contra índice del PDF (cap. 1 = pp. 3–10; cap. 5 = pp. 36–45; cap. 6 = pp. 46–53; cap. 7 = pp. 54–60).
- No se invoca a Ostrom ni Williamson con cita textual: queda como `needs_biblio` hasta recuperación.
- No se ha editado `Tesis.md` ni ningún `metrics.json`. No se ha modificado el capítulo fuente. Edits propuestos en este documento son **borradores**, no aplicados.
