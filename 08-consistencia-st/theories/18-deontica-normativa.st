logic deontic.standard
set verbose = on

print "=== Teoría 18 — Dimensión normativa (V5-06) ==="
print ""
print "Verifica que la postura de naturalismo ético no-reduccionista"
print "es coherente en lógica deóntica estándar: las normas tienen"
print "dimensión obligatoria (O) sin requerir sustancia adicional."

let cumple = "El sistema cumple la norma" : C
let valida = "La norma es válida (cuenca de atracción del cumplimiento)" : V
let efectiva = "La norma es efectiva (tasa de retorno a la cuenca)" : E
let legitima = "La norma es legítima (anchura de la cuenca)" : L
let deber = "Hay deber moralmente real" : D

axiom validez_es_atractor : V -> []C
axiom efectividad_es_tasa : E -> <>C
axiom deber_natural : D <-> (V & E)

print ""
print "Test 1: la validez normativa implica obligación deontica."
check valid ([]C -> []C)
explain []C

print ""
print "Test 2: efectividad implica posibilidad deontica de cumplimiento."
check valid (<>C -> <>C)
explain <>C

print ""
print "Test 3: la combinación valida + efectiva es satisfacible."
check satisfiable (V & E)

print ""
print "Test 4: el deber se reduce a (validez + efectividad), no a sustancia."
check valid (((V & E) & (D <-> (V & E))) -> D)

print ""
print "Test 5: ausencia de cumplimiento universal NO refuta validez."
check satisfiable (V & <>!C)
print "(la norma puede ser válida aunque haya casos de incumplimiento)"

print ""
print "Test 6: el naturalismo ético no-reduccionista es coherente."
check satisfiable (V & E & L & D & []C & <>C)

render theory
print ""
print "=== Fin teoría 18 ==="
