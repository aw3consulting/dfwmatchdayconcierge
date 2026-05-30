# DFW Client Allocation and Priority Scoring Engine v1.0.0

## 1. Purpose

This file defines the scoring engine for DFW Matchday Concierge client allocation. It translates the hardened business model into operational decision logic for VIP Guest Concierge, Team Family Members, Media / Corporate, and Team Fans.

The scoring engine governs:

- primary operator allocation
- Black 2026 Chevrolet Tahoe allocation
- VIP eligibility
- Team Family escalation
- Media / Corporate escalation
- Team Fan upgrade eligibility
- driver pool routing
- shared ride routing
- waitlist logic
- downgrade logic
- decline logic
- revenue optimization
- privacy and credential-sensitive prioritization

## 2. Governing Principle

Marketing lane is not the same as allocation priority.

A client enters through one of four lanes:

1. VIP Guest Concierge
2. Team Family Support
3. Media / Corporate
4. Team Fan Hub

The allocation engine then scores the inquiry based on value, duration, access relevance, privacy sensitivity, service complexity, capacity, and payment readiness.

## 3. Priority Output Classes

Every inquiry must resolve into one of these output classes:

1. Accept as VIP Guest Concierge
2. Accept as Team Family Support
3. Accept as Media / Corporate Support
4. Accept as Team Fan / Pool Driver Service
5. Escalate to VIP Review
6. Waitlist
7. Downgrade to non-VIP private service
8. Route to driver pool
9. Route to shared ride pool
10. Decline / restricted request

## 4. Score Categories

Total score uses a 100-point structure.

| Category | Max Points | Purpose |
|---|---:|---|
| Booking Value | 20 | Revenue potential |
| Booking Duration | 15 | Multi-day / weekly / full-stay priority |
| Credential or Access Relevance | 15 | VIP, credential, sponsor, federation, team-family relevance |
| Privacy Sensitivity | 15 | Anonymous, high-profile, celebrity-adjacent, family-sensitive handling |
| Operational Complexity | 10 | Itinerary, luggage, catering, multi-stop, group movement |
| Payment Readiness | 10 | Deposit, card, company payment, quote acceptance |
| Strategic Value | 10 | Referral quality, future relationship, repeat potential |
| Capacity Fit | 5 | Schedule, Tahoe, operator, driver pool feasibility |

Maximum score: 100.

## 5. Score Bands

| Score | Allocation Result |
|---:|---|
| 85-100 | VIP Guest Concierge priority review / likely accept if capacity exists |
| 70-84 | VIP review or Team Family / Media high-priority allocation |
| 55-69 | Media / Corporate, Team Family standard, or private non-VIP service |
| 40-54 | Team Fan private route, package, or pool-driver assignment |
| 25-39 | Shared ride, waitlist, or lower-priority inquiry |
| 0-24 | Decline, restrict, or refer away |

## 6. Lane Base Scores

Lane base score begins the evaluation but does not determine final allocation by itself.

| Lane | Base Score |
|---|---:|
| VIP Guest Concierge | 35 |
| Team Family Support | 30 |
| Media / Corporate | 25 |
| Team Fan Hub | 10 |

Team Family starts above Media / Corporate because it may be closer to celebrity, player, or privacy-sensitive movement. Media / Corporate may still outrank Team Family when booking value, payment readiness, recurring schedule, or strategic value is higher.

## 7. Booking Value Score

| Condition | Points |
|---|---:|
| Full-stay / entire trip high-value booking | 20 |
| Weekly booking | 18 |
| Multi-day private booking | 15 |
| Corporate multi-vehicle / catering / recurring booking | 14 |
| Approved high-value single-day block | 12 |
| Private matchday package | 8 |
| Standard private route | 5 |
| Shared ride / low-value inquiry | 2 |

## 8. Booking Duration Score

| Condition | Points |
|---|---:|
| Full stay | 15 |
| Weekly | 14 |
| 4-6 days | 12 |
| 2-3 days | 9 |
| Full-day approved block | 6 |
| Single private trip | 2 |
| Shared ride | 0 |

## 9. Credential or Access Relevance Score

Credential/access status is a priority signal only. It is not a verification claim.

| Condition | Points |
|---|---:|
| Credentialed / access-linked VIP guest | 15 |
| Team Family / federation family / staff family context | 14 |
| Sponsor / hospitality guest | 12 |
| Media credentialed / applied / pending | 9 |
| Guest of credential holder | 8 |
| Corporate guest without credential | 5 |
| Fan without credential/access relevance | 0 |

## 10. Privacy Sensitivity Score

| Condition | Points |
|---|---:|
| Anonymous VIP / high-profile private guest | 15 |
| Team Family with privacy request | 14 |
| Celebrity-adjacent or player-adjacent guest | 13 |
| Executive / sponsor guest requiring discretion | 10 |
| Media/corporate standard | 4 |
| Team fan standard | 0 |

## 11. Operational Complexity Score

| Condition | Points |
|---|---:|
| Airport + hotel + stadium + food/catering + shopping/sightseeing + return | 10 |
| Multi-stop itinerary with luggage/equipment | 8 |
| Catering or large group support | 7 |
| Airport-hotel-stadium loop | 6 |
| Standard round trip | 4 |
| Single route | 2 |
| Shared ride only | 1 |

## 12. Payment Readiness Score

| Condition | Points |
|---|---:|
| Deposit ready immediately | 10 |
| Company card / approved payment link ready | 9 |
| Corporate invoice pathway approved | 8 |
| Quote accepted, payment pending | 6 |
| Price inquiry only | 2 |
| No payment clarity | 0 |

