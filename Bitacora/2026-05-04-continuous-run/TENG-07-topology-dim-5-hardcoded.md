# TENG-07 — `topology_report(x, dim=5)` hard-codeado

Fecha: 2026-05-05
Origen: process-verifier engine 2026-05-05.
Archivo señalado: `09-simulaciones-edi/common/topology.py:183`.

## (a) Verificación de la afirmación

### Lo que la afirmación dice
> `topology_report(x, dim=5)` hard-codeado: con `val_steps≤8` ⇒ `'insufficient embedded points'` silencioso en ~40% del corpus.

### Lo que se verifica en el código

`09-simulaciones-edi/common/topology.py:183`:

```python
def topology_report(x: np.ndarray, dim: int = 5) -> dict[str, Any]:
    x = np.asarray(x, dtype=float)
    if len(x) < 30:
        return {"error": f"series too short (n={len(x)})", "n": len(x)}
    tau = max(1, autocorr_first_zero(x))
    return {
        "n": int(len(x)),
        "embedding_dim": dim,
        "tau_acf_zero": tau,
        "mixing_time": mixing_time(x),
        "lyapunov": lyapunov_rosenstein(x, dim=dim, tau=tau),
        "correlation_dimension": correlation_dimension(x, dim=dim, tau=tau),
    }
```

- `dim=5` es el default fijo. No se adapta a `len(x)` ni a `tau`.
- El número de puntos embebidos es `n_emb = len(x) - (dim-1)*tau`. Tanto `correlation_dimension` (línea 63) como `lyapunov_rosenstein` (línea 114) abortan con `{"error": "insufficient embedded points", "n": n_emb}` cuando `n_emb < 50`.
- Con `dim=5`, `tau≥1` y `len(x)=val_steps≤8`, `n_emb ≤ 8 − 4·1 = 4`. Mucho antes ya falla `len(x)<30` y devuelve `series too short`. La rama "insufficient embedded points" se dispara cuando `30 ≤ len(x) < 50 + 4·tau` (caso típico ~50–70 muestras con `tau∈[5,20]`).

### Lo que NO se verifica empíricamente

Auditoría de los 32 `metrics.json` activos (`09-simulaciones-edi/*/outputs/metrics.json`):

| Métrica | Valor |
|---|---|
| Archivos `metrics.json` | 32 |
| Con bloque `topology` | **0** |
| Con error `insufficient embedded` en `metrics.json` | 0 |

Es decir: **`topology_report` no es invocado por el validador canónico** que produce los `metrics.json` del corpus. No hay grep de uso fuera del propio módulo. La única salida actual de `topology_report` vive en `09-simulaciones-edi/topology/topology_report.json` (solo 7 casos, 0 errores, ejecutado offline con `dim=3`).

→ **La cuantificación "~40% del corpus" no se reproduce con el estado actual.** El defecto del `dim=5` hard-codeado existe en el módulo, pero el efecto silencioso a escala del corpus que enuncia el hallazgo no se materializa porque la función está latente.

## (b) Propuesta concreta

### Edición no controvertida (puede hacerse sin firma humana)

Hacer `dim` adaptativo dentro de `topology_report` y propagar la metadata, dejando intacta la API pública:

```python
def topology_report(x: np.ndarray, dim: int | None = None) -> dict[str, Any]:
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n < 30:
        return {"error": f"series too short (n={n})", "n": n,
                "topology_valid": False}
    tau = max(1, autocorr_first_zero(x))
    # Selección adaptativa: el mayor dim ∈ {5,4,3,2} que asegure n_emb ≥ 50
    candidates = [dim] if dim is not None else [5, 4, 3, 2]
    chosen, n_emb = None, 0
    for d in candidates:
        ne = n - (d - 1) * tau
        if ne >= 50:
            chosen, n_emb = d, ne
            break
    if chosen is None:
        chosen = max(2, candidates[-1])
        n_emb = n - (chosen - 1) * tau
    valid = n_emb >= 50
    return {
        "n": int(n),
        "embedding_dim": chosen,
        "embedding_dim_requested": dim if dim is not None else 5,
        "n_embedded": int(n_emb),
        "tau_acf_zero": tau,
        "topology_valid": bool(valid),
        "mixing_time": mixing_time(x),
        "lyapunov": lyapunov_rosenstein(x, dim=chosen, tau=tau),
        "correlation_dimension": correlation_dimension(x, dim=chosen, tau=tau),
    }
```

Costo: cambia el `dim` reportado en `topology_report.json` (offline). No toca `metrics.json` del corpus porque hoy esos archivos no contienen `topology`.

### Edición que requiere firma humana — **needs_human**

El acceptance pide:

> "campo `topology_valid:bool` en `metrics.json`; ningún `metrics.json` con `topology.lyapunov.error` si `val_steps≥20`"

Eso exige **plumbing nuevo** en el pipeline:

1. Llamar `topology_report` desde el validador canónico (`hybrid_validator.py` u orquestador) sobre la serie observada de cada caso.
2. Inyectar el bloque `topology` (con `topology_valid`) en cada `metrics.json` de los 32 casos.
3. Re-ejecutar y re-firmar hashes (`HASHES_PRE_EJECUCION.json`, `./tesis hash`).

CLAUDE.md §4 prohíbe edits a `metrics.json`; un cambio que rellena `topology` en 32 archivos altera la fuente de verdad numérica. Además, escoger qué serie alimentar a `topology_report` (¿`obs`?, ¿`coupled`?, ¿`val` o `train+val`?) es una decisión metodológica que pertenece a Jacob.

→ **Marcar como `needs_human` (firma de Jacob + Steven):**

- Decidir la serie de entrada canónica para topología por caso.
- Autorizar la inyección del bloque `topology` en los 32 `metrics.json` y la re-firma de hashes.
- Decidir si `topology_valid:False` con `val_steps≥20` debe abortar el caso o solo marcarlo como advertencia.

## (c) Costo argumentativo declarado

- **El defecto técnico es real pero su impacto en la tesis hoy es cero**: ningún capítulo del manuscrito apoya un argumento sobre el bloque `topology` de un `metrics.json`, porque ese bloque no existe en el corpus. La cifra "~40% del corpus" del hallazgo original no se sostiene con la evidencia auditada.
- **Convertir el defecto en mejora**: hacer `dim` adaptativo en el módulo es saludable y barato; pero si NO se llama desde el pipeline, el `topology_valid:bool` en `metrics.json` no puede satisfacerse sin tocar el pipeline y los 32 archivos.
- **Riesgo de auto-indulgencia**: añadir `topology_valid:True` por defecto en casos cortos (val_steps<8) con `dim=2` produciría una métrica "verde" sin contenido. Hay que aceptar `topology_valid:False` como salida legítima y reportar la deuda en lugar de inflar el dim a la baja.
- **Riesgo opuesto**: bajar `dim` a 2 en cualquier caso para "rescatar" la métrica reduce la dimensión del atractor reconstruido y destruye la interpretación Takens (1981) cuando la dimensión real del sistema es ≥3. La regla `n_emb ≥ 50` es necesaria pero no suficiente; los casos con `dim<3` deben llevar etiqueta `topology_indicative_only:True` en la prosa.

## Decisión

- Edición barata propuesta arriba: lista para revisión, no aplicada en esta pasada (no tocó pipeline ni JSON).
- Acceptance completo: `needs_human` — requiere decisión metodológica de Jacob y re-firma de hashes con Steven.

RESULT: complete | TENG-07-topology-dim-5-hardcoded | claim parcial: defecto real, "~40%" no se reproduce; needs_human
