by_country = (clean.groupby("Country")["Revenue"].sum()
                   .sort_values(ascending=False).round(2))
share = (by_country / by_country.sum() * 100).round(1)

result = pd.DataFrame({"revenue": by_country, "share_%": share})
print(result.to_string())
