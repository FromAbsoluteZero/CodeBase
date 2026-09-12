persuade = 0.30    # ASSUMPTION: 30% of at-risk customers stay

contacted = tp + fp
spend = contacted * offer
saved = tp * persuade
revenue = saved * value

print(f"contacted:      {contacted:>8,.0f}")
print(f"cost:           ${spend:>8,.0f}")
print(f"customers kept: {saved:>8,.0f}")
print(f"margin saved:   ${revenue:>8,.0f}")
print(f"net:            ${revenue - spend:>8,.0f}")
