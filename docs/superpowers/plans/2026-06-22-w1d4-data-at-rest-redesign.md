# W1D4 Data at Rest Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a coherent Week 1 Day 4 lesson on data at rest, including a visually verified 22-slide deck, aligned instructor guide, corrected Cloud Storage lab, and beginner-safe query-in-place mini-lab.

**Architecture:** Treat the approved design specification as the instructional contract and the existing W1D4 PPTX as the sole presentation template. Revise Markdown artifacts in place, add one focused required activity, then build an adjacent updated PPTX with `@oai/artifact-tool`; verify terminology, timing, permissions, source integrity, and every rendered slide before delivery.

**Tech Stack:** Markdown, Google Cloud CLI and Console instructions, BigQuery external tables, Node.js ES modules, `@oai/artifact-tool`, bundled presentation template-following and QA scripts, PowerPoint/PPTX, official Google Cloud/AWS/Azure documentation.

---

## File Structure

- Preserve: `Week 1/Slides/W1D4 - Cloud Object Storage.pptx`
- Create: `Week 1/Slides/W1D4 - Data at Rest - Updated.pptx`
- Modify: `Week 1/Instructor Notes/Day 4 - Instructor Guide.md`
- Modify: `Week 1/Labs/Day 4/Activity_Cloud_Object_Storage.md`
- Create: `Week 1/Labs/Day 4/Activity_Query_in_Place_with_BigQuery.md`
- Modify: `Week 1/Labs/Day 4/Student_Resources.md`
- Preserve as optional: `Week 1/Labs/Day 4/Activity_Stretch_Athena_over_S3.md`
- Preserve as optional: `Week 1/Labs/Day 4/Activity_Optional_Athena_Joins.md`
- Preserve as optional: `Week 1/Labs/Day 4/Activity_Optional_Bucket_Lock.md`
- Approved design: `docs/superpowers/specs/2026-06-22-w1d4-data-at-rest-redesign.md`
- This plan: `docs/superpowers/plans/2026-06-22-w1d4-data-at-rest-redesign.md`
- Scratch root: `$TMPDIR/codex-presentations/manual-w1d4-data-at-rest/w1d4-data-at-rest/tmp`
- Authoring module: `$TMP_DIR/build_w1d4_data_at_rest.mjs`
- Acceptance module: `$TMP_DIR/check_w1d4_final.mjs`
- Template artifacts: `$TMP_DIR/template-audit.txt`, `$TMP_DIR/template-frame-map.json`, `$TMP_DIR/deviation-log.txt`, `$TMP_DIR/template-starter.pptx`
- Claim ledger: `$TMP_DIR/source-notes.txt`
- Rendered slides: `$TMP_DIR/preview/final/`
- Layout reports: `$TMP_DIR/layout/final/`
- QA ledger: `$TMP_DIR/qa/final-qa.txt`

### Task 1: Establish the Instructional and Source Baseline

**Files:**
- Read: `docs/superpowers/specs/2026-06-22-w1d4-data-at-rest-redesign.md`
- Read: all files under `Week 1/Labs/Day 4/`
- Read: `Week 1/Instructor Notes/Day 4 - Instructor Guide.md`
- Read: `Week 1/Slides/W1D4 - Cloud Object Storage.pptx`
- Create: `$TMP_DIR/qa/source.sha256`
- Create: `$TMP_DIR/qa/content-baseline.txt`

- [ ] **Step 1: Initialize the presentation workspace and artifact-tool package**

Run:

```bash
SKILL_DIR="/Users/tarekatwan/.codex/plugins/cache/openai-primary-runtime/presentations/26.619.11828/skills/presentations"
TMP_DIR="${TMPDIR:-$(node -p "require('node:os').tmpdir()")}/codex-presentations/manual-w1d4-data-at-rest/w1d4-data-at-rest/tmp"
mkdir -p "$TMP_DIR/qa" "$TMP_DIR/preview/final" "$TMP_DIR/layout/final"
node "$SKILL_DIR/container_tools/setup_artifact_tool_workspace.mjs" --workspace "$TMP_DIR"
```

