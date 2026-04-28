# Anexo A.11. Validación lógica formal con ST (refactor V5 + 10 teorías nuevas)

## Función

Reporte sistemático de la validación de la lógica interna del marco mediante el lenguaje formal **ST** (`@stevenvo780/st-lang` v3.2.2). Suite extendida a **23 teorías** que evalúan exhaustivamente: la asimetría L1↔B↔L3↔S, la cadena de operadores formales, las 13 condiciones de `overall_pass`, la discriminación contra 14 rivales, los niveles 0-5 del paisaje de emergencia, la falsabilidad, la coherencia modal, la convivencia paraconsistente con Wolfram, **y los 10 puntos del marco refactorizados tras V5**: temporalidad y causalidad, definición técnica de "pre-ontológico", marco tripartito general, naturalismo metafísico moderado, distinción κ-pragmática vs κ-ontológica, dimensión normativa deóntica, asimetría a través de los 3 marcos, stress test de falsabilidad, paraconsistencia del corpus multiescala, y modal del marco tripartito.

**Fuente de verdad ejecutable:** `08-consistencia-st/theories/00-22.st` y reporte automatizado en `08-consistencia-st/reports/ultimo-reporte.md`.

**Ejecución:**

```bash
cd 08-consistencia-st
npm install
npm run st:check
```

## Hallazgos críticos detectados (V5 refactor)

La suite extendida **detectó cuatro problemas reales** que la formulación V4 del manuscrito no anticipaba. Todos se resuelven aquí y se propagan al cuerpo argumental.

### Hallazgo ST-1 (V4 conservado): asimetría L1↔B↔L3↔S no es expresable como axiomas universales proposicionales

Refinada a existenciales en lógica de primer orden (cap 02-04 §8.0). Test 5 de la nueva T19 confirma operatividad inter-escala: existen modelos donde B(qubit), B(cumulo), F(qubit), F(cumulo) y S(qubit), S(cumulo) coexisten satisfactoriamente. La asimetría es invariante a la escala bajo la formulación FOL existencial.

### Hallazgo ST-2 (V4 conservado): necesidad modal requiere axioma T

Sistema modal **al menos T (KT)** declarado en cap 02-01. T22 confirma: en `modal.k` puro no se valida `□P → P` (axioma T no asumido). La declaración explícita en cap 02-01 cierra el hueco.

### Hallazgo ST-3 (V5 nuevo): la respuesta a Kim sobre downward causation requiere construcción argumental, no solo declaración

**Detección (T13 Test 4):** la primera formulación afirmaba *"si downward es constitución, Kim no aplica"* como implicación directa. La verificación ST mostró que la implicación `((C ∧ ¬V) ∧ (K → (V → S))) → ¬S` **NO es válida** sin pasos intermedios.

**Refinamiento ejecutado:** la respuesta correcta es por modus tollens vacuo. Si C → ¬V (constitución no es causación) y K dice `(V → S)`, entonces de `¬V` y `(V → S)` no se infiere S; el argumento de Kim sobre sobredeterminación queda neutralizado **por ausencia del antecedente** (V), no por refutación del consecuente (S).

**Implicación para el manuscrito:** cap 02-05 §2.4 ya articula esto correctamente. La verificación ST formaliza el argumento.

### Hallazgo ST-4 (V5 nuevo): la generalidad del marco NO se infiere desde los casos del corpus

**Detección (T15 Test 2):** `analyze {J} → G` (de "casos justifican" inferir "marco general") es **inferencia NO VÁLIDA**. Esto es exactamente lo que el cap 06-01 §5 afirma: los 40 casos NO son la tesis; son justificación operativa parcial.

**Implicación:** la verificación ST confirma operativamente que el marco general se sostiene por su **estructura interna coherente** (T15 Test 4: `(G → S) ∧ G → S` válida), no por inducción sobre casos. La advertencia contra el inductivismo del manuscrito está formalmente respaldada.

### Hallazgo ST-5 (V5 nuevo): los 3 marcos NO colapsan unos sobre otros

