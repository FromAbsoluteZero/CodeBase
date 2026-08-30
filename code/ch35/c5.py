# An embedding is whatever a network's pooled features encode before the
# final classification layer. The transferred filters were never trained
# to distinguish digits five through nine, yet if their features are
# genuinely general, examples of the same target digit should still land
# near each other in that space, with no target-task training at all.
feat_te_embed = extract_features(Xtgt_te, src_filters)         # zero target training

from sklearn.decomposition import PCA
proj = PCA(n_components=2, random_state=35).fit_transform(feat_te_embed)

print(f"embedding dimension (pooled, flattened): {feat_te_embed.shape[1]}")
print(f"reduced to 2 dimensions for inspection, via Chapter 27's PCA")

# nearest-neighbor classification directly in the embedding space --
# no training at all, just distance in the transferred feature space
from sklearn.neighbors import KNeighborsClassifier
feat_tr_embed = extract_features(Xtgt_tr, src_filters)
knn = KNeighborsClassifier(5).fit(feat_tr_embed, ytgt_tr)
knn_acc = knn.score(feat_te_embed, ytgt_te)
print(f"\nk-NN accuracy directly in the transferred embedding space: {knn_acc:.4f}")
print(f"(zero target-task training: no head, no fine-tuning, just distance)")

# compare against k-NN on raw pixels, no embedding at all
knn_raw = KNeighborsClassifier(5).fit(Xtgt_tr.reshape(len(Xtgt_tr), -1), ytgt_tr)
knn_raw_acc = knn_raw.score(Xtgt_te.reshape(len(Xtgt_te), -1), ytgt_te)
print(f"k-NN accuracy on raw pixels, no embedding at all:      {knn_raw_acc:.4f}")
