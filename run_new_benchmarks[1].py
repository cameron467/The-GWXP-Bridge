#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
scripts = [
    ROOT / "scripts" / "gwxp_natural_emergence_benchmark.py",
    ROOT / "scripts" / "gwxp_schedule_hda_bridge.py",
]

for script in scripts:
    print("=" * 80)
    print(f"RUNNING: {script.name}")
    print("=" * 80)
    result = subprocess.run([sys.executable, str(script)])
    if result.returncode != 0:
        raise SystemExit(result.returncode)

print("\nAll new GWXP benchmarks completed successfully.")
