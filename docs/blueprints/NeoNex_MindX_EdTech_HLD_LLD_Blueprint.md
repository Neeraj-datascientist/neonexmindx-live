NEONEX MINDX


# EDTECH

Education • Learning • Internship • Projects • Careers • Community

DOMAIN: neonexmindx.com  |  Dedicated Education Vertical

MASTER HIGH-LEVEL DESIGN (HLD) + LOW-LEVEL DESIGN (LLD)

Prepared as an implementation blueprint • Version 1.0 • 02 November 2026


# Document control & purpose


# 1. Executive summary

NeoNex MindX EdTech is designed as a digital education and career-development ecosystem. It combines the public education website, lead and admission operations, LMS, student information, trainer operations, assessments, project submission and evaluation, internships, placement assistance, interview practice, community, messaging, announcements, calendar, notifications, fees and finance.

The platform should support the complete lifecycle of a learner while providing controlled workspaces for trainers, mentors, academic administrators, placement staff, finance staff and management.


## 1.1 Outcomes

Provide a consistent experience from first enquiry through alumni engagement.

Give students one dashboard for learning, deadlines, projects, internships, career preparation and communication.

Give trainers and mentors structured tools for classes, attendance, evaluation, feedback and supervision.

Give the Placement Assistance Cell an employer, opportunity, application and interview pipeline.

Provide management with measurable academic, operational, financial and career outcomes.

Automate reminders, announcements, approvals and routine administrative workflows.


# 2. Scope, users and domain boundary


# 3. Product and subdomain structure

All hostnames are proposed. Configure DNS, TLS, cookies, redirect allowlists and identity callback URLs only after the domain and deployment plan are approved.


# 4. Functional capability map


# 5. End-to-end learner lifecycle

Figure 1. End-to-end EdTech learner lifecycle.


# 6. Detailed module requirements


## 6.1 LMS and academic management

Course catalogue, course versions, modules, lessons, resources and prerequisites.

Batch/cohort creation, trainer assignment, class timetable, attendance and session links.

Learning progress, completion rules, assessments, quiz attempts and grade records.

Content publishing workflow with draft, review, approved, published and retired states.

Course feedback, trainer feedback, student support and academic intervention flags.


## 6.2 Project submission and evaluation portal

Support individual and team projects, project briefs, objectives, expected deliverables and eligibility.

Track milestones, task ownership, due dates, repository URL, branches/tags and demo links.

Accept code archives, documents, datasets, presentations, videos and links with file validation.

Maintain immutable submission versions, timestamps, submitter identity and receipt.

Assign mentor, reviewer and viva panel; configure rubric by programme/project type.

Rubric dimensions may include requirements coverage, technical correctness, code quality, testing, documentation, originality and presentation.

Support review comments, scoring, moderation, re-submission, appeals and final approval.

Similarity/plagiarism checks are indicators for human review, not automatic proof of misconduct.


## 6.3 Complete internship management

Create internal, employer-sponsored and client-sponsored internship programmes with separate policies.

Define role, skills, duration, eligibility, capacity, supervisor, deliverables and assessment criteria.

Support application, screening, selection, offer, acceptance, onboarding and allocation.

Provide intern workspace with tasks, attendance, daily logs, weekly reports, learning objectives and evidence.

Mentor dashboard for feedback, review cadence, attendance exceptions and escalation.

Final evaluation, completion approval, certificate eligibility and portfolio evidence.

Track withdrawal, extension, pause, incomplete and rework outcomes with reasons.


## 6.4 Placement Assistance Cell

Employer/recruiter records, contacts, agreements, company verification and relationship history.

Job and internship requisitions with role, skills, location, compensation disclosure, eligibility and expiry.

Candidate profile with explicit consent, resume versions, skills, projects, certificates and preferences.

Eligibility rules and shortlisting; keep human review for consequential decisions.

Application pipeline, interview rounds, feedback, offer, joining and outcome tracking.

Placement support status must be clear and must not imply a guaranteed job unless contractually agreed.


## 6.5 Interview preparation and simulator

Question banks by role, skill, difficulty and interview round.

Aptitude, technical MCQ, coding exercises, SQL/Python tasks and HR question practice.

Mock interview booking with human mentors and configurable evaluation rubrics.

AI-assisted text or voice practice with question generation and feedback, subject to consent.

Feedback should explain evidence, strengths, gaps and suggested practice; avoid unsupported personality or hiring claims.

