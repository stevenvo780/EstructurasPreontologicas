# Process-verifier — Auditoría final integrada manuscrito post 16 iteraciones

Fecha: 2026-05-17
Alcance: cap 00 → cap 06 ensamblado, con foco en consistencia post-iter-13/15 (bug detrended fix + reclasificaciones + 5 capas BORRADOR-IA).
Inputs revisados: `00-proyecto/05-resumen-y-abstract.md`, `06-cierre/01-conclusion-demostrativa.md`, `09-simulaciones-edi/{16,21,24,30}/outputs/metrics.json`, audits previos `2026-05-17-process-verifier-cap00-01/` y `cap02-a-06-final/`.

## Tabla pasos del hilo argumental cap 00 → cap 06

| paso | claim | sustained | necesario | transición |
|------|-------|-----------|-----------|-----------|
| P1 (00-05 abstract callout iter 13 ES línea 3) | Conteo Strong baja 8→1 robusto + [0..3] revisión tras fix bug detrended | OK estructura; **NOT-OK numérico** (EDI=0.806 no aparece en `metrics.json` ni `metrics_enriched_v5_2.json` de caso 24) | sí | a P2 (cuerpo abstract) — **transición ROTA**: el callout dice "1 Strong" pero el cuerpo §línea 15 sigue diciendo "8 strong con `overall_pass`" |
| P2 (00-05 cuerpo línea 15 ES + línea 41 EN) | Corpus inter-dominio: 8 strong con `overall_pass` (lista 18, 24, 30, 21 +...) | NOT-OK: contradice directamente P1; conteos iter-11 archivados sin marca [HISTÓRICO PRE-FIX] | NO (debería estar reescrito o marcado como obsoleto) | rota — coexistencia de dos conteos sin disambiguación |
| P3 (00-05 nota epistemológica línea 29 + 06-01 línea 9) | Pre-registros son lock-ins post-hoc (Gelman-Loken), no pre-registros genuinos ex ante | OK con cita verbatim p.460 + p.464 + PRE_REGISTRO_README.md:41 | sí | OK → P4 |
| P4 (06-01 callout iter 13 línea 5) | Solo caso 24 Microplásticos sobrevive Strong robusto (EDI=0.806, p_block=0.001) | **NOT-OK numérico**: vanilla `metrics.json` muestra EDI=0.076 (synthetic) y EDI=-1.0 (real `valid=false`); `metrics_enriched_v5_2.json` muestra EDI=0.7819, p_block=0.0003. No hay JSON que produzca 0.806/0.001/0.332. | sí | a P5 — **transición ROTA** por incoherencia con JSON canónico |
| P5 (06-01 línea 79 cómputo agregado iter 11) | 8 strong gate completo + 1 sin gate + 5 weak (...) post-iter-11 | NOT-OK: declaración iter 11 sin marca [HISTÓRICO PRE-FIX iter 13], coexiste con P4 sin disambiguación | NO en su forma actual | rota — duplicidad de conteos competitivos |
| P6 (06-01 §3 línea 43 Cond 4) | Correspondencia nominal, no medición independiente (reparación BROKEN_STEP iter 1) | OK (audit previo verificó) | sí | OK → P7 |
| P7 (06-01 Tabla 6.1.1 línea 57) | Strong robusto = 1 (Microplásticos EDI=0.806, p_perm=0.0, p_block=0.001, detrended=0.332) | NOT-OK numérico (idéntico a P4) | sí | a P8 OK estructuralmente, pero cifras no reproducibles |
| P8 (06-01 §5 detalle bug iter 13 punto 1-2) | Fix `hybrid_validator.py:1810-1843`; block-perm Politis & White 2004 | OK con paths a archivo + cita | sí | OK → P9 cierre |
| P9 (06-01 línea 290 cierre) | 8 strong con `overall_pass` macro + 7 strong inter-escala = lectura ontológica de instancias | NOT-OK: persiste "8 con `overall_pass` macro" que el callout iter 13 dice que es artefacto | NO en forma actual | rota |

## 7 hallazgos prioritarios

### Hallazgo 1 — INCONSISTENCIA NUMÉRICA CRÍTICA: EDI=0.806 no reproducible
**Severidad: CRÍTICA — bloqueante para defensa.** El abstract (ES línea 3 + EN línea 5) y el cap 06-01 (líneas 5, 57, 75) afirman caso 24 Microplásticos con `EDI=0.806, p_block=0.001, detrended_edi=0.332`. La verificación directa contra `09-simulaciones-edi/24_caso_microplasticos/outputs/metrics.json` muestra:
- Fase synthetic: `edi.value = 0.07596`
- Fase real: `edi.value = -1.0` con `valid=false`
- `metrics_enriched_v5_2.json`: `edi_canonical = 0.7818771547395869`, `p_block = 0.0003333`

