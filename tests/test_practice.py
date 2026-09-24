#!/usr/bin/env python3
"""Practice and reference integrity tests.

They check that the question bank is well formed, that every generated page is up to date, that the
IDs Q1 to Q185 are all present and untouched in number, that new questions continue from Q186, that
every exercise attached to a question exists and passes its own check on the reference solution, that
relative links and anchors resolve, that every book-derived page carries its licence footer, and that
nothing personal or credential-like slipped in. Standard library only.

Run:  python tests/test_practice.py     reports every failure, then exits 1
  or: pytest tests/                     fails the run on the first failed check
Add --skip-exercises to leave out running the exercise checks (they need the pinned libraries).
"""
import csv, re, subprocess, sys, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_practice as bp  # noqa: E402

failures = []
_RUNNING_AS_SCRIPT = False
PRACTICE = ROOT / "practice"
REFERENCE = ROOT / "reference"


def check(name, condition, detail=""):
    if condition:
        print(f"  ok    {name}")
        return
    print(f"  FAIL  {name}  {detail}")
    failures.append(name)
    if not _RUNNING_AS_SCRIPT:
        raise AssertionError(f"{name}  {detail}")


def _bank():
    meta, topics, questions, mocks = bp.load_bank()
    return meta, topics, questions, mocks, bp.chapter_titles()


def test_bank_is_valid():
    print("\nQuestion bank is well formed")
    meta, topics, questions, mocks, chapters = _bank()
    errs = bp.validate(meta, topics, questions, mocks, chapters)
    check("validate() reports no problems", not errs, "; ".join(errs[:5]))


def test_printed_ids_are_stable():
    print("\nQ1 to Q185 are permanent, new questions continue from Q186")
    _, _, questions, _, _ = _bank()
    nums = sorted(bp.qnum(q["id"]) for q in questions)
    check("Q1 to Q185 all present", nums[:185] == list(range(1, 186)),
          f"first missing: {next((n for n in range(1, 186) if n not in nums), None)}")
    new = [n for n in nums if n > 185]
    check("new ids are consecutive from Q186", new == list(range(186, 186 + len(new))), str(new[:5]))
    printed = {q["id"] for q in questions if bp.qnum(q["id"]) <= 185}
    check("no printed id was retired or renamed", len(printed) == 185)


def test_generated_pages_are_current():
    print("\nGenerated pages match the bank")
    out = bp.build()
    stale = bp.stale_files(out)
    check("no stale generated files (run python scripts/build_practice.py)", not stale,
          ", ".join(p.relative_to(ROOT).as_posix() for p in stale[:5]))
    for n in range(1, 46):
        check(f"practice/by-chapter/ch{n:02d}.md exists", (PRACTICE / "by-chapter" / f"ch{n:02d}.md").exists())


def test_chapter_titles_match_chapter_map():
    print("\nChapter titles agree with docs/CHAPTER_MAP.md")
    chapters = bp.chapter_titles()
    text = (ROOT / "docs" / "CHAPTER_MAP.md").read_text(encoding="utf-8")
    rows = {int(m.group(1)): m.group(2).strip()
            for m in re.finditer(r"^\| (\d{1,2}) \| ([^|]+?) \|", text, re.M)}
    for n in range(1, 46):
        check(f"chapter {n} title", rows.get(n) == chapters[n]["title"],
              f"map says {rows.get(n)!r}, bank says {chapters[n]['title']!r}")


