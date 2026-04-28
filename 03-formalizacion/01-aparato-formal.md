# Aparato formal mínimo

## Función de este capítulo

Este capítulo fija el aparato formal de la tesis. El formalismo no aparece para decorar con símbolos sino para disciplinar el pensamiento. Su función es impedir tres confusiones recurrentes — confundir realidad con modelo, categoría con entidad, complejidad con falta de estructura — y producir un lenguaje común que cualquier capítulo posterior pueda invocar. Lo que aquí se define es lo que los capítulos 03-02 (criterios), 03-03 (auditoría) y 03-04 (operacionalización empírica) operan. La formalización es deliberadamente mínima: gana precisión sin inventar metafísica matemática.

## Tesis del capítulo

> El aparato mínimo de la tesis consiste en cinco operadores (μ, G, H, κ, ε) y una pregunta paramétrica (Q con tolerancia τ). Cada operador tiene definición precisa, criterio de admisión, criterio de fallo y procedimiento empírico de aplicación. Ningún operador entra en el manuscrito sin protocolo. La formalización no es ontología adicional: es disciplina de inteligibilidad de la ontología material-relacional sobre fenómenos empíricamente accesibles.

## 1. Niveles del esquema general

El aparato articula cinco registros del proyecto:

```
O0  — sustrato ontológico                      (capítulo 02-01)
E1  — acceso empírico                          (régimen de medición)
F2  — formalización basal (grafo G)            (este capítulo)
F3  — organización estructural superior (H, κ) (este capítulo y 03-04)
S4  — semántica revisada (S)                   (capítulo 02-03)
```

El nivel B (conductual-biológico, capítulo 02-04) no es un registro paralelo; es el lugar donde E1 vive cuando el dominio es psicológico-conductual: la medición se hace sobre el par dinámico acoplado.

> Notas terminológicas: cada operador definido a continuación está glosado además en el **Anexo A.1 — Glosario operativo**. Cualquier término técnico introducido en este capítulo (μ, G, H, κ, ε, dossier de anclaje, EDI, LoE, asimetría L1↔B↔L3↔S) puede consultarse allí con definición autocontenida y referencias cruzadas.

> Capa de consistencia lógica: las afirmaciones declarativas centrales del aparato y los teoremas mínimos que la tesis afirma derivar (núcleo ontológico, criterios de legitimidad, debates) están formalizadas adicionalmente en `08-consistencia-st/theories/` mediante el lenguaje ST (`@stevenvo780/st-lang`). Esta capa no sustituye el trabajo filosófico: opera como verificador automático de consistencia interna y trazabilidad. Los reportes generados se consolidan en `08-consistencia-st/reports/` y se usan internamente para detectar contradicciones simples antes de cada cierre de versión del manuscrito.

## 2. La pregunta como parámetro: Q

Toda formalización se evalúa respecto a una pregunta `Q` con tolerancia explícita:

```
Q = (φ, τ, R)
```

donde:

- `φ` es la formulación del problema explicativo o interventivo;
- `τ` es la tolerancia: qué diferencia entre modelo y datos cuenta como aceptable;
- `R` es el régimen de medición: qué se mide, con qué instrumento, bajo qué condiciones.

`Q` se fija antes del intento de modelización y queda fechada. Cambiar `Q` después de un fallo invalida el ciclo y exige reiniciar admisión. Esto cierra la objeción de irrefutabilidad por nivel (capítulo 04-02).

## 3. Operador 1: medición μ

### 3.1. Definición

```
μ : R → X
```

`μ` es la operación de medición, observación, registro o intervención que recorta el dominio efectivo de realidad `R` en un conjunto de variables `X` observables, inferidas u operacionalizadas.

### 3.2. Qué entra en X

Para fenómenos a nivel B, `X` puede incluir variables conductuales, informacionales ecológicas, biomecánicas, de tarea e históricas (capítulo 02-04). Para otros dominios, `X` se especifica análogamente.

### 3.3. Criterio de admisión de μ

Una medición es admisible si:

- el régimen `R` está especificado (instrumento, condiciones, frecuencia de muestreo);
- las variables `X` están operacionalizadas (definición precisa de qué se cuenta);
- la repetibilidad está documentada (protocolo accesible a tercero).

### 3.4. Criterio de fallo

Si las variables medidas no son repetibles bajo el mismo régimen, el problema no es del modelo: es de la medición. La tesis no avanza con μ defectuoso.

