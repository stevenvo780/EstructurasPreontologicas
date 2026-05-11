---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 04-debates/04-anticipacion-objeciones-filosoficas.md:216-221 (§5)
hallazgo: Bitacora/2026-05-04-continuous-run/F04-03-dennett-real-patterns-mal-leido.md
tipo: reemplazo_parrafo
---

## Diagnóstico

El §5 de `04-debates/04-anticipacion-objeciones-filosoficas.md` invoca a Dennett *Real Patterns* (1991, *J. Phil.* 88: 27-51) paginando "p. 32-34" y le atribuye autoridad sobre el criterio de "compresión predictiva sin pérdida estructural relevante" como aliado del aparato EDI bajo dos condiciones que la tesis declara como adiciones propias (sustrato material + Woodward). La lectura directa de Dennett pp. 38-40 muestra que Dennett autoriza el ascenso al *design level* **dentro del mismo sustrato simulado** (Game of Life como bit-map cerrado), no la transferencia desde una simulación ablada a un sustrato físico re-identificado. Donde Dennett habla de "intervención", la intervención es interna al bit-map (encroachment de configuraciones vecinas), no intervención woodwardiana sobre sustrato externo. La equivalencia "ablación interna del modelo EDI = intervención woodwardiana sobre el sustrato físico" excede tanto a Dennett como a Woodward.

## Verificación contra fuente primaria (PDF local)

`07-bibliografia/Dennett - Real Patterns (1991).pdf`, p. 39-40:

> "Notice, too, that at this level one proposes generalizations that require 'usually' or 'provided nothing encroaches' clauses. Stray bits of debris from earlier events can 'break' or 'kill' one of the objects in the ontology at this level; their salience as real things is considerable, but not guaranteed." (p. 39, transición a p. 40)

> "To say that their salience is considerable is to say that one can, with some small risk, ascend to this design level, adopt its ontology, and proceed to predict —sketchily and riskily— the behavior of larger configurations or systems of configurations, **without bothering to compute the physical level**." (p. 40)

Cita verificada palabra por palabra contra el PDF local mediante extracción `pdftotext` (la frase "without bothering to compute the physical level" aparece literalmente en el cuerpo de la p. 40, primera columna).

## Texto propuesto (voz autoral filosófica de Jacob)

**Reemplazar el bloque de líneas 216-221 (sub-sección sobre Dennett) en `04-debates/04-anticipacion-objeciones-filosoficas.md` §5 por:**

> Sobre **Dennett** en *Real Patterns* (1991, *Journal of Philosophy* 88: 27-51): la lectura fuerte (pp. 38-40, en particular p. 39 donde Dennett describe el ascenso al *design level* en el Game of Life) ofrece una analogía exacta con el régimen empírico del corpus EDI, pero con un costo que conviene declarar antes de invocarla.
>
> Dennett autoriza elevar a un nivel ontológico cuyas predicciones sobreviven *con cierto riesgo* — p. 39: *"generalizations […] require 'usually' or 'provided nothing encroaches' clauses"* — **dentro del mismo sustrato simulado**. La intervención que Dennett contempla es interna al bit-map del Life world: encroachment de configuraciones vecinas, condiciones iniciales alternativas dentro del mismo autómata determinista cerrado. No es una intervención woodwardiana sobre un sustrato físico externo a la simulación. La frase canónica de la página 40 lo explicita: *"one can, with some small risk, ascend to this design level, adopt its ontology, and proceed to predict —sketchily and riskily— the behavior of larger configurations or systems of configurations, **without bothering to compute the physical level**"*.
>
> El protocolo EDI hereda esa estructura: la ablación `EDI = 1 − RMSE_coupled / RMSE_no_ode` apaga el acoplamiento ODE→ABM **en el modelo acoplado**, no en el sistema físico que el modelo abstrae. La intervención es **modelo-interna y simulada**, no woodwardiana sobre el sustrato. La tesis declara explícitamente esta asimetría: **intervención ablativa simulada ≠ intervención woodwardiana sobre sistema físico.** El corpus EDI ofrece evidencia de que cierto patrón es real *en el sentido denneteano de p. 39* (sobrevive el filtro de compresión predictiva interna), no evidencia de que el patrón sobreviva manipulación física directa del sustrato.
>
> Casos donde la diferencia es operativamente decisiva:
>
> - **Caso 16 deforestación (von Thünen, EDI ≈ 0.58–0.60).** La ablación apaga el acoplamiento von Thünen→agentes en el simulador; no se tala ni se reforesta el paisaje real. La evidencia woodwardiana sobre el paisaje exigiría experimentos cuasi-naturales (cortes de carretera, moratorias, expropiaciones).
> - **Caso 04 energía (Lotka-Volterra, EDI = 0.65).** La ablación es del acoplamiento red↔demanda en el modelo; la intervención woodwardiana exigiría apagar líneas reales y medir efectos en consumo agregado.
> - **Caso 20 Kessler (densidad orbital, EDI = 0.35).** La ablación cierra el feedback fragmentación→colisión en el simulador; ninguna agencia interviene físicamente la densidad orbital.
> - **Caso 27 riesgo biológico (mortalidad, EDI = 0.33).** La ablación apaga el acoplamiento patógeno→demografía en el modelo; los datos físicos provienen de eventos epidémicos no manipulados experimentalmente.
> - **Caso 30 VENLab (Fajen-Warren).** Aquí la asimetría se invierte: el caso sí tiene intervención experimental real sobre sujetos humanos en el VENLab, y por eso la sonda alternativa pudo detectar circularidad estructural (cf. F03-10). El contraste con el resto del corpus muestra que **cuando la intervención woodwardiana existe, opera como filtro adicional al EDI**, no como su sinónimo.
>
> La tesis recoge entonces el criterio denneteano de patrón real (compresión predictiva interna) como criterio **necesario pero no suficiente** para la realidad woodwardiana del patrón. Donde el corpus tiene además acceso a manipulación física (caso 30 VENLab), la condición woodwardiana opera como filtro adicional; donde sólo tiene ablación interna del modelo, la tesis afirma realidad denneteana del patrón, no realidad woodwardiana fuerte. Esa modestia es el costo declarado de operar mayoritariamente con datos observacionales sobre los que no se interviene físicamente.

## Texto a reemplazar / propagar

- Actualizar el rango paginado citado de "pp. 32-34" a "pp. 32-34, 38-40 (esp. p. 39 y p. 40, primera columna)".
- Verificar y, si procede, ajustar el §"criterios-admision" de cap 03 y la narrativa de cada caso EDI en cap 09 para alinearlas con la asimetría ablación-de-modelo ≠ intervención-woodwardiana.

## Costo argumentativo declarado

- La tesis pierde la lectura cómoda de Dennett como aliado universal y gana defensibilidad frente a un evaluador familiarizado con *Real Patterns* y con Woodward 2003.
- El §5 deja de responder sólo a F6 (cita decorativa) y asume además la asimetría F4 (ablación como evidencia limitada).
- La modestia metodológica es el precio de operar con datos observacionales mayoritarios; la alternativa (afirmar manipulabilidad woodwardiana sobre los sustratos físicos del corpus desde los EDI internos) es indefendible.
