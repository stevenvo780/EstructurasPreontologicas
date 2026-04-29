# La dinámica de la percepción y la acción, reconstruida bajo monismo material-relacional con compresión multiescala

## MODO DEMOSTRATIVO — CASO ANCLA CANÓNICO

Este capítulo presenta el único caso del manuscrito que entra en **modo demostrativo** según el capítulo 05-00. Su dossier de anclaje está completo en sus catorce componentes con datos públicos, ecuaciones ajustadas, predicciones cumplidas, intervenciones documentadas y comparación rival con discriminación verificable. La tesis se demuestra aquí; los demás dominios quedan en modo programático con criterios de elevación.

> Reconstrucción de Warren, W. H. (2006). *The Dynamics of Perception and Action*. Psychological Review, 113(2), 358–389.

## Por qué este caso

Tres razones convergen en la elección.

Primero, la respuesta del profesor a la pregunta L1/L2/L3 fija explícitamente la condición de anclaje conductual-biológico y propone como ilustración un artículo del tipo de programa de investigación que respalda. El paper de Warren es, dentro de ese género, un caso paradigmático. Trabajar sobre él permite responderle al profesor en su mismo terreno.

Segundo, Warren ofrece todo lo que la tesis exige a un caso demostrativo: variables conductuales medidas, ecuaciones diferenciales ajustadas, atractores y bifurcaciones identificadas, predicciones, intervenciones, comparación con marcos rivales (representacionalismo, control óptimo, modelos internos). Trabajar sobre él prueba si el aparato material-relacional puede absorber un programa científico maduro sin caricaturizarlo y sin redundancia retórica.

Tercero, Warren mismo formula el debate en los términos que la tesis necesita: rechaza atribuir la organización del comportamiento a un controlador centralizado, plan de acción o modelo interno, y propone que la organización emerge de la interacción agente–entorno bajo restricciones físicas, informacionales y de tarea. Esa formulación es ya, sin nombrarla así, una versión específica del monismo material-relacional con compresión multiescala. Lo que hace falta es mostrar que la lectura es exacta y que el aparato de la tesis explicita lo que en Warren queda implícito.

## Tesis del capítulo

> Las dinámicas conductuales que Warren formaliza son sistemas dinámicos acoplados organismo–entorno cuyas estabilizaciones (atractores, repulsores, bifurcaciones) son patrones materiales realmente existentes. Su descripción mediante ecuaciones diferenciales de bajo orden no es un nuevo dominio ontológico ni una representación interna postulada, sino la operación empírica de κ — compresión legítima — sobre el sistema acoplado, traducible a variables biomecánicas, informacionales y de tarea. Bajo el marco material-relacional, el programa de Warren se lee no como antirepresentacionalismo polémico sino como un caso paradigmático de L3 anclado, demostrando lo que la tesis sostiene de manera general.

## Recorte del fenómeno

### Q (la pregunta explicativa)

¿Cómo se organiza el comportamiento adaptativo orientado a meta — locomoción, frenado, equilibrio, intercepción, raqueteo — sin postular un controlador interno, un plan de acción o un modelo del mundo?

### Unidad de análisis principal

El **sistema acoplado agente–entorno** bajo una tarea, no el agente aislado ni el entorno aislado. La tarea (botar pelota, equilibrar palo, frenar antes de obstáculo, caminar hacia meta) es parte constitutiva del sistema porque selecciona variables relevantes y tolerancias.

### Escalas que intervienen

- microsegundos: detección informacional;
- milisegundos a segundos: ciclo percepción–acción;
- segundos a minutos: estabilización de la tarea;
- minutos a horas: aprendizaje y exploración del régimen estable;
- meses a años: desarrollo y calibración perceptiva;
- escalas filogenéticas: morfología y repertorio motor disponible.

La tesis exige no privilegiar una escala única; el modelo de Warren ya cumple esa exigencia.

## El sistema de variables (el dossier de anclaje)

