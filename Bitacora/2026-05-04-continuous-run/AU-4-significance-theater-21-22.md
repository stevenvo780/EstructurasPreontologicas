# AU-4 — Significance theater en casos 21 (Salinización) y 22 (Fósforo)

**Fecha:** 2026-05-04
**Origen:** Hallazgo de `adversarial-reviewer` 2026-05-05.
**Modo:** Auditoría read-only sobre `metrics.json` + lectura de capítulos.
**Status:** `needs_human` — reclasificación y citación canónica requieren firma de Jacob.

---

## 1. Verificación de la afirmación

### 1.1 Fuente de verdad numérica (real phase)

**Caso 21 Salinización** (`09-simulaciones-edi/21_caso_salinizacion/outputs/metrics.json`):

| Magnitud | Valor |
|---|---:|
| EDI (1 − rmse_abm/rmse_abm_no_ode) | **0.0184** |
| p_perm | 0.0028 |
| Bootstrap mean EDI | 0.0142 |
| **CI 95 %** | **[−0.0771, +0.0825]** |

**Caso 22 Fósforo** (`09-simulaciones-edi/22_caso_fosforo/outputs/metrics.json`):

| Magnitud | Valor |
|---|---:|
| EDI | **0.1924** |
| p_perm | 0.0000 |
| Bootstrap mean EDI | 0.1989 |
| **CI 95 %** | **[−0.2214, +0.5502]** |

### 1.2 Lo que el manuscrito declara hoy

- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:109` reporta caso 22 en bloque "Weak (Nivel 3)" con `EDI=0.1924, p=0.0000` — **sin CI**.
- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:125` reporta caso 21 en bloque "Suggestive (Nivel 2)" con `EDI=0.0184, p=0.0028` — **sin CI**.
- `06-cierre/04-versiones-cortas-defensa.md:110` lista Fósforo como "weak" y Salinización como "suggestive", sin advertir que en ambos el bootstrap CI cruza cero.

### 1.3 Diagnóstico

La afirmación del adversarial es **correcta y reproducible**:

1. **Caso 21**: EDI puntual de 1.8 % indica reducción de RMSE prácticamente nula. El p_perm=0.0028 sólo certifica que la diferencia 0.32828 vs 0.33444 no es atribuible al orden temporal aleatorio — pero la diferencia *es* trivial (≈0.6 % de RMSE). El CI bootstrap [−0.077, +0.083] **incluye el cero y se extiende a magnitudes opuestas**: la estimación de EDI es estadísticamente compatible con que el acoplamiento ODE→ABM *empeore* la predicción. Significance theater clásico (p significativo + magnitud trivial + CI cruza cero).
2. **Caso 22**: EDI puntual 0.1924 con p_perm=0.0 parece sólido, pero el CI bootstrap [−0.221, +0.550] cruza cero y abarca casi 0.8 unidades de EDI. Discrepancia severa entre permutación y bootstrap → la estimación es *frágil*: el ranking del estadístico observado bajo permutación es alto, pero su magnitud no es estable bajo re-muestreo. **No es defensible declararlo "weak" sin advertir esta inconsistencia**.

---

## 2. Propuesta de edición concreta (necesita firma humana)

### 2.1 Tablas resumen — añadir columna CI 95 %

`05-aplicaciones/07-mapa-aplicaciones-corpus.md` Tablas 5.7.5 y 5.7.6, y la tabla agregada en `06-cierre/01-conclusion-demostrativa.md`:

| # | Caso | EDI | CI 95 % | p_perm | Comentario |
|---|------|----:|:-------:|------:|------------|
| 22 | Fósforo | 0.1924 | **[−0.221, +0.550]** | 0.0000 | CI cruza cero — magnitud frágil |
| 21 | Salinización | 0.0184 | **[−0.077, +0.083]** | 0.0028 | Significance theater (p<0.01 con magnitud trivial) |

### 2.2 Reclasificación honesta

- **Caso 21 (Salinización):** mover de "Suggestive (Nivel 2)" a **"Trend / null por magnitud"** o a un bloque nuevo *"Significativos pero magnitud trivial — no contabilizan a favor de la tesis"*. La existencia de un p<0.01 no rescata un EDI de 1.8 % cuyo CI cruza cero.
- **Caso 22 (Fósforo):** mantener en "Weak" **solo si** se acompaña explícitamente del CI [−0.22, +0.55] con la nota "p_perm=0.0 pero CI bootstrap incluye cero — ranking robusto, magnitud no". Alternativa más estricta: degradar a "Suggestive" hasta resolver la discrepancia perm/bootstrap.

