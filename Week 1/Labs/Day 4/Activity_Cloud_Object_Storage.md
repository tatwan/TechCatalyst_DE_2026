# Week 1 · Day 4 — Cloud Object Storage Landing-Zone Lab

**Module:** Data at Rest  
**Estimated time:** 100 minutes (core lab) + 45 minutes (team design activity)  
**Difficulty:** Beginner  
**Format:** Individual or paired core lab; small-group design activity  
**Status:** Required core Day 4 activity

## Objective

Build and inspect a secure Google Cloud Storage landing zone. By the end, you can:

- create buckets with uniform bucket-level access and public access prevention;
- organize objects into zones and date-based prefixes;
- explain lifecycle and recovery controls without confusing their purposes;
- test authenticated and unauthenticated access safely;
- optionally translate the landing-zone design to Amazon S3 without requiring an AWS account.

## Files and Deliverables

Use the files in `Lab Resources/`: `coffee.jpg`, `hartford.jpeg`, and `intro.docx`.

| Deliverable | Required contents | Due |
| :--- | :--- | :--- |
| `day4_lab.md` | Commands, answers to Q1–Q7, four Predict/Observe responses, lifecycle JSON, and screenshots of the raw and processed buckets (or the embedded fallback evidence) | End of day |
| Team storage convention | Required template items 1–7 and a 3-minute readout; item 8 is optional | End of day |

Replace these placeholders before running commands:

```bash
export PROJECT_ID="YOUR_ASSIGNED_PROJECT_ID"
export USERNAME="YOUR_SHORT_USERNAME"
export RAW_BUCKET="techcatalyst-de-2026-${USERNAME}-raw"
export PROCESSED_BUCKET="techcatalyst-de-2026-${USERNAME}-processed"
```

Bucket names are globally unique. If a name is taken, add the short suffix supplied by your instructor.

---

# Core Lab — 100 Minutes

## Part 0 — Account and Project Preflight (10 minutes)

> [!IMPORTANT]
> Use only the assigned course account and project. Do not attach your own billing account or payment method. If any check below fails, stop the write-path instructions and use the fallback immediately below.

1. Open Cloud Shell, or a terminal where the Google Cloud CLI is installed.
2. Run the checks exactly as shown:

   ```bash
   gcloud auth list
   gcloud config set project "$PROJECT_ID"
   CONFIGURED_PROJECT="$(gcloud config get-value project)"
   if [[ "$CONFIGURED_PROJECT" == "$PROJECT_ID" ]]; then
     echo "Project check passed: $CONFIGURED_PROJECT"
   else
     echo "STOP: expected $PROJECT_ID but found $CONFIGURED_PROJECT"
   fi
   gcloud billing projects describe "$PROJECT_ID"
   gcloud services list --enabled \
     --filter='name:(storage.googleapis.com OR bigquery.googleapis.com)'
   ```

3. Confirm all five readiness conditions:

   - the active account is your assigned classroom account;
   - `gcloud config get-value project` prints the assigned project ID;
   - the billing result says `billingEnabled: true`, or the instructor confirms billing is enabled if your classroom role cannot view billing details;
   - `storage.googleapis.com` is enabled (BigQuery is also needed for the next required activity);
   - the instructor confirms you have a course role that can create and manage lab buckets and objects, normally a scoped Storage Admin role.

   A `PERMISSION_DENIED` response from the billing command does not prove that billing is disabled. Ask the instructor to check it. Do not attach your own billing account or payment method.

4. Record the active account, project ID, billing confirmation, and enabled-service result in `day4_lab.md`. Do not record access tokens or credentials.

**Q1:** Which result proves that subsequent commands target the assigned project? Why is seeing the correct signed-in email alone insufficient?

### No-write fallback

If the assigned account, project, API, billing status, or role is missing:

1. Show the failed check to the instructor; do not try to enable billing or broaden your own role.
2. Pair with a learner whose course environment works and take the **observer/recorder** role. Record each prediction, command, output, and explanation yourself.
3. If pairing is unavailable, use the representative evidence below. Complete Q1–Q7, all Predict/Observe responses, the control table analysis, and the team design. Mark each action `simulated from fallback evidence` rather than `ran`.
4. Add `Fallback used: <reason>` at the top of `day4_lab.md`. The learning criteria are the same; bucket ownership is not required for a blocked learner.

