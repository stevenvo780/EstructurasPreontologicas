# Pre-registro EDI B-T2.1 (segunda corrida genuina) — `24_caso_microplasticos`

> **B-T2.1**: pre-registro pre-ejecución sobre datos REFRESCADOS, firmado ANTES de la corrida. Resuelve la objeción del adversarial iter 11 ("los B-T2 son lock-in post-hoc": el pre-registro fue escrito después de ver al menos una corrida real). Esta segunda corrida usa una **ventana temporal restringida** y una **descarga de OWID refrescada hoy**, garantizando que el aparato no ha visto estos datos exactos en la configuración aquí declarada.
>
> **Declaración firme:** los datos a usar (OWID `plastic-waste-mismanaged-by-country` descargado el `YYYY-MM-DD` después de firmar este documento, restringidos a 2000-2022) **no han sido vistos por el aparato bajo este `case_config_b_t2_1.json`**. La corrida B-T2 previa (1980-2020) queda como evidencia de partida, no como contaminación de esta segunda corrida.

## 1. Header

- **Caso:** `24_caso_microplasticos`
- **Fecha de pre-registro:** `2026-05-17`
- **Pre-registrador:** Steven Vallejo (técnica) bajo dirección de Jacob Agudelo (autor)
- **Commit del repo en el momento del registro:** `4a43a472c2b7167c6fe363e5a36fee5f7112b3b6` (HEAD pre-firma; el commit que incluya este archivo será el sello temporal verificable)
- **Asistencia IA:** Claude Opus 4.7 (1M context) bajo dirección humana

## 2. Hipótesis y predicciones (honestas, basadas en iter 13 post-fix)

Estado conocido B-T2 (ventana 1980-2020, fuente Jambeck+OWID original):

- `EDI_real = 0.8057` (CI95% [0.701, 0.880])
- `p_perm = 0.000`, `permutation_method = iid`
- `trend_bias.detrended_edi = 0.332` (≈41% del EDI sobrevive detrending)
- `trend_bias.trend_ratio = 0.412`, `trend_r2 = 0.978`
- Categoría: **strong (Nivel 4)** robusto (único strong del corpus que sobrevive detrending claramente)

**Predicciones para B-T2.1 (ventana 2000-2022, descarga OWID refrescada):**

- **H0 (clasificación predicha):** `Strong` con probabilidad alta, posibilidad real de degradar a `Weak` por ventana corta.
- **Predicción puntual:** `EDI_real ∈ [0.55, 0.85]`. Reducción esperada respecto a B-T2: la ventana 2000-2022 tiene 23 puntos vs 41; menos grados de libertad para detectar el acoplamiento.
- **Predicción de detrended EDI:** `detrended_edi ∈ [0.20, 0.40]`. Si cae a `< 0.10` el resultado se reclasifica como **trend-dominated** y degradamos taxonomía pública a `weak con dominancia de tendencia`.
- **Predicción de p-valor:** `p_perm < 0.05` esperado; si `p ≥ 0.10` se reclasifica como `null` y se documenta como **contraevidencia frente al B-T2 original**.
- **Margen aceptable de variación:** `|ΔEDI_B-T2.1 − EDI_B-T2| ≤ 0.20` (margen amplio justificado por reducción de ventana y posible refresco de cifras OWID).
- **Justificación física (≤3 líneas):** la acumulación oceánica de microplásticos es un proceso de stock con vida media larga (décadas), independiente de la ventana específica de observación. Si el acoplamiento residuos→stock es genuino, debe sobrevivir el truncamiento. Si depende críticamente de los 20 años anteriores, el strong no era robusto.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `accumulation_decay` (idéntica a `common/ode_models.py`; **no se cambia** entre B-T2 y B-T2.1)
- **ODE key / series key:** `mp` / `mp`
- **Drivers:** `["mismanaged_waste", "river_discharge"]` (idénticos)
- **Hiperparámetros (canónicos):**
  - `n_perm = 999`
  - `n_boot = 500`
  - `seed = 42`
  - **`permutation_method = block`** (cambio respecto a `iid` original; bloque = 3 años para preservar autocorrelación; declaración explícita: este cambio es para hacer el test MÁS conservador, no menos)
