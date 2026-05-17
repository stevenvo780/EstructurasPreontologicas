from __future__ import annotations

import argparse
import copy
import json
import sys
import subprocess
from pathlib import Path
from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from web_tesis.data import (
        ROOT as DATA_ROOT,
        SIM_ROOT,
        VIS_ROOT,
        case_docs_rendered,
        case_math_explainer_html,
        case_readme_html,
        case_report_html,
        get_dataset,
        refresh_dataset,
        resolve_case,
        resolve_chapter,
        resolve_chapter_extra,
        render_markdown,
        render_markdown_with_toc,
    )
except ImportError:
    from data import (  # type: ignore
        ROOT as DATA_ROOT,
        SIM_ROOT,
        VIS_ROOT,
        case_docs_rendered,
        case_math_explainer_html,
        case_readme_html,
        case_report_html,
        get_dataset,
        refresh_dataset,
        resolve_case,
        resolve_chapter,
        resolve_chapter_extra,
        render_markdown,
        render_markdown_with_toc,
    )

APP_DIR = Path(__file__).resolve().parent
# En despliegue Vercel los estáticos viven en /public; en desarrollo local
# generamos a web_react/dist con `npm run build`. El servidor FastAPI escoge
# la ubicación que exista (público > dist).
_REACT_PUBLIC = ROOT / "public"
_REACT_DIST = ROOT / "web_react" / "dist"
if _REACT_PUBLIC.exists() and (_REACT_PUBLIC / "index.html").exists():
    REACT_DIST = _REACT_PUBLIC
elif _REACT_DIST.exists() and (_REACT_DIST / "index.html").exists():
    REACT_DIST = _REACT_DIST
else:
    REACT_DIST = _REACT_DIST  # default, USE_REACT será False
USE_REACT = (REACT_DIST / "index.html").exists()


def _asset_version() -> str:
    """mtime de app.css como versión cache-bust del navegador."""
    css = APP_DIR / "static" / "css" / "app.css"
    try:
        return str(int(css.stat().st_mtime))
    except OSError:
        return "1"


app = FastAPI(
    title="Estructuras Pre-Ontológicas — Visual",
    description="Capa web para la tesis: API JSON + SPA React",
    version="2.0.0",
)

templates = Jinja2Templates(directory=str(APP_DIR / "templates"))

app.mount(
    "/legacy_static",
    StaticFiles(directory=str(APP_DIR / "static")),
    name="static",  # nombre `static` para compatibilidad con templates Jinja2 legacy
)

if USE_REACT:
    # Servir assets compilados con hash desde web_react/dist/assets/
    app.mount(
        "/assets",
        StaticFiles(directory=str(REACT_DIST / "assets")),
        name="react_assets",
    )

if VIS_ROOT.exists():
    app.mount("/visualizations", StaticFiles(directory=str(VIS_ROOT)), name="visualizations")
app.mount("/sim_files", StaticFiles(directory=str(SIM_ROOT)), name="sim_files")
app.mount("/repo_files", StaticFiles(directory=str(DATA_ROOT)), name="repo_files")


# ─── Helpers de serialización para la API JSON nueva ──────────────────────────


def _case_summary_dict(case: dict[str, Any]) -> dict[str, Any]:
    """Forma compacta para listados (sin reportes ni docs renderizados)."""
    metrics = case.get("metrics", {})
    return {
        "case_id": case.get("case_name"),
        "case_name": case.get("case_name"),
        "sim_path": case.get("sim_path", case.get("case_name")),
        "scope": case.get("scope"),
        "case_num": case.get("case_num"),
        "title": case.get("title"),
        "scale": case.get("scale"),
        "category": metrics.get("category"),
        "metrics": {
            "edi": metrics.get("edi"),
            "pvalue": metrics.get("pvalue"),
            "cr": metrics.get("cr"),
            "overall_pass": bool(metrics.get("overall_pass")),
            "nivel": metrics.get("nivel"),
            "category": metrics.get("category"),
        },
        "meta": case.get("meta", {}),
    }


def _phases_compact_dict(case: dict[str, Any]) -> dict[str, Any]:
    """Subset comparable de fases (synthetic vs real) para la UI.

    Solo expone los campos que el panel comparativo necesita: EDI, p-perm,
    IC95, categoría/nivel y overall_pass. Mantiene phase_order canónico.
    """
    phases = case.get("phases") or {}
    if not isinstance(phases, dict):
        return {}
    out: dict[str, Any] = {}
    for name, ph in phases.items():
        if not isinstance(ph, dict):
            continue
        edi = ph.get("edi") or {}
        sym = ph.get("symploke") or {}
        tax = ph.get("taxonomy") or {}
        out[name] = {
            "overall_pass": bool(ph.get("overall_pass", False)),
            "edi": edi.get("value"),
            "edi_ci_lo": edi.get("ci_lo"),
            "edi_ci_hi": edi.get("ci_hi"),
            "pvalue": edi.get("pvalue"),
            "significant": edi.get("significant"),
            "cr": sym.get("cr"),
            "category": tax.get("category"),
            "nivel": tax.get("nivel"),
        }
    return out


