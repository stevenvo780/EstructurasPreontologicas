logic classical.propositional

let p_patrones = passage([[../07-bibliografia/01-bibliografia-orientativa.md#2-realismo-estructural-y-patrones]])
let f_patrones = formalize p_patrones as (D & L)
claim c_patrones = f_patrones
support c_patrones <- p_patrones
confidence c_patrones = 0.90
context c_patrones = "Dennett y Ladyman/Ross apoyan el eje patrones-estructura"

let p_mecanismos = passage([[../07-bibliografia/01-bibliografia-orientativa.md#3-explicacion-mecanicista-y-multinivel]])
let f_mecanismos = formalize p_mecanismos as (C & B)
claim c_mecanismos = f_mecanismos
support c_mecanismos <- p_mecanismos
confidence c_mecanismos = 0.91
context c_mecanismos = "Craver y Bechtel apoyan el plano de niveles, mecanismos y organización"

let p_st = passage([[../07-bibliografia/01-bibliografia-orientativa.md#11-herramientas-formales-y-de-validacion]])
let f_st = formalize p_st as S
claim c_st = f_st
support c_st <- p_st
confidence c_st = 0.97
context c_st = "ST se incorpora como herramienta metodológica de validación local"

render claims
render theory
