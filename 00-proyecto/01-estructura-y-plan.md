# Estructura del proyecto y plan de capítulos

> **BORRADOR-IA — pendiente firma H-J8.** Este archivo es el resultado de la fusión D.4 (`00-proyecto/01-estructura-general.md` + `00-proyecto/03-plan-de-capitulos.md` → un solo archivo) ejecutada como consolidación editorial bajo Fase 2 de la síntesis 2026-05-11. Reemplaza ambos archivos sin afectar `TesisFinal/Tesis.md` (ninguno entra al ensamblado). Origen: `Bitacora/2026-05-11-sintesis-tesis/borradores/D4-proyecto-01-03-decision.md`. Decisión pendiente Jacob: (1) si `01-estructura-y-plan.md` debe promoverse al cuerpo del manuscrito como capítulo introductorio metodológico; (2) si la política «un capítulo = una pregunta = un interlocutor principal» debe sobrevivir como doctrina declarada en este archivo o sólo operativa en el cuerpo.

## Función de esta carpeta y de este archivo

Esta carpeta aloja **andamiaje del repositorio**: arquitectura del manuscrito doctoral, formulación institucional y materiales operativos no incorporados al cuerpo ensamblado. La **fuente de verdad del orden de capítulos** del manuscrito es `TesisFinal/build.py` (lista `PARTS`), no este archivo. Este documento sirve para **navegación humana del repositorio**: explica cómo se relacionan las carpetas numeradas con el ensamblado final, qué pregunta resuelve cada módulo y bajo qué política se admiten capítulos.

La fuente de verdad textual son los capítulos individuales en `00-…/`, `02-…/`, `03-…/`, `04-…/`, `05-…/`, `06-…/` y derivados. El manuscrito-fuente histórico (formulación extensa continua de la intuición central) está archivado en `Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md`.

## Principio de organización

El proyecto se organiza desde una lógica explícita y verificable. **Cada carpeta resuelve una pregunta del manuscrito; cada capítulo dentro de cada carpeta resuelve un nodo del argumento.** La consigna: ningún capítulo entra sin función argumental clara, ningún capítulo se queda sin demostración o sin marca explícita de modo programático.

```
1. PRIMERO se diagnostica el estado del manuscrito-fuente.
2. LUEGO se fijan preguntas, objetivos, hipótesis, plan.
3. DESPUÉS se desarrolla el núcleo: ontología y epistemología.
4. MÁS TARDE se formaliza el aparato y se opera el método.
5. A CONTINUACIÓN se contrasta con rivales bajo criterios públicos.
6. ENSEGUIDA se prueba en caso ancla canónico (modo demostrativo).
7. PARALELAMENTE se articula extensión programática a otros dominios.
8. FINALMENTE se cierra con conclusión demostrativa, defensa y hoja de ruta.
```

Esto evita el defecto frecuente en proyectos filosóficos ambiciosos: pasar demasiado rápido de una intuición potente a una teoría total sin haber fijado problema, criterios, aparato y casos.

## Política de admisión de capítulos

Reglas que cualquier capítulo debe satisfacer para entrar al manuscrito ensamblado (consolidación de `01-estructura-general.md §"Lógica de redacción"` + `03-plan-de-capitulos.md §"Política de capítulos"` + `§"Regla práctica"`):

1. **Pregunta declarada.** Cada capítulo responde a una pregunta específica enunciada al inicio, en una línea, y verificada en el cierre.
2. **Interlocutor principal nombrado.** Cada capítulo nombra su interlocutor bibliográfico principal y los secundarios (la distribución vive en `06-cierre/03-hoja-de-ruta-para-tesis-final.md:88-104`).
3. **Modo declarado.** Cada aplicación se etiqueta inequívocamente como **modo demostrativo** (dossier completo + EDI + discriminación rival verificable) o **modo programático** (con criterios públicos de elevación).
4. **Función argumental clara.** Ningún capítulo se admite sin función argumental verificable; si un capítulo no genera la necesidad del siguiente, todavía está demasiado ensayístico y poco arquitectónico.
5. **Transición preparada.** Cada capítulo deja preparada la transición al siguiente, no se cierra en sí mismo.

## Mapa carpeta → Partes del manuscrito ensamblado

Tabla canónica que cruza las nueve carpetas numeradas del repositorio con las cinco Partes que `TesisFinal/build.py` ensambla en `TesisFinal/Tesis.md`. Para el orden y los anchors exactos, consultar `TesisFinal/build.py` `PARTS` directamente.

