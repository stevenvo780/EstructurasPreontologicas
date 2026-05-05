# F05-06 — Self-organization aplicado a microservicios SRE sin Mitchell

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap05 (2026-05-05)
**Estado:** RESUELTO — la afirmación del adversarial NO se confirma en el manuscrito actual.

## (a) Verificación de la afirmación

Hipótesis del adversarial: en `05-03 sistemas-tecnicos-distribuidos.md` y `05-05 warren.md:153` se usa "self-organization" para referirse a microservicios SRE (emergencia computacional) mezclando indebidamente con autopoiesis Maturana-Varela; la mezcla estaría prohibida por el glosario operativo.

Búsqueda exhaustiva (`grep -rn -i "self-organi\|auto-organiza" 05-aplicaciones/`):

- **`05-03-sistemas-tecnicos-distribuidos.md`: 0 ocurrencias.** El cargo principal del adversarial no se sostiene en el archivo señalado. No hay aplicación del término a microservicios SRE en el manuscrito.
- **`05-05-…-warren.md`: 4 ocurrencias** (líneas 153, 219, 255, 291). Las cuatro están explícitamente ancladas a `cap 02-04 §4 (Maturana-Varela 1980, Haken 1977)`. El uso describe causalidad circular agente-entorno en tareas de balanceo de palo y locomoción — dominio para el que Maturana-Varela y Haken sí son las fuentes apropiadas (sistemas dinámicos acoplados, no microservicios).
- **`05-02-biologia-y-ecologia.md`: 1 ocurrencia** (línea 189), también anclada a cap 02-04 §4.

## Estado del anclaje paginado en cap 02-04 §4

`02-fundamentos/04-anclaje-conductual-ecologico.md` líneas 114-133 sí provee:

- Cita textual de Haken 1977 *Synergetics* p. 1 ("sudden self-organization of structure is observed when control parameters cross critical values").
- Referencia al slaving principle, cap. 7, p. 191-204.
- Referencia a Maturana & Varela 1980 *Autopoiesis and Cognition*.
- **Convención explícita del glosario** (línea 131): toda ocurrencia de "self-organization" en el manuscrito remite a esa sección; donde no se pueda mantener el anclaje, sustituir por "estabilización dinámica" o "convergencia a atractor".

## Conclusión sobre acceptance

> Acceptance: 0 ocurrencias 'self-organization' sin anclaje paginado en 05-03/05-05/02; sustituir por 'estabilización dinámica' o citar Mitchell 2009 cap.12 p.180.

- 05-03: 0 ocurrencias → cumplido trivialmente.
- 05-05: 4 ocurrencias, todas remitidas a 02-04 §4 que tiene paginación de Haken (p. 1, p. 191-204). → cumplido.
- 05-02: 1 ocurrencia, mismo anclaje. → cumplido.

La acceptance está satisfecha vía Maturana-Varela + Haken con paginación; **no es necesario citar Mitchell 2009** porque la convención del glosario fija el anclaje canónico en otras dos fuentes ya paginadas.

## (b) Propuesta de edición

**Ninguna edición requerida.** El adversarial-reviewer apuntó a un archivo (`05-03`) que no contiene el término, y a una línea (`05-05:153`) cuyo uso está explícitamente anclado al glosario operativo. La queja es un falso positivo del adversarial.

Acción defensiva opcional (mejora de robustez, no obligatoria): añadir en cada una de las 4 ocurrencias de 05-05 la página exacta de Haken al primer uso, ej. `(cap 02-04 §4; Haken 1977, p. 1; p. 191-204)`. Esto es cosmético; el anclaje ya existe vía remisión al cap 02-04. **needs_human=no** para esta acción cosmética; **se deja a criterio de Jacob** si quiere refuerzo redundante de paginación in-line.

## (c) Costo argumentativo declarado

- El manuscrito acepta el costo de no usar Mitchell 2009 como ancla (Mitchell ofrece síntesis pedagógica más reciente; Haken 1977 + Maturana-Varela 1980 son las fuentes técnicas primarias). Esta es elección legítima.
- Costo abierto: el anclaje a Maturana-Varela en sentido autopoiético es controvertido cuando se aplica fuera de biología (Warren=ecología perceptual, no autopoiesis estricta). El cap 02-04 §4 lo mitiga restringiendo el sentido a "estabilización dinámica del sistema acoplado bajo restricciones", no a clausura operacional autopoiética. La convención del glosario es la salvaguarda.
- **Riesgo residual:** un lector hostil podría argumentar que importar "self-organization Maturana-Varela" a Warren-Yilmaz (frenado, balanceo) es estiramiento. Defensa: el cap 02-04 ya disocia el término del compromiso autopoiético fuerte. Si Jacob quiere endurecer, podría reemplazar las 4 ocurrencias en 05-05 por "estabilización dinámica (cap 02-04 §4)" — operación mecánica, sin pérdida de contenido. Decisión H-J.

## Resultado

VERIFIED — la mezcla denunciada por el adversarial no existe en el manuscrito. Acceptance satisfecha. Sin acción obligatoria.
