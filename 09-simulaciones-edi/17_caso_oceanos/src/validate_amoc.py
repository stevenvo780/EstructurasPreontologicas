"""validate_amoc.py — Test RAPID AMOC variant for caso 17

Temporary test runner that loads AMOC data instead of ENSO.
"""

import os
import sys
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from case_runner import run_case
from case_runner import load_config_from_path

case_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(case_dir)

# Load base config
cfg_path = os.path.join(parent_dir, "case_config.json")
config = load_config_from_path(cfg_path)

# Override for AMOC test
config["case_name"] = "Océanos (AMOC RAPID)"
config["data"]["csv"] = "data/dataset_amoc_rapid.csv"

# Save temporarily
amoc_cfg_path = os.path.join(parent_dir, "case_config_amoc_active.json")
with open(amoc_cfg_path, "w") as f:
    json.dump(config, f, indent=2)

print(f"[TEST] Using AMOC config: {amoc_cfg_path}")
print(f"[TEST] Data source: {config['data']['csv']}")

# Run with modified config (need to patch case_runner to use it)
# For now, just verify the dataset exists and has data
amoc_csv = os.path.join(parent_dir, config['data']['csv'])
if os.path.exists(amoc_csv):
    import pandas as pd
    df = pd.read_csv(amoc_csv, parse_dates=['date'])
    print(f"[DATA] RAPID AMOC: {len(df)} rows, {df['date'].min()} to {df['date'].max()}")
    print(f"[DATA] Value range: [{df['value'].min():.4f}, {df['value'].max():.4f}]")
    print("\n[NOTE] To run full validation with AMOC, copy dataset_amoc_rapid.csv → dataset.csv")
else:
    print(f"[ERROR] AMOC dataset not found: {amoc_csv}")
