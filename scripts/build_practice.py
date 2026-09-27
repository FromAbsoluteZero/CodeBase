"""Build the practice pages from the question bank.

The bank in practice/bank/ is the only place questions are written. Every page under
practice/by-chapter, practice/by-topic, practice/mock-interviews, practice/by-level.md,
practice/by-type.md, practice/exercises/README.md, practice/tracker.csv and the generated
block of practice/README.md is produced from it by this script.

    python scripts/build_practice.py            write every generated file
    python scripts/build_practice.py --check    change nothing; exit 1 if any file is stale

Standard library only (Python 3.11 or newer, for tomllib).
"""
from __future__ import annotations

import csv
import io
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRACTICE = ROOT / "practice"
BANK = PRACTICE / "bank"

LEVELS = ["beginner", "intermediate", "advanced", "any"]
LEVEL_TITLES = {"beginner": "Beginner", "intermediate": "Intermediate",
                "advanced": "Advanced", "any": "Any level (behavioural)"}
TYPES = ["conceptual", "coding", "scenario", "behavioural"]
TYPE_TITLES = {
    "conceptual": "Conceptual: explain, compare, derive",
    "coding": "Coding: write and run it",
    "scenario": "Scenario: a situation, a number, a design or a business case",
    "behavioural": "Behavioural: how you work",
}
ID_RE = re.compile(r"^Q([1-9][0-9]*)$")
FIRST_PRINTED, LAST_PRINTED = 1, 185

TEXT_LICENCE = (
    "Question and answer text © 2026 Shanmukh Behara, licensed under "
    "[CC BY-NC-SA 4.0]({up}LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence "
    "that applies to the code. See [LICENSING.md]({up}LICENSING.md)."
)
BLOCK_START = "<!-- generated:start (edit practice/bank, then run python scripts/build_practice.py) -->"
BLOCK_END = "<!-- generated:end -->"


# --------------------------------------------------------------------------- loading

def load_bank():
    """Return (meta, topics, questions, mocks). Questions keep file order within a topic."""
    meta = tomllib.loads((BANK / "meta.toml").read_text(encoding="utf-8"))
    topics = tomllib.loads((BANK / "topics.toml").read_text(encoding="utf-8"))["topic"]
    questions = []
    for t in topics:
        path = BANK / f"{t['slug']}.toml"
        data = tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        for q in data.get("question", []):
            q = dict(q)
            q["topic"] = t["slug"]
            questions.append(q)
    mocks = tomllib.loads((BANK / "mocks.toml").read_text(encoding="utf-8")).get("mock", [])
    return meta, topics, questions, mocks


def chapter_titles():
    data = tomllib.loads((BANK / "chapters.toml").read_text(encoding="utf-8"))
    return {c["number"]: c for c in data["chapter"]}


def qnum(qid):
    return int(ID_RE.match(qid).group(1))


# --------------------------------------------------------------------------- validation