A nivel B (conductual-biológico) se distinguen, para cada tarea, cinco familias de variables.

### Variables del entorno (e)

Posición y velocidad de objetos, geometría de superficies, gravedad, fricción, propiedades materiales (coeficiente de restitución α en raqueteo), restricciones físicas.

### Variables del agente (a)

Estado del sistema motor: ángulos articulares, velocidades, fases, frecuencias preferidas, rigidez aparente, repertorio de coordinaciones motoras.

### Variables informacionales (i)

Patrones detectables del flujo óptico, acústico y háptico. Variables ecológicas críticas:

- `τ`: razón entre tamaño angular óptico y su tasa de cambio; especifica tiempo hasta contacto;
- `τ̇`: derivada temporal de τ; especifica adecuación de la deceleración;
- `τ_bal`: razón entre ángulo del palo y su velocidad angular; especifica tiempo hasta la vertical;
- ángulo de declinación bajo el horizonte: especifica distancia;
- foco de expansión del flujo óptico: especifica dirección de auto-movimiento (heading φ_flow);
- error de heading β = φ − ψ_g: ángulo entre dirección actual y dirección de la meta.

### Variables de tarea

Objetivo (meta espacial, altura constante, parar antes del obstáculo), restricciones (rapidez, riesgo, costo energético), criterios de éxito.

### Variables históricas

Rondas previas, calibración perceptiva en curso, fase de aprendizaje, exposición a perturbaciones.

Estas familias constituyen el conjunto X del operador μ. Toda la formalización subsiguiente se construye sobre ellas y vuelve sobre ellas en cada paso de validación.

## El sistema acoplado en notación canónica

El sistema mínimo es un par dinámico:

```text
ė = Φ(e, F)              dinámica del entorno bajo fuerzas F
ȧ = Ψ(a, i)              dinámica del agente bajo información i
F = β(a)                 fuerzas que el agente ejerce sobre el entorno
i = λ(e)                 información ecológica disponible en el entorno
```

Esto es exactamente el ciclo percepción–acción. En el aparato de la tesis se lee así:

- `Φ` y `Ψ` son las reglas de actualización `T` del grafo `G`;
- `β` y `λ` son los acoplamientos que `E` representa;
- las variables de `e`, `a`, `i` constituyen `V` y `X`.

El sistema completo, escrito en términos de las variables conductuales clave `x` que la tarea selecciona, se reduce a:

```text
ẋ = Ω(x, r)              dinámica conductual de baja dimensión
```

donde `x` son las pocas variables conductuales relevantes y `r` los parámetros del sistema (físicos, biomecánicos, de tarea, informacionales). Esa reducción es la operación κ. Su legitimidad se examina caso por caso con el procedimiento del capítulo de operacionalización.

## Caso 1: Botar la pelota en una raqueta (tarea pasivamente estable)

### Datos y modelo

La pelota cae bajo gravedad `g`, rebota con coeficiente de restitución `α`. La raqueta oscila con amplitud `A` y frecuencia `ω`. Sternad y colegas (1996, 2000, 2001) midieron centenares de impactos en humanos.

La región del espacio de fase donde el bote es **pasivamente estable** corresponde a aceleración de impacto entre `0` y `−2g(1+α²)/(1+α)²`, con máximo en el medio del rango. Si el sistema arranca dentro de esa región, el ciclo se autocorrige sin necesidad de información sensorial.

### Lectura bajo el marco

- `e`: trayectoria de la pelota, gravedad, restitución;
- `a`: fase y amplitud del raqueteo, parámetro de rigidez efectiva `k`;
- `i`: información visual y háptica sobre el ciclo;
- variable conductual clave: aceleración de impacto `ẍ_R`;
- atractor: aceleración de impacto en la región pasivamente estable;
- repulsores: aceleraciones fuera del rango (la dinámica diverge);
- compresión κ: del par dinámico completo a un sistema de bajo orden con aceleración de impacto como variable conductual y rigidez como parámetro de control.

