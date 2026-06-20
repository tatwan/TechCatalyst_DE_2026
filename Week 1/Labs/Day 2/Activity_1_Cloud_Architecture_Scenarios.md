# Week 1 · Day 2 — Activity 1: You're the Architect

**Duration:** 60 min  
**Format:** Groups of 3–4 (same teams as Day 1)

---

## The scenario

Your team is advising The Hartford's data platform group. Each scenario below is a real type of problem data engineers face at an insurer. For each one, choose the right cloud services and defend your choices.

---

## Scenarios

### 1. The nightly claims feed

A vendor drops a 2 GB CSV file of claims updates via SFTP every night at 1:00 AM. Business analysts need it queryable in the data warehouse by 8:00 AM. Data volume grows ~10% per year.

### 2. The telematics stream

A usage-based insurance pilot streams driving events (JSON, ~500 events/sec) from mobile apps. The pricing team wants near-real-time risk scores; the actuarial team wants full history for monthly analysis.

### 3. The legacy report

A 15-year-old on-prem application produces a monthly Excel report that three executives read. IT wants it "moved to the cloud" with minimal effort and cost. No transformation needed — just host it reliably.

### 4. The ML feature store

Data scientists need the last 3 years of cleaned policy and claims data, refreshed weekly, and accessible from Python notebooks to train a churn model.

---

## Worksheet

Complete one table per scenario assigned to your group.

| Question | Answer |
| :--- | :--- |
| Batch or streaming? Why? | |
| Service model (IaaS / PaaS / SaaS) | |
| Primary GCP service(s) | |
| AWS equivalent(s) | |
| Cost risk | |
| Security / PII consideration | |

---

## Deliverable

- Completed worksheet for each scenario your group tackled
- **5-minute group readout** — one scenario explained per member
- Reviewers: challenge at least one service choice per team ("Why not just use a VM?" / "Could this be streaming instead of batch?")

> [!TIP]
> You don't need to know the exact GCP/AWS service names yet — the translation table from today's slides is your cheat sheet. The goal is to reason about the right *capability*, then map it to the right service.

---

## Model answers (instructor reference — not for students)

| Scenario | Service model | GCP | AWS | Key cost risk |
| :--- | :--- | :--- | :--- | :--- |
| Claims feed | PaaS | GCS + Dataflow + BigQuery | S3 + Glue + Redshift/Athena | Full BQ scans if not partitioned |
| Telematics stream | PaaS | Pub/Sub + Dataflow + BigQuery | Kinesis + Glue + Redshift | Idle Dataflow workers between bursts |
| Legacy report | SaaS / IaaS | Cloud Storage (static hosting) or GCS bucket | S3 | Minimal — just storage cost |
| ML feature store | PaaS | BigQuery + Vertex AI Workbench | Redshift + SageMaker | Forgotten notebook instances |
