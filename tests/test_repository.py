#!/usr/bin/env python3
"""Repository integrity tests.

These check that the repository is internally consistent: that documented files exist, that the
data manifest points at real files, and that no credentials have been committed. They do not
re-run the book's experiments.

Run:  python tests/test_repository.py     reports every failure, then exits 1
  or: pytest tests/                      fails the run on the first failed check
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures = []
_RUNNING_AS_SCRIPT = False

def check(name, condition, detail=""):
    if condition:
        print(f"  ok    {name}")
        return
    print(f"  FAIL  {name}  {detail}")
    failures.append(name)
    # pytest decides pass/fail from exceptions, so a check that only records a
    # failure would let `pytest tests/` report success on a broken repository.
    # Raise when running under pytest; when run as a script, main() collects
    # every failure first and then exits non-zero.
    if not _RUNNING_AS_SCRIPT:
        raise AssertionError(f"{name}  {detail}")

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
            # Rows for datasets that ship inside a dependency (scikit-learn's
            # load_digits and load_breast_cancer) name a call, not a path. They are
            # listed so the manifest is complete, and there is no file to check.
            if row.get("generated_or_external") == "bundled_with_scikit-learn":
                check(fn, True)
                continue
            # Chapter 38 writes its corpus into the working directory where the book
            # writes it, so the reader watches it being made. Nothing is shipped, so
            # there is no path to check here; test_generators_exist checks the script
            # that makes it, and code/ch38/_lib.py regenerates it if a block is skipped.
            if row.get("generated_or_external") == "generated_in_working_directory":
                check(fn, (ROOT / row["generation_script"]).exists(),
                      "written at runtime; its generator must exist")
                continue
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

def test_bridges_present_and_executed():
    print("\nFramework bridges")
    import json as _j
    bd = ROOT / "bridges"
    check("bridges/ directory", bd.exists())
    if not bd.exists():
        return
    for ch in (30, 31, 32, 33, 34, 35):
        nb = bd / f"ch{ch}_bridge.ipynb"
        ok = nb.exists()
        check(nb.name, ok)
        if not ok:
            continue
        d = _j.loads(nb.read_text())
        has_out = any(c.get("outputs") for c in d["cells"] if c["cell_type"] == "code")
        errs = [o for c in d["cells"] for o in c.get("outputs", []) if o.get("output_type") == "error"]
        check(f"{nb.name} carries saved outputs", has_out, "notebook has no outputs")
        check(f"{nb.name} executed without error", not errs, f"{len(errs)} error outputs")
    check("bridges/requirements-bridges.txt", (bd / "requirements-bridges.txt").exists())
    check("bridges/README.md", (bd / "README.md").exists())

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
    global _RUNNING_AS_SCRIPT
    _RUNNING_AS_SCRIPT = True
    print("Repository integrity checks")
    print("=" * 46)
    for fn in [test_required_files, test_manifest_files_exist, test_generators_exist,
               test_chapter_map_code_dirs, test_no_secrets, test_no_env_files,
               test_bridges_present_and_executed, test_notebooks_valid_json]:
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
