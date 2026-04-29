from __future__ import annotations

import argparse
import json
import sys
import subprocess
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
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
        render_markdown,
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
        render_markdown,
    )

APP_DIR = Path(__file__).resolve().parent


def _asset_version() -> str:
    """mtime de app.css como versión cache-bust del navegador."""
    css = APP_DIR / "static" / "css" / "app.css"
    try:
        return str(int(css.stat().st_mtime))
    except OSError:
        return "1"


app = FastAPI(
    title="Estructuras Pre-Ontológicas — Visual",
    description="Capa web para la tesis Realismo Irrealista Operativo y EDI multidominio",
    version="1.0.0",
)

templates = Jinja2Templates(directory=str(APP_DIR / "templates"))

app.mount("/static", StaticFiles(directory=str(APP_DIR / "static")), name="static")
if VIS_ROOT.exists():
    app.mount("/visualizations", StaticFiles(directory=str(VIS_ROOT)), name="visualizations")
app.mount("/sim_files", StaticFiles(directory=str(SIM_ROOT)), name="sim_files")
app.mount("/repo_files", StaticFiles(directory=str(DATA_ROOT)), name="repo_files")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, refresh: bool = Query(default=False)):
    dataset = refresh_dataset() if refresh else get_dataset()
    return templates.TemplateResponse(
        request,
        "home.html",
        {
            "asset_version": _asset_version(),
            "page_title": "Estructuras Pre-Ontológicas — Tesis Visual",
            "summary": dataset["summary"],
            "cases": dataset["cases"],
            "chapters": dataset["chapters"],
            "thesis_html": dataset["thesis_html"],
            "thesis_toc": dataset["thesis_toc"],
            "summary_json": json.dumps(dataset["summary"], ensure_ascii=False),
        },
    )


@app.get("/casos", response_class=HTMLResponse)
async def cases_index() -> RedirectResponse:
    return RedirectResponse(url="/")


@app.get("/casos/{case_id}", response_class=HTMLResponse)
async def case_detail(request: Request, case_id: str, refresh: bool = Query(default=False)):
    case = resolve_case(case_id, refresh=refresh)
    if not case:
        raise HTTPException(status_code=404, detail=f"Caso no encontrado: {case_id}")

    report_html = case_report_html(case)
    thesis_readme_html = case_readme_html(case)
    thesis_docs_html = case_docs_rendered(case)
    math_explainer_html = case_math_explainer_html(case)
    return templates.TemplateResponse(
        request,
        "case.html",
        {
            "asset_version": _asset_version(),
            "page_title": f"{case['case_name']} — Tesis Visual",
            "case": case,
            "report_html": report_html,
            "thesis_readme_html": thesis_readme_html,
            "thesis_docs_html": thesis_docs_html,
            "math_explainer_html": math_explainer_html,
        },
    )


@app.get("/capitulos/{slug}", response_class=HTMLResponse)
async def chapter_detail(request: Request, slug: str, refresh: bool = Query(default=False)):
    chapter = resolve_chapter(slug, refresh=refresh)
    if not chapter:
        raise HTTPException(status_code=404, detail=f"Capítulo no encontrado: {slug}")
    return templates.TemplateResponse(
        request,
        "chapter.html",
        {
            "asset_version": _asset_version(),
            "page_title": f"{chapter['title']} — Tesis Visual",
            "chapter": chapter,
        },
    )


@app.get("/st", response_class=HTMLResponse)
async def st_view(request: Request):
    return templates.TemplateResponse(
        request,
        "st.html",
        {
            "asset_version": _asset_version(),
            "page_title": "Consistencia ST — Tesis Visual",
        },
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
            timeout=45
        )
        success = result.returncode == 0
        log = result.stdout + "\n" + result.stderr
    except Exception as e:
        success = False
        log = f"Error ejecutando npm: {e}"

    html = ""
    if report_path.exists():
        html = render_markdown(report_path.read_text(encoding="utf-8", errors="ignore"))

    return JSONResponse({
        "success": success,
        "log": log,
        "html": html
    })




@app.get("/api/summary", response_class=JSONResponse)
async def api_summary(refresh: bool = Query(default=False)):
    dataset = refresh_dataset() if refresh else get_dataset()
    return JSONResponse(dataset["summary"])


@app.get("/api/casos/{case_id}", response_class=JSONResponse)
async def api_case(case_id: str, refresh: bool = Query(default=False)):
    case = resolve_case(case_id, refresh=refresh)
    if not case:
        raise HTTPException(status_code=404, detail=f"Caso no encontrado: {case_id}")
    return JSONResponse(case)


@app.get("/healthz", response_class=JSONResponse)
async def healthz():
    return JSONResponse({"status": "ok", "cases": len(get_dataset()["cases"])})


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
