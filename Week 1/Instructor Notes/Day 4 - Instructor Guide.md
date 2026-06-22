# W1D4 - Data at Rest - Instructor Guide

- **Deck:** `Slides/W1D4 - Data at Rest - Updated.pptx`
- **Landing-zone lab:** `Labs/Day 4/Activity_Cloud_Object_Storage.md`
- **Query-in-place lab:** `Labs/Day 4/Activity_Query_in_Place_with_BigQuery.md`
- **Audience:** Fresh graduates and junior data engineers
- **Day:** 8:30 AM-5:00 PM

## Day purpose and learning objectives

By the end of the day, learners can:

1. Explain where object storage fits in a data engineering pipeline.
2. Distinguish a data lake, lakehouse, data warehouse, and data mart at a high level.
3. Explain why separating storage from compute changes scalability, cost, and tool choice.
4. Choose a suitable file format, folder/prefix convention, and lifecycle tier for a basic landing zone.
5. Distinguish lifecycle rules, soft delete, versioning, retention, and lock controls.
6. Create and inspect a secure Cloud Storage landing zone.
7. Explain schema-on-read and query-in-place using an external table or equivalent guided example.

Use the day's narrative throughout: **Place -> Organize -> Protect -> Query -> Operate**.

## Pre-class readiness

Complete these checks before learners arrive. Keep a screenshot or supplied-result fallback ready for every cloud-dependent observation.

- Confirm course project IDs are assigned and every learner can sign in to the course-managed GCP account.
- Confirm billing is active for the project and that Cloud Storage and BigQuery are available.
- Confirm learners can create and inspect buckets and objects. At minimum, the classroom role must permit the actions used in the landing-zone lab.
- Confirm learners can create or use the provided BigQuery dataset and external table. If they cannot create resources, pre-create one read-only external table for the class.
- Confirm public access prevention is enforced or selected consistently with the landing-zone lab. Do not ask learners to make an object public.
- Confirm Cloud Shell opens and that `gcloud auth list` and `gcloud config get-value project` return the expected account and project.
- Stage `Labs/Day 4/Lab Resources/yellow_trip_sample.csv`, `coffee.jpg`, `hartford.jpeg`, and `intro.docx` where learners can reach them.
- Use globally unique bucket names. Recommended pattern: `techcatalyst-de-2026-<username>-raw`.
- Verify the demo bucket name is available, or append the instructor username/date.
- Run the 15-minute demo and both required labs once using a learner-equivalent account.
- Capture fallback evidence: bucket settings, an authenticated object view, an `AccessDenied` public request, object generations, the external-table definition, query results, and bytes processed.
- Do not depend on signed URLs. If teaching this optional extension, confirm the service account and `signBlob` permission are available.

## Full-day schedule and slide map

Use this exact schedule, supported by the prompts, boundaries, and facilitation notes that follow.

| Time | Segment | Slides | Delivery focus |
| :--- | :--- | :--- | :--- |
| 8:30-9:00 | Recap and data-at-rest placement | 1-4 | Connect Days 1-3 to stored data and Day 5's pipeline. |
| 9:00-9:40 | Lake vs. lakehouse vs. warehouse vs. mart | 5-6 | Compare purpose, contents, ownership, and consumers. |
| 9:40-10:00 | Storage and compute separation | 7-9 | Independent scaling, shared data, cost, and governance responsibilities. |
| 10:00-10:15 | Break | | |
| 10:15-11:00 | Formats, compression, file size, and layout | 10-15 | Organize a landing zone; connect layout to efficient reads and operations. |
| 11:00-11:40 | Lifecycle and cost | 16-17 | Hot/warm/cold/archive plus recovery, retention, holds, and lock. |
| 11:40-12:00 | Security, recovery, retention, and preflight | 17, 20 | Run the 15-minute demo, then use 5 minutes to brief the required lab and transition. |
| 12:00-1:00 | Lunch | | |
| 1:00-2:40 | Required Cloud Storage landing-zone lab | 20 | Coach and observe; do not repeat the lab as a demo. |
| 2:40-2:50 | Break | | |
| 2:50-3:30 | Required query-in-place mini-lab | 18-19, 21 | Schema-on-read, external table, bytes processed, limitations. |
| 3:30-4:15 | Team storage-convention design | 21 | Require all design decisions listed below. |
| 4:15-4:45 | NYC Taxi Day 5 handoff | 22 | Turn today's storage choices into tomorrow's pipeline inputs. |
| 4:45-5:00 | Exit ticket and recap | 22 | Collect the three responses before dismissal. |

