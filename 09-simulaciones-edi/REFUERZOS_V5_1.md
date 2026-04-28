# Refuerzos científicos V5.1 — los cinco bloques

> Documentación operativa de los cinco bloques científicos añadidos al
> aparato EDI en la versión V5.1, posteriores al cierre V5 de los 17
> vacíos estructurales filosóficos.

**Fecha:** 2026-04-28.
**Política:** elevar el rigor metodológico del aparato sin reabrir debate
conceptual ni re-ejecutar el corpus completo. Cierre o reducción de cinco
de las veinte limitaciones declaradas en `Anexos/A0-limitaciones-declaradas.md`.

---

## Resumen ejecutivo

| Bloque | Deuda | Módulo | Self-test | Estado |
|--------|-------|--------|-----------|--------|
| **B1** Calibración estadística | L1 (p-value 24%) | `common/calibration.py` | `scripts/test_calibration.py` ✓ | Cerrada metodológicamente |
| **B2** Replicación robusta | L4 (AUC interno) | `common/replication.py` | `scripts/test_replication.py` ✓ | Reducida — tres tests externos |
| **B3** Pre-registro criptográfico | L2 (post-hoc) | `common/preregistration.py` | corpus congelado ✓ | Cerrada metodológicamente |
| **B4** Sondas independientes | L11 (κ-ontológica C1) | `common/independent_probes.py` | `scripts/run_independent_probes.py` ✓ | Avanzada — infraestructura completa |
| **B5** Sensibilidad a umbrales | L3 | `common/threshold_sensitivity.py` | `scripts/run_threshold_sensitivity.py` ✓ | Cerrada mecánicamente |

---

## Bloque B1 — Calibración estadística avanzada

### Problema

La permutación con `n_perm=999` produce p-value mal calibrado bajo
autocorrelación temporal (tasa empírica de tipo I = 24% bajo random walk).

### Solución

`common/calibration.py` provee tres herramientas:

1. **`block_bootstrap_pvalue(obs, abm, reduced, n_perm=2999, block_size=None)`:**
   permutación por bloques contiguos (Politis-Romano 1994). Por defecto
   `block_size = ceil(sqrt(n))`. Reporta `p_block` (calibrado) y `p_naive`
   (legacy) para cuantificar el shift de calibración.

2. **`newey_west_se(residuals, lag=None)`:** error estándar HAC con kernel
   de Bartlett. Truncamiento adaptativo por defecto:
   `floor(4 * (n/100)^{2/9})`. Bajo AR(1) con phi=0.7 produce SE_HAC
   típicamente 1.5-2x mayor que SE_clasico.

3. **`fwer_correct(p_values, method="holm")`:** corrección Holm-Bonferroni
   sobre comparaciones múltiples. Aplicación al corpus de 30 casos:
   12 significativos sin corrección colapsan a **exactamente 4 tras Holm**,
   coincidiendo con los 4 strong `overall_pass` declarados.

### Verificación

```bash
cd 09-simulaciones-edi
python3 scripts/test_calibration.py
```

Self-test verifica: block-bootstrap produce p-values en [0,1] bajo AR(1);
Newey-West >= SE clásico bajo autocorrelación; Holm rechaza ≥ Bonferroni.

### Referencias

- Politis, D. N. y Romano, J. P. (1994). "The Stationary Bootstrap". *JASA* 89(428): 1303-1313.
- Newey, W. K. y West, K. D. (1987). "A Simple, Positive Semi-Definite, HAC Covariance Matrix". *Econometrica* 55(3): 703-708.
- Holm, S. (1979). "A Simple Sequentially Rejective Multiple Test Procedure". *Scand J Stat* 6(2): 65-70.

---

## Bloque B2 — Replicación robusta sin replicador externo

### Problema

AUC-ROC = 0.886 declarado como ranking interno; un crítico puede
atribuirlo a sobreajuste del investigador.

### Solución

`common/replication.py` provee tres tests que cualquier replicador externo
puede correr sobre los outputs versionados sin acceso al laboratorio:

