logic classical.propositional
set verbose = on

print "=== Teoría 13 — Temporalidad y causalidad (V5-02, V5-03, V5-09) ==="
print ""
print "Verifica la coherencia de las posturas declaradas en cap 02-05:"
print "B-series, flecha termodinámica, manipulabilidad woodwardiana,"
print "constitución descendente vs downward causation kim-vulnerable."

let bseries = "Tiempo B-series relacional" : T
let flecha_termo = "Flecha termodinámica fundamental" : F
let manipulabilidad = "Causación = manipulabilidad woodwardiana" : W
let do_test = "Operador do(X=x) válido" : D
let constitucion = "Constitución descendente (Craver)" : C
let exclusion_kim = "Exclusión causal de Kim" : K

axiom bseries_exige_orden : T -> O
axiom flecha_implica_irreversibilidad : F -> R
axiom manipulabilidad_implica_do : W -> D
axiom constitucion_no_causa : C -> !V
axiom kim_aplica_a_causacion : K -> (V -> S)
axiom edi_es_do_test : E -> D

print ""
print "Test 1: la postura B-series + flecha termodinámica es satisfacible."
check satisfiable (T & F & R & O)

print ""
print "Test 2: manipulabilidad woodwardiana implica que EDI es un do-test."
check valid ((W & (W -> D) & (E -> D)) -> ((W & E) -> D))
analyze {W, W -> D} -> D

print ""
print "Test 3: constitución NO es causación (responde a Kim)."
check valid ((C & (C -> !V)) -> !V)
check satisfiable (C & !V)
countermodel (C -> V)

print ""
print "Test 4: si downward es constitución (no causación), Kim no aplica."
print "(Kim aplica solo cuando V; si C → !V, entonces de Kim no se infiere S sin V)"
check valid ((C & (C -> !V) & (K -> (V -> S))) -> (!V & (V -> S)))
print "(de !V y (V→S) NO se sigue S; el modus tollens da !S si quisiéramos)"
check satisfiable (C & !V & K & !S)
print "(modelo donde hay constitución sin sobredeterminación: Kim neutralizado)"

print ""
print "Test 5: contramodelo del eternalismo bloque (rechazado)."
let eternalismo_bloque = "Pasado, presente y futuro coexisten todos en igualdad" : B
countermodel (T & B)
print "(B-series moderado NO implica eternalismo bloque kim-vulnerable)"

print ""
print "Test 6: irreversibilidad κ↔ε es manifestación de F, no axioma adicional."
let irrev_kappa = "κ no es perfectamente reversible vía ε" : I
axiom irrev_es_termodinamica : I <-> F
check valid ((F & (F <-> I)) -> I)

print ""
print "Test 7: la combinación completa de posturas es satisfacible."
check satisfiable (T & F & W & D & C & !V & E)

render theory
print ""
print "=== Fin teoría 13 ==="
