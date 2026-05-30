# DFW Command Hub Access Fee and Credit Governance Layer v1.0.0

## 1. Purpose

This file governs the commercial treatment of Personal Matchday Command Hub access, Concierge Planning Deposit language, activation fees, forward credit, referral credit, refund boundaries, payment authority, coordinator payment handling, and public claim control.

This layer must govern public copy, AI-assisted intake, Personal Matchday Command Hub activation, payment requests, and quote presentation before any fee or deposit is charged.

## 2. Core Determination

The preferred commercial framing is:

`Concierge Planning Deposit`

not:

`Access Fee`

The client is not paying merely to access a webpage. The client is paying to initiate structured concierge planning, AI-assisted intake, Personal Matchday Command Hub preparation, itinerary organization, and operator review.

## 3. Product Being Monetized

The planning deposit may cover:

- secure intake continuation
- AI-assisted concierge discovery
- Personal Matchday Command Hub Preview preparation
- operator review
- preliminary itinerary organization
- service-category mapping
- missing-detail review
- quote preparation pathway

The planning deposit does not automatically guarantee:

- VIP acceptance
- Tahoe availability
- driver assignment
- security availability
- final booking confirmation
- official credential or event access
- final pricing

## 4. Proposed Deposit Amount

Working concept:

`$100 Concierge Planning Deposit`

This amount remains under hardening review and must not be treated as final public pricing until approved for publication.

## 5. Deposit Application

The planning deposit may be applied as a forward credit toward a confirmed package purchase when:

- the client proceeds with an approved service package
- quote terms allow credit application
- payment is confirmed
- no restricted or declined request invalidates the inquiry

Recommended public framing:

`Your planning deposit may be credited toward your confirmed concierge package when your service is approved and booked.`

Avoid:

`Fully refundable access fee`

unless refund terms are separately finalized.

## 6. Referral Credit Concept

A referral credit may be considered when a paying planning-deposit client refers another client who activates a hub or confirms a package.

Referral credit may be structured as:

- forward credit toward package balance
- add-on credit
- future booking credit
- operator-approved discretionary credit

Referral credit must not be publicly promised until the referral policy is finalized.

## 7. Coordinator and Representative Payment Authority

Because many VIP, Team Family, Media, and Corporate bookings may be managed by coordinators, payment authority must be checked before charging or applying credit.

Potential payment actors:

- Principal Client
- Coordinator / Representative
- Executive assistant
- Travel manager
- Corporate payment contact
- Media coordinator
- Sponsor / hospitality contact
- Family coordinator
- Operator override

The system must record:

- payer name
- payer role
- payment authority type
- payment method
- payment timestamp
- credit eligibility
- quote or itinerary version tied to payment

## 8. Payment Authority Rules

A Coordinator may pay a planning deposit only when they select or are assigned one of these authority states:

- authorized to pay deposit
- authorized company payment contact
- authorized representative
- operator-approved payment authority

If payment authority is unclear, the inquiry may continue but hub activation, itinerary confirmation, or quote approval may remain pending.

## 9. Activation States

Command Hub commercial states:

1. No Hub
2. Verified Preview
3. Planning Deposit Requested
4. Planning Deposit Paid
5. Activated Hub
6. Quote Pending
7. Quote Sent
8. Booking Deposit Requested
9. Booking Deposit Paid
10. Confirmed Package
11. Balance Pending
12. Completed / Closed
13. Credit / Refund Review

## 10. Payment Flow

Recommended flow:

1. Visitor submits starter inquiry.
2. Visitor or coordinator verifies access.
3. AI-assisted intake creates review-ready inquiry.
4. Personal Matchday Command Hub Preview is generated.
5. Operator determines whether planning deposit is appropriate.
6. Planning deposit request is issued through approved payment method.
7. Payment is confirmed through provider or operator.
8. Hub is activated.
9. Itinerary and quote are refined.
10. Package deposit or balance is requested.
11. Service is confirmed after payment and operator acceptance.

## 11. Payment Methods

Potential methods:

- card payment link
- Zelle
- Cash App
- Venmo
- Revolut request by approval
- company card by approved processor
- invoice by approval

Raw card details must not be collected directly through the site or AI intake.

## 12. Refund and Credit Boundaries

Refund and credit handling depends on the stage of work completed.

Potential rules under review:

- If no operator review or planning work has started, refund may be available.
- If AI intake, hub preparation, or operator review has started, deposit may become non-refundable or partially creditable.
- If the request is declined due to DFW Matchday Concierge capacity, credit or refund review may be available.
- If the request is restricted due to prohibited service request, refund/credit may be limited.
- If the client proceeds to a package, deposit may be credited toward the confirmed service if allowed by quote.

Final refund language must be approved before public collection.

## 13. Declined / Restricted Request Handling

If a request involves prohibited or restricted claims, such as official ticket brokerage, credential validation, escrow, illegal alcohol handling, or guaranteed official access, the planning deposit should not be collected until operator review determines whether a lawful alternative request can be supported.

If a prohibited request is identified after deposit payment, operator must review refund/credit eligibility based on the final policy.

## 14. Public Copy Rules

Allowed public language:

- A Concierge Planning Deposit may be required to activate detailed planning.
- Your deposit may be credited toward an approved confirmed package.
- Final service acceptance, price, vehicle, driver, and payment terms require operator review.
- Coordinators and representatives may manage planning and payment when authorized.

Avoid:

- guaranteed refund
- guaranteed VIP approval
- guaranteed Tahoe availability
- guaranteed confirmed service after deposit
- access fee as the primary language
- final price before operator review

## 15. Data Layer Impact

Future data/config files should include:

- `data/planning-deposit-rules.json`
- `data/credit-rules.json`
- `data/referral-credit-rules.json`
- `data/hub-commercial-states.json`
- `data/payment-authority-rules.json`
- `data/refund-review-rules.json`

## 16. Final Determination

The Personal Matchday Command Hub commercial entry should be governed as a Concierge Planning Deposit, not a simple access fee.

The working amount of `$100` is accepted only as a concept under hardening review. It must be finalized through pricing, refund, credit, payment provider, and public copy review before publication.

The planning deposit may support AI-assisted intake, hub preview, operator review, itinerary structuring, and quote preparation, but it does not guarantee final booking, VIP approval, Tahoe availability, security, driver assignment, or official access.
