cust = clean.dropna(subset=["CustomerID"]).groupby("CustomerID").agg(
    spend=("Revenue", "sum"),
    orders=("InvoiceNo", "nunique"),
    variety=("Description", "nunique"),
)
X = cust.values.astype(float)
print(f"matrix shape: {X.shape}")
print(cust.head(3).round(2).to_string())
