---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
afecta: [00-proyecto/01-estructura-general.md, 00-proyecto/03-plan-de-capitulos.md]
salida_elegida: a
ahorro_lineas_estimado: 175
---

# Decisión D.1: fusión de `00-proyecto/01-estructura-general.md` + `00-proyecto/03-plan-de-capitulos.md`

## Diagnóstico que sostiene la decisión

### Hecho 1 — ninguno de los dos archivos entra al manuscrito ensamblado

`TesisFinal/build.py` (líneas 56–63 y siguientes) ensambla de `00-proyecto/` únicamente: `00-introduccion.md`, `05-resumen-y-abstract.md`, `06-listas-figuras-tablas-abreviaturas.md` y `07-glosario-operativo.md`. Los archivos `01-estructura-general.md`, `02-preguntas-objetivos-hipotesis.md`, `03-plan-de-capitulos.md` y `04-formalizacion-institucional.md` **no entran al manuscrito**: son **documentos de andamiaje y registro institucional del repositorio**, leídos por colaboradores y por sub-agentes del harness, no por el comité que recibirá `TesisFinal/Tesis.md`.

Esto cambia la naturaleza de la decisión: no se está fusionando prosa que el comité vaya a leer. Se está reduciendo la deuda cognitiva del repositorio.

### Hecho 2 — `03-plan-de-capitulos.md` describe una arquitectura obsoleta

`03-plan-de-capitulos.md` plantea un manuscrito en seis capítulos (Cap 1 problema; Cap 2 ontología; Cap 3 epistemología y aparato; Cap 4 rivales; Cap 5 aplicaciones; Cap 6 conclusión) más introducción y conclusión general.

`TesisFinal/build.py` (líneas 66–121) ensambla la realidad: cinco Partes, treinta y un capítulos numerados, separación entre Parte I (Fundamentos, seis capítulos del `02-fundamentos/`), Parte II (Aparato, ocho capítulos del `03-formalizacion/`), Parte III (Evidencia, diez capítulos), Parte IV (Discusión, cinco capítulos), Parte V (Cierre, dos capítulos), Bibliografía y tres Apéndices.

El esquema de seis capítulos del `03-plan-de-capitulos.md` no es una vista pedagógica complementaria del esquema folder-by-folder del `01-estructura-general.md`: **es una versión anterior del proyecto que sobrevivió a las pasadas de reorganización sin actualizarse**. Mantenerla activa es desinformación interna.

### Hecho 3 — el solapamiento real, descontada la obsolescencia

Donde no hay obsolescencia, ambos archivos sí se solapan en:

- enumeración de carpetas/capítulos con su función argumental (≈ 60 % de líneas);
- política de redacción (un capítulo = una pregunta = un interlocutor principal — declarada dos veces, una en `01` "Lógica de redacción", otra en `03` "Política de capítulos" y "Regla práctica");
- lectura cruzada (declarada en `03` líneas 200–207 con la misma vocación que el `01` "Resultado que esta arquitectura produce", líneas 125–138);
- fórmula sintética por carpeta/capítulo (línea 117 de `01` "tesis simultáneamente más precisa…" + líneas 189–198 de `03` "Fórmula útil").

La auditoría D.1 dice ≈ 60 % común; la lectura cuidada lo confirma para la parte no-obsoleta.

### Hecho 4 — la distinción de roles que la auditoría preserva como hipótesis no se sostiene

Hipótesis amable: `01` describe estructura argumental (qué afirma cada parte) y `03` describe estructura formal (qué archivos hay en qué orden). Es la lectura que justificaría no fusionar.

Lectura cerrada de ambos archivos: la hipótesis no se sostiene. `01-estructura-general.md` declara la pregunta argumental por carpeta (sección "Módulos del proyecto", líneas 24–84) y `03-plan-de-capitulos.md` también la declara por capítulo, con prácticamente la misma redacción ("¿qué sostiene exactamente la tesis y qué no sostiene?" en `01`:38 vs. "¿qué existe según esta tesis y bajo qué condiciones?" en `03`:54). Ambos hacen lo mismo trabajo, con desfase de unidad (carpeta vs. capítulo) que ya no se sostiene cuando una carpeta produce seis capítulos del ensamblado.

