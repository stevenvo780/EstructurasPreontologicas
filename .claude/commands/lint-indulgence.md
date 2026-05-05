---
description: Lint de auto-indulgencia: versionología, manierismo, plantillas spam (CLAUDE.md §1).
allowed-tools: Bash, Read
---

1. `python3 harness/cli.py verify --self-indulgence`
2. Si `flag_hits_count > 0` o `template_duplicates_count > 0`:
   - Lista al usuario los primeros hits con file:line.
   - Si los hits están en `Bitacora/` reciente o en outputs propios: invoca `@self-indulgence-linter` para reescritura concreta.
3. Si pasa: el manuscrito y bitácoras no tienen los patrones-bandera. NO significa "prosa de calidad" — solo "sin las banderas léxicas conocidas".
