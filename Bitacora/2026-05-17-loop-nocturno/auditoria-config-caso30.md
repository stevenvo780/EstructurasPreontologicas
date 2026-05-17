# Auditoría — violación pre-registro caso 30 (Behavioral Dynamics)

**Fecha:** 2026-05-17
**Detección:** `verify_preregistration.py` iter 11→12 reportó `config_modified_count=1`
**Verificador:** harness pre-registro
**Severidad:** ALTA — violación explícita del §6 del pre-registro

## Hallazgo

### Commit-sello del pre-registro
`c6b3d3b2bbe21b28c8afc0a3e1c740eca55fc3b0` (2026-05-17 06:56:56)
Documento: `09-simulaciones-edi/30_caso_behavioral_dynamics/docs/PRE_REGISTRO.md`

### Commit violatorio
`e5c85f4` (2026-05-17 09:59:04) — "loop nocturno iter 11"
Δt = 3 horas tras el sello.

### Cambios introducidos (NO autorizados por §6)

1. **`case_config.json`**:
   - `data` → mismo (synthetic)
   - **Nuevo bloque `data_real`**: fuente `Google Mobility proxy (COVID-19 2020-2021)`, LoE=1.5
   - `dates.real_*`: `2000-2010` → `2020-03-01..2021-01-31` (rango pandemia)
   - `metadata.version`: `v2 sonda segundo orden` → `v3 real Google Mobility 2026-05-17`
2. **`src/data.py`**: 130 líneas modificadas (pipeline de ingesta)
3. **`src/fetch_real.py`**: archivo nuevo (130 líneas, no existía al sello)
4. **`data/behavioral_dynamics_real.csv`**: archivo nuevo (no existía al sello)

### Impacto en resultados

| Variable | Pre-violación (sello) | Post-violación (iter 11) | Δ |
|---|---|---|---|
| Real EDI | 0.262 | 0.614 | **+0.352** |
| Real p-value | 0.044 | 0.000 | −0.044 |
| Clasificación | Weak | **Strong** | upgrade no autorizado |
| overall_pass | false | true | flip |

El pre-registro §2 predijo **Weak con cola hacia Null** y `downgrade probable` sobre datos reales humanos. La violación produjo el **resultado opuesto** (upgrade a Strong), que es exactamente el modo de fallo "garden of forking paths" que el pre-registro buscaba bloquear (Gelman & Loken 2014).

Adicionalmente: el pre-registro §4 declaraba como datasets candidatos VENLab / OpenLocomotionData / WALK-MS (todos perception-action locomotion humana, LoE 3-4). Google Mobility (LoE=1.5) **no aparece como opción**; mide presencia agregada en ubicaciones durante pandemia, **no** trayectorias de heading. La sustitución es ilegítima por dos razones independientes:

1. Violación procedimental: cambio post-sello prohibido por §6.
2. Violación de constructo: el proxy ya no mide locomoción dirigida Fajen-Warren; mide otra cosa (movilidad poblacional) y por tanto el EDI alto no testea la hipótesis pre-registrada.

## Decisión: REVERTIR

Acción ejecutada:

```bash
git show c6b3d3b:09-simulaciones-edi/30_caso_behavioral_dynamics/case_config.json > .../case_config.json
git checkout c6b3d3b -- 09-simulaciones-edi/30_caso_behavioral_dynamics/src/data.py
rm 09-simulaciones-edi/30_caso_behavioral_dynamics/src/fetch_real.py
cd 09-simulaciones-edi && source .venv/bin/activate
python3 30_caso_behavioral_dynamics/src/validate.py
```

Resultado tras revert (reproducible):
- `synthetic`: EDI=0.1327, pass=false
- `real`: EDI=0.2622, p=0.044, pass=false

El EDI=0.262 sobre el sintético es coherente con la **predicción pre-registrada** (Weak con p<0.05 en perfil agresivo implícito por defecto del runner). Nótese que el "real" en este caso reverted sigue siendo sintético (el real CSV se eliminó porque no existía al sello y violaba §6). El pre-registro §4 declaraba fecha de descarga prevista `2026-05-22` — aún no era exigible una corrida con datos reales.

## Estado del manuscrito

Si algún capítulo cita EDI=0.614 / Strong para caso 30 → debe corregirse a EDI=0.262 / Weak (sintético; real pendiente de fetch legítimo el 2026-05-22 según §4 del pre-registro).

### Archivos del manuscrito con citas afectadas (todos marcan EDI=0.6143 / Strong / Google Mobility — IRREALIZABLES):

- `00-proyecto/05-resumen-y-abstract.md`
- `05-aplicaciones/07-mapa-aplicaciones-corpus.md`
- `06-cierre/01-conclusion-demostrativa.md`
- `06-cierre/02-guia-de-defensa.md`
- `TesisFinal/Tesis.md` (derivado — se regenera tras corregir capítulos)

Estos pasajes están declarados **BORRADOR-IA en deuda** hasta que: (a) se ejecute el fetch real legítimo conforme §4 (VENLab / OpenLocomotionData / WALK-MS) en o después de `2026-05-22`, o (b) se firme un pre-registro nuevo y se reporten los resultados como análisis exploratorio post-hoc explícito. Mientras tanto, el resultado defendible para caso 30 es **EDI=0.262 sintético Weak/Trend**, no Strong.

## Lección operativa

El loop nocturno iter 11 ejecutó B-T2 (sustituir sintético por real) sobre caso 30 **horas después** de firmar el pre-registro que congelaba el protocolo y declaraba fecha de fetch `2026-05-22`. El sub-agente que ejecutó el cambio violó §6 sin verificación del compromiso de no-modificación. Recomendación al harness:

- `verify_preregistration.py` debe correr **antes** de cualquier modificación de `case_config.json` o `src/data.py` de casos con `PRE_REGISTRO.md` activo, no solo después.
- Hook pre-commit que bloquee modificaciones a `case_config.json` si existe `docs/PRE_REGISTRO.md` con commit-sello posterior al último modificador.
