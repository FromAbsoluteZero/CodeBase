#!/usr/bin/env python3
"""Check that the environment can run this book's code. Run after installing dependencies."""
import sys, importlib

CORE = ["numpy", "pandas", "sklearn", "scipy", "matplotlib"]
OPTIONAL = {"statsmodels": "Chapter 28", "shap": "Chapter 29", "imblearn": "Chapter 23"}

def main():
    ok = True
    print(f"Python {sys.version.split()[0]}")
    if sys.version_info < (3, 10):
        print("  ! Python 3.10 or newer is required"); ok = False
    else:
        print("  ok")

    print("\nCore dependencies:")
    for m in CORE:
        try:
            mod = importlib.import_module(m)
            print(f"  ok   {m:<14}{getattr(mod, '__version__', '?')}")
        except ImportError:
            print(f"  MISSING  {m}  -> pip install -r requirements.txt"); ok = False

    print("\nOptional dependencies:")
    for m, why in OPTIONAL.items():
        try:
            mod = importlib.import_module(m)
            print(f"  ok   {m:<14}{getattr(mod, '__version__', '?')}  ({why})")
        except ImportError:
            print(f"  --   {m:<14}not installed  ({why} will not run)")

    print("\n" + ("Environment ready." if ok else "Environment NOT ready - see messages above."))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
