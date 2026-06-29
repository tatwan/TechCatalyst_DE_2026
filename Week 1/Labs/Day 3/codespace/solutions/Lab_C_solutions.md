# Lab C: Solution Key (instructor) — GitHub: Remote & Collaboration

Share after the lab. Reward correct reasoning over exact wording.

## Section 1 — Remote sync (Parts 1–4)

### Path choice

- Path A (Codespace created from the repo) is correct for students who followed Lab B; `git remote -v` is pre-populated and `git push` works without a PAT.
- Path B is only for students who started from a blank template. The single most common live issue is the 403 on first push; the fix is the fine-grained PAT plus `git -c credential.helper= push`. Do not let students mix Path A and Path B commands.

### Part 4: fetch versus pull

- `git fetch` downloads the remote commits into the remote-tracking branch (`origin/main`) but does **not** change your working files or your branch. `git status` then reports "your branch is behind origin/main by N commits."
- `git merge origin/main` integrates the already-fetched commits into your current branch and updates your working files. In this lab it is a clean fast-forward (no conflicts).
- `git pull` is exactly those two steps in one: `fetch` + `merge`. The lab splits them on purpose so students see what `pull` is actually doing.
- One-sentence answers to accept: "fetch downloads but does not integrate; merge integrates what was fetched; pull does both." Watch for students who think `git pull` after `git fetch` is doing something new — it just re-fetches (finds nothing) and merges.

### Common issues to watch

- Push rejected with "fetch first" or "behind": the remote has commits the student does not have (often from the web edit). Correct move: `git pull`, then push. Same lesson as the Knowledge Check question on rejected pushes.
- Student edits on GitHub and expects the Codespace to update automatically. Reinforce: nothing syncs without push or pull.
- Clone path confusion: Codespaces sometimes places repos under `/workspaces/...` rather than `~`. Always run `pwd` first.
- 403 reappears mid-lab: repeat `git -c credential.helper= push`. After the first successful authenticated push it is rarely needed again, and Path A students almost never see it.

## Section 2 — Branch, PR, merge (Parts 5–7)

Reference answers to Q1–Q5:

- **Q1:** `git branch` lists local branches with `*` on the current one; after `git switch -c add-about-section`, the `*` is on `add-about-section`.
- **Q2:** A PR proposes merging one branch into another and opens a place to **review and discuss** before the change lands on `main`. A direct push to `main` skips review entirely; a PR lets a teammate read the diff, comment, and approve first.
- **Q3:** Green = added lines, red = removed lines. Reviewing a diff is faster than re-reading the whole file because it shows only what changed, in context — you don't re-verify unchanged code.
- **Q4:** No — before `git pull` the About section was only on the **remote** `main`. Merging the PR on github.com updates GitHub's copy; the Codespace is a separate copy that only catches up when you `pull`. (This is the central local-vs-remote lesson again.)
- **Q5:** Accept any sound data-engineering review concern: correctness of the transformation, data-quality/test coverage, PII handling, cost (bytes scanned, warehouse size), readability/commit hygiene. The point is that review is about more than "does it run."

> [!NOTE]
> **Time-permitting section.** If the cohort only completed Section 1, that's fine — branching, PRs, and merge conflicts get full treatment on **Week 2 Day 1**. Section 2 here is the on-ramp.
