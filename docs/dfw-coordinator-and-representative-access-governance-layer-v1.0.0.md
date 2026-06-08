# DFW Coordinator and Representative Access Governance Layer v1.0.0

## 1. Purpose

This file governs coordinator and representative access for DFW Matchday Concierge. It defines how a person acting on behalf of a VIP, Team Family, Media, Corporate, or Fan client may initiate inquiry, complete AI-assisted intake, access a Personal Matchday Command Hub, submit itinerary information, coordinate payment, and manage booking details.

This layer must govern access-fee, planning-deposit, payment, hub-activation, privacy, and confirmation workflows before those workflows are finalized.

## 2. Core Determination

The person booking the matchday experience may not be the person receiving the service.

The platform must distinguish between:

- Principal Client
- Coordinator / Representative
- Guest
- Operator
- Driver / Fulfillment Support

Coordinator access is not a separate customer tier. It is an authority and access model that can apply across VIP Guest Concierge, Team Family Support, Media / Corporate, and Team Fan Hub workflows.

## 3. Role Definitions

### 3.1 Principal Client

The Principal Client is the person, family, organization, executive, media party, corporate group, or fan party receiving the core service.

The Principal Client may be anonymous or non-disclosed in public-facing workflows when privacy-sensitive handling is requested.

### 3.2 Coordinator / Representative

A Coordinator / Representative is an authorized person acting on behalf of the Principal Client.

Coordinator types may include:

- executive assistant
- personal assistant
- family coordinator
- travel manager
- media coordinator
- corporate coordinator
- sponsor / hospitality coordinator
- team or federation representative
- event operations contact
- parent / guardian
- fan group organizer

### 3.3 Guest

A Guest is a person included in the itinerary, movement plan, concierge plan, or service schedule.

A Guest may have limited visibility, no hub access, or specific itinerary visibility depending on authorization.

### 3.4 Operator

The Operator is DFW Matchday Concierge or an authorized internal user controlling review, quote, pricing, assignment, confirmation, and fulfillment decisions.

### 3.5 Driver / Fulfillment Support

Driver / Fulfillment Support may receive only the information necessary to complete assigned service safely and professionally.

Driver / Fulfillment Support must not receive unnecessary VIP identity, sensitive status, budget, payment, or private guest details.

## 4. Coordinator Access Lane

Public intake must support a Coordinator / Representative entry path.

Recommended public question:

`Are you completing this inquiry for yourself or on behalf of someone else?`

Options:

- Myself
- VIP guest
- Team Family member
- Executive / corporate client
- Media group
- Sponsor / hospitality guest
- Family or guest group
- Fan group
- Other

If the user selects an on-behalf-of option, the platform must collect coordinator details and principal/client context separately.

## 5. Required Coordinator Fields

Coordinator fields:

- coordinator first name
- coordinator last name
- organization or relationship if applicable
- email
- mobile phone
- preferred contact method
- role type
- authority type
- time zone
- notes

Principal/client context fields:

- principal/client first name if disclosed
- principal/client last name if disclosed
- principal/client lane
- privacy preference
- sensitive status disclosure preference
- guest count
- service window
- trip context

## 6. Authority Types

Coordinator authority must be classified.

Authority types:

1. Inquiry Only
2. Intake Completion
3. Itinerary Management
4. Payment Coordination
5. Booking Confirmation
6. Full Representative Authority
7. Operator-Verified Authority

### 6.1 Inquiry Only

May submit starter inquiry but may not activate hub, confirm itinerary, or approve payment.

### 6.2 Intake Completion

May complete AI-assisted intake and provide trip details.

### 6.3 Itinerary Management

May add or edit itinerary details, obligations, guests, food, luggage, and service requests.

### 6.4 Payment Coordination

May receive payment links, coordinate payment, or submit company/payment-contact details.

### 6.5 Booking Confirmation

May approve final service scope after operator quote, if authority is accepted.

### 6.6 Full Representative Authority

May act as the primary hub user for the Principal Client.

### 6.7 Operator-Verified Authority

Authority confirmed by direct operator review or known relationship.

## 7. Hub Owner vs Principal Client

The Hub Owner may be the Coordinator, while the Principal Client receives the service.

The hub must support:

- hub owner contact
- principal client profile
- guest profiles
- privacy settings
- authority level
- payment authority
- itinerary authority

This prevents incorrect assumptions that the login user is always the VIP, player family member, executive, media guest, or traveler.

## 8. Access Controls

Coordinator access must follow the Secure Access and Client Authentication Layer.

Minimum requirements:

- coordinator verification by email or mobile
- secure hub link or authenticated session
- access state assignment
- authority level recorded
- operator review before sensitive access expansion

