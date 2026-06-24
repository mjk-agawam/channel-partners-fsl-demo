# Break/Fix Operations - Workflow & Support Center

**Last Updated:** June 24, 2026  
**Source:** Architecture session discussion

---

## Overview

**Break/Fix** is a service line focused on maintaining interactive displays at retail locations. Field technicians troubleshoot issues on-site, often collaborating live with the support center to resolve problems or order necessary parts.

---

## Break/Fix Workflow

### On-Site Troubleshooting

**Field Technician Process:**
1. Rep arrives at store with reported display issue
2. Troubleshoots issue on-site (testing, diagnostics)
3. Collaborates live with support center (phone/chat) if needed
4. Determines if parts are required
5. Orders parts (if approved) OR resolves issue without parts
6. Completes work order with photos/notes
7. Returns later to install parts (if shipped to store)

**Live Collaboration:**
- Field reps connect with support center in real-time
- Support center has visibility into store location, display details, part inventory
- Collaborative problem-solving to avoid unnecessary parts orders

### Parts Ordering & Shipping

**Typical Flow:**
- Parts shipped directly to store (not to rep's home)
- Technician returns to store to install parts when they arrive
- Tracking visible in OpenSky mobile app

**Goal:**
- Minimize go-backs by ensuring correct parts ordered first time
- Reduce troubleshooting time via live support collaboration

---

## Support Center Infrastructure

### Freshdesk (Primary Ticketing System)

**Purpose:**
- Unified ticketing system for phone and chat interactions
- Handles both:
  - **Internal employee support** (IT, system issues, work guidance)
  - **External client-facing issues** (store reports, client escalations)

**Integration with OpenSky:**
- Support teams use OpenSky alongside Freshdesk
- OpenSky provides visibility into:
  - Store locations
  - Part orders
  - Specific display issues
  - Field rep assignments

**Telephony:**
- Multiple telephony systems across different locations (not unified)
- Freshdesk serves as the unified ticketing layer on top of fragmented phone systems

### Issue Reporting Workflow

**When Store or Client Reports Issue:**
1. Issue reported to support center (phone, chat, email)
2. **Account teams upload issue into OpenSky**
3. Issue surfaces as specific task in field rep's mobile app workflow
4. Rep sees issue details, location, parts (if pre-ordered), instructions
5. Rep completes work, updates status in OpenSky
6. Ticket closed in Freshdesk

**Manual Process Today:**
- Account teams manually upload issues into OpenSky
- Not automated from Freshdesk → OpenSky

---

## Second Nature (AI Training Tool)

**Purpose:**
- Tool designed to capture support interactions (calls, chats)
- Feed intelligence back into training models
- Improve rep knowledge and reduce support call volume

**Current State:**
- **Not fully implemented** (exploring, not in production)
- Vision: Analyze support interactions to identify training gaps
- Use case: If 50 reps call about same issue, create training content proactively

---

## Resource Management: Cross-Functional Model

### Current State (LOB Silos)

**Dedicated Break/Fix Teams (~500 reps):**
- Work exclusively on break/fix issues
- Deep expertise in display maintenance
- Predictable scheduling
- Internal preference for dedicated structure

### Future State (Cross-Functional)

**Multi-Tactic Field Staff:**
- Assign multiple "tactics" (skill sets) to field staff
- Same rep can do: merchandising + break/fix + audits
- Optimize resource allocation across LOBs
- Reduce idle time (rep does merch visit, spots break/fix issue, handles it same visit)

**Organizational Goal:**
- Move away from dedicated break/fix teams
- Cross-train reps to handle multiple work types
- Requires: incentive changes, training, systems support

**Challenge:**
- Internal resistance (reps/managers prefer dedicated teams)
- Skills/training gap (merch rep may not know how to troubleshoot displays)
- Billing complexity (how to allocate time across multiple work types in same visit)

---

## Integration Points

### OpenSky ⟷ Freshdesk

**Current State:**
- Support teams use both systems side-by-side
- No automated integration
- Account teams manually upload issues from Freshdesk → OpenSky

**Desired State:**
- Freshdesk ticket → Auto-create work order in OpenSky
- OpenSky work order status → Auto-update Freshdesk ticket
- Bidirectional sync

### OpenSky ⟷ WMS (Parts)

**Parts Workflow:**
1. Rep or support center identifies parts need
2. Parts ordered in OpenSky (approval required for high-value items)
3. OpenSky → WMS (Project Center, Sphere, or Launch)
4. WMS → Shipping provider (UPS/FedEx)
5. Tracking data → OpenSky
6. Rep sees tracking in mobile app
7. Rep installs parts at store

---

## Salesforce Mapping

### Break/Fix Operations

| OpenSky Component | Salesforce Equivalent | Notes |
|---|---|---|
| **Support Center (Freshdesk)** | Service Cloud (Cases) | Unified ticketing for internal + external |
| **Telephony (fragmented)** | Service Cloud Voice OR Amazon Connect | Unified telephony layer |
| **Live collaboration (rep + support)** | Slack + Einstein Bots | Real-time collaboration, AI-assisted troubleshooting |
| **Issue → Work Order** | Case → Work Order (automated) | Flow automation, no manual upload |
| **Parts ordering** | Asset Management + Product Request | Parts catalog, approval workflows |
| **Second Nature (AI training)** | Einstein Discovery + Trailhead | Analyze support interactions, auto-generate training content |
| **Cross-functional resource model** | Skills-Based Routing + Multi-Skills | Assign reps with multiple skills (merch + break/fix) |

### Salesforce Differentiators

**Service Cloud Integration:**
- Case → Work Order automation (no manual upload by account teams)
- Omni-Channel routing (phone, chat, email unified)
- Einstein Bots (deflect simple support calls, guide reps through troubleshooting)

**Einstein AI:**
- Analyze support interactions to identify training gaps (replace Second Nature)
- Recommend next best action for field reps (troubleshooting steps, parts to order)
- Predict which issues require go-backs (alert before rep leaves site)

**Skills-Based Routing:**
- Match work orders to reps with multiple skills (merch + break/fix)
- Support cross-functional resource model
- Optimize utilization across LOBs

**Experience Cloud:**
- Store contacts can self-report issues (portal)
- Client portals for issue tracking (Samsung, LG see their display issues in real-time)

---

## Open Questions

**Support Center:**
1. How many support center agents? (Internal IT support vs. client-facing?)
2. What % of support calls are from field reps vs. stores vs. clients?
3. Average handle time for support calls?
4. What % of issues can be resolved without dispatching a field rep?
5. Freshdesk feature usage - using knowledge base, macros, SLAs, routing?

**Break/Fix Operations:**
6. How many break/fix reps today? (~500 estimated, confirm?)
7. What % of break/fix work requires parts? (vs. troubleshooting only?)
8. Average time from issue report → rep dispatched → issue resolved?
9. What % of break/fix issues result in go-backs? (Wrong parts, incomplete troubleshooting?)
10. What's the cost per break/fix visit? (Labor, mileage, parts?)

**Cross-Functional Model:**
11. Timeline for cross-functional rollout? (Pilot in 2027? Full rollout 2028?)
12. Which LOBs will cross-train first? (Merch + break/fix? Merch + audits?)
13. What incentive changes needed? (Bonus for handling multiple work types?)
14. How will billing work? (Split time between work types? Single rate for multi-tactic reps?)

**Freshdesk Integration:**
15. Is Freshdesk → OpenSky integration a priority? (Q4 2026? 2027?)
16. If Salesforce replaced OpenSky, would you also replace Freshdesk with Service Cloud?
17. Or would Freshdesk remain and need integration with Salesforce FSL?

**Second Nature:**
18. Timeline for Second Nature implementation? (Still evaluating? Pilot in 2027?)
19. If Salesforce replaced OpenSky, could Einstein Discovery replace Second Nature?

---

**End of Break/Fix Operations Documentation**
