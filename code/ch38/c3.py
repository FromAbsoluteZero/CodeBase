from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

vec = TfidfVectorizer(stop_words="english").fit(texts)
index = np.asarray(normalize(vec.transform(texts)).todense())

def search(q, k=3):
    qv = np.asarray(normalize(vec.transform([q])).todense()).ravel()
    sims = index @ qv
    if sims.max() == 0:        # no shared vocabulary: nothing found
        return [], sims
    return list(np.argsort(-sims)[:k]), sims

hits = empty = 0
for q, gold in queries:
    top, sims = search(q)
    if not top:
        empty += 1
        print(f"  NONE  {q[:46]:<46}")
        continue
    ok = gold in top
    hits += ok
    print(f"  {'HIT ' if ok else 'MISS'}  {q[:46]:<46} "
          f"best={sims[top[0]]:.2f}")

print(f"\ntf-idf recall@3: {hits}/{len(queries)} = {hits/len(queries):.0%}"
      f"   ({empty} queries matched no vocabulary at all)")
