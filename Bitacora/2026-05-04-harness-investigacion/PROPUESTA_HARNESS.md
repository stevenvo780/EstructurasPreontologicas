# Propuesta — Harness de investigación científico-filosófica para la tesis

**Fecha:** 2026-05-04
**Naturaleza del aporte:** 90% asistencia (síntesis de literatura + diseño), 10% Jacob/Steven (encuadre del problema en conversación previa). **Estado:** propuesta abierta, requiere firma humana antes de implementar cualquier componente. Esta no es una decisión, es un mapa de opciones.

---

## 0. Por qué este documento existe (y por qué podría no merecer existir)

El usuario pidió investigar los harnesses de investigación de Google y Anthropic para diseñar uno mejor para esta tesis, con énfasis en autonomía de larga duración. Se investigaron: AI co-scientist (Google), FunSearch, AlphaEvolve, AlphaProof, Gemini Deep Research; Anthropic Multi-agent Research System, Claude Agent SDK, Building Effective Agents; Sakana AI Scientist v1/v2, Agent Laboratory, Stanford STORM, OpenAI Deep Research, LangGraph/CrewAI/AutoGen.

**Riesgo declarado de origen** (regla §1 de CLAUDE.md sobre auto-indulgencias): un "harness propio" puede degenerar fácilmente en un meta-aparato que duplica en prosa y JSON lo que el motor EDI ya hace, o en una infraestructura agentica genérica desvinculada del trabajo real de la tesis. Para evitarlo, esta propuesta sigue tres restricciones:

1. **No reinventar lo que ya existe.** El repo ya tiene validador empírico (`hybrid_validator.py`, 2252 líneas), auditoría profunda, hashes de reproducibilidad, build de manuscrito, CLI unificada (`./tesis`). Cualquier componente nuevo se justifica solo si cubre una fricción real del Mapeo (§3 abajo).
2. **El harness sirve a Jacob, no al revés.** Las decisiones filosóficas (`H-J*`) no se automatizan. El harness reduce la carga de tareas verificables (citas, paginación, ejecución, auditoría prosa↔JSON, deuda) para que el tiempo humano se concentre donde la firma humana es irreductible.
3. **Verificador formal antes que verificador blando.** Lección dura de FunSearch/AlphaProof vs AI co-scientist: los sistemas con verificador determinista (código ejecutable, prueba en Lean, hash de output) producen conocimiento defendible; los sistemas con LLM-juez producen hipótesis prometedoras que requieren cierre humano. Esta tesis exige defensibilidad bajo crítica hostil — el harness debe inclinarse al primer modo siempre que sea posible.

---

## 1. Síntesis del estado del arte (lo que se aprovecha, lo que se descarta)

### 1.1 Google AI co-scientist (Gottweis, Weng et al., 2025, arXiv:2502.18864)

Coalición de 7 agentes sobre Gemini 2.0 orquestada por Supervisor: Generation, Reflection, Ranking (torneo Elo con debate pairwise), Evolution, Proximity, Meta-review. Test-time compute escalable; cola asíncrona; expert-in-the-loop.

**Lo que se aprovecha:** patrón de torneo evaluativo entre hipótesis rivales (aplicable a debates filosóficos del cap 04), separación Generation/Reflection (refleja la regla §2: lo que generas no lo cierras tú).

**Lo que se descarta:** la métrica Elo es **auto-evaluación** del propio sistema (crítica documentada en TechCrunch y DrugDiscovery.NET). Para esta tesis, Elo entre hipótesis filosóficas sería exactamente el tipo de "auto-indulgencia con ropaje cuantitativo" que CLAUDE.md §1 prohíbe. El ranking final lo firma Jacob.

### 1.2 FunSearch + AlphaEvolve + AlphaProof (DeepMind)

Patrón **LLM-generador + verificador formal duro** (función Python ejecutable en FunSearch, cota numérica medible en AlphaEvolve, prueba en Lean en AlphaProof). El verificador elimina alucinaciones por construcción.

**Aprovechable directamente:** este es el patrón correcto para el motor EDI. La métrica EDI = 1 - RMSE_coupled/RMSE_no_ode es un verificador formal duro; los hashes de `replay_hash.py` también lo son. Cualquier sub-agente que genere código de simulación, sondas alternativas, o configuraciones de caso, debe tener un verificador determinista (ejecuta validate.py, compara metric.json contra baseline) antes de aceptarse.

