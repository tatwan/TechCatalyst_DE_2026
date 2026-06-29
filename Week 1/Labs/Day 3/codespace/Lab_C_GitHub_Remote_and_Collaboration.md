# Lab C: GitHub — Remote & Collaboration

**Module:** Developer foundations (Git deep dive, Day 3) · **Format:** Pairs · ⏱️ about 60–90 minutes

> [!WARNING]
> **AI-Free Zone (Weeks 1 to 4).** Type every command yourself. No Copilot, no LLM-generated code, SQL, or Git commands. The point is to understand the local-and-remote model before any tool touches it.

---

## 🎯 Goal

By the end of this lab you can:

- connect your local repo to GitHub and push commits (`git push`);
- pull a change made on GitHub down to your machine (`git pull`);
- clone an existing repository (`git clone`) and explain `fetch` vs `pull`;
- create a branch, open a pull request (PR), review its diff, and merge it;
- explain why local and remote are separate copies, and why teams work on branches and PRs instead of pushing straight to `main`.

## 🧠 Why this matters

In Lab B your work lived in one Codespace, one spilled coffee (or one deleted Codespace) away from oblivion. **Parts 1–4** push it to GitHub and teach the solo sync loop (push, pull, clone, fetch). **Parts 5–7** step up to the **team** loop — branch → PR → review → merge — which is how real data engineering teams ship. You practice it on your *own* repo so the mechanics are familiar before **Week 2 Day 1**, where you do it on a shared repo and handle merge conflicts for real.

## 🗺️ What to expect

You'll publish the `techcatalyst-2026-<yourname>` repo you built in Lab B, simulate a teammate's change, pull it down, clone a fresh copy, then practice the branch-and-pull-request workflow.

> [!NOTE]
> **Short on time?** Parts 1–4 (remote sync) are the must-do core. **Stop after Part 4 if needed** — Parts 5–7 (branch / PR / merge) are the on-ramp to Week 2 Day 1, where branching and merge conflicts are covered in full. Do them today if you have time; they're worth it.

> [!IMPORTANT]
> **The first-push gotcha.** If you created your Codespace from a **blank template**, your first `git push` may fail with a 403 "Permission denied" because the token is scoped to the template, not your repo. Part 1 gives you two clear paths. If you followed Lab B and created your Codespace **from your repo**, you are on Path A and pushing usually just works.

---

# Section 1 · Local meets remote (Parts 1–4)

## Part 1: Publish your repo (choose one path, do not mix)

### Path A (recommended): Codespace created from your repo

You created your Codespace from your repo in Lab B, so the remote is already wired and the token is correct.

```bash
pwd                  # confirm you are in your repo folder
git remote -v        # origin should already point to your repo
git status
git push             # or: git push -u origin main  (first push of the branch)
```

If `git remote -v` is empty (you started from a blank template instead), switch to Path B.

✅ **Checkpoint (Path A):** your commits appear on github.com after a refresh.

### Path B: Stay in a blank Codespace (PAT plus credential bypass)

Use this only if Path A's `git remote -v` was empty.

1. Create a **fine-grained Personal Access Token**: GitHub, then your profile, then **Settings**, then **Developer settings**, then **Personal access tokens**, then **Fine-grained tokens**, then **Generate new token**. Resource owner: you. Repository access: **Only select repositories**, your repo. Permissions: **Contents** set to **Read and write**. Generate and copy it immediately.
2. Point your local repo at the remote using the token, then push once with the bypass:

```bash
git remote remove origin 2>/dev/null || true
git remote add origin https://YOUR-USERNAME:YOUR_PAT@github.com/YOUR-USERNAME/techcatalyst-2026-yourname.git
git remote -v
git -c credential.helper= push -u origin main
```

The `-c credential.helper=` tells Git to ignore the scoped Codespaces helper for this one command, so it uses the token in the URL.

✅ **Checkpoint (Path B):** your commits appear on github.com, and you worked around the blank-template token.

> From here on, plain `git push` and `git pull` should work. If a push ever fails again with 403, repeat the bypass: `git -c credential.helper= push`.

---

## Part 2: Pull a teammate's change (10 min)

Your repo now exists in two places, and they can drift apart. Let's make that happen on purpose.

### Step 1: Edit on GitHub (you are playing the teammate)

1. On your repo page, open `README.md`, click the pencil (✏️ Edit this file).
2. Add a line at the bottom: `Remote edit: changed directly on GitHub.`
3. Click **Commit changes**, keep the default message, commit to `main`.

GitHub just made a commit your Codespace knows nothing about.

### Step 2: Prove your local copy is behind

```bash
git log --oneline     # the web edit is NOT here
cat README.md         # the new line is missing
```

### Step 3: Pull

