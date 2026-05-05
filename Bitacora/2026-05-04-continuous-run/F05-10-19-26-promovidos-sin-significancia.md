# F05-10 — Casos 19 y 26 promovidos a Trend sin significancia estadística

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap05 (2026-05-05). Crítica anclada en Ioannidis 2005 (PLoS Med 2(8):e124) — separar tamaño de efecto de significancia estadística; promover por EDI alto sin p<α y sin replicabilidad es categoría inventada.

## (a) Verificación de la afirmación contra metrics.json

Lectura directa de outputs canónicos (fuente de verdad §4 CLAUDE.md):

### Caso 19 — Acidificación oceánica
`09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/metrics.json` → `phases.real`:

- `edi.value = 0.7278`
- `permutation_pvalue = 0.49` (no significativo a α=0.05)
- `permutation_significant = False`
- `bootstrap CI = [0.659, 0.791]` (estrecho pero no informa significancia)
- `trend_bias.trend_ratio = 1.0`, `trend_r2 = 0.861` → **el EDI está dominado por la tendencia, no por estructura acoplada genuina**
- `weighted_value (LoE=0.6) = -0.00011` (negativo tras ponderar por evidencia)
- `val_steps = 360`

Texto actual en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:140` (Tabla 5.7.8 Null) describe el caso así: *"EDI elevado pero p=0.49 (no significativo); promovido a Nivel 1\* trend con cautela inferencial — candidato a re-evaluación con sondas físicas alternativas"*.

**Verdict:** la promoción a Trend con asterisco es exactamente la categoría inventada que Ioannidis 2005 advierte. Un p=0.49 con weighted_value negativo no es Trend — es Null con tendencia espuria.

### Caso 26 — Starlink
`09-simulaciones-edi/26_caso_starlink/outputs/metrics.json` → `phases.real`:

- `edi.value = 0.6892`
- `permutation_pvalue = 1.0`
- `permutation_significant = False`
- `bootstrap CI = [0.6892, 0.6892]` (**degenerado**: lo = hi = value, no hay distribución bootstrap real)
- `val_steps = 1` (un solo punto de validación)
- `phases.synthetic.edi.value = -0.457` (negativo y fallido)

Texto actual en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:124` (Tabla 5.7.7 Trend): *"0.6892 | 1.0000 | val_steps=1 — exploratorio"*.

**Verdict:** val_steps=1 con CI bootstrap degenerado y p=1.0 no es Trend ni siquiera con asterisco. Es un dato no-evaluable. Inclusión en Trend infla el numerador del conteo.

## (b) Propuesta de edición concreta — `needs_human` parcial

Reformulación propuesta (firma de Jacob requerida para alterar la taxonomía):

1. **Eliminar caso 26 de Tabla 5.7.7 (Trend).** Reclasificar como "exploratorio no-evaluable" en una tabla separada o nota al pie: "val_steps=1, CI bootstrap degenerado, p=1.0 — no admite inferencia."
2. **Eliminar caso 19 de Tabla 5.7.8 con la nota actual de promoción.** Mantener en Null sin asterisco; la nota debe leer literalmente: *"EDI nominal 0.728 dominado por trend (r²=0.861, weighted_value=-0.0001); p=0.49 — no significativo. Re-evaluación con sondas alternativas pendiente (B-T multi-probe-null caso 19)."* Sin "promovido a Nivel 1*".
3. **Recalcular conteos del corpus.** Si los textos de §05/§06 dicen "30 casos con discriminación EDI" o equivalente, descontar 19 y 26 de cualquier numerador de "Trend o superior". El conteo correcto debe distinguir: (i) casos con p<α genuino; (ii) casos exploratorios; (iii) casos null; (iv) casos no-evaluables.
4. **Sustituir asterisco "*"** (categoría inventada) por marcadores operativos verificables: `p<0.05`, `p≥0.05`, `n.e.` (no-evaluable). Eliminar "trend con cautela inferencial" como nivel.

Bloqueado para asistencia: la decisión de mantener o no la fila para 19/26 en alguna tabla, y de re-numerar el conteo agregado del corpus, **es decisión filosófico-estructural de Jacob** (afecta la narrativa de "40 casos justifican operativamente la tesis" en cap 05/06). Marcado **needs_human (H-J)**.

Acción operativa que la asistencia sí puede ejecutar tras firma: edit del archivo según pauta arriba; regenerar `TesisFinal/Tesis.md` con `python3 TesisFinal/build.py`; añadir entrada B-T `multi-probe-null --case 19` para sondas alternativas.

## (c) Costo argumentativo declarado

- **Concesión 1.** El conteo del corpus se reduce: si antes se afirmaba "X casos con discriminación EDI > 0", X baja en al menos 2. Esto debilita el argumento cuantitativo del aparato pero **fortalece** la honestidad metodológica (CLAUDE.md §1, §7).
- **Concesión 2.** El nivel "Trend (Nivel 1)" pierde dos miembros, dejando solo 10 (Justicia, EDI=0.227, p=0.48), 28 (Fuga cerebros, p=0.998), 01 (Clima, p=0.999) — los tres también con p≥α. Esto **expone que la categoría Trend completa carece de discriminación estadística**, no solo 19/26. Posible necesidad de eliminar el bloque entero o renombrarlo "exploratorios sin significancia".
- **Concesión 3.** El caso 19 había servido como gancho narrativo en cap 05-02 (acidificación → biología). Reclasificarlo como Null obliga a reescribir el gancho o a sustituirlo por un caso publicado de regime shift (Scheffer) según ya está propuesto en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:179`.
- **Beneficio.** El aparato gana defensibilidad bajo crítica hostil tipo Ioannidis: separa cleanly "tamaño de efecto" (EDI) de "significancia" (p). El precio es admitir que solo los Bloques I-IV (Strong/Robust/Weak/Suggestive) sostienen la tesis empíricamente; Trend/Null no son gradiente sino discontinuidad.

## Estado

`needs_human` — propuesta de edición lista; espera firma de Jacob para reformular taxonomía y recontar corpus. La asistencia no debe ejecutar la edición sin firma porque toca la narrativa estructural del cap 05.

Cross-ref: F05-10 (este archivo), F03-03 (dossier tautológico), F02-08 (criterios). Patrón común: categorías inventadas para que las cifras encajen — CLAUDE.md §1 explícitamente prohibido.
