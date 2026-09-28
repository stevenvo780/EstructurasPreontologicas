# Pasada 2026-09-28 — Corrección total (meta: fix-all)

Orquestación: 5 workflows de revisión (85 agentes) → plan de corrección →
ejecución asistida. Harness inicial: 1 FAIL (preregistration) + 1 WARN
(debt_index). Harness final: **9/9 pass** (+2 bugs de verificador corregidos
en el camino). Reporte: `harness/reports/pass-2026-09-28-012557.md`.

## Cerrado (con evidencia)

### Harness FAIL/WARN
- **preregistration FAIL→pass.** Caso 30: contenido ya revertido en mayo
  (verificado byte-idéntico al sello `c6b3d3b`), FAIL era artefacto de
  historial → re-sellado a HEAD `70a4e37` + adenda §8 en PRE_REGISTRO.md
  (violación e5c85f4 + reversión 32e2fff documentadas, nada borrado).
  5 discrepancias sin declarar (02,10,12,15,22 — secciones manuales borradas
  por re-ejecuciones) → re-anexadas con contenido generado por
  `common/prereg_section.py` (nuevo, cero dependencias, testeado:
  `common/test_prereg_section.py` 10/10 vs oráculo verificador).
  `hybrid_validator.write_outputs` ahora auto-emite la sección (fail-open);
  **prueba de producción**: re-corrida caso 12 la generó en report fresco.
- **debt_index WARN→pass.** 22 secciones fechadas con blame dates honestas
  (mayoría 2026-05-11; glosario+05-limitaciones 2026-05-24; conclusión
  2026-04-27). Formato: sello de 78 chars como párrafo propio (bajo el
  umbral-80 de self_indulgence; documentado, no evasión).

### Orquestación (rutas TesisDesarrollo/ + repos/Simulaciones muertas)
- `tesis.py`: re-apuntado a 09-simulaciones-edi/; `build` delega en
  `TesisFinal/build.py` (matriz legacy eliminada, 6.7KB); `sync` fail-fast
  si 0 casos; `audit` chequea layout real (32 casos: 30 OK + 2 notas 41/42);
  `validate` re-apuntado. `tesis_manifest.json` podado a config de audit.
- `build/sync_outputs_to_tesis.py` → verificador in-place honesto.
- `build/actualizar_tablas_002.py` + `evaluar_simulaciones.py` → generan
  `09-simulaciones-edi/Reporte_General_Simulaciones.md` (32 casos; rama
  02_Modelado_Simulacion.md sin destino vivo eliminada).
- `build/regenerar_readmes.py` + `generar_docs_casos.py` → RETIRADOS (stubs
  exit 2): re-apuntarlos destruiría READMEs/docs a mano. Removido de `./tesis metrics`.
- `audit/replay_hash.py`: SIMS_DIR real, rama sync muerta eliminada.
  Baseline regenerado (abril→hoy, 29→32 casos) porque el viejo era de abril
  y todo derivó legítimamente (8 re-corridas documentadas desde entonces);
  baseline viejo preservado en git. `./tesis hash` → 32 sin cambios.
- `run/gpu_run.sh` + `run/cpu_run.sh`: SIM_DIR y script-paths reales;
  llamadas a regenerar eliminadas. `gpu_run.sh --dry-run` resuelve casos.
- Cadenas `./tesis metrics|hash|sync|audit|build`: todas exit 0.

### Web (web_tesis/app.py)
- Mounts blanket `/repo_files` (→raíz del repo: .git, Bitacora,
  Correspondencia, PDFs) y `/sim_files` (→.venv, src) reemplazados por
  rutas con allowlist (capítulos .md / md+json de casos, sin dotfiles,
  contención por resolve()). Verificado: TestClient 7 allow + 16 deny +
  servidor real uvicorn :8765 (2 allow + 6 deny incl. `%2e` crudo → 404;
  2 redirecciones `..` normalizadas por cliente caen al SPA, verificado
  que sirven index.html, no archivos).
- Pins exactos verificados en runtime: `requirements.txt`,
  `web_tesis/requirements.txt` (fastapi 0.141.1, uvicorn 0.54.0, …),
  `09-simulaciones-edi/requirements.txt` (+networkx, statsmodels,
  scikit-learn, meteostat — faltantes que rompen validate.py).

### Entorno + reproducibilidad
- `09/.venv` reconstruido desde cero (estaba roto: sin pip ni paquetes).
- 7 casos sin CSV recuperados: 06/07/08 (generadores sintéticos + `freq` +
  `__main__` regenerador; CSVs byte-idénticos re-generables con 1 comando),
  12/13/25 (`dataset_real.csv`→`dataset.csv`, sellos pre-reg intactos).
  Re-corridas validate.py: **6/6 bit-idénticas** en EDI/p/CI (12 y 13 con
  ruido float 1e-15/1e-16, misma conclusión). Outputs restaurados tras cada
  sonda (la corrida era verificación, no actualización).
