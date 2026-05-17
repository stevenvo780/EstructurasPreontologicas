"""
data.py — 27_caso_riesgo_biologico
Carga datos reales cuando es posible; fallback sintético si falla.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from data_universal import fetch_case_data

# Import real fetcher from this case
try:
    from fetch_real import fetch_real_biological_risk, synthetic_fallback
    HAS_REAL_FETCHER = True
except ImportError:
    HAS_REAL_FETCHER = False


def _synthetic_fallback(start_date, end_date, seed=42):
    """Fallback if real fetcher not available."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    if len(dates) < 6:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)
    trend = np.linspace(0.0, 1.0, steps)
    seasonal = 0.2 * np.sin(np.linspace(0, 4 * np.pi, steps))
    noise = rng.normal(0, 0.3, steps)
    values = trend + seasonal + noise
    return pd.DataFrame({"date": dates, "value": values}), {"source": "synthetic_fallback"}


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    """
    Primary data loader for case 27.
    
    1. If HAS_REAL_FETCHER and not refresh: try fetch_real_biological_risk()
    2. Else: try fetch_case_data() (World Bank fallback)
    3. Else: synthetic
    """
    start_date = start_date or "2000-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "27_caso_riesgo_biologico"}

    # Priority 1: Real biological risk data (WHO/OWID)
    if HAS_REAL_FETCHER:
        df, meta = fetch_real_biological_risk(start_date, end_date, cache_path=cache_path)
        if df is not None and not df.empty:
            df["date"] = pd.to_datetime(df["date"])
            return df, meta
        
        # If real fetch fails, try synthetic from real fetcher
        if not refresh:
            df, meta = synthetic_fallback(start_date, end_date)
            if df is not None and not df.empty:
                if cache_path:
                    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                    df.to_csv(cache_path, index=False)
                return df, meta

    # Priority 2: World Bank fallback
    df, meta = fetch_case_data("27_caso_riesgo_biologico", start_date, end_date, cache_path=None)
    if df is not None and not df.empty:
        df["date"] = pd.to_datetime(df["date"])
        return df, meta

    # Priority 3: Fallback synthetic
    return _synthetic_fallback(start_date, end_date)
