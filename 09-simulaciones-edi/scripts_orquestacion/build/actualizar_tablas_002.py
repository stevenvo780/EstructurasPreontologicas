#!/usr/bin/env python3
"""Genera Reporte_General_Simulaciones.md desde outputs/metrics.json.

Lee 09-simulaciones-edi/<caso>/outputs/metrics.json y escribe la tabla
consolidada en 09-simulaciones-edi/Reporte_General_Simulaciones.md.

Historial: también actualizaba 02_Modelado_Simulacion.md en TesisDesarrollo/;
ese árbol se retiró 2026-09-28 y esa rama se eliminó (no hay documento vivo
equivalente con matriz inyectable).
"""
import argparse
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[3]
EDI_DIR = ROOT / '09-simulaciones-edi'
REPORT_DOC = EDI_DIR / 'Reporte_General_Simulaciones.md'

# Mapeo categoría → nivel de cierre operativo (Irrealismo Operativo)
NIVEL_MAP = {
    'strong': 4, 'weak': 3, 'suggestive': 2, 'trend': 1, 'null': 0,
    'falsification': None,  # Control — no se clasifica
}


def read_metrics(case_dir: Path):
    p = case_dir / 'outputs' / 'metrics.json'
    if not p.exists():
        return None
    return json.loads(p.read_text())


def compute_metrics(metrics_obj):
    if not metrics_obj:
        return None
    ph = metrics_obj.get('phases', {}).get('real') or metrics_obj.get('phases', {}).get('synthetic')
    if not ph:
        return None
    # EDI: leer valor directo (calculado por hybrid_validator)
    edi = ph.get('edi', {}).get('value')
    edi_pval = ph.get('edi', {}).get('permutation_pvalue')
    edi_sig = ph.get('edi', {}).get('permutation_significant', False)
    # CR: usar campo 'cr' de symploké (abs(internal/external))
    symploke = ph.get('symploke', {})
    cr = symploke.get('cr')
    if cr is None:
        internal = symploke.get('internal')
        external = symploke.get('external')
        if internal is not None and external not in (None, 0):
            cr = abs(internal / external)
    # Taxonomía
    taxonomy = ph.get('emergence_taxonomy', {})
    category = taxonomy.get('category', '?')
    # Nivel: leer de metrics.json si existe, si no mapear desde categoría
    nivel = taxonomy.get('nivel')
    if nivel is None:
        nivel = NIVEL_MAP.get(category)
    return {
        'edi': edi,
        'edi_pval': edi_pval,
        'edi_sig': edi_sig,
        'cr': cr,
        'overall_pass': ph.get('overall_pass'),
        'category': category,
        'nivel': nivel,
    }


def fmt(x):
    if x is None:
        return 'n/a'
    if isinstance(x, float):
        if math.isinf(x):
            return '∞'
        if math.isnan(x):
            return 'NaN'
    return f"{x:.3f}"


def build_rows():
    rows = []
    for case_dir in sorted(EDI_DIR.glob('[0-9][0-9]_caso_*')):
        if not case_dir.is_dir():
            continue
        metrics_obj = read_metrics(case_dir)
        m = compute_metrics(metrics_obj)
        case = case_dir.name
        case_name = (metrics_obj or {}).get('case') or case
        report_link = f"`{case_dir.name}/outputs/report.md`"
        rows.append((case, case_name, m, report_link))
    return rows


def build_table(rows):
    lines = []
    lines.append("| Caso | Tema | EDI | p-perm | sig | CR | Cat | Nivel | Reporte |")
    lines.append("| :--- | :--- | ---: | ---: | :---: | ---: | :--- | :---: | :--- |")
    for case, case_name, m, report_link in rows:
        if m:
            edi = fmt(m['edi'])
            pval = fmt(m.get('edi_pval'))
            sig = '✅' if m.get('edi_sig') else '❌'
            cr = fmt(m['cr'])
            cat = m.get('category', '?')
            nivel = m.get('nivel')
            nivel_s = str(nivel) if nivel is not None else '—'
        else:
            edi = pval = cr = 'n/a'
            sig = 'n/a'
            cat = 'n/a'
            nivel_s = 'n/a'
        lines.append(
            f"| {case} | {case_name} | {edi} | {pval} | {sig} | {cr} | {cat} | {nivel_s} | {report_link} |"
        )
    return "\n".join(lines)


def update_report(rows):
    table = build_table(rows)
    content = "# Reporte General de Simulaciones\n\n" + table + "\n"
    REPORT_DOC.write_text(content, encoding='utf-8')


def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera Reporte_General_Simulaciones.md desde metrics.json"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="No escribe archivos; solo valida y reporta acciones.",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Imprime la tabla consolidada en stdout.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    rows = build_rows()
    if not rows:
        raise SystemExit(f"[ERROR] Sin casos en {EDI_DIR} (¿layout cambiado?)")
    table = build_table(rows)

    if args.stdout:
        print(table)

    if args.dry_run:
        print(f"[DRY-RUN] actualizar: {REPORT_DOC} ({len(rows)} casos)")
        return

    update_report(rows)
    print(f"OK: actualizado {REPORT_DOC} ({len(rows)} casos)")


if __name__ == '__main__':
    main()
