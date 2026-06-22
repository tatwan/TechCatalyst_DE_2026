# Week 1 · Day 1 — Activity 2: DE Case Study — Car Insurance

![ChatGPT Image Jun 29, 2025 at 11_46_11 PM](images/de.png)

**Duration:** 60 min group work · Presentations follow
**Format:** Groups of 3–4 (same groups as Activity 1)

---

## The scenario

Tell the story of a data engineer's role in a car insurance company. You are building the data infrastructure that powers underwriting, claims, and fraud detection. Your job today is to map the data: where it comes from, how it moves, and what can go wrong.

---

## Tasks

### 1. Types of data 

Identify real examples of each data shape in car insurance and describe how each is collected:

| Data shape | Real example at an insurer | How it's collected |
| :--- | :--- | :--- |
| Structured | |  |
| Semi-structured | | |
| Unstructured | | |

### 2. One data flow, end to end

Pick one flow and trace it through these stages:

`Where generated → How ingested → Where it lands → Who consumes it → Through what tool`

- **Option A:** A telematics event — a hard brake or speeding event from the mobile app
- **Option B:** A new claim — a policyholder submits online after a collision

> [!TIP]
> Whether you're new to the company or already embedded in a division, The Hartford's auto insurance line has all the data flows you need:
> - **Telematics** — driving events (hard brake, speeding) streamed from the mobile app
> - **Claims** — a policyholder submits a claim online after a collision
> - **Vendor feeds** — third-party data (DMV records, credit) arriving via SFTP
>
> Use what you know — and if you're newer, pick **Option B (new claim)** — it's the most intuitive flow to trace end-to-end.

### 3. Sketch the flow (your slide deliverable)

Draw your flow as a box-and-arrow diagram. Each box = a system or storage layer. Each arrow = a data movement. Name real or plausible system types at each stage — not just "database" or "storage."

Use this skeleton to calibrate the level of detail expected:

`Mobile App → Event Queue (Kafka) → Raw Storage (S3) → Feature Pipeline → Risk Score DB → Underwriting Dashboard`

### 4. What could go wrong? 

For your chosen flow, identify at least one risk in each category:

| Category | Risk in your flow |
| :--- | :--- |
| Data quality | |
| Privacy / PII | |
| Latency | |
| Scale | |

### 5. Story time 

Prepare a "day in the life of this data" narrative starting at the source and ending at the business user. Write it as if you're explaining it to a new colleague on their first day.

---

## Deliverable

**Up to 2 slides:**

| Slide | Content |
|---|---|
| **Slide 1 — The Flow** | Box-and-arrow diagram with system names and arrows. Risks annotated directly on the diagram near the stage where they occur. |
| **Slide 2 — The Story anchor** *(optional)* | One sentence per stage summarizing what the data looks like at that point — use this as your speaking guide during the readout. |

**5-minute group story** — every member presents at least one stage of the flow.

> The best slides will make the risks *part of the diagram* — not a separate list. If the PII risk is at the claims intake form, the flag belongs on that arrow.