## Teaching prompts and boundaries

### Place: data at rest in the pipeline

Ask: "Yesterday's systems produced data and tomorrow's pipeline will move it. Where does the data wait, and what must still be true while it waits?"

Expected ideas: durable storage, controlled access, discoverable location and format, recoverability, and manageable cost. Clarify that object storage is one storage layer, not the entire pipeline.

### Compare lake, lakehouse, warehouse, and mart

Ask teams to classify each structure by **purpose, typical contents, and consumer**, then ask: "Could one company need all four?" The answer is yes; these are not mutually exclusive maturity stages.

Required prompt: **Can one company use a lake, lakehouse, warehouse, and data mart at the same time? Why?**

Use these concise distinctions:

| Structure | Teach now |
| :--- | :--- |
| Data lake | Varied raw and processed objects at scale for engineers, scientists, and analytical engines. |
| Lakehouse | Table semantics, governance, and reliable updates layered over lake storage. |
| Data warehouse | Curated, governed analytical tables optimized for SQL and reporting. |
| Data mart | A focused analytical subset for one department or bounded domain. |

**Defer to Week 3:** dimensional modeling, star and snowflake schemas, detailed ETL/ELT architecture, table-format internals, ACID implementation, warehouse physical design, and vendor-specific warehouse configuration.

### Storage and compute separation

Ask: "If two query engines read the same objects, must each engine own another copy? What can scale independently, and who now owns layout and quality?"

Required prompt: **What changes when ten compute clusters can read the same durable storage?**

Teach now: S3, Cloud Storage, and Azure Blob Storage are durable, independently scalable object stores. Modern engines can read shared objects and scale compute separately, enabling elastic compute, multiple tools, and separate cost controls. This also increases responsibility for layout, metadata, governance, and quality.

Do **not** claim that separation of storage and compute created object storage. Give GCP and AWS equal conceptual weight; use Azure only to translate bucket/object terminology to container/blob.

**Defer to Week 3:** engine selection, performance architecture, detailed lakehouse implementation, and workload-specific cost modeling.

### Organize, protect, query, and operate

- Ask learners which format they would choose for human exchange versus analytical column scans. Expected: CSV/JSON can aid interchange; Parquet is generally better for selective analytical scans; Avro supports row-oriented records and schema evolution use cases.
- Ask why 10,000 tiny files can be worse than fewer reasonably sized files. Expected: per-file listing, metadata, open, and scheduling overhead.
- Use `raw/date=2026-06-22/` to show that prefixes organize a flat object namespace and can expose partition values; they are not ordinary directories.
- Use **hot -> warm -> cold -> archive**. "Frozen" is informal, not a standard cloud storage-class term. Tiering depends on access frequency, retrieval-time tolerance, retention, and total cost, not age alone.
- Ask: **Would you store a dashboard extract and a seven-year compliance archive in the same tier?** Expected: usually not; their access frequency, retrieval tolerance, retention, and total-cost profiles differ.
- Contrast controls: lifecycle automates actions; soft delete preserves recently deleted objects; versioning preserves replaced/deleted generations; retention blocks deletion for a period; lock makes the retention policy irreversible; holds protect selected objects.
- Ask before query-in-place: "What must the engine know that the CSV file does not enforce?" Expected: location, format, schema, delimiters/header behavior, and permissions.
- Required prompt: **What information must a query engine know before it can interpret a CSV or Parquet object?**

## Minimal preflight demonstration (15 minutes)

