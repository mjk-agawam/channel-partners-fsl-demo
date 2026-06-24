# OpenSky Platform - Complete Feature List

**Source:** Provided by Channel Partners team  
**Date:** June 24, 2026  
**Purpose:** Comprehensive feature inventory for FSL gap analysis and demo scoping

---

## Platforms

| Feature | Details |
|---|---|
| **Installed Mobile Android** | Android mobile app |
| **Installed Mobile IOS** | iOS mobile app |

---

## Admin/Ops Features

| Feature | Details |
|---|---|
| **Universal Store List (USL)** | List of locations used by all teams to assign work. IT maintains the list and the field execution teams use it to assign work to field reps |
| **Store Assignments** | List of locations assigned to a field rep for a project/call form |
| **Store assignment to not knowable stores** | Ability for field reps to schedule a visit to a custom location not in the stores list. Entered by the rep at time of scheduling. |
| **Link to survey** | Ability to generate a link for a specific assignments call form to send out to the 3rd party vendor. Rep can click on link to enter the data without login |
| **Position Tree (Hierarchy)** | A tree of who reports to who. Utilizing placeholder positions that can have people associated to them for a specific time periods |
| **Bulk Upload for Store/Assignments** | Tool that allows administrators to reassign store assignments across many projects using the assignment id and the id of the rep to make the change in bulk |
| **Call Form/Project** | Project details and configuration. Linked to the Call form is the survey questions, materials, job creation etc. |
| **Review different Call Form Types** | There are several different call form types in use:<br>• **Store visit** - utilizes the calendar, requires a location and is paid mileage and drive time between locations<br>• **Non Travel Store visit** - utilizes the calendar, requires a location and is NOT paid mileage and drive time between locations, used for precalls or virtual visits to locations<br>• **Hours only** - utilizes the calendar, used to collect time only, no locations, no questions<br>• **Survey** - non calendared, does not use locations, used to collect answers to questions, not paid<br>• **Store Survey** - non calendared, does use locations, used to collect answers to questions, not paid |
| **Work Order Scopes** | Scopes serve as a container for all associated photos and documents as well as issues reported. Scopes are statused and trackable |
| **Expense Management** | Ability for reps to enter their expenses by visit with categories and receipts. Managers can approve or reject the expense. Payroll can review and export for payroll processing |
| **Travel Management** | Travel request process for travel team who books travel. Travel request form which is approved by manager. Travel team has queue for approved travel requests and can book travel and put in details back to manager |
| **Items** | Products/SKUs that can be authorized to locations/retailers. Items are associated to item level questions that allow for the same question to be asked against multiple items. For example: Is this product on display? Then this can be asked against 10 separate SKUs |
| **Waves** | Waves represent date ranged execution windows for a select list of locations. It sets duration of work, allowed dates, allowed days of the week. |
| **Materials** | Shippable supplies needed by a field user to complete a particular product. Associated to individual locations for a specific wave of work. Includes shipping tracking. Prompts the rep to indicate whether they have the material with them upon data entry. |
| **Job Costing (Billing)** | Billing is the association of job codes for use in the integration into our financial systems |
| **Course Billing** | Association of job codes for specific rep types on courses completed by field reps |
| **Call Form Invoicing/State Tax** | Ability for client service to upload how much is being billed per visit, if the visit is billable. Exports to a dashboard for determining taxes to pay for visits invoiced. Includes a module to tag work as invoiced. |
| **Messaging/Notifications** | Communications sent to users. User generated, system generated. One way communication currently |
| **Prioritization of Visits by Call Form or Client** | Admin module allowing teams to prioritize work by call form/wave leading the field reps to schedule the most important work first. |
| **Resources/Documents Management** | Resources include uploaded documents, URL's of reference materials and videos. Can be associated to call forms for display during call form entry. |
| **Store Management (USL)** | USL = Universal Store List - a centralized database of locations available to have work done in. Managed and maintained by the IT group currently |
| **People Management** | Ability to add people to a field team, including setting where in the hierarchy they exist and what system role they have |
| **Uploading Assignments/Schedules** | Ability to upload a spreadsheet of location assignments for waves of execution with who they want assigned. In addition the ability to upload a sheet of location assignments with specific dates and times to be placed on the reps schedule |
| **Multi Rep Scheduling** | Ability to upload locations that need multiple field reps to perform the work at the same time. For example we need 2 reps to work at the same date/time because a display is too heavy for one rep to perform the work. At it's simplest allows for a schedule upload with the reps associated. At it's best the system find the reps and find the ideal scheduling for those reps |
| **Manager Dashboard (Field Vision)** | Dashboard interface enabling managers to view the work field reps under these managers are assigned to and the progress with their work. |
| **Teams** | Allow for multi-tenant use by separating field execution teams so each team can manage their field execution separately. Management of call forms, people, items, etc. are separated by the team barrier |
| **Call Form Quality Assurance/Call Out because of errors/problems with visit** | Client service tool to flag particular answers to questions as needing follow up, creates revisits for the reps to complete |
| **Call Form Edit/Bulk Edit of entered call forms** | Tool that allows client service to update answers to questions across multiple visits and save updates at once instead of editing each visit individually |
| **Tracking of Material Shipments for Projects** | Upload of materials (as described above) |

