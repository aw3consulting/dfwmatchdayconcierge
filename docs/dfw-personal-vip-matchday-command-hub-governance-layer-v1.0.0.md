# DFW Personal VIP Matchday Command Hub Governance Layer v1.0.0

## 1. Purpose

This file governs the Personal VIP Matchday Command Hub for DFW Matchday Concierge. It defines the hub product, access states, preview state, activated state, widget rules, itinerary builder, guest details, payment state, operator confirmation, security dependency, and public claim boundaries.

This layer translates the inquiry-first funnel into a personalized, secure, operator-reviewed concierge planning and execution surface.

## 2. Core Determination

The Personal VIP Matchday Command Hub is the primary client-facing product after verified AI-assisted intake.

It is not a public webpage. It is not a generic booking confirmation page. It is a private, secure, personalized matchday planning and concierge coordination surface.

The hub exists to organize the full value of the client's World Cup stay across arrival, departure, hotel/housing, matchday attendance, obligations, transportation, food, beverages, luggage, sightseeing, security interest, budget, itinerary, pricing, payment terms, and operator confirmation.

## 3. Required Access Sequence

The required sequence is:

1. Public inquiry entry
2. Email and/or mobile verification
3. AI-assisted intake
4. Personal Matchday Command Hub Preview
5. Operator review
6. Hub activation by approval, payment, planning deposit, or manual operator action
7. Activated Personal Matchday Command Hub
8. Itinerary selection and refinement
9. Pricing and payment terms
10. Final confirmation
11. Service execution and status tracking

The hub must not expose personal itinerary, guest, budget, payment, or sensitive status data before secure access.

## 4. Hub Access States

### 4.1 No Hub State

A public visitor has no hub.

They may view public pages and start an inquiry.

### 4.2 Verified Preview State

A verified inquiry visitor may access a limited Personal Matchday Command Hub Preview.

Preview may show:

- intake summary
- service categories identified
- trip planning gaps
- recommended next steps
- preliminary concierge plan sections
- operator review required status

Preview must not show:

- confirmed itinerary
- final price
- confirmed driver
- confirmed Tahoe
- confirmed security
- payment-confirmed status
- official credential/access claims

### 4.3 Activated Hub State

An activated client may access the full Personal VIP Matchday Command Hub.

Activated hub may include:

- personal details
- guest details
- itinerary builder
- service selections
- payment status
- operator messages or notes approved for client visibility
- booking statuses
- document/request checklist
- confirmed or pending services

### 4.4 Operator-Controlled State

Operator/admin may view the full operational record, including internal scoring, allocation, payment state, privacy flags, and assignment notes.

## 5. Hub Widgets

The Personal VIP Matchday Command Hub should be widget-based.

Core widgets:

1. Client Profile Widget
2. Guest Details Widget
3. Arrival Plan Widget
4. Departure Plan Widget
5. Airport Movement Widget
6. Hotel / Housing Widget
7. Matchday Attendance Widget
8. Obligation Locations Widget
9. Stadium / Practice / Outing Routes Widget
10. Sightseeing Interest Widget
11. Food / Snack / Beverage Widget
12. Luggage Coordination Widget
13. Private Security Interest Widget
14. VIP Driver / Tahoe Eligibility Widget
15. Budget and Planning Range Widget
16. Itinerary Builder Widget
17. Quote / Pricing Status Widget
18. Payment / Deposit Status Widget
19. Concierge Requests Widget
20. Operator Review Status Widget
21. Booking Status Tracker Widget

Widgets must appear based on inquiry data, access state, privacy setting, budget, availability, and operator confirmation state.

## 6. Widget Visibility Rules

### 6.1 Always Visible in Preview

- Intake summary
- missing information checklist
- recommended plan sections
- operator review required status
- next step to activate or continue

### 6.2 Conditional Preview Widgets

Visible only when relevant from intake:

- Arrival plan
- departure plan
- airport movement
- matchday attendance
- food / snack / beverage
- luggage coordination
- sightseeing
- security interest
- VIP/Tahoe eligibility note

### 6.3 Activated-Only Widgets

Visible only after hub activation:

- guest details
- payment status
- detailed itinerary builder
- quote terms
- operator communication history
- confirmed driver/vehicle details
- confirmed security coordination details if any
- final service status tracking

## 7. Itinerary Builder Governance

The itinerary builder may allow the client to organize:

- arrival movement
- hotel/housing transfer
- stadium movement
- matchday pickup/return
- practice or obligation routes
- food / snack / beverage stops
- luggage coordination
- sightseeing and free-time blocks
- departure movement

The itinerary builder must distinguish:

- requested
- under review
- quoted
- payment pending
- confirmed
- assigned
- completed
- declined/restricted

The itinerary builder may not imply that requested items are confirmed.

## 8. Guest Detail Governance

Guest details are activated-hub data and must remain protected.

Guest detail fields may include:

- guest first name
- guest last name
- role/context if voluntarily provided
- contact if needed
- luggage needs
- accessibility or comfort notes
- pickup/drop-off participation

Sensitive guest details must not appear in public static files or unsecured pages.

## 9. Payment and Pricing Governance

The hub may show pricing and payment status only after operator review.

Allowed states:

- quote pending
- quote sent
- planning deposit requested
- deposit paid
- balance pending
- paid in full
- add-on pending
- refund/credit review if applicable

The hub must not collect raw card information directly unless an approved compliant payment provider is implemented.

## 10. Planning Deposit / Access Fee Relationship

The hub may support a planning deposit or access fee concept, but the language must remain open until pricing governance is finalized.

Preferred working language:

`Concierge Planning Deposit`

instead of:

`Access Fee`

Reason:

The client is paying for planning, intake structuring, operator review, and command hub activation, not merely access to a page.

## 11. VIP Driver / Tahoe Widget

The VIP Driver / Tahoe widget must follow the VIP Driver and Vehicle Profile Layer.

Allowed preview language:

`VIP Tahoe eligibility is reviewed after intake and operator availability check.`

Allowed activated language after confirmation:

`VIP vehicle and driver details confirmed for your itinerary.`

Prohibited:

- Tahoe confirmed before operator assignment
- driver confirmed before operator assignment
- guaranteed availability
- official credentialed vehicle claim

## 12. Security and Privacy Governance

The hub must follow the Secure Access and Client Authentication Layer.

Required controls:

- verified access before preview
- protected activated hub
- no search indexing
- no guessable public URL
- no client data in public static files
- secure payment flow
- limited operator/admin access

## 13. AI Role Inside Hub

AI may assist with:

- summarizing intake
- identifying missing details
- suggesting itinerary categories
- drafting operator review summaries
- recommending questions
- creating preliminary plan structure

AI may not:

- confirm services
- confirm driver or vehicle
- set final price
- approve payment
- guarantee security
- validate credentials
- make official event/access claims

## 14. Operator Review Requirement

Every hub must display operator review state.

Operator review states:

- not submitted
- inquiry received
- intake incomplete
- under operator review
- quote pending
- quote sent
- awaiting payment/deposit
- confirmed
- restricted/declined

## 15. Public Website Impact

The public website should describe the hub as a secure, personalized planning surface.

Allowed public language:

`Complete a secure inquiry to generate your Personal Matchday Command Hub preview.`

`Your hub organizes arrival, hotel, matchday movement, food, luggage, sightseeing, security interest, budget, and concierge planning for operator review.`

Avoid:

- instant confirmed itinerary
- guaranteed VIP approval
- guaranteed Tahoe access
- guaranteed security
- guaranteed official access

## 16. Data Layer Impact

Future files should include:

- `data/hub-widgets.json`
- `data/hub-access-states.json`
- `data/hub-statuses.json`
- `data/hub-widget-rules.json`
- `data/itinerary-statuses.json`
- `data/hub-payment-statuses.json`

## 17. Final Determination

The Personal VIP Matchday Command Hub is accepted as the primary post-verification client product for DFW Matchday Concierge.

It has two client-facing states:

1. Verified Preview State
2. Activated Hub State

It is governed by secure access, AI-assisted intake, operator review, widget visibility, itinerary status control, payment governance, and strict claim boundaries.

The hub does not replace operator confirmation. It improves intake quality, planning quality, monetization, and client confidence before final booking confirmation.
