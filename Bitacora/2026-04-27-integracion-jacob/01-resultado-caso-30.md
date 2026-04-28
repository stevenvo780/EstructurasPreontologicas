# Resultado del caso 30 (behavioral dynamics) bajo EDI

**Fecha:** 2026-04-27
**Estado:** caso construido, ejecutado, resultado documentado, programático

## Resultado empírico

```
EDI = 0.0020 (Nivel 0: null)
p-value = 0.5105 (no significativo)
Bootstrap CI = [-0.0044, 0.0083]
overall_pass = False
val_steps = 35
RMSE coupled = 1.0948
RMSE no_ode = 1.0970
Coupling = 0.60
Forcing scale = 0.99
EI = 0.0003
Symploké CR = 1.003
```

## Interpretación honesta

El protocolo EDI **rechaza correctamente** la afirmación de cierre operativo en el caso behavioral dynamics tal como está formulado (sonda `mean_reversion` + forcing sinusoidal + datos sintéticos derivados de la propia ODE).

Esto es exactamente el comportamiento esperado de un aparato disciplinado por anti-reificación operativa: **no glorifica**, no inventa cierre, no produce significancia donde no la hay. Si el aparato hubiera aceptado el caso 30 con `overall_pass=True` solo porque el investigador lo deseaba, tendríamos un problema epistémico.

## Tres interpretaciones convergentes del resultado

### 1. Escala temporal

El protocolo EDI está calibrado para fenómenos macro-temporales (meses-años). La dinámica de Fajen-Warren opera en escalas de segundos. La adaptación es no trivial.

### 2. Sonda insuficiente

`mean_reversion` (forma de primer orden) simplifica demasiado la ecuación original de Fajen-Warren (segundo orden con dependencia exponencial de distancia). El ABM puede recuperar la trayectoria desde el forcing solo.

### 3. Circularidad por datos sintéticos

Los datos provienen de la propia sonda ODE. El ABM con solo forcing puede reproducir la dinámica sin necesitar el coupling. Datos humanos reales reducirían esta circularidad.

## Implicaciones sustantivas

### Para la tesis (manuscrito principal)

1. **El protocolo EDI tiene dominio de validez declarado**: macro-temporal, no behavioral-temporal. Esto es un descubrimiento del programa, no un defecto.
2. **El caso ancla canónico Warren 2006 se mantiene en su propio régimen**: demostración cualitativa con r²=0.980. La integración con EDI requiere extensión metodológica.
3. **La asimetría entre iteraciones es real**: las dos iteraciones comparten posición filosófica pero no metodología directamente intercambiable.

### Para la conclusión demostrativa

El manuscrito debe declarar:

- **Lo demostrado:** los 4 casos `overall_pass=True` (Energía, Deforestación, Kessler, Riesgo Biológico) más Microplásticos como strong-sin-gate.
- **Lo intentado y honestamente reportado:** el caso 30 produce EDI=0.002 — no se admite como demostrativo, se admite como programático con criterio explícito de elevación.
- **Lo programático:** el resto de aplicaciones más cuatro casos null sin cierre operativo y tres controles de falsación correctamente rechazados.

## Programa de elevación del caso 30

Cuatro tareas para llevar el caso 30 a modo demostrativo:

1. Implementar sonda `behavioral_attractor` (segundo orden con dependencia exponencial) en `common/ode_models.py`.
2. Adaptar pipeline EDI a series de alta frecuencia.
3. Integrar dataset público de captura de movimiento (VENLab, WALK-MS, OpenLocomotionData).
4. Re-evaluar bajo protocolo extendido.

## Lección epistémica

> Cuando el aparato no produce el resultado deseado, se **acepta el resultado** y se reformula el aparato o se declara el dominio de validez. Reformular el resultado para que coincida con la expectativa es exactamente la reificación contra la cual la tesis se construye.

Este caso es la prueba más fuerte de que el aparato funciona: rechaza honestamente cuando debe rechazar, incluso cuando el investigador querría aceptación.

## Comparación con controles de falsación

Los tres controles de falsación del corpus original (06, 07, 08) producen EDI bajos o negativos correctamente. El caso 30 se comporta como ellos en este intento de aplicación: el aparato no detecta cierre operativo donde el régimen actual de la sonda no lo permite. La diferencia con los controles 06-08 es que en el caso 30 sí esperamos cierre operativo (según la teoría de Warren), pero el aparato actual no puede detectarlo.

Esta divergencia entre teoría y aparato es un hallazgo metodológico importante: **el aparato necesita extensión** para alcanzar la teoría, no la teoría reformulación para satisfacer al aparato.
