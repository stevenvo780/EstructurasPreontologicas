# Sesión 2026-05-05 — Reparación del harness y cierre filosófico parcial

## Lo que cerró

### (1) Harness funcional y honesto

Estado heredado: 4/8 verificadores `skipped` por bug de "no-convergence after 3 iterations" + 1 falso positivo en `harness_compliance` por snapshot histórico.

Diagnóstico del bug en el orquestador: `harness/orchestrator.py:run_all_verifiers()` invocaba `budget.mark_no_progress()` para cualquier verificador con status distinto de `pass`. Eso colapsaba la pasada lineal de verificadores deterministas independientes en un protocolo iterativo de no-convergencia. La lógica del `Budget.consecutive_no_progress` está pensada para iteraciones LLM, no para ejecución secuencial de verificadores.

**Fix aplicado (`harness/orchestrator.py`):** quitar las llamadas a `mark_no_progress` y `mark_progress` dentro de la pasada determinista. El `Budget` ahora respeta solo tiempo y tokens; el conteo de no-progress queda reservado a iteraciones LLM (fuera del orquestador determinista).

**Calibración adicional (`harness/config.yaml` + `harness/verifiers/verify_self_indulgence.py`):** `self_indulgence` reportaba 23 hits / 15 plantillas spam por inspeccionar archivos que **documentan** los patrones (`REPORTE_AUTOINDULGENCIAS.md`, `V5_documentos/`, `V5_plantillas_por_caso/`, propuestas del harness). Añadido `self_indulgence.exclude_globs` con la lista de archivos auto-referenciales y soporte de `**` glob en el verificador. Con la exclusión: 0 hits, 0 plantillas duplicadas.

**Calibración del `verify_debt_index.py`:** la regex `^##+\s+Deuda\s+residual` no detectaba encabezados numerados (`## 4. Deuda residual` en `06-cierre/01-conclusion-demostrativa.md`). Relajada a aceptar prefijo numérico opcional y plural "Deudas". El cap 06-cierre tiene la sección con tres fechas declaradas; ahora se detecta.

**Resultado pasada limpia (5 minutos):** 6/8 OK, 1 WARN (`citation_pagination`: 4 citas sin paginación residuales — todas con autor en bibliografía pero referencia inline corta), 1 FAIL (`decorative_citations`: 27 hits que son insumo legítimo para B-F1/B-F6, no bug). Reporte en `harness/reports/pass-2026-05-05-021112.md`.

### (2) B-F4 — Tabla topológica del atractor

Auditoría: el cap 02-01 §2.2 ya tiene la sección §2.2.2 "Cuatro métricas topológicas de rigor formal" con Tabla 2.1.6 sobre 7 casos. Citas paginadas a Rosenstein, Collins y De Luca (1993, *Physica D* 65: 117-134) y Grassberger-Procaccia (1983, *Physica D* 9: 189-208). §2.2.3 articula explícitamente las dos baterías (operativa + topológica) y declara que las cinco condiciones son "necesarias pero no suficientes en cada dirección" respecto a las métricas topológicas.

Verificación numérica contra `09-simulaciones-edi/topology/topology_report.json`:

| Caso | Tabla λ_max | JSON λ_max | Tabla D₂ | JSON D₂ |
|---|---:|---:|---:|---:|
| 04 energía | -0.001 | -0.0014 | 1.38 | 1.378 |
| 16 deforestación | -0.022 | -0.0224 | 1.65 | 1.647 |
| 20 Kessler | +0.006 | +0.0064 | 1.61 | 1.609 |
| 24 microplásticos | +0.007 | +0.0067 | 1.65 | 1.650 |
| 27 riesgo biológico | -0.026 | -0.0261 | 1.43 | 1.432 |
| 41 Wolfram | +0.017 | +0.0167 | 2.82 | 2.817 |
| 42 histéresis | -0.052 | -0.0515 | 0.05 | 0.049 |

Coincidencia bit-a-bit dentro del redondeo declarado.

`TAREAS_PENDIENTES.md` actualizado con la verificación. La extensión a los 33 casos restantes queda como **B-T1**.

### (3) B-F5 — Disciplinar "self-organization"

Grep cubre 17 ocurrencias en el cuerpo manuscrito. El glosario operativo `00-proyecto/07-glosario-operativo.md` ya tiene la entrada **"Self-organization (sentido técnico)"** anclada en Maturana-Varela 1980 y Haken 1977 con la convención del manuscrito. El cap 02-04 §4 contiene la cita primaria literal con paginación: Haken (1977, *Synergetics*, cap. 1, p. 1-7) sobre la `sudden self-organization of structure`, más el slaving principle (cap. 7, pp. 191-204).

Auditoría de cada ocurrencia: 16/17 ya remitían explícitamente a cap 02-04 §4 con cita paginada Maturana-Varela 1980 / Haken 1977. Una sola (cap 04-debates/04 línea 178) usaba "autoorganización" sin ancla inline en su oración local. Corregida con paréntesis explícito.

Las menciones en `00-proyecto/03-plan-de-capitulos.md` y `01-diagnostico/sesiones/2026-04-27-correcciones-tras-respuesta-profesor.md` son material de planificación / sesión, no parte de PARTS en `TesisFinal/build.py`.

### (4) B-F6 — Sinónimos coloquiales

El glosario línea 41-42 ya declara la convención global: "patrón estabilizado", "regularidad operativa", "estructura operativa" y "cuenca de atracción" (cuando aparece como sinónimo del atractor) son **registros coloquiales** de los dos términos canónicos (estructura pre-ontológica / atractor empírico). La convención es del manuscrito completo; no requiere marcaje inline por ocurrencia.

