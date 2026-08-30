# Four ways to turn a probability distribution into an actual next word.
def sample_from(probs_dict, method, seed, temperature=1.0, k=5, p=0.9):
    r = np.random.default_rng(seed)
    words = list(probs_dict.keys())
    p_arr = np.array([probs_dict[w] for w in words])

    if method == "greedy":
        return words[p_arr.argmax()]
    if method == "temperature":
        logp = np.log(p_arr + 1e-12) / temperature
        adj = np.exp(logp - logp.max()); adj /= adj.sum()
        return r.choice(words, p=adj)
    if method == "top_k":
        idx = np.argsort(-p_arr)[:k]
        sub = p_arr[idx]; sub /= sub.sum()
        return r.choice([words[i] for i in idx], p=sub)
    if method == "top_p":
        order = np.argsort(-p_arr)
        cum = np.cumsum(p_arr[order])
        cutoff = np.searchsorted(cum, p) + 1
        idx = order[:cutoff]
        sub = p_arr[idx]; sub /= sub.sum()
        return r.choice([words[i] for i in idx], p=sub)

def generate(counts, vocab, method, seed, max_len=12, **kw):
    r_start = np.random.default_rng(seed)
    words = ["<s>", "<s>"]
    for i in range(max_len):
        context = tuple(words[-2:])
        probs = next_word_probs(counts, context, vocab)
        nxt = sample_from(probs, method, seed=seed * 1000 + i, **kw)
        if nxt == "</s>":
            break
        words.append(nxt)
    return " ".join(words[2:])

print("greedy (always the single most likely word):")
print(" ", generate(counts, vocab, "greedy", seed=36))
print(" ", generate(counts, vocab, "greedy", seed=37))
print(" ", generate(counts, vocab, "greedy", seed=38))

print("\ntemperature = 0.7 (sample, mildly reshaped toward the top):")
for s in (36, 37, 38):
    print(" ", generate(counts, vocab, "temperature", seed=s, temperature=0.7))

print("\ntop-k = 3 (sample among the three most likely words only):")
for s in (36, 37, 38):
    print(" ", generate(counts, vocab, "top_k", seed=s, k=3))

print("\ntop-p = 0.9 (sample among the smallest set covering 90% mass):")
for s in (36, 37, 38):
    print(" ", generate(counts, vocab, "top_p", seed=s, p=0.9))
