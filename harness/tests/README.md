# Tests del harness

Tests pytest con fixtures conocidas. Cada test verifica que un verificador detecta lo que debe detectar y NO levanta falsos positivos en casos limpios.

## Ejecutar

```bash
cd /datos/repos/EstructurasPreontologicas
python3 -m pytest harness/tests/ -v
# o sin pytest:
python3 harness/tests/test_verifiers.py
```

## Convención de fixtures

`harness/tests/fixtures/` contiene mini-textos con casos conocidos:
- `chapter_with_decorative_citation.md` — debe disparar `verify_decorative_citations`.
- `chapter_with_paginated_citation.md` — debe pasar limpio.
- `chapter_with_indulgence.md` — debe disparar `verify_self_indulgence`.
- `chapter_with_debt_section.md` — debe pasar `verify_debt_index`.

Los tests cargan estas fixtures e invocan los verificadores aislados (no escanean todo el repo).
