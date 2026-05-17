# Criterios de admisión de aplicaciones


## Tesis del capítulo

> Una aplicación entra en modo demostrativo solo si presenta dossier completo de anclaje con datos públicos, ecuaciones ajustadas, predicciones cumplidas, intervenciones documentadas y comparación rival con discriminación verificable. Una aplicación entra en modo programático si presenta conjetura articulada con criterio explícito de elevación a demostrativo: qué datos hacen falta, qué rival se enfrentaría, qué predicción discriminante se buscaría. Cualquier capítulo de aplicación se etiqueta inequívocamente con uno de los dos modos.

## 1. Modo demostrativo: condiciones de admisión

**Nota sobre la genealogía de los catorce componentes.** Los catorce componentes que organizan este dossier fueron extraídos como **abstracción del caso ancla** (cap 05-05, Warren 2006). La adecuación del caso ancla a estos criterios es por construcción y no constituye evidencia independiente de la potencia del marco: cada componente del dossier tiene correspondencia textual en una sección del cap 05-05 (auditoría detallada en `Bitacora/2026-05-04-continuous-run/F05-08-criterios-admision-post-hoc.md`). Lakatos (1978, *The Methodology of Scientific Research Programmes*) llamaría a esto **ad hoc rescue tipo 3**: una rejilla evaluativa diseñada para que sólo el caso paradigmático la satisfaga. La tesis declara el costo y opta por la salida más honesta operativamente: los demás casos del corpus entran en **modo programático** (dossier técnico ejecutado y reproducible) no porque sean ontológicamente menos firmes, sino porque carecen de un caso paradigmático con las catorce dimensiones desarrolladas independientemente. Los catorce componentes funcionan, por tanto, como **agenda regulativa para futuros casos paradigmáticos**, no como medida de adecuación ontológica de los 30 casos ejecutados.

Una aplicación se admite en modo demostrativo si y solo si su dossier de anclaje (capítulo 03-02 §3) está completo en sus catorce componentes con contenido sustantivo:

1. **Pregunta Q fechada** con tolerancia y régimen de medición explícitos;
2. **Variables X** operacionalizadas con régimen R;
3. **Sustrato material instanciante** descrito;
4. **Grafo G** con criterios de admisión de aristas verificados por intervención;
5. **Hipergrafo H** si procede, con justificación de la no-reducibilidad a pares;
6. **Compresión κ** con dimensionalidad efectiva empíricamente justificada;
7. **Atractores, repulsores, bifurcaciones** identificados en datos;
8. **Pruebas de validación**: reproducción dentro de τ, generalización fuera del entrenamiento, preservación topológica, intervención discriminante;
9. **Predicción discriminante** contra rival explícito;
10. **Intervención discriminante** que falsaría la propuesta si se ejecuta y produce resultado contrario;
11. **Operador ε** con protocolo de reapertura;
12. **Traducción B↔L3** completa: cada parámetro de L3 se traduce a variable de B;
13. **Limitaciones declaradas** con régimen de no aplicabilidad;
14. **Comparación rival** con tabla de discriminación.

Un componente vacío o decorativo invalida la admisión en modo demostrativo. La aplicación pasa a modo programático con la marca correspondiente o queda fuera.

## 2. Modo programático: condiciones de admisión

Una aplicación se admite en modo programático si presenta:

1. **Pregunta Q candidata** con formulación explícita (puede no estar fechada);
2. **Esbozo de variables X** con indicación de régimen de medición plausible;
3. **Sustrato material instanciante** descrito en términos generales;
4. **Esbozo de grafo** con dependencias plausibles;
5. **Conjetura de κ** con dimensionalidad esperada (sin demostración);
6. **Atractores conjeturados** con argumento plausible;
7. **Criterio de elevación a demostrativo**: qué datos cuantitativos harían falta, qué rival se enfrentaría, qué predicción discriminante se buscaría;
8. **Diálogo bibliográfico** con interlocutores principales del dominio;
9. **Limitación honesta**: el modo programático no demuestra; conjetura.

La marca `MODO PROGRAMÁTICO` debe aparecer en el primer párrafo del capítulo y en el cierre.

## 3. Por qué la distinción es importante

### 3.1. Honestidad académica

Una tesis que presenta como demostraciones lo que son conjeturas se debilita en defensa oral. Un evaluador competente detecta inmediatamente la asimetría entre caso ancla y dominios adicionales. Mejor declararla.

### 3.2. Trazabilidad del programa

La distinción permite que la hoja de ruta (capítulo 06-03) priorice exactamente qué dominios necesitan trabajo demostrativo y en qué orden. Sin la distinción, la tesis se queda en una nube uniforme de aplicaciones todas igual de creíbles, todas igual de inverificadas.

### 3.3. Vigilancia contra sustitución nominal

Una aplicación que solo renombra el fenómeno con vocabulario del marco sin producir predicción discriminante es candidata a sustitución nominal. La obligación de criterio de elevación obliga a articular la diferencia.

## 3.bis. Modo técnico-ejecutado: tercera categoría operativa

