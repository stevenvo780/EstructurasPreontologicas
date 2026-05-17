"""
generate_dataset.py — Genera dataset real para caso 27.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from fetch_real import fetch_real_biological_risk, synthetic_fallback
import pandas as pd

def main():
    case_root = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(case_root, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    dataset_path = os.path.join(data_dir, "dataset.csv")
    
    print("[27] Attempting to fetch real biological risk data...")
    
    # Try real data first
    df, meta = fetch_real_biological_risk(
        start_date="2000-01-01",
        end_date="2024-01-01",
        cache_path=None
    )
    
    if df is None or df.empty:
        print("[27] Real data fetch failed. Using synthetic fallback.")
        df, meta = synthetic_fallback("2000-01-01", "2024-01-01")
    
    print(f"[27] Dataset: {len(df)} records")
    print(f"[27] Source: {meta.get('source', 'unknown')}")
    print(f"[27] Date range: {df['date'].min()} to {df['date'].max()}")
    
    # Save
    df.to_csv(dataset_path, index=False)
    print(f"[27] Saved to {dataset_path}")
    
    # Save metadata
    meta_path = os.path.join(data_dir, "dataset_meta.json")
    import json
    with open(meta_path, "w") as f:
        # Convert non-serializable objects
        meta_clean = {}
        for k, v in meta.items():
            if isinstance(v, (str, int, float, bool, list, dict, type(None))):
                meta_clean[k] = v
            else:
                meta_clean[k] = str(v)
        json.dump(meta_clean, f, indent=2)
    print(f"[27] Metadata saved to {meta_path}")

if __name__ == "__main__":
    main()
