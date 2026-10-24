import pandas as pd
df = pd.read_csv("retail.csv")

print(f"rows {len(df):,}  invoices {df['InvoiceNo'].nunique():,}")
print(f"missing CustomerID: {df['CustomerID'].isna().sum()}")
print(f"quantity range: {df['Quantity'].min()} to {df['Quantity'].max()}")
print(f"date range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")
