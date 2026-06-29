# Week 1 Day 3: Class VM Lab

**Theme:** Developer foundations with Linux terminal, VS Code, Python environments, Git, and GitHub  
**Format:** Separated hands-on activities for pacing, breaks, and live recovery  
**Environment:** Classroom Linux terminal plus VS Code. Use this path when students are working locally or on a class Linux machine.

> [!WARNING]
> **AI-Free Zone, Weeks 1 to 4.** Type every command yourself. No Copilot, no LLM-generated code, SQL, or Git commands. Docs, peers, and instructor demos are allowed.

## Why This Folder Exists

The original Day 3 content depended on a hosted development environment. This `class_vm` version is the recovery path for a regular Linux classroom machine. Use it when students have terminal and VS Code access.

The original hosted-environment version is preserved in:

```text
Week 1/Labs/Day 3/codespace/
```

## Provided Files

| File | What it is |
| :--- | :--- |
| `README.md` | This class VM guide |
| `Lab_A_Python_Environments.md` | Python environment setup with UV as the main path and venv plus pip as the comparison |
| `Lab_B_Git_The_Solo_Cycle.md` | Local repo, terminal commands, Python script, and Git solo cycle |
| `Lab_C_GitHub_Remote_and_Collaboration.md` | GitHub remote, clone, push, pull, branch, PR, and merge |
| `Lab_D_Profile_Page.md` | Optional GitHub profile page |
| `Lab_E_GitHub_Pages.md` | Optional GitHub Pages site |
| `Student_Resources.md` | Current references for Linux terminal, VS Code, UV, Python, Git, and GitHub |
| `GitHub Troubleshooting.md` | Common local Git and GitHub issues |
| `data/hartford_claims_sample.csv` | 12-row sample claims dataset |
| `github-pages-template/` | Starter files for the optional Pages lab |
| `solutions/` | Instructor solution notes |
| `quiz/` | Knowledge checks, update questions live if you skip optional sections |

## Suggested Flow

| Block | Activity | Time |
| :--- | :--- | :--- |
| 1 | Lab A: Python environments with UV | 60-75 min |
| 2 | Break and reset | 10-15 min |
| 3 | Lab B: local repo, terminal, Python script, and Git solo cycle | 75-90 min |
| 4 | Lunch or longer break | 45-60 min |
| 5 | Lab C Section 1: GitHub remote, push, pull, clone, fetch | 60-75 min |
| 6 | Break and troubleshooting | 10-15 min |
| 7 | Lab C Section 2: branch, PR, review, merge | 45-60 min |
| 8 | Optional Lab D or E, quiz, cleanup, and debrief | 45-90 min |

Fast students can move into Lab D, Lab E, or the challenge sections. Students who need more time should complete Labs A, B, and Lab C Section 1 first.

## Deliverables

| # | Deliverable | From | Format |
| :--- | :--- | :--- | :--- |
| 1 | Notes answering the Lab A reflection questions | Lab A | Notes or `README.md` |
| 2 | Local `techcatalyst-2026-<yourname>` project with UV files, Python script, data file, `.gitignore`, and Git history | Lab B | Local folder and Git repo |
| 3 | GitHub repository published from the local project | Lab C | GitHub repo |
| 4 | A verified clone named `journal-clone` | Lab C | Local folder |
| 5 | About section merged into `main` through a pull request | Lab C | GitHub PR and local sync |
| 6 | Optional GitHub profile or Pages site | Lab D or E | GitHub |

## How the Day Fits Together

**Lab A** fixes environment confusion. Students use UV to create a project, add packages, run code, rebuild the environment from a lock file, and compare that workflow to venv plus pip.

**Lab B** keeps everything local. Students create the course repo in VS Code, use terminal commands to inspect files, run a Python script against the sample dataset, and practice Git status, add, diff, commit, and log.

**Lab C** connects local work to GitHub. Students create an empty GitHub repo, push local commits, pull a web edit, clone a second copy, compare fetch and pull, then practice branch and PR workflow.

**Labs D and E** are optional portfolio activities. They are useful if the class finishes early or if you want a morale boost after Git-heavy work.

## Currentness Check

| Topic | Source checked | Date checked | Class decision |
| :--- | :--- | :--- | :--- |
| UV project setup | <https://docs.astral.sh/uv/concepts/projects/init/> | 2026-06-28 | Use `uv init`, `uv add`, `uv sync`, and `uv run` for local Python project setup |
| Python venv | <https://docs.python.org/3/library/venv.html> | 2026-06-28 | Use venv plus pip only as a comparison path |
| VS Code terminal | <https://code.visualstudio.com/docs/terminal/basics> | 2026-06-28 | Use integrated terminal or a regular Linux terminal |
| GitHub clone | <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository> | 2026-06-28 | Teach local clone from GitHub after pushing |
| GitHub pull requests | <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request> | 2026-06-28 | Teach PR flow after local Git basics |

## Troubleshooting

Use `GitHub Troubleshooting.md` in this folder. Most live issues in this path are local path confusion, missing Git identity, missing GitHub authentication, or forgetting to run commands from the project root.
