#!/usr/bin/env bash
# Regenera versiones vectoriales (SVG + PNG) de las figuras Mermaid del Anexo A10.
# Requiere: node, npx, y un /tmp/puppeteer-config.json con --no-sandbox para entornos sin sandbox.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_DIR="$ROOT/figures/mermaid_src"
SVG_DIR="$ROOT/figures/mermaid_svg"
PNG_DIR="$ROOT/figures/mermaid_png"
A10="$ROOT/Anexos/A10-figuras-mermaid.md"
PUPPETEER_CONFIG="${PUPPETEER_CONFIG:-/tmp/puppeteer-config.json}"

mkdir -p "$SRC_DIR" "$SVG_DIR" "$PNG_DIR"

if [[ ! -f "$PUPPETEER_CONFIG" ]]; then
  cat > "$PUPPETEER_CONFIG" <<'EOF'
{ "args": ["--no-sandbox", "--disable-setuid-sandbox"] }
EOF
fi

# Extract mermaid blocks from A10 with python
python3 - <<PY
import re
from pathlib import Path

src = Path("$A10").read_text()
blocks = re.findall(r"```mermaid\n(.*?)\n```", src, re.DOTALL)
for i, b in enumerate(blocks, 1):
    Path("$SRC_DIR/figura_%02d.mmd" % i).write_text(b)
print(f"extracted {len(blocks)} mermaid blocks")
PY

for src_file in "$SRC_DIR"/figura_*.mmd; do
  base="$(basename "$src_file" .mmd)"
  svg="$SVG_DIR/${base}.svg"
  png="$PNG_DIR/${base}.png"
  echo "→ $base"
  npx --yes -p @mermaid-js/mermaid-cli mmdc -i "$src_file" -o "$svg" -p "$PUPPETEER_CONFIG" >/dev/null
  npx --yes -p @mermaid-js/mermaid-cli mmdc -i "$src_file" -o "$png" -p "$PUPPETEER_CONFIG" -w 1600 -H 1200 >/dev/null
done

echo "done. SVG → $SVG_DIR, PNG → $PNG_DIR"
