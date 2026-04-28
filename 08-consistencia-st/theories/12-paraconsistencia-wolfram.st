logic paraconsistent.belnap
set verbose = on

print "=== Teoría 12 — Paraconsistencia: Wolfram irreducible micro Y EDI cierre macro ==="
print "Probar que la coexistencia aparente no colapsa la teoría."

let irreducible_micro = "Rule 110 es computacionalmente irreducible al nivel micro" : I
let cierre_macro      = "Rule 110 admite cierre operativo EDI ≥ 0.30 a nivel macro" : C

print ""
print "Test 1: ambas afirmaciones coexisten en lógica de Belnap (T, F, both, neither)."
check satisfiable (I & C)

print ""
print "Test 2: la conjunción NO trivializa todo (no se sigue P arbitraria)."
let P_arbitrario = "Proposición arbitraria" : P
check satisfiable (I & C & !P)
countermodel ((I & C) -> P)

print ""
print "Test 3: en lógica clásica la aparente contradicción exige resolución; aquí NO."
check satisfiable (I & C & !(I -> !C))

render theory
print ""
print "=== Fin teoría 12 ==="
