# Auditoría process-verifier — Hilo narrativo Cap 02 → 03 → 05 → 06

**Fecha:** 2026-05-16
**Cadena auditada:** 02-01 → 02-04 → 03-01 → 03-02/07 → 03-04 → 05-05 → 06-01
**Protocolo:** PRM step-by-step + 3 preguntas hostiles por salto.

---

## Tabla maestra de pasos

| # | Etapa | Claim central | Sustenido | Necesario | Transición a N+1 |
|---|-------|---------------|-----------|-----------|-------------------|
| 1 | 02-01 §0.2.3 + §2.2.1 | "Estructura pre-ontológica" = atractor empírico con 5 condiciones de admisión | OK (definición técnica explícita) | OK (centra ontología) | Parcialmente válida — ver Salto A |
| 2 | 02-04 §1 + §4 + §8 | B es acoplamiento empírico genérico multiescalar; asimetría L1↔B↔L3↔S; self-organization anclada en Maturana-Varela + Haken | OK con concesión declarada (la doble base "no es convergencia", §4 último párrafo) | OK | Parcialmente válida — ver Salto B |
| 3 | 03-01 §3-7 | 5 operadores μ, G, H, κ, ε con criterios de admisión/fallo | OK (cada operador con criterio formal) | OK | Parcialmente válida — ver Salto C |
| 4 | 03-07 (plantilla) | Dossier de anclaje con 14 componentes; 1-3 + 7-9 obligatorios en programático | OK (plantilla explícita) | OK | Válida |
| 5 | 03-04 | EDI = 1 - RMSE_coupled/RMSE_no_ode + 4 pruebas + C1-C5 | OK con caveats (TENG-01, TENG-02, TENG-08 declarados en 06-01 §4.2) | OK | Parcialmente válida — ver Salto D |
| 6 | 05-05 (caso ancla Warren) | Caso ancla canónico demuestra los 4 puntos (compresión legítima, atractores reales, bifurcaciones, predicciones discriminantes) | Mixto — los r² = 0.98 vienen de Fajen-Warren, no de la pipeline EDI del cap 03-04. F05-07 declara que los 7 parámetros se ajustan sobre los mismos datos | OK como caso paradigmático | Parcialmente válida — ver Salto E |
| 7 | 06-01 §1 + §2 | 7 condiciones de demostración + 3+1 escenarios de fracaso | Mixto — la Condición 7 (honestidad sobre dominio de validez) se sostiene; condición 5 (cartografía multidominio) está debilitada por §3.6 (baselines superan al acoplado en 2 de 4 strong) | OK | — |

---

## Saltos críticos (3-5 que requieren refuerzo)

### Salto A. 02-01 → 02-04 (ontología → anclaje B multiescalar)

**Problema estructural.** El cap 02-01 define estructura pre-ontológica como **atractor empíricamente identificable con 5 condiciones** (§2.2.1). El cap 02-04 redefine B como **acoplamiento empírico genérico** (§1) e instancia los 4 invariantes en 8 escalas (qubit-baño, proteína-solvente, organismo-entorno, cúmulo-marea). El problema: el cap 02-01 introduce **cuatro invariantes ontológicos** (sustrato, acoplamiento, atractor, cierre operativo κ) en su §"La tesis como ontología general invariante a la escala" (líneas 83-90), y el cap 02-04 abre con la asimetría L1↔B↔L3↔S sin reaclarar la correspondencia *4 invariantes → asimetría 4 registros*. Los registros L1/B/L3/S no son los 4 invariantes — son niveles descriptivos, no estructuras del sustrato.

**Pregunta hostil (a):** Si eliminamos el §"La tesis como ontología general invariante a la escala" de 02-01, ¿sobrevive 02-04? **Sí**, porque 02-04 reintroduce los 4 invariantes vía Tabla 2.4.1. Esto sugiere que el §invariantes de 02-01 es **redundante** con la tabla de 02-04 (suspicious: filler en 02-01 o falta de cross-reference explícito).

