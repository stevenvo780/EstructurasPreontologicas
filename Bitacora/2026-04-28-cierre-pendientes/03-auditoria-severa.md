# Auditoría severa — ataques constructivos al manuscrito

> Auditoría sin auto-indulgencia. Lo anterior estaba bien estructurado pero **demasiado complaciente**. Aquí se nombran los problemas reales que un comité hostil o un revisor de *Synthese* / *Philosophy of Science* / *Erkenntnis* señalaría sin dudar. Cada ataque viene con su corrección operativa.

**Política:** asumimos que la tesis vale la pena defender, por eso atacamos donde flaquea. Si la respuesta a un ataque es *"depende del lector"*, el ataque es válido y debe corregirse, no defenderse.

---

## ATAQUE A1 — La métrica EDI puede ser un artefacto del propio aparato

### Acusación

`EDI = 1 − RMSE_coupled / RMSE_no_ode` mide la diferencia de RMSE entre el ABM con ODE y el ABM sin ODE manteniendo el mismo forcing. Si la sonda ODE está ajustada al fenómeno, **por construcción** RMSE_coupled < RMSE_no_ode y EDI sale positivo. Lo que el aparato detecta no es necesariamente cierre operativo del fenómeno, sino que **la sonda está calibrada al fenómeno**. Esto es tautología disfrazada de descubrimiento.

### Por qué duele

- Un revisor pregunta: *"¿cómo distingues 'sonda calibrada al fenómeno' de 'fenómeno con cierre operativo'?".*
- La respuesta actual es la prueba de permutación. Pero permutar la observación NO permuta la calibración: la sonda sigue siendo la sonda. La permutación rompe la asociación temporal, no la calibración paramétrica.
- Los controles de falsación (06, 07, 08) tienen forcing/datos diseñados para que la sonda falle. **Eso es selección sesgada de controles**: un escéptico diría "elegiste controles donde sabías que ibas a fallar; eso no demuestra que los strong sean genuinos".

### Corrección operativa requerida

1. **Test de falsos positivos masivo bajo random walk + bootstrap de calibración.** Generar 500 series de random walk puro, calibrar la sonda como en el aparato real, computar EDI. La distribución de EDI esperada bajo nulo debe centrarse en 0; si se centra en > 0, el aparato es sesgado.
2. **Reportar tasa de tipo I empírica.** Si la tasa al umbral declarado (p < 0.05) es > 5%, hay calibración rota.
3. **Implementar el control con shuffling de calibración**, no solo de observación.

### Prioridad

**Crítica.** Sin esto, todos los EDI altos del corpus son sospechosos.

---

## ATAQUE A2 — El caso 30 sufre circularidad ABM ≡ ODE no resuelta

### Acusación

El caso 30 declara: *"los datos no se generan con la sonda EDI simplificada; se generan con el sistema completo Fajen-Warren. Esto evita la circularidad ABM ≡ ODE."*

Falso. Los datos se generan con la **ecuación de segundo orden de Fajen-Warren**. La sonda EDI usa la **misma ecuación de segundo orden de Fajen-Warren**. La diferencia es solo de implementación numérica (Euler dt=0.05 vs runge-kutta o lo que sea). El test es: *¿predice Fajen-Warren a Fajen-Warren?*. Por supuesto.

### Por qué duele

- Para el comité, *"datos sintéticos generados por la teoría que la tesis prueba"* es un patrón clásico de circularidad.
- La defensa "evita circularidad porque el ABM y el ODE son distintos" no se sostiene: ambos siguen la misma ecuación dinámica.

### Corrección operativa requerida

1. **Generar datos con un sistema ALTERNATIVO** que no sea Fajen-Warren (e.g., minimum-jerk control de Hogan 1984, o random walk con drift, o τ-dot de Lee 1976 puro sin atractor).
2. **Aplicar la sonda Fajen-Warren a esos datos.**
3. Si EDI sigue siendo > 0.20: el resultado es genuino bajo desafío.
4. Si EDI cae a < 0.05: la sonda solo funciona en su propio dominio generativo; el caso 30 debe rebajarse a ilustración metodológica, no demostración.

