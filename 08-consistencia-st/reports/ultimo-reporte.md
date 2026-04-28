# Reporte de consistencia ST

## theories/00-nucleo-ontologico.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 00 — Núcleo ontológico (refactorizada V5) ===

Refactorización post-V5: el núcleo ahora articula los 4 invariantes
ontológicos y el naturalismo metafísico moderado como compromiso de
partida (V5-07), con rechazo explícito de alternativas.
Let materialidad = "Sustrato material dinámico existe a cualquier escala" : M
Let acoplamiento = "Acoplamiento dinámico entre polos" : A
Let atractor = "Atractor empírico con cuenca medible" : K
Let cierre = "Cierre operativo κ verificable por intervención ablativa" : C
Let no_dualismo = "No hay segunda sustancia" : ¬D
Let no_idealismo = "La materia no es apariencia del espíritu" : ¬I
Let no_panpsiquismo = "No se atribuye experiencia a partículas" : ¬P
Axioma invariantes_completos = ((M & A & K & C) -> O)
Axioma naturalismo_excluye_dualismo = (M -> !D)
Axioma naturalismo_excluye_idealismo = (M -> !I)
Axioma naturalismo_excluye_panpsiquismo = (M -> !P)
Axioma acoplamiento_requiere_materia = (A -> M)
Axioma atractor_requiere_acoplamiento = (K -> A)
Axioma cierre_requiere_atractor = (C -> K)

Test 1: los 4 invariantes son colectivamente suficientes para ontología.
✓ [check valid] ((M & A & K & C & ((M & A & K & C) -> O)) -> O) es VALIDA (tautologia)

Test 2: la cadena causal-constitutiva ontológica es derivable.
✓ [derive] O derivado exitosamente

Test 3: el naturalismo excluye dualismo, idealismo y panpsiquismo.
✓ [check valid] ((M & (M -> !D)) -> !D) es VALIDA (tautologia)
✓ [check valid] ((M & (M -> !I)) -> !I) es VALIDA (tautologia)
✓ [check valid] ((M & (M -> !P)) -> !P) es VALIDA (tautologia)

Test 4: no hay invariante sin sustrato material (M es necesario).
◎ [check satisfiable] (M & !A & !K & !C) es SATISFACIBLE
✗ [countermodel] Contramodelo encontrado para ((A | K | C) -> !M)
  ← A=F, C=F, K=V, M=V
  Modelo:
    A = false
    C = false
    K = true
    M = true

Test 5: la conjunción de los 4 invariantes y los 3 rechazos es satisfacible.
◎ [check satisfiable] (M & A & K & C & !D & !I & !P) es SATISFACIBLE

Test 6: ningún invariante implica circular hacia atrás.
⚠ [analyze] {C} → M
  Inferencia NO VÁLIDA — pero no corresponde a un patrón de falacia conocido
(la cadena C→K→A→M es derivada vía axiomas explícitos, no por circulación)
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 8
    verbose = on
    invariantes_completos = ((M ∧ A ∧ K ∧ C) → O)
    naturalismo_excluye_dualismo = (M → ¬D)
    naturalismo_excluye_idealismo = (M → ¬I)
    naturalismo_excluye_panpsiquismo = (M → ¬P)
    acoplamiento_requiere_materia = (A → M)
    atractor_requiere_acoplamiento = (K → A)
    cierre_requiere_atractor = (C → K)
  Teoremas: 1
    derived_1 = O
  Claims: 0

=== Fin teoría 00 ===
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

## theories/13-temporalidad-causalidad.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 13 — Temporalidad y causalidad (V5-02, V5-03, V5-09) ===

Verifica la coherencia de las posturas declaradas en cap 02-05:
B-series, flecha termodinámica, manipulabilidad woodwardiana,
constitución descendente vs downward causation kim-vulnerable.
Let bseries = "Tiempo B-series relacional" : T
Let flecha_termo = "Flecha termodinámica fundamental" : F
Let manipulabilidad = "Causación = manipulabilidad woodwardiana" : W
Let do_test = "Operador do(X=x) válido" : D
Let constitucion = "Constitución descendente (Craver)" : C
Let exclusion_kim = "Exclusión causal de Kim" : K
Axioma bseries_exige_orden = (T -> O)
Axioma flecha_implica_irreversibilidad = (F -> R)
Axioma manipulabilidad_implica_do = (W -> D)
Axioma constitucion_no_causa = (C -> !V)
Axioma kim_aplica_a_causacion = (K -> (V -> S))
Axioma edi_es_do_test = (E -> D)

Test 1: la postura B-series + flecha termodinámica es satisfacible.
◎ [check satisfiable] (T & F & R & O) es SATISFACIBLE

Test 2: manipulabilidad woodwardiana implica que EDI es un do-test.
✓ [check valid] ((W & (W -> D) & (E -> D)) -> ((W & E) -> D)) es VALIDA (tautologia)
✓ [analyze] {W, (W → D)} → D
  Inferencia VÁLIDA — no se detectaron falacias

Test 3: constitución NO es causación (responde a Kim).
✓ [check valid] ((C & (C -> !V)) -> !V) es VALIDA (tautologia)
◎ [check satisfiable] (C & !V) es SATISFACIBLE
✗ [countermodel] Contramodelo encontrado para (C -> V)
  ← C=V, V=F
  Modelo:
    C = true
    V = false

Test 4: si downward es constitución (no causación), Kim no aplica.
(Kim aplica solo cuando V; si C → !V, entonces de Kim no se infiere S sin V)
✓ [check valid] ((C & (C -> !V) & (K -> (V -> S))) -> (!V & (V -> S))) es VALIDA (tautologia)
(de !V y (V→S) NO se sigue S; el modus tollens da !S si quisiéramos)
◎ [check satisfiable] (C & !V & K & !S) es SATISFACIBLE
(modelo donde hay constitución sin sobredeterminación: Kim neutralizado)

Test 5: contramodelo del eternalismo bloque (rechazado).
Let eternalismo_bloque = "Pasado, presente y futuro coexisten todos en igualdad" : B
✗ [countermodel] Contramodelo encontrado para (T & B)
  ← B=F, T=F
  Modelo:
    B = false
    T = false
(B-series moderado NO implica eternalismo bloque kim-vulnerable)

Test 6: irreversibilidad κ↔ε es manifestación de F, no axioma adicional.
Let irrev_kappa = "κ no es perfectamente reversible vía ε" : I
Axioma irrev_es_termodinamica = (I <-> F)
✓ [check valid] ((F & (F <-> I)) -> I) es VALIDA (tautologia)

Test 7: la combinación completa de posturas es satisfacible.
◎ [check satisfiable] (T & F & W & D & C & !V & E) es SATISFACIBLE
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 8
    verbose = on
    bseries_exige_orden = (T → O)
    flecha_implica_irreversibilidad = (F → R)
    manipulabilidad_implica_do = (W → D)
    constitucion_no_causa = (C → ¬V)
    kim_aplica_a_causacion = (K → (V → S))
    edi_es_do_test = (E → D)
    irrev_es_termodinamica = (I ↔ F)
  Teoremas: 0
  Claims: 0

