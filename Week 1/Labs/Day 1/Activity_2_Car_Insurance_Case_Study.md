# Week 1 · Day 1 — Activity 2: DE Case Study — Car Insurance

**Duration:** 60 min  
**Format:** Groups of 3–4 (same groups as Activity 1)

---

## The scenario

Tell the story of a data engineer's role in a car insurance company. You are building the data infrastructure that powers underwriting, claims, and fraud detection. Your job today is to map the data — where it comes from, how it moves, what can go wrong.

---

## Tasks

### 1. Types of data (15 min)

Identify real examples of each data shape in car insurance and describe how each is collected:

| Data shape | Real example at an insurer | How it's collected |
| :--- | :--- | :--- |
| Structured | Policy records, claims tables, premium ledgers | Core systems DB, batch exports |
| Semi-structured | | |
| Unstructured | | |

### 2. One data flow, end to end (20 min)

Pick **one** of the following flows and trace it completely:

- **Option A:** A telematics event — a driving event (hard brake, speeding) recorded by the mobile app
- **Option B:** A new claim — a policyholder submits a claim online after a collision

Trace it through these stages:

```
Where generated → How ingested → Where it lands → Who consumes it → Through what tool
```

Draw this as a simple box-and-arrow diagram (whiteboard or on your slide).

### 3. What could go wrong? (10 min)

For your chosen flow, identify at least one risk in each category:

| Category | Risk in your flow |
| :--- | :--- |
| Data quality | |
| Privacy / PII | |
| Latency | |
| Scale | |

### 4. Story time (15 min)

Prepare a 5-minute **"day in the life of this data"** narrative — starting at the source and ending at the business user. Write it as if you're explaining it to a new colleague on their first day.

---

## Deliverable

- **One slide** showing your data flow (boxes and arrows)
- **5-minute group story** — every member presents at least one stage of the flow

> [!TIP]
> Use what you've seen in your Hartford division — anonymized and generalized — to make it real. If you're a new intern who hasn't been in a division long, use The Hartford's auto insurance line as your frame: think telematics data from mobile apps, claims submitted online, adjuster notes, and SFTP vendor feeds. Those are all real data flows you can trace.