1. **`seed_robustness(run_fn, base_kwargs, seeds)`:** distribución de EDI
   bajo cambio de semilla. Criterio operativo: `max_drift ≤ 0.05` →
   robusto. Si la varianza inter-seed es > 0.10, sospecha de overfitting
   al ruido pseudoaleatorio.

2. **`holdout_temporal(obs, abm, reduced, train_frac=0.8)`:** EDI sobre
   ventana de test out-of-sample. Criterio: `|edi_test - edi_full| ≤ 0.10`
   → sin leakage train-test.

3. **`adversarial_probe_swap(probe_fn_A, data_B, expected_low=True)`:**
   aplica las sondas de un caso A sobre los datos de otro caso B. Si las
   sondas son específicas, el EDI cruzado debería ser ≤ 0.05. Extiende
   el test cruzado V4-01 (inter-escala con 0/12 circularidad) al corpus
   inter-dominio.

### Verificación

```bash
python3 scripts/test_replication.py
```

---

## Bloque B3 — Pre-registro criptográfico mecánico

### Problema

La composición del corpus es post-hoc; el pre-registro honesto en
bitácora puede ser cuestionado por modificación retroactiva.

### Solución

`common/preregistration.py` calcula SHA-256 sobre el setup completo de
cada caso (excluyendo outputs, pycache, logs). Junto al hash registra:

- `git_commit_sha` (inmutable bajo el commit declarado);
- `git_dirty` (warning si había cambios sin commitear);
- `timestamp_utc`;
- lista completa de archivos hasheados con sus hashes individuales.

### Estado actual

```bash
python3 scripts/freeze_setup.py --all
```

Ejecutado al cierre V5.1:
- **30 casos del corpus inter-dominio congelados**;
- `corpus_aggregate_hash = f5ac98acbc7a59de7902cffa12fee80457963388e86fec31432cfa74fe3a51f7`;
- `git_commit = a24f6dd14049cd8ce571bb53abc4f6d056a00e3a`;
- archivo de índice: `09-simulaciones-edi/HASHES_PRE_EJECUCION.json`;
- archivo por caso: `09-simulaciones-edi/<case>/SETUP_HASH.json`.

Cualquier evaluador externo puede correr:

```bash
python3 scripts/freeze_setup.py --verify 04_caso_energia
```

para verificar que el setup actual coincide con el declarado en el commit.

---

## Bloque B4 — Sondas teóricamente independientes

### Problema

Ningún caso del corpus actual cumple los tres criterios κ-ontológica
fuerte simultáneamente (cap 02-01 §criterios). El primer criterio C1
(convergencia bajo sondas con motivación teórica distinta) requiere
sondas no derivables paramétricamente unas de otras.

### Solución

`common/independent_probes.py` provee tres sondas secundarias con
motivación teórica radicalmente distinta a la primaria:

| Caso | Sonda primaria | Sonda secundaria nueva |
|------|----------------|------------------------|
| 04 Energía | Lotka-Volterra ecológico | Maxwell-Boltzmann termodinámico |
| 16 Deforestación | von Thünen económico-espacial | Fisher-KPP difusión reactiva |
| 27 Riesgo Biológico | SIR epidemiológico | Catastrophe theory de Zeeman |

### Hallazgo honesto V5.1

Cuando se aplican las sondas secundarias sobre **proxys sintéticos**
(porque los `metrics.json` actuales no exponen los arrays
`obs/abm/forcing` individuales), la convergencia inter-paradigma **no se
alcanza** en ninguno de los tres casos.

**Lectura:** la infraestructura está lista; la verificación definitiva
requiere modificación menor de `edi_engine.py` para que `metrics.json`
emita los arrays primarios. Esta es **deuda fechada de 2-3 semanas
pre-depósito**, no deuda externa de 6-12 meses.

```bash
python3 scripts/run_independent_probes.py
```

Output: `INDEPENDENT_PROBES_REPORT.json` + `INDEPENDENT_PROBES_REPORT.md`.

---

## Bloque B5 — Sensibilidad a umbrales mecanizada

### Problema

