import numpy as np, pandas as pd
rng = np.random.default_rng(26)

# Four real customer types, plus a scatter of people who fit none of them.
specs = [("bargain hunters",  900, [ 18,  2.1,  46,  1.4]),
         ("weekly regulars", 1100, [ 34,  8.6,  12,  3.2]),
         ("bulk buyers",      700, [128,  1.4,   9,  6.1]),
         ("lapsed",           600, [ 22,  0.4,  71,  1.1])]
rows, truth = [], []
for name, n, (basket, freq, recency, lines) in specs:
    rows.append(np.c_[
        np.exp(rng.normal(np.log(basket), 0.30, n)),
        np.abs(rng.normal(freq, freq * 0.28, n)),
        np.abs(rng.normal(recency, recency * 0.30, n)),
        np.abs(rng.normal(lines, lines * 0.25, n))])
    truth += [name] * n
noise = 200
rows.append(np.c_[np.exp(rng.normal(np.log(45), 1.0, noise)),
                  np.abs(rng.normal(4, 3, noise)),
                  np.abs(rng.normal(40, 30, noise)),
                  np.abs(rng.normal(3, 2, noise))])
truth += ["unclassifiable"] * noise

X = np.vstack(rows)
df = pd.DataFrame(X, columns=["AvgBasket", "OrdersPerMonth",
                              "DaysSinceLast", "LinesPerOrder"]).round(2)
df["TrueType"] = truth
df = df.sample(frac=1, random_state=0).reset_index(drop=True)
df.to_csv("segments.csv", index=False)
print(f"wrote segments.csv: {len(df):,} customers, "
      f"{df.TrueType.nunique()} true groups "
      f"({(df.TrueType == 'unclassifiable').sum()} belong to none)")
