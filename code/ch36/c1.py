# Byte-pair encoding builds a vocabulary bottom-up: start from individual
# characters, and repeatedly merge whichever adjacent pair appears most
# often, treating that pair as one new unit from then on.
def get_pair_counts(word_freqs):
    pairs = Counter()
    for word, freq in word_freqs.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs

def merge_pair(pair, word_freqs):
    merged = {}
    bigram = " ".join(pair)
    replacement = "".join(pair)
    for word, freq in word_freqs.items():
        merged[word.replace(bigram, replacement)] = freq
    return merged

corpus = make_corpus(200, seed=36)
text = " ".join(corpus)
words = text.split()
word_freqs = Counter(" ".join(list(w)) + " </w>" for w in words)     # start as characters

print(f"corpus: {len(words)} word occurrences, {len(word_freqs)} distinct words")
print(f"starting vocabulary: {len(set(c for w in word_freqs for c in w.split()))} characters")

merges = []
vocab_over_time = []
wf = dict(word_freqs)
for step in range(30):
    pairs = get_pair_counts(wf)
    if not pairs:
        break
    best = max(pairs, key=pairs.get)
    wf = merge_pair(best, wf)
    merges.append((best, pairs[best]))
    vocab_size = len(set(c for w in wf for c in w.split()))
    vocab_over_time.append(vocab_size)

print(f"\nfirst eight merges, most frequent adjacent pair each round:")
for i, (pair, count) in enumerate(merges[:8], 1):
    print(f"  {i}. {pair[0]!r} + {pair[1]!r}  (seen together {count} times)")
