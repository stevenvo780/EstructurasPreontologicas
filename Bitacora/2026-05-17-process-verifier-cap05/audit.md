# Process-verifier cap 05-aplicaciones — auditoría paso por paso
**Fecha:** 2026-05-17  
**Auditor:** process-verifier (Opus 4.7 1M)  
**Alcance:** archivos reales de `05-aplicaciones/` (00, 01, 02, 03, 04, 05, 06, 07)

---

## 0. Discrepancia en el mapeo solicitado

El usuario pidió auditar:
- 01 fisica-y-cuantica
- 02 biologia-y-ecologia
- 03 economia-y-mercados
- 04 cultura-y-cognicion
- 06 tecnologia-y-redes

Pero el directorio contiene en realidad:
- 01 mente-memoria-yo
- 02 biologia-y-ecologia
- 03 sistemas-tecnicos-distribuidos
- 04 instituciones-mercado-y-estado
- 05 dinamica-conductual-Warren (caso ancla)
- 06 corpus-multiescala (no figura en la lista pedida)
- 07 mapa-aplicaciones-corpus

No existe capítulo dedicado a física/cuántica como aplicación filosófica autónoma; el dominio cuántico aparece sólo en el corpus inter-escala (§06 + casos 31, 32). No existe capítulo "cultura-y-cognición" agregado. No existe capítulo "economía-y-mercados" autónomo (el dominio se trata bajo "Instituciones, mercado y Estado").

**Hallazgo H0 (estructural).** La lista pedida no coincide con la estructura efectiva del manuscrito. Auditamos lo que existe.

---

## 1. Tabla de auditoría paso por paso

| Paso | Archivo | Modo declarado | Coherencia con criterios §00 | Necesario | Transición al siguiente |
|---|---|---|---|---|---|
| §00 | 00-criterios-de-admision.md | metateoría | Establece 14 componentes demostrativos + 9 programáticos. **Auto-declara genealogía post-hoc** (Lakatos: ad hoc rescue tipo 3, líneas 10). | Sí, ancla todo el capítulo | Anuncia inventario; coherente |
| §01 | 01-mente-memoria-yo.md | PROGRAMÁTICO | Marcado §00. Cumple §6 (5 preguntas). §7-8 (qualia, libertad) introduce engagement Chalmers/Frankfurt/Pereboom NO previsto en §00 inventario. | Sí | Salta a biología sin puente narrativo |
| §02 | 02-biologia-y-ecologia.md | PROGRAMÁTICO | Marcado §00. Introduce §0 "Qué es vida" (cinco condiciones autopoiéticas) — categoría **no derivada de criterios §00**, importada de Maturana-Varela + Schrödinger. Cumple §6 mínimo. | Parcialmente: §0 es expansión teórica adicional | Continuidad razonable |
| §03 | 03-sistemas-tecnicos-distribuidos.md | PROGRAMÁTICO | Marcado §00. Cumple §6. Pero **§6.3 SRE-Beyer es deuda F05-12 declarada** (homologías sin formalizar, cap.22 vs cap.4 confundidos). | Sí | Transición ok |
| §04 | 04-instituciones-mercado-y-estado.md | PROGRAMÁTICO ACOTADO | Marcado §00 con variante "acotado" no prevista en §00 (introduce subcategoría ad-hoc). §6 cumplido. Engagement Searle/Bourdieu/North robusto. §7.1 caso piloto COVID OxCGRT **fetch pendiente** declarado. | Sí | Transición al ancla §05 abrupta |
| §05 | 05-dinamica-conductual-Warren.md | DEMOSTRATIVO | Único caso demostrativo. Auto-declara que los 14 componentes §00 fueron extraídos de este caso (genealogía circular declarada). Engagement Warren verbatim. §"Aclaración terminológica" distingue r²=0.98 (Fajen-Warren intra-muestra) vs EDI=0.262 (caso 30). | Sí, es la prueba | Transición a §06 ok |
| §06 | 06-corpus-multiescala.md | DEMOSTRATIVO EMPÍRICO | NO está marcado con etiqueta §00. Reporta 7 strong + 1 weak + 1 null + 1 failure mode (10 casos inter-escala). Datos sintéticos declarados. | Sí | Transición a §07 ok |
| §07 | 07-mapa-aplicaciones-corpus.md | MAPA INTEGRADOR | Agrega 40 casos (30 inter-dominio + 10 inter-escala). | Sí | — |

---