## Salida elegida: (a) fusión total

Producir `00-proyecto/01-estructura-y-plan.md` que reemplaza ambos archivos y se alinea con la realidad de `TesisFinal/build.py`. Eliminar `00-proyecto/03-plan-de-capitulos.md`.

**Razón corta defendible:** los dos archivos son andamiaje interno del repositorio, no manuscrito; el `03` describe una arquitectura obsoleta de seis capítulos; el solapamiento residual es alto y de tipo letanía; la decisión-coste de mantenerlos separados es mantener desinformación dos veces.

**Razón larga:** la auditoría D.1 los marca como ≈ 60 % comunes "salvo función pedagógica deseada". La función pedagógica que se invocaría (folder-view vs. chapter-view) ya está cubierta por dos artefactos vivos del repositorio: `TesisFinal/build.py` mismo (que es la fuente de verdad del orden de capítulos) y `00-proyecto/00-introduccion.md` líneas 67–75 (que declara la estructura final en cinco Partes para el lector del manuscrito). Un tercer artefacto que diga lo mismo solo introduce deriva: como ya pasó con el `03` actual, que dice seis capítulos cuando el build.py dice treinta y uno.

## Estructura propuesta para el archivo fusionado

`00-proyecto/01-estructura-y-plan.md` (≈ 190 líneas estimadas, frente a 164 + 207 = 371 actuales, ahorro neto ≈ 175 líneas), con secciones:

1. **Función de esta carpeta y de este archivo** — heredada de `01` § "Función de esta carpeta", actualizada para declarar que la fuente de verdad del orden de capítulos es `TesisFinal/build.py` y que este archivo es navegación humana del repositorio.
2. **Principio de organización** — heredado de `01` § "Principio de organización" íntegro (líneas 7–22 de `01`); es lo único que ningún otro artefacto sustituye.
3. **Política de admisión de capítulos** — fusión de `01` "Lógica de redacción" + `03` "Política de capítulos" + `03` "Regla práctica". Un solo bloque de reglas: pregunta declarada, interlocutor principal, modo demostrativo/programático marcado, función argumental verificable.
4. **Mapa carpeta → Partes I–V del manuscrito** — tabla nueva, no presente en ninguno de los dos archivos actuales, que cruza las nueve carpetas (`01-diagnostico/` … `08-consistencia-st/`) con las cinco Partes que `build.py` ensambla. Es lo único que da valor agregado real y elimina la ambigüedad que mantiene viva la doble vista folder/chapter.
5. **Lógica de fases del proyecto** — versión corta de `01` "Lógica de redacción" (Fase 1–4), sin la enumeración detallada que ya está en cada `00-…/` y `02-…/`. Una página, no cuatro.
6. **Criterio rector** — heredado de `01` § "Criterio rector" (líneas 115–123 de `01`); es declaración de doctrina del proyecto, no se repite en otros archivos.
7. **Diferencia con el borrador original y trazabilidad histórica** — heredado de `01` § "Diferencia con el borrador original" (líneas 140–150 de `01`); referencia al `Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md`.
8. **Política de subcarpetas y materiales auxiliares** — heredado de `01` § "Política de subcarpetas" + `03` § "Integración de materiales operativos", fusionados en una sola lista numerada.
9. **Lectura cruzada** — heredada de `03` § "Lectura cruzada" actualizada para apuntar a los `xx-…` y `06-…` actuales.

Lo que se elimina sin pérdida:

- de `01`: § "Resultado que esta arquitectura produce" (líneas 125–138) — la lista de "diez resultados" es decorativa y duplica el mapa carpeta→Parte;
- de `03`: § "Visión general" (líneas 3–6), § "Introducción" + "Capítulo 1" + … + "Capítulo 6" + "Conclusión general" (líneas 15–172) — toda la enumeración capítulo-por-capítulo se reemplaza por la tabla del § 4 que apunta directo a `TesisFinal/build.py`;
- de `03`: § "Fórmula útil" (líneas 189–198) — la "fórmula de seis capítulos" es la versión obsoleta y se elimina.

