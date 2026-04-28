# Temporalidad y causalidad — fundamentos generales

## Función de este capítulo

Este capítulo articula explícitamente lo que la tesis presupone sobre **tiempo** y **causalidad**, dimensiones ontológicas fundamentales que ningún capítulo anterior trató sistemáticamente. Su existencia responde a los vacíos V5-02 (temporalidad ausente), V5-03 (causalidad sin teoría) y V5-09 (downward causation sin tratamiento de Kim) identificados en la auditoría V5.

Una ontología que se afirma **general multiescalar** debe tener postura explícita sobre tiempo y causalidad, porque ambas son dimensiones ontológicas que atraviesan toda escala (no son propiedades regionales). La omisión de estos temas en la primera iteración del manuscrito era laguna estructural.

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

Kim (1998, *Mind in a Physical World*, cap. 4, p. 84) presenta el **argumento de exclusión causal**: si el nivel macro M causa Y y los componentes micro P causan Y, entonces M es causalmente sobredeterminante o epifenoménico; ambas opciones rechazables, luego M no causa Y.

**Respuesta de la tesis (V5-09):**

La tesis NO afirma downward causation en el sentido fuerte que Kim ataca. La tesis afirma **constitución descendente** (downward constitution), que es relación distinta:

- **causación**: X causa Y si una intervención sobre X cambia Y (Woodward);
- **constitución**: X constituye Y si X es parte de la realización material de Y;
- la **constricción macro→micro** del aparato EDI es **constitutiva, no causal**: el atractor macroscópico **constituye las restricciones** dentro de las cuales los componentes operan, sin causar nuevos eventos por encima de sus partes.

Esto se alinea con Craver (2007, *Explaining the Brain*, cap. 4, p. 152) que define *mutual manipulability* como criterio constitutivo, no causal: X es constitutivamente relevante para S si manipular X cambia S y manipular S cambia X. La tesis adopta esta noción para operacionalizar la constitución.

**Implicación:** la cláusula "downward causation material" del cap 02-04 §4 se refina como **"constitución descendente material"**: el atractor del sistema acoplado constituye las restricciones del componente sin violar exclusión causal. El argumento de Kim no aplica.

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

## 4. Lectura cruzada

- ontología que estas dimensiones presuponen: cap 02-01;
- aparato formal que opera intervenciones causales: cap 03-01;
- procedimiento empírico de κ (que presupone temporalidad): cap 03-04;
- self-organization (que presupone constitución descendente): cap 02-04 §4;
- limitaciones reconocidas: cap 04-02.

## 5. Cierre

> El tiempo es real-relacional, la flecha es termodinámica, la causalidad es manipulabilidad woodwardiana, la circularidad es retroacción dinámica con grafos cíclicos, y lo que parecía downward causation es constitución descendente compatible con exclusión causal. Estas posturas no son originales — son adopciones explícitas de la literatura — pero hacían falta articuladas para que la ontología material-relacional general no quedara con dos huecos centrales sin cerrar.
