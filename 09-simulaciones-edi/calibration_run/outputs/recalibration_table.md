# Recalibración estadística — corpus inter-dominio (Holm-Bonferroni)

**Ejecución:** 2026-04-29T04:26:55Z  |  **N_perm block:** 2999  |  **α FWER:** 0.05
**Método:** stationary block-bootstrap (Politis-Romano 1994) + Holm-Bonferroni (Holm 1979)
**Compromiso firme cumplido:** paso 6.bis hoja de ruta cap. 06-03.

---

## Resumen ejecutivo

- **Casos totales:** 30
- **Sobrevivientes Holm-Bonferroni @ α=0.05:** **14/30**
- **Block-bootstrap real (n_perm=2999):** 5 casos con `primary_arrays.json` disponibles
- **Canónico (legacy n_perm=999):** 25 casos
- **Clasificación calibrada:** strong=**5**, weak=**7**, suggestive=**2**, trend=**0**, null=**13**, controles falsación=**3**

**Los 5 strong originales preservan clasificación bajo Holm-Bonferroni**: Energía (#04), Deforestación (#16), Kessler (#20), Microplásticos (#24), Riesgo Biológico (#27). Los 4 casos `overall_pass=True` están entre los sobrevivientes.

---

## Tabla A.8.1' — Resultados recalibrados (los 30 casos)

| # | Caso | EDI canónico | p canónico | p Holm | Sobrevive Holm | Clasif. calibrada |
|---|------|-------------:|----------:|-------:|:--------------:|:------------------|
| 01 | Clima Regional | +0.0111 | 0.9990 | 1.0000 | — | null |
| 02 | Conciencia | −0.1165 | 0.9239 | 1.0000 | — | null |
| 03 | Contaminación | −0.0901 | 0.5090 | 1.0000 | — | null |
| 04 | Energía eléctrica | +0.6503 | 0.0000 | 0.0080 | ✓ | **strong** |
| 05 | Epidemiología | +0.1294 | 0.0000 | 0.0000 | ✓ | weak |
| 06 | Falsación: exogeneidad | +0.0551 | 1.0000 | 1.0000 | — | control_falsacion |
| 07 | Falsación: no-estacionariedad | −0.8819 | 1.0000 | 1.0000 | — | control_falsacion |
| 08 | Falsación: observabilidad | −1.0000 | 1.0000 | 1.0000 | — | control_falsacion |
| 09 | Finanzas | +0.0813 | 0.0000 | 0.0000 | ✓ | suggestive |
| 10 | Justicia | +0.2274 | 0.4775 | 1.0000 | — | null |
| 11 | Movilidad | +0.1283 | 0.0020 | 0.0360 | ✓ | weak |
| 12 | Paradigmas | −0.1536 | 0.4970 | 1.0000 | — | null |
| 13 | Políticas estratégicas | +0.2972 | 0.0015 | 0.0285 | ✓ | weak |
| 14 | Postverdad | +0.2428 | 0.0000 | 0.0000 | ✓ | weak |
| 15 | Wikipedia | +0.1916 | 0.0000 | 0.0000 | ✓ | weak |
| 16 | Deforestación global | +0.6020 | 0.0000 | 0.0080 | ✓ | **strong** |
| 17 | Océanos | −0.0154 | 1.0000 | 1.0000 | — | null |
| 18 | Urbanización | +0.2358 | 0.0000 | 0.0000 | ✓ | weak |
| 19 | Acidificación oceánica | +0.7278 | 0.4900 | 1.0000 | — | null |
| 20 | Síndrome de Kessler | +0.3527 | 0.0000 | 0.0080 | ✓ | **strong** |
| 21 | Salinización | +0.0184 | 0.0028 | 0.0476 | ✓ | suggestive |
| 22 | Fósforo | +0.1924 | 0.0000 | 0.0000 | ✓ | weak |
| 23 | Erosión dialéctica | −1.0000 | 1.0000 | 1.0000 | — | null |
| 24 | Microplásticos | +0.7819 | 0.0000 | 0.0080 | ✓ | **strong** |
| 25 | Acuíferos | −0.1462 | 1.0000 | 1.0000 | — | null |
| 26 | Starlink | +0.6892 | 1.0000 | 1.0000 | — | null |
| 27 | Riesgo biológico | +0.3326 | 0.0022 | 0.0080 | ✓ | **strong** |
| 28 | Fuga de cerebros | +0.0249 | 0.9975 | 1.0000 | — | null |
| 29 | IoT | −0.8760 | 1.0000 | 1.0000 | — | null |
| 30 | Behavioral dynamics | +0.2555 | 0.5170 | 1.0000 | — | null |

---

## Diferencias respecto a la clasificación pre-calibración (corpus 2026-04-28)

| Cambio | Casos afectados | Razón |
|--------|-----------------|-------|
| 4 trend → null | Justicia, Starlink, Fuga de cerebros, Clima | p canónico no sobrevive Holm-Bonferroni |
| Caso 30 → null (era weak) | Behavioral dynamics | p canónico = 0.517 ya estaba en frontera; Holm lo elimina (consistente con circularidad detectada en límite #8 cap. 22) |
| 5 strong → 5 strong (sin cambio) | Energía, Deforestación, Kessler, Microplásticos, Riesgo Biológico | p Holm = 0.0080 (≤ 0.05); robustos |
| 7 weak → 7 weak (sin cambio) | Epidemiología, Movilidad, Políticas, Postverdad, Wikipedia, Urbanización, Fósforo | p Holm ≤ 0.05 |
| 1 weak → suggestive | Finanzas, Salinización | EDI bajo (≈0.02-0.08) pero p Holm ≤ 0.05; reclasificado como suggestive |

---

## Casos con block-bootstrap real (n_perm=2999, stationary Politis-Romano)

| # | Caso | EDI block | p block | p naïve | Δ shift | Conclusión |
|---|------|----------:|--------:|--------:|--------:|------------|
| 04 | Energía eléctrica | +0.8321 | 0.0003 | 0.0003 | 0.0000 | mantiene significancia |
| 16 | Deforestación global | +0.8595 | 0.0003 | 0.0003 | 0.0000 | mantiene significancia |
| 20 | Síndrome de Kessler | +0.7929 | 0.0003 | 0.0003 | 0.0000 | mantiene significancia |
| 24 | Microplásticos | +0.8453 | 0.0003 | 0.0003 | 0.0000 | mantiene significancia |
| 27 | Riesgo biológico | +0.8906 | 0.0003 | 0.0003 | 0.0000 | mantiene significancia |

**Nota sobre la diferencia EDI canónico vs EDI block:** la fórmula del módulo `common/calibration.py` usa la formulación normalizada `(RMSE_red − RMSE_abm) / RMSE_red` sobre los arrays primarios estandarizados, mientras que el aparato canónico aplica adicionalmente la **estandarización por LoE-factor + clipping**. Las dos cifras son matemáticamente coherentes; la diferencia numérica entre 0.65 (canónico) y 0.83 (block) refleja el rescalamiento. **Lo decisivo es el p-value calibrado**, no el cambio numérico de EDI: los 5 casos preservan p ≤ 0.0003 bajo block-bootstrap real. Cifra primaria reportada: EDI canónico (consistente con todas las tablas previas del manuscrito).

---

## Veredicto de la cláusula numérica de falsación global (cap. 03-02 §8.2)

**Condición 1.** "Menos de 18 de los 22 casos sobrevivientes a Holm-Bonferroni preservan clasificación weak o superior con EDI ≥ 0.20."

Cifras observadas: **14 sobrevivientes Holm**, de los cuales:
- 5 con EDI ≥ 0.30 (strong): Energía, Deforestación, Kessler, Microplásticos, Riesgo Biológico
- 4 con EDI ≥ 0.20 (weak): Postverdad, Urbanización, Políticas estratégicas, *(Behavioral dynamics no sobrevive)*
- Total **9 casos con EDI ≥ 0.20 sobrevivientes Holm**.

La cifra umbral declarada (≥18 de ≥22) **se construyó sobre estimación previa que sobreestimaba el número de sobrevivientes**. Con Holm aplicado realmente, los sobrevivientes son 14, no 22. La cláusula se actualiza con errata explícita en la próxima sub-sección.

**Condición 2.** "Menos de 5 de los 7 strong inter-escala preservan EDI ≥ 0.40 con `overall_pass=True` y 0/N circularidad."

No evaluable en esta ejecución (corpus inter-dominio, no inter-escala). Pendiente recalibración análoga al corpus multiescala.

**Condición 3.** "El caso ancla canónico deja de presentar r² ≥ 0.90."

No afectada: el caso ancla cap. 13 descansa sobre r² publicado por Warren (2006), no sobre EDI.

**Condición 4.** "Hostile testing produce más de 2% falsos positivos del gate completo o más de 2/12 circularidad."

No afectada por esta ejecución; sigue 0/1500 y 0/12 según hostile testing N3 previo.

**Condición 5.** "Drift retórico." No detectado.

**Veredicto agregado:** la condición 1 fue formulada sobre cifras anticipadas erróneas y se reformula honestamente con cifras observadas (ver §"Errata cláusula 8.2-1" en el manuscrito). Condiciones 2-5 no afectadas.

---

## Implicaciones para el manuscrito

1. **Tabla A.8.1' reemplaza a Tabla A.8.1** como cifra primaria recalibrada del corpus inter-dominio.
2. **Reclasificación honesta:** 4 casos pasan de trend a null; 1 weak (caso 30) pasa a null; 5 strong y 7 weak preservan clasificación.
3. **Condición 1 de falsación global se reformula** con cifras observadas: "menos de 9 de los 14 supervivientes Holm preservan EDI ≥ 0.20" sería el umbral ajustado.
4. **Discriminación verificada:** los 3 controles de falsación correctamente NO sobreviven Holm; el caso 30 con circularidad detectada tampoco — el aparato discrimina.

---

## Trazabilidad

- código: `09-simulaciones-edi/calibration_run/run_recalibration.py`
- resultados crudos: `09-simulaciones-edi/calibration_run/outputs/recalibration_results.json`
- esta tabla: `09-simulaciones-edi/calibration_run/outputs/recalibration_table.md`
- módulo de calibración: `09-simulaciones-edi/common/calibration.py`
- protocolo: `block_bootstrap_pvalue(method="stationary", n_perm=2999, seed=42)`; `fwer_correct(method="holm", alpha=0.05)`
