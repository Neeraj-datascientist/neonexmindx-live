# NeoNeX MindX — Project Status, Portals & Marketing Master Roadmap (TODO)

> **Last Updated:** November 2026  
> **Status:** Multi-Device Portals Active • Dynamic Sitemap Operational • Central CRM Synced • Social Hub & Attribution Builder Deployed  
> **Authoritative Directories:** [`deployment_NeoNex/`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex) & [`finalised_deployment/`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/finalised_deployment)  
> **Strict Lock:** [`Cleaned HTML/`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/Cleaned%20HTML) is **PERMANENTLY LOCKED & READ-ONLY** (per [`AGENTS.md`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/AGENTS.md)).

---

## 1. Quick Access & Multi-Device Credentials

All portals are accessible from any phone, tablet, or secondary laptop on the same local network or in production.

### Portal URLs:
* **Local Network (Wi-Fi):**
  * **CMS Studio:** `http://192.168.0.10:3000/cms`
  * **Admissions CRM:** `http://192.168.0.10:3000/crm`
  * **Digital Marketing Hub:** `http://192.168.0.10:3000/digital-marketing`
* **Production Deployment:**
  * **CMS Studio:** `https://neonexmindx.com/cms`
  * **Admissions CRM:** `https://neonexmindx.com/crm`
  * **Digital Marketing Hub:** `https://neonexmindx.com/digital-marketing`

### Team Credentials:
| Account Name | Username | Password | Permitted Roles & Portals |
| :--- | :--- | :--- | :--- |
| **Neeraj** | `Neeraj` | `Hsc19ph0040@` | **SuperAdmin** (Admissions CRM, CMS Studio, Marketing Hub) |
| **Puneeth** | `puneeth` | `puneeth$123` | **Admin** (Admissions CRM, CMS Studio, Marketing Hub) |
| **Mercy** | `mercy` | `mercy$123` | **Editor / Counsellor** (Admissions CRM) |

*Note: Mobile screens feature **1-Tap Quick Fill** buttons inside [`neonex-auth.js`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/neonex-auth.js) to avoid typing errors on touchscreens.*

---

## 2. Completed Implementations & Systems in Place

### A. Dynamic Sitemap Engine
- [x] Built dynamic sitemap generator in [`deployment_NeoNex/generate_sitemap.py`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/generate_sitemap.py) reading [`data/blogs.json`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/data/blogs.json).
- [x] Integrated dynamic `/sitemap.xml` endpoint into [`serve_netlify.py`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/serve_netlify.py) with live `application/xml` header.
- [x] Integrated auto-regeneration trigger on CMS blog save (`/api/save-blogs`).
- [x] Added **"⚡ Sync Live Sitemap to Server"** button in CMS Studio ([`deployment_NeoNex/cms/index.html`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/cms/index.html)).

### B. Multi-Device Central Authentication & RBAC Sync
- [x] Created central [`data/users.json`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/data/users.json) and mirrored to `finalised_deployment/`.
- [x] Added `/api/auth/users` (GET & POST) in [`serve_netlify.py`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/serve_netlify.py) with CORS preflight support.
- [x] Updated [`deployment_NeoNex/neonex-auth.js`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/neonex-auth.js) with async cloud synchronization, 1-tap mobile credentials, and iOS auto-zoom prevention.

### C. CRM Data Silo Fix & Universal Telemetry
- [x] Created centralized [`data/crm_data.json`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/data/crm_data.json) replacing isolated browser `localStorage`.
- [x] Added `/api/submit-lead` and `/api/leads` endpoints in [`serve_netlify.py`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/serve_netlify.py).
- [x] Built [`deployment_NeoNex/neonex-tracker.js`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/neonex-tracker.js): captures `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `gclid`, `fbclid` into `sessionStorage` and intercepts form submissions to route them straight to `/api/submit-lead`.
- [x] Injected `neonex-tracker.js` across all 17 public-facing landing and course pages.
- [x] Added marketing attribution badges in CRM table (`🎯 utm_source • utm_campaign`).

### D. Digital Marketing Hub Enhancements
- [x] Fixed sign-out typo (`NeoNexAuth.logout` -> `NeonexAuth.logout`) in [`digital-marketing/index.html`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/digital-marketing/index.html).
- [x] Built **Social & Community Distribution View (`#view-social`)**:
  - 4 Social KPIs: LinkedIn Reach (14.2K), YouTube Watch Time (48.6K), Reels/Shorts (120K), Community (1,420 Active Learners).
  - 5 Channel Architecture Cards (LinkedIn, YouTube, Instagram, WhatsApp/Discord, Twitter/X).
  - 7-Day Editorial Content Matrix (Monday Tech Build, Wednesday Alumni Spotlight, Friday Hiring Trends, Sunday Live AMA).
  - Interactive **UTM Campaign Link Generator Tool** with 1-click copy and instant test link.

