# the quick form: one column, one statistic
by_country = (clean.groupby("Country")["Revenue"]
                   .sum().sort_values(ascending=False))
print(by_country.round(2).to_string())

# named aggregation: several statistics, names you choose
summary = clean.groupby("Category").agg(
    revenue=("Revenue", "sum"),
    lines=("Revenue", "size"),
    avg_qty=("Quantity", "mean"),
).round(2)
print(summary.to_string())