This demonstration proves readiness and creates shared observations. Prepare the private bucket, object, and external table in advance. Do not walk through resource creation or the lifecycle/versioning steps learners perform in the lab.

1. **Authenticate and select the project (3 min).** In Cloud Shell, run:

   ```bash
   gcloud auth list
   gcloud config get-value project
   ```

   Point out the active identity and project. Stop and switch to the fallback if either is wrong and cannot be corrected quickly.

2. **Inspect one prepared private bucket and object (6 min).** Show the bucket's region, uniform bucket-level access, and public access prevention, then open one object's inspection screen. Point out its full name/prefix, size, type, and authenticated access. Explain why compute/data region choices can affect latency and network cost.

3. **Preview one external query estimate (6 min).** Open the prepared BigQuery external table, show its source URI/schema, and paste one supplied query. Explain that the validator or dry run may report `0 B`, an unavailable estimate, or only a lower bound for external data; do not present that value as actual bytes processed. Stop before running the query. In the afternoon mini-lab, learners run the query and interpret actual bytes processed from the completed query's **Job information**.

The demo ends here. Do not demonstrate lifecycle configuration, version restoration, or signed-URL creation before the landing-zone lab.

### Lab briefing and transition (5 minutes)

Point learners to `Activity_Cloud_Object_Storage.md`, confirm the required naming convention and public access prevention setting, and remind them to complete authentication/project checks before creating resources. Direct anyone who lacks permissions to the instructor-shared, view-only, or paired-execution fallback rather than changing access controls.

## 1:00-2:40 Cloud Storage landing-zone lab

Use `Activity_Cloud_Object_Storage.md`. At 1:00, require learners to complete its authentication/project checks before creating resources. At 1:50, check that each learner has a secure raw landing zone and correctly placed objects. Reserve the final 20 minutes for validation, reflection, and cleanup.

Use the centralized **Fallbacks and troubleshooting** section for operational issues. During coaching, immediately challenge any learner who describes soft delete as versioning; require them to state the different triggers and recovery behavior.

## 2:50-3:30 query-in-place mini-lab

Use `Activity_Query_in_Place_with_BigQuery.md`. Keep the SQL supplied and copy/paste-friendly. Learners inspect the CSV, predict required metadata, review or create the BigQuery external table, run the supplied queries, observe results and bytes processed, and explain limitations.

Do not present BigQuery and Athena as identical. Both can run serverless SQL and expose scan-related cost signals; BigQuery is also a managed data warehouse, whereas Athena queries data in sources such as S3.

## 3:30-4:15 team storage-convention activity

Each team designs an NYC Taxi convention and must specify:

- raw, quarantine, processed, and curated locations;
- a date-based prefix convention;
- the expected format in each zone;
- handling for late, duplicate, and malformed files;
- hot/warm/cold/archive transitions and the reason for each;
- who can read and write each zone;
- one query-in-place use case and one warehouse use case.

Allow 25 minutes to design, 15 minutes for brisk readouts, and 5 minutes to name one choice they will carry into Day 5.

## 4:15-4:45 Day 5 handoff

Ask learners to point to tomorrow's NYC Taxi pipeline on the Day 5 architecture: where data lands, how it is named, what happens to malformed or duplicate files, which engine reads it, and which outputs belong in curated storage or a warehouse. The goal is a usable storage contract, not a Week 3 architecture design.

## 4:45-5:00 exit ticket

Collect one concise response to each question:

1. Explain one difference between a data lake and a data warehouse without naming a vendor product.
2. Why can separating storage and compute improve flexibility, and what new responsibility does it create?
3. Choose one control for accidental deletion and one control for compliance retention; explain the difference.

**Exit-ticket key:** (1) A lake stores varied raw/processed files for multiple future uses; a warehouse holds curated, governed analytical tables optimized for SQL/reporting. (2) Multiple engines and compute clusters can use shared durable data and scale independently; teams must own layout, metadata, governance, quality, and cost. (3) Soft delete or versioning can recover accidental deletion; a retention policy prevents deletion for a required period. A locked retention policy is irreversible, so do not accept "versioning" as a compliance lock.