### Prioridad

**Alta.** El caso 30 es bisagra entre demostración cualitativa y cuantitativa; si circula, el bisagra cae.

---

## ATAQUE A3 — Multi-sonda no es validación cruzada genuina

### Acusación

El programa multi-sonda (`09-simulaciones-edi/multi_sonda/`) se ejecuta así:

1. genera serie con sonda primaria;
2. predice con sonda primaria → RMSE_p;
3. predice con sonda alternativa → RMSE_alt;
4. compara EDI_p vs EDI_alt.

Pero los DATOS de referencia los genera la sonda primaria (test step 1). Lo que se mide es: *¿qué tan bien la sonda alternativa predice algo generado por la primaria?*. Esto no es convergencia ontológica; es ajuste de cobertura de modelo.

### Por qué duele

- Un revisor preguntaría: *"si las dos sondas convergen sobre datos generados por la primaria, ¿qué pasaría sobre datos REALES (no generados)?"*.
- La respuesta correcta requiere ejecutar multi-sonda sobre los datos reales del caso, no sobre re-simulación.

### Corrección operativa requerida

1. **Multi-sonda contra datos REALES del caso**, no contra serie sintética generada por la primaria.
2. Re-ejecutar caso 16 Deforestación con World Bank real bajo `accumulation_decay` y `spatial_logistic`, comparar RMSE de validación contra los datos.
3. Solo si convergen sobre datos reales, la objeción se neutraliza.

### Prioridad

**Alta.**

---

## ATAQUE A4 — Selectividad del corpus = posible cherry picking

### Acusación

El corpus tiene 30 casos seleccionados. Pregunta básica:

- ¿cuántos casos se INTENTARON antes de fijar estos 30?
- ¿hay casos que intentaron y se descartaron porque produjeron EDI inconvenientes (e.g., EDI muy alto en algo que conceptualmente no debería tenerlo, o EDI muy bajo en algo que conceptualmente debería)?

No hay registro pre-experimental de cuántos candidatos hubo. El reporte de 4 strong + 8 weak + 8 null + 3 falsación parece equilibrado, pero **el equilibrio puede ser artefacto de selección**.

### Por qué duele

- Sin pre-registro de criterios de admisión al corpus, la composición misma del corpus es susceptible a sesgo del autor.
- Los 8 nulls "son casos donde la sonda no aplica bien". Pero la decisión de incluirlos o no es discrecional.

### Corrección operativa requerida

1. **Crear `Bitacora/2026-04-28-cierre-pendientes/05-pre-registro-corpus.md`** que liste:
   - todos los dominios considerados ANTES de la ejecución;
   - criterios de inclusión/exclusión declarados ex-ante;
   - reconocer honestamente que el corpus actual es post-hoc;
   - declarar limitación.
2. **Reportar tasas de éxito esperadas por nivel** ANTES de la ejecución, no después.

### Prioridad

**Media-alta.** No invalida la metodología, pero limita la fuerza inferencial del agregado.

---

## ATAQUE A5 — Los umbrales de niveles (0.10, 0.30) son post-hoc

### Acusación

El paisaje de emergencia clasifica casos así:

- weak: 0.10 ≤ EDI < 0.30
- strong: EDI ≥ 0.30

¿Por qué 0.10? ¿Por qué 0.30? El cap 03-04 no justifica estos umbrales con razonamiento pre-empírico. Son **escogidos para que la distribución del corpus quede equilibrada**, no para que tengan significado independiente del corpus.

### Por qué duele

- Cualquier comité experto en estadística pregunta: *"¿este umbral fue declarado antes de mirar los datos?"*. La respuesta honesta es no.
- Los umbrales de p-value (0.05, 0.01) sí son convención disciplinar; los de EDI son del autor.

### Corrección operativa requerida

