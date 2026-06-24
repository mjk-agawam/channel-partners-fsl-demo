# Mars - Third-Party Labor Management System

**Last Updated:** June 24, 2026  
**Source:** Architecture session discussion

---

## Overview

**Mars** is a distinct system used for managing third-party labor that remains separate from OpenSky. It handles partners/contractors who are not W-2 employees of Channel Partners.

---

## Purpose

**Third-Party Labor Management:**
- Manage data for third-party partners/contractors
- Track hours worked by third-party labor
- Handle invoicing and billing for partner work
- **NOT integrated into main OpenSky employee workflows**

---

## Current State

**Separation from OpenSky:**
- Mars operates independently
- Third-party labor tracked separately from 4,140 W-2 employees
- Data flows to Snowflake for analytics/reporting
- No direct integration with OpenSky workforce management

**Use Case:**
Break Fix Merchandising division often reaches out to 3rd party field marketing companies to partner on projects where Channel Partners does not have market coverage. Mars manages these partner relationships and their work.

---

## Integration Points

**Data Warehouse:**
- Mars data → SFTP → S3 → Snowflake → Tableau
- Combined reporting with OpenSky data in Snowflake
- Analytics across W-2 employees + third-party contractors

**Partner Data Flow (Mentioned in Feature List):**
> "The Break Fix Merchandising division of Channel Partners often reaches out to 3rd party field marketing companies to partner on projects where Channel Partners does not have market coverage. This feature refers to any capability for partner data to flow into a Workforce Management solution to get call form question answer/completion data from these partners for combined reporting/analytics. Or is there way for 3rd party field reps to come into the system as guests to complete work"

**Gap:** Partner call form data does NOT flow automatically into OpenSky today (manual export/import from Mars).

---

## Salesforce Opportunity

### Unified Workforce Management

**Replace Mars + OpenSky with unified FSL:**
- W-2 employees as Service Resources
- Third-party contractors as Service Resources (different resource type)
- Unified scheduling, mobile, and time tracking
- Separate billing/invoicing by resource type
- Single platform for all field workers

**Benefits:**
- Eliminate dual system maintenance
- Unified view of all field capacity (W-2 + contractors)
- Cross-pollination opportunities (assign contractor when W-2 not available)
- Simplified reporting (one source of truth)
- Reduced data integration complexity

### Guest Access for Partner Reps

**Experience Cloud + FSL Mobile:**
- Third-party partner reps login as Community users
- Access assigned work orders via FSL Mobile
- Complete surveys/call forms
- Submit time and expenses
- Data flows into same Salesforce org as W-2 employees

**Licensing:**
- Community licenses for partner users (lower cost than full FSL)
- Or: FSL licenses allocated to partner firms (they manage their own reps)

---

## Open Questions

**Mars System Details:**
1. Which vendor/platform is Mars? (Custom-built? Third-party?)
2. How many third-party contractors managed in Mars? (Dozens? Hundreds? Thousands?)
3. What % of field work is done by contractors vs. W-2 employees?
4. Do contractors use mobile apps to complete work? Or just time tracking?
5. Do contractors complete surveys/call forms like W-2 reps?
6. How is quality controlled for contractor work? (Same QA process as W-2?)
7. What's the invoicing process? (Partner bills CP, CP bills client?)
8. Are contractors ever assigned to same projects as W-2 reps? (Mixed teams?)
9. Timeline for Mars replacement or integration with OpenSky?

**Integration Strategy:**
10. If Salesforce replaced OpenSky, would you also replace Mars?
11. Or would Mars remain and need integration with Salesforce?
12. Could MuleSoft integrate Mars → Salesforce if Mars stays?

---

**End of Mars Documentation**
