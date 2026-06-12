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

Channel Partners Solutions is a **31-person professional services firm** in Irvine, CA. They are currently running a **homegrown field service solution** and are growing fast enough that it can no longer keep up. They are evaluating Salesforce Field Service as the replacement.

The opportunity name encodes the target footprint:
- **+60 FSL Tech licenses** (field technicians)
- **+10 FSL Dispatcher licenses**
- **"Crawl"** = phased/starter deployment

### What SE Is Being Asked To Do

From the DSR (`Reason_for_SE_Involvement__c`):
> Requesting Ken Schatzeder for SFS discovery and strategic demo/positioning. Customer is on a homegrown solution, growing quickly. Has a need to replace their solution with an industry best solution. Request: in depth discovery/reverse demo and demo

SE Next Steps (`SE_Next_Steps__c`):
> Internal engagement and level setting ahead disco/reverse demo. Prepare demonstration to follow

### Demo Approach

This is a **discovery-first** engagement:
1. Internal SE level-set on the account (understand the homegrown system, pain points, growth trajectory)
2. **Reverse demo** — show the customer you understand their world before showing product
3. Targeted FSL demo — focused on replacing a homegrown solution for a 31-person PS firm

Key themes to hit:
- FSL vs. homegrown: why purpose-built wins at scale
- Dispatcher console + scheduling automation (they have dispatchers in scope)
- Mobile for field techs (60 techs)
- Reporting/visibility that a homegrown system can't provide
- "Crawl" path — phased rollout, low risk, fast time to value

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