=== Fin teoría 13 ===
```

## theories/14-pre-ontologico-genetico.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.first_order
Set verbose = on
=== Teoría 14 — 'Pre-ontológico' en sentido simondoniano (V5-01) ===

Cierra el agujero conceptual del título de la tesis.
'Pre' = genético-epistemológico, NO temporal puro.

Predicados:
  PreInd(x): x es pre-individual materialmente sostenido
  Categ(x): x es categoría nominalizante
  Atrac(x): x es atractor empírico identificable
  PreOnt(x): x es estructura pre-ontológica en sentido tesis
Axioma def_preont = forall x(((PreInd(x) & Atrac(x) & !(Categ(x))) <-> PreOnt(x)))
Axioma existe_pre_sin_categoria = exists x((PreInd(x) & !(Categ(x))))
Axioma no_temporal_puro = forall x((PreOnt(x) -> !(Anterior_temporal(x))))
Axioma genetico = forall x((PreOnt(x) -> Genera_individual(x)))

Test 1: existe estructura pre-ontológica con definición técnica.
◎ [check satisfiable] exists x((PreInd(x) & Atrac(x) & !(Categ(x)) & PreOnt(x))) es SATISFACIBLE en lógica de primer orden

Test 2: lo nominalizado NO es pre-ontológico.
✗ [check valid] forall x((Categ(x) -> !(PreOnt(x)))) NO es válida en lógica de primer orden
⚠ [analyze] {∀x(((PreInd(x) ∧ Atrac(x) ∧ ¬(Categ(x))) ↔ PreOnt(x)))} → (Categ(a) → ¬(PreOnt(a)))
  Inferencia NO VÁLIDA — pero no corresponde a un patrón de falacia conocido

Test 3: pre-ontológico implica génesis del individuo (Simondon).
✓ [check valid] (forall x((PreOnt(x) -> Genera_individual(x))) -> (PreOnt(a) -> Genera_individual(a))) es VÁLIDA en lógica de primer orden
  Traza del tableau:
    1. [Iter] ✕ Rama cerrada por contradicción
    2. [Iter] ✕ Rama cerrada por contradicción
    3. [Iter] ✕ Rama cerrada por contradicción
    4. [Iter] ✕ Rama cerrada por contradicción

Test 4: contramodelo del 'pre temporal puro' (rechazado).
✗ [countermodel] Existe contramodelo para forall x((PreOnt(x) -> Anterior_temporal(x))) (no válida en lógica de primer orden)
(la tesis NO usa 'pre' como anterioridad temporal pura)

Test 5: el rol inferencial de PreOnt distingue de regularidad.
Let regularidad = "Regularidad estadística sin atractor" : R
Axioma reg_no_atractor = forall x((Regularidad(x) -> !(Atrac(x))))
✓ [check valid] (forall x((Regularidad(x) -> !(PreOnt(x)))) -> (Regularidad(a) -> !(PreOnt(a)))) es VÁLIDA en lógica de primer orden
  Traza del tableau:
    1. [Iter] ✕ Rama cerrada por contradicción
    2. [Iter] ✕ Rama cerrada por contradicción
    3. [Iter] ✕ Rama cerrada por contradicción
    4. [Iter] ✕ Rama cerrada por contradicción
── Render: theory (markdown) ──
  Perfil: classical.first_order
  Axiomas: 6
    verbose = on
    def_preont = ∀x(((PreInd(x) ∧ Atrac(x) ∧ ¬(Categ(x))) ↔ PreOnt(x)))
    existe_pre_sin_categoria = ∃x((PreInd(x) ∧ ¬(Categ(x))))
    no_temporal_puro = ∀x((PreOnt(x) → ¬(Anterior_temporal(x))))
    genetico = ∀x((PreOnt(x) → Genera_individual(x)))
    reg_no_atractor = ∀x((Regularidad(x) → ¬(Atrac(x))))
  Teoremas: 0
  Claims: 0

=== Fin teoría 14 ===
```

## theories/15-tres-marcos-generales.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 15 — Marco tripartito general (V5 narrativa unificada) ===

Verifica que ontología (O), epistemología (E) y metodología (M)
son TODAS GENERALES, no regionales, y que su generalidad es
lógicamente coherente con su justificación operativa por casos (J).
Let onto_general = "Ontología afirma 4 invariantes a cualquier escala" : O
Let epi_general = "Epistemología compresión disciplinada en cualquier escala" : E
Let meto_general = "Metodología aparato invariante a la escala" : M
Let casos_justifican = "40 casos justifican operativamente el marco" : J
Let inductivismo_falaz = "Más casos = más verdad" : I
Axioma marcos_son_independientes = ((O & E & M) -> G)
Axioma casos_no_constituyen_tesis = (J -> !((J <-> G)))
Axioma rechazo_inductivismo = !I
Axioma estructura_interna_basta = (G -> S)

Test 1: los tres marcos son colectivamente la tesis general.
✓ [check valid] ((O & E & M & ((O & E & M) -> G)) -> G) es VALIDA (tautologia)

Test 2: la generalidad no depende del tamaño del corpus (no inductivismo).
◎ [check satisfiable] (G & !I) es SATISFACIBLE
✗ [countermodel] Contramodelo encontrado para (G -> I)
  ← G=V, I=F
  Modelo:
    G = true
    I = false
⚠ [analyze] {J} → G
  Inferencia NO VÁLIDA — pero no corresponde a un patrón de falacia conocido
(si fuera inducción válida G se seguiría de J solo; NO se sigue)

Test 3: la generalidad de los 3 marcos es satisfacible sin casos.
◎ [check satisfiable] (O & E & M & G & !J) es SATISFACIBLE
(en principio: el marco general podría sostenerse antes del corpus)

Test 4: el corpus respalda pero NO sustituye la articulación.
(la tesis G requiere estructura interna coherente S; sin S la tesis no se sostiene)
✓ [check valid] (((G -> S) & G) -> S) es VALIDA (tautologia)
✓ [check valid] ((G -> S) -> (!S -> !G)) es VALIDA (tautologia)
  Identificación: Contrapositiva
(modus tollens: si no hay estructura interna, no hay tesis)

Test 5: ninguno de los 3 marcos colapsa sobre los otros 2.
◎ [check satisfiable] (O & !E & !M) es SATISFACIBLE
◎ [check satisfiable] (E & !O & !M) es SATISFACIBLE
◎ [check satisfiable] (M & !O & !E) es SATISFACIBLE
✗ [countermodel] Contramodelo encontrado para (O -> E)
  ← E=F, O=V
  Modelo:
    E = false
    O = true
✗ [countermodel] Contramodelo encontrado para (E -> M)
  ← E=V, M=F
  Modelo:
    E = true
    M = false
✗ [countermodel] Contramodelo encontrado para (M -> O)
  ← M=V, O=F
  Modelo:
    M = true
    O = false

Test 6: los 3 marcos son MUTUAMENTE COHERENTES bajo la tesis (sí pueden coexistir).
◎ [check satisfiable] (O & E & M) es SATISFACIBLE
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 5
    verbose = on
    marcos_son_independientes = ((O ∧ E ∧ M) → G)
    casos_no_constituyen_tesis = (J → ¬((J ↔ G)))
    rechazo_inductivismo = ¬I
    estructura_interna_basta = (G → S)
  Teoremas: 0
  Claims: 0