Expected: exit code 0 and `@oai/artifact-tool` resolves inside `$TMP_DIR`.

- [ ] **Step 2: Record the source checksum and baseline counts**

Run:

```bash
SOURCE="$PWD/Week 1/Slides/W1D4 - Cloud Object Storage.pptx"
FINAL="$PWD/Week 1/Slides/W1D4 - Data at Rest - Updated.pptx"
shasum -a 256 "$SOURCE" > "$TMP_DIR/qa/source.sha256"
rg -n '^#|^##|Estimated time|minutes|hours' "Week 1/Instructor Notes/Day 4 - Instructor Guide.md" "Week 1/Labs/Day 4" > "$TMP_DIR/qa/content-baseline.txt"
test ! -e "$FINAL"
```

Expected: source checksum and content inventory exist; final deck does not yet exist.

- [ ] **Step 3: Write the failing cross-artifact acceptance script**

Create `$TMP_DIR/check_w1d4_final.mjs` to assert:

```js
import fs from "node:fs/promises";
import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const [deckPath, guidePath, storageLabPath, queryLabPath, resourcesPath] = process.argv.slice(2);
const deck = await PresentationFile.importPptx(await FileBlob.load(deckPath));
if (deck.slides.items.length !== 22) throw new Error(`Expected 22 slides, got ${deck.slides.items.length}`);
const inventory = await deck.inspect({ kind: "slide,textbox,table,notes", maxChars: 120000 });
const files = [guidePath, storageLabPath, queryLabPath, resourcesPath];
const text = [inventory.ndjson, ...(await Promise.all(files.map((p) => fs.readFile(p, "utf8"))))].join("\n").toLowerCase();
const required = [
  "data lake", "lakehouse", "data warehouse", "data mart",
  "storage and compute", "hot", "warm", "cold", "archive",
  "schema-on-read", "query-in-place", "soft delete", "versioning",
  "raw", "quarantine", "processed", "curated"
];
for (const phrase of required) if (!text.includes(phrase)) throw new Error(`Missing required concept: ${phrase}`);
if (text.includes("bigquery and athena are the same")) throw new Error("Over-broad Athena/BigQuery equivalence remains");
console.log("PASS: 22-slide deck and aligned Day 4 artifacts contain all required concepts");
```

- [ ] **Step 4: Verify the acceptance script is red**

Run the script with the five final artifact paths.

Expected: failure because `W1D4 - Data at Rest - Updated.pptx` and the query-in-place lab do not exist.

### Task 2: Rewrite the Instructor Guide Around the New Day Narrative

**Files:**
- Modify: `Week 1/Instructor Notes/Day 4 - Instructor Guide.md`

- [ ] **Step 1: Replace the objectives and schedule**

Use the six approved learning objectives and the exact schedule from the design specification. The section sequence must be:

```text
Day purpose and learning objectives
Pre-class account and permissions checklist
8:30–12:00 teaching guide
1:00–2:40 Cloud Storage landing-zone lab
2:50–3:30 query-in-place mini-lab
3:30–4:15 team storage-convention activity
4:15–4:45 Day 5 handoff
4:45–5:00 exit ticket
Fallbacks and troubleshooting
Answer key and expected observations
Official references
```

- [ ] **Step 2: Add the pre-class readiness checklist**

Require the instructor to verify:

```text
course project IDs are assigned
billing is enabled for course-managed projects
Cloud Storage and BigQuery APIs are available
learners can authenticate with gcloud and select the assigned project
learners can create/manage assigned buckets or a prepared shared fallback exists
learners can create a BigQuery dataset/external table or the instructor demo fallback is ready
the signed-URL service account and signBlob permission are available only if the optional extension is taught
```

- [ ] **Step 3: Add teaching prompts and Week 3 boundaries**

Include these prompts:

```text
Can one company use a lake, lakehouse, warehouse, and data mart at the same time? Why?
What changes when ten compute clusters can read the same durable storage?
Would you store a dashboard extract and a seven-year compliance archive in the same tier?
What information must a query engine know before it can interpret a CSV or Parquet object?
```

