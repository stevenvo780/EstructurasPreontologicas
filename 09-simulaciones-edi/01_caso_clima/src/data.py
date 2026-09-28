"""data.py — Caso 01 Clima: builder CONUS real + fallback sintético.

Vía real: fetch_regional_monthly() construye data/conus_monthly.csv desde
  - tavg: media regional CONUS de estaciones meteostat (≥85% cobertura),
  - co2: NOAA GML Mauna Loa mensual,
  - tsi/ohc/aod: enhanced_data_fetchers (TSI solar, OHC, AOD GISS).
Vía fallback: make_realistic_synthetic() determinista (seed=42).

NOTA DEUDA (2026-09-28): outputs/metrics.json commiteado (re-corrida
2026-07-16) usó un CSV post-procesado indocumentado (media≈0, std≈0.01,
408 filas: 1991-2024) que NO es salida directa de este builder (tavg crudo
en °C). Reproducción bit-idéntica bloqueada en rescate de datos; este
builder restaura la capacidad de correr el caso con datos reales.
Regenerar caché:  .venv/bin/python 09-simulaciones-edi/01_caso_clima/src/data.py
"""

import os
import sys
from datetime import datetime
import urllib.request

import numpy as np
import pandas as pd
from meteostat import Point, stations, monthly


# Wrappers sobre meteostat 2.x (verificado con meteostat==2.1.5)
def _meteostat_stations_nearby(lat, lon, radius):
    """stations.nearby(Point, radius) → DataFrame directo (sin .fetch())."""
    return stations.nearby(Point(lat, lon), radius=radius, limit=200)


def _meteostat_monthly(station_id, start, end):
    """monthly(station, start, end) → TimeSeries con .fetch()."""
    return monthly(station_id, start, end)


sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import (
    fetch_tsi_monthly,
    fetch_wmo_ohc,
    fetch_giss_aod_monthly,
)
CO2_URL = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"


def _conus_bounds():
    # Continental US approximate bounds
    return (24.0, -125.0, 49.5, -66.5)


def _select_stations(start, end, max_stations):
    lat_min, lon_min, lat_max, lon_max = _conus_bounds()
    # Centro aproximado de CONUS
    center_lat = (lat_min + lat_max) / 2
    center_lon = (lon_min + lon_max) / 2
    # Radio ~2500km cubre todo CONUS desde el centro
    stn_df = _meteostat_stations_nearby(center_lat, center_lon, 2_500_000)
    # Filtrar solo estaciones de US
    if "country" in stn_df.columns:
        stn_df = stn_df[stn_df["country"] == "US"]

    # Probar cobertura real: descargar datos mensuales de cada estación
    # y quedarnos con las que tengan ≥85% del periodo solicitado
    total_months = (end.year - start.year) * 12 + (end.month - start.month) + 1
    good_ids = []
    for station_id in stn_df.index.tolist():
        if len(good_ids) >= max_stations * 3:  # probar hasta 3x candidatas
            break
        try:
            ts = _meteostat_monthly(station_id, start, end)
            data = ts.fetch()
            if data is None or data.empty:
                continue
            # meteostat 2.x mensual usa 'temp'; versiones viejas 'tavg'
            tcol = "temp" if "temp" in data.columns else "tavg"
            if tcol not in data.columns:
                continue
            coverage = len(data.dropna(subset=[tcol])) / total_months
            if coverage >= 0.85:
                good_ids.append(station_id)
        except Exception:
            continue

    return stn_df.loc[stn_df.index.isin(good_ids)].head(max_stations)


def fetch_co2_monthly(start_date, end_date, cache_path=None):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    with urllib.request.urlopen(CO2_URL, timeout=60) as resp:
        raw = resp.read().decode("utf-8")

    rows = []
    for line in raw.splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        year = int(parts[0])
        month = int(parts[1])
        avg = float(parts[3])
        if avg < -99:
            continue
        dt = datetime(year, month, 1)
        if dt < start or dt > end:
            continue
        rows.append({"date": dt, "co2": avg})

    df = pd.DataFrame(rows).sort_values("date")
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df


def fetch_regional_monthly(start_date, end_date, max_stations=10, cache_path=None):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    stations = _select_stations(start, end, max_stations)
    if stations.empty:
        raise RuntimeError("No stations with sufficient coverage found in CONUS bounds")

    series_list = []
    for station_id in stations.index.tolist():
        ts = _meteostat_monthly(station_id, start, end)
        data = ts.fetch()
        if data is None or data.empty:
            continue
        tcol = "temp" if "temp" in data.columns else "tavg"
        if tcol not in data.columns:
            continue
        s = data[tcol].dropna()
        s = s.rename(station_id)
        series_list.append(s)

    if not series_list:
        raise RuntimeError("No station data available for selected period")

    combined = pd.concat(series_list, axis=1)
    coverage = combined.notna().mean()
    top = coverage.sort_values(ascending=False).head(max_stations).index.tolist()
    combined = combined[top]

    regional = combined.mean(axis=1).dropna()
    df = regional.reset_index().rename(columns={"time": "date", 0: "tavg", "tavg": "tavg"})

    # Merge CO2 driver
    co2_cache = None
    if cache_path:
        co2_cache = os.path.join(os.path.dirname(cache_path), "co2_mlo.csv")

    # Intentionally propagate exceptions to debug data issues
    df_co2 = fetch_co2_monthly(start_date, end_date, cache_path=co2_cache)
    if not df_co2.empty:
        df = df.merge(df_co2, on="date", how="left")
        df["co2"] = df["co2"].interpolate(limit_direction="both")
    else:
        raise RuntimeError("Failed to fetch CO2 data (empty result)")

    # Merge TSI (solar), OHC (ocean heat content) y aerosoles (AOD)
    driver_specs = [
        ("tsi", fetch_tsi_monthly),
        ("ohc", fetch_wmo_ohc),
        ("aod", fetch_giss_aod_monthly),
    ]
    for col, fn in driver_specs:
        driver_cache = None
        if cache_path:
            driver_cache = os.path.join(os.path.dirname(cache_path), f"{col}.csv")

        # Drivers opcionales: un fallo de red no tumba tavg/co2 (core).
        # Se declara con warning; case_runner ignora drivers ausentes.
        try:
            df_drv, meta = fn(start_date, end_date, cache_path=driver_cache)
        except Exception as e:
            print(f"Warning: {col} fetch failed ({type(e).__name__}); column=None.")
            df_drv = None
        if df_drv is not None and not df_drv.empty:
            df = df.merge(df_drv, on="date", how="left")
            if col in df.columns:
                df[col] = df[col].interpolate(limit_direction="both")
        else:
            print(f"Warning: Failed to fetch {col} data (empty result). Using fallback/None.")
            df[col] = None

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df