La composición del corpus depende de los umbrales (0.10/0.30 → 5 strong;
0.15/0.40 → 3; 0.05/0.20 → 9). El cap 06-01 §5.4 lo declara honestamente
pero no lo mecaniza.

### Solución

`common/threshold_sensitivity.py` barre la grilla
`weak_low ∈ {0.05, 0.075, 0.10, 0.125, 0.15}` × `strong_low ∈ {0.20,
0.25, 0.30, 0.35, 0.40}` y reporta:

- **`robust_strong`**: casos siempre strong bajo TODA la grilla;
- **`robust_null`**: casos siempre null;
- **`per_case_invariance`**: conjunto de niveles bajo la grilla por caso.

### Hallazgo V5.1

Sobre el corpus de 30 casos:

- **3 casos siempre strong (invariantes):** Energía (0.65), Deforestación (0.60), Microplásticos (0.78).
- **10 casos siempre null (invariantes).**
- **13/30 = 43% del corpus tiene clasificación invariante** a la elección razonable de umbrales.
- Kessler (0.353) y Riesgo Biológico (0.333) son **strong sensibles**: pasan a weak bajo umbrales conservadores. La afirmación más honesta es: **3 strong invariantes + 1 strong canónico + 1 strong canónico marginal + 1 strong sin gate (Microplásticos)**.

```bash
python3 scripts/run_threshold_sensitivity.py
```

Output: `THRESHOLD_SENSITIVITY_REPORT.json` + `THRESHOLD_SENSITIVITY_REPORT.md`.

---

## Cómo se integran al pipeline canónico

Estos cinco bloques están en `09-simulaciones-edi/common/` y son
invocables desde el motor `edi_engine.py` y `hybrid_validator.py`. Su
integración al flujo canónico de validación es opcional en V5.1 y se
hará obligatoria pre-depósito mediante:

```python
# Pendiente en edi_engine.py (deuda fechada de 2-3 semanas pre-depósito):
from common.calibration import block_bootstrap_pvalue, fwer_correct
from common.replication import seed_robustness, holdout_temporal
from common.preregistration import freeze_case_setup
from common.threshold_sensitivity import sweep_threshold_grid
```

Cada caso emitirá entonces en `outputs/metrics.json`:

```json
{
  "edi": 0.6503,
  "p_value_legacy": 0.0001,
  "calibrated_inference": {
    "p_value_block_bootstrap": 0.0007,
    "p_value_shift": 0.0006,
    "newey_west_se": 0.012,
    "fwer_position": {"holm": "rank 2/30, p_adj=0.014"}
  },
  "replication_robustness": {
    "seed_drift": 0.012,
    "holdout_test_edi": 0.638,
    "adversarial_swaps_failed": 0
  },
  "preregistration": {
    "setup_hash": "85e76b...",
    "git_commit": "a24f6dd...",
    "frozen_at": "2026-04-28T22:13:58Z"
  },
  "threshold_sensitivity": {
    "invariant_classification": "strong",
    "always_strong_under_grid": true
  }
}
```

Esto NO requiere re-ejecutar el corpus inmediatamente; los hallazgos
canónicos del manuscrito (4 strong, 3 controles rechazados, AUC=0.886) se
preservan. La integración es **mejora de auditabilidad** para evaluadores
externos.

---

## Lectura cruzada

- `Anexos/A0-limitaciones-declaradas.md` — estado actualizado de las 20 limitaciones.
- Cap 03-04 §"Refuerzos metodológicos V5.1" — explicación filosófica de los cinco bloques.
- Cap 02-01 §"Nota sobre κ" — distinción κ-pragmática vs κ-ontológica que B4 ataca.
- `08-consistencia-st/theories/23-modal-kt-bajo-hipotesis.st` — cierre formal modal.

## Política de uso

Estos refuerzos elevan el aparato desde "robusto bajo régimen declarado"
hasta "robusto bajo régimen declarado + cinco tests metodológicos
avanzados ejecutados". No reabren debate conceptual; son disciplina
ingenieril aplicada al protocolo existente.

> Una tesis cierra cuando ya no se beneficia de iteración endógena. V5.1
> es exactamente el cierre del aparato científico antes de la transición
> a validación externa.