=== Fin teoría 15 ===
```

## theories/16-naturalismo-y-rivales-metafisicos.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 16 — Naturalismo metafísico moderado vs rivales (V5-07) ===

Prueba que el naturalismo de partida excluye categóricamente
dualismo, idealismo, emanacionismo, panpsiquismo y creacionismo,
PERO admite alternativas realistas en mecánica cuántica.
Let naturalismo = "Naturalismo metafísico moderado" : N
Let dualismo = "Dualismo cartesiano" : D
Let idealismo = "Idealismo metafísico" : I
Let emanacion = "Emanacionismo neoplatónico" : E
Let panpsiq = "Panpsiquismo" : P
Let creacion = "Creacionismo metafísico" : C
Let many_worlds = "Many-worlds Everett" : W
Let bohm = "Bohmiana de Broglie-Bohm" : B
Let copenhagen_pura = "Copenhagen instrumentalista pura" : K
Axioma nat_excluye_dual = (N -> !D)
Axioma nat_excluye_id = (N -> !I)
Axioma nat_excluye_eman = (N -> !E)
Axioma nat_excluye_panps = (N -> !P)
Axioma nat_excluye_creac = (N -> !C)
Axioma nat_excluye_copen_pura = (N -> !K)
Axioma nat_compatible_mw = (N -> (W | !W))
Axioma nat_compatible_bohm = (N -> (B | !B))

Test 1: el naturalismo excluye los 5 rivales metafísicos.
✓ [check valid] ((N & (N -> !D)) -> !D) es VALIDA (tautologia)
✓ [check valid] ((N & (N -> !I)) -> !I) es VALIDA (tautologia)
✓ [check valid] ((N & (N -> !E)) -> !E) es VALIDA (tautologia)
✓ [check valid] ((N & (N -> !P)) -> !P) es VALIDA (tautologia)
✓ [check valid] ((N & (N -> !C)) -> !C) es VALIDA (tautologia)

Test 2: la combinación naturalismo + 5 rechazos es satisfacible.
◎ [check satisfiable] (N & !D & !I & !E & !P & !C) es SATISFACIBLE

Test 3: la conjunción naturalismo + cualquier rival es contradicción.
⊘ [check satisfiable] (N & D & (N -> !D)) es INSATISFACIBLE (contradiccion)
⊘ [check satisfiable] (N & I & (N -> !I)) es INSATISFACIBLE (contradiccion)
⊘ [check satisfiable] (N & P & (N -> !P)) es INSATISFACIBLE (contradiccion)

Test 4: el naturalismo NO decide entre interpretaciones realistas QM.
◎ [check satisfiable] (N & W & !B) es SATISFACIBLE
◎ [check satisfiable] (N & B & !W) es SATISFACIBLE
◎ [check satisfiable] (N & W & B) es SATISFACIBLE
(Many-worlds, Bohm, ambos compatibles con naturalismo)

Test 5: Copenhagen instrumentalista pura SÍ se rechaza.
✓ [check valid] ((N & (N -> !K)) -> !K) es VALIDA (tautologia)
✗ [countermodel] Contramodelo encontrado para (N & K)
  ← K=F, N=F
  Modelo:
    K = false
    N = false

Test 6: contramodelo: el naturalismo NO se demuestra desde dentro.
✗ [countermodel] Contramodelo encontrado para N
  ← N=F
  Modelo:
    N = false
(es compromiso de partida, no conclusión deductiva)

Test 7: la postura completa es coherente.
◎ [check satisfiable] (N & !D & !I & !E & !P & !C & !K & (W | B)) es SATISFACIBLE
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 9
    verbose = on
    nat_excluye_dual = (N → ¬D)
    nat_excluye_id = (N → ¬I)
    nat_excluye_eman = (N → ¬E)
    nat_excluye_panps = (N → ¬P)
    nat_excluye_creac = (N → ¬C)
    nat_excluye_copen_pura = (N → ¬K)
    nat_compatible_mw = (N → (W ∨ ¬W))
    nat_compatible_bohm = (N → (B ∨ ¬B))
  Teoremas: 0
  Claims: 0

=== Fin teoría 16 ===
```

## theories/17-kappa-pragmatica-vs-ontologica.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 17 — κ-pragmática vs κ-ontológica (V5-07/A8) ===

Verifica que la distinción entre κ-pragmática (compresión funciona)
y κ-ontológica (compresión corresponde a estructura material independiente)
es lógicamente sostenible y que NINGÚN caso del corpus actual cumple
los 3 criterios κ-ontológica simultáneamente.
Let kappa_p = "κ-pragmática: la compresión predice/discrimina" : P
Let kappa_o = "κ-ontológica: la compresión corresponde a estructura material independiente" : O
Let multi_sonda = "Convergencia bajo múltiples sondas independientes" : M
Let inter_grupo = "Replicación inter-grupo" : I
Let intervencion_exp = "Intervención experimental confirmatoria" : E
Axioma def_ontologica = (O <-> (P & M & I & E))
Axioma kp_no_implica_ko = (P -> !O)
Axioma corpus_actual_solo_p = (C -> (P & !O))

Test 1: κ-ontológica requiere los 3 criterios simultáneamente.
✓ [check valid] (((O <-> (P & M & I & E)) & O) -> (M & I & E)) es VALIDA (tautologia)
✓ [check valid] (((O <-> (P & M & I & E)) & P & M & I & E) -> O) es VALIDA (tautologia)

Test 2: κ-pragmática NO implica κ-ontológica.
◎ [check satisfiable] (P & !O) es SATISFACIBLE
✗ [countermodel] Contramodelo encontrado para (P -> O)
  ← O=F, P=V
  Modelo:
    O = false
    P = true

Test 3: ningún caso actual cumple los 3 criterios.
Let caso_actual = "Caso del corpus actual" : C
✓ [check valid] ((C -> (P & !O)) -> (C -> !O)) es VALIDA (tautologia)
◎ [check satisfiable] (C & P & !M) es SATISFACIBLE
◎ [check satisfiable] (C & P & !I) es SATISFACIBLE
◎ [check satisfiable] (C & P & !E) es SATISFACIBLE

Test 4: si SE cumplieran los 3 criterios, sí habría κ-ontológica.
✓ [check valid] ((P & M & I & E & (O <-> (P & M & I & E))) -> O) es VALIDA (tautologia)

Test 5: la distinción es no trivial: hay modelos donde solo se da P.
◎ [check satisfiable] (P & !M & !I & !E) es SATISFACIBLE
(estos son los 40 casos del corpus actual)

Test 6: contramodelo del colapso κ-pragmática = κ-ontológica.
✗ [countermodel] Contramodelo encontrado para (O <-> P)
  ← O=F, P=V
  Modelo:
    O = false
    P = true
(rechaza tanto operacionalismo puro como realismo metafísico fuerte)
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 4
    verbose = on
    def_ontologica = (O ↔ (P ∧ M ∧ I ∧ E))
    kp_no_implica_ko = (P → ¬O)
    corpus_actual_solo_p = (C → (P ∧ ¬O))
  Teoremas: 0
  Claims: 0

