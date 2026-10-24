by_dow = s.groupby(s.index.day_name()).mean()
order = ["Monday", "Tuesday", "Wednesday", "Thursday",
         "Friday", "Saturday", "Sunday"]
overall = s.mean()

for d in order:
    print(f"  {d:<10} {by_dow[d]:>8,.0f}   {by_dow[d]/overall:>5.2f}x")
print(f"  {'overall':<10} {overall:>8,.0f}")
