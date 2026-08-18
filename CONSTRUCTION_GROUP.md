# Construction Group - Third-Party Contractor Model

**Last Updated:** June 24, 2026  
**Source:** Architecture session discussion

---

## Overview

**Construction Group** is a distinct line of business (LOB) focused on building out entire store sections rather than routine maintenance or break-fix work.

---

## Scope of Work

**Construction Projects:**
- Building out entire store sections
- Examples:
  - Flooring installation (full department)
  - Table/fixture installation (demo areas)
  - TV wall installations (electronics sections)
  - End-to-end buildouts (new store openings, major remodels)

**NOT in Scope:**
- Routine merchandising (product placement, signage updates)
- Break-fix (display troubleshooting, parts replacement)
- Audits (compliance checks, inventory counts)

---

## Labor Model: Third-Party Contractors (Not W-2 Employees)

**Key Distinction:**
- Construction work performed by **third-party contractors**
- Paid via **invoice** (not payroll)
- NOT W-2 employees of Channel Partners

**Comparison to Other LOBs:**

| LOB | Labor Type | Payment Method | System Used |
|-----|------------|----------------|-------------|
| **Merchandising** | W-2 employees | ADP payroll | OpenSky |
| **Break-Fix** | W-2 employees | ADP payroll | OpenSky |
| **Audits** | W-2 employees | ADP payroll | OpenSky |
| **Installations (small)** | W-2 employees | ADP payroll | OpenSky |
| **Construction (large)** | Third-party contractors | Invoice/AP | Project Center (NOT OpenSky) |

---

## Workflow: Link-Based Call Form Entry (Not Standard System Access)

**Current Process:**

1. **Project setup:**
   - Construction project created in Project Center (NOT OpenSky)
   - Call Form generated with survey questions
   - Unique link generated for contractor access

2. **Contractor access:**
   - Contractor receives **link** (via email or text)
   - Clicks link → Opens call form in browser (no login required)
   - Completes survey questions, uploads photos
   - Submits form
   
**John's Explanation:** "They use essentially the call form where they it's like a link on a phone to a website that they fill out and then they fill it out... once they fill it out that information then sends to us and then we create invoices for them"

3. **Data flow:**
   - Completed call form data stored in Project Center
   - Channel Partners account team reviews submission
   - Invoice generated based on completed work
   - Contractor paid via AP (not payroll)

**Key Point:**
- Contractors do NOT have OpenSky accounts (no login, no mobile app access)
- Link-based access only (similar to guest user model)
- Limited functionality (can only complete assigned call form, can't see schedule, can't see other projects)

---

## System Limitation: Project Center Used Because OpenSky Lacks Subcontractor Tracking

**Why Construction NOT in OpenSky:**

**Quote (paraphrased):**
> "Construction work is managed in 'Project Center' because Open Sky lacks the mechanisms to track subcontractors."

**What OpenSky Can't Do Today:**
1. **Contractor profiles:**
   - No "contractor" resource type (only W-2 employee profiles)
   - Can't track contractor availability, skills, certifications
   - Can't assign work to contractor in scheduling module

2. **Invoice-based payment:**
   - OpenSky time tracking tied to ADP payroll (hourly wage × hours worked)
   - No mechanism for "flat fee" or "project-based" contractor invoicing
   - Can't track contractor rates that differ from employee rates

3. **Limited access model:**
   - OpenSky assumes full mobile app access for all users
   - No "guest user" or "link-only" access model
   - Contractors would need full OpenSky login (security concern, licensing cost)

4. **Project-based costing:**
   - Construction projects billed as fixed price (not time & materials)
   - OpenSky job costing designed for hourly labor + expenses + parts
   - Can't easily model "contractor submits $10K invoice for completed buildout"

---

## Integration Goal: Bring Construction into OpenSky (No Immediate Mechanism)

**Desired Future State:**
- All LOBs managed in single platform (OpenSky)
- Unified reporting (W-2 employees + third-party contractors)
- Cross-LOB resource visibility (can a W-2 employee help with construction project?)

**Blockers:**
> "The team identified the need to eventually integrate this line of business into Open Sky, though no immediate mechanism exists."

**Why No Immediate Solution:**
1. **OpenSky roadmap doesn't include contractor management** (focused on W-2 employee features)
2. **Project Center works well enough for now** (not urgent to migrate)
3. **Construction is small % of revenue** (prioritize merchandising, break-fix first)
4. **Custom development required** (would need to build contractor tracking from scratch)

---

## Salesforce Opportunity: Unified Workforce Management (W-2 + Contractors)

### Service Resources with Resource Types

**Salesforce FSL Supports:**
1. **Service Resource Types:**
   - Employee (W-2, paid via payroll)
   - Contractor (1099, paid via invoice)
   - Partner (third-party firm, paid via AP)
   - Crew (team of mixed resource types)

2. **Different Payment Models:**
   - Employee: Hourly rate × time tracked
   - Contractor: Flat fee per project OR hourly rate (different from employee rate)
   - Partner: Invoice-based (no time tracking, just completion milestone)

3. **Limited Access via Experience Cloud:**
   - Contractors get Community license (lower cost than full FSL license)
   - Access via mobile-responsive web portal (not full FSL Mobile app)
   - Can view assigned Work Orders, complete surveys, upload photos
   - Can't see schedule, can't see other projects, can't message other users

