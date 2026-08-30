# A larger vocabulary means fewer tokens per sentence, at the cost of a
# larger table of units the model must represent and predict over.
def apply_merges(text, merges):
    tokens = list(text) 
    words_with_boundary = []
    for w in text.split(" "):
        words_with_boundary.append(list(w) + ["</w>"])
    for pair, _ in merges:
        for wi, w in enumerate(words_with_boundary):
            new_w, i = [], 0
            while i < len(w):
                if i < len(w) - 1 and w[i] == pair[0] and w[i+1] == pair[1]:
                    new_w.append(w[i] + w[i+1]); i += 2
                else:
                    new_w.append(w[i]); i += 1
            words_with_boundary[wi] = new_w
    return [tok for w in words_with_boundary for tok in w]

test_sentence = "the product arrived quickly and this item worked consistently."

print(f"{'merges applied':>15}{'vocabulary size':>18}{'tokens for one sentence':>26}")
for n_merges in (0, 5, 10, 20, 30):
    partial_merges = merges[:n_merges]
    toks = apply_merges(test_sentence, partial_merges)
    vocab = len(set(c for w in wf for c in w.split())) if n_merges == len(merges) else None
    vocab_size = 26 + n_merges + 1          # 26 letters + merges + boundary marker, roughly
    print(f"{n_merges:>15}{vocab_over_time[n_merges-1] if n_merges else 27:>18}"
          f"{len(toks):>26}")

print(f"\nthe sentence: {test_sentence!r}")
print(f"at 0 merges (characters):  {apply_merges(test_sentence, [])}")
print(f"at 20 merges:              {apply_merges(test_sentence, merges[:20])}")