### 2.3 Sumarios agregados que cambian si se reclasifica

Si Caso 21 sale de "suggestive" y Caso 22 baja de "weak":
- `06-cierre/04-versiones-cortas-defensa.md:110` actual: "8 weak: …, Fósforo, …" + "2 suggestive: Finanzas, Salinización" → cambia conteo.
- Recalcular el "balance honesto" del corpus inter-dominio.

### 2.4 Cita canónica en `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md`

Añadir, en la sección que justifica el uso conjunto de p_perm y CI bootstrap, cita textual:

> Wasserstein, R. L., & Lazar, N. A. (2016). The ASA's Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, 70(2), 129-133.
>
> "Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold." (p. 131, Principle 3)

Y en consecuencia: **el corpus reportará EDI con CI 95 % siempre, y la admisión a Niveles 2-4 exige no solo p<0.05 sino CI 95 % que no cruce cero** (o declaración explícita cuando lo cruza).

> ⚠️ Esta cita debe verificarse contra el PDF original antes de fijarla. El PDF debe estar en `07-bibliografia/`. Si no está, marcar B-T como "fetch + verificar paginación" antes de incluirla.

---

## 3. Costo argumentativo declarado

1. **El corpus pierde fuerza cuantitativa**: si se reclasifica caso 21 fuera de "suggestive" y se añade nota crítica al 22, el conteo "8 weak + 2 suggestive" baja, y el balance "casos a favor / casos en contra" empeora ligeramente. Esto es lo correcto: **declarar la deuda es virtud (CLAUDE.md §7); ocultarla es fraude**.
2. **La regla de admisión se vuelve más estricta retroactivamente**: aplicar el criterio "CI 95 % no cruza cero" puede afectar a otros casos del corpus que hoy figuran como significativos (ver §4).
3. **Confirma una crítica adversarial seria**: la sola existencia del par {p<0.01, CI cruza 0} en dos casos contabilizados a favor de la tesis muestra que el aparato actual no filtra significance theater. Esto **debe declararse en la "Deuda residual" del capítulo 03 o 06**.
4. **Contribución positiva**: incorporar Wasserstein-Lazar 2016 alinea explícitamente la metodología con la guía oficial de la ASA y blinda contra una crítica obvia en defensa.

---

## 4. Trabajo derivado (sugerido a Jacob)

- **B-T (técnica):** auditar los 40 casos del corpus extrayendo `bootstrap_ci` de cada `metrics.json` y producir tabla "EDI · p · CI" completa. Identificar todos los casos con CI cruzando cero pese a p<0.05.
- **B-T (técnica):** investigar la discrepancia perm/bootstrap del caso 22. Posibles causas: (a) baja n efectiva por unidad temporal, (b) heteroscedasticidad en residuos, (c) sensibilidad del estadístico a outliers. Si la inestabilidad es estructural del caso, el caso debe degradarse.
- **H-J (filosófica):** decisión de Jacob sobre la regla nueva: ¿"CI 95 % no cruza cero" se vuelve criterio duro de admisión a Niveles ≥ 2, o queda como condición de robustez separada?
- **B-T (bibliográfica):** verificar disponibilidad de Wasserstein & Lazar 2016 en `07-bibliografia/`. Si ausente, fetch.

---

## 5. Acciones NO realizadas (intencionalmente)

- No se editaron `Tesis.md` ni `metrics.json` (CLAUDE.md §4, hooks del harness).
- No se editaron las tablas en `05-aplicaciones/07` ni `06-cierre/01`/`04`: la reclasificación tiene consecuencias narrativas sobre el "balance honesto" del corpus que requieren la voz autoral de Jacob (CLAUDE.md §3).
- No se introdujo la cita Wasserstein-Lazar sin verificación previa de paginación contra PDF (CLAUDE.md §5).

---

## 6. Resultado

**Verificación:** la afirmación del adversarial se sostiene. Caso 21 es significance theater inequívoco; Caso 22 es magnitud frágil con discrepancia perm/bootstrap.
**Edición:** `needs_human` — Jacob decide la reclasificación y la regla nueva.
**Numérico:** los CI [−0.077, +0.083] (caso 21) y [−0.221, +0.550] (caso 22) están en `metrics.json` y son trazables a `phases.real.edi.ci_lo / ci_hi`.
