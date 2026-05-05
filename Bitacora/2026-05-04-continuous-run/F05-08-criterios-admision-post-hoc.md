# F05-08 — 14 criterios de admisión diseñados post-hoc leyendo Warren

**Fecha:** 2026-05-05
**Origen:** adversarial-reviewer cap05 (2026-05-05)
**Archivos afectados:**
- `05-aplicaciones/00-criterios-de-admision.md` (líneas 10-25)
- `05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md`
- `05-aplicaciones/07-mapa-aplicaciones-corpus.md` (líneas 11, 17)

## (a) Verificación de la afirmación

**Afirmación adversarial (Lakatos ad hoc rescue):**
los 14 componentes del *dossier de anclaje* (cap 05-00 §1, vv. 1-14) coinciden punto por punto con los elementos que Warren (2006) ya provee — variables operacionalizadas, ecuaciones diferenciales ajustadas, atractores/bifurcaciones identificados, predicciones, intervenciones, comparación rival, traducción B↔L3, limitaciones declaradas. Por construcción el caso ancla 05-05 satisface el criterio porque el criterio fue diseñado leyéndolo.

**Mapeo verificado uno-a-uno (criterio del cap 05-00 → fuente literal en cap 05-05):**

| Criterio §1 (00) | Frase/sección concreta en 05-05 que lo satisface |
|---|---|
| 1. Pregunta Q fechada con tolerancia | §"Q (la pregunta explicativa)" lín. 25-27 |
| 2. Variables X operacionalizadas | §"El sistema de variables (el dossier de anclaje)" lín. 44-75 |
| 3. Sustrato material instanciante | §"Variables del agente / entorno / informacionales" lín. 48-66 |
| 4. Grafo G con aristas verificadas por intervención | §"El sistema acoplado en notación canónica" lín. 78-99 |
| 5. Hipergrafo H si procede | (omitido en 05-05 — el propio cap admite que no procede para este caso) |
| 6. Compresión κ con dimensionalidad efectiva | §"Lectura bajo el marco" en cada caso (1-4); explícito lín. 99-100 |
| 7. Atractores, repulsores, bifurcaciones | §Casos 1-4: "atractor / repulsor / bifurcación tangente" lín. 116, 173, 194-195 |
| 8. Pruebas de validación (4 sub-pruebas) | §"Lo que esto le aporta" + lín. 287 ("varianza explicada > 97%") |
| 9. Predicción discriminante contra rival explícito | §"Comparación con marcos rivales" lín. 226-258 |
| 10. Intervención discriminante | "manipular el flujo óptico cambia el frenado" lín. 175 |
| 11. Operador ε con protocolo de reapertura | §"Casos de presión para la tesis" lín. 260-279 |
| 12. Traducción B↔L3 completa | §"Cómo este caso sostiene la tesis general" lín. 283-291 |
| 13. Limitaciones declaradas | §"Lo que este caso no demuestra" lín. 293-295 + lín. 206 |
| 14. Comparación rival con tabla de discriminación | Tabla 5.5.1 lín. 213-225 |

**Conclusión:** la afirmación adversarial es **estructuralmente correcta**. El cap 05-00 §1 enumera los 14 componentes en el orden y con la granularidad exactos que el cap 05-05 ya despliega. No hay un solo criterio en la lista que el caso ancla no satisfaga sin esfuerzo de adecuación. La marca textual de circularidad está además explícita en la propia bitácora del cap 05-00 lín. 71 (`requires: H-J*`): la cita de Warren se introduce *para fundar* el caso ancla, no como criterio independiente.

**Esto es la definición de Lakatos de ad hoc rescue tipo 3 (Lakatos 1970, p. 175 — *needs_human* para citación literal):** una hipótesis modificada para acomodar un caso problemático, donde el contenido empírico añadido coincide exactamente con el caso que motivó la modificación. Aquí: los criterios de admisión se diseñan leyendo el caso ancla, garantizando que solo el caso ancla los satisface.

## Contradicción 00 vs 05-05 vs 07 (verificada)

