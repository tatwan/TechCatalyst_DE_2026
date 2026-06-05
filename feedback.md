# TechCatalyst DE 2026 — Curriculum Evaluation & Recommendations

## Executive Summary

The revised outline is a significant improvement over the first draft. The most critical sequencing errors from the initial version have been resolved: DataOps is no longer in Week 1, GenAI libraries no longer compete with pandas in Week 2, Vertex AI has been moved out of Week 3, and analytical SQL now sits in Week 4 where it belongs. The structure is credible and can work. What remains are several refinements that will determine whether the 7 weeks of learning genuinely *pays off* in Week 8 for junior DE professionals in an insurance context.

***

## Week-by-Week Evaluation

### Week 1 — Data & Cloud Foundations ✅ Solid

This week is well structured. Days 1–2 cover essential mental models, Day 3 does environment setup (a smart fix from the first draft), and Days 4–5 are lab-focused. For a student who may have only done internship-level DE work, starting with "what is this industry and how do I set up my environment" is exactly right.

**One concern:** Day 5's deliverable — a data flow diagram in Draw.io — is conceptual, which is fine for Week 1. But consider explicitly tying it to insurance. Give students a skeleton insurance scenario (e.g., *claims data arrives from an external broker, needs to land in a data warehouse, and feed a dashboard for actuaries*). That narrative thread through all 8 weeks will make the capstone feel like a continuation, not a surprise.

***

### Week 2 — Architecture, Linux, Python ⚠️ One Structural Issue

Days 1–3 are logical: architecture concepts → Linux/terminal → Git/GitHub. These belong together as "developer foundations."

**The problem is Day 4.** You have: *pandas, polars, Dask* — three different DataFrame libraries in one day. For a junior DE with 1-2 years of experience, this is too wide. Polars and Dask are not the same category as pandas; they're pandas *alternatives for scale*, and introducing them on the same day before students have even done a pipeline hands-on creates confusion about when to use what.

**Recommendation:** Day 4 should be **pandas only** — reading from files, REST APIs (add `requests` here), writing to GCS. That directly sets up the deliverable (Python script → GCS). Introduce **polars** as a 30-minute comparison on Day 5 alongside the AWS orientation demo. Drop **Dask** entirely from Week 2 — it belongs in Week 3 or 5 alongside "scaling Python" discussion, or omit it given the GCP/Spark-first direction.

**The deliverable** (Python script that pulls from a public API and lands in GCS) is well-chosen — concrete, testable, directly relevant to DE work. Keep it.

***

### Week 3 — Modern GCP Data Engineering ⚠️ SQL Placement Needs Reconsideration

The addition of Cloud Composer (Day 5) and the SQL Primer (Day 2) are both good moves from the previous draft. However, there is a sequencing tension: the deliverable is **Pub/Sub → Dataflow → BigQuery**, but students don't see BigQuery SQL until Day 3, *after* the pipeline is introduced conceptually on Day 1. This means on Day 2 they're doing SQL in a vacuum without yet knowing what BigQuery is.

**Recommendation:** Swap Days 2 and 3:
- Day 2: BigQuery intro (datasets, tables, partitioning, cost) — establish the target
- Day 3: SQL Primer anchored in BigQuery — query the tables they just created
- Days 4–5: Dataflow + Pub/Sub, then Composer/IAM

This makes the learning arc logical: "here's where data lands → here's how you query it → here's how you build the pipeline that fills it."

**Day 5 (Cloud Composer + IAM)** is slightly overloaded but workable if Composer is kept at the conceptual + demo level (a DAG that triggers a GCS → BigQuery load), and IAM is covered as a 90-minute block. Don't lab both on the same day.

***

### Week 4 — Snowflake, dbt & Advanced SQL ✅ Best Week in the Outline

This is the strongest week. The progression is clean:
1. Snowflake architecture (Day 1) → understand the platform
2. Advanced SQL in Snowflake/BigQuery (Day 2) → build the analytical skills
3. dbt Core (Day 3) → learn the transformation tool
4. Advanced dbt (Day 4) → go deeper
5. Snowflake Cortex AI (Day 5) → first taste of AI on real data

