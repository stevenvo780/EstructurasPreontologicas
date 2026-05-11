---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 03-formalizacion/04-operacionalizacion-de-kappa.md:106-108 ; 03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:94 ; 03-formalizacion/07-plantilla-dossier-anclaje.md:128-141 ; 03-formalizacion/05-etica-y-gobernanza-de-datos.md:55
hallazgo: Bitacora/2026-05-04-continuous-run/F03-04-traduccion-b-l3-sin-criterio.md
tipo: reemplazo_parrafo + reformulacion_tabla + nota_caso_30
---

## Diagnóstico

La traducción B↔L3 tal como está formulada admite **trampa nominal**: basta que un parámetro de L3 tenga nombre biomecánico o informacional para considerarlo "traducido", sin exigir que su valor numérico provenga de un procedimiento de medición independiente del ajuste a L3 (Frigg & Hartmann, *Stanford Encyclopedia of Philosophy*, "Models in Science", §2.4). El caso ancla 30 (Fajen-Warren) lo evidencia: sus cuatro parámetros centrales `(b, k_g, c_1, c_2) = (3.25, 7.50, 0.40, 0.40)` provienen del ajuste original de Fajen & Warren (2003) a sus datos VENLab; aunque las variables tienen interpretación biomecánica, el valor numérico es ajuste, no medición independiente.

## Verificación

- `03-formalizacion/04-operacionalizacion-de-kappa.md:108` — la Patología 3 define el remedio como "reformular las funciones del sistema en términos de leyes de control con motivación ecológica o biomecánica": el criterio es la motivación del nombre, no la medición.
- `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:94` — el criterio de fallo "algún parámetro de L3 no se traduce a B" no especifica qué cuenta como traducción válida.
- `03-formalizacion/07-plantilla-dossier-anclaje.md:128-141` Tabla 3.7.4 — columna "Operacionalización" admite "calibración empírica" sin distinguirla de "medición directa".
- `03-formalizacion/05-etica-y-gobernanza-de-datos.md:55` — declara explícitamente que `(b, k_g, c_1, c_2)` son "los publicados en la fuente original [Fajen y Warren 2003]"; ese origen es ajuste, no medición independiente del comportamiento de aproximación-evitación.
- Frigg & Hartmann, "Models in Science" SEP §2.4 — PDF de SEP no se almacena localmente; el argumento metodológico es estándar y se sostiene sin cita literal. Si Jacob inscribe la cita en el manuscrito, debe registrar la versión consultada de SEP con fecha (las entradas SEP versionan).

## Texto propuesto (voz autoral filosófica de Jacob)

**Reemplazar `03-formalizacion/04-operacionalizacion-de-kappa.md:106-108` (Patología 3):**

> ## Patología 3: el modelo que no se traduce a B
>
> Caso: la dinámica de baja dimensión funciona, pero ninguno de sus parámetros se traduce a una variable biomecánica, informacional o de tarea **mediante un procedimiento de medición independiente del ajuste a L3**. Diagnóstico: el modelo es L3 desanclado, aun si los nombres de las variables sugieren motivación biomecánica. No basta con que un parámetro se llame "rigidez de control" o "tasa de aproximación"; se exige que su valor numérico provenga de un protocolo de medición en B (cinemática, fuerza, latencia perceptiva, intervención discriminante directa, etc.) que **no use los mismos datos** que se ajustan en L3. Remedio: (i) aportar el procedimiento de medición independiente, (ii) declarar el parámetro como **calibrado por ajuste** y por tanto **no traducido**, lo que degrada el dossier al estatus de descripción nominal en ese parámetro, o (iii) reformular el sistema con leyes cuyos parámetros sí admitan medición externa. Una traducción por nombre sin medición independiente es **trampa nominal** y queda explícitamente prohibida como criterio de admisión a modo demostrativo.

**Reescribir Tabla 3.7.4 (`03-formalizacion/07-plantilla-dossier-anclaje.md:128-141`)** desdoblando la columna "Operacionalización" en dos:

> | Parámetro de L3 | Variable de B | Unidad | Procedimiento de medición independiente | Valor medido independientemente | Valor usado en L3 | Diferencia |
> |---|---|---|---|---|---|---|
> | ode_alpha | tasa de … | s⁻¹ | [protocolo en B, citado] | [valor + IC] | [valor de ajuste] | [δ relativo] |
> | … | … | … | Si esta celda dice "ajuste a los mismos datos", el parámetro queda marcado como **NO TRADUCIDO** | — | … | — |

Y bajo la tabla, la regla operativa:

> **Regla de admisión.** Un parámetro cuya celda "Procedimiento de medición independiente" esté vacía o coincida con el ajuste de L3 se reporta como **calibrado, no traducido**. Un dossier con uno o más parámetros centrales calibrados y no traducidos se admite **sólo en modo programático**, no demostrativo, y debe declararlo en §13 Limitaciones.

**Reformular criterio de fallo en `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:94`:**

> - algún parámetro de L3 no se traduce a B mediante medición independiente del ajuste L3 (formalismo desanclado **o calibración nominalizada como traducción**);

**Añadir nota explícita de costo al caso 30 en `03-formalizacion/05-etica-y-gobernanza-de-datos.md:55`:**

> **Aclaración de costo.** Los parámetros `(b, k_g, c_1, c_2) = (3.25, 7.50, 0.40, 0.40)` provienen del ajuste de Fajen y Warren (2003) a sus propios datos de captura motora en el VENLab, no de medición independiente de variables biomecánicas (rigidez efectiva, viscosidad de control, latencia perceptiva). Por la regla de Patología 3 actualizada, el caso 30 queda **calibrado, no traducido** en sus cuatro parámetros centrales y por tanto opera en **modo programático**, no demostrativo, respecto al criterio D (traducibilidad B↔L3). Esto se asume como deuda residual del caso ancla y debe declararse en §13.

## Costo argumentativo declarado

El caso ancla canónico (Fajen-Warren) deja de cumplir el criterio D en sentido estricto y la matriz 20/20 de Tabla 3.2.1 baja en al menos un criterio. Varios casos del corpus que hoy figuran como "traducidos" porque sus parámetros ODE tienen nombres físicos caerán a "calibrados, no traducidos" hasta que se aporten mediciones independientes; el modo demostrativo se restringe a un subconjunto menor. Ganancia: la traducibilidad B↔L3 se vuelve auditable con un criterio binario (¿hay protocolo de medición externo, sí o no?), no por inspección semántica del nombre del parámetro — Frigg-Hartmann §2.4 cierra. Decisión abierta para Jacob: si la regla admite **medición indirecta por intervención discriminante** (manipular `d_g` y observar respuesta de `φ̇`) como sustituto aceptable de medición directa, o si exige medición directa estricta.