Explicitly defer ETL/ELT architecture, star/snowflake schemas, detailed ACID table formats, and warehouse physical design to Week 3.

- [ ] **Step 4: Replace the repeated full demo with a 20-minute preflight demo**

The demo must show only authentication, project selection, one private bucket/object, one object-inspection screen, and one query estimate. It must stop before lifecycle/versioning steps that learners perform in the lab.

- [ ] **Step 5: Add fallbacks, answer key, and exit ticket**

Document three fallbacks: instructor-shared bucket, view-only screenshots/results, and paired execution. Add expected observations for private access, prefixes, lifecycle, version restoration, schema-on-read, and bytes processed. Use this exit ticket:

```text
1. Explain one difference between a data lake and a data warehouse without naming a vendor product.
2. Why can separating storage and compute improve flexibility, and what new responsibility does it create?
3. Choose one control for accidental deletion and one control for compliance retention; explain the difference.
```

- [ ] **Step 6: Validate guide structure**

Run:

```bash
rg -n 'Pre-class|8:30|2:50|query-in-place|Week 3|Fallback|Answer key|Exit ticket' "Week 1/Instructor Notes/Day 4 - Instructor Guide.md"
```

Expected: every required section is found and the time blocks match the design specification.

### Task 3: Correct and Strengthen the Cloud Storage Landing-Zone Lab

**Files:**
- Modify: `Week 1/Labs/Day 4/Activity_Cloud_Object_Storage.md`

- [ ] **Step 1: Align metadata, duration, and outcomes**

Set the required lab to `100 minutes`, identify it as the core Day 4 activity, and list outcomes for secure object storage, zone/prefix design, lifecycle, recovery controls, and cross-cloud translation.

- [ ] **Step 2: Add a deterministic preflight**

Include copy/paste commands:

```bash
gcloud auth list
gcloud config set project YOUR_ASSIGNED_PROJECT_ID
gcloud config get-value project
gcloud services list --enabled --filter='name:(storage.googleapis.com OR bigquery.googleapis.com)'
```

Tell learners to stop and use the instructor fallback if the assigned account/project or required role is missing. Do not tell them to attach personal billing.

- [ ] **Step 3: Make access controls internally consistent**

Keep public access prevention and uniform bucket-level access enabled. Replace any instruction to make an object public with authenticated access testing and an incognito `AccessDenied` observation. Keep partner sharing at bucket/prefix-compatible IAM scope supported by the chosen instructions.

- [ ] **Step 4: Add prediction and reflection prompts**

Place a `Predict` question before public-access testing, lifecycle activation, object overwrite, and restore. Place an `Observe and explain` question after each action. Questions must be answerable from observed behavior rather than memorized syntax.

- [ ] **Step 5: Distinguish data-protection controls**

Add this conceptual table:

| Control | Primary purpose | Can normal deletion still occur? | Typical use |
| :--- | :--- | :--- | :--- |
| Lifecycle rule | Automate transition or deletion | Yes | Cost and housekeeping |
| Soft delete | Recover recently deleted objects | Deletion creates recoverable state | Accidental deletion recovery |
| Versioning | Preserve overwritten/deleted generations | Yes, with versions retained | Change recovery |
| Retention policy | Prevent deletion before an age | No | Minimum retention |
| Bucket Lock | Make retention policy irreversible | No | Regulated/compliance data |

- [ ] **Step 6: Move signed URLs out of the core path**

Label signed URLs optional. State that signing requires appropriate credentials, commonly a service account with permission to sign blobs, and provide an instructor-readiness check rather than assuming every learner can generate one.

- [ ] **Step 7: Strengthen the team design deliverable and answer key**

Require raw/quarantine/processed/curated zones, Hive-style date keys, file format by zone, late/duplicate/malformed handling, lifecycle tiers, zone-level access, one external-query use case, and one warehouse use case. Add an instructor answer key for all numbered questions and a plausible reference design.

- [ ] **Step 8: Validate risky language and prerequisites**

Run:

