# Week 1 · Day 3 — Lab

**Theme:** Developer Environment Setup  
**Format:** Guided setup lab (pairs — navigator/driver, swap every 30 min)

## Lab Index

### Provided files

| File | What it is |
| :--- | :--- |
| [README.md](README.md) *(this file)* | Step-by-step setup lab with verification checklist |
| [GitHub Troubleshooting.md](GitHub%20Troubleshooting.md) | Common auth, Codespace, and Git errors with fixes |
| [Student_Resources.md](Student_Resources.md) | VS Code shortcuts, Git cheat sheet, Codespaces docs, and more |

### Deliverables

| # | Deliverable | Format | Due |
| :--- | :--- | :--- | :--- |
| 1 | Pushed `techcatalyst-2026-<yourname>` repo with `hello_data.py`, `requirements.txt`, `.gitignore` | GitHub repo | End of day |
| 2 | Completed Part 5 verification checklist committed into `README.md` | Markdown in repo | End of day |
| 3 | At least 2 commits visible in `git log`, partner-verified | Git history | End of day |

---

# Setup Lab: Your Environment, End to End (150 min, pairs)

Work in pairs (navigator/driver — swap every 30 minutes). Both partners complete every step on their own account.

## Part 1 — GitHub & repo (20 min)

1. Create/sign in to your **personal** GitHub account.
2. Create a repository: `techcatalyst-2026-<yourname>` (public or private — your choice), initialized with a README.
3. In the README, add: your name, cohort, and a one-line bio.

## Part 2 — Codespace (25 min)

4. From your repo: **Code → Codespaces → Create codespace on main**.
5. In the terminal, record the output of:
   ```bash
   python --version
   pip --version
   git --version
   uname -a
   ```
6. Install the **Python** and **Jupyter** extensions in VS Code.
7. ⚠️ Find where to **stop** your Codespace. Practice stopping and restarting it once.

## Part 3 — Python environment (35 min)

8. In your repo root:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install pandas requests
   pip freeze > requirements.txt
   ```
9. Create `.gitignore` containing `.venv/`.
10. Create `hello_data.py`:
    ```python
    import pandas as pd
    import requests

    print(f"pandas {pd.__version__} ready")
    r = requests.get("https://api.github.com")
    print(f"GitHub API says: {r.status_code}")
    ```
11. Run it: `python hello_data.py`. Both lines must print.

## Part 4 — First Git cycle (30 min)

12. Configure identity (once):
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```
13. Run the cycle and observe `git status` between every step:
    ```bash
    git status
    git add .
    git status
    git commit -m "Add hello_data script and requirements"
    git push
    git log --oneline
    ```
14. Verify the files appear on github.com.

## Part 5 — Verification checklist (commit this to your README)

- [ ] Codespace starts and stops; I know where the stop button is
- [ ] `python --version` ≥ 3.11 inside the Codespace
- [ ] `(.venv)` shows in my prompt when activated
- [ ] `requirements.txt` exists and lists pandas + requests
- [ ] `.venv/` is git-ignored (does NOT appear on GitHub)
- [ ] `hello_data.py` runs and prints both lines
- [ ] At least 2 commits visible in `git log`
- [ ] My partner has verified all of the above on my machine

**Deliverable:** pushed repo with `hello_data.py`, `requirements.txt`, `.gitignore`, and the completed checklist in `README.md`.

## Troubleshooting
See `GitHub Troubleshooting.md` in this folder (carried over from 2025 — still accurate). Stuck >10 minutes? Raise a hand; debugging together is the point, but so is finishing.