```bash
git pull
git log --oneline     # there it is
cat README.md         # the new line is present
```

> 💡 `git pull` = fetch the remote commits + merge them into your branch. **Habit: pull before you start working, every time.** It prevents most conflicts before they happen.

✅ **Checkpoint:** the web-edit commit appears in your local `git log`.

---

## Part 3: Clone (10 min)

`clone` is how you get a repo you do not already have; your first day on any team starts with it.

```bash
cd ~
git clone https://github.com/YOUR-USERNAME/techcatalyst-2026-yourname.git journal-clone
cd journal-clone
git log --oneline     # identical history
git remote -v         # origin already configured, no remote add needed
```

Notice what `clone` did automatically: downloaded the **entire history** (not just the latest files), set up `origin`, and checked out `main`. That is why cloning is one command while init-and-connect was three: clone is init plus remote add plus pull, bundled.

✅ **Checkpoint:** `journal-clone` has identical history to your repo.

---

## Part 4: fetch versus pull (5 min)

```bash
# in journal-clone, make and push a change
echo "from the clone" > clone-note.md
git add clone-note.md && git commit -m "Add clone note"
git push

# switch to your original repo folder and look WITHOUT integrating
cd ~/techcatalyst-2026-yourname    # or your Lab B path
git fetch                          # download origin/main; your files are untouched
git status                         # "behind origin/main by 1 commit"
git log --oneline origin/main      # you can SEE the new commit before integrating
git merge origin/main              # integrate the commits you already fetched
```

> 💡 `git fetch` downloads remote commits **without** touching your files; `git status` then tells you that you are behind. `git merge origin/main` integrates the commits you already fetched. Running them back-to-back is exactly what `git pull` does in one step: **`pull = fetch + merge`**. Splitting them lets you look before you leap. (This is a clean fast-forward merge — no conflicts; conflict resolution is Week 2.)

✅ **Checkpoint:** you can explain, in one sentence each, what `fetch`, `merge`, and `pull` do, and why `pull` equals `fetch` plus `merge`.

> [!NOTE]
> **This is the must-do core.** If you're short on time, stop here — you've mastered the solo sync loop. Continue to Section 2 (branch + PR) when you can; it's the on-ramp to Week 2 Day 1.

---

# Section 2 · The team workflow: branch, PR, merge (Parts 5–7)

Labs B and Section 1 taught the **solo** loop: edit, add, commit, push, pull, clone. But real data engineering is a **team sport** — you never push straight to `main` on a shared repo. The everyday collaboration loop is **branch → push → pull request → review → merge**.

## Part 5: Start from a clean, up-to-date main (3 min)

Make sure you are in the right place and your `main` is current before you branch.

```bash
cd ~/techcatalyst-2026-<yourname>   # your ORIGINAL repo (not journal-clone)
pwd                                 # confirm the path is your repo, not journal-clone
git switch main                     # make sure you are on main
git status                          # should say "On branch main", working tree clean
git pull                            # pull anything you merged on github.com earlier
git log --oneline                   # confirm your Lab B/Section 1 history is here
ls                                  # confirm README.md exists
```

✅ **Checkpoint:** you are on `main`, in your original repo folder, the working tree is clean, and `README.md` is present.

> 💡 If `pwd` shows a path ending in `journal-clone`, you are in the wrong copy — `cd ~/techcatalyst-2026-<yourname>` (Codespaces sometimes uses `/workspaces/...`). Run `pwd` first, every time.

---

## Part 6: Branch, commit, and open a PR (15 min)

### Step 1: Create and switch to a branch

```bash
git switch -c add-about-section     # create a new branch AND switch to it
git branch                          # list local branches
```

**Q1:** What does `git branch` show now, and which branch has the `*` next to it?

### Step 2: Make a change on the branch

Open `README.md` in the Codespace editor and add a short section at the bottom (2–3 lines):

```markdown
## About this repo
My TechCatalyst DE 2026 working repo. Built by hand during Week 1 (Codespaces, venv, Git).
```

Save the file.

### Step 3: Commit and push the branch

```bash
git add README.md
git status                          # README.md is staged (green), on branch add-about-section
git commit -m "Add About section to README"
git push -u origin add-about-section   # -u sets the upstream for this new branch
```

**Q2:** The push output prints a URL to open a pull request. In your own words: what is a PR, and what does it let a teammate do that a direct push to `main` does not?

### Step 4: Open the PR on GitHub

1. Open your repo on github.com. You will see a banner: **"add-about-section had recent pushes — Compare & pull request."** Click it (or go to the **Pull requests** tab → **New pull request**).
2. Confirm the PR is merging `add-about-section` **into** `main`.
3. Give it a title (`Add About section to README`) and a one-line description.
4. Click **Create pull request**. **Do not merge yet.**

### Step 5: Read the diff

