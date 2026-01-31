# ROADMAP — Technician Inventory Ledger (PoC)

> **Scope:** Practical, interview-ready milestones that extend the current MVP without overbuilding.
>
> **Philosophy:** Small, auditable steps. Each phase ends with a demoable outcome.

---

## Phase 1 — Data Realism (1–2 sessions)

**Goal:** Make the system feel real with believable data.

* Seed 20–50 parts
* Create 1 warehouse + 2–3 technician locations
* Enter RECEIVE / ISSUE ledger entries
* Capture screenshots for README

**Deliverable:** Demo-ready data set

---

## Phase 2 — On‑Hand Inventory (Core Value) (2–3 sessions)

**Goal:** Derive current stock from the ledger.

* Query helpers to compute on‑hand by `(location, part)`
* Read‑only inventory views (warehouse + technician)
* Validate negative stock prevention

**Deliverable:** Live inventory view derived from history

---

## Phase 3 — Low‑Stock Alerts (1–2 sessions)

**Goal:** Surface actionable signals.

* Reorder thresholds per part or per location
* Alert list / dashboard widget

**Deliverable:** Low‑stock alert page

---

## Phase 4 — Requests & Approvals (Business Flow) (3–4 sessions)

**Goal:** Model real technician workflows.

* Request + RequestLine models
* Status lifecycle (DRAFT → SUBMITTED → APPROVED → FULFILLED)
* Fulfillment auto‑creates ISSUE ledger entries

**Deliverable:** End‑to‑end request workflow

---

## Phase 5 — RBAC & Guardrails (2–3 sessions)

**Goal:** Enforce least privilege.

* Roles: Technician / Supervisor / Manager
* View/action restrictions
* Adjustment reasons required

**Deliverable:** Role‑aware UI with audit guardrails

---

## Phase 6 — API & Deployment (Optional) (as needed)

**Goal:** Future‑proof the PoC.

* Django REST Framework endpoints
* Dockerized app
* SQLite → Postgres

**Deliverable:** Deployable external PoC

---

## Definition of “Done”

* Clean Git history
* Clear README + screenshots
* Demo script (2–3 minutes)
* No proprietary data

---

*Last updated:* *(fill on commit)*
