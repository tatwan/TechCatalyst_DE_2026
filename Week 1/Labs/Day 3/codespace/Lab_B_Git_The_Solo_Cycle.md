# Lab B: Git — The Solo Cycle

**Module:** Developer foundations (Git deep dive, Day 3) · **Format:** Pairs (navigator and driver, swap every 20 minutes) · ⏱️ about 45 minutes

> [!WARNING]
> **AI-Free Zone (Weeks 1 to 4).** Type every command yourself. No Copilot, no LLM-generated code, SQL, or Git commands. Read the error messages; debug yourself first. Docs and your peers are fair game. Building this muscle memory now is what lets you trust (and challenge) AI suggestions in Week 6.

---

## 🎯 Goal

By the end of this lab you can:

- create your course repository and launch a Codespace, and manage its free-tier budget (stop and restart);
- set up your project environment with **venv + pip** (the course baseline you compared in Lab A) and record it in `requirements.txt`;
- read a small dataset with pandas from a script you wrote by hand;
- run the solo Git cycle (`status`, `add`, `diff`, `commit`, `log`) and explain each step;
- use a `.gitignore` so your environment and secrets never get committed.

## 🧠 Why this matters

This repo is your home for the next seven weeks. Every pipeline, query, and notebook starts here. Today you build it by hand and verify it works, so a broken setup never blocks your learning later. The Git cycle you practice here is the single most-repeated workflow in data engineering; you will run these commands thousands of times.

## 🗺️ What to expect

This lab is **entirely local to your Codespace** (no pushing to GitHub yet; that is Lab C). You will create a tiny "claims journal" project, wire up a Python environment, read a provided sample of Hartford-style claims data, and make at least three commits, running `git status` and `git diff` constantly so the mental model sticks.

> In Lab A you tried conda, venv + pip, and uv. From here on the program uses the **venv + pip** baseline. You'll set one up below — it should feel familiar now.

---

## Part 1: GitHub repo and Codespace (15 min)

### Step 1: Create your course repository

1. Sign in to your **personal** GitHub account (use a personal account for the course, matching program practice).
2. Create a repository named `techcatalyst-2026-<yourname>` (public or private, your choice), and check **Add a README file**.
3. In the README, add your name, cohort (TechCatalyst DE 2026), and a one-line bio.

### Step 2: Launch a Codespace from your repo

1. On your repo page, click the green **Code** button, then the **Codespaces** tab, then **Create codespace on main**.
2. Wait about 30 seconds for VS Code to load in your browser.

> 💡 Creating the Codespace **from your repo** (not from a blank template) gives it the correct permissions for Lab C's push later. This is the recommended path.

### Step 3: Verify the machine and record it

In the terminal (Ctrl+backtick), run and record the output:

```bash
python --version
pip --version
git --version
uname -a
```

✅ **Checkpoint:** `python --version` shows 3.11 or higher.

### Step 4: Practice the budget habit (do not skip)

1. Find where to **stop** your Codespace: the menu (☰), or github.com/codespaces.
2. Stop it, then restart it once. Confirm your files are still there.

> 💡 **Budget reality:** personal accounts get 120 core-hours and 15 GB of storage per month free. A 2-core Codespace burns the 120 hours in about 60 hours of active time. **Stop a Codespace when you step away.** Stopping keeps your state (and uses storage); deleting frees storage but loses uncommitted work, so push first. Check usage on the GitHub billing and plans page.

---

## Part 2: Python environment — the venv + pip baseline (15 min)

You compared the options in Lab A. The program standard is **venv + pip + `requirements.txt`**. Set yours up here.

### Step 5: Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # prompt now shows (.venv)
pip list                          # nearly empty: this environment is isolated
```

✅ **Checkpoint:** your prompt shows `(.venv)`. Make checking it a reflex.

> 💡 We name it `.venv` (with the leading dot) so it sits quietly in the project and is easy to git-ignore. Same `source .../activate` and `deactivate` you practiced in Lab A.

### Step 6: Install and record dependencies

```bash
pip install pandas requests
python -c "import pandas; print(pandas.__version__)"
pip freeze > requirements.txt
cat requirements.txt
```

> 💡 `requirements.txt` is the **record** that makes your environment reproducible by anyone, anywhere. We commit it; we never commit the `.venv/` folder itself.

---

## Part 3: Read real data with a script you wrote (15 min)

### Step 7: Add the sample dataset

A small sample of Hartford-style claims data is provided at `data/hartford_claims_sample.csv` in this lab folder (12 rows: `claim_id, state, claim_type, reported_date, amount_usd, status`). Copy it into your repo:

- In the Codespaces file explorer, create a `data/` folder and upload `hartford_claims_sample.csv` into it, or
- paste the contents into a new file at `data/hartford_claims_sample.csv`.

### Step 8: Write hello_data.py by hand

Create `hello_data.py` and type it out yourself rather than copy-pasting. Typing each line makes you think about what you're actually putting in the file; pasting a whole blob is overwhelming and easy to skim past without understanding it.

```python
import pandas as pd
import requests

