---
title: "Histórico — notas iter 13/15/17 retiradas de versiones-cortas-defensa.md"
fecha: 2026-05-17
origen: 06-cierre/_extendido/versiones-cortas-defensa.md
motivo: limpieza final pre-defensa; el archivo principal queda con cifras finales sin changelog acumulado
---

# Histórico de capas iter 13 / iter 15 / iter 17 retiradas

Se preservan aquí las notas iter X que se acumularon en §2 (versión 5 min) y §3.7 (versión 15 min) durante el loop nocturno B-T2 / B-T2.1. La versión depurada del archivo conserva sólo cifras finales y la mención breve "el aparato declara falsificación local en 4 casos (honestidad metodológica)".

## §2 (5 min) — "Justificación operativa (40 casos)" — nota retirada

> **Corrección honesta iter 13 (cross-reference, BORRADOR-IA pendiente H-J12).** La sección abajo está en formulación previa al fix del bug `detrended_edi`. Conteo operativo actual: **1 Strong robusto definitivo (24 Microplásticos) + [0..3] en revisión (04, 20, 22)**. **Iter 15: 5 inversiones de signo adicionales detectadas (09, 12, 14, 27 + 23 rescate); el bug afectaba 11 casos en total, no solo los 6 upgrades B-T2 — caso 09 Finanzas sale de Weak (+0.103→-0.002), caso 27 Riesgo Biológico sale de Strong gate completo (+0.216→-0.002).** Detalle empírico íntegro en **cap 06-01 §5 Tabla 6.1.1 Nota iter 13/iter 15**.

Capas iter dentro del bloque inter-dominio (5 min):

- "6 casos strong validados con gate completo (post-iter-7 B-T2 2026-05-17)" — fechado iter 7.
- "caso 18 promovido iter 5 B-T2 con datos World Bank reales".
- "caso 24 promovido Strong-sin-gate→gate completo iter 7 B-T2 con datos Jambeck reales".
- "caso 26 promovido Trend→Strong-sin-gate iter 7 B-T2 con CI bootstrap estable [0.741, 0.775]".
- "caso 09 Finanzas promovido Suggestive→Weak iter 5 B-T2 con yfinance + FRED reales".
- "caso 17 Océanos promovido Null/rechazado-por-gate→Weak iter 7 B-T2".
- "Wikipedia retirado iter 8 → Null tras pre-registro firmado".
- "Justicia (caso 10 reclasificado Trend→Suggestive Nivel 2 iter 8 B-T2 ...)".

## §3.7 (15 min) — "Cartografía agregada inter-dominio + inter-escala" — nota retirada

> **Corrección honesta iter 13 (cross-reference, BORRADOR-IA pendiente H-J12).** El bloque siguiente está en formulación previa al fix. Conteo operativo actual: **Strong robusto definitivo = 1 (caso 24 Microplásticos) + [0..3] en revisión urgente (04, 20, 22)**; reclasificados 4 a NULL/Weak por bug de tendencia (16, 17, 18, 21) + 2 a Weak por fallo block-perm (26, 30). El "6 strong con gate completo" del manuscrito iter 11 era artefacto de tendencia + permutación iid inadecuada. **Ampliación iter 15 `[BORRADOR-IA pendiente firma H-J12]`:** re-ejecución 16 casos post-fix detecta **5 inversiones de signo adicionales bajo detrended honesto (09 Finanzas raw=+0.103→-0.002 Weak→Null; 12 Paradigmas raw=-0.172→+0.043 sigue Null con signo opuesto; 14 Postverdad raw=+0.002→-0.0004 trivial; 27 Riesgo Biológico raw=+0.216→-0.002 sale de Strong gate completo, alinea con costo declarado del agregador `overall_pass` por CI bootstrap cruzando cero) + 1 rescate (23 Erosión dialéctica raw=-1.0→detrended=-0.023, sigue null/falsificación local pero dos órdenes menos extremo) — el bug afectaba 11 casos en total, no solo los 6 upgrades B-T2 inicialmente re-ejecutados iter 13**. Detalle empírico íntegro en **cap 06-01 §5 Tabla 6.1.1 Nota iter 13/iter 15 + §4.5 deuda B-T2.1**. Lectura honesta: el aparato detecta su propio bug y reclasifica sin proteger su narrativa previa.

