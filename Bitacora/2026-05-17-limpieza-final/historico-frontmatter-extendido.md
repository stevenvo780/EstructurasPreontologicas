# Histórico — drenaje de frontmatter `parte_de: H-J8 (fusión D.2)` y `created:` en `04-debates/_extendido/rival-*.md`

Fecha de drenaje: 2026-05-24
Operación: eliminar líneas `created: 2026-05-XX` y `parte_de: H-J8 (fusión D.2)` del frontmatter YAML de los 7 archivos extendidos de rivales.

Razón: metadata de proceso interno (tarea H-J8) y fecha de creación no son metadata académica legítima; se conserva sólo `title` y `extends`.

## Estado previo (frontmatter capturado verbatim)

### `04-debates/_extendido/rival-enactivismo-radical.md`

```yaml
---
title: "Enactivismo radical — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
created: 2026-05-11
parte_de: H-J8 (fusión D.2)
---
```

### `04-debates/_extendido/rival-wolfram-physics-project.md`

```yaml
---
title: "Wolfram Physics Project — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
created: 2026-05-11
parte_de: H-J8 (fusión D.2)
---
```

### `04-debates/_extendido/rival-realismo-estructural-informativo.md`

```yaml
---
title: "Realismo estructural informativo (Ladyman-Ross) — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
created: 2026-05-11
parte_de: H-J8 (fusión D.2)
---
```

### `04-debates/_extendido/rival-cognitivismo-computacional.md`

```yaml
---
title: "Cognitivismo computacional — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
created: 2026-05-11
parte_de: H-J8 (fusión D.2)
---
```

### `04-debates/_extendido/rival-modelos-internos.md`

```yaml
---
title: "Modelos internos / control óptimo — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
created: 2026-05-11
parte_de: H-J8 (fusión D.2)
---
```

### `04-debates/_extendido/rival-mecanicismo-multinivel.md`

```yaml
---
title: "Mecanicismo multinivel (Bechtel-Craver) — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
created: 2026-05-11
parte_de: H-J8 (fusión D.2)
---
```

### `04-debates/_extendido/rival-conductismo-radical.md`

```yaml
---
title: "Conductismo radical — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
created: 2026-05-11
parte_de: H-J8 (fusión D.2)
---
```

## Estado posterior

Todos los archivos quedan con frontmatter mínimo:

```yaml
---
title: "<título>"
extends: 04-debates/01-debates-con-posiciones-rivales.md
---
```

Verificación final: `grep -l "parte_de\|fusión D\." 04-debates/_extendido/*.md` → 0 hits.
