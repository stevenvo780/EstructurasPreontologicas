logic modal.k
set verbose = on

print "=== Teoría 11 — Modal: necesidad lógica vs contingencia empírica del marco ==="
print "Probar coherencia de qué es necesario ([] ) vs qué es contingente (<>)."

let materialidad      = "Sustrato material" : M
let cierre_operativo  = "κ verificado vía EDI" : K
let edi_alto          = "EDI ≥ 0.30 con p < 0.01" : E
let strong_class      = "Clasificación strong (Nivel 4)" : S

print ""
print "Test 1: la materialidad del sustrato es asumida como necesaria por la tesis."
check satisfiable []M
explain []M

print ""
print "Test 2: el cierre operativo es contingente — depende del fenómeno y la sonda."
check satisfiable (<>K & <>!K)

print ""
print "Test 3: si EDI alto entonces es POSIBLE (no necesario) que sea strong."
axiom strong_def : E -> <>S
check satisfiable (E & <>S & <>!S)

print ""
print "Test 4: regla K — distribución del operador necesidad."
check valid ([](M -> K) -> ([]M -> []K))

print ""
print "Test 5: contramodelo — necesidad NO se sigue de mera satisfacibilidad."
countermodel (<>M -> []M)

render theory
print ""
print "=== Fin teoría 11 ==="
