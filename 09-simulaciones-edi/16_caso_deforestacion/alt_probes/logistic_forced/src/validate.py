"""validate.py — Deforestación Global — Sonda: logistic_forced

Alt-probe: logistic_forced (Lambin et al. 2003, von Thünen renta económica).
Path adjustment: src/ is 4 levels deep from common/ in alt_probes layout.
"""

import os
import sys

# Alt probe: path to common/ is 4 levels up from src/ (alt_probes/<probe>/src/)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "common"))

from case_runner import run_case

if __name__ == "__main__":
    run_case(os.path.dirname(os.path.abspath(__file__)))
