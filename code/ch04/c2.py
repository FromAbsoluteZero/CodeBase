# one column is a Series, several are a DataFrame
print(type(df["Quantity"]).__name__)
print(type(df[["Quantity", "UnitPrice"]]).__name__)

# a condition produces a boolean for every row
is_uk = df["Country"] == "United Kingdom"
print(is_uk.head(3).to_list(), "...")
print("UK rows:", is_uk.sum())

# pass the mask back to the frame to keep those rows
uk = df[is_uk]
print("filtered shape:", uk.shape)

# combine with & and | — parentheses are required
big = df[(df["Quantity"] > 10) & (df["UnitPrice"] > 20)]
print("big-ticket lines:", len(big))
