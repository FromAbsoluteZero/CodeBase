regions = pd.DataFrame({
    "Country": ["United Kingdom", "Germany", "France",
                "Netherlands", "Ireland"],
    "Region":  ["UK & IE", "Continental", "Continental",
                "Continental", "UK & IE"],
})

before = len(clean)
m = clean.merge(regions, on="Country", how="left", validate="m:1")
print(f"rows before {before:,}  after {len(m):,}")

print(m.groupby("Region")["Revenue"].sum().round(2).to_string())

# unmatched keys show up as missing, not as an error
print("unmatched rows:", m["Region"].isna().sum())
