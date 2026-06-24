# RMS Merger & Integration Challenge

**Last Updated:** June 24, 2026  
**Source:** Architecture session discussion

---

## Overview

**RMS** is a Minnesota-based company recently acquired by Channel Partners. RMS operates on a distinct homegrown system called "Portal" that is NOT currently integrated with OpenSky.

---

## RMS Business Profile

**Primary Business Line:**
- **80% merchandising for a single retailer**
- Dedicated retail relationship (likely Target, Best Buy, or similar major chain)
- Minnesota-based operations

**Current State:**
- Uses homegrown system called "Portal" for workforce management
- Payroll migrated to Channel Partners' ADP instance
- Operational workflows still separate from OpenSky

---

## Integration Status

### Completed
- ✅ Payroll moved to Channel Partners ADP instance

### In Progress / Delayed
- ❌ Full migration to OpenSky **delayed**
- Reason: Complexity of reconciling distinct project setup and operational structures

---

## Integration Challenges

### Project Setup Differences

**RMS "Portal" System:**
- Custom-built for single-retailer operations
- Likely optimized for their specific merchandising workflows
- 20+ years of accumulated business logic and customizations

**Challenge:**
- RMS project structure may not map cleanly to OpenSky Call Form/Wave/Bucket hierarchy
- Single-retailer focus vs. OpenSky multi-client model
- Different terminology, workflows, reporting requirements

### Operational Structure Differences

**Potential Gaps:**
1. **Scheduling:** RMS may use different scheduling logic (dedicated teams, recurring visits, different optimization rules)
2. **Time tracking:** Different payroll codes, expense categories, mileage calculations
3. **Reporting:** Client may have custom reporting formats that don't exist in OpenSky
4. **Survey structure:** Different data collection requirements (question types, photo workflows, signature capture)
5. **Billing/invoicing:** Different job costing structure, rates, contractual terms

---

## Migration Strategy Questions

**Timing:**
1. What's the target date for full RMS → OpenSky migration?
2. Is this blocked on July 6 OpenSky rollout stabilization?
3. Or is this a 2027+ initiative?

**Approach:**
4. Will RMS migrate to OpenSky as-is? Or will OpenSky be customized to match RMS workflows?
5. Is "Portal" staying live indefinitely? Or sunset after migration?
6. How many RMS field reps? (Scale of migration effort?)
7. Are RMS reps W-2 employees of Channel Partners now? Or still separate entity?

**Technical:**
8. Does RMS Portal have APIs? Or is data extraction manual?
9. Is there historical data migration requirement? (Past projects, completed work, rep profiles?)
10. What's the cutover strategy? (Big bang vs. phased by region/client/function?)

**Business:**
11. Does RMS's single-retailer client need to approve new systems? (Contract clause?)
12. Are RMS billing rates different from Channel Partners standard rates?
13. Does RMS have dedicated account management? Or will they use Channel Partners account teams?

---

## Salesforce Opportunity

### Unified Platform (Replace Both Portal + OpenSky)

**Benefits:**
- Single platform for all 4,140+ Channel Partners reps + RMS reps
- Avoid dual system maintenance (OpenSky + Portal)
- Standardize workflows across merged entity
- Single source of truth for payroll, scheduling, time tracking

**Approach:**
- FSL Work Types map to different business lines (Channel Partners multi-client vs. RMS single-retailer)
- Service Territories for geographic/operational divisions
- Custom objects/fields to preserve RMS-specific requirements
- Experience Cloud for client-specific portals (if RMS client needs custom reporting)

### Migration Accelerator

**If OpenSky stays:**
- MuleSoft could integrate Portal → OpenSky during transition period
- Data Loader for historical data migration
- Einstein Analytics for unified reporting across both systems (during dual-system period)

---

## Open Questions

**RMS Business:**
1. How many field reps does RMS have? (Scale?)
2. What's RMS annual revenue? (% of total Channel Partners revenue?)
3. Is RMS's single-retailer client also a Channel Partners client?
4. Are there other RMS clients beyond the 80% retailer? (20% = ?)
5. Does RMS do break/fix, installations, audits? Or only merchandising?

**RMS Portal System:**
6. Who built Portal? (In-house dev team? Vendor? Consultant?)
7. Does RMS have a dev team that would transition to OpenSky customization?
8. What's Portal's tech stack? (Web-based? Mobile app? Desktop?)
9. Does Portal have mobile offline capabilities like OpenSky?

**Integration Timeline:**
10. What's blocking the migration today? (Technical complexity? Resource bandwidth? Business priority?)
11. Is Jay's CTO team responsible for RMS migration? Or separate RMS IT team?
12. Are there other recent acquisitions beyond RMS? (Pattern of M&A integration challenges?)

**Payroll Integration:**
13. How does payroll work today? (RMS reps → ADP via Portal? Or manual upload?)
14. Does GAMS handle RMS payroll? Or direct to ADP?
15. Are RMS reps using SmarterMail? Or separate email system?

---

## Salesforce Positioning

**Channel Partners is a PE-backed roll-up.** RMS is likely the first of multiple acquisitions. Each acquisition brings:
- Different homegrown systems
- Different operational workflows
- Integration complexity and cost

**Key Message:**
> "Every acquisition is a 6-12 month integration project on OpenSky. What if the next 3 acquisitions could onboard in 30 days on Salesforce? Standardized platform, proven M&A playbook, Experience Cloud for client-specific customization."

**Deal Sizing:**
- If RMS has 500 reps → another $1M+ in FSL licenses
- If PE playbook is "acquire 5 companies in next 3 years" → $5M+ recurring revenue opportunity

---

**End of RMS Documentation**
