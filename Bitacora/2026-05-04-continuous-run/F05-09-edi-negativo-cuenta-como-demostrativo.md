# F05-09 — EDI negativo cuenta como "demostrativo"

**Fecha:** 2026-05-05
**Origen:** adversarial-reviewer cap05 (2026-05-05)
**Archivo afectado:** `05-aplicaciones/07-mapa-aplicaciones-corpus.md` (líneas 17, 134)

## (a) Verificación de la afirmación

**Afirmación adversarial:** la Tabla 5.7.1 cuenta 30 casos como "Modo demostrativo (con dossier completo)" sin separar resultados por signo de EDI. Esto pone bajo la misma etiqueta:

- 4 strong (EDI 0.33-0.65, p<0.01) — caso 04, 16, 20, 27.
- 1 strong sin gate (EDI 0.78) — caso 24.
- 8 weak (EDI 0.13-0.30, p<0.05) — casos 05, 11, 13, 14, 15, 18, 22, 30.
- 2 suggestive (EDI 0.02-0.08) — caso 09, 21.
- 4 trend (p NS) — caso 01, 10, 26, 28.
- 8 null incl. EDI<0 — casos 02 (-0.12), 03 (-0.09), 12 (-0.15), 17 (-0.02), 19 (+0.73 pero p=0.49), 23 (-1.00), 25 (-0.15), 29 (-0.88).
- 3 controles de falsación (06, 07, 08).

**Verificación textual:** confirmada. Línea 17 dice literalmente *"Modo demostrativo (con dossier completo): 30 casos"*. La tabla 5.7.1 (líneas 26-34) suma efectivamente 4+1+8+2+4+8+3 = 30. La etiqueta "demostrativo" se aplica de forma indiferenciada a casos con falsación por la propia métrica (EDI≤0) — a 23 (-1.00) y 29 (-0.88) en particular, que indican degradación predictiva tras desacoplar, no acoplamiento detectable.

**Validez de la objeción:** sólida. "Demostrativo" en CLAUDE.md y en el glosario operativo connota *caso que instancia operativamente el aparato con éxito*. Un EDI≤0 con p≈1 NO instancia el aparato; o bien funciona como control negativo (la ablación no degrada porque no hay acoplamiento real), o bien indica no-aplicabilidad de la sonda elegida. Englobarlos bajo "demostrativo" oculta el costo argumentativo y debilita la fuerza de los casos genuinamente positivos.

## (b) Propuesta de edición — needs_human (firma Jacob)

La taxonomía a aplicar **requiere decisión filosófica** sobre el estatus epistémico de los EDI<0: ¿control negativo no diseñado? ¿no-aplicabilidad? ¿falsación local de la sonda? Tres salidas posibles, cada una con costo:

**Opción 1 — Reclasificar EDI<0 como controles negativos no-diseñados:**
unirlos a los 3 controles de falsación (Bloque VII). Costo: agranda la cifra "100% de falsación correcta" desde 3/3 a 8/8, pero diluye la fuerza de los 3 controles diseñados ex-ante.

**Opción 2 — Reclasificar EDI<0 como no-aplicabilidad de la sonda:**
crear bloque "VIII — Sonda no aplicable" para 02, 03, 12, 23, 25, 29 (y revisar 17 con EDI≈0). Costo: requiere caso-por-caso justificar por qué la sonda elegida no aplica, no es una decisión global automática.

**Opción 3 — Mantener nomenclatura pero distinguir en el resumen ejecutivo:**
sustituir línea 17 *"Modo demostrativo (con dossier completo): 30 casos"* por desglose:
- Casos con instancia positiva del aparato (EDI>0, p<0.05): N=15.
- Casos con señal sugerida (EDI>0, p NS o suggestive): N=4 (incluye trend).
- Casos null/no-instancia (EDI≤0 o p≈1 con sonda inadecuada): N=8.
- Controles de falsación diseñados: N=3.

La aceptance del task propone *N=12 demostrativos, N=8 nulls, N=8 negativos, N=2 suggestive*, pero no cuadra con los conteos actuales (4+1+8=13 weak+, no 12; los EDI<0 son 6 estrictos, no 8) ni separa "trend" del resto. La discrepancia confirma que la reclasificación requiere criterio humano.

**Edición concreta mínima sin firma humana** (segura, no compromete taxonomía):
- Reemplazar línea 17: *"Modo demostrativo (con dossier completo)"* → *"Casos con dossier técnico ejecutado (incluye positivos, nulls y controles)"*.
- Añadir nota bajo Tabla 5.7.1: *"'Dossier completo' indica que el caso fue ejecutado con el protocolo C1-C5 y produce metrics.json reproducible. NO equivale a 'demostración positiva del aparato': los Bloques V-VII (12 casos: 4 trend + 8 null) NO instancian acoplamiento detectable; funcionan como casos de no-aplicabilidad o falsación local."*

Esta edición textual menor preserva las cifras y NO reorganiza tablas, pero corrige la equivocidad léxica detectada.

## (c) Costo argumentativo declarado

Aceptar la objeción reduce la cifra de impacto retórico: en vez de "30 casos demostrativos" la tesis pasa a defender ~15-19 casos con instancia positiva del aparato. **Esto es honestidad metodológica, no debilidad** (cf. CLAUDE.md §7). La fuerza inferencial real de la tesis no depende de N=30 indistinto sino de:

1. La heterogeneidad de dominios donde EDI>0 con p<0.05 sí aparece (15 casos en física, ecología, epidemiología, social, técnico).
2. El éxito 3/3 de controles diseñados.
3. La existencia documentada de 8 casos null/negativos que **operan como evidencia adicional de discriminación** (no de fracaso): el aparato no produce EDI alto cuando no hay acoplamiento real.

El costo de NO corregir es mayor: queda como flanco abierto a la crítica de que "demostrativo" enmascara falsaciones, lo que invalida la afirmación del 50% señal significativa al hacerla parecer underselling de un dataset 100% exitoso.

## Marca de cierre

**Estado:** `needs_human` — la opción 1 vs 2 vs 3 requiere firma Jacob.
**Acción asistencia segura:** preparar edit textual propuesto en *Edición concreta mínima* arriba, pendiente de validación humana antes de aplicar al manuscrito.
**No editado:** Tesis.md, metrics.json, ni 05-aplicaciones/07-mapa-aplicaciones-corpus.md (esperando decisión).
