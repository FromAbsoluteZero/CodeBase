N = 10_000
churners = N * prior
stayers = N - churners

tp = churners * recall          # flagged and would churn
fn = churners * (1 - recall)    # missed churners
fp = stayers * fpr              # flagged but would have stayed
tn = stayers * (1 - fpr)

print(f"                 flagged   not flagged")
print(f"would churn   {tp:>9,.0f}   {fn:>11,.0f}")
print(f"would stay    {fp:>9,.0f}   {tn:>11,.0f}")
print(f"\ntotal flagged: {tp + fp:,.0f}")
print(f"P(churn | flagged) = {tp / (tp + fp):.1%}")
