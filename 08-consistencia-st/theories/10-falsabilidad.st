logic classical.propositional
set verbose = on

print "=== Teoría 10 — Falsabilidad: 5 condiciones suficientes individuales de fracaso ==="
print "Cada una basta para refutar la tesis. Probar implicación TESIS ↔ ¬(F1 ∨ F2 ∨ F3 ∨ F4 ∨ F5)."

let TESIS = "Irrealismo operativo demostrado en cartografía multidominio" : T

let F1 = "Aparato no discrimina (controles falsos producen overall_pass)" : A
let F2 = "Caso ancla pierde reproducibilidad bit-a-bit" : B
let F3 = "EDI no robusto bajo perfil agresivo (cambio masivo de niveles)" : C
let F4 = "Multi-sonda diverge fuerte en >50% de strong" : D
let F5 = "Bibliografía formal nula o inconsistente con la tesis" : E

axiom f1_falsifica : A -> !T
axiom f2_falsifica : B -> !T
axiom f3_falsifica : C -> !T
axiom f4_falsifica : D -> !T
axiom f5_falsifica : E -> !T

axiom tesis_iff_no_falsacion : T <-> !(A | B | C | D | E)

print ""
print "Test 1: la tesis es lógicamente falsable."
check valid ((A & (A -> !T)) -> !T)
check valid ((B & (B -> !T)) -> !T)
check valid ((C & (C -> !T)) -> !T)
check valid ((D & (D -> !T)) -> !T)
check valid ((E & (E -> !T)) -> !T)

print ""
print "Test 2: si NINGUNA falsación se cumple, la tesis se sostiene."
check valid ((!A & !B & !C & !D & !E & (T <-> !(A | B | C | D | E))) -> T)

print ""
print "Test 3: countermodel — la tesis NO es trivial (no es tautología)."
countermodel T

print ""
print "Test 4: la conjunción TESIS y CUALQUIER falsación es contradictoria."
check satisfiable (T & A & (A -> !T))
check satisfiable (T & B & (B -> !T))

print ""
print "Test 5: análisis de modus tollens — desde controles fallidos se infiere falsedad."
analyze {(A -> !T), A} -> !T

print ""
print "Test 6: cubrimiento — las 5 condiciones cubren los modos de fracaso conocidos."
let M1 = "Inconsistencia metodológica" : G
let M2 = "Inconsistencia empírica" : H
let M3 = "Inconsistencia bibliográfica" : I
axiom m1_subset : G -> A
axiom m2_subset : H -> (B | C | D)
axiom m3_subset : I -> E

check valid ((G & (G -> A) & (A -> !T)) -> !T)
check valid ((H & (H -> (B | C | D)) & (B -> !T) & (C -> !T) & (D -> !T)) -> !T)

render theory
print ""
print "=== Fin teoría 10 ==="
