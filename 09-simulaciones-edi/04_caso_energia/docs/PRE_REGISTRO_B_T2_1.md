# Pre-registro EDI B-T2.1 (segunda corrida genuina) — `04_caso_energia`

> **B-T2.1**: pre-registro pre-ejecución sobre datos REFRESCADOS, firmado ANTES de la corrida. Resuelve la objeción del adversarial iter 11. Esta segunda corrida sustituye la fuente actual (`World Bank fallback`, marcado como limitación en `FETCH_MANIFEST.json`) por **OWID Renewables específicos** (share renovable global) y restringe ventana.
>
> **Declaración firme:** los datos a usar (OWID `share-electricity-renewables.csv` + `energy-consumption-by-source.csv`, descargados el `2026-05-18` después de firmar este documento) **no han sido vistos por el aparato bajo este `case_config_b_t2_1.json`**. La corrida B-T2 previa (1990-2023, dataset proxy World Bank) queda como evidencia de partida pero está marcada como `limitation` en el manifest original.

## 1. Header

- **Caso:** `04_caso_energia`
- **Fecha de pre-registro:** `2026-05-17`
- **Pre-registrador:** Steven Vallejo (técnica) bajo dirección de Jacob Agudelo (autor)
- **Commit del repo en el momento del registro:** `4a43a472c2b7167c6fe363e5a36fee5f7112b3b6`
- **Asistencia IA:** Claude Opus 4.7 (1M context) bajo dirección humana

## 2. Hipótesis y predicciones (honestas, basadas en iter 13 post-fix)

Estado conocido B-T2 (ventana 1990-2023, dataset proxy):

- `EDI_real = 0.4615` (CI95% [0.378, 0.550])
- `p_perm = 0.000`, `permutation_method = iid`
- `trend_bias.detrended_edi = 0.0036` (**colapso casi total: ~0.8% del EDI sobrevive detrending**)
- `trend_bias.trend_ratio = 0.008`, `trend_r2 = 0.912`
- Categoría: **strong (Nivel 4)** PERO con warning de trend-bias severo
- `FETCH_MANIFEST` declara: `"limitation": "API World Bank/OWID no disponibles en ejecución. Dataset generado con patrones reales"` → **el strong actual puede ser artefacto del proxy + tendencia compartida**

**Predicciones para B-T2.1 (ventana 1995-2022, OWID renovables específico):**

- **H0 (clasificación predicha):** `Weak` o `Trend`. La predicción honesta es que el strong B-T2 **NO sobrevivirá** una vez (a) usemos datos OWID genuinos en vez del proxy, y (b) apliquemos detrending implícito al elegir un indicador estacionario (share renovable).
- **Predicción puntual EDI bruto:** `EDI_real ∈ [0.05, 0.30]`. Predicción puntual modal: `0.15`.
- **Predicción puntual detrended EDI:** `detrended_edi ∈ [0.00, 0.10]`. Si supera `0.15` sería evidencia positiva fuerte.
- **Predicción de p-valor:** `p_perm` cualquier valor; sin filtro previo. Si `p ≥ 0.10`, **null genuino**.
- **Margen aceptable de variación:** `|ΔEDI_B-T2.1 − EDI_B-T2| ≤ 0.30` (margen amplio justificado por cambio de fuente y de indicador).
- **Justificación física (≤3 líneas):** el consumo energético per cápita y los drivers (GDP, urbanización, industria) co-crecen monotónicamente desde 1990. La correlación es real pero no implica acoplamiento causal en el sentido EDI. Al re-correr con share renovable (estacionario por construcción: porcentaje acotado 0-100), si el acoplamiento es genuino debe persistir; si es solo co-tendencia, desaparecerá.

**Predicción de honestidad:** este caso es el principal candidato a **degradar de strong a weak/null** tras B-T2.1. Aceptamos ese resultado por adelantado como deuda saldada.

## 3. Especificación analítica pre-registrada (no modificable post-hoc)

- **Sonda ODE:** `mean_reversion` (idéntica a `common/ode_models.py`; **no se cambia** entre B-T2 y B-T2.1)
- **ODE key / series key:** `e` / `e`
- **Drivers NUEVOS:** `["renewables_share", "fossil_share", "gdp_pc"]` (vs `["gdp_growth", "urban_pct", "industry_pct"]` en B-T2; cambio justificado por usar OWID Renewables como fuente primaria)
- **Hiperparámetros (canónicos):**
  - `n_perm = 999`
  - `n_boot = 500`
  - `seed = 42`
  - **`permutation_method = block`** (bloque = 3 años; conservador frente a autocorrelación)