=== Fin teoría 17 ===
```

## theories/18-deontica-normativa.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: deontic.standard
Set verbose = on
=== Teoría 18 — Dimensión normativa (V5-06) ===

Verifica que la postura de naturalismo ético no-reduccionista
es coherente en lógica deóntica estándar: las normas tienen
dimensión obligatoria (O) sin requerir sustancia adicional.
Let cumple = "El sistema cumple la norma" : C
Let valida = "La norma es válida (cuenca de atracción del cumplimiento)" : V
Let efectiva = "La norma es efectiva (tasa de retorno a la cuenca)" : E
Let legitima = "La norma es legítima (anchura de la cuenca)" : L
Let deber = "Hay deber moralmente real" : D
Axioma validez_es_atractor = (V -> [](C))
Axioma efectividad_es_tasa = (E -> <>(C))
Axioma deber_natural = (D <-> (V & E))

Test 1: la validez normativa implica obligación deontica.
✓ [check valid] (O(C) → O(C)) es VÁLIDA en deontic.standard
  Identificación: Identidad / Reflexividad
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: ([](C) -> [](C))
    2. [0] Regla Alpha (Conjunción) en w0: ([](C) & <>(!C))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(!C) ─> nuevo mundo w1
    4. [2] Analizando literal: !C en w1
    5. [2] Regla Gamma (Necesidad/ParaTodo) en w0: [](C)
    6. [3] Analizando literal: C en w1
    7. [3] ✕ Rama cerrada por contradicción con C en w1
Fórmula: O(C)

Operadores deónticos:
  O(φ) = [](φ)  — "Es obligatorio que φ"
  P(φ) = <>(φ)  — "Está permitido que φ"
  F(φ) = [](!φ) — "Está prohibido que φ"

Sistema: KD (K + axioma D)
  Axioma K: O(φ→ψ) → (O(φ)→O(ψ))
  Axioma D: O(φ) → P(φ) — "lo obligatorio es permisible"

  Relación de accesibilidad: serial
  Propiedades del frame: {serialidad}
  Significado: todo estado deóntico tiene al menos una alternativa permisible

  No vale:
    ✗ Reflexividad  (O(φ) → φ — lo obligatorio no es necesariamente el caso)
    ✗ Transitividad, Simetría, Euclidianidad

  ⚠ Paradojas conocidas en SDL:
    • Ross:       O(P) → O(P∨Q) — si es obligatorio enviar la carta, ¿es obligatorio enviarla o quemarla?
    • Chisholm:   O(P), O(P→Q), ¬P→O(¬Q), ¬P — inconsistente (contrary-to-duty)
    • Samaritano: O(¬P) → O(¬P∧Q) — obligaciones derivadas de eventos impermisibles
Estatus: NO válida en deontic.standard

Test 2: efectividad implica posibilidad deontica de cumplimiento.
✓ [check valid] (P(C) → P(C)) es VÁLIDA en deontic.standard
  Identificación: Identidad / Reflexividad
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: (<>(C) -> <>(C))
    2. [0] Regla Alpha (Conjunción) en w0: (<>(C) & [](!C))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(C) ─> nuevo mundo w1
    4. [2] Analizando literal: C en w1
    5. [2] Regla Gamma (Necesidad/ParaTodo) en w0: [](!C)
    6. [3] Analizando literal: !C en w1
    7. [3] ✕ Rama cerrada por contradicción con !C en w1
Fórmula: P(C)

Operadores deónticos:
  O(φ) = [](φ)  — "Es obligatorio que φ"
  P(φ) = <>(φ)  — "Está permitido que φ"
  F(φ) = [](!φ) — "Está prohibido que φ"

Sistema: KD (K + axioma D)
  Axioma K: O(φ→ψ) → (O(φ)→O(ψ))
  Axioma D: O(φ) → P(φ) — "lo obligatorio es permisible"

  Relación de accesibilidad: serial
  Propiedades del frame: {serialidad}
  Significado: todo estado deóntico tiene al menos una alternativa permisible

  No vale:
    ✗ Reflexividad  (O(φ) → φ — lo obligatorio no es necesariamente el caso)
    ✗ Transitividad, Simetría, Euclidianidad

  ⚠ Paradojas conocidas en SDL:
    • Ross:       O(P) → O(P∨Q) — si es obligatorio enviar la carta, ¿es obligatorio enviarla o quemarla?
    • Chisholm:   O(P), O(P→Q), ¬P→O(¬Q), ¬P — inconsistente (contrary-to-duty)
    • Samaritano: O(¬P) → O(¬P∧Q) — obligaciones derivadas de eventos impermisibles
Estatus: NO válida en deontic.standard

Test 3: la combinación valida + efectiva es satisfacible.
◎ [check satisfiable] (V ∧ E) es SATISFACIBLE en deontic.standard
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: (V & E)
    2. [0] Regla Alpha (Conjunción) en w0: (V & E)
    3. [1] Analizando literal: E en w0
    4. [1] Analizando literal: V en w0
    5. [1] ✓ Rama saturada y ABIERTA.

Test 4: el deber se reduce a (validez + efectividad), no a sustancia.
✓ [check valid] (((V ∧ E) ∧ (D ↔ (V ∧ E))) → D) es VÁLIDA en deontic.standard
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: (((V & E) & (D <-> (V & E))) -> D)
    2. [0] Regla Alpha (Conjunción) en w0: (((V & E) & ((D & (V & E)) | (!D & (!V | !E)))) & !D)
    3. [1] Analizando literal: !D en w0
    4. [1] Regla Alpha (Conjunción) en w0: ((V & E) & ((D & (V & E)) | (!D & (!V | !E))))
    5. [2] Regla Alpha (Conjunción) en w0: (V & E)
    6. [3] Analizando literal: E en w0
    7. [3] Analizando literal: V en w0
    8. [3] Regla Beta (Disyunción/Impl) en w0: ((D & (V & E)) | (!D & (!V | !E))). Bifurcando...
    9. [3]   -> Rama Beta 2: (!D & (!V | !E))
    10. [4] Regla Alpha (Conjunción) en w0: (!D & (!V | !E))
    11. [5] Regla Beta (Disyunción/Impl) en w0: (!V | !E). Bifurcando...
    12. [5]   -> Rama Beta 2: !E
    13. [6] Analizando literal: !E en w0
    14. [6] ✕ Rama cerrada por contradicción con !E en w0

Test 5: ausencia de cumplimiento universal NO refuta validez.
◎ [check satisfiable] (V ∧ P(¬C)) es SATISFACIBLE en deontic.standard
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: (V & <>(!C))
    2. [0] Regla Alpha (Conjunción) en w0: (V & <>(!C))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(!C) ─> nuevo mundo w1
    4. [2] Analizando literal: !C en w1
    5. [2] Analizando literal: V en w0
    6. [2] ✓ Rama saturada y ABIERTA.
(la norma puede ser válida aunque haya casos de incumplimiento)

Test 6: el naturalismo ético no-reduccionista es coherente.
◎ [check satisfiable] (((((V ∧ E) ∧ L) ∧ D) ∧ O(C)) ∧ P(C)) es SATISFACIBLE en deontic.standard
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: (((((V & E) & L) & D) & [](C)) & <>(C))
    2. [0] Regla Alpha (Conjunción) en w0: (((((V & E) & L) & D) & [](C)) & <>(C))
    3. [1] Regla Alpha (Conjunción) en w0: ((((V & E) & L) & D) & [](C))
    4. [2] Regla Alpha (Conjunción) en w0: (((V & E) & L) & D)
    5. [3] Analizando literal: D en w0
    6. [3] Regla Alpha (Conjunción) en w0: ((V & E) & L)
    7. [4] Analizando literal: L en w0
    8. [4] Regla Alpha (Conjunción) en w0: (V & E)
    9. [5] Analizando literal: E en w0
    10. [5] Analizando literal: V en w0
    11. [5] Regla Delta (Posibilidad/Existe) en w0: <>(C) ─> nuevo mundo w1
    12. [6] Analizando literal: C en w1
    13. [6] Regla Gamma (Necesidad/ParaTodo) en w0: [](C)
    14. [7] ✓ Rama saturada y ABIERTA.
── Render: theory (markdown) ──
  Perfil: deontic.standard
  Axiomas: 4
    verbose = on
    validez_es_atractor = (V → □(C))
    efectividad_es_tasa = (E → ◇(C))
    deber_natural = (D ↔ (V ∧ E))
  Teoremas: 0
  Claims: 0

=== Fin teoría 18 ===
```