## 13. Strategic Value Score

| Condition | Points |
|---|---:|
| High-quality referral / sponsor / federation / team relationship | 10 |
| Repeat or weekly client potential | 9 |
| Media/corporate relationship potential | 8 |
| Team Family relationship potential | 8 |
| High-profile guest potential | 7 |
| Standard fan one-time customer | 2 |
| Low-fit inquiry | 0 |

## 14. Capacity Fit Score

| Condition | Points |
|---|---:|
| Tahoe and primary operator available | 5 |
| Primary operator available, Tahoe blocked | 4 |
| Trusted driver available | 3 |
| Driver pool likely available | 2 |
| Capacity uncertain | 1 |
| No feasible capacity | 0 |

## 15. Allocation Rules

### 15.1 VIP Accept Rule

Accept as VIP Guest Concierge when:

- total score is 85 or higher
- deposit/payment readiness exists
- Tahoe or approved alternate vehicle is available
- primary operator or approved VIP operator is available
- claim boundaries remain controlled

### 15.2 VIP Review Rule

Send to VIP review when:

- score is 70-84
- Team Family escalation factors exist
- Media / Corporate high-profile factors exist
- high-value single-day block may justify exception
- Tahoe or primary operator allocation requires judgment

### 15.3 Team Family Priority Rule

Team Family can outrank Media / Corporate when:

- privacy score is high
- player/federation/staff family context exists
- service window is multi-day or weekly
- primary operator discretion is warranted
- payment readiness exists

### 15.4 Media / Corporate Priority Rule

Media / Corporate can outrank Team Family when:

- booking value is materially higher
- recurring route or multi-vehicle value exists
- catering or group support creates higher revenue
- company-card payment is ready
- Team Family request lacks privacy, duration, or payment strength

### 15.5 Team Fan Routing Rule

Team Fans should route to:

- shared ride pool
- pool driver
- private non-VIP route
- matchday package
- food/cooler support
- Team Matchday Hub

Team Fans should not receive VIP Tahoe allocation unless escalated and approved.

## 16. Tahoe Allocation Conflict Rule

When multiple clients compete for Tahoe access, use this order:

1. confirmed paid VIP full-stay / weekly booking
2. highest-scoring VIP booking
3. Team Family VIP escalation
4. high-profile Media / Corporate escalation
5. highest-value approved day block
6. approved premium upgrade

If a lower-scoring client has already paid and been confirmed, the booking must not be displaced unless the service agreement permits operator rescheduling and the client approves the change.

## 17. Primary Operator Conflict Rule

Primary operator allocation follows:

1. confirmed VIP Guest Concierge
2. Team Family escalation
3. high-profile Media / Corporate escalation
4. highest-value private booking
5. operational emergency / discretion case

Primary operator must not be consumed by ordinary shared rides or low-value fan routes when qualified VIP or Team Family demand exists.

## 18. Waitlist Logic

Waitlist when:

- score is high but Tahoe is unavailable
- score is high but primary operator is unavailable
- payment is pending
- route timing is uncertain
- capacity may open through driver recruitment

Waitlist priority should follow score order.

## 19. Downgrade Logic

Downgrade when:

- VIP requested but score falls below VIP review threshold
- single-trip request lacks strategic value
- Tahoe unavailable but private route is feasible
- Team Family request does not require VIP handling
- Media / Corporate request is operational rather than privacy-sensitive

Downgrade options:

- private non-VIP ride
- assigned trusted driver
- pool driver
- shared ride
- package-only support

## 20. Decline / Restrict Logic

Decline or restrict when:

- request implies official access guarantee
- request requires credential validation
- request involves ticket brokerage, escrow, or authentication guarantee
- request requires medical advice
- request requires unlawful alcohol handling
- payment is unclear and capacity is scarce
- timing is infeasible
- safety or privacy risk is unacceptable

## 21. Public-Facing Data Fields

The public intake should collect enough information for scoring without exposing the scoring engine.

Recommended fields:

- lane selection
- service window
- date / matchday
- location / hotel / airport
- party size
- luggage/equipment
- service need
- credential/access status if applicable
- privacy preference
- payment readiness
- notes

Avoid asking for public proof, credential uploads, or relationship evidence in the first public step.

## 22. Internal Scoring Record

Internal record should include:

- client lane
- base score
- score category values
- total score
- allocation result
- capacity status
- payment status
- privacy flag
- Tahoe allocation decision
- primary operator decision
- assigned operator/driver if applicable
- downgrade/waitlist/decline reason if applicable

## 23. Website Impact

The website should show four public lanes in this order:

1. VIP Guest Concierge
2. Team Family Support
3. Media / Corporate
4. Team Fan Hubs

The booking widget should ask who the guest is before asking what ride they need.

Homepage copy must avoid exposing internal scoring language. Use visitor-friendly language such as:

`Choose the matchday lane that best fits your trip.`

`VIP and Team Family support are reviewed by request.`

`Fan rides and shared rides are routed through available driver support.`

## 24. Governance Boundary

This scoring engine does not create a public guarantee of service. It creates internal allocation logic for operator decision-making.

All final booking decisions remain operator-confirmed.

## 25. Final Determination

The allocation engine is now governed as a 100-point scoring model with lane base scores, value, duration, credential/access relevance, privacy sensitivity, operational complexity, payment readiness, strategic value, and capacity fit.

This converts the business model into an operating-system decision layer and should govern the next mockup, booking form, data files, and client intake architecture.