**Pregunta hostil (c):** ¿"Atractor empírico" en 02-01 §2.2.1 coincide bit-a-bit con "atractor" en Tabla 2.4.1 de 02-04? **No exactamente**: en 02-01 el atractor exige cuenca de atracción **medida experimentalmente** (condición 3); en 02-04 la columna "Atractor empírico" lista "relación P-L como atractor" para caso 39 (Cefeida) sin que la cuenca sea producto de manipulación experimental — es ajuste a datos observacionales. **El cap 02-01 §0.3 (κ-pragmática vs κ-ontológica) ya admite esto**, pero la sustitución se hace en silencio en 02-04.

**Refuerzo sugerido:** añadir en 02-04 §1, después de la Tabla 2.4.1, una nota: "los atractores de las escalas no-experimentales (33, 39, 40) son atractores en sentido κ-pragmática según cap 02-01 §0.3, no κ-ontológica con cuenca manipulada".

---

### Salto B. 02-04 → 03-01 (asimetría L1↔B↔L3↔S → operadores μ, G, H, κ, ε)

**Problema estructural.** El cap 02-04 §11 dice "el operador μ : R → X debe leerse, en el caso de fenómenos psicológicos y conductuales, como medición a nivel B". El cap 03-01 §3.2 dice "para fenómenos a nivel B, X puede incluir variables conductuales..., para otros dominios X se especifica análogamente". El **"análogamente" no está especificado** para escala cuántica, astrofísica o molecular. En 03-01 no hay una tabla equivalente a Tabla 2.4.1 que muestre **cómo X se especifica en cada escala**.

**Pregunta hostil (a):** Si el revisor elimina la asimetría L1↔B↔L3↔S del cap 02-04, ¿sobreviven los operadores de 03-01? **Sí**: los operadores se definen formalmente sin referencia a L1/B/L3/S. Esto es **sospechoso**: si la asimetría es protocolo central de la tesis, debería ser **constitutiva** del aparato formal, no decorativa. La nota terminológica en 03-01 §1 ("El nivel B... es el lugar donde E1 vive cuando el dominio es psicológico-conductual") **reduce B a un caso particular**, contradiciendo la generalización multiescalar de 02-04 §1.

**Pregunta hostil (c):** ¿"B" en 02-04 (acoplamiento empírico genérico) = "B" en 03-01 (dominio psicológico-conductual)? **NO**. 02-04 generaliza B; 03-01 lo regionaliza. **Esto es redefinición silenciosa entre capítulos** — exactamente el tipo de no-coherencia que el cap 02-01 §0.2.4 prohibía bajo "regla de cierre".

**Refuerzo sugerido:** reescribir 03-01 §1 nota terminológica para reflejar la generalización de 02-04: "B es el nivel donde E1 vive en cualquier escala donde la medición se hace sobre el par dinámico acoplado".

---

### Salto C. 03-01 → 03-04 (operadores formales → operacionalización EDI)

**Problema estructural.** En 03-01 §6.3 la legitimidad de κ exige: (a) reproducir trayectorias dentro de τ, (b) preservar atractores/repulsores/bifurcaciones, (c) predecir respuestas a perturbaciones. En 03-04 (operacionalización) **se añade una 4ª prueba: generalización a condiciones no usadas para ajuste**. Las 4 pruebas del Paso 6 de 03-04 NO son exactamente las 3 de 03-01 §6.3 — hay un componente nuevo introducido sin justificación.

**Pregunta hostil (b):** ¿Existe una alternativa que produciría conclusión distinta? Sí: si en lugar de "EDI = 1 - RMSE_coupled/RMSE_no_ode" se hubiera definido EDI como cociente de likelihoods, los 4 casos `overall_pass=True` podrían ser distintos. **El cap 03-04 no justifica que la forma 1 - RMSE_coupled/RMSE_no_ode sea la única operacionalización legítima de κ**. La cita Glymour 1980 (bootstrap problem) es decorativa: no resuelve la pregunta "por qué esta forma específica de EDI".

**Pregunta hostil (a):** Si se elimina el cap 03-01 (operadores formales), ¿sobrevive 03-04? **Casi sí**: 03-04 §"Relación con el aparato formal previo" liga los pasos a μ, G, H, κ, ε, pero el procedimiento empírico de 03-04 (PCA, Lyapunov, ajuste de baja dimensión) es **independiente del aparato formal**. Esto sugiere que el aparato formal de 03-01 puede ser **recubrimiento retórico** del pipeline EDI, no su fundamento. La transición se sostiene débilmente.

