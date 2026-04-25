logic classical.propositional
set verbose = on

let materialidad = "Todo fenómeno empíricamente explicable está materialmente instanciado" : M
let compresion = "Las categorías funcionan como compresiones estructurales" : C
let no_reificacion = "Las categorías no deben reificarse como sustancias simples" : R
let niveles = "Los niveles no son mundos separados" : L
let estructura = "La explicación debe preservar estructura relevante" : E

axiom puente_cr : C -> R
axiom puente_md : M -> D
axiom puente_ls : L -> S
axiom puente_ep : E -> P

derive R from {compresion, puente_cr}
derive D from {materialidad, puente_md}
derive S from {niveles, puente_ls}
derive P from {estructura, puente_ep}

check satisfiable (M & C & L & E & (C -> R) & (M -> D) & (L -> S) & (E -> P))
check valid ((C & (C -> R)) -> R)
check valid ((M & (M -> D)) -> D)
check valid ((L & (L -> S)) -> S)
check valid ((E & (E -> P)) -> P)

analyze {M, M -> D} -> D
analyze {C, C -> R} -> R
render theory
