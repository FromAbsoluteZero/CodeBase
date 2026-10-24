clean["InvoiceDate"] = pd.to_datetime(clean["InvoiceDate"])
clean["Month"] = clean["InvoiceDate"].dt.month

monthly = clean.groupby("Month")["Revenue"].sum().round(2)
print(monthly.to_string())

h1 = monthly.loc[1:6].sum()
h2 = monthly.loc[7:12].sum()
print(f"\nH1 ${h1:,.0f}  H2 ${h2:,.0f}  change {(h2/h1-1):+.1%}")
