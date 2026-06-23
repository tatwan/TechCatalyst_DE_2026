# Week 1 · Day 2 · Activity 3: Estimate the Bill

**Duration:** 45 min  
**Difficulty:** Beginner  
**Format:** Same teams as Activity 2 (groups of 3 to 4)  
**Prerequisites:** Activity 2 (you priced an architecture conceptually); no cloud account, no credit card, and no billing needed for this lab

***

## Why this activity

In Activity 1 you watched BigQuery report **bytes processed**. In Activity 2 you chose services for a business problem. This activity connects the two: you put a **dollar figure** on an architecture before anyone builds it, and you design the **budget and alerts** you would set to keep it from surprising you.

This is a core data engineering habit. The fastest way to lose trust with a platform team is a surprise five-figure bill. The fastest way to build trust is to estimate first, set a budget, and watch the cost drivers.

The main lesson is not the exact dollar amount. The main lesson is that **cloud services use different pricing meters**. Some charge by time, some by data stored, some by data processed, some by request/API call, and some by network transfer. A single service can also have more than one meter.

> [!IMPORTANT]
> **Why not create a real budget today?** A real Cloud Billing budget can only be set on a project that has a **billing account**. Your BigQuery Sandbox has no billing account, so today you **plan** the budget using the Pricing Calculator (which needs no account at all). You will create a real budget on your own project later this week, once setup is done.

> [!WARNING]
> **AI-Free Zone (Weeks 1 to 4).** Do not ask an LLM to produce the estimate or pick the numbers. Use the calculator, read the figures, and reason about them yourself.

***

## Pricing mechanisms to watch

Cloud pricing is easier when you ask, "What is the meter?" Keep these common meters in mind as you estimate:

| Pricing meter | What you pay for | Example |
| :--- | :--- | :--- |
| **Time** | A resource running for seconds, minutes, or hours | VM hours, Spark cluster time, some serverless execution time |
| **Storage size** | Data kept at rest, usually per GB-month | Cloud Storage bucket, warehouse storage, database storage |
| **Processing size** | Data scanned, transformed, or processed | BigQuery bytes scanned, Athena bytes scanned |
| **Requests / API calls** | Number of operations or calls | Object read/write requests, function invocations, API calls |
| **Network transfer** | Data leaving a region, zone, or cloud | Cross-region copy, internet egress, downloads |

> [!TIP]
> Most beginner surprises come from **time-based compute left running**, **processing more data than expected**, and **network transfer nobody planned for**. Storage is often visible and predictable; compute, scans, requests, and egress are easier to miss.

***

## What you will price

Use **this default workload** unless your instructor tells you to price your own Activity 2 scenario instead.

> **The nightly claims landing zone (GCP)**
> - A **Cloud Storage** bucket holding **200 GB** of raw claims files, in one region (Standard storage class).
> - A **BigQuery** load and daily summary that **scans about 50 GB per day** of that data, on-demand pricing, roughly **30 days** per month.
> - A small **scheduled compute** job that validates the file each night (treat it as a tiny always-available service or a short job; price the smallest option the calculator offers).

You do not need exact real numbers from The Hartford. The goal is a defensible estimate and an understanding of which line dominates.

***

## Timing

| Time | Task |
| ---: | :--- |
| 5 min | Open the calculator and price storage (Parts 1–2) |
| 10 min | Price the queries and the compute job (Parts 3–4) |
| 10 min | Read the total, classify meters, find the driver (Part 5) |
| 10 min | Design the budget and alerts (Part 6) |
| 10 min | Debrief, instructor reveal, and exit ticket |

***

## Part 1: Open the Pricing Calculator

1. Go to **https://cloud.google.com/products/calculator**. No sign-in is required.
2. You will add one estimate per service, then read the running total.

> [!NOTE]
> The calculator's layout changes from time to time. The pattern is always the same: **search for a service, add it, fill in the quantities, and it appears in your estimate list with a monthly cost.** If a field is unfamiliar, leave the default and note what you left.

## Part 2: Price storage

3. Add **Cloud Storage** to your estimate.
4. Set the **location** to a single region (for example `us-east1`), the **storage class** to **Standard**, and the **total amount of storage** to **200 GB**.
5. Record the monthly storage cost.

**Q1:** What is the monthly cost of storing 200 GB? Is storage a large or small part of your total so far?

**Meter check:** Which pricing meter did Cloud Storage use here: time, storage size, processing size, requests/API calls, or network transfer?

## Part 3: Price the queries

6. Add **BigQuery** to your estimate. Choose the **on-demand** (per-TiB-scanned) option, not a capacity/edition commitment.
7. On-demand BigQuery bills by **data scanned**, not by rows returned (you saw this in Activity 1). Convert the workload: about **50 GB scanned per day** for **30 days**. Enter the monthly scanned volume the calculator asks for.
8. Record the monthly query cost.