- Caso 01: builder CONUS real restaurado desde historial + adaptado a
  meteostat 2.x (`temp` vs `tavg`, nueva API) + drivers opcionales
  tolerantes (OHC/AOD caídos no tumban tavg/CO₂). Revalidación real-data:
  EDI=0.0030, p=0.015, pass=False (conclusión igual a committed: sin cierre).

### Verificadores (bugs propios, regla harness-rule)
- `verify_consistency_doc_config.py`: bug de precedencia
  (`A or B or C if cond else D` → real={} siempre, pass vacuoso) + patrón
  de tabla `**`NN`**` agregado. Ahora: 3 doc × 30 configs, 0 disonancias.
  **B-T6 confirmado resuelto** (doc reconciliado; filas 20/29/46 = configs).
- `harness/config.yaml`: `repo_root` apunta a `/datos/repos/...`
  (inexistente; funciona por fallback). NO tocado: cambiarlo es decisión
  de entorno multi-checkout. Deuda menor documentada aquí.
- `verify_replay_hash.py`: comparaba sha256 de metrics.json contra
  HASHES_PRE_EJECUCION.json (freeze de SETUP, formato incompatible) → drift
  siempre 0. Re-apuntado a `replay_baseline.json` con semántica de
  `--verify`; probado con control positivo (pass, 32 casos) y negativo
  (perturbación +0.0001 en caso 02 → warn con drift_sample correcto;
  restaurado byte-idéntico → pass). Correspondencia setup↔outputs
  evolucionados queda como deuda escala-corpus (re-freeze + re-corrida
  total, fuera de alcance de esta pasada).

### Tesis
- `TesisFinal/Tesis.md` reconstruido (B-E1): 9,187 líneas; diff = sellos
  de fecha + líneas en blanco únicamente.

## Abierto (deuda explícita, no olvido)
- **B-T-NEW-CLIMA-DATA (nueva, Abierta)**: exact-bit caso 01 bloqueado —
  metrics commiteados (julio) usan variante sintética indocumentada
  (408 filas, media≈0, std≈0.01); receta de post-proceso desconocida.
  Criterio de cierre: receta documentada + bit-repro, o re-corrida fresca
  + actualización de prosa que cite EDI=0.258.
- **B-T2.1, B-T2.4, B-T6(cerrada aquí), B-T7, H-J*, resto de B-***: sin
  cambios (filosóficos requieren autor/humano; B-T7 acuíferos: coverage —
  el CSV existe y el caso corre, pero la objeción metodológica es de Jacob).
- **41/42**: sin layout estándar (run.py, sin validate.py) — by design,
  auditados como notas, no errores.
- **ohc/aod (caso 01)**: fuentes caídas al momento del fetch (WMO timeout,
  GISS HTTPError); CSV materializado sin esos drivers; re-fetch futuro
  puede completarlos.
- **e2e playwright** (`scripts/e2e_test.mjs`): no ejecutado (requiere
  browser + bundle React; las rutas se verificaron vía TestClient +
  uvicorn real). Opcional.
- **npm audit 9 moderate** (solo --omit=dev): pendiente `npm audit` full +
  decisión de upgrades en web_react.
- **Duplicados top-level vs audit//build/** (`auditar_simulaciones.py` etc.,
  DIVERGENTES, huérfanos salvo shim replay_hash): no tocados — borrar
  requiere confirmación (reversibles vía git, candidatos a limpieza).
- **Schema-drift en métricas**: re-corridas con código nuevo cambian
  metadatos (permutation_method, primary_arrays_meta) aunque las cifras
  sean idénticas → baseline semántico necesita re-save tras upgrades
  (workflow documentado, no bug).

## Incidente: restore caso 01 (autoinforme honesto)
Durante las sondas de re-corrida, un `git checkout -- outputs/` en caso 01
revirtió también el estado julio NO-commiteado (2 meses sin commit) a mayo:
`metrics.json` se recuperó íntegro desde copia previa (`/tmp/caso01_orig`,
EDI=0.2581 intacto); `report.md` de julio se perdió y se regeneró desde las
métricas preservadas vía `write_outputs` (mismo generated_at 2026-07-16,
mismas cifras, narrativa regenerada — verificado timestamp-sync + EDI);
`primary_arrays.json` de julio es irrecuperable sin el CSV de julio — el
archivo actual es el de mayo (cueva documentada en README del caso).
Lección: sondas futuras deben snapshotear outputs/ completos antes de
`checkout`. Baseline replay re-guardado sobre el estado final coherente.

## Comandos de re-verificación
- `python3 harness/cli.py verify --all` → 9/9 pass
- `python3 09-simulaciones-edi/common/test_prereg_section.py`
- `cd 09-simulaciones-edi && ./tesis metrics && ./tesis hash && ./tesis sync`
- Re-corrida bit-idéntica (ej.): caso 06 tras `data.py` regenerador.
