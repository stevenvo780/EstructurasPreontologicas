# Pre-registro EDI — instrucciones de uso

Plantilla: [`PRE_REGISTRO_TEMPLATE.md`](./PRE_REGISTRO_TEMPLATE.md).

## Cuándo aplicar

Para los ~20 casos del corpus que **aún no se han re-ejecutado sobre datos reales** (ver `Evaluacion_Modelos_Dominio.md`, columna "estado"). El pre-registro se firma **antes** de ejecutar `validate.py` sobre la serie real; no aplica a casos ya cerrados (resultado conocido = no hay pre-registro posible).

## Procedimiento

1. **Copiar plantilla:**
   ```bash
   cp 09-simulaciones-edi/PRE_REGISTRO_TEMPLATE.md \
      09-simulaciones-edi/<NN>_caso_<nombre>/docs/PRE_REGISTRO.md
   ```
2. **Rellenar §1–§5** sin haber inspeccionado el CSV real (si ya se vio, declararlo como sesgo de §2).
3. **Commit del pre-registro antes de descargar/ejecutar:**
   ```bash
   git add 09-simulaciones-edi/<NN>_caso_<nombre>/docs/PRE_REGISTRO.md
   git commit -m "pre-registro B-T2: caso <NN>_<nombre> (pre-ejecución)"
   ```
   El hash del commit queda como sello temporal verificable.
4. **Descargar datos reales** según §4. Calcular sha256 del CSV y commitear actualización:
   ```bash
   sha256sum 09-simulaciones-edi/<NN>_caso_<nombre>/data/<archivo>.csv
   ```
5. **Ejecutar `validate.py`** con la seed y los hiperparámetros declarados en §3. Sin modificar `case_config.json` ni `src/*.py` entre §3 y la ejecución.
6. **Reportar resultado** en `outputs/report.md` indicando si coincide con la predicción (§2) o constituye contraevidencia (§6).
7. **Actualizar** `Evaluacion_Modelos_Dominio.md` con la clasificación observada.

## Compatibilidad con OSF (Open Science Framework)

La plantilla sigue la estructura mínima de un pre-registro OSF (hipótesis → especificación → criterios de cierre → firma). Si Jacob decide subirla públicamente:

- Crear proyecto en https://osf.io/, copiar §1–§6 al formulario "Preregistration".
- Adjuntar el commit hash del repo como sello temporal independiente.
- DOI del pre-registro va a `07-bibliografia/` como referencia auto-citable.

## Qué NO es un pre-registro válido

- Rellenar la plantilla **después** de ejecutar `validate.py` (eso es post-hoc, no pre).
- Cambiar la sonda ODE o los umbrales tras ver el primer resultado y volver a firmar (eso es p-hacking).
- Pre-registrar solo casos donde se espera Strong (sesgo de selección).
- Declarar margen de tolerancia tan amplio que cualquier resultado lo cumpla (`|ΔEDI| ≤ 1.0` = no es predicción).

## Vínculo con el harness

El verificador `harness/verifiers/preregistration.py` (pendiente, B-T2.1) comprobará:
- existencia de `docs/PRE_REGISTRO.md` para casos en estado "pre-registrado"
- coincidencia entre §3 (sonda, n_perm, seed) y `case_config.json` + `outputs/metrics.json`
- timestamp del commit del pre-registro **anterior** al timestamp de `outputs/metrics.json`

Mientras ese verificador no exista, la disciplina es manual: el commit del pre-registro debe preceder al commit de los outputs.