**Representative fallback evidence:**

```text
ACTIVE ACCOUNT: learner@course.example
ACTIVE PROJECT: course-project-123
BILLING: billingEnabled: true (instructor-confirmed is also acceptable)
ENABLED SERVICES: storage.googleapis.com, bigquery.googleapis.com

RAW BUCKET CONTROLS:
  uniformBucketLevelAccess.enabled: true
  publicAccessPrevention: enforced
PRECHECK RECOVERY CONTROLS:
  softDeletePolicy.retentionDurationSeconds: 604800
  versioning.enabled: false
AUTHENTICATED CONSOLE OPEN: coffee.jpg displayed
INCOGNITO OBJECT URL: AccessDenied / anonymous caller lacks storage.objects.get
PARTNER IAM OBSERVATION:
  authenticated partner with roles/storage.objectViewer listed the objects
  the same object remained unavailable to an anonymous incognito request

OBJECT LIST:
  gs://...-raw/coffee.jpg
  gs://...-raw/raw/source=classroom/year=2026/month=06/day=22/hartford.jpeg
  gs://...-raw/raw/source=classroom/year=2026/month=06/day=22/intro.docx
  gs://...-processed/staging/hartford.jpeg
  gs://...-processed/staging/intro.docx

AFTER SAVING LIFECYCLE RULES: coffee.jpg remains Standard because it is 0 days old
VERSIONING AFTER ENABLE WAIT: enabled: true
AFTER OVERWRITE (`ls -a`): coffee.jpg#1001, coffee.jpg#1002
UNQUALIFIED LIVE OBJECT METADATA: generation: 1002
STATE INFERENCE: #1002 is live because it matches the unqualified object; #1001 is noncurrent
AFTER RESTORE (`ls -a`): coffee.jpg#1001, coffee.jpg#1002, coffee.jpg#1003
UNQUALIFIED LIVE OBJECT METADATA AFTER RESTORE: generation: 1003
STATE INFERENCE: #1003 is the new live copy of the original; #1001 and #1002 remain noncurrent
```

Use this representative lifecycle JSON for the fallback:

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "NEARLINE"
        },
        "condition": {
          "age": 30
        }
      },
      {
        "action": {
          "type": "Delete"
        },
        "condition": {
          "age": 365
        }
      }
    ]
  }
}
```

For the screenshot requirement, paste the evidence block into `day4_lab.md` and label it `Fallback evidence substituted for screenshots`. For the lifecycle requirement, paste the supplied JSON, label it `Fallback lifecycle JSON`, and annotate it: `Expected behavior: objects become eligible for Nearline at age 30 days and deletion at age 365 days; today's object remains Standard immediately after activation.` Commands may be recorded as `observed from fallback evidence`. These substitutions cover every core deliverable when write permissions are unavailable.

## Part 1 — Create and Secure the Raw Bucket (25 minutes)

1. In the Google Cloud Console, go to **Cloud Storage → Buckets → Create**.
2. Create `techcatalyst-de-2026-<your-username>-raw` with:

   - Location type: **Region**
   - Region: `us-east1`
   - Default storage class: **Standard**
   - **Uniform bucket-level access:** enabled
   - **Public access prevention:** enforced

3. Upload `coffee.jpg` to the bucket root.
4. Open the object from the console while signed in. It should open because the console sends your authenticated request.

### Access test

**Predict:** Before testing, write whether the direct object URL will open in an incognito window and identify which control or identity your prediction depends on.

5. Copy the object's `https://storage.googleapis.com/...` URL and open it in an incognito window where you are not signed in. Do **not** change either access-control setting.

**Observe and explain:** Record the exact response or error. Compare the identity used by the console request with the identity used by the incognito request.

**Q2:** Why did the authenticated console action work while the incognito request failed?

6. Upload `hartford.jpeg` and `intro.docx` under this prefix:

   ```text
   raw/source=classroom/year=2026/month=06/day=22/
   ```

**Q3:** Did Cloud Storage create real folders? What does the console tree represent?

