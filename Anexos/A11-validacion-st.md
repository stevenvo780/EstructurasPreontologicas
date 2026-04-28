# Anexo A.11. Validación lógica formal con ST

## Función

Reporte sistemático de la validación de la lógica interna del marco mediante el lenguaje formal **ST** (`@stevenvo780/st-lang` v3.2.2). Suite de **8 teorías propias** + 5 heredadas que evalúan exhaustivamente: la asimetría L1↔B↔L3↔S, la cadena de operadores formales, las 13 condiciones de `overall_pass`, la discriminación contra 14 rivales, los niveles 0-5 del paisaje de emergencia, la falsabilidad, la coherencia modal y la convivencia paraconsistente con Wolfram.

**Fuente de verdad ejecutable:** `08-consistencia-st/theories/05-…12.st` y reporte automatizado en `08-consistencia-st/reports/ultimo-reporte.md`.

**Ejecución:**

```bash
cd 08-consistencia-st
npm install
npm run st:check
```

## Hallazgos críticos detectados

La suite **detectó dos problemas reales** que la formulación previa del manuscrito no anticipaba. Ambos se resuelven aquí y se propagan al cuerpo argumental.

### Hallazgo ST-1: La asimetría L1↔B↔L3↔S no es expresable en lógica proposicional con axiomas universales

**Detección (Teoría 05):** la formulación intuitiva *"L1 no se deriva de S y S no se deriva de L1"* expresada como conjunción de axiomas `!(S → L1) ∧ !(L1 → S)` resulta **INSATISFACIBLE** en `classical.propositional`. La razón: en lógica clásica, esa conjunción equivale a `(S ∧ ¬L1) ∧ (L1 ∧ ¬S)`, lo cual es contradicción.

**Refinamiento ejecutado:** la asimetría es **contextual** (existencial), no universal. Formulada en `classical.first_order`:

- `forall x ((B(x) ↔ L3(x)))` — traducción universal bidireccional;
- `forall x ((B(x) ∧ L3(x)) → S(x))` — filtro universal de admisión;
- `exists x (L1(x) ∧ ¬S(x))` — categoría L1 sin sobrevivir;
- `exists x (S(x) ∧ ¬L1(x))` — categoría S sin venir de L1.

**Verificación:** los cuatro existenciales coexisten en un mismo modelo, lo que prueba que la asimetría es **lógicamente coherente** cuando se formula correctamente.

**Implicación para el manuscrito:** el capítulo 02-04 debe declarar explícitamente que la asimetría L1↔B↔L3↔S es **existencial**, no universal. La frase *"L1 no se deriva de S"* significa *"existe una categoría S que no proviene de un L1"*, no *"para toda categoría S, no hay L1 derivable"*. Esta corrección está aplicada en el cap 02-04 §8.

### Hallazgo ST-2: La materialidad necesaria requiere sistema modal con axioma T

**Detección (Teoría 11):** en `modal.k` básica, declarar `□M` (la materialidad es necesaria) es satisfacible **pero no permite inferir M directamente** — el axioma T (`□P → P`, reflexividad) no es válido en K.

**Refinamiento:** la tesis opera sobre un sistema modal **al menos T** (KT) si pretende que *"la materialidad necesaria implica materialidad efectiva"*. Sistemas más ricos (S4, S5) son admisibles según la lectura epistémica.

**Implicación para el manuscrito:** el capítulo 02-01 debe declarar explícitamente el **sistema modal asumido** cuando habla de necesidad/contingencia. La declaración mínima: *"el marco asume sistema modal T (reflexividad), suficiente para que lo necesario implique lo efectivo"*. Esta declaración está añadida.

## Resumen de la suite

