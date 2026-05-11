---
borrador: IA
requires: H-J* + B-T
propuesta_fecha: 2026-05-11
destino: harness/ + 09-simulaciones-edi/scripts_orquestacion/audit/ + cap 06 Deuda residual
hallazgo: Bitacora/2026-05-04-continuous-run/TENG-12-hash-no-detecta-inconsistencia-interna.md
tipo: tarea_B-T_verify_internal_consistency.py + insercion_deuda
---

## Diagnóstico

`09-simulaciones-edi/scripts_orquestacion/audit/replay_hash.py:44-52` (`md5_metrics`) calcula MD5 sobre el JSON normalizado. Detecta cualquier divergencia carácter a carácter, pero **no examina ninguna relación algebraica entre campos**. Esto permite que un `metrics.json` internamente contradictorio (como el caso 19 fase real documentado en F4-TENG-05) pase la auditoría `replay_hash --verify` reportando "Sin cambios" mientras el archivo viola los invariantes algebraicos que `hybrid_validator.py` declara garantizar. **La reproducibilidad reproduce el bug en lugar de exponerlo.**

## Verificación

- `replay_hash.py:44-52` — `md5_metrics` hashea bytes del JSON normalizado (con `sort_keys=True`).
- `replay_hash.py:129-175` — `verify_baseline` compara hash actual contra baseline guardado; no abre el JSON ni recomputa nada.
- Inspección directa de `09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/metrics.json`:
  - `phases.real.edi.value = 0.7278`
  - `value * loe_factor = 0.4367`
  - `weighted_value reportado = -0.000115` (incompatible con value)
  - `(rmse_no_ode − rmse_abm)/rmse_no_ode = -0.000191` (incompatible con value)
  - `ci_lo ≤ value ≤ ci_hi`: True (CI sí abraza 0.7278 — único invariante respetado)
- Comportamiento de `replay_hash.py --verify`: reporta "✓ Sin cambios" y código de salida 0 porque el archivo es bit-idéntico entre corridas; la auditoría declara reproducibilidad cuando lo que se está reproduciendo es un metrics.json internamente contradictorio.

## Texto propuesto (voz autoral filosófica de Jacob)

**Insertar como deuda residual del harness en `06-cierre/Deuda residual` o en la documentación de `harness/`:**

> **Deuda residual técnica: hash MD5 no detecta inconsistencia interna.** El verificador `replay_hash.py` certifica reproducibilidad **bit-a-bit** del `metrics.json` entre corridas, pero no examina invariantes algebraicos entre campos. Esto permitió que el bug del caso 19 fase real (cf. F4-TENG-05) sobreviviera múltiples corridas de auditoría: el archivo es internamente contradictorio (`value`, `weighted_value` y `errors` provienen de ejecuciones distintas fusionadas) pero el hash MD5 reporta "Sin cambios". La reproducibilidad reproduce el bug.
>
> La tesis adopta como B-T abierta la implementación de un verificador adicional `verify_internal_consistency.py` que examine, por cada fase de cada caso del corpus, los siguientes tres invariantes con tolerancias declaradas:
>
> 1. `|edi.value − weighted_value/loe_factor| < 1e-6` (si `loe_factor ≠ 0`)
> 2. `|edi.value − (rmse_abm_no_ode − rmse_abm)/rmse_abm_no_ode| < 1e-4`
> 3. `ci_lo ≤ edi.value ≤ ci_hi`
>
> Salida: `internal_consistency_report.json` listando, por caso/fase, las violaciones. Casos que violen algún invariante quedan bloqueados para citación en prosa hasta su re-ejecución.
>
> Esta deuda no resuelve la causa raíz del caso 19; la expone y la previene a futuro. La causa raíz (cuáles dos ejecuciones se fusionaron y por qué) sigue requiriendo `B-T5 — caso 19 anomaly` y la re-ejecución del caso bajo perfil canónico (cf. F4-TENG-05).

## Acciones técnicas derivadas (B-T)

1. **Decisión metodológica previa (H-J):** declarar cuál escalar es **canónico** en la fase real del caso 19 — `value` o `weighted_value/rmse_derived`. Esta decisión condiciona la dirección del verificador (qué se considera fuente de verdad si los tres invariantes discrepan).
2. **Implementar `09-simulaciones-edi/scripts_orquestacion/audit/verify_internal_consistency.py`** con los tres invariantes; cobertura: 40 casos inter-dominio + 10 corpus inter-escala = 50 casos × ≥2 fases.
3. **Cablear a `./tesis audit`**: ejecutar `verify_internal_consistency.py` antes de `replay_hash.py`. Cualquier violación bloquea el build hasta resolución o declaración explícita de deuda por caso.
4. **Manejo de bordes:** casos con `loe_factor = 0` o `rmse_no_ode = 0` deben tratarse explícitamente para evitar falsos positivos.

## Costo argumentativo declarado

- Esto no resuelve la anomalía del caso 19; sólo la expone (y previene futuras inconsistencias similares).
- Añade un verificador más a la cadena del harness; riesgo de falsos positivos en bordes (mitigable con manejo explícito).
- Coste de no actuar: cualquier caso que reproduzca el patrón del caso 19 pasará la auditoría de hash silenciosamente, y la regla "gana el JSON" deja de tener sentido cuando el JSON es internamente contradictorio.
- No detecta inconsistencias **semánticas** fuera de los tres invariantes algebraicos (por ejemplo, p-valor incompatible con la null distribution); esa sería deuda adicional separada.
