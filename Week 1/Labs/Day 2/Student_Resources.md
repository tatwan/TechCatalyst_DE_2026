# Week 1 · Day 2 — Student Resources

> **AI-Free Zone (Weeks 1–4):** Reason through the architecture scenarios yourself — no Copilot or LLM-generated service picks. Mapping a business need to the right capability by hand is exactly the muscle today builds.

External resources to go deeper on today's topics. Pick what's most useful to you.

## Core Documentation

| Resource | Why it helps |
| :--- | :--- |
| [What is cloud computing? (Google Cloud)](https://cloud.google.com/learn/what-is-cloud-computing) | Clean IaaS/PaaS/SaaS refresher if the service models felt fuzzy |
| [Shared responsibility model (Google Cloud)](https://cloud.google.com/architecture/framework/security/shared-responsibility) | Definitive who-manages-what reference for permissions |
| [AWS/Azure/GCP service comparison (Google Cloud)](https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison) | The canonical GCP↔AWS translation table you'll keep all summer |
| [GCP IAM overview](https://cloud.google.com/iam/docs/overview) | Principals, roles, policies, resources — maps to today's IAM block |
| [BigQuery cost best practices](https://cloud.google.com/bigquery/docs/best-practices-costs) | The five cost habits expanded — required before Week 3 |

---

## Cloud fundamentals

**"Cloud Computing Explained" — Google Cloud**
https://cloud.google.com/learn/what-is-cloud-computing
Short official overview of IaaS/PaaS/SaaS with concrete examples. Good refresher if the service model distinctions felt fuzzy.

**"Shared Responsibility Model" — Google Cloud documentation**
https://cloud.google.com/architecture/framework/security/shared-responsibility
The definitive breakdown of what Google manages vs what you manage. Bookmark for whenever you're setting up permissions.

---

## GCP vs AWS — the service map

**Google Cloud vs AWS service comparison — official**
https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison
Google's own comparison table, updated regularly. The closest thing to a canonical translation guide. Wider than what we covered today — focus on the Storage, Database, Analytics, and ML rows.

**GCP products overview (all services in one page)**
https://cloud.google.com/products
Useful to bookmark. When you encounter a service name you don't recognize this summer, find it here first.

---

## IAM (Identity & Access Management)

**GCP IAM overview — official documentation**
https://cloud.google.com/iam/docs/overview
The authoritative reference. Read the "Concepts" section — it maps to exactly what we covered: principals, roles, policies, and resources.

**"Understanding GCP IAM" — Google Cloud blog**
https://cloud.google.com/blog/products/identity-security/dont-get-pwned-practicing-the-principle-of-least-privilege
A practical read on least privilege with real examples. Explains the most common misconfiguration mistakes DEs make.

---

## Billing and cost control

**GCP pricing calculator**
https://cloud.google.com/products/calculator
Enter your workload specs and see what it costs. Run the numbers on the telematics scenario from today's activity — it's eye-opening.

**GCP free tier — what's always free**
https://cloud.google.com/free/docs/free-cloud-features
The exact limits for BigQuery, Cloud Storage, Cloud Shell, and other services we'll use this summer. Know these so you don't accidentally run up a bill during labs.

**"BigQuery cost optimization" — Google Cloud documentation**
https://cloud.google.com/bigquery/docs/best-practices-costs
The five habits from today's slide, expanded with examples and SQL patterns. Required reading before Week 3.

---

## The NYC Taxi dataset in BigQuery

**Querying BigQuery public datasets — Google Cloud documentation**
https://cloud.google.com/bigquery/public-data
How to access the public dataset project we queried in the demo. Try running a query yourself in the BigQuery sandbox (free — no billing account needed).

**NYC Taxi trips dataset in BigQuery**
```sql
-- Run this in BigQuery sandbox (console.cloud.google.com → BigQuery)
SELECT pickup_datetime, trip_distance, fare_amount, payment_type
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
LIMIT 100
```
This is your first look at the data that powers the longitudinal pipeline project. Notice how fast it runs and what "bytes processed" says — that's your future cost driver.

---

## Recommended reading

**"Fundamentals of Data Engineering" — Chapter 4: Choosing Technologies**
Joe Reis & Matt Housley (O'Reilly, 2022) — the chapter on picking the right tool covers the same build-vs-buy and IaaS-vs-PaaS reasoning we applied today. Pairs well with this week's service model content.
https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/

---

## Lab Deliverable Checklist

| ✓ | Deliverable |
| :--- | :--- |
| ☐ | Worksheet completed for each assigned scenario (batch/streaming decision + justification) |
| ☐ | Service model (IaaS/PaaS/SaaS) identified for each scenario |
| ☐ | Primary GCP service(s) named, with the AWS equivalent for each |
| ☐ | Cost risk and PII/security consideration noted per scenario |
| ☐ | 5-minute readout prepared — one scenario per group member |
| ☐ | At least one challenge raised against another team's service choice |