7. On the bucket **Permissions** tab, grant your assigned partner **Storage Object Viewer** on this bucket. Have the partner list or inspect the objects while authenticated.

   This grant is bucket-scoped. With uniform bucket-level access, the `raw/...` prefix is not a separate IAM resource. If two zones need different readers or writers, separate buckets are usually clearer than pretending a prefix is an access boundary.

8. Verify the bucket controls:

   ```bash
   gcloud storage buckets describe "gs://${RAW_BUCKET}" \
     --format='yaml(name,location,iamConfiguration.uniformBucketLevelAccess,iamConfiguration.publicAccessPrevention)'
   ```

**Q4:** Why is a bucket-level viewer grant consistent with public access prevention?

## Part 2 — Build the Processed Zone with the CLI (20 minutes)

1. Create a second bucket with the same access-control posture:

   ```bash
   gcloud storage buckets create "gs://${PROCESSED_BUCKET}" \
     --project="${PROJECT_ID}" \
     --location=us-east1 \
     --uniform-bucket-level-access \
     --public-access-prevention
   ```

2. Copy the two source objects into a staging prefix:

   ```bash
   gcloud storage cp \
     "gs://${RAW_BUCKET}/raw/source=classroom/year=2026/month=06/day=22/*" \
     "gs://${PROCESSED_BUCKET}/staging/"
   ```

3. List the processed bucket recursively with sizes:

   ```bash
   gcloud storage ls -l "gs://${PROCESSED_BUCKET}/**"
   ```

4. Take one screenshot showing each bucket and its object/prefix layout.

**Q5:** In these commands, what does `**` match that `*` may not match?

## Part 3 — Lifecycle and Recovery Controls (35 minutes)

These controls solve different problems. Copy this table into your notes before configuring anything.

| Control | Primary purpose | Can normal deletion still occur? | Typical use |
| :--- | :--- | :--- | :--- |
| Lifecycle rule | Automate transition or deletion | Yes | Cost and housekeeping |
| Soft delete | Recover recently deleted objects | Deletion creates recoverable state | Accidental deletion recovery |
| Versioning | Preserve overwritten/deleted generations | Yes, with versions retained | Change recovery |
| Retention policy | Prevent deletion before an age | No | Minimum retention |
| Bucket Lock | Make retention policy irreversible | No | Regulated/compliance data |

Soft delete is a bucket recovery window for deleted objects. Versioning retains noncurrent generations created by overwrite or deletion. Neither is a substitute for a retention policy, and Bucket Lock is an irreversible compliance action that is not performed in this core lab.

### A. Add a lifecycle rule

**Predict:** Will saving a “Nearline after 30 days” rule move today's objects immediately? What object property will the rule evaluate?

1. In the raw bucket, open **Lifecycle → Add a rule**.
2. Add a rule to change objects to **Nearline** after 30 days.
3. Add a second rule to delete objects after 365 days.
4. Save the configuration, then retrieve the applied lifecycle JSON with the CLI and paste its output into `day4_lab.md`:

   ```bash
   gcloud storage buckets describe "gs://${RAW_BUCKET}" \
     --format='json(lifecycle)'
   ```

**Observe and explain:** Inspect `coffee.jpg` immediately after saving. Record its current storage class and explain why it did or did not change.

**Q6:** Regulatory raw data must be retained for seven years. Why is a 365-day lifecycle deletion rule unsafe, and which control prevents early deletion rather than merely scheduling deletion?

### B. Enable versioning and overwrite an object

1. Check the raw bucket's current soft delete policy and record what the console or command reports:

   ```bash
   gcloud storage buckets describe "gs://${RAW_BUCKET}" \
     --format='yaml(softDeletePolicy,versioning)'
   ```

2. Enable object versioning:

   ```bash
   gcloud storage buckets update "gs://${RAW_BUCKET}" --versioning
   sleep 30
   gcloud storage buckets describe "gs://${RAW_BUCKET}" \
     --format='yaml(versioning)'
   ```

   Continue only after the result shows `enabled: true`. If it does not, wait another 30 seconds and describe the bucket again.

**Predict:** When `coffee.jpg` is overwritten, will the original generation disappear from an all-versions listing? What do you expect the new live generation to contain?

