# Lab A: Python Environments & Package Management

**Module:** Developer foundations (Day 3) · **Format:** Pairs (navigator and driver, swap every 20 minutes) · ⏱️ about 50–60 minutes

> [!WARNING]
> **AI-Free Zone (Weeks 1 to 4).** Type every command yourself. No Copilot, no LLM-generated commands. The whole point of today is that you *feel* the difference between these tools with your own hands. Read the output of every command before you run the next one.

---

## 🎯 Goal

By the end of this lab you can:

- explain the **two separate jobs** every Python tool is doing: *isolating an environment* and *managing packages*;
- create, activate, use, deactivate, and **delete** an environment with **conda**, **venv + pip**, and **uv**;
- read a `pyproject.toml` and a lock file, and explain what `uv add` and `uv sync` each do;
- say, in one sentence each, when you would reach for conda, for venv + pip, and for uv.

## 🧠 Why this matters

Yesterday this confused the room, and that is normal — there are three tools that *look* like they do the same thing. They do not. The fastest way to stop being confused is to run all three back-to-back on the **same tiny task** (make an environment, install `pandas`, throw it away) and watch how each one behaves. You will see conda's careful-but-heavy solver, venv's "it's just a folder" simplicity, and why **uv** is the one the modern Python world is moving to.

> [!NOTE]
> **This lab is a sandbox, not your course repo.** Everything here happens in a throwaway folder (`~/env-lab`). You will delete all of it at the end. Your real course repo (built in Lab B) uses **venv + pip** — the program baseline. Today is about *understanding the choices*, not changing the baseline.

## 🗺️ What to expect

Three rounds, same task each time, so the differences jump out:

| Round | Tool | What you'll feel |
| :--- | :--- | :--- |
| 1 | **conda** | Environments + packages + non-Python binaries. Careful solver, heavier. (Already installed in Codespaces.) |
| 2 | **venv + pip** | The standard-library baseline. An environment is *literally a folder*. `pip freeze` is how you record it. |
| 3 | **uv** ⭐ | One fast tool: project init, a `pyproject.toml`, a lock file, `add` and `sync`. **This is the focus.** |

First, set up the sandbox:

```bash
mkdir -p ~/env-lab && cd ~/env-lab
pwd                 # confirm you are in ~/env-lab, NOT your course repo
```

---

## Part 0: The two jobs (read this — 3 min)

Every tool below is doing one or both of these two jobs. Keep this table in your head all lab:

| Job | What it means | Why you care |
| :--- | :--- | :--- |
| **Isolate the environment** | Give *this* project its own Python and its own packages, walled off from every other project and from the system Python | So project A's `pandas 1.x` never breaks project B's `pandas 2.x` |
| **Manage packages** | Install, upgrade, remove, and **record** what's installed so someone else can rebuild it exactly | So "works on my machine" becomes "works on everyone's machine" |

`venv` does the *first* job only. `pip` does the *second* job only. `conda` and `uv` each do **both**. That single fact explains most of the confusion. ✅ Say it back to your partner before moving on.

---

## Part 1: conda — careful, complete, heavy (about 12 min)

conda manages **environments and packages together**, and it can install non-Python things (C libraries, system binaries, R, etc.) that pip cannot. That power is why it is popular in data science — and why it is heavier and its installs feel slower. To your surprise, **conda is already installed in Codespaces**, so there is nothing to download.

### Step 1: Turn conda on for your shell (one-time, Codespaces quirk)

In a fresh Codespace the `conda activate` command does not work until you initialize your shell. Do this once:

```bash
conda --version          # prove conda is already here
conda init bash          # wires conda into your shell startup
```

Now **close the terminal and open a new one** (the trash-can icon, then Ctrl+backtick), or run `source ~/.bashrc`. Your prompt should now start with `(base)` — that is conda's default environment.

```bash
cd ~/env-lab             # come back to the sandbox in the new terminal
```

> 💡 `(base)` means conda's *base* environment is active. We never install project packages into `base`; we make a dedicated environment, which is the next step.

