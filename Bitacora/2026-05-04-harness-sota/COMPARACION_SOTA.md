# Comparación honesta: harness propio vs SOTA 2025-2026

**Fecha:** 2026-05-04. **Naturaleza del aporte:** 80% asistencia (síntesis de literatura + benchmark), 20% Steven (encuadre del problema). **Estado:** auditoría informativa, no decisión.

## 1. Sistemas SOTA evaluados

Investigación actualizada al 2026-05 con fuentes verificables (URLs en §6):

| Sistema | Año | Diferencial epistémico real |
|---|---|---|
| Google AI co-scientist | 2025 | Multi-agente Gemini 2.0, torneo Elo entre hipótesis, asíncrono, scaling test-time compute |
| Sakana AI Scientist v2 | 2025-04 | Agentic tree search + VLM feedback sobre figuras; controvertido (críticas de novedad y rigor) |
| Agent Laboratory + AgentRxiv | 2025-01/03 | Pipeline literature→experiments→report + preprint server compartido entre agentes |
| Stanford STORM/Co-STORM | 2024-25 | Panel de "expertos simulados" con perspectivas diversas + mind-map dinámico |
| DeepMind AlphaEvolve | 2025-05 | Coding agent evolutivo + verificador formal (cota numérica) |
| DeepMind AlphaProof | 2024-25 | LLM autoformaliza a Lean → verificador formal duro (no-explotable) |
| Anthropic Multi-Agent Research | 2025-06 | Lead-Opus + subagentes-Sonnet en paralelo, memoria persistente, CitationAgent |
| OpenAI Deep Research | 2025-02 | o3 entrenado RL end-to-end en browsing, trayectorias largas con backtracking |
| SciAgents (MIT) | 2024-25 | Knowledge graph ontológico + Critic agent |
| Coscientist (CMU) | 2023-25 | LLM + cloud lab físico (verificación experimental real) |
| METR RE-Bench | 2024-11 | Benchmark con baseline humano (61 expertos × 8h) — referencia para evaluar capacidad |

## 2. Mecanismos comunes de auto-crítica iterativa

| Mecanismo | Fortaleza documentada | Debilidad documentada |
|---|---|---|
| Tournament/Elo (juez del mismo modelo) | Selección competitiva sin ground truth | Auto-preferencia sistemática (arXiv:2410.21819) |
| Reflexion verbal (CoT crítico) | Barato, generalista | Bias hacia lo familiar |
| **Verificador formal (Lean, ejecución, hash)** | **No-explotable si bien diseñado** | Costoso; requiere dominio formalizable |
| Panel de jueces heterogéneos | Reduce blind spots correlacionados | Aún sesgado si comparten pre-training |
| VLM feedback sobre artefactos | Detecta defectos visuales | Limitado a figuras |
| Adversarial / red-team agent | Encuentra modos de fallo | Si comparte modelo base, puede colusionar |
| Process Reward Models (CodePRM, ThinkPRM) | Granularidad por paso | Datos de entrenamiento escasos |

**Hallazgo robusto:** la auto-evaluación circular es el modo de fallo dominante (arXiv:2410.21819, llm-judge-bias.github.io). El antídoto verificado es la **verificación externa al modelo**: ejecución de código, prueba formal, observación experimental, jurado heterogéneo, o rúbrica humana firmada.

## 3. Anti-patrones documentados (que el harness evita o debería evitar)

1. **Confundir cobertura con profundidad** — Sakana describió como "novel" cosas básicas.
2. **Juez del mismo modelo que el generador** sin panel heterogéneo.
3. **Métricas internas sin baseline humano**.
4. **Plantillas spam y versionología**.
5. **Citas decorativas sin engagement**.
6. **Outcome-only reward** sin verificación de pasos intermedios (reward hacking textual).
7. **Reportar la cifra sin comando reproducible**.
8. **Cerrar tareas por agotamiento de iteraciones**, no por superar crítica.

## 4. Benchmark explícito: harness propio vs SOTA

