# Week 1 · Day 1 — Student Resources

> **AI-Free Zone (Weeks 1–4):** No Copilot, ChatGPT, or LLM-generated answers for today's activities. Read these sources and write your own reasoning by hand — the point is to build the mental model before you automate it.

These are external resources that complement today's content. You don't need to go through all of them — pick what's most relevant to where you want to dig deeper.

## Core Documentation

| Resource | Why it helps |
| :--- | :--- |
| [Fundamentals of Data Engineering (Reis & Housley)](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) | Ch. 1–3 map directly to today: the DE lifecycle, data generation, and storage |
| [Apache Parquet docs](https://parquet.apache.org/docs/) | The "why columnar wins" reference you'll reuse in Weeks 3 and 5 |
| [Confluent — Batch vs Real-Time Processing](https://www.confluent.io/learn/batch-vs-real-time-data-processing/) | Authoritative trade-off breakdown for the batch-vs-streaming decision |
| [dbt Labs — The Modern Data Stack](https://www.getdbt.com/blog/future-of-the-modern-data-stack) | High-level map of how the tools fit together and why ELT replaced ETL |
| [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | The actual source for your pipeline data — browse the data dictionary |

---

## What is data engineering?

**DataTalksClub — Data Engineering Zoomcamp (free, self-paced)**
https://github.com/DataTalksClub/data-engineering-zoomcamp
The most widely used free DE course online. Uses the same NYC Taxi dataset we use in this program. Module 1's architecture overview is a great companion to today's content. Skip Docker/Terraform sections — those are out of scope for this bootcamp.

**"What is a Data Engineer?" — Towards Data Science**
https://www.tealhq.com/career-paths/data-engineer
A readable overview of the DE role, how it differs from data analyst and data scientist, and what skills matter. Good if today's role comparison felt abstract.

**"The Rise of the Data Engineer" — Maxime Beauchemin (original essay)**
https://medium.com/free-code-camp/the-rise-of-the-data-engineer-91be18f1e603
The article that defined the DE title. Short, direct, historically important. Beauchemin also created Apache Airflow (which you'll see in Week 3).

---

## Data formats

**Apache Parquet — official documentation**
https://parquet.apache.org/docs/
Explains the columnar format in depth — row groups, column chunks, encodings, and why it matters for analytics workloads. Reference it when the "why columnar?" argument comes up in BigQuery (Week 3) and Spark (Week 5).

**"Comparing Data Formats: CSV, JSON, Parquet, Avro" — Databricks blog**
https://www.databricks.com/glossary/what-is-parquet
Concise comparison of the formats we covered today. Useful as a quick reference before Week 3.

---

## Batch vs streaming

**"Batch vs Stream Processing" — Confluent (makers of Kafka)**
https://www.confluent.io/learn/batch-vs-real-time-data-processing/
Clear breakdown of trade-offs, latency requirements, and when each model is appropriate. Confluent are the streaming experts — this is authoritative.

**"The Lambda Architecture" — Jay Kreps (original article)**
http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html
The original thinking behind Lambda architecture (batch + speed layers). Background reading for Day 5's architecture content.

---

## The modern data stack

**"The Modern Data Stack: Past, Present, and Future" — dbt Labs blog**
https://www.getdbt.com/blog/future-of-the-modern-data-stack
Written by the team that built dbt (Week 4). Good high-level map of how the tools fit together and why ELT replaced ETL as the dominant pattern.

**"Emerging Architectures for Modern Data Infrastructure" — a16z**
https://a16z.com/emerging-architectures-for-modern-data-infrastructure/
A deeper architecture survey from Andreessen Horowitz. Shows how the stack has evolved and where it's heading. Worth bookmarking and returning to after Week 4 when you have more context.

---

## The NYC Taxi dataset (your pipeline's data source)

**NYC TLC Trip Record Data**
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
The actual source for your pipeline data. Monthly Parquet files going back to 2009. Browse the data dictionary — understanding your source schema is a real DE skill.

**NYC Taxi Data Dictionary (Yellow Trips)**
https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
The field definitions for the yellow taxi dataset. Download and keep this — you'll refer to it in Weeks 3, 4, and 5.

---

## Book recommendation

**"Fundamentals of Data Engineering" — Joe Reis & Matt Housley (O'Reilly, 2022)**
The single best book on the DE discipline. Chapters 1–3 map directly to today's content (the lifecycle, data generation, storage). Available at most libraries and through O'Reilly Learning if The Hartford provides access.
https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/

---

## Lab Deliverable Checklist

| ✓ | Deliverable |
| :--- | :--- |
| ☐ | Activity 1: four analytics questions (one per type) with named data sources and data shapes |
| ☐ | Activity 1: 2–3 slides built; every group member has a speaking part |
| ☐ | Activity 2: structured / semi-structured / unstructured examples identified for car insurance |
| ☐ | Activity 2: one data flow traced end-to-end as a box-and-arrow diagram |
| ☐ | Activity 2: risk table completed — one risk each for quality, PII, latency, scale |
| ☐ | Activity 2: 5-minute "day in the life of this data" story prepared |
