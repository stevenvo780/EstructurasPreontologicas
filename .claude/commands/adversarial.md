---
description: Red-team contra una afirmación específica del manuscrito. Busca el modo de fallo más serio.
argument-hint: <archivo>:<línea> "<afirmación literal>"
allowed-tools:
  - Read
  - Grep
  - Bash
---

Lanza `@adversarial-reviewer` contra la afirmación dada por el usuario.

1. Lee el contexto del archivo en la línea indicada.
2. Confirma con el usuario que la afirmación citada es la que quiere atacar.
3. Invoca `@adversarial-reviewer` con la afirmación + contexto.
4. Tras el reporte, si el agente encontró objeciones serias (`WARN_THESIS_VULNERABLE`):
   - Lista las 3 objeciones al usuario.
   - Pregunta cuál de las dos respuestas (blanda/dura) prefiere.
   - Marca el item en `needs_human` para Jacob.