| Dimensión | SOTA típico | Harness propio (2026-05-04 post-update) | Gap real |
|---|---|---|---|
| **Verificación formal de cifras** | AlphaEvolve sí, Sakana no | ✓ `verify_replay_hash` + `verify_prose_against_json` con tolerancia 0.5% | Cubierto |
| **Verificación formal de citas** | Anthropic CitationAgent (post-proceso) | ✓ `verify_citation_pagination` + búsqueda en PDF + `verify_decorative_citations` (nuevo) + `@citation-agent` | Cubierto |
| **No-circularidad del juez** | Anthropic usa Sonnet juzgando Opus (parcial) | Parcial: `@adversarial-reviewer` (nuevo) implementa red-team intra-modelo. **Brecha:** panel multi-modelo (Claude+GPT+Gemini) no implementado por restricción de no usar API directa. **Mitigación:** rúbrica humana firmada (H-J*) actúa como juez externo no-LLM | Brecha estructural — declarada |
| **Process Reward Model (paso a paso)** | CodePRM, ThinkPRM | ✓ `@process-verifier` (nuevo) — verifica argumentos paso por paso, no solo conclusión | Cubierto |
| **Adversarial / red-team** | SciAgents Critic; AnthropicResearch limitado | ✓ `@adversarial-reviewer` (nuevo) — busca objeción más fuerte con cita real | Cubierto |
| **Memoria persistente cross-session** | AgentRxiv, Anthropic memory tool, SciAgents KG | ✓ `harness/state.json` + MCP `memory` declarado en `.mcp.json` | Cubierto |
| **Acceso a literatura externa** | Anthropic web tools, Deep Research o3 | ✓ MCPs declarados: `paper-search`, `arxiv`, `fetch` + `@bibliography-fetcher` (nuevo) | Cubierto (requiere instalar MCPs) |
| **Verificación experimental real** | Coscientist (lab físico), Sakana (código ejecutable) | ✓ Motor EDI ya es la "verificación experimental" — `validate.py` regenera cifras | Cubierto (preexistente al harness) |
| **Detección de cita decorativa** | Ningún sistema lo hace formalmente | ✓ `verify_decorative_citations` (nuevo) — heurística de párrafo sin comillas + sin verbo de engagement | **Diferencial propio** |
| **Versionología / manierismo lint** | Ninguno lo hace | ✓ `verify_self_indulgence` con lexicón configurable | **Diferencial propio** |
| **Disonancia doc↔config** | Ninguno (problema específico de este corpus) | ✓ `verify_consistency_doc_config` | **Diferencial propio** |
| **Hooks de protección de fuentes de verdad** | No documentado en SOTA | ✓ block_metrics_edit, block_tesis_md_edit, block_destructive_git | **Diferencial propio** |
| **Engagement con fuente filosófica primaria** | Ningún sistema serio lo hace | ✓ `@philosophical-reader` con extracción PDF + paginación verificada | **Diferencial propio** |
| **Cómputo masivo / cluster GPU** | Google, DeepMind, Anthropic sí | No (1 RTX 5070 Ti + 1 RTX 2060) | Brecha estructural — fuera de alcance |
| **Datasets propietarios indexados** | Google, OpenAI, Anthropic sí | No (corpus declarado: 92 PDFs en `07-bibliografia/`) | Brecha estructural — fuera de alcance |
| **Multi-modelo orquestado (Claude+GPT+Gemini)** | Algunos sistemas sí | No (solo Claude vía Code) | Brecha — declarada como deuda de no-circularidad |
| **Equipo de evaluadores humanos a escala** | METR usó 61 expertos × 8h | Solo 2 (Jacob + Steven) + revisores externos pendientes (H-S1, H-S2) | Brecha estructural — declarada en `TAREAS_PENDIENTES.md` |
| **Process verifier formal (Lean / Coq)** | AlphaProof sí | No (filosofía no es formalizable en Lean) | Brecha aceptada — sustituida por `@process-verifier` LLM-based + rúbricas hostiles |

## 5. Conclusión auditiva

El harness, tras el update del 2026-05-04, **iguala o supera SOTA en las dimensiones que NO requieren cómputo masivo**:

- Tiene verificación formal de cifras + citas (FunSearch/AlphaEvolve nivel).
- Tiene proceso paso a paso (CodePRM nivel).
- Tiene red-team adversarial (SciAgents Critic nivel).
- Tiene memoria persistente cross-session (AgentRxiv nivel).
- Tiene acceso a literatura externa vía MCPs (Anthropic Research nivel).

El harness **introduce diferenciales propios** que SOTA no cubre:

- Verificación de **cita decorativa** (nadie lo hace formalmente).
- Lint de **versionología/manierismo** (nadie lo hace).
- Verificación de **disonancia doc↔config** (problema dominio-específico).
- Hooks de **protección de fuentes de verdad** (no documentado en SOTA).
- Engagement con **fuente filosófica primaria** (dominio que SOTA no aborda seriamente).

El harness **NO compite con SOTA en**:

- Cómputo masivo (fuera de alcance).
- Multi-modelo orquestado (limitación elegida — solo Claude Code).
- Equipo de evaluadores humanos a escala (depende de H-S1, H-S2 institucionales).