### 1.3 Anthropic Multi-Agent Research System (jun 2025)

Lead-agent (Opus) planifica y persiste plan en *memory*; subagentes (Sonnet) en paralelo con context windows propios; CitationAgent post-proceso para verificar citas. Coste 15× tokens vs single-agent; solo se justifica para tareas paralelizables de alto valor.

**Aprovechable:** (a) patrón orchestrator-worker para tareas de larga duración con memoria persistente; (b) **CitationAgent** es exactamente la pieza faltante para la regla §5 de CLAUDE.md ("cita textual con paginación o no cita"); (c) evaluación con LLM-as-judge sobre rubrics pequeñas (~20 ítems) en vez de benchmarks gigantes.

### 1.4 Building Effective Agents (Schluntz & Zhang, dic 2024)

Workflows vs agents. Patrones canónicos: prompt chaining, routing, parallelization (sectioning + voting), orchestrator-workers, evaluator-optimizer. Tesis central: **empieza simple; añade complejidad solo cuando la calidad lo exija**.

Esta es la regla rectora del diseño abajo. Cada componente se introduce solo si elimina una fricción concreta del §3.

### 1.5 Claude Agent SDK

Subagentes con frontmatter (`description, prompt, tools, model, permissionMode, hooks, mcpServers, isolation`). Hooks (`PreToolUse`, `PostToolUse`, `SessionStart`, `Stop`) permiten bloquear acciones destructivas. Permissions (`acceptEdits`, `plan`, `bypassPermissions`) + callback `canUseTool`.

**Aprovechable:** es la primitiva concreta de implementación. Cada sub-agente del harness es un `.claude/agents/<nombre>.md`. Hooks bloquean: (a) edición de `metrics.json` post-cómputo (preserva fuente de verdad numérica); (b) edición directa de `TesisFinal/Tesis.md` (que es derivado).

### 1.6 Sakana AI Scientist v2, Agent Laboratory, STORM

- **Sakana v2:** agentic tree search con Experiment Progress Manager + VLM feedback loop para figuras. Costo ~$15-20/run con Sonnet 3.5. Logró aceptación en workshop ICLR (no conferencia principal).
- **Agent Laboratory + AgentRxiv:** repositorio compartido entre agentes para acumular hallazgos.
- **STORM:** pre-writing en dos fases: descubrir perspectivas diversas, luego conversaciones simuladas perspectiva↔experto grounded en fuentes.

**Aprovechable:** el patrón de **perspectivas múltiples antes de escribir** (STORM) es la operacionalización exacta de la regla §6 de CLAUDE.md ("no te quedes en la formulación más débil de la objeción rival; busca la más fuerte"). Se incorpora al sub-agente de redacción filosófica.

**Descartable para esta tesis:** el ciclo end-to-end "idea→manuscrito" de Sakana v2. La voz autoral de Jacob no se delega a un pipeline; un Sakana-style cerrado violaría §3.

### 1.7 OpenAI Deep Research

o3 entrenado con RL end-to-end en browsing; corridas 5-30 min; tools mínimos (`search`, `fetch`). Útil como referencia de **trayectorias largas con backtracking aprendido**, pero no replicable sin acceso al modelo entrenado. Para esta tesis se aproxima con loops evaluator-optimizer explícitos.

---

## 2. Principios rectores del harness (no negociables)

Derivados directamente de CLAUDE.md, no inventados:

1. **Verificador formal antes que LLM-juez.** Cuando exista un verificador determinista (ejecuta script, compara hash, valida cita contra PDF), se usa. LLM-as-judge solo para lo que no admite verificación formal (calidad argumental, claridad), y siempre con rubric externa.
2. **Cero edición a fuentes de verdad sin checkpoint humano.** `metrics.json`, `case_config.json`, `TesisFinal/Tesis.md` (derivado) están protegidos por hooks. Solo se modifican vía pipelines declarados.
3. **Cada cifra que el harness reporta debe venir con su comando regenerador.** Si una cita o métrica no puede señalar el comando exacto, no se reporta.
4. **Memoria persistente entre pasadas, pero auditable.** Estado del harness en JSON/SQLite legible por humanos, no opaco.
5. **Las decisiones H-J* nunca las cierra el harness.** Se preparan, se argumentan, se ofrecen opciones con costos, pero la firma es humana.
6. **Cuotas de detención obligatorias.** Cada sub-agente tiene `maxTurns`, presupuesto de tokens y criterio de parada explícito. Una corrida larga que no converge se detiene y reporta fracaso, no continúa por inercia.
7. **Honestidad sobre la deuda.** Si una pasada larga produjo 70% de lo prometido, el reporte dice 70%, no 100% con asteriscos.