def make_realistic_synthetic(start_date, end_date, seed=42):
    """Dataset sintético realista: trend + ciclo estacional.

    Simula temperatura global anomalía con forcing CO₂-correlacionado.
    Determinista: mismo seed → mismo resultado.
    """
    rng = np.random.default_rng(seed)

    # Parse dates
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)

    dates = pd.date_range(start=start, end=end, freq="MS")
    n = len(dates)

    if n < 12:
        dates = pd.date_range(start=start, end=end, freq="YS")
        n = len(dates)

    t = np.arange(n)

    # Trend: 0.015°C/año (IPCC-like warming trend)
    trend = 0.015 * (t / 12)  # mensual

    # Seasonality: ±0.3°C ciclo anual
    season = 0.3 * np.sin(2 * np.pi * t / 12)

    # Noise blanco pequeño
    noise = rng.normal(0, 0.05, n)

    # Temperatura anomalía total (detrended por el modelo)
    temp_anom = trend + season + noise

    # CO2: 315 ppm (1959) → 420 ppm (2023), lineal
    co2_1959 = 315.0
    co2_2023 = 420.0
    start_ref = pd.Timestamp(1959, 1, 1)
    end_ref = pd.Timestamp(2023, 12, 31)

    if start >= start_ref and end <= end_ref:
        months_elapsed = np.arange(n)
        total_months = (end_ref - start_ref).days // 30
        co2_trend = co2_1959 + (co2_2023 - co2_1959) * (months_elapsed / total_months)
        # Agregar ciclo anual pequeño (~1 ppm)
        co2 = co2_trend + 0.5 * np.sin(2 * np.pi * t / 12)
    else:
        # Genérico si está fuera del rango
        co2 = 350 + 0.1 * t + rng.normal(0, 0.1, n)

    df = pd.DataFrame({
        'date': dates,
        'value': temp_anom,
        'co2': co2
    })

    return df


def make_synthetic(start_date, end_date, seed=101):
    """Sintético tradicional: forcing radiativo creciente (CO₂-like)."""
    rng = np.random.default_rng(seed)

    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    forcing = [0.005 * t + 0.3 * np.sin(2 * np.pi * t / 12) for t in range(steps)]

    # Simple ODE simulation
    x = np.zeros(steps)
    x[0] = 0.0
    for t in range(1, steps):
        dx = -0.04 * x[t-1] + 0.015 * forcing[t-1]
        x[t] = x[t-1] + dx + rng.normal(0, 0.03)

    obs = x + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.04, "beta": 0.015}, "measurement_noise": 0.05}
    return df, meta


def load_real_data(start_date, end_date, seed=42):
    """Carga CONUS real (caché o fetch) con desestacionalización (IPCC AR6 WG1 Ch2).

    case_runner prefiere esta función sobre la lectura CSV directa: el df
    retornado DEBE traer columna 'value'. Fallback sintético determinista
    si el fetch falla.
    """
    cache_abs = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "conus_monthly.csv")
    )
    if os.path.exists(cache_abs):
        df = pd.read_csv(cache_abs, parse_dates=["date"])
    else:
        try:
            df = fetch_regional_monthly(start_date, end_date, cache_path=cache_abs)
        except Exception as e:
            print(f"Note: CONUS fetch failed ({type(e).__name__}: {e}); synthetic fallback")
            return make_realistic_synthetic(start_date, end_date, seed=seed)

    df = df.rename(columns={"tavg": "value"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["date", "value"])

    # Desestacionalización: quitar ciclo anual (~97% varianza)
    df["month"] = df["date"].dt.month
    clim_mean = df.groupby("month")["value"].mean()
    df["value"] = df["value"] - df["month"].map(clim_mean)
    df = df.drop(columns=["month"])

    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return df.reset_index(drop=True)


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(description="Materializa data/conus_monthly.csv (fetch real)")
    p.add_argument("--start", default="1990-01-01")
    p.add_argument("--end", default="2024-12-31")
    p.add_argument("--stations", type=int, default=10)
    a = p.parse_args()
    _here = os.path.dirname(os.path.abspath(__file__))
    _csv = os.path.join(_here, "..", "data", "conus_monthly.csv")
    _df = fetch_regional_monthly(a.start, a.end, max_stations=a.stations, cache_path=_csv)
    print(f"OK: {os.path.abspath(_csv)} ({len(_df)} filas)")
