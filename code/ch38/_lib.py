import re, numpy as np
text = open("policy.md").read()
sections = re.split(r"\n(?=# )", text)
chunks = []
for sec in sections:
    title = sec.split("\n")[0].lstrip("# ").strip()
    body = " ".join(sec.split("\n")[1:]).strip()
    for sent in re.split(r"(?<=\.)\s+", body):
        if sent:
            chunks.append({"section": title, "text": sent})
texts = [c["text"] for c in chunks]

# Ten questions, with the index of the chunk that actually answers each.
queries = [
    ("How long do I have to send something back?",        0),
    ("When will the money reach my card?",                2),
    ("Can I get my money back on a gift voucher?",        3),
    ("How fast is the quickest delivery option?",         5),
    ("Do you deliver overseas and who pays the duty?",    7),
    ("What if my device stops working from a fault?",     8),
    ("Is water damage covered?",                          9),
    ("I forgot my login credentials.",                   11),
    ("What happens to a dormant profile?",               12),
    ("What is the penalty for paying an invoice late?",  16),
]
