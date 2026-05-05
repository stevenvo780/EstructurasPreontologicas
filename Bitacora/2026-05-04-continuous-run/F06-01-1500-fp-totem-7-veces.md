# F06-01-1500-fp-totem-7-veces — Auditoría del totem "0/1500 falsos positivos"

**Fecha:** 2026-05-04
**Origen:** Hallazgo adversarial-reviewer cap 04+06 (2026-05-05).
**Tipo:** Auditoría retórico-metodológica de cierre.
**Estado:** `needs_human` (la reformulación toca defensa argumental).

---

## (a) Verificación de la afirmación

Conteo real de la cadena `"0/1500 falsos positivos"` (o variantes con "1500 ejecuciones" / "random walk masivo") en `06-cierre/`:

| Archivo | Línea | Cita literal mínima |
|---|---|---|
| `01-conclusion-demostrativa.md` | 5 | "(0/1500 falsos positivos del gate completo bajo random walk masivo, 0/12 circularidad …)" |
| `01-conclusion-demostrativa.md` | 174 | "hostile testing (0/1500 falsos positivos)" |
| `01-conclusion-demostrativa.md` | 198 | "el motor es robusto bajo random walk masivo" (alusión, sin cifra) |
| `01-conclusion-demostrativa.md` | 246 | "hostile testing aplicado al motor (0/1500 falsos positivos en gate completo bajo random walk masivo)" |
| `01-conclusion-demostrativa.md` | 253 | "Robustez del gate completo: 0/1500 falsos positivos bajo random walk masivo." |
| `02-guia-de-defensa.md` | 136 | "Bajo random walk masivo (1500 ejecuciones), 0% supera el umbral strong …" |
| `04-versiones-cortas-defensa.md` | 25 | "Hostile testing severo: 0/1500 falsos positivos del gate completo bajo random walk masivo." |
| `04-versiones-cortas-defensa.md` | 60 | idem (resumen 90s) |
| `04-versiones-cortas-defensa.md` | 114 | idem (resumen 5min) |
| `05-respuestas-tipo-defensa.md` | 61 | "Bajo random walk masivo (1500 ejecuciones), 0% supera el umbral strong (EDI ≥ 0.30) y sólo 0.6% supera weak." |

**≥ 9 menciones explícitas** en `06-cierre/` (≥ 7 con la cifra `0/1500` exacta). El hallazgo del adversarial-reviewer es correcto: la cifra opera como **totem retórico**, no como evidencia argumentada.

### Dos problemas estadístico-metodológicos no declarados

1. **Intervalo de confianza ausente.** `0/1500` no es "cero falsos positivos" sino una proporción puntual con incertidumbre.
   - **Wilson 95 % CI** para p̂ = 0, n = 1500: $[0,\; 0.00255]$.
   - El límite superior 0.255 % traslada que la tasa de FP del gate **podría ser hasta ~0.25 %** y los datos no la distinguirían de cero. La afirmación honesta es "FP rate ≤ 0.25 % al 95 %", no "0 FP".

2. **El gate C1-C5 filtra random walk por diseño, no por discriminación inferencial.** C1 exige acoplamiento ODE→ABM con macro-sonda; un random walk puro carece de la estructura que el gate verifica (no hay sonda macro ni ablación contrafáctica significativa). Por construcción, RW masivo no puede pasar el gate. Reportar `0/1500` como evidencia de **discriminación contra rivales** confunde dos cosas:
   - "el gate excluye ruido sin estructura" (verdadero, esperable, cuasi-tautológico),
   - "el gate discrimina entre teorías rivales con estructura" (lo que la tesis necesita; no se demuestra con RW).

   La discriminación real contra rivales se establece por el **AUC-ROC = 0.886 vs ARIMA 0.600** y por los **3/3 controles de falsación rechazados**, no por el bombardeo de RW.

## (b) Propuesta de edición concreta

**Marca:** `needs_human` — reformula una afirmación defensiva. Se propone, no se aplica.

### Edición B-1: reducir a ≤ 2 menciones en `06-cierre/`

Conservar SOLO:

- **Una mención canónica con CI Wilson** en `01-conclusion-demostrativa.md:253` (sección "Robustez del gate"):

  > **Robustez del gate completo:** 0/1500 falsos positivos bajo random walk masivo (Wilson 95 % CI [0, 0.00255]; FP rate ≤ 0.25 %). El gate filtra ruido sin acoplamiento ODE→ABM por construcción (§3.4); el resultado confirma ausencia de fugas en la implementación, no demuestra discriminación contra teorías rivales — esa carga la sostienen AUC-ROC = 0.886 vs ARIMA y 3/3 controles de falsación rechazados.

