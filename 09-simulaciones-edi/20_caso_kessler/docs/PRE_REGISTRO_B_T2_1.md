# Pre-registro EDI B-T2.1 (segunda corrida genuina) — `20_caso_kessler`

> **B-T2.1**: pre-registro pre-ejecución sobre datos REFRESCADOS, firmado ANTES de la corrida. Resuelve la objeción del adversarial iter 11. Esta segunda corrida sustituye la fuente actual (`NASA ODPO calibrated` con `Celestrak offline` como limitación) por **catálogo Space-Track CSpOC** descargado vivo + restricción de ventana al periodo con telemetría densa (2000-2024).
>
> **Declaración firme:** los datos a usar (Space-Track `gp` query + ESA DISCOS si disponible, descargados el `2026-05-18` después de firmar este documento) **no han sido vistos por el aparato bajo este `case_config_b_t2_1.json`**. La corrida B-T2 previa (1980-2024, dataset NASA ODPO calibrado) queda como evidencia de partida pero el FETCH_MANIFEST declara `Celestrak live endpoint unavailable during execution`.

## 1. Header

- **Caso:** `20_caso_kessler`
- **Fecha de pre-registro:** `2026-05-17`
- **Pre-registrador:** Steven Vallejo (técnica) bajo dirección de Jacob Agudelo (autor)
- **Commit del repo en el momento del registro:** `4a43a472c2b7167c6fe363e5a36fee5f7112b3b6`
- **Asistencia IA:** Claude Opus 4.7 (1M context) bajo dirección humana

## 2. Hipótesis y predicciones (honestas, basadas en iter 13 post-fix)

Estado conocido B-T2 (ventana 1980-2024, NASA ODPO calibrado):

- `EDI_real = 0.6936` (CI95% [0.662, 0.717])
- `p_perm = 0.000`, `permutation_method = iid`
- `trend_bias.detrended_edi = -1.0` (**catastrófico: detrended completamente negativo**)
- `trend_bias.trend_ratio = -1.442`, `trend_r2 = 1.0` (R² perfecto)
- `effective_information = 0.0` (señal informacional nula tras corrección)
- Categoría: **strong (Nivel 4)** PERO con `trend_r2 = 1.0` y `detrended = -1.0` → **el strong es artefacto puro de tendencia monotónica creciente**

**Predicciones para B-T2.1 (ventana 2000-2024, Space-Track vivo):**

- **H0 (clasificación predicha):** `Null` o `Trend`. La predicción honesta es que el strong B-T2 **NO sobrevivirá** una vez (a) usemos catálogo Space-Track con resolución mensual real en vez de NASA ODPO interpolado anualmente, y (b) restrinjamos al periodo con telemetría densa post-2000.
- **Predicción puntual EDI bruto:** `EDI_real ∈ [0.00, 0.25]`. Predicción puntual modal: `0.10`.
- **Predicción puntual detrended EDI:** `detrended_edi ∈ [-0.20, 0.10]`. Esperamos que siga negativo o nulo.
- **Predicción de p-valor:** `p_perm ≥ 0.10` probable (resultado null genuino).
- **Margen aceptable de variación:** `|ΔEDI_B-T2.1 − EDI_B-T2| ≤ 0.40` (margen amplio justificado por cambio drástico de fuente y resolución temporal).
- **Justificación física (≤3 líneas):** la población de debris >10cm crece casi-monotónicamente desde 1957 por acumulación física (sin sumidero efectivo en órbitas altas) y por eventos discretos (ASATs, colisiones). La sonda `saturation_growth` ajusta cualquier curva monotónica saturada; el strong observado es geometría de la curva, no acoplamiento Kessler genuino (que requeriría detectar la **realimentación** colisión→fragmento→colisión, no solo el stock).

**Predicción de honestidad:** este caso es el **candidato más fuerte a degradar** del corpus tras B-T2.1. El `trend_r2=1.0` es una señal de alarma textbook. Aceptamos por adelantado que la lectura honesta es: la sonda `saturation_growth` no discrimina cascada Kessler de crecimiento monotónico simple. Sondas alternativas (Kessler-Liou con término colisional cuadrático) deberían intentarse en B-T2.2 como `/multi-probe-null`.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `saturation_growth` (idéntica a `common/ode_models.py`; **no se cambia** entre B-T2 y B-T2.1 para que la comparación sea limpia)
- **ODE key / series key:** `k` / `k`
- **Drivers NUEVOS:** `["launch_rate", "asat_events", "active_satellites"]` (vs `[]` vacío en B-T2; agregamos drivers que la teoría Kessler-Liou requiere)
- **Hiperparámetros (canónicos):**
  - `n_perm = 999`
  - `n_boot = 500`
  - `seed = 42`
  - **`permutation_method = block`** (bloque = 12 meses; conservador frente a autocorrelación temporal alta de un stock cumulativo)
