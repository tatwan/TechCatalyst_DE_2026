# W1D4 Data at Rest Redesign

## Objective

Redesign Week 1 Day 4 from a narrow Google Cloud Storage product tour into a coherent beginner-level lesson on the data-at-rest layer of a data engineering system.

The revised day must connect the cloud foundations from Days 1–3 to the pipeline work on Day 5 while giving learners enough architectural vocabulary to explain why object storage, file layout, data lifecycle, access controls, and query engines belong together.

The existing source deck remains unchanged. Deliver the revised deck as:

`Week 1/Slides/W1D4 - Data at Rest - Updated.pptx`

Revise the supporting Day 4 instructor guide and labs in place where needed. Add one short required query-in-place activity rather than turning the existing SQL-heavy optional activities into required work.

## Audience and Scope

- Audience: fresh graduates and junior data engineers in Week 1.
- Duration: one instructional day, approximately 8:30 AM–5:00 PM.
- Primary hands-on platform: Google Cloud Storage using the course-managed GCP environment.
- Cloud comparison: Google Cloud and AWS receive equal instructional weight; Azure Blob Storage appears only as a concise terminology translation.
- Architecture concepts are awareness-level. Week 3 retains the detailed treatment of ETL/ELT, analytical architecture, dimensional modeling, and lakehouse implementation.
- SQL is copy/paste-friendly. Questions ask learners to predict, observe, compare, and explain rather than rely on prior SQL fluency.

## Learning Objectives

By the end of the day, learners can:

1. explain where object storage fits in a data engineering pipeline;
2. distinguish a data lake, lakehouse, data warehouse, and data mart at a high level;
3. explain why separating storage from compute changes scalability, cost, and tool choice;
4. choose a suitable file format, folder/prefix convention, and lifecycle tier for a basic landing zone;
5. distinguish lifecycle rules, soft delete, versioning, retention, and lock controls;
6. create and inspect a secure Cloud Storage landing zone;
7. explain schema-on-read and query-in-place using an external table or equivalent guided example.

## Conceptual Boundaries

### Architecture Comparison

Introduce the four terms through purpose and ownership rather than vendor products:

| Architecture | Primary purpose | Typical contents | Main consumers |
| :--- | :--- | :--- | :--- |
| Data lake | Store varied data at scale, often before all uses are known | Raw and processed files/objects | Data engineers, data scientists, analytical engines |
| Lakehouse | Add table semantics, governance, and reliable updates to lake storage | Open table formats over object storage | Engineers, analysts, data scientists |
| Data warehouse | Curated, governed analytical data optimized for SQL and reporting | Structured analytical tables | Analysts, BI tools, business teams |
| Data mart | A focused analytical subset for one domain or team | Subject-specific tables and metrics | A department or bounded business function |

Avoid presenting these as mutually exclusive maturity stages. A modern organization may use all four.

### Storage and Compute Separation

Teach the precise relationship:

- Object storage did not originate solely because analytics platforms separated storage and compute.
- Services such as Amazon S3, Google Cloud Storage, and Azure Blob Storage provide durable, independently scalable object storage.
- Modern query and processing engines can read shared data from object storage and scale compute independently.
- This enables multiple engines, elastic compute, and independent cost controls, but it also creates responsibilities for layout, metadata, governance, and data quality.

### Data Lifecycle Vocabulary

Use **hot → warm → cold → archive** as the primary lifecycle. Explain that “frozen” is an informal description sometimes used for data that is immutable or rarely accessed; it is not the standard cloud storage-class term.

Lifecycle decisions depend on access frequency, retrieval-time tolerance, retention requirements, and total cost. They are not simply “old data moves to the cheapest tier.”

## Narrative

Use this progression: **Place → Organize → Protect → Query → Operate**.

1. Place data at rest within the end-to-end pipeline.
2. Compare the roles of lake, lakehouse, warehouse, and mart.
3. Explain independently scalable object storage and compute.
4. Organize objects using suitable formats, sizes, zones, and partition-like prefixes.
5. Protect data using IAM, recovery, lifecycle, and compliance controls.
6. Query data in place using schema-on-read and external tables.
7. Build and evaluate a Cloud Storage landing zone.
8. Hand the resulting mental model to Day 5's NYC Taxi pipeline.

## Revised Day Schedule

| Time | Segment |
| :--- | :--- |
| 8:30–9:00 | Recap and data-at-rest placement in the pipeline |
| 9:00–9:40 | Lake vs. lakehouse vs. warehouse vs. data mart |
| 9:40–10:00 | Storage and compute separation |
| 10:15–11:00 | File formats, compression, file size, and landing-zone layout |
| 11:00–11:40 | Hot/warm/cold/archive lifecycle and cost |
| 11:40–12:00 | Security, recovery, retention, and minimal demo/preflight |
| 1:00–2:40 | Required Cloud Storage landing-zone lab |
| 2:50–3:30 | Required guided query-in-place mini-lab |
| 3:30–4:15 | Team storage-convention design activity |
| 4:15–4:45 | NYC Taxi Day 5 preview and architecture handoff |
| 4:45–5:00 | Exit ticket and recap |

## Slide Deck Design

The revised deck should contain approximately 22 slides:

