# Week 1 · Day 4 — Lab

**Theme:** Cloud Object Storage — GCS hands-on, landing zone design  
**Format:** Individual lab + group design activity

## Lab Index

### Provided files

| File | What it is |
| :--- | :--- |
| [README.md](README.md) *(this file)* | Full lab: landing zone build + group storage layout design |
| [Student_Resources.md](Student_Resources.md) | GCS docs, gcloud reference, S3 comparison, and lifecycle examples |
| [Lab Resources/coffee.jpg](Lab%20Resources/coffee.jpg) | Sample image — upload, overwrite, and version in Parts 1 & 3 |
| [Lab Resources/hartford.jpeg](Lab%20Resources/hartford.jpeg) | Sample image — upload under a prefix in Part 1 |
| [Lab Resources/intro.docx](Lab%20Resources/intro.docx) | Sample non-image object — upload under a prefix in Part 1 |

### Deliverables

| # | Deliverable | From | Format | Due |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `day4_lab.md` — all commands run + answers to Q1–Q5 + screenshots of both buckets | Landing Zone lab | Markdown committed to course repo | End of day |
| 2 | GCS↔S3 differences list (stretch) | Part 4 | Appended to `day4_lab.md` | Optional |
| 3 | One-page team storage convention doc (bucket/prefix layout for the 8-week pipeline) | Group Think | One-pager / whiteboard photo | End of day |

---

# Lab: Build Your Landing Zone (120 min)

You'll create, secure, organize, and script a GCS landing zone — the bucket your pipeline uses for the rest of the program. Take your time on each section; exploring the options is part of the learning.

**Resources:** `Lab Resources/` contains `hartford.jpeg`, `coffee.jpg`, and `intro.docx` (same assets as the 2025 S3 lab).

## Part 1 — Console (40 min)

1. Create a bucket named `techcatalyst-de-2026-<your-username>-raw`:
   - Location type: **Region** → `us-east1`
   - Storage class: **Standard**
   - **Uniform** bucket-level access: ON
   - Public access prevention: ON
2. Upload `coffee.jpg`. Click it and press **Open** — it works. Why?
3. Copy the **Object URL** (`https://storage.googleapis.com/...`) into an incognito window.

   **Q1:** You got an error. Paste it into your lab notes and explain *why* you got it when "Open" worked.
4. Upload `hartford.jpeg` and `intro.docx` under the prefix `raw/2026/06/`.

   **Q2:** Did GCS create folders? What are you actually looking at?
5. Grant your lab partner's Google account `Storage Object Viewer` on your bucket. Have them list it from their console.

## Part 2 — CLI (40 min)

Open Cloud Shell (or your Codespace with `gcloud` authenticated).

```bash
# create a second bucket for processed data
gcloud storage buckets create gs://techcatalyst-de-2026-<your-username>-processed \
  --location=us-east1 --uniform-bucket-level-access

# copy between buckets
gcloud storage cp gs://techcatalyst-de-2026-<your-username>-raw/raw/2026/06/* \
  gs://techcatalyst-de-2026-<your-username>-processed/staging/

# list recursively with sizes
gcloud storage ls -l gs://techcatalyst-de-2026-<your-username>-processed/**
```

**Q3:** What does `**` do differently from `*`?

6. Add a lifecycle rule to the raw bucket: transition to **Nearline** after 30 days, delete after 365. (Console UI is fine; inspect the JSON it generates and save it in your notes.)

   **Q4:** Your raw zone holds regulatory data that must be retained 7 years. Rewrite the rule.

## Part 3 — Versioning (20 min)

7. Enable object versioning on the raw bucket:
   ```bash
   gcloud storage buckets update gs://techcatalyst-de-2026-<your-username>-raw --versioning
   ```
8. Upload a *different* image as `coffee.jpg` (overwrite). List all generations:
   ```bash
   gcloud storage ls -a gs://techcatalyst-de-2026-<your-username>-raw/coffee.jpg
   ```
9. Restore the original generation.

   **Q5:** Why might you want versioning OFF on a high-volume raw zone, and what protects you instead? (Hint: bronze immutability.)

## Part 4 — Stretch: the S3 mirror (optional)

Repeat Parts 1–2 in AWS S3 (course account). Keep a running list of every difference you notice — naming, console layout, CLI syntax, permissions model. Add the list to your lab notes.

## Deliverable

`day4_lab.md` committed to your course repo containing: all commands you ran, answers to Q1–Q5, screenshots of both buckets, and (stretch) your GCS↔S3 differences list.

---

# Group Think — Taxi Storage Layout (45 min)

Design your team's bucket/prefix convention for the 8-week pipeline:

1. One bucket with `raw/` + `processed/` prefixes, or separate buckets? Defend it (think IAM, lifecycle, blast radius).
2. Date-partitioned naming for taxi data, e.g. `raw/yellow/year=2026/month=06/yellow_tripdata_2026-06.parquet`. Why this `key=value` style? (It will matter in Weeks 3 and 5.)
3. Storage class + lifecycle policy per zone.
4. 3-minute whiteboard readout.

**Deliverable:** one-page storage convention doc — your team follows it for the rest of the program.