3. Upload a different image using the exact object name `coffee.jpg`.
4. List all generations:

   ```bash
   gcloud storage ls -a "gs://${RAW_BUCKET}/coffee.jpg"
   gcloud storage objects describe "gs://${RAW_BUCKET}/coffee.jpg" \
     --format='yaml(name,generation,size,updated)'
   ```

`gcloud storage ls -a` lists generation-qualified names; it does **not** label them live or noncurrent. The unqualified `objects describe` command returns the current live object's generation. Match that number to the all-generations list: the match is live and the other listed generations are noncurrent.

**Observe and explain:** Record the all-generations list and the unqualified object's generation. Show how you inferred which generation is live and explain how the result differs from a bucket with versioning disabled.

### C. Restore the original generation

**Predict:** Will restoring an old generation erase the newer generation, or create another live generation? Write your prediction before running the command.

5. Copy the original generation number from the listing, then restore it:

   ```bash
   gcloud storage cp \
     "gs://${RAW_BUCKET}/coffee.jpg#ORIGINAL_GENERATION" \
     "gs://${RAW_BUCKET}/coffee.jpg"
   gcloud storage ls -a "gs://${RAW_BUCKET}/coffee.jpg"
   gcloud storage objects describe "gs://${RAW_BUCKET}/coffee.jpg" \
     --format='yaml(name,generation,size,updated)'
   ```

**Observe and explain:** Open the live object, then compare its described generation with the all-generations listing. State what became live and whether the intervening generation remains available.

**Q7:** How do unique append-only object names reduce the value of versioning on a high-volume raw zone, and why can deletions or operational mistakes still create billable recovery data? Name one bounded recovery control.

## Part 4 — Document and Check Your Work (10 minutes)

1. Confirm that `day4_lab.md` contains:

   - preflight evidence and any fallback note;
   - commands run or observed;
   - answers to Q1–Q7;
   - all four Predict and Observe responses;
   - lifecycle JSON and both bucket screenshots.

2. Optionally compare the services without creating an AWS account:

   | Concept | Google Cloud | AWS |
   | :--- | :--- | :--- |
   | Object storage service | Cloud Storage | Amazon S3 |
   | URI | `gs://bucket/key` | `s3://bucket/key` |
   | Default secure posture used here | Public access prevention + uniform bucket IAM | Block Public Access + bucket/IAM policies |
   | CLI example | `gcloud storage ls gs://bucket/**` | `aws s3 ls s3://bucket/ --recursive` |

**Optional S3 reflection:** Name one concept that transfers directly from GCS to S3 and one implementation detail that changes. This is not part of the required submission.

### Classroom ownership and cleanup

The course project and its buckets belong to the classroom environment. Follow the instructor's retention decision because these buckets may be reused by later pipeline activities. Do not delete buckets, disable soft delete, or shorten recovery or retention settings unless the instructor explicitly directs it. Noncurrent generations and soft-deleted objects can remain billable, so leaving test data indefinitely is not free; lifecycle actions are also not immediate cleanup.

If you granted partner access, revoke that temporary grant after the observation. Replace the email first:

```bash
export PARTNER_EMAIL="PARTNER_CLASSROOM_EMAIL"
gcloud storage buckets remove-iam-policy-binding "gs://${RAW_BUCKET}" \
  --member="user:${PARTNER_EMAIL}" \
  --role="roles/storage.objectViewer"
```

If the instructor directs full cleanup, have the classroom owner verify retention and soft-delete policy first. Run the following only after that explicit approval; stop if any retention-policy error appears:

```bash
# Removes live and noncurrent versions; soft delete may still retain recoverable data.
gcloud storage rm --all-versions "gs://${RAW_BUCKET}/**"
gcloud storage rm --recursive "gs://${PROCESSED_BUCKET}/**"
gcloud storage buckets delete "gs://${RAW_BUCKET}"
gcloud storage buckets delete "gs://${PROCESSED_BUCKET}"
```

Soft delete may retain recoverable data or the deleted bucket and continue storage charges during its recovery window; only the classroom owner should decide whether that policy changes. Learners must not improvise other destructive cleanup commands.