### Resultados que el modelo captura

- la mayoría de los ensayos humanos cae en la región pasivamente estable;
- con práctica, los participantes convergen al máximo de estabilidad pasiva;
- cerrar los ojos no destruye la estabilización (la estabilidad la pone la física, no la información);
- ante una perturbación, los humanos modulan el período de raqueteo según el período aparente del vuelo de la pelota: control discreto sobre un ciclo donde la estabilización principal es física.

### Diagnóstico bajo el marco

Aquí la tesis identifica un atractor **realmente existente** en el sistema acoplado: la región pasivamente estable es una propiedad de la composición pelota–raqueta–gravedad, no del agente. La conducta humana se acopla al atractor, no lo construye. Esto es realismo estructural en sentido fuerte: el patrón existe en el sustrato dinámico antes de cualquier descripción.

La compresión es legítima por las cuatro pruebas: reproduce las distribuciones de aceleración de impacto observadas (Sternad et al. 2001, fig. 5 del paper), generaliza a otros valores de `g` y `α`, conserva el atractor empíricamente identificado, y predice correctamente la respuesta a perturbaciones.

## Caso 2: Equilibrio del palo invertido (tarea activamente estable)

### Datos y modelo

Un palo apoyado sobre el dedo o un carrito es físicamente inestable: hay un punto fijo en la vertical pero es repulsor, no atractor. El equilibrio requiere control activo.

Foo, Kelso y Guzman (2000) propusieron y midieron el uso de la variable informacional `τ_bal = θ/θ̇`. Los participantes mantienen `τ_bal` entre 0.5 y 1.0 modulando periódicamente la rigidez `α` del oscilador del brazo:

```text
F = α τ_bal θ + β x          ley de control derivada
```

### Lectura bajo el marco

- el sistema agente–entorno tiene un repulsor físico (vertical);
- el agente convierte el repulsor en atractor del sistema acoplado mediante una ley de control que usa información ecológica (`τ_bal`) para modular un parámetro físico de su propio cuerpo (`α`);
- la compresión κ entrega un sistema dinámico de pocas variables (ángulo θ, velocidad angular θ̇, posición de mano x, fuerza F) cuyo campo vectorial reproduce la oscilación regular alrededor de la vertical.

### Lo que esto le aporta a la tesis

Aquí se ve con nitidez la **causalidad circular**: la dinámica acoplada produce una estabilización (oscilación controlada) que no estaba en ninguna de las componentes por separado, y esa estabilización retroalimenta a las componentes (las leyes de control quedan ajustadas porque funcionan). Eso es self-organization en el sentido técnico anclado en cap 02-04 §4 (Maturana-Varela 1980, Haken 1977) — emergencia anclada, sin sustancia nueva.

Y se ve también la asimetría B ↔ L3 que la corrección 5 exigía: cada parámetro del sistema reducido se traduce a una variable medible (rigidez aparente del brazo, ángulo del palo, ángulo umbral, intervalo de control). No hay nada flotante.

## Caso 3: Frenado antes de obstáculo (tarea neutralmente estable)

### Datos y modelo

Un agente avanza hacia un obstáculo a velocidad `ż`. La física no fija dónde para; las condiciones iniciales y la fuerza de frenado lo deciden. El sistema es neutralmente estable: no hay atractor físico hasta que la información lo crea.

Lee (1976) propuso que los humanos estabilizan el frenado manteniendo `τ̇ ≈ −0.5`. Yilmaz y Warren (1995) midieron cuatro mil ochocientos ensayos en doce participantes y encontraron exactamente esa relación: la regresión del cambio de fuerza de frenado contra `τ̇` cruza el cero en `τ̇ = −0.52`, con pendiente `−1.04` y `r² = 0.98` (fig. 6 del paper).

La ley de control resultante:

```text
Δx = b(−0.52 − τ̇) + ε
```

### Lectura bajo el marco

