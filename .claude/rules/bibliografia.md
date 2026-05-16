---
paths:
  - "07-bibliografia/**"
  - "**/04-debates/**/*.md"
  - "**/02-fundamentos/**/*.md"
---

# Citas bibliográficas

Reglas que aplican cuando trabajas con bibliografía o capítulos densos en citas.

## Cita textual con paginación o no cita

"Citas decorativas" — autor invocado como autoridad sin engagement con su argumento — son **fallo F6 declarado**. La biblioteca en `07-bibliografia/` es accesible: úsala.

- Si vas a citar (Bunge / Dennett / Simondon / Wittgenstein / Searle / Chalmers / Goff / Strawson / Lakatos / Maturana-Varela / Haken / etc.), trae **página + cita verbatim**.
- Si no puedes acceder a la fuente, **no cites**, o cita fuente secundaria fiable y declara que es secundaria.
- Si el verificador `verify_citation_pagination` reporta un hit, delega a `@citation-agent` (haiku) para resolverlo. Si la cita decorativa requiere engagement filosófico real (no solo pagination), delega a `@philosophical-reader` (opus).

## Para autores fuera de `07-bibliografia/`

Delega a `@bibliography-fetcher` (sonnet). Usa MCPs `paper-search`, `arxiv`, `fetch` cuando estén disponibles; fallback WebSearch + WebFetch.

NUNCA inventes metadata (DOI, año, página). Si no puedes verificar, marca `needs_human`.

## Antes de incluir una cita

Tres preguntas:

1. ¿Tengo el PDF en `07-bibliografia/`? Si no → ¿es accesible vía bibliography-fetcher?
2. ¿Reproduzco la cita verbatim con `pdftotext -layout` + búsqueda?
3. ¿El autor está siendo invocado como argumento (engage con su tesis) o como autoridad ("X dice")? Si es lo segundo → es decorativa.

## Verificadores relevantes

- `python3 harness/verifiers/verify_citation_pagination.py` — pagina faltante
- `python3 harness/verifiers/verify_decorative_citations.py` — menciones decorativas
