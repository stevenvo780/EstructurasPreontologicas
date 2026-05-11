---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 05-aplicaciones/07-mapa-aplicaciones-corpus.md:124,140 (Tablas 5.7.7 y 5.7.8)
hallazgo: Bitacora/2026-05-04-continuous-run/F05-10-19-26-promovidos-sin-significancia.md
tipo: reformulacion_tabla + correccion_taxonomia
---

## Diagnóstico

Los casos 19 (Acidificación oceánica) y 26 (Starlink) están promovidos a "Trend (Nivel 1*)" o "Trend Nivel 1*" en las Tablas 5.7.7-8 del cap 05-07 a partir de `edi.value` alto (`0.728`, `0.689`) pese a que la permutación es **no significativa** (p = 0.49, p = 1.0). Caso 19 tiene `weighted_value = -0.0001` (negativo tras ponderar por LoE) y `trend_r²=0.861` (el EDI nominal está dominado por la tendencia, no por estructura acoplada; ver además F4-TENG-05 para la inconsistencia interna de su `metrics.json`). Caso 26 tiene `val_steps = 1` con CI bootstrap degenerado (`ci_lo = ci_hi = edi.value`) — sin contenido estadístico (ver F4-AU1). Promoverlos a "Trend" con asterisco es la categoría inventada que Ioannidis 2005 advierte: separar tamaño de efecto de significancia y darle peso evidencial al primero sin lo segundo.

## Verificación contra fuente primaria

`09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/metrics.json` phases.real:
```
edi.value                    = 0.7278  (probablemente stale; ver F4-TENG-05)
edi.permutation_pvalue       = 0.49
edi.permutation_significant  = False
edi.bootstrap CI             = [0.659, 0.791]
edi.weighted_value           = -0.00011  (ponderado por LoE=0.6)
trend_bias.trend_r2          = 0.861
val_steps                    = 360
```

`09-simulaciones-edi/26_caso_starlink/outputs/metrics.json` phases.real:
```
edi.value                    = 0.6892
edi.permutation_pvalue       = 1.0
edi.permutation_significant  = False
edi.ci_lo == edi.ci_hi       = 0.6892   (CI bootstrap degenerado)
val_steps                    = 1
phases.synthetic.edi.value   = -0.457   (negativo y fallido)
```

Ioannidis 2005, "Why Most Published Research Findings Are False", *PLoS Medicine* 2(8):e124. PDF no presente en `07-bibliografia/` (B-T:fetch-ioannidis-2005). El argumento operativo (separar tamaño de efecto y significancia) es estándar y se sostiene sin la cita literal.

## Texto propuesto (voz autoral filosófica de Jacob)

**Eliminar casos 19 y 26 de la fila "Trend (Nivel 1*)" en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:124,140` y reubicarlos.**

Para caso 19, reescribir su línea en el bloque correspondiente:

> **Caso 19 (Acidificación oceánica).** `edi.value` nominal `= 0.728` está **dominado por tendencia** (`trend_r² = 0.861`); la permutación no es significativa (`p_perm = 0.49`); el `weighted_value` ponderado por LoE es negativo (`-0.0001`); el `metrics.json` presenta además inconsistencia interna detectada (cf. F4-TENG-05). Se clasifica como **null por tendencia espuria**, **no como Trend**. Re-evaluación con sondas alternativas y re-ejecución de `validate.py` pendiente (B-T multi-probe-null caso 19 + re-run assertion-protegida).

Para caso 26, reescribir en bloque nuevo "casos no-evaluables":

> **Caso 26 (Starlink).** `val_steps = 1`, CI bootstrap degenerado (`ci_lo = ci_hi = edi.value`), `p_perm = 1.0`. La métrica EDI carece de contenido estadístico bajo `val_steps = 1` y el CI bootstrap colapsado lo confirma. Se reclasifica como **exploratorio no-evaluable**: no admite inferencia. Acción pendiente: verificar viabilidad de extender el split temporal a `val_steps ≥ 8`; si el dataset real no lo admite, reclasificar a null por insuficiencia de datos (cf. F4-AU1).

**Eliminar el marcador asterisco "*" como nivel** en todas las tablas del cap 05-07; sustituirlo por marcadores operativos: `p < 0.05`, `p ≥ 0.05`, `n.e.` (no-evaluable). El nivel "Trend con cautela inferencial" no se sostiene como categoría — colapsa a "exploratorio sin significancia".

**Nota propuesta para los tres trend restantes (10 Justicia, 28 Fuga cerebros, 01 Clima):** todos tienen `p_perm ≥ α`. Si Jacob acepta que la categoría "Trend" tenga sentido sólo bajo significancia genuina, el bloque entero pierde miembros y debe renombrarse "**exploratorios sin significancia estadística**" o disolverse en Null.

## Texto a reemplazar / propagar

- Eliminar caso 26 de Tabla 5.7.7 (Trend), línea 124. Crear bloque "Exploratorio no-evaluable" o reportar en nota separada.
- Eliminar caso 19 de Tabla 5.7.8 (Null con asterisco), línea 140. Reescribir como null por tendencia espuria sin asterisco; pendiente la re-ejecución de TENG-05.
- Recalcular conteos del corpus en cap 05 y 06: si previamente había "4 trend", ahora 2 (si Jacob mantiene 10/28/01) o cero (si Jacob acepta que la categoría completa carece de discriminación estadística).
- Coordinar con F4-AU1 (Starlink en cuarentena) y F4-TENG-05 (re-ejecución de caso 19).

## Costo argumentativo declarado

- **Concesión 1.** El conteo del corpus se reduce en al menos 2 casos en "Trend o superior".
- **Concesión 2.** El nivel "Trend (Nivel 1)" pierde dos miembros y expone que la categoría completa puede carecer de discriminación estadística genuina (todos los Trend restantes tienen `p ≥ α`). Posible necesidad de disolver el bloque o renombrarlo "exploratorios sin significancia".
- **Concesión 3.** El caso 19 había servido como gancho narrativo en cap 05-02 (acidificación → biología). Reclasificarlo obliga a reescribir el gancho o sustituirlo por un caso publicado de regime shift (Scheffer) como ya está propuesto en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:179`.
- **Beneficio.** El aparato gana defensibilidad bajo crítica tipo Ioannidis: separa tamaño de efecto (EDI) de significancia (p). El precio es admitir que sólo los Bloques I-IV (Strong / Strong sin gate / Weak / Suggestive) sostienen la tesis empíricamente; Trend / Null no son gradiente sino discontinuidad.
