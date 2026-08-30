#!/usr/bin/env python3
"""Regenerate every synthetic dataset from its generation script.

All generators are seeded, so regeneration is byte-identical to the shipped files.
"""
import subprocess, sys, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "generated"

# (generation script, file it produces)
GENERATORS = [
    ("code/ch16/gen_hr.py",      "hr.csv"),
    ("code/ch17/gen_retail.py",  "retail.csv"),
    ("code/ch22/gen_tx.py",      "transactions.csv"),
    ("code/ch24/gen_orders.py",  "customers.csv"),
    ("code/ch26/gen_seg.py",     "segments.csv"),
]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    failures = []
    for script, produced in GENERATORS:
        path = ROOT / script
        if not path.exists():
            print(f"  SKIP  {script} not found"); failures.append(script); continue
        r = subprocess.run([sys.executable, path.name], cwd=path.parent,
                           capture_output=True, text=True)
        made = path.parent / produced
        if r.returncode == 0 and made.exists():
            shutil.copy(made, OUT / produced)
            print(f"  ok    {produced:<20} <- {script}")
        else:
            print(f"  FAIL  {script}\n{r.stderr[-300:]}"); failures.append(script)

    print("\nNote: daily_revenue.csv is generated inline by Chapter 28, not by a separate script.")
    if failures:
        print(f"\n{len(failures)} generator(s) failed."); return 1
    print("\nAll datasets regenerated.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
