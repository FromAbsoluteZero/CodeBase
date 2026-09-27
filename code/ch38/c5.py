import re
def embed(s):
    ws = [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w in ix]
    if not ws:
        return np.zeros(E.shape[1])
    v = E[[ix[w] for w in ws]].mean(0)
    n = np.linalg.norm(v)
    return v / n if n else v

dense = np.vstack([embed(t) for t in texts])

def search(q, k=3):
    sims = dense @ embed(q)
    return list(np.argsort(-sims)[:k]), sims

hits = 0
for q, gold in queries:
    top, sims = search(q)
    ok = gold in top
    hits += ok
    print(f"  {'HIT ' if ok else 'MISS'}  {q[:46]:<46} "
          f"best={sims[top[0]]:.2f}")
print(f"\ndense recall@3: {hits}/{len(queries)} = {hits/len(queries):.0%}"
      f"   (tf-idf managed 30%)")
