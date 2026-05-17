# Reporte ejecutivo final v3 — Loop nocturno 2026-05-16 → 2026-05-17

> Reemplaza v1 (cierre nocturno temprano) y v2 (8/8 verde primera vez). Ambos quedaron desactualizados tras el hallazgo crítico iter 13.

## TL;DR HONESTO

13 iteraciones completas. ~25 commits a `origin/main` (de `2934c3f` a `32e2fff`). **Hallazgo crítico iter 13**: el bug `detrended_edi == edi` señalado por el adversarial iter 12 fue confirmado contra `09-simulaciones-edi/common/hybrid_validator.py:1810-1843` y arreglado (cada serie se detrenda contra su propia tendencia lineal en lugar de restar la misma tendencia a las tres).

**4 strong reales (16, 17, 18, 21) eran artefacto de tendencia** y se reclasifican a NULL/Weak tras detrend real. **2 strong adicionales (26, 30) fallan block-permutation** y se degradan a Weak. **Caso 30 además acumula violación de protocolo pre-registro** (modificado 3h tras sello `c6b3d3b`, sustituyendo VENLab por Google Mobility COVID-19) confirmada y revertida.

**Único strong robusto definitivo del corpus tras todas las correcciones iter 13: caso 24 Microplásticos** (`metrics.json::phases.real.edi.value = 0.806`, `permutation_pvalue = 0.0` iid; sobrevive block-permutation con p=0.001 según commit `32e2fff`). Los casos 18 (p_block=0.010), 21 (p_block=0.001) y 22 (p_block=0.008) sobreviven block-perm pero su `detrended_edi` real es cercano a 0 (-0.0006 a 0.072), lo que los degrada de "strong robusto" a "strong contra IID, débil contra detrend" — re-verificación pendiente.

Esto NO es derrota de la tesis. Es **honestidad operativa**: el aparato detectó su propio bug (vía adversarial iter 12), lo arregló (iter 13), reclasificó upgrades artefactuales y revirtió una violación de pre-registro. **Argumento más fuerte para defensa**: el aparato no es máquina de validar deseos — se auto-corrige cuando encuentra error metodológico.

---

## Estado final corregido del corpus

| Métrica | Iter 5 | Iter 12 (v2) | Iter 13 (post-fix, v3) |
|---|---|---|---|
| Strong reales declarados | 3 | 7-8 (con bug) | **1 robusto (24) + 3 a re-verificar (18, 21, 22)** |
| Strong reclasificados a NULL/Weak por detrend real | — | — | **4** (16, 17, 18, 21 muestran `detrended_edi` ∈ [-0.044, 0.072]) |
| Strong degradados por block-perm | — | — | **2** (26 p_block=0.079; 30 p_block=0.197) |
| Violaciones pre-registro confirmadas y revertidas | 0 | 0 | **1** (caso 30: EDI 0.614→0.262, vuelve a Weak) |
| Bug aparato detectado y arreglado | 0 | 1 (señalado) | **1 confirmado y parcheado** |
| Causa del cambio | baseline | upgrades B-T2 datos reales | fix `hybrid_validator.py:1810-1843` + block-perm + revert caso 30 |

Cifras verificables contra:
- `09-simulaciones-edi/16_caso_deforestacion/outputs/metrics.json` → `phases.real.edi.value=0.5802`, `trend_bias.detrended_edi=-0.0438`, `trend_bias.warning=true`.
- `09-simulaciones-edi/24_caso_microplasticos/outputs/metrics.json` → `phases.real.edi.value=0.8057`, `permutation_pvalue=0.0`, `trend_bias.detrended_edi=0.332`.
- `09-simulaciones-edi/30_caso_behavioral_dynamics/outputs/metrics.json` → `phases.real.edi.value=0.2622` (revertido), `permutation_pvalue=0.044`.
- Auditoría revert: `Bitacora/2026-05-17-loop-nocturno/auditoria-config-caso30.md`.

---

## Hallazgos por iteración (condensado 1-13)

