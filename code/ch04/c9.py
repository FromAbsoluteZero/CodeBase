df["Revenue"] = df["Quantity"] * df["UnitPrice"]

neg = df[df["Quantity"] < 0]
print("negative-quantity rows:", len(neg))
print("all start with C:", neg["InvoiceNo"].str.startswith("C").all())

clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
print(f"kept {len(clean):,} of {len(df):,} rows")
print(f"revenue: ${clean['Revenue'].sum():,.2f}")
