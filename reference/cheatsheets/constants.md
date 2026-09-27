# Constants worth memorizing

These are also printed in the book's Quick Reference (Appendix D).

| Constant | Value | Chapter |
|---|---|---|
| Normal distribution | ≈68% within 1 sd · ≈95% within 2 · ≈99.7% within 3 | 6 |
| 95% interval | mean ± 1.96 standard errors | 8 |
| Standard error of a mean | sd / √n — halving it needs four times the data | 8 |
| Common alpha | 0.05, by convention rather than by law | 8 |
| Untrained loss, k classes | ln(k). For ten classes, ln(10) ≈ 2.30. A much lower start suggests leakage | 30 |
| Chance accuracy | 1 / k for k balanced classes · the majority share when imbalanced | 22 |
| Random ROC-AUC | 0.5 | 22 |
| Sigmoid | Output in (0, 1) · its gradient never exceeds 0.25 | 14, 30 |
| ReLU gradient | 1 where the input was positive, 0 where it was not | 30 |
| Softmax | Outputs sum to 1 · subtract the max before exponentiating for stability | 30 |
| Attention scaling | Divide scores by √dₖ to stop the softmax saturating | 34 |
| CLT rule of thumb | n ≈ 30, a rule of thumb rather than a guarantee — skew needs more | 7, 8 |

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). Corrections: [docs/ERRATA.md](../../docs/ERRATA.md). Every snippet was checked against the versions pinned in `requirements.txt` (pandas 3.0.2, scikit-learn 1.8.0).</sub>
