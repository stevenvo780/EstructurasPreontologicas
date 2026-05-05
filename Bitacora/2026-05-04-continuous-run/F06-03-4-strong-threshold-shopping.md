# F06-03 — '4 strong' y threshold-shopping (Lakatos ad hoc)

**Fecha:** 2026-05-04
**Status:** `needs_human` (decisión editorial de Jacob)
**Origen:** adversarial-reviewer cap04+06 2026-05-05
**Files señalados:** `06-cierre/01-conclusion-demostrativa.md:5`, `06-cierre/01-conclusion-demostrativa.md:55`

## (a) Verificación de la afirmación

La objeción adversarial es **factualmente correcta** en su núcleo: el conteo "4 strong" depende de la pareja de umbrales (weak / strong) elegida, y la propia tesis lo reconoce.

Evidencia interna ya presente en el manuscrito:

- `06-cierre/01-conclusion-demostrativa.md:187`: "la composición numérica del corpus inter-dominio es frágil a umbrales (N4: pasar de 0.10/0.30 a 0.15/0.40 reduce strong de 5 a 3)".
- `06-cierre/01-conclusion-demostrativa.md:252`: "los umbrales 0.10/0.30 producen 5 strong; 0.15/0.40 produce 3; 0.05/0.20 produce 9 (N4). La composición es post-hoc."
- `04-debates/05-limitaciones-declaradas-consolidacion.md:21`: tabla L3 con la misma sensibilidad declarada y mecanización vía `common/threshold_sensitivity.py`.
- `Bitacora/2026-04-28-iteraciones-IA/V5_reportes_tecnicos/THRESHOLD_SENSITIVITY_REPORT.md:15-17`: los **4 casos canónicos** (Energía, Deforestación, Kessler, Riesgo Biológico) son `robust_strong` — **invariantes** sobre la grilla 0.05–0.15 × 0.20–0.40. Esto matiza la objeción: no es threshold-shopping libre; el subconjunto de los 4 con `overall_pass=True` (gate completo, no sólo umbral EDI) es estable bajo la rejilla razonable de umbrales declarada.
- Auditoría doctoral V3 (`06-auditoria-doctoral-v3-final.md:40`): "4 strong + 1 strong sin gate preservados bajo umbrales 0.10/0.30".

**Diagnóstico honesto:**
1. La afirmación "4 strong" en abstract (línea 5) y en la tabla 6.1.1 (línea 55) **no es** threshold-shopping si se entiende como "4 casos con `overall_pass=True`" (gate de 13 condiciones, no sólo EDI ≥ 0.30). El gate completo es el criterio operativo, no el umbral aislado.
2. Pero el lector hostil **lee "strong" como umbral EDI**, y bajo esa lectura el conteo cambia (3 / 4-5 / 9 según rejilla). La asimetría entre "strong (gate)" y "strong (umbral)" no está suficientemente marcada en abstract/tabla.
3. La sensibilidad **ya está declarada** en §5.4 (línea 187) y en §"No afirma" (línea 252), lo que neutraliza la acusación de ocultamiento. Lo que falta es **propagar la marca** al primer punto de mención (abstract + tabla 6.1.1) para que el lector no tenga que llegar a §5.4 para enterarse.

La objeción de Lakatos ad hoc es **parcialmente válida como crítica de presentación**, **inválida como crítica de fondo** (los 4 son invariantes en la rejilla razonable, y el manuscrito declara la sensibilidad).

## (b) Propuesta de edición concreta — `needs_human`

Tres opciones, ordenadas por costo argumental creciente. La decisión es de Jacob.

**Opción 1 (mínima, recomendada técnicamente).** Añadir paréntesis de sensibilidad en los dos puntos de primera mención, sin reabrir §5.4:

- Línea 5 (abstract): cambiar "4 casos `overall_pass=True`" → "4 casos `overall_pass=True` (gate completo de 13 condiciones; cf. §5.4 para sensibilidad de la grilla de umbrales: 3 con 0.15/0.40, 9 con 0.05/0.20)".
- Línea 55 (tabla 6.1.1, fila Strong gate completo): añadir nota al pie a la tabla: "Conteo bajo umbrales canónicos 0.10/0.30. Sensibilidad declarada en §5.4 y en `04-debates/05` tabla L3. Los 4 casos son invariantes a la rejilla razonable 0.05–0.15 × 0.20–0.40 según `THRESHOLD_SENSITIVITY_REPORT.md`."

Costo argumental: bajo. Solo formaliza lo que el manuscrito ya dice. Riesgo: ninguno; refuerza la honestidad declarada.

**Opción 2 (intermedia).** Además de Opción 1, sustituir "4 strong" por "4 robust_strong" en abstract y tabla, definiendo `robust_strong` como "invariante a la rejilla 0.05–0.15 × 0.20–0.40 bajo `common/threshold_sensitivity.py`". Coste: introduce vocabulario nuevo; obliga a actualizar glosario operativo (`00-proyecto/07-glosario-operativo.md`).

**Opción 3 (máxima, costosa).** Pre-registrar los umbrales con commit hash anterior al cierre del corpus. **Imposible retroactivamente**: el corpus ya está cerrado y los umbrales fueron fijados después de mirar los EDI. Declararlo como deuda fechada en §5.4 y aceptar que la pre-registración honesta no es posible para esta tesis; sería deuda hacia trabajo futuro. Coste: concesión filosófica fuerte; pero ya está implícita en línea 252 ("La composición es post-hoc").

## (c) Costo argumentativo declarado

- **Si se adopta Opción 1**: la tesis pierde la apariencia de robustez puntual ("4" sin matiz) pero gana defensibilidad bajo crítica hostil. El revisor no puede acusar de ocultamiento si la sensibilidad aparece junto al conteo. Coste neto: **negativo** (mejora la posición).
- **Si NO se edita**: la sensibilidad declarada en §5.4 + L3 es defensa suficiente en disputatio escrita, pero un revisor oral hostil puede señalar la asimetría abstract↔§5.4 como "burying bad news". Coste neto: **moderado** (riesgo en defensa oral).
- **Lo que NO puede hacer la asistencia**: decidir si la voz autoral filosófica de Jacob acepta el matiz parentético en abstract o prefiere mantener la formulación limpia y remitir a §5.4. Esa es decisión de voz, no técnica.

## Acción

- **Asistencia técnica:** este reporte. No edita `Tesis.md` ni `metrics.json`.
- **Jacob (firma humana, H-J*):** elegir Opción 1 / 2 / 3 y aplicar a:
  - `06-cierre/01-conclusion-demostrativa.md:5` (abstract)
  - `06-cierre/01-conclusion-demostrativa.md:53-55` (tabla 6.1.1)
  - Considerar también `06-cierre/02-guia-de-defensa.md` y `06-cierre/05-respuestas-tipo-defensa.md` (toda mención de "4 strong" en defensa).
- **Tras edición humana:** re-ejecutar `python3 TesisFinal/build.py`.

## Referencias verificadas

- `06-cierre/01-conclusion-demostrativa.md` líneas 5, 25, 55, 63, 85, 119, 182, 187, 252, 272.
- `04-debates/05-limitaciones-declaradas-consolidacion.md:21` — tabla L3.
- `Bitacora/2026-04-28-iteraciones-IA/V5_reportes_tecnicos/THRESHOLD_SENSITIVITY_REPORT.md:15-17`.
- `Bitacora/2026-04-28-cierre-pendientes/06-auditoria-doctoral-v3-final.md:20,40` — N4.
- `09-simulaciones-edi/common/threshold_sensitivity.py` — barrido mecanizado (no leído en esta pasada; declarado).