Lectura cruzada:
- `05-00` lín. 67-71: **único** caso demostrativo = 05-05 (Warren).
- `05-05` lín. 5: *"el único caso del manuscrito que entra en modo demostrativo"*.
- `05-07` lín. 17: **30 casos** "Modo demostrativo (con dossier completo)".

Las dos tablas (5.0.1 y 5.7.1) usan el término "demostrativo" con extensiones incompatibles. F05-09 (esta misma carpeta) ya documentó la equivocidad léxica en 05-07. Aquí se confirma una segunda contradicción más severa: **el criterio de 05-00 fija un único demostrativo (05-05), mientras 05-07 cuenta 30**. No es solo equivocidad — es contradicción extensional directa entre dos capítulos vecinos.

## Aplicación de los 14 criterios a 5 casos EDI muestreados

Muestra: 16 (deforestación, strong), 04 (energía, strong), 05 (políticas, weak), 23 (acuíferos, EDI=−1.00), 30 (behavioral dynamics, weak — comparable a 05-05).

Tabla pase/falla por componente (verificación de aplicabilidad del criterio §1 de 00, sin re-correr validate.py — basada en metrics.json y case_config.json existentes):

| # | Criterio | 16 | 04 | 05 | 23 | 30 |
|---|----------|:--:|:--:|:--:|:--:|:--:|
| 1 | Q fechada + tolerancia τ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | X operacionalizadas | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | Sustrato material descrito | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | Grafo G con aristas verificadas por intervención | ⚠ (proxy) | ⚠ (proxy) | ⚠ | ✗ | ⚠ |
| 5 | Hipergrafo H justificado | n/a | n/a | n/a | n/a | n/a |
| 6 | κ con dimensionalidad efectiva justificada | ✓ | ✓ | ⚠ | ⚠ | ✓ |
| 7 | Atractores/bifurcaciones identificados en datos | ⚠ | ⚠ | ✗ | ✗ | ⚠ |
| 8 | 4 sub-pruebas (reproducción, gen., topología, intervención) | ✓ | ✓ | parcial | ✗ | parcial |
| 9 | Predicción discriminante contra rival explícito | ✗ | ✗ | ✗ | ✗ | ✗ |
| 10 | Intervención discriminante ejecutada | ✗ (ablación ODE no es intervención sobre el sistema real) | ✗ | ✗ | ✗ | ✗ |
| 11 | Operador ε con protocolo de reapertura | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |
| 12 | Traducción B↔L3 completa parámetro a parámetro | ✗ | ✗ | ✗ | ✗ | ⚠ |
| 13 | Limitaciones declaradas con régimen no aplicable | ✓ | ✓ | ✓ | ✓ (caso null asume no-aplicabilidad) | ✓ |
| 14 | Comparación rival con tabla de discriminación | parcial (baselines.py vs ARIMA/VAR) | parcial | parcial | n/a | parcial |