### E. CMS Studio, Dynamic Sitemap & SEO Meta Engine Upgrades
- [x] **Dynamic Sitemap & Real-time Server Sync:**
  - Removed all hardcoded stale dates (`2026-10-09`) in CMS client templates; replaced with real-time dynamic dates and post `updatedAt`/`publishDate`.
  - Added auto-fetch of `/sitemap.xml` on CMS view render.
  - Linked **"⚡ Sync Live Sitemap to Server"** to `POST /api/sync-sitemap` with instant textarea refresh.
- [x] **RTE Heading Tags & Toolbar Selection Persistence:**
  - Added `onmousedown="event.preventDefault()"` across all toolbar buttons (`#rte-btn-h1`, `#rte-btn-h2`, `#rte-btn-h3`, alignments, inline formats).
  - Built `APP.saveSelection()` & `APP.restoreSelection()` hooked into `onmouseup`, `onkeyup`, `oninput`, `onclick`, `onblur`, and `onfocus`.
  - Rewrote `applyHeading(tag, isButtonToggle)` to seamlessly transform blocks (`<h1>`, `<h2>`, `<h3>`), preserve cursor position, sync `#rte-format-select.value`, and toggle `.active` classes.
- [x] **Dedicated Meta Title (SEO Title) with Live SERP Preview:**
  - Added `#ed-metatitle` field in CMS SEO tab with character counter (`0 / 60 characters`) and optimal length indicator (50-60 chars).
  - Built interactive live Google SERP snippet preview rendering real-time headline, slug URL, and meta description.
  - Integrated `metaTitle` into `calculateLiveSeo()`, `saveCurrentEditor()`, `updateLiveSchemas()`, and [`blog-post.html`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/blog-post.html) `<title>` & `og:title`.
- [x] **Dedicated URL Article Draft Preview:**
  - Refactored `previewCurrentEditor()` to package draft post data into `localStorage['neonex_blog_preview_draft']`.
  - Opens dedicated browser tab at `/blog-post.html?preview=true&slug=...` with full live template and top preview mode banner.
- [x] **Author Profile Edit Modal & Data Sync:**
  - Added **"Edit"** button alongside "Delete" on author rows in CMS Authors view.
  - Built `APP.openEditAuthorModal(authorId)` with pre-filled Name, Designation, Email, LinkedIn URL, Avatar photo upload/URL, and Bio.
  - Built `APP.saveAuthorChanges(authorId)` persisting updates to local storage, `/api/save-blogs`, and server disk.
  - Fixed startup sync in `init()` to merge `diskData.authors` into `DB.authors`.
- [x] **Course & Landing Pages Meta Details Manager:**
  - Built Course & Landing Pages Meta Manager in `renderPages()` tracking all 14 site pages (Home, Data Analytics, Data Science, AI/ML, Data Engineering, Business Analytics, Excel/PowerBI, SQL, Python, ML, About Us, Trainers, Contact Us, Blogs Directory).
  - Created `POST /api/save-page-meta` and `GET /api/page-meta` in [`serve_netlify.py`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/serve_netlify.py).
  - Built `openEditPageMetaModal(pageKey)` and `savePageMeta(pageKey)` allowing instant edits to `<title>`, `<meta name="description">`, keywords, canonical, and OG image with automated regex replacement directly in underlying HTML files.

### F. Enterprise Sales CRM, Ad Integrations & Social Media Studio (SMS)
- [x] **Test Record Purge & Production Readiness:**
  - Removed all fake and test records (`pooja.sharma.test@gmail.com`) from [`data/crm_data.json`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/data/crm_data.json).
  - Validated clean production data structure for leads, batches, counselor assignments, and financial tracking.
- [x] **Meta Lead Ads & Google Ads Direct Webhook Connectors:**
  - Added `GET /api/webhook/meta` with verification challenge (`hub.challenge` & `hub.verify_token`).
  - Added `POST /api/webhook/meta` automatically ingesting Facebook & Instagram Instant Form leads into CRM with attribution (`utm_source: 'meta_ads'`).
  - Added `POST /api/webhook/google-ads` extracting Lead Form extension fields into CRM leads with attribution (`utm_source: 'google_ads'`).
  - Verified live endpoint responses and CRM persistence.
- [x] **Dedicated Social Media Management Hub (SMS):**
  - Created [`deployment_NeoNex/sms/index.html`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/sms/index.html) matching CMS design language (DM Sans, Sora, JetBrains Mono, glassmorphism, dark/light theme).
  - Built channel connectors for LinkedIn, YouTube, Instagram, WhatsApp, and X/Twitter.
  - Built multi-channel Editorial Calendar, ad campaign performance tracking, and interactive UTM Attribution Builder.
  - Wired routing in [`_redirects`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/_redirects) for `/sms` and `/social`.