## Optional Extension — Signed URL (10 minutes)

Signed URLs are **not required** for the core lab. They grant time-limited access to a specific object without making the bucket anonymous or changing public access prevention.

Signing requires suitable credentials. In classroom environments this commonly means an approved service account whose signer can use the `iam.serviceAccounts.signBlob` capability; user credentials alone may not be ready to sign.

**Instructor readiness check:** Before offering this extension, confirm that an approved service account exists, the learner can impersonate or use it as intended, the signer has permission to sign blobs, and the object reader permissions are correct. Do not create keys during class merely to complete this extension.

If the instructor confirms readiness, generate a 10-minute URL using the supplied classroom command or console workflow, test it in incognito, and record when this is preferable to a durable bucket IAM grant.

## Success Criteria

- Both buckets enforce uniform bucket-level access and public access prevention.
- Objects use a source and Hive-style date prefix rather than simulated ad hoc folders.
- Authenticated access succeeds and unauthenticated incognito access fails as predicted.
- Lifecycle, soft delete, versioning, retention, and Bucket Lock are explained distinctly.
- The original object generation is restored and the observed result is documented.
- `day4_lab.md` contains all required evidence and answers.

## Hints

<details>
<summary>A command still points at the wrong project</summary>

Run `gcloud config get-value project`, then repeat `gcloud config set project "$PROJECT_ID"`. Also check whether `${PROJECT_ID}` still contains the placeholder.
</details>

<details>
<summary>The partner cannot inspect objects</summary>

Check that the grant is on the bucket, the full classroom email is correct, and the partner is authenticated as that account. Do not weaken the bucket's public-access controls.
</details>

<details>
<summary>The generation restore command fails</summary>

Copy the numeric generation exactly from `gcloud storage ls -a`. Keep `#GENERATION` inside the quoted URI so the shell passes it literally.
</details>

---

# Team Design Activity — Taxi Storage Convention (45 Minutes)

Design the storage convention your team could use for the eight-week NYC Taxi pipeline. Submit one page; a list, table, or diagram is acceptable, but every decision needs a one-sentence reason.

## Required Team Template

1. **Zones:** Define `raw`, `quarantine`, `processed`, and `curated` locations. Decide whether access or lifecycle differences justify separate buckets.
2. **Keys:** Give one complete Hive-style example using `year=YYYY/month=MM/day=DD` and state how source and taxi type appear in the key.
3. **Formats:** Choose an expected file format for every zone.
4. **Exceptions:** State what happens to late, duplicate, and malformed files. Include how an operator can trace each file.
5. **Lifecycle:** Define hot, warm, cold, and archive transitions or explain why a zone skips a tier. Include deletion timing.
6. **Access:** Name who can read and write each zone; do not treat prefixes as IAM boundaries unless your proposed platform explicitly supports that design.
7. **Consumption:** Give one query-in-place use case and one use case that should load curated data into a warehouse.
8. **Optional translation:** State how the same design maps from GCS to S3 without changing its architectural intent. This item is not required for the team deliverable.

**Deliverable:** One-page convention plus a 3-minute readout. Every team member must be able to explain one design choice and its trade-off.

---

# Instructor Answer key and Reference Design

## Core Questions

**Q1:** The `Project check passed` result proves that `gcloud config get-value project` exactly equals the previously defined `$PROJECT_ID`. Authentication identifies the caller, but one account can access several projects, so the email does not prove the active project or billing/IAM context.

**Q2:** The console request includes the learner's authenticated identity and succeeds through IAM. Incognito has no authorized identity, and public access prevention blocks anonymous exposure, so the direct request returns an access error (the exact wording may vary).

**Q3:** No filesystem folders were created. Object names are flat keys; the console groups shared name prefixes to display a folder-like tree.

**Q4:** Public access prevention blocks access granted to anonymous/public principals. A named partner with `Storage Object Viewer` is an authenticated principal receiving an explicit bucket-level IAM grant.

**Q5:** `*` matches within one path segment in this use; `**` recursively matches objects beneath nested prefixes.

**Q6:** A 365-day deletion action conflicts with a seven-year minimum. A retention policy prevents deletion before the required age; locking it with Bucket Lock makes that policy irreversible and should only follow formal compliance approval. A lifecycle rule alone automates an action but does not impose a minimum-retention barrier.

