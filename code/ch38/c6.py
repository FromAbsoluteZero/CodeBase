# A retriever always returns its top k, even when the answer is absent.
out_of_scope = ["Do you offer a student discount?",
                "Who is the chief executive?",
                "Can I book an installation visit?"]

def head(text, n=24):        # a chunk's first words, cut at a word
    return text[:n].rsplit(" ", 1)[0] + " ..."

print(f"{'score':>6}  {'question':<44} top chunk retrieved")
for q, _ in queries[:2]:
    s = dense @ embed(q)
    print(f"{s.max():>6.2f}  {q:<44} {head(texts[s.argmax()])}")
print()
for q in out_of_scope:
    s = dense @ embed(q)
    print(f"{s.max():>6.2f}  {q:<44} {head(texts[s.argmax()])}")

THRESH = 0.55
bad = [q for q in out_of_scope if (dense @ embed(q)).max() >= THRESH]
print(f"\na floor at {THRESH} rejects {3 - len(bad)} of 3 out-of-scope "
      f"questions, and still lets through:")
for q in bad:
    print(f"  {q}")
