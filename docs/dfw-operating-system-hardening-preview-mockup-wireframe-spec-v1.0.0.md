# DFW Operating System Hardening Preview Mockup Wireframe Spec v1.0.0

## 1. Purpose

This file defines the mockup-ready wireframe specification for the DFW Matchday Concierge Operating System hardening preview.

It converts the approved UX blueprint, mockup plan, and mockup execution package into exact screen structures that may be used to create a visual mockup.

This is a documentation and mockup-specification artifact only.

## 2. Control Boundary

This file does not authorize:

- frontend implementation
- public deployment
- DreamHost production deployment
- public claim expansion
- fake official affiliation
- fake team logos
- fake tournament marks
- unsupported service claims
- live payment claims
- live dispatch claims
- live map routing claims

Frontend code changes remain blocked until the mockup is reviewed and accepted.

## 3. Governing Source Files

This wireframe spec is governed by:

1. `docs/dfw-operating-system-ux-blueprint-v1.0.0.md`
2. `docs/dfw-operating-system-hardening-preview-mockup-plan-v1.0.0.md`
3. `docs/dfw-operating-system-hardening-preview-mockup-execution-package-v1.0.0.md`

## 4. Wireframe System Principle

Every screen must answer four questions quickly:

1. Who is this visitor?
2. What matchday lane do they belong in?
3. What planning or service path should they enter?
4. What status boundary controls the next step?

The wireframes must move the visitor from public orientation into structured inquiry without implying confirmed service.

## 5. Frame 01: Desktop Homepage Funnel

### 5.1 Layout Structure

```text
[Sticky Header]
  [Approved Logo] [VIP] [Team Family] [Media / Corporate] [Fan Hubs] [Start Inquiry]

[Hero / Operating System Intro]
  Eyebrow: DFW World Cup Matchday Operating System
  H1: Welcome to Dallas/Fort Worth for matchday.
  Body: Choose your lane and build the command hub for your route, team, schedule, food, luggage, group, and concierge needs.
  Primary CTA: Start Inquiry
  Secondary CTA: Ask Concierge

[Four-Lane Selector]
  [VIP Guest Concierge] [Team Family Support] [Media / Corporate] [Team Fan Hubs]

[Fast Need Chips]
  Airport Arrival | Hotel to Stadium | Shared Ride | Food + Cooler | Luggage | Team Hub | VIP Review | Ask Concierge

[DFW Map / Location Preview]
  DFW Airport | Love Field | Dallas | Arlington Stadium | Fort Worth | Stockyards | FIFA Fan Experience

[Hub Preview Teaser]
  Public guidance -> Verified preview -> Activated command hub -> Quote -> Payment/deposit -> Confirmation

[Claim Badge Strip]
  Live Capability | Operator-Assisted | Development | Restricted | Referral / Third-Party | Operator Review Required

[Footer]
  Independent concierge planning and coordination service boundary
```

### 5.2 Acceptance Rules

- Four lanes must be visible without scrolling on desktop.
- `Start Inquiry` must be visible above the fold.
- The homepage must read as a planning operating system, not a transportation homepage.
- Tahoe may appear only in VIP context and only with confirmation boundary language.

## 6. Frame 02: Mobile Homepage Funnel

### 6.1 Layout Structure

```text
[Top Bar]
  [Logo] [Start Inquiry]

[Hero]
  DFW World Cup Matchday Operating System
  Welcome to Dallas/Fort Worth for matchday.
  [Start Inquiry]
  [Ask Concierge]

[Stacked Lane Cards]
  [VIP Guest Concierge]
  [Team Family Support]
  [Media / Corporate]
  [Team Fan Hubs]

[Need Chips]
  Airport | Stadium | Shared Ride | Food | Luggage | Team | VIP | Corporate

[Location Input]
  Where are you staying or arriving?

[Map Card]
  DFW geography preview

[Status Boundary]
  Operator review required before quote, payment, assignment, or confirmation.

[Footer Contact]
  Call | Text | Email | QR Destination
```