**Q7:** With unique append-only names, normal ingestion does not overwrite an existing object, so versioning adds little protection to that normal path while retaining extra generations when mistakes do overwrite or delete data. Deletions, accidental overwrites, reruns that reuse a name, and later cleanup can still leave billable noncurrent or soft-deleted data. A bounded soft-delete window can provide recovery while controlled writers and unique immutable names reduce overwrite risk; it does not eliminate deletion or cost risk.

**Optional S3 reflection:** Transferable concepts include buckets, object keys, prefixes, IAM, lifecycle, version history, and storage tiers. Details that change include URI schemes, CLI syntax, IAM/policy mechanics, tier names, and provider-specific recovery defaults.

## Expected Predict and Observe Responses

- **Access test:** Predict denial because the browser has no authorized identity. Observe an access error in incognito while the authenticated console succeeds.
- **Lifecycle:** Predict no immediate transition because new objects have not reached the age condition. Observe that `coffee.jpg` remains Standard immediately after the rule is saved.
- **Overwrite:** Predict that the previous live generation becomes noncurrent and a new live generation appears. Observe at least two generation numbers, then match the unqualified object's described generation to infer which one is live.
- **Restore:** Predict that copying an old generation creates a new live generation rather than deleting history. Match the unqualified object's new generation to the listing and observe that intervening history remains available.

## Plausible Team Reference Design

| Zone | Example location and format | Handling and access | Lifecycle |
| :--- | :--- | :--- | :--- |
| Raw | `gs://taxi-raw/source=nyc-tlc/type=yellow/year=2026/month=06/day=22/yellow_2026-06-22_001.parquet` (source format accepted; Parquet preferred when supplied) | Ingestion service writes; engineers read; immutable names include source/checksum metadata | Standard (hot) 30 days → Nearline (warm) to day 365 → Coldline (cold) to year 2 → Archive through year 7 → delete after 7 years only when retention permits and approval exists |
| Quarantine | `gs://taxi-quarantine/reason=schema/year=2026/month=06/day=22/...` (original file + JSON error report) | Validator writes; operators read/write; analysts denied | Standard (hot) 30 days → Nearline (warm) to day 180 → delete at day 180 unless held; skip cold/archive because investigation data is short-lived and later-tier minimum-duration/retrieval costs add little value |
| Processed | `gs://taxi-processed/type=yellow/year=2026/month=06/day=22/part-*.parquet` | Pipeline writes; engineers and approved query engines read | Standard (hot) 90 days → Nearline (warm) to year 1 → Coldline (cold) to year 3 → Archive through year 7 → delete at year 7 after approved reproducibility window |
| Curated | `gs://taxi-curated/dataset=trips/type=yellow/year=2026/month=06/day=22/part-*.parquet` | Release pipeline writes; analysts/query engines read | Standard (hot) 180 days → Nearline (warm) to year 1 → Coldline (cold) to year 3 → Archive older snapshots through year 7 → delete snapshots at year 7; retain or rebuild the current published dataset |

Late files land under their event date with an ingestion timestamp in metadata and trigger a targeted partition rerun. Duplicate detection uses source ID plus checksum; duplicates go to quarantine with a reason record. Malformed files go to quarantine unchanged with validation output and a trace/correlation ID.

Query-in-place is suitable for an engineer validating a newly processed partition before promotion. Repeated dashboards and governed business metrics should use curated warehouse tables for predictable performance, metadata, and access controls. Optionally, the team can translate the design to S3: the bucket/key layout and responsibilities stay the same while `gs://` becomes `s3://`, GCS IAM becomes AWS IAM/bucket policy design, and lifecycle/storage-class names use S3 equivalents.

## Common Mistakes and Debrief

- Learners confuse a prefix with a folder or security boundary.
- Learners assume lifecycle rules protect data from manual deletion.
- Learners call soft delete and versioning interchangeable.
- Learners interpret an authenticated console preview as anonymous access.

Debrief prompt: **Which control manages cost, which supports recovery, and which enforces a minimum retention period? Why might one bucket need more than one of them?**