Aquí ocurre algo conceptualmente decisivo. El sistema físico no tiene atractor hasta que la información lo introduce. La variable informacional `τ̇` actúa como **parámetro que crea el atractor**: sin acoplamiento informacional el sistema diverge, con acoplamiento `τ̇ = −0.5` el sistema converge a una parada precisa antes del obstáculo.

Esto es lo que en la ontología corregida llamamos `realidad estructural` (§29.2 de la tesis original): la estabilidad no está ni en el agente ni en el entorno por separado, está en el acoplamiento informacional como hecho material. Y es lo que justifica que el realismo estructural sea **moderado**: el atractor no preexiste al acoplamiento, pero una vez constituido el sistema acoplado el atractor es plenamente real, predice intervención (manipular el flujo óptico cambia el frenado) y resiste a explicaciones alternativas (frenado por velocidad o por distancia angular no encajan los datos).

## Caso 4: Locomoción dirigida con obstáculos

### Datos y modelo

Fajen y Warren (2003) modelaron la dirección de marcha humana caminando hacia metas y evitando obstáculos. La variable conductual es el heading φ. Las ecuaciones empíricamente ajustadas:

```text
φ̈ = −b φ̇ − k_g(φ − ψ_g)(e^{−c1 d_g} + c2)
       + k_o(φ − ψ_o)(e^{−c3|φ−ψ_o|})(e^{−c4 d_o})
```

con `b = 3.25`, `k_g = 7.50`, `c1 = 0.40`, `c2 = 0.40`, `k_o = 198.0`, `c3 = 6.5`, `c4 = 0.8`. Las simulaciones reproducen 0.980 de la varianza de los caminos humanos para meta sola y 0.975 para meta con obstáculo.

### Atractores, repulsores, bifurcaciones

- la dirección de la meta `ψ_g` actúa como atractor del heading;
- la dirección de un obstáculo `ψ_o` actúa como repulsor del heading;
- cuando hay múltiples obstáculos, el campo vectorial puede ser biestable: dos rutas posibles (interna y externa) coexisten;
- al cambiar parámetros del entorno (ángulo entre obstáculo y meta, distancia), el sistema atraviesa una bifurcación tangente: una de las rutas pierde estabilidad y solo una queda viable. Esto explica el cambio de ruta sin necesidad de planificación previa.

### Lectura bajo el marco

Este es el caso más contundente para la tesis porque ilustra simultáneamente:

1. **compresión legítima**: cientos de músculos y articulaciones se reducen a una sola variable conductual `φ` y su derivada;
2. **atractores y repulsores como patrones reales**: meta y obstáculo no son representados por el agente; son posiciones del campo vectorial generado por el acoplamiento;
3. **bifurcaciones como transiciones cualitativas**: el cambio de ruta es una bifurcación, no una decisión interna;
4. **predicciones discriminantes**: hipótesis alternativas (estrategia de excentricidad fija, deriva de la meta) se ajustan peor a los datos humanos. La discriminación es pública.

Y también ilustra los límites: el modelo trata obstáculos como puntos, no captura intención de interceptar agentes con su propia dinámica de evitación, no maneja toma de decisiones bajo memoria larga. La tesis exige que esos límites se nombren explícitamente — y aquí están nombrados.

## Tabla de pérdidas y ganancias respecto al programa original de Warren

**Tabla 5.5.1.**

