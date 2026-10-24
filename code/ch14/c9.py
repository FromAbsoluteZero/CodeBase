call_cost = 400
replace_cost = 9000
success = 0.30      # ASSUMPTION: conversations retain 30%

print(f"cost of a wasted call:     ${call_cost:,}")
print(f"cost of losing someone:    ${replace_cost:,}")
print(f"net value of calling a leaver: "
      f"${replace_cost * success - call_cost:,.0f} expected")
print(f"break-even precision: "
      f"{call_cost / (replace_cost * success):.1%}")
