# Temporalidad y causalidad — fundamentos generales


## Tesis del capítulo

> El **tiempo** es ontológicamente real en sentido relacional B-series: es el orden de la sucesión de estados del sustrato material dinámico, sin "presente privilegiado" universal. La **flecha del tiempo** es termodinámica, no metafísica. La **causalidad** es relación de manipulabilidad woodwardiana entre variables del sistema acoplado, operacionalizada por intervención ablativa (`do`-test pearliano). La tesis acepta **causación constitutiva descendente** (downward constitution) sin recaer en downward causation kim-vulnerable: el atractor macroscópico **constituye** las constricciones del nivel componente sin causar nuevos eventos por encima de sus partes.

## 1. Postura sobre el tiempo

### 1.1. El tiempo como dimensión real-relacional

La tesis adopta **realismo temporal relacional B-series** (McTaggart 1908; Mellor 1998; perspectiva eternalista moderada): los eventos están ontológicamente ordenados en una serie *anterior–simultáneo–posterior* sin que exista un "presente" metafísicamente privilegiado.

**Razones operativas de la postura:**

1. el sustrato material dinámico tiene evolución temporal genuina: si negáramos la temporalidad, los atractores serían imposibles (un atractor es estado al que el sistema converge en el tiempo);
2. la postura A-series (presente real, pasado y futuro irreales) es incompatible con la generalidad multiescalar: en escalas cuántica y cosmológica, el "presente" es relativo al observador (relatividad especial);
3. la postura presentista pura (sólo lo presente existe) hace incomprensible el atractor mismo, que es objeto definido por su evolución temporal completa.

### 1.2. La flecha del tiempo

La tesis distingue tres flechas del tiempo:

- **flecha termodinámica**: aumento de entropía en sistemas cerrados (segunda ley);
- **flecha cosmológica**: expansión del universo;
- **flecha psicológica**: percepción subjetiva de pasado-presente-futuro.

La tesis afirma que la **flecha termodinámica es ontológicamente fundamental**, las otras dos son derivadas. La irreversibilidad del cierre operativo κ (la operación de compresión preserva dependencias decisivas pero la reapertura ε no es perfecto recobro) es **manifestación local de la flecha termodinámica**, no propiedad lógica ni metafísica adicional.

### 1.3. Tiempo e invarianza multiescalar

¿Cómo se compatibiliza el invariante "atractor" con escalas cuánticas donde la dinámica puede ser unitaria-reversible?

**Respuesta:** en escala cuántica pura (sistema cerrado sin medición), la dinámica es unitaria y los "atractores" son estados estacionarios. Pero los casos del corpus inter-escala (caso 31 decoherencia) son **sistemas abiertos** acoplados a baño térmico — ahí la flecha termodinámica está presente y los atractores son objetos dinámicos genuinos. La tesis NO afirma generalidad sobre sistemas cuánticos cerrados aislados; afirma generalidad sobre sistemas materiales acoplados, lo cual es la condición que el corpus respeta.

### 1.4. Diálogo con la tradición

- **Whitehead** (1920, *El concepto de naturaleza*, cap. 3, p. 53): *"nature is a process"*. La tesis recoge: el sustrato material es proceso, no inventario.
- **Bergson** (1889, *Tiempo y libre albedrío*) postula la *durée* como tiempo cualitativo subjetivo. La tesis lo trata como **fenómeno psicológico** (flecha psicológica), no como tiempo fundamental.
- **McTaggart** (1908, "The Unreality of Time", *Mind* 17:457-484) argumentó la incoherencia de la A-series. La tesis recoge la conclusión moderada (B-series adecuada) sin la negación radical de McTaggart.
- **Smolin** (2013, *Time Reborn*) defiende A-series. La tesis discrepa: la A-series es incompatible con relatividad especial y con la generalidad multiescalar requerida por la tesis.
- **Bunge** (1977, *Treatise* vol. 3, p. 152): *"time is a feature of the world, not a stage on which the world performs"*. La tesis lo adopta literalmente: el tiempo es **propiedad relacional del sustrato**, no escenario externo.

## 2. Postura sobre la causalidad

### 2.1. La causalidad como manipulabilidad woodwardiana