Open the **Files changed** tab.

**Q3:** What exactly do the green and red lines show? Why is reviewing a diff faster than re-reading the whole file?

---

## Part 7: Merge and sync back down (10 min)

### Step 6: Merge the PR

On the PR page, click **Merge pull request** → **Confirm merge** (**Squash and merge** is fine). The branch is now merged into `main` **on GitHub**.

### Step 7: Prove your local main is behind, then catch up

```bash
git switch main
git log --oneline                   # the About commit is NOT here yet
git pull                            # bring the merge down from GitHub
git log --oneline                   # now it is here
cat README.md                       # the About section is present locally
```

**Q4:** Before `git pull`, was the About section in your local `main`? Why did merging on github.com not update your Codespace automatically?

### Step 8: Clean up the merged branch

```bash
git branch -d add-about-section     # delete the local branch; its work is now on main
git branch                          # only main remains locally
```

> 💡 `git branch -d` only deletes a branch whose work is already merged into the branch you are standing on — a safety net. That is why you switched to `main` and pulled first.

✅ **Checkpoint:** the About section is on `main` both on GitHub and in your Codespace, and the feature branch is deleted locally.

### Step 9 (optional, needs a partner): Review a teammate's PR

1. Swap repo URLs with your partner.
2. On their PR, open **Files changed** → **Review changes**.
3. Leave **one** comment and submit the review as **Comment** (not Approve — you are practicing the mechanics, not gatekeeping).

**Q5:** As a reviewer, what is one thing you would check before approving a real teammate's data-pipeline change? (Think back to Day 1 and Day 2: data quality? PII? cost?)

---

## Success criteria

- [ ] Repo published to github.com (Path A or Path B)
- [ ] Pulled a web-made edit down to your Codespace
- [ ] Cloned a second copy that matches
- [ ] Can explain fetch, merge, and pull (and why `pull = fetch + merge`), and local vs remote
- [ ] *(Section 2)* Created a branch, pushed it, opened and merged a PR, pulled it back, deleted the branch
- [ ] *(Section 2)* Q1–Q5 noted in your repo or your notes
- [ ] Partner verified all of the above

**Deliverable:** your `techcatalyst-2026-<yourname>` repo published to GitHub, a clone verified to match, and (if you did Section 2) the About section merged into `main` via a pull request with the branch deleted and Q1–Q5 answered.

---

## Hints

<details>
<summary>Hint 1: `git switch -c` says "not a git command" or unknown</summary>

You are on an older Git. Use `git checkout -b add-about-section` (same effect). `git --version` should be 2.23 or higher for `switch`; Codespaces is current, so this usually means a typo.
</details>

<details>
<summary>Hint 2: push rejected or "no upstream branch"</summary>

The first push of a new branch needs `-u origin <branch>` to set the upstream. After that, plain `git push` works for that branch.
</details>

<details>
<summary>Hint 3: "Cannot delete branch, not fully merged"</summary>

Make sure the PR actually merged on github.com **and** you ran `git switch main && git pull` first. `git branch -d` only deletes branches whose work is already on the branch you are standing on.
</details>

<details>
<summary>Hint 4: `pwd` shows a path ending in journal-clone</summary>

You are in the Lab C clone, not your original repo. `cd ~/techcatalyst-2026-<yourname>` (Codespaces sometimes uses `/workspaces/...`). Always `pwd` before you branch.
</details>

---

## 🧾 What you learned

| Command | What it does |
| :--- | :--- |
| `git remote add origin <url>` / `git remote -v` | Connect a local repo to a remote / list remotes |
| `git push -u origin main` / `git push` | First push (sets tracking) / push after tracking |
| `git pull` | Receive commits (`fetch` + `merge`) |
| `git clone <url>` | Copy an entire remote repo, history and all |
| `git fetch` / `git merge origin/main` | Download without touching files / integrate fetched commits |
| `git switch -c <branch>` / `git branch` | Create + switch to a branch / list branches |
| `git push -u origin <branch>` | Push a new branch and set its upstream |
| `git branch -d <branch>` | Delete a local branch whose work is merged |

**Key mental model:** local and remote are separate repos that only sync when you say so. `push` sends, `fetch` looks, `merge` integrates, `pull` = `fetch` + `merge`. Teams protect `main` and integrate through branches and pull requests, so every change is reviewed before it lands.

> [!NOTE]
> **Coming in Week 2 Day 1:** branching on a *shared* repo, and what happens when two people edit the same lines — **merge conflicts** and how to resolve them. Today's PR was a clean merge; that will not always be the case.

---

## ➡️ Next: Lab D — your GitHub profile page

Close the day with `Lab_D_Profile_Page.md` (the Fun Lab): turn everything you learned into your own GitHub profile / personal branding page.