**Conteo de criterios pasados con contenido sustantivo (✓):** 16→6/14, 04→6/14, 05→4/14, 23→3/14, 30→6/14.
**Conteo en 05-05 Warren:** 13/14 (omite #5 hipergrafo legítimamente).

**Diagnóstico cuantitativo:** ningún caso EDI muestreado alcanza el umbral del caso ancla. La distancia (~7 criterios) es sistemática y no aleatoria: los criterios que fallan son los mismos (4, 7, 9, 10, 12) — exactamente aquellos donde Warren provee material publicado independiente del aparato EDI.

**Conclusión operativa:** la afirmación de 05-07 lín. 17 (*"30 casos modo demostrativo"*) es falsa según el criterio del propio cap 05-00 §1. Los casos EDI tienen *dossier técnico ejecutado* (metrics.json reproducible), pero NO satisfacen los 14 componentes del dossier de anclaje. Solo Warren los satisface — porque el criterio se construyó sobre Warren.

## (b) Propuesta de edición — needs_human (firma Jacob)

La contradicción 00 vs 07 sumada al ad hoc rescue de los 14 criterios obliga a una decisión filosófica que **no puede tomar la asistencia**:

**Opción A — Asumir el ad hoc y declararlo:**
Mantener los 14 criterios pero añadir en cap 05-00 §1 una nota *"Estos componentes fueron extraídos como abstracción del caso ancla 05-05 (Warren 2006). La adecuación del caso ancla al criterio es por construcción y no constituye evidencia independiente de la potencia del marco. Los demás dominios entran en modo programático no porque sean ontológicamente menos firmes, sino porque carecen de un caso paradigmático con las 14 dimensiones desarrolladas independientemente."*
Costo: la tesis admite que su único caso demostrativo es circular. Honestidad metodológica máxima; impacto retórico mínimo.

**Opción B — Sustituir los 14 criterios por una versión independiente del aparato:**
Reformular §1 de 00 con criterios derivados de filosofía de la ciencia (Hempel-Lakatos-Worrall) sin referencia a Warren. Re-evaluar 05-05 contra el nuevo criterio y aceptar que pueda fallar parcialmente.
Costo: trabajo filosófico mayor; riesgo de que el caso ancla pierda estatus.

**Opción C — Reducir 14 a un subconjunto verdaderamente discriminante (~5-7):**
Eliminar criterios redundantes (3 está implícito en 2; 5 es opcional; 11-12 solapan con 8). Quedarse con: Q operacionalizada / X medidas públicamente / atractor identificado en datos / predicción cumplida con rival / intervención ejecutada. Aplicar el subconjunto a los 5 casos EDI muestreados y a 05-05.
Costo: requiere recalibrar también el cap 05-07 y las tablas A.5.1-A.5.2.

**Resolución de la contradicción 00 vs 07:** independientemente de A/B/C, la línea 17 de 05-07 debe corregirse. Edit textual mínimo seguro:
- Reemplazar *"Modo demostrativo (con dossier completo): 30 casos"* por *"Modo técnico-ejecutado (dossier EDI completo, no equivalente a demostrativo en el sentido de 05-00 §1): 30 casos. Demostrativo en sentido estricto (14/14 componentes del dossier de anclaje): 1 caso (05-05 Warren)."*

Esta edición textual está alineada con la propuesta de F05-09 y debería aplicarse en una sola pasada coordinada.

## (c) Costo argumentativo declarado

Aceptar la objeción tiene costo retórico alto:
1. La tesis pasa de *"30 demostrativos en 7 dominios"* a *"1 demostrativo + 30 ejecuciones técnicas + 4 programáticos"*.
2. El único demostrativo es además circular (criterio diseñado leyendo el caso).
3. La defensa oral debe explicitar que el aparato EDI (validate.py + C1-C5) no equivale al dossier de anclaje filosófico — son dos verificaciones distintas con dos extensiones distintas.

**Costo de NO corregir:** flanco abierto a una objeción Lakatosiana directa: *"sus 14 criterios son una racionalización post-hoc del único caso que tienen; por eso solo ese lo satisface"*. Esa objeción es correcta según la verificación arriba; no responderla en el manuscrito la deja para la defensa, donde será más cara.

**Beneficio de corregir:** la tesis gana defensibilidad. Asumir el ad hoc y reformularlo (opción A o C) convierte una vulnerabilidad oculta en una concesión declarada — que es lo que CLAUDE.md §3 pide explícitamente.

## Marca de cierre

**Estado:** `needs_human` — opciones A/B/C requieren firma Jacob.
**Acción asistencia segura:** propuesta textual mínima coordinada con F05-09 lista para validación humana.
**No editado:** Tesis.md, metrics.json, 05-aplicaciones/00-criterios-de-admision.md, 05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md, 05-aplicaciones/07-mapa-aplicaciones-corpus.md.
**Citación pendiente:** Lakatos (1970) "Falsification and the Methodology of Scientific Research Programmes" — paginación literal sobre ad hoc rescue tipo 3 a verificar contra `07-bibliografia/` (cf. CLAUDE.md §5).
