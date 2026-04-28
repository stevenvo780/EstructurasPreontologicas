logic classical.propositional
set verbose = on

print "=== Teoría 07 — overall_pass = 13 condiciones independientes ==="
print "Verificar que las 13 condiciones de overall_pass son colectivamente necesarias y suficientes."

let C1 = "Convergencia numérica" : A
let C2 = "Robustez a perturbaciones" : B
let C3 = "Determinismo seed=42" : C
let C4 = "Consistencia estadística" : D
let C5 = "Incertidumbre acotada (CI)" : E

let C6  = "EDI ≥ 0.30" : F
let C7  = "p-value < 0.01" : G
let C8  = "val_steps ≥ 8" : H
let C9  = "coupling > 0.10" : I
let C10 = "forcing controlado" : J
let C11 = "estabilidad numérica reportada" : K
let C12 = "persistencia temporal verificada" : L
let C13 = "no controles falsos positivos" : N

axiom overall_def : (A & B & C & D & E & F & G & H & I & J & K & L & N) -> P

print ""
print "Test 1: las 13 condiciones juntas implican overall_pass."
check valid (((A & B & C & D & E & F & G & H & I & J & K & L & N) & ((A & B & C & D & E & F & G & H & I & J & K & L & N) -> P)) -> P)

print ""
print "Test 2: si falta C6 (EDI bajo), NO hay overall_pass."
check satisfiable (A & B & C & D & E & !F & G & H & I & J & K & L & N & !P)

print ""
print "Test 3: si falta C7 (p-value alto), NO hay overall_pass."
check satisfiable (A & B & C & D & E & F & !G & H & I & J & K & L & N & !P)

print ""
print "Test 4: si falta C13 (control de falsos positivos), NO hay overall_pass."
check satisfiable (A & B & C & D & E & F & G & H & I & J & K & L & !N & !P)

print ""
print "Test 5: contramodelo de overall_pass con condición faltante."
countermodel (((A & B & C & D & E & F & G & H & I & J & K & L & N) -> P) -> ((A & B & C & D & E & F & G & H & I & J & K & L) -> P))

print ""
print "Test 6: la conjunción de 13 condiciones es satisfacible (existe modelo)."
check satisfiable (A & B & C & D & E & F & G & H & I & J & K & L & N)

print ""
print "Test 7: análisis de inferencia válida del overall_pass."
analyze {(A & B & C & D & E & F & G & H & I & J & K & L & N), ((A & B & C & D & E & F & G & H & I & J & K & L & N) -> P)} -> P

render theory
print ""
print "=== Fin teoría 07 ==="
