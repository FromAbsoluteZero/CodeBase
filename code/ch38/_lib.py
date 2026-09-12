import re, numpy as np, os as _os
# policy.md and tickets.txt are written by this chapter's own blocks (Step 1, gen_docs.py, and
# Step 5, gen_tickets.py), which the README's command runs in their printed places. If either
# block was skipped, write its file here so the later blocks still run: Step 1's line prints
# where the book prints it; Step 5's is written quietly so nothing appears out of order.
if not _os.path.exists("policy.md") and _os.path.exists("gen_docs.py"):
    exec(open("gen_docs.py").read())
if not _os.path.exists("tickets.txt") and _os.path.exists("gen_tickets.py"):
    import io as _io, contextlib as _cl
    with _cl.redirect_stdout(_io.StringIO()): exec(open("gen_tickets.py").read())
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