Store session history, candidate consent, retention rules and improvement trends.


## 6.6 Community, messaging and announcements

Separate public/community posts, private conversations and official announcements.

Spaces for courses, batches, projects, technical topics, alumni, mentors and job referrals.

Direct messages and group chats with membership checks, block/report/moderation and retention policy.

Official announcements can target all students, selected courses, batches, trainers, alumni or placement cohorts.

Job referrals need verification, expiry, source attribution, consent and moderation.

Provide search, attachments, reactions, threaded discussions and report handling.


## 6.7 Calendar and notifications

Unified EdTech calendar for classes, assessments, counselling, deadlines, internships, interviews and events.

Availability slots, recurring events, attendee responses, reschedule/cancel and timezone support.

Notification preferences by channel and category; in-app, email, push and approved messaging providers.

Scheduled reminders, retries, delivery tracking, deduplication, quiet hours and escalation.

Read/acknowledgement tracking for mandatory policy or academic announcements.


## 6.8 Fees, invoices and finance

Fee plans, discounts, scholarships, instalment schedules, due dates and student account ledger.

Invoice and receipt numbering, tax configuration, credit notes, refunds and reconciliation.

Payment provider adapters; never store card CVV or raw card credentials.

Webhook signature validation, idempotency, payment state machine and audit history.

Finance reports for collections, receivables, refunds, discounts and ageing.


# 7. High-level technical architecture

Figure 2. EdTech high-level architecture.


# 8. Service catalogue and ownership


# 9. Core data model (logical)


# 10. API and event design

Expose versioned domain APIs through the gateway. Keep internal service APIs private and enforce authorization in the owning service, not only at the gateway.


# 11. Roles and permission model


# 12. Security, privacy and governance

Use OIDC/OAuth2 SSO, MFA for privileged roles and short-lived access tokens.

Apply server-side RBAC and ABAC using role, business unit, cohort, assignment, ownership and consent.

Use least-privilege database credentials; consider PostgreSQL row-level security for shared tables.

Keep object storage private and use short-lived authorized download links.

Validate every webhook signature and use idempotency keys for financial operations.

Encrypt data in transit and at rest; manage secrets outside source control.

Record sensitive changes, grade publication, refunds, access grants and administrator actions in audit logs.

Define retention, deletion, consent and data export procedures for student and candidate information.

AI retrieval and chatbot tools must inherit the user's permissions; do not expose one student's records to another.

Use synthetic data in development and masked data in testing.


# 13. Analytics and management dashboards


# 14. Recommended technology stack


# 15. Delivery roadmap


# 16. Non-functional requirements and acceptance criteria


# 17. Decisions required before detailed build

Confirm exact EdTech domain/subdomain names and whether the existing CRM/LMS codebase will be reused.

Confirm course, batch, fee and certificate policies.

Define internship tracks and whether external employer/client-sponsored internships are in scope at launch.

Define placement assistance terms, employer verification and candidate consent language.

Choose payment providers and validate merchant onboarding, settlement and refund requirements.

Define expected user volumes, concurrent sessions, storage and video delivery requirements.

Approve retention, privacy, accessibility and support policies.


# 18. Glossary



| STRATEGY & EXPERIENCE | PLATFORM & SERVICES | SECURITY & OPERATIONS |
| --- | --- | --- |




| Item | Definition |
| --- | --- |
| Document | NeoNex MindX EdTech – Master HLD & LLD |
| Purpose | Define the complete EdTech operating platform, user experiences, services, data ownership, integrations and delivery plan. |
| Business boundary | Education vertical only. IT consultancy client operations remain on the separate technology domain and platform boundary. |
| Status | Proposed architecture for validation and implementation planning. |
| Version | 1.0 – 02 November 2026 |
| Audience | Founder, product owner, architects, developers, QA, operations, academic and placement teams. |




| Architecture principle Build a complete learner lifecycle platform: discover → enquire → enrol → learn → practice → submit projects → complete internships → prepare for interviews → access opportunities → join alumni community. Keep education data and workflows independent from the IT consultancy vertical. |
| --- |




