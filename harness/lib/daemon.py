"""Daemon de modo continuo — DEPRECADO Y NEUTRALIZADO (2026-05-11).

Este módulo solía lanzar workers `claude -p` headless en paralelo vía
`subprocess.Popen`. Esa arquitectura producía instancias de Claude
independientes, sin contexto compartido y sin orquestación, que
escribían archivos al repo de forma descoordinada (ver
`Bitacora/2026-05-04-continuous-run/` para evidencia: 79 archivos
generados por workers ciegos entre sí).

La política actual es:

  - El modo continuo se ejecuta como **orquestación interactiva**
    dentro de la sesión Claude Code activa, usando el `Agent` tool
    para delegar a sub-agentes (`.claude/agents/*.md`) bajo el contexto
    del orquestador (este Claude). No se spawnean instancias `claude -p`.

  - Entrada: `/continuous-run` (orquestación interactiva), iteraciones
    vía `/continuous-run-tick` o `/loop /continuous-run-tick`.

Importar o ejecutar este módulo levanta `SystemExit` con código 2.
El código original está en git history (commit anterior a 2026-05-11).
"""
from __future__ import annotations
import sys


_DEPRECATION_MSG = (
    "[harness.lib.daemon] DEPRECADO Y NEUTRALIZADO (2026-05-11).\n"
    "Razón: spawneaba `claude -p` headless sin orquestación, produciendo\n"
    "       outputs IA descoordinados (ver Bitacora/2026-05-04-continuous-run/).\n"
    "Uso correcto:\n"
    "  - Iteración: /continuous-run-tick   (Agent tool, contexto compartido)\n"
    "  - Sesión:    /continuous-run        (orquestación interactiva)\n"
    "  - Verificadores deterministas:      python3 harness/cli.py verify --all\n"
    "Para recuperar el código viejo: git log --all -- harness/lib/daemon.py\n"
)


def run_daemon(*_args, **_kwargs) -> None:
    sys.stderr.write(_DEPRECATION_MSG)
    raise SystemExit(2)


if __name__ == "__main__":
    sys.stderr.write(_DEPRECATION_MSG)
    raise SystemExit(2)