1. **Justificar pre-empíricamente los umbrales.** Por ejemplo: 0.30 = "reducción del 30% del error predictivo bajo ablación", basado en convenciones de tamaño-efecto en ciencias del movimiento (Cohen 1988 d > 0.5 ≈ 30% varianza).
2. **Análisis de sensibilidad a umbrales:** ¿cómo cambia la clasificación si umbrales son 0.05/0.20 o 0.15/0.40? Si la composición se desbarata fuerte, la elección actual es arbitraria.
3. **Reportar el análisis** en `Anexos/A8-tablas-crudas-corpus.md`.

### Prioridad

**Media-alta.**

---

## ATAQUE A6 — Baselines: ARIMA puede ganar el debate completo

### Acusación

`09-simulaciones-edi/baselines/README.md` reporta que ARIMA gana en RMSE absoluto en 3 de 5 strong. La defensa es *"el aparato no aspira a predicción, aspira a discriminación"*. Pero:

- **¿discrimina ARIMA igual de bien?** Si el ranking ARIMA-RMSE entre strong y null es tan separable como el EDI, el aparato no aporta valor diferencial.
- El reporte actual no compara DISCRIMINACIÓN (clasificación strong vs null vía baseline), solo RMSE puntual.

### Por qué duele

- Un revisor obvio diría: *"si tu valor único es la discriminación, demuéstralo midiendo discriminación, no RMSE"*.
- La defensa actual es post-hoc: cambiar el criterio de evaluación cuando se pierde en el original.

### Corrección operativa requerida

1. **Definir métrica de discriminación:** AUC-ROC o similar entre RMSE de strong vs RMSE de null.
2. **Calcular AUC-ROC para EDI y para |RMSE_arima - RMSE_naive|** sobre los 8 casos.
3. Si AUC-ROC del aparato ≤ AUC-ROC de ARIMA + 0.10, la ventaja diferencial no existe.
4. **Reportar honestamente.**

### Prioridad

**Alta.** Es el ataque más directo a la utilidad del aparato.

---

## ATAQUE A7 — Falsabilidad declarada pero NO probada agresivamente

### Acusación

El cap 06-01 lista 5 condiciones de fracaso que falsearían la tesis. Pero **ningún test ha intentado activamente generar esas condiciones**. Es como decir *"si el cielo se cae, mi teoría es falsa"* y no mirar al cielo.

Específicamente:
- Condición 1 (controles falsos producen overall_pass): los 3 controles existen, pero ¿se han generado **controles de prueba aleatorios** repetidamente para verificar que el aparato rechaza consistentemente? No.
- Condición 3 (drift bajo perfil agresivo): solo se ha verificado en 2 casos; el resto es heurística.
- Condición 4 (multi-sonda diverge en >50% de strong): solo se han probado 3 casos.

### Por qué duele

- Falsabilidad no es declarar; es ofrecer la prueba.
- La distinción Popper: una teoría falsable que nadie intentó falsar es teoría débil.

### Corrección operativa requerida

1. **Hostile testing automatizado:** generar 100 series random walk con calibración real del aparato; reportar cuántas pasan overall_pass. Debe ser ≤ 5%.
2. **Ejecutar perfil agresivo masivo** en los 5 casos strong, no solo en 2.
3. **Multi-sonda real (post-A3)** en los 5 strong.

### Prioridad

**Crítica.**

---

## ATAQUE A8 — La conjetura κ es circular

### Acusación

Cap 03-04 define: *"Una compresión κ(G) = G* es legítima respecto de Q si y solo si existe un sistema dinámico de baja dimensión sobre G* que reproduce trayectorias, preserva topología, predice perturbaciones y no oculta transiciones."*

Esto es: **la compresión es legítima si funciona el modelo reducido**. Es circular: la legitimidad ontológica se define por éxito del modelo, no por correspondencia con realidad independiente del modelo.

### Por qué duele

- La objeción "irrealismo operativo es operacionalismo disfrazado" se aplica directamente.
- El manuscrito reconoce esto en parte ("la dependencia instrumento-fenómeno no es defecto, es condición") pero no responde la objeción dura: *si la compresión solo se valida internamente, no es ontología; es ergonomía de modelado*.

