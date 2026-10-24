print(df.dtypes.to_string())
print(f"\nrows {len(df):,}   churn {y.mean():.1%}")
for c in ["City", "Plan", "Channel"]:
    print(f"  {c:<9} {df[c].nunique():>4} distinct   "
          f"most common: {df[c].value_counts().index[0]}")
print(f"  AnnualIncome missing: {df.AnnualIncome.isna().sum()} "
      f"({df.AnnualIncome.isna().mean():.1%})")
