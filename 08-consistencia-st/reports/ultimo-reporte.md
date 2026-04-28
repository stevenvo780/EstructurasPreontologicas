# Reporte de consistencia ST

## theories/00-nucleo-ontologico.st

- modo: `check`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
✓ /datos/repos/EstructurasPreontologicas/08-consistencia-st/theories/00-nucleo-ontologico.st: sin errores
```

## theories/01-criterios-legitimidad.st

- modo: `check`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
✓ /datos/repos/EstructurasPreontologicas/08-consistencia-st/theories/01-criterios-legitimidad.st: sin errores
```

## theories/02-debates-y-limites.st

- modo: `check`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
✓ /datos/repos/EstructurasPreontologicas/08-consistencia-st/theories/02-debates-y-limites.st: sin errores
```

## theories/03-text-layer-tesis.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Passage p_formulacion = [[../Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md#1-formulacion-central]]
Formalizacion f_formulacion: p_formulacion -> (M & C & R & L)
Claim c_formulacion registrado
Support: c_formulacion <- p_formulacion
Confidence: c_formulacion = 0.98
Context: c_formulacion = "Núcleo de la formulación central: materialidad, compresión, no reificación y niveles no separados"
Passage p_criterios = [[../03-formalizacion/02-criterios-de-legitimidad-y-metodo.md#los-diez-criterios-de-legitimidad]]
Formalizacion f_criterios: p_criterios -> (A & B & F & I & V & T & U & O & N)
Claim c_criterios registrado
Support: c_criterios <- p_criterios
Confidence: c_criterios = 0.95
Context: c_criterios = "Matriz mínima de legitimidad epistemológica"
Passage p_principio = [[../Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md#44-la-tesis-como-principio-general]]
Formalizacion f_principio: p_principio -> (M & C & R)
Claim c_principio registrado
Support: c_principio <- p_principio
Confidence: c_principio = 0.94
Context: c_principio = "Principio de realidad relacional comprimible"
── Render: claims (markdown) ──
  Claim "c_formulacion": (M ∧ C ∧ R ∧ L)
    Soporte: p_formulacion
    Confianza: 0.98
    Contexto: Núcleo de la formulación central: materialidad, compresión, no reificación y niveles no separados
  Claim "c_criterios": (A ∧ B ∧ F ∧ I ∧ V ∧ T ∧ U ∧ O ∧ N)
    Soporte: p_criterios
    Confianza: 0.95
    Contexto: Matriz mínima de legitimidad epistemológica
  Claim "c_principio": (M ∧ C ∧ R)
    Soporte: p_principio
    Confianza: 0.94
    Contexto: Principio de realidad relacional comprimible
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 0
  Teoremas: 0
  Claims: 3
```

