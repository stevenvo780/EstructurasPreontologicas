# Snapshot iteración 4 — loop nocturno

## Hora del snapshot

- **Local:** 2026-05-16 23:49:28 -05
- **UTC:** 2026-05-17 04:49:28 UTC
- **Iteración:** 4 (sucede a `iteracion-3-snapshot.md` de 23:37:58 -05)
- **Delta vs iter 3:** +11m 30s wall-clock

## Harness status (8/8 verificadores)

```
[pass ] harness_compliance
[pass ] citation_pagination
[warn ] decorative_citations
[pass ] prose_against_json
[pass ] replay_hash
[pass ] debt_index
[pass ] self_indulgence
[pass ] consistency_doc_config
```

Comando: `python3 harness/cli.py verify --all`. Sin regresiones vs iter 3. `decorative_citations` sigue `warn` (estado idéntico a iter 3, no aparece en banner top-level pero el campo `status` reporta `warn`; el resto de verificadores `pass`).

## Git

- **Branch:** `harness/fix-orchestration-policy`
- **HEAD:** `22b167f` — *loop nocturno iter 4: hallazgo Ioannidis + downgrades caso 03/13 + Ladyman PNC engagement* (2026-05-16 23:46:51 -05)
- **Commits nuevos desde iter 3 (HEAD anterior `904aeae`):**
  - `5ed3012` *loop nocturno iter 3: 3 downgrades datos reales + engagement Yablo+L&R + PDF re-build* (23:41:25) — recoge el trabajo dirty de iter 3.
  - `22b167f` *loop nocturno iter 4: hallazgo Ioannidis + downgrades caso 03/13 + Ladyman PNC engagement* (23:46:51) — propaga downgrade caso 03, suma caso 13 (Trend Nivel 1) y reescribe 04-04 §1 con engagement Ladyman-Ross PNC.
- **Avance committeado:** 2 commits, 19 archivos tocados en `22b167f` (+1196/−1268 líneas), incluyendo casos 11 y 13 con datos reales (`fetch_real.py` nuevos) y propagación documental del downgrade 03.

### Working tree dirty (no commiteado)

```
M 00-proyecto/05-resumen-y-abstract.md
M 06-cierre/01-conclusion-demostrativa.md
M 09-simulaciones-edi/09_caso_finanzas/outputs/{metrics,primary_arrays,report}.{json,json,md}
?? 09-simulaciones-edi/18_caso_urbanizacion/src/fetch_real.py
```

- 4 archivos modificados + 1 untracked (vs iter 3: 7 mod + 0 untracked).
- `00-proyecto/05-resumen-y-abstract.md` y `06-cierre/01-conclusion-demostrativa.md` contienen ahora **dos bloques BORRADOR-IA explícitos** (uno en cierre, dos en abstract ES/EN) que declaran la reformulación opción (c) endurecida del adversarial, pendientes firma H-J5/H-J6/H-J7. No comitearlos sin firma o aprobación; deben quedar visibles para Jacob.
- `09_caso_finanzas/outputs/*` cambió mtime a 23:49:09 (re-ejecución en curso o auto-trigger). EDI cayó de −0.4051 a −0.6648 (sintético; sigue invalid, no afecta veredicto), C1 pasó True→False. Documentar la re-ejecución o revertir antes del próximo commit.
- `18_caso_urbanizacion/src/fetch_real.py` untracked nuevo: agente B-T2 inició expansión del caso 18 pero no llegó a re-ejecución ni a outputs reales en este ciclo.

## Cobertura B-T2 datos reales (post iter 4)