NINGUNA fuente produce 0.806, 0.001 ni 0.332. La cifra `0.806` aparece en >10 lugares (abstract ES, EN, cap 06-01 líneas 5/57/75/79-sub) sin trazabilidad reproducible. **Viola la Regla 3 del CLAUDE.md: "Cada cifra reproducible con un comando".**

Repair propuesto: o (a) re-ejecutar caso 24 con perfil agresivo + block-perm activado y publicar metrics.json que reproduzca 0.806; o (b) corregir el manuscrito a `EDI=0.7819, p_block=0.0003` (la cifra del enriched_v5_2.json).

### Hallazgo 2 — COEXISTENCIA DE DOS CONTEOS COMPETITIVOS SIN DISAMBIGUACIÓN
**Severidad: ALTA.** El callout iter 13 (abstract línea 3, cap 06-01 línea 5) declara "1 Strong robusto + [0..3] en revisión". El cuerpo del abstract (línea 15) y el cap 06-01 línea 79/línea 290 mantienen "8 strong con `overall_pass`" sin marca explícita de `[HISTÓRICO PRE-FIX iter 13]`. Para Ricardo (lector externo): la pregunta "¿cuántos strong tiene el corpus?" admite dos respuestas opuestas en el mismo manuscrito sin disambiguación visual.

La línea 7 cap 06-01 declara genéricamente que "la formulación canónica del párrafo anterior permanece vigente mientras Jacob no firme", pero esto es **antes** del callout iter 13. El callout iter 13 (línea 5) y la nota iter 11 (línea 9) coexisten sin orden de precedencia explícito.

Repair: insertar en cada bloque iter 11 una etiqueta visual `[FORMULACIÓN PRE-FIX iter 13 — ver línea 5 para conteo vigente]` o reescribir el cuerpo del abstract.

### Hallazgo 3 — 5 PRE-REGISTROS POST-HOC AUTOCONFESOS — declaración OK pero fricción de lectura
**Severidad: MODERADA.** La nota línea 9 cap 06-01 + nota línea 29 abstract declaran honestamente que los 5 "pre-registros" (10, 15, 21, 23, 28) son lock-ins post-hoc per `PRE_REGISTRO_README.md:41` + Gelman-Loken 2014 p.460/p.464 (citas verbatim verificadas en audit cap02-06). La defensa por proceso ("auto-detección del bug") está documentada pero ENTRELAZADA con los 5 lock-ins post-hoc en el mismo párrafo de ~750 palabras (audit previo Hallazgo 5).

Para un revisor estadístico hostil: la combinación "auto-detección bug + lock-ins post-hoc" puede leerse como "el aparato declara su honestidad pero sus 5 pre-registros son retroactivos". La declaración OK pero la lectura externa requiere fragmentación.

Repair: separar en (a) Nota sobre bug detrended (auto-detección como virtud), (b) Nota sobre lock-ins post-hoc (limitación reconocida); hoy van en un solo bloque.

### Hallazgo 4 — Opción (c) suave/endurecida: 1 instancia, no 5
**Severidad: BAJA.** El prompt menciona "5 lugares donde aparece opción (c) suave/endurecida". El grep encuentra `opción (c)` en 1 lugar canónico (cap 06-01 línea 7) + 1 referencia cruzada (cap 05-00 línea 84 según audit previo). NO aparece en abstract, cap 03, cap 04. No hay riesgo de inconsistencia múltiple — el riesgo es la opacidad de la marca "opción (c)" para un lector que no conoce el historial iter.

Repair: si "opción (c)" se mantiene como código interno, glosarla la primera vez que aparece.

### Hallazgo 5 — Distribución BORRADOR-IA: 16 en cap 06-01, 2 en abstract, 2 en cap 03, 0 en cap 04 — concentración cierre
**Severidad: BAJA estructuralmente, MODERADA para legibilidad.** Cap 06-01 acumula 16 marcadores `BORRADOR-IA pendiente firma H-J*`, concentrados en §1 (4), §3 (1), §5 (5), §4.5 (3), §cierre (3). El audit previo cap02-06 ya marcó esto como "esperable porque el cierre integra capas". Sin embargo, el conteo 16 sugiere que el cap 06-01 NO es texto firmado por Jacob — es un palimpsesto de borradores IA esperando firma. Defendible si Ricardo lo lee como "manuscrito en revisión activa"; problemático si lo lee como "tesis lista".

Repair: en preamble del cap 06-01 declarar explícitamente "16 bloques BORRADOR-IA pendientes firma H-J* — capítulo en revisión activa, firma autoral pendiente".

### Hallazgo 6 — Casos reclasificados iter 11 NO actualizados en cuerpo abstract
**Severidad: ALTA.** El callout iter 13 dice "Casos reclasificados a NULL/Weak: 16, 17, 18, 21". El cuerpo abstract sigue listando caso 18 Urbanización como "promovido Weak→Strong iter 5 con `overall_pass=True`" y caso 21 Salinización como "promovido Null→Strong iter 11". Esto es contradicción directa — el caso 21 está reclasificado a NULL por el fix Y promovido a Strong por iter 11, en el mismo abstract.

