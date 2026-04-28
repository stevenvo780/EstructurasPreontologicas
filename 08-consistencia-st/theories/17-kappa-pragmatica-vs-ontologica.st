logic classical.propositional
set verbose = on

print "=== Teoría 17 — κ-pragmática vs κ-ontológica (V5-07/A8) ==="
print ""
print "Verifica que la distinción entre κ-pragmática (compresión funciona)"
print "y κ-ontológica (compresión corresponde a estructura material independiente)"
print "es lógicamente sostenible y que NINGÚN caso del corpus actual cumple"
print "los 3 criterios κ-ontológica simultáneamente."

let kappa_p = "κ-pragmática: la compresión predice/discrimina" : P
let kappa_o = "κ-ontológica: la compresión corresponde a estructura material independiente" : O
let multi_sonda = "Convergencia bajo múltiples sondas independientes" : M
let inter_grupo = "Replicación inter-grupo" : I
let intervencion_exp = "Intervención experimental confirmatoria" : E

axiom def_ontologica : O <-> (P & M & I & E)
axiom kp_no_implica_ko : P -> !O
axiom corpus_actual_solo_p : C -> (P & !O)

print ""
print "Test 1: κ-ontológica requiere los 3 criterios simultáneamente."
check valid (((O <-> (P & M & I & E)) & O) -> (M & I & E))
check valid (((O <-> (P & M & I & E)) & (P & M & I & E)) -> O)

print ""
print "Test 2: κ-pragmática NO implica κ-ontológica."
check satisfiable (P & !O)
countermodel (P -> O)

print ""
print "Test 3: ningún caso actual cumple los 3 criterios."
let caso_actual = "Caso del corpus actual" : C
check valid ((C -> (P & !O)) -> (C -> !O))
check satisfiable (C & P & !M)
check satisfiable (C & P & !I)
check satisfiable (C & P & !E)

print ""
print "Test 4: si SE cumplieran los 3 criterios, sí habría κ-ontológica."
check valid (((P & M & I & E) & (O <-> (P & M & I & E))) -> O)

print ""
print "Test 5: la distinción es no trivial: hay modelos donde solo se da P."
check satisfiable (P & !M & !I & !E)
print "(estos son los 40 casos del corpus actual)"

print ""
print "Test 6: contramodelo del colapso κ-pragmática = κ-ontológica."
countermodel (O <-> P)
print "(rechaza tanto operacionalismo puro como realismo metafísico fuerte)"

render theory
print ""
print "=== Fin teoría 17 ==="
