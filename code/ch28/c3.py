roll = s.rolling(7, center=True).mean()      # 7 days kills the weekly cycle

print(f"raw    standard deviation: {s.std():>8,.0f}")
print(f"smooth standard deviation: {roll.std():>8,.0f}")
print(f"share of variation the smoothing removes: "
      f"{1 - roll.var()/s.var():.1%}")
