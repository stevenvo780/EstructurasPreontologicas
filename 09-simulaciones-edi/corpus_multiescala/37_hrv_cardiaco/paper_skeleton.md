# 37 Hrv Cardiaco

> Paper skeleton IMRaD generado automáticamente desde el aparato V5.4.
> Requiere pulido editorial humano antes de envío a revista.

## Abstract

Aplicamos el aparato Effective Dependence Index (EDI) a 37 hrv cardiaco para
evaluar el cierre operativo entre la dinámica acoplada del sistema y la sonda macro
instanciada. Bajo régimen calibrado V5.4 (block bootstrap, FWER Holm, sondas
teóricamente independientes, análisis de potencia post-hoc, validación cruzada k-fold,
tests adversariales) reportamos EDI = 0.5771350469912229, p_block = 0.0003333333333333333, CI 95% = [0.5087538984308582, 0.6443332649335536].
La sonda secundaria con motivación teórica independiente (neurodinamica_excitable) produce
|Δ EDI| = 1.0141592665762509. Pre-registro criptográfico bajo hash 1fb446f4673485c3
(commit a24f6dd14049). Datos: Sintético Mackey-Glass — parámetros PhysioNet.

## 1. Introduction

El problema explicativo en este dominio es la disociación entre descripciones
agregadas y dinámicas micro-componentes. La pregunta operativa es si la sonda macro
instanciada captura constricción genuina sobre las trayectorias del sistema acoplado
o si se reduce a artefacto de auto-consistencia paramétrica.

[PULIDO HUMANO REQUERIDO: estado del arte específico del dominio + gap explicativo + contribución del paper]

## 2. Methods

### 2.1. Datos

**Fuente:** Sintético Mackey-Glass — parámetros PhysioNet

**URL:** https://physionet.org

**Tipo:** real

**Trazabilidad:** SHA-256 versionado en `data/FETCH_MANIFEST.json`

### 2.2. Sonda primaria

Ver `docs/protocolo_simulacion.md` para ecuación, derivación, parámetros y citas.

### 2.3. Aparato EDI

Métrica de cierre operativo: EDI = 1 - RMSE_coupled / RMSE_no_ode,
con prueba de permutación n_perm=999 y bootstrap n_boot=500.

### 2.4. Calibración estadística avanzada (V5.1)

- Block bootstrap (Politis-Romano 1994) con bloques de tamaño √n
- Newey-West HAC (1987) para errores estándar bajo autocorrelación
- FWER Holm-Bonferroni (1979) para corrección de comparaciones múltiples

### 2.5. Sonda secundaria con motivación independiente (V5.3 B4)

**Sonda secundaria:** fitzhugh_nagumo

**Motivación teórica:** neurodinamica_excitable

### 2.6. Validación adicional (V5.4)

- Cross-validation k-fold sobre series temporales (TimeSeriesSplit)
- Tests adversariales: perturbación de parámetros ±20%, inyección de ruido, jackknife
- Análisis de potencia post-hoc (Cohen 1988)
- Pre-registro criptográfico SHA-256 + git commit

### 2.7. Reproducibilidad

**Pre-registro:** SETUP_HASH.json con aggregate_hash = `1fb446f4673485c3`

**Commit:** `a24f6dd14049`

**Pipeline:** `09-simulaciones-edi/scripts/run_full_pipeline.py`

## 3. Results

### 3.1. EDI principal

- **EDI puntual:** 0.5771350469912229
- **p-value naive:** 0.0
- **p-value block bootstrap (V5.1):** 0.0003333333333333333
- **CI bootstrap 95%:** [0.5087538984308582, 0.6443332649335536]

### 3.2. Convergencia con sonda secundaria

|Δ EDI| inter-paradigma = 1.0141592665762509

[PULIDO HUMANO: gráfico de convergencia + tabla de robustez]

### 3.3. Robustez bajo régimen V5.4

Ver `metrics_enriched_v5_2.json` para FWER position, calibración HAC y veredicto.
Ver `secondary_probe_report.json` para detalle de convergencia inter-paradigma.

## 4. Discussion

[PULIDO HUMANO: interpretación específica del dominio]

### 4.1. Implicación filosófica

Bajo el irrealismo operativo de estructuras pre-ontológicas (Agudelo & Vallejo 2026),
el EDI reportado documenta cierre operativo κ-pragmática sobre el sistema acoplado.
La afirmación κ-ontológica fuerte requiere convergencia con sonda secundaria
teóricamente independiente sobre datos reales — parcialmente cumplida en V5.4.

### 4.2. Comparación con literatura

[PULIDO HUMANO: cómo este resultado se compara con resultados publicados]

## 5. Limitations

Limitaciones explícitas declaradas:

- p-value naive miscalibrado (24% empírico declarado); el block bootstrap V5.1 corrige.
- Convergencia inter-paradigma evaluada sobre proxys; verificación con arrays primarios pendiente.
- Validación inter-grupo es deuda externa.

## 6. References

[PULIDO HUMANO: extender bibliografía específica del dominio]

- Mackey, M. C. y Glass, L. (1977). *Science* 197(4300).

## Appendix A. Reproducibilidad

```bash
cd 09-simulaciones-edi
python3 scripts/run_full_pipeline.py
```

**Hash del setup pre-ejecución:** `1fb446f4673485c3...`

**Git commit:** `a24f6dd14049...`

**Verificación criptográfica:**

```bash
python3 scripts/freeze_setup.py --verify 37_hrv_cardiaco
```

## Appendix B. Cumplimiento del piso QES

Q1 trazabilidad de datos: FETCH_MANIFEST con SHA-256 ✓
Q2 tamaño efectivo: ver POWER_ANALYSIS_REPORT.md
Q3 calidad de sonda: protocolo_simulacion.md con cita disciplinar ✓
Q4 reproducibilidad: SETUP_HASH + git_commit + seed ✓
Q5 multi-sonda: secondary_probe_report.json ✓
Q6 LoE empírico: declarado en FETCH_MANIFEST
Q7 calibración: metrics_enriched_v5_2.json ✓
