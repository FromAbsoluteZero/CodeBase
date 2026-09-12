# The deliverable is not the labels. It is the profile.
km = KMeans(4, n_init=10, random_state=0).fit(X)
prof = df.copy()
prof["cluster"] = km.labels_
overall = prof[FEATS].mean()

print(f"{'cluster':>8}{'n':>7}" + "".join(f"{f:>16}" for f in FEATS))
for c in range(4):
    sub = prof[prof.cluster == c]
    cells = "".join(f"{sub[f].mean():>16.1f}" for f in FEATS)
    print(f"{c:>8}{len(sub):>7}{cells}")
print(f"{'ALL':>8}{len(prof):>7}" +
      "".join(f"{overall[f]:>16.1f}" for f in FEATS))

print(f"\nindex against the average (100 = typical customer)")
print(f"{'cluster':>8}" + "".join(f"{f:>16}" for f in FEATS))
for c in range(4):
    sub = prof[prof.cluster == c]
    cells = "".join(f"{100*sub[f].mean()/overall[f]:>16.0f}" for f in FEATS)
    print(f"{c:>8}{cells}")
