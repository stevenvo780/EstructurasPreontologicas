---
borrador: IA
requires: H-J* + B-T
propuesta_fecha: 2026-05-11
destino: 03-formalizacion/05-etica-y-gobernanza-de-datos.md:55
hallazgo: Bitacora/2026-05-04-continuous-run/F03-10-caso30-sintetico-circularidad-parcial.md
tipo: reemplazo_parrafo + tarea_B-T_sonda_alternativa
---

## Diagnóstico

El cap 03-05 afirma que "la elección de generar datos sintéticos del sistema completo (no de la sonda EDI simplificada) evita la circularidad ABM ≡ ODE". La afirmación es correcta respecto a la circularidad **ABM ≡ ODE**, pero falsa respecto a una circularidad distinta y operativa: la sonda EDI macro **comparte la forma funcional Fajen-Warren con el generador sintético**, con idénticos parámetros `fw_b, fw_k_g, fw_c1, fw_c2, fw_d_g`. Esto es **circularidad estructural parcial** (Forster & Sober 1994): si el modelo evaluador comparte familia funcional con el generador, un RMSE bajo no testea la hipótesis de fondo (control informacional vs alternativas estructurales) — testea auto-consistencia paramétrica.

## Verificación contra fuente primaria

- `03-formalizacion/05-etica-y-gobernanza-de-datos.md:55` — afirmación literal sobre "evita circularidad ABM ≡ ODE".
- `09-simulaciones-edi/30_caso_behavioral_dynamics/case_config.json`:
  - `ode_model: "behavioral_attractor"`, `ode_key: "heading_error"`
  - `synthetic.true_params`: `fw_b=3.25, fw_k_g=7.50, fw_c1=0.40, fw_c2=0.40, fw_d_g=4.0`
  - `metadata.ode_interpretation` (línea 89): ecuación `φ̈ = -b·φ̇ - k_g·(φ - ψ_g)·(e^{-c1·d_g} + c2)`, idéntica al generador.
- Forster & Sober 1994, "How to Tell when Simpler, More Unified, or Less Ad Hoc Theories will Provide More Accurate Predictions", *British Journal for the Philosophy of Science* 45(1):1–35. PDF ausente en `07-bibliografia/`; si Jacob inscribe la cita literal, abrir `/fetch-biblio forster sober 1994 simpler unified ad hoc`. La afirmación operativa (overfitting estructural cuando generador y evaluador comparten familia funcional) es resultado estándar y se sostiene sin la cita literal.

## Texto propuesto (voz autoral filosófica de Jacob)

**Reemplazar en `03-formalizacion/05-etica-y-gobernanza-de-datos.md:55`:**

> "La elección de generar datos sintéticos del sistema completo (no de la sonda EDI simplificada) evita la circularidad ABM ≡ ODE."

**por:**

> "La elección de generar datos sintéticos con la ecuación completa de Fajen y Warren (2003) —y no con la sonda EDI simplificada— neutraliza una **primera** circularidad (ABM ≡ ODE: que el generador sea el propio ABM ya ajustado). Subsiste, sin embargo, una **segunda** circularidad parcial: la sonda EDI macro `behavioral_attractor` comparte forma funcional con el generador sintético, con los mismos parámetros publicados `(b, k_g, c_1, c_2, d_g)`. Esto es **circularidad estructural parcial** en sentido de Forster & Sober (1994): un EDI alto bajo esta configuración confirma reproducibilidad paramétrica del modelo Fajen-Warren, no superioridad del control informacional frente a alternativas estructurales (neural ODE, GP, MLP). La tesis declara este costo como deuda. Mitigación pendiente: re-ejecutar el caso 30 con al menos una sonda de familia funcional distinta y reportar `edi_alt_probe` con el delta de EDI; un delta `< 0.05` indicaría que la circularidad explica buena parte del EDI reportado, obligando a re-graduar la fuerza de la conclusión; un delta `> 0.10` indicaría que la estructura Fajen-Warren captura algo que la sonda alternativa no captura."

## Texto a reemplazar y acciones derivadas

- Sustituir la única oración indicada en `03-formalizacion/05-etica-y-gobernanza-de-datos.md:55`.
- **Glosario operativo:** añadir entrada **"Circularidad estructural parcial"** — generador y evaluador comparten familia funcional pero con parámetros estimados independientemente; mitigación: comparar con sonda de familia distinta.
- **Tarea B-T derivada:** implementar sonda alternativa en `09-simulaciones-edi/30_caso_behavioral_dynamics/`. Opciones:
  - (A más estricta) Neural ODE (torchdiffeq, MLP de 2 capas como derivada).
  - (B) Gaussian Process con kernel RBF sobre `(φ, φ̇, ψ_g, d_g)`.
  - (C mínima) Baselines ARIMA/VAR ya disponibles — **no satisface el acceptance**.
  Añadir campo `edi_alt_probe` en `outputs/metrics.json` con `probe_type`, `edi`, `rmse_coupled`, `rmse_no_ode`, `delta_vs_fajen_warren`, `p_perm`.
- Si el delta confirma la circularidad, retirar el caso 30 del peso justificatorio actual y reubicarlo entre los casos ilustrativos.

## Costo argumentativo declarado

Sin la B-T de sonda alternativa, la tesis pierde una afirmación fuerte ("evita circularidad") y queda con limitación reconocida pero no cuantificada — coste asumido. Con la B-T ejecutada y `delta` pequeño, el caso 30 deja de ser evidencia robusta del control informacional Fajen-Warren y se rebaja a ilustración con datos sintéticos. Esto **no derrumba la tesis general** (los marcos generales no dependen del caso 30 individualmente), pero obliga a retirar el caso 30 de la lista de casos confirmatorios. La alternativa —ignorar el hallazgo— deja la objeción Forster-Sober como vector publicable contra el aparato.
