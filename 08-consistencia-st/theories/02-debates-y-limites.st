logic classical.propositional
set verbose = on

let monismo = "La tesis mantiene monismo material-relacional" : M
let compresion_controlada = "La tesis usa compresión controlada" : C
let criterio_estructural = "La tesis evalúa categorías por estructura real" : E

axiom anti_dualismo : M -> !D
axiom anti_reduccion : C -> !R
axiom anti_emergencia_fuerte : E -> !S
axiom anti_constructivismo : (M & E) -> !A

derive !D from {monismo, anti_dualismo}
derive !R from {compresion_controlada, anti_reduccion}
derive !S from {criterio_estructural, anti_emergencia_fuerte}
derive !A from {monismo, criterio_estructural, anti_constructivismo}

check satisfiable (M & C & E & (M -> !D) & (C -> !R) & (E -> !S) & ((M & E) -> !A))
countermodel (M -> D)
countermodel (C -> R)
countermodel (E -> S)
countermodel ((M & E) -> A)

render theory
