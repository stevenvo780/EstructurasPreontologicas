# Auditoría de redundancia inter-capítulos (read-only)

**Fecha:** 2026-05-11
**Auditor:** asistencia técnica bajo dirección humana (rol: auditor de redundancia, read-only).
**Alcance:** los seis capítulos principales — `00-proyecto/`, `01-diagnostico/`, `02-fundamentos/`, `03-formalizacion/`, `04-debates/`, `05-aplicaciones/`, `06-cierre/`. Se excluyen `07-bibliografia/` y `08-consistencia-st/` (subproyecto).
**Volumen base:** 9 313 líneas Markdown en 43 archivos. `TesisFinal/Tesis.md` (9 173 líneas) es derivado y no se edita.

**Política de la auditoría.** Se aplica CLAUDE.md §1 (anti auto-indulgencia: identificar plantillas spam, frases manieristas, documentos meta) y §3 (preservar voz autoral de Jacob). Una recomendación de borrado solo se sostiene si la prosa redundante NO añade matiz, función argumental o registro de discusión distinto al canónico. Cuando hay matiz que justifica conservación, se declara.

---

## Conteo agregado

| Categoría | N detectados | N alto impacto |
|-----------|-------------:|---------------:|
| A. Conceptos centrales con redefinición en ≥2 sitios | 11 | 6 |
| B. Argumentos repetidos textual o semánticamente | 14 | 7 |
| C. Tablas y listas duplicadas | 9 | 4 |
| D. Capítulos candidatos a fusión total o parcial | 5 | 3 |

Si las recomendaciones A-D se aplicaran sin matización, el manuscrito derivado podría reducirse en torno a **1 500–2 100 líneas (16–22 %)** sin pérdida argumental. Pero parte de esa reducción requiere decisión humana (sección E).

---

## A. Conceptos definidos en más de un lugar

Para cada concepto: definición canónica recomendada en **negrita**, redundancias menores en lista.

### A.1. EDI (Effective Dependence Index) — **6 redefiniciones**

- **Canónica:** `00-proyecto/07-glosario-operativo.md:26-27` (entrada autocontenida con fórmula, permutación, bootstrap, capítulo de referencia).
- Redundancia funcional: `03-formalizacion/06-mapa-operadores-formales.md:91, 180` (fórmula en código + tabla resumen) — **conservar** porque opera como mapa visual del pipeline.
- Redundancia menor: `06-cierre/04-versiones-cortas-defensa.md:45, 100` (dos veces dentro del mismo archivo, en versión 5min y 15min). **Sintetizar a una sola mención** y referenciar.
- Redundancia menor: `06-cierre/01-conclusion-demostrativa.md:23` (definición dentro de párrafo conclusivo). Puede mantenerse compacto: ya es referencia inline.

### A.2. Estructura pre-ontológica — **8 ocurrencias con peso definicional**

- **Canónica:** `02-fundamentos/01-ontologia-material-relacional.md:36-…` (§0.2 *"En qué sentido las estructuras son pre-ontológicas"*, cinco sentidos de "pre" distinguidos).
- Complemento: `00-proyecto/07-glosario-operativo.md:29-30, 51-52` (dos entradas: técnica + genético-epistemológica). Conservar ambas — son referencia rápida.
- Redundancia: `00-proyecto/00-introduccion.md:11`, `00-proyecto/05-resumen-y-abstract.md:5,7`, `06-cierre/04-versiones-cortas-defensa.md:21,41,84`, `06-cierre/05-respuestas-tipo-defensa.md:13`. Estas son **paráfrasis ejecutivas** legítimas si son cortas; pero `04-versiones-cortas-defensa` repite la definición tres veces *internamente*: ahí sí hay redundancia evitable.

### A.3. Irrealismo operativo — **5 redefiniciones de mismo contenido**

- **Canónica:** `00-proyecto/07-glosario-operativo.md:32-33` (=realismo estructural moderado + pluralismo epistemológico + anti-reificación operativa).
- Re-expresión idéntica en: `00-proyecto/05-resumen-y-abstract.md:5`, `02-fundamentos/01-ontologia-material-relacional.md:137`, `06-cierre/04-versiones-cortas-defensa.md:21,41`, `06-cierre/01-conclusion-demostrativa.md:246`. Las re-expresiones son legítimas en abstract y conclusión; las que están dentro de `04-versiones-cortas-defensa` son **versionología duplicada del mismo bloque**.

### A.4. Asimetría L1↔B↔L3↔S — **>15 menciones**

- **Canónica:** `02-fundamentos/04-anclaje-conductual-ecologico.md:164…` (§8 *"Asimetría L1↔B↔L3↔S como protocolo"*) + `00-proyecto/07-glosario-operativo.md:151-163` (entradas L1/B/L3/S).
- Redundancia argumental: `00-proyecto/01-estructura-general.md:40,93`, `00-proyecto/02-preguntas-objetivos-hipotesis.md:82,99`, `00-proyecto/03-plan-de-capitulos.md:62,109,169` re-explican la asimetría sin añadir matiz. **Estos tres archivos del `00-proyecto/` repiten entre sí el mismo discurso de "novedad de articulación = dossier + asimetría"** (ver D.1).

### A.5. Dossier de anclaje de catorce componentes — **≥12 lugares**

