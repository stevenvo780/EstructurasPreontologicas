"""validate.py — Wikipedia alt_probe (path corrected for alt_probes structure)"""
import os, sys
_src = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_src, "..", "..", "..", "..", "common")))
from case_runner import run_case
if __name__ == "__main__":
    run_case(_src)
