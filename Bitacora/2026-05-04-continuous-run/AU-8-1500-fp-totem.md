# AU-8 — "0/1500 falsos positivos" — totem retórico SIN regenerador bit-a-bit

**Fecha:** 2026-05-04
**Origen:** Hallazgo adversarial-reviewer 2026-05-05 (5 ocurrencias literales en 06-cierre/).
**Tipo:** Auditoría retórico-metodológica + verificación de regenerador (CLAUDE.md §1, §4).
**Estado:** `needs_human` (la edición toca defensa argumental + cifra reportada).
**Relación:** complementa y amplía `F06-01-1500-fp-totem-7-veces.md` con un hallazgo nuevo.

---

## (a) Verificación de la afirmación

### Conteo de ocurrencias literales

≥ 9 menciones de `0/1500` (o variante "1500 ejecuciones") en `06-cierre/` —
ya enumeradas en `F06-01-1500-fp-totem-7-veces.md` (no se repite la tabla).

### Hallazgo NUEVO: el numeral 1500 NO se reproduce con ningún script declarado

Búsqueda exhaustiva de scripts de hostile testing en el repo
(`grep n_trials Bitacora/2026-04-28-cierre-severo/`):

| Script | `n_trials` | Resultado JSON |
|---|---|---|
| `N1_falsos_positivos.py` | **500** | `N1_resultados.json` (`n_trials: 500`) |
| `V4_06_hostile_multiescala.py` | **500** | `V4_06_resultados.json` (`n_trials: 500`) |
| `N5_hostile_testing.py` | **1000** | `N5_resultados.json` (`n_trials: 1000`, `tasa_overall_pass: 0.0`) |

**Suma de runs declarados: 500 + 500 + 1000 = 2000**, no 1500.

**Ningún archivo `*.py` ni `*.json` del repo contiene `n_trials=1500`** para hostile
testing del gate (la única mención de `1500` en el motor es `n_boot=1500` del
perfil agresivo de bootstrapping, que es OTRA cosa: re-muestreo dentro de cada
caso, no random walks contra el gate).

### Implicaciones

1. **CLAUDE.md §4 violado:** la cifra `0/1500` reportada 9 veces en `06-cierre/`
   y propagada a `02-fundamentos/01-ontologia-material-relacional.md:118` y a
   `Tesis.md:176, 200, 1003, 7244, 7831, 8056, 8063` **no tiene comando regenerador
   exacto.** No se reproduce bit-a-bit con ningún script versionado.

2. Existen dos lecturas posibles, ambas problemáticas:
   - **Lectura A — agregación informal:** "1500" sería suma parcial de N1+V4_06+N5
     redondeada o truncada (500+500+1000 = 2000; no 1500). El número agregado de
     "0 falsos positivos" sí es defendible (N1: 0/500, V4_06: 0/500, N5: 0/1000
     según `tasa_overall_pass: 0.0`), pero el denominador correcto es **2000**, no 1500.
   - **Lectura B — selección parcial:** "1500" agregaría dos de los tres scripts
     (e.g. N5+N1 = 1500). En ese caso, V4_06 quedaría arbitrariamente excluido sin
     justificación documentada.

3. **Wilson 95 % CI** (ya señalado en F06-01): para `0/1500`, CI = [0, 0.00255].
   Para el conteo correcto `0/2000`, CI = [0, 0.00191]. La diferencia es marginal,
   pero el numeral correcto importa para honestidad metodológica.

4. **Argumento ya conocido** (heredado de F06-01): el gate C1-C5 filtra RW por
   construcción (RW carece de sonda macro y ablación contrafáctica). Reportar
   `0/N` como evidencia de **discriminación contra rivales** es categóricamente
   incorrecto; lo demuestra AUC-ROC=0.886 vs ARIMA y 3/3 controles falsados.

---

## (b) Propuesta de edición concreta — `needs_human`

### B-1: corregir el denominador (acción técnica de bajo riesgo)

Reemplazar literalmente, en TODAS las ocurrencias del repo (no solo `06-cierre/`):

- `0/1500` → `0/2000` (si se asume agregación N1+V4_06+N5)
- `1500 ejecuciones` → `2000 ejecuciones`
- `1500 random walks` → `2000 random walks`

