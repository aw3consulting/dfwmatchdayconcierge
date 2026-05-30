# DFW AI-Assisted Intake and Command Hub Queue v1.0.0

## 1. Locked Determination

The DFW Matchday Concierge funnel is now inquiry-first.

The platform must begin by helping the visitor complete a structured concierge inquiry before presenting a final package, price, payment term, or activated personal command hub.

The AI-assisted intake layer is accepted as a major future operating layer, subject to authentication, security, claim governance, payment governance, and operator confirmation.

## 2. Core Operating Concept

Visitor flow:

1. Visitor selects lane or starts inquiry.
2. AI-assisted intake walks the visitor through structured questions.
3. Intake output generates a Personal VIP Matchday Command Hub preview.
4. Visitor reviews preview scope.
5. Visitor may pay an access fee to unlock or continue full hub activation.
6. Activated hub collects personal details, guest details, itinerary details, payment information, and service selections.
7. Operator reviews, scores, quotes, and confirms.
8. Final itinerary and payment terms are set.
9. Concierge services begin after confirmation.

## 3. Key Intake Variables Accepted

The AI-assisted intake must be able to ask for:

- VIP status, disclosed or non-disclosed
- sensitive status non-disclosure option
- arrival date
- departure date
- arriving airport, including private airports
- departing airport, including private airports
- hotel or housing location
- stay period by location
- obligation locations
- obligation dates
- stadium obligations
- practice facility obligations
- outings and personal stops
- matchday attendance
- sightseeing interest
- food interest
- snack interest
- beverage interest
- luggage coordination interest
- private security interest
- overall budget
- guest count
- guest details after hub activation
- payment information after hub activation

## 4. Security Gate Determination

An authentication/security layer is required before a visitor accesses the AI-assisted intake platform or personal command hub.

Required future control:

- email verification code and/or mobile verification code
- authenticated session
- secure intake continuation link
- limited access preview state
- protected full command hub state

No public build may expose personal command hub functionality without access control.

## 5. Monetization Determination

A Personal VIP Matchday Command Hub Preview may be monetized through an access fee.

Current concept:

- $100 preview/full-access fee under review
- fee may be credited toward package purchase
- referral credit may be considered
- goal is to increase serious inquiries, itinerary building, and driver/concierge recruitment signal

This fee is not final until payment governance and refund/credit terms are hardened.

## 6. Personal VIP Matchday Command Hub Concept

The personalized hub should be assembled from inquiry variables.

Potential hub widgets:

- Arrival plan
- Departure plan
- airport movement
- hotel / housing plan
- matchday attendance plan
- stadium route plan
- practice / obligation route plan
- sightseeing plan
- food / snack / beverage plan
- luggage coordination plan
- private security coordination request
- VIP driver / Tahoe profile
- guest detail collection
- payment status
- itinerary builder
- total price / payment terms
- operator confirmation status

Widgets should appear based on client inquiry, budget, availability, and operator confirmation status.

## 7. Controlled File Queue

Create the following governed files in this order:

### 1. `docs/dfw-ai-assisted-intake-governance-layer-v1.0.0.md`

Purpose:
Define the AI-assisted intake role, boundaries, allowed questions, restricted claims, operator-confirmed workflow, personalization logic, and non-disclosure handling.

### 2. `docs/dfw-secure-access-and-client-authentication-layer-v1.0.0.md`

Purpose:
Define email/mobile verification, authenticated intake access, protected command hub access, session limits, privacy handling, and launch-safe security requirements.

### 3. `docs/dfw-personal-vip-matchday-command-hub-governance-layer-v1.0.0.md`

Purpose:
Define the Personal VIP Matchday Command Hub, preview state, activated state, widget rules, guest detail entry, payment entry, itinerary builder, and operator confirmation logic.

### 4. `docs/dfw-command-hub-access-fee-and-credit-governance-layer-v1.0.0.md`

Purpose:
Define the proposed $100 access fee, forward credit, referral credit concept, refund/credit boundaries, payment timing, and claim control.

### 5. `docs/dfw-ai-intake-question-bank-v1.0.0.md`

Purpose:
Define the actual intake question sequence for VIP, Team Family, Media/Corporate, and Team Fan lanes, including conditional questions and sensitive-status non-disclosure options.

### 6. `docs/dfw-personalized-hub-widget-visibility-rules-v1.0.0.md`

Purpose:
Define which widgets appear based on inquiry data, budget, availability, lane, service window, privacy setting, and operator-confirmed scope.

### 7. `docs/dfw-inquiry-to-itinerary-pricing-and-confirmation-flow-v1.0.0.md`

Purpose:
Define the flow from inquiry to preview hub, activated hub, itinerary selection, total price, payment terms, deposit, confirmation, and service start.

### 8. `docs/dfw-vip-concierge-operator-standard-v1.0.0.md`

Purpose:
Define operator conduct, client interaction, airport protocol, stadium protocol, privacy protocol, family protocol, credential-aware protocol, and trip-value protection protocol.

## 8. Mockup Impact

The next visual mockup should not materially change its top-level concept, but it must support these new variables:

- inquiry-first CTA
- AI-assisted intake preview
- secure access gate
- Personal VIP Matchday Command Hub Preview
- activated command hub
- widget-based itinerary sections
- budget-aware concierge planning
- operator confirmation status
- payment/access fee state

## 9. Governance Boundary

AI may assist with intake and plan structuring, but it must not publicly guarantee:

- service acceptance
- VIP approval
- Tahoe availability
- driver assignment
- security availability
- credential validation
- event access
- final pricing before operator review
- payment confirmation before payment processor confirmation

All final acceptance, pricing, payment terms, assignment, and confirmation remain operator-controlled.