---

## Calendar Features

| Feature | Details |
|---|---|
| **Calendar** | Mobile calendar to view scheduled work |
| **Syndication** | Prompting user that other visits to the same store are available on the same day/time |
| **Consolidation** | Prompting user that all visits should be done on one of the days chosen not multiple |
| **Scheduling Rules** | Rule or configuration that set how reps can schedule. Which days which times etc. per project |

---

## Call Form/Survey Question Answer Types

| Feature | Details |
|---|---|
| **Questions** | Administration of questions asked during a survey. Includes authorization of which questions appear in locations/retailers |
| **Tasks** | Grouping of questions into logical groups based on work to be done in store |
| **Question Sets** | Group of tasks and questions that can be associated to multiple call forms. |
| **Question Library** | List of questions added to the system previously that can be added to new call forms. The original Question ID is preserved to help identify this question across call forms and projects. |
| **Copy** | Ability to copy a call form with all of its configuration (Questions, Store Assignments) |
| **Show independent levels of Question and Location and Item authorization** | Authorizations are defined as setting visibility of a question based on individual location or retailer |
| **Comment** | Long text - 2-3000 characters |
| **Date** | Date like 3/14/2023 |
| **Single Select** | Drop down where only a single value can be selected |
| **Grid** | List of questions asked for a defined number of products (items). Sometimes displayed with questions across the horizontal axis and product on the vertical axis like a grid. |
| **Header/Instructions** | Placeholder text to start a new section on the call form or text instructions and an image. Used to provide direction or information about the task or question. |
| **Image** | Image question to either upload an image or take a live picture with a device camera |
| **Multi-select** | Drop down allowing the user to select more than option |
| **Numeric** | Question to collect numbers with validation to ask for specific numeric types like whole numbers or ranges. |
| **Text** | Question to collect short text, 2-300 characters |
| **Time** | Time entry question |
| **Yes/No** | Drop down with Yes and No options |
| **Item Counts** | Item counting question type |
| **Signature** | Option to capture a signature at the end of the call form |
| **Barcode** | Question enabling the user to scan a barcode with their device camera and put the value into a form field on the call form |
| **Parent and Child nesting levels - how many levels** | Call Form with the ability to setup conditionality or skip logic between questions. This question is answered with this choice and as a result this other question is asked. Currently OS has unlimited skip logic between questions. |
| **Ability to enter default answers to questions** | Default answer shows and reps only have to change it if the answers are different for their current entry or location. |
| **Ability to bring last entries answers forward to current entry** | Option that allows a call form upon entry to have all answer prepopulated by the answers from the previous visit to this location for this call form |
| **Survey (call form not scheduled)** | • **Survey** - non calendared, does not use locations, used to collect answers to questions, not paid<br>• **Store Survey** - non calendared, does use locations, used to collect answers to questions, not paid |

---

## Contact Management

| Feature | Details |
|---|---|
| **Contact Management - SRM Contact Questions** | Questions that can be asked per contact during a visit. Current answers for each contact is brought back on each visit. |
| **Contact Management** | Ability to enter contacts by location visited, including detailed contact card. After creating a contact can that contact be connected through meta data to a store location, a reps position in the system, the retail chains position hierarchy |
| **Bulk Upload for contacts** | Ability to upload a list of contacts and associate to stores or positions |
| **Contact associations - position, location, hierarchy** | Ability to associate a contact to a store, position, other contact |

---

## Field Rep Features

