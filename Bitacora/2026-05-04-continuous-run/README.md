# Bitácora 2026-05-04 — Modo continuo (DAEMON HEADLESS — DEPRECADO)

**Aviso (2026-05-11):** los archivos en esta carpeta son output del **daemon paralelo viejo** del harness, que entre 2026-05-04 y 2026-05-05 lanzó workers `claude -p` headless en paralelo vía `subprocess.Popen` (ver `harness/lib/daemon.py` en git history, commits anteriores a `0c61ede`).

## Por qué este contenido NO es fuente de verdad

- Cada worker fue una **instancia Claude independiente**, sin contexto compartido y sin visibilidad de lo que estaban editando los otros workers en paralelo. Los outputs no fueron orquestados.
- El daemon marcó **118 tareas como "done"** en `harness/state/continuous_run.json` sin que ningún orquestador (humano o IA) hubiera leído los reportes antes de marcarlas.
- Esta carpeta contiene **~79 archivos** (`AU-*.md`, `F0*-*.md`, `daemon.log`, etc.) generados por esos workers ciegos entre sí.

## Estado actual de estos archivos

- **Conservados como evidencia auditable** del modo de fallo (a petición del usuario, 2026-05-11).
- **NO consumir como fuente para decisiones sobre el manuscrito** sin verificación independiente.
- Cualquier "hallazgo" reportado aquí debe re-verificarse manualmente o re-ejecutarse bajo el modo de orquestación interactiva (`/continuous-run-tick`) antes de cerrar la tarea correspondiente en `TAREAS_PENDIENTES.md`.

## Modo correcto desde 2026-05-11

- `/continuous-run` y `/continuous-run-tick` operan **dentro de la sesión interactiva** vía el `Agent` tool.
- El daemon (`harness/lib/daemon.py`, `harness/scripts/run_daemon.sh`, `python3 harness/cli.py continuous daemon`) está **neutralizado**: saltan con `SystemExit(2)` y mensaje de error claro.
- Un hook (`block_claude_headless`) bloquea cualquier `Bash` que intente spawnear `claude -p` o `claude --print`.

Ver `harness/CLAUDE.md` §"Modo continuo" para la política actualizada.
