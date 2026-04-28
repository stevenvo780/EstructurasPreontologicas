logic classical.propositional
set verbose = on

print "=== Teoría 06 — Operadores μ, G, H, κ, ε y ausencia de circularidad viciosa ==="
print "Probar que la cadena μ → G → H → κ → ε es coherente y no circular maliciosamente."

let mu      = "Operador de medición μ : R → X"  : M
let grafo   = "Grafo basal G = (V, E, W, T)"     : G
let hiper   = "Hipergrafo H de relaciones n-arias" : H
let kappa   = "Compresión κ : G → G*"            : K
let epsilon = "Errores de traducción ε"          : E

axiom mu_genera_G     : M -> G
axiom G_genera_H      : G -> H
axiom H_admite_K      : H -> K
axiom K_genera_E      : K -> E
axiom E_reabre_a_K    : E -> (E | K)

print ""
print "Test 1: la cadena completa M → ... → E es derivable."
derive G from {mu, mu_genera_G}
derive H from {mu, mu_genera_G, grafo, G_genera_H}
derive K from {mu, mu_genera_G, grafo, G_genera_H, hiper, H_admite_K}
derive E from {mu, mu_genera_G, grafo, G_genera_H, hiper, H_admite_K, kappa, K_genera_E}

print ""
print "Test 2: NO se puede derivar μ desde κ (circularidad viciosa prohibida)."
analyze {K} -> M
check satisfiable (K & !M)
countermodel (K -> M)

print ""
print "Test 3: NO se puede derivar G desde ε (ε reabre al SIGUIENTE κ, no genera grafos primarios)."
analyze {E} -> G
check satisfiable (E & !G)
countermodel (E -> G)

print ""
print "Test 4: la cadena directa es válida pero no equivalente."
check valid ((M & (M -> G)) -> G)
check valid ((G & (G -> H)) -> H)
check valid ((H & (H -> K)) -> K)
check valid ((K & (K -> E)) -> E)

print ""
print "Test 5: μ no implica directamente E sin pasar por toda la cadena (no atajos ontológicos)."
analyze {M} -> E
print "(análisis previo debe pedir intermediarios)"

print ""
print "Test 6: la teoría completa es satisfacible (no hay contradicción interna)."
check satisfiable (M & G & H & K & E & (M -> G) & (G -> H) & (H -> K) & (K -> E))

render theory
print ""
print "=== Fin teoría 06 ==="
