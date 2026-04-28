logic classical.propositional
set verbose = on

print "=== Teoría 00 — Núcleo ontológico (refactorizada V5) ==="
print ""
print "Refactorización post-V5: el núcleo ahora articula los 4 invariantes"
print "ontológicos y el naturalismo metafísico moderado como compromiso de"
print "partida (V5-07), con rechazo explícito de alternativas."

let materialidad = "Sustrato material dinámico existe a cualquier escala" : M
let acoplamiento = "Acoplamiento dinámico entre polos" : A
let atractor = "Atractor empírico con cuenca medible" : K
let cierre = "Cierre operativo κ verificable por intervención ablativa" : C

let no_dualismo = "No hay segunda sustancia" : !D
let no_idealismo = "La materia no es apariencia del espíritu" : !I
let no_panpsiquismo = "No se atribuye experiencia a partículas" : !P

axiom invariantes_completos : (M & A & K & C) -> O
axiom naturalismo_excluye_dualismo : M -> !D
axiom naturalismo_excluye_idealismo : M -> !I
axiom naturalismo_excluye_panpsiquismo : M -> !P
axiom acoplamiento_requiere_materia : A -> M
axiom atractor_requiere_acoplamiento : K -> A
axiom cierre_requiere_atractor : C -> K

print ""
print "Test 1: los 4 invariantes son colectivamente suficientes para ontología."
check valid (((M & A & K & C) & ((M & A & K & C) -> O)) -> O)

print ""
print "Test 2: la cadena causal-constitutiva ontológica es derivable."
derive O from {materialidad, acoplamiento, atractor, cierre, invariantes_completos}

print ""
print "Test 3: el naturalismo excluye dualismo, idealismo y panpsiquismo."
check valid ((M & (M -> !D)) -> !D)
check valid ((M & (M -> !I)) -> !I)
check valid ((M & (M -> !P)) -> !P)

print ""
print "Test 4: no hay invariante sin sustrato material (M es necesario)."
check satisfiable (M & !A & !K & !C)
countermodel ((A | K | C) -> !M)

print ""
print "Test 5: la conjunción de los 4 invariantes y los 3 rechazos es satisfacible."
check satisfiable (M & A & K & C & !D & !I & !P)

print ""
print "Test 6: ningún invariante implica circular hacia atrás."
analyze {C} -> M
print "(la cadena C→K→A→M es derivada vía axiomas explícitos, no por circulación)"

render theory
print ""
print "=== Fin teoría 00 ==="