| User persona | Primary responsibilities | Access boundary |
| --- | --- | --- |
| Prospective learner | Explore courses, submit enquiry, book counselling | Public pages and own enquiry |
| Student | Learning, attendance, assessments, projects, internship, career profile | Own record, assigned cohorts and permitted community spaces |
| Trainer | Classes, learning content, attendance, assessment | Assigned courses, batches and students |
| Mentor / Evaluator | Project reviews, internship supervision, feedback | Assigned projects/interns only |
| Placement officer | Employers, jobs, eligibility, applications, outcomes | Placement records and consented candidate profiles |
| Employer / Recruiter | Post roles, review permitted profiles, shortlist | Employer organization and authorized candidates |
| Finance staff | Fees, invoices, receipts, refunds and reconciliation | Financial records by assigned scope |
| Academic admin | Courses, batches, schedules, policies and approvals | Education operations |
| Management | Business KPIs and authorized approvals | Aggregated reporting plus explicitly authorized records |
| Alumni | Community, mentoring and referrals | Own profile and approved alumni spaces |




| Strict separation This document covers the EdTech vertical only. The IT consultancy public website, client onboarding portal, client project management, consultancy contracts and client billing are specified in a separate architecture document. |
| --- |




| Proposed host | Experience | Notes |
| --- | --- | --- |
| neonexmindx.com | Official EdTech public website | Courses, programmes, faculty, outcomes, enquiries, reviews, events and admissions. |
| learn.neonexmindx.com | Student learning portal | Learning dashboard, course content, attendance, assessments and progress. |
| community.neonexmindx.com | Student and alumni community | Forums, groups, mentoring, job referrals and moderated discussions. |
| careers.neonexmindx.com | Career and placement portal | Jobs, internships, applications, placement status and employer interactions. |
| practice.neonexmindx.com | Interview practice portal | Mock interviews, question banks, coding and aptitude practice. |
| admin.neonexmindx.com | Internal administration | Role-specific operations and management dashboards. |
| api.neonexmindx.com | API entry point | Versioned API gateway; internal services remain private. |
| auth.neonexmindx.com | Identity entry point | Central authentication for the EdTech domain. |




| Domain | Capabilities |
| --- | --- |
| Public website & admissions | Service/course catalogue, programme pages, enquiry forms, counselling booking, lead capture, application and admission status. |
| CRM & sales | Lead assignment, source tracking, counselling, follow-up, conversion, pipeline and communication history. |
| LMS | Courses, modules, lessons, learning resources, cohorts, live sessions, progress, completion and certificates. |
| Student information | Student profile, enrolment, batch, academic history, documents, status and consent. |
| Trainer information | Trainer profile, skills, availability, allocation, workload and feedback. |
| Academic operations | Timetable, attendance, assessments, results, academic calendar and course quality. |
| Projects & evaluation | Project catalogue, allocation, teams, milestones, repository links, submission versions, rubrics, viva and rework. |
| Internship management | Programme creation, applications, selection, allocation, mentor, tasks, logbook, review and completion. |
| Placement assistance | Employer CRM, job postings, eligibility, candidate matching, applications, interviews and outcomes. |
| Interview practice | Question banks, coding/aptitude exercises, mock interviews, scoring and improvement plans. |
| Community & alumni | Discussion spaces, alumni directory, mentorship, job referrals, events and moderation. |
| Finance | Course fees, instalments, discounts, invoices, receipts, refunds, payment allocation and reconciliation. |
| Collaboration | Messaging, announcements, calendar, notifications, tasks and approvals. |
| Analytics | Admissions funnel, learning progress, completion, trainer utilization, internship and placement outcomes. |




| Service boundary | Owns | Key integrations |
| --- | --- | --- |
| Identity & access | Users, memberships, roles, permissions, sessions | All portals and services |
| Admissions & CRM | Leads, enquiries, counselling, applications | Public site, finance, notifications |
| Academic core | Courses, batches, enrolments, trainer allocation | LMS, calendar, student profile |
| Learning & assessment | Content progress, attendance, assessments, results | Academic core, notifications, analytics |
| Project & evaluation | Project briefs, allocations, submissions, rubrics, reviews | LMS, Git provider, documents |
| Internship | Programmes, applications, allocations, logs, reviews | Calendar, mentors, certificates |
| Career & placement | Employers, jobs, applications, referrals, outcomes | Career portal, community, consent |
| Interview practice | Question banks, sessions, attempts, feedback | AI gateway, calendar, career profile |
| Community & communications | Spaces, conversations, messages, announcements | Identity, notification, moderation |
| Calendar & scheduling | Events, slots, attendees, recurrence | All modules, external calendars |
| Notification orchestration | Templates, preferences, delivery, retries | Email, push, SMS/WhatsApp providers |
| Finance & payments | Fee accounts, invoices, payment orders, refunds | Provider adapters, ledger, receipts |
| Documents | Files, metadata, versions, access grants | Projects, internship, finance, agreements |
| Analytics | Aggregated reporting models and metrics | Read-only event/data pipelines |




