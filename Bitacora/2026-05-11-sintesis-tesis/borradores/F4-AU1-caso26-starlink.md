---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 05-aplicaciones/07-mapa-aplicaciones-corpus.md:124 ; 06-cierre/04-versiones-cortas-defensa.md:110
hallazgo: Bitacora/2026-05-04-continuous-run/AU-1-caso26-starlink.md
tipo: reemplazo_parrafo + recuento agregado
---

## Diagnóstico

Caso 26 Starlink figura como "Trend (Nivel 1)" en Tabla 5.7.7 pese a que `metrics.json` (fase real, líneas 679–765) reporta `val_steps=1`, `ci_lo == ci_hi == edi.value = 0.6892`, `permutation_pvalue = 1.0` y `correlations.abm_obs = 0.0`. Con un único punto de validación el bootstrap colapsa y la permutación carece de grados de libertad: el EDI=0.689 es **artefacto numérico, no medición**. La patología es estructuralmente idéntica a la del caso 19 (ya en cuarentena por B-T5).

## Verificación contra fuente primaria

`09-simulaciones-edi/26_caso_starlink/outputs/metrics.json` (phases.real):

```
data.val_steps              = 1
edi.value                   = 0.6891705119737255
edi.ci_lo == edi.ci_hi      = 0.6891705119737255
edi.permutation_pvalue      = 1.0
edi.permutation_significant = false
correlations.abm_obs        = 0.0
viscosity.pass              = false
```

Comando regenerador: `python3 09-simulaciones-edi/26_caso_starlink/src/validate.py`.

## Texto propuesto (voz autoral filosófica de Jacob)

**En `05-aplicaciones/07-mapa-aplicaciones-corpus.md:124`**, mover el caso 26 de la Tabla 5.7.7 (Trend Nivel 1) a una sub-sección nueva o nota visible:

> **Casos en cuarentena por insuficiencia de datos.** Caso 26 (Starlink) y caso 19 (acidificación oceánica) comparten una misma patología: el dato real disponible para la fase de validación es estructuralmente insuficiente para que el EDI tenga contenido estadístico. Para 26 esto se traduce en `val_steps=1` con `ci_lo = ci_hi = edi.value` (el bootstrap colapsa cuando no hay puntos para remuestrear) y `permutation_pvalue=1.0` (la permutación sobre un único punto carece de grados de libertad). En ambos casos el EDI numérico que figura en `metrics.json` no debe leerse como medición sino como artefacto numérico del pipeline. La tesis declara estos casos en cuarentena hasta que el dataset admita un `val_steps≥8` o se decida su reclasificación como null por insuficiencia de datos. El comando regenerador asociado es `python3 09-simulaciones-edi/26_caso_starlink/src/validate.py`; cualquier reclasificación posterior queda condicionada a una re-ejecución con dataset extendido.

## Texto a reemplazar

- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:124`: línea actual en Tabla 5.7.7 que cita `0.6892 | 1.0000 | val_steps=1 — exploratorio`. El epíteto "exploratorio" no salva la clasificación como Trend; debe sustituirse por reubicación en bloque de cuarentena.
- `06-cierre/04-versiones-cortas-defensa.md:110`: la enumeración "4 trend" pasa a "3 trend + cuarentena por insuficiencia de datos (19, 26)".

## Costo argumentativo declarado

El conteo "4 trend" del corpus inter-dominio cae a 3; los conteos agregados en defensas cortas y en cap 06 deben recalcularse en cascada. La pérdida narrativa es menor que el coste de mantener una cifra que cualquier revisor que abra `metrics.json` rechazará en segundos.

## Acción técnica derivada (B-T)

Verificar si el dataset Starlink admite `val_steps≥8` ajustando el split temporal; si no, reclasificar como null por insuficiencia de datos.
