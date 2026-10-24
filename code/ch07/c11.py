breakeven = spend / (tp * value)
print(f"break-even persuasion rate: {breakeven:.1%}")
print()
for r in [0.05, 0.10, 0.15, 0.20, 0.30]:
    net = tp * r * value - spend
    flag = "loses money" if net < 0 else ""
    print(f"  persuade {r:>4.0%}: net ${net:>8,.0f}  {flag}")
