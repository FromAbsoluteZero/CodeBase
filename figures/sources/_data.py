"""The order table Chapters 6 to 10 work on, built exactly as their c1.py builds it.
"""
import os, shutil, numpy as np, pandas as pd

def retail_path():
    for d in ("../../data/generated", "../data/generated", "data/generated",
              os.path.join(os.path.dirname(__file__), "..", "..", "data", "generated")):
        p = os.path.join(d, "retail.csv")
        if os.path.exists(p): return p
    raise SystemExit("retail.csv not found")

def orders():
    df = pd.read_csv(retail_path())
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
    return clean.groupby("InvoiceNo").agg(rev=("Revenue", "sum"),
                                          units=("Quantity", "sum"),
                                          country=("Country", "first"))