def validate(meta, topics, questions, mocks, chapters):
    """Return a list of problems. An empty list means the bank is consistent."""
    errs = []
    slugs = [t["slug"] for t in topics]
    if len(set(slugs)) != len(slugs):
        errs.append("topics.toml lists a topic twice")
    for f in BANK.glob("*.toml"):
        if f.stem not in slugs + ["topics", "meta", "mocks", "chapters"]:
            errs.append(f"{f.name} is not listed in topics.toml, so its questions would be ignored")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta.get("updated", ""))):
        errs.append("meta.toml needs updated = \"YYYY-MM-DD\"")
    if sorted(chapters) != list(range(1, 46)):
        errs.append("chapters.toml must list chapters 1 to 45")

    ids = []
    for q in questions:
        where = f"{q.get('id', '?')} in {q['topic']}.toml"
        for field in ("id", "question", "answer", "chapters", "level", "type"):
            if field not in q:
                errs.append(f"{where}: missing field {field}")
        if "id" not in q:
            continue
        if not ID_RE.match(q["id"]):
            errs.append(f"{where}: id must look like Q12")
            continue
        ids.append(q["id"])
        if q.get("level") not in LEVELS:
            errs.append(f"{where}: level must be one of {LEVELS}")
        if q.get("type") not in TYPES:
            errs.append(f"{where}: type must be one of {TYPES}")
        if (q.get("level") == "any") != (q.get("type") == "behavioural"):
            errs.append(f"{where}: level 'any' is used for behavioural questions, and only for them")
        chs = q.get("chapters", [])
        if not all(isinstance(c, int) and 1 <= c <= 45 for c in chs):
            errs.append(f"{where}: chapters must be chapter numbers from 1 to 45")
        if len(set(chs)) != len(chs):
            errs.append(f"{where}: a chapter is listed twice")
        if not chs and q.get("type") != "behavioural":
            errs.append(f"{where}: only behavioural questions may have no chapter")
        for field in ("question", "answer", "beyond_book", "revised"):
            if field in q and not str(q[field]).strip():
                errs.append(f"{where}: {field} is empty")
        ex = q.get("exercise")
        if q.get("type") == "coding" and qnum(q["id"]) > LAST_PRINTED and not ex:
            errs.append(f"{where}: new coding questions need an exercise folder")
        if ex:
            d = PRACTICE / "exercises" / ex
            if not d.is_dir():
                errs.append(f"{where}: exercise folder practice/exercises/{ex} does not exist")
            elif not d.name.startswith(q["id"].lower() + "-"):
                errs.append(f"{where}: exercise folder name must start with {q['id'].lower()}-")
            else:
                for need in ("README.md", "check.py"):
                    if not (d / need).exists():
                        errs.append(f"{where}: practice/exercises/{ex}/{need} is missing")
            if "dataset" not in q:
                errs.append(f"{where}: exercises must name the dataset they use")
    if len(set(ids)) != len(ids):
        dup = sorted({i for i in ids if ids.count(i) > 1}, key=qnum)
        errs.append(f"duplicate ids: {dup}")
    nums = sorted(qnum(i) for i in set(ids))
    printed = [n for n in nums if n <= LAST_PRINTED]
    if printed != list(range(FIRST_PRINTED, LAST_PRINTED + 1)):
        missing = sorted(set(range(FIRST_PRINTED, LAST_PRINTED + 1)) - set(printed))
        errs.append(f"Q1 to Q185 are permanent and must all be present; missing {missing[:10]}")
    new = [n for n in nums if n > LAST_PRINTED]
    if new and new != list(range(LAST_PRINTED + 1, LAST_PRINTED + 1 + len(new))):
        errs.append("new questions must be numbered from Q186 without gaps")
    known = set(ids)
    for q in questions:
        for r in q.get("related", []):
            if r not in known:
                errs.append(f"{q['id']}: related question {r} does not exist")
            if r == q["id"]:
                errs.append(f"{q['id']}: relates to itself")
    ex_dirs = {p.parent.relative_to(PRACTICE / "exercises").as_posix()
               for p in (PRACTICE / "exercises").glob("*/*/check.py")}
    used = [q["exercise"] for q in questions if q.get("exercise")]
    for d in sorted(ex_dirs - set(used)):
        errs.append(f"practice/exercises/{d} is not attached to any question")
    for d in {u for u in used if used.count(u) > 1}:
        errs.append(f"practice/exercises/{d} is attached to more than one question")

    mids = [m.get("id") for m in mocks]
    if len(set(mids)) != len(mids):
        errs.append("mocks.toml repeats an id")
    for m in mocks:
        for field in ("id", "slug", "title", "minutes", "round", "suits", "items"):
            if field not in m:
                errs.append(f"mock {m.get('id', '?')}: missing {field}")
        items = m.get("items", [])
        if sum(i.get("minutes", 0) for i in items) != m.get("minutes"):
            errs.append(f"mock {m.get('id')}: item minutes add up to "
                        f"{sum(i.get('minutes', 0) for i in items)}, not {m.get('minutes')}")
        qs = [i.get("q") for i in items]
        if len(set(qs)) != len(qs):
            errs.append(f"mock {m.get('id')}: a question appears twice")
        for i in qs:
            if i not in known:
                errs.append(f"mock {m.get('id')}: {i} does not exist")
    return errs


