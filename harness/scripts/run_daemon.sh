#!/usr/bin/env bash
# DEPRECADO Y NEUTRALIZADO (2026-05-11)
#
# Este launcher arrancaba un daemon que spawneaba `claude -p` en paralelo.
# Esa arquitectura producía instancias Claude independientes, sin contexto
# compartido y sin orquestación. La política actual usa el `Agent` tool dentro
# de la sesión interactiva (un único contexto orquestador).
#
# Uso correcto:
#   /continuous-run          → orquestación interactiva (este Claude orquesta)
#   /continuous-run-tick     → una iteración (Agent tool)
#   /loop /continuous-run-tick → loop autoritmado, también vía Agent tool
#
# Para verificadores deterministas (sin LLM):
#   python3 harness/cli.py verify --all
#   python3 harness/cli.py pass
#
# El código original está en git history (commit anterior a 2026-05-11).

cat >&2 <<'EOF'
[run_daemon] DEPRECADO Y NEUTRALIZADO (2026-05-11).

Razón: spawneaba `claude -p` headless sin orquestación.
       Producía outputs IA descoordinados (79 archivos en
       Bitacora/2026-05-04-continuous-run/ son la evidencia).

Uso correcto:
  /continuous-run                  → orquestación interactiva
  /continuous-run-tick             → una iteración (Agent tool)
  /loop /continuous-run-tick       → loop autoritmado
  python3 harness/cli.py verify --all  → verificadores deterministas

Para recuperar el script viejo:
  git log --all -- harness/scripts/run_daemon.sh

EOF
exit 2