def test_chapter_map_practice_counts():
    print("\ndocs/CHAPTER_MAP.md practice column matches the bank")
    _, _, questions, _, _ = _bank()
    text = (ROOT / "docs" / "CHAPTER_MAP.md").read_text(encoding="utf-8")
    counts = {n: sum(1 for q in questions if q["chapters"] and q["chapters"][0] == n) for n in range(1, 46)}
    for m in re.finditer(r"^\| (\d{1,2}) \|(?:[^|]*\|){7}\s*\[(\d+)\]\(\.\./practice/by-chapter/ch(\d{2})\.md\)", text, re.M):
        n, shown, link = int(m.group(1)), int(m.group(2)), int(m.group(3))
        check(f"chapter {n} practice count {shown}", shown == counts[n] and link == n, f"bank has {counts[n]}")
    found = len(re.findall(r"\]\(\.\./practice/by-chapter/ch\d{2}\.md\)", text))
    check("every chapter row links its practice page", found == 45, f"found {found}")


def test_exercises_exist_and_pass():
    print("\nExercises")
    _, _, questions, _, _ = _bank()
    ex = [q for q in questions if q.get("exercise")]
    check("at least one exercise per area", {e["exercise"].split("/")[0] for e in ex} >= {"python", "pandas", "sql", "challenges"})
    for q in ex:
        d = PRACTICE / "exercises" / q["exercise"]
        starter = next(iter(d.glob("starter.*")), None)
        solution = next(iter(d.glob("solution.*")), None)
        check(f"{q['id']} has README, starter, solution, check", all(p is not None and p.exists() for p in (starter, solution)) and (d / "README.md").exists() and (d / "check.py").exists())
        check(f"{q['id']} README names the question id", q["id"] in (d / "README.md").read_text(encoding="utf-8"))
        check(f"{q['id']} dataset exists", (ROOT / "data" / "generated" / q["dataset"]).exists(), q["dataset"])
    if "--skip-exercises" in sys.argv:
        print("  (exercise checks skipped)")
        return
    for q in ex:
        d = PRACTICE / "exercises" / q["exercise"]
        r = subprocess.run([sys.executable, str(d / "check.py"), "--solution"], capture_output=True, text=True)
        check(f"{q['id']} solution passes its check", r.returncode == 0, (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else "")
        r = subprocess.run([sys.executable, str(d / "check.py")], capture_output=True, text=True)
        check(f"{q['id']} starter fails its check (nothing is pre-solved)", r.returncode != 0)


def test_mocks():
    print("\nMock interviews")
    _, _, questions, mocks, _ = _bank()
    ids = {q["id"] for q in questions}
    check("at least eight sets", len(mocks) >= 8)
    for m in mocks:
        total = sum(i["minutes"] for i in m["items"])
        check(f"{m['id']} minutes add up ({total})", total == m["minutes"])
        check(f"{m['id']} questions exist", all(i["q"] in ids for i in m["items"]))
        page = PRACTICE / "mock-interviews" / f"{bp.mock_file(m)}.md"
        review = PRACTICE / "mock-interviews" / f"{bp.mock_file(m)}-review.md"
        check(f"{m['id']} question sheet carries no answer notes", page.exists() and "What a strong answer contains" not in page.read_text(encoding="utf-8"))
        check(f"{m['id']} review sheet exists", review.exists())


def _md_files():
    files = list(PRACTICE.rglob("*.md")) + list(REFERENCE.rglob("*.md")) + [ROOT / "README.md", ROOT / "LICENSING.md", ROOT / "CONTRIBUTING.md"] + list((ROOT / "docs").glob("*.md"))
    return [p for p in files if "bank" not in p.parts or p.name == "README.md"]


def test_links_and_anchors():
    print("\nRelative links and anchors resolve")
    anchors = {}
    for p in _md_files():
        text = p.read_text(encoding="utf-8")
        ids = set(re.findall(r'<a id="([^"]+)"></a>', text))
        for h in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.M):
            slug = re.sub(r"[^\w\s-]", "", h.lower()).strip().replace(" ", "-")
            slug = re.sub(r"-+", "-", slug)
            ids.add(slug)
        anchors[p.resolve()] = ids
    bad = []
    for p in _md_files():
        text = p.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, frag = target.partition("#")
            dest = (p.parent / path).resolve() if path else p.resolve()
            if path and not dest.exists():
                bad.append(f"{p.relative_to(ROOT)} -> {target} (missing)")
                continue
            if frag and dest.is_file() and dest.suffix == ".md" and frag not in anchors.get(dest, set()):
                bad.append(f"{p.relative_to(ROOT)} -> {target} (no such anchor)")
    check("all relative links and anchors resolve", not bad, "; ".join(bad[:6]))


