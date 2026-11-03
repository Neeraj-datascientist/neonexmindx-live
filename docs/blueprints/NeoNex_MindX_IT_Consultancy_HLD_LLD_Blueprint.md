NEONEX MINDX


# IT CONSULTANCY & TECHNOLOGY SERVICES

Client Experience • Consulting • Engineering • AI/ML • Project Delivery

DOMAIN: [YOUR PURCHASED IT CONSULTANCY DOMAIN]  |  Dedicated Technology Vertical

MASTER HIGH-LEVEL DESIGN (HLD) + LOW-LEVEL DESIGN (LLD)

Prepared as an implementation blueprint • Version 1.0 • 02 November 2026


# Document control & purpose


# 1. Executive summary

The IT Consultancy platform should operate as a professional digital front door and client delivery environment. The public website explains who NeoNex MindX is, what it provides, its specialities, delivery approach, differentiators, evidence of capability and reasons to engage. The private client portal begins after qualification/onboarding and gives each client organization a secure workspace for contracts, SOPs, projects, assigned team profiles, tasks, milestones, deliverables, live updates, meetings, invoices, payments and support.

The platform is designed around a professional-services lifecycle: attract → qualify → discover → propose → contract → onboard → plan → deliver → accept → invoice → support → renew.


## 1.1 Business objectives

Present NeoNex MindX as a credible, specialist IT consultancy and technology solutions partner.

Explain service offerings, technical specialities, business outcomes, differentiators and engagement models.

Convert website visitors into qualified enquiries and booked discovery consultations.

Provide controlled, transparent client onboarding and project visibility.

Show approved consultant profiles and relevant experience without exposing internal HR data.

Manage agreements, SOPs, requirements, projects, tasks, deliverables, approvals and change requests.

Connect delivery progress with timesheets, invoices, payment status, support and client satisfaction.

Build repeatable operations for multiple clients and concurrent projects.


# 2. Domain and experience architecture

The purchased technology domain name was not supplied in this request. Replace [TECH-DOMAIN] with the exact registered domain before DNS, certificates and callback configuration.


# 3. Public website – professional information architecture


# 4. Public website conversion and trust design

Use a precise headline describing the business value, not generic claims such as 'world-class' without evidence.

Present 3–6 clear service pillars and connect each to business problems and deliverables.

Show a structured process: discovery → solution design → build → validate → deploy → support.

Use case studies only where the work is real and publication is authorized; anonymize confidential client work.

Show team profiles, certifications and partnerships only after verification and approval.

Use testimonials with client permission, attribution rules and a review moderation process.

Provide enquiry forms that capture company, role, business challenge, service interest, timeline and consent.

Offer a discovery-call calendar with timezone, availability, confirmation and rescheduling.

Provide clear privacy and data-use notices at forms and booking points.

Track conversion analytics with consent and avoid collecting unnecessary personal data.


# 5. Service catalogue – proposed consultancy capability map

These are proposed service categories. Publish only offerings that NeoNex MindX is ready and qualified to deliver. Define scope, exclusions, assumptions, dependencies and acceptance criteria for each service.


# 6. Client acquisition and onboarding lifecycle

Figure 1. Lead-to-client-to-renewal lifecycle.


# 7. Client portal – complete client experience

Each client organization receives a secure tenant/workspace. Within the organization, users are invited with roles such as client administrator, project sponsor, project manager, finance contact and read-only stakeholder. Users see only projects and records explicitly shared with their organization and role.


# 8. Client portal dashboard – recommended layout

Top summary: active projects, overall health, pending approvals, unpaid invoices and next meeting.

Project cards: status, progress, next milestone, owner, last update and risk indicator.

Activity timeline: latest deliverables, decisions, task updates, document changes and announcements.

Action centre: client approvals, information requests, overdue actions and signature requests.

Calendar panel: next meeting, upcoming milestones and review sessions.

Finance panel: invoice number, amount, due date and payment state; hide internal cost/margin.

Support panel: open tickets, priority, SLA status and escalation contact.


# 9. Consultant showcase and resource management

Maintain a complete internal employee/consultant record in the HR/resource system.

Create a separately approved public/client profile containing selected name, professional summary, skills, relevant experience, certifications and portfolio.

