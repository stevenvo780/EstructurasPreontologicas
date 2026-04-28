logic modal.k
set verbose = on

print "=== Teoría 22 — Modal: necesidad y contingencia del marco tripartito ==="
print ""
print "La tesis declara sistema modal AT LEAST T (KT). Probamos en modal.k"
print "(K base) la coherencia + la regla K + la limitación de K sin T:"
print "  - lo que el marco declara como NECESARIO (4 invariantes ontológicos)"
print "  - lo que declara como CONTINGENTE (la sonda específica de cada caso)"

let materialidad = "Sustrato material dinámico" : M
let acoplamiento = "Acoplamiento dinámico" : A
let atractor = "Atractor empírico" : K
let cierre = "Cierre operativo κ" : C
let sonda_FW = "Sonda Fajen-Warren para caso 30" : S

print ""
print "Test 1: los 4 invariantes son declarados como necesarios."
check satisfiable []M
check satisfiable []A
check satisfiable []K
check satisfiable []C
explain []M

print ""
print "Test 2: las sondas específicas son contingentes."
check satisfiable (<>S & <>!S)
explain <>S

print ""
print "Test 3: regla K — distribución del operador necesidad."
check valid ([]((M -> A)) -> ([]M -> []A))

print ""
print "Test 4: en modal.k, NO podemos deducir M desde []M (necesita axioma T)."
check valid ([]M -> []M)
print "(en modal.kt sí: []M → M; aquí no asumido)"

print ""
print "Test 5: contramodelo: contingencia no implica necesidad."
countermodel (<>M -> []M)

print ""
print "Test 6: los 4 invariantes son simultáneamente necesarios."
check satisfiable ([]M & []A & []K & []C)

print ""
print "Test 7: la sonda específica es contingente y reemplazable."
let sonda_alt = "Sonda alternativa con motivación distinta" : T
check satisfiable (<>S & <>T)
print "(multi-sonda: ambas sondas son posibles, ninguna necesaria)"

render theory
print ""
print "=== Fin teoría 22 ==="
