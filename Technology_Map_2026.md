# TechCatalyst DE 2026 — Technology Map

**Program:** June 22 – August 14, 2026 · 8 weeks · ~10 Hartford interns  
**AI-Free Zone:** Weeks 1–4 (no AI coding tools until Week 6)  
**Holiday:** July 3 (Week 2 Day 5 cancelled — Week 2 is 4 days)

---

## Part 1 — Week × Day Grid

| Week | Day | Title | Technologies Introduced / Used |
|------|-----|-------|-------------------------------|
| **1** | D1 | Data Engineering Foundations | Concepts only: batch vs streaming, modern data stack, DE vs DA/DS roles |
| **1** | D2 | Cloud Fundamentals | **GCP** (overview), **AWS** (overview), IAM (principals/roles/resources), billing budgets; **BigQuery Sandbox guided preview** using provided GoogleSQL (not formal SQL instruction) |
| **1** | D3 | Developer Environment Setup | **GitHub**, **GitHub Codespaces**, **VS Code**, Git (branch/commit/PR), Python venv |
| **1** | D4 | Cloud Object Storage | **GCS** (buckets, storage classes, lifecycle), **S3** (comparison), `gcloud storage` CLI, `aws s3` CLI |
| **1** | D5 | Data Architectures & Pipeline Design | **Draw.io** (architecture diagrams); Lambda, Kappa, Medallion patterns |
| **2** | D1 | Linux CLI & Git Collaboration | Linux shell (bash, cron, pipes, redirects), Git (branching, merge conflicts, PRs) |
| **2** | D2 | Python Foundations | **Python** (types, collections, control flow, functions, docstrings) |
| **2** | D3 | Intermediate Python & APIs | Python (OOP, error handling, file I/O), **requests** library, REST APIs, `argparse`, `logging` |
| **2** | D4 | Pandas, Polars & Shipping to GCS | **pandas**, **Polars**, GCS upload via Python (`google-cloud-storage`) |
| **3** | D1 | Modern Data Warehousing | Concepts: ETL vs ELT, star vs snowflake schema, OLAP vs OLTP, lake/warehouse/lakehouse |
| **3** | D2 | BigQuery Foundations | **BigQuery** (storage/compute separation, partitioning, clustering, authorized views, column masking), GoogleSQL |
| **3** | D3 | SQL on BigQuery | **BigQuery** SQL (JOINs, GROUP BY, HAVING, subqueries, window functions), GoogleSQL (not legacy SQL) |
| **3** | D4 | Pub/Sub & Dataflow | **Pub/Sub**, **Apache Beam**, **Dataflow** (batch pipeline: GCS → BigQuery) |
| **3** | D5 | Orchestration & Governance | **Cloud Composer** (Airflow DAGs), **Knowledge Catalog** (policy tags, data lineage), BigQuery PII masking, IAM |
| **4** | D1 | Snowflake Architecture | **Snowflake** (three-layer architecture, virtual warehouses, stages, COPY INTO, RBAC, Time Travel, zero-copy clones) |
| **4** | D2 | Advanced SQL & Performance | **Snowflake** SQL (window functions, QUALIFY, LAG/LEAD, frames, Query Profile), **BigQuery** SQL (same patterns) |
| **4** | D3 | dbt Fundamentals | **dbt** (Fusion engine, VS Code extension, sources, models, ref, materializations, tests, YAML), dbt Projects on Snowflake |
| **4** | D4 | Advanced dbt & CI/CD | **dbt** (incremental models, snapshots, Jinja macros), **GitHub Actions** (CI/CD pipelines) |
| **4** | D5 | Cortex AI & Snowflake Governance | **Snowflake Cortex AISQL** (COMPLETE, CLASSIFY, SUMMARIZE), Snowflake masking policies, tag-based masking |
| **5** | D1 | Distributed Computing & Spark | **Apache Spark** concepts (driver/executors, DAG, lazy evaluation, shuffle, DataFrames) |
| **5** | D2 | Databricks & PySpark Essentials | **Databricks Free Edition** (serverless), **PySpark** (display(), chaining, groupBy/agg/alias(), SQL interop, explain()) |
| **5** | D3 | Advanced PySpark & Lakehouse Formats | **PySpark** (broadcast joins, window functions, dedup), **Delta Lake** (ACID, MERGE, time travel, schema evolution), **Apache Iceberg** (conceptual + S3 Tables mention) |
| **5** | D4 | Production Spark on Databricks | **Databricks Free Edition** (Jobs / Lakeflow), `spark-submit` concepts, `argparse`, `logging`; **Dataproc** (GCP — conceptual comparison), **AWS EMR** (conceptual mention) |
| **5** | D5 | Choosing Your Engine | **Databricks Free Edition** (hands-on), engine decision map: **pandas**, **Polars**, **BigQuery**, **Snowflake**, **Databricks**, **Dataproc** (conceptual), **AWS EMR** (conceptual), **Dataproc Serverless** (conceptual) |
| **6** | D1 | GenAI Foundations | **Google AI Studio**, **Gemini** (LLMs, tokens, context windows, embeddings, temperature), prompt engineering concepts |
| **6** | D2 | Programmatic LLMs | **google-genai SDK**, **Gemini API** (structured output, generation controls, rate limits, usage_metadata), **Pydantic v2**, LangChain (conceptual map) |
| **6** | D3 | Vertex AI & the DE Role in ML | **Vertex AI** / Gemini Enterprise Agent Platform, ADC + IAM service accounts, **BigQuery ML** (remote models), **AutoML** (tabular), **Cloud Logging** (audit trail) |
| **6** | D4 | Applied NLP & BigQuery AI | **BigQuery AI functions** (`AI.GENERATE`, `ML.GENERATE_TEXT`, `VECTOR_SEARCH`, `ML.GENERATE_EMBEDDING`), **BigQuery ML** |
| **6** | D5 | GitHub Copilot for Data Engineers | **GitHub Copilot** (inline, chat, agent mode), **BigQuery Data Engineering Agent** (NL → pipeline) |
| **7** | D1 | Data Storytelling & Streamlit | **Streamlit** (data apps on BigQuery/Snowflake) |
| **7** | D2 | Tableau | **Tableau** Desktop/Online — calculated fields, LOD expressions, dashboards connected to BigQuery/Snowflake |
| **7** | D3 | ThoughtSpot | **ThoughtSpot** — AI search analytics, SpotIQ auto-insights, Liveboards |
| **7** | D4 | BI Architecture + Looker (optional) | Semantic layers, caching, access control; **Looker** intro (time-permitting — free via Google account) |
| **7** | D5 | Capstone Kickoff | NYC Taxi dataset reveal, EDA, team roles, architecture planning |
| **8** | D1 | Capstone — Architecture & Kickoff | All platforms (architecture review, no new instruction) |
| **8** | D2 | Capstone — Ingestion Sprint | **GCS**, **PySpark**, **Dataflow** → BigQuery / Snowflake |
| **8** | D3 | Capstone — Transformation & Governance Sprint | **Snowflake**, **dbt**, **Knowledge Catalog**, BigQuery PII masking |
| **8** | D4 | Capstone — AI + BI Integration Sprint | **Snowflake Cortex** / **Gemini** (google-genai / Vertex AI), **Tableau**, **Streamlit** |
| **8** | D5 | Final Presentations | All platforms (live demo + retrospective) |