| Feature | Details |
|---|---|
| **Calendar** | A mobile calendar to view scheduled work and create manual appointments based on assigned locations. |
| **Scheduling** | A calendar screen used to schedule work. Could be a part of the calendar. Includes a list of the work assigned to the rep that they can add to the calendar to set the date and time it will be done. |
| **Call Form/Survey entry flow** | Workflow to check into a store, complete tasks/questions assigned for a location, check out of a store and verify the time for a location |
| **Profile** | Field Rep profile showing a reps attributes, tactics they have performed, hardware they possess. Retailer IDs etc. |
| **GPS/Check in/out** | Field rep needs to click a button when starting a visit to send the GPS coordinates |
| **Contacts** | Field rep access on a mobile device to contacts they have created. This includes all meta data and the answering of contact questions during store visits |
| **Rep Dashboard** | Mobile dashboard providing field reps a summary of work to be completed with links to start the work broken down by type of work. Access and links to messages from their team, their profile, stores assigned to them etc. |
| **Last visit preview** | Access during the call form entry flow to the previous entered call form questions for a specific store and call form. Used to familiarize them on what happened during the previous visit. |
| **Access to files (files and video) within call form flow** | Resource necessary, useful for a call form project accessible to a field rep while answering call form questions during a visit |
| **Partial save or pause a call form entry** | Ability to pause call form entry and save the call form questions already answered to take care of something else and then return to the call form entry where they left off |
| **Messaging/Notifications** | Access to read/respond to two way messages from the team or manager in the app including notifications sent for the whole team |
| **Offline/Sync** | Ability to work offline during a visit and sync calendar/call form/messages when a connection is available. Retail locations can have very spotty coverage at time deep into the large box stores. |
| **Availability** | Ability for a rep to designate what time they have available per day to work. This is used by the team to schedule reps according to their set availability when projects are schedule for them. This is especially useful for 2 or 3 person projects where a team needs to go in to do work together. |
| **High number of visits per day per person (over 25) map and optimize** | Field reps may do greater than 25 visits in a day during busy seasons. For optimization engines this has caused issues with our partners optimization routines |
| **Prioritization of visits for field reps** | Ability for a rep to have work presented to them prioritized list to schedule |
| **Training validation before visits** | Field reps are not able to schedule or begin work until they have completed their required work in the LMS system |
| **Material Shipping Tracking** | Want to see tracking number, link to tracking, date of delivery, status, was it delivered to the rep assigned |
| **Entering/Editing payroll hours, mileage, drive time** | Ability for field reps on their mobile app to view and edit all of their payroll related time, mileage, drive time |
| **Travel Estimator** | Break Fix module allowing Field Managers to create an itinerary for travel for a rep and an approval process. |
| **Rep can run an optimize route on their appointments** | Enable reps to turn on or run themselves an optimization for the appointments on their calendar to reduce drive time and mileage and improve efficiency |
| **Retailer Inventory of products to sell based on program** | Allowing data to be available for the user on their mobile devices about products on their call form the inventory of those product available to sell for the retailer the visit is in |
| **Call Form setup for demo with 800 questions with a minimum of 60 image questions** | Currently our team have call forms with 800 questions which are conditionally shown to the field user based on how they answer questions. This requirement is to make sure the system can support these large call forms with a good experience for the user |
| **Resources/Links** | Ability for reps to view resources (files, links, images) on the app and in the call form entry flow to reference for a project or to answer a question from the store employee |
| **Work List** | List of work assigned/available for the field rep to schedule or start entering |
| **Mobile UI** | New Work order view that is responsive and allows field reps to access the work orders from a mobile browser without needed an app. The mobile UI is designed with task completion in mind and was made to enable a rep an easy to use interaction with upwards of hundreds of tasks in a single work order which is common among construction remodel projects. The mobile UI can be used for all project types and ultimately is replacing the need for a mobile app. |

---

## Parts/Display Maintenance

