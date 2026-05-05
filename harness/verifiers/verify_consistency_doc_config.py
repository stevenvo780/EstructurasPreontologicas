"""Verificador: doc Evaluacion_Modelos_Dominio.md vs case_config.json reales.

CLAUDE.md §4: si la prosa contradice la config, gana el código ejecutado.
B-T6 declara disonancias específicas: 03/12/29.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import path, glob, repo_root


def main() -> dict:
    eval_doc = path("evaluacion_doc")
    if not eval_doc.exists():
        return {
            "verifier": "consistency_doc_config",
            "status": "warn",
            "error": f"{eval_doc} no existe",
        }

    doc_text = eval_doc.read_text(encoding="utf-8", errors="replace")

    # Extraer pares (caso_NN, sonda_declarada) del doc
    # Patrón heurístico: línea con número de caso y mención de sonda
    declared = {}
    case_section_rx = re.compile(
        r'(?:caso\s+|case[_\s])(\d+)[^\n]*\n((?:.{0,300}\n){0,8})',
        re.IGNORECASE,
    )
    for m in case_section_rx.finditer(doc_text):
        num = m.group(1).zfill(2)
        block = m.group(2).lower()
        # extraer nombres de sondas conocidas
        for sonda in ["lotka-volterra", "von thünen", "von thunen", "budyko",
                      "sir", "seir", "jambeck", "carpenter", "kessler",
                      "mean_reversion", "mean reversion", "bilinear",
                      "landau-ginzburg", "landau ginzburg",
                      "acumulación", "acumulacion", "dispersión", "dispersion",
                      "metcalfe", "difusión", "difusion"]:
            if sonda in block:
                declared.setdefault(num, set()).add(sonda)

    # Extraer sondas reales de case_config.json
    real = {}
    for cfg_path in glob("case_configs_glob"):
        case_dir = cfg_path.parent.name
        num_match = re.match(r'(\d+)_caso_', case_dir)
        if not num_match:
            continue
        num = num_match.group(1)
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception:
            continue
        # buscar campo sonda
        sonda = (
            cfg.get("ode_model") or cfg.get("sonda")
            or cfg.get("ode", {}).get("model") if isinstance(cfg.get("ode"), dict) else None
        ) or cfg.get("probe")
        if isinstance(sonda, str):
            real[num] = sonda.lower()

    discordances = []
    for num in sorted(set(declared) & set(real)):
        decl = declared[num]
        rl = real[num]
        # match si alguna declarada aparece en el real
        if not any(d.replace(" ", "") in rl.replace(" ", "")
                   or rl.replace(" ", "") in d.replace(" ", "")
                   for d in decl):
            discordances.append({
                "case": num,
                "declared_in_doc": list(decl),
                "real_in_config": rl,
                "tareas_pendientes_id": "B-T6" if num in ("03", "12", "29") else None,
            })

    status = "pass" if not discordances else ("fail" if len(discordances) > 5 else "warn")
    return {
        "verifier": "consistency_doc_config",
        "status": status,
        "cases_in_doc": len(declared),
        "cases_with_config": len(real),
        "discordances_count": len(discordances),
        "discordances": discordances,
        "interpretation": (
            "Disonancias entre Evaluacion_Modelos_Dominio.md y case_config.json indican "
            "que el doc declara una sonda y el código ejecuta otra. CLAUDE.md §4: gana el código."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
