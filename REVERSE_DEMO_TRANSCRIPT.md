# OpenSky Reverse Demo Transcript — June 18, 2026

**Session:** Channel Partners / Salesforce - OpenSky Reverse Demo  
**Date:** June 18, 2026  
**Duration:** ~2 hours  
**Attendees:**

**Channel Partners:**
- Jay Chandran
- Kari Kraus (Project Management & Dev Team Lead)
- Mario Alejandro Morales García (Development Manager)
- Tambra Owens (Project Manager)
- James Dyer (Director of Data Services, 27 years with company)

**Salesforce:**
- Dan Jenks (AE)
- Kalin Gabbert (SE)
- Mike Knight (Service SE)
- Stephen Jackson (Enterprise Architect)
- Laura Landy (Sales Performance Management Solutions)

---

## Key Takeaways

### Business Context
- **31-person company** managing thousands of field reps across retail locations (Target, Best Buy, LG, Samsung, etc.)
- **Multiple lines of business:** Merchandising, break/fix, installations, dedicated brand teams
- **OpenSky:** Homegrown field service system, built by merging two company platforms
- **Major rollout:** Deploying OpenSky across 6-7 business units on July 6, 2026
- **Post-rollout:** Expecting "massive stabilization effort" with resource constraints

### Top Pain Points ("Magic Wand" Responses)

**Jay Chandran:**
1. Intelligent scheduling (AI-driven, cross-LOB optimization)
2. Field-facing efficiency improvements
3. Real-time exception reporting to minimize go-backs

**Kari Kraus:**
- Mobile app that works consistently across all devices/environments

**Mario Morales:**
- Smarter scheduling for reactive breaks (sick reps, job runs long, mid-day reassignments)

**Tambra Owens:**
- Better rep mobile dashboard (not just calendar view, but guidance on daily work)

**James Dyer:**
- Lower-latency data with delta/CDC instead of 4-hour batch extracts for data warehouse

---

## OpenSky System Overview

### Core Capabilities Demonstrated

**Scheduling & Calendaring**
- Two modes:
  - **Hard scheduling:** Manager pushes schedule to rep's calendar (needed time/date/location)
  - **Self-scheduling:** Rep drags unscheduled work to their own calendar within a wave window
- Overnight route optimization for self-scheduled appointments (consolidates same-store visits, optimizes drive sequence)
- Hard scheduling does NOT have route optimization today
- Multi-rep team scheduling (5-15 people, same store, same time) is manual and complex

**Project & Survey Creation**
- **Call form = Project** (configured once, supports unlimited store visits)
- **Waves = Execution windows** (date range, store count, time-in-store duration)
- Highly configurable surveys: conditional logic, products, items, question sets, date-based question visibility
- Question library for reuse across teams
- Survey pivots based on store chain, product SKUs, dates

**Store Relationship Management (SRM)**
- Contact management tied to stores and reps
- Not integrated with sales CRM today — no lead-to-project pipeline

**Materials & Shipping**
- Materials can be linked to projects and stores
- Warehouse integration (pick/pack/ship data flows back to OpenSky)
- Reps can track shipments via mobile
- Parts mostly ship to store location; some now shipping to rep's home for scheduling flexibility

**Product Display Management (Break/Fix)**
- Call center intake → troubleshoot → parts order → approval → warehouse → ship → track → rep install → ticket close
- Not automated; manual export from dashboards to create go-back assignments
- Parts display tracking end-to-end