## 4. Operador 2: grafo basal G

### 4.1. Definición

```
G = (V, E, W, T)
```

donde:

- `V` son nodos (variables, estados, unidades) sobre el conjunto X;
- `E` son aristas (relaciones, dependencias, transiciones);
- `W` son pesos (intensidades, signos, condiciones de activación, sensibilidades);
- `T` son reglas de actualización dinámica (ecuaciones diferenciales, leyes de control, transiciones probabilísticas).

### 4.2. Qué representa E

`E` no se reduce a una sola noción de causalidad. Una arista puede representar:

- causalidad directa, condición de posibilidad, restricción, acoplamiento dinámico, constitución funcional, dependencia histórica, dependencia contextual, correlación robusta con valor explicativo verificada por intervención.

La tesis prohíbe la arista decorativa: solo entran las relaciones que afectan la inteligibilidad del fenómeno respecto de Q.

### 4.3. Criterio de admisión de G

Una arista `(v_i, v_j) ∈ E` es admisible si:

- es detectable por covarianza condicional bajo régimen R;
- es robusta a intervenciones específicas (`do(v_i)` cambia `v_j`);
- su peso `w_{ij}` tiene unidad dimensionalmente coherente.

### 4.4. Criterio de fallo

Si una arista no resiste intervención (manipular `v_i` no cambia `v_j` de la manera predicha), se elimina o se reformula. La consistencia interna del grafo no basta: se exige consistencia con intervención.

## 5. Operador 3: hipergrafo H

### 5.1. Por qué hace falta

Muchos fenómenos no se explican con relaciones binarias. Hay acoplamientos múltiples (proteína que depende de varias moléculas a la vez, conducta que depende de organismo + entorno + tarea simultáneamente, institución que depende de cuerpos + documentos + normas + reconocimientos), restricciones globales y configuraciones de orden superior.

### 5.2. Definición

```
H = (V, 𝓔)
```

donde `𝓔` es un conjunto de hiperaristas que conectan conjuntos de nodos simultáneamente. Cada hiperarista `e ∈ 𝓔` es un subconjunto de `V` con su régimen de actualización conjunta.

### 5.3. Para qué sirve

`H` permite representar:

- co-dependencias múltiples;
- módulos funcionales con frontera identificable;
- ensamblajes contextuales;
- restricciones globales que se actualizan conjuntamente;
- agregaciones de tarea que no se reducen a pares.

### 5.4. Criterio de admisión

Una hiperarista es admisible si la dependencia conjunta no se reduce sin pérdida a una conjunción de relaciones binarias bajo Q. La prueba es la diferencia inferencial: si separar la hiperarista en pares produce las mismas predicciones, no hay hiperarista; hay grafo binario.

## 6. Operador 4: compresión κ

### 6.1. Definición

```
κ : G → G*
```

`κ` es la operación que reemplaza una subestructura compleja `G' ⊂ G` por una unidad operativa `n_{G'}` (nodo, módulo, clase) en un grafo más tratable `G*`, cuando el detalle interno de `G'` no produce diferencia inferencial relevante para Q.

### 6.2. Sentido filosófico

`κ` modela el paso desde dependencias finas a organización de orden superior sin postular sustancia nueva. La unidad comprimida es real en sentido estructural si su atractor es empíricamente identificable; teórica si solo modeliza regularidades sin captura empírica directa.

### 6.3. Sentido operativo

`κ` reduce dimensionalidad efectiva conservando la estructura relevante para Q. La operacionalización empírica detallada está en el capítulo 03-04. Aquí se fija el criterio:

> κ(G) = G* es legítima respecto a Q si y solo si existe un sistema dinámico de baja dimensión sobre G* que (a) reproduce las trayectorias observadas dentro de τ, (b) preserva atractores, repulsores y bifurcaciones empíricamente identificadas, (c) predice respuestas a perturbaciones e intervenciones, (d) no oculta una transición que sí ocurre en los datos.

### 6.4. Criterio de fallo

Si alguno de los cuatro requisitos falla, la compresión está empíricamente desautorizada y debe revisarse o sustituirse por expansión ε.

## 7. Operador 5: expansión ε

### 7.1. Definición

```
ε : n → G_n
```

`ε` abre un nodo comprimido `n` para mostrar su subgrafo interno `G_n` cuando la pregunta lo exige.

