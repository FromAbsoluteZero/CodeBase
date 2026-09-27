budget = 60
order = np.argsort(p)[::-1]
top = order[:budget]
caught = yte[top].sum()

print(f"calling the top {budget} by score:")
print(f"  leavers among them: {caught} of {yte.sum()} "
      f"({caught/yte.sum():.1%} of all leavers)")
print(f"  precision: {caught/budget:.1%}")
print(f"  implied threshold: {p[order[budget-1]]:.3f}")
print(f"  spend ${budget*call_cost:,}, expected saved "
      f"${caught*success*replace_cost:,.0f}")
print(f"  net: ${caught*success*replace_cost - budget*call_cost:,.0f}")

rand = yte.mean() * budget
print(f"\ncalling 60 at random would find "
      f"{rand:.1f} leavers; the model finds {caught}")