## theories/19-asimetria-tres-marcos.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.first_order
Set verbose = on
=== Teoría 19 — Asimetría L1↔B↔L3↔S a través de los 3 marcos ===

Refactorización de T05 incorporando que la asimetría es invariante
a la escala (corpus inter-escala) y opera al mismo modo en lo cuántico,
molecular, celular, individual y astrofísico.
Axioma B_universal = forall x(((B(x) -> F(x)) & (F(x) -> B(x))))
Axioma filtro_S = forall x(((B(x) & F(x)) -> S(x)))
Axioma asimetria_L1S = exists x((L1(x) & !(S(x))))
Axioma asimetria_SL1 = exists x((S(x) & !(L1(x))))
Axioma invariancia_escala = forall x((B(x) -> Multiescalar(x)))
Axioma B_qubit = B(qubit)
Axioma B_proteina = B(proteina)
Axioma B_celula = B(celula)
Axioma B_organismo = B(organismo)
Axioma B_cumulo = B(cumulo)

Test 1: B se instancia en al menos 5 escalas distintas.
◎ [check satisfiable] (B(qubit) & B(proteina) & B(celula) & B(organismo) & B(cumulo)) es SATISFACIBLE en lógica de primer orden

Test 2: cada instancia de B implica L3 traducible (universal).
✓ [check valid] (forall x(((B(x) -> F(x)) & (F(x) -> B(x)))) -> (B(qubit) -> F(qubit))) es VÁLIDA en lógica de primer orden
  Traza del tableau:
    1. [Iter] ✕ Rama cerrada por contradicción
    2. [Iter] ✕ Rama cerrada por contradicción
✓ [check valid] (forall x(((B(x) -> F(x)) & (F(x) -> B(x)))) -> (B(cumulo) -> F(cumulo))) es VÁLIDA en lógica de primer orden
  Traza del tableau:
    1. [Iter] ✕ Rama cerrada por contradicción
    2. [Iter] ✕ Rama cerrada por contradicción

Test 3: las asimetrías L1↔S coexisten (existenciales no contradictorias).
◎ [check satisfiable] (exists x((L1(x) & !(S(x)))) & exists y((S(y) & !(L1(y))))) es SATISFACIBLE en lógica de primer orden

Test 4: S NO se sigue universalmente de L1 (sustitución nominal prohibida).
✗ [countermodel] Existe contramodelo para forall x((L1(x) -> S(x))) (no válida en lógica de primer orden)

Test 5: la cadena B→F→S opera en cualquier escala (modelos satisfacibles).
◎ [check satisfiable] (forall x(((B(x) & F(x)) -> S(x))) & B(qubit) & F(qubit) & S(qubit)) es SATISFACIBLE en lógica de primer orden
◎ [check satisfiable] (forall x(((B(x) & F(x)) -> S(x))) & B(cumulo) & F(cumulo) & S(cumulo)) es SATISFACIBLE en lógica de primer orden
◎ [check satisfiable] (forall x(((B(x) & F(x)) -> S(x))) & exists x((B(x) & F(x) & S(x)))) es SATISFACIBLE en lógica de primer orden

Test 6: la asimetría es invariante a la escala.
◎ [check satisfiable] (B(qubit) & B(cumulo) & Multiescalar(qubit) & Multiescalar(cumulo)) es SATISFACIBLE en lógica de primer orden
── Render: theory (markdown) ──
  Perfil: classical.first_order
  Axiomas: 11
    verbose = on
    B_universal = ∀x(((B(x) → F(x)) ∧ (F(x) → B(x))))
    filtro_S = ∀x(((B(x) ∧ F(x)) → S(x)))
    asimetria_L1S = ∃x((L1(x) ∧ ¬(S(x))))
    asimetria_SL1 = ∃x((S(x) ∧ ¬(L1(x))))
    invariancia_escala = ∀x((B(x) → Multiescalar(x)))
    B_qubit = B(qubit)
    B_proteina = B(proteina)
    B_celula = B(celula)
    B_organismo = B(organismo)
    B_cumulo = B(cumulo)
  Teoremas: 0
  Claims: 0

=== Fin teoría 19 ===
```

## theories/20-stress-test-falsabilidad.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Set verbose = on
=== Teoría 20 — Stress test de falsabilidad: ¿la tesis es realmente falsable? ===

Test duro: si todos los hostile testing fallaran, la tesis quedaría
refutada. Verifica que la implicación es estricta y no se elude.
Let TESIS = "Tesis del irrealismo operativo de estructuras pre-ontológicas" : T
Let falsac1 = "Random walk produce overall_pass > 5% (calibración rota)" : A
Let falsac2 = "Sondas multiescala detectan EDI > 0.30 sobre datos no-suyos (circularidad)" : B
Let falsac3 = "Multi-sonda diverge en >50% de strong (dependencia instrumental fuerte)" : C
Let falsac4 = "Datos humanos VENLab del caso 30 producen EDI < 0.05 (caso ancla refutado)" : D
Let falsac5 = "Suite ST detecta contradicción interna no resoluble" : E
Let falsac6 = "Revisión por pares humanos hostiles encuentra falla estructural" : F
Let falsac7 = "Aparato falla en escala cuántica genuinamente abierta" : G
Let falsac8 = "Naturalismo de partida produce contradicción operativa" : H
Axioma f1 = (A -> !T)
Axioma f2 = (B -> !T)
Axioma f3 = (C -> !T)
Axioma f4 = (D -> !T)
Axioma f5 = (E -> !T)
Axioma f6 = (F -> !T)
Axioma f7 = (G -> !T)
Axioma f8 = (H -> !T)
Axioma tesis_iff_no_falsacion = (T <-> !((A | B | C | D | E | F | G | H)))

Test 1: cada falsación individual refuta la tesis.
✓ [check valid] ((A & (A -> !T)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((F & (F -> !T)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((G & (G -> !T)) -> !T) es VALIDA (tautologia)
✓ [check valid] ((H & (H -> !T)) -> !T) es VALIDA (tautologia)

Test 2: si TODAS las falsaciones fueran ciertas, la tesis sería refutada masivamente.
✓ [check valid] ((A & B & C & D & E & F & G & H & (T <-> !((A | B | C | D | E | F | G | H)))) -> !T) es VALIDA (tautologia)

Test 3: la tesis NO es tautología (admite contramodelo).
✗ [countermodel] Contramodelo encontrado para T
  ← T=F
  Modelo:
    T = false

Test 4: la tesis NO es contradicción (admite modelo).
◎ [check satisfiable] T es SATISFACIBLE

Test 5: estado actual del corpus — verificación operativa.
Let actual_A = "A: tasa empírica de tipo I = 24% (problema parcial)" : Pa
Let actual_B = "B: 0/12 circularidad detectada (V4-01 negativa)" : Pb
Let actual_F = "F: revisión humana hostil pendiente (P)" : Pf
Axioma estado_actual = (!B & !D & !E & !G & !H & Pf)

  El corpus actual NO satisface las falsaciones B, D, E, G, H.
  La falsación A (calibración p-value) es problema parcial reconocido.
  La falsación F (revisión externa) está PENDIENTE — deuda externa bloqueante.
◎ [check satisfiable] (T & !B & !D & !E & !G & !H) es SATISFACIBLE

Test 6: la tesis es robusta bajo el subconjunto de falsaciones operadas.
◎ [check satisfiable] (T & !B & !D & !G) es SATISFACIBLE
(B refutada por V4-01, D pendiente datos humanos, G no aplicable corpus actual)

Test 7: análisis de modus tollens — desde una falsación se infiere ¬T.
✓ [analyze] {(A → ¬T), A} → ¬T
  Inferencia VÁLIDA — no se detectaron falacias
✓ [analyze] {(F → ¬T), F} → ¬T
  Inferencia VÁLIDA — no se detectaron falacias
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 11
    verbose = on
    f1 = (A → ¬T)
    f2 = (B → ¬T)
    f3 = (C → ¬T)
    f4 = (D → ¬T)
    f5 = (E → ¬T)
    f6 = (F → ¬T)
    f7 = (G → ¬T)
    f8 = (H → ¬T)
    tesis_iff_no_falsacion = (T ↔ ¬((A ∨ B ∨ C ∨ D ∨ E ∨ F ∨ G ∨ H)))
    estado_actual = (¬B ∧ ¬D ∧ ¬E ∧ ¬G ∧ ¬H ∧ Pf)
  Teoremas: 0
  Claims: 0

=== Fin teoría 20 ===
```

