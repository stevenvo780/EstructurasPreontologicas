# Caso 30. Behavioral Dynamics, Fajen-Warren 2003

## Función

Caso piloto que aplica el EDI a una sonda inspirada en dinámica conductual. Evalúa los límites del aparato en escala conductual; no constituye demostración multidominio ni validación cuantitativa del caso experimental de Warren.

## Tesis del caso

> Bajo la sonda `behavioral_attractor` y datos sintéticos generados con una dinámica emparentada, el caso produce EDI = 0.2622 y `overall_pass=false`. La significancia iid p = 0.044 no sobrevive el control posterior con block bootstrap, p ≈ 0.978. El caso se conserva como piloto con circularidad parcial.

## Sistema modelado

### Macro

La sonda sigue una ecuación de segundo orden inspirada en Fajen y Warren (2003):

```text
φ̈ = -b·φ̇ - k_g·(φ - ψ_g)·(e^{-c1·d_g} + c2)
```

Usa b=3.25, k_g=7.50, c1=0.40, c2=0.40 y d_g=4.0.

### Micro

Retícula 40×40 con difusión espacial, ruido motor, heterogeneidad y acoplamiento al estado macro. Esta retícula representa una población simulada; no es equivalente a un participante humano en una tarea de locomoción.

### Datos

Serie sintética de 121 puntos generada con una ecuación de segundo orden de la misma familia teórica que la sonda. Aunque generador y sonda no son idénticos, comparten estructura suficiente para producir riesgo de circularidad. LoE = 2. La elevación requiere datos humanos reales.

## Hipótesis

| Hipótesis | Enunciado | Resultado vigente |
|---|---|---|
| H30.1 | Significancia robusta | Rechazada bajo block bootstrap, p≈0.978 |
| H30.2 | EDI > 0.30 y gate completo | Rechazada: EDI 0.2622, `overall_pass=false` |
| H30.3 | Controles internos suficientes | Pendiente |
| H30.4 | Convergencia con sonda distinta | Rechazada o no resuelta; τ-dot produjo failure mode |

## Resultado

| Métrica | Valor | Lectura |
|---|---:|---|
| EDI | 0.2622 | Magnitud Weak bajo taxonomía cruda |
| p iid | 0.0440 | Marginal; no calibrado para autocorrelación |
| CI bootstrap iid | [0.2494, 0.2798] | No incorpora adecuadamente dependencia temporal |
| p block bootstrap posterior | ≈0.978 | No significativo |
| `overall_pass` | false | Gate no superado |
| val_steps | 35 | Ventana técnica suficiente, no confirmatoria |
| LoE | 2 | Datos sintéticos |

La reejecución canónica reproduce EDI = 0.2622. La estabilidad numérica frente a la semilla o al número de permutaciones no elimina el problema de identificación: si la familia del generador favorece la familia de la sonda, el resultado puede ser estable y circular a la vez.

## Interpretación

El caso no permite afirmar que el cierre conductual sea real bajo el EDI. Permite identificar tres límites:

1. la significancia iid no es adecuada para la dependencia temporal presente;
2. el generador y la sonda no son teóricamente independientes;
3. una retícula poblacional no reproduce sin más la dinámica de un agente situado.

El ajuste r² = 0.980 reportado en el trabajo experimental de Warren pertenece a otro diseño, otros datos y otro criterio. Funciona como anclaje conceptual de la behavioral dynamics, no como validación del EDI de este caso.

## Programa de elevación

Para elevar el caso se requiere:

1. datos humanos abiertos o adquiridos bajo protocolo ético;
2. pre-registro anterior a la selección de sonda y ventana;
3. block-permutation desde el inicio;
4. al menos una sonda alternativa estructuralmente distinta;
5. baseline con presupuesto de ajuste equivalente;
6. predicción confirmatoria sobre intervención no usada en calibración;
7. replicación independiente.

Hasta entonces, el caso debe presentarse como piloto metodológico y resultado adverso para la pretensión de generalidad conductual.

## Cómo ejecutar

```bash
python3 09-simulaciones-edi/30_caso_behavioral_dynamics/src/validate.py --seed 42
```

## Conexión con el manuscrito

- capítulo 02-04: traducción entre niveles;
- capítulo 03-04: definición de κ y EDI;
- capítulo 05-05: Warren como caso ancla conceptual independiente;
- capítulo 05-07: mapa reconciliado del corpus;
- capítulo 06-01: límite inferencial y condiciones de elevación.

## Referencias

- Fajen, B. R., y Warren, W. H. (2003). Behavioral dynamics of steering, obstacle avoidance, and route selection. *Journal of Experimental Psychology: Human Perception and Performance*, 29(2), 343-362.
- Warren, W. H. (2006). The dynamics of perception and action. *Psychological Review*, 113(2), 358-389.

## Trazabilidad

La fuente numérica es `outputs/metrics.json`. La interpretación vigente incorpora la auditoría posterior de circularidad y debe prevalecer sobre narrativas históricas que lo llamaban Strong, Weak genuino o demostración conductual.
