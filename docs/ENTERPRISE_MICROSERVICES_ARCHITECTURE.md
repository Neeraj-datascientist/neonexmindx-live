# NeoNeX MindX — Enterprise Microservices Architecture & Ecosystem Planning

> **Authoritative Specification Document**  
> **Status:** Architecture Blueprint & Implementation Roadmap  
> **Target Subdomains:** `crm.neonexmindx.com` · `cms.neonexmindx.com` · `lms.neonexmindx.com` · `sms.neonexmindx.com`  
> **Unified Authentication:** Centralized SSO with JWT / OAuth2 and Cross-Domain Session Sync

---

## 1. Executive Summary & Core Principle

The fundamental architectural principle of the NeoNeX MindX platform is **separation of concerns across independent business capabilities**. 
Every business capability operates as an autonomous service exposing strictly typed APIs and publishing event streams. No service directly queries another service's private database.

---

## 2. Module Matrix & Business Responsibilities

| Module | Core Responsibility | Primary Data Entities |
| :--- | :--- | :--- |
| **CRM** | Leads, prospective candidates, follow-ups, counseling pipelines, conversion funnel | Leads, Counselor Notes, Follow-up Queue, Conversion Stages |
| **CMS** | Website architecture, blog publishing, curriculum pages, landing page meta | Articles, Authors, Course Pages, Dynamic Sitemap, SEO Schemas |
| **LMS** | Course delivery, batch management, live sessions, assignments, student grading | Courses, Modules, Cohorts, Submissions, Quizzes, Certificates |
| **DMS** | Digital marketing management, keyword ranking, SEO sentry, performance telemetry | Keywords, PageSpeed Audits, Backlinks, SERP Positions |
| **SMS** | Social media management, post scheduling, channel connectors, engagement | Scheduled Posts, Accounts, UTM Links, Channel Metrics |
| **HRMS** | Employee management, attendance, shifts, leave requests, payroll processing | Employees, Shifts, Leaves, Payroll Slips, Appraisals |
| **EIS** | Employee Information System, internal directory, roles, credentials | Staff Profiles, Designations, Permissions, Hardware Inventory |
| **SIS** | Student Information System, enrollment records, batch attendance, certificates | Enrolled Students, Batch Allocations, Attendance, Graduation |
| **TIS** | Trainer Information System, mentor allocations, demo schedules, ratings | Trainers, Mentors, Assigned Batches, Feedback Scores |
| **Teams** | Departmental organization, team roles, escalation paths | Departments, Team Leads, Slack/Discord Workspaces |
| **Analytics** | Business intelligence, blended CAC, LTV, revenue forecasting, cohort analysis | Telemetry Events, Conversion Funnels, Revenue Attribution |
| **Legal & Doc** | Terms of service, student agreements, placement disclaimers, NDA signatures | Legal Documents, Digital Signatures, Compliance Logs |
| **Finance** | General ledger, accounting, profit/loss, operational expenditures, taxes | Ledger Accounts, Invoices, Expenses, GST Filings |
| **Payments** | Payment collection, multi-gateway routing, instant reconciliation, refunds | Transactions, Payment Orders, Webhook Logs, Refund Requests |
| **Fees** | Student fee schedules, flexible installments, No-Cost EMI plans, outstanding dues | Fee Plans, Due Reminders, EMI Schedules, Receipts |
| **Feedback** | Student NPS, module reviews, counselor ratings, trainer appraisals | Review Submissions, NPS Trends, Testimonials |
| **ERP** | Cross-department business workflow orchestration, resource planning | Cross-Service Orchestration, Inventory, System Workflows |

---

## 3. Microservices Architecture Topology

```
                       [ Incoming Public / Client Traffic ]
                                      │
                                      ▼
                 ┌──────────────────────────────────────────┐
                 │          Central API Gateway             │
                 │  - Routing & Reverse Proxy               │
                 │  - Token Verification (JWT/OAuth2)       │
                 │  - Rate Limiting & Sentry Protection     │
                 │  - API Versioning (/v1, /v2)             │
                 └────────────────────┬─────────────────────┘
                                      │
         ┌──────────────┬─────────────┼──────────────┬──────────────┐
         ▼              ▼             ▼              ▼              ▼
   ┌───────────┐  ┌───────────┐ ┌───────────┐  ┌───────────┐  ┌───────────┐
   │ Identity  │  │    CRM    │ │ Academic  │  │  Payment  │  │ Finance   │
   │  Service  │  │  Service  │ │ (LMS/SIS) │  │  Service  │  │  Service  │
   └─────┬─────┘  └─────┬─────┘ └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
         │              │             │              │              │
         └──────────────┴─────────────┼──────────────┴──────────────┘
                                      ▼
                 ┌──────────────────────────────────────────┐
                 │          Event Bus / Message Broker      │
                 │         (RabbitMQ / Cloudflare Queues)   │
                 └────────────────────┬─────────────────────┘
                                      │
         ┌──────────────┬─────────────┼──────────────┬──────────────┐
         ▼              ▼             ▼              ▼              ▼
   ┌───────────┐  ┌───────────┐ ┌───────────┐  ┌───────────┐  ┌───────────┐
   │ Comm / WA │  │ Document  │ │ Analytics │  │    SMS    │  │  AI Voice │
   │  Gateway  │  │  Storage  │ │  Service  │  │  Service  │  │  Gateway  │
   └───────────┘  └───────────┘ └───────────┘  └───────────┘  └───────────┘
```

