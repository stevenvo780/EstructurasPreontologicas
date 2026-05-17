# Snapshot iteración 2 — loop nocturno

## Hora del snapshot

- **Local:** 2026-05-16 23:29:10 -05
- **UTC:** 2026-05-17 04:29:10 UTC
- **Iteración:** 2 (snapshot de base para comparar con iter 3)

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

Comando: `python3 harness/cli.py verify --all`.

## Git

- **HEAD:** `2934c3f` — *loop nocturno iter 1: B-T2 expansión + block-perm + adversarial + PDF*
- **Branch:** `harness/fix-orchestration-policy`
- **Main branch del repo:** `main` (no es la actual)
- **Últimos 3 commits:**
  - `2934c3f` loop nocturno iter 1
  - `661af57` web+abstract: sync build React + corregir divergencia ST 13→24 en abstract EN
  - `bfae94c` tesis: pasada completa 2026-05-16 — 8/8 verificadores en verde

### Working tree dirty (no commitado)

```
M 02-fundamentos/04-anclaje-conductual-ecologico.md
M 06-cierre/01-conclusion-demostrativa.md
M 09-simulaciones-edi/01_caso_clima/src/data.py
M 09-simulaciones-edi/20_caso_kessler/outputs/metrics.json
M 09-simulaciones-edi/20_caso_kessler/outputs/primary_arrays.json
M 09-simulaciones-edi/20_caso_kessler/outputs/report.md
M TesisFinal/Tesis.md
?? 09-simulaciones-edi/01_caso_clima/src/fetch_real.py
?? 09-simulaciones-edi/20_caso_kessler/src/fetch_real.py
```

Observación: `Tesis.md` modificado en working tree pero CLAUDE.md §7 prohíbe edición directa — verificar si es output de `build.py` no committeado o edición ilegal antes de iter 3.

## Cobertura datos

- **Casos con `metrics.json` generado:** 32 / 40 (`09-simulaciones-edi/*_caso_*/outputs/metrics.json`)
- **Casos con `data/dataset_real.csv` (nombre literal):** 0 — convención del repo NO es `dataset_real.csv`. Cobertura real medible por:
  - `data/dataset.csv` (sintético/calibrado o real-renombrado): >= 6 (01, 04, 19, 20, 27)
  - CSVs identificables como reales: `16_caso_deforestacion/data/wb_deforestation.csv`, `oos_oxcgrt/OxCGRT_nat_2023.csv`, `oos_owid_co2/owid_co2.csv`, `covid_pilot/data_cache/owid-covid.csv`
  - **Acción iter 3:** definir convención y auditar — métrica como está reporta 0 falso.
- **Untracked fetch_real.py nuevos:** `01_caso_clima`, `20_caso_kessler` (work in progress de iter 1, no integrado al pipeline).

## PDF Tesis

- **Path:** `TesisFinal/Tesis.pdf`
- **Tamaño:** 1.6 MB (1620598 bytes)
- **Mtime:** 2026-05-16 23:24 (generado en iter 1)
- **Estado:** existente y reciente; no requiere regenerar salvo cambios en capítulos.

## harness/state.json

- **Versión:** 1
- **Created:** 2026-05-05
- **Updated:** 2026-05-16 13:49 UTC
- **needs_human:** 0 ítems en cola explícita (`state.json` solo registra `passes[]`, no `items[]` con status — la cola humana vive en `TAREAS_PENDIENTES.md`).
- **Última pasada registrada:** ver `passes[]` (modo `dry` con 8/8 verde inferido por arquitectura actual).

## Cola humana (TAREAS_PENDIENTES.md)

12 ítems H-J* abiertos (firma humana de Jacob requerida, no cerrables desde asistencia):

| ID | Tema clave |
|----|------------|
| H-J1 | Firma cap 04-debates §04 (anticipación objeciones filosóficas) |
| H-J2 | Categoría "ontología única multiescalar": regulativa / constitutiva / programática |
| H-J3 | Estatus asimetría L1↔B↔L3↔S: ontológica / epistemológica / procedimental |
| H-J4 | Dimensiones omitidas (estética + política agonística) |
| H-J5 | Engagement primarios (Simondon, Gibson, Dennett, Searle, Bunge) |
| H-J6 | Refutación dualismo/idealismo/panpsiquismo (Chalmers, Goff, Strawson) |
| H-J7 | "0/1500" → "0/2000" en defensa (Wilson CI verificado) |
| H-J8 | Fusiones D.1-D.4 — −694 líneas brutas; conteo canónico escenarios 4/5/6 |
| H-J9 | Reconocer baselines ARIMA/VAR ganan en 2/4 strong (deforest + riesgo bio) |
| H-J10 | Reclasificar Ladyman & Ross como rival eliminativista |
| H-J11 | AUC-ROC=0.886 como coherencia interna del umbral (no discriminación externa) |
| H-J12 | Caso 19 reclasificado a NULL (EDI=0.00044, p=0.43) — ejecutado, falta firma |

## Hallazgos abiertos críticos (iter 1)

### 1. Red-team contra "irrealismo operativo como tercera vía"

Archivo: `Bitacora/2026-05-16-adversarial-irrealismo-operativo/red-team.md`.

