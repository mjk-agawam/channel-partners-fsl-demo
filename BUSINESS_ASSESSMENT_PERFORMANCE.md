# Business Performance Assessment - Functional Area Ratings

**Last Updated:** June 24, 2026  
**Source:** Architecture session - Stephen's performance assessment exercise  
**Context:** Team rating effectiveness of different business functions on 1-10 scale

---

## Assessment Methodology

**Stephen initiated a structured assessment** asking the team to rate various business functions on a scale of 1 to 10, where:
- **1-3:** Significant dysfunction, major gaps
- **4-6:** Functional but needs improvement
- **7-8:** Working well, minor gaps
- **9-10:** Best-in-class, competitive advantage

---

## Marketing Effectiveness: 3/10

**Rating:** 3 out of 10 (consensus after discussion)

### Jay's "Loaded Question" Response

Jay described marketing effectiveness as a "loaded question" because **marketing challenges are symptoms of deeper systemic resource optimization issues**, not marketing team failures.

---

## Root Causes (Jay's Analysis)

### 1. Lead Generation Misses Due to Capacity Constraints

**Problem:**
- Opportunities for new business exist (inbound leads, referrals, market expansion)
- Team **lacks bandwidth to pursue them** because resources already constrained
- Large client projects (Target 1,900 stores/week, Samsung/LG installations) consume all available capacity
- Can't scale to take on new work without hiring more reps

**Quote (paraphrased):**
> "While opportunities for lead generation exist, the team often lacks the bandwidth to pursue them because resources are already constrained by large client projects and scheduling is inefficient."

**Impact:**
- Lost revenue (opportunities not pursued)
- Inability to grow beyond existing client base
- Competitive disadvantage (competitors can scale faster)

---

### 2. Unbalanced Resource Ratio (Full-Time vs. Part-Time vs. Floater)

**Problem:**
- Current ratio of **full-time to floating resources is not correctly sized**
- Too many full-time employees sitting idle during slow periods?
- OR too few full-time employees, causing over-reliance on part-time staff?
- No clear definition of "floating" vs. "part-time" vs. "full-time"

**Resource Segmentation Confusion:**
- **Full-time W-2:** Dedicated employees (40+ hours/week)
- **Part-time W-2:** Regular employees (10-30 hours/week, retained, reliable)
- **Floaters/Gig Workers:** On-demand labor (1-5 hours/week, unreliable availability)

**Current State:**
- Treating all "part-time" staff as interchangeable (they are NOT)
- Reliable part-timers should be treated more like full-time (dedicated, trained, predictable)
- True gig workers/floaters should be used only for overflow/peak demand

---

### 3. Over-Reliance on "Part-Timers" as Generic Bucket

**Problem:**
- Part-time staff treated as **"over-abused" generic bucket**
- No distinction between:
  - **Reliable, retained part-timers** (15-30 hours/week, trained, loyal, long-tenure)
  - **True gig workers/floaters** (5-10 hours/week, untrained, transient, no loyalty)

**Impact:**
- Reliable part-timers feel undervalued (treated same as gig workers)
- Scheduling assumes all part-timers are interchangeable (they are NOT)
- Quality issues when gig workers assigned to complex work
- Higher training costs (gig workers churn, must retrain constantly)

**Salesforce Opportunity:**
- **Service Resource Types** to distinguish Full-Time, Part-Time Retained, Floater/Gig
- **Skills-Based Routing** to prioritize reliable part-timers over gig workers
- **Einstein Scheduling** to optimize mix of resource types by project complexity

---

### 4. Lack of Cross-Training (Tactics Locked to Specific Skills)

