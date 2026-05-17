"""validate.py — Deforestación Global — Sonda: spatial_logistic

Alt-probe: spatial_logistic (Mather 1992, Rudel et al. 2005).
Path adjustment: src/ is 4 levels deep from common/ in alt_probes layout.
"""

import os
import sys

# Alt probe: path to common/ is 4 levels up from src/ (alt_probes/<probe>/src/)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "common"))

from case_runner import run_case

if __name__ == "__main__":
    run_case(os.path.dirname(os.path.abspath(__file__)))