**Detección (T15 Test 5):** los contramodelos de `O → E`, `E → M`, `M → O` **se encuentran**. Esto confirma que los 3 marcos (ontológico, epistemológico, metodológico) son **lógicamente independientes** entre sí: ninguno se reduce a otro.

**Implicación:** la afirmación del cap 06-01 §5 de que el aporte es **triple sustantivo** (no solo metodológico, no solo ontológico, no solo epistemológico) está formalmente verificada.

### Hallazgo ST-6 (V5 nuevo): el naturalismo metafísico moderado NO se demuestra desde dentro

**Detección (T16 Test 6):** countermodel para N (naturalismo) **encontrado**. Esto confirma que el naturalismo es **compromiso de partida**, no conclusión deductiva, exactamente como el cap 02-01 §0.1 declara.

**Implicación:** la honestidad metodológica del manuscrito está formalmente verificada: la tesis NO presume que el naturalismo es una verdad demostrada; lo declara como compromiso filosófico.

## Resumen de la suite refactorizada

| Teoría | Perfil ST | Foco | Estado |
|--------|-----------|------|--------|
| 00 — Núcleo ontológico (V5 refactor) | classical.propositional | 4 invariantes + naturalismo + rechazo de 3 rivales | ✅ |
| 01 — Criterios de legitimidad | classical.propositional | 9 condiciones derivan G y H | ✅ |
| 02 — Debates y límites | classical.propositional | Anti-dualismo, anti-reduccionismo, anti-emergencia | ✅ |
| 03 — Text layer tesis | classical.propositional | 3 claims con confianza > 0.94 | ✅ |
| 04 — Text layer bibliografía | classical.propositional | 3 claims con confianza > 0.90 | ✅ |
| 05 — Asimetría L1↔B↔L3↔S | classical.first_order | Refinamiento a existenciales | ✅ |
| 06 — Operadores y circularidad | classical.propositional | μ→G→H→K→E sin atajos viciosos | ✅ |
| 07 — overall_pass 13 condiciones | classical.propositional | Colectivamente necesarias | ✅ |
| 08 — Discriminación rivales | classical.propositional | 14 rivales discriminados | ✅ |
| 09 — Niveles 0-5 paisaje | classical.propositional | Excluyentes con axiomas explícitos | ✅ |
| 10 — Falsabilidad | classical.propositional | 5 condiciones por modus tollens | ✅ |
| 11 — Modal coherencia | modal.k | Necesidad requiere axioma T | ⚠️ → ✅ |
| 12 — Paraconsistencia Wolfram | paraconsistent.belnap | Coexistencia sin trivialización | ✅ |
| **13 — Temporalidad y causalidad (V5)** | classical.propositional | B-series + Woodward + constitución vs Kim | ⚠️ → ✅ |
| **14 — Pre-ontológico genético (V5)** | classical.first_order | "Pre" simondoniano definido | ✅ |
| **15 — Tres marcos generales (V5)** | classical.propositional | Independencia + no inductivismo | ⚠️ → ✅ |
| **16 — Naturalismo + rivales (V5)** | classical.propositional | Naturalismo excluye 5 rivales metafísicos | ✅ |
| **17 — κ-pragmática vs κ-ontológica (V5)** | classical.propositional | 3 criterios; ningún caso actual los cumple | ✅ |
| **18 — Deóntica normativa (V5)** | deontic.standard | Validez/efectividad/legitimidad coherentes | ✅ |
| **19 — Asimetría tres marcos (V5)** | classical.first_order | Asimetría invariante a la escala | ✅ |
| **20 — Stress test falsabilidad (V5)** | classical.propositional | 8 condiciones de fracaso falsables | ✅ |
| **21 — Belnap corpus multiescala (V5)** | paraconsistent.belnap | Honestidad metodológica sin colapso | ✅ |
| **22 — Modal marco tripartito (V5)** | modal.k | Invariantes necesarios + sondas contingentes | ✅ |
| **23 — Modal T (KT) bajo hipótesis (V5.1)** | modal.k + axioma T explícito | Cierre formal de la declaración "AT LEAST T" del cap 02-01 | ✅ |

