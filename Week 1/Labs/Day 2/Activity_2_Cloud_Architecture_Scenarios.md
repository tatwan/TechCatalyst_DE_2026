# Week 1 · Day 2 · Activity 2: You're the Architect

**Duration:** 75 min  
**Difficulty:** Beginner  
**Format:** Groups of 3–4 (same teams as Day 1)  
**Prerequisites:** Day 2 cloud-fundamentals instruction and Activity 1's guided BigQuery Sandbox experience

## Objective

Use the cloud mental model from today to choose capabilities for a business problem, map them to GCP and AWS services, and defend the trade-offs. Exact service-name recall is not the goal.

## Plain-English Version

This is a **choose-the-right-tool** activity.

Your team gets a business problem, then answers:

1. What kind of problem is this: file landing, streaming events, simple hosting, analytics, or ML support?
2. What cloud capability does it need: storage, warehouse, streaming, scheduler, notebook, database, or something else?
3. What is that capability called in GCP and AWS?
4. What trade-off matters most: cost, speed, security, simplicity, or reliability?

You are not expected to design a perfect enterprise architecture. The goal is to practice translating a messy business ask into a small set of cloud capabilities.

## Connection to Activity 1

In BigQuery Sandbox, Google managed the infrastructure while you controlled the query and the amount of data requested. Use that experience as one concrete example while deciding which managed capabilities each scenario needs.

***

## The Scenario

Your team is advising The Hartford's data platform group. Each scenario below is a real type of problem data engineers face at an insurer. For each one, choose the right cloud services and defend your choices.

***

## Reference: One Mental Model, Two Clouds

| Capability | Google Cloud (primary) | AWS (secondary) |
| :--- | :--- | :--- |
| Object storage | Cloud Storage (GCS) | S3 |
| Warehouse / query | BigQuery | Redshift · Athena |
| Batch / stream pipelines | Dataflow (Apache Beam) | Glue (batch) · Kinesis Data Firehose (stream) |
| Messaging / events | Pub/Sub | SNS · SQS · Kinesis Data Streams |
| Managed Spark | Dataproc | EMR |
| Orchestration | Cloud Composer (Airflow) | MWAA (Airflow) |
| Simple scheduled trigger | Cloud Scheduler | EventBridge Scheduler |
| AI / ML platform | Vertex AI · Gemini Enterprise | SageMaker · Bedrock |
| Notebooks / interactive compute | Vertex AI Workbench | SageMaker Studio |

> *Learn the capability, not the logo; the concepts transfer across clouds.*

## Reference: Data Store Families

Use this when your scenario needs storage beyond "put the file in a bucket." Pick the family first, then map to a cloud service.

| Family | Use when | Google Cloud examples | AWS examples |
| :--- | :--- | :--- | :--- |
| OLTP relational | Apps need transactions, constraints, and strong schema | Cloud SQL · AlloyDB · Spanner | RDS · Aurora |
| OLAP warehouse | Analysts need large scans, joins, aggregates, BI | BigQuery · Snowflake | Redshift · Athena |
| Document | Records are nested or flexible JSON-like documents | Firestore | DocumentDB |
| Key-value / cache | The access pattern is fast lookup by key | Memorystore · Bigtable patterns | DynamoDB · ElastiCache |
| Wide-column | Very high-scale sparse rows or telemetry-style writes | Bigtable | Keyspaces |
| Graph | The question is about relationships or paths | Spanner Graph | Neptune |
| Time-series | The data is mostly measurements over time | BigQuery / Bigtable patterns | Timestream |
| Vector / search | The question is similarity, semantic search, or RAG | AlloyDB AI · BigQuery vector search | Aurora pgvector · OpenSearch |

***

## Scenarios

### 1. The Nightly Claims Feed

A vendor drops a 2 GB CSV file of claims updates via SFTP every night at 1:00 AM. Business analysts need it queryable in the data warehouse by 8:00 AM. Data volume grows ~10% per year.

### 2. The Telematics Stream

A usage-based insurance pilot streams driving events (JSON, ~500 events/sec) from mobile apps. The pricing team wants near-real-time risk scores; the actuarial team wants full history for monthly analysis.

### 3. The Legacy Report

A 15-year-old on-prem application produces a monthly Excel report that three executives read. IT wants it "moved to the cloud" with minimal effort and cost. No transformation needed, just host it reliably.

### 4. The Churn Training Dataset

Data scientists need the last 3 years of cleaned policy and claims data, refreshed weekly, and accessible from Python notebooks to train a churn model.

Do they need a dedicated feature store yet, or can cleaned warehouse data plus managed notebooks meet the stated requirement?

***

## Scenario Assignment and Team Roles

Each group chooses one **primary scenario**. If two groups want the same scenario, the instructor can either allow the overlap or ask one group to choose a different case so the readouts have more variety.

- With three groups, it is fine if one of the four scenarios is not selected.
- The instructor will cover any unselected scenario during the reveal.
- If you finish early, pick one unselected scenario and complete only the first three worksheet rows: batch or streaming, data format, and primary GCP services.

Assign these roles. With three people, combine **facilitator** and **skeptic**.