Capas iter dentro del corpus inter-dominio (15 min):

- "caso 18 promovido Weak→Strong iter 5 B-T2 ... EDI=0.3366, p_perm=0.0, CI=[0.331, 0.347]".
- "caso 24 promovido Strong-sin-gate→Strong gate completo iter 7 B-T2 ... EDI=0.806, p_perm=0.0, CI=[0.701, 0.880]".
- "caso 26 promovido Trend→Strong sin gate iter 7 B-T2 ... EDI=0.7575, p_perm=0.0, CI bootstrap [0.741, 0.775]".
- "caso 09 promovido Suggestive→Weak iter 5 B-T2 ... EDI=0.1027, p_perm=0.0, CI=[0.1006, 0.1052]".
- "caso 17 promovido Null/rechazado-por-gate→Weak iter 7 B-T2 ... EDI=0.1902, CI=[0.157, 0.280], `valid=False`".
- "Wikipedia retirado iter 8 → Null genuino tras pre-registro firmado con DISCREPANCIA honesta".
- "caso 10 reclasificado Trend→Suggestive Nivel 2 iter 8 B-T2 ... EDI=0.0579, p_perm=0.017".
- "caso 13 reclasificado Weak→Trend tras re-ejecución iter 4 B-T2 ... EDI=0.0821, p_perm=0.162".
- "caso 11 confirmado Trend tras re-ejecución iter 4 B-T2 ... EDI=0.0599, p_perm=0.922".
- "Justicia retirado iter 8 a Suggestive Nivel 2. Starlink retirado iter 7 a Strong sin gate. Fuga de cerebros retirada iter 9 a Null genuino".
- "Nota iter 8 pre-registro firmado 2026-05-17: ... Gelman & Loken 2014".
- "Nota iter 9 pre-registro firmado VALIDADO 2026-05-17 (segundo bloque pre-registrado): ... 21 Salinización, 28 Fuga cerebros, 23 Erosión dialéctica ... Null real confirmado para 21 (EDI=0.0184) y 28 (EDI=0.030), Falsificación local del aparato CONFIRMADA EXACTA para 23 (EDI=-1.000 EXACTO)".
- "Nota iter 7 calibración bidireccional consolidada 2026-05-17: ... downgrades (01, 03, 10, 11, 13, 15) como upgrades (09, 17, 18, 22, 24, 26); el aparato modula en ambas direcciones".
- "Bloque \"null\" subdividido (AU-9, actualizado iter 9 con casos 15 Wikipedia + 21 Salinización + 28 Fuga cerebros pre-registrados)" + detalle por caso (Conciencia confirmado iter 7, Clima reclasificado Trend→Null, Contaminación reclasificado Weak→Null iter 3, Wikipedia caso 15 iter 8, Salinización caso 21 iter 9, Fuga de cerebros caso 28 iter 9, Acidificación caso 19 iter 4, Erosión dialéctica caso 23 reubicado iter 9).
- "Océanos promovido iter 7 a Weak con disclosure".
- "caso 16 Deforestación re-ejecutado con datos World Bank descargados en vivo, EDI=0.580 vs referencia 0.602".

## Síntesis para defensa

Lo que queda en la prosa depurada (cifras finales, sin changelog):

- 6 strong con gate completo, 1 strong sin gate, 6 weak con disclosure, 1 suggestive, 2 trend, 9 null genuinos, 1 EDI fuertemente negativo por sonda inadecuada, 2 falsificación local del aparato, 0 rechazados por gate, 3 controles correctamente rechazados (inter-dominio 30 casos).
- 7 strong / 1 weak / 2 null (inter-escala 10 casos).
- Mención única: "el aparato declara falsificación local en 4 casos (honestidad metodológica)" — sin detalle por iter.

El changelog operativo iter-a-iter vive aquí y en `cap 06-01 §5 Tabla 6.1.1 Notas iter`. La defensa oral no necesita reproducir ese rastro.