**Mobile App (iOS/Android, Offline-First)**
- Calendar view (start screen)
- Self-schedule unscheduled work or see hard-scheduled appointments
- Availability entry (day/time granularity)
- Check-in at store (open, temp closed, closed, not permitted)
- Survey completion with photos, conditional questions, task lists
- Time entry (check-in, check-out, duration auto-calculated)
- Work periods (spans multiple days for graveyard shifts)
- End-of-day questionnaire (legal compliance)
- Expense capture with receipt photo
- Resources (training videos, PDFs, client presentations)
- Contact management (some teams use, some don't)
- Mileage calculation
- Sync to server when online

**Travel Management**
- Supervisors submit travel requests
- Dedicated travel team books via Agency (travel platform)
- Travel cost is "insane" — reps move across country frequently for multi-day projects
- Last-minute changes are common

**Timekeeping & Payroll**
- Timecards reviewed weekly by supervisors
- Mileage and drive time auto-calculated
- LMS (learning management system) course hours imported
- Pushed to payroll processing app → ADP
- Overtime calculated AFTER all LOB time is aggregated (can't see overtime risk in real-time)

**Parts Management**
- Parts programs, partners, displays, parts lists all configured in system
- Order management screen for parts team
- Reps can call support center to request parts (with troubleshooting first)
- Manual upload of parts tickets from survey results (not automated)

**Expense Management**
- Reps enter expenses tied to specific visit (job costing)
- Photo of receipt
- Manager approval workflow

**Reporting & Data**
- 4-hour batch to data warehouse
- Tableau & PowerBI dashboards
- No real-time exception reporting today

---

## Current Gaps & Opportunities

### Scheduling
- **Hard scheduling has no route optimization** — inefficient routes, excess mileage reimbursement
- **Self-scheduling works but is challenged by leadership** — "people-friendly" culture vs. cost control
- **No intelligent scheduling** — no AI, no skill-based auto-matching beyond basic rules
- **Spreadsheet-based for complex projects** — bulk upload to "bucket" tool, manual assignment
- **Multi-rep team scheduling is painful** — availability, skills, geography all manual
- **No real-time rep location visibility** — can't see who's available for mid-day reassignment
- **Reactive scheduling is hard** — sick rep, job runs long, store closed → manual bulk reschedule tool

### Cross-LOB & Multi-Client Work
- **Silos by line of business** — no cross-pollination, no incentive to do merch + break/fix in same visit
- **No automated escalation** — merch rep spots LG issue, no trigger to create break/fix ticket
- **No shared resource pool** — work is assigned to specific rep, not available for anyone to pick up
- **Org is shifting to "fluid resources"** — wants reps to work on multiple clients, but not set up for it today (training, systems, incentives all siloed)

### Mobile & Rep Experience
- **Mobile stability issues** — inconsistent across devices, environments (iOS vs. Android, offline mode)
- **No historical context** — reps can't see previous visits, prior issues, contact history, photos from last visit
- **Calendar-only dashboard** — no prioritization, no guidance on "what should I do first today"
- **Support center calls** — reps call in for system issues, work guidance, parts/travel logistics

### Break/Fix & Go-Backs
- **Go-backs are manual** — defects found in survey → export to dashboard → manually create new assignment
- **No automation on parts ordering** — call center approval required; want to automate with safeguards (dollar threshold, manager approval)
- **Parts tracking is fragmented** — warehouse integration works; partner warehouse data is manual spreadsheet upload

### Data & Integrations
- **4-hour latency to data warehouse** — can't answer real-time questions (overtime risk, SLA breach, schedule adherence)
- **No delta/CDC API** — James (data services) wants to request "give me changes since last sync" instead of full extracts
- **CRM not integrated** — no sales pipeline to project execution to field upsell opportunity
- **ADP payroll integration** — works but overtime calculated after-the-fact, payroll errors do happen
- **LMS integration** — two-way feed works, but no enforcement that reps complete required courses before going on-site

---

## Business Model & Culture

### Workforce Mix
- **Dedicated teams** (LG, Samsung) — salary, can go off-script for client because flat rate
- **Shared teams** (merch, flex) — hourly, strict time boundaries, can work on 5 different clients in one day
- **Full-time, part-time, gig/contract** — mix of all three
- **Self-scheduling philosophy** — attracts talent pool, but hurts optimization
- **CEO challenges self-scheduling** — sees it as cost driver

### Travel & Geography
- **Reps use personal vehicles** (or mass transit) — reimbursed for mileage and expenses
- **No assigned vehicles** — no truck stock model today
- **Reps travel overnight frequently** — teams of 5-15 fly in for multi-day installations
- **Travel spend is "insane"** — opportunity to reduce by better local scheduling, hiring local reps

### Billing & Job Costing
- **Every visit is billable** (unless it's a go-back for Channel Partners' mistake)
- **Mix of hourly, salary, per-diem, door fee (bonus per location)**
- **Job costing by project** — flows to Business Central (ERP)
- **No real-time project profitability** — after-the-fact reporting

---

## Technical Architecture (High-Level)

**OpenSky (Homegrown):**
- Built by merging two company platforms (one did self-scheduling, one did hard scheduling)
- Web app + mobile app (iOS/Android, offline-first)
- Hosted internally (QA and Production environments)

**Integrations:**
- **ADP:** Timekeeping → payroll processing app → ADP
- **Business Central:** Job costing, invoicing
- **LMS (third-party):** Two-way feed (users/teams out, course completions back)
- **Warehouse system:** Materials/shipping requests, pick/pack/ship data back
- **Agency:** Travel booking platform
- **Freshdesk:** Help desk for IT support and call center
- **Data Warehouse:** 4-hour batch from OpenSky → Tableau/PowerBI

**Data Services (James Dyer):**
- Extract data every 4 hours via API (date range queries)
- Must derive delta manually — wants delta/CDC capability
- Joins OpenSky data with financial systems, payroll, overtime processing

---

## Organizational Context

### Roles in OpenSky
- **Field reps:** Complete work in stores (merch, break/fix, installs, dedicated brand reps)
- **Client service / Project managers:** Set up projects, build surveys, configure waves, manage client relationships, billing
- **Account team / Supervisors:** Manage field ops (payroll review, schedule compliance, rep performance)
- **Support center / Call center:** Troubleshoot, parts ordering, IT help
- **Parts fulfillment team:** Triage parts requests, approve, manage warehouse
- **Travel team:** Book flights/hotels for field teams
- **Payroll/finance team:** Review timecards, process payroll
- **Learning team:** Manage LMS, course assignments
- **Data services (James):** ETL, data warehouse, reporting

### Hierarchy & Permissions
- **Position tree = hierarchy** per line of business (not company-wide)
- Supervisors see only their reps' data (filtered by hierarchy)
- Some teams (small dedicated) have one person doing both client service + field ops
- Large teams (merch, 5,000 reps, 60 field managers, 30 client service managers) have separate roles
- **Org shifting to geographic model** (away from LOB silos) in next 2-3 months

---

## Demo Walkthrough Notes

### Mobile App Flow
1. **Login → Calendar view** (appointments scheduled or unscheduled)
2. **Unscheduled list** (work assigned to rep, needs to be dragged to calendar)
3. **Drag appointment to calendar** → system prompts to consolidate same-store visits, optimize route
4. **Click appointment → Start visit**
5. **Check-in at store** (open, closed, temp closed, not permitted)
6. **Survey task list** (configured per project, conditional questions, photos, products)
7. **Complete tasks** → Auto-calculate time in store
8. **Time entry** (check-in, check-out, duration, work period selection)
9. **End-of-day questionnaire** (if last visit of the day)
10. **Sync to server** (uploads all data)
11. **Expenses** (tied to visit, photo of receipt)
12. **Resources** (training videos, PDFs)
13. **Mileage report** (auto-calculated, displayed to rep)

### Manager/Client Service View
1. **Call form list** (projects, one row per project)
2. **Click into call form** → Configure:
   - Client, job costing, overview info, retailers
   - Features (image gallery, overnights, SRM, required courses)
   - Materials management
   - Waves (date range, store count, time in store, per-diem, door fee)
3. **Bucket tool** (store assignment):
   - Upload store list or pull from universal store list
   - Match rules: existing assignments, distance (e.g., within 35 miles), tactics (rep profiles), position types (full-time MDM, ASR, etc.)
   - View matched/unmatched stores
   - Configure alternate pay rates → email rep for acceptance
   - Finalize → Push to reps (now visible on their calendars)
4. **Survey creation**:
   - Question sets, tasks, questions
   - Conditional logic, product pivots, date-based visibility
   - Question library for reuse
5. **Payroll review screen**:
   - See all reps, all visits, all time (mileage, drive time, in-store, admin, LMS)
   - Drill down per rep, per visit
   - Approve/reject time entries
6. **Parts management**:
   - Call center creates parts ticket (caller, issue, display, part search)
   - Parts team triages (approve/reject)
   - Assign rep for go-back
   - Track status (open, part ordered, in stock, completed)
   - Upload parts tickets from survey export (manual template upload)

---

## Questions Raised During Demo

**Dan (Salesforce):**
- How does CRM data flow into OpenSky? **Answer:** It doesn't — sales CRM is separate, only job costing flows to Business Central.
- How is overtime managed? **Answer:** Calculated after-the-fact by payroll processing app; no real-time visibility.
- How do you prevent inefficient routes on hard-scheduled work? **Answer:** We don't today — that's a gap.
- Can reps see historical work at a location? **Answer:** No — that's a gap, especially for dedicated teams.
- How do reps get help in the field? **Answer:** Call support center.
- What's the value of self-scheduling? **Answer:** Attract talent, flexibility — but CEO challenges it due to cost.

**Kalin (Salesforce):**
- If someone is sick, how is work reassigned? **Answer:** Bulk reschedule tool or line-by-line manual.
- Is the survey checklist templatized or manual? **Answer:** Question sets can be reused, or built from scratch.
- Can reps search historical work or defects at a store? **Answer:** No — that's a gap.
- What % of work is break/fix vs. merchandising? **Answer:** Don't have that metric by visit count; can get by revenue (Jay will follow up).

**Stephen (Salesforce):**
- Do you have a complete list of OpenSky capabilities? **Answer:** Yes (feature chart shared, will be cleaned up and sent).

**James (Salesforce, via Dan):**
- Can you extract delta data instead of full snapshots? **Answer:** No — we call API with date range, derive delta manually. This is a big wish for us.

---

## Magic Wand Question Responses

**Dan asked: "If you could wave a magic wand, what's the one or two things you wish would change?"**

**Jay:**
1. Intelligent scheduling (AI-driven, fully optimized, cross-LOB)
2. Field-facing efficiency improvements
3. Real-time exception reporting to minimize go-backs

**Kari:**
- Mobile app that works consistently across all devices/environments

**Mario:**
- Smarter scheduling for reactive breaks (sick rep, job runs long) and provisioning slots dynamically

**Tambra:**
- Better rep mobile dashboard (not just calendar — guide them on what to do today)

**James:**
- Lower-latency data with delta/CDC instead of 4-hour batch extracts

---

## Reverse Question: What's Salesforce Missing?

**Jay asked: "After seeing OpenSky, what gaps do you see in Salesforce?"**

**Dan's response:**
- Scheduling and routing efficiency is the glaring one — especially knowing the mileage reimbursement impact.
- Lots of opportunity to streamline, but didn't want to solution yet — need to debrief internally first.

---

## Next Steps Agreed

1. **June 24, 9am:** Architecture workshop (integrations, tech stack deep dive)
2. **Week of July 1-5:** Follow-up session with targeted questions (after debrief + architecture session)
3. **Post-July 6:** Stabilization period for OpenSky rollout; limited bandwidth
4. **Deliverables from Channel Partners:**
   - OpenSky feature chart (cleaned up, shared via PowerPoint link)
   - Capability breakdown by % (revenue, visits, hours) for break/fix vs. merch vs. dedicated teams

---

## Key Insights for Salesforce Discovery

### Where FSL Wins
- **Intelligent scheduling** (AI, route optimization, skill-based, cross-LOB) — their #1 ask
- **Real-time exception reporting** (SLA risk, overtime alerts, rep location, job status)
- **Mobile consistency** (offline-first, cross-platform, stable)
- **Automated go-back workflows** (defect found → auto-create ticket → auto-route → auto-schedule)
- **Cross-LOB work enablement** (one rep, multiple clients, same visit — incentives, training, billing)
- **Historical context for reps** (prior visits, defects, contacts, photos)
- **Lower-latency data** (delta/CDC for data warehouse, real-time project profitability)

### Where OpenSky Is Strong (Must Match or Beat)
- **Survey flexibility** (conditional logic, product pivots, question library, date-based visibility)
- **Offline mobile** (reps work in stores with poor connectivity)
- **Travel management** (dedicated team, frequent multi-day projects)
- **Multi-LOB support** (dedicated + shared teams, different billing models, separate hierarchies)
- **Work period model** (spans multiple days for graveyard shifts)

### Red Flags / Risks
- **July 6 rollout + stabilization** — limited bandwidth until Q4
- **Org structure in flux** — LOB silos → geographic model (next 2-3 months)
- **Self-scheduling culture** — reps value flexibility; moving to hard scheduling risks attrition
- **Integration complexity** — ADP, Business Central, LMS, warehouse, travel platform, Freshdesk
- **Mobile offline requirement** — non-negotiable
- **Survey configuration speed** — client service managers build complex surveys; must be fast/easy

---

## Full Transcript

[Transcript follows — see original document for full verbatim conversation]

---

## Contact Log

**Channel Partners Team:**
- Jay Chandran (leadership)
- Kari Kraus (Project Management & Dev Lead) — main demo presenter
- Mario Alejandro Morales García (Development Manager)
- Tambra Owens (Project Manager) — has done multiple demos, collaborating with Dan on separate project
- James Dyer (Director of Data Services, 27 years tenure)

**Salesforce Team:**
- Dan Jenks (AE, new to account in 2026)
- Kalin Gabbert (SE, Dan's technical counterpart)
- Mike Knight (Service SE, workforce management specialist)
- Stephen Jackson (Enterprise Architect) — knows Jay from HSN tokenization project ~2013
- Laura Landy (Sales Performance Management Solutions)

**Small World Moment:**
Stephen and Jay worked together at HSN in St. Petersburg, FL around 2012-2013 on credit card tokenization for PCI compliance. Stephen was lead architect. This created instant rapport.

---

## Open Questions for Follow-Up

1. What % of work is self-scheduled vs. hard-scheduled? (By visit count, by revenue, by LOB?)
2. What % of workforce is dedicated vs. shared? Full-time vs. part-time?
3. What % of work is break/fix vs. merch vs. installations? (By revenue preferred)
4. How often do schedules break mid-day? (Sick rep, job runs long, store closed?)
5. What's the average number of stores per rep per day? (Shared teams vs. dedicated teams?)
6. What's the average mileage reimbursement per rep per week?
7. What's the travel spend annually? What % is avoidable with better local scheduling?
8. How many go-backs per week? What % are due to wrong parts vs. incomplete work vs. quality issues?
9. What's the typical lag between field work completion and invoice to client?
10. How many parts tickets are created per week? What % are approved vs. rejected?
11. What's the typical survey build time for a new project?
12. What's the payroll error rate? (Time entry disputes, overtime miscalculations, etc.)
13. What's the rep attrition rate? Does self-scheduling reduce attrition?
14. What's the support center call volume per week? What % are system issues vs. work guidance vs. logistics?
15. What's the timeline for org restructure (LOB silos → geographic model)?

---

**End of Transcript Summary**