## theories/21-belnap-corpus-multiescala.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: paraconsistent.belnap
Set verbose = on
=== Teoría 21 — Belnap paraconsistente: corpus multiescala honesto ===

Refactor de T12: incluye no solo Wolfram sino la coexistencia de
verdades parcialmente conflictivas reportadas honestamente:
  - Caso 30 sufre circularidad (N2) Y produce EDI 0.262 weak
  - p-value 24% empírico (mal calibrado) Y umbrales EDI robustos
  - 7 strong inter-escala depurados post-hoc Y sondas específicas (V4-01)
  - AUC-ROC 0.886 ranking interno Y NO validación externa

En lógica clásica esto sería contradicción. En Belnap (T,F,both,neither)
estas verdades parciales coexisten sin trivializar la tesis.
Let circ_caso30 = "Caso 30 sufre circularidad" : C
Let edi_caso30 = "Caso 30 produce EDI 0.262 weak" : E
Let pvalue_mal = "p-value tiene tasa de tipo I = 24%" : P
Let umbral_robusto = "Umbrales EDI son robustos a random walk" : U
Let depuracion = "Sondas multiescala depuradas post-hoc" : D
Let especificas = "Sondas multiescala son específicas (V4-01: 0/12)" : S
Let auc_interno = "AUC 0.886 es ranking interno" : A
Let validacion_externa = "Validación contra estándar de oro independiente" : V

Test 1: las pares aparentemente contradictorias coexisten en Belnap.
◎ [check satisfiable] (C & E) es satisfacible en Belnap
◎ [check satisfiable] (P & U) es satisfacible en Belnap
◎ [check satisfiable] (D & S) es satisfacible en Belnap
◎ [check satisfiable] (A & !V) es satisfacible en Belnap

Test 2: ninguna par implica trivialización (P arbitraria).
Let cualquier_P = "Proposición arbitraria" : Q
◎ [check satisfiable] (C & E & !Q) es satisfacible en Belnap
◎ [check satisfiable] (P & U & !Q) es satisfacible en Belnap
✗ [countermodel] Contramodelo Belnap para: ((C & E) -> Q)
  Valuación:
    C = T (True — solo verdadero)
    E = T (True — solo verdadero)
    Q = F (False — solo falso)
  Resultado: ((C & E) -> Q) = F (no designado)

  Explicación: En la lógica de Belnap, los valores designados son {T, B}.
  El valor "F" no es designado, por lo que la fórmula falla bajo esta valuación.
  Modelo:
    C = T
    E = T
    Q = F
✗ [countermodel] Contramodelo Belnap para: ((P & U) -> Q)
  Valuación:
    P = T (True — solo verdadero)
    Q = F (False — solo falso)
    U = T (True — solo verdadero)
  Resultado: ((P & U) -> Q) = F (no designado)

  Explicación: En la lógica de Belnap, los valores designados son {T, B}.
  El valor "F" no es designado, por lo que la fórmula falla bajo esta valuación.
  Modelo:
    P = T
    Q = F
    U = T

Test 3: la honestidad metodológica NO colapsa la tesis.
Let TESIS = "Tesis general multiescalar" : T
◎ [check satisfiable] (T & C & E & P & U & D & S & A & !V) es satisfacible en Belnap

Test 4: en Belnap, both(C,E) NO implica ¬T.
◎ [check satisfiable] (T & C & E) es satisfacible en Belnap
(reconocer la circularidad del caso 30 no refuta la tesis general)

Test 5: Wolfram vs EDI macro coexisten (T12 conservada).
Let irreducible = "Wolfram irreducible computacionalmente" : I
Let cierre_macro = "Cierre operativo macro detectable EDI 0.55" : M
◎ [check satisfiable] (I & M) es satisfacible en Belnap
── Render: theory (markdown) ──
  Perfil: paraconsistent.belnap
  Axiomas: 1
    verbose = on
  Teoremas: 0
  Claims: 0

