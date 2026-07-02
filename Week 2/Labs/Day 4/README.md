# Week 2 Day 4: Mini-Project, Medallion ETL (S3 to GCS bronze to silver)

**This is the Week 2 deliverable.** It is the payoff for the whole week.

## Where this fits (the Week 2 arc)

- **Day 1** you worked with raw files in the terminal.
- **Day 2** you wrote Python to read, clean, and model records *by hand* (dicts,
  `collections`, `datetime`, file/CSV/JSON I/O, error handling).
- **Day 3** you ingested JSON from a live API and wrote a clean CSV.
- **Today** you formalize all of it into a **medallion pipeline**: land raw data
  untouched (**bronze**), then refine it into a typed, analysis-ready table
  (**silver**) in cloud storage.

Two cohesion notes worth saying out loud:

- **By hand, then by library.** On Day 2 you summed groups with `collections` and
  parsed dates with `datetime` yourself. Today `pandas.groupby` and
  `pd.to_datetime` do exactly that, at scale. Same ideas, less code.
- **Bronze/silver is the real pattern.** You will formalize it again in Week 3
  (BigQuery) and the capstone. This is how data lakes are organized.

## The shape of today

```text
PUBLIC S3 bucket (raw)  ->  YOUR GCS bucket
   weather_raw.csv           bronze/weather/ingest_date=YYYY-MM-DD/weather_raw.csv   (untouched)
                             silver/weather/weather_clean.parquet                    (cleaned, typed)
```

You read the source **anonymously from S3** (no AWS keys), and you write to **your
own GCP project** with Application Default Credentials (no key files). A `--local`
mode runs the whole pipeline offline so you can build before you touch the cloud.

## Lab Index

### Provided files

| Folder / File | Purpose |
|---|---|
| `Activity_0_UV_GCS_Setup.md` | Project + GCP auth setup (do this first) |
| `Reading_Big_Data_DataFrames.md` | Explainer: pandas, Polars, Modin, FireDucks, and when to use each |
| `Mini_Project_Medallion_ETL/README.md` | Mini-project instructions (the how-to) |
| `Mini_Project_Medallion_ETL/Walkthrough.ipynb` | Guided teaching notebook: medallion, pandas vs Polars |
| `Mini_Project_Medallion_ETL/starter/medallion_etl.py` | Starter scaffold with TODOs |
| `Mini_Project_Medallion_ETL/data/raw/weather_raw.csv` | Local fallback raw data (for `--local`) |
| `Mini_Project_Medallion_ETL/solutions/` | Instructor reference (open at debrief) |
| `Group_Activity_Pipeline_Advisory.md` | Group: present your architecture and advise the VP, with a future-state diagram |
| `Python Drills/` | Optional intermediate Python foundations notebook: functions, loops, nested data, and the `math`, `statistics`, `random`, `datetime`, `calendar`, `pathlib`, `glob`, `itertools` modules. Use for extra reps or if Day 2 felt fast. |
| `Pandas Instructor Demos/` | Optional 2025 pandas notebooks for the morning live-code or extra reps |
| `Pandas Student Activities/` | Optional 2025 pandas drills if you finish early |
| `Yellow Taxi Analysis/` | Optional preview of Week 3, where NYC Taxi becomes the pipeline spine |

### Deliverables

| # | Deliverable | Format | Due |
| :--- | :--- | :--- | :--- |
| 1 | `medallion_etl.py`: S3 → bronze (GCS) → silver (GCS), runs end to end | Python file + PR | 5:00pm |
| 2 | `silver/<dataset>/<dataset>_clean.parquet` in your GCS bucket | GCS object + screenshot in PR | 5:00pm |
| 3 | `README.md`: how to run, your cleaning decisions, profile highlights, the `gs://` paths for bronze and silver | Markdown in repo | 5:00pm |
| 4 | Reviewed one teammate's PR with 2+ substantive comments | PR review | 5:00pm |
| 5 | Group advisory: present your architecture, observations, risks, and a future-state diagram (`Group_Activity_Pipeline_Advisory.md`) | Team presentation | Afternoon |

