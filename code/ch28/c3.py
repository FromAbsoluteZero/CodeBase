roll = s.rolling(7, center=True).mean()      # 7 days kills the weekly cycle

print(f"raw    standard deviation: {s.std():>8,.0f}")
print(f"smooth standard deviation: {roll.std():>8,.0f}")
print(f"weekly cycle's share of variation: {1 - roll.var()/s.var():.1%}")
