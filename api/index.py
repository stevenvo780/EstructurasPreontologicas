"""Vercel serverless entry-point — expone la app FastAPI como handler ASGI."""
from web_tesis.app import app  # noqa: F401 — Vercel detecta `app` automáticamente