- **Umbrales de clasificación (canónicos, no negociables):** Strong ≥0.33+p<0.05; Weak 0.10-0.33+p<0.05; Trend 0.05-0.10 o p 0.05-0.10; Null EDI<0.05 o p≥0.10; Falsificación EDI<0 con CI excluyendo cero.
- **Criterio adicional B-T2.1:** clasificación final usa **`detrended_edi`** como prueba dura. Si `detrended_edi < 0.10`, se degrada a `trend-dominated` independientemente del EDI bruto. Dado el colapso 0.46→0.0036 en B-T2, este criterio es el central para este caso.
- **Variable de observación:** consumo energético per cápita (kWh/persona/año), agregación global
- **Ventana temporal NUEVA:** `1995-01-01` a `2022-12-31` (vs 1990-2023 en B-T2; recorte de 5 años iniciales evita el período de transición post-URSS de calidad de dato cuestionable)
- **Split train/test:** `2012-01-01` (17 años entrenamiento, 11 años validación)
- **Tratamiento de datos faltantes:** interpolación lineal
- **Agregación temporal:** anual (`YS`)

## 4. Fuente de datos NUEVA (no usada en B-T2)

- **URL exacta primaria (observable):** `https://ourworldindata.org/grapher/per-capita-energy-use.csv?v=1&csvType=full&useColumnShortNames=true` agregado `OWID_WRL`
- **URL drivers:**
  - Renewables share: `https://ourworldindata.org/grapher/share-electricity-renewables.csv?v=1&csvType=full&useColumnShortNames=true`
  - Fossil share: `https://ourworldindata.org/grapher/share-electricity-fossil-fuels.csv?v=1&csvType=full&useColumnShortNames=true`
  - GDP per cápita (PPP, USD constantes): `https://ourworldindata.org/grapher/gdp-per-capita-worldbank.csv?v=1&csvType=full&useColumnShortNames=true`
- **Indicador específico:** `primary_energy_consumption__kwh_per_capita__per_year` (OWID short name)
- **Países / región:** agregación global (`OWID_WRL`)
- **Fecha de descarga prevista:** `2026-05-18`
- **Hash esperado del CSV post-descarga (sha256):** `<a calcular tras descarga; commit posterior añadirá hash>`
- **Diferencia clave vs B-T2:** B-T2 usó dataset proxy generado localmente (declarado como `limitation` en FETCH_MANIFEST). B-T2.1 fuerza descarga viva de OWID con drivers cualitativamente distintos (mix energético en vez de demografía).

## 5. Criterio de cierre

Tras ejecutar `python3 09-simulaciones-edi/04_caso_energia/src/validate.py --seed 42 --config case_config_b_t2_1.json`:

| Resultado observado (EDI bruto / detrended / p) | Clasificación | Acción |
|---|---|---|
| `EDI ≥ 0.33`, `detrended ≥ 0.10`, `p < 0.05` | **Strong robusto sorprendente** | Re-evaluar: si datos OWID nuevos preservan strong, es evidencia más fuerte que B-T2 |
| `EDI ≥ 0.33`, `detrended < 0.10`, `p < 0.05` | **Strong trend-dominated (esperado)** | Reclasificar caso 04 a `weak/trend-dominated`; confirmar lectura de B-T2 |
| `0.10 ≤ EDI < 0.33`, `p < 0.05` | **Weak (predicción modal)** | Degradar caso 04 de `strong` a `weak`; actualizar `Evaluacion_Modelos_Dominio.md` |
| `EDI < 0.10` o `p ≥ 0.10` | **Null/Trend** | Caso 04 pierde estatus de strong; mover a sección `falsificaciones honestas` |
| `EDI < 0` con CI excluyendo cero | **Falsificación local** | Documentar como contraevidencia dura |

## 6. Compromiso de no-modificación

Entre la firma y la ejecución no se modifica:

- `case_config_b_t2_1.json` (a crear como copia de `case_config.json` con drivers, ventana y `permutation_method` actualizados según §3)
- `src/data.py`, `src/ode.py`, `src/abm.py`
- Hiperparámetros declarados en §3
- Umbrales declarados en §3

Si tras ver el resultado se considera necesario ajustar algún parámetro, se reporta como **análisis exploratorio post-hoc, NO confirmatorio**, y se firma B-T2.2 con tercera descarga.

## 7. Firma

- **Autor (Jacob Agudelo):** ___________________  Fecha: `____-__-__`
- **Co-firma técnica (Steven Vallejo):** ___________________  Fecha: `____-__-__`
- **Asistencia IA bajo dirección humana** (declarativo, no firmante): Claude Opus 4.7 (1M context), 2026-05-17

---

**Sello temporal:** el commit que añada este archivo al repo es la prueba pública de que el pre-registro existió antes que los datos. Verificable con `git log --diff-filter=A -- 09-simulaciones-edi/04_caso_energia/docs/PRE_REGISTRO_B_T2_1.md`.
