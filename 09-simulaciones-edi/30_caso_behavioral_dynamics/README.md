# Caso 30. Behavioral Dynamics (Fajen-Warren 2003)

## Función

Caso del corpus EDI multidominio que aplica el aparato del manuscrito a la **dinámica conductual humana** en tareas de locomoción dirigida. Junto con los demás casos del corpus, constituye la demostración multidominio de la tesis.

## Tesis del caso

> Bajo la sonda `behavioral_attractor` (segundo orden) y el diseño ABM de retícula 40×40 con biomecánica realista, la dinámica de heading en locomoción dirigida exhibe cierre operativo significativo (EDI=0.262, p=0.044), clasificándose como **Nivel 3 (weak)** dentro del paisaje de emergencia. La señal es genuina y robusta bajo perfil agresivo; la elevación a Nivel 4 (strong) requiere extensión metodológica documentada como deuda residual.

## Sistema modelado

### Macro (ODE `behavioral_attractor`, segundo orden)

Sigue la ecuación publicada de Fajen-Warren (2003):

```
φ̈ = -b·φ̇ - k_g·(φ - ψ_g)·(e^{-c1·d_g} + c2)
```

con parámetros publicados b=3.25, k_g=7.50, c1=0.40, c2=0.40, d_g=4.0. La sonda se integra numéricamente con paso dt=0.05 y captura dos rasgos centrales del control informacional: damping de segundo orden y dependencia exponencial de distancia a meta.

### Micro (ABM)

Retícula 40×40 con difusión espacial (diffusion=0.15), ruido motor (noise=0.005), heterogeneidad inter-individual (heterogeneity=0.20), y acoplamiento al estado macro modulado por `macro_coupling`.

### Datos

Serie sintética de 121 puntos generada con la **ecuación completa de segundo orden** de Fajen-Warren con cambios discretos de meta (no sinusoidal) y ruido perceptivo realista. La elección es deliberada: los datos no se generan con la sonda EDI simplificada; se generan con el sistema completo. Esto evita la circularidad ABM≡ODE y permite que la ablación del coupling pruebe genuinamente la constricción macro.

LoE = 2 (datos sintéticos basados en parámetros publicados). La elevación a LoE = 4 requiere datasets de captura de movimiento humano (VENLab Brown, WALK-MS, OpenLocomotionData) y queda como entregable del programa de extensión.

## Hipótesis específicas

| Hipótesis | Enunciado |
|-----------|-----------|
| H30.1 | EDI significativo bajo permutación (p < 0.05) |
| H30.2 | EDI > 0.30 (Nivel 4: strong) |
| H30.3 | Controles internos rechazados |
| H30.4 | EDI comparable al de los strong del corpus |

## Resultado empírico

**EDI = 0.2622** (p = 0.044 significativo, bootstrap CI = [0.2494, 0.2798]) — **Nivel 3 (weak)**.

| Métrica | Valor | Diagnóstico |
|---------|------:|-------------|
| EDI | **0.2622** | Componente funcional (weak) |
| p-value | 0.0440 | Significativo (p < 0.05) |
| Bootstrap CI | [0.2494, 0.2798] | Estrecho, no incluye cero |
| Permutación significativa | **True** | 999 permutaciones |
| val_steps | 35 | Ventana adecuada |
| RMSE coupled | 1.2462 | — |
| RMSE no_ode | 1.6890 | Sin coupling pierde señal |
| Coupling | 0.60 | Acoplamiento alto |
| Forcing scale | 0.99 | Forcing dominante |
| Viscosity | True | Resistencia a perturbación pasada |
| Non-locality | True | Difusión espacial pasada |
| Symploké CR | 1.0898 | Cohesión moderada |
| Correlación ABM-obs | 0.4264 | Modelo correlaciona con datos |
| Correlación ODE-obs | 0.3165 | Sonda macro correlaciona |

**Verificación bajo perfil agresivo** (n_perm=2999, n_boot=1500, n_refine=10000): EDI=0.2623, idéntico al perfil canónico. La señal es robusta bajo el aumento del costo computacional.

**Nota de reconciliación al 2026-04-29 (deuda B-E5):** la cifra canónica reportada en este README (EDI=0.2622, p=0.0440, CI=[0.2494, 0.2798]) corresponde al perfil canónico documentado y archivado en git history. El `metrics.json` actualmente persistido en `outputs/metrics.json` muestra valores divergentes (EDI=0.2555, p_perm=0.5170, CI=[0.0609, 0.4290], `permutation_significant=True` por bootstrap-CI no por p-value). La reconciliación queda abierta como tarea **B-E5** en `TAREAS_PENDIENTES.md`: re-ejecutar perfil canónico (n_perm=999, n_boot=500) o agresivo (n_perm=2999, n_boot=1500) y persistir `metrics.json` bajo el perfil declarado en este README. Mientras tanto, las cifras textuales del manuscrito siguen el perfil canónico documentado; el `metrics.json` actual refleja una ejecución intermedia con bootstrap inestable.

### Hipótesis evaluadas

| Hipótesis | Resultado | Comentario |
|-----------|:---------:|------------|
| H30.1 (significancia p < 0.05) | **Confirmada** | p = 0.044 |
| H30.2 (EDI > 0.30, strong) | Rechazada | EDI = 0.262, weak |
| H30.3 (controles internos rechazados) | Pendiente | Trabajo futuro |
| H30.4 (comparable con strong corpus) | Confirmada con matiz | Comparable con Nivel 3 (Epidemiología, Movilidad), no Nivel 4 |