Support client-specific shortlists and interview requests with permission and availability checks.

Allocate resources by skill, capacity, timezone, project phase and commercial agreement.

Track allocation percentage, planned capacity, actual time, leave/availability and utilization.

Do not expose personal phone numbers, private HR documents, salary or internal performance data to clients.


# 10. Project delivery and PSA capabilities


# 11. Task taxonomy – defect vs feature vs change


# 12. Agreements, SOPs and document governance

Support NDA, MSA, SOW, SLA, DPA, change orders, purchase orders and handover documents as applicable.

Use a controlled template library with version, owner, legal review status and effective date.

Track draft, internal review, approved, sent, partially signed, executed, expired and terminated states.

Use an e-signature provider with signer authentication, audit evidence and completed-document retention.

Store SOPs with owner, version, approval, effective date, review date and acknowledgement requirement.

Separate internal SOPs from client-visible SOPs; publish only approved copies.

Maintain immutable or tamper-evident document activity records and controlled access grants.

Do not treat a file upload as proof that a contract is executed.


# 13. Calendar, meetings and client scheduling

Client self-service booking for discovery calls and agreed meeting types.

Internal availability, working hours, holidays, timezones, buffers and conflict detection.

Kickoff, workshops, sprint planning, demos, status reviews and steering committee meetings.

Calendar invitations, attendee responses, reschedule/cancel workflows and video meeting links.

Meeting agenda, notes/minutes, decisions, risks and action items linked to the project.

Reminder rules configurable by event type and participant preference.

Integration with Google Calendar or Microsoft 365 only after account and permission decisions.


# 14. Billing, invoices, payment gateway and reviews

Support fixed-fee, milestone, time-and-materials, retainer and recurring support billing models.

Generate quote/proposal, pro-forma where appropriate, tax invoice, credit note and receipt based on approved finance policy.

Use payment provider adapters so the business can support more than one provider without coupling project logic to a provider.

Create payment orders server-side, verify provider webhooks, apply idempotency and reconcile settlements.

Show client-facing payment status and receipts; restrict internal costs, margins and bank reconciliation details.

Support payment links or checkout on the public site only for clearly defined products/services with approved terms; project invoices should normally be paid through the authenticated client portal.

Publish client reviews/testimonials on the public website only after verification and explicit publication consent.

Keep private service feedback and support complaints separate from public testimonials.


# 15. High-level technical architecture

Figure 2. IT consultancy platform high-level architecture.


# 16. Service catalogue and data ownership


# 17. Client data model (logical)


# 18. API and event contracts


# 19. Client tenant security and access model


# 20. Security, privacy and operational controls

Use OIDC/OAuth2, MFA for privileged users and strong client invitation/activation workflows.

Derive tenant context from validated identity membership; never trust a client_id sent by the browser alone.

Enforce object-level authorization on every read/write endpoint and download operation.

Use private object storage, tenant/project-scoped keys, malware scanning and short-lived download URLs.

Separate client-visible activity from internal notes, internal estimates and confidential delivery discussion.

Use least-privilege service identities, secrets management, encryption and key rotation.

Use audit trails for login, access grants, document access, approvals, agreement execution, invoice and payment changes.

Apply webhook signature validation, idempotency, replay protection and reconciliation for payments.

Use backups, restore testing, incident response, vulnerability management and dependency scanning.

Define data retention, export, deletion and offboarding procedures in client agreements and policies.

For AI features, prevent cross-tenant retrieval and require explicit authorization for tools that change client records.


# 21. Invoicing and payment design

Maintain a legal-entity and tax-configuration layer; invoice numbering and tax treatment must match the actual registered entity and applicable law.

Support fixed price, milestone, time-and-materials, retainer and recurring support billing.

Create invoice drafts from approved SOW milestones or approved billable timesheets; require authorized review before issue.

Track invoice issued, viewed, partially paid, paid, overdue, disputed, credited and cancelled states as applicable.

Use payment provider adapters to avoid coupling the invoice service to a single provider.

The provider webhook is not trusted until signature, amount, currency, order reference and idempotency are verified.

Reconcile provider settlement and fees against bank/finance records; keep refund and credit-note trails.

