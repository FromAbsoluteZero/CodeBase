import numpy as np
rng = np.random.default_rng(5)

# Past support conversations. Each topic has its own vocabulary, and the
# same idea gets phrased many ways inside it. That pairing -- different
# words, same company -- is the only signal an encoder needs.
topics = {
  "refund_window": (["return", "send back", "give back", "ship back"],
     ["thirty days", "delivery date", "unused",
      "original packaging", "window"]),
  "refund_timing": (["refund", "money back", "reimbursement", "repayment"],
     ["payment method", "business days", "issued", "card", "processed"]),
  "voucher":       (["gift card", "gift voucher", "store credit"],
     ["purchase", "cannot", "non refundable", "balance"]),
  "fast_ship":     (["express", "quickest", "fastest", "rush delivery"],
     ["two business days", "before 2 pm", "arrives", "option", "upgrade"]),
  "abroad":        (["international", "overseas", "outside the country"],
     ["customs", "duties", "recipient", "twenty one days", "border"]),
  "fault":         (["defect", "fault", "manufacturing flaw",
                     "stopped working"],
     ["warranty", "one year", "replaced", "unit", "covered"]),
  "liquid":        (["water damage", "liquid damage", "spill"],
     ["misuse", "excluded", "not covered", "unauthorized repair"]),
  "login":         (["password", "login credentials", "sign in details"],
     ["reset", "screen", "email", "account access", "forgot"]),
  "dormant":       (["inactive", "dormant", "unused for months", "idle"],
     ["archived", "twenty four months", "account", "reactivate"]),
  "overdue":       (["late fee", "penalty for paying late", "overdue charge"],
     ["invoice", "1.5 percent", "monthly", "outstanding balance"]),
}

keys = list(topics)
generic = ["order", "account", "please", "team", "ticket", "policy"]
rows = []
for _ in range(6000):
    key = str(rng.choice(keys))
    terms, ctx = topics[key]
    # synonyms are not perfectly interchangeable: each has its own slight tilt
    t_i = int(rng.integers(len(terms)))
    term = terms[t_i]
    # each phrasing leans on the topic's context words a little differently
    w = np.full(len(ctx), 1.0)
    w[t_i % len(ctx)] += 2.2
    w[(t_i + 1) % len(ctx)] += 1.1
    words = [term] + list(rng.choice(ctx, 3, replace=False, p=w / w.sum()))
    if rng.random() < 0.18:                      # conversations wander
        other = topics[str(rng.choice(keys))][1]
        words.append(str(rng.choice(other)))
    words += list(rng.choice(generic, 2, replace=False))
    rng.shuffle(words)
    rows.append("customer asked about " + " ".join(words))

open("tickets.txt", "w").write("\n".join(rows))
print(f"wrote tickets.txt: {len(rows):,} past conversations across "
      f"{len(topics)} topics")