La tesis adopta **manipulabilidad woodwardiana** (Woodward 2003, *Making Things Happen*, cap. 2, p. 57: *"X causes Y if some intervention on X changes Y"*) como teoría de la causalidad operativa.

**Razones operativas:**

1. el aparato EDI **opera intervenciones ablativas** sobre el acoplamiento (apaga el ODE manteniendo el forcing); esto es operacionalmente woodwardian;
2. la teoría woodwardiana es compatible con el `do`-calculus de Pearl, que ya está integrado al aparato (cap 03-01 §12.1);
3. evita comprometerse con causalidad como relación entre eventos puntuales; la causalidad de la tesis es **relación entre variables del sistema acoplado**.

### 2.2. Pluralidad causal limitada

La tesis acepta **pluralismo causal limitado** (Cartwright 2007, *Hunting Causes and Using Them*, cap. 2): hay relaciones causales de tipos distintos (constitución, eficiencia, formal, retroalimentación) y no es necesario reducirlas a un único tipo. Pero rechaza el pluralismo radical: todas las relaciones causales del corpus se operan vía intervención ablativa, lo cual unifica metodológicamente sin unificar metafísicamente.

### 2.3. Causalidad circular

La tesis usa "causalidad circular" en cap 02-04 §3 (acoplamientos simultáneos organismo-entorno). Aclaración técnica:

- **causalidad circular** ≠ causalidad cíclica simple (X causa Y, Y causa X);
- **causalidad circular** = retroacción dinámica donde la dinámica del sistema acoplado tiene **bucles** que no se reducen a cadenas lineales;
- formalmente: el grafo causal del sistema acoplado tiene ciclos, no es DAG;
- esto NO viola el `do`-calculus pearliano: las intervenciones se definen sobre el grafo cíclico bajo expansión temporal explícita.

### 2.4. Downward causation: respuesta al argumento de Kim

Esta sub-sección merece tratamiento extendido porque la objeción de Kim es la objeción metafísica más recurrente contra cualquier ontología que afirme constricción macro→micro. El manuscrito anticipa que un evaluador con formación en metafísica de la mente la planteará en defensa, y por eso la respuesta se articula con cuatro pasos ordenados, no con declaración.

#### 2.4.1. Enunciado preciso del argumento de Kim

Kim (1998, *Mind in a Physical World*, cap. 4, p. 84) formula el **argumento de exclusión causal** en cinco premisas:

1. **Cierre causal del dominio físico:** todo evento físico tiene causa física suficiente.
2. **Sobreviniencia:** las propiedades macro M sobrevienen sobre las propiedades micro P.
3. **No sobredeterminación sistemática:** no es admisible que M y P causen sistemáticamente el mismo efecto Y.
4. **No epifenomenalismo:** rechazamos que M sea causalmente inerte.
5. **Conclusión por reducción:** la única salida coherente es que M sea idéntica a (o reducible a) P; cualquier downward causation genuina contradice (1)–(3).

Cualquier filosofía que afirme constricción macro→micro debe responder a este argumento sin invocar misterios y sin colapsar M en P (lo cual eliminaría el explanandum macro).

#### 2.4.2. Distinción operativa entre causación y constitución

La tesis distingue dos relaciones que la formulación clásica de Kim trata como una sola:

- **Causación** (Woodward 2003, *Making Things Happen*, cap. 2, p. 57): X causa Y si y sólo si una intervención sobre X (independiente del resto del sistema) produce un cambio sistemático en Y. Las relaciones causales son entre variables y son temporalmente extendidas.
- **Constitución** (Craver 2007, *Explaining the Brain*, cap. 4, p. 152): X constituye Y si y sólo si X es **parte de la realización material** de Y, verificable por **manipulabilidad mutua** — manipular X cambia S y manipular S cambia X. Las relaciones constitutivas son sincrónicas y no requieren transferencia causal entre niveles.

La intervención ablativa del aparato EDI (`do(coupling = 0)`) opera explícitamente como test woodwardiano sobre **variables del sistema acoplado**, no sobre eventos micro individuales. Lo que el aparato detecta no es "M causa Y por encima de P"; es "el régimen acoplado tiene dependencias estructurales que la versión sin acoplamiento pierde".