### 7.2. Cuándo es necesaria

Tres signos obligan a expandir:

- la compresión actual impide distinguir casos relevantes para Q;
- la estructura interna modifica predicciones o intervenciones;
- el sistema se aproxima a una bifurcación donde el régimen interno cambia.

### 7.3. Criterio de admisión

`ε` es legítima si la expansión produce ganancia inferencial mayor que el costo introducido. La regla:

> expandir cuando la estructura interna produce diferencias inferenciales relevantes; comprimir cuando el detalle interno no las produce.

### 7.4. Importancia de ε para κ

Una compresión sin expansión inversa disponible es caja negra ilegítima. La existencia operativa de `ε` es condición de admisión de `κ`. Esto cierra la cláusula de reversibilidad parcial del capítulo 02-02.

## 8. Cómo se articulan los operadores

El flujo canónico de uso es:

```
1. Fijar Q = (φ, τ, R)                                       [pregunta paramétrica]
2. Aplicar μ : R → X                                          [medición]
3. Construir G = (V, E, W, T) sobre X                         [grafo basal]
4. Detectar relaciones de orden superior → H si procede       [hipergrafo]
5. Ensayar κ : G → G* (vía baja dimensionalidad empírica)     [compresión]
6. Validar G* contra datos: reproducción, generalización,
   topología, intervención                                    [validación]
7. Si validación pasa: G* admisible respecto a Q              [admisión]
8. Si validación falla en alguna prueba: aplicar ε en la
   subestructura responsable                                  [expansión]
9. Iterar hasta admisión o declarar fallo trazado             [cierre o deuda]
```

Este flujo no es retórico. Es protocolo y se aplica al caso ancla canónico (capítulo 05-05) y a cualquier aplicación admisible.

## 9. Niveles y escalas sin multiplicación de mundos

El paso `G → G*` mediante κ no introduce una nueva realidad. Introduce una nueva organización descriptiva y explicativa. Los operadores formalizan **registros** del mismo plano material:

- el grafo no es la realidad;
- el hipergrafo no es la realidad;
- el modelo reducido no es la realidad;
- todos son representaciones de restricciones reales del sustrato.

La cláusula es estricta: ninguna entidad del aparato formal se reifica. La discusión filosófica de este punto está en capítulo 02-01 §10 y en capítulo 04-02.

## 10. Ejemplo canónico: caso ancla

En el caso ancla canónico (Warren 2006, capítulo 05-05) los operadores se instancian así:

| Operador | Instanciación |
|---|---|
| Q | `¿qué dirección de marcha adopta un humano caminando hacia meta y evitando obstáculo?` con τ = error en `r²` ≤ 0.02 |
| μ | Captura de movimiento en VENLab (Brown), 12 m × 12 m, head-mounted display, sonic-inertial tracking, frecuencia 60 Hz |
| X | heading φ, error de heading β, velocidad v, distancia a meta d_g, ángulo a meta ψ_g, distancia a obstáculo d_o, ángulo a obstáculo ψ_o |
| G | Grafo de dependencias entre las variables anteriores con leyes físicas (gravedad, biomecánica) y leyes informacionales (flujo óptico, dirección egocéntrica) como T |
| H | Hiperarista que conecta meta + obstáculo + heading cuando hay biestabilidad de ruta |
| κ | Reducción a sistema de segundo orden φ̈ = −b φ̇ − k_g(φ−ψ_g)(e^{−c1·d_g}+c2) + k_o(φ−ψ_o)(e^{−c3|φ−ψ_o|})(e^{−c4·d_o}) con d=2 dimensiones efectivas y r²=0.980/0.975 |
| ε | Reapertura cuando aparecen patologías no capturadas (obstáculos como puntos, agentes con dinámica de evitación propia) |

Este ejemplo no es ilustrativo: es la prueba de que el aparato opera empíricamente sobre datos reales con resultados públicamente verificables. Cualquier otra aplicación admisible debe alcanzar instanciación equivalente.

## 11. Ejemplo programático: sistemas técnicos

En sistemas distribuidos los operadores se instancian programáticamente (sin medición experimental controlada equivalente al caso ancla):

