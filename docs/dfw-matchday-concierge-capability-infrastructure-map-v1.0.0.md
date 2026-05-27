# DFW Matchday Concierge Capability and Infrastructure Map v1.0.0

## 1. Purpose

This file defines the missing capability layer for the DFW Matchday Concierge Digital Command Platform.

No public claim may appear on the website unless the claim is mapped to a current, assisted, or future capability with a clear infrastructure basis.

The site is not a generic transportation website. It is a premium Dallas matchday trip-value platform that must support a $600 to $2,000+ service expectation through operational capability, not cosmetic language.

## 2. Governing Principle

Every claim must pass the capability test.

A claim is allowed only when one of the following statuses applies:

1. Live Capability - the function works on the live site or through the active operator workflow.
2. Operator-Assisted Capability - the function is fulfilled manually by DFW Matchday Concierge after inquiry or direct contact.
3. Development Capability - the function is planned and architecturally supported, but must not be marketed as live.
4. Restricted Capability - the function is useful but requires legal, payment, data, ticketing, safety, insurance, or partner validation before public activation.

## 3. Platform Layers

### Layer 1: Public UI and Conversion Layer

Purpose: present a Fortune 100 quality front end that sells trip-value protection and captures high-intent leads.

Required capabilities:
- Premium homepage
- Connect page for QR traffic
- Booking and inquiry page
- Dallas Matchday Hub
- Match pages
- Team fan pages
- Group and scores pages
- Ticket coordination page
- Language routing pages
- Mobile-first experience
- Strong call, SMS, WhatsApp, and email actions

Infrastructure:
- HTML
- CSS
- JavaScript
- Static assets
- DreamHost production hosting
- GitHub source control

### Layer 2: Service Capability Layer

Purpose: map service claims to fulfillment actions.

Capabilities:
- Private transportation
- Airport transfers
- Hotel transfer coordination
- Stadium arrival planning
- Post-match pickup planning
- Return-to-hotel or return-to-airport planning
- Group and VIP transportation
- Luggage coordination
- Food pickup coordination
- Snacks, water, cooler, and convenience item preparation
- Drinks coordination where lawful and controlled
- Multi-stop itinerary planning
- Fan language support
- Team and match-specific guidance

Infrastructure:
- Service pages
- Inquiry form
- WhatsApp/SMS action links
- Operator workflow checklist
- Service menu data file
- Match data file
- Manual fulfillment workflow

### Layer 3: Matchday Intelligence Layer

Purpose: make the site valuable to football fans and premium travelers beyond transportation.

Capabilities:
- Dallas match calendar
- Dallas group-stage pages
- Dallas knockout watch
- Group pages
- Team pages
- Advancement watch
- Scores and updates page
- Fan guidance by team
- Match-specific CTAs

Infrastructure:
- Static match data file
- Static group data file
- Static team data file
- Manual score update process for launch
- Future sports data API integration after provider selection and cost validation

### Layer 4: Fan Utility Layer

Purpose: support practical fan needs while controlling liability.

Capabilities:
- Extra ticket post intake
- Ticket needed post intake
- Safe handoff coordination inquiry
- Official ticket channel guidance
- Delivery coordination inquiry

Restricted claims:
- No ticket brokerage claim
- No resale marketplace claim
- No ticket authentication guarantee
- No escrow claim
- No guarantee of ticket validity
- No claim of official tournament affiliation

Infrastructure:
- Ticket coordination page
- Intake form
- Manual moderation
- Liability disclaimer
- Official-channel language
- Operator approval before any ticket-related service is accepted

### Layer 5: Multilingual Layer

Purpose: make the platform useful to international fans attending Dallas matches.

Initial language routes:
- English
- Spanish
- Japanese
- Dutch
- German
- Swedish
- Croatian
- Arabic

Capabilities:
- Language-specific connect page
- Language-specific match summary
- Language-specific service explanation
- Language-specific call-to-action

Infrastructure:
- Static language pages for launch
- Human-audited copy before public use
- Future AI-assisted translation draft workflow with human review before publishing

### Layer 6: Operations and Automation Layer

Purpose: reduce operator friction and prevent unsupported claims.

Required scripts and automations:
- Build script for static site generation
- Sitemap generator
- Link checker
- Claim-to-capability validator
- Match page generator
- Team page generator
- Group page generator
- QR destination validator
- Form submission logger or email routing script
- Deployment package builder for DreamHost

Launch stack:
- Static HTML/CSS/JS
- JSON data files
- Node.js or Python local build scripts
- DreamHost static hosting
- GitHub source control

Future stack:
- DreamHost PHP form endpoint or serverless form handler
- Data update admin page
- Sports data API
- AI-assisted content drafting
- Moderation queue for fan posts
- Optional CRM or Google Sheets lead capture
- Optional payment links or deposit request system

## 4. Claim-to-Capability Map