### 6.2 Acceptance Rules

- Inquiry start must be reachable within three taps.
- Mobile must avoid long explanatory copy before the first action.
- Lane cards must remain distinct and easy to tap.

## 7. Frame 03: Four-Lane Selector Detail

### 7.1 Layout Structure

```text
[Section Title]
Choose the matchday lane that best fits your trip.

[VIP Guest Concierge Card]
  Badge: Operator Review Required
  Copy: Private scheduled VIP planning with Black 2026 Chevrolet Tahoe eligibility for approved bookings.
  CTA: Request VIP Review
  Boundary: Tahoe and operator assignment require review, quote, payment/deposit approval, and availability confirmation.

[Team Family Support Card]
  Badge: Privacy-Sensitive
  Copy: Representative-friendly support for family, team-adjacent, or federation-linked planning.
  CTA: Request Private Support
  Boundary: No official team relationship, access, or credential validation is claimed.

[Media / Corporate Card]
  Badge: Quote Required
  Copy: Coordinator-led support for crews, sponsors, executives, groups, equipment, catering, and recurring schedules.
  CTA: Request Corporate Quote
  Boundary: Fleet, provider, invoice, and assignment availability require operator review.

[Team Fan Hubs Card]
  Badge: Free Guidance + Activated Planning
  Copy: Team, language, route, food, Fan Experience, shared ride, sightseeing, and activated planning support.
  CTA: Choose Team Hub
  Boundary: Shared ride matching and fulfillment are not guaranteed until confirmed.
```

## 8. Frame 04: AI Intake Starter

### 8.1 Layout Structure

```text
[AI Intake Header]
Build your matchday planning preview.

[Progress Indicator]
Lane -> Trip -> Needs -> Privacy -> Review

[Step 1: Lane]
  VIP Guest Concierge
  Team Family Support
  Media / Corporate
  Team Fan Hub
  Not Sure / Ask Concierge

[Step 2: Self or Coordinator]
  Myself
  I am a coordinator / representative
  I am organizing for a group

[Step 3: Trip Basics]
  Arrival date
  Departure date
  Airport or arrival point
  Hotel / stay area
  Matchday or team interest

[Step 4: Need Chips]
  Ride route
  Shared ride
  Food + drinks
  Cooler setup
  Luggage
  Catering
  Security coordination interest
  Sightseeing

[Step 5: Privacy]
  Standard coordination
  Privacy-sensitive
  Prefer to disclose details after verification
  Representative will provide details

[Step 6: Submit]
  Submit for operator review

[Disclaimer]
AI-assisted intake prepares a planning preview. Final availability, pricing, vehicle assignment, payment terms, and service confirmation require operator review.
```

### 8.2 Prohibited Visual States

- confirmed booking
- final price
- confirmed Tahoe
- confirmed driver
- confirmed security
- official access confirmation

## 9. Frame 05: Verified Hub Preview

### 9.1 Layout Structure

```text
[Secure Preview Header]
Personal Matchday Command Hub Preview
Badge: Secure Access / Operator Review Required

[Preview Summary]
  Lane selected
  Dates
  Arrival/departure
  Hotel/stay area
  Matchday interests
  Service categories

[Missing Details Checklist]
  Guest count
  Luggage details
  exact pickup point
  payment readiness
  privacy preference

[Recommended Widgets]
  Arrival Plan
  Matchday Movement
  Food + Cooler
  Luggage
  Route Map
  Quote Status

[Activation CTA]
  Activate Personal Matchday Command Hub

[Boundary]
Preview planning is not a confirmed booking. Final service acceptance, pricing, payment terms, vehicle assignment, and provider routing require operator review.
```

## 10. Frame 06: Activated Command Hub Dashboard

### 10.1 Layout Structure

