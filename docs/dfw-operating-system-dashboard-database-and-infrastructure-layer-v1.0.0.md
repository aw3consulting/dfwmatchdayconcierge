# DFW Operating System Dashboard, Database, and Infrastructure Layer v1.0.0

## 1. Purpose

This file closes the full-scope audit gap for dashboards, databases, records, CRM, DreamHost, GitHub Pages, GitHub source control, and Oracle OCI.

## 2. Dashboard Architecture

### Client / Coordinator Dashboards

Required dashboard concepts:

- Personal Matchday Command Hub
- VIP Guest Command Hub
- Team Family Support Command Hub
- Media / Corporate Command Hub
- Team Fan Hub
- Fulfillment Request Profile

### Supply-Side Dashboards

Required dashboard concepts:

- Personal Driver Command Hub
- Driver Matchday Page
- Concierge Operations Command Hub

### Internal Operator Dashboards

Required operator dashboards:

- inquiry queue
- quote queue
- payment/deposit status board
- driver readiness board
- concierge readiness board
- fulfillment queue
- escalation board
- closeout board
- monetization dashboard
- referral/affiliate/ad dashboard
- marketing dashboard
- SEO dashboard
- 24-hour launch readiness dashboard

## 3. Minimum Manual Tracker Model

Immediate launch may use a manual tracker.

Required fields:

- inquiry ID
- lane
- lead source / QR / referral
- client or coordinator name
- phone
- email
- preferred contact method
- matchday / event
- arrival date
- departure date
- airport
- hotel / stay area
- group size
- luggage count
- service needs
- budget / payment readiness
- quote status
- deposit status
- confirmation status
- driver status
- concierge status
- fulfillment path
- escalation status
- closeout status
- privacy flag
- monetization source
- follow-up date
- operator owner
- notes

Private client, driver, concierge, payment, and sensitive data must not be stored in public GitHub files.

## 4. Data Separation

Data categories:

- public static site data
- private inquiry data
- driver candidate data
- concierge candidate data
- payment status data
- fulfillment data
- analytics data
- referral/ad data

Public GitHub may store only public static site data and governed templates.

## 5. Infrastructure Roles

### GitHub

- source of truth
- PR control
- governance record storage
- static source files
- workflow checks

### GitHub Pages

- temporary preview surface only
- user review route
- not final production authority

### DreamHost

- immediate static production host target
- final domain target
- fastest candidate for 24-hour production launch after approval

### Oracle OCI

Oracle OCI is the future or parallel controlled infrastructure path for:

- backend intake database
- secure command center application
- private dashboards
- AI automation backend
- API layer
- dispatch/routing logic
- analytics and reporting
- operator control tools

OCI is not required for static 24-hour launch, but it must remain in the infrastructure roadmap.

## 6. Launch Infrastructure Decision

Immediate launch candidate:

`DreamHost static production deployment after approval`

Preview candidate:

`GitHub Pages only`

Future controlled backend candidate:

`Oracle OCI`

## 7. Current Status

Dashboard and database architecture are now defined for launch planning.

Implementation remains blocked until manual tracker, dashboard shell, and production deployment package are reviewed.
