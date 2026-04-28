# El nivel B: anclaje conductual-ecológico

## Función de este capítulo

Este capítulo introduce el nivel pleno que el borrador original tenía mal definido. Lo que llamaba `L2 — neurobiológico local` saltaba precisamente el nivel donde el fenómeno vive: el organismo acoplado con su entorno, ejecutando una tarea, condicionado por una historia. La respuesta del profesor a la pregunta L1/L2/L3 lo nombró como condición de anclaje y el caso ancla canónico (Warren 2006) lo ocupa con derecho propio. Este capítulo lo formaliza, le da ecuaciones canónicas y lo articula con los demás registros.

## Tesis del capítulo

> El nivel donde la tesis material-relacional gana o pierde anclaje empírico no es la neurobiología aislada ni el lenguaje psicológico ordinario, sino el sistema dinámico acoplado organismo–entorno bajo restricciones de tarea, físicas, informacionales e históricas. A ese nivel lo llamamos B. La asimetría L1↔B↔L3↔S es el protocolo formal de traducción que prohíbe la sustitución nominal y operacionaliza la auditoría categorial.

## 1. Los cuatro registros articulados

```
L1 — psicológico/ordinario     : fija qué pregunta importa (vínculo indirecto)
B  — conductual-biológico      : ancla la respuesta (vínculo directo y traduccional)
L3 — estructural-relacional    : reconstruye formalmente las dependencias detectadas
S  — semántica revisada        : recoge las categorías que sobreviven a la auditoría
```

Lo que el borrador llamaba L2 se reparte entre B (donde están conducta, biomecánica, información ecológica, tarea, historia) y los tramos neurobiológicos específicos cuando hagan falta para una pregunta concreta. Neurobiología no desaparece: queda como zoom de B cuando la pregunta lo exige.

## 2. Qué incluye B

`B` es el dominio de las relaciones materialmente sostenidas entre cinco familias de variables. Ninguna es prescindible. El recorte habitual `cerebro versus mundo` deja fuera tarea e historia, y por eso es mal anclaje.

### 2.1. Organismo

Cuerpo, biomecánica (longitudes, masas, frecuencias naturales, rigidez aparente), repertorio motor, sistemas perceptivos, plasticidad, estado fisiológico. Cuando proceda, actividad neural específica como subgrafo de B.

### 2.2. Entorno

Superficies, objetos, fuerzas físicas (gravedad, fricción, restitución), propiedades materiales, otros agentes con sus dinámicas.

### 2.3. Información ecológica

Patrones detectables del flujo óptico, acústico y háptico que estructuran el entorno. Ejemplos canónicos verificados en el caso ancla:

- `τ`: razón entre tamaño angular óptico y su tasa de cambio; especifica tiempo hasta contacto;
- `τ̇`: derivada temporal; especifica adecuación de la deceleración;
- `τ_bal = θ/θ̇`: razón entre ángulo y velocidad angular; especifica tiempo hasta vertical;
- ángulo de declinación bajo el horizonte: especifica distancia;
- foco de expansión del flujo óptico: especifica dirección de auto-movimiento (heading φ_flow);
- error de heading β = φ − ψ_g: ángulo entre dirección actual y dirección de meta.

Estas variables son materialmente reales: están inscritas en la geometría y la física del entorno y pueden ser detectadas por sistemas perceptivos calibrados. No son representaciones internas.

### 2.4. Tarea

Objetivo (meta espacial, altura constante, parar antes del obstáculo), restricciones (rapidez, riesgo, costo energético), criterios de éxito o fracaso. La tarea selecciona qué variables son relevantes y qué tolerancia es aceptable. Selectividad que hace que la dinámica observable a nivel B sea de baja dimensión: la tarea ya hizo el primer trabajo de compresión antes de que el modelador llegue.

### 2.5. Historia

Trayectorias previas, aprendizaje, desarrollo, evolución, exposición a perturbaciones. Sin esta dimensión no se explica por qué dos agentes con la misma fisiología frente al mismo entorno producen conductas distintas. La historia entra como variables explícitas en el dossier de anclaje cuando el dominio lo requiere.

## 3. El acoplamiento como estructura básica de B

La unidad mínima de descripción a este nivel no es el organismo aislado ni el entorno aislado. Es el par dinámico acoplado:

```
ė = Φ(e, F)              dinámica del entorno bajo fuerzas F
ȧ = Ψ(a, i)              dinámica del agente bajo información i
F = β(a)                 fuerzas que el agente ejerce sobre el entorno
i = λ(e)                 información ecológica disponible en el entorno
```

Estas cuatro ecuaciones (formalmente equivalentes a las del ciclo percepción-acción de Warren) capturan dos acoplamientos simultáneos:

- **acoplamiento mecánico**: el agente actúa físicamente sobre el entorno y el entorno reacciona;
- **acoplamiento informacional**: el entorno produce patrones detectables que modulan la dinámica del agente.

