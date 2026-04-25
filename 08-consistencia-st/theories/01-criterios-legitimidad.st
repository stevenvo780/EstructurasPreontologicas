logic classical.propositional
set verbose = on

let anclaje = "Anclaje material" : A
let empiria = "Dependencia empírica" : B
let fidelidad = "Fidelidad relacional" : F
let inferencia = "Poder inferencial" : I
let prediccion = "Poder predictivo" : V
let intervencion = "Poder interventivo" : T
let reversibilidad = "Reversibilidad parcial" : U
let economia = "Economía explicativa" : O
let no_reifica = "No reificación" : N

axiom base_legitimidad : (A & B & F & N) -> G
axiom legitimidad_fuerte : (G & I & V & T & U & O) -> H

derive G from {anclaje, empiria, fidelidad, no_reifica, base_legitimidad}
derive H from {anclaje, empiria, fidelidad, no_reifica, inferencia, prediccion, intervencion, reversibilidad, economia, base_legitimidad, legitimidad_fuerte}

check satisfiable (A & B & F & I & V & T & U & O & N & ((A & B & F & N) -> G) & ((G & I & V & T & U & O) -> H))
check valid ((((A & B) & (F & N)) & (((A & B) & (F & N)) -> G)) -> G)
check valid ((((G & I) & (V & T) & (U & O)) & ((((G & I) & (V & T) & (U & O))) -> H)) -> H)

render theory