Expose only client-appropriate payment status and receipts in the portal.


# 22. Public reviews and client feedback

Trigger feedback requests after agreed milestones, project closure or support interactions.

Separate private CSAT/complaint records from public testimonials.

Record explicit permission for name, company, logo, quotation, rating and case-study publication.

Provide internal moderation, authenticity checks, response workflow and correction/removal process.

Do not fabricate reviews, customer logos, case studies, certifications or performance metrics.

Display only approved, attributable and current material on the official website.


# 23. Analytics and management dashboards


# 24. Recommended technology stack


# 25. Delivery roadmap


# 26. Non-functional requirements and acceptance criteria


# 27. Decisions required before implementation

Insert the exact purchased IT consultancy domain and confirm registrar/DNS control.

Confirm legal company name, registered entity, GST/tax configuration and invoice issuer.

Approve the service catalogue and distinguish currently deliverable services from future capabilities.

Define engagement models, pricing rules, proposal templates and approval limits.

Choose payment providers and verify merchant eligibility, settlement, fees and refund operations.

Select e-signature provider and agreement templates with legal review.

Define client visibility rules for consultant profiles, tasks, timesheets, progress and internal notes.

Set client data retention, offboarding, export and deletion policies.

Define expected client count, project concurrency, data residency and uptime targets.

Confirm whether client communication should include portal chat, email integration and optional WhatsApp.


# 28. Glossary



| STRATEGY & EXPERIENCE | PLATFORM & SERVICES | SECURITY & OPERATIONS |
| --- | --- | --- |




| Item | Definition |
| --- | --- |
| Document | NeoNex MindX IT Consultancy – Master HLD & LLD |
| Purpose | Define the official consultancy website, lead-to-client journey, secure client portal, delivery operations, commercial workflows and platform architecture. |
| Business boundary | IT consultancy / technology services only. EdTech has a separate domain, public website, operations and data boundary. |
| Status | Proposed architecture for validation and implementation planning. |
| Version | 1.0 – 02 November 2026 |
| Audience | Founder, sales, solution architects, delivery managers, developers, QA, finance, support and clients where appropriate. |




| Positioning principle The IT consultancy domain is the official public identity of NeoNex MindX as a technology and consulting company. Its public website builds credibility and generates enquiries. A separate secure client portal under the same domain family handles onboarding, agreements, SOPs, project dashboards, progress, communication, invoices, payments, support and reviews. EdTech remains a separate business vertical. |
| --- |




| Proposed host | Purpose | Audience |
| --- | --- | --- |
| [TECH-DOMAIN] | Official IT consultancy website | Public visitors, prospects, partners and clients |
| clients.[TECH-DOMAIN] | Secure client portal | Client contacts and authorized client administrators |
| workspace.[TECH-DOMAIN] | Internal delivery workspace | Employees, consultants, project managers and management |
| admin.[TECH-DOMAIN] | Administration and operations | Authorized platform and business administrators |
| api.[TECH-DOMAIN] | Versioned API gateway | Frontend applications and approved integrations |
| auth.[TECH-DOMAIN] | Identity entry point | Authorized employees and client users |




| Website objective The public site must answer five questions quickly: Who are you? What business problems do you solve? What are your specialities? Why should a client trust you? What is the next step to engage? |
| --- |




| Website section | Content and functionality |
| --- | --- |
| Home | Clear positioning, primary specialities, client problem statements, proof points, featured work and consultation CTA. |
| About NeoNex MindX | Company overview, mission, values, leadership, operating model and delivery philosophy. |
| Services | Service catalogue with business outcomes, scope, deliverables, engagement models and FAQs. |
| AI & Data Solutions | AI/ML, generative AI, RAG, document intelligence, automation, analytics and applied AI solutions. |
| Software Engineering | Web applications, backend systems, API platforms, integrations, portals and modernization. |
| Consulting & Advisory | Technology strategy, architecture reviews, process optimization, technical discovery and implementation planning. |
| Industries / Use Cases | Only industries and use cases supported by actual experience or clearly labelled capability areas. |
| Expertise & Technology | Technical capabilities, frameworks, platforms, delivery practices and security approach. |
| Case Studies / Portfolio | Problem, context, approach, solution, measurable outcome and client permission status. |
| Why Choose Us | Specialization, transparent delivery, accountable ownership, fit-for-purpose architecture and communication. |
| Team / Expertise | Approved leadership and consultant profiles; no unapproved personal data. |
| Testimonials & Reviews | Verified client feedback, permission to publish, source/date and moderation. |
| Insights / Resources | Technical articles, explainers, whitepapers, guides and announcements. |
| Engagement Process | Discovery, proposal, agreement, onboarding, delivery, acceptance and support. |
| Contact / Consultation | Enquiry form, service selection, consultation booking, contact options and consent. |
| Client Login | Secure route to the client portal. |
| Policies | Privacy, terms, cookies, accessibility, grievance/contact and applicable legal disclosures. |