- **Canónica:** `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:60-94` (§3, lista numerada 1-14 con explicación).
- Versión-plantilla: `03-formalizacion/07-plantilla-dossier-anclaje.md:11-100` (es la plantilla, no redundancia).
- Versión-checklist: `05-aplicaciones/00-criterios-de-admision.md:10-26` — re-enumera los 14 componentes íntegros. **Esta enumeración es redundante con `03-02 §3`**: bastaría referencia cruzada + remitir a checklist.
- Glosario: `00-proyecto/07-glosario-operativo.md:23-24` — entrada compacta legítima.
- Decoración en otros 8 sitios ("dossier de catorce componentes" como letanía): `00-proyecto/01-estructura-general.md:98,123`, `00-proyecto/02-preguntas-objetivos-hipotesis.md:83,103`, `00-proyecto/03-plan-de-capitulos.md:88`, `06-cierre/02-guia-de-defensa.md:10,24,70,104,120`, `06-cierre/03-hoja-de-ruta-para-tesis-final.md:20`. Estos no redefinen, mencionan. La mención repetida es **manierismo de "14 componentes"** señalado por CLAUDE.md §1 ("8/8 verdes, 42/42 ROBUSTO" como totem de completud → aquí "14/14"). Es plausible reducir las menciones decorativas a 2-3 en todo el manuscrito.

### A.6. Protocolo C1-C5 + 13 condiciones overall_pass — **≥10 lugares**

- **Canónica:** `00-proyecto/07-glosario-operativo.md:167-182` (lista C1-C5 limpia) + `03-formalizacion/04-operacionalizacion-de-kappa.md` (§ con tabla detallada) + `03-formalizacion/06-mapa-operadores-formales.md:184-185` (resumen visual).
- Decoración: `00-proyecto/00-introduccion.md:19`, `06-cierre/04-versiones-cortas-defensa.md:45,100`, `06-cierre/01-conclusion-demostrativa.md:246`. Mismo patrón de letanía ("13 condiciones simultáneas").

### A.7. Modo demostrativo vs programático — **2 definiciones casi idénticas**

- **Canónica:** `05-aplicaciones/00-criterios-de-admision.md:8-43` (§1-2 con listas completas para cada modo).
- Glosario: `00-proyecto/07-glosario-operativo.md:204-210`. Conservar (referencia rápida).
- Redundancia parcial: `03-formalizacion/07-plantilla-dossier-anclaje.md:5,206` repite el principio. Puede comprimirse a 1 línea con referencia.

### A.8. κ-pragmática vs κ-ontológica — **3 desarrollos**

- **Canónica:** `02-fundamentos/01-ontologia-material-relacional.md:132-162` (§ "Nota sobre κ" con tres criterios externos).
- Complemento: `03-formalizacion/08-validacion-logica-st.md:82,126-132` (formalización ST de la distinción). Mantener — es la verificación lógica.
- Redundancia: `06-cierre/05-respuestas-tipo-defensa.md:21` y `04-debates/05-limitaciones-declaradas-consolidacion.md:57` (L11) repiten la distinción para el lector. **Útil para evaluación rápida; mantener si es corto**.
- Redundancia: `04-debates/04-anticipacion-objeciones-filosoficas.md:19-55` (§1 entero) re-articula la objeción de circularidad. Este sí añade matiz filosófico (Quine, Carnap, Hacking) — **conservar íntegro**.

### A.9. Self-organization (Maturana-Varela 1980 + Haken 1977) — **6 referencias**

- **Canónica:** `02-fundamentos/04-anclaje-conductual-ecologico.md:120-135` (§4 con cita textual paginada de ambas fuentes).
- Glosario: `00-proyecto/07-glosario-operativo.md:38-39`. Conservar.
- Re-referencia a cap 02-04 §4: `06-cierre/02-guia-de-defensa.md:28,100`, `02-fundamentos/01-ontologia-material-relacional.md:329`, `04-debates/03-tabla-comparativa-rivales.md:176`, `05-aplicaciones/02-biologia-y-ecologia.md:191`. Todas reenvían a cap 02-04 §4 — esto es **buen patrón canónico, no redundancia evitable**.

### A.10. Realismo estructural moderado (uso operativo no-Ladyman) — **2 lugares**

- **Canónica:** `00-proyecto/07-glosario-operativo.md:35-36`.
- Apoyo: `02-fundamentos/01-ontologia-material-relacional.md:137`. La declaración de no-importación de Ladyman está en glosario; el cuerpo solo la usa. Patrón correcto.

### A.11. Cuatro invariantes ontológicos (sustrato, acoplamiento, atractor, κ) — **5 lugares**

- **Canónica:** `02-fundamentos/01-ontologia-material-relacional.md:88` + `05-aplicaciones/06-corpus-multiescala.md:160`.
- Redundancia: `05-aplicaciones/07-mapa-aplicaciones-corpus.md:5,60` repite la fórmula dos veces dentro del mismo archivo. **Una mención basta**.
- Cita en cierre: `06-cierre/01-conclusion-demostrativa.md:164`. Legítimo.

---

## B. Argumentos repetidos textual o semánticamente

### B.1. "Justificación operativa de 40 casos; los 40 casos NO son la tesis" — **alta repetición, 8 lugares**