| Aspecto | Conservado tal cual | Reformulado | Añadido por el marco |
|---|---|---|---|
| Ciclo percepción–acción y ecuaciones acopladas | Sí | — | Lectura como par dinámico acoplado canónico |
| Variables informacionales τ, τ̇, τ_bal, β, flujo óptico | Sí | — | Estatuto explícito de `realidad estructural` (modo de ser intermedio entre fuerte y teórica) |
| Atractores, repulsores, bifurcaciones | Sí | — | Identificados como `patrones estabilizados` reales (§5 ontología) |
| Self-organization, causalidad circular | Sí | — | Modelo positivo de emergencia anclada (§11 corregido) |
| Crítica al representacionalismo | Sí | Reformulada como aplicación de la auditoría ontológica (§28) | Test público de fallo: dossier de anclaje |
| Leyes de control | Sí | — | Lectura como `disposiciones relacionales` del sistema (§ propiedades) |
| Reducción de dimensionalidad | Implícita en los modelos | Explícita como operador κ | Procedimiento empírico de admisión y reapertura |
| Modelos internos | Rechazados como recurso primario | Tratados como caja a auditar antes de admitir | Criterio: solo si las pruebas de control no bastan |
| Anclaje a tarea e historia | Reconocido | Constitutivo del sistema acoplado | Variables históricas integradas a `X` por defecto |

## Comparación con marcos rivales

### Modelos internos / control óptimo

Postulan que el sistema nervioso construye representaciones del cuerpo y del entorno y resuelve un problema de optimización para emitir comandos. Bajo el aparato del capítulo de auditoría:

- ¿qué patrón material-relacional comprime `modelo interno`? Una caja desconocida.
- ¿qué dependencias preserva? Las que el modelo sintáctico estipula, no las que se hayan medido.
- ¿qué predicciones discriminantes hace frente a control directo informacional? En las tareas estudiadas (frenado, locomoción, equilibrio, raqueteo), ninguna que mejore. El degrado de desempeño al retirar la información en línea (Wallis et al. 2002, Hildreth et al. 2000) es predicho por el control informacional y no por el modelo interno robusto.
- ¿se traduce a B? Solo nominalmente.

Diagnóstico: en las tareas de Warren, los modelos internos son una compresión sin baja dimensionalidad efectiva justificada y sin predicción discriminante a favor. La tesis los descalifica para esos casos. Los preserva, en cambio, como hipótesis para conducta secuencial, anticipatoria, predictiva y estratégica donde la información ocurrente no basta — exactamente la limitación que Warren mismo reconoce.

### Cognitivismo computacional

Postula que la conducta es ejecución de programas mentales sobre representaciones. Bajo el marco:

- ¿es atractor empírico identificable? No.
- ¿se traduce a B? No directamente.
- ¿agrega poder predictivo? No para las tareas de percepción–acción estudiadas.

Diagnóstico: en este dominio, sustitución nominal (§18.8 de la tesis): cambia el vocabulario sin ganar discriminación. Dejamos abierta la cuestión de si en otros dominios (lenguaje, razonamiento explícito) la situación cambia — el marco exige un caso paradigmático trabajado para cada dominio antes de admitir o rechazar.

### Conductismo radical

Postula que solo cuentan las relaciones entre estímulos y respuestas observables. Bajo el marco:

- recorta correctamente el plano B pero borra la estructura formal L3 que efectivamente discrimina hipótesis;
- niega la realidad estructural de los atractores que sí están empíricamente identificados;
- no provee aparato para tratar acoplamientos múltiples, bifurcaciones, self-organization (en el sentido técnico anclado en cap 02-04 §4).

Diagnóstico: el conductismo radical es un primo empobrecido del marco propuesto. La tesis le añade L3 sin perder anclaje en B.

## Casos de presión para la tesis

Tres casos donde el programa puede fallar y donde la tesis debe responder.

### Caso de presión 1. Conducta secuencial y planificación

Hacer un sándwich, vestirse, tocar una pieza musical: secuencias largas con dependencias no adyacentes. Los datos sugieren que la mera dinámica de baja dimensión no basta. Warren mismo lo señala como límite.

Respuesta de la tesis: el marco no se compromete con eliminativismo. Cuando un dominio exige variables internas no reducibles a información ocurrente, el dossier de anclaje debe incluir esas variables y el modelo debe admitirlas — siempre que pasen el test de discriminación frente a alternativas. La tesis prohíbe la postulación gratuita; no prohíbe la postulación justificada.

### Caso de presión 2. Conducta anticipatoria con metas remotas