**Problem:**
- Staff are **locked into specific "tactics"** (merchandising, break/fix, audits, installations)
- Cannot optimize availability or flexibility when assigning work
- Rep with 10 hours free this week CAN'T be assigned to different work type (not trained)
- Must hire new reps to scale new service lines (can't redeploy existing reps)

**Example:**
- Merchandising rep has slow week (only 20 hours scheduled, 20 hours idle)
- Break/fix work available in same geography (need 20 more hours of coverage)
- **Rep can't help** because not trained on break/fix
- Company pays overtime to break/fix reps while merchandising reps sit idle

**Ties to Earlier Discussion:**
- **Cross-functional resource model** (moving from dedicated break/fix teams to multi-tactic reps)
- Organizational resistance (reps/managers prefer dedicated teams)
- Skills/training gap (merch rep doesn't know how to troubleshoot displays)
- Billing complexity (how to allocate time across work types)

**Salesforce Opportunity:**
- **Multi-Skills on Service Resources** (rep can have: Merchandising + Break/Fix + Audits)
- **Skills-Based Routing** to match work to reps with required skills
- **Training Management** (LearnUpon integration OR Trailhead) to track certifications
- **Incentive Management** (bonus for handling multiple work types)

---

## Impact on Marketing Effectiveness

**Why these resource issues tank marketing effectiveness:**

1. **Can't scale to pursue leads:**
   - Sales team brings in new opportunity (new brand client, new retailer)
   - Operations says "we don't have capacity"
   - Lead dies, competitor wins deal

2. **Can't staff proof-of-concept projects:**
   - Prospect wants pilot project (10 stores, 2-week test)
   - Operations can't free up 5 reps for 2 weeks (all booked on existing clients)
   - Prospect goes with competitor who can staff immediately

3. **Can't offer new services:**
   - Market demand for new service line (e.g., EV charger installations, smart home device setup)
   - Would require training existing reps OR hiring new specialized reps
   - Company can't invest in training (reps already fully utilized)
   - Opportunity lost

4. **Inefficient pricing:**
   - Scheduling inefficiencies drive up labor costs (overtime, excess mileage)
   - Must price projects higher to maintain margins
   - Lose deals on price vs. competitors with better scheduling

---

## Salesforce FSL Positioning

**Key Message:**
> "You rated marketing 3/10, but the real issue is resource optimization. Salesforce FSL's intelligent scheduling, skills-based routing, and multi-tactic workforce management unlock 15-20% more capacity WITHOUT hiring. That's your growth engine."

**ROI Calculation:**
- 4,140 reps × 40 hours/week × 52 weeks = 8.6M labor hours/year
- 15% efficiency gain = 1.3M freed hours/year
- At $25/hour billing rate = **$32M additional revenue capacity**
- At 20% margin = **$6.4M/year incremental profit**

**Proof Points to Validate:**
1. What % of rep hours are idle today? (Target, Best Buy slow weeks, seasonal dips)
2. What % of overtime is "avoidable"? (Better scheduling could eliminate it)
3. How many leads were declined in last 12 months due to capacity? (Revenue left on table)
4. What's average drive time per rep per day? (Route optimization opportunity)
5. What % of reps are cross-trained on 2+ tactics today? (Baseline for cross-functional model)

---

## Open Questions for Next Assessment Areas

**Other functional areas to rate:**
- Operations effectiveness (scheduling, dispatch, execution)
- Client service / account management
- Finance / billing / invoicing
- HR / recruiting / retention
- IT / systems / data
- Training / learning & development

**Hypothesis:**
- Operations will rate LOW (scheduling inefficiencies, July 6 rollout risk)
- Finance will rate MEDIUM (Business Central works, but project profitability visibility is poor)
- IT will rate LOW (3 WMS systems, Freshdesk not integrated, RMS Portal not integrated, Mars not integrated)
- Client service will rate MEDIUM (Freshdesk works, but manual processes, no self-service portals)

---

## Next Steps

1. **Continue performance assessment** across other functional areas
2. **Quantify efficiency gaps** (idle time %, overtime %, lead decline rate)
3. **Map gaps to FSL capabilities** (scheduling, skills-based routing, mobile UX)
4. **Build ROI model** (freed capacity → revenue growth → profit)
5. **Identify pilot scope** (single LOB, single geography, 100 reps) to prove value

---

**End of Business Assessment Documentation**