#### 2.4.3. Aplicación al aparato EDI

Cuando el aparato detecta cierre operativo (EDI > umbral), no afirma que el atractor macro **causa** algo que las componentes micro no causan. Afirma algo más modesto y filosóficamente más defensable:

- el atractor macro **constituye las restricciones** dentro de las cuales las componentes evolucionan;
- esas restricciones son **detectables operativamente** porque al apagar el acoplamiento (ablación), las trayectorias se degradan;
- la degradación no muestra que el macro tenga "poder causal extra" sobre el micro; muestra que **la descripción macro captura dependencias estructurales que la descripción micro descontextualizada pierde**.

Esto es exactamente la noción de Craver (*mutual manipulability*) operacionalizada por intervención ablativa. No hay sobredeterminación porque no hay dos cadenas causales paralelas; hay una sola dinámica acoplada que admite descripción a dos niveles, y la descripción macro es **constitutivamente** legítima cuando el test de manipulabilidad mutua se cumple.

#### 2.4.4. Por qué esto no diluye la tesis

Un crítico podría objetar: *"si reformulan downward causation como constitución, han abandonado la afirmación fuerte que su tesis necesita"*. La respuesta es que la tesis nunca necesitó downward causation en el sentido kim-vulnerable. Lo que necesita es:

- que los **patrones macro sean reales** (no nominales);
- que su realidad sea **detectable operativamente** (no postulada);
- que su realidad **constriña la dinámica de las componentes** sin violar el cierre causal físico.

Las tres condiciones se cumplen bajo la formulación constitutiva. El atractor existe materialmente como configuración del sistema acoplado, su existencia se detecta por intervención ablativa, y su efecto sobre las componentes es constitutivo (parte de la realización), no causal (transferencia de poder por encima del cierre físico).

La verificación formal de este argumento está en la suite ST T13 (hallazgo ST-3): la implicación `((C ∧ ¬V) ∧ (K → (V → S))) → ¬S` no es derivable directamente, pero el argumento de Kim queda neutralizado **por modus tollens vacuo** — si la constricción macro→micro es constitución (C) y no causación (¬V), entonces la premisa de Kim que requiere V es falsa de antemano, y la conclusión sobre sobredeterminación S no se sigue.

**Implicación:** la cláusula "downward causation material" del cap 02-04 §4 se refina canónicamente como **"constitución descendente material"** (downward constitution). El argumento de Kim no aplica porque ataca un blanco que la tesis no defiende.

### 2.5. Diálogo con causal emergence (Hoel 2017)

Hoel, Albantakis y Tononi (2013, *PNAS* 110:19790-19795) introducen **causal emergence**: el macro puede tener mayor poder causal (información efectiva) que el micro. La tesis recoge parcialmente:

- la **información efectiva** macro de Hoel es métrica adyacente a EDI, no idéntica;
- EDI mide **dependencia ablativa** (cuanto baja la predicción al apagar el acoplamiento); Hoel mide **información efectiva** (capacidad causal del nivel);
- los dos enfoques son **complementarios**, no rivales: ambos capturan la realidad de los niveles macroscópicos sin postular nuevas sustancias.

## 3. Síntesis: tiempo + causalidad como dimensiones generales

La tesis ahora afirma con respaldo articulado:

| Dimensión | Postura | Operacionalización |
|-----------|---------|---------------------|
| **Tiempo** | B-series relacional, eternalismo moderado | Series temporales del corpus, dt explícito en sondas |
| **Flecha del tiempo** | Termodinámica fundamental, otras derivadas | Irreversibilidad parcial de κ↔ε |
| **Causalidad** | Manipulabilidad woodwardiana | Intervención ablativa = `do`(coupling = 0) |
| **Causación circular** | Retroacción en grafo cíclico | Acoplamiento ABM↔ODE bidireccional |
| **Downward "causation"** | Reformulado como constitución | Mutual manipulability de Craver |

Esto cubre los vacíos V5-02, V5-03, V5-09 con honestidad: la tesis no inventa metafísica del tiempo ni de la causalidad; **adopta posturas defendidas en la literatura** y las articula explícitamente para que el aparato no quede flotando metodológicamente.