Argumento de núcleo:
- `00-proyecto/00-introduccion.md:21` *"Los 40 casos del corpus son justificación operativa de los tres marcos, no son la tesis."*
- `00-proyecto/05-resumen-y-abstract.md:13` *"Los 40 casos son justificación operativa del marco tripartito… no son la tesis."*
- `03-formalizacion/08-validacion-logica-st.md:39` (formalización ST T15) — **conservar**, es la prueba.
- `06-cierre/01-conclusion-demostrativa.md:5,246` — paráfrasis dentro de tesis del capítulo + cierre.
- `06-cierre/04-versiones-cortas-defensa.md:27,62` — *"Los 40 casos son justificación operativa del marco tripartito; NO son la tesis."* (literal repetido dos veces dentro del mismo archivo).
- `06-cierre/05-respuestas-tipo-defensa.md:116` (Trampa 3).

**Recomendación:** la afirmación es central. Conservarla en introducción (`00-00`), resumen (`00-05`), formalización ST (`03-08`), conclusión (`06-01`) y una sola vez en `06-04`. Las dos ocurrencias dentro de `06-04` (líneas 27 y 62) son plantilla spam: una sola basta.

### B.2. "Wolfram fundamenta; nosotros disciplinamos" / piloto Rule 110 EDI=0.55 — **6 lugares**

`04-debates/03-tabla-comparativa-rivales.md:222 ↔ 06-cierre/05-respuestas-tipo-defensa.md:93 ↔ 04-debates/01-debates-con-posiciones-rivales.md (§ Wolfram, líneas ~408-440) ↔ 06-cierre/01-conclusion-demostrativa.md:149,246 ↔ 06-cierre/04-versiones-cortas-defensa.md:25,64,84 ↔ 00-proyecto/05-resumen-y-abstract.md:15`.

Extracto literal recurrente: *"Piloto Rule 110 ejecutado mostrando convivencia de irreducibilidad computacional micro y cierre operativo macro detectable (EDI = 0.55 sobre dos sondas independientes). Wolfram fundamenta; nosotros disciplinamos."*

**Recomendación:** la frase aparece **6 veces en sustancia idéntica**. El argumento canónico vive en `04-debates/01 §Wolfram`. El resto son menciones operativas — pueden reducirse a referencia cruzada en 4 de los 6 lugares. La fórmula "Wolfram fundamenta; nosotros disciplinamos" es de las que CLAUDE.md §1 señala como manierismo a podar.

### B.3. Catálogo de "los 14 rivales" enumerados nominalmente — **3 lugares**

- `04-debates/01-debates-con-posiciones-rivales.md:6` (lista completa de los 14).
- `06-cierre/04-versiones-cortas-defensa.md:64` (la misma lista, literal).
- `00-proyecto/05-resumen-y-abstract.md:15` (mención agregada).
- `00-proyecto/03-plan-de-capitulos.md:108` (lista parcial, 13 sin Wolfram — **incoherencia menor que debería corregirse**).

**Recomendación:** la lista íntegra solo necesita aparecer una vez (cap 04-01 §1 o tabla 04-03). En el resto, referencia cruzada.

### B.4. "La novedad no es de inventario sino de articulación" — **8 lugares**

`00-proyecto/00-introduccion.md:65`, `00-proyecto/02-preguntas-objetivos-hipotesis.md:103`, `00-proyecto/05-resumen-y-abstract.md:15`, `04-debates/03-tabla-comparativa-rivales.md:67`, `06-cierre/02-guia-de-defensa.md:120,168`, `06-cierre/05-respuestas-tipo-defensa.md:77`, `04-debates/01-debates-con-posiciones-rivales.md:6`.

**Recomendación:** afirmación legítima como tesis del cap 04-01; las reiteraciones son **letanía discursiva**. Reducir a 3 lugares (cap 04-01, conclusión 06-01, abstract).

### B.5. "Hostile testing severo: 0/1500 falsos positivos del gate completo bajo random walk masivo" — **5 lugares**

`00-proyecto/05-resumen-y-abstract.md:11`, `06-cierre/01-conclusion-demostrativa.md:5,246`, `06-cierre/04-versiones-cortas-defensa.md:11,25`, `06-cierre/05-respuestas-tipo-defensa.md:61`. La cifra exacta es cita técnica defensible — pero la repetición de "0/1500 falsos positivos… 0/12 circularidad…" como par de cifras-totem es señal CLAUDE.md §1 (versionología). **Conservar** en abstract, conclusión 06-01 y una versión corta de defensa; eliminar de las otras.

### B.6. "Lección epistémica del caso 30 (v1 rechazado, v2 weak honesto)" — **4 lugares**

`06-cierre/01-conclusion-demostrativa.md:285`, `06-cierre/04-versiones-cortas-defensa.md:27,68`, `06-cierre/05-respuestas-tipo-defensa.md:53,85`. El argumento *"el aparato funciona porque rechaza honestamente cuando debe rechazar"* es central y aparece literalmente repetido. **Conservar 2 ocurrencias** (cap 06-01 y P10 de 06-05); las otras son spam.

### B.7. "Filtro de admisión simultáneo: dossier + asimetría" — **6 lugares**

