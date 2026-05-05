# E1 — Auditoría corpus summary (apéndice ↔ metrics.json)

**Fecha:** 2026-05-05
**Modo:** continuous-run / kind=audit / READ-ONLY
**Tarea:** comparar `09-simulaciones-edi/<NN>_caso_<x>/outputs/metrics.json` contra Tabla A.8.1 de `10-apendices-tecnicos/01-tablas-crudas-corpus-interdominio.md`.

## Alcance

- 32 archivos `metrics.json` encontrados (casos 01–30 + 41 wolfram_extendido + 42 histeresis_institucional).
- Tabla A.8.1 enumera 30 filas (corpus inter-dominio canónico). Casos 41 y 42 no están en la tabla A.8.1 — pertenecen al corpus extendido fuera del alcance de este apéndice y se omiten de la comparación.
- Campos comparados: `edi.value` (vs columna EDI) y `edi.permutation_pvalue` (vs columna p) de la fase `real` (con fallback `synthetic`). Se eligió la fase con menor distancia agregada a la fila de prosa.
- Tolerancias: ΔEDI < 0.005, Δp < 0.01.

## Resultado agregado

| Estado | Casos |
|---|---|
| Coincidencia dentro de tolerancia | **29 / 30** |
| Discrepancia | **1 / 30** (caso 16) |
| Casos fuera de alcance del apéndice | 2 (41, 42) |

Los 29 casos coincidentes coinciden con la fase `real` de cada `metrics.json` (no con `synthetic`). La diferencia residual en EDI es del orden 1e-5 a 5e-5 — ruido de redondeo a 4 decimales en la prosa, no discrepancia material.

## Discrepancia material

| # | Caso | Prosa A.8.1 | JSON (fase real) | ΔEDI | Δp |
|---|------|--:|--:|--:|--:|
| 16 | Deforestación global | EDI=0.6020, p=0.0000 | EDI=0.5802, p=0.0000 | **0.0218** | 0.0000 |

**Estado:** discrepancia ya **declarada** en el propio apéndice (líneas 9 y 100 del documento, nota de reconciliación 2026-04-29):

> "para el caso 16 (Deforestación), la cifra canónica reportada en Tabla A.8.1 (EDI=0.6020) corresponde al perfil canónico documentado y archivado en git history; el `metrics.json` actualmente persistido (...) refleja la re-ejecución agresiva (EDI=0.5802 con CI más amplio), reportada en Tabla A.8.3 como verificación contrastiva."

La Tabla A.8.3 reporta explícitamente el par (0.6020, 0.5802) como verificación canónico↔agresivo. El nivel 4 strong se preserva en ambas ejecuciones. La reconciliación de re-ejecutar y persistir el JSON canónico está abierta como tarea **B-E7** en `TAREAS_PENDIENTES.md`.

**Veredicto:** la discrepancia no es fraude ni inconsistencia oculta — está documentada en el mismo apéndice, vinculada a una tarea pendiente (B-E7), y la cifra canónica es defendible vía la nota de reconciliación. **No requiere acción correctiva en este pase**; cierre formal depende de B-E7 (re-ejecución canónica que persista el JSON).

## Caso 30 — nota separada

La cabecera del apéndice (línea 17) declara una discrepancia **prevista** en caso 30:

> "Para el caso 30 Behavioral Dynamics: la fila tabular conserva la cifra canónica histórica (EDI=0.2622 con p=0.0440) (...); el `metrics.json` actual persiste valores divergentes (EDI=0.2555 con p=0.5170)."

Sin embargo, la lectura actual del JSON da `phases.real.edi.value ≈ 0.26224` y `permutation_pvalue ≈ 0.04404` — coincidente con la prosa dentro de tolerancia. La discrepancia anunciada en la nota de cabecera **ya no se observa**: el JSON parece haberse re-ejecutado/sincronizado tras escribir esa nota. La tarea B-E5 (descrita como abierta en la cabecera) podría estar de facto cerrada; conviene que un humano (Jacob) actualice la nota de reconciliación para retirarla y cierre B-E5 si corresponde.

## Casos fuera de alcance

- `41_caso_wolfram_extendido` y `42_caso_histeresis_institucional` no aparecen en Tabla A.8.1. No es discrepancia: el apéndice 1 cubre el corpus inter-dominio de 30 casos. Estos pertenecen a un sub-corpus extendido posterior. Recomendación opcional para Jacob: confirmar si el apéndice 1 debe extenderse o si existe un apéndice separado para casos 41+.

## Comando regenerador

```bash
python3 - <<'PY'
import json, glob, re
table = open('10-apendices-tecnicos/01-tablas-crudas-corpus-interdominio.md').read()
prose = {}
in_t = False
for line in table.split('\n'):
    if 'Tabla A.8.1.' in line: in_t = True
    if 'A.8.2' in line: in_t = False
    if in_t:
        m = re.match(r'\|\s*(\d{2})\s*\|\s*([^|]+)\|[^|]*\|\s*(-?[\d.]+)\s*\|\s*(-?[\d.]+)\s*\|', line)
        if m:
            try: prose[m.group(1)] = (float(m.group(3)), float(m.group(4)))
            except: pass
for path in sorted(glob.glob('09-simulaciones-edi/*/outputs/metrics.json')):
    cid = path.split('/')[1].split('_')[0]
    if cid not in prose: continue
    j = json.load(open(path))
    for ph in ('real','synthetic'):
        e = j.get('phases',{}).get(ph,{}).get('edi',{})
        if e:
            print(f"{cid} [{ph}] json EDI={e.get('value'):.4f} p={e.get('permutation_pvalue'):.4f} | prose EDI={prose[cid][0]} p={prose[cid][1]}")
PY
```

## Conclusión

El corpus apéndice ↔ JSON está **internamente consistente** modulo dos casos (16, 30) que el propio apéndice identifica con notas de reconciliación. No se detectaron discrepancias ocultas. No hay edits a aplicar en este pase (auditoría read-only). Acciones para Jacob:

1. Cerrar B-E7 ejecutando re-validación canónica del caso 16 con persistencia del JSON.
2. Verificar caso 30: el JSON actual ya coincide con prosa; la nota de reconciliación de cabecera puede retirarse y B-E5 cerrarse si confirma.
3. Considerar si casos 41/42 deben incorporarse a A.8.1 o tabularse en apéndice aparte.
