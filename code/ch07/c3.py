prior = 0.04        # P(buys)
sens  = 0.80        # P(flagged | buys)
fpr   = 0.10        # P(flagged | does not buy)

# the formula
p_flag = sens * prior + fpr * (1 - prior)
posterior = sens * prior / p_flag
print(f"P(flagged)        = {p_flag:.4f}")
print(f"P(buys | flagged) = {posterior:.4f}")

# the same thing as counts, which is easier to believe
N = 10_000
buyers, others = N * prior, N * (1 - prior)
tp, fp = buyers * sens, others * fpr
print(f"\nof {N:,} leads: {buyers:,.0f} buy, {others:,.0f} do not")
print(f"flagged: {tp:,.0f} true + {fp:,.0f} false = {tp+fp:,.0f}")
print(f"share of flags that really buy: {tp/(tp+fp):.1%}")