# 1) confirm the environment is alive
print(f"pandas {pd.__version__} ready")

# 2) read the sample claims data
df = pd.read_csv("data/hartford_claims_sample.csv")
print(f"rows: {len(df)}  columns: {list(df.columns)}")

# 3) one quick aggregation: total claim amount by state
by_state = df.groupby("state")["amount_usd"].sum().sort_values(ascending=False)
print("Total claim amount by state:")
print(by_state)

# 4) confirm outbound network works (you will need APIs in Week 2)
r = requests.get("https://api.github.com")
print(f"GitHub API says: {r.status_code}")
```

### Step 9: Run it

```bash
python hello_data.py
```

✅ **Checkpoint:** you see the pandas version, the row and column summary, a per-state total, and a `200` status code.

---

## Part 4: The Git cycle, by hand (15 min)

### Step 10: Configure your identity (once)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Step 11: Ignore what should never be committed

Create `.gitignore` containing:

```gitignore
.venv/
__pycache__/
.env
*.log
```

### Step 12: Run the loop and watch every state change

```bash
git status                       # see what is untracked
git add .gitignore
git status                       # .gitignore is now staged (green)
git commit -m "Add gitignore for venv, cache, and secrets"

git add requirements.txt data/ hello_data.py
git status
git diff --staged                # review exactly what you are about to commit
git commit -m "Add environment, sample data, and hello_data script"

git log --oneline                # your history so far
```

> 💡 Run `git status` between every step until it is automatic. Red means working directory; green means staging area; nothing is saved until you commit.

### Step 13: Make one more focused commit with a diff

```bash
echo "" >> README.md
echo "## Day 3 setup complete" >> README.md
git diff                          # your unstaged change
git add README.md
git diff                          # empty now: working dir matches staging
git diff --staged                 # there is your change
git commit -m "Note day 3 setup in README"
git log --oneline                 # at least 3 commits
```

✅ **Checkpoint:** `git log --oneline` shows **at least 3 commits**, and `.venv/` does **not** appear in `git status`.

---

## Part 5: Verification checklist (add this to your README and commit it)

- [ ] Codespace starts and stops; I know where the stop button is
- [ ] `python --version` is 3.11 or higher inside the Codespace
- [ ] `(.venv)` shows in my prompt when activated
- [ ] `requirements.txt` exists and lists pandas and requests
- [ ] `.venv/` is git-ignored (does not appear in `git status`)
- [ ] `hello_data.py` runs and prints the per-state totals and a `200`
- [ ] At least 3 commits visible in `git log --oneline`
- [ ] My partner has verified all of the above on my machine

**Deliverable for Lab B:** a local repo (in your Codespace) with `hello_data.py`, `data/hartford_claims_sample.csv`, `requirements.txt`, `.gitignore`, and the completed checklist in `README.md`, with at least three commits. You will publish it to GitHub in Lab C.

> [!IMPORTANT]
> **Day 4 heads-up.** Tomorrow's Cloud Storage labs run in **Google Cloud Shell** (in the GCP console), where `gcloud` is already installed and authenticated to your course project — so there's nothing to install in this Codespace for Day 4. Keep this repo; you'll return to the Codespace for Python/Git work later in the program.

---

## 🏆 Challenge: on your own (about 8 min)

1. Add a function to `hello_data.py` that prints the count of `open` versus `closed` claims, then commit it with a clear message after reviewing the staged diff.
2. Create a throwaway `secret.env` file containing a fake key. Confirm `.gitignore` keeps it out of `git status`. Now reason: if you had committed it last week and added it to `.gitignore` today, would it be safe? (Answer in the solution key.)
3. **Bonus:** show the full 40-character hash of your first commit.

---

## 🧾 What you learned

| Command | What it does |
| :--- | :--- |
| `python -m venv .venv` | Create an isolated environment |
| `source .venv/bin/activate` | Activate it (prompt shows `(.venv)`) |
| `pip install` / `pip freeze > requirements.txt` | Install packages / record them |
| `git status` | Show the state of all areas (run it constantly) |
| `git add` / `git commit -m` | Stage changes / save a snapshot |
| `git diff` / `git diff --staged` | Review unstaged / staged changes |
| `git log --oneline` | Read your history |

**Key mental model:** isolate the environment, record what is installed, and move every change deliberately through working directory, staging area, and repository.

---

## ➡️ Next: Lab C — local meets remote (GitHub)

When both partners finish, move on to `Lab_C_GitHub_Remote_and_Collaboration.md`. You'll publish this repo to GitHub and learn push, pull, clone, fetch — then branch and pull requests, the team workflow.