**Refuerzo sugerido:** en 03-04 §"Tesis del capítulo", añadir justificación explícita de por qué EDI = 1 - RMSE_coupled/RMSE_no_ode es la operacionalización canónica (vs alternativas como likelihood ratio, KL-divergencia entre ensembles). Cap 06-01 §4.2 [TENG-10] ya identifica un problema en baselines target distinto — esto debería citarse explícitamente.

---

### Salto D. 03-04 → 05-05 (EDI + protocolo → caso ancla Warren)

**Problema estructural.** El cap 05-05 reporta "r² = 0.980 / 0.975" (Fajen-Warren 2003) como demostración de compresión legítima. **Pero esto NO es EDI**. EDI es ablación interna del término ODE→ABM; r² es ajuste paramétrico. El cap 05-05 nunca calcula EDI sobre los datos VENLab; el caso 30 del corpus EDI sí lo calcula y da **0.262 weak**, no strong. El cap 05-05 dice "Esta reducción es la operación κ. Su legitimidad se examina caso por caso con el procedimiento del capítulo de operacionalización" pero **no aplica las 4 pruebas del Paso 6 de 03-04** sobre el caso ancla; aplica el ajuste Fajen-Warren que es **pre-EDI**.

**Pregunta hostil (c):** ¿"κ" en 05-05 (ajuste Fajen-Warren con r² = 0.98) coincide bit-a-bit con "κ" en 03-04 (4 pruebas validadas)? **NO**. 05-05 demuestra **compresión paramétrica** a un modelo de segundo orden; 03-04 exige reproducción + generalización + topología + intervención. El cap 05-05 §"Caso 4" sólo verifica reproducción + topología, no generalización ni intervención cuantificada (la "predicción discriminante" §6.4 es cualitativa).

**Pregunta hostil (b):** ¿Si hubiéramos usado un ajuste polinomial alto-grado en lugar de Fajen-Warren, daría r² = 0.98 también? **Probablemente sí** — F05-07 declara explícitamente esta vulnerabilidad (Roberts-Pashler 2000). El cap 05-05 NO declara nº de parámetros libres ni cross-validation; la deuda está fechada pero **el capítulo sigue presentando r² = 0.98 como evidencia fuerte** en el cuerpo principal.

**Refuerzo sugerido:** en 05-05 §"Caso 4" añadir párrafo explícito de "Cota interpretativa" con (a) nº de parámetros libres, (b) ausencia de cross-validation, (c) asimetría con EDI = 0.262 del caso 30 EDI, (d) reformulación del r² = 0.98 como "cota superior intra-sesión, no demostración del cierre operativo en sentido EDI".

---

### Salto E. 05-05 → 06-01 (caso ancla → 7 condiciones de demostración)

**Problema estructural.** El cap 06-01 §1 Condición 4 dice "todos los parámetros corresponden a magnitudes físicas, biológicas o socioeconómicas con contraparte empírica" en los 5 casos strong. **Pero la Patología 3 de 03-04 prohíbe traducción por nombre sin medición independiente del ajuste a L3**. El cap 06-01 NO documenta caso por caso que los parámetros ode_alpha, ode_beta, macro_coupling, forcing_scale hayan sido medidos por procedimiento independiente del ajuste. La Condición 4 está enunciada como **verificación sostenida** sin que el proceso de verificación sea explícito.

**Pregunta hostil (a):** Si eliminamos el cap 05-05, ¿sobreviven las 7 condiciones del cap 06-01? **Sí, salvo Condición 7** (que cita explícitamente el caso 30). Las Condiciones 1-6 son verificables sin caso ancla. Esto sugiere que el caso ancla está **infrautilizado** en la conclusión: si fuera caso paradigmático canónico, su ausencia debería derribar al menos 3 de las 7 condiciones.

**Pregunta hostil (c):** ¿"strong" en 06-01 §1 Cond 5 (4 casos con overall_pass) coincide bit-a-bit con "strong" en cap 02-01 §"Tabla síntesis" (donde caso 31 cuántico aparece como strong con EDI = 0.91)? **NO**. 02-01 mezcla casos macro y casos inter-escala bajo etiqueta común "strong"; 06-01 §1 Cond 5 separa "4 strong macro" y "7 strong inter-escala". La asimetría inter-dominio vs inter-escala se hace **explícita sólo en 06-01**; los caps 02-01 y 02-04 las presentan como equivalentes.