# --------------------------------------------------------------------------- rendering

def md_escape_table(s):
    return s.replace("|", "\\|")


def ch_links(chs, up):
    return " · ".join(f"[{c}]({up}by-chapter/ch{c:02d}.md)" for c in chs) or "none"


def licence_line(depth):
    """depth = number of folders below the repository root."""
    up = "../" * depth
    return "<sub>" + TEXT_LICENCE.format(up=up) + "</sub>"


def question_block(q, depth_practice, topics_by_slug, exercises_rel="exercises/"):
    """Render one question with its answer folded shut. depth_practice: '' for practice/, '../' below it."""
    up = depth_practice
    out = [f'<a id="{q["id"].lower()}"></a>', ""]
    out.append(f'**{q["id"]}.** {q["question"]}')
    out.append("")
    meta_bits = [f"Chapters {ch_links(q['chapters'], up)}" if q["chapters"] else "No chapter: about how you work",
                 q["level"] if q["level"] != "any" else "any level", q["type"]]
    out.append("<sub>" + " &nbsp;·&nbsp; ".join(meta_bits) + "</sub>")
    out.append("")
    if q.get("exercise"):
        out.append(f'Exercise: [{q["exercise"]}]({up}exercises/{q["exercise"]}/) · data: `{q["dataset"]}`')
        out.append("")
    if q.get("beyond_book"):
        out.append(f"> **Beyond the book.** {q['beyond_book']}")
        out.append("")
    out += ["<details>", "<summary>What a strong answer contains</summary>", "", q["answer"], ""]
    if q.get("related"):
        rel = ", ".join(link_q(r, up, topics_by_slug) for r in q["related"])
        out += [f"Related: {rel}", ""]
    if q.get("revised"):
        out += [f"*Revised: {q['revised']}*", ""]
    out += ["</details>", ""]
    return out


_QINDEX = {}


def link_q(qid, up, topics_by_slug=None):
    q = _QINDEX[qid]
    return f"[{qid}]({up}by-topic/{q['topic']}.md#{qid.lower()})"


def short(text, n=110):
    text = " ".join(text.split())
    return text if len(text) <= n else text[: n - 1].rsplit(" ", 1)[0] + "…"


def render_topic(t, qs, meta, topics_by_slug, mocks_by_q):
    lines = [f"# {t['title']}", "", t["blurb"], "",
             f"Track: {t['track']} · {len(qs)} question{'s' if len(qs) != 1 else ''} · "
             f"[All topics](README.md) · [Practice home](../README.md)", ""]
    counts = {lv: sum(q["level"] == lv for q in qs) for lv in LEVELS}
    tcounts = {ty: sum(q["type"] == ty for q in qs) for ty in TYPES}
    lines.append("Levels: " + ", ".join(f"{lv} {n}" for lv, n in counts.items() if n) +
                 ". Types: " + ", ".join(f"{ty} {n}" for ty, n in tcounts.items() if n) + ".")
    lines.append("")
    lines.append("Answer each question aloud before you open its note.")
    lines.append("")
    for q in qs:
        lines += question_block(q, "../", topics_by_slug)
    lines += ["---", "", licence_line(2), ""]
    return "\n".join(lines)


def render_topics_index(topics, by_topic, meta):
    lines = ["# Questions by topic", "",
             "Topics are grouped into tracks. Each topic page lists its questions with the notes folded shut.",
             "", "[Practice home](../README.md)", ""]
    track = None
    for t in topics:
        if t["track"] != track:
            track = t["track"]
            lines += [f"## {track}", "", "| Topic | Questions | What it covers |", "|---|---:|---|"]
        lines.append(f"| [{t['title']}]({t['slug']}.md) | {len(by_topic[t['slug']])} | {md_escape_table(t['blurb'])} |")
        nxt = topics[topics.index(t) + 1]["track"] if topics.index(t) + 1 < len(topics) else None
        if nxt != track:
            lines.append("")
    lines += ["---", "", licence_line(2), ""]
    return "\n".join(lines)