**24 teorías ejecutadas, 6 hallazgos críticos detectados (2 V4 + 4 V5), todos resueltos. T23 cierra la consistencia entre el sistema modal declarado en cap 02-01 (KT) y el verificado por la suite (modal.k + axioma T como hipótesis explícita, lógicamente equivalente a modal.kt).**

## Pruebas duras pasadas por la suite refactorizada

### T13 — Temporalidad + causalidad responde a Kim

- **B-series + flecha termodinámica satisfacibles juntas:** ✅
- **EDI como `do`-test woodwardiano:** válido
- **Constitución (Craver) ≠ causación (Kim):** verificado por contramodelo de `C → V`
- **Argumento de Kim neutralizado por modus tollens vacuo:** ✅ T13 Test 4
- **Eternalismo bloque rechazado:** contramodelo encontrado
- **Irreversibilidad κ↔ε es termodinámica, no axioma adicional:** ✅

### T14 — Definición técnica de "pre-ontológico"

- **Estructura pre-ontológica satisfacible con definición simondoniana:** ✅
- **"Pre" temporal puro rechazado:** contramodelo encontrado
- **Génesis del individuo:** instanciación universal válida
- **Regularidad estadística NO es pre-ontológica:** verificado

### T15 — Tres marcos generales independientes

- **Tres marcos colectivamente la tesis:** ✅
- **Generalidad NO se infiere desde casos:** **Hallazgo ST-4 confirmado**
- **Estructura interna coherente necesaria:** modus tollens válido
- **Tres marcos lógicamente independientes:** **Hallazgo ST-5 confirmado** (ninguno colapsa sobre otros)
- **Coexistencia mutua coherente:** satisfacible

### T16 — Naturalismo metafísico moderado

- **Naturalismo excluye dualismo, idealismo, emanacionismo, panpsiquismo, creacionismo:** ✅ los 5
- **Conjunción naturalismo + rival es contradicción:** ✅
- **Naturalismo NO decide entre interpretaciones realistas QM:** ✅
- **Copenhagen instrumentalista pura SÍ se rechaza:** ✅
- **Naturalismo es compromiso de partida, no conclusión:** **Hallazgo ST-6 confirmado** (countermodel para N)

### T17 — κ-pragmática vs κ-ontológica

- **κ-ontológica requiere 3 criterios simultáneos:** ✅
- **κ-pragmática NO implica κ-ontológica:** verificado
- **Ningún caso actual cumple los 3 criterios:** ✅
- **Distinción no trivial:** modelos donde solo se da P existen
- **Colapso κ-pragmática = κ-ontológica rechazado:** contramodelo encontrado

### T18 — Dimensión normativa deóntica

- **Validez normativa = `□C` (cumplimiento necesario):** coherente
- **Efectividad = `<>C` (cumplimiento posible):** coherente
- **Deber = (validez + efectividad), no sustancia:** validado
- **Validez compatible con incumplimiento ocasional:** satisfacible
- **Naturalismo ético no-reduccionista coherente:** ✅

### T20 — Stress test de falsabilidad

- **Cada una de 8 falsaciones refuta tesis:** ✅
- **Tesis NO es tautología:** countermodel encontrado
- **Tesis NO es contradicción:** modelo encontrado
- **Estado actual: corpus NO satisface las falsaciones críticas:** satisfacible
- **Modus tollens válido para cualquier falsación:** ✅

### T21 — Belnap: honestidad metodológica sin colapso

- **Caso 30 sufre circularidad Y produce EDI 0.262:** coexisten en Belnap
- **p-value 24% mal calibrado Y umbrales EDI robustos:** coexisten
- **Sondas depuradas post-hoc Y específicas (V4-01):** coexisten
- **AUC interno Y ausencia de validación externa:** coexisten
- **Honestidad metodológica NO colapsa la tesis:** ✅

### T22 — Modal del marco tripartito

