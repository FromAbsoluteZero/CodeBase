print(f"1. Each additional unit is associated with "
      f"${bc[1]:.2f} more revenue.")
print(f"2. UK orders run ${bc[-1]:.0f} above comparable French "
      f"ones (p={pc[-1]:.3f}); Germany and Ireland do not differ.")
print(f"3. Product variety adds nothing once volume is known.")
print(f"4. The model explains {1-(ec**2).sum()/((y-y.mean())**2).sum():.0%} "
      f"of variation; typical miss ${ec.std(ddof=1):,.0f}.")
lo_e, hi_e = pd.Series(ec).groupby(band, observed=True).std().iloc[[0, -1]]
print(f"5. Errors grow with order size (${lo_e:.0f} to ${hi_e:.0f}), "
      f"so p-values are optimistic.")