**Q2:** Which costs more per month, storing the data or querying it? In one sentence, why does scanning 50 GB every day add up?

**Meter check:** Which pricing meter did BigQuery use for the on-demand query line?

> [!TIP]
> If the team partitioned the table by date and queried only one day at a time, the scanned volume per query would drop sharply. You will learn partitioning in Week 3. Note it here as a future cost lever.

## Part 4: Price the compute

9. Add a small **compute** option for the nightly validation job. The cheapest realistic choice is a **serverless** option (for example Cloud Run) sized small and running only briefly each night. If the serverless option is hard to model, add the **smallest Compute Engine VM** instead and assume it runs only a short time per day.
10. Record the monthly compute cost.

**Q3:** What happens to the compute cost if someone forgets to stop a VM and it runs **24/7** instead of a few minutes a night? Estimate the difference using the calculator.

**Meter check:** Which pricing meter makes idle compute expensive?

## Part 5: Read the total and find the driver

11. Look at the **estimated monthly total** for all three line items together.

| Line item | Monthly cost |
| :--- | ---: |
| Storage (200 GB) | |
| Queries (about 1.5 TB scanned/month) | |
| Compute (nightly job) | |
| **Total** | |

Now classify each line item by pricing meter:

| Line item | Primary pricing meter | Why |
| :--- | :--- | :--- |
| Cloud Storage | | |
| BigQuery on-demand query | | |
| Nightly compute job | | |

**Q4:** Which single line item is the **biggest cost driver**? Name **one concrete change** that would cut it (for example: scan less data, stop idle compute, move to a cheaper storage class).

**Q5:** You did not add an egress line. When would egress appear on this bill, and roughly how could it become the largest item?

**Q6:** Name one way the same service could have more than one pricing meter. For example, object storage may charge for GB-month storage, operations, and network transfer.

## Part 6: Design the budget you would set

You cannot create a real budget today, but you can decide exactly what it should be.

12. Pick a **budget amount**. A good default is a round number a bit above your estimated total, with headroom for growth (the workload grows about 10% per year).
13. Decide your **alert thresholds**. The course convention is **50%, 90%, and 100%** of the budget.
14. Decide **who gets the alert** (for example: the team channel and the project owner).

| Budget decision | Your answer |
| :--- | :--- |
| Monthly budget amount | |
| Alert thresholds | 50% / 90% / 100% |
| Who is notified | |
| First action when the 90% alert fires | |

**Q7:** Why alert at 50% and 90% rather than only at 100%? What can you still do at 90% that you cannot do at 110%?

***

## AWS translation (read, do not rebuild)

The same thinking maps directly to AWS. You are not required to redo the estimate there.

| GCP | AWS |
| :--- | :--- |
| Pricing Calculator (`cloud.google.com/products/calculator`) | AWS Pricing Calculator (`calculator.aws`) |
| Cloud Billing budgets and alerts | AWS Budgets |
| Cloud Storage (GB-month) | Amazon S3 (GB-month) |
| BigQuery on-demand (per TiB scanned) | Amazon Athena (per TB scanned) |
| Compute Engine / Cloud Run | Amazon EC2 / AWS Lambda or Fargate |

> *The product names change; the pricing meters and the budget habit do not.*

***

## Deliverable

Record these in your lab notes (one set per team; every member should be able to explain the cost driver):

- The completed cost table — storage, queries, compute, and total — with each line classified by its pricing meter.
- The single biggest cost driver, plus one concrete change that would cut it.
- A budget plan: amount, the 50/90/100% alert thresholds, who is notified, and your first action when the 90% alert fires.

***

## Success Criteria

Your team is finished when it can check every item:

- [ ] We have a monthly figure for storage, queries, and compute, plus a total.
- [ ] We classified each line item by pricing meter: time, storage size, processing size, requests/API calls, or network transfer.
- [ ] We identified the single biggest cost driver and one way to cut it.
- [ ] We can explain why idle compute, large scans, API/request volume, and egress are easy ways to overspend.
- [ ] We chose a budget amount, three alert thresholds, and who gets notified.
- [ ] We can state one action we would take when the 90% alert fires.

## Exit Ticket

Answer without looking back:

1. Name three different cloud pricing meters.
2. Two queries return the same 100 rows. Why can one cost far more than the other?
3. Why can the same service appear on a bill under more than one meter?
4. Why estimate and set a budget *before* building instead of watching the bill afterward?

***

## 

## References

- [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator)
- [Create, edit, or delete budgets and budget alerts](https://cloud.google.com/billing/docs/how-to/budgets)
- [BigQuery: estimate and control costs](https://cloud.google.com/bigquery/docs/best-practices-costs)
- [Cloud Storage pricing (including network egress)](https://cloud.google.com/storage/pricing)
- [AWS Pricing Calculator](https://calculator.aws/) and [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
