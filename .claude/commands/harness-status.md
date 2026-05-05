---
description: Muestra estado actual del harness — última pasada, items needs_human, cola de ejecución.
allowed-tools: Bash, Read
---

1. `python3 harness/cli.py status`
2. Resume al usuario: última pasada, items needs_human, jobs en cola.
3. Si `needs_human` no está vacío: lista cada item y sugiere acción (qué slash command o sub-agente lo destrabaría).
4. NO recomiendas cierres — solo presentas estado.
