# A next-token distribution to decode from. A trigram model: predict the
# next word from the two words before it, estimated by counting.
def train_ngram(docs, n=3):
    counts = defaultdict(Counter)
    for doc in docs:
        words = ["<s>"] * (n - 1) + doc.split() + ["</s>"]
        for i in range(len(words) - n + 1):
            context = tuple(words[i:i + n - 1])
            counts[context][words[i + n - 1]] += 1
    return counts

def next_word_probs(counts, context, vocab, smoothing=0.1):
    c = counts.get(context, Counter())
    total = sum(c.values()) + smoothing * len(vocab)
    return {w: (c.get(w, 0) + smoothing) / total for w in vocab}

train_docs = make_corpus(400, seed=36)
vocab = sorted(set(w for d in train_docs for w in d.split()) | {"</s>"})
counts = train_ngram(train_docs, n=3)

context = ("the", "product")
probs = next_word_probs(counts, context, vocab)
top5 = sorted(probs.items(), key=lambda x: -x[1])[:5]
print(f"trained on {len(train_docs)} synthetic reviews, vocabulary of {len(vocab)} words")
print(f"\nafter the context {context}, most likely next words:")
for w, p in top5:
    print(f"  {w:<14}{p:.4f}")
print(f"\ntotal probability mass: {sum(probs.values()):.4f}   (must sum to 1)")