---

## 4. Gateways Hierarchy: Distinction of Boundaries

> [!IMPORTANT]
> **Architectural Law: Payment Gateway $\neq$ API Gateway.**  
> The **API Gateway** manages internal microservices communication and security. The **Payment Gateway** connects payment services to banking and settlement rails.

| Gateway Layer | Primary Purpose | Examples / Vendors |
| :--- | :--- | :--- |
| **API Gateway** | Central entry point for all frontend apps, routing, SSL termination, JWT auth, rate limiting | Cloudflare Workers / Traefik / Kong / Express Gateway |
| **Payment Gateway** | External payment processing, UPI QR, card charges | Razorpay, Cashfree, PhonePe, Stripe |
| **Banking Gateway** | Institutional bank integrations, payout APIs, virtual accounts | ICICI/HDFC Corporate Banking, Cashfree Payouts |
| **EMI Gateway** | Instant No-Cost EMI approval and NBFC partnerships | Propelld, LiquiLoans, Eduvanz, ShopSe |
| **Communication Gateway**| Multi-channel messaging (WhatsApp, SMS, transactional email) | Meta WhatsApp Cloud API, Resend, SendGrid, Twilio |
| **Authentication Gateway**| Single Sign-On (SSO), RBAC, session cookie management | Supabase Auth / Keycloak / Clerk |
| **AI Gateway** | Unified routing to LLMs and voice synthesis engines | Google Cloud Vertex AI (Gemma/Gemini), ElevenLabs, Deepgram |
| **Storage Gateway** | Object storage for syllabus PDFs, student submissions, agreements | Cloudflare R2 / AWS S3 / MinIO (S3-compatible) |

---

## 5. Subdomain Organization & DNS Topology

* **Main Portal:** `https://neonexmindx.com` — Landing pages, course catalog, conversion funnels.
* **Admissions CRM:** `https://crm.neonexmindx.com` — Master sales application, counselor queues, incoming Meta/Google webhooks.
* **CMS Studio:** `https://cms.neonexmindx.com` — Blog publisher, dynamic sitemap, landing page metadata manager.
* **LMS Academy:** `https://lms.neonexmindx.com` — Enrolled learner dashboard, video curriculum, quizzes, coding labs.
* **Social Hub:** `https://sms.neonexmindx.com` — Content calendar, channel publishers, attribution generators.
* **API Gateway:** `https://api.neonexmindx.com` — Unified endpoint routing (`/v1/crm/*`, `/v1/auth/*`, `/v1/payments/*`).

---

## 6. Open-Source Database Selection & Scalability Analysis

### Primary Recommendation: **PostgreSQL on Cloudflare Hyperdrive / Supabase**
1. **Generous Free Tier & Open-Source Foundation:**
   - **Cloudflare D1 (Edge SQLite)**: Unlimited read replication, zero cold start, globally distributed across 300+ PoPs, 5 GB storage free.
   - **PostgreSQL (Supabase / Neon)**: Fully relational ACID compliance, row-level security (RLS), JSONB support for dynamic lead metadata, 500 MB to 3 GB free tier.
2. **Enterprise Reliability:**
   - Decoupled database per microservice or isolated schemas (`schema_crm`, `schema_lms`, `schema_finance`) in a unified PostgreSQL instance.
   - Zero vendor lock-in: Can be self-hosted on Hetzner, AWS, or local bare-metal via Docker Compose at any time.

---

## 7. Phase 2 AI & Sales Automation Roadmap

1. **AI Autonomous Voice Calling for Inbound Leads:**
   - **Mechanism:** When a lead is ingested via `/api/webhook/meta` or `/api/webhook/google-ads`, trigger an automated webhook to an AI voice pipeline (Deepgram speech-to-text $\rightarrow$ Gemma 2 / Gemini $\rightarrow$ ElevenLabs/Cartesia realistic Indian English voice).
   - **Conversation Objective:** Clarify learning background (e.g. "Hi Karthik, this is the NeoNeX MindX admissions desk. We saw your inquiry about Data Science. Are you looking to transition from QA or another field?").
   - **Handoff:** If the candidate expresses high intent, transfer live or schedule a calendar demo with Mercy or Neeraj.
2. **Website AI Chatbot:**
   - Embedded widget on `neonexmindx.com` answering curriculum, placement assistance, and fee queries with instant lead capture.
3. **Automated Brochure & Syllabus Sharing:**
   - **WhatsApp Cloud API Automation:** Send syllabus PDF instantly upon form submission.
   - **Direct 1-Click Download:** Instant PDF download on website with background CRM lead logging.
4. **Autonomous Digital Marketing Agents (Agency Council):**
   - Autonomous scheduled agents running daily competitor SERP scans, auto-generating LinkedIn carousel drafts, and validating SEO metadata before publishing.