[BORRADOR-IA · requires: H-J* — integración 2026-05-17 tras audit process-verifier cap 05] La dicotomía demostrativo/programático cubre los casos del manuscrito principal (§4.1 y §4.2), pero **no captura el régimen bajo el cual operan los 40 casos del corpus EDI** (30 inter-dominio + 10 inter-escala, capítulos 05-06 y 05-07). Para esos casos se reconoce explícitamente una tercera categoría operativa: **modo técnico-ejecutado**.

### 3.bis.1. Definición

Un caso está en modo técnico-ejecutado si:

1. **El aparato EDI se ejecuta completo**: sonda ODE + ABM contrafáctico + permutación (N ≥ 999) + bootstrap (N ≥ 500) + protocolo C1-C5 (13 condiciones simultáneas), produciendo `metrics.json` reproducible con comando declarado.
2. **NO se construye dossier completo de catorce componentes** del §1: faltan típicamente predicción discriminante fechada con rival específico, intervención discriminante ejecutable empíricamente, traducción B↔L3 desarrollada por extenso, operador ε con protocolo de reapertura caso-específico, y/o comparación rival con tabla de discriminación caso-por-caso.

### 3.bis.2. Justificación

El corpus de 30 casos inter-dominio + 10 inter-escala opera en este modo por diseño metodológico: la pregunta que el corpus responde no es ontológica fuerte («este atractor existe en sentido pleno bajo dossier de catorce componentes»), sino **operativa de cobertura del aparato** («el aparato EDI discrimina señal acoplada de baseline desacoplado bajo permutación y gate C1-C5 en este dominio/escala, con tasa de falsos positivos acotada por hostile testing»). La discriminación es protocolar (permutación + gate + Wilson CI), no dossier ontológico fuerte. Construir dossier de catorce componentes para los 40 casos excedería el alcance de la tesis y, por la genealogía declarada en el §1 nota inicial, repetiría el problema de ad hoc rescue tipo 3 al escalar.

### 3.bis.3. Relación con los otros modos

| Modo | Aparato EDI ejecutado | Dossier 14 componentes | Pretensión filosófica | Casos |
|---|---|---|---|---|
| Demostrativo | Sí | Completo y sustantivo | Ontológica fuerte: el atractor es patrón material realmente existente bajo dossier auditado | 1 (Warren, cap 05-05) |
| Programático | No (o piloto parcial) | Conjeturado con criterio de elevación | Conjetura articulada con plan de prueba; no demuestra | 4 (caps 05-01 a 05-04) |
| **Técnico-ejecutado** | **Sí, completo y reproducible** | **No (mapeo de cobertura, no dossier ontológico)** | **Operativa: el aparato discrimina y mapea cobertura del marco a esta escala/dominio** | **40 (corpus 05-06 + 05-07)** |

El modo técnico-ejecutado **coincide con la reformulación opción (c) suave** del cierre `06-01` y la nota epistemológica BORRADOR-IA de `06-02 §3 P7-bis`: los 40 casos son **mapa de cobertura del aparato y calibración bidireccional**, no demostración ontológica adicional. La afirmación «ontología general multiescalar» se sostiene operativamente sobre los casos con datos públicos reales (subconjunto B-T2 + Warren); los demás técnicos-ejecutados son evidencia de transferibilidad estructural del aparato sin reentrenar arquitectura, con falsos positivos acotados por hostile testing (Wilson 95 % CI [0, 0.00191] sobre 0/2000 random walk).

### 3.bis.4. Marca obligatoria

Un capítulo o caso en modo técnico-ejecutado debe declararlo explícitamente y referenciar su `metrics.json` reproducible. La marca distingue cobertura operativa del aparato (admisible) de dossier ontológico completo (no reclamado).

## 4. Inventario de aplicaciones del manuscrito

### 4.1. Caso ancla canónico (modo demostrativo)

**Tabla 5.0.1.**

| Capítulo | Tema | Estado |
|---|---|---|
| 05-05 | Behavioral dynamics: locomoción, obstáculos, frenado, raqueteo, equilibrio | DEMOSTRATIVO con dossier completo; el anclaje primario es Warren (2006, pp. 358–359), engaged textualmente en el párrafo siguiente, complementado con Fajen y Warren (2003), Yilmaz y Warren (1995), Foo et al. (2000) y Sternad et al. (2001) |

[BORRADOR-IA · requires: H-J*] El anclaje teórico del caso 05-05 es explícitamente Warren (2006), quien plantea que «the agent and its environment are treated as a pair of dynamical systems that are coupled mechanically and informationally. Their interactions give rise to the behavioral dynamics, a vector field with attractors that correspond to stable task solutions, repellers that correspond to avoided states, and bifurcations that correspond to behavioral transitions» (Warren, 2006, p. 358). Esta tesis hace al programa de Warren un caso ancla natural para la ontología material-relacional: los atractores no se postulan como entidades internas al agente ni como propiedades del entorno aislado, sino que «are codetermined by the confluence of task constraints and perceptual–motor control laws» (p. 359). El capítulo 05-05 hereda esa carga discriminante —no la presupone—.