| Carpeta | Pregunta que responde | Parte(s) del manuscrito | Capítulos ensamblados |
|---|---|---|---|
| `00-proyecto/` | ¿Cómo se organiza este proyecto? (andamiaje + introducción + resumen + glosario) | Front matter + Introducción | `00-introduccion.md`, `05-resumen-y-abstract.md`, `06-listas-figuras-tablas-abreviaturas.md`, `07-glosario-operativo.md` |
| `01-diagnostico/` | ¿Qué le falta a la tesis para ser académicamente robusta? | Introducción | `03-estado-del-arte.md` |
| `02-fundamentos/` | ¿Qué sostiene exactamente la tesis y qué no sostiene? | Parte I — Fundamentos | 6 capítulos (ontología, epistemología, categorías, anclaje, temporalidad, normatividad) |
| `03-formalizacion/` | ¿Cómo se vuelve operativa la tesis? | Parte II — Aparato y método | 8 capítulos (aparato formal, operadores, dossier, auditoría, κ vía EDI, ST, ética) |
| `04-debates/` | ¿Frente a qué posiciones se define y qué límites reconoce? | Parte IV — Discusión crítica | 5 capítulos (debates, tabla rivales, objeciones, limitaciones, consolidación L1-L20) |
| `05-aplicaciones/` | ¿Qué gana la investigación al usar esta tesis en casos reales? | Parte III — Evidencia empírica | 10 capítulos (criterios, mapa corpus, caso ancla, inter-dominio, inter-escala, caso 30, 4 programáticos) |
| `06-cierre/` | ¿La tesis queda demostrada y cómo se proyecta? | Parte V — Cierre | 2 capítulos en manuscrito (`01-conclusion-demostrativa.md`, `03-hoja-de-ruta-para-tesis-final.md`); el resto (`02-…`, `_extendido/`) son satélites de defensa oral fuera del ensamblado |
| `07-bibliografia/` | Corpus PDF + interlocutores funcionales por capítulo | Bibliografía | `01-bibliografia-orientativa.md` |
| `08-consistencia-st/` | Validación lógica formal local | (interna; ensamblada vía cap 13 de Parte II) | suite ST de 24 teorías formales |
| `09-simulaciones-edi/` | Motor empírico (40 casos del corpus EDI) | Parte III — Evidencia empírica | `README.md` (cap 18) + `30_caso_behavioral_dynamics/README.md` (cap 20) |
| `10-apendices-tecnicos/` | Tablas crudas + figuras | Apéndices técnicos mínimos | 3 apéndices (tablas inter-dominio, tablas inter-escala, figuras Mermaid) |

**Notas operativas:**

- Los archivos `00-proyecto/01-…`, `02-…`, `03-…`, `04-…` **no entran al manuscrito ensamblado**: son andamiaje interno del repositorio (formulación institucional, preguntas-objetivos-hipótesis, este plan).
- Los archivos `06-cierre/02-…`, `06-cierre/_extendido/…` **no entran al ensamblado**: son satélites de defensa oral.
- Las bitácoras en `Bitacora/<fecha>-<tema>/` son trazabilidad histórica, no canon vivo.

## Lógica de fases del proyecto

### Fase 1: consolidación del problema y del marco

- diagnóstico cerrado;
- preguntas, objetivos, hipótesis fijados;
- ontología y epistemología consolidadas;
- nivel B y asimetría L1↔B↔L3↔S explícitos.

### Fase 2: consolidación del aparato

- operadores definidos con criterio de admisión y de fallo;
- dossier de anclaje como filtro;
- procedimiento empírico de κ vía EDI;
- auditoría ontológica como protocolo replicable.

### Fase 3: contraste y demostración

- discriminación pública contra rivales;
- caso ancla canónico con dossier completo;
- aplicaciones programáticas con criterios de elevación;
- limitaciones nombradas (L1-L20 en cap 04-05).

### Fase 4: cierre y proyección

- conclusión demostrativa con condiciones de fracaso falsables;
- guía de defensa oral (`06-cierre/02-…` + `_extendido/`);
- hoja de ruta hacia tesis final (`06-cierre/03-…`).

## Criterio rector

> La tesis debe ser simultáneamente más precisa que el borrador original, más defendible que un manifiesto y más operativa que una posición filosófica programática.

Esto exige tres disciplinas simultáneas:

- **disciplina ontológica**: no inflar entidades, definir patrón con cinco condiciones técnicas;
- **disciplina epistemológica**: no confundir categoría con realidad, operacionalizar la compresión;
- **disciplina metodológica**: no dejar la tesis inmune a evaluación, exigir dossier de catorce componentes.

## Diferencia con el borrador original y trazabilidad histórica

El manuscrito-fuente histórico (archivado en `Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md`) es la formulación extensa y continua de la intuición central. El resto del repositorio convierte esa intuición en arquitectura doctoral defendible mediante seis correcciones estructurales documentadas (capítulo 01-01):

- **caso ancla canónico** (caso 05-05 del corpus, ver capítulo 05-05), elegido porque formula explícitamente el patrón conductual como atractor de un sistema agente-entorno acoplado: «Agent–environment interactions give rise to emergent behavior that has a dynamics of its own [...] stable behavioral solutions correspond to attractors in the behavioral dynamics, and transitions between behavioral patterns correspond to bifurcations» (Warren, 2006, p. 359), en lugar de generalidad sin demostración;
- **patrón estabilizado** definido técnicamente como atractor empírico;
- **aparato formal** con protocolo empírico de κ vía baja dimensionalidad operacionalizado como EDI;
- **nivel B** (acoplamiento empírico genérico multiescalar) en lugar de L2 neurobiológico estrecho;
- **condiciones de fracaso global falsables** según el conteo canónico unificado de cap 06-01 §2 (3 escenarios falsables con criterio externo + 1 condición de prioridad histórica; decisión pendiente firma H-J8 declarada en TAREAS_PENDIENTES.md);
- **bibliografía integrada por capítulo** con interlocutor principal nombrado.

## Política de subcarpetas y materiales auxiliares

Material auxiliar (bitácoras de sesión, dossiers individuales, notas tácticas, extensiones bajo demanda) se conserva en subcarpetas internas. Convenciones del repositorio:

1. **`<NN-carpeta>/sesiones/`** — trazabilidad histórica de sesiones de trabajo (ejemplo: `01-diagnostico/sesiones/`).
2. **`<NN-carpeta>/dossiers/`** — dossiers detallados por dominio (cuando se construyan; ejemplo proyectado: `05-aplicaciones/dossiers/`).
3. **`<NN-carpeta>/notas/`** — notas operativas no incorporadas (ejemplo: `06-cierre/notas/`).
4. **`<NN-carpeta>/_extendido/`** — convención de manuscrito para extensiones bajo demanda (versiones largas, bancos completos, materiales de consulta). Usado por `06-cierre/_extendido/` para versiones extendidas de defensa oral.
5. **Materiales operativos integrados al ensamblado:**
   - glosario operativo → preliminares (`00-proyecto/07-…`);
   - mapa de operadores formales → Parte II (cap 08);
   - plantilla del dossier de anclaje → Parte II (cap 10);
   - matriz de auditoría ontológica → Parte II (cap 11);
   - cuadros comparativos con rivales → Parte IV (cap 26);
   - mapa de aplicaciones → Parte III (cap 16);
   - versiones cortas de defensa → fuera del manuscrito en `06-cierre/02-…` + `_extendido/`;
   - bibliografía consolidada → capítulo final (`07-bibliografia/01-…`).

La raíz de cada carpeta de capítulo contiene solo el texto canónico que entra en el manuscrito (cuando corresponde) o el andamiaje (cuando no).

## Lectura cruzada

- `TesisFinal/build.py` — fuente de verdad del orden de capítulos (lista `PARTS`).
- `00-proyecto/00-introduccion.md` — síntesis introductoria final del manuscrito (estructura en cinco Partes para el lector).
- `00-proyecto/02-preguntas-objetivos-hipotesis.md` — preguntas, objetivos e hipótesis fijados.
- `00-proyecto/04-formalizacion-institucional.md` — documentación administrativa (director, programa, fechas).
- `01-diagnostico/01-…` — diagnóstico estructural que motivó las correcciones.
- `06-cierre/01-conclusion-demostrativa.md` — siete condiciones de demostración y deuda residual.
- `06-cierre/03-hoja-de-ruta-para-tesis-final.md` — hoja de ruta post-defensa con interlocutores principales/secundarios.

## Cierre

Si el manuscrito-fuente es el cuerpo vivo de la idea, esta arquitectura define su esqueleto. Sin esqueleto, incluso una idea brillante termina filosóficamente amorfa. Con esqueleto, la idea se vuelve manuscrito, el manuscrito tesis, y la tesis programa de investigación.
