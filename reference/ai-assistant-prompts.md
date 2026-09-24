# Working with an AI assistant: the prompt library

The complete library from Appendix E of *From Absolute Zero*, with the reasoning behind each prompt.
The appendix keeps the principle, the routine and six of these prompts in print; this page holds all of
them, so you can copy one with the button GitHub puts on every code block.

**The line that matters.** An assistant is useful exactly to the degree that you can check its output.
If you understand what a `groupby` does, one that writes it saves you a minute. If you do not, it has
handed you a result you must take on faith, and you have gained a number you cannot defend. Every
prompt below is written to keep you on the side of that line where you remain the person who decides
whether the answer is right.

The prompts name no product. They work in any chat assistant, and they will keep working as the
assistants change. The one thing that does change is how much an assistant can do on its own; the
prompts that say "do not fix it" and "wait for my answer" matter more, not less, as that grows.

Contents: [Teach, don't solve](#prompts-that-teach-rather-than-solve) ·
[Understanding](#prompts-for-understanding-something) · [Debugging](#prompts-for-debugging) ·
[Checking your own work](#prompts-for-checking-your-own-work) · [Practice and recall](#prompts-for-practice-and-recall) ·
[Interview preparation](#interview-preparation) · [Real work](#prompts-for-real-work) ·
[Prompts that will hurt you](#prompts-that-will-hurt-you) · [A rhythm for each chapter](#a-rhythm-for-each-chapter) ·
[A working discipline](#a-working-discipline)

## Prompts that teach rather than solve

| Asks it to solve | Asks it to teach |
|---|---|
| Write the groupby for revenue by country. | Explain groupby on three rows; then I write it. |
| Fix this error. | Say what it means and where to look; do not fix it. |
| Is this result significant? | What must I know about how the data was collected? |
| What model should I use? | What is the simplest baseline, and what must beat it? |

The right-hand column takes longer and is the entire point. Each of those prompts leaves you having
produced the understanding rather than received the answer.

## Prompts for understanding something

For the moment a paragraph does not land. Each one asks the assistant to change the angle rather than
restate the words.

```text
Explain X as if I have never seen it, then again as if I am an analyst, then tell me what the difference between those two explanations reveals.
```
The third part is the useful one. It surfaces the assumptions the simple version quietly dropped, which
is usually where your confusion actually sits.

```text
Give me the same worked example with different numbers, and change one thing so the answer reverses.
```
Seeing a result flip teaches you which input the conclusion depends on. This is the fastest way to find
the load-bearing assumption in any method.

```text
What is the most common wrong mental model people have about X, and why is it wrong?
```
You often hold the common wrong model without knowing it. Naming it directly is quicker than
discovering it three chapters later.

```text
Where does X break down? Give me a case where applying it would produce a confident wrong answer.
```
Every method has a domain. Knowing the edge is what separates using a tool from operating it.

```text
I think X means the following: [your understanding]. Tell me where I am wrong, and be specific rather than encouraging.
```
State your understanding first and ask for correction. Assistants agree too readily when you ask an
open question, so give them something to disagree with. *(Printed in Appendix E.)*

## Prompts for debugging

The instinct when code breaks is to ask for a fix. Resist it once, because the error message is the
lesson and the fix is only the outcome.

```text
Here is my error and my code. Do not fix it. Explain what the error is telling me and which line to look at.
```
You keep the diagnosis, which is the transferable part. Ask for the fix afterwards if you still need it.
*(Printed in Appendix E.)*

```text
My code runs but the answer looks wrong. Here is what I expected and what I got. What are three things that could cause that gap?
```
Silent wrongness is far more dangerous than a crash, and this is the prompt for it. Three candidate
causes give you something to test rather than a guess to accept.

```text
Walk through this code line by line and tell me the shape and type of every variable after each step.
```
Most pandas and NumPy bugs are shape or type bugs. Making the intermediate states explicit finds them
faster than reading the logic.

```text
What would this code do wrong if my data had missing values, duplicates, or an unexpected type?
```
Code that works on the sample and fails on the full file usually fails on exactly one of those three.

```text
Rewrite this so it fails loudly instead of silently when an assumption is violated.
```
Turns a quiet corruption into an error you will notice. This is the habit behind `validate="m:1"` and
the row-count check.

## Prompts for checking your own work

Use these before you send anything. They are adversarial on purpose, because the questions you are
not asking are the ones a reviewer will.

```text
Play a sceptical executive. Here is my conclusion and the evidence. Attack it. Give me the three strongest objections, not a general critique.
```
The single most valuable prompt in this library. *(Printed in Appendix E.)*

```text
What is the most likely way this analysis is wrong, given how it was built?
```
Different from asking whether it is right. It presumes an error exists and makes the assistant look
for it.

```text
What would someone who disagreed with this conclusion say, and what would they ask to see?
```
Tells you which follow-up analysis to run before the meeting rather than during it.

```text
I claim this number means X. What else could it mean?
```
Alternative explanations are the whole of diagnostic work, and they are much easier to generate than
to remember.

```text
Read my write-up and tell me which sentences overclaim relative to the evidence.
```
Catches the drift from "associated with" to "caused by", which is the most common credibility failure
in analytical writing.

```text
What have I not measured that would change this conclusion if it were large?
```
The unmeasured-confounder question, asked systematically. Chapter 15 explains why it usually has no
answer without an experiment.

## Prompts for practice and recall

Reading feels like learning and is not. These convert passive reading into the retrieval that actually
builds competence.

```text
Quiz me on this chapter, one question at a time. Wait for my answer before giving the next, and tell me what I missed rather than the whole answer.
```
One at a time matters. A list of ten questions becomes a list you read; one at a time forces you to
produce an answer. *(Printed in Appendix E.)*

```text
Give me five practice problems on X at increasing difficulty, without solutions. I will ask for those after I have attempted them.
```
Withholding the solution is the whole point. Ask for the answers only after you have written something
down.

```text
Give me a dataset description and a business question, and let me tell you how I would approach it. Then critique my plan.
```
Rehearses the framing skill from Chapter 1, which is the part interviews probe and courses rarely drill.

```text
Show me code with a subtle bug in it and let me find it. Do not tell me where it is.
```
Reading broken code is a distinct skill from writing working code, and it is most of what debugging
actually is.

```text
Ask me the question from this chapter that I am most likely to answer badly.
```
Targets the weak spot instead of the comfortable material, which is where review time is worth
spending.

## Interview preparation

Pair these with the [question bank](../practice/README.md). The point is rehearsal out loud, because
fluency is a separate skill from knowledge and only the spoken version is graded. The bank cannot
prepare you for the deep dive into your own work; the second prompt here can.

```text
Act as an interviewer for an analyst role. Ask me one question, wait for my answer, then push back on the weakest part of it.
```
The follow-up is where real interviews are decided. Practising the first answer alone prepares you for
a quarter of the conversation. *(Printed in Appendix E.)*

```text
Here is a project I worked on: [describe it]. Ask me the five hardest questions an interviewer could ask about it.
```
Prepares the deep dive, which is where experienced candidates are actually separated.
*(Printed in Appendix E.)*

```text
I answered the following question like this: [question, then your answer]. Rate that answer, then show me what a stronger version would have included.
```
Comparative feedback beats a score. Ask specifically what was missing rather than whether it was good.

```text
Give me a SQL question at the level of a mid-level analyst screen, and do not show the solution until I have written mine.
```
Write the query before seeing an answer. Reading a solution creates recognition, not the ability to
produce one. The [SQL exercises](../practice/exercises/README.md) do the same with a check instead of
an assistant.

```text
Ask me a case question about a business I have never worked in, then evaluate how I structured the answer rather than whether I got it right.
```
Case rounds grade structure. Being explicit about that in the prompt gets you feedback on the thing
being assessed.

## Prompts for real work

Once you are analysing something that matters, the assistant is most useful before you start and after
you finish, and least useful in the middle.

```text
Here is a vague request from a stakeholder: [paste it]. Ask me the questions I should be asking them before I start.
```
Chapter 1's framing discipline, prompted. Far cheaper than discovering the real question after a week
of work. *(Printed in Appendix E.)*

```text
I am about to analyse this dataset: [describe it]. What should I check before trusting any of it?
```
Produces the pre-flight list, and will usually remind you of the grain question you were about to skip.

```text
Explain this finding three ways: for an executive, for the team that owns the process, and for a technical reviewer.
```
The audience-adaptation work from Chapter 42, done fast. Write the technical version yourself and use
this to derive the others.

```text
Turn this analysis into a one-page recommendation with a finding, an impact, a risk, and a next step.
```
Gives you a structure to react to. Never send the output unedited; the judgment about what matters is
yours.

```text
What is the simplest thing that would answer this question, and why might it be enough?
```
Guards against the reflex to model. Often the answer is a groupby, which Chapter 42 shows can be worth
close to four times the model.

## Prompts that will hurt you

The prompts above work because they leave the judgment with you. These fail for the same reason in
reverse: each one hands over the part of the work that was the point.

| Prompt | Why it hurts |
|---|---|
| *Write the analysis for me.* | You get something plausible and you learn nothing, which is a bad trade on a task you will have to defend. The failure is not that the output is wrong; it is that you cannot tell whether it is wrong. |
| *Is this result significant?* | Chapter 8 is an argument against exactly this question. An assistant cannot know your design, your sampling, or how many things you already tested, and it will answer anyway. |
| *What model should I use for this dataset?* | Asked before you have looked at the data, this skips Chapters 1 and 11, the framing and the cleaning, which is where most of the value and nearly all of the mistakes live. Ask it after you can describe the grain, the target, and the baseline. |
| *Explain why my model is fair.* | A question phrased for a conclusion rather than an answer. Chapter 44 shows fairness has several definitions that cannot all hold at once, so a question asking for reassurance will get reassurance. Ask which definition it satisfies and what that costs under the others. |
| *Just give me the code.* | The code is the cheapest part. Debugging code you do not understand costs more than writing it would have, and it is the reason Chapter 30 builds a network by hand before any framework appears in the book. |

The pattern is consistent enough to be worth stating once: an assistant is useful when it is arguing
with you, and unreliable when it is agreeing with you. If a prompt is phrased so that only one answer is
acceptable, you will get that answer, and it will tell you nothing about whether it is true.

## A rhythm for each chapter

Read the chapter first, without asking anything. Then work the practice problems, and only then open
an assistant. At that point three prompts cover most of the value: ask to be quizzed on the chapter and
answer out loud; ask for five more practice problems of the same kind; and ask what you would still get
wrong. Checking its solutions against the reasoning in the chapter is part of the exercise rather than
a formality, because it will occasionally be wrong and noticing that is the skill.

## Where assistants fail, and the habits that cover it

- **Plausible statistics, delivered with confidence.** A wrong mean, a misremembered formula, an invented
  threshold, all in the same tone as a correct one. Recompute any number that matters.
- **Functions that do not exist, and arguments that were removed two versions ago.** If a call looks
  unfamiliar, check the library's official documentation for the version pinned in `requirements.txt`.
- **Agreeing with you.** Ask whether your conclusion is sound and it will often find reasons it is. Ask
  it to argue the opposite case and you get something far more useful.

These are habits, not claims about any particular assistant; they stay worth keeping as the tools improve.

## A working discipline

- [ ] Read the chapter and form your own view before asking anything
- [ ] Ask for a different explanation rather than the answer
- [ ] Recompute any number that will appear in something you send
- [ ] Check unfamiliar function calls against the official documentation
- [ ] Ask it to argue against your conclusion, not for it
- [ ] Never paste in data you would not email to a stranger
- [ ] If you cannot explain the code you were given, you are not finished

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../LICENSING.md). Corrections: [docs/ERRATA.md](../docs/ERRATA.md).</sub>