def test_licence_footers():
    print("\nLicence footers on book-derived pages")
    missing = []
    for p in list(PRACTICE.rglob("*.md")) + list(REFERENCE.rglob("*.md")):
        if p.parent == PRACTICE / "bank" or p.parent == REFERENCE / "templates":
            continue
        if p.parent.parent == PRACTICE / "exercises" or p.parent.parent.parent == PRACTICE / "exercises":
            continue  # exercise READMEs are covered by practice/exercises/README.md's footer
        text = p.read_text(encoding="utf-8")
        if "CC BY-NC-SA 4.0" not in text and "LICENSING.md" not in text:
            missing.append(p.relative_to(ROOT).as_posix())
    check("every generated or hand-written practice/reference page names its licence", not missing, ", ".join(missing[:6]))
    for name in ("CC-BY-NC-SA-4.0.txt", "CC0-1.0.txt", "MIT.txt"):
        check(f"LICENSES/{name} present", (ROOT / "LICENSES" / name).exists())


def test_hygiene():
    print("\nHygiene")
    rx_path = re.compile(r"/Users/[A-Za-z]|/home/[A-Za-z]|C:\\Users\\|/private/tmp/")
    rx_credit = re.compile(r"(?i)co-authored-by|generated with \[|noreply@anthropic\.com")
    hits = []
    for p in list(PRACTICE.rglob("*")) + list(REFERENCE.rglob("*")) + [ROOT / "scripts" / "build_practice.py", ROOT / "LICENSING.md", ROOT / "docs" / "ERRATA.md"]:
        if not p.is_file() or p.suffix not in {".md", ".toml", ".py", ".sql", ".csv", ".gitignore", ""}:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if rx_path.search(text) or rx_credit.search(text):
            hits.append(p.relative_to(ROOT).as_posix())
    check("no personal paths or tool credits", not hits, ", ".join(hits[:5]))
    ignored = [line.strip() for line in (ROOT / ".gitignore").read_text().splitlines() if line.strip() and not line.startswith("#")]
    import fnmatch
    shadowed = []
    for p in list(PRACTICE.rglob("*")) + list(REFERENCE.rglob("*")):
        if "__pycache__" in p.parts or p.suffix == ".pyc":
            continue  # bytecode is meant to be ignored
        if p.is_file() and any(fnmatch.fnmatch(p.name, pat) for pat in ignored if "/" not in pat):
            shadowed.append(p.relative_to(ROOT).as_posix())
    check("no practice or reference file matches a .gitignore pattern", not shadowed, ", ".join(shadowed[:5]))


def test_printed_paths():
    print("\nPaths the printed book names exist")
    for line in (ROOT / "tests" / "printed_paths.txt").read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            check(line, (ROOT / line).exists(), "printed in the book but missing")


def test_tracker():
    print("\nTracker")
    _, _, questions, _, _ = _bank()
    raw = (PRACTICE / "tracker.csv").read_bytes()
    check("tracker.csv starts with a UTF-8 byte-order mark (for Excel)", raw.startswith(b"\xef\xbb\xbf"))
    rows = list(csv.DictReader(raw.decode("utf-8-sig").splitlines()))
    check("one row per question", len(rows) == len(questions), f"{len(rows)} rows")
    check("blank progress columns", all(r["status"] == "" and r["notes"] == "" for r in rows))


def main():
    global _RUNNING_AS_SCRIPT
    _RUNNING_AS_SCRIPT = True
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print()
    if failures:
        print(f"{len(failures)} check(s) failed:")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("All practice checks passed.")


if __name__ == "__main__":
    main()
