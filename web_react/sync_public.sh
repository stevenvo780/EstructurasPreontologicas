#!/bin/bash
# Sincroniza el build de Vite a /public/ que es lo que Vercel sirve estáticamente.
set -e
cd "$(dirname "$0")"
npm run build
ROOT="$(cd .. && pwd)"
rm -rf "$ROOT/public/assets" "$ROOT/public/index.html"
cp -r dist/. "$ROOT/public/"
echo "✓ Sincronizado web_react/dist/ → /public/ ($(du -sh "$ROOT/public/" | cut -f1))"