---

## Part 2 — Technology Index

Organized by platform / tool family. ★ = first introduced.

### Python & Libraries

| Technology | First Introduced | Also Used |
|-----------|-----------------|-----------|
| **Python** (core language) | W2D2 ★ | W2D3, W2D4, W5D2–D4, W6D2–D3 |
| **requests** (REST API client) | W2D3 ★ | W6D2 (google-genai replaces it) |
| **argparse** | W2D3 ★ | W5D4 (etl_trips.py) |
| **logging** | W2D3 ★ | W5D4, W6D2 |
| **pandas** | W2D4 ★ | W5D5 (engine decision map) |
| **Polars** | W2D4 ★ | W5D5 (engine decision map) |
| **Pydantic v2** | W6D2 ★ | |
| **google-cloud-storage** (Python) | W2D4 ★ | W5D4 |
| **google-genai SDK** | W6D2 ★ | W6D3, W6D4, W8D4 |

### Google Cloud Platform (GCP)

| Technology | First Introduced | Also Used |
|-----------|-----------------|-----------|
| **GCP** (platform overview) | W1D2 ★ | throughout |
| **IAM** (GCP) | W1D2 ★ | W3D5, W6D3 |
| **GCS** (Google Cloud Storage) | W1D4 ★ | W2D4, W3D4, W5D4, W8D2 |
| **BigQuery** | W1D2 guided preview ★ | W3D2–D3 formal instruction, W3D5, W4D2, W6D3–D4, W8D3 |
| **GoogleSQL** | W1D2 copy/paste preview ★ | W3D2–D3 formal instruction, W4D2, W6D4 |
| **Pub/Sub** | W3D4 ★ | |
| **Apache Beam** | W3D4 ★ | |
| **Dataflow** | W3D4 ★ | W8D2 |
| **Cloud Composer** (Airflow) | W3D5 ★ | |
| **Knowledge Catalog** (formerly Dataplex) | W3D5 ★ | W8D3 |
| **Vertex AI** / Gemini Enterprise Agent Platform | W6D3 ★ | W8D4 |
| **BigQuery ML** | W6D3 ★ | W6D4 |
| **BigQuery AI functions** (`AI.GENERATE`, `VECTOR_SEARCH`) | W6D4 ★ | |
| **BigQuery Data Engineering Agent** | W6D5 ★ | |
| **AutoML** (tabular) | W6D3 ★ | |
| **Cloud Logging** | W6D3 ★ | |
| **Google AI Studio** | W6D1 ★ | |
| **Gemini** (models / API) | W6D1 ★ | W6D2, W6D3, W6D4, W8D4 |