---

## 3. Mapa de fricción → componentes (justificación de cada pieza)

Solo componentes con fricción demostrable. Cada uno enuncia: nombre, fricción que resuelve, criterio de éxito verificable, costo estimado.

| # | Componente | Fricción real (del repo, no hipotética) | Criterio de éxito verificable | Costo |
|---|---|---|---|---|
| 1 | **Orquestador-tesis** (lead agent) | No hay coordinación entre auditoría técnica + ejecución masiva + verificación bibliográfica + síntesis. Cada tarea se hace a mano. | Una corrida larga ejecuta plan documentado, persiste estado, reanuda tras fallo, produce reporte verificable | Medio |
| 2 | **CitationAgent (verificador de paginación)** | 92 PDFs en `07-bibliografia/` sin vinculación automática. Regla §5 (cita con paginación o no cita) verificada manualmente. B-F1 bloqueado. | Para toda cita en prosa: encuentra pasaje en PDF, extrae página, marca discrepancias. Reporte JSON. | Medio |
| 3 | **Juez de defensibilidad (rubric hostil)** | Regla §2 (cierre solo si sobrevive crítica hostil) sin operacionalización. | Lista 10-15 preguntas hostiles por tipo de tarea (filosófica, técnica, bibliográfica). Falla = bloquea cierre. | Bajo |
| 4 | **Memoria persistente** (`harness/state.json` o SQLite) | Cada bitácora es registro post-hoc, no estado activo. No hay "qué se intentó, por qué falló, precondiciones para reintentar". | Estado consultable: tarea_id → {intentos, último_error, próxima_acción, requisito_humano} | Bajo |
| 5 | **Multi-sonda autom. sobre nulls** | 8 casos null sin re-análisis sistemático con sondas alternativas. `full_secondary_probes.py` existe pero no se ejecuta en grid. | Para cada null: 3-5 sondas alternativas físicamente motivadas, ejecutadas, reportadas. Decisión final humana. | Alto (GPU horas) |
| 6 | **Verificador prosa↔JSON** | Disonancias detectadas en B-E6 (3/30 casos). `auditoria_cientifica_profunda.py` detecta algunas; falta extracción regex de toda afirmación cuantitativa de prosa contra `metrics.json`. | Reporte: cada cifra en `Tesis.md` mapea a JSON específico. Discrepancia = falla CI. | Medio |
| 7 | **Validador de deuda residual** | Regla §7 exige sección "Deuda residual" en cada cap. No hay índice automatizado. | Índice JSON de deudas: por capítulo, fecha, descripción, tracking activo en `TAREAS_PENDIENTES.md`. | Bajo |
| 8 | **Detector de auto-indulgencia** | Patrones (versionología, "brutalmente honesto", plantillas spam, V5_FINAL) detectados a mano. | Linter sobre prosa nueva: lexicón de banderas + contexto. Reporte advisory, no bloqueante. | Bajo |
| 9 | **Cola de ejecución masiva con reintentos** | `run_all_validations_parallel.py` no maneja CUDA OOM ni reintentos inteligentes. Pasadas de horas pueden caer a la mitad. | Cola con flock, fallback CPU, reintentos exponenciales, estado persistente. Resume tras crash. | Medio |
| 10 | **Sub-agente lector filosófico** | Engagement profundo con fuentes primarias (B-F1: Bunge, Dennett, Simondon, Strawson, Chalmers, Goff, Lakatos) hecho a mano, con riesgo de cita decorativa. | Para autor: extrae argumento principal (cita+pág), localiza en disputa, propone borrador de engagement con costos declarados. Output siempre como **opción**, no decisión. | Alto |

**Componentes deliberadamente excluidos** (con razón):

- *Generador autónomo de prosa filosófica final.* Violaría §3 (voz autoral de Jacob).
- *Ranking Elo de hipótesis filosóficas.* Auto-evaluación circular, violaría §1.
- *Agente que cierre tareas H-J\*.* Violaría §3 explícitamente.
- *VLM feedback loop sobre figuras estilo Sakana v2.* Las figuras del repo se renderizan deterministamente con `render_mermaid.sh` y `number_tables.py`; añadir VLM agrega ruido sin valor.

