"""Auto-generación de tareas para el modo continuo.

El plan estático en `harness/plans/autonomous_workplan.yaml` solo tiene ~17 tareas.
Para sesiones de 80-150 horas necesitamos generar tareas a partir de la salida
real de los verificadores. Cada hit (cita sin paginación, mención decorativa,
list dump) se convierte en UNA tarea ejecutable autónomamente.

Reglas:
  - Sólo se generan tareas seguras (engagement / audit). Nunca toca metrics.json
    ni Tesis.md.
  - Los IDs son deterministas (hash corto del file:line:autor) para evitar
    duplicados al replenish múltiples veces.
  - Si una tarea ya existe en el state (cualquier status), no se re-añade.
"""
from __future__ import annotations
import hashlib
import re
import sys
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.verifiers import verify_citation_pagination as vcp
from harness.verifiers import verify_decorative_citations as vdc
from harness.verifiers import verify_debt_index as vdi
from harness.verifiers import verify_consistency_doc_config as vcc
from harness.verifiers import verify_self_indulgence as vsi


def _stable_id(prefix: str, *parts: str) -> str:
    h = hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:8]
    return f"{prefix}-{h}"


def _slug(s: str, n: int = 20) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-")[:n].lower() or "x"


def generate_pagination_tasks() -> list[dict]:
    r = vcp.main(verbose=True)
    out = []
    for hit in r.get("without_pagination_full", []):
        f, line, autor = hit["file"], hit["line"], hit["autor"]
        tid = _stable_id("AP", f, str(line), autor)
        out.append({
            "id": tid,
            "subject": f"Paginación {autor} en {f}:{line}",
            "priority": 2,
            "est_minutes": 15,
            "action": {
                "kind": "engagement",
                "target_file": f,
                "target_line": line,
                "author": autor,
                "strategy": (
                    f"Buscar PDF de {autor} en 07-bibliografia/. Si existe, "
                    f"extraer cita textual con paginación verbatim y editar "
                    f"{f} en la línea {line}. Si NO existe PDF, reformular como "
                    f"mención secundaria declarada (CLAUDE.md §5). NO inventar "
                    f"paginación. NO editar Tesis.md ni metrics.json (hooks bloquean)."
                ),
            },
            "touches": [f],
            "acceptance": "cita textual con pp. verificada contra PDF, o reformulación secundaria declarada con deuda",
            "_generated": True,
        })
    return out


def generate_missing_pdf_tasks() -> list[dict]:
    """Citas cuyo autor no aparece en 07-bibliografia/.
    Acción: intentar fetch-biblio externo (arXiv/Semantic Scholar) o reformular
    como mención secundaria declarada.
    """
    r = vcp.main(verbose=True)
    out = []
    for hit in r.get("without_pdf_in_07_full", []):
        f, line, autor = hit["file"], hit["line"], hit["autor"]
        if not autor or autor.lower() in ("nivel", "ver", "cf", "et"):
            continue
        tid = _stable_id("AM", f, str(line), autor)
        out.append({
            "id": tid,
            "subject": f"PDF ausente para {autor} en {f}:{line}",
            "priority": 3,
            "est_minutes": 20,
            "action": {
                "kind": "engagement",
                "target_file": f,
                "target_line": line,
                "author": autor,
                "strategy": (
                    f"Autor {autor} citado en {f}:{line} pero sin PDF en "
                    f"07-bibliografia/. Opciones: (a) intentar bibliography-fetcher "
                    f"contra arXiv/Semantic Scholar/OpenAlex; si recupera PDF, "
                    f"depositarlo y agregar paginación verbatim; (b) reformular "
                    f"como mención secundaria declarada (CLAUDE.md §5) con cita "
                    f"a fuente disponible. NO inventar paginación."
                ),
            },
            "touches": [f],
            "acceptance": "PDF añadido a 07-bibliografia/ con paginación verbatim, o mención secundaria declarada",
            "_generated": True,
        })
    return out


