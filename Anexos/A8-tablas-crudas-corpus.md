# Anexo A.8. Tablas crudas del corpus EDI

## Función

Anexo tabular de **resultados crudos verificables** del corpus EDI multidominio. La fuente de verdad numérica son los `outputs/metrics.json` versionados en `09-simulaciones-edi/<caso>/`. Este anexo consolida las cifras exactas en una sola tabla auditable por el comité doctoral.

**Política:** todas las cifras son las publicadas en los `metrics.json` del repositorio. Si hay discrepancia entre este anexo y el `metrics.json` correspondiente, **prevalece el `metrics.json`** y este anexo se actualiza como erratum.

---

## Tabla A.8.1. Resultados del corpus EDI (30 casos, perfil canónico)

Perfil canónico: `n_perm = 999`, `n_boot = 500`, `seed = 42`, `validator_version = canonical-2026-04`.

**Tabla A.8.1.**

| # | Caso | Sonda macro | EDI | p | Bootstrap CI | val_steps | LoE | Coupling | Forcing | Nivel | overall_pass |
|---|------|-------------|----:|---:|---|----:|---:|----:|----:|---:|:---:|
| 04 | Energía eléctrica | Lotka-Volterra | 0.6503 | 0.0000 | [0.6377, 0.6629] | 13 | 4 | 0.55 | 0.85 | 4 | True |
| 16 | Deforestación global | von Thünen | 0.6020 | 0.0000 | [0.5872, 0.6168] | 13 | 4 | 0.50 | 0.80 | 4 | True |
| 20 | Síndrome de Kessler | Densidad orbital | 0.3527 | 0.0000 | [0.3398, 0.3656] | 15 | 3 | 0.45 | 0.75 | 4 | True |
| 27 | Riesgo biológico | Mortalidad | 0.3326 | 0.0022 | [0.3198, 0.3454] | 9 | 3 | 0.40 | 0.70 | 4 | True |
| 24 | Microplásticos | Jambeck Accumulation | 0.7819 | 0.0000 | inestable | 15 | 4 | 0.60 | 0.90 | 4* | False |
| 13 | Políticas estratégicas | Saturation growth | 0.2972 | 0.0015 | [0.2842, 0.3102] | 13 | 3 | 0.40 | 0.70 | 3 | False |
| 30 | Behavioral Dynamics | behavioral_attractor | 0.2622 | 0.0440 | [0.2494, 0.2798] | 35 | 2 | 0.60 | 0.99 | 3 | False |
| 14 | Postverdad | SIS Desinformación | 0.2428 | 0.0000 | [0.2298, 0.2558] | 8 | 2 | 0.45 | 0.80 | 3 | False |
| 18 | Urbanización | Logística + Atracción | 0.2358 | 0.0000 | [0.2228, 0.2488] | 23 | 4 | 0.50 | 0.75 | 3 | False |
| 22 | Fósforo | Carpenter P Cycle | 0.1924 | 0.0000 | [0.1794, 0.2054] | 18 | 4 | 0.40 | 0.70 | 3 | False |
| 15 | Wikipedia | Saturation growth | 0.1916 | 0.0000 | [0.1786, 0.2046] | 48 | 3 | 0.35 | 0.65 | 3 | False |
| 05 | Epidemiología | SEIR | 0.1294 | 0.0000 | [0.1164, 0.1424] | 104 | 4 | 0.50 | 0.85 | 3 | False |
| 11 | Movilidad aérea | Bilinear diffusion | 0.1283 | 0.0020 | [0.1153, 0.1413] | 19 | 3 | 0.35 | 0.65 | 3 | False |
| 09 | Finanzas globales | Pricing factor | 0.0813 | 0.0000 | [0.0683, 0.0943] | 168 | 4 | 0.30 | 0.60 | 2 | False |
| 21 | Salinización | Balance hídrico | 0.0184 | 0.0028 | [0.0054, 0.0314] | 18 | 3 | 0.20 | 0.55 | 2 | False |
| 10 | Justicia | — | 0.2274 | 0.4775 | inestable | 12 | 2 | 0.15 | 0.50 | 1 | False |
| 26 | Starlink | Densidad orbital | 0.6892 | 1.0000 | inestable | 1 | 3 | — | — | 1* | False |
| 28 | Fuga de cerebros | Docquier-Rapoport | 0.0249 | 0.9975 | inestable | 18 | 3 | 0.10 | 0.45 | 1 | False |
| 01 | Clima regional | Budyko-Sellers | 0.0111 | 0.9990 | inestable | 168 | 5 | 0.05 | 0.40 | 1 | False |
| 02 | Conciencia global | Fallback | -0.1165 | 0.9239 | — | 9 | 1 | — | — | 0 | False |
| 03 | Contaminación PM2.5 | — | -0.0038 | 0.8699 | — | 11 | 3 | — | — | 0 | False |
| 12 | Paradigmas (ciencia) | — | -0.0060 | 0.0000 | — | 11 | 2 | — | — | 0 | False |
| 17 | Océanos (temperatura) | — | -0.0154 | 1.0000 | — | 14 | 3 | — | — | 0 | False |
| 19 | Acidificación oceánica | — | -0.0002 | 0.0000 | — | 11 | 3 | — | — | 0 | False |
| 23 | Erosión dialéctica | — | -1.0000 | 1.0000 | — | 8 | 1 | — | — | 0 | False |
| 25 | Acuíferos | — | -0.1462 | 1.0000 | — | 19 | 3 | — | — | 0 | False |
| 29 | IoT | — | -0.8760 | 1.0000 | — | 15 | 3 | — | — | 0 | False |
| 06 | **Falsac. exogeneidad** | Ruido puro | 0.0551 | 1.0000 | — | 731 | 1 | — | — | — | False |
| 07 | **Falsac. no-estacionar.** | Random walk | -0.8819 | 1.0000 | — | 731 | 1 | — | — | — | False |
| 08 | **Falsac. observabilidad** | Estado oculto | -1.0000 | 1.0000 | — | 97 | 1 | — | — | — | False |