Submission is by pull request (the instructor cannot see inside your GCP project),
so the screenshot of your silver object is required.

## Setup

Do `Activity_0_UV_GCS_Setup.md` first. In short, from the repo root:

```bash
mkdir -p student-work/week2 && cd student-work/week2
uv init
uv add "pandas>=3.0" polars pyarrow boto3 google-cloud-storage
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

Add `.venv/`, `__pycache__/`, `data/bronze/`, `data/silver/`, and `*.parquet` to
the `.gitignore` in `student-work/week2/`. Select
`student-work/week2/.venv/bin/python` as the VS Code interpreter and notebook
kernel. Then copy the starter and `data/` into your project and build there. Run
with `--local` first; switch to the cloud path once your GCS write works.

## Requirements

### 1. Extract (S3, anonymous)
- Read the raw object from the public S3 source bucket with `boto3` (unsigned
  config). No AWS keys. (Use `--local` to read `data/raw/weather_raw.csv` instead
  while you build.)

### 2. Bronze (land raw, immutable)
- Upload the raw bytes **unchanged** to
  `gs://<your-bucket>/bronze/<dataset>/ingest_date=YYYY-MM-DD/<dataset>_raw.csv`.
- Bronze is never edited. It is your reproducible source of truth.

### 3. Silver (clean with pandas)
- `pd.read_csv`, then profile: `info()`, `describe()`, `isna().sum()` (paste
  highlights into your README).
- Clean with explicit, justified decisions:
  - normalize column names (lowercase)
  - `pd.to_datetime(..., errors="coerce")` and `pd.to_numeric(..., errors="coerce")`
  - a missing-value policy per column (say why: fill vs drop)
  - `drop_duplicates` on a sensible key (here `station` + `date`)
  - at least **two derived columns** (e.g., `temp_range`, `is_rainy`)
- Write parquet and upload to `gs://<your-bucket>/silver/<dataset>/<dataset>_clean.parquet`.

### 4. Polars comparison (the week's Pandas vs Polars promise)
- Do one transform (a `group_by(...).agg(...)`) in **Polars** as well, and note in
  your README one difference you noticed between the pandas and Polars APIs.

### 5. Code quality
- Functions with docstrings, a `__main__` guard, no secrets anywhere. UV manages
  the environment with `pyproject.toml` and `uv.lock`; do not create a legacy
  package-list file for this lab.

## Expected local output (`--local`)

With the provided `weather_raw.csv` (20 raw rows) and the cleaning decisions above:

```text
silver rows: 14
{'MA1BOS': 5, 'RI1PVD': 3, 'US1NY': 6}
```

(7 of the 14 rows are rainy; 6 rows are dropped: missing date, duplicates, bad or
missing temperatures.) Your exact numbers can differ if you justify different
cleaning choices.

## Rubric

| Criterion | Weight |
| :--- | :--- |
| Runs end to end: S3 → bronze → silver, parquet in GCS | 30% |
| Cleaning decisions explicit and justified | 25% |
| Code quality (functions, docstrings, main guard, UV env, no secrets) | 20% |
| Bronze is immutable and silver is typed; sensible partition/paths | 15% |
| PR hygiene and review comments | 10% |

## Optional extras (finish early)

- `Python Drills/`: an intermediate Python foundations notebook (functions, loops,
  nested data, and the `math`, `statistics`, `random`, `datetime`, `calendar`,
  `pathlib`, `glob`, `itertools` modules) with a solutions notebook. Good if Day 2
  moved too fast or you want more standard-library practice.
- `Pandas Instructor Demos/` and `Pandas Student Activities/`: the 2025 pandas drill
  set for extra reps.
- `Yellow Taxi Analysis/`: a preview of Week 3, where NYC Taxi becomes the spine.