### Amazon Web Services (AWS)

| Technology | First Introduced | Also Used |
|-----------|-----------------|-----------|
| **AWS** (platform overview) | W1D2 ★ | |
| **S3** | W1D4 ★ | W8D2 |
| **AWS EMR** | W5D5 ★ (conceptual) | W8D2 (conceptual) |

### Snowflake

| Technology | First Introduced | Also Used |
|-----------|-----------------|-----------|
| **Snowflake** (architecture, warehouses) | W4D1 ★ | W4D2, W4D3, W4D5, W8D3 |
| **Snowflake Cortex AISQL** | W4D5 ★ | W8D4 |
| **Time Travel** | W4D1 ★ | |
| **Zero-copy clones** | W4D1 ★ | |

### dbt

| Technology | First Introduced | Also Used |
|-----------|-----------------|-----------|
| **dbt** (Fusion engine + VS Code ext) | W4D3 ★ | W4D4, W8D3 |
| **dbt models / materializations** | W4D3 ★ | W4D4 |
| **dbt incremental / snapshots** | W4D4 ★ | |
| **dbt Jinja macros** | W4D4 ★ | |
| **dbt Projects on Snowflake** | W4D3 ★ (demo) | |

### Apache Spark & Databricks

| Technology | First Introduced | Also Used |
|-----------|-----------------|-----------|
| **Apache Spark** (concepts) | W5D1 ★ | W5D2–D5 |
| **PySpark** | W5D2 ★ | W5D3, W5D4, W8D2 |
| **Databricks Free Edition** (serverless) | W5D2 ★ | W5D3, W5D4, W5D5, W8D2 |
| **Databricks Jobs / Lakeflow** | W5D4 ★ | |
| **Delta Lake** | W5D3 ★ | W8D2 |
| **Apache Iceberg** | W5D3 ★ (conceptual) | |
| **Dataproc** (GCP) | W5D4 ★ (conceptual) | W5D5 (conceptual) |
| **Dataproc Serverless** | W5D5 ★ (conceptual) | |

### Developer Tooling

| Technology | First Introduced | Also Used |
|-----------|-----------------|-----------|
| **Git** | W1D3 ★ | W2D1, throughout |
| **GitHub** | W1D3 ★ | throughout |
| **GitHub Codespaces** | W1D3 ★ | throughout |
| **VS Code** | W1D3 ★ | W4D3 (dbt ext), W6D5 |
| **GitHub Actions** | W4D4 ★ | |
| **GitHub Copilot** | W6D5 ★ | W7–W8 |
| **Draw.io** | W1D5 ★ | W7D4, W8D1 |
| **Linux CLI / bash** | W2D1 ★ | W5D4 |

### BI & Data Apps

| Technology | First Introduced | Also Used |
|-----------|-----------------|-----------|
| **Streamlit** | W7D1 ★ | W8D4 |
| **Tableau** | W7D2 ★ | W8D4 |
| **ThoughtSpot** | W7D3 ★ | |
| **Looker** | W7D4 ★ (optional) | |

---

## Part 3 — "Under the Hood" View: The Spark Family

> All of the following platforms run **Apache Spark**. The PySpark code you write is portable across all of them. The platform choice is an infrastructure, governance, and cost decision — not a code decision.

| Platform | Who manages it | Auth model | When we use it |
|----------|---------------|------------|----------------|
| **Databricks Free Edition** | Databricks (serverless) | Databricks account | W5D2–D5 hands-on (all labs) |
| **Google Dataproc** | GCP (managed cluster) | IAM / service account | W5D4–D5 conceptual comparison |
| **Dataproc Serverless** | GCP (no cluster) | IAM / service account | W5D5 conceptual |
| **AWS EMR** | AWS (managed cluster) | IAM / EC2 role | W5D5 conceptual comparison |
| **AWS EMR Serverless** | AWS (no cluster) | IAM / execution role | W5D5 conceptual |

**The mental model:** Your `etl_trips.py` script runs on all five without code changes. Only the submission command and the path prefixes (`dbfs://`, `gs://`, `s3://`) differ. Databricks is the platform of the Spark creators — it provides the richest managed experience at zero infrastructure cost with Free Edition.

---

## Part 4 — Accuracy Rules Quick Reference

| Rule | Detail |
|------|--------|
| BigQuery SQL | **GoogleSQL only** — Legacy SQL availability is restricted for many projects after June 1, 2026 |
| Databricks tier | **Free Edition (serverless)** — never "Community Edition" |
| Knowledge Catalog | Renamed from Dataplex, April 2026 |
| GCP AI SDK | **`google-genai`** only — `google-generativeai` is deprecated |
| AI-Free Zone | **Weeks 1–4** — no AI coding tools (Copilot, etc.) until Week 6 |
| dbt engine | **Fusion engine** + VS Code extension |
