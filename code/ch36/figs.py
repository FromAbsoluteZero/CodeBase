import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
exec(open('c1.py').read().split('print(f"\\nfirst eight')[0])
exec(open('c3.py').read().split('train_docs = ')[0])
train_docs = make_corpus(400, seed=36)
vocab = sorted(set(w for d in train_docs for w in d.split()) | {'</s>'})
counts = train_ngram(train_docs, n=3)
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 36.1: vocab size vs tokens-per-sentence tradeoff
merge_counts = [0, 5, 10, 20, 30]
vocab_sizes = [27, 31, 35, 42, 50]
token_counts = [63, 54, 48, 38, 28]
fig, ax1 = plt.subplots(figsize=(6.6, 3.3))
ax1.plot(merge_counts, vocab_sizes, 'o-', color=NAVY, lw=2)
ax1.set_xlabel("BPE merges applied"); ax1.set_ylabel("vocabulary size", color=NAVY)
ax1.tick_params(axis='y', colors=NAVY)
ax2 = ax1.twinx()
ax2.plot(merge_counts, token_counts, 'o-', color=RED, lw=2)
ax2.set_ylabel("tokens needed for one test sentence", color=RED)
ax2.tick_params(axis='y', colors=RED)
ax2.spines['top'].set_visible(False)
ax1.set_title("More merges: a larger vocabulary, a shorter sequence",
              color=NAVY, fontsize=11.3, loc="left")
fig.tight_layout(); fig.savefig("fig36_1.png", bbox_inches="tight")

# Fig 36.2: data scaling (perplexity vs corpus size, log-log)
ns = [10, 30, 100, 300, 1000, 3000]
ppls = [24.82, 15.44, 9.77, 6.94, 5.49, 4.86]
fig, ax = plt.subplots(figsize=(6.6, 3.3))
ax.plot(ns, ppls, 'o-', color=NAVY, lw=2)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("training documents (log scale)"); ax.set_ylabel("perplexity (log scale)")
ax.set_title("Perplexity falls with more data, with diminishing returns",
             color=NAVY, fontsize=11.3, loc="left")
fig.tight_layout(); fig.savefig("fig36_2.png", bbox_inches="tight")

# Fig 36.3: capacity x data interaction
doc_sizes = [10, 50, 300, 2000]
bigram_p = [14.57, 7.69, 5.37, 4.86]
trigram_p = [24.82, 12.48, 6.94, 5.03]
fourgram_p = [36.97, 22.24, 11.47, 6.56]
fig, ax = plt.subplots(figsize=(6.6, 3.4))
ax.plot(doc_sizes, bigram_p, 'o-', color=GREEN, lw=2, label="bigram (n=2)")
ax.plot(doc_sizes, trigram_p, 'o-', color=NAVY, lw=2, label="trigram (n=3)")
ax.plot(doc_sizes, fourgram_p, 'o-', color=RED, lw=2, label="4-gram (n=4)")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("training documents (log scale)"); ax.set_ylabel("perplexity (log scale)")
ax.set_title("More capacity helps once there is data enough to use it",
             color=NAVY, fontsize=11.2, loc="left")
ax.legend(frameon=False)
fig.tight_layout(); fig.savefig("fig36_3.png", bbox_inches="tight")
print("ok")