La trayectoria conductual del par no es la suma de la trayectoria del agente y la del entorno: es la trayectoria del sistema conjunto en su espacio de estados.

### Consecuencias ontológicas

1. el `patrón estabilizado` (capítulo 02-01) se identifica con un atractor del sistema acoplado;
2. la `restricción real` se identifica con la estructura del campo vectorial (dónde converge, dónde diverge, dónde transiciona);
3. la `causalidad circular` se opera técnicamente: las componentes determinan la dinámica conjunta y la dinámica conjunta retroalimenta a las componentes a través de las leyes de control.

## 4. Self-organization: el modelo positivo de la emergencia

El borrador rechazaba el emergentismo fuerte (correctamente) pero solo como negación. Faltaba el modelo positivo. La tesis lo proporciona aquí:

> Un fenómeno es emergente, en el sentido del marco, cuando dos o más sistemas dinámicos materialmente acoplados generan en el espacio conjunto estabilidades, inestabilidades y transiciones que no están preinscritas en ninguno de los componentes aislados pero tampoco son sustancia nueva.

Esta es la formulación técnica de self-organization: la emergencia es estabilización dinámica del sistema acoplado, no aparición de entidad adicional. Tres rasgos:

- **upward causation**: las componentes producen la dinámica global;
- **downward causation**: la dinámica global retroalimenta a las componentes (las leyes de control quedan ajustadas porque funcionan en el régimen estable);
- **anclaje material**: el fenómeno emergente es materialmente realizado y empíricamente identificable.

Esto cierra la cláusula del capítulo 02-01: la emergencia no multiplica sustancias, opera como auto-organización.

## 5. Información ecológica como categoría central

Una tentación de cualquier ontología material es hacer del entorno una pasividad. La tesis ya lo rechaza, pero el mecanismo positivo aparece aquí: la información ecológica es regularidad estructural del medio físico que el organismo puede detectar sin requerir representación interna.

Para la tesis, esto cierra una brecha: explica cómo la conducta puede ser regular sin requerir un controlador central. La regularidad la pone en parte el entorno; el organismo se acopla a ella vía variables informacionales que no son representaciones sino diferencias materialmente implementadas que modulan la dinámica.

Estatuto ontológico: la información ecológica es realidad de tipo estructural (capítulo 02-01). No es realidad fuerte (no es cuerpo) y no es teórica (no es solo modelo): es la estructura del campo informacional que el acoplamiento detecta y aprovecha.

## 6. Tarea como dimensión constitutiva

La tarea no es accesorio. Es parte del sistema acoplado. Sin tarea no hay variables conductuales relevantes: la pelota es solo un proyectil parabólico, no `pelota a botar a altura constante`. El error de heading β no existe sin meta `ψ_g`. La tarea fija qué cuenta como atractor para una `Q` específica.

Esto tiene una consecuencia para la ontología. Algunos atractores existen incondicionalmente en el sistema (atractor pasivamente estable del raqueteo, repulsor físico del palo invertido, sistema neutralmente estable del frenado). Pero los atractores conductuales típicos son creados por el acoplamiento informacional bajo restricción de tarea: emergen cuando la información se acopla al sistema con una ley de control específica, y desaparecen sin acoplamiento. Esto es realismo estructural en su versión más sutil: el atractor no preexiste a la tarea, pero una vez constituida la tarea el atractor es plenamente real.

## 7. Historia como variable explícita

La historia entra como variables explícitas siempre que la pregunta lo requiera:

- **rondas previas** en una sesión de aprendizaje;
- **fase de aprendizaje** (exploración inicial, calibración, estabilización);
- **calibración perceptiva** previa a la tarea;
- **exposición** a perturbaciones específicas;
- **desarrollo ontogenético** cuando aplica;
- **historia evolutiva** cuando proceda para repertorios motores o sensoriales.

La historia no se trata como variable aparte; se incorpora como parte de las variables `X` del operador μ (capítulo 03-01). Esto permite que las leyes de control sean específicas del agente sin perder la forma funcional general.

## 8. Asimetría L1↔B↔L3↔S como protocolo

Este es el aporte estructural del capítulo. La asimetría no es decorativa; es protocolo de admisión y traducción.

### 8.1. L1 con L3: indirecto y restrictivo

L1 plantea preguntas comunicables (`¿cómo decide alguien por dónde caminar?`, `¿cómo recuerda una secuencia?`). Esas preguntas son indispensables para fijar relevancia. Pero L1 no responde: nombra el explanandum. La respuesta se construye en B y se formaliza en L3. L3 no debe responder con el mismo vocabulario de L1 (so pena de sustitución nominal); le habla a L1 solo a través de sus consecuencias observables.

### 8.2. B con L3: directo y traduccional

L3 es la reconstrucción formal de las dependencias detectadas en B. Cada término de L3 debe traducirse a una variable conductual o biológica medible. Si una clase estructural de L3 no se traduce a B, la clase está flotando — formalismo vacío.