1. Title — Data at Rest
2. Why this layer matters
3. Learning objectives and day map
4. Data at rest in an end-to-end pipeline
5. Four analytical data structures: lake, lakehouse, warehouse, mart
6. Choosing among them: one company can use all four
7. Storage and compute: coupled versus independently scalable
8. Object storage translations: GCS, S3, Azure Blob Storage
9. Object-storage mental model: bucket/container, object/blob, key/name, prefix
10. File formats: CSV, JSON, Parquet, Avro
11. Row-oriented versus columnar access
12. Compression, file count, and the small-files problem
13. Landing zones: raw, quarantine, processed, curated
14. Prefix conventions and Hive-style partition paths
15. Handling late, duplicate, and malformed files
16. Schema-on-read versus schema-on-write
17. Query-in-place and external tables
18. Hot, warm, cold, and archive lifecycle
19. Lifecycle, soft delete, versioning, retention, lock, and holds
20. Secure landing-zone lab briefing
21. Query-in-place activity and team design challenge
22. Day 5 handoff, recap, and exit ticket

The architecture comparison must remain concise enough to teach in approximately 40 minutes. Do not add dimensional modeling, star schemas, detailed ACID table-format internals, or vendor-specific warehouse configuration.

## Visual Design

Use `Week 1/Slides/W1D4 - Cloud Object Storage.pptx` as the sole visual reference.

- Preserve its typography, palette, footer treatment, spacing, and overall classroom style.
- Use the source deck's existing slide layouts as the frame bank.
- Prefer one clear comparison, flow, or decision per slide.
- Use native PowerPoint shapes for simple flows and comparisons.
- Give GCP and AWS equal visual weight; show Azure only in the cross-cloud vocabulary slide.
- Avoid dense service catalogs, decorative stock imagery, and dashboard-like card grids.
- Include speaker notes with the teaching point, one learner prompt, the Week 3 boundary where relevant, and official sources for current platform claims.

## Required Lab Revisions

### Cloud Storage Landing-Zone Lab

Revise `Activity_Cloud_Object_Storage.md` to:

- add explicit authentication and project-selection checks;
- add a preflight section for billing, IAM roles, APIs, and classroom account readiness;
- keep public access prevention consistent with the activity instructions;
- distinguish soft delete from object versioning;
- label signed URLs as optional and document the service-account/signing prerequisite;
- align the stated duration with the schedule;
- add brief prediction and reflection questions before and after consequential actions;
- provide an instructor answer key for the existing questions;
- retain an optional S3 translation without requiring a second cloud account.

### Query-in-Place Mini-Lab

Create a required, guided mini-lab that demonstrates schema-on-read and external querying with minimal SQL. Prefer BigQuery over Cloud Storage when classroom permissions permit. Include a no-permission observation fallback using supplied results/screenshots or an instructor demonstration.

Learners should:

1. inspect the stored file and its format;
2. review or create an external-table definition;
3. predict what the query engine must know before reading the data;
4. run supplied queries;
5. observe bytes processed and limitations;
6. explain when query-in-place is useful and when loading curated warehouse tables is preferable.

Do not describe Athena and BigQuery as “the same.” Explain that both can run serverless SQL and expose scan-related cost signals, while their default storage and warehouse roles differ.

### Team Storage-Convention Activity

Retain the NYC Taxi layout scenario, but require each team to define:

- raw, quarantine, processed, and curated locations;
- a date-based prefix convention;
- expected format by zone;
- late/duplicate/malformed-file handling;
- hot/warm/cold/archive transitions;
- who can read and write each zone;
- one query-in-place use case and one warehouse use case.

## Instructor Guide Revisions

Update the guide so it matches the revised schedule, slide order, and lab durations. Add:

- a pre-class account and permissions checklist;
- a minimal demonstration that does not repeat the full student lab;
- prompts for the architecture comparison and storage-compute discussion;
- explicit “teach now” versus “defer to Week 3” guidance;
- fallback paths for missing cloud permissions;
- an answer key and expected observations;
- an exit ticket with three questions aligned to the learning objectives.

## Technical Sources

Use official documentation for current claims:

- Google Cloud Storage overview: https://docs.cloud.google.com/storage/docs/introduction
- Cloud Storage lifecycle management: https://docs.cloud.google.com/storage/docs/lifecycle
- Cloud Storage soft delete: https://docs.cloud.google.com/storage/docs/soft-delete
- Cloud Storage object versioning: https://docs.cloud.google.com/storage/docs/object-versioning
- BigQuery external tables: https://docs.cloud.google.com/bigquery/docs/external-tables
- BigQuery external data over Cloud Storage: https://docs.cloud.google.com/bigquery/docs/external-data-cloud-storage
- BigQuery Hive partitioning: https://docs.cloud.google.com/bigquery/docs/hive-partitioned-queries
- Amazon S3 storage classes: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
- Athena data optimization: https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html
- Azure Blob Storage introduction: https://learn.microsoft.com/azure/storage/blobs/storage-blobs-introduction

## Acceptance Criteria

- The source W1D4 PPTX remains unchanged.
- The revised deck contains approximately 22 slides and fits the revised schedule.
- The deck, instructor guide, lab filenames, activity order, and timing agree.
- Lake, lakehouse, warehouse, and mart are accurate and do not consume the Week 3 deep dive.
- Storage-compute separation is described without claiming it created object storage.
- Lifecycle terminology uses hot/warm/cold/archive and qualifies “frozen” as informal.
- GCP and AWS receive equal instructional weight; Azure appears only as terminology translation.
- The main lab includes reliable prerequisites, fallbacks, aligned access controls, and an answer key.
- The query-in-place activity is achievable without prior SQL fluency.
- Official sources support current product claims.
- All final slides render without unintended overlap, clipping, overflow, broken wrapping, or unresolved placeholders.
- Every slide is visually inspected at full size before delivery.