| Service pillar | Potential service offerings | Typical deliverables |
| --- | --- | --- |
| AI / ML Engineering | Predictive ML, NLP, computer vision, model deployment, AI integration | Solution architecture, model/service, API, monitoring and documentation |
| Generative AI & RAG | Enterprise knowledge assistants, document intelligence, RAG, agent workflows | Knowledge pipeline, retrieval layer, evaluation, guardrails and application |
| Data & Analytics | Data analysis, BI dashboards, KPI design, data integration and reporting | Data model, dashboards, KPI definitions and operating documentation |
| Software Engineering | Web apps, portals, backend services, API development and modernization | Requirements, UX, code, tests, deployment and handover |
| Automation & Integration | Business workflow automation, third-party APIs, system integration | Workflow maps, connectors, exception handling and audit trail |
| Cloud & DevOps | Deployment architecture, CI/CD, observability and reliability improvements | Infrastructure design, pipelines, monitoring and runbooks |
| Technology Consulting | Discovery, architecture assessment, technical roadmap and feasibility | Assessment report, architecture, risk register and roadmap |
| Managed Support | Maintenance, incident response, upgrades and service support | SLA, support process, incident records and service reports |




| Client portal area | Capabilities |
| --- | --- |
| Overview dashboard | Project health, milestones, open actions, recent updates, upcoming meetings, risks and pending approvals. |
| Organization profile | Company details, authorized contacts, billing contacts, timezone, notification preferences and onboarding status. |
| Agreements | NDA, MSA, SOW, SLA, DPA, change orders, versions, signature status, effective dates and renewal alerts. |
| SOP & knowledge library | Approved SOPs, project runbooks, onboarding guides, release notes, version history and acknowledgement. |
| Team & profiles | Assigned team, approved bios, roles, skills, responsibilities, availability windows and escalation contacts. |
| Projects | Project scope, status, timeline, milestones, dependencies, risks and deliverables. |
| Tasks & action items | Task owner, status, priority, due date, acceptance criteria, comments and client-visible updates. |
| Live progress | Activity feed, sprint progress, milestone completion, release updates, blockers and decisions. |
| Deliverables | Documents, reports, demos, release packages, review status, acceptance and download permissions. |
| Meetings & calendar | Discovery, kickoff, workshops, demos, recurring reviews, minutes and action items. |
| Communication | Project-specific conversations, announcements, requests and support handoff. |
| Invoices & payments | Invoice list, due dates, payment instructions, payment status, receipts and statements. |
| Support & SLA | Ticket submission, severity, response target, status, resolution notes and escalation. |
| Feedback & reviews | Project feedback, service review, CSAT/NPS where used, testimonial approval and complaint handling. |
| Audit timeline | Client-visible history of key milestones, approvals, document versions and status changes. |




| Capability | Detailed requirements |
| --- | --- |
| Engagement management | Client, agreement, service scope, commercial model, start/end, sponsor, delivery owner and status. |
| Project planning | Objectives, scope, exclusions, assumptions, architecture, work breakdown, milestones and dependencies. |
| Task management | Type, owner, reviewer, priority, estimate, due date, acceptance criteria, status and history. |
| Sprint / delivery | Backlog, sprint planning, work in progress, review, demo, release and retrospective. |
| Requirements | Business requirements, technical specifications, traceability, acceptance criteria and sign-off. |
| Change management | Change request, reason, scope impact, effort/cost/timeline impact, approval and versioned SOW. |
| Quality management | Test plan, test cases, defects, severity, regression, QA approval and client acceptance. |
| Release management | Release plan, environments, deployment approvals, release notes, rollback and handover. |
| Timesheets | Daily/weekly time, project/task reference, billable flag, approval and invoice linkage. |
| Risk & issue management | Risk register, impact, probability, mitigation, owner, escalation and resolution. |
| Client reporting | Weekly/monthly status, milestone progress, blockers, decisions, effort and next steps. |