| Caso | Estado iter 3 | Estado iter 4 | EDI real | Clasificación post B-T2 |
|------|---------------|----------------|----------|--------------------------|
| 01 Clima IPCC | overall_pass=False | sin cambio | −0.0007 | **Null** (Trend→Null en iter 3) |
| 03 Contaminación PM2.5 | overall_pass=False | propagado a tabla 6.1.1 y mapa corpus | −0.0109, CI [−0.075, +0.066] | **Null** (Weak→Null, propagación iter 4) |
| 04 Energía OWID | sin cambio | sin cambio | 0.4615 | **Strong real** |
| 11 Movilidad TomTom | sin re-run real | **Re-ejecutado con TomTom** | 0.0599, p=0.922 | **Trend Nivel 1** (Weak→Trend) |
| 13 Políticas | sin re-run real | **Re-ejecutado con datos institucionales** | 0.0821, p=0.162 | **Trend Nivel 1** (Weak→Trend) |
| 16 Deforestación WB | sin cambio | sin cambio | 0.5802 (~0.602 baseline) | **Strong real** |
| 18 Urbanización | sin cambio | `fetch_real.py` untracked, sin ejecución | n/d | (pendiente) |
| 19 Acidificación | NULL confirmado iter 3 | **Reclasificado a "falsificación local"** | −0.0047, CI [−0.0054, −0.0041] *excluye cero por izquierda* | **Falsificación local del aparato** (sonda Revelle/calcificadores inadecuada para serie Aloha pH) |
| 20 Kessler NASA | overall_pass=True | sin cambio | 0.6936 | **Strong real** |
| 27 Riesgo Bio WHO | sin cambio | sin cambio | (gate full) | **Strong** (datos reales WHO confirmados) |

- **Convención `dataset_real.csv`:** sigue sin documentarse globalmente (deuda iter 3 aún abierta).
- **`metrics.json` generados:** 32/40 (sin cambio vs iter 3 — caso 18 todavía sin ejecución).
- **Casos B-T2 ejecutados con datos reales (total agregado):** 9 (01, 03, 04, 11, 13, 16, 19, 20, 27); +2 vs iter 3 (11 y 13).

## Hallazgos iter 4

### Conteo por categoría

| Categoría | Conteo | Observación |
|-----------|-------:|--------------|
| `BORRADOR-IA` pendientes firma en cuerpo del manuscrito | **29** hits | Repartidos en 14 archivos. Cap `06-cierre/01-conclusion-demostrativa.md` concentra 8. Nuevo: 1 hit en abstract ES + 1 en abstract EN + 1 en conclusión = 3 nuevos en iter 4. |
| Firmas H-J* únicas referenciadas | 9 (H-J1, H-J3, H-J5..H-J11) | H-J5/6/7 cargan la decisión epistémica mayor (reformulación opción (c)). |
| `WARN_THESIS_VULNERABLE` adversariales abiertos | 2 + 1 | Yablo, Ladyman (WARN); Dennett (CONCESIÓN OBLIGATORIA, no WARN); Goff/Strawson (concesión menor). El hallazgo Ioannidis iter 4 no aparece como WARN explícito porque su salida vive en commit message + cuerpo manuscrito, no en `Bitacora/2026-05-16-adversarial-downgrades/` (directorio vacío). **Debilidad: el documento adversarial citado en chapters no existe en disco.** |
| `BROKEN_STEP` reportados por process-verifier | 0 nuevos en iter 4 | Los 5 saltos detectados en iter 2 (saltos A, B, C críticos) **siguen sin atender** — el agente process-verifier-debates-cierre quedó silencioso de nuevo (directorio existe, vacío). |
| Sub-agentes silenciosos (sin entregable verificable) | 2 (vs 3 en iter 3) | `process-verifier-debates-cierre/` sigue vacío; `engagement-ladyman-ross-pnc/` ahora sí entregó `engagement-lr-pnc.md` (mejora vs iter 3); el directorio `adversarial-downgrades/` está vacío pese a ser citado como evidencia en cap 06-01 y 00-05. |
| Casos re-clasificados en iter 4 | 3 | 03 (Weak→Null propagado), 11 (Weak→Trend), 13 (Weak→Trend), 19 (Null→Falsificación local). |
| Hallazgos críticos nuevos | 1 mayor | **Patrón Ioannidis 2005 Corolario 4 sobre corpus sintético**: flexibilidad analítica documentada en TENG-01/02/04/08 + forcing_scale + ode_alpha + ventana + umbral → PPV inflado por construcción. |