```bash
rg -n '100 minutes|gcloud auth list|public access prevention|soft delete|Versioning|Bucket Lock|Predict|Answer key|quarantine|curated' "Week 1/Labs/Day 4/Activity_Cloud_Object_Storage.md"
rg -ni 'make .*public|disable public access prevention|personal billing' "Week 1/Labs/Day 4/Activity_Cloud_Object_Storage.md" && exit 1 || true
```

Expected: required markers exist and contradictory/public-billing instructions do not.

### Task 4: Create the Required Query-in-Place Mini-Lab

**Files:**
- Create: `Week 1/Labs/Day 4/Activity_Query_in_Place_with_BigQuery.md`
- Modify: `Week 1/Labs/Day 4/Student_Resources.md`

- [ ] **Step 1: Create a 40-minute guided activity with a permission-safe design**

Use this structure:

```text
Purpose and learning outcomes
Concept checkpoint: schema-on-read and query-in-place
Permission preflight and instructor fallback
Part 1: inspect yellow_trip_sample.csv in Cloud Storage
Part 2: review/create a BigQuery external table
Part 3: run supplied SELECT and aggregation queries
Part 4: compare bytes processed and identify limitations
Part 5: choose external query or loaded curated table
Submission and answer key
```

- [ ] **Step 2: Provide copy/paste SQL with beginner reasoning prompts**

Include SQL equivalent to:

```sql
CREATE OR REPLACE EXTERNAL TABLE `PROJECT_ID.day4_external.yellow_trip_sample`
OPTIONS (
  format = 'CSV',
  uris = ['gs://BUCKET_NAME/raw/taxi/yellow_trip_sample.csv'],
  skip_leading_rows = 1,
  autodetect = TRUE
);

SELECT *
FROM `PROJECT_ID.day4_external.yellow_trip_sample`
LIMIT 10;

SELECT payment_type, COUNT(*) AS trip_count
FROM `PROJECT_ID.day4_external.yellow_trip_sample`
GROUP BY payment_type
ORDER BY trip_count DESC;
```

Before each query, ask learners to predict what metadata or data must be read. After each query, ask them to record schema observations, bytes processed, and one limitation of querying CSV externally.

- [ ] **Step 3: Add explicit decision guidance**

Use this decision rule:

```text
Query in place when data is exploratory, infrequently queried, shared with another engine, or not yet ready for curation.
Load/transform into managed warehouse tables when queries are repeated, performance matters, governance requires a stable schema, or downstream BI depends on consistent results.
```

State that BigQuery external tables and Athena both support serverless SQL over external data and scan-related cost awareness, but BigQuery is also a managed analytical warehouse while Athena primarily queries data in S3.

- [ ] **Step 4: Add the no-permission fallback**

Provide a table containing the expected external schema, representative query output, and sample bytes-processed observations. Learners using the fallback must still answer the prediction, limitation, and architecture-choice questions.

- [ ] **Step 5: Update Student Resources**

Add the required query-in-place activity to the Day 4 order before the optional Athena and Bucket Lock extensions. Add concise glossary entries for external table, schema-on-read, prefix, lifecycle, soft delete, versioning, retention, lake, lakehouse, warehouse, and mart.

- [ ] **Step 6: Validate the mini-lab and resources**

Run:

```bash
rg -n '40 minutes|CREATE OR REPLACE EXTERNAL TABLE|autodetect|bytes processed|fallback|Query in place|managed warehouse' "Week 1/Labs/Day 4/Activity_Query_in_Place_with_BigQuery.md"
rg -n 'Activity_Query_in_Place_with_BigQuery|schema-on-read|lakehouse|retention' "Week 1/Labs/Day 4/Student_Resources.md"
```

Expected: all required activity and glossary markers exist.

### Task 5: Map and Build the Updated 22-Slide Deck

**Files:**
- Read: presentation skill `artifact_tool/API_QUICK_START.md`
- Read: presentation skill `artifact_tool/api/API_DOCS.md`
- Read: presentation skill `references/template-following.md`
- Create: `$TMP_DIR/template-audit.txt`
- Create: `$TMP_DIR/template-frame-map.json`
- Create: `$TMP_DIR/deviation-log.txt`
- Create: `$TMP_DIR/source-notes.txt`
- Create: `$TMP_DIR/template-starter.pptx`
- Create: `$TMP_DIR/build_w1d4_data_at_rest.mjs`
- Create: `Week 1/Slides/W1D4 - Data at Rest - Updated.pptx`

