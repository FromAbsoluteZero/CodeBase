uk = orders["country"] == "United Kingdom"
big = orders["big"]

print(f"P(big)        = {big.mean():.4f}")
print(f"P(UK)         = {uk.mean():.4f}")
print(f"P(big AND UK) = {(big & uk).mean():.4f}")
print()
print(f"P(big | UK)   = {big[uk].mean():.4f}")
print(f"P(UK | big)   = {uk[big].mean():.4f}")
print()
print(pd.crosstab(orders['country'], orders['big'],
                  margins=True).to_string())