## 2. Respuesta a las tres preguntas hostiles

### (a) ¿Hay casos del corpus mencionados en algún subcapítulo SIN figurar en §07?

**SÍ — hallazgos H1-H3.**

- **H1.** §02 (biología) §0.3 menciona "Casos del corpus inter-escala (33 Villin, 34 MM, 35 ciclo celular, 36 NF-κB)". Los cuatro **sí figuran** en §07 Tabla 5.7.2. OK.
- **H2.** §03 (sistemas técnicos) §4 cita "datasets de Google Borg, traces de Microsoft Azure". **No son casos del corpus** (son candidatos futuros). OK formal.
- **H3.** §05 (Warren) Caso 1 cita "Sternad, Duarte, Katsumata y Schaal 2001" como evidencia secundaria. No es caso del corpus, pero §05 menciona "caso 30" (behavioral_dynamics) implícitamente; aparece en §07 Bloque III Weak. OK.
- **H4 CRÍTICO.** §01 (mente) §6.1 menciona "Dennett — patrones reales y centro de gravedad narrativo" y §7.2 cita Chalmers 1995. Estas figuras son ricamente engaged pero **ningún caso EDI del corpus** instancia mente/conciencia. §07 dice explícitamente *"El caso 30 NO cuenta como elevación parcial de este capítulo"*. Coherente y declarado. OK.

**Resultado:** no hay casos del corpus mencionados sin figurar en §07. La coherencia bibliográfica es buena.

### (b) ¿Algún criterio del §00 contradice una clasificación del §07?

**SÍ — hallazgos H5-H7.**

- **H5.** §00 §1 exige para modo demostrativo "14 componentes con contenido sustantivo" + "comparación rival con tabla de discriminación". §07 Bloque I Strong promueve caso 18 (Urbanización) a Strong tras re-ejecución. Caso 18 **NO tiene dossier de 14 componentes ni aparece como demostrativo en §05-00**: tiene `metrics.json`. La nota interna del propio §07 lo aclara: *"Modo técnico-ejecutado ≠ demostración positiva del aparato"*. Esto **resuelve la aparente contradicción declarándola explícitamente**, pero la nomenclatura "Strong" + "overall_pass=True" induce a leerlo como demostrativo. **WARN_BROKEN_STEP soft**: nomenclatura ambigua resuelta por aclaración.
- **H6.** §00 §3.3 (vigilancia contra sustitución nominal) exige que el modo programático **articule diferencia respecto al lenguaje ordinario**. §01 §1.7 ("`mente` se admite como compresión legítima en S si el dossier completo se construye") es **condicional contrafáctico**: no demuestra elevación, sólo promete. Coherente con modo programático pero raya el incumplimiento de §00 §3.3.
- **H7 CRÍTICO.** §00 §1 punto 14 exige "Comparación rival con tabla de discriminación". §04 (instituciones) §6 hace engagement extenso con Searle/Bourdieu/North/Latour/Gilbert/Bunge **pero NO hay tabla comparativa** rival. §05 (Warren) sí tiene comparación rival (modelos internos, cognitivismo, conductismo). Como §04 es programático no demostrativo, no es violación dura, pero §00 §6 también pide a programáticos identificar "rival principal" — esto **sí está** en §04 §6.1 (Searle como fricción) y §2.4 (rival de mercado).

### (c) ¿El §05 Warren cumple TODOS los criterios del §00?

**Verificación componente por componente (14 puntos):**

| # | Componente §00 | Presente en §05 | Evidencia |
|---|---|---|---|
| 1 | Pregunta Q fechada con tolerancia | Parcial | §"Q" pregunta cualitativa; **no fecha ni tolerancia τ explícita** |
| 2 | Variables X operacionalizadas | Sí | §"Sistema de variables": e, a, i, tarea, históricas |
| 3 | Sustrato material instanciante | Sí | Sistema acoplado agente-entorno-tarea |
| 4 | Grafo G con criterios de admisión | Parcial | Ecuaciones acopladas declaradas; criterios de admisión de aristas por intervención **no explícitos** |
| 5 | Hipergrafo H si procede | NO aplica explícitamente | No se justifica no-reducibilidad a pares |
| 6 | Compresión κ con dimensionalidad efectiva | Sí | Reducción a `ẋ=Ω(x,r)` |
| 7 | Atractores, repulsores, bifurcaciones | Sí | Casos 1-4 ilustran cada uno |
| 8 | Pruebas de validación (4 tipos) | Parcial | r²>0.97 reportado; cross-validation **ausente** (deuda F05-07 declarada) |
| 9 | Predicción discriminante contra rival | Sí | §"Comparación con marcos rivales" |
| 10 | Intervención discriminante | Parcial | Oclusión óptica mencionada vía Wallis 2002/Hildreth 2000 como **mención secundaria BORRADOR-IA** |
| 11 | Operador ε con protocolo de reapertura | NO | No hay protocolo ε explícito |
| 12 | Traducción B↔L3 completa | Sí | §2 caso palo invertido: "cada parámetro se traduce a variable medible" |
| 13 | Limitaciones declaradas | Sí | §"Casos de presión" + §"Lo que este caso no demuestra" |
| 14 | Comparación rival con tabla | Sí | Tabla 5.5.1 + §"Comparación con marcos rivales" |