Coordinator access may be revoked, restricted, or downgraded by the operator.

## 9. Privacy and Non-Disclosure Controls

A Coordinator may submit an inquiry without disclosing sensitive principal identity.

Allowed sensitive-status options:

- principal identity disclosed now
- principal identity disclosed after verification
- principal identity disclosed only to operator
- principal identity withheld until direct contact
- representative authorized to discuss details

Public workflow must not force disclosure of celebrity, player, credential, family, sponsor, or federation relationship before secure access and operator review.

## 10. Payment Authority

Payment authority must be separate from itinerary authority.

A Coordinator may:

- request a quote
- receive a payment link
- coordinate company-card payment
- request invoice approval
- pay planning deposit if authorized

A Coordinator must not be assumed to have payment authority unless selected, declared, or operator-approved.

Payment authority options:

- no payment authority
- payment contact only
- authorized to pay deposit
- authorized to approve quote
- authorized company payment contact
- operator-approved payment authority

## 11. Confirmation Authority

Booking confirmation must identify who approved the service.

Approval may come from:

- Principal Client
- Coordinator / Representative
- Corporate payment authority
- Media coordinator
- Team/family representative
- Operator override

The system should record:

- approver name
- authority type
- confirmation timestamp
- payment status
- itinerary version approved

## 12. Visibility Rules

### 12.1 Coordinator Visible

A Coordinator may see:

- intake questions
- trip summary
- itinerary builder if authorized
- missing information checklist
- quote/payment status if authorized
- booking statuses relevant to coordination

### 12.2 Coordinator Restricted

A Coordinator may be restricted from seeing:

- principal private notes
- sensitive identity details
- guest private data
- payment details beyond status
- operator internal scoring
- driver internal notes

### 12.3 Driver / Fulfillment Visible

Drivers and fulfillment support may see only:

- assigned task
- pickup/drop-off
- timing
- passenger count
- luggage/equipment notes
- client-facing name or booking code
- safety-relevant notes

They must not see unnecessary sensitive identity, budget, or payment information.

## 13. Lane-Specific Coordinator Rules

### 13.1 VIP Guest Concierge

Coordinator likely roles:

- executive assistant
- personal assistant
- private travel manager
- sponsor/hospitality representative

VIP coordinator access requires privacy-sensitive handling and operator review before full hub activation.

### 13.2 Team Family Support

Coordinator likely roles:

- family coordinator
- team/federation representative
- assistant
- parent/guardian

Team Family coordinator access should allow non-disclosure and protected identity handling.

### 13.3 Media / Corporate

Coordinator likely roles:

- production coordinator
- travel coordinator
- corporate assistant
- sponsor event contact
- hospitality coordinator

Media / Corporate coordinator access may include group movement, catering, recurring schedules, equipment, and company-card or invoice coordination.

### 13.4 Team Fan Hub

Coordinator likely roles:

- fan group organizer
- family group lead
- small group travel lead

Fan coordinators may manage shared rides, group routes, food packages, and Fan Experience plans, but they do not receive VIP/Tahoe authority unless escalated and approved.

## 14. Access Revocation

Coordinator access may be revoked when:

- authority is disputed
- payment authority is unclear
- privacy risk exists
- principal client requests restriction
- abusive or unsafe behavior occurs
- duplicate or conflicting coordinators exist
- operator determines access should be limited

## 15. Conflict Handling

When multiple coordinators exist, operator must establish a primary coordinator.

Potential hierarchy:

1. Principal Client instruction
2. Verified representative authority
3. Payment authority
4. Organization/family authority
5. Earliest verified inquiry only as temporary default

## 16. Public Copy Rules

Allowed public language:

- Completing this for someone else? Start as a Coordinator or Representative.
- Coordinators may complete intake, organize trip details, and request operator review.
- Principal and guest details can remain protected until verified or operator-reviewed.
- Payment and confirmation authority are reviewed before booking is confirmed.

Avoid:

- guaranteed authority acceptance
- automatic booking authority
- public proof requirement
- official team/federation authorization claims
- payment approval without operator/payment confirmation

## 17. Data Layer Impact

Future data/config files should include:

- `data/client-roles.json`
- `data/coordinator-authority-types.json`
- `data/hub-access-roles.json`
- `data/payment-authority-rules.json`
- `data/confirmation-authority-rules.json`

## 18. Final Determination

Coordinator / Representative Access is accepted as a cross-lane access model applying to VIP Guest Concierge, Team Family Support, Media / Corporate, and Team Fan Hubs.

The system must distinguish Hub Owner, Principal Client, Guest, Operator, and Driver/Fulfillment roles before finalizing hub activation fees, planning deposits, payment authority, itinerary approval, and confirmation workflows.
