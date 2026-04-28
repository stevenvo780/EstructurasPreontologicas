logic classical.first_order
set verbose = on

print "=== Teoría 05 — Asimetría L1↔B↔L3↔S en lógica de primer orden ==="
print ""
print "HALLAZGO PREVIO (proposicional): la formulación con !(S→L) y !(L→S)"
print "como axiomas simultáneos es INSATISFACIBLE en lógica proposicional."
print "REFINAMIENTO: la asimetría es contextual (existencial), no universal."

axiom traduccional_BL3 : forall x ((B(x) -> F(x)) & (F(x) -> B(x)))
axiom filtro_S         : forall x ((B(x) & F(x)) -> S(x))
axiom L1_via_BL3       : forall x ((L1(x) & B(x) & F(x)) -> S(x))

print ""
print "Test 1: existe categoría L1 sin sobrevivir como S (no traduce a B/L3)."
check satisfiable (exists x (L1(x) & !S(x)))

print ""
print "Test 2: existe categoría S sin venir de L1 (atractor real no nombrado)."
check satisfiable (exists x (S(x) & !L1(x)))

print ""
print "Test 3: ambas existenciales coexisten."
check satisfiable ((exists x (L1(x) & !S(x))) & (exists y (S(y) & !L1(y))))

print ""
print "Test 4: traducción B↔L3 es bidireccional universal."
check valid (forall x ((B(x) -> F(x)) & (F(x) -> B(x))) -> (B(a) -> F(a)))

print ""
print "Test 5: una categoría con L1 ∧ B ∧ L3 pasa a S."
check valid (forall x ((L1(x) & B(x) & F(x)) -> S(x)) -> ((L1(a) & B(a) & F(a)) -> S(a)))

print ""
print "Test 6: contramodelo del colapso simétrico (si S<->L1 universal todo trivial)."
countermodel (forall x (S(x) -> L1(x)))

print ""
print "Test 7: la asimetría es no trivial: el universo tiene categorías heterogéneas."
check satisfiable ((exists x (B(x) & F(x) & L1(x) & S(x))) & (exists y (B(y) & F(y) & !L1(y) & S(y))) & (exists z (L1(z) & !B(z) & !S(z))))

render theory
print ""
print "=== Fin teoría 05 ==="
print ""
print "RESULTADO: la asimetría L1↔B↔L3↔S es coherente cuando se formula como:"
print "  - bidireccional B↔L3 (universal)"
print "  - filtro de S vía B∧L3 (universal)"
print "  - asimetrías L1↔S como existenciales (NO universales)"
print ""
print "El cap 02-04 debe declarar explícitamente este nivel cuantificacional."