def generate_decorative_tasks() -> list[dict]:
    r = vdc.main()
    out = []
    for hit in r.get("decorative_suspect_full", []):
        f, line = hit["file"], hit["line"]
        cits = hit.get("citations", []) or ["?"]
        autor = cits[0]
        tid = _stable_id("AD", f, str(line), autor)
        out.append({
            "id": tid,
            "subject": f"Decorativa→engagement {autor} en {f}:{line}",
            "priority": 3,
            "est_minutes": 25,
            "action": {
                "kind": "engagement",
                "target_file": f,
                "target_line": line,
                "author": autor,
                "citations": cits,
                "snippet": hit.get("snippet", ""),
                "strategy": (
                    f"En {f}:{line} la cita {cits} aparece como decorativa "
                    f"(sin comillas ni verbo de engagement). Convertir a engagement: "
                    f"agregar cita textual paginada (verificada contra PDF en "
                    f"07-bibliografia/) o explicar técnicamente el argumento del "
                    f"autor. Si no hay PDF, reformular como mención secundaria. "
                    f"NO Tesis.md, NO metrics.json."
                ),
            },
            "touches": [f],
            "acceptance": "párrafo contiene cita textual paginada o explicación técnica del argumento del autor",
            "_generated": True,
        })
    for hit in r.get("list_dump_full", []):
        f, line = hit["file"], hit["line"]
        cits = hit.get("citations", []) or ["?"]
        tid = _stable_id("AL", f, str(line), "_".join(cits[:3]))
        out.append({
            "id": tid,
            "subject": f"List-dump→engagement individual en {f}:{line}",
            "priority": 3,
            "est_minutes": 35,
            "action": {
                "kind": "engagement",
                "target_file": f,
                "target_line": line,
                "authors": cits,
                "snippet": hit.get("snippet", ""),
                "strategy": (
                    f"En {f}:{line} hay una lista de >3 autores agrupados sin "
                    f"engagement individual ({cits}). Romper la lista: para cada "
                    f"autor, dar una cláusula con su posición específica y, "
                    f"cuando sea posible, cita textual paginada. Conservar "
                    f"economía argumental — si dos autores comparten posición, "
                    f"agruparlos explícitamente. NO Tesis.md, NO metrics.json."
                ),
            },
            "touches": [f],
            "acceptance": "cada autor citado tiene engagement diferenciado o agrupación explícita justificada",
            "_generated": True,
        })
    return out


def generate_debt_tasks() -> list[dict]:
    """Capítulos sin sección Deuda residual fechada (CLAUDE.md §7)."""
    r = vdi.main()
    out = []
    for ch in r.get("required_chapters_missing_debt", []):
        tid = _stable_id("DB", ch, "missing")
        out.append({
            "id": tid,
            "subject": f"Deuda residual ausente en {ch}",
            "priority": 2,
            "est_minutes": 25,
            "action": {
                "kind": "engagement",
                "target_file": ch,
                "strategy": (
                    f"El capítulo {ch} no declara sección 'Deuda residual' fechada. "
                    f"Auditar el capítulo y proponer una sección Deuda residual con "
                    f"items concretos fechados (CLAUDE.md §7). NO inventar items — "
                    f"deben derivarse del contenido real del capítulo y de hits de "
                    f"verificadores. Marcar BORRADOR-IA con requires: H-J*."
                ),
            },
            "touches": [ch],
            "acceptance": "sección 'Deuda residual' fechada con items concretos derivados de auditoría real",
            "_generated": True,
        })
    for hit in r.get("debt_sections_without_date_sample", []):
        ch = hit.get("file") if isinstance(hit, dict) else str(hit)
        if not ch:
            continue
        tid = _stable_id("DD", ch, "undated")
        out.append({
            "id": tid,
            "subject": f"Deuda sin fecha en {ch}",
            "priority": 3,
            "est_minutes": 10,
            "action": {
                "kind": "engagement",
                "target_file": ch,
                "strategy": (
                    f"La sección Deuda residual de {ch} no tiene fecha. Añadir "
                    f"fecha actual (YYYY-MM-DD) al header de la sección. NO "
                    f"reescribir el contenido."
                ),
            },
            "touches": [ch],
            "acceptance": "header 'Deuda residual' contiene fecha YYYY-MM-DD",
            "_generated": True,
        })
    return out