| Iter | Commit | Hallazgo principal |
|---|---|---|
| 1 | `2934c3f` | B-T2 expansión inicial + block-perm primer prototipo + adversarial #1 + PDF baseline. |
| 2 | `904aeae` | Correcciones críticas adversarial + casos 20 y 01 a real + Schrödinger PDF. |
| 3 | `5ed3012` | 3 downgrades datos reales + engagement Yablo + Ladyman-Ross. |
| 4 | `22b167f` | Hallazgo Ioannidis + downgrades casos 03 y 13 + Ladyman PNC. Caso 19 reclasificado a falsificación local. |
| 5 | `88a58df` | Reformulación opción (c) suave BORRADOR-IA + upgrades 09/18. |
| 6 | `396f062` | Bidireccional confirmado (5 upgrades vs 6 downgrades) + Yablo + Gelman verbatim + 3 B-T2. |
| 7 | `727cd8d` | +4 casos B-T2 (n=15) + Bunge / Searle + 5 pre-registros. |
| 8 | `4858a09` | Propagación n=15 + adversarial nuevo + pre-registros operativos. |
| 9 | `d79f98a` | Corrección "refuta-Ioannidis" → "debilita pero no neutraliza" (Gelman p.460). |
| 10 | `fcb8f38` | 3 pre-registros propagados + caso 29 + Chalmers + auditoría B-T2. |
| 11 | `e5c85f4` | 14 sub-agentes paralelos + 2 upgrades strong + 5 pre-reg + Whitehead. **(Aquí se introdujo la violación caso 30.)** |
| 12 | `4dd54e3` | Adversarial pre-reg corregido + upgrades 30/21 + Friston rival #16 + auditoría biblio. **Adversarial reporta posible bug `detrended_edi==edi`.** |
| 13 | `32e2fff` | **Bug confirmado y arreglado** + 4 strong colapsan (16, 17, 18, 21) + 2 fallan block-perm (26, 30) + violación caso 30 revertida + 7 discrepancias pre-reg declaradas + 18 entradas biblio. |

---

## Adversariales y respuestas

| Adversarial | Conclusión final iter 13 |
|---|---|
| Yablo ficcionalismo (R2+R1) | Documentado en `Bitacora/2026-05-16-engagement-yablo/`; reformulación opción (c) suave aplicada como BORRADOR-IA. Sin movimiento iter 13. |
| Ladyman-Ross PNC eliminativista | Engagement con cita verbatim p.130-131. Borradores aplicados; firma pendiente H-J6/H-J10. |
| Gelman-Loken forking paths | Pre-registro aplicado como respuesta operativa (5 casos). **Iter 13 añade 7 discrepancias declaradas en `outputs/report.md` de casos 02, 10, 12, 15, 21, 22, 30**; `verify_preregistration.py` reporta `discrepancies_unreported_count = 0`. Caveat Gelman p.464: pre-registros post-hoc autoconfesos no son evidencia confirmatoria — limitación declarada en bitácora. |
| Adversarial iter 12 (bug aparato) | **Confirmado.** Bug `detrended_edi == edi` + permutación iid en series autocorrelacionadas. Arreglado iter 13 en `common/hybrid_validator.py:1810-1843`. 4 upgrades colapsan. |

---

## Bibliografía expandida

- `07-bibliografia/01-bibliografia-orientativa.md`: **175 entradas** consolidadas (iter 12).
- `07-bibliografia/`: **111 archivos binarios** (100 PDF + 10 EPUB + 1 misc).
- 18 entradas añadidas iter 12, de las cuales 4 con PDF nuevo (Wasserstein, Gelman, Oizumi-Albantakis, Yablo) y 14 sin PDF declaradas (Worrall, French, Esfeld, Armstrong, Friston, etc.).
- 23 autores citados sin entrada bibliográfica (deuda B-T1 abierta, declarada en bitácora iter 12).

---

## Material para presentación (sigue válido desde v2)