def render_chapter(n, info, primary, secondary, mocks_for, topics_by_slug):
    title = info["title"]
    lines = [f"# Chapter {n} · {title}", ""]
    lines.append("Interview practice that draws on this chapter. The chapter's own practice problems, "
                 "with their solutions, are in the book; work those first.")
    lines.append("")
    links = []
    if info.get("code"):
        links.append(f"code: [{info['code']}](../../{info['code']}/)")
    if info.get("notebook"):
        links.append(f"notebook: [{info['notebook']}](../../{info['notebook']})")
    if links:
        lines.append("Companion " + " · ".join(links) + ".")
    else:
        lines.append("This chapter has no companion code folder; "
                     "[docs/CHAPTER_MAP.md](../../docs/CHAPTER_MAP.md) says why.")
    lines += ["", f"[All chapters](README.md) · [Practice home](../README.md)", ""]
    if not primary and not secondary:
        lines += ["No interview questions draw on this chapter yet.", ""]
    if primary:
        lines += [f"## Questions that start here ({len(primary)})", ""]
        for q in primary:
            lines += question_block(q, "../", topics_by_slug)
    if secondary:
        lines += [f"## Questions that also draw on this chapter ({len(secondary)})", ""]
        for q in secondary:
            lines.append(f"- {link_q(q['id'], '../')} {short(q['question'])} "
                         f"<sub>(starts in chapter {q['chapters'][0]})</sub>")
        lines.append("")
    if mocks_for:
        lines += ["## Mock interviews that use these questions", ""]
        for m in mocks_for:
            lines.append(f"- [{m['id']} · {m['title']}](../mock-interviews/{m['id'].lower()}-{m['slug']}.md)")
        lines.append("")
    lines += ["---", "", licence_line(2), ""]
    return "\n".join(lines)


def render_chapters_index(chapters, prim_count, sec_count):
    lines = ["# Questions by chapter", "",
             "Each chapter page lists the questions that start in that chapter, then the ones that also "
             "draw on it. A question's first chapter is where its idea is taught; practise it once you "
             "have finished that chapter.", "", "[Practice home](../README.md)", "",
             "| Chapter | Title | Starts here | Also draws on it |", "|---:|---|---:|---:|"]
    for n in range(1, 46):
        lines.append(f"| {n} | [{md_escape_table(chapters[n]['title'])}](ch{n:02d}.md) | "
                     f"{prim_count[n]} | {sec_count[n]} |")
    lines += ["", "---", "", licence_line(2), ""]
    return "\n".join(lines)


def render_grouped(title, intro, groups, order, titles):
    lines = [f"# {title}", "", intro, "", "[Practice home](README.md)", ""]
    for key in order:
        qs = groups.get(key, [])
        lines += [f"## {titles[key]} ({len(qs)})", ""]
        for q in qs:
            ch = f" · chapter {q['chapters'][0]}" if q["chapters"] else ""
            lines.append(f"- [{q['id']}](by-topic/{q['topic']}.md#{q['id'].lower()}) {short(q['question'])}"
                         f" <sub>({q['topic']}{ch})</sub>")
        lines.append("")
    lines += ["---", "", licence_line(1), ""]
    return "\n".join(lines)


def mock_file(m):
    return f"{m['id'].lower()}-{m['slug']}"


