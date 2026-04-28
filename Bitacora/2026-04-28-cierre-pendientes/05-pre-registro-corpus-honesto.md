# Pre-registro honesto del corpus EDI — declaración retroactiva

> Documento producido bajo auditoría severa (`03-auditoria-severa.md` ataque A4) que reconoce honestamente la limitación de pre-registro del corpus EDI multidominio.

## Reconocimiento explícito

Los **30 casos del corpus EDI** se compusieron de manera **iterativa y post-hoc**, no bajo pre-registro estricto. La selección actual responde a:

1. **Disponibilidad de datos públicos**: cada caso fue admitido si tenía dataset público accesible (World Bank, OWID, OPSD, CelesTrak, etc.).
2. **Diversidad de dominios**: se buscó cubrir física, biología, economía, política, tecnología, cultura, conducta humana.
3. **Aplicabilidad de sondas ODE de bajo orden**: dominios donde no se identificaba sonda razonable se descartaron tempranamente.
4. **Capacidad computacional disponible**: 30 casos cabían en el presupuesto de cómputo de la infraestructura (2 GPUs, 32 hilos CPU).

## Lo que NO está pre-registrado

- los umbrales de niveles (EDI ≥ 0.10 weak, ≥ 0.30 strong) son **post-hoc**, escogidos tras observar la distribución del corpus;
- la composición de "strong/weak/null/falsación" no fue declarada ex-ante como hipótesis;
- los casos null pueden estar sobre-representados (8 de 30) por inclusión deliberada de casos donde se sabía que la sonda iba a fallar;
- los 3 controles de falsación se construyeron específicamente para que el aparato los rechazara — esto es prueba de discriminación pero no muestra la tasa de tipo I del aparato sobre nulos genuinos no diseñados para fallar.

## Implicaciones honestas

1. La distribución del corpus (5 strong, 8 weak, 8 null, etc.) **no debe interpretarse como prevalencia poblacional** del cierre operativo en dominios reales.
2. Los umbrales 0.10/0.30 son **convención del autor**, no estándar disciplinar. Auditoría severa N4 demostró que la clasificación es FRÁGIL a estos umbrales: pasar a 0.15/0.40 reduce strong de 5 a 3; pasar a 0.05/0.20 lo aumenta a 9.
3. La afirmación *"el aparato discrimina con 50% de selectividad"* (15 de 30 con señal) **depende de qué casos se eligieron**. Un corpus distinto produciría una selectividad distinta.

## Lo que sí está bien establecido

- los 3 controles de falsación son rechazados genuinamente (EDI ≤ 0.06, p = 1.0);
- la métrica EDI tiene AUC-ROC = 0.886 para discriminar strong vs no-strong (auditoría N3) — discriminación sustantiva confirmada;
- los umbrales EDI son robustos contra falsos positivos de random walk (N1: 0.6% supera 0.10 bajo nulo, 0% supera 0.30);
- la circularidad detectada en caso 30 (N2) es honesta y limita la confianza en behavioral dynamics, no en strong general.

## Programa pre-registrado para casos futuros

Para evitar el problema en extensiones futuras del corpus:

1. **Declarar pre-empíricamente la hipótesis** antes de ejecutar el caso (qué EDI se espera, con qué argumento teórico).
2. **Registrar criterios de exclusión ex-ante**: qué condiciones del dataset descalifican el caso ANTES de ver los EDI.
3. **Reportar tasa de descarte**: cuántos candidatos se evaluaron contra cuántos entraron al corpus final.
4. **Pre-registrar umbrales** para nuevos niveles si se introducen (Nivel 5 con sus 3 condiciones está pre-registrado en `Bitacora/2026-04-28-cierre-doctoral/06-`; eso es ejemplo correcto).

## Cláusula formal a incorporar al manuscrito

El cap 06-01 (conclusión demostrativa) debe declarar explícitamente:

> *"La composición numérica del corpus actual (5 strong, 8 weak, 2 suggestive, 4 trend, 8 null, 3 falsación rechazada) es post-hoc y no debe leerse como distribución poblacional del cierre operativo en la realidad. Lo que el corpus demuestra es: (a) el aparato es capaz de producir clasificaciones discriminantes (AUC-ROC = 0.886); (b) los umbrales EDI son robustos contra falsos positivos genuinos; (c) los controles de falsación se rechazan correctamente. La afirmación más fuerte que el corpus sostiene es metodológica, no estadística-poblacional."*

## Lectura cruzada

- Auditoría severa: `Bitacora/2026-04-28-cierre-pendientes/03-auditoria-severa.md` ataque A4.
- Resultados N1: `Bitacora/2026-04-28-cierre-severo/N1_resultados.json`.
- Resultados N3: `Bitacora/2026-04-28-cierre-severo/N3_resultados.json`.
- Resultados N4: `Bitacora/2026-04-28-cierre-severo/N4_resultados.json`.