```text
[Activated Hub Header]
Personal Matchday Command Hub
Badge: Activated Planning / Operator Review Required

[Status Tracker]
Inquiry Received -> Intake Complete -> Operator Review -> Quote Pending -> Payment Pending -> Confirmed -> Assigned -> Service or Referral

[Dashboard Grid]
  [Itinerary Builder]
  [Guest Details]
  [Arrival Plan]
  [Matchday Movement]
  [Food / Cooler / Essentials]
  [Luggage Coordination]
  [Quote Status]
  [Payment / Deposit Status]
  [Operator Next Steps]
  [Service or Referral Routing]

[Footer Boundary]
Activated planning does not equal confirmed service.
```

### 10.2 Acceptance Rules

- Status tracker must be visible near the top.
- Quote and payment status must remain separate.
- Requested items must not appear visually confirmed.

## 11. Frame 07: VIP Guest Concierge Hub

### 11.1 Layout Structure

```text
[Private VIP Header]
VIP Guest Concierge
Badge: Operator Review Required

[VIP Vehicle Panel]
Black 2026 Chevrolet Tahoe
Seats up to 7 passengers, subject to luggage and comfort review.
Badge: Subject to Confirmation

[VIP Planning Grid]
  [Arrival / Airport / FBO]
  [Hotel / Stay Plan]
  [Stadium / Matchday Movement]
  [Food / Drinks / Cooler]
  [Luggage]
  [Security Coordination Interest]
  [Privacy Preference]
  [Payment / Deposit Status]

[Operator Boundary]
VIP service is reviewed by request. Tahoe and operator assignment are confirmed only after operator review, quote, payment/deposit approval, and availability confirmation.
```

### 11.2 Acceptance Rules

- No ads.
- No guaranteed Tahoe language.
- No official access claim.
- No celebrity/team/federation implication.

## 12. Frame 08: Team Family Support Hub

### 12.1 Layout Structure

```text
[Privacy-Sensitive Header]
Team Family Support
Badge: Privacy-Sensitive / Operator Review Required

[Coordinator Panel]
  Hub owner
  principal client disclosure preference
  representative authority
  payment authority

[Family Planning Grid]
  [Airport / Hotel]
  [Stadium / Matchday]
  [Food / Grocery / Essentials]
  [Sightseeing]
  [Luggage]
  [VIP Escalation Review]
  [Operator Review]

[Boundary]
Team Family Support protects privacy and representative handling. DFW Matchday Concierge does not claim official team authorization, credential validation, or official access.
```

### 12.2 Acceptance Rules

- No ads.
- No forced public disclosure.
- Coordinator and principal client must be visually separate.

## 13. Frame 09: Media / Corporate Hub

### 13.1 Layout Structure

```text
[Hub Header]
Media / Corporate Matchday Command Hub
Badge: Quote Required

[Organization Intake]
  Organization
  contact name
  role type
  phone/email
  payment pathway preference

[Operations Builder]
  route schedule
  pickup/drop-off
  passenger count
  equipment/luggage count
  vehicle count request
  catering request
  recurring route request
  dedicated driver request

[Status Panels]
  Quote Status
  Payment Pathway
  Assignment Status
  Operator Notes

[Boundary]
Media / Corporate support is quote-required. Vehicle count, dispatch, catering, payment pathway, and provider assignment require operator confirmation.
```

### 13.2 Acceptance Rules

- Must feel operational and quote-ready.
- No ads.
- No guaranteed fleet or invoice approval claim.

## 14. Frame 10: Team Fan Hub

### 14.1 Layout Structure

```text
[Fan Hub Header]
Team Matchday Hub
Badge: Free Guidance + Activated Planning

[Team + Language]
  Select team
  Select language

[Matchday Cards]
  Match / stadium / date placeholder

[Fan Planning Grid]
  Route guidance
  Fan Experience
  Shared ride interest
  Food + drinks
  Cooler setup
  Stockyards / sightseeing
  Airport return

[Activation CTA]
Activate personalized planning

[Safe Monetization Zone]
Referral / affiliate / ad-supported fan guidance, clearly labeled.

[Boundary]
Free fan guidance supports planning. Activated planning unlocks personalized itinerary support and operator review. Fulfillment and shared ride matching are confirmed separately.
```