**Resultado:** §05 cumple ~9/14 componentes plenamente, ~4/14 parcialmente, 1 ausente (operador ε). El propio §00 declara que **el dossier fue retroconstruido a partir de §05** (genealogía post-hoc, líneas 10), lo cual hace circular la verificación: la rejilla evaluativa fue diseñada para que §05 la cumpliese. **El propio manuscrito reconoce esta circularidad como ad hoc rescue tipo 3 lakatosiano.** Honesto pero estructuralmente débil.

---

## 3. Términos huérfanos entre subcapítulos

- **"realismo estructural moderado"** aparece en §05 sin definición en §00; sí está en glosario (`00-proyecto/07-glosario-operativo.md`) — coherente.
- **"causalidad circular"** §05 §"Lo que esto aporta" — sin referencia interna a otros capítulos.
- **"behavioral dynamics"** se usa como sinónimo de §05 + caso 30 EDI; §07 §"behavioral dynamics como caso bisagra" declara explícitamente la complementariedad.
- **"self-organization"** anclado correctamente en §02 §0 (Maturana-Varela) y §05 §"Lo que aporta" (Maturana-Varela + Haken). Coherente con regla `thesis-prose.md`.
- **"sustitución nominal"** §00 §3.3 + §05 §"Cognitivismo computacional" + §01 §6.5 (Searle). Coherente.

---

## 4. Saltos críticos detectados (resumen)

1. **H4 (resuelto declarado):** §07 declara explícitamente que caso 30 NO cuenta como elevación de §01. Esto es honestidad ejemplar.
2. **H5 (WARN soft):** nomenclatura "Strong/overall_pass=True" en §07 puede leerse como "demostrativo §00" aunque §07 aclara que NO lo es.
3. **H7 (criterio parcial):** §00 §6 cumplido en §04, pero la tabla rival ausente.
4. **Circularidad §00 ↔ §05:** los 14 componentes son retro-extraídos de §05. Declarado como ad hoc rescue. **Es honesto pero debilita la rejilla.**
5. **Genealogía declarada del propio §00:** este es el hallazgo más sustantivo. La rejilla evaluativa **no es independiente** del caso que evalúa.

---

## 5. Diagnóstico final

- **Coherencia interna §00 → §01-04:** alta. Cada capítulo declara modo programático en primer párrafo, cumple §6 (5 preguntas), incluye "Deuda residual" fechada.
- **Coherencia §00 → §05 (caso ancla):** estructuralmente circular, declarada honestamente como ad hoc rescue tipo 3.
- **Coherencia §06 + §07 con §00:** §06 introduce "demostración empírica multiescalar" que **no está prevista en §00** (que sólo contemplaba un demostrativo: Warren). §07 navega la tensión distinguiendo "modo técnico-ejecutado" vs "modo demostrativo §00 estricto" — solución correcta pero la distinción **no aparece en §00**.

**Veredicto:** los 8 capítulos son internamente consistentes y honestamente etiquetados, con dos costos estructurales declarados: (1) la rejilla §00 es post-hoc al ancla §05; (2) la categoría "modo técnico-ejecutado" usada en §07 no está prevista en §00 y debería incorporarse al inventario §00 §4 como modo intermedio.

**Recomendación de reparación:**
- añadir a §00 §4 una tercera categoría "modo técnico-ejecutado (EDI sin dossier de 14 componentes)" para que §06+§07 hereden cobertura formal de §00.
- declarar en §00 §1 la genealogía post-hoc de los 14 componentes ya está hecho (líneas 10), no requiere reparación.