### Corrección operativa requerida

1. **Distinguir formalmente** dos lecturas de κ:
   - κ-pragmática: la compresión es útil para predecir/intervenir.
   - κ-ontológica: la compresión corresponde a una estructura material independiente del modelo.
2. La tesis solo demuestra κ-pragmática. La declaración ontológica fuerte ("estructuras pre-ontológicas son reales") requiere argumento adicional.
3. **Reformular el cap 02-01** para distinguir niveles de compromiso ontológico.

### Prioridad

**Alta** (filosóficamente).

---

## ATAQUE A9 — La validación ST es lógica interna, no validación científica

### Acusación

La suite ST de 13 teorías verifica que **los axiomas declarados son consistentes**. Eso es bueno. Pero:

- ST no valida que los axiomas sean **verdaderos** en el mundo.
- ST no detecta si los axiomas son **vacíos** (consistentes pero sin contenido empírico).
- La tesis trata ST como certificación; pero ST solo certifica no-contradicción.

### Por qué duele

- Un revisor dice: *"tu suite ST muestra que las afirmaciones que haces son lógicamente coherentes. Eso no quita que puedan ser tonterías ontológicamente."*

### Corrección operativa requerida

1. **Nota explícita en Anexo A.11**: la validación ST es **interna**, no externa. La validez empírica está en el corpus EDI; ST garantiza que los axiomas no se contradicen.
2. **Reformular las conclusiones del A.11** para no sugerir certificación filosófica donde solo hay certificación lógica.

### Prioridad

**Media.**

---

## ATAQUE A10 — Cobertura bibliográfica desigual

### Acusación

Las citas con paginación se inyectaron en cap 02-04, 04-01, 05-04. Los capítulos 02-01 (ontología), 02-02 (epistemología), 02-03 (categorías), 03-01 (aparato), 03-02 (criterios), 03-03 (auditoría) **no tienen ese diálogo textual sostenido**. Pero estos son los capítulos doctrinales más importantes.

### Por qué duele

- Un comité experto en filosofía de la mente leerá cap 02-01 esperando diálogo con Bunge, Ladyman-Ross, Dennett. Encontrará menciones nominales.

### Corrección operativa requerida

1. Inyectar al menos **3 citas textuales con paginación por capítulo** en 02-01, 02-02, 02-03, 03-01, 03-02, 03-03.
2. Cada cita debe ser un pasaje real con respuesta argumental de la tesis.

### Prioridad

**Media-alta.**

---

## ATAQUE A11 — Reproducibilidad declarada, no certificada

### Acusación

`requirements.txt` no está pinneado a versiones exactas. La afirmación "29/29 casos pasan reproducibilidad bit-a-bit con seed=42" depende de:
- versión exacta de numpy/scipy/pandas;
- versión exacta de Python;
- arquitectura del CPU (algunas operaciones SIMD difieren);
- versión de CUDA/cuDNN si se usa GPU.

Sin lock, cualquiera con versiones distintas obtendrá números cercanos pero no idénticos.

### Por qué duele

- El compromiso "reproducibilidad bit-a-bit" es objetivable y, si no se cumple, daña la credibilidad del corpus completo.

### Corrección operativa requerida

1. Generar `requirements-locked.txt` con `pip freeze`.
2. Documentar versión exacta de Python (3.13.x), arquitectura (x86_64), kernel.
3. Probar reproducibilidad en al menos un caso desde cero con `requirements-locked.txt`.
4. Si las cifras NO son bit-a-bit idénticas, decirlo: el seed garantiza determinismo dentro de la misma instalación, no entre instalaciones.

### Prioridad

**Media.**

---

## ATAQUE A12 — Manuscrito-fuente original vs capítulos refinados: divergencia no auditada

### Acusación

`Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md` (408 líneas) es la formulación intuitiva inicial. Los capítulos refinados son su versión doctoral. ¿Hay claims del manuscrito-fuente que se DILUYERON o ABANDONARON sin declaración explícita?

### Por qué duele

- Si el manuscrito-fuente afirmaba X y los capítulos lo abandonan, eso debe estar declarado.

### Corrección operativa requerida

1. Diff conceptual entre manuscrito-fuente y capítulos canónicos.
2. Lista de claims abandonados o refinados radicalmente, con justificación.
3. Archivar como `Bitacora/2026-04-28-cierre-pendientes/04-evolucion-conceptual.md`.

### Prioridad

**Baja-media.**

---

## ATAQUE A13 — La tesis no ha sido sometida a ningún revisor par externo real

### Acusación

Todas las auditorías (v1, exhaustiva, ST, esta) son **internas** o producidas por la asistencia IA. Ningún experto humano externo ha leído el manuscrito y reportado.

### Por qué duele

- La afirmación *"el manuscrito anticipa las preguntas que un comité formularía"* es presunción del autor; no se verifica sin un comité real (o equivalente).

### Corrección operativa requerida

1. **No es ejecutable internamente**, pero documentar claramente como deuda externa.
2. Identificar 2-3 lectores hostiles potenciales (filósofo analítico, modelista computacional, fenomenólogo) para envío preliminar.

### Prioridad

**Crítica para defensa.** Pero externa.

---

## ATAQUE A14 — La afirmación "conocimiento útil" no se opera

### Acusación

El usuario pregunta lo más importante: *¿es esto conocimiento útil?*

El manuscrito demuestra que **el aparato EDI clasifica 30 dominios en 6 niveles de cierre operativo**. ¿Para quién es útil esto?

- Un científico en un dominio específico (e.g., deforestación) ¿gana algo nuevo aplicando EDI? El cap 16 reporta EDI=0.60 con World Bank data, pero ningún ecólogo se beneficia: ya saben que la deforestación tiene dinámica acoplada.
- Un filósofo de la mente ¿gana algo aplicando EDI a behavioral dynamics? El caso 30 con EDI=0.26 weak reproduce lo que Warren ya hizo cualitativamente con r²=0.98.
- Un metodólogo ¿gana un protocolo replicable? Sí, eso sí. El dossier de 14 componentes y la métrica EDI son aporte metodológico.

**El aporte real es metodológico, no descubrimiento sustantivo en ningún dominio.** El manuscrito a veces sugiere lo contrario.

### Corrección operativa requerida

1. **Redefinir explícitamente el aporte:** la tesis es contribución a **metodología filosófica de la complejidad**, no a la ciencia de cada uno de los 30 dominios.
2. Reformular el cap 06-01 para que no presuma descubrimiento sustantivo donde solo hay aplicación metodológica.
3. Listar **un caso concreto** donde EDI haya producido conclusión que la literatura del dominio no tenía. Si no lo hay, decirlo.

### Prioridad

**Crítica conceptualmente.**

---

# Plan de trabajo nocturno autónomo

Listado de ataques con prioridad y plan de ejecución sin supervisión. Numerados por orden de ejecución preferido (más críticos y más rápidos primero):

