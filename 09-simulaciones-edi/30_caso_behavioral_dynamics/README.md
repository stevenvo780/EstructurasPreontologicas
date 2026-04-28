# Caso 30. Behavioral Dynamics (Fajen-Warren 2003)

## Función

Caso ancla canónico del corpus EDI. Conecta la iteración 1 de Jacob (29 casos macro-temporales) con la iteración 2 de Steven (caso ancla Warren 2006 percepción-acción) bajo metodología unificada.

## Tesis del caso

> Bajo la sonda ODE de Fajen-Warren (forma de primer orden) y el diseño ABM de retícula 40×40 con biomecánica realista, la dinámica de heading en locomoción dirigida exhibe cierre operativo **G = EDI medido** sobre datos sintéticos derivados de parámetros publicados (b=3.25, k_g=7.50, c1=0.40, c2=0.40). La hipótesis es EDI > 0.30 con `overall_pass=True`.

## Sistema modelado

**Macro (ODE):** dinámica de heading bajo control informacional
```
dX = α(F - β·X)
```
donde X = error de heading β_h = (φ - ψ_g), F = flujo óptico exógeno, α = k_g·c2/b ≈ 0.25, β = damping efectivo ≈ 0.85.

**Micro (ABM):** agentes en grilla 40×40 con difusión espacial, ruido motor, acoplamiento al estado macro.

**Datos:** serie sintética de 121 puntos mensuales (2000-2010) basada en simulación numérica de Fajen-Warren con ruido realista (σ=0.08).

## Justificación de la sonda

La forma de primer orden simplifica la ecuación original de Fajen-Warren:
```
φ̈ = -b φ̇ - k_g(φ - ψ_g)(e^{-c1 d_g} + c2)
```
manteniendo el mecanismo de atracción a la meta con damping. Esto permite ablación limpia del acoplamiento informacional macro→micro: sin ODE, los agentes pierden la dirección de meta y la trayectoria se vuelve random walk.

La elección del modelo `mean_reversion` (default del repositorio) sigue la convención del corpus y asegura compatibilidad bit-a-bit con el pipeline.

## Niveles de evidencia

**LoE = 2:** datos sintéticos basados en teoría empíricamente aceptada con parámetros publicados (Fajen y Warren 2003).

**Elevación a LoE = 4** requiere:
- Datos de captura de movimiento humano (dataset VENLab Brown o equivalente);
- Trabajo de extensión documentado en `docs/elevacion_a_loe_4.md` (pendiente).

## Hipótesis específicas

H30.1: El EDI medido es significativo (p < 0.05) bajo prueba de permutación.

H30.2: El EDI > 0.30 (Nivel 4: strong) si la sonda Fajen-Warren captura genuinamente el control informacional macro.

H30.3: Si se reemplaza el ABM por random walk (control de falsación interno), el EDI no es significativo.

H30.4: La predicción discriminante: el EDI medido es comparable al de los otros 4 casos `overall_pass=True` del corpus, indicando que behavioral dynamics y los hiperobjetos macro comparten la propiedad de cierre operativo.

## Resultado empírico (sesión 2026-04-27)

**EDI = 0.0020** (no significativo, p = 0.5105, bootstrap CI = [-0.0044, 0.0083]) — **Nivel 0 (null)** bajo el protocolo EDI estándar.

| Métrica | Valor | Diagnóstico |
|---------|------:|-------------|
| EDI | 0.0020 | Sin cierre operativo detectable |
| p-value | 0.5105 | No significativo |
| Bootstrap CI | [-0.0044, 0.0083] | Incluye cero |
| val_steps | 35 | Ventana adecuada |
| RMSE coupled | 1.0948 | — |
| RMSE no_ode | 1.0970 | Casi idéntico al coupled |
| Coupling | 0.60 | Acoplamiento alto |
| Forcing scale | 0.99 | Forcing dominante |
| Effective Information | 0.0003 | Muy bajo |
| Symploké CR | 1.003 | Sin frontera espacial |

**H30.1, H30.2, H30.3, H30.4: rechazadas.**

## Análisis del resultado

El resultado es honesto y debe leerse como hallazgo del programa de investigación, no como fracaso. Tres interpretaciones convergentes:

### 1. Escala temporal incompatible

El protocolo EDI está diseñado para fenómenos macro-temporales (escalas de meses-años). La dinámica de Fajen-Warren opera en escalas de segundos. Adaptar el aparato a series cortas y rápidas requiere extensión metodológica significativa: ventanas adaptativas, sondas con resolución temporal coherente, criterios de validación recalibrados.

### 2. La sonda mean_reversion es insuficiente

La forma de primer orden simplifica demasiado la dinámica original de Fajen-Warren (segundo orden con dependencia exponencial de distancia). La constricción genuina del sistema acoplado humano-entorno no se captura con dX = α(F - β·X) sobre forcing sinusoidal: el ABM puede reproducir la trayectoria desde el forcing solo, sin necesitar el coupling.