def render_mock(m, qindex):
    lines = [f"# {m['id']} · {m['title']}", "",
             f"{m['minutes']} minutes · round: {m['round']} · suits: {m['suits']}", "",
             "**How to run it.** Set a timer for the full time. Answer each question aloud, in order, and keep "
             "to its minutes; record yourself if you can. For a coding item, open the exercise and write the "
             "solution without looking at its solution file. Do not open the review sheet until the time is up.",
             "", "| # | Question | Minutes |", "|---:|---|---:|"]
    for k, it in enumerate(m["items"], 1):
        q = qindex[it["q"]]
        text = md_escape_table(" ".join(q["question"].split()))
        if q.get("exercise"):
            text += f" <br><sub>Exercise: [{q['exercise']}](../exercises/{q['exercise']}/)</sub>"
        lines.append(f"| {k} | **{q['id']}** {text} | {it['minutes']} |")
    lines += ["", "## After the timer", "",
              f"Open the [review sheet]({mock_file(m)}-review.md) and compare each answer with its note. Then ask:",
              "",
              "- Did I state my assumptions before answering?",
              "- Did I name the trade-off instead of claiming one right answer?",
              "- Did I say what I would check, and what would change my mind?",
              "- What would the follow-up question be, and could I answer it?",
              "- Where I stalled, which chapter does the question point to?",
              "", "[All mock interviews](README.md) · [Practice home](../README.md)",
              "", "---", "", licence_line(2), ""]
    return "\n".join(lines)


def render_mock_review(m, qindex):
    lines = [f"# {m['id']} · {m['title']}: review sheet", "",
             f"Read this only after you have sat the [mock interview]({mock_file(m)}.md).", ""]
    for k, it in enumerate(m["items"], 1):
        q = qindex[it["q"]]
        lines += [f"## {k}. {q['id']}", "", q["question"], "",
                  f"<sub>Chapters {ch_links(q['chapters'], '../')}</sub>" if q["chapters"] else
                  "<sub>No chapter: about how you work</sub>", ""]
        if q.get("exercise"):
            lines += [f"Check your code: `python practice/exercises/{q['exercise']}/check.py`", ""]
        lines += ["**What a strong answer contains.** " + q["answer"], ""]
    lines += ["[Back to the mock interview](" + mock_file(m) + ".md)", "", "---", "", licence_line(2), ""]
    return "\n".join(lines)


def render_mocks_index(mocks, qindex):
    lines = ["# Mock interviews", "",
             "Timed sets built from the rounds of a typical interview loop: a coding exercise, a screen on "
             "concepts, a design or business case, a deep dive into your own work, and a conversation about "
             "how you work. Each set has a question sheet with no answers on it and a separate review sheet.",
             "",
             "The deep-dive round is about your own project, so no set can be written for it. Prepare it with "
             "your portfolio (Appendix B of the book) and the interview prompts in "
             "[reference/ai-assistant-prompts.md](../../reference/ai-assistant-prompts.md#interview-preparation).",
             "", "| Set | Round | Minutes | Questions | Suits |", "|---|---|---:|---:|---|"]
    for m in mocks:
        lines.append(f"| [{m['id']} · {m['title']}]({mock_file(m)}.md) | {m['round']} | {m['minutes']} | "
                     f"{len(m['items'])} | {m['suits']} |")
    lines += ["", "[Practice home](../README.md)", "", "---", "", licence_line(2), ""]
    return "\n".join(lines)


def render_exercises_index(questions):
    ex = [q for q in questions if q.get("exercise")]
    areas = {}
    for q in ex:
        areas.setdefault(q["exercise"].split("/")[0], []).append(q)
    names = {"python": "Python", "pandas": "pandas", "sql": "SQL", "challenges": "Multi-step challenges"}
    lines = ["# Coding exercises and challenges", "",
             "Every exercise runs on one of the book's own datasets in `data/generated/`, and every one has a "
             "check that tells you whether your answer is right. The reference solutions were run and checked "
             "before publication, under the library versions pinned in `requirements.txt`.", "",
             "**How to work one.** Read the exercise's README. Write your answer in its `starter` file, then "
             "run its check from the repository root, for example:", "",
             "```bash", "python practice/exercises/sql/q208-revenue-by-category/check.py", "```", "",
             "The check runs your starter file. `--solution` runs the reference solution instead; "
             "open it only after you have a working answer of your own.", ""]
    order = ["python", "pandas", "sql", "challenges"]
    for a in order + sorted(set(areas) - set(order)):
        if a not in areas:
            continue
        lines += [f"## {names.get(a, a)}", "", "| ID | Exercise | Level | Chapters | Data |", "|---|---|---|---|---|"]
        for q in sorted(areas[a], key=lambda q: qnum(q["id"])):
            name = q["exercise"].split("/")[1].split("-", 1)[1].replace("-", " ")
            lines.append(f"| {q['id']} | [{name}]({q['exercise']}/) — {md_escape_table(short(q['question'], 90))} | "
                         f"{q['level']} | {', '.join(str(c) for c in q['chapters'])} | `{q['dataset']}` |")
        lines.append("")
    lines += ["[Practice home](../README.md)", "", "---", "",
              "<sub>Exercise text © 2026 Shanmukh Behara, licensed under "
              "[CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). The exercise code (every "
              "`starter`, `solution` and `check` file) is MIT-licensed like the rest of the code. "
              "See [LICENSING.md](../../LICENSING.md).</sub>", ""]
    return "\n".join(lines)


