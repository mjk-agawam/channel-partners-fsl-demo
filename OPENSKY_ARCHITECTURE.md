# OpenSky Platform Architecture - Detailed Technical Specification

**Last Updated:** June 24, 2026  
**Source:** June 18 reverse demo + June 24 architecture session

---

## Table of Contents

1. [Core Data Model](#core-data-model)
2. [Integration Landscape](#integration-landscape)
3. [Survey System Architecture](#survey-system-architecture)
4. [Data Warehouse & Reporting](#data-warehouse--reporting)
5. [Mobile Architecture](#mobile-architecture)
6. [Scheduling Modes](#scheduling-modes)
7. [Salesforce Mapping](#salesforce-mapping)

---

## Core Data Model

### Call Form (Project Container)

**Call Form** is the top-level container object that serves as a project master structure:

**Functions:**
- **Project Management:** Acts as the central object for specific pieces of work
- **Execution Scheduling:** Contains "waves" that define timeframes of execution
- **Operational Setup:** Specifies primary tactic and assigns locations (stores)
- **Resource Alignment:** Uses profiles/tags to match skill sets to store needs
- **Data Collection:** Houses survey configuration (questions and setup)

**Hierarchy:**
```
Call Form (Project)
  └─ Wave(s) — time-bounded execution (weekly, monthly, custom)
      └─ Store(s)/Location(s) — assigned under each wave
```

### Wave (Execution Timeframe)

**Wave** defines the execution window for a call form:

**Attributes:**
- Time-bounded (weekly, monthly, or custom duration)
- Expected visit duration
- Store count
- Can be recurring or one-time

**Example:** Target merchandising might have:
- Call Form: "Target Q3 2026 Resets"
- Wave 1: "Week of July 1-7" (stores 1-500)
- Wave 2: "Week of July 8-14" (stores 501-1000)

### Bucket (Assignment Tool)

**Bucket** is the matching/routing engine that assigns work to reps:

**Matching Logic:**
- Distance (radius-based, e.g., 30 miles)
- Skills/tactics (installation, merchandising, etc.)
- Position type (dedicated vs. shared)
- Availability
- Manual overrides allowed

### Tactics (Skill Sets)

**Tactics** are the primary skill requirements tagged to individual profiles:

**Examples:**
- Installation
- Merchandising
- Break-fix
- Audits
- Training/demos

**Usage:**
- Tagged to rep profiles
- Used for matching stores to personnel
- Combined with geographic proximity for assignment

---

## Integration Landscape

### Full Integration Map

```
┌─────────────┐
│   iCIMS     │ ──► Recruiting & Onboarding
└─────────────┘
       │
       ▼
┌─────────────┐
│    GAMS     │ ──► Payroll Aggregation + Unique ID Generation
└─────────────┘     (solves cross-country ADP file number issues)
       │
       ▼
┌─────────────┐
│    ADP      │ ──► Payroll Processing
└─────────────┘
       │
       ▼
┌─────────────┐
│    AWS      │ ──► Middleware (Step Functions + Microservices)
└─────────────┘
       │
       ▼
┌──────────────────────────────────────────────────┐
│              OPEN SKY PLATFORM                   │
│  • Call Forms / Waves / Buckets                  │
│  • Survey Engine                                 │
│  • Mobile Sync (offline-first)                   │
│  • Time Entry & Expenses                         │
│  • Parts Management                              │
│  • Team Scheduling                               │
└──────────────────────────────────────────────────┘
       │
       ├──────────► Business Central (ERP: job costing, invoicing)
       ├──────────► LearnUpon LMS (certifications, training)
       ├──────────► WMS (warehouse: pick/pack/ship)
       ├──────────► Agency (travel booking: flights/hotels)
       ├──────────► Snowflake (data warehouse: ETL 4x/day)
       └──────────► Client APIs (Samsung, LG: file/API feeds)
                            │
                            ▼
                    ┌──────────────┐
                    │   Tableau    │ ──► Client Portals + Internal BI
                    └──────────────┘
```

### Integration Details

#### 1. iCIMS → GAMS → ADP → AWS → OpenSky (Employee Master Data)

**iCIMS (Recruiting/Onboarding):**
- Recruitment process automation
- Candidate management
- Offer letter generation
- Service integration capabilities

**GAMS (Gems) - Payroll & Incentive Middleware:**
- **Unique ID generation:** Enterprise-wide ID assignment (solves cross-country ADP file number conflicts)
- **Payroll aggregation:** Overtime + regional calculations before ADP export
- **Incentive/commission calculations:** Third-party application for comp calculations
- **SmarterMail account trigger:** Creates SmarterMail accounts for part-time staff
- **Data integration:** Middle layer between internal systems and ADP

**ADP (Payroll System):**
- Payroll processing
- Time card imports from OpenSky
- Expense reimbursement
- Overtime calculation (after-the-fact)

**AWS (Middleware):**
- Step functions for data orchestration
- Microservices for ADP → OpenSky sync
- Employee profiles, roles, team assignments

**Flow:**
```
iCIMS (recruit/hire) 
  → GAMS (assign enterprise ID, aggregate payroll, calculate incentives, trigger SmarterMail) 
    → ADP (process payroll) 
      → AWS (step functions) 
        → OpenSky (profiles, teams, hierarchies)
```

#### 2. OpenSky → Business Central (ERP)

**Data Flow:**
- Job costing by project (all time, mileage, expenses tracked to job number)
- Invoicing (project-level billing to clients)
- Financial reporting

**Pain Point:**
- No real-time project profitability visibility
- Can't see client-level view (only project-level)

#### 3. OpenSky → LearnUpon LMS (Learning Management)

**Data Flow:**
- **Two-way feed:** Users/teams out, completions back
- Course completions block reps from starting work (if required)
- Certifications tracked

**On-the-fly Training:**
- Cloud-stored resources linked in OpenSky
- Not full LMS courses
- Accessible via mobile app Resources section

#### 4. OpenSky ⟷ WMS (Warehouse Management)

**Current WMS Landscape (3 Systems):**
1. **Project Center WMS** - Homegrown system
2. **Sphere** - Third-party platform
3. **Launch** - Third-party system

**Integration Priority:**
- Goal: Consolidate 3 WMS into single enterprise solution
- Risk: Breaking existing custom integrations (particularly Samsung)
- Mitigation strategy: API gateway/proxy layer to decouple integrations from underlying WMS (allows system swaps without forcing clients to rework their integrations)

**Data Flow:**
- Parts requests pushed from OpenSky to warehouse
- Pick/pack/ship integration
- Tracking data flows back to OpenSky
- Rep sees shipment status on mobile

**Parts Workflow:**
1. Call center or survey creates parts request
2. Parts team approves/rejects
3. Pushed to warehouse system
4. Pick/pack/ship
5. Tracking data → OpenSky
6. Rep mobile app shows status

#### 5. OpenSky → Agency (Travel Platform)

**Data Flow:**
- Travel requests from OpenSky (multi-day projects)
- Booking: flights, hotels, rental cars
- Itinerary management
- Details flow back to OpenSky

**Volume:**
- "Insane amount of money" on travel annually
- Multi-person teams (5-15 reps)
- Often fly in from multiple regions
- Last-minute changes common

#### 6. OpenSky → Snowflake → Tableau (Data Warehouse)

**ETL Frequency:** 4 times per day

**Data Integration Architecture:**
- **SFTP + S3 buckets:** Data staged in S3 buckets for integration
- **Snowflake:** Central ETL provider for processing and repository storage
- **Flow:** Source systems → SFTP → S3 staging → Snowflake (ETL) → Tableau/PowerBI

**Snowflake Data Sources (Beyond OpenSky):**
1. **Client POS data:** Via client API integrations (Samsung, LG, etc.)
2. **ADP HR reports:** Payroll/personnel data
3. **Third-party site data:**
   - Geospatial data
   - Demographics
   - Retail traffic (e.g., Best Buy foot traffic)
   - Location insights
4. **Mars system data:** Third-party labor management (see below)

**Tableau Output:**
- Client portals (company-controlled data models)
- Clients can pay for raw data access (self-service analytics)
- Internal BI dashboards
- Access limited due to licensing costs

**Pain Point (James Dyer):**
- 4-hour latency minimum
- Must request full date range, manually derive delta
- No change data capture (CDC) capability
- Want: "Please give us a delta" (real-time incremental updates)

#### 7. OpenSky → Client APIs (Samsung, LG, Others)

**Data Export Methods:**
- File extracts (CSV)
- Legacy API gateways
- Modern APIs (migration in progress)

**Data Ownership:**
- Company prefers internal retention ("authoritative intelligence")
- Major clients require direct access for their analytics
- Contractual SLA alignment (granular vs. high-level)

#### 8. PowerBI (Internal Reporting)

**Purpose:** Internal operations dashboards
**Source:** Snowflake data warehouse (same 4x/day ETL)

---

## Survey System Architecture

### Overview

**Survey = Collection of Questions** subdivided into **Tasks** for mobile app stability/performance.

**Scale:**
- 600-1,200 questions per survey (potential)
- Individual visits typically involve fewer
- Subdivided into tasks for manageability

### Components

#### Question Library

**Reusable question bank** allowing:
- Custom questions per project
- Shared question instances across multiple call forms/projects
- Question sets that can be attached to multiple projects

#### Question Types

1. **Standard Questions:**
   - Multiple choice
   - Text entry
   - Photo capture
   - Signature
   - Date/time

2. **Grid Questions:**
   - Ask same question across multiple items/SKUs simultaneously
   - Example: "Verify price tag for 20 SKUs" → single grid instead of 20 separate questions

3. **Conditional Questions:**
   - Parent/child logic
   - Display rules based on prior answers
   - Can pivot based on:
     - Store attributes
     - Date ranges
     - Product/SKU presence
     - Prior question responses

### Survey Configuration

**Client Service Manager** sets up:
- One survey or project
- Attribute to multiple waves or stores
- Create once, use across many visits

**Quote (Kari):**
> "The client service manager sets up one survey or project and they can attribute however many waves or stores they want to that individual survey. They create one survey, they can do as many visits as they want on it."

### Mobile Workflow

**Sync Process:**
- Surveys synced to mobile app
- **Offline-first architecture** with local XML file
- Data entry works without cellular connectivity
- Syncs when connectivity returns

**Tasks:**
- Field reps navigate specific sections (e.g., inventory, fixture installation)
- Not a single massive form
- Improves performance and usability

### Field Use Cases

**Examples:**
- Inventory verification
- Task completion confirmation (e.g., "fixture placed")
- Multi-item data collection
- Defect identification
- Compliance audits
- Product placement validation

### Data Output

**Primary:** Internal project reporting
**Secondary:** Client exports (Samsung, LG, etc.) via files or APIs
**Preference:** Retain data internally for "authoritative intelligence"

### Competitive Advantage

**Survey flexibility is a key OpenSky differentiator:**
- Extremely configurable (600-1,200 questions)
- Conditional logic (parent/child, date-based, product-based)
- Grid questions (multi-item efficiency)
- Reusable library (no rebuilding for each project)
- Offline-first (critical for retail environments)

**FSL Risk:** Survey flexibility is a high-risk area for replacement. Must demonstrate equivalent or superior capability.

---

## Data Warehouse & Reporting

### Snowflake Architecture

**ETL Frequency:** 4 times per day (6-hour intervals)

**Data Sources:**
1. **OpenSky operational data:**
   - Time entries
   - Survey responses
   - Parts tickets
   - Expenses
   - Job costing

2. **Client POS data:**
   - Sales transactions
   - Inventory levels
   - Store performance
   - Captured via client API integrations

3. **ADP HR data:**
   - Payroll reports
   - Employee demographics
   - Attrition/tenure

4. **Third-party enrichment data:**
   - Geospatial (store locations, demographics)
   - Retail traffic (Best Buy foot traffic, etc.)
   - Market/competitive intelligence

### Reporting Layers

**Tableau (Client Portals):**
- Company-controlled data models
- Limited user access (licensing costs)
- Clients can pay for raw data access
- Self-service analytics (if purchased)

**PowerBI (Internal Operations):**
- Internal operations dashboards
- Same Snowflake source (4x/day)
- Operational KPIs, project tracking

### Pain Points

**James Dyer (Data Director):**
> "We would love to engage with a platform that is able to extract data not just like in a report... When we last spoke, this is where we were at. Please give us a delta."

**Current Limitations:**
- 4-hour minimum latency (actually 6-hour average with 4x/day)
- Must request full date range, manually derive delta
- No change data capture (CDC)
- No real-time exception reporting
- Overtime visibility after-the-fact (payroll processing lag)

**Use Cases Blocked by Latency:**
- Real-time overtime alerts
- SLA breach warnings
- Project profitability tracking (while project is active)
- Reactive scheduling (rep call-outs, job runs long)

---

## Mobile Architecture

### Offline-First Design

**Critical Requirement:** Must work in stores with poor/no connectivity.

**Local Storage:**
- XML file-based data storage
- Syncs when connectivity returns
- Check-in/check-out with GPS
- Photo capture (stored locally until sync)

### Mobile Features

**Core Capabilities:**
1. **Survey Data Entry:**
   - Navigate tasks/sections
   - Conditional logic (parent/child questions)
   - Grid questions (multi-item)
   - Photo capture
   - Signature capture

2. **Time Entry:**
   - In-store time
   - Drive time
   - Mileage (auto-calculated)
   - Admin time

3. **Expense Reporting:**
   - Photo of receipt
   - Tied to specific visit (job costing)
   - Manager approval workflow

4. **Parts Management:**
   - Create parts ticket from survey
   - View shipment status
   - Installation completion tracking

5. **Calendar/Schedule:**
   - Self-scheduling (drag/drop)
   - Hard-scheduled assignments (pushed by manager)
   - Multi-day projects

6. **Learning Resources:**
   - Access training materials (PDFs, videos)
   - On-the-fly content (not full LMS courses)

### Device Fragmentation Challenge

**Quote (Kari):**
> "A mobile app that works consistently in all different environments across multiple different types of devices. We have that, but man is that hard to keep clean."

**Platforms:**
- iOS (multiple device types, OS versions)
- Android (extreme device fragmentation)

**FSL Advantage:**
- Field Service Mobile built on Salesforce Mobile SDK
- Consistent platform across iOS/Android
- Enterprise-grade testing/QA
- Regular releases with backward compatibility

---

## Scheduling Modes

### Self-Scheduling

**How It Works:**
1. Rep views unscheduled work in mobile app
2. Drags work from unscheduled list to calendar
3. System forces consolidation (multiple visits at same store → same day)
4. **Nightly route optimization runs automatically**
5. Rep sees optimized route next morning

**Used For:**
- Merchandising (routine store visits)
- Audits and compliance checks
- Dedicated brand teams

**Optimization:**
- Only applies to self-scheduled visits
- Consolidates multiple brands/projects at same store
- Minimizes mileage reimbursement

**Pain Point (Jay):**
> "We believe that we attract a lot more talent pool because of the flexibility in terms of scheduling right which is true in most cases but also it kind of hurts us because we're not able to really schedule anything and and track our schedule right it's kind of a double-edged sword."

**CEO Challenge:** Self-scheduling is "people-friendly" but may not be cost-optimal.

### Hard Scheduling

**How It Works:**
1. Manager assigns work to specific rep(s)
2. Schedule pushed to rep's calendar
3. **No automatic optimization** (manual route planning)
4. Used for team projects (5-15 people)

**Used For:**
- Multi-person installations
- Multi-day construction projects
- Team-based work requiring coordination

**Pain Point (Kari):**
> "The manager goes in when and they're looking at the store bucket and they're loading those stores, it doesn't prompt them that they're making a mistake because they should be grouping these together for these people for this reason. We only have it on the front end for self-scheduling."

**Gap:** Hard scheduling has NO route optimization today. This is a major efficiency leak (excess mileage reimbursement, inefficient routes).

### Team Scheduling Complexity

**Challenge:** Coordinating 5-15 person teams for multi-day projects.

**Quote (Kari):**
> "How do you schedule single projects and how do you schedule multiple teams when you need maybe five to 15 people at the store on the same day at the same time and you have to look at availability. You have to see whether they're on other projects. All that stuff has to be taken in effect when you do it."

**Manual Process Today:**
1. Check availability across team members
2. Verify skills/certifications
3. Consider geography (often fly in from multiple regions)
4. Coordinate travel (flights, hotels)
5. Account for conflicts with other projects
6. Push schedule to entire team

**Pain Point:** Manual, time-consuming, error-prone.

---

## Communication Infrastructure

### Email & Messaging Architecture

**SmarterMail (Part-Time Staff):**
- Used for most employees to manage licensing costs
- Avoids full Microsoft E3 licenses for part-time staff
- Part-time staff use intra-ID for portal access + SmarterMail for communication

**ARSCONNECT.COM (Corporate Email):**
- Corporate employees use ARSCONNECT.COM email addresses
- Distinction between corporate and part-time roles is narrowing

**Go Happy (Mass Communication):**
- Tool for bidirectional communication campaigns (email + text)
- Used for mass outreach to field reps

**Salesforce Alternative:**
- **Slack:** Team collaboration, automated notifications
- **Experience Cloud:** Field rep portal (replace intra-ID portal)
- **Marketing Cloud:** Mass communication campaigns (replace Go Happy)
- **Email-to-Case / Email-to-Anything:** Replace SmarterMail for support workflows

---

## Go-Backs Process

**Definition:** Instances where a field representative must return to a store to complete work that was originally missed or could not be finished during the first visit.

**Common Causes:**
- Incomplete kits (missing materials)
- Customer density (store too crowded to complete work)
- Store unavailability (closed unexpectedly, remodeling, etc.)
- Wrong parts shipped
- Rep didn't have required skills/training

**Current Tracking:**
- Call Form Quality Assurance tool flags answers needing follow-up
- Creates revisits for reps to complete
- Deficiency Reporting tracks issues with statuses, resolutions, follow-up dates, shipment tracking

**Cost Impact:**
- Additional mileage reimbursement
- Additional labor hours
- Client frustration
- Reputation damage
- Delayed project completion

---

## Salesforce Mapping

### FSL Component Mapping

| OpenSky Concept | Salesforce Equivalent | Notes |
|---|---|---|
| **Call Form** | Work Type + Custom Project Object | Project container with survey config |
| **Wave** | Custom Wave Object OR Scheduling Policy | Time-bounded execution window |
| **Store/Location** | Service Territory OR Location | Assignment unit |
| **Bucket (Assignment Tool)** | Skills-Based Routing + Location Services | Matching logic: distance, skills, availability |
| **Tactics** | Skills | Tagged to Service Resources |
| **Survey** | Field Service Mobile Custom Forms/Flows | Lightning Web Components + dynamic forms |
| **Tasks (Survey Sections)** | Mobile Flow Screens/Sections | Performance optimization |
| **Question Library** | Reusable Field Metadata / Custom Objects | Question bank |
| **Question Sets** | Shared Field Set Templates | Reusable question groups |
| **Grid Questions** | Repeat Screen Logic OR Line Items | Multi-item data capture |
| **Conditional Logic** | Screen Visibility Rules / Dynamic Forms | Parent/child display logic |
| **Self-Scheduling** | Customer-Managed Scheduling (Appointment Assistant) | Rep drags/drops to calendar |
| **Hard Scheduling** | Dispatcher Console (Manual or Auto-Assign) | Manager pushes schedule |
| **Nightly Route Optimization** | FSL Optimization (Scheduled or Real-Time) | Einstein-driven route optimization |
| **Parts Management** | Asset Management + Product Request | Parts ordering, tracking, installation |
| **Time Entry** | Time Sheets (native FSL) | In-store, drive, admin time |
| **Expense Management** | Expense Reports (custom or AppExchange) | Photo capture, manager approval |
| **Job Costing** | Work Order + Service Appointment (cost tracking) | Project-level profitability |

### Integration Architecture Mapping

| OpenSky Integration | Salesforce Solution | Notes |
|---|---|---|
| **iCIMS → GAMS → ADP → AWS → OpenSky** | MuleSoft → Salesforce (Employee sync) | Real-time vs. batch |
| **OpenSky → Business Central (ERP)** | MuleSoft + ERP Connector | Job costing, invoicing |
| **OpenSky ⟷ LearnUpon LMS** | MuleSoft + myTrailhead OR third-party LMS | Certifications, training |
| **OpenSky ⟷ WMS** | MuleSoft + Warehouse Connector | Parts fulfillment |
| **OpenSky → Agency (Travel)** | MuleSoft + Travel API OR AppExchange | Booking integration |
| **OpenSky → Snowflake (4x/day ETL)** | **MuleSoft CDC + Data Cloud** | Real-time streaming, delta extraction |
| **Snowflake → Tableau** | **Tableau CRM / Embedded Analytics** | Real-time dashboards |
| **OpenSky → Client APIs (Samsung, LG)** | **Platform Events + MuleSoft** | Real-time data push |

### Key Salesforce Differentiators

#### 1. Einstein AI - Intelligent Scheduling

**OpenSky Gap:** No AI-driven scheduling optimization.

**Salesforce Solution:**
- Einstein Optimization (multi-constraint resource matching)
- Real-time route optimization (not just nightly batch)
- Predictive analytics (forecast job duration, rep performance)
- Cross-LOB optimization (break silos)

**Quote (Jay):**
> "Intelligent scheduling number one, right?"

#### 2. Real-Time Data & Exception Handling

**OpenSky Gap:** 4x/day ETL, no CDC, after-the-fact reporting.

**Salesforce Solution:**
- MuleSoft Change Data Capture (real-time delta)
- Platform Events (streaming)
- Proactive alerts (overtime risk, SLA breach)
- Event-driven workflows

**Quote (James):**
> "Please give us a delta."

#### 3. Cross-LOB Workflow Automation

**OpenSky Gap:** Silos by line of business, no cross-LOB workflows.

**Salesforce Solution:**
- Unified platform (FSL + Rex + Sales Cloud + Service Cloud)
- Automated workflows (merch rep spots issue → create service ticket)
- Client 360 view (all projects, all LOBs)

**Quote (Jay):**
> "A merch goes to a target, sees one of the install broken or a display broken. There is not even an incentive for the person to capture that and send it because that's not the line of business."

#### 4. Mobile Platform Consistency

**OpenSky Challenge:** Device fragmentation across iOS/Android.

**Salesforce Solution:**
- Field Service Mobile (Salesforce Mobile SDK)
- Consistent platform, enterprise QA
- Regular releases, backward compatibility
- Offline-first architecture (already proven)

**Quote (Kari):**
> "A mobile app that works consistently in all different environments across multiple different types of devices."

#### 5. Data Cloud vs. Snowflake

**OpenSky Architecture:** Snowflake ETL 4x/day + third-party data enrichment.

**Salesforce Solution:**
- **Data Cloud:** Unified customer/employee/operations data
- Real-time CDC (no 4x/day batch)
- Third-party data connectors (geospatial, POS, traffic)
- Embedded analytics (no separate BI license)

---

## Privacy & Legal Constraints

**Retail Environment Restrictions:**
- **No body cams or glasses recording** (loss prevention policies)
- Cannot capture customer footage (legal constraints)
- Photo capture limited to products/fixtures/compliance (not people)

**FSL Demo Implication:** No wearables or AR demo components for retail use cases.

---

## Next Steps

### Documentation Updates Needed

1. **Update DISCOVERY_QUESTIONS.md:**
   - Add GAMS/iCIMS integration questions
   - Probe Snowflake third-party data sources
   - Survey scale/complexity deep dive
   - Legal constraints validation

2. **Update BUSINESS_MODEL.md:**
   - Add GAMS to integration map
   - Add iCIMS to employee lifecycle flow
   - Update Snowflake architecture (4x/day, third-party data)

3. **Update REVERSE_DEMO_INSIGHTS.md:**
   - Add survey scale details (600-1,200 questions)
   - Add GAMS/iCIMS context
   - Update data warehouse architecture

### Demo Scoping

**Must-Demo Components:**
1. **Survey Flexibility:** Dynamic forms, conditional logic, grid questions (600+ question scale)
2. **Offline Mobile:** Prove FSL works without connectivity
3. **Intelligent Scheduling:** Einstein optimization for team scheduling (5-15 people)
4. **Real-Time Data:** MuleSoft CDC, delta extraction, proactive alerts
5. **Cross-LOB Workflows:** Automated escalation (merch → break-fix)

**Risk Mitigation:**
- Survey flexibility is HIGH RISK (OpenSky extremely configurable)
- Must show equivalent or superior capability
- Consider AppExchange partners (FormAssembly, Survey Force) if FSL native forms insufficient

---

**End of Architecture Documentation**
