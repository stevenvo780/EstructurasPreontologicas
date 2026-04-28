logic classical.propositional
set verbose = on

print "=== Teoría 15 — Marco tripartito general (V5 narrativa unificada) ==="
print ""
print "Verifica que ontología (O), epistemología (E) y metodología (M)"
print "son TODAS GENERALES, no regionales, y que su generalidad es"
print "lógicamente coherente con su justificación operativa por casos (J)."

let onto_general = "Ontología afirma 4 invariantes a cualquier escala" : O
let epi_general = "Epistemología compresión disciplinada en cualquier escala" : E
let meto_general = "Metodología aparato invariante a la escala" : M
let casos_justifican = "40 casos justifican operativamente el marco" : J
let inductivismo_falaz = "Más casos = más verdad" : I

axiom marcos_son_independientes : (O & E & M) -> G
axiom casos_no_constituyen_tesis : J -> !(J <-> G)
axiom rechazo_inductivismo : !I
axiom estructura_interna_basta : G -> S

print ""
print "Test 1: los tres marcos son colectivamente la tesis general."
check valid (((O & E & M) & ((O & E & M) -> G)) -> G)

print ""
print "Test 2: la generalidad no depende del tamaño del corpus (no inductivismo)."
check satisfiable (G & !I)
countermodel (G -> I)
analyze {J} -> G
print "(si fuera inducción válida G se seguiría de J solo; NO se sigue)"

print ""
print "Test 3: la generalidad de los 3 marcos es satisfacible sin casos."
check satisfiable (O & E & M & G & !J)
print "(en principio: el marco general podría sostenerse antes del corpus)"

print ""
print "Test 4: el corpus respalda pero NO sustituye la articulación."
print "(la tesis G requiere estructura interna coherente S; sin S la tesis no se sostiene)"
check valid (((G -> S) & G) -> S)
check valid ((G -> S) -> (!S -> !G))
print "(modus tollens: si no hay estructura interna, no hay tesis)"

print ""
print "Test 5: ninguno de los 3 marcos colapsa sobre los otros 2."
check satisfiable (O & !E & !M)
check satisfiable (E & !O & !M)
check satisfiable (M & !O & !E)
countermodel (O -> E)
countermodel (E -> M)
countermodel (M -> O)

print ""
print "Test 6: los 3 marcos son MUTUAMENTE COHERENTES bajo la tesis (sí pueden coexistir)."
check satisfiable (O & E & M)

render theory
print ""
print "=== Fin teoría 15 ==="