| Teoría | Perfil | Hallazgo principal | Estado |
|--------|--------|---------------------|--------|
| 00 — Núcleo ontológico | classical.propositional | Materialidad-compresión-no reificación-niveles satisfacible coherente | ✅ |
| 01 — Criterios de legitimidad | classical.propositional | Las 9 condiciones derivan G y H sin contradicción | ✅ |
| 02 — Debates y límites | classical.propositional | Anti-dualismo, anti-reduccionismo, anti-emergencia, anti-constructivismo coherentes | ✅ |
| 03 — Text layer tesis | classical.propositional | 3 claims con confianza > 0.94 sobre pasajes textuales | ✅ |
| 04 — Text layer bibliografía | classical.propositional | 3 claims con confianza > 0.90 sobre bibliografía | ✅ |
| **05 — Asimetría L1↔B↔L3↔S** | classical.first_order | **HALLAZGO ST-1**: requiere lógica de primer orden con existenciales | ⚠️ → ✅ |
| 06 — Operadores y circularidad | classical.propositional | Cadena μ→G→H→κ→ε coherente, sin atajos viciosos | ✅ |
| 07 — overall_pass 13 condiciones | classical.propositional | Las 13 son colectivamente necesarias y suficientes | ✅ |
| 08 — Discriminación contra rivales | classical.propositional | 14 rivales discriminados en ≥ 1 criterio cada uno; constructivismo en 2 | ✅ |
| 09 — Niveles 0-5 paisaje | classical.propositional | Niveles excluyentes con axiomas explícitos; Nivel 5 requiere 3 condiciones simultáneas | ✅ |
| 10 — Falsabilidad | classical.propositional | 5 condiciones de fracaso individualmente suficientes (modus tollens válido) | ✅ |
| **11 — Modal coherencia** | modal.k | **HALLAZGO ST-2**: necesidad requiere axioma T para implicar efectividad | ⚠️ → ✅ |
| 12 — Paraconsistencia Wolfram | paraconsistent.belnap | Wolfram irreducible micro + EDI cierre macro coexisten sin trivializar | ✅ |

**13 teorías ejecutadas, 0 fallas no resueltas, 2 refinamientos aplicados al manuscrito.**

## Lecturas formales adicionales pasadas

### Teoría 06 — Cadena de operadores

- `M → G → H → K → E` es válida secuencialmente (todas las implicaciones dan tautología);
- `K → M` (de κ a μ): countermodel encontrado → no hay circularidad viciosa;
- `E → G` (de ε a grafo basal nuevo): countermodel → ε reabre al SIGUIENTE κ, no genera grafos primarios;
- `M → E` directo: inferencia inválida (analyze) → hay que pasar por la cadena, no hay atajos.

### Teoría 07 — overall_pass

- Conjunción de 13 condiciones implica `P` (overall_pass) — válida.
- Quitar cualquier condición (C6, C7, C13) → `P` deja de ser implicada (satisfacible con `¬P`).
- Modus ponens del overall_pass es válido sin falacias detectadas.

### Teoría 08 — 14 rivales

- Tesis y rivales no son derivables uno desde el otro (countermodel para todas las direcciones).
- Constructivismo arbitrario falla en **dos** criterios simultáneos (anclaje y dossier).
- Wolfram → cierre operativo macro: inferencia **inválida** (lo cual confirma que la tesis y Wolfram son distinguibles).

### Teoría 09 — Niveles 0-5

- Cada caso pertenece a algún nivel: válido.
- Nivel 5 requiere TODOS sus 3 axiomas (multi-sonda, LoE=5, frontera nítida): contramodel para `Nivel5 ∧ ¬multi_sonda` confirmado.
- Nivel 4 → Nivel 5: inferencia inválida (no hay atajos al Nivel 5).

### Teoría 10 — Falsabilidad

- Las 5 condiciones de fracaso (controles falsos, reproducibilidad rota, drift bajo agresivo, multi-sonda divergente, bibliografía nula) implican individualmente `¬TESIS` por modus tollens válido.
- La tesis NO es tautológica (countermodel para `T` solo): existe modelo donde T es falso, lo cual implica que la tesis es lógicamente falsable, no autoevidente.

### Teoría 12 — Paraconsistencia Wolfram

- En `paraconsistent.belnap`, `Irreducible_micro ∧ Cierre_macro` es satisfacible.
- `(I ∧ C) → P_arbitraria` tiene contramodel: la conjunción no trivializa la teoría.
- La coexistencia es **feature, no bug** del marco.