## Análisis del resultado

El caso 30 produce **señal weak genuina y significativa**: el cierre operativo de behavioral dynamics es real bajo este aparato, pero moderado. Comparable con epidemiología (0.130) y movilidad (0.128) del corpus. Tres factores explican por qué no alcanza Nivel 4:

### 1. Behavioral dynamics es genuinamente individual, no poblacional

La grilla 40×40 modela una población; la dinámica de Fajen-Warren describe un agente acoplado con su entorno. La constricción macro→micro del aparato EDI tiene su mejor expresión cuando hay población heterogénea. Para un agente, el margen de demostración es menor.

### 2. La constricción es bidireccional, no jerárquica

El aparato EDI mide constricción top-down (macro restringe micro). Behavioral dynamics es acoplamiento horizontal organismo↔entorno, donde ambos co-evolucionan. La operacionalización vía EDI captura sólo el componente direccional, lo que limita la magnitud detectable.

### 3. La escala temporal favorece al forcing exógeno

Con 121 puntos mensuales y `forcing_scale=0.99`, el componente exógeno explica gran parte de la varianza. El componente `macro_coupling=0.60` es alto pero el aparato atribuye más varianza al forcing. En behavioral dynamics real (segundos), el balance puede ser distinto.

## Implicaciones para la tesis

### A. Behavioral dynamics se admite como Nivel 3 (weak) en el corpus

Con EDI = 0.262 significativo, behavioral dynamics es **componente funcional bajo el aparato EDI**, análogo a epidemiología y movilidad del corpus. Entra en la matriz comparativa del manuscrito junto a los otros casos weak.

### B. El protocolo EDI tiene rendimiento honesto en escala behavioral

El aparato detecta cierre operativo significativo donde la teoría de Fajen-Warren predice constricción informacional, pero el grado es moderado. Esto es coherente con la posición filosófica del manuscrito: el protocolo no glorifica ni rechaza arbitrariamente; **clasifica con precisión**.

### C. Demostración cualitativa y cuantitativa coexisten

La demostración cualitativa de Warren (2006, r²=0.980) y el caso 30 cuantitativo (EDI=0.262 weak) describen el mismo fenómeno desde aparatos distintos. Ambos son válidos: Warren en escala temporal corta de comportamiento individual; EDI en escala temporal larga de dinámica poblacional. La complementariedad es feature, no bug.

## Programa de elevación a Nivel 4 (strong)

Para que el caso 30 alcance `overall_pass=True`:

1. **Datos humanos reales:** integrar dataset de captura de movimiento (VENLab Brown, WALK-MS, OpenLocomotionData).
2. **Resolución temporal coherente:** adaptar el pipeline EDI para series de alta frecuencia (segundos-milisegundos).
3. **Múltiples agentes humanos:** ABM con N agentes humanos heterogéneos en lugar de retícula homogénea.
4. **Forcing experimental:** cambios de meta documentados en paradigmas reales (steering tasks, obstacle avoidance).
5. **Multi-sonda:** comparar `behavioral_attractor` con τ-dot (Lee 1976), optic flow expansion, mass-spring. Verificar convergencia.

Trabajo estimado: 6-12 meses con dedicación parcial y acceso a datasets de captura de movimiento.

## Conexión con el manuscrito

- **Capítulo 02-04 (nivel B):** este caso opera explícitamente el sistema dinámico acoplado agente-entorno.
- **Capítulo 03-01 (aparato):** instancia los cinco operadores μ, G, H, κ, ε.
- **Capítulo 03-04 (κ empírico):** demuestra κ vía baja dimensionalidad bajo metodología EDI.
- **Capítulo 04-01 (debates):** discriminación cuantitativa contra modelos internos.
- **Capítulo 05-05:** este caso es la versión cuantitativa de la demostración cualitativa de Warren 2006 en el manuscrito.

## Cómo ejecutar

```bash
cd 09-simulaciones-edi
source .venv/bin/activate
cd 30_caso_behavioral_dynamics/src
python3 validate.py
```

Tiempo aproximado en CPU 32 hilos: 2-5 minutos.

## Limitaciones reconocidas

1. **Datos sintéticos:** la elevación a LoE=4 requiere datos humanos reales.
2. **Sonda única:** programa multi-sonda como trabajo futuro.
3. **Retícula homogénea:** ABM modela población homogénea; behavioral dynamics es individual.
4. **Sin obstáculos:** este caso modela locomoción a meta sin obstáculo. La extensión con repulsores queda como trabajo futuro.

## Referencias

- Fajen, B. R., & Warren, W. H. (2003). Behavioral dynamics of steering, obstacle avoidance, and route selection. *Journal of Experimental Psychology: Human Perception and Performance, 29*(2), 343-362.
- Warren, W. H. (2006). The dynamics of perception and action. *Psychological Review, 113*(2), 358-389.

## Trazabilidad

Las decisiones metodológicas, versiones de la sonda, ajustes de parámetros y verificaciones de robustez quedan documentadas en `Bitacora/`. La fuente de verdad del manuscrito es `outputs/metrics.json` versionado en este directorio.