| Role | Responsibility |
| :--- | :--- |
| Facilitator | Keeps the group focused on business requirements and time |
| Recorder | Completes the worksheet |
| Service mapper | Uses the GCP↔AWS reference to map capabilities to products |
| Skeptic | Challenges cost, security, and unnecessary complexity |

## Timing

| Time | Task |
| ---: | :--- |
| 5 min | Choose a scenario and assign team roles |
| 25 min | Complete the worksheet |
| 10 min | Prepare the five-minute readout |
| 20 min | Group readouts and peer challenges |
| 10 min | Instructor reveal covering all four scenarios |
| 5 min | Debrief and success check |

## Worksheet

Complete one table for your chosen primary scenario.

| Question | Answer |
| :--- | :--- |
| Batch or streaming? Why? | |
| What data format is involved? (CSV, JSON, Parquet, etc.) | |
| Primary GCP service(s) | |
| AWS equivalent(s) | |
| Which data-store family is this? (OLTP, OLAP, object store, document, key-value, etc.) | |
| For each service, what is closest: IaaS, PaaS/managed service, or SaaS? What does the provider manage? | |
| How is the pipeline triggered or scheduled? | |
| Cost risk | |
| Security / PII consideration | |
| One alternative you rejected, and why | |

***

## Quick-Reference Aids

> [!TIP]
> **Batch vs. Streaming Decision Aid**
>
> Ask yourself:
> - Does the business need results *within seconds or minutes*? → **Streaming**
> - Can it wait *hours or overnight*? → **Batch**
> - Does it need *both* (real-time + historical)? → Consider separate real-time and batch paths. You will learn the formal architecture patterns on Day 5.

> [!TIP]
> **Service Model Quick Reference**
>
> | Model | Who manages the infra? | Hartford example |
> | :--- | :--- | :--- |
> | **IaaS** | You manage OS, runtime, scaling | EC2 VM you configure yourself |
> | **PaaS** | Cloud manages runtime; you manage code & data | BigQuery, Dataflow, Glue |
> | **SaaS** | Cloud manages everything | A vendor-hosted reporting tool |

> [!NOTE]
> **PII in Insurance Data**
>
> Claims data commonly contains: full name, date of birth, SSN, medical diagnosis codes, home address, and vehicle data. Driving event streams may contain precise GPS coordinates.
>
> Ask yourself: *At which layer do you mask or restrict this: ingestion, storage, or query time?*

***

## Deliverable

- Completed worksheet for your chosen primary scenario
- **5-minute group readout** for your primary scenario; every member must contribute
- Reviewers: challenge at least one service choice per team

> [!TIP]
> **Your 5-Minute Readout Structure**
>
> 1. Scenario in one sentence: what's the core problem? *(30 sec)*
> 2. Batch or streaming: your decision and why *(45 sec)*
> 3. GCP + AWS services chosen, with a one sentence defense *(90 sec)*
> 4. Biggest cost or security risk *(30 sec)*
> 5. Take one challenge question from the room *(60 sec)*

**Reviewer Challenge Bank (one per scenario):**

| Scenario | Challenge Question |
| :--- | :--- |
| Claims feed | "What happens if the vendor delivers the file at 6 AM instead of 1 AM?" |
| Telematics stream | "Why not just batch the events every 5 minutes instead?" |
| Legacy report | "How do executives actually access the file: do they need a URL or an email?" |
| Churn training dataset | "Who pays for the notebook when a data scientist forgets to shut it down?" |

> [!TIP]
> You don't need to know the exact GCP/AWS service names yet; the translation table above is your cheat sheet. The goal is to reason about the right *capability*, then map it to the right service.

## Success Criteria

Your team is finished when it can check every item:

- [ ] We made one defensible batch, streaming, or dual-path decision.
- [ ] Our selected services are connected in execution order.
- [ ] We identified how the work starts: event, file arrival, or schedule.
- [ ] We classified what the provider manages for each selected service.
- [ ] We named one realistic cost risk and one security/PII control.
- [ ] We rejected one plausible alternative and explained why.
- [ ] Every member has a speaking role in the five-minute readout.

## Instructor Notes

### Expected Direction (Reveal After the Readouts)

These are defensible starting points, not single correct answers. Reward reasoning from requirements over exact product names.

| Scenario | Likely direction | Key teaching point |
| :--- | :--- | :--- |
| Nightly claims feed | SFTP landing → GCS/S3 → scheduled validation/transformation → BigQuery/Redshift | Batch meets the 8:00 AM requirement; plan for late and duplicate files |
| Telematics stream | Pub/Sub/Kinesis → streaming processing → operational scoring path plus historical warehouse storage | Immediate scoring and monthly analysis require different serving needs |
| Legacy report | Secure GCS/S3 object access or an existing managed document/reporting service | Do not build a pipeline when reliable file distribution satisfies the requirement |
| Churn training dataset | Weekly cleaned warehouse data → managed Python notebook environment | A dedicated feature store is not justified unless reuse, online serving, or consistency requirements appear |

### Debrief

Ask:

1. Where did a team add a service that the requirements did not justify?
2. Which requirement most strongly determined batch versus streaming?
3. How did the BigQuery experience help you reason about provider-managed infrastructure and usage cost?