| # | Ataque | Prioridad | Acción ejecutable | Estimado |
|---|--------|-----------|-------------------|----------|
| N1 | A1 — falsos positivos del aparato | Crítica | Generar 500 random walks; correr EDI simplificado; reportar tasa empírica de falsos positivos | 30-60 min |
| N2 | A2 — circularidad caso 30 | Alta | Generar 100 series con sistemas alternativos (random walk, minimum-jerk Hogan, AR(2) puro); correr sonda behavioral_attractor; reportar EDI esperado bajo nulo | 30 min |
| N3 | A6 — discriminación AUC-ROC del aparato vs ARIMA | Alta | Calcular AUC-ROC del EDI para clasificar strong/null; calcular igual con ARIMA-RMSE; reportar diferencia honesta | 20 min |
| N4 | A5 — análisis de sensibilidad a umbrales | Media-alta | Calcular composición del corpus bajo umbrales {0.05, 0.20}, {0.10, 0.30}, {0.15, 0.40}; reportar | 15 min |
| N5 | A7 — hostile testing automatizado | Crítica | Combinar N1 + permutaciones del corpus; reportar tasa de overall_pass bajo nulo masivo | 45 min |
| N6 | A11 — lock de dependencias | Media | `pip freeze > requirements-locked.txt` + reporte de versiones | 10 min |
| N7 | A4 — pre-registro retroactivo | Media-alta | Crear `Bitacora/2026-04-28-cierre-pendientes/05-pre-registro-corpus-honesto.md` reconociendo limitación post-hoc | 20 min |
| N8 | A8 — distinción κ-pragmática vs κ-ontológica | Alta | Sección nueva en cap 02-01 con declaración explícita | 30 min |
| N9 | A9 — limitación ST en A.11 | Media | Sección "Lo que ST no valida" en A.11 | 15 min |
| N10 | A10 — cobertura bibliográfica restante | Media-alta | Inyectar 3 citas con paginación en cap 02-01, 02-02, 02-03, 03-01, 03-02, 03-03 (18 citas total) | 90 min |
| N11 | A12 — diff conceptual fuente vs capítulos | Baja-media | Reporte en `Bitacora/.../04-evolucion-conceptual.md` | 30 min |
| N12 | A14 — redefinir aporte metodológico | Crítica conceptual | Reformular cap 06-01 §"Aporte conceptual sustantivo" + cap 06-01 cierre | 30 min |
| N13 | Re-build manuscrito + commit final | — | `python3 TesisFinal/build.py` + PDF + commit | 10 min |
| N14 | Auditoría v3 con resultados de los ataques | — | Reporte agregado en Bitacora | 30 min |

**Total estimado:** 6-7 horas de trabajo continuo sin supervisión.

**Política de ejecución autónoma:**

1. cada ataque se ejecuta como tarea individual con commit propio;
2. resultados negativos se reportan honestamente; si A1 muestra tasa de falsos positivos > 5%, se declara explícitamente y se rebaja la confianza del corpus;
3. cada ejecución produce archivo en `Bitacora/2026-04-28-cierre-severo/` con cifras crudas + interpretación;
4. al final, una nueva auditoría v3 reporta qué ataques fueron resueltos, cuáles dejaron heridas reales, y cuáles requieren trabajo posterior;
5. ningún ataque se "explica" si el resultado es desfavorable; se reporta y se ajusta el manuscrito.

**Lo que NO se ejecuta esta noche (requiere recurso externo o discusión humana):**

- A13 (revisor par externo real): solo se documenta como deuda explícita.
- A2 contra-ataque con datasets humanos reales: requiere acceso VENLab/WALK-MS.
- Conversión LaTeX/PDF con plantilla institucional: requiere plantilla.

---

## Veredicto provisional

El manuscrito está **bien arquitecturado pero NO defendido empíricamente con la severidad que sus afirmaciones requieren**. Las correcciones de las auditorías anteriores fueron de coherencia interna, no de prueba empírica del marco contra ataques honestos.

**El plan de trabajo nocturno cierra el último gap real:** demostrar que el aparato funciona bajo prueba hostil, no solo bajo condiciones favorables a su autor.

Si tras ejecutar N1-N14 algunos resultados son negativos, **eso fortalece la tesis**, no la debilita: porque demuestra honestidad metodológica. Una tesis que admite lo que no funciona es más defendible que una que no se atreve a probarse.

> *La auditoría no es un acto de demolición. Es la prueba de que el manuscrito puede mirarse al espejo sin perder coherencia. Si la tesis sobrevive a esto, es defendible. Si no, hay que ajustar las afirmaciones.*

---

**Auditor severo:** preparado por la asistencia IA bajo dirección humana, sin auto-indulgencia.
**Fecha:** 2026-04-28.
**Plan de ejecución:** autónomo, sin supervisión, durante la noche.
