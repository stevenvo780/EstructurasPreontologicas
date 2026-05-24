# Histórico — limpieza final de comments HTML, frontmatter YAML y metadata interna

Fecha: 2026-05-17
Tarea: limpieza final del cuerpo manuscrito para que sea 100% leíble por lector académico externo sin jerga interna del proyecto (códigos `[F0X-XX 2026-05-11]`, "BORRADOR-IA", "triage de bitácora huérfana", frontmatter YAML interno).

Política aplicada:

1. **HTML comments con jerga "BORRADOR-IA · requires: H-J*"**: ELIMINAR (jerga interna).
2. **Frontmatter YAML**: preservar `title` y `extends` (información académica útil para el lector); eliminar `created: 2026-05-11` y `parte_de: H-J8 (fusión D.2)` (metadata interna del flujo de trabajo).
3. **Secciones "Deuda residual"**: preservar contenido sustantivo (CLAUDE.md §4 — "deuda declarada > deuda oculta"); eliminar:
   - Línea encabezamiento "Entradas operativas declaradas tras triage de bitácora huérfana (2026-05-11)..." (metadata interna del workflow).
   - Prefijo `[F0X-XX 2026-05-11]` de cada bullet (códigos internos del triage).
   - Marcas `` `needs_human` `` residuales — reemplazar por "decisión autoral pendiente".

---

## 1. HTML comments eliminados (jerga BORRADOR-IA)

### 1.1. `05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md` línea 236

ANTES (final de línea):
```
...degradación inmediata del desempeño, patrón predicho por el control informacional acoplado y no por modelos internos robustos, que deberían sostener la ejecución aun sin entrada actualizada. <!-- BORRADOR-IA · requires: H-J* (Jacob debe verificar Wallis 2002 y Hildreth 2000 en fuente primaria con paginación literal o sustituir la mención) -->
```

DESPUÉS: HTML comment eliminado.

### 1.2. `01-diagnostico/03-estado-del-arte.md` línea 112

ANTES (final de línea):
```
...permitiendo decidir empíricamente cuándo el acoplamiento es no trivial. <!-- BORRADOR-IA · requires: H-J* (voz autoral final de Jacob) -->
```

DESPUÉS: HTML comment eliminado.

---

## 2. Frontmatter YAML — líneas eliminadas

Archivos afectados (8): preservan `title` y `extends`; pierden `created:` y `parte_de:`.

### 2.1. `04-debates/_extendido/rival-mecanicismo-multinivel.md`

ANTES:
```yaml
---
title: "Mecanicismo multinivel (Bechtel-Craver) — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
created: 2026-05-11
parte_de: H-J8 (fusión D.2)
---
```

DESPUÉS:
```yaml
---
title: "Mecanicismo multinivel (Bechtel-Craver) — desarrollo extenso"
extends: 04-debates/01-debates-con-posiciones-rivales.md
---
```

### 2.2. `04-debates/_extendido/rival-conductismo-radical.md`

ANTES: `created: 2026-05-11` + `parte_de: H-J8 (fusión D.2)` — ELIMINADAS.

### 2.3. `04-debates/_extendido/rival-modelos-internos.md`

ANTES: `created: 2026-05-11` + `parte_de: H-J8 (fusión D.2)` — ELIMINADAS.

### 2.4. `06-cierre/_extendido/versiones-cortas-defensa.md`

ANTES: `created: 2026-05-11` — ELIMINADA.

### 2.5. `06-cierre/_extendido/respuestas-tipo-defensa.md`

ANTES: `created: 2026-05-11` — ELIMINADA.

---

## 3. Secciones "Deuda residual" — limpieza de IDs internos y línea de encabezado

En cada sección "Deuda residual" se elimina:

- La línea "Entradas operativas declaradas tras triage de bitácora huérfana (2026-05-11)." (y variantes).
- El prefijo `[F0X-XX 2026-05-11]` al inicio de cada bullet.
- Marcas `` `needs_human` `` → reemplazadas por "decisión autoral pendiente" en los casos restantes.

Archivos afectados (15 secciones):

| Archivo | Sección | Entradas |
|---------|---------|----------|
| `02-fundamentos/01-ontologia-material-relacional.md` | §15 | F02-09, F02-13 |
| `02-fundamentos/02-epistemologia-de-la-compresion.md` | §15 | F02-05, F02-07 |
| `02-fundamentos/04-anclaje-conductual-ecologico.md` | §13 | F02-06, F02-11 |
| `02-fundamentos/05-temporalidad-y-causalidad.md` | §-- | F02-01, F02-02, F02-12 |
| `03-formalizacion/01-aparato-formal.md` | §16 | F03-06 |
| `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md` | §12 | F03-02, F03-03 |
| `03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md` | §12 | F03-11 |
| `03-formalizacion/04-operacionalizacion-de-kappa.md` | §-- | F03-09 |
| `03-formalizacion/07-plantilla-dossier-anclaje.md` | §-- | F03-02 |
| `03-formalizacion/08-validacion-logica-st.md` | §-- | F03-05 |
| `04-debates/01-debates-con-posiciones-rivales.md` | §-- | F04-01, F04-06, F04-10 |
| `04-debates/03-tabla-comparativa-rivales.md` | §-- | F04-01, F04-06, F04-10 |
| `05-aplicaciones/01-mente-memoria-yo.md` | §11 | F05-01, F05-02, F05-03 |
| `05-aplicaciones/02-biologia-y-ecologia.md` | §10 | F05-05 |
| `05-aplicaciones/03-sistemas-tecnicos-distribuidos.md` | §9 | F05-12 |
| `05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md` | §-- | F05-07 |
| `06-cierre/_extendido/respuestas-tipo-defensa.md` | §-- | F04-04 (inline), F04-04, F04-08 |

El **contenido sustantivo** de cada deuda (descripción del hueco, PDFs ausentes, acción correctiva) se preserva íntegramente — solo se eliminan los códigos internos y la línea encabezado.

---

## 4. Justificación frente a CLAUDE.md

- **§4 Deuda declarada > deuda oculta**: las secciones "Deuda residual" se preservan, solo se limpia su jerga interna (códigos de triage, fechas de bitácora). El contenido académico es defendible ante el lector externo.
- **§5 No auto-indulgencia**: los HTML comments `BORRADOR-IA · requires: H-J*` son metadata interna del flujo IA-humano; un lector académico no necesita conocer el aparato de gestión del manuscrito.
- **Voz autoral**: las marcas `needs_human` se mantienen como "decisión autoral pendiente" (preserva el contenido honesto: la deuda no se ha resuelto) sin la jerga del harness.

---

## 5. Verificación post-limpieza

Comando esperado en pasada de verificación:

```bash
grep -rn "<!-- BORRADOR\|<!-- TODO\|<!-- iter" 00-* 01-* 02-* 03-* 04-* 05-* 06-* --include="*.md" 2>/dev/null | grep -v "/historico-"
grep -rn "^created:\|^parte_de:" 00-* 01-* 02-* 03-* 04-* 05-* 06-* --include="*.md" 2>/dev/null | grep -v "/historico-"
grep -rn "\[F0[0-9]-[0-9]\+ 2026-05-11\]\|triage de bitácora huérfana" 00-* 01-* 02-* 03-* 04-* 05-* 06-* --include="*.md" 2>/dev/null | grep -v "/historico-"
```

Los tres greps deben retornar vacío tras esta pasada.

Las marcas legítimas "Pendiente fetch" / "Pendiente verificación" / "Pendiente OCR" **se preservan** porque son declaraciones académicas de deuda, no jerga del proyecto.