Variantes que dicen literalmente lo mismo: `00-proyecto/00-introduccion.md:65`, `00-proyecto/02-preguntas-objetivos-hipotesis.md:103`, `06-cierre/02-guia-de-defensa.md:120,168`, `06-cierre/05-respuestas-tipo-defensa.md:77`, `04-debates/03-tabla-comparativa-rivales.md:67`. Frase: *"dossier de anclaje + asimetría L1↔B↔L3↔S como filtro de admisión simultáneo"*. **Una vez en el cuerpo argumental (cap 04-01) y otra en cierre (cap 06-01) bastan**.

### B.8. Objeción "sustitución nominal" + respuesta — **3 lugares**

- `01-diagnostico/02-objeciones-y-riesgos.md:8-28` (Objeción 1, versión "inicial").
- `04-debates/04-anticipacion-objeciones-filosoficas.md` (versión más sofisticada, con concesiones y costos).
- `06-cierre/02-guia-de-defensa.md:96` y `06-cierre/05-respuestas-tipo-defensa.md:118` (Trampa 4).

**Decisión humana requerida (E):** ¿se elimina el tratamiento "inicial" en 01-02 y se conserva solo el sofisticado de 04-04? El 01-diagnostico tiene función histórica (es el diagnóstico que motivó las correcciones); pero hoy su contenido vive duplicado en 04-debates.

### B.9. "Cuatro/cinco/seis condiciones de fracaso falsables" — **inconsistencia y duplicación**

- `04-debates/02-limitaciones-y-puntos-de-presion.md:6` afirma **seis** límites genuinos.
- `06-cierre/02-guia-de-defensa.md:86,128` afirma **cuatro** escenarios falsables.
- `06-cierre/04-versiones-cortas-defensa.md:70-72` afirma **cinco** escenarios falsables.
- `04-debates/05-limitaciones-declaradas-consolidacion.md` consolida **20 limitaciones (L1-L20)**.

**Decisión humana requerida:** la inconsistencia 4 vs 5 vs 6 escenarios es vulnerabilidad en defensa oral. Hay que fijar UN número canónico (probablemente 5 de 06-04, o el conjunto 20 de 04-05) y eliminar las otras numeraciones.

### B.10. Definición de "patrón estabilizado / atractor con cinco condiciones" — **5 lugares**

`01-diagnostico/01-falencias-de-la-tesis.md:33-50` (Falencia 2) + `02-fundamentos/01-ontologia-material-relacional.md` (canónica) + `00-proyecto/02-preguntas-objetivos-hipotesis.md:79,98-101` + `06-cierre/02-guia-de-defensa.md:54` + `06-cierre/04-versiones-cortas-defensa.md:41`. **Conservar la canónica + glosario; el resto puede comprimirse a referencia.**

### B.11. Bloque "Strong/Weak/Suggestive/Trend/Null/Falsación rechazada" — **3 enumeraciones casi idénticas**

`00-proyecto/05-resumen-y-abstract.md:11`, `06-cierre/01-conclusion-demostrativa.md:5,246`, `06-cierre/04-versiones-cortas-defensa.md:25,49-60`. El conteo se repite cuatro veces con números idénticos. **Vive una sola vez en cap 05-07 (mapa de aplicaciones-corpus) con tablas; las menciones agregadas pueden reducirse a cifras compactas**.

### B.12. "Régimen declarado / propuesta operativamente articulada con demostración parcial" — **manierismo identitario**

Aparece en: `00-proyecto/00-introduccion.md:45`, `00-proyecto/05-resumen-y-abstract.md:21`, `02-fundamentos/01-ontologia-material-relacional.md:162`, `06-cierre/01-conclusion-demostrativa.md:5,198,246,268`, `06-cierre/04-versiones-cortas-defensa.md`. Es una **fórmula manierista** señalada por CLAUDE.md §1 ("frases manieristas"). Conservar **1 vez por capítulo máximo**; aparece 4 veces solo en `06-cierre/01`.

### B.13. Inventario "ontología/epistemología/metodología generales" — **5 lugares**

`00-proyecto/00-introduccion.md:11-19` (con los tres marcos enumerados), `00-proyecto/05-resumen-y-abstract.md:5`, `06-cierre/01-conclusion-demostrativa.md:246`, `06-cierre/04-versiones-cortas-defensa.md:11,21,41,84`. Variante reiterada: *"ontología, epistemología y metodología generales invariantes a la escala"*. **Conservar 2-3 ocurrencias**; las restantes son letanía.

### B.14. Discusión panpsiquismo (Strawson/Goff/Chalmers combination problem) — **2 lugares**

`02-fundamentos/01-ontologia-material-relacional.md:31` (tabla rivales) + `04-debates/04-anticipacion-objeciones-filosoficas.md:156-188` (desarrollo extenso). **Conservar ambos**: 02-01 lo lista; 04-04 lo desarrolla. Patrón correcto.

---

## C. Tablas y listas duplicadas

### C.1. Tabla "Tesis vs Rival" — la misma estructura **15 veces** en cap 04

`04-debates/01-debates-con-posiciones-rivales.md` repite 14 micro-tablas (una por rival: §2 dualismo, §3 materialismo de partículas, etc., líneas 37-49, 67-79, etc.) con encabezado "Tabla 4.1.X" + criterios A-F. **El cap `04-03-tabla-comparativa-rivales.md` ya provee la tabla síntesis 14×6 de una sola pieza** (líneas 36-51), seguida de fila "tesis" (líneas 63-65), y luego replica las micro-discusiones por rival (§§1-14, líneas 73-230).