def render_tracker(questions):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["id", "topic", "first_chapter", "chapters", "level", "type", "question",
                "status", "last_practised", "confidence", "notes"])
    for q in sorted(questions, key=lambda q: qnum(q["id"])):
        w.writerow([q["id"], q["topic"], q["chapters"][0] if q["chapters"] else "",
                    " ".join(str(c) for c in q["chapters"]), q["level"], q["type"],
                    " ".join(q["question"].split()), "", "", "", ""])
    return "﻿" + buf.getvalue()


def render_readme_block(meta, topics, questions, mocks):
    printed = sum(1 for q in questions if qnum(q["id"]) <= LAST_PRINTED)
    new = len(questions) - printed
    by_type = {t: sum(q["type"] == t for q in questions) for t in TYPES}
    by_level = {lv: sum(q["level"] == lv for q in questions) for lv in LEVELS}
    ex = [q for q in questions if q.get("exercise")]
    ex_area = {}
    for q in ex:
        ex_area[q["exercise"].split("/")[0]] = ex_area.get(q["exercise"].split("/")[0], 0) + 1
    last = max(qnum(q["id"]) for q in questions)
    lines = [BLOCK_START, "",
             f"**{len(questions)} questions**, Q1 to Q{last}: the 185 first written for the book (Q1 to Q185) "
             f"and {new} added since (Q186 on). Bank last updated {meta['updated']}.", "",
             "| By type | | By level | |", "|---|---:|---|---:|"]
    rows = max(len(TYPES), len(LEVELS))
    for i in range(rows):
        a = (TYPES[i], by_type[TYPES[i]]) if i < len(TYPES) else ("", "")
        b = (LEVELS[i], by_level[LEVELS[i]]) if i < len(LEVELS) else ("", "")
        lines.append(f"| {a[0]} | {a[1]} | {b[0]} | {b[1]} |")
    lines += ["", "Coding exercises with checks: " +
              ", ".join(f"{k} {v}" for k, v in sorted(ex_area.items())) + f". Mock interviews: {len(mocks)}.",
              "", BLOCK_END]
    return "\n".join(lines)


# --------------------------------------------------------------------------- build

