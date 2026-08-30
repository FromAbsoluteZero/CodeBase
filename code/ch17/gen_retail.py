import numpy as np, pandas as pd
rng = np.random.default_rng(7)
items = [("Cold Brew Concentrate", 12.50, "Beverage"),
         ("Ceramic Mug", 8.75, "Merch"),
         ("Espresso Beans 1kg", 24.00, "Beans"),
         ("Paper Filters x100", 4.25, "Supplies"),
         ("Travel Tumbler", 18.90, "Merch"),
         ("Decaf Beans 1kg", 22.50, "Beans"),
         ("Milk Frother", 31.00, "Equipment"),
         ("Gift Card", 25.00, "Other")]
ctry = ["United Kingdom", "Germany", "France", "Netherlands", "Ireland"]
rows, inv = [], 536000
for month in range(1, 13):
    for _ in range(int(rng.integers(55, 85))):
        inv += 1
        c = str(rng.choice(ctry, p=[.55, .15, .12, .10, .08]))
        cust = int(rng.integers(12000, 12400))
        day = int(rng.integers(1, 29))
        for _ in range(int(rng.integers(1, 4))):
            i = int(rng.integers(0, len(items)))
            rows.append({"InvoiceNo": str(inv), "StockCode": "S%d" % (1000 + i),
                "Description": items[i][0], "Category": items[i][2],
                "Quantity": int(rng.integers(1, 13)),
                "InvoiceDate": "2024-%02d-%02d" % (month, day),
                "UnitPrice": items[i][1], "CustomerID": cust, "Country": c})
df = pd.DataFrame(rows)
cancel = df.sample(18, random_state=3).index
df.loc[cancel, "InvoiceNo"] = "C" + df.loc[cancel, "InvoiceNo"]
df.loc[cancel, "Quantity"] = -df.loc[cancel, "Quantity"]
df.loc[df.sample(40, random_state=5).index, "CustomerID"] = np.nan
df.to_csv("retail.csv", index=False)
print(f"wrote retail.csv: {len(df):,} rows, {df.InvoiceNo.nunique():,} invoices")