## Fallbacks and troubleshooting

- **Instructor-shared bucket:** If learners cannot create/manage assigned buckets, use a prepared private bucket with scoped learner access. Never disable public access prevention to bypass an IAM problem.
- **View-only evidence:** If cloud access is unavailable, give learners the prepared screenshots/results for bucket settings, private access, prefixes, generations, lifecycle configuration, external-table metadata, query results, and bytes processed. Require all predictions and explanations.
- **Paired execution:** Pair an unauthorized learner with an authorized classmate as driver/navigator. Both learners submit their own observations and answers.
- **BigQuery fallback:** Prefer a pre-created read-only external table. If query execution is also unavailable, use an instructor demonstration or supplied results.
- **Bucket-name collision:** Add the learner name or another approved unique suffix.
- **Wrong project/account:** Correct it before resource creation.
- **Region mismatch:** Discuss the implication; do not spend lab time recreating a valid bucket unless instructions require it.
- **Public URL fails:** This is expected evidence of private access, not a defect.
- **Lifecycle change is not visible:** Inspect the configuration; rules are asynchronous and objects must meet their conditions.
- **Signed URL cannot be created:** Skip this optional extension unless the configured service account and `signBlob` permission are available.

## Answer key and expected observations

Use these as the minimum acceptable ideas; equivalent well-reasoned answers are valid.

1. **Why use a unique bucket name?** Bucket names occupy a shared global namespace; the course suffix reduces collisions and identifies ownership.
2. **Are prefix "folders" real directories?** No. A name such as `raw/date=2026-06-22/trips.csv` is one object name; tools render delimiter-separated prefixes like folders.
3. **Why does the public object URL fail?** Public access prevention and IAM deny anonymous access while an authenticated principal with permission can read it.
4. **What is the difference between soft delete and versioning?** Soft delete retains deleted objects for a recovery window. Versioning retains noncurrent generations when objects are replaced or deleted. They are separate controls and may coexist.
5. **What should version restoration show?** Listing generations exposes a live and at least one noncurrent generation; copying or restoring the selected earlier generation makes its prior content current without making the bucket public.
6. **Why can a configured lifecycle rule appear to do nothing?** Evaluation and transitions are asynchronous, and an object must meet the rule conditions. Validate the rule rather than waiting during class.
7. **What should an external query engine know?** Object location, file format, schema or inference rules, parsing options, and authorization.
8. **What demonstrates schema-on-read?** The stored CSV is not changed; the external-table definition supplies a schema when the engine reads it.
9. **What should learners observe from the supplied query?** Rows are returned without first loading the file into a native warehouse table, and the UI/job details report bytes processed or a comparable scan signal.
10. **When is query-in-place useful?** Exploration, occasional access, validation, or avoiding an immediate copy. It is less suitable than curated native tables for repeated, governed, performance-sensitive BI workloads.
11. **What is a defensible landing-zone design?** Immutable raw intake, quarantine for suspect files, processed standardized data, curated consumer-ready data, date-based prefixes, explicit access ownership, and lifecycle choices tied to recovery/compliance and access needs.

## Official references

- Cloud Storage overview: https://docs.cloud.google.com/storage/docs/introduction
- Cloud Storage lifecycle: https://docs.cloud.google.com/storage/docs/lifecycle
- Cloud Storage soft delete: https://docs.cloud.google.com/storage/docs/soft-delete
- Cloud Storage object versioning: https://docs.cloud.google.com/storage/docs/object-versioning
- BigQuery external tables: https://docs.cloud.google.com/bigquery/docs/external-tables
- BigQuery external data over Cloud Storage: https://docs.cloud.google.com/bigquery/docs/external-data-cloud-storage
- BigQuery Hive partitioning: https://docs.cloud.google.com/bigquery/docs/hive-partitioned-queries
- Amazon S3 storage classes: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
- Athena data optimization: https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html
- Azure Blob Storage terminology: https://learn.microsoft.com/azure/storage/blobs/storage-blobs-introduction