| Entity group | Representative entities | Relationship notes |
| --- | --- | --- |
| Identity | User, Role, Permission, Membership, Consent | One identity may hold multiple authorized roles; no duplicate user record per portal. |
| Academic | StudentProfile, Course, CourseVersion, Batch, Enrollment, TrainerProfile | Enrollment links a student to a course/cohort and governed academic status. |
| Assessment | Assessment, Question, Attempt, Result, Attendance | Keep attempts and published results auditable. |
| Projects | ProjectBrief, ProjectTeam, Assignment, Milestone, Submission, Evaluation, Rubric | Submission is versioned; evaluation references a specific submission version. |
| Internship | Programme, Application, Placement, LogEntry, MentorReview, Completion | Application state and programme state are separate. |
| Career | Employer, Job, CandidateProfile, Application, Referral, InterviewRound, Offer | Candidate visibility requires consent and eligibility checks. |
| Community | Space, Membership, Post, Conversation, Message, Announcement | Audience membership and visibility must be checked server-side. |
| Calendar | Calendar, Event, Attendee, AvailabilitySlot, Reminder | Events can reference source records such as class or interview. |
| Finance | FeePlan, StudentAccount, Invoice, InvoiceLine, PaymentOrder, Transaction, Refund | Ledger movements and payment events must be auditable. |
| Documents | Document, Version, Attachment, AccessGrant | Object storage keys are private; authorization is checked before download. |




| API area | Example endpoints |
| --- | --- |
| Admissions | POST /v1/admissions/enquiries; POST /v1/admissions/applications; GET /v1/admissions/{id} |
| Academic | GET /v1/academic/courses; POST /v1/academic/enrollments; POST /v1/academic/attendance |
| Projects | POST /v1/projects/{id}/submissions; GET /v1/projects/{id}/evaluations |
| Internships | POST /v1/internships; POST /v1/internships/{id}/applications; POST /v1/internship-placements/{id}/logs |
| Career | GET /v1/career/jobs; POST /v1/career/applications; POST /v1/career/referrals |
| Interview | POST /v1/interview/sessions; POST /v1/interview/sessions/{id}/attempts |
| Calendar | POST /v1/calendar/events; POST /v1/calendar/availability |
| Communication | POST /v1/communications/conversations; POST /v1/announcements |
| Finance | POST /v1/finance/invoices; POST /v1/payments/orders |




| Event | Typical consumers |
| --- | --- |
| student.enrolled | LMS, finance, notification, analytics |
| class.scheduled | Calendar, notification |
| project.submitted | Evaluation, mentor notification, audit |
| evaluation.completed | Student dashboard, notification, analytics |
| internship.assigned | Calendar, mentor, notification |
| internship.completed | Career profile, certificate, analytics |
| job.published | Career portal, eligible audience notification |
| interview.scheduled | Calendar, candidate and interviewer notification |
| payment.completed | Student account, invoice, receipt, reconciliation |




| Role | Typical permissions | Restrictions |
| --- | --- | --- |
| Student | Own learning, submissions, profile, applications, messages | Cannot view other student records or unassigned evaluation data. |
| Trainer | Assigned course/batch, attendance, content and assessments | No access to unrelated batches or finance administration. |
| Mentor/evaluator | Assigned internship/project review and rubric | Cannot change published policy or unrelated results. |
| Placement officer | Employer/job pipeline and consented candidate profiles | Sensitive student records remain restricted. |
| Recruiter | Own job requisitions and approved candidate profiles | No access to private academic or financial records. |
| Finance | Fees, invoices, refunds and reconciliation | No unrestricted academic or placement access. |
| Academic admin | Course, batch, schedule and academic approvals | Financial and identity administration remain separately controlled. |
| Platform admin | Configuration and operational controls | Privileged actions require audit and least privilege. |




