cust["rank_raw"] = cust["score"].rank(ascending=False)
cust["rank_z"] = cust["score_z"].rank(ascending=False)
cust["moved"] = (cust["rank_raw"] - cust["rank_z"]).abs()

print(f"customers whose rank moved 20+ places: "
      f"{(cust['moved'] >= 20).sum()}")
biggest = cust.nlargest(3, "moved")
print(biggest[["spend", "orders", "variety",
               "rank_raw", "rank_z"]].round(1).to_string())
