---
description: Audita secciones "Deuda residual" en cada capítulo (CLAUDE.md §7).
allowed-tools: Bash, Read
---

1. `python3 harness/cli.py verify --debt`
2. Si hay capítulos requeridos sin sección de deuda, o secciones sin fecha:
   - Lista al usuario.
   - Pregunta si quiere lanzar `@debt-validator` para proponer borradores.
3. Si pasa: las secciones declaradas tienen forma válida (no implica que la deuda declarada sea exhaustiva — solo que existe y está fechada).
