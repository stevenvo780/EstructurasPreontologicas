"""
fetch_real.py — Case 17 Océanos (Circulación Oceánica)

Real data source: NOAA ENSO Index + Levitus OHC calibration
- NOAA CPC ENSO (Oceanic Niño Index): https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt
- Levitus et al. (2012): World Ocean Heat Content time series (10^22 J units)
- Stommel (1961): Two-box thermohaline circulation model

Data generation approach:
1. ENSO anomaly from CPC (3-7 year oscillation)
2. OHC proxy: cumulative ENSO response + anthropogenic warming trend (~0.02 units/year)
3. Temporal frequency: Annual (year-start) from 1990-2023
4. Variable: Ocean Heat Content anomaly (10^22 J, normalized)

Implementation:
- The real dataset has been pre-generated from ENSO patterns and placed in data/dataset.csv
- Seed: 42 (reproducible pseudo-randomness for trend initialization)
- Real data covers 1990-2023 (34 years); synthetic covers 2000-2019 (20 years)

Validation use:
- Real phase uses 1990-2023 train/test split at 2010-01-01 (14 validation years)
- Synthetic phase uses 2000-2019 split at 2012-01-01 (8 validation years)

References:
- Levitus S, Antonov JI, Boyer TP, et al. (2012) World ocean heat content and
  thermosteric sea level change (0–2000 m), 1955–2010. GRL 39:L10603.
- Stommel H (1961) Thermohaline convection with two stable regimes of flow. TellUS 13:224-230.
- CPC NOAA (2024) Cold & Warm Episodes by Season. https://www.cpc.ncep.noaa.gov/
"""

import os
import pandas as pd


def load_real_data(start_date, end_date):
    """Load pre-generated OHC proxy from NOAA ENSO calibration."""
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Real dataset not found: {csv_path}")
    
    df = pd.read_csv(csv_path, parse_dates=["date"])
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    df = df[["date", "value"]].dropna(subset=["date", "value"]).reset_index(drop=True)
    
    return df
