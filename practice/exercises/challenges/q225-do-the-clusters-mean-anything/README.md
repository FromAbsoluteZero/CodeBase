# Q225 · Do the clusters mean anything

Chapters 26 and 27 · intermediate · data: `data/generated/segments.csv`

Write `cluster_quality(df, k=4)` returning a dictionary with:

| key | value |
|---|---|
| `ari` | adjusted Rand index between the k-means labels and `TrueType` |
| `silhouette` | silhouette score of the k-means labels on the standardized features |
| `largest_cluster_share` | share of rows in the biggest cluster |

Standardize the four numeric columns with `StandardScaler`, then fit
`KMeans(n_clusters=k, n_init=10, random_state=0)`.

```bash
python practice/exercises/challenges/q225-do-the-clusters-mean-anything/check.py
```