def build():
    """Return {path: text} for every generated file."""
    meta, topics, questions, mocks = load_bank()
    chapters = chapter_titles()
    errs = validate(meta, topics, questions, mocks, chapters)
    if errs:
        raise SystemExit("The question bank has problems:\n  " + "\n  ".join(errs))
    _QINDEX.clear()
    _QINDEX.update({q["id"]: q for q in questions})
    topics_by_slug = {t["slug"]: t for t in topics}
    by_topic = {t["slug"]: [q for q in questions if q["topic"] == t["slug"]] for t in topics}
    mocks_by_q = {}
    for m in mocks:
        for it in m["items"]:
            mocks_by_q.setdefault(it["q"], []).append(m)

    out = {}
    for t in topics:
        out[PRACTICE / "by-topic" / f"{t['slug']}.md"] = render_topic(t, by_topic[t["slug"]], meta,
                                                                      topics_by_slug, mocks_by_q)
    out[PRACTICE / "by-topic" / "README.md"] = render_topics_index(topics, by_topic, meta)

    ordered = sorted(questions, key=lambda q: qnum(q["id"]))
    prim = {n: [q for q in ordered if q["chapters"] and q["chapters"][0] == n] for n in range(1, 46)}
    sec = {n: [q for q in ordered if n in q["chapters"][1:]] for n in range(1, 46)}
    for n in range(1, 46):
        ids = {q["id"] for q in prim[n] + sec[n]}
        ms = [m for m in mocks if any(it["q"] in ids for it in m["items"])]
        out[PRACTICE / "by-chapter" / f"ch{n:02d}.md"] = render_chapter(n, chapters[n], prim[n], sec[n], ms,
                                                                        topics_by_slug)
    out[PRACTICE / "by-chapter" / "README.md"] = render_chapters_index(
        chapters, {n: len(prim[n]) for n in prim}, {n: len(sec[n]) for n in sec})

    lv = {k: [q for q in ordered if q["level"] == k] for k in LEVELS}
    out[PRACTICE / "by-level.md"] = render_grouped(
        "Questions by level",
        "Beginner questions ask for one idea from one chapter. Intermediate questions connect two ideas, "
        "compare a trade-off or read a number in context. Advanced questions ask for a derivation, research-level "
        "depth or an open design. Behavioural questions have no level.",
        lv, LEVELS, LEVEL_TITLES)
    ty = {k: [q for q in ordered if q["type"] == k] for k in TYPES}
    out[PRACTICE / "by-type.md"] = render_grouped(
        "Questions by type",
        "Conceptual questions ask you to explain, compare or derive. Coding questions are answered by writing "
        "code, and each new one has a runnable exercise with a check. Scenario questions give you a situation, a "
        "number, a design or a business case. Behavioural questions are about how you work.",
        ty, TYPES, TYPE_TITLES)

    for m in mocks:
        out[PRACTICE / "mock-interviews" / f"{mock_file(m)}.md"] = render_mock(m, _QINDEX)
        out[PRACTICE / "mock-interviews" / f"{mock_file(m)}-review.md"] = render_mock_review(m, _QINDEX)
    out[PRACTICE / "mock-interviews" / "README.md"] = render_mocks_index(mocks, _QINDEX)
    out[PRACTICE / "exercises" / "README.md"] = render_exercises_index(questions)
    out[PRACTICE / "tracker.csv"] = render_tracker(questions)

    readme = PRACTICE / "README.md"
    text = readme.read_text(encoding="utf-8")
    if BLOCK_START not in text or BLOCK_END not in text:
        raise SystemExit("practice/README.md must contain the generated block markers")
    head, rest = text.split(BLOCK_START, 1)
    _, tail = rest.split(BLOCK_END, 1)
    out[readme] = head + render_readme_block(meta, topics, questions, mocks) + tail
    return out


def stale_files(out):
    """Generated files that differ from what is on disk, plus generated-folder files nobody generates."""
    stale = [p for p, text in out.items()
             if not p.exists() or p.read_bytes() != text.encode("utf-8")]
    for folder in ("by-chapter", "by-topic", "mock-interviews"):
        for p in (PRACTICE / folder).glob("*.md"):
            if p not in out:
                stale.append(p)
    return sorted(stale)


def main(argv):
    out = build()
    if "--check" in argv:
        stale = stale_files(out)
        if stale:
            print("These generated files are out of date; run python scripts/build_practice.py:")
            for p in stale:
                print("  " + p.relative_to(ROOT).as_posix())
            return 1
        print(f"practice pages are up to date ({len(out)} generated files)")
        return 0
    for folder in ("by-chapter", "by-topic", "mock-interviews"):
        for p in (PRACTICE / folder).glob("*.md"):
            if p not in out:
                p.unlink()
    for p, text in out.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))
    print(f"wrote {len(out)} generated files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