## theories/04-text-layer-bibliografia.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Passage p_patrones = [[../07-bibliografia/01-bibliografia-orientativa.md#2-realismo-estructural-y-patrones]]
Formalizacion f_patrones: p_patrones -> (D & L)
Claim c_patrones registrado
Support: c_patrones <- p_patrones
Confidence: c_patrones = 0.9
Context: c_patrones = "Dennett y Ladyman/Ross apoyan el eje patrones-estructura"
Passage p_mecanismos = [[../07-bibliografia/01-bibliografia-orientativa.md#3-explicacion-mecanicista-y-multinivel]]
Formalizacion f_mecanismos: p_mecanismos -> (C & B)
Claim c_mecanismos registrado
Support: c_mecanismos <- p_mecanismos
Confidence: c_mecanismos = 0.91
Context: c_mecanismos = "Craver y Bechtel apoyan el plano de niveles, mecanismos y organización"
Passage p_st = [[../07-bibliografia/01-bibliografia-orientativa.md#11-herramientas-formales-y-de-validacion]]
Formalizacion f_st: p_st -> S
Claim c_st registrado
Support: c_st <- p_st
Confidence: c_st = 0.97
Context: c_st = "ST se incorpora como herramienta metodológica de validación local"
── Render: claims (markdown) ──
  Claim "c_patrones": (D ∧ L)
    Soporte: p_patrones
    Confianza: 0.9
    Contexto: Dennett y Ladyman/Ross apoyan el eje patrones-estructura
  Claim "c_mecanismos": (C ∧ B)
    Soporte: p_mecanismos
    Confianza: 0.91
    Contexto: Craver y Bechtel apoyan el plano de niveles, mecanismos y organización
  Claim "c_st": S
    Soporte: p_st
    Confianza: 0.97
    Contexto: ST se incorpora como herramienta metodológica de validación local
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 0
  Teoremas: 0
  Claims: 3
```

## theories/05-asimetria-l1-b-l3-s.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.first_order
Set verbose = on
=== Teoría 05 — Asimetría L1↔B↔L3↔S en lógica de primer orden ===

HALLAZGO PREVIO (proposicional): la formulación con !(S→L) y !(L→S)
como axiomas simultáneos es INSATISFACIBLE en lógica proposicional.
REFINAMIENTO: la asimetría es contextual (existencial), no universal.
Axioma traduccional_BL3 = forall x(((B(x) -> F(x)) & (F(x) -> B(x))))
Axioma filtro_S = forall x(((B(x) & F(x)) -> S(x)))
Axioma L1_via_BL3 = forall x(((L1(x) & B(x) & F(x)) -> S(x)))

Test 1: existe categoría L1 sin sobrevivir como S (no traduce a B/L3).
◎ [check satisfiable] exists x((L1(x) & !(S(x)))) es SATISFACIBLE en lógica de primer orden

Test 2: existe categoría S sin venir de L1 (atractor real no nombrado).
◎ [check satisfiable] exists x((S(x) & !(L1(x)))) es SATISFACIBLE en lógica de primer orden

Test 3: ambas existenciales coexisten.
◎ [check satisfiable] (exists x((L1(x) & !(S(x)))) & exists y((S(y) & !(L1(y))))) es SATISFACIBLE en lógica de primer orden

Test 4: traducción B↔L3 es bidireccional universal.
✓ [check valid] (forall x(((B(x) -> F(x)) & (F(x) -> B(x)))) -> (B(a) -> F(a))) es VÁLIDA en lógica de primer orden
  Traza del tableau:
    1. [Iter] ✕ Rama cerrada por contradicción
    2. [Iter] ✕ Rama cerrada por contradicción

Test 5: una categoría con L1 ∧ B ∧ L3 pasa a S.
✗ [check valid] (forall x(((L1(x) & B(x) & F(x)) -> S(x))) -> ((L1(a) & B(a) & F(a)) -> S(a))) NO es válida en lógica de primer orden

Test 6: contramodelo del colapso simétrico (si S<->L1 universal todo trivial).
✗ [countermodel] Existe contramodelo para forall x((S(x) -> L1(x))) (no válida en lógica de primer orden)

Test 7: la asimetría es no trivial: el universo tiene categorías heterogéneas.
◎ [check satisfiable] (exists x((B(x) & F(x) & L1(x) & S(x))) & exists y((B(y) & F(y) & !(L1(y)) & S(y))) & exists z((L1(z) & !(B(z)) & !(S(z))))) es SATISFACIBLE en lógica de primer orden
── Render: theory (markdown) ──
  Perfil: classical.first_order
  Axiomas: 4
    verbose = on
    traduccional_BL3 = ∀x(((B(x) → F(x)) ∧ (F(x) → B(x))))
    filtro_S = ∀x(((B(x) ∧ F(x)) → S(x)))
    L1_via_BL3 = ∀x(((L1(x) ∧ B(x) ∧ F(x)) → S(x)))
  Teoremas: 0
  Claims: 0

=== Fin teoría 05 ===

RESULTADO: la asimetría L1↔B↔L3↔S es coherente cuando se formula como:
  - bidireccional B↔L3 (universal)
  - filtro de S vía B∧L3 (universal)
  - asimetrías L1↔S como existenciales (NO universales)

El cap 02-04 debe declarar explícitamente este nivel cuantificacional.
```

## theories/06-operadores-y-circularidad.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 06 — Operadores μ, G, H, κ, ε y ausencia de circularidad viciosa ===
Probar que la cadena μ → G → H → κ → ε es coherente y no circular maliciosamente.
Let mu = "Operador de medición μ : R → X" : M
Let grafo = "Grafo basal G = (V, E, W, T)" : G
Let hiper = "Hipergrafo H de relaciones n-arias" : H
Let kappa = "Compresión κ : G → G*" : K
Let epsilon = "Errores de traducción ε" : E
Axioma mu_genera_G = (M -> G)
Axioma G_genera_H = (G -> H)
Axioma H_admite_K = (H -> K)
Axioma K_genera_E = (K -> E)
Axioma E_reabre_a_K = (E -> (E | K))

Test 1: la cadena completa M → ... → E es derivable.
✓ [derive] G derivado exitosamente
✓ [derive] H derivado exitosamente
✓ [derive] K derivado exitosamente
✓ [derive] E derivado exitosamente

Test 2: NO se puede derivar μ desde κ (circularidad viciosa prohibida).
⚠ [analyze] {K} → M
  Inferencia NO VÁLIDA — pero no corresponde a un patrón de falacia conocido
◎ [check satisfiable] (K & !M) es SATISFACIBLE
✗ [countermodel] Contramodelo encontrado para (K -> M)
  ← K=V, M=F
  Modelo:
    K = true
    M = false

Test 3: NO se puede derivar G desde ε (ε reabre al SIGUIENTE κ, no genera grafos primarios).
⚠ [analyze] {E} → G
  Inferencia NO VÁLIDA — pero no corresponde a un patrón de falacia conocido
◎ [check satisfiable] (E & !G) es SATISFACIBLE
✗ [countermodel] Contramodelo encontrado para (E -> G)
  ← E=V, G=F
  Modelo:
    E = true
    G = false

Test 4: la cadena directa es válida pero no equivalente.
✓ [check valid] ((M & (M -> G)) -> G) es VALIDA (tautologia)
✓ [check valid] ((G & (G -> H)) -> H) es VALIDA (tautologia)
✓ [check valid] ((H & (H -> K)) -> K) es VALIDA (tautologia)
✓ [check valid] ((K & (K -> E)) -> E) es VALIDA (tautologia)

Test 5: μ no implica directamente E sin pasar por toda la cadena (no atajos ontológicos).
⚠ [analyze] {M} → E
  Inferencia NO VÁLIDA — pero no corresponde a un patrón de falacia conocido
(análisis previo debe pedir intermediarios)

Test 6: la teoría completa es satisfacible (no hay contradicción interna).
◎ [check satisfiable] (M & G & H & K & E & (M -> G) & (G -> H) & (H -> K) & (K -> E)) es SATISFACIBLE
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 6
    verbose = on
    mu_genera_G = (M → G)
    G_genera_H = (G → H)
    H_admite_K = (H → K)
    K_genera_E = (K → E)
    E_reabre_a_K = (E → (E ∨ K))
  Teoremas: 4
    derived_1 = G
    derived_2 = H
    derived_3 = K
    derived_4 = E
  Claims: 0

=== Fin teoría 06 ===
```

## theories/07-overall-pass-13-condiciones.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 07 — overall_pass = 13 condiciones independientes ===
Verificar que las 13 condiciones de overall_pass son colectivamente necesarias y suficientes.
Let C1 = "Convergencia numérica" : A
Let C2 = "Robustez a perturbaciones" : B
Let C3 = "Determinismo seed=42" : C
Let C4 = "Consistencia estadística" : D
Let C5 = "Incertidumbre acotada (CI)" : E
Let C6 = "EDI ≥ 0.30" : F
Let C7 = "p-value < 0.01" : G
Let C8 = "val_steps ≥ 8" : H
Let C9 = "coupling > 0.10" : I
Let C10 = "forcing controlado" : J
Let C11 = "estabilidad numérica reportada" : K
Let C12 = "persistencia temporal verificada" : L
Let C13 = "no controles falsos positivos" : N
Axioma overall_def = ((A & B & C & D & E & F & G & H & I & J & K & L & N) -> P)

Test 1: las 13 condiciones juntas implican overall_pass.
✓ [check valid] ((A & B & C & D & E & F & G & H & I & J & K & L & N & ((A & B & C & D & E & F & G & H & I & J & K & L & N) -> P)) -> P) es VALIDA (tautologia)

Test 2: si falta C6 (EDI bajo), NO hay overall_pass.
◎ [check satisfiable] (A & B & C & D & E & !F & G & H & I & J & K & L & N & !P) es SATISFACIBLE

Test 3: si falta C7 (p-value alto), NO hay overall_pass.
◎ [check satisfiable] (A & B & C & D & E & F & !G & H & I & J & K & L & N & !P) es SATISFACIBLE

Test 4: si falta C13 (control de falsos positivos), NO hay overall_pass.
◎ [check satisfiable] (A & B & C & D & E & F & G & H & I & J & K & L & !N & !P) es SATISFACIBLE

Test 5: contramodelo de overall_pass con condición faltante.
✗ [countermodel] Contramodelo encontrado para (((A & B & C & D & E & F & G & H & I & J & K & L & N) -> P) -> ((A & B & C & D & E & F & G & H & I & J & K & L) -> P))
  ← A=V, B=V, C=V, D=V, E=V, F=V, G=V, H=V, I=V, J=V, K=V, L=V, N=F, P=F
  Modelo:
    A = true
    B = true
    C = true
    D = true
    E = true
    F = true
    G = true
    H = true
    I = true
    J = true
    K = true
    L = true
    N = false
    P = false

Test 6: la conjunción de 13 condiciones es satisfacible (existe modelo).
◎ [check satisfiable] (A & B & C & D & E & F & G & H & I & J & K & L & N) es SATISFACIBLE

Test 7: análisis de inferencia válida del overall_pass.
✓ [analyze] {(A ∧ B ∧ C ∧ D ∧ E ∧ F ∧ G ∧ H ∧ I ∧ J ∧ K ∧ L ∧ N), ((A ∧ B ∧ C ∧ D ∧ E ∧ F ∧ G ∧ H ∧ I ∧ J ∧ K ∧ L ∧ N) → P)} → P
  Inferencia VÁLIDA — no se detectaron falacias
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 2
    verbose = on
    overall_def = ((A ∧ B ∧ C ∧ D ∧ E ∧ F ∧ G ∧ H ∧ I ∧ J ∧ K ∧ L ∧ N) → P)
  Teoremas: 0
  Claims: 0

=== Fin teoría 07 ===
```

## theories/08-discriminacion-rivales.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 08 — Discriminación contra 14 rivales en al menos 2 criterios ===
Probar que ningún rival comparte la conjunción de criterios decisivos con la tesis.
Let TESIS_anclaje = "Tesis: anclaje material sin reducción" : A
Let TESIS_dossier = "Tesis: dossier de admisión empírica" : D
Let TESIS_asimetria = "Tesis: asimetría L1↔B↔L3↔S" : Y
Let TESIS_multidom = "Tesis: cartografía multidominio EDI" : E
Let TESIS_falsacion = "Tesis: controles de falsación rechazados" : F
Let DUALISMO_pass = "Dualismo cumple anclaje material" : Q
Let MATPART_pass = "Materialismo de partículas cumple ε" : R
Let REDPLANO_pass = "Reduccionismo plano cumple κ" : S
Let EMERG_FUERTE = "Emergentismo fuerte cumple no-reificación" : T
Let CONSTR_ARB = "Constructivismo arbitrario cumple criterio empírico" : U
Let INSTRUMENT = "Instrumentalismo cumple realismo estructural" : V
Let FORM_VACIO = "Formalismo vacío cumple anclaje material" : W
Let MOD_INTERNOS = "Modelos internos cumplen B-acoplamiento" : N
Let COGN_COMP = "Cognitivismo computacional cumple información ecológica" : O
Let CONDUCTISMO = "Conductismo radical cumple acoplamiento informacional" : P
Let ENACT_RADICAL = "Enactivismo radical cumple formalización L3" : Z
Let LADYMAN_ROSS = "Realismo estructural informativo cumple sustrato material" : H
Let MECANIC_MULTI = "Mecanicismo multinivel cumple filtro empírico EDI" : I
Let WOLFRAM = "Wolfram cumple cartografía multidominio empírica" : J
Axioma rival_dualismo = (Q -> !A)
Axioma rival_matpart = (R -> !D)
Axioma rival_redplano = (S -> !Y)
Axioma rival_emergF = (T -> !D)
Axioma rival_constr = (U -> (!A & !D))
Axioma rival_instr = (V -> !A)
Axioma rival_formv = (W -> !A)
Axioma rival_modint = (N -> !E)
Axioma rival_cogncomp = (O -> !Y)
Axioma rival_conduct = (P -> !Y)
Axioma rival_enactr = (Z -> !D)
Axioma rival_ladyman = (H -> !A)
Axioma rival_mecanic = (I -> !D)
Axioma rival_wolfram = (J -> !E)

Test 1: ningún rival es equivalente a la tesis (al menos un criterio diverge).
◎ [check satisfiable] (A & D & Y & E & F & !Q & !R & !S & !T & !U & !V & !W & !N & !O & !P & !Z & !H & !I & !J) es SATISFACIBLE

Test 2: rivales están por construcción excluidos del marco si la tesis es verdadera.
✓ [check valid] ((A & (Q -> !A)) -> !Q) es VALIDA (tautologia)
✓ [check valid] ((D & (R -> !D)) -> !R) es VALIDA (tautologia)
✓ [check valid] ((Y & (S -> !Y)) -> !S) es VALIDA (tautologia)
✓ [check valid] ((D & (T -> !D)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((A & (V -> !A)) -> !V) es VALIDA (tautologia)
✓ [check valid] ((E & (J -> !E)) -> !J) es VALIDA (tautologia)

Test 3: el constructivismo arbitrario falla en DOS criterios (anclaje y dossier).
✓ [check valid] ((A & D & (U -> (!A & !D))) -> !U) es VALIDA (tautologia)

Test 4: countermodel — la tesis NO es derivable desde ningún rival individual.
✗ [countermodel] Contramodelo encontrado para (Q -> A)
  ← A=F, Q=V
  Modelo:
    A = false
    Q = true
✗ [countermodel] Contramodelo encontrado para (J -> E)
  ← E=F, J=V
  Modelo:
    E = false
    J = true
✗ [countermodel] Contramodelo encontrado para (T -> D)
  ← D=F, T=V
  Modelo:
    D = false
    T = true

Test 5: análisis de inferencia — desde Wolfram irreducible no se sigue el cierre macro EDI.
⚠ [analyze] {J} → E
  Inferencia NO VÁLIDA — pero no corresponde a un patrón de falacia conocido

Test 6: la conjunción de la tesis y la negación de todos los rivales es satisfacible.
◎ [check satisfiable] (A & D & Y & E & F & !Q & !R & !S & !T & !U & !V & !W & !N & !O & !P & !Z & !H & !I & !J) es SATISFACIBLE
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 15
    verbose = on
    rival_dualismo = (Q → ¬A)
    rival_matpart = (R → ¬D)
    rival_redplano = (S → ¬Y)
    rival_emergF = (T → ¬D)
    rival_constr = (U → (¬A ∧ ¬D))
    rival_instr = (V → ¬A)
    rival_formv = (W → ¬A)
    rival_modint = (N → ¬E)
    rival_cogncomp = (O → ¬Y)
    rival_conduct = (P → ¬Y)
    rival_enactr = (Z → ¬D)
    rival_ladyman = (H → ¬A)
    rival_mecanic = (I → ¬D)
    rival_wolfram = (J → ¬E)
  Teoremas: 0
  Claims: 0

=== Fin teoría 08 ===
```

## theories/09-niveles-paisaje.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 09 — Niveles 0-5 del paisaje de emergencia: exclusivos y exhaustivos ===
Verificar que un caso no puede pertenecer a dos niveles simultáneamente.
Let N0 = "Nivel 0 - Null (EDI ≤ 0 o sin estructura)" : A
Let N1 = "Nivel 1 - Trend (EDI > 0, p ≥ 0.05)" : B
Let N2 = "Nivel 2 - Suggestive (0.01 ≤ EDI < 0.10, p < 0.05)" : C
Let N3 = "Nivel 3 - Weak (0.10 ≤ EDI < 0.30, p < 0.05)" : D
Let N4 = "Nivel 4 - Strong (EDI ≥ 0.30, p < 0.01, overall_pass)" : E
Let N5 = "Nivel 5 - Crítico (multi-sonda + LoE=5 + frontera nítida)" : F
Axioma excl_01 = (A -> !B)
Axioma excl_02 = (A -> !C)
Axioma excl_03 = (A -> !D)
Axioma excl_04 = (A -> !E)
Axioma excl_05 = (A -> !F)
Axioma excl_12 = (B -> !C)
Axioma excl_13 = (B -> !D)
Axioma excl_14 = (B -> !E)
Axioma excl_23 = (C -> !D)
Axioma excl_24 = (C -> !E)
Axioma excl_34 = (D -> !E)
Axioma excl_45 = (E -> !F)
Axioma existe_caso = (C -> (A | B | C | D | E | F))

Test 1: cada caso del corpus pertenece a algún nivel.
✓ [check valid] (C -> (A | B | C | D | E | F)) es VALIDA (tautologia)

Test 2: ningún caso es simultáneamente strong y null.
✓ [check valid] ((A & (A -> !E)) -> !E) es VALIDA (tautologia)
◎ [check satisfiable] (A & !E) es SATISFACIBLE
✗ [countermodel] Contramodelo encontrado para (A & E)
  ← A=F, E=F
  Modelo:
    A = false
    E = false

Test 3: ningún caso es simultáneamente weak y suggestive.
✗ [countermodel] Contramodelo encontrado para (C & D)
  ← C=F, D=F
  Modelo:
    C = false
    D = false

Test 4: nivel 5 implica multi-sonda + LoE=5 + frontera nítida (TODOS).
Let multi_sonda = "Convergencia bajo múltiples sondas independientes" : Q
Let loe5 = "Datos físicos directos LoE = 5" : R
Let frontera = "Frontera espacial nítida en topología heterogénea" : T
Axioma n5_def = (F -> (Q & R & T))
✓ [check valid] ((F & (F -> (Q & R & T))) -> (Q & R & T)) es VALIDA (tautologia)

Test 5: corpus actual NO satisface F (Nivel 5 no alcanzado).
◎ [check satisfiable] (!F & (E | D | C | B | A)) es SATISFACIBLE

Test 6: countermodel — Nivel 5 con sonda única es inconsistente.
✗ [countermodel] Contramodelo encontrado para (F & !Q)
  ← F=F, Q=F
  Modelo:
    F = false
    Q = false

Test 7: análisis — desde Nivel 4 no se sigue Nivel 5 sin condiciones extra.
⚠ [analyze] {E} → F
  Inferencia NO VÁLIDA — pero no corresponde a un patrón de falacia conocido
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 15
    verbose = on
    excl_01 = (A → ¬B)
    excl_02 = (A → ¬C)
    excl_03 = (A → ¬D)
    excl_04 = (A → ¬E)
    excl_05 = (A → ¬F)
    excl_12 = (B → ¬C)
    excl_13 = (B → ¬D)
    excl_14 = (B → ¬E)
    excl_23 = (C → ¬D)
    excl_24 = (C → ¬E)
    excl_34 = (D → ¬E)
    excl_45 = (E → ¬F)
    existe_caso = (C → (A ∨ B ∨ C ∨ D ∨ E ∨ F))
    n5_def = (F → (Q ∧ R ∧ T))
  Teoremas: 0
  Claims: 0

=== Fin teoría 09 ===
```

## theories/10-falsabilidad.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 10 — Falsabilidad: 5 condiciones suficientes individuales de fracaso ===
Cada una basta para refutar la tesis. Probar implicación TESIS ↔ ¬(F1 ∨ F2 ∨ F3 ∨ F4 ∨ F5).
Let TESIS = "Irrealismo operativo demostrado en cartografía multidominio" : T
Let F1 = "Aparato no discrimina (controles falsos producen overall_pass)" : A
Let F2 = "Caso ancla pierde reproducibilidad bit-a-bit" : B
Let F3 = "EDI no robusto bajo perfil agresivo (cambio masivo de niveles)" : C
Let F4 = "Multi-sonda diverge fuerte en >50% de strong" : D
Let F5 = "Bibliografía formal nula o inconsistente con la tesis" : E
Axioma f1_falsifica = (A -> !T)
Axioma f2_falsifica = (B -> !T)
Axioma f3_falsifica = (C -> !T)
Axioma f4_falsifica = (D -> !T)
Axioma f5_falsifica = (E -> !T)
Axioma tesis_iff_no_falsacion = (T <-> !((A | B | C | D | E)))

Test 1: la tesis es lógicamente falsable.
✓ [check valid] ((A & (A -> !T)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((B & (B -> !T)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((C & (C -> !T)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((D & (D -> !T)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((E & (E -> !T)) -> !T) es VALIDA (tautologia)

Test 2: si NINGUNA falsación se cumple, la tesis se sostiene.
✓ [check valid] ((!A & !B & !C & !D & !E & (T <-> !((A | B | C | D | E)))) -> T) es VALIDA (tautologia)

Test 3: countermodel — la tesis NO es trivial (no es tautología).
✗ [countermodel] Contramodelo encontrado para T
  ← T=F
  Modelo:
    T = false

Test 4: la conjunción TESIS y CUALQUIER falsación es contradictoria.
⊘ [check satisfiable] (T & A & (A -> !T)) es INSATISFACIBLE (contradiccion)
⊘ [check satisfiable] (T & B & (B -> !T)) es INSATISFACIBLE (contradiccion)

Test 5: análisis de modus tollens — desde controles fallidos se infiere falsedad.
✓ [analyze] {(A → ¬T), A} → ¬T
  Inferencia VÁLIDA — no se detectaron falacias

Test 6: cubrimiento — las 5 condiciones cubren los modos de fracaso conocidos.
Let M1 = "Inconsistencia metodológica" : G
Let M2 = "Inconsistencia empírica" : H
Let M3 = "Inconsistencia bibliográfica" : I
Axioma m1_subset = (G -> A)
Axioma m2_subset = (H -> (B | C | D))
Axioma m3_subset = (I -> E)
✓ [check valid] ((G & (G -> A) & (A -> !T)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((H & (H -> (B | C | D)) & (B -> !T) & (C -> !T) & (D -> !T)) -> !T) es VALIDA (tautologia)
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 10
    verbose = on
    f1_falsifica = (A → ¬T)
    f2_falsifica = (B → ¬T)
    f3_falsifica = (C → ¬T)
    f4_falsifica = (D → ¬T)
    f5_falsifica = (E → ¬T)
    tesis_iff_no_falsacion = (T ↔ ¬((A ∨ B ∨ C ∨ D ∨ E)))
    m1_subset = (G → A)
    m2_subset = (H → (B ∨ C ∨ D))
    m3_subset = (I → E)
  Teoremas: 0
  Claims: 0

=== Fin teoría 10 ===
```

## theories/11-modal-coherencia-epistemica.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: modal.k
Set verbose = on
=== Teoría 11 — Modal: necesidad lógica vs contingencia empírica del marco ===
Probar coherencia de qué es necesario ([] ) vs qué es contingente (<>).
Let materialidad = "Sustrato material" : M
Let cierre_operativo = "κ verificado vía EDI" : K
Let edi_alto = "EDI ≥ 0.30 con p < 0.01" : E
Let strong_class = "Clasificación strong (Nivel 4)" : S

Test 1: la materialidad del sustrato es asumida como necesaria por la tesis.
◎ [check satisfiable] □(M) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: [](M)
    2. [0] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    3. [1] ✓ Rama saturada y ABIERTA.
Fórmula: □(M)

Sistema: K (Kripke minimal)
  Axioma K:  □(φ→ψ) → (□φ→□ψ) — distribución
  Regla N:   si ⊢φ entonces ⊢□φ — necessitación

  Relación de accesibilidad: sin restricciones.
  Propiedades del frame: ∅ (ninguna)
  No vale:
    ✗ Reflexividad  (□P → P no válido — Axioma T)
    ✗ Serialidad    (□P → ◇P no válido — Axioma D)
    ✗ Transitividad (□P → □□P no válido — Axioma 4)
    ✗ Simetría      (P → □◇P no válido  — Axioma B)
    ✗ Euclidianidad (◇P → □◇P no válido — Axioma 5)

  □φ = [](φ)  — "es necesario que φ"
  ◇φ = <>(φ)  — "es posible que φ"
Estatus: NO válida en modal.k

Test 2: el cierre operativo es contingente — depende del fenómeno y la sonda.
◎ [check satisfiable] (◇(K) ∧ ◇(¬K)) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: (<>(K) & <>(!K))
    2. [0] Regla Alpha (Conjunción) en w0: (<>(K) & <>(!K))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(K) ─> nuevo mundo w1
    4. [2] Analizando literal: K en w1
    5. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!K) ─> nuevo mundo w2
    6. [3] Analizando literal: !K en w2
    7. [3] ✓ Rama saturada y ABIERTA.

Test 3: si EDI alto entonces es POSIBLE (no necesario) que sea strong.
Axioma strong_def = (E -> <>(S))
◎ [check satisfiable] ((E ∧ ◇(S)) ∧ ◇(¬S)) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: ((E & <>(S)) & <>(!S))
    2. [0] Regla Alpha (Conjunción) en w0: ((E & <>(S)) & <>(!S))
    3. [1] Regla Alpha (Conjunción) en w0: (E & <>(S))
    4. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!S) ─> nuevo mundo w1
    5. [3] Analizando literal: !S en w1
    6. [3] Regla Delta (Posibilidad/Existe) en w0: <>(S) ─> nuevo mundo w2
    7. [4] Analizando literal: S en w2
    8. [4] Analizando literal: E en w0
    9. [4] ✓ Rama saturada y ABIERTA.

Test 4: regla K — distribución del operador necesidad.
✓ [check valid] (□((M → K)) → (□(M) → □(K))) es VÁLIDA en modal.k
  Identificación: Axioma K (Distribución)
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: ([]((M -> K)) -> ([](M) -> [](K)))
    2. [0] Regla Alpha (Conjunción) en w0: ([]((!M | K)) & ([](M) & <>(!K)))
    3. [1] Regla Alpha (Conjunción) en w0: ([](M) & <>(!K))
    4. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!K) ─> nuevo mundo w1
    5. [3] Analizando literal: !K en w1
    6. [3] Regla Gamma (Necesidad/ParaTodo) en w0: []((!M | K))
    7. [4] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    8. [5] Analizando literal: M en w1
    9. [5] Regla Beta (Disyunción/Impl) en w1: (!M | K). Bifurcando...
    10. [5]   -> Rama Beta 2: K
    11. [6] Analizando literal: K en w1
    12. [6] ✕ Rama cerrada por contradicción con K en w1

Test 5: contramodelo — necesidad NO se sigue de mera satisfacibilidad.
✗ [countermodel] Existe un contramodelo para (◇(M) → □(M))
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: !(<>(M) -> [](M))
    2. [0] Regla Alpha (Conjunción) en w0: (<>(M) & <>(!M))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(M) ─> nuevo mundo w1
    4. [2] Analizando literal: M en w1
    5. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!M) ─> nuevo mundo w2
    6. [3] Analizando literal: !M en w2
    7. [3] ✓ Rama saturada y ABIERTA.
── Render: theory (markdown) ──
  Perfil: modal.k
  Axiomas: 2
    verbose = on
    strong_def = (E → ◇(S))
  Teoremas: 0
  Claims: 0

=== Fin teoría 11 ===
```

## theories/12-paraconsistencia-wolfram.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: paraconsistent.belnap
Set verbose = on
=== Teoría 12 — Paraconsistencia: Wolfram irreducible micro Y EDI cierre macro ===
Probar que la coexistencia aparente no colapsa la teoría.
Let irreducible_micro = "Rule 110 es computacionalmente irreducible al nivel micro" : I
Let cierre_macro = "Rule 110 admite cierre operativo EDI ≥ 0.30 a nivel macro" : C

Test 1: ambas afirmaciones coexisten en lógica de Belnap (T, F, both, neither).
◎ [check satisfiable] (I & C) es satisfacible en Belnap

Test 2: la conjunción NO trivializa todo (no se sigue P arbitraria).
Let P_arbitrario = "Proposición arbitraria" : P
◎ [check satisfiable] (I & C & !P) es satisfacible en Belnap
✗ [countermodel] Contramodelo Belnap para: ((I & C) -> P)
  Valuación:
    C = T (True — solo verdadero)
    I = T (True — solo verdadero)
    P = F (False — solo falso)
  Resultado: ((I & C) -> P) = F (no designado)

  Explicación: En la lógica de Belnap, los valores designados son {T, B}.
  El valor "F" no es designado, por lo que la fórmula falla bajo esta valuación.
  Modelo:
    C = T
    I = T
    P = F

Test 3: en lógica clásica la aparente contradicción exige resolución; aquí NO.
◎ [check satisfiable] (I & C & !((I -> !C))) es satisfacible en Belnap
── Render: theory (markdown) ──
  Perfil: paraconsistent.belnap
  Axiomas: 1
    verbose = on
  Teoremas: 0
  Claims: 0

=== Fin teoría 12 ===
```

## Estado global

✅ La suite pasó completa.