| Feature | Details |
|---|---|
| **Parts Management** | Module to add/edit parts from all CP partners. Users can add manually or upload a list with the required attributes |
| **Ticket System & Queue** | Ticketing screen enabling user to do the following:<br>• Open a new ticket<br>• Associate multiple issues with a single ticket<br>• Issues can be connected to retail displays and parts for those displays<br>• Screen displays history of tickets/orders to a particular location<br>Tickets/orders can also be uploaded if teams are not getting them by calling in the orders |
| **Ticket Issue/Order Approval/Assignment** | Screen after the Tickets where managers for Display/Parts programs do the following:<br>• Assign field reps to troubleshoot or place parts at a location<br>• Update or change any information originally on the ticket/order<br>• Approve the order to move to the next step<br>The next step being approval by the managers of the field reps. |
| **Order Shipping** | Screen to upload shipping details manually where the fulfillment partner is not a CP warehouse with is integrated. Uploading the information provides users ship dates and tracking information which is visible in their app. If the parts are shipped from a CP Warehouse the Warehouse Management System (WMS) is integrated with the system to provide shipping information after the shipments are completed. |
| **Parts/Issue Resolution - OSMobile integration** | Task in the field reps call form flow enabling them to provide updates/feedback about all Part Issues/Orders for the location they are currently working in. User can see:<br>• Parts on order for location<br>• Active part orders the user should provide status and completion photos<br>• Issues where troubleshooting is needed<br>User can also track part order packages with UPS/FedEx details |

---

## Shipping Management

| Feature | Details |
|---|---|
| **Shipping Module** | Module to enable users to create shipping requests that go into a queue for the team/warehouse to manage. Requests go through statuses until they are approved by the warehouse and flow (through an integration) into the Warehouse Management System (WMS) for processing |
| **One off shipment (Simple)** | Shipment request type allowing users to configure a shipment to one person with 1 to many products. |
| **Group/Bulk Shipment (Complex)** | Shipment for many people for multiple products for a project. Can be linked back to a project/call form and job costing information. |
| **Warehouse Queue and Management** | Warehouse request queue where warehouse can edit/move requests into the WMS for processing |
| **Integration with WMS** | The integration allows shipping requests to flow into our WMS and completed shipment details to flow back into our systems to populate reports and updates management and field user screens. |

---

## Other Features

| Feature | Details |
|---|---|
| **Localization** | Ability for the system to support other languages and localization (time zone, etc). |
| **Routing Optimization** | Ability for teams to load in store visits and the system supply routing for the field reps assigned to minimize mileage and drive time. |
| **Signature capture** | Capturing signatures in a call form to verify at the store level that a task or call form is completed correctly |
| **Territory Mapping** | Ability for Account Teams to draw territories on a map for a rep, supervisor and use that geopoint data to assign stores for projects and do reporting |
| **Field Rep Availability** | Ability to use Reps Availability for Scheduling reps to a date and time on a project |
| **Single Sign On** | Users can login using their Active Directory single sign instead of username and password |
| **Black out days** | Ability to set by chain what days reps cannot schedule for. |

---

## Payroll Types

| Feature | Details |
|---|---|
| **In Store Hours** | Time captured for in store visit time, often based on geo-check in and geo-check out for the visit |
| **Admin Hours** | Additional administrative time that the rep needed for the visit |
| **Drive Time Hours** | Time for travel to and between locations during their visit day |
| **Mileage** | Mileage for travel to and between locations during their visit day |
| **Course Hours** | Completed, required course hours for payment to the rep |
| **Additional Pay $** | Extra pay uploaded for reps, includes bonuses, commissions - hours and dollar amounts to Jobs |
| **Travel Hours** | Call forms specifically for travel - Airline, Rental Car, Hotel |
| **Meal Break Time** | Capture of mandated meal breaks in system after working state defined minimum times |

---

## Payroll Features

| Feature | Details |
|---|---|
| **Mileage Federal Rate** | Ability to set mileage pay rate to federal rate and adjust as it changes |
| **Pay Rate Type** | Three types: Default, Project Pay, Job Rate |
| **Door Fee** | Bonus type additional payroll info for accepting an assignment |
| **Per Diem** | 0-3 number of days for per diem tied to a work assignment |
| **End of Day Questionnaire** | Questionnaire asking if the field rep was compensated for all of their pay for the day |
| **Mileage State Rates (Locality)** | Ability to set mileage pay rate to state minimums and adjust as it changes |
| **Mileage Travel Commute (First and Last leg)** | Set thresholds for payment of mileage and drive time for commuting to the first location of the day and from the last location of the day |
| **Drive time rates based on Locality (State, County and Postal Code)** | Ability to calculate minimum wage for drive time based on travel to particular localities. For example if a rep travels from Oakland to San Francisco they would be paid at the San Francisco rate because that rate is higher than Oakland |
| **Drive Time Pay Rate Rules** | Multiple rules apply here some of which have been explained above, in addition we have different pay rates based on type of rep performing the work |
| **Drive Time Travel Segment (Add/Calculate mileage/drive time)** | Manually added additional location to track mileage/drive time during the day |
| **Drive Time Smoothing Algorithm** | For visits that are syndicated (multiple projects in the same location done on the same day) mileage and drive time between locations are only applied to one of the projects performed. From a billing perspective we want to distribute mileage/drive time across those visits so they can be billed with equal amounts of the cost. |
| **Payroll Verification** | Mechanism for managers to verify payroll hours before posting to Payroll |
| **Payroll Management** | Regular and expense payroll approval by Managers. Approved payroll then becomes available to the HR/Payroll Department to run the "payroll processing" action, that becomes the file uploaded to ADP. |

