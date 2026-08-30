# Scaling laws, at a scale small enough to run in seconds rather than
# GPU-months: does more training data reduce a language model's error,
# and does that benefit run out? Perplexity is the standard metric,
# the exponential of the average negative log-likelihood per word.
def perplexity(counts, vocab, docs, n=3):
    total_logp, total_words = 0.0, 0
    for doc in docs:
        words = ["<s>"] * (n - 1) + doc.split() + ["</s>"]
        for i in range(n - 1, len(words)):
            context = tuple(words[i - n + 1:i])
            probs = next_word_probs(counts, context, vocab)
            total_logp += np.log(probs.get(words[i], 1e-12))
            total_words += 1
    return np.exp(-total_logp / total_words)

held_out = make_corpus(300, seed=999)             # fixed evaluation set, never trained on
vocab_full = sorted(set(w for d in (train_docs + held_out) for w in d.split()) | {"</s>"})

print(f"{'training documents':>19}{'perplexity on held-out text':>30}")
for n_docs in (10, 30, 100, 300, 1000, 3000):
    docs_n = make_corpus(n_docs, seed=36)
    counts_n = train_ngram(docs_n, n=3)
    ppl = perplexity(counts_n, vocab_full, held_out)
    print(f"{n_docs:>19}{ppl:>30.2f}")

print(f"\nfor reference, a model assigning equal probability to all ")
print(f"{len(vocab_full)} words would score a perplexity of {len(vocab_full)}.")
