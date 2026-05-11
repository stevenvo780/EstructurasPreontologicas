# Convención `_extendido/`

Esta carpeta aloja material **extendido** que NO entra en el ensamblado de `TesisFinal/Tesis.md` (`TesisFinal/build.py` solo lista archivos explícitos en `PARTS`). La capa web lo expone bajo demanda en `/api/chapters/<cap>/extras` y `/api/chapters/<cap>/extras/<tema>.md`.

## Convención por archivo

Cada `<cap>/_extendido/<tema>.md` debe comenzar con frontmatter mínimo YAML:

```
---
title: Título legible del material extendido
extends: <cap>/<archivo-principal>.md
---
```

- `title`: cadena humana mostrada en la web. Si falta, se usa el primer `# H1` del cuerpo, o el nombre del archivo.
- `extends`: ruta relativa al archivo principal del que se extiende este material (informativo, no se valida).

## Reglas duras

- **NO** referenciar `_extendido/*.md` desde `TesisFinal/build.py`. La carpeta vive fuera del ensamblado por diseño.
- **NO** poner aquí el contenido único de un argumento: si un argumento solo existe en `_extendido/`, no aparece en la tesis impresa. `_extendido/` es elaboración, no carga argumental.
- `README.md` de cada carpeta es metadocumentación; queda excluido del listado de extras servido por la API.