Un ajedrecista que evalúa siete jugadas hacia adelante. Aquí la `información ocurrente` no es suficiente, y `acoplamiento físico–informacional inmediato` no captura el fenómeno.

Respuesta: el marco material-relacional no exige un único nivel temporal de acoplamiento. Permite anidar dinámicas (Keijzer, multiscale dynamics) donde los acoplamientos lentos modulan parámetros de las dinámicas rápidas. La planificación se vuelve, dentro del marco, una dinámica de parámetros sobre dinámicas conductuales. Este es modo programático: aún no hay caso paradigmático trabajado del estilo Warren, y la tesis lo reconoce.

### Caso de presión 3. Variabilidad individual

Distintos agentes con la misma fisiología y la misma tarea producen conductas distintas. ¿No erosiona esto la pretensión de atractores universales?

Respuesta: no, si se incluyen variables históricas en el dossier de anclaje. Las leyes de control son producto de aprendizaje y calibración, y los parámetros (no las formas funcionales) varían entre agentes. El atractor es una propiedad del sistema acoplado para un agente con su historia particular. La universalidad reside en la **forma del campo vectorial**, no en sus parámetros — y los datos confirman esa forma con varianzas explicadas mayores al 97%.

## Cómo este caso sostiene la tesis general

Este capítulo demuestra cuatro cosas.

1. **L3 puede anclarse de manera no nominal**: cada parámetro del modelo dinámico se traduce a una variable conductual, biomecánica, informacional o de tarea. Ningún término flota.

2. **κ se opera empíricamente**: la baja dimensionalidad del modelo (uno o dos grados de libertad efectivos para tareas con cientos de grados de libertad físicos) está justificada por análisis de componentes principales sobre los datos, por ajustes con varianza explicada superior al 97%, por preservación de la topología de atractores y bifurcaciones.

3. **Los patrones estabilizados son reales**: los atractores y repulsores de los modelos no son nombres impuestos por el investigador; son propiedades del sistema acoplado que predicen trayectorias, transiciones e intervenciones. Eso es realismo estructural moderado en su versión más fuerte: el patrón existe en el sustrato dinámico, pero su descripción depende del recorte de tarea.

4. **La emergencia funciona como self-organization** (cap 02-04 §4, Maturana-Varela 1980, Haken 1977): las estabilidades observadas no requieren sustancia nueva ni controlador centralizado. Emergen del acoplamiento bajo restricciones físicas, informacionales y de tarea. La causalidad es circular y completamente material.

## Lo que este caso no demuestra

No demuestra que la tesis funcione en todos los dominios mencionados en su versión general. Mente, identidad, mercados, instituciones, ecología requieren cada uno su propio caso paradigmático trabajado. Lo que el capítulo demuestra es que cuando el dominio admite tarea, medición y acoplamiento empíricamente identificable, el aparato funciona y mejora respecto a alternativas. Eso es lo máximo que puede pedir un caso, y es exactamente lo que el profesor pedía.

## Cierre

La frase de Gibson que Warren cita al inicio — `el comportamiento puede ser regular sin ser regulado` — admite ahora una traducción precisa al marco material-relacional: el comportamiento es regular cuando el sistema acoplado tiene atractores empíricamente identificables; no necesita ser regulado por un controlador central porque la regulación está distribuida entre la física del entorno, la biomecánica del cuerpo, la información ecológica y la ley de control aprendida. La tesis no añade misterio a esa formulación; le añade un aparato ontológico, un procedimiento empírico de compresión, un test público de admisión y una taxonomía de errores. El paper de Warren, leído así, no es un argumento contra la representación: es la demostración de que un L3 anclado puede explicar lo que parecía requerir L1 sin caer en sustitución nominal, sin desligarse de B y sin multiplicar sustancias.

Esto es lo que el profesor pedía como demostración. Esto es lo que la tesis material-relacional pretendía hacer. Aquí están en el mismo cuadro.
