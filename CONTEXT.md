# Channel Partners FSL Demo — Deal Context

Last updated: 2026-06-12  
SE: Mike Knight  
AE/Owner: Daniel Jenks

---

## The Deal

### Account: Channel Partners Solutions, LLC.
- **Salesforce ID:** `0013y00001dxh8aAAA`
- **Website:** https://www.channelpartners.com/
- **Industry:** Professional Services
- **Employees:** 31
- **Annual Revenue:** ~$26.4M
- **Location:** Irvine, CA
- **Account Owner:** Daniel Jenks

### Opportunity: "Channel Partners +60 FSL Tech, +10 FSL Dispatcher - Crawl"
- **Salesforce ID:** `006ed00000YQ5i1AAD`
- **Stage:** 02 - Determining Problem, Impact, Ideal
- **Amount:** $73,500
- **Close Date:** October 30, 2026
- **Type:** New Business
- **Owner:** Daniel Jenks
- **Org62 URL:** https://org62.lightning.force.com/lightning/r/Opportunity/006ed00000YQ5i1AAD/view

### DSR: DS-1712752
- **Salesforce ID:** `a25ed000001yhxZAAQ`
- **Status:** Assigned
- **Request Type:** Specialist SE
- **Product Line:** Field Service (FSL)
- **Region:** AMER
- **Due Date:** June 17, 2026
- **Org62 URL:** https://org62.lightning.force.com/lightning/r/Deal_Support_Request__c/a25ed000001yhxZAAQ/view

---

## The Scenario

Channel Partners Solutions is a **PE-backed retail execution and field services consolidator** in Irvine, CA that has unified 6 acquired companies: Apollo, BDS, WhiteHawk, BTR, MAG, and MaaS. They employ **4,140 W-2 field reps** delivering hybrid services across break-fix, installations, merchandising, audits, and training.

They are currently consolidating 3 legacy workforce management systems into "Open Sky" (custom-built platform). **Major rollout scheduled July 6, 2026** across all 6-7 business units, followed by stabilization phase.

The current opportunity is a **pilot/crawl deployment**:
- **+60 FSL Tech licenses** (field technicians)
- **+10 FSL Dispatcher licenses**
- **70 total licenses for 4,140 reps = 1.7% coverage**
- **"Crawl"** = testing with one LOB or region before expansion

**Full deployment potential:** $4M-$5M (all 4,140 reps across FSL + potential Retail Execution hybrid)

### What SE Is Being Asked To Do

From the DSR (`Reason_for_SE_Involvement__c`):
> Requesting Ken Schatzeder for SFS discovery and strategic demo/positioning. Customer is on a homegrown solution, growing quickly. Has a need to replace their solution with an industry best solution. Request: in depth discovery/reverse demo and demo

SE Next Steps (`SE_Next_Steps__c`):
> Internal engagement and level setting ahead disco/reverse demo. Prepare demonstration to follow

**Completed:**
- ✅ June 18, 2026: Reverse demo (2-hour OpenSky walkthrough with Jay, Kari, Mario, Tambra, James)
- ✅ June 23, 2026: Discovery questions drafted, reverse demo analysis documented

**Upcoming:**
- June 24, 2026 (9am): Architecture review session
- Week of July 1-5: Follow-up discovery session
- July 6, 2026: Open Sky rollout begins (customer resource constrained after this date)
- Q4 2026: Earliest realistic evaluation window for Salesforce (post-stabilization)

### Demo Approach

This is a **discovery-first** engagement with **long sales cycle** (Q4 2026 earliest decision window):

**Phase 1 (June 2026):** Discovery & Reverse Demo ✅
- Understand Open Sky system, pain points, business model
- Map workforce structure (4,140 reps across 6 business units)
- Identify gaps Open Sky can't address

**Phase 2 (July-Sept 2026):** Architecture & Relationship Maintenance
- Architecture review (June 24)
- Monitor Open Sky rollout progress
- Position Salesforce as enhancement/complement (not replacement)
- Share relevant content (AI scheduling case studies, reference architectures)

**Phase 3 (Q4 2026):** Formal Evaluation
- Solution architecture and design sessions
- Proof of concept / pilot planning
- Commercial proposal (crawl → walk → run expansion path)

**Key Themes:**
- **Intelligent scheduling** (AI-driven, cross-LOB optimization) — their #1 need
- **Real-time data & exception handling** (4-hour batch → streaming CDC)
- **Cross-LOB resource optimization** (break silos between merch/break-fix/installations)
- **Mobile stability & UX** (offline-first, consistent across devices)
- **FSL + Retail Execution hybrid** (break-fix on FSL, merchandising on Rex)
- **Crawl → Walk → Run** (70 licenses → 500-1000 → 4,140 full deployment)

---

## What Needs to Be Built

The demo org is: `mjk-260320-scheduler` (admin@mjk-260320.scheduler)

Planned demo components (TBD based on discovery):
- FSL dispatcher console walkthrough — scheduling, Gantt, optimization
- Field tech mobile experience — work orders, checklist, GPS
- Replace-the-spreadsheet story — scheduling vs. manual dispatch
- Reporting/dashboards for a PS firm
- LWC components as needed to customize for the scenario

---

## Org62 Access Notes

The Org62 records were pulled using the `scripts/org62_query.py` helper in this repo. See that file and `~/.cursor/rules/org62-access.mdc` for full documentation on how authentication works from Cursor/Claude.

To re-query any record:
```bash
python3 scripts/org62_query.py "SELECT Id, Name, StageName, Amount FROM Opportunity WHERE Id = '006ed00000YQ5i1AAD'"
```