### Comparación iter 3 → iter 4

| Deuda iter 3 | Estado iter 4 |
|--------------|----------------|
| Tres agentes silenciosos (Ladyman, process-verifier, slides) | **Parcial:** Ladyman entregó engagement (`engagement-lr-pnc.md`), aplicado al cap 04-04 §1 con verbatim p.37/p.130 — BORRADOR-IA H-J6 pendiente. Process-verifier sigue silencioso. Slides Marp sigue sin generar. |
| Caso 03 PM2.5 reclasificar a NULL | **Cerrado documentalmente:** propagado a tabla 6.1.1, mapa corpus, abstract ES/EN, defensa corta, resumen Ricardo, borrador respuesta. |
| Saltos A/B/C del process-verifier (iter 2 §1) | **Aún abiertos.** Iter 4 no delegó al sub-agente. |
| Convención `dataset_real.csv` | **Aún abierta.** Sin documentación global; casos 03, 19 con literal; 11, 13 ejecutados con datos reales pero sin renombrar archivo. |
| `Tesis.md`/`Tesis.pdf` dirty pendientes auditoría | **Cerrado parcial:** `Tesis.md` ahora limpio post `5ed3012`/`22b167f`; PDF sigue en 1.6 MB / 413 pp pero `Tesis.pdf` no aparece en working tree dirty actual (re-build en iter 3, no en iter 4). |
| Yablo PDFs faltantes | **Aún abierto.** Cita secundaria persiste. |

### Métricas comparadas

| Métrica | iter 3 | iter 4 | Δ |
|---------|--------|--------|---|
| Verificadores en verde | 8/8 (con warn decorativo) | 8/8 (con warn decorativo) | = |
| HEAD commit | `904aeae` | `22b167f` | +2 commits |
| Working tree mod | 7 | 4 | −3 |
| Working tree untracked | 0 | 1 | +1 (urbanización pendiente) |
| `metrics.json` generados | 32/40 | 32/40 | = |
| Casos B-T2 ejecutados con datos reales | 7 | 9 | +2 (11, 13) |
| Casos B-T2 `overall_pass=True` real | 1 (20) | 1 (20) + 2 strong real sin gate complete (04, 16) + 1 strong gate complete (27) → **3 strong reales** | dependiente de auditoría |
| Casos reclasificados (acumulado iter 1→4) | 5 | 8 | +3 |
| Falsificaciones locales del aparato detectadas | 0 | 1 (caso 19) | +1 |
| Tamaño Tesis.pdf | 1632200 B / 413 pp | 1632200 B (sin re-build iter 4) | = |
| H-J* abiertos (etiquetas únicas) | 9 (H-J1..H-J12 mencionadas) | 9 (mismas) | = |
| Sub-agentes silenciosos | 3/8 | 2/8 (process-verifier, slides) | −1 |
| PDFs primarios faltantes | 4 | 4 (Quine, Yablo, Goff, Strawson) | = |

### Hallazgo más serio iter 4

**Patrón Ioannidis 2005 Corolario 4 + reclasificación caso 19 a falsificación local.**

Texto exacto en commit `22b167f`: *"Patrón Ioannidis 2005 Corolario 4 detectado: corpus EDI tiene flexibilidad analítica documentada (TENG-01,02,04,08 + forcing_scale + ode_alpha + ventana + umbral). PPV inflado por construcción flexible. […] Caso 19: EDI=-0.0047 CI=[-0.0054, -0.0041]. CI EXCLUYE CERO por la izquierda. NO es null — es falsificación local del aparato. Llamarlo 'null confirmado' viola ASA principio 5. Tasa downgrade real 28% extrapolada: soporte esperado ≈ 12-13 strong, no 30."*