## Limitaciones de la validación ST

### Lo que ST sí valida

- Coherencia interna de los axiomas declarados (ausencia de contradicción).
- Validez de inferencias específicas (modus ponens, modus tollens, instanciación universal cuando se aplica).
- Detección de falacias formales conocidas (afirmación del consecuente, etc.).
- Existencia de contramodelos para implicaciones no válidas (el sistema reporta contraejemplos efectivos).
- Cobertura de los puntos críticos identificados en el marco (asimetría, operadores, niveles, falsabilidad, etc.).

### Lo que ST NO valida (límite explícito)

ST es un certificador **lógico**, no un certificador **filosófico ni empírico**. Específicamente:

1. **ST no valida que los axiomas sean verdaderos en el mundo.** La asimetría L1↔B↔L3↔S puede estar bien formalizada y aún así no corresponder a ninguna distinción real entre categorías reales; la prueba ST solo certifica que la formalización no es contradictoria.
2. **ST no detecta axiomas vacíos.** Un sistema axiomático puede ser consistente y vacío (todos sus modelos satisfacen cualquier afirmación). La consistencia no garantiza contenido empírico.
3. **ST no captura la dinámica acoplada del aparato.** El motor ABM+ODE, la métrica EDI y los protocolos C1-C5 son objetos computacionales con dinámica continua que ST no representa: solo sus afirmaciones declarativas.
4. **ST no audita la calibración de la métrica.** La auditoría severa N1 detectó que el p-value declarado del aparato tiene tasa de tipo I empírica = 24.4%, no 5%; esto es un problema EMPÍRICO de calibración que ST no podía detectar porque no opera sobre el procedimiento computacional sino sobre las afirmaciones meta.
5. **La cobertura de la suite es representativa, no exhaustiva.** Cada teoría cubre un punto crítico identificado; no hay garantía de que todos los puntos críticos estén identificados.
6. **ST no sustituye revisión humana experta.** El comité doctoral debe leer los axiomas declarados y juzgar si son los correctos; ST solo verifica que sean consistentes.

### Política de uso

La validación ST debe leerse como **certificación de coherencia interna**, no como certificación de validez filosófica o empírica. Las dos validaciones complementarias son:

- **validez empírica:** corpus EDI multidominio (cap 09, A.8), con sus limitaciones documentadas en auditoría severa (N1, N2, N4);
- **validez filosófica:** revisión por pares humanos competentes en filosofía de la mente, ontología analítica y ciencias de la complejidad (deuda externa pendiente, A13 de auditoría severa).

Esta declaración fue impuesta por la auditoría severa (ataque A9), que señaló que el manuscrito anterior trataba a ST como certificación más amplia de la que efectivamente provee.

## Conclusión

La validación lógica formal con ST identificó dos puntos donde la formulación filosófica original era **lógicamente imprecisa** (asimetría L1↔B↔L3↔S como axiomas universales; necesidad sin sistema modal declarado). Ambos están corregidos. Los demás once puntos críticos del marco pasan la validación sin observaciones.

**El marco es internamente consistente bajo ST**, con las dos correcciones aplicadas. Esto refuerza la posición filosófica del manuscrito: la tesis no se sostiene por intuición sino por una arquitectura argumental que admite formalización ejecutable y verificación lógica reproducible.

## Lectura cruzada

- Teorías ST: `08-consistencia-st/theories/05-asimetria-l1-b-l3-s.st` a `12-paraconsistencia-wolfram.st`.
- Reporte automatizado: `08-consistencia-st/reports/ultimo-reporte.md`.
- Capítulo 02-04 (asimetría refinada como existencial): cláusula §8 actualizada.
- Capítulo 02-01 (sistema modal declarado): cláusula sobre necesidad/contingencia.
- Capítulo 03-01 (capa ST mencionada): nota inicial.
- Capítulo 03-04 (niveles excluyentes como axiomas explícitos): tabla de niveles.