- **Umbrales de clasificación (canónicos, no negociables):** Strong ≥0.33+p<0.05; Weak 0.10-0.33+p<0.05; Trend 0.05-0.10 o p 0.05-0.10; Null EDI<0.05 o p≥0.10; Falsificación EDI<0 con CI excluyendo cero.
- **Criterio adicional B-T2.1 (CENTRAL):** clasificación final usa **`detrended_edi`** como prueba dura. Dado el `detrended=-1.0` en B-T2, **si `detrended_edi < 0.05` se reclasifica como `null` independientemente del EDI bruto**. Este caso no puede sostener el strong sin pasar este filtro.
- **Variable de observación:** número de objetos catalogados >10cm en LEO/MEO/GEO (suma total mensual)
- **Ventana temporal NUEVA:** `2000-01-01` a `2024-12-31` (vs 1980-2024 en B-T2; el recorte elimina el período 1980-2000 que tiene muy baja densidad de catálogo y fue interpolado en NASA ODPO)
- **Split train/test:** `2017-01-01` (17 años entrenamiento, 8 años validación)
- **Tratamiento de datos faltantes:** interpolación lineal
- **Agregación temporal:** mensual (`MS`) — mejora resolución vs anual de B-T2

## 4. Fuente de datos NUEVA (no usada en B-T2)

- **URL primaria:** `https://www.space-track.org/basicspacedata/query/class/gp_history/decay_date/null-val/orderby/EPOCH%20desc/format/csv` (catálogo CSpOC oficial USA Space Force; requiere credenciales registradas)
- **URL alternativa pública (si Space-Track no disponible):** `https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json` + `https://celestrak.org/NORAD/elements/gp.php?GROUP=cosmos-1408-debris&FORMAT=json` + agregaciones por evento
- **URL drivers:**
  - Launch rate anual: `https://planet4589.org/space/gcat/data/derived/launchlog.html` (Jonathan McDowell, JSR Launch Vehicle Database)
  - ASAT events: documentado manualmente desde `https://celestrak.org/events/` (2007 ASAT-Fengyun, 2009 Iridium-Cosmos, 2021 Russian ASAT)
- **Indicador específico:** conteo total de objetos catalogados con `OBJECT_TYPE in {DEBRIS, ROCKET BODY, PAYLOAD}` con `RCS_SIZE >= LARGE` (proxy >10cm), agregado mensualmente
- **Países / región:** órbita terrestre completa (LEO + MEO + GEO)
- **Fecha de descarga prevista:** `2026-05-18`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; commit posterior añadirá hash>`
- **Diferencia clave vs B-T2:** B-T2 usó NASA ODPO con limitación declarada `Celestrak offline` (esencialmente: dataset calibrado por aparato propio sobre estadísticas agregadas de los reportes trimestrales). B-T2.1 fuerza catálogo orbital crudo con resolución mensual real.

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/20_caso_kessler/src/validate.py --seed 42 --config case_config_b_t2_1.json`:

| Resultado observado (EDI bruto / detrended / p) | Clasificación | Acción |
|---|---|---|
| `EDI ≥ 0.33`, `detrended ≥ 0.10`, `p < 0.05` | **Strong robusto sorprendente** | Re-evaluar; si Space-Track vivo preserva strong + detrended positivo, es evidencia inesperada y debe rastrearse a qué cambió |
| `EDI ≥ 0.33`, `detrended < 0.05`, `p < 0.05` | **Strong trend-dominated (esperado)** | Reclasificar caso 20 a `trend-dominated artifact`; confirmar lectura B-T2 |
| `0.10 ≤ EDI < 0.33`, `p < 0.05` | **Weak** | Degradar caso 20 de `strong` a `weak con sospecha de trend` |
| `EDI < 0.10` o `p ≥ 0.10` (**predicción modal**) | **Null/Trend** | Caso 20 pierde estatus de strong; mover a `falsificaciones honestas`; abrir `/multi-probe-null` con sonda Kessler-Liou colisional |
| `EDI < 0` con CI excluyendo cero | **Falsificación local** | Documentar como contraevidencia dura; sonda `saturation_growth` rechazada |

## 6. Compromiso de no-modificación

Entre la firma y la ejecución no se modifica:

- `case_config_b_t2_1.json` (a crear como copia de `case_config.json` con drivers, ventana, frecuencia mensual y `permutation_method` actualizados según §3)
- `src/data.py`, `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3
- Umbrales declarados en §3

Si tras ver el resultado se considera necesario ajustar algún parámetro, se reporta como **análisis exploratorio post-hoc, NO confirmatorio**, y se firma B-T2.2 (con sonda Kessler-Liou colisional) como nueva tercera corrida.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `____-__-__`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `____-__-__`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context), 2026-05-17

---

**Sello temporal:** el commit que añada este archivo al repo es la prueba pública de que el pre-registro existió antes que los datos. Verificable con `git log --diff-filter=A -- 09-simulaciones-edi/20_caso_kessler/docs/PRE_REGISTRO_B_T2_1.md`.