def generate_doc_config_tasks() -> list[dict]:
    """Discordancias doc↔config (B-T6)."""
    r = vcc.main()
    out = []
    for hit in r.get("discordances", []):
        case = hit.get("case", "?") if isinstance(hit, dict) else str(hit)
        tid = _stable_id("DC", case)
        out.append({
            "id": tid,
            "subject": f"Discordancia doc↔config en caso {case}",
            "priority": 2,
            "est_minutes": 30,
            "action": {
                "kind": "audit",
                "target_case": case,
                "strategy": (
                    f"Caso {case}: discordancia entre doc y case_config.json. "
                    f"Detalle: {hit}. Producir reporte en Bitacora/<fecha>-continuous-run/"
                    f"doc-config-{case}.md con (a) cambiar config, (b) cambiar doc, "
                    f"(c) ambas, con costo declarado. NO editar metrics.json. "
                    f"Marcar needs_human."
                ),
            },
            "touches": [],
            "acceptance": "reporte de discordancia con propuesta de salida y costo",
            "_generated": True,
        })
    return out


def generate_indulgence_tasks() -> list[dict]:
    """Hits de auto-indulgencia (CLAUDE.md §1)."""
    r = vsi.main()
    out = []
    for hit in r.get("flag_hits_sample", []):
        if not isinstance(hit, dict):
            continue
        f = hit.get("file", "")
        line = hit.get("line", 0)
        pat = hit.get("pattern", hit.get("match", "?"))
        if not f:
            continue
        tid = _stable_id("SI", f, str(line), str(pat)[:20])
        out.append({
            "id": tid,
            "subject": f"Auto-indulgencia '{str(pat)[:30]}' en {f}:{line}",
            "priority": 3,
            "est_minutes": 10,
            "action": {
                "kind": "engagement",
                "target_file": f,
                "target_line": line,
                "strategy": (
                    f"En {f}:{line} hay patrón de auto-indulgencia ({pat}). "
                    f"Aplicar CLAUDE.md §1: si el adjetivo es removible y la oración "
                    f"sobrevive, eliminarlo; si el sustantivo es manierista (versionología, "
                    f"'8/8 verdes', 'brutalmente honesto'), reformular sin adjetivo. "
                    f"NO Tesis.md, NO metrics.json."
                ),
            },
            "touches": [f],
            "acceptance": "patrón eliminado y oración sobrevive sin pérdida de contenido",
            "_generated": True,
        })
    return out


def generate_all() -> list[dict]:
    out = []
    out.extend(generate_pagination_tasks())
    out.extend(generate_missing_pdf_tasks())
    out.extend(generate_decorative_tasks())
    out.extend(generate_debt_tasks())
    out.extend(generate_doc_config_tasks())
    out.extend(generate_indulgence_tasks())
    return out


def existing_ids(state: dict) -> set[str]:
    return {t["id"] for t in state.get("tasks", [])}


def replenish(state: dict, max_new: int = 200) -> int:
    """Añade tareas generadas al state, sin duplicar. Devuelve cuántas añadió."""
    have = existing_ids(state)
    new = [t for t in generate_all() if t["id"] not in have]
    new = new[:max_new]
    for t in new:
        state["tasks"].append({
            "id": t["id"],
            "subject": t["subject"],
            "priority": t["priority"],
            "est_minutes": t["est_minutes"],
            "status": "pending",
            "started_at": None,
            "finished_at": None,
            "result": None,
            "notes": [],
        })
    return len(new)


def task_action_for(task_id: str) -> dict | None:
    """Resuelve action para una tarea generada (no en YAML estático)."""
    for t in generate_all():
        if t["id"] == task_id:
            return t
    return None


if __name__ == "__main__":
    import json
    tasks = generate_all()
    print(f"# {len(tasks)} tareas generadas")
    for t in tasks[:5]:
        print(json.dumps(t, indent=2, ensure_ascii=False))
