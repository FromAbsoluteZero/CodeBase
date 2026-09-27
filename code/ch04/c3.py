# label-based vs position-based
print(df.loc[0, "Description"])
print(df.iloc[0, 2])

# create a column: elementwise, no loop
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
print(f"total incl. cancellations: ${df['Revenue'].sum():,.2f}")

# cancellations start with C and carry negative quantities
cancels = df[df["InvoiceNo"].str.startswith("C")]
print(f"{len(cancels)} canceled lines, "
      f"${cancels['Revenue'].sum():,.2f}")

# .copy() makes the intent explicit and avoids the ambiguity
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
print(f"clean rows: {len(clean):,}")
print(f"clean revenue: ${clean['Revenue'].sum():,.2f}")
