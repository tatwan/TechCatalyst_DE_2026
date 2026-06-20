# Week 1 · Day 5 — Student Resources

> **AI-Free Zone (Weeks 1–4):** Reason through the requirements and draw the architecture yourselves — no AI-generated diagrams or design write-ups. The point is to practice the architect's discipline of letting requirements drive boxes, by hand.

References for architecture patterns, the NYC Taxi dataset, and Draw.io. Keep these open during the design lab.

## Core Documentation

| Resource | Why it helps |
| :--- | :--- |
| [Medallion architecture (Databricks)](https://www.databricks.com/glossary/medallion-architecture) | Bronze/Silver/Gold — your operating model from Week 2 onward |
| [Fundamentals of Data Engineering, Ch. 3–4](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) | Source of the six architect questions in today's lab |
| [GCP reference architectures](https://cloud.google.com/architecture) | Worked GCP pipeline examples shaped like your taxi pipeline |
| [NYC TLC trip record data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | The pipeline source — inspect one month's Parquet schema |
| [Taxi zone lookup CSV](https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv) | Your first dimension table — every team should include it |

---

## Architecture patterns

**"The Lambda Architecture" — Nathan Marz (original)**
http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html
The original article defining Lambda architecture. Short and historically important — read it to understand where the pattern came from and why Kappa was invented as a reaction to it.

**"Questioning the Lambda Architecture" — Jay Kreps (the case for Kappa)**
https://www.oreilly.com/radar/questioning-the-lambda-architecture/
Jay Kreps (co-creator of Kafka) arguing that unified stream processing makes Lambda's two-path approach unnecessary. Read alongside the Marz article for the full debate.

**Medallion architecture — Databricks**
https://www.databricks.com/glossary/medallion-architecture
The clearest explanation of Bronze / Silver / Gold with diagrams. This is the pattern you'll implement from Week 2 onward.

**"Fundamentals of Data Engineering" — Chapters 3 & 4 (Reis & Housley)**
https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
Chapter 3 covers the data engineering lifecycle; Chapter 4 covers choosing the right architecture patterns. The six architect questions in today's lab come directly from this framework.

**Google Cloud reference architectures**
https://cloud.google.com/architecture
Worked examples of real GCP pipelines, including data lake and analytics architectures. Browse the "Data Analytics" section — several examples match the shape of your taxi pipeline.

---

## The NYC Taxi dataset

**NYC TLC trip record data (source)**
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
The actual source for your pipeline. Monthly Parquet files going back to 2009. Click any year and download one month's yellow taxi file to inspect the schema.

**Yellow taxi data dictionary (PDF)**
https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
Field definitions for every column. Know this before Week 3 — you'll write SQL against these fields.

**Taxi zone lookup table (CSV)**
https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
Maps `PULocationID` and `DOLocationID` integers to borough and zone names. This is your first dimension table — every team should include it as a companion dataset.

**NYC Motor Vehicle Collisions dataset**
https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95
If your team chooses the safety analysis slant, this is the companion dataset. Updated daily; filterable by borough and date.

**NYC Open Data (other companion options)**
https://opendata.cityofnewyork.us
Air quality, weather, subway ridership — all joinable to taxi trip data by time and borough. Pick one if you want a richer analysis angle.

**DataTalksClub DE Zoomcamp (same dataset, GCP architecture)**
https://github.com/DataTalksClub/data-engineering-zoomcamp
A free, self-paced course that uses the NYC Taxi data on GCP — the same stack as this program. Their Module 1 architecture diagram is worth looking at as a reference for your own.

---

## Draw.io

**Draw.io (no account needed)**
https://app.diagrams.net
Open the starter file (`architecture_starter.drawio`) directly here: File → Open from → Device.

**Draw.io keyboard shortcuts**
https://www.diagrams.net/blog/shortcuts
The ones you need today: `A` to fit diagram to screen, `Ctrl/Cmd+Shift+H` to reset view, `E` to edit shape style, `Ctrl+Shift+P` to toggle shape panel.

**Adding GCP icons to Draw.io**
In Draw.io: Extras → Edit Diagram (XML) for fine control, or More Shapes → Networking → Google Cloud Platform for the official GCP icon set. Use these to name services visually — a GCS bucket icon communicates faster than a box labeled "storage."

**Exporting from Draw.io**
File → Export As → PNG (for your repo's `architecture.png`) and File → Save As → `.drawio` (for the editable version). Commit both — the PNG is for reading, the `.drawio` is for editing in Weeks 3, 5, and 7.

---

## Architecture diagram examples

**DE Zoomcamp pipeline diagram**
https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/images/architecture/arch_v3_workshops.jpg
A real worked example using the same dataset. Study how zones, services, and arrows are labeled.

**GCP data analytics reference architecture**
https://cloud.google.com/architecture/data-lifecycle-cloud-platform
Google's own end-to-end data lifecycle diagram covering ingestion → storage → processing → analytics. Compare its layer structure to the Medallion model.

---

## Lab Deliverable Checklist

| ✓ | Deliverable |
| :--- | :--- |
| ☐ | Six architect questions answered *before* any drawing (requirements-first) |
| ☐ | Business slant chosen (demand / driver economics / safety / your own) |
| ☐ | `architecture.drawio` built with medallion zones, left→right flow |
| ☐ | Every arrow labeled with data + format + cadence |
| ☐ | ⚠ quality-check and 🔒 PII-handling points marked |
| ☐ | `architecture.png` exported and committed alongside the `.drawio` |
| ☐ | `design_narrative.md` half-page walkthrough written |
| ☐ | Readout prepared — every member presents one zone |