4. **Unified Scheduling:**
   - Same Work Order object for W-2 employees + contractors
   - Skills-Based Routing works across all resource types
   - Can assign W-2 employee to help contractor if needed (flex across resource types)

5. **Unified Reporting:**
   - Single dashboard showing all construction projects (W-2 + contractor)
   - Margin calculation includes contractor invoice costs (not just W-2 labor)
   - Client sees same reporting format (doesn't matter if work done by employee or contractor)

---

### Example Use Case: Mixed Team Construction Project

**Scenario:**
- Major retailer remodel: $500K project, 3 weeks duration
- Work breakdown:
  - Flooring: Third-party contractor (specialist firm, $200K flat fee)
  - Fixtures: Channel Partners W-2 installation team (5 people, 2 weeks, $150K labor)
  - TV wall: Third-party contractor (AV specialist, $100K flat fee)
  - Project management: Channel Partners W-2 project manager (full 3 weeks, $50K loaded cost)

**In Salesforce FSL:**

1. **Single Work Order (project container):**
   - Total value: $500K
   - Duration: 3 weeks
   - Location: Store #1234

2. **Child Work Orders (phases):**
   - Flooring Work Order → Assigned to Contractor A (third-party firm)
   - Fixtures Work Order → Assigned to 5 W-2 employees (installation team)
   - TV Wall Work Order → Assigned to Contractor B (AV specialist)
   - PM Work Order → Assigned to W-2 project manager

3. **Contractor access:**
   - Contractor A gets Experience Cloud portal login
   - Sees only Flooring Work Order
   - Completes survey, uploads photos, marks complete
   - Submits invoice ($200K) via portal

4. **W-2 employee access:**
   - Installation team gets FSL Mobile app
   - Sees only Fixtures Work Order
   - Tracks time daily (5 people × 10 days × 8 hours = 400 hours)
   - Time flows to payroll automatically

5. **Unified visibility:**
   - Project manager sees ALL 4 Work Orders in single dashboard
   - Client portal shows overall project status (all phases visible)
   - CFO sees margin calculation (revenue $500K - costs $500K = break-even, but this is example)

---

## Comparison: OpenSky/Project Center vs. Salesforce FSL

| Capability | OpenSky + Project Center | Salesforce FSL |
|------------|--------------------------|----------------|
| **W-2 employee management** | ✅ OpenSky (full featured) | ✅ FSL (full featured) |
| **Contractor management** | ⚠️ Project Center (separate system) | ✅ FSL (same platform, Resource Type = Contractor) |
| **Unified scheduling** | ❌ Separate systems (OpenSky for W-2, Project Center for contractors) | ✅ Same Work Order object, Skills-Based Routing works across types |
| **Guest/limited access** | ⚠️ Link-based (no login, no mobile app) | ✅ Experience Cloud (Community login, mobile-responsive portal) |
| **Invoice-based payment** | ⚠️ Manual AP process (not integrated with Project Center) | ✅ Invoice object linked to Work Order (AP automation possible) |
| **Unified reporting** | ❌ Must combine data from OpenSky + Project Center | ✅ Single dashboard (all resource types, all LOBs) |
| **Mixed teams** | ❌ Can't schedule W-2 + contractor on same project in system | ✅ Crew scheduling (mix resource types on one Work Order) |

---

## Migration Path: Construction → Salesforce FSL

**Phase 1: Parallel Operation (Months 1-3)**
- Keep Project Center for existing construction projects
- Start NEW construction projects in Salesforce FSL (pilot with 1-2 contractors)
- Validate contractor Experience Cloud portal works (survey completion, photo upload)
- Test invoice workflow (Work Order complete → Invoice generated → AP approval)

**Phase 2: Onboard Contractor Firms (Months 4-6)**
- Migrate 5-10 key contractor firms to Experience Cloud
- Train contractors on portal (vs. link-based call forms)
- Validate unified reporting (W-2 + contractor projects in same dashboard)

**Phase 3: Sunset Project Center (Months 7-9)**
- Complete all in-flight Project Center projects
- Historical data migration (optional, may leave in Project Center for archive)
- Decommission Project Center (cost savings, one less system to maintain)

---

## Open Questions

**Construction Group Operations:**
1. How many third-party contractors work on construction projects? (Firms? Individual contractors?)
2. What % of Channel Partners revenue is construction? (vs. merchandising, break-fix, etc.?)
3. Average construction project size? ($10K? $100K? $1M?)
4. Average construction project duration? (Days? Weeks? Months?)
5. How many construction projects active at any given time? (Dozens? Hundreds?)

**Project Center System:**
6. Is Project Center homegrown or third-party vendor?
7. What other functionality does Project Center provide? (Just construction? Or other use cases?)
8. Who maintains Project Center? (Jay's IT team? Separate vendor?)
9. Timeline for Project Center sunset? (2027? 2028? Never?)

**Contractor Management:**
10. How are contractors sourced? (RFP? Network? Referrals?)
11. Do contractors have insurance/bonding requirements? (Tracked in system?)
12. Are there preferred contractor lists? (Pre-vetted firms?)
13. Do contractors ever work alongside W-2 employees on same project?
14. What's the payment terms for contractors? (Net 30? Net 60? Upon completion?)

**Link-Based Access:**
15. Is link-based access secure? (Anyone with link can submit? Or authenticated somehow?)
16. How often do contractors need technical support? (Call form issues, photo upload failures?)
17. Do contractors ever need to see their historical projects? (Or just current project?)

---

**End of Construction Group Documentation**
