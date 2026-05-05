# TENG-12 — Hash MD5 no detecta inconsistencia interna del metrics.json

**Fecha:** 2026-05-05
**Sub-agente:** auditoría headless (process-verifier follow-up)
**Modo:** read-only sobre código + lectura de `metrics.json`. No edita Tesis.md ni metrics.json.
**Estado:** `needs_human` (B-T*) — propuesta de verificador adicional, no parche en caliente.

---

## (a) Verificación de la afirmación

**Afirmación auditada:** "MD5(metrics.json) en `replay_hash.py` detecta cambios externos (re-ejecución, edición textual) pero no contradicciones internas como las del caso 19. La reproducibilidad reproduce el bug en lugar de exponerlo."

**Verificación operativa.**

1. `09-simulaciones-edi/scripts_orquestacion/audit/replay_hash.py:44-52` (`md5_metrics`) calcula MD5 sobre el JSON normalizado (clave `sort_keys`, sin `generated_at`/`commit`/`dirty`). Es decir, **hash criptográfico de bytes**: detecta cualquier divergencia carácter a carácter, pero no examina ninguna relación algebraica entre campos.
2. `verify_baseline` (`replay_hash.py:129-175`) compara el hash actual contra un baseline guardado. Si los dos coinciden, declara "Sin cambios". No abre el JSON ni recomputa nada.
3. **Inspección directa de `09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/metrics.json`:**

   | Fase | `edi.value` | `value * loe_factor` | `weighted_value` reportado | `(rmse_no_ode − rmse_abm)/rmse_no_ode` | `ci_lo ≤ value ≤ ci_hi` |
   |---|---|---|---|---|---|
   | synthetic | 4.279e-5 | 2.568e-5 | 2.568e-5 ✓ | 4.279e-5 ✓ | True |
   | real | **0.7278** | **0.4367** | **−0.000115 ✗** | **−0.000191 ✗** | True (CI sí abraza 0.7278) |

   El `edi.value=0.7278` declarado en la fase real es **incompatible** con los RMSE crudos del mismo objeto (`(rmse_no_ode−rmse_abm)/rmse_no_ode = −0.000191`), e incompatible con el `weighted_value` reportado (que es ≈0 cuando debería ser 0.4367 si `loe_factor=0.6`). Sólo el CI `[0.6587, 0.7909]` es coherente con el `value`, lo que sugiere que `value` y `ci_*` provienen de un cálculo y `weighted_value`+`rmse_*` provienen de otro: el JSON fija dos estimaciones contradictorias del mismo escalar.

4. **Comportamiento de `replay_hash.py` ante este caso:** dado que el archivo es bit-idéntico entre corridas, `--verify` reporta "✓ Sin cambios" y emite código de salida 0. La auditoría declara reproducibilidad cuando lo que se está reproduciendo es un metrics.json internamente contradictorio. La afirmación se confirma.

**Conclusión:** la afirmación es correcta y operacionalmente verificada en el caso 19, fase real. No es teórica.

## (b) Propuesta concreta — `needs_human`

Crear un nuevo verificador `09-simulaciones-edi/scripts_orquestacion/audit/verify_internal_consistency.py` (o módulo dentro de `replay_hash.py`) que, **por cada fase de cada caso**, compruebe:

```
C1: |edi.value − weighted_value/loe_factor| < 1e-6        (si loe_factor != 0)
C2: |edi.value − (rmse_abm_no_ode − rmse_abm)/rmse_abm_no_ode| < 1e-4
C3: ci_lo ≤ edi.value ≤ ci_hi
```

con tolerancias declaradas en cabecera y output JSON `internal_consistency_report.json` listando, por caso/fase, las violaciones. Acceptance del task pide ≥30 casos cubiertos; el corpus tiene 40, así que basta iterar `SIMS_DIR.glob("[0-9]*_caso_*")` igual que `collect_hashes`.

**Costo argumentativo declarado:**

- Esto **no resuelve** la anomalía del caso 19; sólo la expone. La causa raíz (fase real con `weighted_value≈0` y `value=0.7278`) sigue requiriendo `B-T5 — caso 19 anomaly`.
- Añade un verificador más a la cadena ya barroca del harness; hay riesgo de que dispare falsos positivos en casos donde `loe_factor=0` o `rmse_no_ode=0` (necesario manejo explícito).
- El criterio C2 con tolerancia 1e-4 asume que `weighted_value` no es la fuente canónica; si el equipo decide que `weighted_value` *sí* es la fuente (y `value` debe re-derivarse), el verificador debe invertirse. **Esa decisión es de Jacob/Steven, no del sub-agente.**
- No detecta inconsistencias *semánticas* fuera de los tres invariantes algebraicos (p.ej. p-valor incompatible con la null distribution); sería otro verificador adicional.

**Por qué `needs_human`:** introducir un verificador nuevo en la cadena de auditoría requiere (i) decidir cuál de los dos valores en disputa (`value` vs `weighted_value`) es canónico y (ii) decidir si los casos que actualmente fallan C1/C2 deben bloquear el build o sólo emitir warning. Ambos son cortes editoriales que pertenecen a Steven (técnico canónico) o Jacob (interpretación). La asistencia no debe cerrarlos.

## (c) Acceptance — estado

| Criterio | Estado |
|---|---|
| `|edi.value − weighted_value/loe_factor| < 1e-6` | Verificador **no implementado** (propuesta arriba). Caso 19 fase real **violaría** (diff ≈ 0.437). |
| `|edi.value − (rmse_no_ode − rmse_abm)/rmse_no_ode| < 1e-4` | Verificador **no implementado**. Caso 19 fase real **violaría** (diff ≈ 0.728). |
| `ci_lo ≤ edi.value ≤ ci_hi` | Verificador **no implementado**. Caso 19 ambos OK; útil sin embargo. |
| Corre sobre 30+ casos | Pendiente de implementación. Cobertura factible: 40 casos. |

## Próxima acción

1. Steven/Jacob deciden cuál escalar es canónico en la fase real del caso 19 (`value` vs `weighted_value`/`rmse`).
2. Si se aprueba, asistencia implementa `verify_internal_consistency.py` con los 3 invariantes y lo cablea a `./tesis audit`.
3. Una vez activo, **se vuelve obligatorio** declarar deuda en cada caso que viole algún invariante, en lugar de seguir hasheando el bug.

**RESULT: complete | TENG-12-hash-no-detecta-inconsistencia-interna | claim verified, fix needs_human**