The cost optimization callout (warehouse sizing, table types, views) is an excellent addition — this is exactly what separates junior DEs who build things from junior DEs who build things that run up $50K cloud bills in production. It belongs on **Day 1** (Snowflake architecture) and **Day 2** (where query performance directly impacts cost).

**One gap:** The dbt section doesn't mention **data testing** explicitly (i.e., `dbt test`, `schema.yml` assertions, `great_expectations` integration). For an insurance client, data quality testing isn't optional — actuarial data feeding dashboards or ML models must be validated. Add at least half a day of explicit dbt testing + data quality checks.

**The deliverable** (dbt project on Snowflake with a Cortex AI-enriched model) is excellent — it's the most "real job" deliverable of the first 4 weeks.

***

### Week 5 — NLP, LLMs, GenAI & GitHub Copilot ⚠️ Vertex AI Still Underanchored

The GenAI Fundamentals → APIs → Vertex AI → Gemini lab → Copilot arc is logical. The optional topics note (Snowpark, Advanced Snowflake ML) is a good safety valve.

**The main structural issue:** Day 3 (Vertex AI overview + AutoML demo) and Day 4 (Gemini API + Vertex AI GenAI lab) are covering the same platform on consecutive days with different focal points. Students will conflate AutoML (training models) with Gemini API (calling hosted LLMs). These are genuinely different things, and the confusion will surface in the capstone when students try to use Vertex AI for something and don't know which service to reach for.

**Recommendation:** Be explicit about the distinction:
- **Day 3:** Vertex AI as an *MLOps/AutoML platform* — how a DE hands off a dataset for model training, monitoring, prediction serving. Tie it to insurance: *"You built the claims pipeline. The data scientist trains a fraud detection model in Vertex AI AutoML. Your job is to feed it clean data and consume the predictions."*
- **Day 4:** Vertex AI as a *Generative AI platform* — Gemini API for text classification, summarization, embeddings. Lab: summarize insurance claim notes using Gemini API.

This framing also answers the "what does a DE do with AI" question — you're the plumbing, not the model builder.

**GitHub Copilot (Day 5):** This is well placed at the end of the week. By this point students have written real Python (Week 2), SQL (Weeks 3–4), and seen GenAI concepts. They can now engage meaningfully with Copilot, not just marvel at autocomplete. Focus the session on: inline suggestions, chat for debugging, agent mode for scaffolding a new pipeline, and — critically — **reviewing what Copilot generates** rather than blindly accepting it. This directly addresses the "kids don't code" risk.

***

### Week 6 — Governance, Best Practices & CI/CD ⚠️ Redundancy Between Days 3 and 4

The overall theme is right and the placement (post-build, pre-BI) is correct. But Days 3 and 4 overlap significantly:

- Day 3: *GitHub Actions for dbt runs, data tests, auto-deploy pipelines*
- Day 4: *DataOps — CI/CD for data, data quality principles, observability*

Both are CI/CD for data. DataOps on Day 4 should be the conceptual framing, and GitHub Actions on Day 3 should be the implementation. Running implementation before concepts creates the same sequencing issue we're fixing elsewhere.

**Recommendation:** Swap them:
- Day 3: **DataOps concepts** — the *why* of CI/CD for data, data quality manifesto, observability principles, what "done" looks like for a data pipeline in production
- Day 4: **GitHub Actions implementation** — *now* build the workflow that proves you understand Day 3's principles

**Day 5** (GitHub collaboration + AWS equivalents demo) is fine. The AWS equivalents demo (Redshift, Glue, SageMaker) is a useful "you'll encounter this in the wild" framing — keep it brief.

**One missing topic for insurance:** **Data lineage and PII handling**. Dataplex (Day 2) covers cataloging, but insurance data contains PHI/PII. Even a 45-minute segment on: tagging PII columns in BigQuery/Snowflake, column-level masking, audit logging — would be directly relevant to the client's industry and gives students a concrete governance skill they'll use on Day 1 of the job.

***