| Type | Definition | Required control |
| --- | --- | --- |
| BUG | Existing agreed functionality does not behave as specified. | Reproduce, severity, defect owner, fix, regression test and verification. |
| FEATURE | New capability not in agreed baseline scope. | Requirements, priority, estimate and scope approval. |
| CHANGE REQUEST | Modification to approved requirements, deliverables or commercial baseline. | Impact analysis and written client approval before execution. |
| INCIDENT | Unplanned interruption or degradation of a live service. | Severity, response target, incident commander, communication and post-incident review. |
| SERVICE REQUEST | Routine request within an agreed service catalogue. | Authorization, workflow and SLA. |
| TECHNICAL DEBT | Internal engineering improvement that reduces future risk or maintenance cost. | Engineering prioritization and documented rationale. |




| Service boundary | Owns | Key integrations |
| --- | --- | --- |
| Public website/CMS | Pages, service catalogue, case studies, testimonials, SEO metadata | CRM, analytics, review publishing |
| Sales CRM | Leads, contacts, opportunities, discovery notes and pipeline | Website forms, calendar, proposal |
| Client onboarding | Organization profile, contacts, verification, access requests and onboarding checklist | Identity, agreements, documents |
| Agreement & document | Contracts, SOW, SOP, versions, signatures and access grants | E-sign provider, project, finance |
| Project/PSA | Engagements, projects, tasks, milestones, dependencies and delivery status | Resource, calendar, client portal |
| Resource management | Consultant profiles, skills, capacity, assignments and availability | HR, project planning, timesheets |
| Requirements & change | Requirements, acceptance criteria, change requests and approvals | Project, contract, task |
| QA & release | Test cases, defects, releases, deployment evidence and acceptance | Project, support, client portal |
| Communication | Conversations, announcements, client-visible activity | Identity, notification |
| Calendar & scheduling | Events, slots, attendees and meeting metadata | Project, CRM, notification |
| Finance & invoicing | Quotes, invoices, invoice lines, credit notes, receivables | Timesheet, milestones, payment |
| Payment orchestration | Payment orders, provider references, webhook records, refunds | Payment providers, finance |
| Support & SLA | Tickets, incidents, severity, response and resolution timestamps | Client portal, notifications |
| Analytics | Project, revenue, utilization, delivery and client metrics | Read-only event/data pipelines |




| Entity group | Representative entities | Relationship notes |
| --- | --- | --- |
| Client organization | ClientOrganization, ClientContact, ClientMembership, BillingProfile | One organization can have multiple users, engagements and billing contacts. |
| Sales | Lead, Opportunity, Discovery, Proposal, Quote | Qualified opportunity becomes a client/engagement after approval. |
| Contract | Agreement, AgreementVersion, Signer, SignatureEvent, SOW, SLA | Executed agreement defines approved scope and terms. |
| Engagement | Engagement, ServiceLine, CommercialModel, Sponsor | A client may have multiple engagements. |
| Project | Project, ProjectMember, Milestone, Dependency, Risk, Decision | An engagement can contain multiple projects. |
| Work management | Task, TaskType, Comment, Attachment, ChangeRequest, Approval | Task changes and approvals are versioned/auditable. |
| Resource | ConsultantProfile, Skill, Availability, Assignment, Timesheet | Published profile is a controlled projection of internal data. |
| Delivery | Requirement, Deliverable, TestCase, Defect, Release, Acceptance | Deliverables link to acceptance criteria and evidence. |
| Calendar | Event, Attendee, AvailabilitySlot, MeetingMinute, ActionItem | Events reference client, engagement or project. |
| Finance | Invoice, InvoiceLine, CreditNote, Payment, Refund, Settlement | Invoices link to approved commercial terms and accepted work. |
| Support | Ticket, Incident, SLAClock, Resolution, Escalation | Ticket visibility is limited to authorized client members. |
| Feedback | FeedbackRequest, Rating, TestimonialConsent, PublishedReview | Public testimonial requires a separate consent and approval state. |