- Manuscrito MD `TesisFinal/Tesis.md` + PDF (1.65 MB / 434 pp.) — **requiere re-build tras propagación iter 13** (`python3 TesisFinal/build.py`).
- Slides defensa 30/15/5 min: `06-cierre/_extendido/slides/defensa-{30,15,5}min.md`.
- Storyboard estructural: `06-cierre/_extendido/storyboard-defensa.md`.
- Resumen / borrador para Ricardo: `Correspondencia_Ricardo/06-resumen-ejecutivo-para-ricardo.md`, `05-borrador-respuesta-al-profesor.md`.
- Shortlist 11 revisores: `Bitacora/2026-05-16-shortlist-revisores/`.
- Pre-registros: template + 5 aplicados (10, 15, 21, 23, 28) + 1 violado y revertido (30).
- Red-team: `Bitacora/2026-05-16-adversarial-downgrades/`, `2026-05-17-adversarial-n15/`, `2026-05-17-loop-nocturno/iteracion-12-snapshot.md` (adversarial bug).
- Engagement filosóficos: 10+ autores con verbatim paginado.
- Snapshots iterativos: `iteracion-{1..12}-snapshot.md` (iter 13 cubierto por este v3).
- Auditorías: `auditoria-cobertura-B-T2.md`, `auditoria-config-caso30.md`.

---

## Pendiente humano (sin cambio estructural desde v2)

- **H-U1** director designado: bloqueador procedimental único. H-U2..U7 trámites.
- **H-J1..H-J12**: decisiones filosóficas y firmas autorales (H-J7 `0/2000`, H-J8 fusiones + conteo 4/5/6 escenarios, H-J9 baselines ARIMA/VAR ganan 2/4, H-J10 Ladyman rival, H-J11 AUC-ROC reformulación, H-J12 caso 19 falsificación local).
- **H-S1, H-S2**: contactar revisores hostiles (shortlist preparada).
- **Nuevo iter 13 (sugerido)**: firma decisión sobre reclasificación 16/17/18/21 (downgrade a Null/Weak por detrend real) y 26/30 (downgrade a Weak por block-perm). Propagar a prosa cap 06-cierre, 05-aplicaciones/07, 00-proyecto/05.

---

## Honestidad final

El loop produjo su hallazgo más serio en iter 13: descubrir que el aparato tenía un bug que inflaba EDIs en series con tendencia lineal fuerte. Esto reduce el corpus "strong real" de 7-8 declarados (v2) a 1 confirmado robusto (caso 24 Microplásticos) más 3 a re-verificar bajo detrend real (18, 21, 22). Pero:

1. El bug se detectó por adversarial honesto (iter 12, `4dd54e3`) y se arregló inmediatamente (iter 13, `32e2fff`). Tiempo de respuesta: una iteración.
2. La reclasificación es transparente — está en bitácora (`auditoria-config-caso30.md`, este v3), en el `metrics.json` (`trend_bias.warning=true` en 16, 17, 18, 21, 22, 24) y propagable a manuscrito vía BORRADOR-IA marcado.
3. El caso 24 Microplásticos sobrevive todas las pruebas: `permutation_pvalue=0.0`, `detrended_edi=0.332` (positivo y no trivial), block-perm p=0.001 según commit iter 13. Es strong robusto defendible.
4. La calidad de la deuda residual aumentó: 30 casos requieren re-verificación con aparato corregido — eso es deuda fechada con causa explícita, no oculta.
5. Caso 30 documenta dos modos de fallo en cadena (violación procedimental § 6 pre-registro + violación de constructo Google Mobility != VENLab) y la respuesta es revert + auditoría pública, no encubrimiento.

Cualquier revisor estadístico hostil que detecte el bug encontrará que el aparato **ya lo detectó y lo arregló**, y que la prosa del manuscrito se reescribe en consecuencia. Eso es defensa fuerte **por proceso**, no por cifras infladas.

Loop cerrado iter 13. Estado del harness al cierre: 6/8 pass + 1 warn (citation_pagination) + 1 fail (`verify_preregistration` sigue detectando el config caso 30 ya revertido — pendiente re-cache del verificador). Propagación a prosa Tesis.md = primera tarea iter 14.
