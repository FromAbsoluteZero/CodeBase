#!/usr/bin/env python3
"""Repository integrity tests.

These check that the repository is internally consistent: that documented files exist, that the
data manifest points at real files, and that no credentials have been committed. They do not
re-run the book's experiments.

Run:  python tests/test_repository.py     (or: pytest tests/)
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures = []

def check(name, condition, detail=""):
    if condition:
        print(f"  ok    {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        failures.append(name)

def test_required_files():
    print("\nRequired files")
    for f in ["README.md", "LICENSE", "requirements.txt", "DATA_MANIFEST.csv",
              "CITATION.cff", "SECURITY.md", ".gitignore",
              "docs/HOW_TO_USE.md", "docs/CHAPTER_MAP.md", "docs/REPRODUCIBILITY.md",
              "docs/DATA_GUIDE.md", "docs/TROUBLESHOOTING.md"]:
        check(f, (ROOT / f).exists())

def test_manifest_files_exist():
    print("\nDATA_MANIFEST references real files")
    with open(ROOT / "DATA_MANIFEST.csv", newline="") as fh:
        for row in csv.DictReader(fh):
            fn = row["filename"]
            check(fn, (ROOT / fn).exists(), "declared in manifest but missing")

def test_generators_exist():
    print("\nGeneration scripts referenced by the manifest exist")
    with open(ROOT / "DATA_MANIFEST.csv", newline="") as fh:
        for row in csv.DictReader(fh):
            g = row["generation_script"]
            if g.endswith(".py"):
                p = ROOT / g.replace("ch", "code/ch", 1) if not g.startswith("code/") else ROOT / g
                check(g, p.exists() or (ROOT / g).exists(), "generator not found")

def test_chapter_map_code_dirs():
    print("\nCode directories named in CHAPTER_MAP exist")
    text = (ROOT / "docs" / "CHAPTER_MAP.md").read_text()
    for m in sorted(set(re.findall(r"`(code/ch\d{2})/`", text))):
        check(m, (ROOT / m).is_dir(), "referenced in CHAPTER_MAP but missing")

def test_no_secrets():
    print("\nNo credentials committed")
    patterns = [
        (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key"),
        (re.compile(r"sk-[A-Za-z0-9]{20,}"), "API secret key"),
        (re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"), "private key"),
        (re.compile(r"(?i)(password|passwd|secret|api[_-]?key)\s*=\s*['\"][^'\"]{8,}"), "hardcoded credential"),
    ]
    hits = []
    for p in list(ROOT.rglob("*.py")) + list(ROOT.rglob("*.ipynb")) + list(ROOT.rglob("*.md")):
        if ".venv" in p.parts or "tests" in p.parts:
            continue
        try:
            txt = p.read_text(errors="replace")
        except Exception:
            continue
        for rx, what in patterns:
            if rx.search(txt):
                hits.append(f"{p.relative_to(ROOT)} ({what})")
    check("no secrets found", not hits, "; ".join(hits[:5]))

def test_no_env_files():
    print("\nNo .env or key files committed")
    bad = [p for p in ROOT.rglob("*") if p.is_file()
           and (p.name == ".env" or p.suffix in {".pem", ".key", ".p12"})]
    check("no .env/.pem/.key files", not bad, str([str(b.relative_to(ROOT)) for b in bad[:5]]))

def test_notebooks_valid_json():
    print("\nNotebooks are valid JSON")
    import json
    nbs = sorted((ROOT / "notebooks").glob("*.ipynb"))
    check("notebooks present", len(nbs) > 0)
    for nb in nbs:
        try:
            json.loads(nb.read_text())
            ok = True
        except Exception:
            ok = False
        check(nb.name, ok, "not valid JSON")

def main():
    print("Repository integrity checks")
    print("=" * 46)
    for fn in [test_required_files, test_manifest_files_exist, test_generators_exist,
               test_chapter_map_code_dirs, test_no_secrets, test_no_env_files,
               test_notebooks_valid_json]:
        fn()
    print("\n" + "=" * 46)
    if failures:
        print(f"{len(failures)} check(s) FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("All checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
