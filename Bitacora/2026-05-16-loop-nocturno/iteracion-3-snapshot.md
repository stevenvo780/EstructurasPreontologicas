# Snapshot iteración 3 — loop nocturno

## Hora del snapshot

- **Local:** 2026-05-16 23:37:58 -05
- **UTC:** 2026-05-17 04:37:58 UTC
- **Iteración:** 3 (sucede a `iteracion-2-snapshot.md` de 23:29:10 -05)
- **Delta vs iter 2:** +8m 48s wall-clock

## Harness status (8/8 verificadores)

```
[pass ] harness_compliance
[pass ] citation_pagination
[pass ] decorative_citations
[pass ] prose_against_json
[pass ] replay_hash
[pass ] debt_index
[pass ] self_indulgence
[pass ] consistency_doc_config
```

Comando: `python3 harness/cli.py verify --all`. Sin regresiones respecto a iter 2.

## Git

- **Branch:** `harness/fix-orchestration-policy`
- **HEAD:** `904aeae` — *loop nocturno iter 2: correcciones críticas adversarial + B-T2 caso 20+01 + Schrödinger* (2026-05-16 23:35:34 -05)
- **Commits nuevos desde iter 2 (HEAD anterior `2934c3f`):**
  - `2a47350` *feat(case-20): expand Kessler (orbital debris) to real data + full EDI evaluation* (23:29:05)
  - `904aeae` *loop nocturno iter 2: correcciones críticas adversarial + B-T2 caso 20+01 + Schrödinger* (23:35:34)
- **Avance committeado:** 2 commits, principalmente caso 20 → datos reales (Kessler, único caso B-T2 con `overall_pass=True` en fase real).

### Working tree dirty (no commitado, output de iter 3 en curso)

```
M 00-proyecto/05-resumen-y-abstract.md
M 05-aplicaciones/07-mapa-aplicaciones-corpus.md
M 06-cierre/01-conclusion-demostrativa.md
M 09-simulaciones-edi/03_caso_contaminacion/case_config.json
M 09-simulaciones-edi/03_caso_contaminacion/outputs/{metrics,primary_arrays}.json
M 09-simulaciones-edi/03_caso_contaminacion/outputs/report.md
M 09-simulaciones-edi/19_caso_acidificacion_oceanica/case_config.json
M 09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/{metrics,primary_arrays}.json
M 09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/report.md
M TesisFinal/Tesis.md
M TesisFinal/Tesis.pdf
```

- `Tesis.md` modificado (CLAUDE.md §7 lo prohíbe si no proviene de `build.py`) — verificar antes de commit.
- `Tesis.pdf` regenerado en iter 3.
- 7 archivos modificados, 0 untracked (vs iter 2: 7 mod + 2 untracked → los `fetch_real.py` se committearon en `2a47350`).

## Cobertura B-T2 datos reales

| Caso | Path canónico | Estado iter 3 | EDI real |
|------|---------------|---------------|----------|
| 01 Clima IPCC | `01_caso_clima/data/dataset.csv` (real-renombrado) + `fetch_real.py` committeado | overall_pass=False (fase real existe) | n/d (run en curso) |
| 03 Contaminación | `03_caso_contaminacion/data/dataset_real.csv` **NUEVO** | overall_pass=False ambas fases | real: **−0.0109** [CI: −0.075, +0.066] → NULL claro |
| 04 Energía OWID | `04_caso_energia/data/dataset.csv` (calibrado/fallback) | sin cambios iter 3 | n/d |
| 16 Deforestación WB | `16_caso_deforestacion/data/wb_deforestation.csv` | sin cambios iter 3 | EDI baseline ~0.602 |
| 19 Acidificación | `19_caso_acidificacion_oceanica/data/dataset_real.csv` **NUEVO** | overall_pass=False ambas fases | real: **−0.0047** [CI: −0.0054, −0.0041] → NULL confirmado |
| 20 Kessler NASA | `20_caso_kessler/data/dataset.csv` (committeado en iter 3) | overall_pass=**True** fase real | n/d (único B-T2 verde) |
| 27 Riesgo Bio WHO | `27_caso_riesgo_biologico/data/dataset.csv` | sin cambios iter 3 | n/d |

- **Convención auditada:** dos casos (03, 19) adoptaron el nombre literal `dataset_real.csv` por primera vez. Los demás siguen usando `dataset.csv`. **Inconsistencia de convención abierta** (acción AC-iter4).
- Adicionalmente: `oos_oxcgrt/OxCGRT_nat_2023.csv`, `oos_owid_co2/owid_co2.csv`, `covid_pilot/data_cache/owid-covid.csv` — fuentes reales out-of-sample.
- **Total casos con `metrics.json`:** 32 / 40 (sin cambio vs iter 2).

