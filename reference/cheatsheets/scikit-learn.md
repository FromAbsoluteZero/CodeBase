# scikit-learn patterns

The patterns the book uses from Chapter 13 on, in the form that avoids leakage. New here; there was no
room for it in print.

| Task | Idiom | Chapter |
|---|---|---|
| Split | `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)` — `stratify` keeps a rare class balanced across the split | 16 |
| Time series split | Never random: train on the past, validate on the future (`TimeSeriesSplit`, or slice by date) | 16, 28 |
| Preprocess without leaking | Put every fitted step in a `Pipeline`, so cross-validation fits it on each fold's training rows only: `make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(max_iter=1000))` | 24 |
| Mixed column types | `ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols), ("num", StandardScaler(), num_cols)])` as the first pipeline step | 24 |
| Cross-validate | `cross_val_score(model, X, y, cv=StratifiedKFold(5, shuffle=True, random_state=0), scoring="roc_auc")` | 16, 25 |
| Tune honestly | `GridSearchCV` or `RandomizedSearchCV` on the training rows; report the **test** score once, at the end (Q92) | 25 |
| Class imbalance | `class_weight="balanced"` on the estimator, then choose the threshold from `precision_recall_curve` rather than using 0.5 | 23 |
| Metrics | `roc_auc_score(y, prob)` · `precision_recall_curve(y, prob)` · `classification_report(y, pred)` · `confusion_matrix(y, pred)` | 22 |
| Calibration | `CalibratedClassifierCV`, checked with `calibration_curve` | 22 |
| Clustering | `StandardScaler` first, then `KMeans(n_clusters=k, n_init=10, random_state=0)`; judge with `silhouette_score` and a look at the clusters | 26 |
| Save a model | `joblib.dump(model, "model.joblib")`, with the library versions written next to it | 43 |

The challenges [Q221](../../practice/by-topic/challenges.md#q221) to
[Q223](../../practice/by-topic/challenges.md#q223) exercise the split, tune and evaluate patterns on
the book's datasets.

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). Corrections: [docs/ERRATA.md](../../docs/ERRATA.md). Every snippet was checked against the versions pinned in `requirements.txt` (pandas 3.0.2, scikit-learn 1.8.0).</sub>