---

## Integrations

| Feature | Details |
|---|---|
| **LearnUpon LMS** | Two way integration between OpenSky and LMS for courses course completions |
| **Rain payday advancement** | Integration with RAIN payday advance for reps to get paid prior to pay day |
| **Best Buy Vendor ID/Lilo/Training data download** | Custom integration to automatically pull down Best Buy IDs, Training data and Lilo data for Data Warehouse reporting |
| **Target** | Target requires all vendors to send over schedule information and check in out completions for visits |
| **Snowflake (Data Warehouse)** | All OS data is moved to the Snowflake data warehouse 4 times daily. This data is used for Analytics reporting and integrations support. |
| **GAMS** | Employees and essential payroll information is pushed from Snowflake to GAMS. A payroll detail report is exported from OS and uploaded to GAMS every week for weekly payroll. |
| **WMS - Warehouse Management System(s)** | OS Integration with a WMS system for all shipping. WMS is then integrated with the shipping providers for rates and service. The integration provides inventory on all parts/products in the warehouse to OS users creating shipments |
| **ADP (People and People attributes and status)** | OS also gets all new employees from an integration between ADP->OS |
| **Partner Call Form Data flow into system automatically (IC Import)** | The Break Fix Merchandising division of Channel Partners often reaches out to 3rd party field marketing companies to partner on projects where Channel Partners does not have market coverage. This feature refers to any capability for partner data to flow into a Workforce Management solution to get call form question answer/completion data from these partners for combined reporting/analytics. Or is there way for 3rd party field reps to come into the system as guests to complete work |
| **SAMSUNG SRMS** | Integration into Samsung's Work Order Management System called SRMS which is used to track all retail and maintenance work. |
| **Rapid Displays Inventory Management System** | Rapid Provided Parts fulfillment for Samsung in all Best Buy Stores as well as most other retailers. |

---

## Reporting

| Feature | Details |
|---|---|
| **Tableau Reporting** | Tableau cloud instance where teams and clients can login and see reports custom for their programs. Data sourced from Snowflake and curated by Data Services team. |
| **SSRS and Offline Reports** | Custom Reports built using SSRS and served up in OS for users reporting self service |
| **Image Gallery** | Ability to filter/view/export/provide access to images collected on call forms |
| **Payroll Reporting** | Reporting used to find issues and export data regarding payroll (hours, mileage, drive time, etc.) |
| **GeoTracking Reporting/Dashboard** | Reporting or dashboarding providing feedback about the location of reps and whether check in/out was done correctly on call forms |
| **Question Alerts** | User created alerts linked to call form questions messaging a person or group to something that needs to be followed up |
| **All Column Detail Report** | Call Form Question Answer Data Export |
| **Target PML Email** | Custom email send to Target internal store staff after each execution visit to one of their stores |
| **Deficiency Reporting** | Itemized issue tracking by scope of work. Issues that are reported by the reps are trackable items with their own statuses and data fields including any resolutions, follow-up, go back dates and shipment tracking info associated with that issue. |

---

## Human Resources

| Feature | Details |
|---|---|
| **Human Resource Admin (HRM)** | Screen to display a person profile for HR purposes which combines both ADP and OpenSky profile data. Ex OpenSky - last day worked and how many visits completed. ADP - are you eligible for rehire and are you MVR eligible. |

---

## Finance

| Feature | Details |
|---|---|
| **Job and Client creation** | Account teams able to create clients with financial attributes and generate job numbers for new projects |

---

## Finance/Operations

| Feature | Details |
|---|---|
| **Billing/Invoicing** | Ability for Client service managers to pull detailed billing reporting by project and job including all of the costs for the project. |

---

**End of Feature List**