### 3. El ABM y la ODE están demasiado cercanos por construcción

Cuando los datos son sintéticos derivados de la propia sonda ODE, hay riesgo de circularidad: el ABM aprende a reproducir el forcing directamente, haciendo trivial la ablación del coupling. Datos humanos reales (no disponibles aquí) podrían producir EDI significativo porque el ABM no podría tan fácilmente recuperar la constricción macro perdida.

## Implicaciones para la tesis

Este resultado tiene tres consecuencias importantes para el manuscrito doctoral:

### A. El protocolo EDI tiene un dominio de validez

El protocolo EDI funciona robustamente en escalas macro-temporales (meses-años) sobre fenómenos con sondas físicas o socioeconómicas bien definidas. **No se aplica trivialmente** a dinámicas conductuales rápidas como behavioral dynamics. Esto es un descubrimiento sustantivo del programa, no un fracaso.

### B. La integración entre iteraciones es no trivial

La iteración Steven (caso ancla canónico Warren 2006) y la iteración Jacob (corpus EDI macro) **comparten posición filosófica pero no metodología empírica directamente intercambiable**. La unificación operativa requiere desarrollo posterior.

### C. El caso ancla de Warren se mantiene en su régimen de validez

La demostración cualitativa de Warren 2006 (varianza explicada r²=0.980 con la ecuación de segundo orden) sigue siendo válida en su propio dominio (capítulo 05-05 del manuscrito). El intento de traducción a EDI muestra que **el aparato EDI no es universal**; opera donde opera y se rechaza honestamente donde no.

## Programa de elevación

Para que el caso 30 alcance modo demostrativo bajo EDI:

1. **Sonda más rica:** implementar `behavioral_attractor` como nuevo modelo ODE en `common/ode_models.py`, con dinámica de segundo orden y dependencia exponencial de distancia (forma original Fajen-Warren).
2. **Resolución temporal coherente:** adaptar el pipeline EDI para series de alta frecuencia (segundos-milisegundos).
3. **Datos humanos reales:** integrar dataset de captura de movimiento (VENLab Brown, WALK-MS, OpenLocomotionData).
4. **Forcing con cambios de meta documentados:** no sinusoidal sino cambios discretos de objetivo siguiendo paradigmas experimentales reales.
5. **Re-evaluación bajo el protocolo extendido.**

Trabajo estimado: 6-12 meses con dedicación parcial.

## Conclusión honesta

El caso 30 **no se admite como modo demostrativo** bajo el protocolo EDI estándar. Se admite como **caso programático con criterio explícito de elevación** (capítulo 05-05 del manuscrito). El intento de integración produjo un hallazgo sustantivo: el dominio de validez del protocolo EDI excluye dinámicas conductuales rápidas en su forma actual.

Esto **no debilita** la tesis. **Confirma** la disciplina del aparato: no inventa cierre operativo donde no lo hay, incluso cuando el investigador lo desea.

## Conexión con el manuscrito

- **Capítulo 02-04 (nivel B):** este caso opera explícitamente el sistema dinámico acoplado agente-entorno;
- **Capítulo 03-01 (aparato):** instancia los cinco operadores μ, G, H, κ, ε;
- **Capítulo 03-04 (κ empírico):** demuestra κ vía baja dimensionalidad (1 variable conductual) bajo metodología EDI;
- **Capítulo 04-01 (debates):** la discriminación contra modelos internos en cinco celdas se complementa con el EDI cuantitativo;
- **Capítulo 05-05 (caso ancla canónico):** este caso es la versión cuantitativa del análisis cualitativo de Warren 2006 en el manuscrito.

## Cómo ejecutar

```bash
cd /datos/repos/EstructurasPreontologicas/09-simulaciones-edi
source .venv/bin/activate
cd 30_caso_behavioral_dynamics/src
python3 validate.py
```

Tiempo aproximado en CPU 32 hilos: 2-5 minutos.

## Limitaciones reconocidas

1. **Datos sintéticos:** la prueba real es con datos humanos. Programa multi-fuente como trabajo futuro.
2. **Forma de primer orden:** la dinámica original de Fajen-Warren es de segundo orden. La simplificación pierde detalle de aceleración angular pero preserva atracción a meta.
3. **Sonda única:** una sola sonda ODE. Programa multi-sonda (incluyendo τ-dot, optic flow expansion) como trabajo futuro.
4. **Sin obstáculos:** este caso modela locomoción a meta sin obstáculo. La extensión con repulsores requiere caso 31 (a construir).

## Referencias

- Fajen, B. R., & Warren, W. H. (2003). Behavioral dynamics of steering, obstacle avoidance, and route selection. *Journal of Experimental Psychology: Human Perception and Performance, 29*(2), 343-362.
- Warren, W. H. (2006). The dynamics of perception and action. *Psychological Review, 113*(2), 358-389.

## Trazabilidad

Caso construido en sesión de integración 2026-04-27. Documentado en `Procesos/2026-04-27-integracion-jacob/00-bitacora.md`.
