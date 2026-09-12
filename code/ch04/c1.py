import pandas as pd
df = pd.read_csv("retail.csv")

print("1. shape:", df.shape)
print("2. columns:", list(df.columns)[:5], "...")
print("3. dtypes:")
print(df[["Quantity", "UnitPrice", "CustomerID"]].dtypes.to_string())
print("4. missing values:")
print(df.isna().sum()[df.isna().sum() > 0].to_string())
print("5. suspicious extremes:")
print(f"   Quantity min = {df['Quantity'].min()}")
print(f"   Quantity max = {df['Quantity'].max()}")
