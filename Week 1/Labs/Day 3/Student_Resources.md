# Week 1 · Day 3 — Student Resources

> **AI-Free Zone (Weeks 1–4):** Today is where the rule gets real — type every command yourself. No Copilot autocompleting your Git or venv steps. Building this muscle memory now is what lets you trust (and challenge) AI suggestions in Week 6.

Reference links and cheat sheets for today's tools. Keep these bookmarked — you'll use them all summer.

## Core Documentation

| Resource | Why it helps |
| :--- | :--- |
| [GitHub Codespaces docs](https://docs.github.com/en/codespaces) | Your dev environment for the whole program — start here |
| [Codespaces free-tier limits](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) | 120 core-hours/month — know why you stop your Codespace |
| [Python venv docs](https://docs.python.org/3/library/venv.html) | The authoritative reference on isolated environments |
| [Git cheat sheet (GitHub Education)](https://education.github.com/git-cheat-sheet-education.pdf) | One page with every command you need for four weeks |
| [.gitignore templates](https://github.com/github/gitignore) | Use `Python.gitignore` so `.venv/` never gets committed |

---

## VS Code

**VS Code keyboard shortcuts — Linux/Windows (PDF)**
https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf

**VS Code keyboard shortcuts — macOS (PDF)**
https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf

The three you need today: `Ctrl/Cmd+Shift+P` (command palette), `Ctrl+\`` (terminal), `Ctrl/Cmd+P` (quick open file). Learn five more per week.

**VS Code "Getting Started" docs**
https://code.visualstudio.com/docs
The official docs are genuinely good. Start with "User Interface" and "Python" sections.

---

## GitHub Codespaces

**GitHub Codespaces documentation**
https://docs.github.com/en/codespaces

**Codespaces free tier limits**
https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts
Personal accounts get 120 core-hours/month free. A 2-core Codespace uses those up in 60 hours of active time. **Stop your Codespace when you're not using it** — the billing page shows where your hours go.

**Codespace lifecycle — how to stop, restart, and delete**
https://docs.github.com/en/codespaces/getting-started/the-codespace-lifecycle

---

## Python virtual environments

**Python `venv` — official documentation**
https://docs.python.org/3/library/venv.html
The authoritative reference. Short and worth reading once.

**"Python Virtual Environments: A Primer" — Real Python**
https://realpython.com/python-virtual-environments-a-primer/
The best tutorial on why venvs exist, how they work internally, and common mistakes. Read this before Week 2 if the concepts felt shaky today.

**`pip` user guide**
https://pip.pypa.io/en/stable/user_guide/
How `pip install`, `pip freeze`, and `requirements.txt` actually work.

---

## Git and GitHub

**Git cheat sheet (PDF) — GitHub Education**
https://education.github.com/git-cheat-sheet-education.pdf
One page. Print it or keep it open. Every command you need for the next four weeks is on it.

**Git official reference**
https://git-scm.com/docs
Not for browsing — use it when you need to look up exactly what a command does.

**"Git and GitHub for Beginners" — freeCodeCamp (video, ~1 hour)**
https://www.youtube.com/watch?v=RGOj5yH7evk
The best introductory video on Git. If today felt fast, watch the first 30 minutes tonight.

**`.gitignore` templates — GitHub**
https://github.com/github/gitignore
The Python template (`Python.gitignore`) is the one to use for all your course repos. Copy it into your `.gitignore` and you won't accidentally commit `.venv/`, `__pycache__/`, or `.env` files.

**Conventional commits — commit message format**
https://www.conventionalcommits.org/
Not required this week, but a good habit. `feat:`, `fix:`, `chore:` prefixes make `git log` readable. We'll enforce this in the longitudinal project from Week 3 onward.

---

## Troubleshooting

**GitHub Troubleshooting guide (course-specific)**
See `GitHub Troubleshooting.md` in this folder. Covers auth errors, Codespace boot failures, and the most common Git mistakes from past cohorts.

**GitHub status page**
https://githubstatus.com
If Codespaces won't launch and nothing else explains it — check here first.

---

## Lab Deliverable Checklist

| ✓ | Deliverable |
| :--- | :--- |
| ☐ | `techcatalyst-2026-<yourname>` repo created with a README (name, cohort, bio) |
| ☐ | Codespace starts and stops; you know where the stop button is |
| ☐ | `.venv` activated (prompt shows `(.venv)`); `requirements.txt` lists pandas + requests |
| ☐ | `.venv/` is git-ignored and does NOT appear on GitHub |
| ☐ | `hello_data.py` runs and prints both lines |
| ☐ | At least 2 commits pushed and visible in `git log --oneline` |
| ☐ | Partner has verified every checklist item on your machine |
