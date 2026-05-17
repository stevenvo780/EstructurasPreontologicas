# Snapshot iter 12 — Loop nocturno 2026-05-17

## Snapshot técnico

| Métrica | Valor |
|---|---|
| Harness última pasada | 2026-05-05T02:21:38 (modo dry, 11 pasadas) |
| Verificadores 8/8 | 6 pass + 1 warn (citation_pagination) + 1 fail (decorative_citations) |
| Items needs_human | 1 (WARN_THESIS_VULNERABLE §5.5 cierre — pendiente Jacob) |
| Commits totales del loop (2026-05-16 → 17) | 21 |
| Commits iter 11→12 | 2 (`e5c85f4`, `4dd54e3`) |
| Casos con datos REAL/MIXTO (B-T2) | 32 de 40 (auditoría `auditoria-cobertura-B-T2.md`) |
| Casos `strong` (grep metrics.json) | 10 |
| Casos con `n=15` reportado | 4 (discrepancia vs claim iter 8) |
| Discrepancias pre-registro detectadas | 2 confirmadas + 3 validaciones honestas |
| BORRADOR-IA pendientes (bitácoras) | 9 referenciadas |
| BORRADOR-IA marcas totales (repo) | 32 archivos |
| Engagements filosóficos (loop) | 10+ (Bunge, Searle, Dennett, Yablo, Simondon, Ladyman-Ross, Chalmers, Goff, Mouffe, Whitehead PR+AI) |
| Adversariales documentados | 3 (irrealismo §5.5, n=15, upgrades iter 12) |

## Análisis filosófico final

**Pregunta clave: ¿La tesis está en mejor posición tras 12 iteraciones?**

**A favor (la honestidad creció):**
- De 0 a 10 casos `strong` con datos reales auditables.
- 5 pre-registros aplicados; 2 discrepancias autoconfesas + 3 validaciones honestas (popperianismo activo, no decorativo).
- Engagement filosófico profundo con 10+ autores primarios (verbatim paginado).
- 3 adversariales documentados con correcciones aplicadas (Friston como rival #16, multi-probe caso 15 confirma null, concesión a Dennett).
- Bibliografía expandida: Schrödinger, Gelman, Yablo, Whitehead (PR+AI).

**En contra (la exposición creció):**
- Adversarial iter 12 es **devastador**: bug aparato (`detrended_edi == edi`) + permutación iid en lugar de block → si se confirma, los 6 upgrades colapsan.
- Pre-registros son lock-in **post-hoc autoconfesos** — Gelman (p.464) los descalifica explícitamente como evidencia confirmatoria.
- 23 autores citados sin entrada bibliográfica (deuda B-T1 abierta).
- Caso 30 ejecutó con `config.yaml` modificado **post-sello** (violación de protocolo de pre-registro).
- §5.5 del cierre sigue marcada `WARN_THESIS_VULNERABLE` (Jacob no ha firmado).

**Veredicto operativo:** La tesis está **más honesta pero más expuesta**. Las correcciones del loop hicieron visible debilidad estructural que estaba latente. Es la dirección correcta (honestidad > apariencia) pero **la posición defensiva final depende íntegramente de iter 13**: si el bug `detrended_edi` se confirma y los upgrades se reclasifican, la cuenta de `strong` baja y hay que reescribir prosa correspondiente. Si no se atiende, el adversarial queda como deuda crítica visible en el manuscrito.

## 5 acciones prioritarias iter 13-14

1. **Auditar bug `detrended_edi == edi`** en el aparato de upgrades (`harness/` + `09-simulaciones-edi/<NN>/src/validate.py`). Si confirmado: reclasificar los 6 upgrades y propagar a prosa.
2. **Cambiar permutación iid → block permutation** en casos con autocorrelación temporal (clima, finanzas, deforestación, oceanos). Recalcular `p_perm`.
3. **Reabrir caso 30**: re-ejecutar con `config.yaml` original sellado o documentar la modificación como deuda B-T1 fechada con justificación.
4. **Cerrar 23 entradas biblio faltantes** o degradar a "cita secundaria" explícita (Jacob decide). No pueden quedar citas decorativas en defensa.
5. **Resolver `WARN_THESIS_VULNERABLE` §5.5**: Jacob firma una de las tres salidas propuestas en `Bitacora/2026-05-16-adversarial-irrealismo-operativo/red-team.md` (recomendada: reposicionar como operativización de Dennett, no "tercera vía").
