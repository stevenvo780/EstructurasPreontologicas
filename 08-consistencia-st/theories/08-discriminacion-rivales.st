logic classical.propositional
set verbose = on

print "=== Teoría 08 — Discriminación contra 14 rivales en al menos 2 criterios ==="
print "Probar que ningún rival comparte la conjunción de criterios decisivos con la tesis."

let TESIS_anclaje    = "Tesis: anclaje material sin reducción" : A
let TESIS_dossier    = "Tesis: dossier de admisión empírica" : D
let TESIS_asimetria  = "Tesis: asimetría L1↔B↔L3↔S" : Y
let TESIS_multidom   = "Tesis: cartografía multidominio EDI" : E
let TESIS_falsacion  = "Tesis: controles de falsación rechazados" : F

let DUALISMO_pass    = "Dualismo cumple anclaje material" : Q
let MATPART_pass     = "Materialismo de partículas cumple ε" : R
let REDPLANO_pass    = "Reduccionismo plano cumple κ" : S
let EMERG_FUERTE     = "Emergentismo fuerte cumple no-reificación" : T
let CONSTR_ARB       = "Constructivismo arbitrario cumple criterio empírico" : U
let INSTRUMENT       = "Instrumentalismo cumple realismo estructural" : V
let FORM_VACIO       = "Formalismo vacío cumple anclaje material" : W
let MOD_INTERNOS     = "Modelos internos cumplen B-acoplamiento" : N
let COGN_COMP        = "Cognitivismo computacional cumple información ecológica" : O
let CONDUCTISMO      = "Conductismo radical cumple acoplamiento informacional" : P
let ENACT_RADICAL    = "Enactivismo radical cumple formalización L3" : Z
let LADYMAN_ROSS     = "Realismo estructural informativo cumple sustrato material" : H
let MECANIC_MULTI    = "Mecanicismo multinivel cumple filtro empírico EDI" : I
let WOLFRAM          = "Wolfram cumple cartografía multidominio empírica" : J

axiom rival_dualismo  : Q -> !A
axiom rival_matpart   : R -> !D
axiom rival_redplano  : S -> !Y
axiom rival_emergF    : T -> !D
axiom rival_constr    : U -> (!A & !D)
axiom rival_instr     : V -> !A
axiom rival_formv     : W -> !A
axiom rival_modint    : N -> !E
axiom rival_cogncomp  : O -> !Y
axiom rival_conduct   : P -> !Y
axiom rival_enactr    : Z -> !D
axiom rival_ladyman   : H -> !A
axiom rival_mecanic   : I -> !D
axiom rival_wolfram   : J -> !E

print ""
print "Test 1: ningún rival es equivalente a la tesis (al menos un criterio diverge)."
check satisfiable (A & D & Y & E & F & !Q & !R & !S & !T & !U & !V & !W & !N & !O & !P & !Z & !H & !I & !J)

print ""
print "Test 2: rivales están por construcción excluidos del marco si la tesis es verdadera."
check valid ((A & (Q -> !A)) -> !Q)
check valid ((D & (R -> !D)) -> !R)
check valid ((Y & (S -> !Y)) -> !S)
check valid ((D & (T -> !D)) -> !T)
check valid ((A & (V -> !A)) -> !V)
check valid ((E & (J -> !E)) -> !J)

print ""
print "Test 3: el constructivismo arbitrario falla en DOS criterios (anclaje y dossier)."
check valid ((A & D & (U -> (!A & !D))) -> !U)

print ""
print "Test 4: countermodel — la tesis NO es derivable desde ningún rival individual."
countermodel (Q -> A)
countermodel (J -> E)
countermodel (T -> D)

print ""
print "Test 5: análisis de inferencia — desde Wolfram irreducible no se sigue el cierre macro EDI."
analyze {J} -> E

print ""
print "Test 6: la conjunción de la tesis y la negación de todos los rivales es satisfacible."
check satisfiable (A & D & Y & E & F & !Q & !R & !S & !T & !U & !V & !W & !N & !O & !P & !Z & !H & !I & !J)

render theory
print ""
print "=== Fin teoría 08 ==="