### Week 7 — BI Tools ✅ Better, But Thoughtspot is Orphaned

Moving data storytelling principles to Day 1 before any tool is smart — students need to know *why* before *how*. Looker on Day 2 with a BigQuery-connected hands-on lab is strong and directly ties to the Week 3 pipeline deliverable.

**The problem is Thoughtspot.** It's not in the Day-by-Day table at all — it appears only in the tech stack summary. If Thoughtspot is in scope, it needs a day. If it's not confirmed, remove it from the tech stack table to avoid confusion.

**Day 4 (TBD/Strategy):** The uncertainty here is reasonable given client TBD status. Suggest having a fallback plan ready: if Strategy isn't confirmed two weeks before the bootcamp, use Day 4 as **Looker advanced / LookML deep dive** (calculated fields, data actions, scheduling) rather than introducing a fourth tool that may never appear in students' jobs.

**The deliverable** (Looker dashboard connected to BigQuery Week 3 data) is clean and directly verifiable. Good choice.

***

### Week 8 — Capstone ✅ Architecture is Right, Pacing Needs Attention

The capstone arc is well designed: ingest → transform → enrich → visualize → present. The insurance use case is industry-relevant and gives the client a concrete artifact to evaluate student readiness.

**Pacing concerns by day:**

| Day | Task | Risk |
|-----|------|------|
| Day 1 | Architecture design + role assignments | ✅ Good start — this sets direction |
| Day 2 | GCS → Dataflow → BigQuery ingestion sprint | ⚠️ Dataflow is complex; teams may need more time |
| Day 3 | Snowflake + dbt + data quality checks | ✅ Well-scoped if dbt was practiced in Week 4 |
| Day 4 | Cortex AI enrichment + Looker/Tableau dashboards | ⚠️ Two distinct deliverables in one day |
| Day 5 | Final presentations | ✅ |

**Recommendation for Day 2:** Give teams a pre-built Dataflow template (a parameterized Apache Beam pipeline) rather than asking them to build from scratch. The goal of the capstone is integration, not re-teaching pipeline authoring. This frees up time for the harder conceptual work on Days 3–4.

**Recommendation for Day 4:** Split the work explicitly: one sub-team owns the GenAI layer (Cortex/Gemini enrichment); another owns the BI layer. They connect at the end. This mirrors real team dynamics in insurance data teams and teaches students to work with handoff points — a skill Week 6's DataOps content should prime them for.

***

## Capstone Payoff Analysis: Do the 7 Weeks Deliver?

The test of the curriculum is whether a junior DE can successfully contribute to Week 8. Here is the skill-to-capstone mapping:

| Capstone Task | Skills Required | Covered In | Readiness |
|---|---|---|---|
| Design data architecture diagram | DE concepts, GCP services overview | Week 1, 3 | ✅ Yes |
| Ingest data to GCS | Python, GCS, REST APIs | Week 2 | ✅ Yes |
| Build Dataflow pipeline | GCP Dataflow, Pub/Sub | Week 3 | ⚠️ One lab — may need scaffold |
| Write BigQuery SQL | SQL (primer + advanced) | Week 3, 4 | ✅ Yes |
| Build dbt models + tests | dbt Core + Advanced | Week 4 | ✅ Yes |
| Load to Snowflake + transform | Snowflake architecture + SQL | Week 4 | ✅ Yes |
| Apply Cortex AI enrichment | Snowflake Cortex LLM functions | Week 4 (Day 5) | ⚠️ One lab — limited practice |
| Build Looker dashboard | Looker + LookML | Week 7 | ✅ Yes |
| Use GitHub + CI/CD for delivery | Git, GitHub Actions, branching | Weeks 2, 6 | ✅ Yes |
| Apply data quality + governance | dbt tests, Dataplex, DataOps | Weeks 4, 6 | ✅ Yes |
| Use GitHub Copilot during build | Copilot setup + modes | Week 5 | ✅ Yes |

