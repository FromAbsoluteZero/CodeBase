# Self-attention has no built-in sense of order. Shuffle the input
# positions and the output shuffles identically: the network cannot
# tell "first" from "third" unless something tells it.
def self_attention(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    d_k = Q.shape[-1]
    weights = softmax((Q @ K.T) / np.sqrt(d_k))
    return weights @ V

r3 = np.random.default_rng(34)
T, D = 5, 8
content = r3.normal(size=(T, D))          # what each position "contains"
Wq, Wk, Wv = (r3.normal(0, np.sqrt(1/D), (D, D)) for _ in range(3))

out = self_attention(content, Wq, Wk, Wv)

perm = [3, 0, 4, 1, 2]                    # shuffle which content sits where
out_shuffled_input = self_attention(content[perm], Wq, Wk, Wv)
out_then_shuffled = out[perm]

print(f"attend(shuffle(content))       row 0: {out_shuffled_input[0].round(4)}")
print(f"shuffle(attend(content))       row 0: {out_then_shuffled[0].round(4)}")
print(f"identical: {np.allclose(out_shuffled_input, out_then_shuffled)}")
print(f"\nself-attention commutes with any reordering of the input.")
print(f"it has no way to know which content came first without help.")

# a positional signal keyed to ARRAY INDEX, added fresh regardless of
# which content occupies that index -- this is the part a shuffle of
# the raw content cannot also shuffle away
idx = np.arange(T)[:, None] / T
pos_encoding = 0.8 * np.concatenate([np.sin(idx), np.cos(idx)] * (D // 2), axis=1)[:, :D]

def with_position(raw_content):
    return raw_content + pos_encoding      # position i always gets encoding i

out_pos = self_attention(with_position(content), Wq, Wk, Wv)
out_pos_shuffled_input = self_attention(with_position(content[perm]), Wq, Wk, Wv)
out_pos_then_shuffled = out_pos[perm]
print(f"\nwith positional encoding tied to array index:")
print(f"identical: {np.allclose(out_pos_shuffled_input, out_pos_then_shuffled, atol=1e-6)}")
print(f"max difference: {np.abs(out_pos_shuffled_input - out_pos_then_shuffled).max():.4f}")
