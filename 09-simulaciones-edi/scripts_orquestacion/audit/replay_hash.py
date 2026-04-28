#!/usr/bin/env python3
"""
replay_hash.py — Genera y verifica hashes MD5 de todos los outputs de simulación.

Uso:
  python3 replay_hash.py                  # Genera hashes para todos los casos
  python3 replay_hash.py --verify         # Verifica contra hashes guardados
  python3 replay_hash.py --save           # Guarda baseline de hashes
  python3 replay_hash.py --case 01_caso_clima  # Solo un caso

Salida: tabla por caso con hash de metrics.json + report.md
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

SIMS_DIR = Path(__file__).resolve().parent.parent.parent / "Simulaciones"
THESIS_DIR = Path(__file__).resolve().parent.parent.parent.parent / "TesisDesarrollo" / "02_Modelado_Simulacion"
HASH_BASELINE = Path(__file__).resolve().parent / "replay_baseline.json"
# Claves volátiles que cambian en cada corrida sin alterar resultados científicos.
VOLATILE_KEYS = {"generated_at", "commit", "dirty"}


def md5_file(path: Path) -> str:
    """Computa MD5 de un archivo."""
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _strip_volatile(obj):
    if isinstance(obj, dict):
        return {k: _strip_volatile(v) for k, v in obj.items() if k not in VOLATILE_KEYS}
    if isinstance(obj, list):
        return [_strip_volatile(v) for v in obj]
    return obj


def md5_metrics(path: Path, raw: bool = False) -> str:
    if raw:
        return md5_file(path)
    # Hash semántico: ignora metadatos volátiles (timestamp y commit) para
    # detectar solo cambios sustantivos de métricas.
    data = json.loads(path.read_text(encoding="utf-8"))
    clean = _strip_volatile(data)
    payload = json.dumps(clean, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.md5(payload.encode("utf-8")).hexdigest()


def md5_report(path: Path, raw: bool = False) -> str:
    if raw:
        return md5_file(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    filtered = [
        line for line in lines
        if not line.lstrip().lower().startswith(("- generated_at:", "generated_at:"))
    ]
    payload = ("\n".join(filtered).strip() + "\n").encode("utf-8")
    return hashlib.md5(payload).hexdigest()


def collect_hashes(case_filter: str = None, raw: bool = False) -> dict:
    """Recoge hashes de metrics.json y report.md para cada caso."""
    results = {}

    for caso_dir in sorted(SIMS_DIR.glob("[0-9]*_caso_*")):
        caso_name = caso_dir.name
        if case_filter and case_filter not in caso_name:
            continue

        outputs_dir = caso_dir / "outputs"
        entry = {"metrics_md5": None, "report_md5": None}

        metrics_path = outputs_dir / "metrics.json"
        report_path = outputs_dir / "report.md"

        if metrics_path.exists():
            entry["metrics_md5"] = md5_metrics(metrics_path, raw=raw)
        if report_path.exists():
            entry["report_md5"] = md5_report(report_path, raw=raw)

        # También checkear en TesisDesarrollo
        thesis_pattern = list(THESIS_DIR.glob(f"*{caso_name}*"))
        if thesis_pattern:
            thesis_metrics = thesis_pattern[0] / "metrics.json"
            thesis_report = thesis_pattern[0] / "report.md"
            if thesis_metrics.exists():
                entry["thesis_metrics_md5"] = md5_metrics(thesis_metrics, raw=raw)
            if thesis_report.exists():
                entry["thesis_report_md5"] = md5_report(thesis_report, raw=raw)
            # Coherencia: metrics.json + report.md en Simulaciones == TesisDesarrollo?
            metrics_sync = entry.get("metrics_md5") and entry.get("thesis_metrics_md5") and (
                entry["metrics_md5"] == entry["thesis_metrics_md5"]
            )
            report_sync = entry.get("report_md5") and entry.get("thesis_report_md5") and (
                entry["report_md5"] == entry["thesis_report_md5"]
            )
            if metrics_sync is not None and report_sync is not None:
                entry["sync"] = bool(metrics_sync and report_sync)

        results[caso_name] = entry

    return results


def print_table(hashes: dict):
    """Imprime tabla de hashes en consola."""
    print(f"{'Caso':<40} {'metrics.json':<34} {'report.md':<34} {'sync':>5}")
    print("-" * 115)
    for caso, h in sorted(hashes.items()):
        m = h.get("metrics_md5", "—") or "—"
        r = h.get("report_md5", "—") or "—"
        s = "✓" if h.get("sync") else ("✗" if h.get("sync") is False else "—")
        print(f"{caso:<40} {m:<34} {r:<34} {s:>5}")


def save_baseline(hashes: dict):
    """Guarda baseline de hashes a disco."""
    with open(HASH_BASELINE, "w") as f:
        json.dump(hashes, f, indent=2)
    print(f"\n✅ Baseline guardado en {HASH_BASELINE} ({len(hashes)} casos)")


def verify_baseline(hashes: dict) -> bool:
    """Verifica hashes actuales contra baseline guardado."""
    if not HASH_BASELINE.exists():
        print("❌ No existe baseline. Ejecuta primero con --save")
        return False

    with open(HASH_BASELINE) as f:
        baseline = json.load(f)

    changed = []
    missing = []
    ok = 0

    for caso, bh in sorted(baseline.items()):
        current = hashes.get(caso, {})
        if not current.get("metrics_md5"):
            missing.append(caso)
            continue
        metrics_changed = current.get("metrics_md5") != bh.get("metrics_md5")
        report_changed = current.get("report_md5") != bh.get("report_md5")
        if metrics_changed or report_changed:
            changed.append((caso, metrics_changed, report_changed))
        else:
            ok += 1

    new_cases = set(hashes.keys()) - set(baseline.keys())

    print(f"\n📊 Resultado de verificación:")
    print(f"  ✓ Sin cambios: {ok}")
    print(f"  ✗ Cambiados:   {len(changed)}")
    print(f"  ? Faltantes:   {len(missing)}")
    print(f"  + Nuevos:      {len(new_cases)}")

    if changed:
        print(f"\n⚠️  Casos con hash diferente al baseline:")
        for c, m_changed, r_changed in changed:
            flags = []
            if m_changed:
                flags.append("metrics")
            if r_changed:
                flags.append("report")
            print(
                f"    {c} ({'+'.join(flags)}): "
                f"{baseline[c].get('metrics_md5','—')[:12]}… → {hashes[c].get('metrics_md5','—')[:12]}…"
            )

    return len(changed) == 0 and len(missing) == 0


def main():
    parser = argparse.ArgumentParser(description="Replay hash — verificación de reproducibilidad")
    parser.add_argument("--verify", action="store_true", help="Verifica contra baseline guardado")
    parser.add_argument("--save", action="store_true", help="Guarda baseline de hashes")
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Usa hash crudo de archivo (incluye timestamps). Por defecto usa hash normalizado.",
    )
    parser.add_argument("--case", type=str, default=None, help="Filtrar por nombre de caso")
    args = parser.parse_args()

    hashes = collect_hashes(args.case, raw=args.raw)
    print_table(hashes)

    if args.save:
        save_baseline(hashes)
    elif args.verify:
        ok = verify_baseline(hashes)
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
