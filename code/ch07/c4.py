cost, margin = 6.00, 140.00

breakeven = cost / margin
print(f"break-even response rate: {breakeven:.2%}")

ev_blanket  = prior * margin - cost
ev_targeted = posterior * margin - cost
print(f"EV per lead, contact everyone: ${ev_blanket:,.2f}")
print(f"EV per lead, contact flagged:  ${ev_targeted:,.2f}")

flagged = int(10_000 * p_flag)
print(f"\nover {N:,} leads:")
print(f"  blanket:  ${10_000 * ev_blanket:,.0f}")
print(f"  targeted: ${flagged * ev_targeted:,.0f} "
      f"(contacting {flagged:,})")