**Recomendación:** `04-debates/01` y `04-debates/03` se **duplican estructuralmente**. Una de las dos tiene que absorber la otra. La opción técnicamente más limpia es:
- Conservar `04-debates/03` (tiene la tabla síntesis + discriminación detallada por rival).
- Eliminar `04-debates/01` o reducirlo a 1-2 secciones que `04-03` no cubra.
- Mover el detalle de cada rival a `04-debates/_extendido/01-rivales-detallados.md` (sub-carpeta para carga web bajo demanda).

### C.2. Marcadores "Tabla X.Y.Z" duplicados — **bug del numerador**

Múltiples tablas tienen 2-3 etiquetas redundantes consecutivas. Por ejemplo `00-proyecto/07-glosario-operativo.md:188-192`:
```
**Tabla A.1.1.**
**Tabla 0.7.1.**
**Tabla 0.7.1.**
```
Aparece en al menos 30 lugares (`04-debates/01`, `04-debates/02`, `04-debates/03`, `04-debates/05`, `03-formalizacion/07`, `05-aplicaciones/00`, `05-aplicaciones/06`, `05-aplicaciones/07`…).

**Recomendación operativa:** ejecutar `scripts/number_tables.py` con flag de des-duplicación. **No es redundancia argumental, es bug del numerador** — pero suma volumen visible (≈60-90 líneas a través del manuscrito).

### C.3. Listas de los 14 componentes del dossier — **2 enumeraciones íntegras**

`03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:60-94` (lista canónica con explicación por componente) vs `05-aplicaciones/00-criterios-de-admision.md:10-26` (la misma lista numerada 1-14 sin explicación). La de `05-00` es **referencia cruzada disfrazada de enumeración**.

**Recomendación:** `05-00 §1` reducir a *"Una aplicación se admite en modo demostrativo si y solo si presenta dossier de anclaje completo en sus 14 componentes (ver cap 03-02 §3 para enumeración detallada)."* Ahorra ~17 líneas.

### C.4. Bloque "criterios A-F de discriminación" — **2 enumeraciones**

`04-debates/01-debates-con-posiciones-rivales.md:11-17` (criterios A-F) y `04-debates/03-tabla-comparativa-rivales.md:18-24` (los mismos A-F, ligeramente reformulados con frase "invariante a la escala"). **Una de las dos**.

### C.5. Tabla "modo demostrativo vs modo programático" — **2 lugares**

`05-aplicaciones/00-criterios-de-admision.md:62-89` (inventario) + `05-aplicaciones/07-mapa-aplicaciones-corpus.md:181-219` (las 4 aplicaciones programáticas con conjeturas). El segundo amplía el primero. **Mover el inventario de 05-00 al 05-07 y dejar 05-00 con la doctrina pura**, o viceversa.

### C.6. Bloques "interlocutor principal por capítulo" — **2 listas**

`00-proyecto/03-plan-de-capitulos.md:43,68,93…` (interlocutores por capítulo, repartidos sección por sección) y `06-cierre/03-hoja-de-ruta-para-tesis-final.md:88-104` (tabla de distribución interlocutor principal / secundarios). Son **listas paralelas con datos solapantes**. Decidir cuál es canónica.

### C.7. Tabla "promesas que la tesis NO hace / SÍ hace" — duplicada

`04-debates/02-limitaciones-y-puntos-de-presion.md:137-167` (tablas 4.2.1 y 4.2.2) + `04-debates/05-limitaciones-declaradas-consolidacion.md:83-94` (§5 "fuera de alcance"). Cubren lo mismo: lo que la tesis NO promete demostrar. **Mover todo a 04-05 y eliminar la tabla de 04-02**.

### C.8. Listas de figuras y tablas — `00-proyecto/06-listas-figuras-tablas-abreviaturas.md`

Este archivo es **catálogo automatizable**. 146 líneas listando "Fig. 3.2 Diagrama del dossier (14 componentes) – 03-02" etc. **Es generable con script desde los marcadores `**Tabla X.Y.Z.**`**. No es redundancia argumental, pero su mantenimiento manual es fuente de inconsistencias.

### C.9. Cronogramas / hojas de ruta — duplicación parcial

`06-cierre/03-hoja-de-ruta-para-tesis-final.md` (cronograma de pasos 1-7) + `04-debates/05-limitaciones-declaradas-consolidacion.md` (entregables L1-L20 con plazos) cubren parcialmente lo mismo (programa post-defensa). Mantener separados — sirven a propósitos distintos (operativo vs limitaciones declaradas).

---

## D. Capítulos candidatos a fusión total o parcial

### D.1. `00-proyecto/01-estructura-general.md` + `00-proyecto/03-plan-de-capitulos.md` — **alto solapamiento**

Ambos describen la arquitectura del manuscrito (carpetas, propósito de cada capítulo, lógica de redacción). El 01 enumera carpetas con función argumental; el 03 enumera capítulos con núcleos e interlocutores. Solapan en: descripción de cada capítulo (~60 % común), política de redacción, lectura cruzada.

**Recomendación:** fusionar en un solo archivo `00-proyecto/01-estructura-y-plan.md`. Ahorra ~150-200 líneas. **Requiere decisión humana** si Jacob considera que la separación tiene función pedagógica.