- [ ] **Step 1: Inspect all 11 source slides**

Run:

```bash
node "$SKILL_DIR/template_following_scripts/inspect_template_deck.mjs" \
  --workspace "$TMP_DIR" \
  --pptx "$SOURCE"
```

Expected: an 11-slide manifest, layout JSON for every source slide, and preview images.

- [ ] **Step 2: Build the frame map for the approved 22-slide sequence**

Map every output slide to the closest source layout. Preserve the source title, typography, palette, footer, and page-number treatment. The narrative roles must be exactly:

```text
title; why it matters; objectives/day map; pipeline placement;
four architectures; choosing architectures; storage/compute separation;
cross-cloud object storage; object-storage mental model; file formats;
row versus columnar; compression/small files; landing zones;
prefix conventions; bad/late/duplicate data; schema-on-read/write;
query-in-place; lifecycle tiers; protection-control comparison;
core lab; query/team activity; Day 5 handoff/recap/exit
```

Populate every `editTargets` entry from stable inherited object IDs, then validate with `validate_template_plan.mjs`.

- [ ] **Step 3: Generate and inspect the 22-slide starter**

Run `prepare_template_starter_deck.mjs` with the validated map. Assert 22 preview PNGs and no visible default placeholder prompts.

- [ ] **Step 4: Implement the authoring module**

Import `$TMP_DIR/template-starter.pptx` with `PresentationFile.importPptx`, resolve inherited objects by stable IDs, rewrite only mapped targets, add speaker notes, and export to the final path. Do not use `python-pptx` and do not create a second visual theme.

- [ ] **Step 5: Author slides 1–9**

Use the exact narrative and architecture definitions from the approved design. Slide 7 must say that object storage enables durable independent storage and modern engines can scale compute independently; it must not claim separation created S3/GCS/Blob Storage. Slide 8 gives equal GCP/AWS weight and a single Azure terminology translation.

- [ ] **Step 6: Author slides 10–17**

Cover CSV/JSON/Parquet/Avro, row versus columnar access, compression and small files, raw/quarantine/processed/curated zones, Hive-style date paths, late/duplicate/malformed handling, schema-on-read/write, and external query-in-place. Keep SQL off the conceptual slides; the activity contains the copy/paste SQL.

- [ ] **Step 7: Author slides 18–22**

Use hot/warm/cold/archive and qualify “frozen” as informal. Compare lifecycle, soft delete, versioning, retention, lock, and holds. Brief the 100-minute core lab and 40-minute query activity, then end with the NYC Taxi Day 5 handoff and the three-question exit ticket.

- [ ] **Step 8: Add notes and official sources**

Every new conceptual slide must include:

```text
Teaching point:
Learner question:
Teach now / defer:
Sources:
```

Use only the official Google Cloud, AWS, and Microsoft URLs listed in the design specification and record them in `$TMP_DIR/source-notes.txt`.

- [ ] **Step 9: Export and run the cross-artifact acceptance check**

Run the authoring module, then `$TMP_DIR/check_w1d4_final.mjs` with the final PPTX, guide, two required labs, and Student Resources.

Expected: `PASS: 22-slide deck and aligned Day 4 artifacts contain all required concepts`.

### Task 6: Verify Cross-Artifact Alignment and Optional-Lab Positioning

**Files:**
- Verify: all revised Day 4 Markdown artifacts
- Verify: `Week 1/Labs/Day 4/Activity_Stretch_Athena_over_S3.md`
- Create: `$TMP_DIR/qa/alignment.txt`

- [ ] **Step 1: Audit terminology and timing**

Record deck/guide/lab duration and order in `$TMP_DIR/qa/alignment.txt`. Required order must be Cloud Storage lab, BigQuery query-in-place mini-lab, team design; Athena joins, Athena over S3, and Bucket Lock remain optional.