- **Objeción A (Yablo, ficcionalismo):** WARN_THESIS_VULNERABLE. "Tercera vía" puede ser ficcionalismo refinado renombrado. Respuesta dura requiere desarrollo argumental ausente en cap 04-04 §1. PDF Yablo no en `07-bibliografia/` — cita secundaria obligatoria.
- **Objeción B (Ladyman & Ross, OSR):** la diferencia "estructural moderado no-Ladyman" es nominal. L&R con PNC son más exigentes que la tesis. PDF disponible, cita verbatim p.121, p.130, p.152 verificada. Salida blanda: redescribir como "OSR + protocolo EDI". Conecta con H-J10.
- **PDFs faltantes:** Quine 1948, Yablo 1998/2014, Goff 2019/2023, Strawson 2006.

### 2. Process-verifier — hilo narrativo Cap 02→03→05→06

Archivo: `Bitacora/2026-05-16-process-verifier-hilo-narrativo/audit.md`.

Cinco saltos críticos identificados:

- **Salto A (02-01 → 02-04):** §invariantes de 02-01 redundante con Tabla 2.4.1 de 02-04. Atractor empírico de 02-01 §2.2.1 NO coincide con atractor en 02-04 para casos no-experimentales (33, 39, 40). Refuerzo sugerido: nota explícita κ-pragmática vs κ-ontológica.
- **Salto B (02-04 → 03-01):** "B" cambia significado entre capítulos (generalizado en 02-04, regionalizado en 03-01 §1). Redefinición silenciosa prohibida por 02-01 §0.2.4.
- **Salto C (03-01 → 03-04):** 4ª prueba "generalización a condiciones no usadas para ajuste" introducida sin justificación. Forma específica `EDI = 1 - RMSE_coupled/RMSE_no_ode` no justificada como canónica vs alternativas (likelihood ratio, KL-divergencia).
- **Salto D y E:** ver `audit.md` (caso ancla Warren — r²=0.98 vienen de Fajen-Warren, no de pipeline EDI; condición 5 cartografía debilitada por §3.6).

## Próximos pasos para iter 3 (priorizado)

1. **[ALTO] Auditar working tree dirty** — decidir si commitear `01_caso_clima/src/data.py` + `fetch_real.py` + `kessler/outputs/*` y `Tesis.md`. Verificar que `Tesis.md` proviene de `build.py` no de edición directa (CLAUDE.md §7 bloquea edición directa). Si edición ilegal, revertir.
2. **[ALTO] Salto B (process-verifier):** redactar nota terminológica reescrita en `03-formalizacion/01-aparato-formal.md` §1 para que B sea consistente con generalización de 02-04 §1. Tarea de prosa filosófica acotada — delegar a `@philosophical-reader` con cita exacta.
3. **[ALTO] Salto A (process-verifier):** insertar nota post-Tabla 2.4.1 en `02-fundamentos/04-anclaje-conductual-ecologico.md` distinguiendo κ-pragmática vs κ-ontológica para casos 33, 39, 40.
4. **[ALTO] Red-team Objeción A (Yablo):** ejecutar `/fetch-biblio` para conseguir Yablo 1998/2014 PDFs (arXiv/Semantic Scholar). Si no recuperable, declarar cita secundaria explícita en cap 04-04 §1 y redactar respuesta dura distinguiendo ficcionalismo reductivo vs materialista.
5. **[MEDIO] Red-team Objeción B (Ladyman):** redactar borrador "OSR + protocolo EDI" en `Bitacora/2026-05-16-loop-nocturno/borradores/`. NO modificar capítulos — sirve para H-J10. Mantener nuance p.131.
6. **[MEDIO] Cobertura datos reales:** auditar 32 `metrics.json` vs origen del CSV. Definir y documentar convención (`dataset.csv` real vs sintético vs calibrado). Actualizar script de medición para que el snapshot no reporte 0 falsamente.
7. **[MEDIO] Salto C (process-verifier):** redactar justificación en `03-formalizacion/04-edi.md` (o equivalente) de por qué `EDI = 1 - RMSE_coupled/RMSE_no_ode` vs alternativas. Citar Glymour 1980 con paginación o eliminar.
8. **[BAJO] Block-permutation TENG:** implementar block-perm en `hybrid_validator.py` (deuda declarada en H-J12). Caso 19 con margen amplio (EDI=0.0004, p=0.43) no cambiaría, pero queda como deuda activa.

## Base de comparación para iter 3

Métricas que iter 3 debe re-medir y comparar contra este snapshot:

| Métrica | Valor iter 2 |
|---------|--------------|
| Verificadores en verde | 8/8 |
| HEAD commit | `2934c3f` |
| Working tree archivos modificados | 7 |
| Working tree archivos untracked | 2 |
| Casos con `metrics.json` | 32/40 |
| Tamaño Tesis.pdf | 1.6 MB (1620598 B) |
| H-J* abiertos | 12 |
| Hallazgos críticos abiertos | 2 (red-team Yablo+Ladyman, 5 saltos process-verifier) |
| PDFs primarios faltantes | 4 (Quine 1948, Yablo, Goff, Strawson) |
