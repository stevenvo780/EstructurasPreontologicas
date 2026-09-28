"""Vercel serverless entry-point — expone la app FastAPI como handler ASGI."""
from urllib.parse import parse_qsl, urlencode

from web_tesis.app import app as fastapi_app


class _VercelRewritePathMiddleware:
    """Restaura el path original tras los rewrites de vercel.json.

    En producción Vercel invoca la función con scope.path = destino del
    rewrite (/api/index.py), no la URL original (verificado 2026-09-28 con
    ruta diag temporal: scope_path=/api/index.py para toda request rewriteada;
    en `vercel dev` y uvicorn local el path llega intacto).
    Los rewrites añaden ?__route__=<original>; este middleware lo restaura
    antes del dispatch. Solo actúa cuando el path es el fichero función;
    en cualquier otro caso es passthrough (dev/local intactos).
    Ante duplicados se toma la PRIMERA ocurrencia (la que inyecta el rewrite;
    Vercel antepone el query del destination al de la request).
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            p = scope.get("path", "")
            if p == "/api/index.py" or p.endswith("/api/index.py"):
                try:
                    pairs = parse_qsl(
                        scope.get("query_string", b"").decode("latin-1"),
                        keep_blank_values=True,
                    )
                except Exception:
                    pairs = []
                orig = None
                rest = []
                for k, v in pairs:
                    if k == "__route__" and orig is None:
                        orig = v
                    elif k != "__route__":
                        rest.append((k, v))
                if orig:
                    scope["path"] = orig if orig.startswith("/") else "/" + orig
                    scope["query_string"] = urlencode(rest).encode("latin-1")
                    if "raw_path" in scope:
                        scope["raw_path"] = scope["path"].encode("latin-1")
        await self.app(scope, receive, send)


app = _VercelRewritePathMiddleware(fastapi_app)