| Operador | Instanciación |
|---|---|
| Q | `¿por qué cayó producción en t = T?` con τ = identificación de la causa raíz |
| μ | Logs, métricas, traces, checks de salud |
| X | Latencia, throughput, error rate, certificate validity, DNS resolution time, queue depth |
| G | Grafo de dependencias entre componentes técnicos |
| H | Hiperaristas para fallos cascada que involucran múltiples servicios |
| κ | Compresión a nivel de servicio cuando la pregunta es disponibilidad global |
| ε | Reapertura cuando la pregunta es diagnóstico fino |

La diferencia con el caso ancla: aquí no hay datos experimentales con sistema controlado y ecuaciones ajustadas. Es modo programático (capítulo 05-03) hasta que se construya el análogo demostrativo.

## 12. Diálogo con interlocutores formales

### 12.1. Pearl — grafos causales y do-calculus

Pearl (2009, *Causality*, 2.ª ed., cap. 3, p. 70) define el operador de intervención: *"the action `do(X = x)` represents an experiment in which the variable X is set to value x by an outside intervention, while the rest of the model remains unchanged"*. La tesis absorbe esta operación en `G` y `E` con dos restricciones: (a) los grafos representan dependencias del sistema acoplado, no causalidad lineal aislada; (b) la admisión de aristas exige `do`-test, no solo correlación. La métrica EDI es **operacionalización directa de un do-test**: ablación del acoplamiento ODE con preservación del forcing exógeno, comparada contra coupled completo.

### 12.2. Ladyman y Ross — realismo estructural informativo

Ladyman y Ross (2007, *Every Thing Must Go*, §3.4) sostienen que la ontología fundamental es estructural: *"the world is not made of things or stuff but of structure all the way down"*. La tesis converge parcialmente: las invariantes son, en este marco, las propiedades preservadas por `κ`. Diverge en que la tesis no postula estructura como ontología fundamental sino como **descripción operativa del sustrato material**: la estructura es estructura **del** sustrato dinámico, no flotante (cap 02-01). Esta es la diferencia que la tabla A.4 codifica como discriminación en el criterio A (anclaje material).

### 12.3. Strogatz, Kelso, Haken — sistemas dinámicos no lineales

Strogatz (1994, *Nonlinear Dynamics and Chaos*, cap. 6, p. 168) define el atractor como *"a closed set A such that any trajectory that comes close enough to A approaches A as t → ∞"*. Kelso (1995, *Dynamic Patterns*, cap. 3, p. 73) extiende el lenguaje al dominio de coordinación: *"the qualitative change in the form of behavioral patterns is termed a phase transition or bifurcation"*. Haken (1977/2004, *Synergetics*, cap. 1) introduce los parámetros de orden como variables macroscópicas que dominan la dinámica cerca de transiciones. La tesis adopta este vocabulario **sin modificación**: la formalización del aparato es precisamente este vocabulario, ahora aplicado bajo dossier de admisión.

### 12.4. Symbolic Theory Language (ST)

ST se usa como capa de validación de consistencia local (capítulo 08-consistencia-st). Su función no es probar verdad sino detectar tensiones internas en la formalización del manuscrito.

## 13. Límites del formalismo

El aparato no sustituye investigación empírica ni análisis filosófico detallado. Sirve para:

- ordenar el problema;
- fijar operadores con criterio público;
- controlar pérdidas de detalle;
- comparar niveles bajo Q común;
- evitar reificaciones.

Si el formalismo se usa para mucho más, sobreactúa. La cláusula:

> ningún operador se justifica si no produce ganancia inferencial concreta sobre alguna `Q`.

## 14. Fórmula final

> El aparato formal mínimo consiste en una pregunta paramétrica Q y cinco operadores (μ, G, H, κ, ε) con criterios de admisión, criterios de fallo y procedimientos empíricos de aplicación. Los operadores no son ontología adicional: son disciplina de la inteligibilidad de la ontología material-relacional sobre fenómenos empíricamente accesibles. Su valor se prueba en el caso ancla canónico (capítulo 05-05); su programa de extensión se especifica en los capítulos de aplicaciones.

## 15. Lectura cruzada

- ontología que el aparato modeliza: capítulo 02-01;
- epistemología que justifica la operación de κ y ε: capítulo 02-02;
- nivel B donde se mide: capítulo 02-04;
- criterios de legitimidad de los operadores: capítulo 03-02;
- protocolo de auditoría que usa el aparato: capítulo 03-03;
- procedimiento empírico de κ: capítulo 03-04;
- aplicación demostrativa: capítulo 05-05;
- aplicaciones programáticas: capítulos 05-01 a 05-04.
