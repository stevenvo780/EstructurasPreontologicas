# Aparato formal mínimo de la tesis

## Por qué hace falta formalizar

El formalismo no aparece aquí para decorar la tesis con símbolos, sino para disciplinar el pensamiento. Su función es impedir tres confusiones recurrentes:

1. confundir realidad con modelo;
2. confundir categoría con entidad;
3. confundir complejidad con falta de estructura.

La formalización propuesta es deliberadamente mínima: quiere ganar precisión sin inventar una metafísica matemática nueva.

## Niveles del esquema general

La tesis puede describirse mediante cinco niveles articulados.

### `O0`: sustrato ontológico

Corresponde a la realidad material dinámica. No es todavía un modelo; es el campo efectivo de procesos, cuerpos, interacciones, flujos y restricciones.

### `E1`: acceso empírico

Corresponde a las operaciones de medición, observación, registro e intervención.

### `F2`: formalización basal

Corresponde a la representación de variables y dependencias mediante grafos, redes dinámicas o sistemas de estados.

### `F3`: organización estructural superior

Corresponde a hipergrafos, módulos, clases estructurales, equivalencias y operaciones de compresión multiescala.

### `S4`: nivel semántico

Corresponde al vocabulario comunicable: mente, organismo, mercado, memoria, servicio, identidad, institución, función.

## Primer operador: medición o extracción

La tesis propone representar el acceso al fenómeno mediante el operador:

```text
μ : R → X
```

Donde:

- `R` representa el dominio efectivo de realidad material;
- `X` representa un conjunto de variables observables, inferidas u operacionalizadas.

### Función de `μ`

`μ` no crea la realidad; la recorta para volverla investigable. Eso significa que toda formalización ya presupone una selección.

## Segundo operador: grafo basal

El primer nivel de modelización puede expresarse como:

```text
G = (V, E, W, T)
```

Donde:

- `V` son variables, nodos o estados relevantes;
- `E` son relaciones o dependencias;
- `W` son pesos, signos, intensidades o condiciones;
- `T` representa temporalidad, dinámica o reglas de actualización.

## Qué puede representar `E`

La tesis no restringe `E` a una sola noción de causalidad. Una relación puede representar:

- causalidad directa;
- condición de posibilidad;
- restricción;
- acoplamiento;
- constitución funcional;
- dependencia histórica;
- correlación robusta con valor explicativo.

### Advertencia importante

No toda relación dibujable merece lugar en el modelo. Solo las relaciones que afectan la inteligibilidad del fenómeno respecto de una pregunta dada.

## Tercer operador: hipergrafo

Muchos fenómenos no son adecuadamente representables mediante relaciones binarias. Para esos casos aparece:

```text
H = (V, 𝓔)
```

Donde `𝓔` es un conjunto de hiperaristas que conectan múltiples nodos simultáneamente.

## Qué gana el hipergrafo

Permite representar:

- co-dependencias múltiples;
- módulos funcionales;
- ensamblajes contextuales;
- restricciones globales;
- configuraciones que no se reducen a pares.

Esto es útil cuando un fenómeno depende de combinaciones y no solo de enlaces punto a punto.

## Cuarto operador: compresión

La operación de compresión puede representarse como:

```text
κ : G → H
```

No significa convertir mágicamente el grafo en otra cosa. Significa reagrupar partes de una estructura compleja en una unidad operativa más tratable.

### Sentido filosófico de `κ`

`κ` modela el paso desde dependencias finas a organización de orden superior.

### Sentido epistemológico de `κ`

`κ` reduce complejidad conservando la estructura relevante para una pregunta `Q`.

## Quinto operador: expansión

La operación inversa puede expresarse así:

```text
ε : n → Gₙ
```

Donde un nodo comprimido `n` se abre en el subgrafo `Gₙ` que explicita su composición interna.

### Función de `ε`

La expansión permite verificar si una compresión seguía siendo legítima o si estaba ocultando diferencias decisivas.

## La pregunta como parámetro del modelo

Un punto decisivo de la tesis es que la legitimidad de una representación depende de una pregunta explícita. Por eso conviene introducir:

```text
Q = problema explicativo o interventivo
```

La formalización no se evalúa en abstracto, sino respecto de `Q`.

## Criterio mínimo de legitimidad formal

Puede expresarse así:

```text
κ(G) es legítima respecto de Q si preserva las dependencias de G necesarias para explicar, predecir o intervenir sobre Q.
```

Esta definición evita dos errores:

1. creer que una compresión vale por ser simple;
2. creer que solo el máximo detalle garantiza fidelidad.

## Niveles y escalas sin multiplicación de mundos

El paso `G → H` no introduce una nueva realidad. Introduce una nueva organización descriptiva y explicativa. Esto es crucial.

- el grafo no es la realidad;
- el hipergrafo no es la realidad;
- ambos son modos de representar restricciones reales de la realidad.

## Ejemplo breve: sistema distribuido

### A nivel `F2`

Podemos representar variables como:

- DNS;
- certificados;
- balanceador;
- base de datos;
- cola;
- latencia;
- permisos;
- tráfico.

### A nivel `F3`

Podemos comprimir todo eso en módulos como:

- acceso externo;
- autenticación;
- persistencia;
- observabilidad;
- recuperación.

Si la pregunta es `¿por qué cayó producción?`, tal vez haya que expandir `persistencia` o `acceso externo`. Si la pregunta es `¿cómo describir la arquitectura general?`, la compresión puede ser suficiente.

## Ejemplo breve: memoria

### A nivel `F2`

Se representan variables y dependencias entre codificación, consolidación, recuperación, contexto, plasticidad, tarea y uso.

### A nivel `F3`

Puede hablarse de `memoria episódica`, `memoria de trabajo` o `memoria procedimental` como módulos compresivos.

La tesis no niega esas categorías, pero exige que se justifique qué patrón están comprimiendo y bajo qué condiciones dejan de servir.

## Límite del formalismo

El formalismo propuesto no sustituye investigación empírica ni análisis filosófico detallado. Sirve para:

- ordenar el problema;
- fijar operadores;
- controlar pérdidas de detalle;
- comparar niveles;
- evitar reificaciones rápidas.

Si se usa para mucho más que eso, empieza a sobreactuar. Y en filosofía conviene que los símbolos no se vuelvan más dramáticos que el argumento.

## Fórmula final

El aparato formal mínimo de la tesis puede resumirse así:

1. se extraen variables desde un dominio material;
2. se representan dependencias en un grafo basal;
3. se detectan organizaciones de orden superior;
4. se comprime o expande según la pregunta;
5. se evalúa la legitimidad del recorte por su capacidad de preservar estructura relevante.

Eso basta para dar a la tesis una columna metodológica precisa sin sacrificar su alcance filosófico.