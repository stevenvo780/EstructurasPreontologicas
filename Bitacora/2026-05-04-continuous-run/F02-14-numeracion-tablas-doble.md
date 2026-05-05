# F02-14 — Numeración doble de tablas en cap 02-01

**Fecha:** 2026-05-04
**Origen:** hallazgo adversarial-reviewer cap02 (2026-05-05)
**Archivos señalados:** `02-fundamentos/01-ontologia-material-relacional.md:23, :228`

## (a) Verificación de la afirmación

Confirmada con grep sobre el archivo. Estado **antes** del fix: 12 etiquetas `**Tabla 2.1.X.**` para 6 tablas (cada tabla tenía dos labels):

```
23  **Tabla 2.1.1.**     ← duplicado idéntico
25  **Tabla 2.1.1.**
105 **Tabla 2.1.2.**     ← duplicado idéntico
107 **Tabla 2.1.2.**
156 **Tabla 2.1.3.**     ← duplicado idéntico
158 **Tabla 2.1.3.**
228 **Tabla 2.1.6.**     ← inconsistente (debería ser 2.1.4)
230 **Tabla 2.1.4.**
263 **Tabla 2.1.4.**     ← inconsistente (debería ser 2.1.5)
265 **Tabla 2.1.5.**
343 **Tabla 2.1.5.**     ← inconsistente (debería ser 2.1.6)
345 **Tabla 2.1.6.**
```

Las parejas 4-6 mostraban **numeración corrida**: el primer label conservaba el ordinal de una versión previa del cap (2.1.6, 2.1.4, 2.1.5) mientras el segundo reflejaba un re-orden parcial.

## (b) Causa raíz — bug en `scripts/number_tables.py`

El script auto-numerador tenía una regex `already_labeled` que **no matcheaba el formato que él mismo emite**:

- Inserta:   `**Tabla 2.1.1.**`   (prefijo multi-dot `2.1` + ordinal + punto final + `**`)
- Detectaba: `\*\*Tabla [\dA-Z]+\.\d+\*\*`   (solo un dot, sin punto final)

Resultado: cada corrida del script veía toda tabla como "no etiquetada" y **anteponía un nuevo label**, acumulando duplicados con numeración independiente. El bug afecta a todos los capítulos con prefijo multi-dot (02-fundamentos, 03-formalizacion, etc.) y a Anexos (`A.X`).

## (c) Acción ejecutada

1. **Fix del script** (`scripts/number_tables.py:94, :112`): regex actualizada a `\*\*Tabla [\dA-Z]+(?:\.\d+)+\.?\*\*` (ídem `Figura`). Ahora reconoce su propio output.
2. **Dedup en cap 02-01** vía sustitución `(label)\n\n\1\n → \1\n` después de igualar los pares 4-6 a sus numeraciones canónicas (2.1.4 / 2.1.5 / 2.1.6).
3. **Re-ejecución `python3 scripts/number_tables.py`**: reportó `Total: 0 tablas + 0 figuras numeradas` (idempotente). Estado **después**: 6 etiquetas monotónicas (`2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.6`) en líneas 23, 103, 152, 222, 255, 333.

## Acceptance

- [x] Script ejecutado sin errores.
- [x] 0 tablas con doble encabezado en cap 02-01.
- [x] Numeración monótona (2.1.1 → 2.1.6).
- [x] Script idempotente (2ª corrida = 0 cambios).

## Costo argumentativo declarado

- Cambios **puramente formales** sobre etiquetas de tabla: no se altera contenido, ni numeración cruzada en otros capítulos (la 2ª corrida del script no modificó nada).
- El fix de regex puede destapar **labels stale** acumulados en otros capítulos por corridas previas. Conviene auditoría análoga sobre `03-formalizacion/`, `04-debates/`, `Anexos/` (no parte de esta tarea, pero registrable como deuda B-T16).
- No se tocó `Tesis.md` ni `metrics.json`. `TesisFinal/build.py` debe re-ejecutarse en el próximo cierre para reflejar la limpieza en el ensamblado.

## Estado

**RESUELTO** — sin needs_human. La asistencia podía cerrar porque (1) el bug es operativo, no filosófico; (2) la numeración correcta se infiere del orden posicional sin decisión autoral; (3) ningún texto de prosa cambió.
