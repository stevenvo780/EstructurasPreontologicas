"""fetch_real.py — Obtiene datos climáticos reales desde OWID CO2 Dataset (GitHub, sin auth).

Fuente verificada:
  - OWID CO2 Dataset: https://github.com/owid/co2-data
  - Incluye: CO2 global, temperature anomaly attribution

Determinismo: seed fijo para interpolación.
"""

import os
import sys
import warnings
import urllib.request
import io

import pandas as pd
import numpy as np

warnings.filterwarnings('ignore')

def fetch_owid_co2_temperature(start_year=1850, end_year=2024, cache_path=None):
    """Descarga CO2 global y cambio de temperatura desde OWID.
    
    Retorna DataFrame con columnas: year, co2, temperature_change_from_co2
    """
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path)
        df['year'] = df['year'].astype(int)
        return df
    
    url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        
        df_raw = pd.read_csv(io.BytesIO(data))
        
        # Filtrar World
        df = df_raw[df_raw['country'] == 'World'].copy()
        
        # Seleccionar columnas
        df = df[['year', 'co2', 'temperature_change_from_co2']].dropna()
        df['year'] = df['year'].astype(int)
        df['co2'] = df['co2'].astype(float)
        df['temperature_change_from_co2'] = df['temperature_change_from_co2'].astype(float)
        
        # Filtrar rango de años
        df = df[(df['year'] >= start_year) & (df['year'] <= end_year)].reset_index(drop=True)
        
        if df.empty:
            print(f"Warning: OWID no rows in range {start_year}-{end_year}")
            return None
        
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        
        print(f"Loaded {len(df)} annual records from OWID")
        return df
    
    except Exception as e:
        print(f"OWID fetch failed: {e}")
        return None


def load_real_data_annual(start_date_str='1959-01-01', end_date_str='2023-12-31', seed=42):
    """Carga datos climáticos reales desde OWID: CO2 + temperatura.
    
    Args:
        start_date_str: string en formato YYYY-MM-DD o YYYY
        end_date_str: string en formato YYYY-MM-DD o YYYY
        seed: seed para reproducibilidad
    
    Interpola a mensual para compatibilidad con validate.py.
    Retorna None si APIs fallan (fallback a sintético).
    """
    rng = np.random.default_rng(seed)
    
    # Parse dates flexiblemente
    try:
        if len(start_date_str) == 4:
            start_year = int(start_date_str)
            start = pd.Timestamp(year=start_year, month=1, day=1)
        else:
            start = pd.to_datetime(start_date_str)
            start_year = start.year
        
        if len(end_date_str) == 4:
            end_year = int(end_date_str)
            end = pd.Timestamp(year=end_year, month=12, day=31)
        else:
            end = pd.to_datetime(end_date_str)
            end_year = end.year
    except Exception as e:
        print(f"Warning: Date parsing failed ({e})")
        return None
    
    cache_dir = os.path.join(os.path.dirname(__file__), "..", "data", "_cache")
    os.makedirs(cache_dir, exist_ok=True)
    
    # Fetch OWID
    owid_cache = os.path.join(cache_dir, "owid_co2_temperature.csv")
    df = fetch_owid_co2_temperature(start_year=start_year, end_year=end_year, cache_path=owid_cache)
    
    if df is None:
        print("Warning: OWID data unavailable, using fallback")
        return None
    
    # Usar temperature_change_from_co2 como proxy de anomalía
    df = df.rename(columns={'temperature_change_from_co2': 'temp_anom'})
    df['year'] = df['year'].astype(int)
    df = df[(df['year'] >= start_year) & (df['year'] <= end_year)].reset_index(drop=True)
    
    if df.empty:
        print("Warning: No data after year filtering")
        return None
    
    # Interpolate to monthly
    df_monthly = []
    for i in range(len(df) - 1):
        year_curr = int(df.iloc[i]['year'])
        year_next = int(df.iloc[i+1]['year'])
        temp_curr = float(df.iloc[i]['temp_anom'])
        temp_next = float(df.iloc[i+1]['temp_anom'])
        co2_curr = float(df.iloc[i]['co2'])
        co2_next = float(df.iloc[i+1]['co2'])
        
        for month in range(1, 13):
            date = pd.Timestamp(year=year_curr, month=month, day=1)
            if date > end:
                break
            frac = (month - 1) / 12.0
            temp_interp = temp_curr + frac * (temp_next - temp_curr)
            co2_interp = co2_curr + frac * (co2_next - co2_curr)
            df_monthly.append({
                'date': date,
                'value': temp_interp,
                'co2': co2_interp
            })
    
    df_out = pd.DataFrame(df_monthly)
    
    # Detrending (linear polynomial)
    if len(df_out) > 2:
        x = np.arange(len(df_out), dtype=float)
        y = df_out['value'].values
        z = np.polyfit(x, y, 1)
        trend = np.polyval(z, x)
        df_out['value'] = y - trend
    
    return df_out


if __name__ == "__main__":
    # Test
    df = load_real_data_annual('1959-01-01', '2023-12-31')
    if df is not None:
        print(f"Loaded {len(df)} monthly rows")
        print(df.head(10))
        print("\nTail:")
        print(df.tail())
    else:
        print("Failed to load real data")
