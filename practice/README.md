# Interview practice

The question bank for *From Absolute Zero*, with timed mock interviews, coding exercises on the book's own
datasets, and a tracker for your progress. Appendix C of the book explains how to prepare; this folder is
where you practise.

Nothing here needs Python unless you want to run the coding exercises. Every page reads in the browser, and
the whole repository downloads as a ZIP from the green **Code** button on the repository's front page.

<!-- generated:start (edit practice/bank, then run python scripts/build_practice.py) -->

**227 questions**, Q1 to Q227: the 185 first written for the book (Q1 to Q185) and 42 added since (Q186 on). Bank last updated 2026-09-23.

| By type | | By level | |
|---|---:|---|---:|
| conceptual | 134 | beginner | 69 |
| coding | 45 | intermediate | 130 |
| scenario | 41 | advanced | 21 |
| behavioural | 7 | any | 7 |

Coding exercises with checks: challenges 8, pandas 12, python 10, sql 12. Mock interviews: 13.

<!-- generated:end -->

## Ways in

| If you want to… | Go to |
|---|---|
| Practise a chapter you have just finished | [by-chapter/](by-chapter/README.md), for example [by-chapter/ch22.md](by-chapter/ch22.md) for Chapter 22 |
| Work through a subject, such as SQL or evaluation | [by-topic/](by-topic/README.md) |
| Start easy, or find the hard ones | [by-level.md](by-level.md) |
| Drill one kind of question: conceptual, coding, scenario, behavioural | [by-type.md](by-type.md) |
| Sit a timed interview | [mock-interviews/](mock-interviews/README.md) |
| Write and run code against a check | [exercises/](exercises/README.md) |
| Keep a record of what you have tried | [tracker.csv](tracker.csv) |

## How to practise

- **Answer aloud.** Reading an answer and saying one are different skills, and only the second is tested.
- **Answer first, then open the note.** Each question carries a note on what a strong answer contains. It is
  not a script. If your answer leaves out what the note names, that is the gap: go back to the chapter the
  question points to.
- **Expect follow-ups.** Nearly every question has a natural second question behind it. After each answer,
  ask what it would be, and answer that too.
- **Do not memorize.** An answer delivered verbatim sounds like what it is, and invites the interviewer to
  probe where the recall stops.

Interview formats have moved away from recall and toward judgement: questions with one memorizable answer are
cheap to look up, so they are being replaced by questions about trade-offs, failure modes and what you would
check. A typical loop runs four to six rounds: a coding exercise, a breadth screen on concepts, a design or
case round, a deep dive into your own past work, and a behavioural conversation. The deep dive is the round
candidates underprepare, and it often decides the outcome. It is about your own project, so no question here
can prepare you for it; your portfolio (Appendix B) and the interview prompts in
[reference/ai-assistant-prompts.md](../reference/ai-assistant-prompts.md#interview-preparation) can.

## How the questions are numbered

Every question has a permanent ID. **Q1 to Q185** are the questions written for the book; new questions
continue from **Q186** without gaps. IDs are never reused or renumbered, so a link to `Q34`, a note in your
tracker, or an erratum stays valid as the bank grows. A question's level, type or chapters may be corrected
over time; its ID will not change.

Each question lists the chapters it draws on. The first is where its central idea is taught. Some questions
go beyond the book, usually because interviews use an industry term the book does not teach; those carry a
**Beyond the book** note saying what is and is not covered. A few questions, the seven behavioural ones
(Q179 to Q185) above all, and many of the design and case questions, have no single correct answer. They are
here because they are asked, and their notes say what the interviewer is listening for.

## Keeping track

[tracker.csv](tracker.csv) has one row per question and blank columns for `status`, `last_practised`,
`confidence` and `notes`. It opens in Excel, Numbers or Google Sheets. **Copy it before you fill it in**, for
example to `my-progress.csv`: the file here is regenerated whenever questions are added, and new questions
simply appear as new rows. Rows are keyed by ID, so an old copy stays valid.

## Corrections and new questions

The questions are written once, in [bank/](bank/), and every page in this folder is generated from them.
To correct or suggest a question, see [CONTRIBUTING.md](../CONTRIBUTING.md). Changes to the bank are listed
in [CHANGELOG.md](CHANGELOG.md).

## Licence

The question and answer text in this folder is © 2026 Shanmukh Behara and licensed under
[CC BY-NC-SA 4.0](../LICENSES/CC-BY-NC-SA-4.0.txt): you may share and adapt it for non-commercial purposes,
with credit, under the same licence. It is **not** covered by the MIT licence that applies to the code. The
exercise code (every `starter`, `solution` and `check` file under `exercises/`) is MIT. `tracker.csv` is
dedicated to the public domain under [CC0 1.0](../LICENSES/CC0-1.0.txt), so your filled-in copy is yours. The
full map is in [LICENSING.md](../LICENSING.md).
