logic classical.propositional

let p_formulacion = passage([[../Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md#1-formulacion-central]])
let f_formulacion = formalize p_formulacion as (M & C & R & L)
claim c_formulacion = f_formulacion
support c_formulacion <- p_formulacion
confidence c_formulacion = 0.98
context c_formulacion = "Núcleo de la formulación central: materialidad, compresión, no reificación y niveles no separados"

let p_criterios = passage([[../03-formalizacion/02-criterios-de-legitimidad-y-metodo.md#los-diez-criterios-de-legitimidad]])
let f_criterios = formalize p_criterios as (A & B & F & I & V & T & U & O & N)
claim c_criterios = f_criterios
support c_criterios <- p_criterios
confidence c_criterios = 0.95
context c_criterios = "Matriz mínima de legitimidad epistemológica"

let p_principio = passage([[../Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md#44-la-tesis-como-principio-general]])
let f_principio = formalize p_principio as (M & C & R)
claim c_principio = f_principio
support c_principio <- p_principio
confidence c_principio = 0.94
context c_principio = "Principio de realidad relacional comprimible"

render claims
render theory
