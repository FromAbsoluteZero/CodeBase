# The break-even threshold falls straight out of the two costs.
p_star = C_FP / (C_FP + C_FN)
print(f"a wasted review costs      {C_FP:>6.0f}")
print(f"a missed fraud costs       {C_FN:>6.0f}")
print(f"break-even threshold p* =  {p_star:.4f}")
print(f"\nflag whenever predicted risk exceeds {p_star:.2%}, not 50%.")
print(f"the default threshold assumes the two errors cost the same,")
print(f"which here would be wrong by a factor of {C_FN/C_FP:.0f}.")