Verificación numérica: `21/outputs/metrics.json` muestra EDI=0.515 (raw) que coincide con la promoción iter 11. Pero el callout iter 13 dice "raw 0.515 → detrended 0.001" que lo reclasifica a NULL. **Ambas afirmaciones son verdaderas bajo distintas métricas (raw vs detrended)** — pero el manuscrito no disambigua. Para Ricardo es contradicción aparente.

Repair: en cuerpo abstract sustituir cada EDI por par `(raw=X, detrended=Y, p_block=Z)`; sin detrended la cifra raw es engañosa post-fix iter 13.

### Hallazgo 7 — "Auto-detección bug = defensa por proceso": documentación parcial
**Severidad: MODERADA.** El cap 06-01 §5 punto 1 documenta el bug (`hybrid_validator.py:1810-1843`), su naturaleza algebraica (detrend no-op), y el fix. Documenta también el efecto sobre 4 strong (16, 17, 18, 21) + 2 block-perm (26, 30) + 5 iter-15 (09, 12, 14, 27, 23). Lo que NO documenta explícitamente para un revisor estadístico hostil:
- (a) ¿Por qué el bug pasó iter 1–12 sin detección? (12 iteraciones del loop sin detectar un no-op algebraico en `detrended_edi` es razonable explicar.)
- (b) ¿Qué garantiza que NO hay otros bugs análogos en el resto de `hybrid_validator.py`? (Audit defensivo: ¿se hizo grep de patrones similares?)
- (c) ¿La nueva métrica `detrended_edi` se validó contra simulación controlada con tendencia lineal conocida? (Para confirmar que el fix es correcto.)

Repair: añadir subsección "§5.bis Audit defensivo post-fix" con respuesta a (a), (b), (c). Sin esto, "defensa por proceso" se sostiene narrativamente pero no resiste revisión estadística hostil.

## Diagnóstico final

**CADENA NO COHERENTE PARA LECTOR EXTERNO.** Marca **WARN_BROKEN_STEP** en P1, P2, P4, P5, P7, P9 con dos sub-problemas:

1. **Inconsistencia numérica P4/P7**: la cifra `EDI=0.806` para Microplásticos NO reproducible contra `metrics.json` actual. Fuentes encontradas: 0.076 (synthetic), -1.0 (real valid=false), 0.7819 (enriched_v5_2). Hallazgo 1 bloqueante para defensa.

2. **Coexistencia conteos competitivos P2/P5/P9**: "8 strong" iter 11 coexiste con "1 strong" iter 13 sin disambiguación. Hallazgo 2 + 6 bloquean lectura externa.

**Para Ricardo:** la cadena P1→P9 NO es legible coherentemente sin que él lea las 5 capas BORRADOR-IA en orden cronológico inverso. La frase canónica "1 Strong robusto definitivo (Microplásticos)" es defendible si el manuscrito declara que TODOS los conteos previos están archivados como históricos — hoy no lo declara visualmente.

**Reparación mínima viable (24h):**
- (R1) Re-ejecutar caso 24 microplásticos con perfil agresivo + block-perm + dump arrays; publicar metrics.json reproducible que dé 0.806 — o corregir manuscrito a 0.7819.
- (R2) Insertar etiquetas `[HISTÓRICO PRE-FIX iter 13]` en cuerpo abstract línea 15 y cap 06-01 líneas 79, 290.
- (R3) Glosario primera aparición de "opción (c)".
- (R4) Sub-bullets en nota línea 9 cap 06-01 (Hallazgo 3 audit previo).

**Reparación profunda (post-firma H-J):**
- (R5) Re-ejecutar B-T2.1 con pre-registro genuino ex ante para 16 Deforestación + 17 Océanos + 18 Urbanización + 21 Salinización (los 4 reclasificados con datos refrescados).
- (R6) Audit defensivo `hybrid_validator.py` para descartar bugs análogos (Hallazgo 7.b).
- (R7) Validar el fix `detrended_edi` contra simulación con tendencia conocida (Hallazgo 7.c).

**Veredicto:** la conclusión "1 Strong robusto + corpus en revisión sistemática" ES sostenible filosóficamente como "defensa por proceso" + "honestidad operativa del aparato", pero ACTUALMENTE el manuscrito no la sostiene operativamente porque (i) la cifra EDI=0.806 no se reproduce contra el JSON canónico y (ii) los conteos competitivos coexisten sin disambiguación. Esto es **textual reward hacking parcial**: la conclusión iter 13 es honesta, pero los pasos intermedios (cuerpo abstract, cap 06-01 línea 79, línea 290) no se actualizaron en armonía. La reescritura es local (R1-R4), no estructural.
