# Quantify what "repetitive" actually means: the fraction of generated
# bigrams that are exact repeats of an earlier bigram in the same
# generation, averaged over many independent generations.
def repetition_rate(counts, vocab, method, n_runs=40, **kw):
    rates = []
    for i in range(n_runs):
        text = generate(counts, vocab, method, seed=1000 + i, max_len=20, **kw)
        toks = text.split()
        if len(toks) < 3:
            continue
        bigrams = list(zip(toks, toks[1:]))
        seen, repeats = set(), 0
        for b in bigrams:
            if b in seen:
                repeats += 1
            seen.add(b)
        rates.append(repeats / max(len(bigrams), 1))
    return np.mean(rates)

print(f"{'method':<16}{'mean bigram repetition rate':>30}")
for method, kw in [("greedy", {}), ("temperature (0.7)", {"temperature": 0.7}),
                   ("top-k (3)", {"k": 3}), ("top-p (0.9)", {"p": 0.9})]:
    key = "temperature" if "temperature" in method else ("top_k" if "top-k" in method else
          ("top_p" if "top-p" in method else "greedy"))
    rate = repetition_rate(counts, vocab, key, **kw)
    print(f"{method:<16}{rate:>30.4f}")
