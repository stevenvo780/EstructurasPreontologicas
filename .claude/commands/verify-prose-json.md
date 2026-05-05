---
description: Verifica que las cifras EDI/p_perm/RMSE en la prosa coincidan con metrics.json (CLAUDE.md §4).
allowed-tools: Bash, Read
---

1. `python3 harness/cli.py verify --prose-json`
2. Si hay discrepancias:
   - Lista las primeras 5 al usuario con file:line.
   - Recuerda: ante divergencia, gana el JSON. La prosa se reescribe.
   - Pregunta si quiere lanzar `@prose-json-verifier` para revisión profunda.
3. Si pasa: las cifras detectadas en prosa coinciden con JSON dentro de tolerancia (default 0.5%).