### 14.2 Acceptance Rules

- Ads allowed only in public/free fan context.
- Shared ride matching must remain non-guaranteed.
- VIP Tahoe must not appear as fan default.

## 15. Frame 11: DFW Map / Location Panel

### 15.1 Layout Structure

```text
[Map Header]
Understand the Dallas / Fort Worth matchday box.

[Map Nodes]
  DFW Airport
  Dallas Love Field
  Dallas
  Arlington Stadium
  Fort Worth
  Fort Worth Stockyards
  FIFA Fan Experience
  Hotel area
  Your location

[Route Lines]
  Airport -> Arlington
  Dallas -> Arlington
  Fort Worth -> Arlington
  Arlington -> Fan Experience
  Dallas -> Stockyards
  Stadium -> Airport

[CTA]
Build route plan

[Boundary]
Map visuals support planning orientation. Live routing, live traffic, and real-time dispatch require verified implementation before publication.
```

## 16. Frame 12: Status Badge System

### 16.1 Required Badge Display

```text
[Live Capability]
[Operator-Assisted]
[Development]
[Restricted]
[Referral / Third-Party]
[Information Only]
[Planning Value]
[Operator Review Required]
[Quote Required]
[Payment Pending]
[Confirmed]
```

### 16.2 Badge Rule

Every major service, route, hub, payment state, and referral zone must map to a badge.

No badge may visually imply confirmation before operator approval.

## 17. Frame 13: Fan Monetization Zone

### 17.1 Layout Structure

```text
[Public Fan Guidance Zone]
  Food recommendation cards
  attraction cards
  route provider cards
  official-source guidance cards
  ad or sponsored placement placeholder where approved

[Disclosure Labels]
  Information Only
  Third-Party Referral
  Affiliate / Referral Link
  Operator-Assisted
```

### 17.2 Blocked Contexts

Do not place this zone inside:

- VIP hub
- Team Family hub
- private Media / Corporate hub
- privacy-sensitive activated hub
- paid premium hub without explicit curated approval

## 18. Frame 14: Mobile Activated Command Hub

### 18.1 Layout Structure

```text
[Mobile Header]
Personal Matchday Command Hub
[Status Chip]

[Status Tracker]
Horizontal scroll or stacked steps

[Primary Cards]
  Next Step
  Itinerary
  Quote Status
  Payment / Deposit
  Route Plan
  Food / Luggage
  Operator Review

[Bottom Action Bar]
  Ask Concierge | Add Detail | View Status
```

### 18.2 Acceptance Rules

- Status must be visible before detailed content.
- Payment and confirmation must remain separate.
- No mobile frame should hide operator review language.

## 19. Global Footer Requirement

Every public or preview frame must include an independent-service boundary in some form.

Approved footer boundary:

`DFW Matchday Concierge is an independent concierge planning and coordination service. Final availability, pricing, payment terms, vehicle assignment, third-party provider routing, and service confirmation require operator review.`

## 20. Final Mockup Acceptance Criteria

The mockup passes if:

- four lanes are distinct
- inquiry is visually primary
- operator review is visible
- AI intake is planning-only
- hub activation is planning, not service confirmation
- VIP and Team Family are privacy-protected
- Media / Corporate is quote-ready
- fan hubs scale through free guidance and activated planning
- ad/referral zones are properly restricted
- Tahoe is governed and not guaranteed
- no fake official affiliation appears
- no unsupported fulfillment claim appears
- mobile path reaches inquiry quickly

## 21. Final Determination

This wireframe spec is accepted as the mockup-ready structure for the next visual design action.

The next controlled action is to create the hardening-preview visual mockup artifact using this wireframe spec.

Frontend implementation remains blocked until the visual mockup is reviewed and accepted.