**Ubicaciones afectadas** (verificadas con grep):
- `06-cierre/01-conclusion-demostrativa.md`: líneas 5, 174, 246, 253
- `06-cierre/04-versiones-cortas-defensa.md`: líneas 25, 60, 114
- `06-cierre/05-respuestas-tipo-defensa.md`: línea 61
- `02-fundamentos/01-ontologia-material-relacional.md`: línea 118
- `06-cierre/02-guia-de-defensa.md`: línea 136 (heredada de F06-01)

**Nota a pie obligatoria** (única, anclada en una sola sección canónica):

> **Nota.** Hostile testing agregado: `N1_falsos_positivos.py` (n=500),
> `V4_06_hostile_multiescala.py` (n=500), `N5_hostile_testing.py` (n=1000),
> total n=2000 random walks. Reproducible vía
> `python3 Bitacora/2026-04-28-cierre-severo/N5_hostile_testing.py`
> (resultado canónico en `N5_resultados.json`: `tasa_overall_pass: 0.0`,
> `fraction_edi_above_030: 0.0`). Wilson 95 % CI = [0, 0.00191].

### B-2: reducir 5+ ocurrencias literales a 1 cita interna

Heredado y consistente con F06-01: conservar **una** mención canónica en
`01-conclusion-demostrativa.md:253` con CI Wilson y la aclaración de alcance
del §3.4. Las otras 4-8 ocurrencias se reemplazan por remisión interna
("ver §3.4" / "ver Robustez del gate") sin recitar la cifra.

### B-3: nota de alcance (§3.4) — heredada de F06-01

Mantener idéntica al draft B-2 de F06-01: el RW masivo certifica integridad de
implementación, no discriminación contra rivales con estructura. Esa carga la
sostienen AUC-ROC=0.886 y 3/3 controles falsados.

---

## (c) Costo argumentativo declarado

1. **Pérdida retórica menor:** corregir `1500 → 2000` no debilita el argumento
   (al contrario, n mayor → CI más estrecho). Pero rompe ~9 ocurrencias verbatim
   ya circuladas en borradores previos. Riesgo: confusión si algún revisor
   externo ya recibió la versión `1500`.

2. **Pérdida retórica heredada de F06-01:** sustituir el totem `0/1500` por
   `≤ 0.19 % al 95 %` es estadísticamente honesto pero menos vendible en
   defensa oral. Trade-off ya documentado y aceptado en F06-01.

3. **Concesión nueva:** el manuscrito debe declarar explícitamente que el
   numeral previo (`1500`) era **agregación informal sin script único
   regenerador**. Esta concesión es CLAUDE.md §7 puro: "deuda declarada es
   virtud, deuda oculta es fraude".

4. **Beneficio:** alineamiento estricto con CLAUDE.md §4 ("cada cifra reportada
   debe poder regenerarse con un comando"). Tras B-1, la cifra `0/2000` con
   nota a pie cumple el criterio bit-a-bit.

---

## Acción requerida

- **`needs_human` para Jacob:** firmar B-1 (cambio de cifra `1500 → 2000` o,
  alternativamente, reformular como `0/N con N ∈ {500, 1000, 2000}` según
  qué runs Jacob considere canónicos para el cierre).
- **Decisión filosófica pendiente:** ¿el denominador agregado es 2000 (los tres
  scripts) o solo el run N5 (1000)? F06-01 propone CI Wilson sin tocar el numeral;
  esta auditoría sostiene que **el numeral está mal** y debe corregirse antes
  de aplicar cualquier reformulación retórica.
- **Tarea técnica post-firma (B-T):** aplicar B-1 + B-2 + B-3, regenerar
  `TesisFinal/Tesis.md` con `python3 TesisFinal/build.py`, verificar que
  `harness/scripts/verify_*` no detecte regresiones.
- **NO tocar** `metrics.json` ni `TesisFinal/Tesis.md` directamente
  (CLAUDE.md §4 + harness hooks).

---

## Aceptación (verificable post-firma)

- [ ] Ninguna ocurrencia de `0/1500` en `*.md` del manuscrito (verificable con grep).
- [ ] ≤ 2 menciones en `06-cierre/` (heredado de F06-01).
- [ ] Una nota a pie con script regenerador + seed + ruta a `N5_resultados.json`.
- [ ] Wilson CI declarado en la mención canónica.
- [ ] Aclaración §3.4 sobre alcance (gate filtra RW por construcción).