- **Umbrales de clasificación (canónicos, no negociables):**
  - Strong: `EDI ≥ 0.33` y `p < 0.05`
  - Weak: `0.10 ≤ EDI < 0.33` y `p < 0.05`
  - Trend: `0.05 ≤ EDI < 0.10` o `0.05 ≤ p < 0.10`
  - Null: `EDI < 0.05` o `p ≥ 0.10` y CI cruza cero
  - Falsificación local: `EDI < 0` con CI excluyendo cero por la izquierda
- **Criterio adicional B-T2.1:** clasificación final usa **`detrended_edi`** como prueba dura. Si `detrended_edi < 0.10`, se degrada a `trend-dominated` independientemente del EDI bruto.
- **Variable de observación:** stock anual estimado de microplásticos oceánicos (Mt) — agregación global
- **Ventana temporal NUEVA:** `2000-01-01` a `2022-12-31` (vs 1980-2020 en B-T2)
- **Split train/test:** `2014-01-01` (14 años entrenamiento, 9 años validación)
- **Tratamiento de datos faltantes:** interpolación lineal (declarado uno solo)
- **Agregación temporal:** anual (`YS`)

## 4. Fuente de datos NUEVA (no usada en B-T2)

- **URL exacta primaria:** `https://ourworldindata.org/grapher/plastic-waste-mismanaged.csv?v=1&csvType=full&useColumnShortNames=true`
- **URL secundaria (driver `river_discharge`):** `https://ourworldindata.org/grapher/plastic-waste-emitted-to-ocean.csv?v=1&csvType=full&useColumnShortNames=true`
- **Indicador específico:** `Mismanaged plastic waste (tonnes per year)` agregado global; `Plastic waste emitted to the ocean (tonnes)`
- **Países / región:** agregación global (`OWID_WRL`)
- **Fecha de descarga prevista:** `2026-05-18` (posterior a este pre-registro)
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; commit posterior añadirá hash a este mismo archivo, sección 4>`
- **Diferencia clave vs B-T2:** B-T2 usó snapshot Jambeck 2015 + OWID local cacheado 2026-04-28. B-T2.1 fuerza re-descarga viva de OWID el 2026-05-18 con ventana restringida.

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/24_caso_microplasticos/src/validate.py --seed 42 --config case_config_b_t2_1.json`:

| Resultado observado (EDI bruto / detrended / p) | Clasificación | Acción |
|---|---|---|
| `EDI ≥ 0.33`, `detrended ≥ 0.10`, `p < 0.05` | **Strong robusto confirmado** | Reportar como confirmación independiente; B-T2.1 corrobora B-T2 |
| `EDI ≥ 0.33`, `detrended < 0.10`, `p < 0.05` | **Strong trend-dominated** | Reclasificar caso 24 a `weak/trend-dominated`; el strong original era artefacto de tendencia compartida |
| `0.10 ≤ EDI < 0.33`, `p < 0.05` | **Weak** | Degradar taxonomía pública; B-T2.1 contradice B-T2 → declarar como contraevidencia |
| `EDI < 0.10` o `p ≥ 0.10` | **Null/Trend** | Caso 24 pierde estatus de strong único; rehacer narrativa de "único strong robusto" en `Evaluacion_Modelos_Dominio.md` |
| `EDI < 0` con CI excluyendo cero | **Falsificación local** | Documentar como contraevidencia dura; revisar sonda `accumulation_decay` |

## 6. Compromiso de no-modificación

Entre la firma de este pre-registro y la ejecución no se modifica:

- `case_config_b_t2_1.json` (a crear como copia de `case_config.json` con ventana y `permutation_method` actualizados)
- `src/data.py`, `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3
- Umbrales declarados en §3

Si tras ver el resultado se considera necesario ajustar algún parámetro, se reporta como **análisis exploratorio post-hoc, NO confirmatorio**, y se firma B-T2.2 con tercera descarga.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `____-__-__`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `____-__-__`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context), 2026-05-17

---

**Sello temporal:** el commit que añada este archivo al repo es la prueba pública de que el pre-registro existió antes que los datos. Verificable con `git log --diff-filter=A -- 09-simulaciones-edi/24_caso_microplasticos/docs/PRE_REGISTRO_B_T2_1.md`.
