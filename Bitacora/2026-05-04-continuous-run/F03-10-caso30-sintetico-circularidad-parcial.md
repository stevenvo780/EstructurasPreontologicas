# F03-10 — Caso 30: circularidad parcial sintético ↔ sonda EDI

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap03 (2026-05-05)
**Estado:** `needs_human` (requiere implementación de sonda alternativa por B-T*)

## (a) Verificación de la afirmación

La afirmación del adversarial es **correcta**. Evidencia textual:

1. **Manuscrito** (`03-formalizacion/05-etica-y-gobernanza-de-datos.md:55`):

   > "datos sintéticos generados con la ecuación completa de Fajen y Warren (2003) … parámetros (b=3.25, k_g=7.50, c1=0.40, c2=0.40)… La elección de generar datos sintéticos del sistema completo (no de la sonda EDI simplificada) **evita la circularidad ABM ≡ ODE**."

2. **Configuración** (`09-simulaciones-edi/30_caso_behavioral_dynamics/case_config.json`):
   - `ode_model: "behavioral_attractor"`, `ode_key: "heading_error"`.
   - `synthetic.true_params` contiene `fw_b=3.25, fw_k_g=7.50, fw_c1=0.40, fw_c2=0.40, fw_d_g=4.0, fw_dt=0.05` — **los mismos parámetros Fajen-Warren** que la sonda macro recibe vía `extra_ode_params` (líneas 74-85).
   - `metadata.ode_interpretation` (línea 89) declara explícitamente que la sonda usa la ecuación de segundo orden `φ̈ = -b·φ̇ - k_g·(φ - ψ_g)·(e^{-c1·d_g} + c2)` — **idéntica forma funcional** a la del generador.

**Conclusión:** la prosa afirma evitar "circularidad ABM ≡ ODE" pero la circularidad real que el adversarial señala es **ODE_generador ≡ ODE_sonda** (misma forma funcional, mismos parámetros). Esto es el problema clásico de overfitting estructural (Forster & Sober 1994, *British J. Phil. Sci.* 45:1, "How to Tell when Simpler, More Unified, or Less Ad Hoc Theories will Provide More Accurate Predictions"): si el modelo evaluador comparte la familia funcional con el generador, el RMSE bajo no testea la hipótesis de fondo (control informacional vs. representacional) — testea la auto-consistencia paramétrica.

La prosa diferencia "sistema completo" vs "sonda EDI simplificada", pero al inspeccionar `case_config.json` la sonda recibe los **siete parámetros Fajen-Warren completos** (`fw_b, fw_k_g, fw_c1, fw_c2, fw_d_g, fw_dt`, más `ode_alpha, ode_beta` macro). La diferencia entre "completo" y "simplificado" no se sostiene en la configuración.

## (b) Propuesta de edición

**No edito Tesis.md ni metrics.json** (regla harness). Propuesta a Jacob/Steven:

### B1. Reescritura de prosa (necesaria, independiente de re-ejecución)

En `03-formalizacion/05-etica-y-gobernanza-de-datos.md:55`, reemplazar:

> "La elección de generar datos sintéticos del sistema completo (no de la sonda EDI simplificada) evita la circularidad ABM ≡ ODE."

por:

> "Limitación reconocida: la sonda EDI macro comparte la forma funcional Fajen-Warren con el generador sintético. Esto produce una **circularidad parcial** (Forster & Sober 1994): un EDI alto en este caso confirma reproducibilidad paramétrica, no superioridad del control informacional sobre alternativas estructurales (neural ODE, MLP, GP). Mitigación pendiente: re-ejecutar con sonda alternativa estructuralmente distinta y reportar `edi_alt_probe` (B-T pendiente)."

### B2. Acción técnica (B-T nueva, requiere ejecución)

Re-ejecutar caso 30 con al menos una sonda estructuralmente distinta:

- **Opción A (más estricta):** Neural ODE (torchdiffeq, MLP de 2 capas como derivada).
- **Opción B:** Gaussian Process con kernel RBF sobre `(φ, φ̇, ψ_g, d_g)`.
- **Opción C (mínima):** baseline ARIMA/VAR ya disponible en `common/baselines.py` — pero esto NO satisface el acceptance (no es ODE alternativa, es serie temporal pura).

Reportar en `outputs/metrics.json` un campo nuevo:

```json
"edi_alt_probe": {
  "probe_type": "neural_ode|gp|...",
  "edi": <valor>,
  "rmse_coupled": <valor>,
  "rmse_no_ode": <valor>,
  "delta_vs_fajen_warren": <edi_fw - edi_alt>,
  "p_perm": <valor>
}
```

Si `delta_vs_fajen_warren > 0.10` con sonda alternativa peor → la circularidad NO era el factor dominante (la estructura Fajen-Warren captura algo real). Si `delta < 0.05` → la circularidad explica buena parte del EDI reportado, y la prosa debe re-graduar la fuerza de la conclusión.

### B3. Glosario operativo

Añadir entrada en `00-proyecto/07-glosario-operativo.md`: **"Circularidad estructural parcial"** — generador y evaluador comparten familia funcional pero con parámetros estimados independientemente; mitigación: comparar con sonda de familia distinta.

## (c) Costo argumentativo declarado

- **Costo si se acepta la edición B1 sin B2:** la tesis pierde una afirmación fuerte ("evita circularidad") y queda con limitación reconocida pero no cuantificada. El caso 30 baja en peso justificatorio dentro del corpus.
- **Costo si se ejecuta B2 y `delta` es pequeño:** el caso 30 deja de ser evidencia robusta del control informacional Fajen-Warren; se rebaja a ilustración pedagógica con datos sintéticos. Esto **no derrumba la tesis general** (los marcos generales no dependen del caso 30 individualmente; CLAUDE.md §"Qué es este repositorio"), pero obliga a quitar el caso 30 de las listas de "casos confirmatorios" y reubicarlo entre los casos "ilustrativos / didácticos".
- **Costo si se ignora la edición:** F03-10 queda como objeción adversarial publicable contra la tesis. Forster-Sober 1994 es referencia obligada en filosofía de la ciencia analítica; un examinador con esa formación lo levantará.

## Marcado

- **B1 (reescritura prosa):** ejecutable por asistencia, pero **requiere firma Jacob** porque cambia una afirmación que el manuscrito sostiene actualmente. Marcado `needs_human` para confirmación de la nueva formulación.
- **B2 (re-ejecución con sonda alternativa):** nueva tarea **B-T** sugerida — implementación de sonda neural-ODE/GP en `09-simulaciones-edi/common/` y campo `edi_alt_probe` en `metrics.json`. Coste estimado: 4–8 h ingeniería + 1–2 h cómputo GPU. **No la ejecuto desde este sub-agente** (excede scope read-only y modificaría `metrics.json`, prohibido por reglas).
- **B3 (glosario):** ejecutable por asistencia tras firma B1.

## Referencias

- Forster, M. & Sober, E. (1994). "How to Tell when Simpler, More Unified, or Less Ad Hoc Theories will Provide More Accurate Predictions". *British Journal for the Philosophy of Science*, 45(1), 1–35. — *No verificado contra PDF en `07-bibliografia/`; cita usada como referencia conceptual estándar; pendiente de verificación con paginación si la edición B1 mantiene la cita literal.*
- Fajen, B. R. & Warren, W. H. (2003). "Behavioral dynamics of steering, obstacle avoidance, and route selection". *Journal of Experimental Psychology: Human Perception and Performance*, 29(2), 343–362. — fuente del generador y de la sonda.

---

RESULT: complete | F03-10-caso30-sintetico-circularidad-parcial | needs_human B-T sonda alt