- **Una mención breve** en el abstract de cierre (`01-conclusion-demostrativa.md:5`) con remisión: "el aparato sobrevivió hostile testing severo (FP rate ≤ 0.25 % bajo RW masivo, ver §3.4)".

**Eliminar** las menciones repetidas en `01-conclusion-demostrativa.md:174, 246`, en `04-versiones-cortas-defensa.md:25, 60, 114`, y reformular `02-guia-de-defensa.md:136` y `05-respuestas-tipo-defensa.md:61` para que apoyen el argumento sin reciclar el numeral. En las versiones cortas (3 min / 90 s / 5 min), reemplazar el totem por la frase única: "FP rate ≤ 0.25 % al 95 %".

### Edición B-2: nota en §3.4 (`01-conclusion-demostrativa.md:123`)

Insertar tras la línea 125, dentro de §3.4 "El éxito de la falsación":

> **Aclaración sobre el alcance del hostile testing con random walk.** El test masivo de RW (1500 ejecuciones, 0 falsos positivos, Wilson 95 % CI [0, 0.00255]) verifica que el gate C1-C5 **excluye por construcción** trayectorias sin acoplamiento ODE→ABM ni sonda macro: un RW carece de la estructura formal que C1 (ablación contrafáctica con sonda calibrada) exige, por lo que su rechazo es esperable y no constituye, por sí mismo, evidencia de discriminación contra teorías rivales con estructura comparable. La discriminación inferencial se sostiene en otros dos resultados: **3/3 controles de falsación rechazados** (sondas estructuradas pero falsas) y **AUC-ROC = 0.886 vs ARIMA 0.600** sobre arrays primarios. El RW masivo certifica integridad de la implementación (ausencia de fugas hacia "todo pasa"); los otros dos certifican capacidad discriminativa.

### Edición B-3: ajuste paralelo en `04-versiones-cortas-defensa.md`

En las tres versiones (resumen 30 s, 90 s, 5 min), reemplazar la línea con `0/1500` por una sola variante:

> Hostile testing: FP rate ≤ 0.25 % al 95 % bajo RW masivo (filtra ruido sin estructura por construcción); discriminación contra rivales sostenida por 3/3 controles falsados y AUC-ROC = 0.886 vs ARIMA.

## (c) Costo argumentativo declarado

Reformular debilita la versión "fuerte" del cierre en dos sentidos honestos:

1. **Pérdida retórica:** la cifra "0/1500" tenía fuerza por su rotundidad cero. Sustituirla por "≤ 0.25 % al 95 %" es estadísticamente correcto pero menos vendible en defensa oral.
2. **Concesión sustantiva:** se reconoce que el bombardeo de RW **no demuestra discriminación contra rivales**, sólo integridad del gate. La carga de la discriminación se traslada explícitamente a AUC-ROC y a los 3 controles de falsación, ambos ya en el manuscrito pero menos repetidos. Si esos dos resultados se debilitaran en una crítica futura, el RW masivo ya no actuará de respaldo.

**Beneficio:** la tesis pasa de afirmar "el aparato discrimina porque RW no pasa" (vulnerable a la objeción "RW no podía pasar por construcción") a afirmar "el aparato discrimina porque rivales estructurados no pasan, y además su implementación no tiene fugas" (defendible bajo crítica adversarial). Ganancia neta en defensibilidad bajo CLAUDE.md §2.

## Acción requerida

- **`needs_human` para Jacob:** firmar las ediciones B-1, B-2, B-3 (afectan abstract, conclusión, §3.4, guía de defensa y versiones cortas — todas piezas de defensa oral).
- **Tarea técnica derivada (post-firma):** aplicar ediciones, regenerar `TesisFinal/Tesis.md` con `python3 TesisFinal/build.py`, registrar en bitácora del día.
- **No tocar** `metrics.json` ni `TesisFinal/Tesis.md` directamente (CLAUDE.md §4 + harness hooks).

---

**Verificación de aceptación pendiente de firma:**
- [ ] ≤ 2 menciones en `06-cierre/` ← tras B-1
- [ ] Al menos una con Wilson 95 % CI [0, 0.0025] ← B-1 mención canónica
- [ ] Nota §3.4 sobre C1-C5 filtrando RW por diseño ← B-2