## Costos asumidos al fusionar

1. **Se pierde la versión-defensa-corta de seis capítulos** del `03-plan-de-capitulos.md`. Riesgo declarado: si Jacob usaba esa enumeración en sustentaciones de avance (mostrar al jurado el manuscrito "en seis capítulos") para no abrumar con los treinta y uno reales, perdería esa pieza retórica.
   - **Mitigación**: la versión sintética por Parte I–V queda en `00-proyecto/00-introduccion.md` líneas 67–75 y en `06-cierre/04-versiones-cortas-defensa.md` (versiones 2/5/15 min). Esa segunda pieza es la que efectivamente se usaría en defensa, no `03-plan-de-capitulos.md`.
2. **Se pierde la lista de interlocutores principales y secundarios por capítulo** que `03` da en sus secciones "Interlocutores" (líneas 43–46, 67–70, 92–95, 114–117, 135–138).
   - **Mitigación**: esa lista vive en `06-cierre/03-hoja-de-ruta-para-tesis-final.md:88-104` (tabla de distribución interlocutor principal / secundarios), señalada por la auditoría C.6 como redundancia paralela ya conocida. Conservar una sola, la de `06-cierre/03`, que está al lado del compromiso de cierre de la bibliografía.
3. **El renombrado del archivo (`01-estructura-y-plan.md`) puede romper enlaces** en bitácoras antiguas y en `harness/`.
   - **Mitigación**: hacer `grep -rn "01-estructura-general\|03-plan-de-capitulos"` antes del merge y actualizar las referencias activas; dejar referencias en bitácoras históricas tal cual (son archivo, no canon vivo).

## Decisión que H-J* debe firmar

Tres cortes filosóficos para Jacob, no técnicos:

1. **¿Se acepta que `00-proyecto/` aloja andamiaje del repositorio, no prosa del manuscrito?** Si la respuesta es no — si Jacob considera que `01-estructura-general.md` debe entrar al cuerpo del manuscrito como capítulo introductorio metodológico —, entonces la decisión cambia: no se fusiona, se promueve `01` a manuscrito (entrando a `build.py`) y se elimina `03` por obsoleto. Es una decisión filosófica sobre qué pertenece al cuerpo defendible.
2. **¿La enumeración de seis capítulos del `03-plan-de-capitulos.md` tenía función retórica que la fusión destruye?** Si Jacob usaba esa enumeración como puente didáctico (manuscrito conceptual de seis capítulos / manuscrito completo de treinta y uno), la fusión la pierde y eso es coste. Si nunca se usó en defensa pública, la fusión es indolora.
3. **¿La política "un capítulo = una pregunta = un interlocutor principal"** debe sobrevivir como doctrina declarada en algún archivo público del repositorio, o ya está suficientemente operativa en el cuerpo del manuscrito como para no necesitar declaración meta?

Si las tres respuestas se inclinan a "fusión limpia", el borrador del archivo fusionado se produce en pasada siguiente. Si alguna se inclina a "no fusionar", se opta por la salida (b): mantener ambos archivos, pero reescribir el `03-plan-de-capitulos.md` desde cero para que refleje la arquitectura real de cinco Partes y treinta y un capítulos del `build.py`, eliminando la obsolescencia que es el daño principal.

## Hallazgo lateral

`03-plan-de-capitulos.md:108` lista trece posiciones rivales (sin Wolfram), incoherente con el inventario canónico de catorce posiciones que la auditoría A.4 fija. Es señal independiente de obsolescencia del archivo: cuando se añadió Wolfram a la discriminación (capítulo 04-01), el `03-plan` no se actualizó. Argumenta a favor de la fusión como saneamiento, no contra ella.
