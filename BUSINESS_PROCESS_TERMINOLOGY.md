# Business Process Terminology & Value Stream

**Last Updated:** June 24, 2026  
**Source:** Architecture session discussion

---

## Preferred Terminology

Channel Partners has clarified their preferred terminology for business processes to ensure alignment across discussions:

---

## Value Stream Stages

### 1. SOW/Contracts
**Preferred Term:** SOW/Contracts  
**NOT:** Marketing/Sales  

**Description:**
- Statement of Work (SOW) creation
- Contract negotiation with brands and retailers
- Pricing, scope, timeline definition

**Systems:**
- Business Central (ERP) for contract management?
- Salesforce opportunity: **Sales Cloud** for pipeline management, CPQ for SOW generation

---

### 2. Project Kick-off / Initiation
**Preferred Term:** Project Kick-off / Initiation  
**Also Known As:** Install phase  

**Description:**
- Project setup after contract signed
- Call Form creation in OpenSky
- Wave definition (timeframes, store assignments)
- Resource allocation (rep skills, availability)
- Training requirements (LearnUpon courses)

**Systems:**
- OpenSky (Call Form/Wave setup)
- LearnUpon LMS (training assignment)
- Salesforce opportunity: **Project Management** custom app OR **Work Orders** for project containers

---

### 3. Client Service
**Preferred Term:** Client Service  
**Umbrella Term Covering:**
- Retail partner interactions (Target, Best Buy, etc.)
- Brand client interactions (Samsung, LG, etc.)

**Description:**
- Ongoing relationship management
- Issue escalation and resolution
- Performance reporting
- Contract renewals

**Systems:**
- Freshdesk (support ticketing)
- Tableau (client portals for reporting)
- Email (account team communication)
- Salesforce opportunity: **Service Cloud** for case management, **Experience Cloud** for client portals

---

## Operational Work Types

### Experiential Marketing & Brand Activations

**Definition:**
- Live events, product launches, in-store demos
- Brand ambassador staffing
- Pop-up retail experiences

**Current State:**
- **Billable work** (revenue-generating)
- Mechanics happen **outside OpenSky** today
- Desire to bring into OpenSky as business grows

**Challenge:**
- Different workflow from routine merchandising/break-fix
- Event-based scheduling (one-time, not recurring)
- Higher labor rates, premium staffing requirements
- More client-facing (brand reps on-site during events)

**Salesforce Opportunity:**
- **Events Management** custom app OR **Work Orders** with custom Event record type
- **Einstein Scheduling** for complex event staffing (availability, skills, geography)
- **Experience Cloud** for brand client visibility into event execution

---

## HR & Administrative Systems

### Expenses and Hours

**Field Staff:**
- Use OpenSky to log hours and expenses
- Time tied to specific visit (job costing)
- Expense photos (receipts) attached to visits
- Manager approval workflow

**Corporate Exceptions:**
- Some corporate employees may use different system (ADP? Business Central?)
- Need to clarify: Do corporate employees use OpenSky? Or separate expense system?

**Salesforce Opportunity:**
- **Field Service Mobile** for time/expense entry (already standard in FSL)
- **Expense Management** (standard Salesforce object OR AppExchange app like Certinia)

---

### Travel Management

**Current Workflow:**
1. Travel request initiated in OpenSky
2. Request reviewed by manager
3. **Booking happens in "Agency" (Amex) portal** (NOT OpenSky)
4. Travel booked by:
   - Manager (for most field reps)
   - Travel agent (for complex/international travel)
   - Employee directly (for specific high-level roles only)

**Integration Gap:**
- OpenSky → Agency is manual (no API integration)
- Travel booking data does NOT flow back into OpenSky automatically
- Reps may not see flight/hotel details in OpenSky mobile app

**Current Pain Points:**
- Manual handoff between OpenSky and Agency portal
- No visibility into travel costs until after booking (can't see cost before approval)
- Travel itinerary not visible in mobile app (reps need separate email/app for flight details)

**Salesforce Opportunity:**
- **Travel Management** custom app OR **Travel Requests** custom object
- API integration to Amex or travel booking platform (Concur, TripActions, etc.)
- Itinerary display in Field Service Mobile (flights, hotels, rental cars)
- Real-time travel cost visibility for approval workflow
- Automatic expense creation (airfare, hotel pre-populated into expense report)

---

## Open Questions

**SOW/Contracts:**
1. What system manages SOW today? (Business Central? OpenSky? Separate CRM?)
2. Is there a pipeline management tool? (Sales forecasting, opportunity tracking?)
3. Who creates SOWs? (Account teams? Sales team? Operations?)
4. How long from SOW signature to project kick-off? (Days? Weeks?)

**Project Kick-off:**
5. Who sets up Call Forms in OpenSky? (Account teams? Project managers? Operations?)
6. Is there a standard project template? (Reusable Call Form structure?)
7. How long does project setup take? (Hours? Days?)

**Client Service:**
8. Is "Client Service" a dedicated team? Or handled by account managers?
9. Does Freshdesk route tickets to Client Service team? Or to account managers?
10. What % of client service interactions are reactive (issues) vs. proactive (relationship building)?

**Experiential/Activations:**
11. What % of revenue is experiential/activations today? (Vs. merchandising, break-fix, etc.?)
12. How many events per year? (Dozens? Hundreds?)
13. Are events always in-store? Or also outdoor/venue-based?
14. Do events use dedicated staff? Or same field reps as merchandising?
15. Why are events not in OpenSky today? (System limitation? Business decision?)

**Expenses:**
16. What % of corporate employees use OpenSky vs. separate expense system?
17. Are corporate expenses tied to projects? (Job costing?) Or just general admin expenses?
18. Is there approval hierarchy for high-value expenses? (Travel, equipment purchases?)

**Travel:**
19. What % of field reps travel regularly? (Vs. local/regional work only?)
20. Average # of trips per rep per month?
21. Does "Agency" refer to Amex GBT (Global Business Travel)? Or different provider?
22. Is there API available from travel provider? (For integration with Salesforce/OpenSky?)
23. How is travel cost allocated? (Job costing by project? Or general overhead?)
24. Do reps book own hotels? Or always through Agency?

---

## Salesforce Value Stream Mapping

| Stage | Current System | Salesforce Equivalent | Gap Closed |
|-------|----------------|----------------------|------------|
| **SOW/Contracts** | Business Central? | Sales Cloud + CPQ | Pipeline visibility, automated SOW generation |
| **Project Kick-off** | OpenSky (Call Form) | Work Orders + Project Management | Standardized templates, faster setup |
| **Execution** | OpenSky (mobile, scheduling) | Field Service Mobile + Scheduling | Real-time updates, better mobile UX |
| **Client Service** | Freshdesk + Email | Service Cloud + Experience Cloud | Unified ticketing, client self-service portals |
| **Reporting** | Snowflake → Tableau | Einstein Analytics (CRM Analytics) | Real-time reporting, no 4-hour ETL lag |
| **Experiential/Events** | Manual / Outside OpenSky | Custom Events App | Structured workflow, better client visibility |
| **Expenses** | OpenSky | FSL Time/Expense OR Certinia | Already standard in FSL |
| **Travel** | OpenSky → Agency (manual) | Custom Travel App + API | Itinerary in mobile app, cost visibility |

---

**End of Business Process Terminology Documentation**