Implicación operativa: el corpus sintético inter-dominio (30 casos) deja de ser leído como "evidencia ontológica positiva" y pasa a ser **calibración del aparato** (mapeo de cobertura). La evidencia ontológica positiva, bajo lectura honesta endurecida, son los casos B-T2 con datos reales independientes. Al cierre iter 4 esa cuenta es **N=3 strong reales** (Deforestación, Energía, Kessler), 3 nulos genuinos, 1 falsificación local.

**Debilidad de bookkeeping detectada:** el cuerpo del manuscrito (abstract ES, abstract EN, conclusión §"Tesis del capítulo") cita `Bitacora/2026-05-16-adversarial-downgrades/` como evidencia, pero **ese directorio está vacío**. La salida del adversarial iter 4 vive solo en el mensaje de commit `22b167f`. Esto reproduce el patrón "sub-agente silencioso" de iter 3 en el agente más crítico de iter 4. **Acción inmediata: materializar el reporte adversarial en disco antes del próximo commit.**

---

## Cuestionamiento filosófico de fondo

### Pregunta clave

¿La reformulación opción (c) endurecida del adversarial iter 4 — "los 30 casos sintéticos son calibración del aparato, no evidencia ontológica positiva; la evidencia son los N casos B-T2 reales" — es consistente con el espíritu de la carta de Ricardo?

### Análisis

**Punto 1 — Distinción central de Ricardo.**
Ricardo defiende la distinción operativa entre *psicologías ancladas* (las que se conectan, vía variables empíricas independientes, a un sustrato medible y manipulable) y *psicologías no ancladas* (las que producen mapas internamente coherentes pero sin externalidad verificable). La opción (c) endurecida hace exactamente este movimiento dentro del corpus EDI: separa los casos que cumplen "variables empíricas independientes con datos reales públicos pre-registrados" (anclados) de los casos sintéticos que producen señales bajo flexibilidad analítica documentada (no anclados, en sentido ricardiano operativo). Esto no es debilitamiento de la tesis: es **alineación con el criterio que la propia carta ya impone**.

**Punto 2 — Los cinco criterios operativos de Ricardo como discriminadores.**
Ricardo nombra cinco criterios; entre ellos *variables empíricas independientes* y *replicación inter-grupo*. La opción (c) los restituye como filtro: los 30 casos sintéticos pasan algunos criterios internos del aparato (C1-C5 dentro del simulador), pero fallan el criterio externo de Ricardo "variables empíricas independientes" en sentido fuerte (las series están calibradas o reconstruidas, no son medidas directas de un proceso externo al simulador). Los casos B-T2 con datos reales sí lo cumplen. Por tanto, la opción (c) **no introduce un estándar nuevo**: aplica el estándar que Ricardo ya pidió, ahora con resolución por caso.

**Punto 3 — La reformulación es alineación, no concesión.**
Pre-iter-4, el discurso del manuscrito leía: *"40 casos validan una ontología multiescalar"*. Esto es leído por Ricardo como **claim ontológico fuerte sobre el corpus**. Post-iter-4 opción (c) endurecida: *"el aparato es protocolo de admisión calibrado sobre 30 casos sintéticos; N≈3-7 casos sobreviven anclaje empírico estricto y constituyen evidencia ontológica positiva acotada"*. Esta segunda formulación es **lo que Ricardo escribió que aceptaría**: una tesis cuya pretensión está calibrada a su evidencia anclada. **No es debilitamiento; es exactamente el alineamiento que la carta pedía.**

