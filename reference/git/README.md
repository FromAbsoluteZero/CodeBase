# Git, beyond the six commands

Appendix A of the book teaches the six commands that cover an analyst's daily work, the `.gitignore`
that keeps data and credentials out, and the rule that matters most: a committed secret stays in the
history. This page covers what the appendix promises but has no room for: getting something back,
working on the same file as somebody else, the first push, and what to do when it goes wrong.

The copyable `.gitignore` is [`../templates/analytics.gitignore`](../templates/analytics.gitignore).

## Getting something back

| You want to… | Command | Notes |
|---|---|---|
| See what happened | `git log --oneline` | one line per commit, newest first; `--since="3 weeks ago"` narrows it |
| See what changed | `git diff` | uncommitted edits; `git diff --staged` for what is staged; `git diff HEAD~3` against three commits ago |
| Undo uncommitted edits to a file | `git restore <file>` | the file goes back to the last commit; the edits are gone |
| Unstage a file you added by mistake | `git restore --staged <file>` | the edits stay; the file is just no longer in the next commit |
| Get a file as it was three weeks ago | `git log --oneline -- <file>` then `git restore --source <commit> <file>` | copies that version into your working folder; commit it if you want to keep it |
| Undo a whole commit, safely | `git revert <commit>` | makes a new commit that reverses the old one; history stays intact, which is what you want on anything already pushed |
| See who changed a line, and when | `git blame <file>` | useful for "why is this here" |

The recovery promise in the appendix, "something you deleted three weeks ago", is the third row.
Nothing committed is ever really lost until you try hard to lose it.

## Working on a file somebody else is also editing

1. `git pull` **before** you start editing, so you edit the current version.
2. Commit in small pieces and push often, so the two of you diverge as little as possible.
3. When `git pull` reports a **conflict**, Git has written both versions into the file between markers:

   ```text
   <<<<<<< HEAD
   your version of the lines
   =======
   their version of the lines
   >>>>>>> origin/main
   ```

   Open the file, keep the lines you want, delete the three marker lines, then `git add <file>` and
   `git commit`. That is the whole procedure. If it goes badly, `git merge --abort` puts things back to
   before the pull.
4. Two people editing the same **notebook** conflict constantly, because the outputs change on every
   run. Clear outputs before committing (`Kernel → Restart & Clear Output`), or keep the code in `.py`
   files and the notebook for exploration only.

## The first push

`git push` needs somewhere to push to and a way to prove who you are. Both depend on the hosting
service, so this is the part that dates; follow the service's current instructions. The shape is:

1. Create an empty repository on the service (no README, no licence; you have those locally).
2. `git remote add origin <the URL it shows you>`
3. `git push -u origin main` (the `-u` remembers the remote, so plain `git push` works after).
4. The first push asks you to sign in. Services no longer accept your account password on the command
   line; they give you a token or a credential helper. Set that up once.

If your local branch is called `master` and the service expects `main`, `git branch -M main` renames it.

## When to learn branches

Not yet, for most analysts. The moment to learn them is the first time you want to try something you
might throw away without losing the version that works:

```bash
git switch -c try-new-model     # make a branch and move to it
# ...edit, commit...
git switch main                 # back to the version that works, untouched
git merge try-new-model         # bring the branch in, if it turned out well
```

## Undoing the mistake that matters

If you committed a credential:

1. **Rotate it now.** Change the password or revoke the key at the service that issued it. This is the
   only real fix; everything below is housekeeping.
2. Remove it from the file and commit.
3. If the repository is public, assume the secret was seen the moment it was pushed. Rewriting history
   to remove it is possible but does not undo that.

If you committed a large data file by mistake and have **not** pushed yet, `git rm --cached <file>`
removes it from the commit while leaving it on disk; add it to `.gitignore`, then `git commit --amend`.

## Do you need Git to use this repository?

No. The green **Code** button on the repository's front page offers **Download ZIP**. Git is only needed
to receive updates without downloading again, and to keep your own projects safe, which is what
Appendix A is for.

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). The `.gitignore` template beside this page is CC0.</sub>
