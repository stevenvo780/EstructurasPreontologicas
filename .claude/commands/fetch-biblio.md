---
description: Recupera papers académicos externos (arXiv, Semantic Scholar, OpenAlex) para autores/temas no presentes en 07-bibliografia/.
argument-hint: <autor> [tema o palabras clave]
allowed-tools: Bash, Read
---

Lanza `@bibliography-fetcher` para recuperar metadata de papers externos.

1. Verifica si el autor ya está localmente:
   ```bash
   ls 07-bibliografia/ | grep -i "$1"
   ```
2. Si SÍ está: avisa y sugiere `/engage-author $1` (con `@philosophical-reader`).
3. Si NO está: invoca `@bibliography-fetcher` con `$1` + resto de args.
4. Tras el reporte: si el usuario quiere descargar PDFs, recuerda consideraciones de copyright y pide confirmación explícita por cada uno.
