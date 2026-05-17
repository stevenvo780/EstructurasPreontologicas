"""
fetch_real.py — 27_caso_riesgo_biologico
Fetcher real para Riesgo Biológico Global usando datos de WHO GHO.

Estrategia:
1. WHO Global Health Observatory API (WHOSIS_000015 — Neonatal mortality)
   como proxy para sistemas de vigilancia epidemiológica mundial.
2. Si falla, fallback sintético.

Fuentes:
- WHO GHO API: https://ghoapi.azureedge.net/api/WHOSIS_000015
- Indicador: Neonatal mortality rate (proxy para capacidad de respuesta epidemiológica)
"""

import os
import sys
import json
import numpy as np
import pandas as pd
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings("ignore")

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CASE_ROOT = os.path.dirname(BASE_PATH)


def fetch_gho_neonatal_mortality(start_year=2000, end_year=2024):
    """
    Fetches WHOSIS_000015 (Neonatal Mortality Rate) from WHO GHO API.
    This serves as proxy for global surveillance system strength.
    
    Returns (df, meta) where df has columns: [date, value, country]
    """
    try:
        import requests
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    except ImportError:
        return None, {"error": "requests not available"}

    url = "https://ghoapi.azureedge.net/api/WHOSIS_000015"
    
    session = requests.Session()
    session.verify = False  # Bypass SSL for Azure endpoint
    
    try:
        print(f"[27] Fetching WHO GHO WHOSIS_000015 from {url}...")
        resp = session.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        print(f"[27] WHO GHO API response received")
    except Exception as e:
        error_msg = f"{type(e).__name__}: {str(e)[:100]}"
        print(f"[27] WHO GHO API failed: {error_msg}")
        return None, {"error": error_msg}

    if not isinstance(data, dict) or "value" not in data:
        return None, {"error": "GHO response malformed"}

    val_list = data.get("value", [])
    if not isinstance(val_list, list) or len(val_list) == 0:
        return None, {"error": "GHO empty value list"}

    print(f"[27] Processing {len(val_list)} WHO GHO records...")
    records = []
    for record in val_list:
        try:
            year = int(record.get("TimeDim", 0))
            if start_year <= year <= end_year:
                # Use NumericValue for reliability
                val = record.get("NumericValue")
                if val is not None:
                    try:
                        val = float(val)
                    except (TypeError, ValueError):
                        continue
                    
                    records.append({
                        "date": f"{year}-01-01",
                        "value": val,
                        "country": record.get("SpatialDim", "GLOBAL"),
                        "year": year,
                    })
        except (TypeError, ValueError):
            continue

    if not records:
        return None, {"error": "No valid records extracted from GHO"}

    print(f"[27] Extracted {len(records)} valid records from {len(set([r['country'] for r in records]))} countries")
    
    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"])
    
    # Aggregate globally by year (average across countries)
    df_global = df.groupby("year").agg({
        "value": ["mean", "std", "count"],
        "date": "first",
    }).reset_index(drop=False)
    
    # Flatten columns
    df_global.columns = ["year", ("value", "mean"), ("value", "std"), ("value", "count"), "date"]
    df_global = df_global[["date", ("value", "mean")]].copy()
    df_global.columns = ["date", "value"]
    
    # Normalize to [0, 1] range for compatibility with synthetic baseline
    vmin, vmax = df_global["value"].min(), df_global["value"].max()
    if vmax > vmin:
        df_global["value"] = (df_global["value"] - vmin) / (vmax - vmin)
        print(f"[27] Normalized from [{vmin:.2f}, {vmax:.2f}] to [0, 1]")
    else:
        df_global["value"] = 0.5
    
    df_global = df_global.sort_values("date")
    
    return df_global, {
        "source": "WHO_GHO_WHOSIS_000015",
        "indicator": "Neonatal Mortality Rate",
        "meaning": "proxy for global surveillance system strength",
        "n_raw_records": len(records),
        "n_countries": df["country"].nunique(),
        "n_aggregated_years": len(df_global),
    }


def fetch_real_biological_risk(start_date="2000-01-01", end_date="2024-01-01", cache_path=None):
    """
    Primary fetcher for biological risk data via WHO GHO.
    
    Returns (df, meta) with df having columns [date, value]
    """
    
    # Try cache first
    if cache_path and os.path.exists(cache_path):
        try:
            df = pd.read_csv(cache_path, parse_dates=["date"])
            print(f"[27] Using cached data from {cache_path}")
            return df, {"source": "cache", "case": "27_caso_riesgo_biologico"}
        except Exception:
            pass

    # Attempt GHO fetch
    df_gho, meta_gho = fetch_gho_neonatal_mortality(2000, 2024)
    
    if df_gho is not None and not df_gho.empty:
        # Filter to requested range
        df_gho["date"] = pd.to_datetime(df_gho["date"])
        df_gho = df_gho[
            (df_gho["date"] >= start_date) & 
            (df_gho["date"] <= end_date)
        ]
        
        if not df_gho.empty:
            print(f"[27] Real data: {len(df_gho)} years from WHO GHO")
            if cache_path:
                os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                df_gho.to_csv(cache_path, index=False)
                print(f"[27] Cached to {cache_path}")
            
            return df_gho, meta_gho

    # If GHO failed, return None to trigger synthetic fallback
    print(f"[27] WHO GHO fetch failed: {meta_gho.get('error', 'unknown')}")
    return None, {
        "source": "none",
        "error": meta_gho.get("error", "gho_unavailable"),
    }


def synthetic_fallback(start_date="2000-01-01", end_date="2024-01-01", seed=42):
    """
    Generates synthetic biological risk data as Woolhouse Cascade proxy.
    Represents hypothetical world with rising zoonotic spillover risk.
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)

    # Trend: rising biological risk (logistic curve)
    t = np.arange(steps)
    trend = 1.0 / (1.0 + np.exp(-0.1 * (t - steps // 2)))

    # Seasonal: weak annual cycle (disease seasonality)
    seasonal = 0.15 * np.sin(2 * np.pi * t / steps)

    # Noise
    noise = rng.normal(0, 0.1, steps)

    # Combine and clip
    values = trend + seasonal + noise
    values = np.clip(values, 0.0, 1.0)

    return pd.DataFrame({
        "date": dates,
        "value": values,
    }), {
        "source": "synthetic_fallback",
        "reason": "real_data_unavailable",
    }
