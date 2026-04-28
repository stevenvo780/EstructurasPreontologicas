logic classical.first_order
set verbose = on

print "=== Teoría 19 — Asimetría L1↔B↔L3↔S a través de los 3 marcos ==="
print ""
print "Refactorización de T05 incorporando que la asimetría es invariante"
print "a la escala (corpus inter-escala) y opera al mismo modo en lo cuántico,"
print "molecular, celular, individual y astrofísico."

axiom B_universal : forall x ((B(x) -> F(x)) & (F(x) -> B(x)))
axiom filtro_S : forall x ((B(x) & F(x)) -> S(x))
axiom asimetria_L1S : exists x (L1(x) & !S(x))
axiom asimetria_SL1 : exists x (S(x) & !L1(x))

axiom invariancia_escala : forall x (B(x) -> Multiescalar(x))
axiom B_qubit : B(qubit)
axiom B_proteina : B(proteina)
axiom B_celula : B(celula)
axiom B_organismo : B(organismo)
axiom B_cumulo : B(cumulo)

print ""
print "Test 1: B se instancia en al menos 5 escalas distintas."
check satisfiable (B(qubit) & B(proteina) & B(celula) & B(organismo) & B(cumulo))

print ""
print "Test 2: cada instancia de B implica L3 traducible (universal)."
check valid (forall x ((B(x) -> F(x)) & (F(x) -> B(x))) -> (B(qubit) -> F(qubit)))
check valid (forall x ((B(x) -> F(x)) & (F(x) -> B(x))) -> (B(cumulo) -> F(cumulo)))

print ""
print "Test 3: las asimetrías L1↔S coexisten (existenciales no contradictorias)."
check satisfiable ((exists x (L1(x) & !S(x))) & (exists y (S(y) & !L1(y))))

print ""
print "Test 4: S NO se sigue universalmente de L1 (sustitución nominal prohibida)."
countermodel (forall x (L1(x) -> S(x)))

print ""
print "Test 5: la cadena B→F→S opera en cualquier escala (modelos satisfacibles)."
check satisfiable (forall x ((B(x) & F(x)) -> S(x)) & B(qubit) & F(qubit) & S(qubit))
check satisfiable (forall x ((B(x) & F(x)) -> S(x)) & B(cumulo) & F(cumulo) & S(cumulo))
check satisfiable (forall x ((B(x) & F(x)) -> S(x)) & exists x (B(x) & F(x) & S(x)))

print ""
print "Test 6: la asimetría es invariante a la escala."
check satisfiable (B(qubit) & B(cumulo) & Multiescalar(qubit) & Multiescalar(cumulo))

render theory
print ""
print "=== Fin teoría 19 ==="