### D.2. `06-cierre/02-guia-de-defensa.md` + `06-cierre/04-versiones-cortas-defensa.md` + `06-cierre/05-respuestas-tipo-defensa.md` — **triple solapamiento**

Las tres cubren defensa oral:
- `02` tiene versiones 2/5/15 min + 4 preguntas tribunal.
- `04` tiene versiones 30s/2min/5min/15min + trampas + cierre filosófico.
- `05` tiene 12 P&R + 4 trampas + fórmula de cierre oral.

**Solapamiento severo:**
- `02 §1 (2 min)` ↔ `04 Versión 2 (2 min)`: contenido casi idéntico.
- `02 §3 (15 min) §§4-12` ↔ `04 Versión 4 (15 min) §§1-12`: numeración y contenido prácticamente espejos.
- Las "preguntas del tribunal" de `02 §4` ↔ las P1-P12 de `05` ↔ las trampas de `04`: tres formatos del mismo material.

**Recomendación:**
- Conservar `05-respuestas-tipo-defensa.md` (formato Q&A es el más utilizable en defensa).
- Conservar `04-versiones-cortas-defensa.md` solo en versión 30s + 5 min + 15 min (eliminar 2 min, que duplica `02`).
- Fundir `02-guia-de-defensa.md` con `04` o eliminarlo. **Reducción potencial: 200-300 líneas de las ~530 actuales**.

### D.3. `04-debates/02-limitaciones-y-puntos-de-presion.md` + `04-debates/05-limitaciones-declaradas-consolidacion.md` — **solapamiento alto**

- `02` tiene 6 límites genéricos (alcance asimétrico, dependencia caso ancla, vigilancia léxica, dimensión normativa, dependencia prácticas externas, deuda fenomenología) + 3 riesgos heredados.
- `05` tiene 20 limitaciones L1-L20 (operativas, empíricas, filosóficas, procedimentales) **más detalladas y fechadas**.

Las 6 límites de `02` están subsumidas en las L1-L20 de `05` (e.g., el "alcance asimétrico" de `02 §1` es parte de L5/L9; "deuda fenomenología" es L13; "dimensión normativa" es L10; etc.).

**Recomendación:** eliminar `04-debates/02` o reducirlo a sección §"Riesgos heredados que sobreviven" (7.1-7.3, que `05` no cubre) y mover el resto a `05`. **Reducción: ~150 líneas**.

### D.4. `01-diagnostico/02-objeciones-y-riesgos.md` ↔ `04-debates/04-anticipacion-objeciones-filosoficas.md` — **solapamiento parcial**

- `01-02` tiene 5 objeciones (sustitución nominal, irrefutabilidad por nivel, vaguedad de patrón, redundancia, sobreextensión) tratadas con respuesta + compromiso público (~165 líneas).
- `04-04` tiene 7 objeciones más sofisticadas (F1-F10) tratadas con concesión + distinción + argumento + costo (~324 líneas), con citas paginadas a Quine, Carnap, Hacking, Strawson, Goff, Chalmers.

Solapan al menos en: sustitución nominal (`01-02 obj.1` ↔ `04-04 §X`), redundancia con vecinos (`01-02 obj.4` ↔ `04-04 §X`), sobreextensión (`01-02 obj.5` ↔ tema de cap 06-01).

**Decisión humana:** el `01-diagnostico/02` tiene función histórica (refleja el diagnóstico original que motivó las correcciones); pero su contenido ya está absorbido y refinado en `04-04`. Opciones:
- Conservar `01-02` como bitácora de diagnóstico inicial (mover a `01-diagnostico/_extendido/`).
- Reducir `01-02` a 1 página de "diagnóstico que motivó cada corrección" → punteros a `04-04` y `01-01`.

### D.5. `00-proyecto/02-preguntas-objetivos-hipotesis.md` — **redundancia con el cierre**

Las hipótesis H1-H7 (líneas 30-69), objetivos específicos 1-14 (76-91), y aporte original (94-103) replican lo que `06-cierre/01-conclusion-demostrativa.md` y `00-proyecto/00-introduccion.md` ya afirman. El archivo cumple función académica formal (preguntas-objetivos-hipótesis es estructura doctoral canónica), pero **podría reducirse en ~30 %** sin pérdida si las hipótesis H1-H7 se acortan a una línea cada una con referencia al capítulo verificador.

---

## E. Recomendación operativa por hallazgo

Notación: SINT = sintetizar en el archivo canónico; MOV = mover a sub-carpeta `<cap>/_extendido/` para carga web bajo demanda; ELIM = eliminar; H-J = decisión filosófica que requiere firma Jacob/Steven.