| Website Claim | Required Capability | Launch Status | Infrastructure Basis | Public Use Rule |
|---|---|---:|---|---|
| Private transportation | Direct booking and operator fulfillment | Live Capability | Call, SMS, WhatsApp, inquiry form | Allowed |
| Airport transfers | Airport pickup and drop-off planning | Live Capability | Airport service page and inquiry form | Allowed |
| Matchday logistics | Stadium arrival and exit planning | Operator-Assisted Capability | Match inquiry workflow | Allowed with direct coordination language |
| Concierge hospitality | Food, snacks, water, comfort, stop, and preparation support | Operator-Assisted Capability | Service menu and inquiry form | Allowed as custom coordination |
| Luggage coordination | Luggage count, loading, timing, and hotel support planning | Operator-Assisted Capability | Luggage service page and inquiry workflow | Allowed |
| Group and VIP transportation | Group movement planning and direct coordination | Operator-Assisted Capability | Group service page and inquiry form | Allowed |
| World Cup scores and updates | Score data and update workflow | Development Capability | Manual score page first, API later | Do not market as live scores until operational |
| Advancement watch | Group and knockout scenario tracking | Development Capability | Manual data model first | Use as editorial intelligence until automated |
| Team fan pages | Team-specific service and language pages | Development Capability | Static page generator and content files | Allowed after pages are published |
| Multilingual support | Language-specific service pages | Development Capability | Static translated pages with human review | Do not claim full support until language pages are live |
| Extra ticket posts | Fan post intake and moderation | Restricted Capability | Ticket page and manual review | Use controlled intake only |
| Ticket delivery coordination | Lawful handoff support with disclaimers | Restricted Capability | Manual operator approval | No guarantee, brokerage, resale, or authentication claims |
| Ticket validation | Verified ticket authentication method | Restricted Capability | Requires official process or validated third-party method | Do not claim until verified |
| Payment or deposit | Payment link or checkout process | Development Capability | Future payment provider | Do not claim until active |
| AI concierge | AI-assisted drafting or service routing | Development Capability | Future AI workflow | Do not claim public AI concierge until live and tested |

## 5. Pure Infrastructure Layer

### Production Hosting

DreamHost is the production host for the premium website experience.

Responsibilities:
- Public website hosting
- SSL certificate
- Domain routing
- Email preservation
- Static file delivery
- Optional PHP form handling

### Source Control

GitHub repository:
- aw3consulting/dfwmatchdayconcierge

Responsibilities:
- Source control
- Version history
- Preview branch or staging workflow
- Deployment package source
- Website file archive

### Build System

Initial build:
- Hand-authored static HTML/CSS/JS

Scale build:
- Structured static generator using JSON data files
- Node.js or Python build scripts

Required data files:
- data/site.json
- data/services.json
- data/matches.json
- data/teams.json
- data/groups.json
- data/languages.json
- data/claims.json
- data/ticket-rules.json

Required scripts:
- scripts/build-site
- scripts/generate-sitemap
- scripts/check-links
- scripts/validate-claims
- scripts/generate-match-pages
- scripts/generate-team-pages
- scripts/package-dreamhost-deploy

### Contact and Lead Handling

Phase 1:
- Direct call
- SMS
- WhatsApp
- Mailto inquiry form

Phase 2:
- DreamHost PHP endpoint
- Email routing to concierge@dfwmatchdayconcierge.com
- Spam control
- Structured lead template

Phase 3:
- Lead log
- CRM or spreadsheet capture
- Booking status field
- Service request classification

### Sports and Score Data

Phase 1:
- Manual score updates
- Static standings pages
- Editorial advancement watch

Phase 2:
- Approved sports data provider
- Scheduled data pull
- Data normalization script
- Static rebuild and redeploy

Phase 3:
- Live update layer
- API cache
- Admin update dashboard

### AI Layer

AI may support internal execution, but public claims must stay controlled.

Allowed internal use:
- Draft multilingual content
- Draft fan guidance
- Draft matchday updates
- Draft service responses
- Classify inquiries
- Generate operator checklists

Public activation requires:
- human review
- safety controls
- liability review
- no unsupported claims

## 6. Deployment Framework

### Development

Work happens in GitHub first.

### Review

Preview can happen through GitHub Pages or local static preview.

### Production

Production files deploy to DreamHost.

### DreamHost Package

Required deploy package:
- index.html
- connect/index.html
- contact/index.html
- service pages
- match pages
- team pages
- group pages
- language pages
- assets/site.css
- assets/site.js
- assets/logo files
- robots.txt
- sitemap.xml

### Production Gate

Before public launch:
- all links pass
- mobile review passes
- QR destination opens
- contact links work
- service pages exist
- unsupported claims removed
- DreamHost SSL active
- email records preserved

## 7. Immediate Build Order

1. Replace current homepage with Trip-Value Protection homepage.
2. Replace connect page with premium command page.
3. Build Dallas Matchday Hub.
4. Build match pages for Dallas fixtures.
5. Build team pages for Dallas teams.
6. Build groups and advancement watch.
7. Build ticket coordination intake with legal boundaries.
8. Build multilingual starter pages.
9. Add JSON data layer.
10. Add scripts for sitemap, claim validation, page generation, and DreamHost package build.

## 8. Final Operating Rule

The website may only claim what the platform can support through one of three channels:

1. live website functionality,
2. direct operator-assisted workflow,
3. clearly labeled future capability.

Any claim outside those channels must be removed before DreamHost production deployment.
