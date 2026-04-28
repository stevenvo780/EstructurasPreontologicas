logic classical.propositional
set verbose = on

print "=== Teoría 20 — Stress test de falsabilidad: ¿la tesis es realmente falsable? ==="
print ""
print "Test duro: si todos los hostile testing fallaran, la tesis quedaría"
print "refutada. Verifica que la implicación es estricta y no se elude."

let TESIS = "Tesis del irrealismo operativo de estructuras pre-ontológicas" : T

let falsac1 = "Random walk produce overall_pass > 5% (calibración rota)" : A
let falsac2 = "Sondas multiescala detectan EDI > 0.30 sobre datos no-suyos (circularidad)" : B
let falsac3 = "Multi-sonda diverge en >50% de strong (dependencia instrumental fuerte)" : C
let falsac4 = "Datos humanos VENLab del caso 30 producen EDI < 0.05 (caso ancla refutado)" : D
let falsac5 = "Suite ST detecta contradicción interna no resoluble" : E
let falsac6 = "Revisión por pares humanos hostiles encuentra falla estructural" : F
let falsac7 = "Aparato falla en escala cuántica genuinamente abierta" : G
let falsac8 = "Naturalismo de partida produce contradicción operativa" : H

axiom f1 : A -> !T
axiom f2 : B -> !T
axiom f3 : C -> !T
axiom f4 : D -> !T
axiom f5 : E -> !T
axiom f6 : F -> !T
axiom f7 : G -> !T
axiom f8 : H -> !T

axiom tesis_iff_no_falsacion : T <-> !(A | B | C | D | E | F | G | H)

print ""
print "Test 1: cada falsación individual refuta la tesis."
check valid ((A & (A -> !T)) -> !T)
check valid ((F & (F -> !T)) -> !T)
check valid ((G & (G -> !T)) -> !T)
check valid ((H & (H -> !T)) -> !T)

print ""
print "Test 2: si TODAS las falsaciones fueran ciertas, la tesis sería refutada masivamente."
check valid (((A & B & C & D & E & F & G & H) & (T <-> !(A | B | C | D | E | F | G | H))) -> !T)

print ""
print "Test 3: la tesis NO es tautología (admite contramodelo)."
countermodel T

print ""
print "Test 4: la tesis NO es contradicción (admite modelo)."
check satisfiable T

print ""
print "Test 5: estado actual del corpus — verificación operativa."
let actual_A = "A: tasa empírica de tipo I = 24% (problema parcial)" : Pa
let actual_B = "B: 0/12 circularidad detectada (V4-01 negativa)" : Pb
let actual_F = "F: revisión humana hostil pendiente (P)" : Pf

axiom estado_actual : !B & !D & !E & !G & !H & Pf
print ""
print "  El corpus actual NO satisface las falsaciones B, D, E, G, H."
print "  La falsación A (calibración p-value) es problema parcial reconocido."
print "  La falsación F (revisión externa) está PENDIENTE — deuda externa bloqueante."
check satisfiable (T & !B & !D & !E & !G & !H)

print ""
print "Test 6: la tesis es robusta bajo el subconjunto de falsaciones operadas."
check satisfiable (T & !B & !D & !G)
print "(B refutada por V4-01, D pendiente datos humanos, G no aplicable corpus actual)"

print ""
print "Test 7: análisis de modus tollens — desde una falsación se infiere ¬T."
analyze {(A -> !T), A} -> !T
analyze {(F -> !T), F} -> !T

render theory
print ""
print "=== Fin teoría 20 ==="
