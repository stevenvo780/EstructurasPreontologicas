logic classical.propositional
set verbose = on

print "=== Teoría 16 — Naturalismo metafísico moderado vs rivales (V5-07) ==="
print ""
print "Prueba que el naturalismo de partida excluye categóricamente"
print "dualismo, idealismo, emanacionismo, panpsiquismo y creacionismo,"
print "PERO admite alternativas realistas en mecánica cuántica."

let naturalismo = "Naturalismo metafísico moderado" : N
let dualismo = "Dualismo cartesiano" : D
let idealismo = "Idealismo metafísico" : I
let emanacion = "Emanacionismo neoplatónico" : E
let panpsiq = "Panpsiquismo" : P
let creacion = "Creacionismo metafísico" : C
let many_worlds = "Many-worlds Everett" : W
let bohm = "Bohmiana de Broglie-Bohm" : B
let copenhagen_pura = "Copenhagen instrumentalista pura" : K

axiom nat_excluye_dual : N -> !D
axiom nat_excluye_id : N -> !I
axiom nat_excluye_eman : N -> !E
axiom nat_excluye_panps : N -> !P
axiom nat_excluye_creac : N -> !C
axiom nat_excluye_copen_pura : N -> !K
axiom nat_compatible_mw : N -> (W | !W)
axiom nat_compatible_bohm : N -> (B | !B)

print ""
print "Test 1: el naturalismo excluye los 5 rivales metafísicos."
check valid ((N & (N -> !D)) -> !D)
check valid ((N & (N -> !I)) -> !I)
check valid ((N & (N -> !E)) -> !E)
check valid ((N & (N -> !P)) -> !P)
check valid ((N & (N -> !C)) -> !C)

print ""
print "Test 2: la combinación naturalismo + 5 rechazos es satisfacible."
check satisfiable (N & !D & !I & !E & !P & !C)

print ""
print "Test 3: la conjunción naturalismo + cualquier rival es contradicción."
check satisfiable (N & D & (N -> !D))
check satisfiable (N & I & (N -> !I))
check satisfiable (N & P & (N -> !P))

print ""
print "Test 4: el naturalismo NO decide entre interpretaciones realistas QM."
check satisfiable (N & W & !B)
check satisfiable (N & B & !W)
check satisfiable (N & W & B)
print "(Many-worlds, Bohm, ambos compatibles con naturalismo)"

print ""
print "Test 5: Copenhagen instrumentalista pura SÍ se rechaza."
check valid ((N & (N -> !K)) -> !K)
countermodel (N & K)

print ""
print "Test 6: contramodelo: el naturalismo NO se demuestra desde dentro."
countermodel N
print "(es compromiso de partida, no conclusión deductiva)"

print ""
print "Test 7: la postura completa es coherente."
check satisfiable (N & !D & !I & !E & !P & !C & !K & (W | B))

render theory
print ""
print "=== Fin teoría 16 ==="