| API area | Example endpoints |
| --- | --- |
| Public lead capture | POST /v1/public/enquiries; POST /v1/public/consultation-bookings |
| Client onboarding | POST /v1/clients/onboarding; GET /v1/clients/{id}/onboarding-status |
| Agreements | GET /v1/clients/{id}/agreements; POST /v1/agreements/{id}/approval |
| Projects | POST /v1/projects; GET /v1/projects/{id}/dashboard; POST /v1/projects/{id}/milestones |
| Tasks | POST /v1/projects/{id}/tasks; PATCH /v1/tasks/{id}; POST /v1/tasks/{id}/approvals |
| Change requests | POST /v1/projects/{id}/change-requests; POST /v1/change-requests/{id}/decision |
| Resources | GET /v1/resources/approved-profiles; POST /v1/projects/{id}/assignments |
| Calendar | POST /v1/calendar/events; POST /v1/calendar/availability |
| Documents | POST /v1/documents; POST /v1/documents/{id}/access-grants |
| Finance | POST /v1/finance/quotes; POST /v1/finance/invoices; GET /v1/finance/invoices/{id} |
| Payments | POST /v1/payments/orders; POST /v1/payments/webhooks/{provider} |
| Support | POST /v1/support/tickets; GET /v1/support/tickets/{id} |
| Reviews | POST /v1/feedback/requests; POST /v1/feedback/{id}/consent |




| Event | Typical consumers |
| --- | --- |
| lead.created | CRM, sales assignment, notification |
| client.onboarded | Identity, project, document, notification |
| agreement.executed | Project initiation, finance, audit |
| project.created | Resource planner, calendar, client portal |
| task.overdue | Project dashboard, notification, escalation |
| change_request.approved | SOW/version, backlog, schedule, finance |
| timesheet.approved | Billing, finance |
| milestone.accepted | Invoice generation, project dashboard |
| invoice.issued | Client portal, notification |
| payment.completed | Receivables, invoice, reconciliation |
| meeting.scheduled | Calendar, notification |
| ticket.sla_breach | Support escalation, management dashboard |
| testimonial.approved | Public CMS/review publication |




| Non-negotiable isolation A client user must never be able to access another client's projects, files, messages, invoices, consultant data or support tickets by changing an identifier or URL. Tenant authorization must be enforced server-side in every service and background job. |
| --- |




| Role | Allowed capabilities | Restricted data |
| --- | --- | --- |
| Client administrator | Manage own organization's portal users and permitted project visibility | Other client organizations and internal delivery records |
| Client sponsor | View portfolio, approve milestones/changes and review reports | Internal cost, margin, private employee records |
| Client project manager | View assigned project, tasks, deliverables, meetings and comments | Unassigned projects and other clients |
| Client finance contact | View invoices, payment instructions and receipts | Internal ledger, bank credentials and other clients |
| Client stakeholder | Read-only access to explicitly shared project information | Private tasks, internal notes and restricted documents |
| Consultant | Assigned projects, tasks, documents and timesheets | Unassigned client data and finance administration |
| Project manager | Delivery plan, resource assignments, risks, client updates and approvals | Unrelated client records unless authorized |
| Finance staff | Quotes, invoices, payment status, reconciliation and refunds | Private project content not required for finance |
| Platform administrator | Technical configuration and controlled support access | Unlogged or unrestricted browsing of client content |




| Dashboard | Core measures |
| --- | --- |
| Public website | Qualified enquiries, service interest, consultation bookings, conversion and content performance |
| Sales pipeline | Lead source, opportunity stage, proposal value, win/loss reasons and sales cycle |
| Client portfolio | Active clients, engagement value, project health, renewals and satisfaction |
| Delivery | Milestone adherence, cycle time, task aging, rework, defect trends and acceptance |
| Resource operations | Capacity, allocation, utilization, skill demand and availability |
| Finance | Revenue, invoiced, collected, receivables, ageing, refunds and project margin where authorized |
| Support | Ticket volume, severity, first response, resolution, SLA compliance and reopen rate |
| Executive | Revenue, pipeline, delivery health, capacity, cash collection and client retention |