- [ ] **Step 2: Scan for known conceptual regressions**

Run:

```bash
rg -ni 'BigQuery and Athena are the same|frozen storage class|storage.compute separation (created|gave us)|make .*public|personal billing' "Week 1/Instructor Notes/Day 4 - Instructor Guide.md" "Week 1/Labs/Day 4" && exit 1 || true
```

Expected: no matches.

- [ ] **Step 3: Verify Week 3 boundary and Day 5 handoff**

Confirm the guide/deck defer dimensional modeling and deeper lakehouse mechanics to Week 3 and use the NYC Taxi storage layout as the Day 5 bridge.

### Task 7: Render, Inspect, and Repair Every Slide

**Files:**
- Create: `$TMP_DIR/preview/final/slide-*.png`
- Create: `$TMP_DIR/layout/final/slide-*.layout.json`
- Create: `$TMP_DIR/preview/final-contact-sheet.png`
- Create: `$TMP_DIR/qa/final-qa.txt`

- [ ] **Step 1: Render all slides and extract layout reports**

Use artifact-tool to render 22 PNGs, produce 22 layout JSON files, and create a contact sheet.

Expected: exactly 22 files of each slide-specific type.

- [ ] **Step 2: Run automated checks**

Check for text overflow, clipping, unintended overlaps, unresolved placeholders, title wrapping, missing footers/page numbers, inconsistent fonts, and unequal GCP/AWS comparison geometry. Record each slide's result in `$TMP_DIR/qa/final-qa.txt`.

- [ ] **Step 3: Inspect every slide visually**

Inspect the contact sheet and every slide at full size. Pay particular attention to slides 5–8, 10–19, and 22. Shorten text or change inherited layout choice instead of shrinking body fonts below the source template size.

- [ ] **Step 4: Repair and rerender until clean**

Modify only `$TMP_DIR/build_w1d4_data_at_rest.mjs`, re-export, and rerender after each repair batch. Finish only when all automated and visual findings are resolved or explicitly documented as intentional.

- [ ] **Step 5: Run template fidelity validation**

Run `check_template_fidelity.mjs` against the starter and final deck. Expected: pass with only intentional edits listed in `$TMP_DIR/deviation-log.txt`.

### Task 8: Final Verification and Delivery

**Files:**
- Verify: all five final Day 4 artifacts
- Verify: `$TMP_DIR/qa/source.sha256`
- Verify: `$TMP_DIR/qa/final-qa.txt`
- Verify: `$TMP_DIR/qa/alignment.txt`

- [ ] **Step 1: Run final gates from a clean import**

Run:

```bash
node "$TMP_DIR/check_w1d4_final.mjs" \
  "$FINAL" \
  "$PWD/Week 1/Instructor Notes/Day 4 - Instructor Guide.md" \
  "$PWD/Week 1/Labs/Day 4/Activity_Cloud_Object_Storage.md" \
  "$PWD/Week 1/Labs/Day 4/Activity_Query_in_Place_with_BigQuery.md" \
  "$PWD/Week 1/Labs/Day 4/Student_Resources.md"
shasum -a 256 -c "$TMP_DIR/qa/source.sha256"
test "$(find "$TMP_DIR/preview/final" -name 'slide-*.png' | wc -l | tr -d ' ')" = 22
test "$(find "$TMP_DIR/layout/final" -name 'slide-*.layout.json' | wc -l | tr -d ' ')" = 22
test -s "$TMP_DIR/qa/final-qa.txt"
test -s "$TMP_DIR/qa/alignment.txt"
```

Expected: acceptance passes, original deck checksum reports `OK`, and all QA evidence exists.

- [ ] **Step 2: Inspect repository status without staging unrelated work**

Run `git status --short`. Do not revert or stage unrelated user files.

- [ ] **Step 3: Deliver the revised module**

Report the updated PPTX, instructor guide, corrected core lab, new query-in-place lab, key conceptual changes, official source families, and verification result. Cite the final PPTX as a presentation artifact and link the Markdown files with absolute workspace paths.

