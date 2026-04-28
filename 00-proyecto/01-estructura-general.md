# Estructura general del proyecto

## Función de esta carpeta

Esta carpeta define la **arquitectura del manuscrito doctoral**. Su función no es repetir `tesis.md` sino organizarlo como obra de tesis con orden de lectura, jerarquía conceptual y secuencia argumentativa que cierre la demostración.

## Principio de organización

El proyecto se organiza desde una lógica explícita y verificable. Cada carpeta resuelve una pregunta del manuscrito; cada capítulo dentro de cada carpeta resuelve un nodo del argumento. La consigna: ningún capítulo entra sin función argumental clara, ningún capítulo se queda sin demostración o sin marca explícita de modo programático.

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

## Módulos del proyecto

### 1. Diagnóstico (carpeta `01-diagnostico/`)

Responde a:

> ¿qué le falta a la tesis para ser académicamente robusta y qué objeciones discriminantes debe enfrentar?

Aquí se identifican falencias estructurales (capítulo 01-01) y objeciones discriminantes anticipadas (capítulo 01-02). Las bitácoras de sesión que produjeron las correcciones quedan en `01-diagnostico/sesiones/` como trazabilidad histórica, no como cuerpo argumental.

### 2. Fundamentos (carpeta `02-fundamentos/`)

Responde a:

> ¿qué sostiene exactamente la tesis y qué no sostiene?

Aquí se fijan ontología material-relacional (02-01), epistemología de la compresión multiescala (02-02), categorías-objetos-propiedades-identidad reformulados (02-03), y nivel B con asimetría L1↔B↔L3↔S (02-04).

### 3. Formalización (carpeta `03-formalizacion/`)

Responde a:

> ¿cómo se vuelve operativa la tesis?

Aquí están aparato formal mínimo (03-01), criterios de legitimidad y dossier de anclaje (03-02), auditoría ontológica como protocolo replicable (03-03), procedimiento empírico de κ vía baja dimensionalidad (03-04).

### 4. Debates (carpeta `04-debates/`)

Responde a:

> ¿frente a qué posiciones se define la tesis y qué límites reconoce?

Aquí se discriminan catorce posiciones rivales con tablas públicas (04-01) y se nombran las limitaciones genuinas que sobreviven a las correcciones (04-02).

### 5. Aplicaciones (carpeta `05-aplicaciones/`)

Responde a:

> ¿qué gana la investigación al usar esta tesis en casos reales?

Aquí están los criterios de admisión que distinguen modo demostrativo y modo programático (05-00), aplicaciones programáticas a mente (05-01), biología (05-02), sistemas técnicos (05-03), instituciones (05-04), y el caso ancla canónico en modo demostrativo (05-05).

### 6. Cierre (carpeta `06-cierre/`)

Responde a:

> ¿la tesis queda demostrada y cómo se proyecta el programa posterior?

Aquí están conclusión demostrativa con condiciones de fracaso falsables (06-01), guía de defensa oral en tres tiempos (06-02), hoja de ruta para tesis final (06-03).

### 7. Bibliografía (carpeta `07-bibliografia/`)

Reúne corpus PDF y mapa de interlocutores funcionales por capítulo. Su conversión en bibliografía formal con citas rigurosas es trabajo del paso 2 de la hoja de ruta.

### 8. Consistencia ST (carpeta `08-consistencia-st/`)

Capa de validación lógica local: formalizaciones mínimas del núcleo argumental con comprobación automática de no-contradicción y trazabilidad textual.

### 9. Tareas (carpeta `Tareas/`)

Backlog duro: crítica radical previa al manuscrito, pasos no negociables, mega-tareas estratégicas (programa científico general, traducción de obras, operacionalización-validación, benchmark rivales, corpus ST), tareas documentales delegables.

## Lógica de redacción

### Fase 1: consolidación del problema y del marco

- diagnóstico cerrado;
- preguntas, objetivos, hipótesis fijados;
- ontología y epistemología consolidadas;
- nivel B y asimetría L1↔B↔L3↔S explícitos.

### Fase 2: consolidación del aparato

- operadores definidos con criterio de admisión y de fallo;
- dossier de anclaje como filtro;
- procedimiento empírico de κ;
- auditoría ontológica como protocolo replicable.

### Fase 3: contraste y demostración

- discriminación pública contra rivales;
- caso ancla canónico con dossier completo;
- aplicaciones programáticas con criterios de elevación;
- limitaciones nombradas.

### Fase 4: cierre y proyección

- conclusión demostrativa con condiciones de fracaso;
- guía de defensa oral;
- hoja de ruta hacia tesis final.

## Criterio rector

> La tesis debe ser simultáneamente más precisa que el borrador original, más defendible que un manifiesto y más operativa que una posición filosófica programática.

Esto exige tres disciplinas simultáneas:

- **disciplina ontológica**: no inflar entidades, definir patrón con cinco condiciones técnicas;
- **disciplina epistemológica**: no confundir categoría con realidad, operacionalizar la compresión;
- **disciplina metodológica**: no dejar la tesis inmune a evaluación, exigir dossier de catorce componentes.

## Resultado que esta arquitectura produce

Una vez completada, esta arquitectura permite que cualquier lector pueda responder sin ambigüedades:

1. cuál es la tesis (capítulo 06-01);
2. por qué hace falta (capítulos 01-01 y 02-01);
3. contra qué discute (capítulo 04-01);
4. con qué herramientas trabaja (capítulo 03-01 y 03-04);
5. cómo se evalúa (capítulo 03-02 y 06-01);
6. dónde funciona ya con datos (capítulo 05-05);
7. dónde queda como programa (capítulos 05-01 a 05-04);
8. cuáles son sus límites (capítulo 04-02);
9. cómo se defiende oralmente (capítulo 06-02);
10. qué falta para tesis final (capítulo 06-03).

## Diferencia con el borrador original

El manuscrito-fuente (`tesis.md`) sigue siendo la formulación extensa y continua de la intuición central. El resto del repositorio convierte esa intuición en arquitectura doctoral defendible mediante seis correcciones estructurales (capítulo 01-01):

- caso ancla canónico (Warren 2006) en lugar de generalidad sin demostración;
- patrón estabilizado definido técnicamente como atractor empírico;
- aparato formal con protocolo empírico de κ vía baja dimensionalidad;
- nivel B (conductual-biológico) en lugar de L2 neurobiológico estrecho;
- condiciones de fracaso global falsables;
- bibliografía integrada por capítulo con interlocutor principal.

## Política de subcarpetas

Material auxiliar (bitácoras de sesión, dossiers individuales, notas tácticas) se conserva en subcarpetas internas:

- `01-diagnostico/sesiones/` — trazabilidad histórica del diagnóstico;
- `05-aplicaciones/dossiers/` (cuando se construyan) — dossiers detallados por dominio;
- `06-cierre/notas/` (si procede) — notas operativas no incorporadas.

La raíz de cada carpeta de capítulo contiene solo el texto canónico que entra en el manuscrito.

## Cierre

Si el manuscrito-fuente es el cuerpo vivo de la idea, esta arquitectura define su esqueleto. Sin esqueleto, incluso una idea brillante termina filosóficamente amorfa. Con esqueleto, la idea se vuelve manuscrito, el manuscrito tesis, y la tesis programa de investigación.