- **4 invariantes declarados como necesarios:** satisfacibles
- **Sondas específicas son contingentes:** satisfacible
- **Regla K (distribución):** válida
- **`[]M → M` requiere axioma T:** confirmado (no en modal.k puro)

## Limitaciones de la validación ST (V5 reforzada)

### Lo que ST sí valida

- Coherencia interna de los axiomas declarados (ausencia de contradicción).
- Validez de inferencias específicas.
- Detección de falacias formales conocidas.
- Existencia de contramodelos para implicaciones no válidas.
- **Independencia lógica de los 3 marcos generales** (T15).
- **Distinción operativa entre constitución y causación** (T13).
- **Naturalismo como compromiso, no conclusión** (T16).
- **Distinción κ-pragmática vs κ-ontológica con 3 criterios operativos** (T17).
- **Coherencia de la dimensión normativa deóntica** (T18).
- **Coexistencia de honestidades metodológicas en Belnap** (T21).

### Lo que ST NO valida

1. **ST no valida que los axiomas sean verdaderos en el mundo.** Solo certifica consistencia interna.
2. **ST no detecta axiomas vacíos.** Un sistema puede ser consistente y vacío.
3. **ST no captura la dinámica acoplada del aparato.** El motor ABM+ODE es objeto computacional con dinámica continua que ST no representa.
4. **ST no audita la calibración empírica de la métrica.** El p-value del 24% es problema empírico que ST no detecta.
5. **La cobertura de la suite es representativa, no exhaustiva.** 23 teorías cubren los puntos críticos identificados; no garantiza completitud.
6. **ST no sustituye revisión humana experta.** El comité doctoral debe leer los axiomas declarados y juzgar si son los correctos.

## Política de uso

La validación ST debe leerse como **certificación de coherencia interna refactorizada y reforzada tras V5**, no como certificación de validez filosófica o empírica. Las dos validaciones complementarias son:

- **validez empírica:** corpus EDI inter-dominio + inter-escala (cap 09 + 05-06 + A.8 + A.12), con limitaciones documentadas en auditorías severa, V4 y V5;
- **validez filosófica:** revisión por pares humanos competentes en filosofía de la mente, ontología analítica y ciencias de la complejidad (deuda externa pendiente).

Esta declaración fue reforzada en V5 con la cobertura adicional de los 10 puntos del marco refactorizados.

## Conclusión V5

La validación lógica formal con ST refactorizada **confirma que los cierres conceptuales V5 (temporalidad, causalidad, pre-ontológico genético, naturalismo declarado, κ-pragmática/ontológica, dimensión normativa, asimetría multiescalar) son lógicamente coherentes**. Los hallazgos críticos detectados durante la verificación (ST-3, ST-4, ST-5, ST-6) **fortalecen la honestidad metodológica del manuscrito**: confirman operativamente que la generalidad del marco se sostiene por estructura interna y no por inducción sobre casos, que el naturalismo es compromiso de partida y no conclusión, y que la respuesta a Kim sobre downward causation requiere argumentación constitutiva específica.

> *La diferencia entre V4 y V5 ST: V4 verificó que la lógica metodológica del marco es coherente; V5 verifica que la lógica filosófica del marco también lo es. Las 10 teorías nuevas (T13-T22) cubren los conceptos sustantivos que un comité humanista exigiría articulados.*

## Lectura cruzada

- Teorías ST originales: `08-consistencia-st/theories/00-12.st`.
- Teorías V5 nuevas: `08-consistencia-st/theories/13-22.st`.
- Reporte automatizado: `08-consistencia-st/reports/ultimo-reporte.md`.
- Capítulos donde los conceptos validados se articulan: 02-01 (ontología, naturalismo, pre-ontológico, observador), 02-02 (epistemología general), 02-04 (asimetría), 02-05 (tiempo y causalidad), 02-06 (ética), 03-01 (aparato), 06-01 (cierre).
- Auditoría V5: `Auditoria_V5_Vacios_Estructurales.md`.