**Punto 4 — Costo de la opción dura (riesgo real).**
Si los 25 casos B-T2 pendientes (todos los sintéticos del corpus inter-dominio que aún no se han re-ejecutado con datos reales públicos) muestran una tasa de downgrade similar a la observada hasta ahora (4/7 cambian de clase en iter 1-4: caso 19 falsificado, caso 01 a null, caso 03 a null, caso 13 a trend; con caso 11 confirmando trend), entonces la proyección Ioannidis del 28% se queda corta: la tasa observada empírica es ≈ 57% (4/7) de reclasificación a la baja. Extrapolando a 30 casos, el soporte final cae a aproximadamente **10-15 strong**, no 30.

¿Eso sostiene una tesis doctoral? Depende del marco que la tesis declare:

- **Lectura A — "la ontología multiescalar es real (κ-ontológica fuerte)":** N=3-7 strong reales es insuficiente para sostener generalidad multiescalar. La tesis cae a "demostración parcial circunscrita a 3-7 dominios".
- **Lectura B — "el aparato funciona como protocolo de admisión refutable (κ-pragmática)":** N=3 strong reales + 1 falsificación local + 3 nulos genuinos **ya demuestra el funcionamiento del aparato**: discrimina, admite, rechaza, falsea. Aquí la tesis no necesita más casos para sostenerse; necesita más calidad de los casos que tiene.

**La reformulación opción (c) elige Lectura B explícitamente.** Esto es coherente con la distinción κ-pragmática vs κ-ontológica que el propio cap 1 y el cap 04-04 §1 ya hacían. La opción (c) no introduce una nueva posición; **realinea el cierre con la distinción que la tesis ya hace en su aparato.** Por tanto, es internamente consistente y externamente alineada con Ricardo.

**Punto 5 — Honestidad sobre el costo simbólico.**
El costo no es filosófico (la posición Lectura B es defendible); es **retórico**. El abstract original vendía "40 casos validan ontología multiescalar". El abstract post-opción-(c) dice "3 casos sobreviven anclaje estricto; el resto es calibración del aparato". El cambio puede ser leído por revisores externos (no Ricardo) como debilitamiento sustancial. La estrategia honesta: mantener ambos textos visibles — el original como formulación canónica vigente y la nota BORRADOR-IA como advertencia de revisión hasta firma — y dejar que Jacob decida si la firma se da antes o después de Ricardo. **El snapshot iter 4 confirma que la estructura "doble texto pendiente firma" ya está implementada en disco** (abstract ES/EN + conclusión §"Tesis del capítulo").

### Veredicto

La opción (c) endurecida del adversarial iter 4 **es la reformulación más Ricardo-compatible posible** del cierre. No debilita la tesis; corrige una sobre-venta. El riesgo real no está en la opción (c) sino en lo que muestren los 25 casos B-T2 pendientes: si confirman tasa de downgrade ≈ 50%, la tesis necesita reposicionarse explícitamente como "aporte metodológico (el aparato) con demostración acotada (3-7 casos anclados)", lo cual es el aporte real verificable. Si la lectura B se firma honestamente, la tesis sobrevive Ricardo. Si se intenta sostener la lectura A con N=3-7 strong reales, no sobrevive.

---

## 8 acciones priorizadas para iter 5

