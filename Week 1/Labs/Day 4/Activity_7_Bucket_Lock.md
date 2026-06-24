# Week 1 · Day 4 Optional: Bucket Lock and Retention (Compliance)

**Duration:** ~25 min  
**Format:** Individual optional, after Part 3 of the core GCS lab  
**Prerequisites:** Course GCP project with billing; Cloud Shell or authenticated `gcloud`

> [!IMPORTANT]
> **Use a separate demo bucket**, do not lock retention on your `-raw` landing-zone bucket. Retention lock is **permanent** once applied. This lab uses `techcatalyst-de-2026-<your-username>-retention-demo`.

> [!NOTE]
> **Console first, here too.** Each step below leads with the **Console** (the Protection tab is where retention, lock, and holds live). A **💻 Also via CLI** box follows each one — and for this lab the CLI is genuinely handy because the demo uses a 60-second retention you can watch expire. Use whichever you prefer; the concepts are identical. **Run the CLI boxes in Cloud Shell** (already signed in, `gcloud` preinstalled) — they won't work in a local or Codespaces terminal unless you set up the CLI yourself.

***

## Why this optional lab exists

Part 3's lifecycle rule (Q6) handles *cost-driven* tiering and deletion timing. **Bucket Lock** handles *compliance-driven* immutability, regulators can require that records cannot be deleted early, even by an admin.

At The Hartford, raw claims and policy files often have **7-year minimum retention**. Lifecycle rules move data to cheaper classes; retention policies **prevent premature deletion**. Both can apply to the same bucket.

This is optional because it is a specialization on top of today's landing-zone lab, not required for the Day 4 deliverable.

***

## Part 1: Create a demo bucket (~5 min)

In the Console: **Cloud Storage → Buckets → Create**. Name it `techcatalyst-de-2026-<your-username>-retention-demo`, Region `us-east1`, **Uniform** access. Then upload a small test file (`Lab Resources/intro.docx`) into a `records/` prefix and rename it `claim_001.docx` (or upload it and note its path).

> [!NOTE]
> **💻 Also via CLI (optional) — in Cloud Shell.**
>
> ```bash
> export DEMO_BUCKET=techcatalyst-de-2026-<your-username>-retention-demo
> gcloud storage buckets create gs://${DEMO_BUCKET} \
>   --location=us-east1 --uniform-bucket-level-access
> gcloud storage cp "Lab Resources/intro.docx" gs://${DEMO_BUCKET}/records/claim_001.docx
> ```

## Part 2: Set a retention policy (~10 min)

Regulators often require multi-year retention. For the lab we use **60 seconds** so you can see expiration without waiting years.

In the Console: open the demo bucket → **Protection** tab → **Set retention policy**. Enter **60** and choose **Seconds** (use the smallest unit available). Save.

**Q1:** What does the Protection tab show for the retention period and its effective time? In plain English: when can this object be deleted?

Now try to delete `claim_001.docx` **before** it expires: open the object (or select it in the list) → **Delete**. It should be blocked.

**Q2:** What error/message do you get? Paste it into `day4_lab.md`.

> [!NOTE]
> **💻 Also via CLI (optional)** — and the easiest way to read the exact expiration timestamp:
>
> ```bash
> gcloud storage buckets update gs://${DEMO_BUCKET} --retention-period=60s
> gcloud storage buckets describe gs://${DEMO_BUCKET} --format="yaml(retention_policy)"
> gcloud storage ls -L gs://${DEMO_BUCKET}/records/claim_001.docx   # look for Retention Expiration
> gcloud storage rm gs://${DEMO_BUCKET}/records/claim_001.docx       # blocked before expiry
> ```

## Part 3: Lock the policy (~5 min)

While **unlocked**, you can shorten or remove a retention policy. **Locking** is permanent, the duration can only be *extended*, never reduced or removed.

In the Console: demo bucket → **Protection** tab → **Lock** the retention policy. Read the warning carefully and confirm (this is irreversible).

**Q3:** What changed on the Protection tab after locking? Why would a compliance officer want this locked state?

> [!NOTE]
> **💻 Also via CLI (optional) — in Cloud Shell.**
>
> ```bash
> gcloud storage buckets update gs://${DEMO_BUCKET} --lock-retention-period
> gcloud storage buckets describe gs://${DEMO_BUCKET} --format="yaml(retention_policy)"
> ```

## Part 4: Temporary hold (~5 min)

A **temporary hold** pauses deletion during an audit, even if the retention period has expired.

In the Console: open `claim_001.docx` → its action menu (⋮) → **Set temporary hold**. Try to **Delete** it (blocked while the hold is active), then **Release temporary hold**.

**Q4:** How is a **temporary hold** different from a **retention policy**? One sentence each.

> [!NOTE]
> **💻 Also via CLI (optional) — in Cloud Shell.**
>
> ```bash
> gcloud storage objects update gs://${DEMO_BUCKET}/records/claim_001.docx --temporary-hold
> gcloud storage rm gs://${DEMO_BUCKET}/records/claim_001.docx          # blocked while held
> gcloud storage objects update gs://${DEMO_BUCKET}/records/claim_001.docx --no-temporary-hold
> ```

> [!NOTE]
> **Event-based holds** (start retention countdown when a loan is "paid off," etc.) exist but are niche. Read about them in [GCS object holds](https://cloud.google.com/storage/docs/object-holds) if curious, not required for Day 4.

## Success criteria

- [ ] Demo bucket created (separate from `-raw`)
- [ ] 60s retention policy set and verified
- [ ] Early delete blocked (Q2 error captured)
- [ ] Retention policy locked
- [ ] Temporary hold demonstrated
- [ ] Q1 to Q4 in `day4_lab.md`

## Cleanup

Wait 60+ seconds after releasing any holds, then:

```bash
gcloud storage rm gs://${DEMO_BUCKET}/records/claim_001.docx
gcloud storage buckets delete gs://${DEMO_BUCKET}
```

> [!WARNING]
> You **cannot** delete a bucket that still has objects under an active retention period. If cleanup fails, wait 60+ seconds for the retention period to expire, then retry. **Never** apply retention lock to your `-raw` landing-zone bucket.

## How this connects to the core lab

| Core lab (Part 3) | This optional lab |
| :--- | :--- |
| Lifecycle: move to Nearline / delete after N days | Retention: *cannot delete* until period ends |
| Q6: 7-year regulatory rewrite | Bucket Lock: make that retention **immutable** |
| Versioning (Part 3) | Retention: protect specific objects from overwrite/delete |