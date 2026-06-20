# TechCatalyst DE 2026: Proposed Curriculum

This is an 8-week Data Engineering Bootcamp curriculum for **TechCatalyst DE 2026**.

![image-20240612110851319](images/image-20240612110851319.png)

This hands-on program is designed for fresh graduates and junior data engineers (1–2 years of experience). The core objective is to prepare students for production-grade roles by modeling a single, continuous, real-world industry project—the **Large-Scale Data Ingestion & Analytics Pipeline**—thoughtfully mapped across the entire course. 

The 2026 curriculum shifts primary cloud focus to **Google Cloud Platform (GCP)** (with AWS as a secondary conceptual overlay), introduces modern data stack standards with **Snowflake** and **dbt**, integrates **AI-native features** (Cortex AI, Gemini API, and Vertex AI), incorporates **Big Data processing with PySpark & Databricks**, and establishes a strict, scaffolded developer progression to teach solid coding practices before introducing AI coding assistants like **GitHub Copilot**.

---

## Strategic Pedagogy: The Coding & AI Progression

To address the modern challenge where new engineers struggle to code due to over-reliance on autocomplete engines, this curriculum enforces a strict **"AI-Free Zone"** for the first four weeks:

1. **Weeks 1–4 (Foundations By Hand):** Students write Python, SQL, dbt, and Git commands from scratch. No GitHub Copilot or LLM-generated code is permitted. This builds syntax familiarity, debugging resilience, and a solid understanding of execution errors.
2. **Week 5 (Big Data & PySpark):** Students scale their coding skills using PySpark and Databricks as a learning environment, before transitioning to deploying production jobs on managed cloud clusters (GCP Dataproc and AWS EMR).
3. **Week 6 (AI Integration & Copilot):** **GitHub Copilot** is formally introduced. The focus is not just on code generation, but on **Prompt/Context Engineering** and **Rigorous Code Review/Validation workflows**. Students are trained to act as "code editors" who must verify correctness rather than blindly accepting AI suggestions.

---

## Longitudinal Project Thread: Large-Scale Ingestion & Analytics (e.g., NYC Taxi Data)