def _load_primary_arrays(case_name: str) -> dict[str, Any] | None:
    """Carga primary_arrays.json si existe; devuelve solo la fase real."""
    pa_path = SIM_ROOT / case_name / "outputs" / "primary_arrays.json"
    if not pa_path.exists():
        # corpus_multiescala
        pa_path = SIM_ROOT / "corpus_multiescala" / case_name / "outputs" / "primary_arrays.json"
    if not pa_path.exists():
        return None
    try:
        data = json.loads(pa_path.read_text(encoding="utf-8"))
        arrays = data.get("arrays", {})
        # algunas variantes anidan por fase
        if isinstance(arrays, dict) and arrays.get("real"):
            arrays = arrays["real"]
        keep = {}
        for k in ("obs", "abm_coupled", "abm_no_ode", "ode_pred", "forcing"):
            if k in arrays and isinstance(arrays[k], list):
                # Limita a 600 puntos para evitar payloads gigantes
                keep[k] = [float(x) for x in arrays[k][:600]]
        return keep or None
    except Exception:
        return None


def _build_summary_v2(dataset: dict[str, Any]) -> dict[str, Any]:
    """Resumen compacto adaptado a la UI React (Recharts amigable)."""
    cases = dataset["cases"]
    edis = [c["metrics"]["edi"] for c in cases if isinstance(c["metrics"].get("edi"), (int, float))]
    edis_sorted = sorted(edis)

    def _median(xs):
        if not xs:
            return None
        n = len(xs)
        if n % 2 == 1:
            return xs[n // 2]
        return 0.5 * (xs[n // 2 - 1] + xs[n // 2])

    def _mean(xs):
        return sum(xs) / len(xs) if xs else None

    overall_pass = sum(1 for c in cases if c["metrics"].get("overall_pass"))
    weak_or_better = sum(
        1
        for c in cases
        if (c["metrics"].get("category") or "").lower() in {"strong", "weak", "suggestive"}
    )
    null_count = sum(1 for c in cases if (c["metrics"].get("category") or "").lower() == "null")
    falsified = sum(
        1
        for c in cases
        if (c["metrics"].get("category") or "").lower() in {"falsified", "falsacion", "falsification"}
    )

    from collections import Counter

    # Distribución por categoría — etiquetas estándar
    cat_counter: Counter[str] = Counter(
        (c["metrics"].get("category") or "unknown").lower() for c in cases
    )
    distribution = [
        {"category": k, "count": v}
        for k, v in sorted(cat_counter.items(), key=lambda kv: (-kv[1], kv[0]))
    ]
    level_counter: Counter[str] = Counter(
        "sin nivel" if c["metrics"].get("nivel") is None else str(c["metrics"].get("nivel"))
        for c in cases
    )
    level_breakdown = [
        {
            "level": int(k) if k.isdigit() else None,
            "label": "Sin nivel" if not k.isdigit() else f"Nivel {k}",
            "count": v,
        }
        for k, v in sorted(level_counter.items(), key=lambda kv: (kv[0] == "sin nivel", kv[0]))
    ]

    top_cases = [
        {
            "case_id": c.get("case_name"),
            "case_num": c.get("case_num"),
            "title": c.get("title"),
            "edi": c["metrics"].get("edi"),
            "category": c["metrics"].get("category"),
            "scope": c.get("scope"),
        }
        for c in sorted(
            [c for c in cases if isinstance(c["metrics"].get("edi"), (int, float))],
            key=lambda c: c["metrics"]["edi"],
            reverse=True,
        )[:8]
    ]

    core_inter_domain = sum(
        1 for c in cases if c.get("scope") == "inter-domain" and isinstance(c.get("case_num"), int) and c["case_num"] <= 30
    )
    multiscale = sum(1 for c in cases if c.get("scope") == "inter-scale")
    extensions = sum(
        1 for c in cases if isinstance(c.get("case_num"), int) and c["case_num"] > 40
    )
    by_scope: Counter[str] = Counter(c.get("scope") or "unknown" for c in cases)

    return {
        "presentation": dataset.get("presentation", {}),
        "stats": {
            "total_cases": len(cases),
            "overall_pass": overall_pass,
            "weak_or_better": weak_or_better,
            "null_count": null_count,
            "falsified": falsified,
            "median_edi": _median(edis_sorted),
            "mean_edi": _mean(edis),
        },
        "distribution": distribution,
        "level_breakdown": level_breakdown,
        "top_cases": top_cases,
        "corpus_scope": {
            "visible_metrics": len(cases),
            "declared_core_cases": core_inter_domain + multiscale,
            "core_inter_domain": core_inter_domain,
            "multiscale": multiscale,
            "extensions": extensions,
            "by_scope": [{"scope": k, "count": v} for k, v in sorted(by_scope.items())],
            "note": "La tesis declara 40 casos agregados; la web muestra además las extensiones versionadas 41-42 cuando existen.",
        },
    }


def _chapter_summary_dict(ch: dict[str, Any]) -> dict[str, Any]:
    docs_simple = []
    for d in ch.get("docs", []) or []:
        docs_simple.append(
            {
                "title": d.get("title", d.get("name", "")),
                "path": d.get("path", ""),
            }
        )
    extras_simple = [
        {
            "name": e.get("name"),
            "title": e.get("title"),
            "extends": e.get("extends"),
            "mtime": e.get("mtime"),
        }
        for e in ch.get("extras", []) or []
    ]
    return {
        "slug": ch.get("slug"),
        "code": ch.get("code"),
        "title": ch.get("title"),
        "description": ch.get("description"),
        "docs": docs_simple,
        "extras": extras_simple,
    }


def _chapter_full_dict(ch: dict[str, Any]) -> dict[str, Any]:
    """Renderiza HTML+TOC por documento."""
    docs_full = []
    for d in ch.get("docs", []) or []:
        path_rel = d.get("path")
        if not path_rel:
            continue
        path_abs = ROOT / path_rel
        if not path_abs.exists():
            continue
        text = path_abs.read_text(encoding="utf-8", errors="ignore")
        html, toc = render_markdown_with_toc(text, max_level=3)
        docs_full.append(
            {
                "title": d.get("title", d.get("name", path_abs.name)),
                "path": path_rel,
                "html": html,
                "toc": toc,
            }
        )
    return {
        "slug": ch.get("slug"),
        "code": ch.get("code"),
        "title": ch.get("title"),
        "description": ch.get("description"),
        "docs": docs_full,
    }


# ─── API JSON v2 ──────────────────────────────────────────────────────────────


@app.get("/api/summary", response_class=JSONResponse)
async def api_summary(refresh: bool = Query(default=False)):
    dataset = refresh_dataset() if refresh else get_dataset()
    return JSONResponse(_build_summary_v2(dataset))


@app.get("/api/cases", response_class=JSONResponse)
async def api_cases(refresh: bool = Query(default=False)):
    dataset = refresh_dataset() if refresh else get_dataset()
    return JSONResponse([_case_summary_dict(c) for c in dataset["cases"]])


@app.get("/api/casos/{case_id}", response_class=JSONResponse)
async def api_case(case_id: str, refresh: bool = Query(default=False)):
    case = resolve_case(case_id, refresh=refresh)
    if not case:
        raise HTTPException(status_code=404, detail=f"Caso no encontrado: {case_id}")

    case_name = case["case_name"]
    return JSONResponse(
        {
            **_case_summary_dict(case),
            "phase_order": case.get("phase_order", []),
            "phases": _phases_compact_dict(case),
            "report_html": case_report_html(case),
            "thesis_readme_html": case_readme_html(case),
            "thesis_docs_html": [
                {"title": d["title"], "html": d["html"]}
                for d in case_docs_rendered(case)
            ],
            "math_explainer_html": case_math_explainer_html(case),
            "primary_arrays": _load_primary_arrays(case_name),
        }
    )


@app.get("/api/chapters", response_class=JSONResponse)
async def api_chapters(refresh: bool = Query(default=False)):
    dataset = refresh_dataset() if refresh else get_dataset()
    return JSONResponse([_chapter_summary_dict(ch) for ch in dataset["chapters"]])


@app.get("/api/chapters/{slug}", response_class=JSONResponse)
async def api_chapter(slug: str, refresh: bool = Query(default=False)):
    chapter = resolve_chapter(slug, refresh=refresh)
    if not chapter:
        raise HTTPException(status_code=404, detail=f"Capítulo no encontrado: {slug}")
    return JSONResponse(_chapter_full_dict(chapter))


@app.get("/api/chapters/{slug}/extras", response_class=JSONResponse)
async def api_chapter_extras(slug: str, refresh: bool = Query(default=False)):
    chapter = resolve_chapter(slug, refresh=refresh)
    if not chapter:
        raise HTTPException(status_code=404, detail=f"Capítulo no encontrado: {slug}")
    return JSONResponse(
        {
            "slug": slug,
            "extras": [
                {
                    "name": e.get("name"),
                    "title": e.get("title"),
                    "extends": e.get("extends"),
                    "mtime": e.get("mtime"),
                }
                for e in chapter.get("extras", []) or []
            ],
        }
    )


@app.get("/api/chapters/{slug}/extras/{name}", response_class=JSONResponse)
async def api_chapter_extra(slug: str, name: str, refresh: bool = Query(default=False)):
    # `refresh` invalida el cache global para reflejar archivos recién añadidos
    if refresh:
        refresh_dataset()
    extra = resolve_chapter_extra(slug, name)
    if not extra:
        raise HTTPException(
            status_code=404, detail=f"Extra no encontrado: {slug}/_extendido/{name}"
        )
    return JSONResponse(extra)


@app.get("/api/thesis", response_class=JSONResponse)
async def api_thesis(refresh: bool = Query(default=False)):
    dataset = refresh_dataset() if refresh else get_dataset()
    html = dataset.get("thesis_html", "")
    toc = dataset.get("thesis_toc", [])
    line_count = html.count("\n") + 1 if html else 0
    word_count = len(html.split()) if html else 0
    return JSONResponse(
        {
            "html": html,
            "toc": toc,
            "line_count": line_count,
            "word_count": word_count,
        }
    )


@app.post("/api/run-st", response_class=JSONResponse)
async def api_run_st():
    st_dir = ROOT / "08-consistencia-st"
    report_path = st_dir / "reports" / "ultimo-reporte.md"
    try:
        result = subprocess.run(
            ["npm", "run", "st:check"],
            cwd=str(st_dir),
            capture_output=True,
            text=True,
            timeout=45,
        )
        success = result.returncode == 0
        log = result.stdout + "\n" + result.stderr
    except Exception as e:
        success = False
        log = f"Error ejecutando npm: {e}"

    html = ""
    if report_path.exists():
        html = render_markdown(report_path.read_text(encoding="utf-8", errors="ignore"))

    return JSONResponse({"success": success, "log": log, "html": html})


@app.get("/healthz", response_class=JSONResponse)
async def healthz():
    return JSONResponse(
        {
            "status": "ok",
            "cases": len(get_dataset()["cases"]),
            "react_build": USE_REACT,
        }
    )


# ─── SPA fallback (sirve index.html para rutas frontend) o legacy Jinja2 ──────


def _serve_spa() -> FileResponse | HTMLResponse:
    if USE_REACT:
        return FileResponse(REACT_DIST / "index.html")
    # Fallback en runtime de Vercel: el bundle React vive en /public/ servido
    # como sitio estático directo del CDN; la lambda nunca debería ver una
    # ruta SPA. Si llega aquí, redirigir a /index.html para que el filesystem
    # static handler lo sirva.
    return HTMLResponse(
        status_code=302,
        content="",
        headers={"Location": "/index.html"},
    )


# Vista legacy Jinja2 (mantiene compatibilidad con la URL antigua)
@app.get("/legacy/", response_class=HTMLResponse)
async def home_legacy(request: Request, refresh: bool = Query(default=False)):
    dataset = refresh_dataset() if refresh else get_dataset()
    return templates.TemplateResponse(
        request,
        "home.html",
        {
            "asset_version": _asset_version(),
            "page_title": "Estructuras Pre-Ontológicas — Tesis Visual (legacy)",
            "summary": dataset["summary"],
            "cases": dataset["cases"],
            "chapters": dataset["chapters"],
            "thesis_html": dataset["thesis_html"],
            "thesis_toc": dataset["thesis_toc"],
            "summary_json": json.dumps(dataset["summary"], ensure_ascii=False),
        },
    )


# Catch-all para SPA — debe ir DESPUÉS de las rutas /api/*
@app.get("/{full_path:path}", response_class=HTMLResponse)
async def spa_catchall(full_path: str, request: Request):
    # Si la URL apunta a un archivo estático, dejar que StaticFiles lo maneje
    if full_path.startswith(("api/", "sim_files/", "repo_files/", "visualizations/", "assets/", "legacy_static/", "legacy/")):
        raise HTTPException(status_code=404)
    return _serve_spa()


# Raíz: misma lógica que catch-all
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root():
    return _serve_spa()


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Servidor web visual para la tesis")
    parser.add_argument("--host", default="127.0.0.1", help="Host de bind")
    parser.add_argument("--port", default=8080, type=int, help="Puerto")
    parser.add_argument("--reload", action="store_true", help="Auto-reload de desarrollo")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    uvicorn.run(
        "web_tesis.app:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        reload_dirs=[str(APP_DIR), str(SIM_ROOT)],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
