from collections import Counter
import numpy as np

# Count which words appear near which other words.
lines = [l.split() for l in open("tickets.txt").read().split("\n")]
vocab = sorted({w for l in lines for w in l})
ix = {w: i for i, w in enumerate(vocab)}
C = np.zeros((len(vocab), len(vocab)))
for l in lines:
    for i, w in enumerate(l):
        for u in l[max(0, i-4):i+5]:
            if u != w:
                C[ix[w], ix[u]] += 1

# Positive pointwise mutual information: how much more often two words
# appear together than chance would give.
tot = C.sum()
row, col = C.sum(1, keepdims=True), C.sum(0, keepdims=True)
pmi = np.log((C * tot) / (row * col + 1e-9) + 1e-9)
P = np.maximum(pmi, 0)

U, S, _ = np.linalg.svd(P, full_matrices=False)
E = U[:, :32] * S[:32]                       # 32-dimensional word vectors
E /= (np.linalg.norm(E, axis=1, keepdims=True) + 1e-9)

def cos(a, b):
    return E[ix[a]] @ E[ix[b]]

for a, b in [("dormant", "inactive"), ("overseas", "international"),
             ("express", "fastest"), ("dormant", "express")]:
    print(f"  cos({a:<12}, {b:<14}) = {cos(a, b):+.3f}")
