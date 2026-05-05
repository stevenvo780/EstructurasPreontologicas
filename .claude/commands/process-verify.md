---
description: Verifica un argumento o pipeline PASO POR PASO (no solo el outcome). Mitiga reward hacking textual.
argument-hint: <archivo o sección o pipeline>
allowed-tools: Read, Grep, Bash
---

Lanza `@process-verifier` sobre el argumento/pipeline indicado.

1. Lee el archivo/sección.
2. Identifica si es argumento filosófico (capítulos 02/04/05) o pipeline técnico (09-simulaciones-edi).
3. Invoca `@process-verifier` con el contexto.
4. Tras el reporte, si encontró pasos rotos (`WARN_BROKEN_STEP`):
   - Lista los pasos rotos.
   - Pregunta al usuario si reescribir, eliminar, o reabrir tarea en TAREAS_PENDIENTES.md.
