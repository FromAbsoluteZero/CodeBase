from imblearn.over_sampling import SMOTE
from imblearn.pipeline import make_pipeline as imb_pipeline

cv = StratifiedKFold(5, shuffle=True, random_state=0)

# WRONG: resample everything, then cross-validate. Synthetic minority
# points are built from rows that later serve as validation data.
sm = SMOTE(random_state=0)
Xr, yr = sm.fit_resample(Xtr, ytr)
wrong = cross_val_score(make_pipeline(StandardScaler(),
                        LogisticRegression(max_iter=5000)),
                        Xr, yr, cv=cv, scoring="average_precision").mean()

# RIGHT: resample inside each fold, on that fold's training rows only.
right = cross_val_score(imb_pipeline(StandardScaler(), SMOTE(random_state=0),
                        LogisticRegression(max_iter=5000)),
                        Xtr, ytr, cv=cv, scoring="average_precision").mean()

plain = cross_val_score(make_pipeline(StandardScaler(),
                        LogisticRegression(max_iter=5000)),
                        Xtr, ytr, cv=cv, scoring="average_precision").mean()

print(f"resampled before splitting (WRONG): {wrong:.4f}")
print(f"resampled inside each fold  (right): {right:.4f}")
print(f"no resampling at all               : {plain:.4f}")
print(f"\nthe wrong version is {wrong/right:.0f}x the honest estimate")
