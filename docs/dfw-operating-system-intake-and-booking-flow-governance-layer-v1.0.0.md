# DFW Operating System Intake and Booking Flow Governance Layer v1.0.0

## 1. Purpose

This file governs the intake and booking flow for DFW Matchday Concierge. It bridges the client marketing priority model, VIP governance layer, and client allocation scoring engine into actual website UX, booking widgets, forms, upsells, payment flow, and confirmation workflow.

This layer controls how the public site asks questions, how inquiries are routed, how services are presented, how upsells occur, how payment is requested, and how bookings move from inquiry to confirmation.

## 2. Governing Product Definition

DFW Matchday Concierge operates as a World Cup Matchday Concierge intake and booking system for Dallas / Fort Worth.

The public experience must identify:

1. who the guest is
2. what kind of support they need
3. how long they need support
4. whether privacy, credential/access relevance, or VIP handling applies
5. whether the request should route to VIP review, Team Family Support, Media / Corporate, Team Fan pool-driver service, shared ride, waitlist, or decline/restrict

## 3. Primary Public Funnel

The public homepage must begin with lane selection before asking for ride details.

Required first question:

`Choose the matchday lane that best fits your trip.`

Public lanes in order:

1. VIP Guest Concierge
2. Team Family Support
3. Media / Corporate
4. Team Fan Hubs

The site should not start with `Book a Ride` as the primary logic because transportation is only one service inside the concierge operating system.

## 4. Intake Flow Sequence

### Step 1: Lane Selection

Fields / choices:

- VIP Guest Concierge
- Team Family Support
- Media / Corporate
- Team Fan Hub
- Ask Concierge / Not Sure

### Step 2: Service Window

Fields / choices:

- full stay
- weekly
- multi-day
- full-day block
- matchday only
- single route
- shared ride request

Rule:

VIP Guest Concierge should default to full stay, weekly, multi-day, or approved full-day block. Single route VIP must route to VIP review or downgrade.

### Step 3: Support Type

Fields / choices:

- private transportation
- airport transfer
- hotel-stadium-airport route
- shared ride
- matchday package
- food / snacks / drinks
- cooler setup
- essentials / OTC request
- luggage coordination
- catering / large group
- sightseeing / Stockyards / Fan Experience
- full concierge
- other concierge request

### Step 4: Client Context

Fields / choices:

- credential/access status
- guest of credential holder
- Team Family
- Media / Corporate
- sponsor / hospitality guest
- federation-linked guest
- fan / supporter
- not applicable

Public rule:

Collect self-reported context only. Do not request credential upload, relationship proof, or official verification in the first public intake step.

### Step 5: Trip Details

Required fields:

- first name
- last name
- phone
- email
- preferred contact method
- language preference
- arrival date
- departure date if applicable
- hotel / pickup area
- matchday date(s)
- passenger count
- luggage/equipment count
- notes

### Step 6: Privacy and Handling Preference

Fields / choices:

- standard coordination
- privacy-sensitive
- anonymous handling requested
- representative / assistant contact preferred

Rule:

VIP and Team Family lanes must allow privacy-sensitive and anonymous handling preference without requiring public identity disclosure.

### Step 7: Payment Readiness

Fields / choices:

- ready to pay deposit
- company card available
- payment link requested
- quote first
- not sure

Rule:

Scarce-capacity requests must not be confirmed before payment or deposit conditions are met.

### Step 8: Submit Inquiry

Output:

- Inquiry received
- Operator review required
- Quote pending
- Booking is not confirmed until quote and payment/deposit approval

## 5. Booking Widget Architecture

The booking widget must be modular and lane-aware.

### 5.1 VIP Guest Concierge Widget

Primary copy:

`Request VIP Guest Concierge`

Required visible rules:

- weekly, full-stay, multi-day, or approved block support
- Black Chevrolet Tahoe subject to approval and availability
- scheduled concierge support
- operator-confirmed quote and deposit required

Fields:

- service window
- arrival/departure
- hotel / stay area
- party size
- credential/access status
- privacy preference
- full concierge needs
- payment readiness

Do not show:

- single VIP ride purchase
- shared VIP ride
- instant Tahoe guarantee

### 5.2 Team Family Support Widget

Primary copy:

`Request Team Family Support`

Required visible rules:

- privacy-sensitive support by request
- no public verification requirement
- may escalate to VIP Guest Concierge
- operator-confirmed quote and availability required

Fields:

- relationship/context self-identification
- privacy preference
- service window
- party size
- airport/hotel/stadium needs
- food/shopping/sightseeing support
- payment readiness

### 5.3 Media / Corporate Widget

Primary copy:

`Request Media / Corporate Support`

Fields:

- organization
- contact person
- role / group type
- company-card or payment method preference
- route/schedule
- passenger count
- luggage/equipment
- catering request
- recurring schedule request
- vehicle count
- notes

Rule:

Media / Corporate should emphasize scheduling, company-card readiness, catering, recurring movement, equipment, and group routing.

### 5.4 Team Fan Hub Widget

Primary copy:

`Build Your Fan Matchday Plan`

Fields:

- team
- language
- matchday
- hotel/area
- passengers
- route need
- shared ride interest
- Fan Experience interest
- food/snack/cooler interest
- sightseeing interest

Rule:

Team Fans route to pool drivers, shared rides, route packages, and fan support. They do not receive VIP Tahoe transport unless escalated and approved.

## 6. Scoring Engine Inputs