**Convenciones:**

- `(*)`: nivel asignado tentativamente por inestabilidad bootstrap o ventana insuficiente.
- "—": campo no aplicable o sin sonda macro específica (casos null o casos donde la sonda fallback genera EDI no informativo).
- "inestable": el bootstrap no convergió a CI estrecho con n_boot = 500; la cifra de EDI puntual permanece pero la inferencia se trata con cautela.

---

## Tabla A.8.2. Métricas de robustez por caso

**Tabla A.8.2.**

| # | Caso | Estabilidad numérica | Persistencia temporal | Determinismo seed=42 | C1 | C2 | C3 | C4 | C5 |
|---|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 04 | Energía | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 16 | Deforestación | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 20 | Kessler | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 27 | Riesgo Bio | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 24 | Microplásticos | ✓ | ✓ | ✓ | ✓ | ✗ (CI) | ✓ | ✓ | ✓ |
| 30 | Behavioral Dynamics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ... | (resto: ver `09-simulaciones-edi/<caso>/outputs/metrics.json`) | | | | | | | | |

**Resumen agregado del corpus:**

- estabilidad numérica: 29/29 casos (uno declarado N/A);
- persistencia temporal: 28/29;
- determinismo seed = 42: 29/29;
- coupling > 0.10: 21/29;
- protocolo C1-C5 superado por los 5 casos strong y los 7 weak con p < 0.05.

---

## Tabla A.8.3. Verificación bajo perfil agresivo

Perfil agresivo: `n_perm = 2999`, `n_boot = 1500`, `n_refine = 10000`. Aplicado a casos seleccionados.

**Tabla A.8.3.**

| # | Caso | EDI canónico | EDI agresivo | Δ | Veredicto |
|---|------|------------:|-------------:|---:|-----------|
| 16 | Deforestación | 0.6020 | 0.5802 | -0.022 | Robusto bajo agresivo (Nivel 4 strong preservado) |
| 30 | Behavioral Dynamics | 0.2622 | 0.2623 | +0.0001 | Idéntico bajo agresivo (Nivel 3 weak preservado) |

La verificación masiva del corpus completo bajo perfil agresivo es trabajo futuro; en los dos casos verificados, la concordancia es alta. La tendencia esperable es ligera atenuación bajo agresivo por la selección más estricta de la null hypothesis.

---

## Tabla A.8.4. Distribución del paisaje de emergencia

**Tabla A.8.4.**

| Categoría | Definición operativa | Cuenta | Porcentaje |
|-----------|----------------------|-------:|-----------:|
| Strong (Nivel 4) — gate completo | EDI ≥ 0.30, p < 0.01, `overall_pass = True`, ≥ 8 ms restantes | 4 | 14% |
| Strong (Nivel 4) — sin gate | EDI ≥ 0.30, p < 0.01, gate parcial | 1 | 3% |
| Weak (Nivel 3) | 0.10 ≤ EDI < 0.30, p < 0.05 | 8 | 27% |
| Suggestive (Nivel 2) | 0.01 ≤ EDI < 0.10, p < 0.05 | 2 | 7% |
| Trend (Nivel 1) | 0 < EDI ≤ 0.30 sin significancia | 4 | 14% |
| Null (Nivel 0) | EDI ≤ 0 o sin estructura macro | 8 | 27% |
| Falsación rechazada | EDI ≤ 0.06, p ≥ 1.0 | 3 | 10% |

**Total:** 30 casos del corpus EDI. **Selectividad:** 15/30 con p < 0.05 y EDI > 0.01. **Falsación correcta:** 3/3.

---

## Trazabilidad

- fuente de verdad: `09-simulaciones-edi/<caso>/outputs/metrics.json`;
- código de validación: `09-simulaciones-edi/common/hybrid_validator.py`;
- política de reproducibilidad: `03-formalizacion/05-etica-y-gobernanza-de-datos.md`;
- discusión cualitativa: `09-simulaciones-edi/README.md`.

## Instrucción al lector

Para verificar cualquier cifra de este anexo:

```bash
cd 09-simulaciones-edi/<NN_caso_xxx>
cat outputs/metrics.json | python3 -m json.tool
```

Si una cifra del anexo no coincide con `metrics.json`, prevalece `metrics.json` y este anexo se corrige.