| Dashboard | Core measures |
| --- | --- |
| Admissions | Enquiries, source, counselling conversion, applications, enrolments, cost per acquisition where available |
| Academic | Attendance, learning progress, assessment completion, course completion, at-risk learners |
| Projects | Submission timeliness, review turnaround, rework, rubric distribution, completion |
| Internships | Applications, allocation, attendance/logs, mentor reviews, completion |
| Placement | Eligible learners, applications, interview progression, offers, joining and employer engagement |
| Finance | Fees billed, collected, outstanding, ageing, refunds, discounts and reconciliation |
| Operations | Trainer workload, room/session utilization, support volume and notification delivery |
| Community | Active participation, event engagement, referral activity and moderation metrics |




| Layer | Recommended baseline | Notes |
| --- | --- | --- |
| Frontend | React / Next.js | Separate branded apps or portal surfaces; shared design system is acceptable. |
| Backend | Python / FastAPI | Domain modules with explicit contracts. |
| API gateway | Kong or equivalent | Routing, rate limiting, API policies and observability. |
| Identity | Keycloak / OIDC provider | SSO and role/membership management. |
| Database | PostgreSQL | Domain-owned schemas/databases and controlled credentials. |
| Cache | Redis | Cache and short-lived coordination; avoid using cache as source of truth. |
| Messaging/events | RabbitMQ initially | Use outbox, retries and dead-letter handling. |
| Files | MinIO / S3-compatible storage | Private buckets, lifecycle and access grants. |
| Search/AI | PostgreSQL full text; pgvector/Qdrant when needed | Permission-aware retrieval. |
| Realtime | WebSockets | Chat, live updates and presence where justified. |
| Observability | OpenTelemetry, Prometheus, Grafana | Logs, metrics, traces and alerts. |
| Deployment | Docker + CI/CD | Start without Kubernetes unless scale/operations justify it. |




| Phase | Scope | Exit criteria |
| --- | --- | --- |
| 0 – Foundation | Domain/DNS, identity, roles, gateway, audit, CI/CD, database conventions | SSO, environments, access policies, backups and deployment pipeline verified. |
| 1 – Admissions & LMS core | Public website, enquiries, CRM, courses, batches, student portal, attendance | A learner can enquire, enrol and access assigned learning. |
| 2 – Academic outcomes | Assessments, project portal, submission versioning, rubric and evaluation | A project can be assigned, submitted, reviewed and finalized. |
| 3 – Internship & career | Internship lifecycle, employer records, jobs, referrals and placement pipeline | Internship and placement workflows operate with consent and audit. |
| 4 – Collaboration | Community, messaging, announcements, calendar and notifications | Targeted communications and reminders are reliable and permission-aware. |
| 5 – Interview & AI | Question bank, practice sessions, AI-assisted feedback and student assistant | AI tools are permission-controlled, evaluated and monitored. |
| 6 – Finance & analytics | Fee engine, invoices, payment orchestration, reconciliation and dashboards | Financial states reconcile and management metrics are validated. |




| Area | Baseline requirement / acceptance test |
| --- | --- |
| Security | Unauthorized cross-student, cross-batch and cross-role access tests must fail. |
| Privacy | Candidate profile visibility requires recorded consent and revocation handling. |
| Reliability | Financial webhooks and event consumers are idempotent; failed messages can be retried safely. |
| Auditability | Grade changes, refunds, approvals and privileged access changes record actor, time and reason. |
| Performance | Set measurable targets after expected concurrent users and workload are estimated; test peak class and submission periods. |
| Accessibility | Keyboard navigation, clear labels, contrast and responsive layouts are tested. |
| Usability | Student dashboard surfaces next class, pending work, deadlines and important notices. |
| Recoverability | Backups are restored in scheduled tests; recovery objectives are documented. |
| Data quality | Course, student, batch and finance identifiers are consistent and validated. |
| AI safety | Assistant cannot retrieve unauthorized records or execute sensitive actions without approved workflows. |




| Term | Meaning |
| --- | --- |
| HLD | High-Level Design: system context, components, interactions and deployment. |
| LLD | Low-Level Design: service boundaries, data entities, APIs, events and rules. |
| RBAC | Role-Based Access Control. |
| ABAC | Attribute-Based Access Control. |
| RLS | PostgreSQL Row-Level Security. |
| Outbox pattern | Persist business change and event record atomically, then publish reliably. |
| RAG | Retrieval-Augmented Generation. |
| SIS / TIS | Student Information System / Trainer Information System. |