The intake flow must capture inputs needed by the scoring engine without exposing scoring to the public.

Mapped scoring inputs:

- lane selection -> lane base score
- service window -> duration score
- payment readiness -> payment readiness score
- credential/access status -> credential/access relevance score
- privacy preference -> privacy sensitivity score
- support type -> operational complexity score
- expected service scope -> booking value score
- referral/context -> strategic value score
- schedule details -> capacity fit score

## 7. Upsell Sequence

Upsells must appear after intent selection, not before.

### 7.1 VIP Upsells

Allowed after VIP intent:

- full-stay concierge support
- airport arrival planning
- dining coordination
- shopping / essentials support
- sightseeing
- family support
- dedicated scheduling

### 7.2 Team Family Upsells

Allowed after Team Family intent:

- airport + hotel + stadium plan
- privacy-sensitive movement
- food/grocery support
- shopping support
- sightseeing
- multi-day support
- VIP escalation review

### 7.3 Media / Corporate Upsells

Allowed after Media / Corporate intent:

- recurring route schedule
- multi-vehicle support
- catering
- equipment/luggage coordination
- dedicated driver block
- company-card payment link

### 7.4 Team Fan Upsells

Allowed after fan intent:

- shared ride
- round trip
- Fan Experience route
- food + snacks + drinks
- cooler setup
- Stockyards add-on
- Dallas/Fort Worth sightseeing
- airport return

## 8. Payment Flow

Payment must remain operator-confirmed at launch.

Flow:

1. Inquiry submitted
2. Operator reviews scope and score
3. Quote prepared
4. Payment/deposit request sent
5. Booking held only after payment/deposit approval
6. Balance/add-ons handled according to quote
7. Confirmation issued

Public language:

`Your booking is confirmed only after availability, quote, and payment/deposit are approved.`

## 9. Payment Method Presentation

Allowed public payment language:

- payment link available after quote
- company-card payment available by request
- international payment options may be available by request
- deposit required for confirmed bookings

Avoid claiming:

- all currencies accepted
- instant checkout for VIP
- guaranteed booking before review
- company invoice approval for all clients

## 10. Confirmation Flow

Confirmation must include:

- service lane
- confirmed service window
- pickup / drop-off details if applicable
- passenger count
- vehicle/service level if confirmed
- payment/deposit status
- operator contact method
- cancellation terms
- status tracking step

Confirmation statuses:

- inquiry received
- quote pending
- quote sent
- payment pending
- confirmed
- assigned
- en route
- active
- return scheduled
- completed
- closed

## 11. Booking Status Workflow

Public-facing status language must remain honest.

Allowed:

- Inquiry received
- Quote pending
- Payment pending
- Confirmed
- Assigned
- Driver en route
- Delivery en route
- Matchday active
- Return scheduled
- Completed

Avoid:

- live tracking if not implemented
- automated dispatch if not implemented
- guaranteed driver if not assigned
- Tahoe confirmed if not allocated

## 12. Decline, Downgrade, and Waitlist Flow

### 12.1 Decline / Restrict

Use when:

- official access guarantee requested
- ticket brokerage/authentication/escrow requested
- medical advice requested
- unlawful alcohol handling requested
- safety/privacy risk is unacceptable
- capacity is unavailable

### 12.2 Downgrade

Use when:

- VIP request is single route or low-fit
- Tahoe unavailable
- primary operator unavailable
- fan request is better suited for pool-driver service
- Media / Corporate request is operational rather than private/VIP

### 12.3 Waitlist

Use when:

- high score but capacity blocked
- payment pending
- Tahoe blocked
- driver availability uncertain
- schedule conflict may clear

## 13. Homepage UX Requirement

Homepage hierarchy:

1. Approved logo and World Cup Matchday Concierge identity
2. Welcome to Dallas / Fort Worth
3. Public lane selector in priority order
4. Concise concierge explanation
5. Lane-aware booking entry
6. DFW map / routing preview
7. service and upsell previews
8. Ask Concierge

Homepage must not begin as a generic transportation site.

## 14. Page Architecture Impact

Required pages / hubs:

- `/vip-guest-concierge/`
- `/team-family/`
- `/media-corporate/`
- `/teams/dallas-qualifiers/`
- `/connect/`

Future pages:

- `/payment-policy/`
- `/booking-status/`
- `/driver-partners/`
- `/routes/`
- `/fan-experience/`

## 15. Intake Data Files Required

Future data layer should include:

- `data/client-lanes.json`
- `data/intake-questions.json`
- `data/scoring-inputs.json`
- `data/booking-flow.json`
- `data/upsell-rules.json`
- `data/payment-rules.json`
- `data/status-workflow.json`

## 16. Mockup Requirements

The next mockup must represent the intake flow visually.

Required above-the-fold components:

- DFW World Cup Matchday Concierge identity
- four lane selector cards
- VIP and Team Family visually separate from fan pool services
- Black Tahoe VIP reference only for approved VIP service
- booking widget that asks `Who are you?` first
- no generic luxury transport homepage

## 17. Final Determination

The governed intake and booking flow is:

1. choose lane
2. choose service window
3. choose support type
4. provide client context
5. provide trip details
6. choose privacy/handling preference
7. indicate payment readiness
8. submit inquiry
9. operator scores/reviews
10. quote sent
11. payment/deposit requested
12. booking confirmed
13. assignment/tracking begins

This flow must govern the next mockup, data layer update, booking widget update, and frontend implementation pass.