Instead of disjointed daily exercises, students work on a single continuous pipeline that processes a high-volume public dataset (such as the **NYC City Taxi Parquet dataset**, containing millions of rows, or a comparable client-specific dataset):
* **Week 1:** Design the conceptual lakehouse/warehouse pipeline architecture.
* **Week 2:** Pull and clean raw metadata records from a REST API and land them in GCS using Python.
* **Week 3:** Ingest event streaming and batch data via Pub/Sub and Dataflow, loading them into BigQuery tables, and apply PII masking.
* **Week 4:** Move data to Snowflake, run analytical SQL queries, write dbt models, write assertions to test quality, and set up a GitHub Actions CI/CD workflow to validate the code.
* **Week 5:** Scale processing using PySpark to transform large Parquet files, starting in Databricks and then executing batch jobs on GCP Dataproc and AWS EMR.
* **Week 6:** Call Vertex AI and the Gemini API to auto-classify and tag unstructured feedback or comments.
* **Week 7:** Connect interactive data applications (Streamlit) and enterprise BI dashboards (client's choice) to the cleaned data.
* **Week 8:** The Capstone. Teams integrate and deploy this end-to-end pipeline in a production-ready state.

---

## Week-by-Week Curriculum Breakdown

---

### Week 1 — Data & Cloud Foundations

**Theme:** Set the stage — what is data engineering, why does cloud matter, and how do we set up?

| Day | Topic | Details / Labs |
| :--- | :--- | :--- |
| **Day 1** | Data Primer & DE Roles | Types of data (structured, semi-structured, unstructured), batch vs. streaming concepts, the Modern Data Stack, and roles in DE. |
| **Day 2** | Cloud Fundamentals | Core concepts: IaaS vs. PaaS vs. SaaS. Conceptual comparison of GCP vs. AWS services. IAM basics and billing management. |
| **Day 3** | Environment Setup | Setting up VS Code and GitHub Codespaces. Installing Python, virtual environments (`venv`), pip, and Git basics. Setting up cloud accounts. |
| **Day 4** | Hands-On Cloud Storage | Lab: Spin up a GCP project, navigate the console, create and configure a Google Cloud Storage (GCS) bucket, and compare it conceptually to AWS S3. |
| **Day 5** | Architecture & Pipeline Thread | **Data Pipeline Introduction:** Overview of the NYC Taxi (or chosen client) dataset. Lab: Design a conceptual data flow diagram using Draw.io showing raw data landing in GCS and loading into BigQuery. |

**Weekly Deliverable:** Conceptual data pipeline design document and architecture diagram for the high-volume data use case.

---

### Week 2 — Developer Foundations & Python Coding (AI-Free Zone)

**Theme:** Developer foundations — how data engineers write, version, and execute code by hand.

| Day | Topic | Details / Labs |
| :--- | :--- | :--- |
| **Day 1** | Data Architecture | Core architectures: Batch vs. Streaming, Lambda vs. Kappa, and the Medallion Architecture (Bronze, Silver, Gold). |
| **Day 2** | Linux CLI & Git Collaboration | Shell basics: filesystem commands, pipes (`\|`), searching (`grep`), cron. Git command line: `git init/clone/commit/push`, branching, PRs, and resolving conflicts. |
| **Day 3** | Python Foundations for DE | Core Python coding: variables, standard data types, collections (lists, dicts, tuples, sets), control flow (loops, conditionals), and custom functions. |
| **Day 4** | Intermediate Python & File I/O | Object-Oriented Programming (OOP) basics (classes/methods for data models), error handling, reading/writing CSV/JSON files, and making API requests using the `requests` library. |
| **Day 5** | Pandas & Polars for DE | Intro to pandas DataFrames (reading files, cleaning, filtering, joins, aggregations). Lab: Land data in GCS using Python. 30-min comparison of pandas vs. Polars (syntax and speed). Brief demo of AWS serverless concepts (Lambda, S3 triggers) as a secondary cloud overview. |

**Weekly Deliverable:** A hand-written Python script that pulls mock metadata from a public API, performs basic cleaning in pandas, and uploads it to a GCP GCS bucket.

---

### Week 3 — Modern Data Warehousing & SQL (GCP-First)

**Theme:** Storage and querying with GCP as the primary workhorse.

| Day | Topic | Details / Labs |
| :--- | :--- | :--- |
| **Day 1** | Modern Data Warehousing | ETL vs. ELT, data lakes vs. data warehouses vs. lakehouses. Schema design: star schemas, snowflake schemas, and columnar storage. |
| **Day 2** | GCP BigQuery Foundations | BQ Architecture: storage vs. compute decoupling. Managing datasets and tables (internal vs. external), partitioning, clustering, and console query execution. |
| **Day 3** | SQL Primer (BigQuery) | Writing queries *by hand*: SELECT, WHERE, JOINs, GROUP BY, aggregations, and HAVING. Querying the high-volume data loaded into BigQuery. |
| **Day 4** | Ingestion & Batch Pipelines | Event streaming vs. batch ingestion. Lab: Spin up GCP Pub/Sub topics. Introduction to Apache Beam concepts and running a GCP Dataflow batch pipeline (loading GCS files into BigQuery). |
| **Day 5** | Orchestration & GCP Governance | Core orchestration concepts. Lab: Introduction to Cloud Composer (Airflow) DAGs. **GCP Security & Governance:** IAM roles, Dataplex cataloging, and PII/PHI column-level masking in BigQuery. |

**Weekly Deliverable:** An end-to-end mini-pipeline: Pub/Sub → Dataflow (scaffolded) → BigQuery, with SQL queries summarizing the loaded dataset, and security policies applied.

---

### Week 4 — Snowflake, dbt & Advanced SQL

**Theme:** The analytical warehouse layer — transformations, advanced SQL, and data modeling.

| Day | Topic | Details / Labs |
| :--- | :--- | :--- |
| **Day 1** | Snowflake Architecture | Introduction to Snowflake: decoupled storage and compute, virtual warehouses, databases, schemas, and RBAC roles. **Cost Optimization:** Warehouse sizing, auto-suspend, and table types (permanent, transient, temporary). |
| **Day 2** | Advanced SQL & Performance | Analytical SQL: window functions (`ROW_NUMBER`, `LEAD`/`LAG`, running totals), CTEs, and query performance tuning (pruning, clustering, and monitoring query profile costs) in BigQuery & Snowflake. |
| **Day 3** | dbt Core & Integration | Introduction to dbt (Data Build Tool). Lab: Set up a local dbt project, define sources and models, write transformations on Snowflake data, and configure basic tests (unique, not_null, accepted_values). |
| **Day 4** | Advanced dbt & CI/CD | Advanced dbt modeling: incremental models, custom macros, seeds, and snapshots. Lab: Build a **GitHub Actions CI/CD workflow** that automatically runs and tests dbt models on pull requests. |
| **Day 5** | Snowflake GenAI & Governance | Cortex LLM functions (COMPLETE, SUMMARIZE, TRANSLATE) and Document AI. Lab: Build an LLM-powered data enrichment pipeline to summarize text columns. **Snowflake Governance:** column-level masking policies, tagging sensitive data. |

**Weekly Deliverable:** A dbt project on Snowflake with comprehensive data tests, a GitHub Actions CI/CD validation workflow, and a Cortex LLM-enriched model.

---

### Week 5 — Big Data & PySpark ETL (Databricks, Dataproc & AWS EMR)

**Theme:** Distributed data processing, lakehouse formats, and deploying production Spark jobs.

> [!NOTE]
> **Pedagogical Strategy:** We use **Databricks (Community Edition)** as a zero-config, interactive environment for learning core Spark concepts and PySpark syntax. Once students have mastered these basics, we transition to deploying their code as production batch jobs on managed cloud clusters: **GCP Dataproc** (primary cloud) and **AWS EMR** (secondary cloud).

| Day | Topic | Details / Labs |
| :--- | :--- | :--- |
| **Day 1** | Big Data & Spark Foundations | Distributed computing concepts, Spark cluster architecture (Driver vs. Executor), Spark Session, RDDs, and Spark DataFrames. |
| **Day 2** | Databricks for Learning | Databricks Community Edition setup, cluster profiles, notebooks, and writing basic PySpark DataFrame transformations (select, filter, basic functions). |
| **Day 3** | PySpark & Lakehouse Formats | Complex transformations (joins, aggregations, window functions). Introduction to modern lakehouse formats: Delta Lake and Apache Iceberg (ACID transactions, time travel, schema evolution). |
| **Day 4** | Deploying on GCP Dataproc | **Production Deployment (GCP):** Packaging PySpark code into standalone scripts. Lab: Upload PySpark scripts and data to GCS, spin up a GCP Dataproc cluster, submit the Spark job, and monitor execution. |
| **Day 5** | Deploying on AWS EMR (Secondary) | **Production Deployment (AWS):** Translating the workflow to the secondary cloud. Lab: Upload scripts to S3, configure and submit jobs to an **AWS EMR (Elastic MapReduce)** cluster. Overview of Dataproc Serverless. |

**Weekly Deliverable:** A PySpark ETL script developed in Databricks, packaged, and executed as a production batch job on a GCP Dataproc cluster, reading from GCS and writing to a Delta/Iceberg table.

---

### Week 6 — NLP, LLMs, GenAI & GitHub Copilot

**Theme:** AI engineering and introducing AI coding assistants to accelerate development.

| Day | Topic | Details / Labs |
| :--- | :--- | :--- |
| **Day 1** | GenAI Foundations | Landscape: Generative AI ecosystem, Foundation Models, LLM architectures, tokenization, embeddings, and basic prompt engineering. |
| **Day 2** | Python API Integration | Programmatic AI: accessing LLMs via REST APIs, google-generativeai SDK, and LangChain high-level concepts. |
| **Day 3** | GCP Vertex AI (MLOps) | Vertex AI platform overview. Tie to pipeline: DE's role in ML (feeding clean datasets to models, deploying AutoML models, and consuming predictive outputs, e.g., taxi demand forecasting). |
| **Day 4** | Applied NLP on GCP | Gemini API for text generation, classification, and embeddings. Lab: Classify comments or notes and extract metadata using Vertex AI Gemini API. |
| **Day 5** | GitHub Copilot for DE | **Introducing Copilot:** Setup, inline suggestions, Copilot Chat, and Agent Mode. Best practices: **Prompt/Context Engineering for DE** and **Rigorous Code Review/Validation workflows** (avoiding AI dependency bugs). |

**Weekly Deliverable:** An LLM-powered pipeline component (built using Copilot assistance but reviewed/debugged by hand) that auto-tags records based on Gemini classification.

---

### Week 7 — BI, Visualization & Python Data Apps

**Theme:** From data to decisions — business intelligence dashboards and programmatic data apps.

> [!NOTE]
> **Client Tool Selection:** Days 2 and 3 are designated as client choice days. The client will select **two BI tools** to focus on from the following options: **Looker** (Primary GCP), **Tableau** (industry standard), **Strategy** (formerly MicroStrategy), or **ThoughtSpot** (AI-powered analytics).

| Day | Topic | Details / Labs |
| :--- | :--- | :--- |
| **Day 1** | Storytelling & Streamlit Data Apps | Principles of data storytelling and dashboard layout. **Python Data Viz:** Introduction to **Streamlit** (widgets, state management, caching). Lab: Connect Streamlit to BigQuery/Snowflake and build an interactive data app with filters and plots. |
| **Day 2** | BI Tool Focus — Day 1 | Tableau, Thoughtspot, Looker |
| **Day 3** | BI Tool Focus — Day 2 | Tableau, Thoughtspot, Looker |
| **Day 4** | Comparative BI Architecture | Architectural review: self-service reporting models, semantic layers, data caching/scheduling, and enterprise access controls. |
| **Day 5** | Capstone Preparation | **Capstone Kickoff:** Dataset reveal (e.g. NYC Taxi or client-specific data), project brief, team formation, and initial exploratory analysis. |

**Weekly Deliverable:** An interactive Python data app (Streamlit) and an enterprise BI dashboard (Client's choice) connected to BigQuery or Snowflake.

---

### Week 8 — End-to-End Capstone

**Theme:** Integrating everything — GCP ingestion, Snowflake transformation, BI, PySpark, and GenAI.

* **Day 1 — Capstone Kickoff & Architecture:** Teams present and refine their end-to-end architecture diagrams. Roles and sub-team tasks are assigned.
* **Day 2 — Ingestion Sprint:** Deploying the GCP Ingestion layer (GCS → Dataflow → BigQuery) or PySpark ETL pipeline. *Note: Students are provided with a pre-built Dataflow/PySpark template to customize, focusing on integration rather than writing pipelines from scratch.*
* **Day 3 — Transformation & Governance Sprint:** Snowflake loading, dbt modeling, data quality assertions (`dbt test`), PII masking rules, and Dataplex lineage tagging.
* **Day 4 — Analytics, BI & Apps Integration:** Teams split into sub-teams:
  * *Sub-team A:* Cortex AI/Gemini API enrichment of unstructured text.
  * *Sub-team B:* Looker/Tableau/Strategy dashboards and Streamlit data apps.
  * *Integration:* Merging the sub-teams' work at the end of the day.
* **Day 5 — Final Presentations:** End-to-end demo, architecture walkthrough, and team retrospective.

**Capstone Deliverable:** A fully operational, CI/CD-deployed data analytics pipeline combining GCP ingestion, Snowflake/dbt modeling, PySpark processing, AI-enriched metadata, and a Looker/Tableau/Strategy dashboard or Streamlit app.

---

## Technology Stack Summary

| Category | Primary (GCP-First) | Secondary (AWS) |
| :--- | :--- | :--- |
| **Storage** | Google Cloud Storage (GCS) | Amazon S3 |
| **Warehouse** | **BigQuery** + Snowflake | Amazon Redshift |
| **Big Data / Spark** | **Databricks**, **GCP Dataproc** | **AWS EMR** |
| **Pipelines** | **GCP Dataflow, Pub/Sub** | AWS Glue |
| **AI/ML Platform** | **Vertex AI, Snowflake Cortex AI** | AWS SageMaker, Amazon Bedrock |
| **Orchestration** | **dbt** + GitHub Actions + Cloud Composer | — |
| **BI / Viz / Apps** | **Looker**, Tableau, Strategy, ThoughtSpot, **Streamlit** | — |
| **Coding & AI** | **GitHub Copilot**, **Gemini API** | — |
| **Languages** | Python, SQL, Bash (Linux), PySpark | — |
