# A retriever always returns its top k, even when the answer is absent.
out_of_scope = ["Do you offer a student discount?",
                "Who is the chief executive?",
                "Can I book an installation visit?"]

print(f"{'score':>6}  {'question':<44} top chunk retrieved")
for q, _ in queries[:2]:
    s = dense @ embed(q)
    print(f"{s.max():>6.2f}  {q:<44} {texts[s.argmax()][:34]}")
print()
for q in out_of_scope:
    s = dense @ embed(q)
    print(f"{s.max():>6.2f}  {q:<44} {texts[s.argmax()][:34]}")

THRESH = 0.55
bad = [q for q in out_of_scope if (dense @ embed(q)).max() >= THRESH]
print(f"\na floor at {THRESH} rejects {3 - len(bad)} of 3 out-of-scope "
      f"questions, and still lets through:")
for q in bad:
    print(f"  {q}")
