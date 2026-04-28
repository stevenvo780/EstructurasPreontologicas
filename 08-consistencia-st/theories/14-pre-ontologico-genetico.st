logic classical.first_order
set verbose = on

print "=== Teoría 14 — 'Pre-ontológico' en sentido simondoniano (V5-01) ==="
print ""
print "Cierra el agujero conceptual del título de la tesis."
print "'Pre' = genético-epistemológico, NO temporal puro."
print ""
print "Predicados:"
print "  PreInd(x): x es pre-individual materialmente sostenido"
print "  Categ(x): x es categoría nominalizante"
print "  Atrac(x): x es atractor empírico identificable"
print "  PreOnt(x): x es estructura pre-ontológica en sentido tesis"

axiom def_preont : forall x ((PreInd(x) & Atrac(x) & !Categ(x)) <-> PreOnt(x))
axiom existe_pre_sin_categoria : exists x (PreInd(x) & !Categ(x))
axiom no_temporal_puro : forall x (PreOnt(x) -> !Anterior_temporal(x))
axiom genetico : forall x (PreOnt(x) -> Genera_individual(x))

print ""
print "Test 1: existe estructura pre-ontológica con definición técnica."
check satisfiable (exists x (PreInd(x) & Atrac(x) & !Categ(x) & PreOnt(x)))

print ""
print "Test 2: lo nominalizado NO es pre-ontológico."
check valid (forall x (Categ(x) -> !PreOnt(x)))
analyze {forall x (PreInd(x) & Atrac(x) & !Categ(x) <-> PreOnt(x))} -> (Categ(a) -> !PreOnt(a))

print ""
print "Test 3: pre-ontológico implica génesis del individuo (Simondon)."
check valid (forall x (PreOnt(x) -> Genera_individual(x)) -> (PreOnt(a) -> Genera_individual(a)))

print ""
print "Test 4: contramodelo del 'pre temporal puro' (rechazado)."
countermodel (forall x (PreOnt(x) -> Anterior_temporal(x)))
print "(la tesis NO usa 'pre' como anterioridad temporal pura)"

print ""
print "Test 5: el rol inferencial de PreOnt distingue de regularidad."
let regularidad = "Regularidad estadística sin atractor" : R
axiom reg_no_atractor : forall x (Regularidad(x) -> !Atrac(x))
check valid (forall x (Regularidad(x) -> !PreOnt(x)) -> (Regularidad(a) -> !PreOnt(a)))

render theory
print ""
print "=== Fin teoría 14 ==="
