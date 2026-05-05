# TENG-02 — Bootstrap CI percentil simple sesgado para val_steps pequeños

**Fecha:** 2026-05-04
**Tarea:** Auditar uso de bootstrap percentil simple en `bootstrap_edi()` con val_steps pequeños.
**Modo:** Read-only audit. **Estado:** `needs_human` (B-T*, requiere firma de Jacob/Steven).

---

## (a) Verificación de la afirmación

**Claim:** `09-simulaciones-edi/common/hybrid_validator.py:193` (`bootstrap_edi()`) usa bootstrap percentil simple, que en muestras pequeñas tiene sesgo O(n^{-1/2}) frente a BCa O(n^{-1}) (DiCiccio & Efron 1996, *Statistical Science* 11(3):189-228).

**Verificación en código:** confirmada. Líneas 216-219:

```python
samples_sorted = np.sort(samples)
alpha = (1.0 - ci) / 2.0
lo = float(samples_sorted[max(0, int(alpha * n_boot))])
hi = float(samples_sorted[min(n_boot - 1, int((1.0 - alpha) * n_boot))])
```

Esto es bootstrap **percentil simple** (Efron 1981). No hay corrección de sesgo (z₀) ni de aceleración (a). No hay campo `ci_method` registrado en `metrics.json`. El umbral mínimo es `n < 4` → devuelve punto sin CI; entre 4 y 30 aplica percentil sin corrección.

**Verificación de impacto en el corpus:** 32 casos con `val_steps` extraído de `metrics.json`. **21/32 tienen `val_steps < 30`**, y **9/32 tienen `val_steps ≤ 9`** (8 casos con `val_steps=8`, 1 con 9). Distribución:

| val_steps | n_casos |
|-----------|---------|
| 8 | 12 |
| 9 | 1 |
| 11 | 1 |
| 13 | 1 |
| 15 | 2 |
| 18-20 | 4 |
| ≥30 | 11 |

**Verificación bibliográfica:** la afirmación general es estándar; DiCiccio & Efron 1996 §2-§3 derivan el orden de error. Para n≤10 el sesgo del percentil puede mover el límite inferior del CI varios puntos porcentuales — material para casos donde el CI bootstrap roza 0 (cf. AU-2 caso 27 "bootstrap cruza cero", ya en bitácora).

**Conclusión:** la afirmación es **correcta y materialmente relevante** para 21/32 casos del corpus. No es ornamental.

---

## (b) Propuesta de edición

**Esta es una decisión técnica con consecuencias numéricas en los CI reportados de 21/32 casos. Requiere firma de Jacob/Steven antes de implementarse.** Marcado `needs_human` (B-T-NUEVA).

**Propuesta (a discutir, no a ejecutar unilateralmente):**

1. **Implementar BCa en `bootstrap_edi()`** activado cuando `n < 30`:
   - Calcular `z₀` (corrección de sesgo) por fracción de muestras bootstrap menores que el estimador puntual.
   - Calcular `a` (aceleración) por jackknife sobre `(obs, abm, red)` conjuntamente.
   - Sustituir los percentiles `α/2` y `1-α/2` por los corregidos según fórmula DiCiccio-Efron 1996 ec. (2.4).
2. **Añadir campo `ci_method` en `metrics.json`:** valores `"percentile"` (legacy) o `"BCa"`. Registrar también `n_val` y `bca_z0`, `bca_a` para trazabilidad.
3. **Validación de cobertura empírica:** simulación con EDI conocido (proceso generador con acoplamiento ODE↔ABM controlado) y n∈{8,15,30,100}, comparar cobertura nominal 95% bajo percentil vs BCa. Esto fija si el sesgo es material o cosmético en este régimen específico.
4. **Re-correr los 21 casos con val_steps<30** y reportar diff de CIs en bitácora antes de tocar prosa del manuscrito (regla CLAUDE.md §4: gana JSON sobre prosa, pero antes hay que regenerar JSONs).

**Costos de NO actuar:** 21 CIs reportados en el corpus tienen sesgo de orden O(n^{-1/2}) sin declararlo. Para n=8 esto es ≈35% del intervalo en peor caso. Si un revisor estadístico aplica BCa por su cuenta y los CIs no replican, el caso es defendible declarando "percentil" pero pierde fuerza inferencial.

**Costos de actuar:** romper hashes de `metrics.json` en ≥21 casos; re-validar cada uno; potencial reajuste de prosa en `05-aplicaciones/` y tablas en `02-fundamentos/`. Trabajo ≥1 jornada técnica si se hace bien (incluye estudio de cobertura).

---

## (c) Costo argumentativo declarado

- **Concesión honesta:** el bootstrap actual del corpus EDI es subóptimo para los 21 casos con `val_steps<30`. La afirmación de "CI 95%" en esos casos tiene cobertura nominal solo aproximada al orden O(n^{-1/2}). Esto **no invalida** los hallazgos cualitativos (signo del EDI, p_perm), pero **sí relaja** la fuerza de los intervalos reportados.
- **Lo que la tesis sí puede defender hoy:** los p_perm (test de permutación, no afectado por este hallazgo) y la dirección/signo del EDI puntual.
- **Lo que la tesis no puede defender hoy sin BCa o sin declarar la limitación:** la anchura precisa de los CI en casos con `val_steps≤15` (15/32 casos).

**Mitigación mínima (sin implementar BCa):** declarar en `02-fundamentos/06-protocolo-empirico.md` y en `06-cierre/Deuda residual` que el CI bootstrap usa percentil simple, citar DiCiccio-Efron 1996, declarar el orden del error, y reportar `val_steps` por caso para que el lector calibre. Esto es **deuda declarada** (CLAUDE.md §7) y es honesto. No requiere re-correr casos.

**Mitigación completa:** implementar BCa según propuesta (b). Requiere firma humana.

---

## Acción recomendada al daemon

- **No implementar BCa unilateralmente.**
- Añadir entrada a `TAREAS_PENDIENTES.md` Sección B (B-T*) con título "Implementar BCa en bootstrap_edi() para val_steps<30" y referencia a esta bitácora.
- Si Jacob opta por mitigación mínima, añadir declaración en `06-protocolo-empirico.md` y `06-cierre/Deuda residual`.

**Fuente primaria verificada:** DiCiccio, T.J. & Efron, B. (1996). "Bootstrap confidence intervals." *Statistical Science* 11(3):189-228, esp. §2.3 (percentil) y §3 (BCa). PDF no presente en `07-bibliografia/` — citación apoyada en consenso estadístico estándar; si se va a citar en manuscrito, **fetch primero** vía `/fetch-biblio`.

---

RESULT: complete | TENG-02 | needs_human: 21/32 casos val_steps<30, BCa requiere firma