---

## 4. Arquitectura propuesta

### 4.1 Topología

```
                       ┌─────────────────────────┐
                       │   Orquestador-tesis     │  (lead, Opus 4.7)
                       │   - lee CLAUDE.md       │
                       │   - lee TAREAS_PEND.md  │
                       │   - lee state.json      │
                       │   - planifica pasada    │
                       │   - persiste plan       │
                       └────────────┬────────────┘
                                    │ delega (paralelo)
        ┌───────────────┬───────────┼───────────┬────────────────┐
        ▼               ▼           ▼           ▼                ▼
  ┌─────────┐    ┌──────────┐ ┌──────────┐ ┌──────────┐  ┌─────────────┐
  │Citation │    │Multi-    │ │Verif.    │ │Lector    │  │Cola         │
  │Agent    │    │sonda     │ │prosa↔JSON│ │filosófico│  │ejecución    │
  │(Sonnet) │    │(Sonnet)  │ │(Sonnet)  │ │(Opus)    │  │(Sonnet)     │
  └────┬────┘    └────┬─────┘ └────┬─────┘ └────┬─────┘  └────┬────────┘
       │              │            │            │             │
       └──────────────┴────────────┴────────────┴─────────────┘
                                    │ resultados verificados
                                    ▼
                       ┌─────────────────────────┐
                       │ Juez de defensibilidad  │  (rubric hostil)
                       │ + Validador de deuda    │
                       │ + Detector autoindulg.  │
                       └────────────┬────────────┘
                                    │
                                    ▼
                       ┌─────────────────────────┐
                       │   Reporte de pasada     │  (bitácora honesta)
                       │   + actualización       │  (cerrado vs abierto)
                       │   TAREAS_PENDIENTES     │
                       │   + state.json          │
                       └────────────┬────────────┘
                                    │
                                    ▼
                       Checkpoint humano (Jacob/Steven firman cierres)
```

### 4.2 Implementación física

```
harness/
├── README.md                   # esta propuesta, tras firmar
├── orchestrator.py             # lead-agent loop + planificador + memoria
├── state.json                  # estado persistente entre pasadas
├── agents/                     # subagentes del Claude Agent SDK
│   ├── citation_agent.md
│   ├── prose_json_verifier.md
│   ├── multi_probe_runner.md
│   ├── philosophical_reader.md
│   ├── debt_validator.md
│   ├── self_indulgence_linter.md
│   └── execution_queue.md
├── rubrics/                    # criterios de defensibilidad
│   ├── philosophical_close.yaml   # 12-15 preguntas hostiles cap filosófico
│   ├── technical_close.yaml       # cierre de caso EDI
│   ├── bibliographic_close.yaml   # cierre de cita / engagement
│   └── debt_declaration.yaml      # validez de sección deuda residual
├── verifiers/                  # verificadores formales (no LLM)
│   ├── verify_citation_pagination.py   # extrae texto del PDF, busca match
│   ├── verify_prose_against_json.py    # regex cifras → match metrics.json
│   ├── verify_replay_hash.py           # ya existe en scripts; wrappear
│   └── verify_debt_index.py            # parsea Deuda residual de cada cap
├── hooks/                      # PreToolUse / PostToolUse / Stop
│   ├── block_metrics_edit.sh           # bloquea edición a metrics.json
│   ├── block_tesis_md_edit.sh          # bloquea edición a TesisFinal/Tesis.md
│   └── checkpoint_after_long_run.sh    # snapshot tras corrida >30min
└── reports/                    # reportes por pasada (ligados a Bitacora/)
    └── YYYY-MM-DD-pasada-NN.md
```

### 4.3 Modelo de pasada larga (long-horizon loop)

El harness opera en "pasadas". Una pasada típica de larga duración (4-12 horas autónomas, con checkpoints cada 30-60 min):

1. **Bootstrap (orquestador, ~5 min):**
   - Lee `CLAUDE.md`, `TAREAS_PENDIENTES.md`, `harness/state.json`, última bitácora.
   - Selecciona N tareas ejecutables (no `H-J*`) de TAREAS_PENDIENTES.md compatibles con el presupuesto de tiempo y tokens.
   - Genera plan (qué subagentes, qué orden, qué dependencias) y lo persiste a `state.json`.
   - Declara explícitamente: "esta pasada NO tocará X, Y, Z porque requieren firma humana".

