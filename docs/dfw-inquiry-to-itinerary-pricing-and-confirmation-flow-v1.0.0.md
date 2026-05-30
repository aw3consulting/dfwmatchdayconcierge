# DFW Inquiry to Itinerary Pricing and Confirmation Flow v1.0.0

## 1. Purpose

This file governs the commercial flow from public inquiry to AI-assisted intake, Personal Matchday Command Hub Preview, activated hub, itinerary development, pricing, payment terms, confirmation, and service execution.

This layer ensures that DFW Matchday Concierge can monetize planning, protect scarce VIP resources, preserve operator control, and avoid unsupported booking claims.

## 2. Core Flow

The governed flow is:

1. Public inquiry
2. Secure verification
3. AI-assisted intake
4. Personal Matchday Command Hub Preview
5. Operator review
6. Planning deposit or activation decision
7. Activated Personal Matchday Command Hub
8. Itinerary refinement
9. Quote and pricing terms
10. Payment/deposit request
11. Confirmation
12. Assignment
13. Service execution
14. Closeout

## 3. Public Inquiry State

The public inquiry state captures only non-sensitive starter information.

Allowed fields:

- name
- email
- mobile
- preferred contact method
- lane interest
- general trip dates
- general support need

Public inquiry must not collect raw payment card data, detailed VIP identity, sensitive Team Family details, exact private location data, or private guest lists.

## 4. Secure Verification State

Before sensitive intake or hub access, the visitor must verify access through the secure access layer.

Verification may include:

- email code
- mobile code
- secure magic link
- operator-issued access link

After verification, the inquiry receives a secure inquiry ID.

## 5. AI-Assisted Intake State

AI intake collects structured details required to build a plan.

Primary outputs:

- trip summary
- service window
- arrival/departure details
- stay locations
- matchday attendance
- obligations
- transportation needs
- food/beverage needs
- luggage needs
- security interest
- guest structure
- budget range
- privacy setting
- missing details
- recommended widgets

AI output remains preliminary and subject to operator review.

## 6. Personal Matchday Command Hub Preview

The preview is a verified, limited-access planning surface.

Preview may show:

- intake summary
- missing detail checklist
- recommended plan sections
- suggested service categories
- preliminary itinerary outline
- operator review required status
- activation path

Preview must not show:

- confirmed services
- final price
- confirmed Tahoe
- confirmed driver
- confirmed security
- official access claims
- payment-confirmed status

## 7. Operator Review State

Operator review determines whether the inquiry is:

- accepted for planning
- routed to VIP review
- routed to Team Family Support
- routed to Media / Corporate
- routed to Team Fan / pool driver
- waitlisted
- downgraded
- restricted / declined

Operator review should consider:

- scoring engine output
- capacity
- Tahoe availability
- primary operator availability
- driver pool availability
- privacy requirements
- security coordination feasibility
- payment readiness
- timing risk

## 8. Planning Deposit / Activation Decision

A Personal Matchday Command Hub may be activated through:

- planning deposit
- approved VIP operator activation
- Media / Corporate account approval
- Team Family privacy approval
- manual operator override

Preferred language:

`Concierge Planning Deposit`

Avoid:

`Access fee`

unless pricing governance later confirms that language.

A planning deposit may be credited toward confirmed package purchase if approved by final pricing governance.

## 9. Activated Hub State

The activated hub may allow the client to:

- complete personal details
- add guest details
- refine itinerary
- select service categories
- request quote items
- view payment/deposit status
- view operator-reviewed next steps
- track booking statuses

Activated hub does not equal confirmed service.

## 10. Itinerary Refinement State

Itinerary items must be status-controlled.

Allowed item statuses:

- requested
- missing details
- under review
- quoted
- payment pending
- confirmed
- assigned
- active
- completed
- declined / restricted

No itinerary item should visually appear confirmed until operator confirmation and payment/deposit requirements are satisfied.

## 11. Pricing State

Pricing may be generated only after operator review.

Pricing may include:

- planning deposit
- VIP concierge block
- multi-day support
- weekly support
- private transportation
- shared/pool-driver transportation
- food/snack/beverage support
- cooler setup
- luggage coordination
- catering
- security coordination request
- sightseeing route
- driver block
- add-ons

Pricing must distinguish:

- estimate
- quote
- confirmed price
- reimbursable expenses
- non-refundable purchases
- deposit
- balance

## 12. Payment State

Allowed payment statuses:

- payment not requested
- planning deposit requested
- planning deposit paid
- booking deposit requested
- booking deposit paid
- balance pending
- paid in full
- add-on payment pending
- refund/credit review

Payment must be processed through approved payment channels. Raw card details must not be collected directly through the site or AI intake.

## 13. Confirmation State

A service becomes confirmed only when:

- operator has accepted the booking
- itinerary scope is agreed
- price/payment terms are issued
- required deposit or payment is received
- assignment or fulfillment path is feasible
- claim restrictions are satisfied

Confirmation must identify:

- confirmed service window
- confirmed itinerary items
- payment status
- vehicle/driver assignment if applicable
- cancellation/refund terms
- operator contact method

## 14. Assignment State

Assignment may include:

- VIP operator
- Tahoe allocation
- trusted driver
- pool driver
- delivery support
- catering support
- security coordination contact if approved

Assignment must not be displayed before it is actually made.

## 15. Service Execution State

Execution statuses:

- scheduled
- preparing
- driver assigned
- en route
- arrived
- active
- return scheduled
- completed
- issue review
- closed

No live tracking claim may appear unless live tracking is implemented.

## 16. Closeout State

Closeout may include:

- completed services
- final balance
- add-on reconciliation
- refund/credit review
- referral credit review
- future booking opportunity
- testimonial request if appropriate

## 17. Claim Boundaries

Allowed public language:

- Complete a secure inquiry.
- Build a Personal Matchday Command Hub Preview.
- Operator review is required before pricing and confirmation.
- Planning deposit may be required to activate detailed planning.
- Final services are confirmed after quote and payment/deposit approval.

Prohibited language:

- instant confirmed VIP booking
- guaranteed Tahoe
- guaranteed driver
- guaranteed security
- guaranteed official access
- final price before operator review
- payment confirmation before processor confirmation

## 18. Final Determination

The governed commercial sequence is inquiry-first, verification-gated, AI-assisted, hub-centered, operator-reviewed, quote-controlled, payment-confirmed, and status-tracked.

This flow must govern future UI, forms, AI intake, command hub design, payment policy, and frontend implementation.