### 8.3. S a posteriori

S (la semántica revisada: las categorías que sobreviven a la auditoría) se gana solo a posteriori. Las categorías que valga la pena conservar son las que: corresponden a atractores reales identificados en B; tienen formalización en L3; discriminan predicción e intervención. Las que no, se eliminan o se descomponen. La aspiración no es eliminar L1; es reconstruir S desde B + L3.

## 9. Qué descarta este nivel

| Tentación rechazada | Razón |
|---|---|
| Reduccionismo neurocéntrico | Sin tarea, entorno e historia, los circuitos no explican conducta |
| Mentalismo solipsista | Las categorías mentales sin acoplamiento con B son etiquetas |
| Formalismo desanclado | L3 sin traducción a B es metafísica formal |
| Conductismo radical | El acoplamiento informacional y la baja dimensionalidad estructural exceden el inventario E–R |
| Cognitivismo computacional fuerte | El sistema no requiere representación interna como recurso primario |

La discusión detallada con cada rival se trata en capítulo 04-01.

## 10. Diálogo con interlocutores

### 10.1. Gibson — psicología ecológica

Gibson (1979) sostiene que la información para la acción está disponible en el entorno y que no se requiere representación interna como recurso primario. La tesis recoge exactamente esto y lo opera: la información ecológica es realidad estructural y se traduce a variables medibles. Donde Gibson queda en la formulación cualitativa, la tesis (vía Warren) avanza al sistema dinámico acoplado.

### 10.2. Maturana y Varela — autopoiesis y enaction

Maturana y Varela proponen autopoiesis como cierre operacional de los sistemas vivos. La tesis recoge la idea de cierre y la operacionaliza como cuenca de atracción del sistema acoplado bajo perturbación, con tolerancia explícita. La autopoiesis no necesita misticismo: es estabilidad asintótica empíricamente verificable.

### 10.3. Varela, Thompson y Rosch — embodied mind

Embodied mind sostiene que la cognición es enacción del acoplamiento agente-entorno. La tesis lo asume como tesis empírica del nivel B. La diferencia: la tesis añade el filtro formal de admisión y la operacionalización empírica de la compresión, que el enactivismo dejaba programáticos.

### 10.4. Andy Clark — extended mind

Clark sostiene que algunos procesos cognitivos se extienden al entorno técnico. La tesis lo opera como caso de B donde el entorno técnico se incorpora a las variables del acoplamiento. La extensión no es metafísica; es decisión sobre qué entra en `X`.

### 10.5. Warren — behavioral dynamics

Warren proporciona el caso paradigmático trabajado del nivel B. La tesis lo recoge como demostración (capítulo 05-05) y como vocabulario operativo (atractor, repulsor, bifurcación, ley de control, dinámica intrínseca, acoplamiento). Warren queda como interlocutor principal de B.

## 11. Consecuencia para el aparato formal

El operador `μ : R → X` debe leerse, en el caso de fenómenos psicológicos y conductuales, como medición a nivel B. `X` puede entonces incluir:

- variables conductuales: trayectoria, error de heading, fase, período, aceleración de impacto, latencia;
- variables informacionales ecológicas: τ, ρ, flujo óptico, ángulo de declinación, fase relativa;
- variables biomecánicas: longitud de extremidad, frecuencia natural, rigidez aparente;
- variables de tarea: objetivo, restricciones, costo, criterio de éxito;
- variables históricas: rondas previas, exposición, fase de aprendizaje.

El grafo `G = (V, E, W, T)` se construye sobre estas variables. Las dependencias que `E` representa son las del sistema acoplado, no las de un agente aislado. Las reglas de actualización `T` son las leyes físicas y las leyes de control empíricamente identificables.

## 12. Cierre

Con la incorporación de B como nivel pleno, la tesis recupera el plano que la respuesta del profesor exigía como condición de anclaje. Las consecuencias son tres:

- la ontología de patrones estabilizados gana su modelo positivo (atractores de sistemas acoplados);
- la epistemología de la compresión gana su test (la dinámica de baja dimensión a nivel B);
- la crítica al mentalismo deja de ser eliminativa para volverse constructiva: no se trata de borrar `mente`, `memoria` o `yo`, sino de reconstruir cuáles atractores conductuales-ecológicos comprime cada una y, a partir de ahí, decidir qué se conserva, qué se reformula y qué se descarta.

## 13. Lectura cruzada

- definición técnica de patrón estabilizado: capítulo 02-01;
- compresión como operación epistémica: capítulo 02-02;
- categorías, objetos, propiedades, identidad: capítulo 02-03;
- aparato formal con μ, G, H, κ, ε: capítulo 03-01;
- procedimiento empírico de κ vía baja dimensionalidad: capítulo 03-04;
- demostración del nivel B en el caso ancla canónico: capítulo 05-05;
- aplicación programática a mente: capítulo 05-01.