2. **Ejecución (subagentes en paralelo donde sea posible, ~horas):**
   - Cada subagente ejecuta en aislamiento (`isolation: worktree` cuando edita), con `maxTurns` y presupuesto declarados.
   - Hooks `PreToolUse` bloquean ediciones prohibidas. Hooks `PostToolUse` registran cada acción a `state.json`.
   - Verificadores formales (no LLM) se ejecutan inline tras cada output: ¿la cita se encontró en el PDF? ¿la métrica reproduce el JSON? ¿el hash coincide?

3. **Evaluación (juez de defensibilidad, ~10 min):**
   - Para cada output de subagente, aplica la rubric correspondiente (hostil, externa, no auto-evaluativa).
   - Output marca cada item: `pass | fail | needs_human`.
   - Linter de auto-indulgencia escanea prosa nueva; reporta banderas (advisory).

4. **Reporte (~15 min):**
   - Bitácora honesta: cerrado vs abierto, costos asumidos, deuda nueva detectada.
   - Actualización de `TAREAS_PENDIENTES.md` y `state.json`.
   - Lista explícita de items `needs_human` para checkpoint.
   - Si la pasada falló al converger: reporte de fracaso con diagnóstico, no continuación por inercia.

5. **Checkpoint humano:** Jacob/Steven revisan `needs_human`. Lo aprobado se marca cerrado en TAREAS. Lo rechazado vuelve a la cola con feedback.

### 4.4 Long-horizon: cómo se sostiene una pasada de 8+ horas

Lecciones combinadas de Anthropic Research + AlphaProof + Sakana v2:

- **Plan persistido fuera del prompt** (memory tool) — sobrevive truncamiento de contexto.
- **Subagentes con context propio** — cada uno solo ve su sub-tarea, no el plan completo.
- **Checkpoints cada 30-60 min** — snapshot de `state.json` + git commit de outputs intermedios. Resume tras crash garantizado.
- **Detección activa de no-convergencia** — si tres iteraciones consecutivas no avanzan en una sub-tarea, se detiene y reporta. No bucle infinito.
- **Presupuesto de tokens explícito por sub-tarea**, no global — evita que un agente quemado consuma recursos de los demás.
- **Verificador formal en cada paso** — un agente no avanza al paso N+1 sin que el verificador haya confirmado el paso N.

---

## 5. Fases de implementación propuestas (no comprometidas — opciones)

Tres opciones, con costos:

### Opción A — Mínimo viable (1-2 semanas, ~30h ingeniería)

Solo: (1) orquestador básico, (2) CitationAgent + verifier, (3) verificador prosa↔JSON, (4) memoria JSON, (5) hooks de protección.

- **Resuelve:** B-F1 (citas con paginación), B-E6 (disonancia prosa↔JSON), reduce riesgo de edición destructiva.
- **No resuelve:** multi-sonda nulls, lector filosófico, cola masiva.
- **Riesgo:** bajo. Componentes aislados; cada uno se prueba solo.
- **Recomendación:** este es el escalón sano si la prioridad es defensibilidad bibliográfica antes de defensa.

### Opción B — Núcleo extendido (3-4 semanas, ~80h)

Opción A + (6) cola de ejecución masiva con reintentos + (7) multi-sonda automática sobre nulls + (8) juez de defensibilidad con rubrics + (9) validador de deuda.

- **Resuelve:** B-T1 a B-T7, deuda residual, anomalía caso 19.
- **Riesgo:** medio. La multi-sonda puede consumir GPU-horas sin convergir; necesita criterios de stop estrictos.
- **Recomendación:** si hay margen calendario y se quiere cerrar el motor EDI con auditoría exhaustiva.

### Opción C — Núcleo completo (6-8 semanas, ~150h)

Opción B + (10) lector filosófico de fuentes primarias + integración con biblioteca de PDFs + perspectivas STORM-style para prep de borradores.

- **Resuelve:** apoya B-F1 a B-F5 reduciendo carga sobre Jacob, sin sustituir su voz.
- **Riesgo:** alto. El lector filosófico es la pieza con más potencial de auto-indulgencia (cita decorativa, manierismo, falsa profundidad). Requiere disciplina estricta de prompts y rubrics, y revisión humana sin excepción.
- **Recomendación:** solo si Jacob declara explícitamente que necesita asistencia previa a engagement, y bajo protocolo de "borradores que él reescribe", no "borradores que él edita".

