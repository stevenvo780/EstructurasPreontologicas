"""
worldbank_universal_fetcher.py — Fetcher Universal de World Bank para Todos los Casos
Implementa descarga automática de indicadores del World Bank para todos los casos aplicables.
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
import pandas as pd
import requests

from common.resource_manager import (
    shared_cache_dir,
    resolve_cache_path,
    ensure_parent,
    offline_mode,
    refresh_mode,
    normalize_timeout,
)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SHARED_CACHE_DIR = str(shared_cache_dir())
WB_CACHE_DIR = os.path.join(SHARED_CACHE_DIR, "worldbank")

# Mapeo de casos a indicadores del World Bank
WORLDBANK_INDICATORS = {
    "03_caso_contaminacion": {
        "indicator": "EN.ATM.PM25.MC.M3",
        "description": "PM2.5 air pollution, population exposed",
        "column_name": "pm25"
    },
    "05_caso_epidemiologia": {
        "indicator": "SH.DYN.MORT",
        "description": "Mortality rate, under-5 (per 1,000 live births)",
        "column_name": "mortality"
    },
    "06_caso_justicia": {
        "indicator": "RL.EST",
        "description": "Rule of Law: Estimate (WGI)",
        "column_name": "rule_of_law"
    },
    "06_caso_movilidad": {
        "indicator": "IS.AIR.PSGR",
        "description": "Air transport, passengers carried",
        "column_name": "passengers"
    },
    "06_caso_politicas_estrategicas": {
        "indicator": "GC.TAX.TOTL.GD.ZS",
        "description": "Tax revenue (% of GDP)",
        "column_name": "tax_revenue"
    },
    "12_caso_postverdad": {
        "indicator": "IT.NET.USER.ZS",
        "description": "Individuals using the Internet (% of population)",
        "column_name": "internet_users"
    },
    "12_caso_deforestacion": {
        "indicator": "AG.LND.FRST.ZS",
        "description": "Forest area (% of land area)",
        "column_name": "forest_area"
    },
    "17_caso_oceanos": {
        "indicator": "EN.ATM.CO2E.KT",
        "description": "CO2 emissions (kt)",
        "column_name": "co2_emissions"
    },
    "06_caso_urbanizacion": {
        "indicator": "SP.URB.TOTL.IN.ZS",
        "description": "Urban population (% of total population)",
        "column_name": "urban_pop"
    },
    "12_caso_acidificacion_oceanica": {
        "indicator": "EN.ATM.CO2E.PC",
        "description": "CO2 emissions (metric tons per capita)",
        "column_name": "co2_per_capita"
    },
    "06_caso_salinizacion": {
        "indicator": "AG.LND.ARBL.ZS",
        "description": "Arable land (% of land area)",
        "column_name": "arable_land"
    },
    "12_caso_fosforo": {
        "indicator": "AG.CON.FERT.ZS",
        "description": "Fertilizer consumption (kg per hectare)",
        "column_name": "fertilizer"
    },
    "17_caso_erosion_dialectica": {
        "indicator": "SE.ADT.LITR.ZS",
        "description": "Literacy rate, adult total (% ages 15+)",
        "column_name": "literacy"
    },
    "06_caso_microplasticos": {
        "indicator": "EN.ATM.GHGT.KT.CE",
        "description": "Total greenhouse gas emissions (kt of CO2 equivalent)",
        "column_name": "ghg_emissions"
    },
    "12_caso_acuiferos": {
        "indicator": "SH.H2O.BASW.ZS",
        "description": "People using safely managed drinking water (% pop)",
        "column_name": "water_access"
    },
    "06_caso_riesgo_biologico": {
        "indicator": "SH.DYN.MORT",
        "description": "Mortality rate, under-5",
        "column_name": "mortality"
    },
    "12_caso_fuga_cerebros": {
        "indicator": "GB.XPD.RSDV.GD.ZS",
        "description": "Research and development expenditure (% of GDP)",
        "column_name": "rd_expenditure"
    },
    "17_caso_iot": {
        "indicator": "IT.CEL.SETS.P2",
        "description": "Mobile cellular subscriptions (per 100 people)",
        "column_name": "mobile_subs"
    },
}


def fetch_worldbank_indicator(
    indicator,
    country="WLD",
    start_year=1960,
    end_year=2023,
    cache_path=None,
    timeout=60,
    refresh=None,
    offline=None,
):
    """Fetch World Bank indicator data (con cache)."""
    refresh = refresh_mode(refresh)
    offline = offline_mode(offline)
    timeout = normalize_timeout(timeout, 60)

    if cache_path is None:
        cache_path = resolve_cache_path(
            None,
            f"{country}_{indicator}.csv",
            subdir="worldbank",
            auto=True,
        )
        cache_path = str(cache_path) if cache_path else None

    if cache_path and os.path.exists(cache_path) and not refresh:
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, None
    if offline:
        return None, "offline (cache miss)"
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"
    params = {"format": "json", "per_page": 500, "date": f"{start_year}:{end_year}"}
    
    try:
        resp = requests.get(url, params=params, headers={"User-Agent": "EDI-validator/1.0"}, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        
        if not isinstance(data, list) or len(data) < 2 or data[1] is None:
            return None, f"No data for {indicator}"
        
        rows = []
        for entry in data[1]:
            year = entry.get("date")
            value = entry.get("value")
            if year and value is not None:
                rows.append({
                    "year": int(year),
                    "date": datetime(int(year), 1, 1),
                    "value": float(value)
                })
        
        if not rows:
            return None, "No valid entries"
        
        df = pd.DataFrame(rows).sort_values("year")
        if cache_path:
            ensure_parent(Path(cache_path))
            df.to_csv(cache_path, index=False)
        return df, None
    
    except Exception as e:
        return None, str(e)


def update_case_data(case_id, info, cache_dir, country="WLD", start_year=1960, end_year=2023, timeout=60,
                     refresh=None, offline=None):
    """Update data.py for a specific case with World Bank data."""
    indicator = info["indicator"]
    column_name = info["column_name"]
    
    print(f"  Fetching {indicator}...")
    cache_path = os.path.join(cache_dir, f"{case_id}_worldbank.csv")
    df, error = fetch_worldbank_indicator(
        indicator,
        country=country,
        start_year=start_year,
        end_year=end_year,
        cache_path=cache_path,
        timeout=timeout,
        refresh=refresh,
        offline=offline,
    )
    
    if df is None:
        print(f"  ❌ Failed: {error}")
        return None
    
    print(f"  ✅ {len(df)} datapoints ({df['year'].min()}-{df['year'].max()})")
    
    return {
        "case": case_id,
        "indicator": indicator,
        "description": info["description"],
        "datapoints": len(df),
        "year_range": f"{df['year'].min()}-{df['year'].max()}",
        "cache_path": cache_path
    }


def _filter_cases(cases_raw):
    if not cases_raw:
        return list(WORLDBANK_INDICATORS.keys())
    out = []
    for token in cases_raw.split(","):
        tok = token.strip()
        if not tok:
            continue
        if tok.isdigit():
            num = f"{int(tok):02d}"
            out.extend([k for k in WORLDBANK_INDICATORS if k.startswith(num + "_")])
        else:
            out.extend([k for k in WORLDBANK_INDICATORS if tok in k])
    return sorted(set(out))


def main():
    parser = argparse.ArgumentParser(
        description="Fetcher universal de indicadores World Bank para la tesis",
    )
    parser.add_argument("--cases", help="Lista separada por coma (ej: 01,03,caso_deforestacion)")
    parser.add_argument("--list", action="store_true", help="Listar indicadores disponibles y salir")
    parser.add_argument("--country", default="WLD", help="Código de país (default: WLD)")
    parser.add_argument("--start-year", type=int, default=1960, help="Año inicial")
    parser.add_argument("--end-year", type=int, default=2023, help="Año final")
    parser.add_argument("--cache-dir", help="Directorio de cache para salidas por caso")
    parser.add_argument("--timeout", type=int, default=None, help="Timeout por request (segundos)")
    parser.add_argument("--refresh", action="store_true", help="Ignorar cache y refrescar")
    parser.add_argument("--offline", action="store_true", help="No hacer requests (solo cache)")
    parser.add_argument("--summary-out", help="Ruta de salida para resumen JSON")
    args = parser.parse_args()

    if args.list:
        print("Casos disponibles:")
        for k, v in WORLDBANK_INDICATORS.items():
            print(f"  {k}: {v['indicator']} — {v['description']}")
        return

    print("WORLD BANK UNIVERSAL FETCHER")
    print("=" * 60)

    cache_dir = args.cache_dir or os.path.join(BASE_PATH, "data_cache", "worldbank")
    os.makedirs(cache_dir, exist_ok=True)

    results = []
    success_count = 0
    fail_count = 0

    selected = _filter_cases(args.cases)
    if not selected:
        print("No hay casos seleccionados.")
        return

    for case_id in selected:
        info = WORLDBANK_INDICATORS.get(case_id)
        if not info:
            print(f"  [WARN] Caso no encontrado en mapa: {case_id}")
            continue
        print(f"\n{case_id}: {info['description']}")

        result = update_case_data(
            case_id,
            info,
            cache_dir,
            country=args.country,
            start_year=args.start_year,
            end_year=args.end_year,
            timeout=args.timeout or 60,
            refresh=args.refresh,
            offline=args.offline,
        )
        if result:
            results.append(result)
            success_count += 1
        else:
            fail_count += 1

    summary_path = args.summary_out or os.path.join(
        BASE_PATH, "outputs_gpu", "worldbank_fetch_summary.json"
    )
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    with open(summary_path, "w") as f:
        json.dump(
            {
                "generated_at": datetime.now().isoformat(),
                "total_cases": len(selected),
                "success": success_count,
                "failed": fail_count,
                "results": results,
            },
            f,
            indent=2,
        )

    print("\n" + "=" * 60)
    print("RESUMEN:")
    print(f"  Exito:    {success_count}/{len(selected)}")
    print(f"  Fallidos: {fail_count}/{len(selected)}")
    print(f"  Cache:    {cache_dir}")
    print(f"  Summary:  {summary_path}")

    print("\nDATOS DESCARGADOS:")
    print("| Caso | Indicador | Puntos | Rango |")
    print("|------|-----------|--------|-------|")
    for r in results:
        print(f"| {r['case'][:20]} | {r['indicator']} | {r['datapoints']} | {r['year_range']} |")


if __name__ == "__main__":
    main()
