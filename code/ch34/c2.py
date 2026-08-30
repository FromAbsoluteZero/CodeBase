# Why divide the scores by sqrt(d_k): the same variance-control argument
# as Chapter 31's initialization, applied to a dot product instead of a
# weighted sum. A dot product of two random d-dimensional vectors has
# variance proportional to d, so larger dimensions produce larger,
# more extreme scores before softmax ever sees them.
r2 = np.random.default_rng(34)

print(f"{'d_k':>6}{'score variance, unscaled':>26}{'score variance, scaled':>25}")
for d in (8, 32, 128, 512):
    q = r2.normal(size=(2000, d))
    k = r2.normal(size=(2000, d))
    raw_scores = np.sum(q * k, axis=1)              # one dot product per row
    scaled_scores = raw_scores / np.sqrt(d)
    print(f"{d:>6}{raw_scores.var():>26.1f}{scaled_scores.var():>25.3f}")

print(f"\nunscaled variance grows linearly with d_k, exactly as an")
print(f"unscaled weighted sum's variance grew with fan-in in Chapter 31.")
print(f"dividing by sqrt(d_k) keeps it near 1 regardless of dimension.")

# real consequence for softmax: one query against five keys at d_k=64
d = 64
q = r2.normal(size=d)
K5 = r2.normal(size=(5, d))
raw = K5 @ q
print(f"\nfive real key vectors scored against one query, d_k = {d}:")
print(f"raw scores:       {raw.round(2)}")
print(f"unscaled softmax: {softmax(raw).round(4)}   <- nearly one-hot")
print(f"scaled softmax:   {softmax(raw / np.sqrt(d)).round(4)}   <- genuinely graded")