### 4.2. Aplicaciones en modo programático

**Tabla 5.0.2.**

| Capítulo | Tema | Estado | Criterio de elevación |
|---|---|---|---|
| 05-01 | Mente, memoria, yo | PROGRAMÁTICO | Tareas cognitivas con datos cuantitativos donde atractores conductuales discriminen contra cognitivismo simbólico |
| 05-02 | Biología y ecología | PROGRAMÁTICO | Atractores de regulación con bifurcaciones empíricas en datos publicados; rival principal: reduccionismo molecular o holismo ecológico inflado |
| 05-03 | Sistemas técnicos distribuidos | PROGRAMÁTICO | Modelo dinámico cuantitativo de sistema distribuido con predicción de fallo verificable; rival: arquitectura sin dependencias dinámicas |
| 05-04 | Instituciones, mercado, Estado | PROGRAMÁTICO | Atractores institucionales con bifurcaciones en datos históricos; rival: individualismo metodológico o holismo trascendental |

### 4.3. Corpus técnico-ejecutado (modo técnico-ejecutado)

[BORRADOR-IA · requires: H-J* — integración 2026-05-17] El corpus EDI agregado opera en **modo técnico-ejecutado** según §3.bis. Se compone de los 30 casos inter-dominio (capítulo 05-07, mapa de aplicaciones-corpus) y 10 casos inter-escala (capítulo 05-06). Cada caso tiene `metrics.json` reproducible bajo el comando declarado en su `src/validate.py`. La cobertura, gates C1-C5 y reclasificaciones bidireccionales se reportan en los capítulos respectivos y en `09-simulaciones-edi/Evaluacion_Modelos_Dominio.md`. Esta capa no constituye dossier de catorce componentes y no se reclama como tal; constituye **mapeo de cobertura del aparato** según la definición del §3.bis.

## 5. Política de extensión

### 5.1. Cuándo agregar aplicaciones

Una aplicación nueva se agrega al manuscrito solo si pasa al menos a modo programático con criterios de los §1-2 de este capítulo. No se admiten capítulos `interesantes` sin estructura.

### 5.2. Cuándo elevar de programático a demostrativo

Una aplicación programática se eleva a demostrativa cuando se cumplen sus criterios de elevación específicos y se produce dossier completo. La elevación se documenta con fecha y se actualiza el inventario.

### 5.3. Cuándo retirar

Una aplicación se retira si:

- en modo demostrativo, el dossier falla en alguna prueba de validación y la falla no se subsana;
- en modo programático, el criterio de elevación se intentó y produjo evidencia contraria a la conjetura;
- el rival principal del dominio absorbe la propuesta sin diferencia discriminante.

El retiro se documenta como deuda explícita en el capítulo 06-01.

## 6. Criterios uniformes de evaluación por aplicación

Cada aplicación, sea demostrativa o programática, debe responder cinco preguntas en su capítulo:

1. **¿Qué pregunta Q se trata?** Formulación explícita.
2. **¿Qué patrón material-relacional se conjetura?** Atractor candidato.
3. **¿Qué rival se enfrenta?** Posición específica con criterios.
4. **¿Qué predicción discriminante se ofrece?** Para demostrativo: cumplida. Para programático: a buscar.
5. **¿Qué se gana respecto al lenguaje ordinario?** Para demostrativo: con datos. Para programático: con argumento.

Sin las cinco respuestas, el capítulo se reescribe.

## 7. Diferencia con presentaciones laxas

Muchas tesis filosóficas presentan aplicaciones como ilustraciones afines a la tesis general. La política de este manuscrito es más severa: una aplicación es prueba de que la tesis funciona donde dice funcionar, o conjetura articulada con plan de prueba. La distinción produce trabajo y reduce ambigüedad. Si parece exigente, es porque la objeción de sobreextensión generalista lo es.

## 8. Diálogo con interlocutores

### 8.1. Lakatos — núcleo duro y cinturón protector

Lakatos distingue núcleo duro de un programa de investigación (no falsable directamente) y cinturón protector (donde se acumulan o se pierden aplicaciones). El caso ancla canónico funciona como cinturón protector consolidado; los modos programáticos son cinturón protector en construcción. El núcleo duro es el aparato del capítulo 03 y la asimetría L1↔B↔L3↔S.

### 8.2. Bunge — relación filosofía-ciencia

Bunge insiste en que la filosofía científica debe diferenciar análisis conceptual de afirmación empírica. La distinción demostrativo/programático honra esa exigencia.

## 9. Cierre

Esta política de admisión es la respuesta operativa a la objeción de sobreextensión. La tesis admite que solo está demostrada en su caso ancla y que los demás dominios son conjeturas con plan. La diferencia entre conjetura articulada y conjetura imprecisa es la articulación de los criterios de elevación. Cada capítulo programático lleva esa articulación; cada capítulo demostrativo lleva su dossier completo.
