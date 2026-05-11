---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 05-aplicaciones/07-mapa-aplicaciones-corpus.md:17 (Tabla 5.7.1)
hallazgo: Bitacora/2026-05-04-continuous-run/F05-09-edi-negativo-cuenta-como-demostrativo.md
tipo: edicion_textual_minima + nota_taxonomia (coordinada con F4-F05-08)
---

## Diagnóstico

La línea 17 de `05-aplicaciones/07-mapa-aplicaciones-corpus.md` rotula los 30 casos del corpus inter-dominio como "Modo demostrativo (con dossier completo)" sin separar por signo del EDI ni por significancia estadística. Esto pone bajo la misma etiqueta casos `overall_pass=True` con `EDI > 0.30`, casos null con `EDI < 0` y `p ≈ 1`, y controles de falsación que la tesis declaró que **debían** fallar. "Demostrativo" en CLAUDE.md y en el glosario operativo connota *caso que instancia operativamente el aparato con éxito*; un EDI < 0 con `p ≈ 1` NO instancia el aparato. La equivocidad léxica oculta el costo argumentativo y debilita la fuerza de los casos genuinamente positivos.

## Verificación

- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:17` — texto literal: "Modo demostrativo (con dossier completo): 30 casos".
- Tabla 5.7.1 suma: 4 strong + 1 strong sin gate + 8 weak + 2 suggestive + 4 trend + 8 null + 3 controles = 30 (verificado).
- Los 8 nulls incluyen casos con `EDI < 0`: 02 (-0.116), 03 (-0.090), 12 (-0.144), 23 (-1.00), 25 (-0.146), 29 (-0.876) — listados literalmente en la sección Null de la tabla. Casos como 23 (-1.00) y 29 (-0.876) indican **degradación predictiva tras desacoplar**, no acoplamiento detectable. (Nota: la cifra "-0.876" del caso 29 contradice parcialmente el reporte adversarial original — ver F4-AU9 para la subdivisión taxonómica completa.)

## Texto propuesto (voz autoral filosófica de Jacob)

**Edición textual mínima en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:17`:**

> *Antes:* "Modo demostrativo (con dossier completo): 30 casos"
>
> *Después:* "**Modo técnico-ejecutado** (dossier técnico completo, `metrics.json` reproducible bajo C1-C5): 30 casos. El rótulo 'demostrativo' se reserva para el caso paradigmático del cap 05-05 (Warren) que cumple los 14 componentes del dossier de anclaje del cap 05-00 §1 con material publicado independiente del aparato; el resto del corpus opera en modo técnico-ejecutado y se desglosa en las Tablas 5.7.2–5.7.8 según el resultado empírico (strong, weak, suggestive, trend, null, control). Casos con `EDI ≤ 0` o `p ≈ 1` están listados explícitamente en sus bloques correspondientes y **no se contabilizan como instancia positiva del aparato**, sino como casos de no-aplicabilidad de la sonda, falsación local o controles correctamente rechazados."

**Añadir nota bajo Tabla 5.7.1:**

> *Nota.* 'Dossier técnico completo' indica que el caso fue ejecutado con el protocolo C1-C5 y produce `metrics.json` reproducible. NO equivale a 'demostración positiva del aparato': los Bloques V-VII de la enumeración (4 trend + 8 null + 3 controles, 15 casos en total) **no instancian acoplamiento detectable**. Funcionan como evidencia adicional de discriminación: el aparato no inventa EDI alto cuando no hay acoplamiento real, los nulls genuinos confirman la batería como filtro, los controles diseñados rechazan por construcción. La fuerza inferencial real del corpus inter-dominio descansa sobre los Bloques I–IV (Strong, Strong sin gate, Weak, Suggestive — del orden de 15 casos según los conteos canónicos vigentes), no sobre la cifra agregada N=30 indistinta.

## Texto a reemplazar

- Sustituir la línea 17 actual por la nueva formulación.
- Añadir la nota bajo Tabla 5.7.1.
- **Coordinación con F4-F05-08:** ambos borradores convergen en la misma corrección textual. Aplicar como pasada única.

## Costo argumentativo declarado

- La cifra retórica "30 demostrativos" baja a "15-19 casos con instancia positiva del aparato + 3 controles diseñados + 8 nulls + 4 trend" (cifras exactas dependen de la reclasificación coordinada con F4-AU9, F4-AU4, F4-F05-10).
- Esto es **honestidad metodológica, no debilidad** (CLAUDE.md §7). La fuerza inferencial real del corpus no depende de N=30 indistinto sino de la heterogeneidad de dominios donde EDI > 0 con `p < 0.05` aparece (15 casos en física, ecología, epidemiología, sociopolítico, técnico), el éxito 3/3 de controles diseñados y la existencia documentada de 8 nulls que operan como discriminación.
- El costo de NO corregir es mayor: la equivocidad léxica queda como flanco abierto a la crítica de que "demostrativo" enmascara falsaciones, lo que invalidaría la cifra del 50 % de señal significativa al hacerla parecer underselling de un dataset 100 % exitoso.
