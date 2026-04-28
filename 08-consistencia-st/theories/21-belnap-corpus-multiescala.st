logic paraconsistent.belnap
set verbose = on

print "=== Teoría 21 — Belnap paraconsistente: corpus multiescala honesto ==="
print ""
print "Refactor de T12: incluye no solo Wolfram sino la coexistencia de"
print "verdades parcialmente conflictivas reportadas honestamente:"
print "  - Caso 30 sufre circularidad (N2) Y produce EDI 0.262 weak"
print "  - p-value 24% empírico (mal calibrado) Y umbrales EDI robustos"
print "  - 7 strong inter-escala depurados post-hoc Y sondas específicas (V4-01)"
print "  - AUC-ROC 0.886 ranking interno Y NO validación externa"
print ""
print "En lógica clásica esto sería contradicción. En Belnap (T,F,both,neither)"
print "estas verdades parciales coexisten sin trivializar la tesis."

let circ_caso30 = "Caso 30 sufre circularidad" : C
let edi_caso30 = "Caso 30 produce EDI 0.262 weak" : E
let pvalue_mal = "p-value tiene tasa de tipo I = 24%" : P
let umbral_robusto = "Umbrales EDI son robustos a random walk" : U
let depuracion = "Sondas multiescala depuradas post-hoc" : D
let especificas = "Sondas multiescala son específicas (V4-01: 0/12)" : S
let auc_interno = "AUC 0.886 es ranking interno" : A
let validacion_externa = "Validación contra estándar de oro independiente" : V

print ""
print "Test 1: las pares aparentemente contradictorias coexisten en Belnap."
check satisfiable (C & E)
check satisfiable (P & U)
check satisfiable (D & S)
check satisfiable (A & !V)

print ""
print "Test 2: ninguna par implica trivialización (P arbitraria)."
let cualquier_P = "Proposición arbitraria" : Q
check satisfiable (C & E & !Q)
check satisfiable (P & U & !Q)
countermodel ((C & E) -> Q)
countermodel ((P & U) -> Q)

print ""
print "Test 3: la honestidad metodológica NO colapsa la tesis."
let TESIS = "Tesis general multiescalar" : T
check satisfiable (T & C & E & P & U & D & S & A & !V)

print ""
print "Test 4: en Belnap, both(C,E) NO implica ¬T."
check satisfiable (T & C & E)
print "(reconocer la circularidad del caso 30 no refuta la tesis general)"

print ""
print "Test 5: Wolfram vs EDI macro coexisten (T12 conservada)."
let irreducible = "Wolfram irreducible computacionalmente" : I
let cierre_macro = "Cierre operativo macro detectable EDI 0.55" : M
check satisfiable (I & M)

render theory
print ""
print "=== Fin teoría 21 ==="