### Step 2: Create an environment and activate it

```bash
conda create -n claims-conda python=3.11 -y    # watch it collect and link packages
conda activate claims-conda                     # prompt changes to (claims-conda)
python --version
```

✅ **Checkpoint:** your prompt shows `(claims-conda)`, not `(base)`.

### Step 3: Install a package and look at the env

```bash
conda install pandas -y        # watch the "Solving environment:" step — that's the careful part
conda list | wc -l             # how many packages did one install pull in?
python -c "import pandas; print('conda pandas', pandas.__version__)"
```

> 💡 **What just happened.** `conda install pandas` printed `Solving environment:` and then installed *dozens* of packages, not one. That solver is conda being careful — it checks that every package version is mutually compatible before it touches your disk. It is thorough, and it is why conda can feel slow and the environment ends up large. Note the count from `conda list | wc -l`.

### Step 4: Switch off and delete it

```bash
conda deactivate               # back to (base) — the env still exists, just not active
conda env list                 # claims-conda is still listed
conda env remove -n claims-conda -y   # delete the environment entirely
conda env list                 # claims-conda is gone
```

✅ **Checkpoint:** `conda env list` no longer shows `claims-conda`.

**Note for your records:** conda installs went through a **solver**, pulled in many packages, and live in a central location (`conda env remove` is how you delete them — you don't just delete a folder). Reach for conda when you need **non-Python / scientific binaries** (GDAL, CUDA, R) in the same environment.

---

## Part 2: venv + pip — "an environment is just a folder" (about 12 min)

`venv` ships with Python itself. It does **one** job: isolate. `pip` does the other job: install. Together they are the **course baseline** for the next 8 weeks, and what most tutorials, CI systems, and Stack Overflow answers assume.

### Step 5: Create and activate a venv

```bash
cd ~/env-lab
python -m venv claims-venv     # creates a folder named claims-venv/
ls claims-venv                 # look inside: bin/, lib/, pyvenv.cfg — it's just a directory
source claims-venv/bin/activate   # activate it; prompt shows (claims-venv)
```

> 💡 `source` runs the activate script *in your current shell* so it can change your `PATH` and prompt. This is the `source ... /activate` command you'll type all summer.

✅ **Checkpoint:** prompt shows `(claims-venv)`. Run `which python` — it points *inside* `claims-venv`, not the system Python.

### Step 6: Install with pip and record it

```bash
pip list                       # nearly empty — this env is isolated and clean
pip install pandas             # pip installs from PyPI into THIS env only
pip freeze > requirements.txt  # record exactly what's installed
cat requirements.txt           # pinned versions: pandas==... plus its dependencies
```

> 💡 **What just happened.** `pip freeze` is how you *record* a pip environment — there is no automatic lock file. It writes every installed package at its exact version into `requirements.txt`, which you commit. Anyone can later run `pip install -r requirements.txt` to rebuild it. Compare the package count to conda: `pip list | wc -l`.

### Step 7: Deactivate, then delete by removing the folder

```bash
deactivate                     # leave the env; prompt returns to normal (or (base))
rm -rf claims-venv             # THIS is how you delete a venv — just remove the folder
ls                             # claims-venv is gone; requirements.txt remains
```

✅ **Checkpoint:** `claims-venv/` is gone, but `requirements.txt` is still there.

**The key insight:** a venv is **just a folder**. Deleting the folder deletes the environment — no special command, nothing left behind in a central location. That simplicity is exactly why it's the baseline. The trade-off: `pip` installs serially (can feel slow on big projects) and `requirements.txt` from `pip freeze` records versions but does **not** lock transitive dependencies with hashes the way a real lock file does. Which is the perfect setup for uv.

---

## Part 3: uv — one fast tool, real projects, real locks ⭐ (about 25 min — this is the focus)

`uv` (from Astral, the Ruff team) does **both jobs** like conda, but it is written in Rust, so it is *fast*, and it manages your project through a `pyproject.toml` plus a real **lock file** — the modern standard. It replaces venv, pip, pip-tools, and more with one command. This is where most new Python projects are heading, so spend your time here.

### Step 8: Install uv

uv is **not** preinstalled in Codespaces, so install it (one line):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env    # put uv on your PATH now (or open a new terminal)
uv --version                   # confirm it's installed
```

✅ **Checkpoint:** `uv --version` prints a version.

### Step 9: Start a real project with `uv init`

```bash
cd ~/env-lab
uv init claims-uv              # create a new project folder, fully scaffolded
cd claims-uv
ls -a                          # look at everything uv created
```

You'll see uv scaffolded a whole project, not just an environment. Open and read each file:

```bash
cat pyproject.toml             # the project's identity + its DEPENDENCIES (human-edited)
cat .python-version            # which Python this project pins
cat main.py                    # a starter script (name may vary by uv version)
```

> 💡 **The TOML file is the heart of it.** `pyproject.toml` is the official, standardized Python project file. The `[project]` section names your project and, crucially, lists your **direct** dependencies. You rarely edit it by hand — `uv add` edits it for you — but you *read* it constantly. This one file replaces the role of `requirements.txt` *and* a lot of setup boilerplate.

### Step 10: Add a dependency with `uv add`

```bash
uv add pandas                  # notice how fast this is compared to pip/conda
```

Watch what one command did. Inspect each result:

```bash
cat pyproject.toml             # pandas is now listed under [project] dependencies
cat uv.lock | head -40         # a LOCK FILE uv created/updated automatically
ls -a                          # uv made a .venv/ for you — no manual `python -m venv`
```

> 💡 **What just happened — three things, one command.** `uv add pandas` (1) added `pandas` to `pyproject.toml`, (2) created/updated **`uv.lock`** — which pins *every* direct and transitive dependency to an exact version **with hashes** for reproducibility, and (3) created a `.venv` and installed into it. You never typed `python -m venv`, never typed `activate`, never ran `pip freeze`. That's the whole pitch.

### Step 11: Run code without manually activating

```bash
uv run python -c "import pandas; print('uv pandas', pandas.__version__)"
```

> 💡 `uv run` executes your command *inside the project's environment automatically* — no `source .../activate` needed. uv reads `pyproject.toml`, makes sure `.venv` matches the lock file, then runs. (You *can* still `source .venv/bin/activate` if you prefer the classic feel.)

### Step 12: `uv sync` — rebuild the exact environment from the lock

This is the command that makes a teammate's machine match yours exactly.

```bash
rm -rf .venv                   # pretend you just cloned this project — no env yet
uv sync                        # rebuild .venv to EXACTLY match uv.lock
uv run python -c "import pandas; print('rebuilt:', pandas.__version__)"
```

✅ **Checkpoint:** after `rm -rf .venv` and `uv sync`, the code runs again with the same pandas version.

> 💡 **`uv add` vs `uv sync` — learn this distinction.**
> - **`uv add <pkg>`** = *change* the project: add a new dependency, update `pyproject.toml`, and re-lock.
> - **`uv sync`** = *reproduce* the project: make your `.venv` exactly match the existing `uv.lock`. No new dependencies, no surprises. This is what you (or CI, or a teammate) run after cloning.

### Step 13: One more, to see it manage the project for you

```bash
uv add requests                # add a second dependency
cat pyproject.toml             # both pandas and requests now listed
uv remove requests             # and it cleanly removes it + re-locks
cat pyproject.toml             # requests is gone again
```

> 💡 **Managing assets better.** Because `pyproject.toml` (what you *want*) and `uv.lock` (the *exact* resolved versions) are always kept in sync by uv, your project is self-describing and reproducible by default. You commit both files; you never hand-maintain a `requirements.txt`; `uv sync` rebuilds anywhere. uv even manages **Python versions** themselves (`uv python install 3.12`), so a project can pin not just its packages but its interpreter.

---

## Part 4: Side-by-side — make the differences explicit (about 5 min)

Fill this in from what you actually saw (the package counts and speed are yours to observe):

| Question | conda | venv + pip | uv |
| :--- | :--- | :--- | :--- |
| Isolates the environment? | Yes | Yes (`venv`) | Yes (auto) |
| Manages packages? | Yes | Yes (`pip`) | Yes |
| Installs non-Python binaries? | **Yes** | No | No |
| How you record deps | `conda env export` → `environment.yml` | `pip freeze` → `requirements.txt` | **automatic** `uv.lock` + `pyproject.toml` |
| Real lock file (hashes, transitive)? | Partial | No | **Yes** |
| How you delete the env | `conda env remove -n …` | `rm -rf <folder>` | `rm -rf .venv` (lock stays) |
| Speed (your observation) | slowest? | middle? | fastest? |
| Reach for it when… | non-Python / scientific stack | the universal baseline | modern projects, speed + reproducibility |

### ✍️ Reflect (write the answers in your notes — 2 min)

1. What are the **two jobs**, and which tool(s) do each? (If you can answer this, yesterday's confusion is gone.)
2. Why is a venv "just a folder," and why is that both its strength and its limit?
3. What does `uv.lock` guarantee that a `pip freeze` `requirements.txt` does not?
4. In one sentence each: when would you choose conda, venv + pip, and uv?

---

## Part 5: Why the course baseline is venv + pip

You just saw uv is faster and more modern — so why does the program standardize on **venv + pip + `requirements.txt`**?

- It's **always there.** venv and pip ship with Python; nothing to install on any machine, any CI runner, any cloud shell.
- It's **transparent.** You see every step (create, activate, install, freeze), which is exactly the muscle memory we're building in the AI-Free Zone.
- It's **what the ecosystem assumes.** Most tutorials, Dockerfiles, and job postings still speak pip + requirements.txt.

We teach **conda** so you can work in scientific/non-Python stacks, and **uv** because it's where the field is moving and you'll meet it on modern teams. Knowing all three — and *why* they differ — is the actual skill.

> [!IMPORTANT]
> Clean up the sandbox so it doesn't linger: `cd ~ && rm -rf ~/env-lab`. Your course repo (Lab B) is untouched.

---

## 🏆 Challenge (for fast finishers, about 8 min)

1. With uv, recreate the project but pin a specific Python: `uv python install 3.12` then start a fresh `uv init` project and check `.python-version`. What changed?
2. Open `uv.lock` and find one package you did **not** install directly (a transitive dependency of pandas). Why is it in the lock file but not in `pyproject.toml`?
3. Make a conda `environment.yml` from a fresh env (`conda env export > environment.yml`) and compare its shape to a `pyproject.toml`. Which would you rather hand a new teammate, and why?

---

## 🧾 What you learned

| Command | Tool | What it does |
| :--- | :--- | :--- |
| `conda init bash` (then restart shell) | conda | One-time: enable `conda activate` in your shell |
| `conda create -n <name> python=3.11` / `conda activate` | conda | Create / activate an environment |
| `conda install <pkg>` / `conda env remove -n <name>` | conda | Install (via solver) / delete the whole env |
| `python -m venv <folder>` / `source <folder>/bin/activate` | venv | Create / activate (an env is just a folder) |
| `pip install <pkg>` / `pip freeze > requirements.txt` | pip | Install / record dependencies |
| `deactivate` / `rm -rf <folder>` | venv | Leave / delete the env |
| `uv init` / `uv add <pkg>` / `uv remove <pkg>` | uv | Start a project / add / remove a dependency (+ auto-lock) |
| `uv sync` / `uv run <cmd>` | uv | Rebuild env from the lock / run inside it without activating |

**Key mental model:** two jobs — *isolate the environment* and *manage the packages*. venv does the first, pip does the second, and **conda and uv do both**. uv adds a `pyproject.toml` + automatic lock file so a project is reproducible by default.

---

## ➡️ Next: Lab B — Git, the solo cycle

You now understand environments. In `Lab_B_Git_The_Solo_Cycle.md` you'll build your actual course repo (using the venv + pip baseline) and run the local Git cycle — status, add, diff, commit, log — entirely on your own machine before you ever touch GitHub.