| Layer | Recommended baseline | Notes |
| --- | --- | --- |
| Public website | Next.js / React | SEO, accessible pages, performance and content management. |
| Client portal | Next.js / React | Tenant-aware, role-aware experience. |
| Internal workspace | React / Next.js | Delivery, resource, finance and admin workflows. |
| Backend | Python / FastAPI | Domain services and API contracts. |
| API gateway | Kong or equivalent | Routing, rate limits, policy and observability. |
| Identity | Keycloak / OIDC provider | Separate realm/client configuration may be appropriate for domain boundary. |
| Database | PostgreSQL | Tenant-aware schema/database strategy and restricted credentials. |
| Cache | Redis | Short-lived cache, locks and rate-limit state. |
| Event broker | RabbitMQ initially | Outbox, retry and dead-letter queue. |
| Storage | MinIO / S3-compatible | Private client/project buckets or strict prefix/access controls. |
| AI | LiteLLM or equivalent + controlled agent framework | Model abstraction and tenant-aware RAG. |
| Realtime | WebSockets | Client activity and messaging updates. |
| Observability | OpenTelemetry, Prometheus, Grafana | Metrics, logs, traces and alerts. |
| Deployment | Docker + CI/CD | Separate environments; Kubernetes only when justified. |




| Phase | Scope | Exit criteria |
| --- | --- | --- |
| 0 – Foundation | Domain, DNS, identity, API gateway, client tenant model, audit, CI/CD and environments | Public and private apps deployed securely; tenant access tests pass. |
| 1 – Public website & CRM | Company pages, service catalogue, contact, enquiries, consultation booking, lead pipeline | Prospect can understand services, enquire and book; sales team can manage leads. |
| 2 – Client onboarding | Organization/contact records, invitation, onboarding checklist, agreements, document access | Qualified client can onboard and access own workspace. |
| 3 – Project delivery portal | Project dashboard, profiles, tasks, milestones, deliverables, progress and client updates | Client can track work, review deliverables and see authorized progress. |
| 4 – Collaboration & scheduling | Messaging, announcements, calendar, meetings, minutes and notifications | Client and team coordinate in the portal with traceable actions. |
| 5 – Finance & support | Quotes, invoices, payment gateway, receipts, timesheets, tickets and SLAs | Commercial and support workflows operate end-to-end. |
| 6 – Advanced PSA & intelligence | Capacity, profitability, advanced analytics, AI client assistant and automation | Management can optimize delivery and service operations. |




| Area | Acceptance criteria |
| --- | --- |
| Tenant isolation | Automated tests prove Client A cannot access Client B records, attachments, search results or cached data. |
| Object authorization | Changing resource IDs does not bypass project, document, invoice or ticket permissions. |
| Client experience | Client can see current project health, next milestone, pending action and latest approved update. |
| Auditability | Agreement, scope, approval, task, invoice and payment changes record actor, time and reason. |
| Financial integrity | Webhook replay, duplicate requests and out-of-order events do not duplicate payments or invoice allocations. |
| Delivery quality | Bug, feature and change request are distinct types with appropriate workflows. |
| Availability | Service-level objectives are defined from business needs and measured with monitoring. |
| Recoverability | Backups restore successfully in scheduled exercises; RPO/RTO are approved. |
| Accessibility | Portal and public website pass keyboard, contrast, responsive and form usability checks. |
| Privacy | Client profile publication, testimonial use and document sharing have recorded approval. |




| Term | Meaning |
| --- | --- |
| PSA | Professional Services Automation: project, resource, time, billing and service delivery operations. |
| NDA | Non-Disclosure Agreement. |
| MSA | Master Services Agreement. |
| SOW | Statement of Work. |
| SLA | Service Level Agreement. |
| DPA | Data Processing Agreement. |
| RBAC / ABAC | Role-Based / Attribute-Based Access Control. |
| RLS | PostgreSQL Row-Level Security. |
| CSAT / NPS | Customer Satisfaction / Net Promoter Score. |
| HLD / LLD | High-Level Design / Low-Level Design. |