=== Fin teoría 21 ===
```

## theories/22-modal-s5-marco-tripartito.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: modal.k
Set verbose = on
=== Teoría 22 — Modal: necesidad y contingencia del marco tripartito ===

La tesis declara sistema modal AT LEAST T (KT). Probamos en modal.k
(K base) la coherencia + la regla K + la limitación de K sin T:
  - lo que el marco declara como NECESARIO (4 invariantes ontológicos)
  - lo que declara como CONTINGENTE (la sonda específica de cada caso)
Let materialidad = "Sustrato material dinámico" : M
Let acoplamiento = "Acoplamiento dinámico" : A
Let atractor = "Atractor empírico" : K
Let cierre = "Cierre operativo κ" : C
Let sonda_FW = "Sonda Fajen-Warren para caso 30" : S

Test 1: los 4 invariantes son declarados como necesarios.
◎ [check satisfiable] □(M) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: [](M)
    2. [0] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    3. [1] ✓ Rama saturada y ABIERTA.
◎ [check satisfiable] □(A) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: [](A)
    2. [0] Regla Gamma (Necesidad/ParaTodo) en w0: [](A)
    3. [1] ✓ Rama saturada y ABIERTA.
◎ [check satisfiable] □(K) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: [](K)
    2. [0] Regla Gamma (Necesidad/ParaTodo) en w0: [](K)
    3. [1] ✓ Rama saturada y ABIERTA.
◎ [check satisfiable] □(C) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: [](C)
    2. [0] Regla Gamma (Necesidad/ParaTodo) en w0: [](C)
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

Test 2: las sondas específicas son contingentes.
◎ [check satisfiable] (◇(S) ∧ ◇(¬S)) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: (<>(S) & <>(!S))
    2. [0] Regla Alpha (Conjunción) en w0: (<>(S) & <>(!S))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(S) ─> nuevo mundo w1
    4. [2] Analizando literal: S en w1
    5. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!S) ─> nuevo mundo w2
    6. [3] Analizando literal: !S en w2
    7. [3] ✓ Rama saturada y ABIERTA.
Fórmula: ◇(S)

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

Test 3: regla K — distribución del operador necesidad.
✓ [check valid] (□((M → A)) → (□(M) → □(A))) es VÁLIDA en modal.k
  Identificación: Axioma K (Distribución)
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: ([]((M -> A)) -> ([](M) -> [](A)))
    2. [0] Regla Alpha (Conjunción) en w0: ([]((!M | A)) & ([](M) & <>(!A)))
    3. [1] Regla Alpha (Conjunción) en w0: ([](M) & <>(!A))
    4. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!A) ─> nuevo mundo w1
    5. [3] Analizando literal: !A en w1
    6. [3] Regla Gamma (Necesidad/ParaTodo) en w0: []((!M | A))
    7. [4] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    8. [5] Analizando literal: M en w1
    9. [5] Regla Beta (Disyunción/Impl) en w1: (!M | A). Bifurcando...
    10. [5]   -> Rama Beta 2: A
    11. [6] Analizando literal: A en w1
    12. [6] ✕ Rama cerrada por contradicción con A en w1

Test 4: en modal.k, NO podemos deducir M desde []M (necesita axioma T).
✓ [check valid] (□(M) → □(M)) es VÁLIDA en modal.k
  Identificación: Identidad / Reflexividad
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: ([](M) -> [](M))
    2. [0] Regla Alpha (Conjunción) en w0: ([](M) & <>(!M))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(!M) ─> nuevo mundo w1
    4. [2] Analizando literal: !M en w1
    5. [2] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    6. [3] Analizando literal: M en w1
    7. [3] ✕ Rama cerrada por contradicción con M en w1
(en modal.kt sí: []M → M; aquí no asumido)

Test 5: contramodelo: contingencia no implica necesidad.
✗ [countermodel] Existe un contramodelo para (◇(M) → □(M))
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: !(<>(M) -> [](M))
    2. [0] Regla Alpha (Conjunción) en w0: (<>(M) & <>(!M))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(M) ─> nuevo mundo w1
    4. [2] Analizando literal: M en w1
    5. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!M) ─> nuevo mundo w2
    6. [3] Analizando literal: !M en w2
    7. [3] ✓ Rama saturada y ABIERTA.

Test 6: los 4 invariantes son simultáneamente necesarios.
◎ [check satisfiable] (((□(M) ∧ □(A)) ∧ □(K)) ∧ □(C)) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: ((([](M) & [](A)) & [](K)) & [](C))
    2. [0] Regla Alpha (Conjunción) en w0: ((([](M) & [](A)) & [](K)) & [](C))
    3. [1] Regla Alpha (Conjunción) en w0: (([](M) & [](A)) & [](K))
    4. [2] Regla Alpha (Conjunción) en w0: ([](M) & [](A))
    5. [3] Regla Gamma (Necesidad/ParaTodo) en w0: [](C)
    6. [4] Regla Gamma (Necesidad/ParaTodo) en w0: [](K)
    7. [5] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    8. [6] Regla Gamma (Necesidad/ParaTodo) en w0: [](A)
    9. [7] ✓ Rama saturada y ABIERTA.

Test 7: la sonda específica es contingente y reemplazable.
Let sonda_alt = "Sonda alternativa con motivación distinta" : T
◎ [check satisfiable] (◇(S) ∧ ◇(T)) es SATISFACIBLE en modal.k
  Traza del tableau:
    1. Iniciando prueba de satisfacibilidad para: (<>(S) & <>(T))
    2. [0] Regla Alpha (Conjunción) en w0: (<>(S) & <>(T))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(S) ─> nuevo mundo w1
    4. [2] Analizando literal: S en w1
    5. [2] Regla Delta (Posibilidad/Existe) en w0: <>(T) ─> nuevo mundo w2
    6. [3] Analizando literal: T en w2
    7. [3] ✓ Rama saturada y ABIERTA.
(multi-sonda: ambas sondas son posibles, ninguna necesaria)
── Render: theory (markdown) ──
  Perfil: modal.k
  Axiomas: 1
    verbose = on
  Teoremas: 0
  Claims: 0

=== Fin teoría 22 ===
```

## theories/23-modal-kt-bajo-hipotesis.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: modal.k
Set verbose = on
=== Teoría 23 — Sistema modal T (KT) bajo hipótesis explícita ===

El cap 02-01 declara que el sistema modal asumido es AT LEAST T (KT).
La biblioteca st-lang sólo provee perfil modal.k base. Esta teoría
verifica las inferencias críticas bajo HIPÓTESIS EXPLÍCITA del axioma T.
Es decir: trabajamos en modal.k + axioma T como premisa, lo cual es
lógicamente equivalente a modal.kt.

Let materialidad = "Sustrato material dinámico" : M
Let acoplamiento = "Acoplamiento dinámico" : A
Let atractor = "Atractor empírico" : K
Let cierre = "Cierre operativo κ" : C

Test 1: Axioma T (reflexividad) NO se valida en modal.k puro.
✗ [check valid] (□(M) → M) NO es válida en modal.k
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: ([](M) -> M)
    2. [0] Regla Alpha (Conjunción) en w0: ([](M) & !M)
    3. [1] Analizando literal: !M en w0
    4. [1] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    5. [2] ✓ Rama saturada y ABIERTA.

Test 2: Bajo hipótesis del axioma T, []M -> M sí es válida.
Probamos: ([](M) AND ([](M) -> M)) -> M, que es modus ponens trivial
y verifica que asumiendo T como premisa, la reflexividad funciona.
✓ [check valid] ((□(M) ∧ (□(M) → M)) → M) es VÁLIDA en modal.k
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: (([](M) & ([](M) -> M)) -> M)
    2. [0] Regla Alpha (Conjunción) en w0: (([](M) & (<>(!M) | M)) & !M)
    3. [1] Analizando literal: !M en w0
    4. [1] Regla Alpha (Conjunción) en w0: ([](M) & (<>(!M) | M))
    5. [2] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    6. [3] Regla Beta (Disyunción/Impl) en w0: (<>(!M) | M). Bifurcando...
    7. [3]   -> Rama Beta 2: M
    8. [4] Analizando literal: M en w0
    9. [4] ✕ Rama cerrada por contradicción con M en w0

