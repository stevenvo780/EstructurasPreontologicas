---
description: Verifica citas con paginación contra los PDFs en 07-bibliografia/ (CLAUDE.md §5).
allowed-tools:
  - Bash
  - Read
---

Ejecuta el verificador formal de citas y luego, si hay hits, invoca `@citation-agent` para análisis profundo.

1. `python3 harness/cli.py verify --citations`
2. Si `without_pagination_count > 0` o `without_pdf_in_07_count > 0`:
   - Resume al usuario los conteos.
   - Pregunta si quiere lanzar `@citation-agent` para resolver caso por caso.
3. Si todo pasa: confirma sin celebrar — solo significa que las citas detectadas tienen forma paginada, NO que estén verificadas contra el PDF (eso lo hace el sub-agente).
