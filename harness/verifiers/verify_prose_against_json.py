"""Verificador formal: cifras en prosa deben coincidir con metrics.json.

Estrategia:
  1. Para cada caso EDI, carga `outputs/metrics.json` y `case_config.json`.
  2. Construye índice de cifras canónicas: edi, p_perm, rmse_*, etc.
  3. Recorre la prosa de la tesis buscando menciones del nombre del caso.
  4. Para cada mención, extrae cifras adyacentes y compara con el índice.
  5. Reporta divergencias > tolerancia.

Esto operacionaliza CLAUDE.md regla §4 ("si la prosa contradice metrics.json,
gana el JSON, y la prosa se reescribe").
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import glob, repo_root, chapter_md_files, load_config


def load_metrics_index() -> dict[str, dict]:
    """case_id -> {edi, p_perm, rmse_coupled, rmse_no_ode, ...}"""
    index = {}
    for p in glob("metrics_glob"):
        case_dir = p.parent.parent.name  # e.g. "16_caso_deforestacion"
        try:
            with open(p, "r", encoding="utf-8") as f:
                m = json.load(f)
        except Exception:
            continue
        flat = {}
        # extraer claves canónicas si existen
        for k in ["edi", "edi_real", "EDI", "p_permutation", "p_perm",
                  "rmse_coupled", "rmse_no_ode", "ci_low", "ci_high"]:
            v = m.get(k)
            if isinstance(v, (int, float)):
                flat[k.lower().replace("permutation", "perm")] = float(v)
        # nested: a veces vienen en m["metrics"] o m["resultado"]
        for nest_key in ("metrics", "resultado", "result", "summary"):
            nest = m.get(nest_key)
            if isinstance(nest, dict):
                for k, v in nest.items():
                    if isinstance(v, (int, float)) and k.lower() in (
                        "edi", "p_perm", "p_permutation", "rmse_coupled",
                        "rmse_no_ode", "ci_low", "ci_high"
                    ):
                        flat[k.lower().replace("permutation", "perm")] = float(v)
        if flat:
            index[case_dir] = flat
    return index


def case_aliases(case_id: str) -> list[str]:
    """16_caso_deforestacion -> ['16', 'deforestacion', 'deforestación', 'caso 16', ...]"""
    parts = case_id.split("_")
    num = parts[0] if parts and parts[0].isdigit() else ""
    name = "_".join(parts[2:]) if len(parts) > 2 else ""
    aliases = []
    if num:
        aliases += [f"caso {int(num)}", f"caso{num}", f"Caso {int(num)}"]
    if name:
        aliases += [name, name.replace("_", " "), name.replace("_", " ").capitalize()]
        # tildes simples
        aliases.append(name.replace("acidificacion", "acidificación"))
        aliases.append(name.replace("contaminacion", "contaminación"))
    return list(set(aliases))


def main() -> dict:
    cfg = load_config()
    index = load_metrics_index()
    tol = cfg["prose_json_verification"]["tolerance_relative"]
    pattern = re.compile(cfg["prose_json_verification"]["numeric_pattern"], re.IGNORECASE)

    files = chapter_md_files()
    discrepancies = []
    matches_total = 0

    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        # Buscar cifras EDI/p_perm en cada línea
        for i, line in enumerate(text.splitlines(), start=1):
            for m in pattern.finditer(line):
                metric_key = m.group(1).lower().replace("-", "_")
                if metric_key in ("p_perm", "p-perm", "p_value"):
                    metric_key = "p_perm"
                value = float(m.group(2))
                matches_total += 1
                # ¿qué caso menciona la línea o las 5 anteriores?
                ctx_start = max(0, i - 6)
                ctx = "\n".join(text.splitlines()[ctx_start:i])
                matched_case = None
                for case_id in index:
                    if any(a.lower() in ctx.lower() for a in case_aliases(case_id)):
                        matched_case = case_id
                        break
                if not matched_case:
                    continue
                json_value = index[matched_case].get(metric_key)
                if json_value is None:
                    continue
                rel_diff = abs(value - json_value) / max(abs(json_value), 1e-9)
                if rel_diff > tol:
                    discrepancies.append({
                        "file": str(f.relative_to(repo_root())),
                        "line": i,
                        "case": matched_case,
                        "metric": metric_key,
                        "prose_value": value,
                        "json_value": json_value,
                        "rel_diff": round(rel_diff, 4),
                        "rule": "CLAUDE.md §4: ante divergencia, gana el JSON",
                    })

    status = "pass" if not discrepancies else ("fail" if len(discrepancies) > 5 else "warn")
    return {
        "verifier": "prose_against_json",
        "status": status,
        "files_scanned": len(files),
        "metrics_indexed_cases": len(index),
        "total_numeric_matches_in_prose": matches_total,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies[:30],
        "tolerance_relative": tol,
        "interpretation": (
            "Discrepancias indican que la prosa reporta una cifra que no se reproduce "
            "ejecutando validate.py del caso. Acción: regenerar prosa o re-ejecutar caso "
            "con perfil canónico (n_perm=999, n_boot=500)."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
