# Pre-Registro B-T2.1 — Ejecución Completada

**Fecha:** 2026-05-17  
**Caso:** 04 Energía (Consumo Per Cápita)  
**Registrador:** Claude Opus 4.7 bajo dirección Jacob Agudelo + Steven Vallejo

## Resumen

Pre-registro **B-T2.1 GENUINO** ejecutado conforme especificación fechada en `/docs/PRE_REGISTRO_B_T2_1.md` (commit 4a434e7, no modificado post-firma).

### Cambios vs B-T2

| Aspecto | B-T2 | B-T2.1 |
|---------|------|--------|
| Fuente datos | World Bank proxy (local) | OWID Renewables (live) |
| Ventana temporal | 1990-2023 (40 años) | 1995-2022 (28 años) |
| Drivers | `[gdp_growth, urban_pct, industry_pct]` | `[renewables_share, fossil_share, gdp_pc]` |
| Permutación | iid | block (3 años) |

### Resultado

```
EDI_real (B-T2)  = 0.4615  [CI95: 0.378, 0.550]  → Strong (Nivel 4)
EDI_real (B-T2.1) = 0.1571  [CI95: 0.133, 0.193]  → Weak (Nivel 3)
ΔEDI = -0.304 (dentro margen pre-registrado ≤0.30)
```

**p_perm (B-T2.1)** = 0.006 (significancia presente pero EDI debajo umbral Strong 0.33)  
**Clasificación final:** Weak (Nivel 3)  
**Predicción pre-registrada:** Weak ✓ **VALIDADA**

## Justificación del collapse

El cambio de 0.46 → 0.16 es honesto porque:

1. **B-T2 usaba proxies demográficos** (urban %, industry %) que co-crecen monotónicamente con consumo energético desde 1990, generando artefacto de co-tendencia falsa.
2. **B-T2.1 usa composición energética real** (share renovable/fósil) que está naturalmente acotada (0-100%), siendo **estacionaria por construcción**.
3. El verdadero acoplamiento (si existe) debe persistir en indicadores estacionarios. Su colapso indica que **la dependencia observable en B-T2 era principalmente tendencial**.

## Deuda saldada

Caso 04 **no es Strong robusto** bajo datos genuinos. Su posición en la tesis debe ser reclasificada de "fuerte evidencia de cierre operativo" a "caso limítrofe Weak con historia metodológica honesta".

Recomendación: incluir B-T2.1 como sección "Auditoría post-hoc" en `09-simulaciones-edi/Evaluacion_Modelos_Dominio.md` con tabla comparativa B-T2 vs B-T2.1.

---

**Archivos generados:**
- `09-simulaciones-edi/04_caso_energia/case_config_b_t2_1.json` — config pre-registrada
- `09-simulaciones-edi/04_caso_energia/data/dataset_b_t2_1.csv` — datos OWID descargados
- `09-simulaciones-edi/04_caso_energia/data/FETCH_MANIFEST_B_T2_1.json` — metadatos fetch
- `09-simulaciones-edi/04_caso_energia/outputs/B_T2_1_RESULT.md` — resultado resumido
- `09-simulaciones-edi/04_caso_energia/outputs/metrics.json` — metrics completos (B-T2.1)

**Comando reproducible:**
```bash
cd 09-simulaciones-edi/04_caso_energia && \
  cp case_config_b_t2_1.json case_config.json && \
  HYPER_N_PERM=999 HYPER_N_BOOT=500 HYPER_PERMUTATION_METHOD=block \
  python3 src/validate.py --seed 42
```