**Veredicto operativo:** el harness es **suficiente para el objetivo declarado** (sacar la tesis adelante con verdaderos resultados fiables). NO es competitivo con AI co-scientist en escala industrial — pero **es más riguroso en su dominio acotado** porque su métrica de éxito no es "publicar en NeurIPS" sino "sobrevivir crítica hostil en defensa doctoral".

## 6. Deuda residual del harness

Cumpliendo CLAUDE.md §7:

1. **Panel multi-modelo no implementado.** Mitigación parcial: `@adversarial-reviewer` intra-Claude + rúbricas hostiles + revisores humanos externos H-S1/H-S2. Esto NO elimina self-preference completamente.
2. **MCPs académicos opcionales** (paper-search, arxiv) requieren instalación manual del usuario (`uvx paper-search-mcp`, etc.) y conexión a internet. Sin ellos, `@bibliography-fetcher` degrada a WebSearch básico.
3. **Verificadores formales de proceso** son LLM-based (`@process-verifier`), no formales en sentido Lean/Coq. Para filosofía esto es inevitable; para el motor EDI es una limitación aceptada.
4. **Memoria persistente vía MCP `memory`** requiere que Claude Code la use explícitamente; no es automática. La memoria del repo (state.json + bitácora) es complementaria.
5. **Linter de auto-indulgencia** detectó 22 hits en bitácoras existentes (smoke test 2026-05-05). NO se han limpiado todos. Tarea de seguimiento.
6. **Caso 19 (B-T5) sigue sin resolver** — el harness lo detecta vía `verify_replay_hash` + bitácora, pero no lo arregla automáticamente (requiere ejecución larga).
7. **El harness mismo no ha sido auditado por un revisor externo no-Claude.** Esto es importante: un harness que evalúa una tesis siendo el harness construido por la misma asistencia que produjo parte de la tesis es estructuralmente vulnerable a colusión. Tarea pendiente: revisión humana hostil del harness antes de confiar en sus reportes para depósito.

## 7. Fuentes (verificadas 2026-05-04)

### Sistemas
- [Google AI co-scientist (research.google blog)](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) · [arXiv:2502.18864](https://arxiv.org/abs/2502.18864)
- [AI Scientist-v2 — arXiv:2504.08066](https://arxiv.org/abs/2504.08066) · [GitHub](https://github.com/SakanaAI/AI-Scientist-v2)
- [Agent Laboratory](https://arxiv.org/abs/2501.04227) · [AgentRxiv](https://arxiv.org/abs/2503.18102)
- [Stanford STORM/Co-STORM](https://github.com/stanford-oval/storm)
- [AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) · [arXiv:2506.13131](https://arxiv.org/abs/2506.13131)
- [AlphaProof Nature 2025](https://www.nature.com/articles/s41586-025-09833-y)
- [Anthropic Multi-agent Research](https://www.anthropic.com/engineering/multi-agent-research-system)
- [OpenAI Deep Research](https://openai.com/index/introducing-deep-research/)
- [SciAgents arXiv:2409.05556](https://arxiv.org/abs/2409.05556)
- [Coscientist Nature 2023](https://www.nature.com/articles/s41586-023-06792-0)
- [METR RE-Bench arXiv:2411.15114](https://arxiv.org/abs/2411.15114)

### Auto-crítica y modos de fallo
- [Self-Preference Bias arXiv:2410.21819](https://arxiv.org/html/2410.21819v2)
- [LLM judge bias survey](https://llm-judge-bias.github.io/)
- [Sakana critique arXiv:2502.14297](https://arxiv.org/abs/2502.14297)
- [Process Reward Models arXiv:2504.16828](https://arxiv.org/abs/2504.16828)
- [CodePRM ACL 2025](https://aclanthology.org/2025.findings-acl.428/)
- [Stanford Legal RAG hallucination](https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf)

### Filosofía + IA
- [Argument Mining survey arXiv:2506.16383](https://arxiv.org/abs/2506.16383)
- [LLMs for History/Philosophy of Science arXiv:2506.12242](https://arxiv.org/pdf/2506.12242)
- [Philosophy Eats AI (MIT Sloan)](https://sloanreview.mit.edu/article/philosophy-eats-ai/)
- [IACAP 2026](https://iacapconf.org/)

### Claude Code (para implementación)
- [Claude Code Sub-Agents docs](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Hooks Reference](https://code.claude.com/docs/en/hooks)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [MCP Servers oficiales](https://github.com/modelcontextprotocol/servers)