- [x] **Enterprise Microservices Architecture & Master Blueprints:**
  - Created [`docs/ENTERPRISE_MICROSERVICES_ARCHITECTURE.md`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/docs/ENTERPRISE_MICROSERVICES_ARCHITECTURE.md) documenting all 17 microservices.
  - Reorganized future roadmap into living document at [`docs/FUTURE_PLANS.md`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/docs/FUTURE_PLANS.md).
  - Saved official **EdTech HLD/LLD Blueprint** ([DOCX](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/docs/blueprints/NeoNex_MindX_EdTech_HLD_LLD_Blueprint.docx) & [Markdown](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/docs/blueprints/NeoNex_MindX_EdTech_HLD_LLD_Blueprint.md)).
  - Saved official **IT Consultancy & Tech Services HLD/LLD Blueprint** ([DOCX](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/docs/blueprints/NeoNex_MindX_IT_Consultancy_HLD_LLD_Blueprint.docx) & [Markdown](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/docs/blueprints/NeoNex_MindX_IT_Consultancy_HLD_LLD_Blueprint.md)).

---

## 3. Pending Tasks & Future Roadmap (To Remind User)

### Phase 1: Social Media Full API Connections (When Ready)
- [ ] **LinkedIn Community Management API v2:**
  - Set up LinkedIn Developer App with `w_member_social` and `w_organization_social` OAuth scopes.
  - Automate publishing of technical project breakdowns, curriculum highlights, and placement success carousels.
  - Track referral conversions back to Admissions CRM.
- [ ] **YouTube Data API v3:**
  - Configure Google Cloud OAuth credentials and channel token.
  - Automate video upload metadata sync and ensure pinned comment UTM links point to syllabus downloads.
- [ ] **Meta Graph API (Instagram & Facebook):**
  - Connect Instagram Professional Account via Meta Business Manager.
  - Automate Reels and Carousel publishing for campus life, salary comparisons, and tech guides.
  - Set up Instagram Direct Message keyword automation (e.g. user comments "SYLLABUS", gets instant tracked download link).
- [ ] **WhatsApp Cloud Business API:**
  - Register Meta WhatsApp Business Account for NeoNeX MindX.
  - Implement automated instant lead alert notifications to counsellors (Mercy/Puneeth/Neeraj) on WhatsApp whenever a student submits a form.
  - Set up broadcast templates for webinar invitations and daily Python/SQL coding challenges.
- [ ] **X / Twitter API v2:**
  - Connect Developer Portal for automated tech thread scheduling and AI paper breakdowns.

---

### Phase 2: AI Automation, Voice Calling & Conversion Funnel
- [ ] **Website AI Conversational Chatbot Widget:**
  - Build and embed conversational assistant on `neonexmindx.com` for instant curriculum questions, fee plans, and lead capture.
  - Context-aware routing based on active course page with instant CRM lead logging.
- [ ] **Autonomous AI Voice Calling Agent:**
  - Connect inbound leads (`/api/webhook/meta`, `/api/webhook/google-ads`) to conversational voice agent (Deepgram STT + Gemma 2/Gemini + ElevenLabs TTS).
  - Screen candidate background and auto-book calendar demo with senior counselors for high-intent learners.
- [ ] **Multi-Channel Syllabus & Brochure Dispatch:**
  - WhatsApp Cloud API automated brochure delivery on form submission.
  - Instagram comment-to-DM keyword trigger for instant syllabus delivery.
  - Website 1-click trackable brochure PDF download with background lead capture.
- [ ] **Mobile Floating WhatsApp Sticky Trigger:**
  - Add an unobtrusive floating WhatsApp widget on mobile course pages for visitors dwelling >45 seconds on curriculum sections.
- [ ] **Exit-Intent Syllabus Download Modal:**
  - Implement non-intrusive desktop exit-intent trigger offering free "Bengaluru Data Analyst 2026 Roadmap PDF" in exchange for name + phone number.
- [ ] **Automated Email Follow-up Webhook:**
  - Connect `/api/submit-lead` to SendGrid or Resend API for instant automated student syllabus delivery via email.

---

### Phase 3: Content Cadence & SEO Authority Execution
- [ ] **Execute 7-Day Content Cadence:**
  - **Monday:** 1 Technical Project Deep-Dive (Python/SQL/Tableau).
  - **Wednesday:** 1 Student Career Pivot Case Study.
  - **Friday:** Bengaluru Tech Hiring Market Digest.
  - **Sunday:** Live Mentor AMA Webinar.
- [ ] **Content Repurposing Pipeline:**
  - Convert each new CMS technical blog post into:
    1. A 5-slide LinkedIn PDF document carousel.
    2. A 60-second YouTube Short showing code execution.
    3. A community challenge post in Discord / WhatsApp.
- [ ] **Search Engine Ping on Publish:**
  - Add Google Indexing API ping and Bing IndexNow API webhook in `/api/save-blogs` to notify crawlers within minutes of new blog releases.

---

### Phase 4: Ongoing Monitoring & Telemetry
- [ ] Maintain Mobile Performance Score >90 via PageSpeed Sentry in [`digital-marketing/index.html`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/digital-marketing/index.html).
- [ ] Monitor striking-distance keywords (ranks #3 to #10 in Google Search Console) to optimize meta titles and headers.
- [ ] Periodically backup [`data/crm_data.json`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/data/crm_data.json) and [`data/blogs.json`](file:///c:/Users/pcnee/Desktop/NeoNeX%20MindX%20website/deployment_NeoNex/data/blogs.json).