| ID | Hallazgo | Acción recomendada | Líneas estimadas |
|----|----------|--------------------|----:|
| A.1 | EDI redefinido 6× | SINT a glosario + una mención inline en mapa operadores | ~10 |
| A.2 | Estructura pre-ontológica re-parafraseada en 06-cierre/04 | SINT (1 sola definición por archivo) | ~15 |
| A.3 | "Irrealismo operativo" duplicado en 06-cierre/04 | SINT | ~10 |
| A.5 | "Dossier de 14 componentes" como letanía | SINT (reducir menciones decorativas a ≤3) | ~25 |
| A.7 | Modo demostrativo/programático en plantilla | SINT (referencia cruzada) | ~10 |
| A.11 | "Cuatro invariantes" repetidos en cap 05-07 | SINT | ~8 |
| B.1 | "40 casos NO son la tesis" duplicado en 06-04 | SINT (2 ocurrencias en 06-04 → 1) | ~5 |
| B.2 | "Wolfram fundamenta; nosotros disciplinamos" 6× | SINT (canónico en 04-01; resto referencias) | ~30 |
| B.3 | Lista íntegra de 14 rivales 3× | SINT (lista solo en 04-01) | ~20 |
| B.4 | "Novedad de articulación" 8× | SINT (reducir a 3) | ~25 |
| B.5 | "0/1500 falsos positivos" 5× | SINT (reducir a 3) | ~15 |
| B.6 | Caso 30 v1 → v2 lección epistémica 4× | SINT (reducir a 2) | ~12 |
| B.7 | "Dossier + asimetría como filtro simultáneo" 6× | SINT (reducir a 2) | ~18 |
| B.9 | **Inconsistencia 4/5/6 escenarios falsables** | **H-J** (decisión de cuál es el conteo canónico) | ~30 |
| B.11 | Bloque Strong/Weak/Null repetido 4× | SINT | ~40 |
| B.12 | Manierismo "régimen declarado / demostración parcial" | SINT (poda a 1/cap) | ~20 |
| C.1 | `04-debates/01` ↔ `04-debates/03` duplican micro-tablas | **H-J + MOV** detalle por rival a `04-debates/_extendido/` | ~250 |
| C.2 | Marcadores `**Tabla X.Y.Z**` triplicados | Ejecutar `scripts/number_tables.py --dedup` | ~80 |
| C.3 | 14 componentes enumerados 2× | SINT en 05-00 | ~17 |
| C.4 | Criterios A-F enumerados 2× | SINT (uno solo) | ~10 |
| C.7 | Tabla "NO promete/SÍ promete" en 04-02 y 04-05 | SINT a 04-05 | ~30 |
| D.1 | `00-01` + `00-03` fundir | **H-J** | ~150-200 |
| D.2 | `06-02` + `06-04` + `06-05` triple defensa | **H-J + SINT** | ~200-300 |
| D.3 | `04-02` absorbido por `04-05` | SINT + conservar §7 de 04-02 | ~150 |
| D.4 | `01-02` ↔ `04-04` | **H-J** (MOV de 01-02 a `_extendido/` o reducción a punteros) | ~100 |
| D.5 | `00-02` H1-H7 verbosas | SINT (compresión a 1 línea/hipótesis) | ~40 |

**Suma neta estimada de la reducción aplicable sin decisión humana:** ~370-450 líneas.
**Suma neta estimada con decisiones humanas (D.1-D.4 y B.9):** ~1 100-1 400 adicionales.

---

## Top 5 hallazgos de mayor impacto (priorización)

1. **D.2 — Triple solapamiento `06-cierre/02 + 04 + 05` en defensa oral.** Tres archivos cubren la misma defensa con formatos distintos (~530 líneas combinadas). La consolidación a un solo archivo Q&A + un solo archivo de versiones cortas reduce 200-300 líneas y elimina la inconsistencia interna (4 vs 5 vs 6 escenarios falsables).

2. **C.1 — `04-debates/01` y `04-debates/03` duplican la discriminación contra rivales.** `01` da micro-tablas + texto por cada uno de los 14 rivales (~551 líneas); `03` da la tabla síntesis + replica las discriminaciones (~239 líneas). Si se conserva `03` íntegro y se mueve el detalle de `01` a una sub-carpeta `_extendido/`, el cuerpo del manuscrito gana ~250 líneas sin perder argumento (el detalle queda accesible).

3. **D.3 — `04-debates/02` (6 límites genéricos) está subsumido por `04-debates/05` (20 limitaciones L1-L20).** Las 6 categorías de `02` son repetidas con menos rigor que las L1-L20 de `05`. Eliminar `02` o reducirlo a §"Riesgos heredados" (~30 líneas) cierra 150 líneas redundantes.

4. **B.9 — Inconsistencia entre "4 / 5 / 6 escenarios de fracaso falsables" en cap 06-02, 06-04 y 04-02.** No es solo redundancia: es una **vulnerabilidad de defensa oral**. Un tribunal hostil señalaría la incongruencia. Hay que fijar UN número canónico (recomendado: las 20 limitaciones L1-L20 son la lista exhaustiva; los "escenarios falsables" deberían ser un subconjunto declarado, probablemente las 5 condiciones en `06-04`).

5. **C.2 — Bug del numerador `scripts/number_tables.py`.** Las etiquetas triplicadas (`**Tabla A.X.Y.**` + `**Tabla X.Y.Z.**` + `**Tabla X.Y.Z.**`) suman ~80 líneas en blanco a través de ≥30 archivos. No es decisión filosófica — es ejecutar el script de des-duplicación. Bajo riesgo, alto retorno visual.

---

## Decisiones que requieren juicio humano (Jacob/Steven)

Estos puntos no admiten cierre desde la asistencia técnica (CLAUDE.md §3):

1. **¿Se fusionan `00-proyecto/01-estructura-general.md` y `00-proyecto/03-plan-de-capitulos.md`?** La separación puede tener función pedagógica (uno cuenta la arquitectura de carpetas, otro la lógica argumental capítulo a capítulo). La asistencia recomienda fusión por solapamiento; Jacob decide.

