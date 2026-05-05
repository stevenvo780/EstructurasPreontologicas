---
description: Prepara material de engagement filosófico con un autor primario (Bunge, Dennett, Simondon, Strawson, Chalmers, Goff, Lakatos, Maturana-Varela, Haken).
argument-hint: <apellido_autor> [obra]
allowed-tools: Bash, Read
---

1. Verifica que el PDF existe: `ls 07-bibliografia/ | grep -i "$1"`
2. Si existe: invoca `@philosophical-reader` con el autor para que produzca BORRADOR-IA en `harness/reports/<fecha>-engagement-$1.md`.
3. Si no existe: avisa al usuario que el PDF falta — NO inventes engagement sin fuente directa (CLAUDE.md §5).
4. Tras el reporte: recuerda al usuario que el output es BORRADOR y requiere H-J5 (firma de Jacob).
