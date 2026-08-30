import re

text = open("policy.md").read()

# Chunk on headings, then on sentences if a section runs long.
sections = re.split(r"\n(?=# )", text)
chunks = []
for sec in sections:
    title = sec.split("\n")[0].lstrip("# ").strip()
    body = " ".join(sec.split("\n")[1:]).strip()
    for sent in re.split(r"(?<=\.)\s+", body):
        if sent:
            chunks.append({"section": title, "text": sent})

print(f"{len(sections)} sections -> {len(chunks)} chunks")
for c in chunks[:4]:
    print(f"  [{c['section']:<9}] {c['text'][:62]}...")
