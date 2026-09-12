prod = clean.groupby("Description").agg(
    revenue=("Revenue", "sum"),
    lines=("Revenue", "size"),
    units=("Quantity", "sum"),
).sort_values("revenue", ascending=False).round(2)
prod["rev_per_line"] = (prod["revenue"] / prod["lines"]).round(2)
print(prod.head(5).to_string())