## PDF Tesis

- **Path:** `TesisFinal/Tesis.pdf`
- **Tamaño:** 1.6 MB (1632200 bytes; +11602 B vs iter 2)
- **Páginas:** 413
- **Mtime:** ~23:30s (regenerado en iter 3, working tree dirty)
- **Estado:** existente, re-construido por agente PDF re-build.

## Hallazgos iter 3

### 1. Caso 03 Contaminación PM2.5 reclasificado a NULL (real)

- Fase real con `dataset_real.csv`: EDI = **−0.0109**, CI 95% incluye 0, RMSE coupled (4.097) > RMSE no_ode (4.053) → acoplamiento no aporta. C1 (convergence) = False.
- Conclusión operativa: PM2.5 sin señal EDI verificable en datos reales → candidato a reclasificación pública (paralelo a caso 19 ya hecho en iter previa).

### 2. Caso 19 Acidificación oceánica confirmado NULL (real)

- Fase real: EDI = **−0.0047**, CI 95% = [−0.0054, −0.0041] (todo negativo). `rmse_ode` (0.61) ya batía a `rmse_coupled` (1.55), señal de mala calibración del acoplamiento.
- H-J12 (cierre de 19 a NULL) ya estaba pendiente; iter 3 aporta la evidencia con datos reales que faltaba.

### 3. Engagement Yablo (DRAFT-IA) entregado

- `Bitacora/2026-05-16-engagement-yablo/engagement-yablo.md` — 49 líneas. Declarado **secundario** (sin PDF de Yablo en `07-bibliografia/`), reconstruye ficcionalismo cuasi-comprometido vía Chalmers "Ontological Anti-Realism" (PDF presente). Ofrece tres respuestas R1/R2/R3 con costos. Concesión §4: sin EDI + criterios externos, el irrealismo operativo es indistinguible de Yablo. Recomienda **R2 + R1 mixta**. Requiere firma H-J (decisión filosófica) y cita verbatim paginada de Yablo (deuda ADV-2026-05-16 abierta).

### 4. Vulnerabilidad: tres sub-agentes iter 3 sin entregable

- `Bitacora/2026-05-16-engagement-ladyman-ross-pnc/` — **directorio vacío**. Agente lanzado, no produjo artefacto.
- `Bitacora/2026-05-16-process-verifier-debates-cierre/` — **directorio vacío**. Igual.
- `06-cierre/_extendido/slides/` — **directorio vacío**. Marp no generó deck.
- **Tasa de entrega iter 3:** 5/8 agentes con output verificable (PDF, downgrade 01, B-T2 03+19, engagement Yablo). 3/8 silenciosos.

### 5. Caso 20 Kessler validado real en commit `2a47350`

- Único B-T2 con `overall_pass=True` en fase real entre los siete auditados. Aporta contraste discriminante (Yablo R2: la intervención EDI sí produce efectos diferenciados sobre datos reales en al menos un caso).

## Comparación iter 2 → iter 3

### Deudas cerradas (parcial)

| Deuda iter 2 | Estado iter 3 |
|--------------|---------------|
| Convención `dataset_real.csv` indefinida | **Parcial**: 03 y 19 adoptan literalmente; convención global aún sin documentar. |
| Caso 19 NULL sin evidencia real | **Cerrado evidencialmente**: real EDI = −0.0047, CI todo negativo. Falta firma H-J12. |
| Caso 20 Kessler sin datos reales | **Cerrado**: commit `2a47350`, `overall_pass=True`. |
| Caso 01 `fetch_real.py` untracked | **Cerrado**: committeado en `2a47350`. |
| Red-team Objeción A Yablo sin borrador | **Cerrado parcial**: borrador R1/R2/R3 disponible; firma H-J + cita paginada pendientes. |

### Deudas nuevas abiertas

- **D-iter3-1:** Caso 03 PM2.5 real NULL → falta reclasificación en `05-aplicaciones/07-mapa-aplicaciones-corpus.md` (modificado pero sin revisar) y prosa de cap 04-debates.
- **D-iter3-2:** Tres agentes silenciosos (Ladyman-Ross, process-verifier-debates, slides Marp). Investigar logs harness; si fallo sistemático, re-lanzar con instrucciones más específicas.
- **D-iter3-3:** `Tesis.md` y `Tesis.pdf` modificados sin commit; verificar origen (debe ser output de `build.py`).
- **D-iter3-4:** Cap `06-cierre/01-conclusion-demostrativa.md` y `00-proyecto/05-resumen-y-abstract.md` modificados — pendiente auditar si los cambios reflejan correctamente los nuevos NULL (03, 19).
- **D-iter3-5:** Saltos B, A, C del process-verifier (iter 2 §1) no atendidos — no se delegó `@philosophical-reader` en iter 3.

