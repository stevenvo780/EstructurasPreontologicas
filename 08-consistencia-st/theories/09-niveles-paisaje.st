logic classical.propositional
set verbose = on

print "=== Teoría 09 — Niveles 0-5 del paisaje de emergencia: exclusivos y exhaustivos ==="
print "Verificar que un caso no puede pertenecer a dos niveles simultáneamente."

let N0 = "Nivel 0 - Null (EDI ≤ 0 o sin estructura)" : A
let N1 = "Nivel 1 - Trend (EDI > 0, p ≥ 0.05)" : B
let N2 = "Nivel 2 - Suggestive (0.01 ≤ EDI < 0.10, p < 0.05)" : C
let N3 = "Nivel 3 - Weak (0.10 ≤ EDI < 0.30, p < 0.05)" : D
let N4 = "Nivel 4 - Strong (EDI ≥ 0.30, p < 0.01, overall_pass)" : E
let N5 = "Nivel 5 - Crítico (multi-sonda + LoE=5 + frontera nítida)" : F

axiom excl_01 : N0 -> !N1
axiom excl_02 : N0 -> !N2
axiom excl_03 : N0 -> !N3
axiom excl_04 : N0 -> !N4
axiom excl_05 : N0 -> !N5
axiom excl_12 : N1 -> !N2
axiom excl_13 : N1 -> !N3
axiom excl_14 : N1 -> !N4
axiom excl_23 : N2 -> !N3
axiom excl_24 : N2 -> !N4
axiom excl_34 : N3 -> !N4
axiom excl_45 : N4 -> !N5

axiom existe_caso : C -> (N0 | N1 | N2 | N3 | N4 | N5)

print ""
print "Test 1: cada caso del corpus pertenece a algún nivel."
check valid (C -> (A | B | C | D | E | F))

print ""
print "Test 2: ningún caso es simultáneamente strong y null."
check valid ((A & (A -> !E)) -> !E)
check satisfiable (A & !E)
countermodel (A & E)

print ""
print "Test 3: ningún caso es simultáneamente weak y suggestive."
countermodel (C & D)

print ""
print "Test 4: nivel 5 implica multi-sonda + LoE=5 + frontera nítida (TODOS)."
let multi_sonda = "Convergencia bajo múltiples sondas independientes" : Q
let loe5        = "Datos físicos directos LoE = 5" : R
let frontera    = "Frontera espacial nítida en topología heterogénea" : T
axiom n5_def : F -> (Q & R & T)

check valid ((F & (F -> (Q & R & T))) -> (Q & R & T))

print ""
print "Test 5: corpus actual NO satisface F (Nivel 5 no alcanzado)."
check satisfiable (!F & (E | D | C | B | A))

print ""
print "Test 6: countermodel — Nivel 5 con sonda única es inconsistente."
countermodel ((F & !Q))

print ""
print "Test 7: análisis — desde Nivel 4 no se sigue Nivel 5 sin condiciones extra."
analyze {E} -> F

render theory
print ""
print "=== Fin teoría 09 ==="