**Refuerzo sugerido:** uniformizar en 02-01 y 02-04 la distinción "strong macro / strong inter-escala" que 06-01 maneja. Actualmente la prosa de capítulos centrales lee "7 strong en 7 escalas" como si fueran tan demostrativos como los 4 strong macro, cuando 06-01 §5.4 (V4) reconoce que los inter-escala son "etiquetas nominales sobre datos sintéticos".

---

## Términos huérfanos o que cambian de sentido entre capítulos

1. **"B" (nivel B):** generalizado en 02-04 §1, regionalizado en 03-01 §1 nota terminológica. **Cambio silencioso**.
2. **"strong":** colapsa casos macro reales y casos inter-escala sintéticos en 02-01 y 02-04; se desambigua sólo en 06-01 §5.4.
3. **"κ legítima":** en 02-01 §0.3 admite distinción κ-pragmática / κ-ontológica; en 03-01 §6 colapsa a "legítima respecto de Q"; en 03-04 las 4 pruebas operacionalizan κ-pragmática, no κ-ontológica. La distinción **no se reactiva** en 05-05.
4. **"compresión":** en 03-01 §6 es reemplazo de subgrafo por nodo; en 03-04 es ajuste de sistema dinámico de baja dimensión; en 05-05 §"El sistema acoplado en notación canónica" es reducción de cientos de DoF a una variable conductual φ. Tres operacionalizaciones distintas presentadas como equivalentes.
5. **"self-organization":** anclada explícitamente en 02-04 §4 (Maturana-Varela + Haken con costo declarado); en 05-05 §"Caso 2" se usa con sufijo "(en el sentido técnico anclado en cap 02-04 §4)" — bien anclado. **Este término es el mejor manejado**.

---

## Sección donde la justificación es más débil

**Cap 06-01 §1 Condición 4 (asimetría L1↔B↔L3↔S como protocolo de traducción).**

Razón: el "test de fallo" ("si algún parámetro no se traduce a B, hay formalismo desanclado") se declara "verificación sostenida en los 5 casos strong: todos los parámetros corresponden a magnitudes físicas, biológicas o socioeconómicas con contraparte empírica". **Pero la Patología 3 del cap 03-04** exige que la medición sea **independiente del ajuste a L3**, y eso NO se verifica en ningún dossier del corpus (los parámetros ode_alpha, ode_beta se ajustan sobre los mismos datos que validan el modelo). La Condición 4 está **enunciada como verificada pero el procedimiento de verificación viola la propia Patología 3 del manuscrito**.

Esta es la inconsistencia interna más relevante de la cadena auditada: el cap 06-01 declara cumplida una condición cuyo protocolo de verificación (cap 03-04 Patología 3) NO se aplicó al corpus.

---

## Diagnóstico final

**WARN_BROKEN_STEP** en transición 05-05 → 06-01 sobre Condición 4. El cap 06-01 §1 Condición 4 declara verificación sostenida usando un criterio (traducción nominal de parámetros) que el propio cap 03-04 Patología 3 declara insuficiente. **Reparación propuesta:** reformular Condición 4 como "verificación parcial: los parámetros tienen contraparte nominal en B, la traducción por medición independiente queda como deuda residual (patología 3 del cap 03-04)".

**SOFT_WARN** en transiciones A (02-01→02-04), B (02-04→03-01), C (03-01→03-04), D (03-04→05-05) — saltos válidos pero con redefiniciones silenciosas que requieren refuerzo explícito de cross-reference.

**Conclusión global:** la cadena narrativa **se sostiene débilmente** porque los pasos individuales son válidos y la conclusión del 06-01 está enunciada con honestidad metodológica (§§3.6, 8.2 reconocen las debilidades). Pero hay **redefiniciones silenciosas** entre capítulos (especialmente B = "nivel B", strong, κ legítima) que un revisor adversarial puede explotar para acusar de bait-and-switch terminológico. **No es leap of faith; sí es prosa filosóficamente desigual.**
