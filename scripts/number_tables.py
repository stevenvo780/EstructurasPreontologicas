#!/usr/bin/env python3
"""
Numera tablas y figuras Mermaid del manuscrito según convención
TX.Y / FX.Y donde X es el capítulo y Y el ordinal dentro del capítulo.

Reglas:
- Inserta etiqueta "**Tabla X.Y**" inmediatamente antes de cada tabla
  (definida como una línea que empieza con | seguida de separador |---|)
  si no la tiene ya.
- Inserta "**Figura X.Y**" antes de bloques ```mermaid si no la tienen.
- Mapeo de capítulos a número:
    00-proyecto/* → 0
    01-diagnostico/* → 1
    02-fundamentos/01 → 2.1, /02 → 2.2, etc.
    Anexos/A1 → A.1, A.2 → A.2, etc.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Mapeo archivo → prefijo de capítulo
def chapter_prefix(path: Path) -> str | None:
    parts = path.parts
    name = path.stem
    if "Anexos" in parts:
        m = re.match(r"^A(\d+)", name)
        if m:
            return f"A.{m.group(1)}"
        m = re.match(r"^B(\d+)", name)
        if m:
            return f"B.{m.group(1)}"
        return None
    if "00-proyecto" in parts:
        m = re.match(r"^(\d{2})-", name)
        if m:
            return f"0.{int(m.group(1))}"
    if "01-diagnostico" in parts and "sesiones" not in parts:
        m = re.match(r"^(\d{2})-", name)
        if m:
            return f"1.{int(m.group(1))}"
    if "02-fundamentos" in parts:
        m = re.match(r"^(\d{2})-", name)
        if m:
            return f"2.{int(m.group(1))}"
    if "03-formalizacion" in parts:
        m = re.match(r"^(\d{2})-", name)
        if m:
            return f"3.{int(m.group(1))}"
    if "04-debates" in parts:
        m = re.match(r"^(\d{2})-", name)
        if m:
            return f"4.{int(m.group(1))}"
    if "05-aplicaciones" in parts:
        m = re.match(r"^(\d{2})-", name)
        if m:
            return f"5.{int(m.group(1))}"
    if "06-cierre" in parts:
        m = re.match(r"^(\d{2})-", name)
        if m:
            return f"6.{int(m.group(1))}"
    if "07-bibliografia" in parts:
        return "7"
    return None


SEP_RE = re.compile(r"^\s*\|[\s\-:|]+\|\s*$")


def number_file(path: Path) -> tuple[int, int]:
    prefix = chapter_prefix(path)
    if not prefix:
        return 0, 0
    text = path.read_text()
    lines = text.splitlines()
    new_lines: list[str] = []
    table_counter = 0
    figure_counter = 0
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        # Detectar tabla: línea | seguida de |---|
        if line.lstrip().startswith("|") and i + 1 < n and SEP_RE.match(lines[i + 1]):
            # ¿Ya tiene etiqueta encima?
            previous_real = ""
            for k in range(len(new_lines) - 1, -1, -1):
                if new_lines[k].strip():
                    previous_real = new_lines[k]
                    break
            already_labeled = bool(re.search(r"\*\*Tabla [\dA-Z]+\.\d+\*\*", previous_real))
            if not already_labeled:
                table_counter += 1
                # Insertar línea en blanco si no la hay
                if new_lines and new_lines[-1].strip():
                    new_lines.append("")
                new_lines.append(f"**Tabla {prefix}.{table_counter}.**")
                new_lines.append("")
            new_lines.append(line)
            i += 1
            continue
        # Detectar bloque mermaid
        if line.strip().startswith("```mermaid"):
            previous_real = ""
            for k in range(len(new_lines) - 1, -1, -1):
                if new_lines[k].strip():
                    previous_real = new_lines[k]
                    break
            already_labeled = bool(re.search(r"\*\*Figura [\dA-Z]+\.\d+\*\*", previous_real))
            if not already_labeled:
                figure_counter += 1
                if new_lines and new_lines[-1].strip():
                    new_lines.append("")
                new_lines.append(f"**Figura {prefix}.{figure_counter}.**")
                new_lines.append("")
            new_lines.append(line)
            i += 1
            continue
        new_lines.append(line)
        i += 1
    new_text = "\n".join(new_lines)
    if not text.endswith("\n"):
        new_text = new_text.rstrip("\n")
    else:
        if not new_text.endswith("\n"):
            new_text += "\n"
    if new_text != text:
        path.write_text(new_text)
    return table_counter, figure_counter


def main() -> int:
    dirs = ["02-fundamentos", "03-formalizacion", "04-debates",
            "05-aplicaciones", "06-cierre", "Anexos",
            "00-proyecto", "01-diagnostico", "07-bibliografia"]
    total_t = 0
    total_f = 0
    for d in dirs:
        for p in sorted((ROOT / d).rglob("*.md")):
            if "node_modules" in str(p) or ".venv" in str(p) or "sesiones" in str(p):
                continue
            t, f = number_file(p)
            if t or f:
                print(f"  {p.relative_to(ROOT)}: T={t}, F={f}")
                total_t += t
                total_f += f
    print(f"\nTotal: {total_t} tablas + {total_f} figuras numeradas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
