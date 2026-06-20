# Week 1 · Day 5 — Lab

**Theme:** Data Architectures & Pipeline Design — the Week 1 deliverable  
**Format:** Team design lab (groups of 3–4)

## Lab Index

### Provided files

| File | What it is |
| :--- | :--- |
| [README.md](README.md) *(this file)* | Design lab brief, rubric, and readout protocol |
| [architecture_starter.drawio](architecture_starter.drawio) | Draw.io skeleton with zone containers pre-drawn — open at https://app.diagrams.net |
| [Student_Resources.md](Student_Resources.md) | Architecture pattern references, dataset links, Draw.io guide |

### Deliverables

| # | Deliverable | From | Format | Due |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Six architect-question answers (requirements before drawing) | Phase 1 | Table in `design_narrative.md` | End of day |
| 2 | `architecture.drawio` + exported `architecture.png` (medallion zones, labeled arrows, ⚠/🔒 marks) | Phase 2 | Committed to a team repo | End of day |
| 3 | `design_narrative.md` — half-page source→dashboard walkthrough with the "why" of each decision | Phase 3 | Markdown in repo | End of day |
| 4 | 5-min readout — every member presents one zone; defend against the critique protocol | Phase 4 | Verbal | End of day |

---

# Design Lab: Your Taxi Pipeline Architecture (120 min)

**This is the Week 1 deliverable.** Your team designs the end-to-end conceptual architecture you will actually build over the next seven weeks.

## The scenario

You are the data engineering team for a transportation analytics startup. You'll ingest NYC TLC trip records (millions of rows/month, Parquet, published monthly: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) plus at least one companion dataset (taxi zones lookup, collisions, air quality). Pick a business slant: demand forecasting, driver economics, safety analysis, or one you propose.

## Phase 1 — Requirements first (30 min, no drawing!)

Write answers to the six architect questions:

| Question | Your answer |
| :--- | :--- |
| Sources, formats, volumes? | |
| How fresh must data be (per consumer)? | |
| Who consumes it and how? | |
| What can go wrong, and where? | |
| What's sensitive (PII or quasi-identifiers)? | |
| What does it cost to run — top 2 cost drivers? | |

## Phase 2 — Draw it (60 min)

In Draw.io (https://app.diagrams.net — a starter skeleton with zone containers is in this folder):

- Zones left → right: **Ingest → Lake (medallion: bronze/silver) → Transform → Warehouse → Serve**
- Use yesterday's storage layout convention for the lake zone
- Label **every arrow**: what moves, in what format, how often
- Mark with a ⚠ where data quality checks happen, and with 🔒 where PII handling happens
- Name real services (GCP primary; you may note AWS equivalents)

## Phase 3 — Narrative (15 min)

Write a half-page walkthrough a new engineer could follow: start at the source, end at the dashboard, mention each decision and *why*.

## Phase 4 — Readout (5 min/team + critique)

Every member presents one zone. Reviewers use the critique protocol:
- What happens when a file fails halfway?
- Where would PII leak?
- What does this cost at 10× volume?
- What would you cut to ship in one week?

## Deliverable (commit to one team member's repo, link from others)

- `architecture.drawio` + exported `architecture.png`
- `design_narrative.md` (requirements table + walkthrough)

## Rubric (instructor)

| Criterion | Weight |
| :--- | :--- |
| Requirements drive the design (not boxes-first) | 25% |
| Correct medallion zones + storage convention reuse | 20% |
| Arrows labeled with data, format, cadence | 20% |
| Quality & PII checkpoints placed sensibly | 15% |
| Narrative clarity + readout defense | 20% |

> [!NOTE]
> This diagram is a living document — you will revise it in Weeks 3, 5, and 7 as the real pipeline takes shape, and it becomes the backbone of your capstone presentation.