**Two weak points stand out:**
1. **Dataflow** — students see it once in Week 3. The capstone requires them to build a real pipeline with real insurance data. Consider assigning a Dataflow take-home mini-lab during Week 6 or making the Week 3 pipeline deliverable more substantial.
2. **Cortex AI** — one hands-on lab in Week 4, Day 5. The capstone uses it for enrichment. This is manageable only if the capstone provides a working Cortex function template they customize, rather than requiring students to build it from scratch.

***

## 2026 Relevance: Skills the Insurance Industry Actually Needs

Junior DEs hired into insurance in 2026 will be working in an environment shaped by several specific pressures:[^1]

- **Regulatory data requirements** — IFRS 17, Solvency II, and state-level data reporting mandates require auditable data lineage and governance. The Week 6 Dataplex + DataOps content is directly aligned with this.
- **Cloud migration** — Most major insurers are mid-migration to GCP or AWS. The GCP-first framing matches what students will encounter.
- **AI for claims and underwriting** — LLM-based document processing (claim notes, policy documents) is a growing use case. The Gemini API + Cortex Document AI content in Weeks 4–5 is exactly on-target.
- **Self-service analytics pressure** — Finance and actuarial teams increasingly want Looker-style self-service rather than waiting for BI reports. Week 7's Looker content prepares students to build what those teams need.
- **GitHub Copilot adoption** — Enterprise GitHub Copilot adoption is accelerating across financial services. Teaching it in the context of DE workflows (not just generic autocomplete) gives students a professional differentiator.

***

## Summary Recommendations Table

| Week | Issue | Action |
|---|---|---|
| Week 2, Day 4 | Pandas + Polars + Dask in one day | Pandas only on Day 4; brief Polars on Day 5; remove Dask |
| Week 3, Days 2–3 | SQL before BigQuery context | Swap: BigQuery first (Day 2), SQL anchored in BigQuery (Day 3) |
| Week 4, Days 1–2 | Cost optimization buried | Explicitly call out cost in Day 1 (warehouse sizing) and Day 2 (query cost) |
| Week 4, Day 3 | dbt testing not explicit | Add half-day on `dbt test`, schema assertions, data quality checks |
| Week 5, Days 3–4 | AutoML vs Gemini conflation | Explicitly distinguish: AutoML = train models; Gemini = call LLMs |
| Week 6, Days 3–4 | CI/CD before DataOps concepts | Swap: DataOps concepts Day 3, GitHub Actions Day 4 |
| Week 6, Day 2 | No PII/PHI coverage | Add 45 min on column masking, PII tagging, audit logs (insurance-critical) |
| Week 7 | Thoughtspot orphaned | Add it as a day or remove from tech stack table entirely |
| Week 8, Day 2 | Dataflow from scratch is risky | Provide pre-built Dataflow template; focus on integration, not authoring |
| Week 8, Day 4 | Two deliverables in one day | Split: sub-team on GenAI layer, sub-team on BI layer — connect at end |

***

## One Framing Recommendation

Consider introducing the insurance use case **in Week 1, Day 5** when students build their first data flow diagram. Give them the capstone dataset schema early — not for analysis, just for context. Every week's deliverable can then be framed as a piece of the same puzzle:

- Week 2: *"Pull claims data from this mock API and land it in GCS"*
- Week 3: *"Build a BigQuery table for this claims schema"*
- Week 4: *"Write dbt models that transform raw claims into a clean analytical layer"*
- Week 5: *"Use Gemini API to classify claim severity from free-text notes"*
- Week 6: *"Add CI/CD so your dbt tests run automatically on every push"*
- Week 7: *"Build an actuary-facing Looker dashboard from your BigQuery data"*

This longitudinal threading turns 7 separate weeks into one continuous project. When students arrive at Week 8, they aren't starting from zero — they're polishing and integrating work they've already built. For junior DEs who may be anxious about the capstone, this dramatically reduces cognitive load and dramatically increases the quality of the final output.

---

## References

1. [Course-Outline.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/233624/b6053e20-fe90-4224-b6d6-9ad26d683d07/Course-Outline.md) - # **2024 Tech Catalyst Data Engineer Curriculum Overview**

## High Level Planning

* Incorporate da...

