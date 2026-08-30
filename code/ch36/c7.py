# Capacity interacts with data. A higher-order model (more context,
# more parameters in the count table) can represent more, but each
# additional context needs its own examples: too little data and a
# larger model overfits to noise in its own counts.
print(f"{'training docs':>14}{'bigram (n=2)':>14}{'trigram (n=3)':>15}{'4-gram (n=4)':>14}")
for n_docs in (10, 50, 300, 2000):
    docs_n = make_corpus(n_docs, seed=36)
    row = [n_docs]
    for order in (2, 3, 4):
        counts_n = train_ngram(docs_n, n=order)
        ppl = perplexity(counts_n, vocab_full, held_out, n=order)
        row.append(ppl)
    print(f"{row[0]:>14}{row[1]:>14.2f}{row[2]:>15.2f}{row[3]:>14.2f}")

print(f"\nmore context helps once there is enough data to fill it in;")
print(f"with too little data, the extra context has nothing reliable")
print(f"to have learned, and can score worse than the simpler model.")