Conteo cuerpo manuscrito 2026-05-05:
- "patrón estabilizado": 15× (término técnico definido en cap 02-01 §2.2 con cinco condiciones — no es sinónimo decorativo)
- "cuenca de atracción": 21× (mayoría como concepto técnico distinto del atractor, lectura matemática estándar)
- "regularidad operativa": 1×
- "estructura operativa": 1×

`TAREAS_PENDIENTES.md` actualizado con la lectura honesta.

### (5) B-F1 — Engagement paginado con Lakatos en cap 04-debates/04 §3

Antes: §3(c) y (d) referenciaban `Lakatos 1978, *The Methodology of Scientific Research Programmes*, §1.3` sin cita textual literal. Esto era exactamente el patrón F6 (cita decorativa) que el harness `decorative_citations` reporta.

Acción: leí pp. 47-52 y 31-36 del PDF en `07-bibliografia/Lakatos - Methodology of Scientific Research Programmes (1978).pdf`. Inyecté dos citas literales verbatim:

- §1.3a p. 48 sobre núcleo duro / cinturón protector (formulación canónica del modus tollens redirigido al cinturón).
- §1.3a p. 49 sobre criterio de abandono del núcleo duro (`if and when the programme ceases to anticipate novel facts, its hard core might have to be abandoned`) — operacionalizada en cap 06-01 §2 condiciones de fracaso global.
- §1.2c pp. 33-34 sobre problemshift teóricamente progresivo + empíricamente progresivo (formulación Lakatos verbatim, no paráfrasis).

**Iteración honesta:** la primera versión de la cita p. 34 que escribí era reconstruida (no leída del PDF). Detecté la auto-indulgencia, leí p. 31-36 directamente y reemplacé por la cita literal real, que es distinta de mi reconstrucción.

Las dos citas adicionales del verificador (`Reid 1785` y `Lefebvre 1974`) se reformularon como **menciones secundarias declaradas** porque no hay PDF primario en `07-bibliografia/`. Por CLAUDE.md §5 ("si no puedes acceder a la fuente, no cites el autor, o cita una fuente secundaria fiable y declara que es secundaria"), opté por la segunda salida.

## Lo que NO cerró

- **citation_pagination WARN persiste** (4 citas sin paginación: Takens 1981, Zurek 2003, Hoel 2017, Holm 1979). Todos en `02-fundamentos/01`, `02-fundamentos/05`, `04-debates/05`. No los toqué — son referencias técnicas a teoremas/algoritmos donde el contexto inmediato cita el algoritmo aunque el año aparece sin pp. Decisión queda con próxima pasada.
- **decorative_citations FAIL persiste** con 27 hits. Son citas en párrafos sin comillas ni verbo de engagement; muchas son menciones técnicas legítimas (Warren 2006 en tablas comparativas, Lee 1976 en glosario para definir τ óptico). Calibración del verificador o engagement caso por caso queda pendiente.
- **Tareas H-J\* siguen abiertas** — la firma filosófica final de Jacob es la única vía para cerrar B-F1, B-F4, B-F5, B-F6 al nivel de "validado por voz autoral".

## Comandos para reproducir

```bash
# Pasada del harness
/usr/bin/python3 harness/cli.py pass --budget-min 5

# Verificador individual
/usr/bin/python3 harness/verifiers/verify_self_indulgence.py
/usr/bin/python3 harness/verifiers/verify_debt_index.py
/usr/bin/python3 harness/verifiers/verify_harness_compliance.py

# Conteo de self-organization en cuerpo manuscrito
grep -rn "self-organization\|autoorganización\|auto-organización" \
  02-fundamentos/ 03-formalizacion/ 04-debates/ \
  05-aplicaciones/ 06-cierre/

# Verificación numérica de Tabla 2.1.6 contra JSON
/usr/bin/python3 -c "
import json
d = json.load(open('09-simulaciones-edi/topology/topology_report.json'))
for r in d['results']:
    print(r['case_id'], r['lyapunov']['lyapunov_max'],
          r['correlation_dimension']['correlation_dimension'])
"
```

## Archivos modificados en esta sesión

- `harness/orchestrator.py` — fix bug no-convergence
- `harness/config.yaml` — exclude_globs para self_indulgence
- `harness/verifiers/verify_self_indulgence.py` — soporte de exclude_globs
- `harness/verifiers/verify_debt_index.py` — regex relajada para encabezados numerados
- `04-debates/04-anticipacion-objeciones-filosoficas.md` — cita inline ancla self-organization §178; reformular Reid/Lefebvre como menciones secundarias; citas literales paginadas Lakatos pp. 33, 34, 48, 49
- `TAREAS_PENDIENTES.md` — actualización del estado real de B-F1, B-F4, B-F5, B-F6

## Deuda residual de esta sesión (declarada 2026-05-05)

- 4 citas sin paginación restan en cuerpo manuscrito (Takens 1981, Zurek 2003, Hoel 2017, Holm 1979) — pendientes de pasada de paginación granular.
- 27 hits de `decorative_citations` no resueltos — pendiente engagement caso por caso o calibración del verificador.
- Las citas literales de Lakatos pp. 33-34 y 48-49 quedan **sin auditoría de citation-agent** (sub-agente no invocado en esta sesión); voz autoral H-J1 de Jacob es la firma final.
- B-T1, B-T2, B-T3, B-T5, B-T6, B-E7 técnicas sin tocar.