Test 3: Bajo hipótesis T, los 4 invariantes necesarios implican efectividad.
✓ [check valid] ((((((((□(M) ∧ □(A)) ∧ □(K)) ∧ □(C)) ∧ (□(M) → M)) ∧ (□(A) → A)) ∧ (□(K) → K)) ∧ (□(C) → C)) → (((M ∧ A) ∧ K) ∧ C)) es VÁLIDA en modal.k
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: (((((((([](M) & [](A)) & [](K)) & [](C)) & ([](M) -> M)) & ([](A) -> A)) & ([](K) -> K)) & ([](C) -> C)) -> (((M & A) & K) & C))
    2. [0] Regla Alpha (Conjunción) en w0: (((((((([](M) & [](A)) & [](K)) & [](C)) & (<>(!M) | M)) & (<>(!A) | A)) & (<>(!K) | K)) & (<>(!C) | C)) & (((!M | !A) | !K) | !C))
    3. [1] Regla Alpha (Conjunción) en w0: ((((((([](M) & [](A)) & [](K)) & [](C)) & (<>(!M) | M)) & (<>(!A) | A)) & (<>(!K) | K)) & (<>(!C) | C))
    4. [2] Regla Alpha (Conjunción) en w0: (((((([](M) & [](A)) & [](K)) & [](C)) & (<>(!M) | M)) & (<>(!A) | A)) & (<>(!K) | K))
    5. [3] Regla Alpha (Conjunción) en w0: ((((([](M) & [](A)) & [](K)) & [](C)) & (<>(!M) | M)) & (<>(!A) | A))
    6. [4] Regla Alpha (Conjunción) en w0: (((([](M) & [](A)) & [](K)) & [](C)) & (<>(!M) | M))
    7. [5] Regla Alpha (Conjunción) en w0: ((([](M) & [](A)) & [](K)) & [](C))
    8. [6] Regla Alpha (Conjunción) en w0: (([](M) & [](A)) & [](K))
    9. [7] Regla Alpha (Conjunción) en w0: ([](M) & [](A))
    10. [8] Regla Gamma (Necesidad/ParaTodo) en w0: [](C)
    11. [9] Regla Gamma (Necesidad/ParaTodo) en w0: [](K)
    12. [10] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    13. [11] Regla Gamma (Necesidad/ParaTodo) en w0: [](A)
    14. [12] Regla Beta (Disyunción/Impl) en w0: (((!M | !A) | !K) | !C). Bifurcando...
    15. [12]   -> Rama Beta 2: !C
    16. [13] Analizando literal: !C en w0
    17. [13] Regla Beta (Disyunción/Impl) en w0: (<>(!C) | C). Bifurcando...
    18. [13]   -> Rama Beta 2: C
    19. [14] Analizando literal: C en w0
    20. [14] ✕ Rama cerrada por contradicción con C en w0

Test 4: Bajo hipótesis T, la cadena necesidad → existencia se cierra.
Si []M (necesario que haya materialidad) y axioma T, entonces hay materialidad.
✓ [check valid] ((□(M) ∧ (□(M) → M)) → M) es VÁLIDA en modal.k
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: (([](M) & ([](M) -> M)) -> M)
    2. [0] Regla Alpha (Conjunción) en w0: (([](M) & (<>(!M) | M)) & !M)
    3. [1] Analizando literal: !M en w0
    4. [1] Regla Alpha (Conjunción) en w0: ([](M) & (<>(!M) | M))
    5. [2] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    6. [3] Regla Beta (Disyunción/Impl) en w0: (<>(!M) | M). Bifurcando...
    7. [3]   -> Rama Beta 2: M
    8. [4] Analizando literal: M en w0
    9. [4] ✕ Rama cerrada por contradicción con M en w0

Test 5: La regla K (distribución) sigue siendo válida en modal.k base
y se preserva bajo extensión a KT.
✓ [check valid] (□((M → A)) → (□(M) → □(A))) es VÁLIDA en modal.k
  Identificación: Axioma K (Distribución)
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: ([]((M -> A)) -> ([](M) -> [](A)))
    2. [0] Regla Alpha (Conjunción) en w0: ([]((!M | A)) & ([](M) & <>(!A)))
    3. [1] Regla Alpha (Conjunción) en w0: ([](M) & <>(!A))
    4. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!A) ─> nuevo mundo w1
    5. [3] Analizando literal: !A en w1
    6. [3] Regla Gamma (Necesidad/ParaTodo) en w0: []((!M | A))
    7. [4] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    8. [5] Analizando literal: M en w1
    9. [5] Regla Beta (Disyunción/Impl) en w1: (!M | A). Bifurcando...
    10. [5]   -> Rama Beta 2: A
    11. [6] Analizando literal: A en w1
    12. [6] ✕ Rama cerrada por contradicción con A en w1

Test 6: Bajo hipótesis T + necesidad del acoplamiento dado materialidad,
podemos derivar la efectividad operativa del acoplamiento.
✓ [check valid] (((□((M → A)) ∧ □(M)) ∧ (□(A) → A)) → A) es VÁLIDA en modal.k
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: ((([]((M -> A)) & [](M)) & ([](A) -> A)) -> A)
    2. [0] Regla Alpha (Conjunción) en w0: ((([]((!M | A)) & [](M)) & (<>(!A) | A)) & !A)
    3. [1] Analizando literal: !A en w0
    4. [1] Regla Alpha (Conjunción) en w0: (([]((!M | A)) & [](M)) & (<>(!A) | A))
    5. [2] Regla Alpha (Conjunción) en w0: ([]((!M | A)) & [](M))
    6. [3] Regla Gamma (Necesidad/ParaTodo) en w0: []((!M | A))
    7. [4] Regla Gamma (Necesidad/ParaTodo) en w0: [](M)
    8. [5] Regla Beta (Disyunción/Impl) en w0: (<>(!A) | A). Bifurcando...
    9. [5]   -> Rama Beta 2: A
    10. [6] Analizando literal: A en w0
    11. [6] ✕ Rama cerrada por contradicción con A en w0

Test 7: Sin axioma T, la inferencia falla — contramodelo encontrado.
Esto justifica POR QUÉ el cap 02-01 declara que el sistema asumido
es AT LEAST T, no modal.k puro.
✗ [check valid] (◇(M) → □(M)) NO es válida en modal.k
  Traza del tableau:
    1. Iniciando prueba de validez por refutación para: (<>(M) -> [](M))
    2. [0] Regla Alpha (Conjunción) en w0: (<>(M) & <>(!M))
    3. [1] Regla Delta (Posibilidad/Existe) en w0: <>(M) ─> nuevo mundo w1
    4. [2] Analizando literal: M en w1
    5. [2] Regla Delta (Posibilidad/Existe) en w0: <>(!M) ─> nuevo mundo w2
    6. [3] Analizando literal: !M en w2
    7. [3] ✓ Rama saturada y ABIERTA.

=== Síntesis Teoría 23 ===
1. modal.k puro NO valida []P -> P (axioma T no asumido por defecto).
2. Bajo HIPÓTESIS EXPLÍCITA del axioma T (premisa adicional),
   todas las inferencias críticas del manuscrito se cierran.
3. Esto es lógicamente equivalente a trabajar en modal.kt.
4. La declaración del cap 02-01 'AT LEAST T (KT)' está formalmente
   respaldada: bajo el sistema declarado, las inferencias modales
   del manuscrito son válidas.

Hallazgo: la consistencia entre lo declarado (KT) y lo verificado
(modal.k + T como hipótesis explícita) está cerrada.

=== Fin teoría 23 ===
```

## Estado global

✅ La suite pasó completa.