1. **[CRÍTICO]** Materializar `Bitacora/2026-05-16-adversarial-downgrades/red-team.md` en disco con el contenido completo del hallazgo Ioannidis + reclasificación caso 19. Hoy el directorio está vacío pero es citado como evidencia en abstract ES, abstract EN y conclusión. **Riesgo de falsa atribución de evidencia si no se materializa antes de defensa.**
2. **[CRÍTICO]** Auditoría del caso 19 como *falsificación local del aparato*: re-ejecutar con sonda alternativa (multi-probe-null) — la inadecuación de la sonda Revelle/calcificadores para serie Aloha pH es testeable. Si una sonda alternativa físicamente motivada produce EDI ≥ 0, el caso 19 vuelve a Trend/Weak; si todas las sondas físicamente justificables fallan, la falsificación local se confirma y debe documentarse como **prueba positiva de falsabilidad del aparato** (no como debilidad).
3. **[CRÍTICO]** Atender los 5 saltos del process-verifier abiertos desde iter 2 (saltos A, B, C son los más graves). Re-lanzar al sub-agente con prompt explícito de salida obligatoria y verificación post-ejecución del archivo en disco.
4. **[ALTO]** Decidir y documentar globalmente la convención `dataset_real.csv` vs `dataset.csv` en `09-simulaciones-edi/README.md` o `CLAUDE.md` §7. Renombrar al menos los casos 11 y 13 (re-ejecutados con datos reales en iter 4 pero sin renombrar archivo); auditar los casos 04, 16, 20, 27 para consistencia.
5. **[ALTO]** Re-ejecutar B-T2 con datos reales sobre los próximos 5 casos sintéticos del corpus inter-dominio (priorizar los que más cargan la prosa: 02, 05, 06, 07, 08, 14, 15, 17, 21-26, 28-30). Cada re-ejecución da evidencia sobre la tasa de downgrade real y, por tanto, sobre la viabilidad de la lectura B vs A.
6. **[ALTO]** Generar slides Marp para defensa (`06-cierre/_extendido/slides/`) — sub-agente silencioso desde iter 2. Input: `06-cierre/_extendido/storyboard-defensa.md`. Verificar archivo en disco post-ejecución.
7. **[MEDIO]** Auditar las 29 marcas `BORRADOR-IA` activas en el cuerpo del manuscrito: cuáles requieren firma H-J* mayor (decisión epistémica), cuáles pueden cerrarse con verificación técnica deterministicamente, cuáles deben moverse a `_extendido/` por ser experimentales. Construir tabla en `TAREAS_PENDIENTES.md`.
8. **[MEDIO]** Resolver el estado dirty de `09_caso_finanzas/outputs/*`: o documentar la re-ejecución (mtime 23:49:09, EDI cayó −0.4051 → −0.6648, C1 True→False) en bitácora con su causa y comitearla, o revertir a baseline antes del próximo commit. La discrepancia silenciosa entre `metrics.json` y `report.md` es exactamente el patrón que `prose_against_json` detecta a posteriori; resolverlo antes evita drift.

---

## Base de comparación para iter 5

| Métrica | Valor iter 4 |
|---------|---------------|
| Verificadores en verde | 8/8 (decorative_citations en warn) |
| HEAD commit | `22b167f` |
| Working tree mod / untracked | 4 / 1 |
| Casos con `metrics.json` | 32/40 |
| Casos B-T2 ejecutados con datos reales | 9 (01, 03, 04, 11, 13, 16, 19, 20, 27) |
| Casos B-T2 con `overall_pass=True` o strong real | 3 (Deforestación 16, Energía 04, Kessler 20) + 1 con gate completo (27 Riesgo Biológico) |
| Casos reclasificados acumulados iter 1→4 | 8 (01, 03, 11, 13, 19, 20 ascendido, + 2 anteriores) |
| Falsificaciones locales del aparato | 1 (caso 19, pendiente multi-probe-null) |
| BORRADOR-IA pendientes firma en cuerpo | 29 hits / 14 archivos |
| H-J* etiquetas únicas referenciadas | 9 (H-J1, H-J3, H-J5..H-J11) |
| Tamaño Tesis.pdf | 1.6 MB (1632200 B), 413 pp (sin re-build iter 4) |
| Sub-agentes silenciosos iter 4 | 2 (process-verifier-debates-cierre, slides Marp) |
| Hallazgos críticos abiertos | 4 (Ioannidis sin reporte en disco; saltos A/B/C process-verifier sin atender; convención dataset; case-19 falsificación local pendiente multi-probe) |
| PDFs primarios faltantes | 4 (Quine, Yablo, Goff, Strawson) |
| Tasa entrega sub-agentes iter 4 | 6/8 (75%) — mejora vs iter 3 (62.5%) |