---

## 6. Costos asumidos y deuda declarada de esta propuesta

Cumpliendo §6 (marcar costos) y §7 (declarar deuda) de CLAUDE.md:

**Costos:**

- **Token cost real:** orchestrator-workers usa ~15× tokens vs single-agent (Anthropic, 2025). Una pasada de 8h con Opus puede costar varios cientos de USD. Esto debe entrar en presupuesto, no asumirse trivial.
- **Riesgo de meta-aparato:** el harness puede crecer en líneas de código y prosa de documentación más rápido que en valor entregado. Mitigación: cada componente debe haber cerrado al menos una tarea de TAREAS_PENDIENTES.md antes de añadir el siguiente.
- **Riesgo de drift autónomo:** una pasada larga puede divergir del objetivo si el plan inicial era frágil. Mitigación: cuotas de detención, checkpoints, no-convergencia explícita.
- **Riesgo epistémico (el más grave):** el lector filosófico (componente 10) puede producir prosa estructuralmente correcta sin contenido sustantivo — exactamente lo que CLAUDE.md §1 prohíbe. Si Jacob percibe esto en cualquier output, el componente se desactiva, no se "ajusta el prompt".

**Deuda residual de la propuesta misma:**

1. No se ha verificado empíricamente cuánto tarda una pasada larga real con esta arquitectura — los tiempos son estimaciones basadas en literatura, no en medición.
2. No se ha estimado el costo real en USD por pasada — depende de mix Opus/Sonnet y uso real.
3. No se ha decidido si el orquestador corre como script Python aislado o como sesión Claude Code con subagentes nativos. Ambas opciones tienen ventajas; pendiente discusión con Steven.
4. Falta diseñar el formato exacto de `state.json` — qué campos, qué granularidad, cómo se versiona.
5. Falta diseñar las rubrics concretas (`philosophical_close.yaml`, etc.). El esqueleto está; el contenido requiere iteración con Jacob.

---

## 7. Lo que se pide a Jacob/Steven

No firmas de cierre, solo decisiones de orientación:

1. **¿Cuál opción (A/B/C) corresponde al calendario y presupuesto reales?** O — válida — ¿ninguna, porque la prioridad es otra cosa?
2. **¿Steven prefiere implementar el orquestador como script Python o como sesión Claude Code con subagentes SDK?** Implica diferentes modos de despliegue.
3. **¿Hay piezas de §3 que no se justifican y deben eliminarse del alcance?** Mejor recortar antes de implementar que después.
4. **¿Hay fricciones reales no listadas en §3?** El mapeo se hizo desde código + TAREAS_PENDIENTES; puede haber fricciones tácitas que solo Jacob conoce.

Si la respuesta a (1) es "ninguna", esta propuesta queda como bitácora de exploración — sin código, sin commits a infraestructura — y se cierra abierta.

---

## 8. Fuentes (todas verificables, no decorativas)

### Anthropic
- "How we built our multi-agent research system" — https://www.anthropic.com/engineering/multi-agent-research-system
- "Building effective agents" (Schluntz & Zhang) — https://www.anthropic.com/research/building-effective-agents
- Claude Agent SDK — https://platform.claude.com/docs/en/agent-sdk/overview
- Constitutional AI (Bai et al.) — https://arxiv.org/abs/2212.08073

### Google / DeepMind
- AI co-scientist (Gottweis, Weng et al., 2025) — https://arxiv.org/abs/2502.18864
- Blog Google Research — https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/
- FunSearch (Romera-Paredes et al., Nature 2024) — https://www.nature.com/articles/s41586-023-06924-6
- AlphaEvolve — https://arxiv.org/abs/2506.13131
- AlphaProof (Nature 2025) — https://www.nature.com/articles/s41586-025-09833-y
- Crítica TechCrunch — https://techcrunch.com/2025/03/05/experts-dont-think-ai-is-ready-to-be-a-co-scientist/

### Otros
- Sakana AI Scientist v2 — https://arxiv.org/abs/2504.08066
- Agent Laboratory — https://arxiv.org/abs/2501.04227
- Stanford STORM — https://arxiv.org/pdf/2402.14207
- OpenAI Deep Research — https://openai.com/index/introducing-deep-research/
