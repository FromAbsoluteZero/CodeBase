# Unsupervised learning

Lighter weight, but a poor answer here reads as gaps in fundamentals.

Track: Machine learning · 8 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 3, intermediate 5. Types: conceptual 8.

Answer each question aloud before you open its note.

<a id="q109"></a>

**Q109.** How do you choose the number of clusters?

<sub>Chapters [26](../by-chapter/ch26.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Silhouette score across candidate k, the gap statistic, or external validation against a known outcome. The elbow method is a heuristic on a monotonically decreasing curve and should be described as such.

</details>

<a id="q110"></a>

**Q110.** When would you use DBSCAN instead of k-means?

<sub>Chapters [26](../by-chapter/ch26.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

When clusters are non-spherical, of unknown number, or when outliers should be labeled as noise rather than absorbed. DBSCAN struggles when clusters have very different densities.

</details>

<a id="q111"></a>

**Q111.** What are the main limitations of k-means?

<sub>Chapters [26](../by-chapter/ch26.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It requires k in advance, assumes roughly spherical and similarly sized clusters, converges only to a local optimum, and is sensitive to feature scaling and to outliers pulling centroids.

</details>

<a id="q112"></a>

**Q112.** How do you know a clustering is actually meaningful?

<sub>Chapters [26](../by-chapter/ch26.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

By validating outside the algorithm: does it predict something you did not cluster on, does it match a distinction domain experts recognize, and does it remain stable under resampling.

</details>

<a id="q113"></a>

**Q113.** How does PCA work?

<sub>Chapters [27](../by-chapter/ch27.md) · [9](../by-chapter/ch09.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Center the data, compute the covariance matrix, take its eigenvectors ordered by eigenvalue, and project onto the leading ones. The eigenvalues give variance explained, which decides how many components to retain.

</details>

<a id="q114"></a>

**Q114.** Why can’t you trust cluster distances in a t-SNE plot?

<sub>Chapters [27](../by-chapter/ch27.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The objective preserves local neighborhood probabilities and is free to distort global geometry, so inter-cluster distances and cluster sizes are artifacts of the optimization rather than properties of the data.

</details>

<a id="q115"></a>

**Q115.** When would you use PCA versus t-SNE or UMAP?

<sub>Chapters [27](../by-chapter/ch27.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

PCA when you need reusable, applicable-to-new-data features or linear compression; t-SNE and UMAP when you need a picture of neighborhood structure. Mixing these up is the standard error.

</details>

<a id="q116"></a>

**Q116.** Does PCA perform feature selection?

<sub>Chapters [27](../by-chapter/ch27.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

No. Every component is a linear combination of all original features, so it reduces dimensionality without discarding any input variable — which is also why components can be hard to interpret.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
