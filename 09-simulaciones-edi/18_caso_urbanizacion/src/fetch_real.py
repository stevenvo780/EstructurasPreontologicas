"""
fetch_real.py — 18_caso_urbanizacion

Descarga datos reales de urbanización.
Estrategia: 
1. Intenta World Bank API con timeout robusto
2. Fallback: OWID JSON (más rápido)
3. Fallback final: sintético calibrado
"""

import os
import sys
import json
import numpy as np
import pandas as pd
from datetime import datetime
from urllib.request import urlopen
from urllib.error import URLError

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))


def fetch_owid_urbanization():
    """
    Descarga desde Our World in Data (JSON, más rápido que WB API).
    URL: https://github.com/owid/datasets/blob/master/datasets/Urbanization%20(%)%20-%20OWID.json
    """
    print("[fetch_real.py] Intentando Our World in Data...")
    try:
        # OWID dataset JSON
        url = "https://raw.githubusercontent.com/owid/datasets/master/datasets/Urbanization%20(%25)%20-%20OWID/data.json"
        response = urlopen(url, timeout=15)
        data = json.loads(response.read().decode())
        
        # Extract World aggregate
        if "data" in data:
            world_data = data["data"].get("World", {})
            if world_data:
                observations = []
                for year_str, value in world_data.items():
                    try:
                        year = int(year_str)
                        val = float(value)
                        if 1960 <= year <= 2022 and 0 <= val <= 100:
                            observations.append((year, val))
                    except (ValueError, TypeError):
                        pass
                
                if observations:
                    observations.sort()
                    years, values = zip(*observations)
                    df = pd.DataFrame({
                        "date": pd.to_datetime([f"{y}-01-01" for y in years]),
                        "value": values
                    })
                    print(f"[fetch_real.py] OWID: {len(df)} observaciones ({df['date'].min().year}-{df['date'].max().year})")
                    return df
    except Exception as e:
        print(f"[fetch_real.py] OWID fallido: {e}")
    
    return None


def fetch_world_bank_simple():
    """
    World Bank API simplificado: solo agrega global (SP.URB.TOTL.IN.ZS para agregado "WLD").
    """
    print("[fetch_real.py] Intentando World Bank API (agregado global)...")
    try:
        base_url = "https://api.worldbank.org/v2"
        url = f"{base_url}/country/WLD/indicator/SP.URB.TOTL.IN.ZS?format=json&date=1960:2022&per_page=100"
        
        response = urlopen(url, timeout=15)
        data = json.loads(response.read().decode())
        
        if data and len(data) > 1:
            observations = []
            for obs in data[1]:
                if obs and obs.get("value"):
                    try:
                        year = int(obs["date"])
                        val = float(obs["value"])
                        if 1960 <= year <= 2022:
                            observations.append((year, val))
                    except (ValueError, TypeError):
                        pass
            
            if observations:
                observations.sort()
                years, values = zip(*observations)
                df = pd.DataFrame({
                    "date": pd.to_datetime([f"{y}-01-01" for y in years]),
                    "value": values
                })
                print(f"[fetch_real.py] WB API: {len(df)} observaciones ({df['date'].min().year}-{df['date'].max().year})")
                return df
    except Exception as e:
        print(f"[fetch_real.py] WB API fallido: {e}")
    
    return None


def make_synthetic_calibrated():
    """Fallback: sintético calibrado a patrones reales de urbanización."""
    print("[fetch_real.py] Fallback: datos sintéticos calibrados")
    rng = np.random.default_rng(42)
    
    # Logística: 1960 ~15%, 2022 ~56% (actual)
    years = np.arange(1960, 2023)
    t = (years - 1960) / 62.0
    # Logística centrada ~1980-1990
    urban_rate = 15 + (50 / (1 + np.exp(-10 * (t - 0.35))))
    urban_rate += rng.normal(0, 0.5, len(years))
    urban_rate = np.clip(urban_rate, 10, 85)
    
    df = pd.DataFrame({
        "date": pd.to_datetime([f"{y}-01-01" for y in years]),
        "value": urban_rate
    })
    print(f"[fetch_real.py] Sintético: {len(df)} observaciones (1960-2022)")
    return df


def fetch_urbanization_data():
    """Pipeline con fallbacks automáticos."""
    # Intenta OWID primero (más confiable y rápido)
    df = fetch_owid_urbanization()
    if df is not None and len(df) > 30:
        return df, "OWID"
    
    # Intenta WB API
    df = fetch_world_bank_simple()
    if df is not None and len(df) > 30:
        return df, "World Bank"
    
    # Fallback a sintético
    df = make_synthetic_calibrated()
    return df, "Synthetic (calibrated to real patterns)"


def save_dataset(df, output_path, source):
    """Guarda CSV con metadatos."""
    df.to_csv(output_path, index=False, date_format='%Y-%m-%d')
    print(f"[fetch_real.py] Guardado en {output_path}")
    
    meta = {
        "source": source,
        "indicator": "SP.URB.TOTL.IN.ZS (% Urban Population)",
        "date_range": f"{df['date'].min().year}-{df['date'].max().year}",
        "n_obs": len(df),
        "fetched_at": datetime.utcnow().isoformat()
    }
    
    if "OWID" in source:
        meta["url"] = "https://ourworldindata.org/urbanization"
    elif "World Bank" in source:
        meta["url"] = "https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS"
    else:
        meta["url"] = "N/A (synthetic)"
    
    meta_path = output_path.replace(".csv", "_metadata.json")
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"[fetch_real.py] Metadatos en {meta_path}")
    
    return meta


if __name__ == "__main__":
    case_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(case_dir, "data", "wb_urbanization.csv")
    
    df, source = fetch_urbanization_data()
    meta = save_dataset(df, output_path, source)
    
    print(f"\n[fetch_real.py] COMPLETADO")
    print(f"  Fuente: {source}")
    print(f"  Obs: {len(df)} ({df['date'].min().year}-{df['date'].max().year})")
    print(f"  Rango: {df['value'].min():.1f}% - {df['value'].max():.1f}%")