### Métricas comparadas

| Métrica | iter 2 | iter 3 | Δ |
|---------|--------|--------|---|
| Verificadores verde | 8/8 | 8/8 | = |
| HEAD commit | `2934c3f` | `904aeae` | +2 commits |
| Working tree mod | 7 | 7 | = |
| Working tree untracked | 2 | 0 | −2 (commiteados) |
| `metrics.json` generados | 32/40 | 32/40 | = |
| Casos B-T2 con `dataset_real.csv` literal | 0 | 2 (03, 19) | +2 |
| Casos B-T2 con `overall_pass=True` real | 0 verificados | 1 (20) | +1 |
| Tamaño Tesis.pdf | 1620598 B | 1632200 B | +11602 B |
| Páginas PDF | n/d (no medido iter 2) | 413 | — |
| H-J* abiertos | 12 | 12 | = (ninguna firma humana iter 3) |
| Hallazgos críticos abiertos | 2 (Yablo+Ladyman, 5 saltos) | 2.5 (Yablo borrador parcial; Ladyman+saltos+silencios sin atender) | parcial |
| PDFs primarios faltantes | 4 | 4 | = |

## Próximos pasos para iter 4 (priorizado)

1. **[ALTO]** Auditar `Tesis.md` y `Tesis.pdf` dirty: confirmar que vienen de `build.py` y no de edición directa. Si limpio, commitear. Si edición ilegal, revertir y re-ejecutar `python3 TesisFinal/build.py`.
2. **[ALTO]** Re-lanzar los tres sub-agentes silenciosos con prompt explícito sobre **archivo de salida obligatorio** y verificación post-ejecución:
   - Engagement Ladyman-Ross PNC (PDF disponible en `07-bibliografia/`, citas verbatim p.121/130/152).
   - Process-verifier debates→cierre (cap 04→06, hilo argumental).
   - Slides Marp para defensa oral (input: `06-cierre/_extendido/storyboard-defensa.md`).
3. **[ALTO]** Caso 03 PM2.5: reclasificar formalmente a NULL en `05-aplicaciones/07-mapa-aplicaciones-corpus.md` y `04-debates/` con evidencia (EDI real = −0.011, CI cruza 0).
4. **[ALTO]** Definir y documentar convención `dataset_real.csv` vs `dataset.csv` (sintético/calibrado) en `09-simulaciones-edi/README.md` o `CLAUDE.md` §7; renombrar los 5 casos restantes (01, 04, 16, 20, 27) para uniformidad o aceptar excepciones documentadas.
5. **[MEDIO]** Atender los 5 saltos del process-verifier (iter 2 §1): saltos A, B, C son los más críticos. Delegar a `@philosophical-reader` con `/process-verify` enfocado.
6. **[MEDIO]** Yablo: ejecutar `/fetch-biblio "Yablo Aboutness 2014"` y `/fetch-biblio "Yablo Does Ontology Rest on a Mistake 1998"` para conseguir PDFs. Si no recuperable, declarar cita secundaria explícita vía Chalmers en cap 04-04 §1.
7. **[MEDIO]** Auditar cap `06-cierre/01-conclusion-demostrativa.md` y `00-proyecto/05-resumen-y-abstract.md` dirty: confirmar que reflejan los downgrades 03 + 19 sin sobre-vender.
8. **[BAJO]** Block-permutation TENG en `hybrid_validator.py` (H-J12, no cambia veredicto pero cierra deuda metodológica).

## Base de comparación para iter 4

| Métrica | Valor iter 3 |
|---------|--------------|
| Verificadores en verde | 8/8 |
| HEAD commit | `904aeae` |
| Working tree mod / untracked | 7 / 0 |
| Casos con `metrics.json` | 32/40 |
| Casos B-T2 con datos reales (literales o equivalentes) | 7 (01, 03, 04, 16, 19, 20, 27); 1 con `overall_pass=True` (20) |
| Tamaño Tesis.pdf | 1.6 MB (1632200 B), 413 pp. |
| H-J* abiertos | 12 |
| Hallazgos críticos abiertos | 5 (Yablo parcial, Ladyman pendiente, 5 saltos process-verifier, 3 silenciosos iter 3, convención dataset) |
| PDFs primarios faltantes | 4 (Quine, Yablo, Goff, Strawson) |
| Tasa entrega sub-agentes iter 3 | 5/8 (62.5%) |