2. **¿Qué hacer con `01-diagnostico/02-objeciones-y-riesgos.md`?** Es la formulación "inicial" de las objeciones críticas; el `04-debates/04` las trata con más profundidad filosófica. Opciones: (a) mover `01-02` a `_extendido/` como bitácora histórica; (b) reducirlo a punteros; (c) conservar tal cual porque tiene valor narrativo en el diagnóstico estructural. Decisión Jacob.

3. **¿Cuál es el conteo canónico de "escenarios falsables"?** Hay 4, 5, 6 según el capítulo. La lista L1-L20 de limitaciones declaradas es exhaustiva; los "escenarios de fracaso global" deberían ser un subconjunto fijo. **Esta es decisión filosófica del autor**: ¿qué tendría que pasar para que la tesis acepte haber fracasado? La asistencia no puede cerrar esta pregunta sin sustituir voz autoral.

4. **¿Se mueven los desarrollos extensos rival por rival a `04-debates/_extendido/`?** La asistencia recomienda movimiento por volumen (cap 04-01 = 551 líneas, el archivo más largo del manuscrito). Pero el "engagement con el rival" es voz filosófica de Jacob; cualquier movimiento debe respetar lo que él considere indispensable mantener en el cuerpo principal.

5. **¿La "fórmula de cierre oral" memorizable está bien repetida en 4 lugares (`06-02`, `06-04`, `06-05`) o es síntoma de redundancia rituálica?** CLAUDE.md §1 señala los "totem de completud" como auto-indulgencia, pero también es legítimo memorizar la frase en defensa oral. Decisión sobre cuántas veces necesita aparecer.

6. **Política de "modo programático" en aplicaciones (cap 05-01 a 05-04).** Estos cuatro capítulos comparten estructura (conjetura + criterio de elevación + interlocutores). No fueron auditados aquí por extensión, pero superficialmente parecen seguir buena disciplina. Hay que revisarlos si la decisión D.1-D.4 abre espacio para más síntesis.

---

## Materiales que NO recomiendo eliminar, aun siendo "repetidos"

CLAUDE.md §2 exige no marcar cerrado lo que sobrevive crítica hostil. Hay redundancias aparentes que tienen función:

- **Reenvíos cruzados a cap 02-04 §4 (Maturana-Varela + Haken)** desde 6 sitios distintos: **no es redundancia, es patrón canónico de anclaje único**. Conservar.
- **Glosario operativo (`00-proyecto/07`)** define muchos términos que también se definen en su capítulo de desarrollo: **función explícita de referencia rápida**. Conservar.
- **Cita de Warren 2006 p. 358** repetida en 3 lugares (introducción, 01-01 falencia 1, 02-04 §1, 05-05): **es la cita canónica del caso ancla; su repetición es función argumental, no decoración**.
- **Plantilla del dossier (`03-formalizacion/07`)** parece duplicar la enumeración de 03-02 §3: **es plantilla para nuevos casos, no redundancia conceptual**.
- **Disputa con panpsiquismo (Strawson/Goff/Chalmers) en `04-04 §X`**: única, larga, con citas paginadas. Conservar íntegra; cualquier compresión dañaría la voz filosófica.

---

## Caveats y trabajo no realizado

- **No auditados en detalle:** capítulos individuales `05-01` a `05-04` (aplicaciones programáticas), `02-fundamentos/02-03-05-06` (epistemología, categorías, temporalidad, normativa), `03-formalizacion/03-04-05` (auditoría, operacionalización κ, ética). Estos pueden tener redundancias internas que esta pasada no detectó.
- **No verificado el `08-consistencia-st/`** (instrucción del usuario).
- **No verificadas referencias bibliográficas** (CLAUDE.md §5 exige otra pasada con `/verify-citations`).
- **La estimación de "líneas reducibles"** asume reescritura inteligente; el ahorro real puede ser 20-30 % menor por las costuras necesarias.
- **No se ejecutó `scripts/number_tables.py`** ni ningún otro script — esta es auditoría read-only.

---

## Cierre

La tesis NO está sobrecargada por **contenido filosófico redundante**; está sobrecargada por **letanía estructural**: las mismas cifras (40 casos, 14 componentes, 13 condiciones, 0/1500 falsos positivos, EDI=0.55, 30 órdenes de magnitud) reaparecen como totem en abstract, introducción, conclusión y tres versiones de defensa oral. Esto es exactamente el patrón CLAUDE.md §1 advierte ("8/8 verdes, 42/42 ROBUSTO como totem de completud").

La síntesis recomendada no toca el cuerpo argumental sustantivo (cap 02 ontología, 03 formalización, 04-04 objeciones filosóficas, 05-06 corpus multiescala). Toca: (a) el aparato de letanía en cap 00, 06; (b) la duplicación 04-01/04-03 en rivales; (c) las múltiples versiones de defensa oral en 06-02/04/05; (d) la duplicación 04-02/04-05 en limitaciones. Si Jacob acepta las síntesis recomendadas y autoriza las decisiones marcadas H-J, el manuscrito puede comprimirse del orden de 1 500-2 000 líneas sin perder defensibilidad. La política CLAUDE.md §10 se cumple: **lo que no eleva la defensa, se borra**.
