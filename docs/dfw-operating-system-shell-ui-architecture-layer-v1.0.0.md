# DFW Operating System Shell UI Architecture Layer v1.0.0

## 1. Purpose

This file qualifies the executive-level operating roles required for the DFW Matchday Concierge web platform and defines the UI architecture layer for converting the governed data layer into real public surfaces.

This architecture governs the next implementation lane for:

- Homepage funnel rebuild
- `/media-corporate/`
- `/teams/[team]/`
- Reusable booking widget component shell
- Route card component shell
- Status-tracking component shell
- Map panel shell
- Location-aware recommendation shell

## 2. Executive-Level Role Qualification

The system must operate as a coordinated executive delivery team, not a generic page generator. Each role has a qualification duty and a failure trigger.

### 2.1 Executive Web Designer

Duty:
Design a visual system that communicates Dallas/Fort Worth, World Cup matchday, maps, routes, teams, travel, fan utility, media/corporate operations, and concierge booking without relying on generic black luxury styling.

Required output behavior:
- Uses approved logo only.
- Uses visual geography, routes, maps, match cards, team cards, icons, and booking widgets as the main experience.
- Avoids huge meaningless headings.
- Avoids generic stealth luxury blocks.
- Builds trust through usefulness.

Failure trigger:
The page feels like a template luxury transportation site, a black-and-white brochure, or a middle-school landing page.

### 2.2 Executive Graphic Artist

Duty:
Translate the approved DFW Matchday Concierge brand into a sports, travel, tourist, and concierge operating system.

Required output behavior:
- Uses approved logo continuity.
- Adds Dallas / Arlington / Fort Worth geography.
- Adds stadium, airport, Fan Experience, Stockyards, food, and route visual cues.
- Uses sport and travel iconography without cartoon styling.
- Builds language-barrier-friendly visuals.

Failure trigger:
The page lacks Dallas/Fort Worth identity, lacks sports/event visual relevance, or reinterprets the logo.

### 2.3 Executive UI Developer

Duty:
Build structured, reusable UI components from data files instead of one-off page sections.

Required output behavior:
- Booking widget component shell.
- Route card component shell.
- Status-tracking component shell.
- Map panel shell.
- Recommendation shell.
- Audience hub shell.
- Team hub shell.

Failure trigger:
The site is built as static brochure content with no reusable operating-system component logic.

### 2.4 Executive UX Coder

Duty:
Make the funnel simple, direct, and monetization-first.

Required output behavior:
- 3-click path to inquiry or confirmation path.
- Booking widget appears before informational content.
- Fan path starts with team and language.
- Media/corporate path starts with scheduling, route, group, catering, or dispatch need.
- Upsells appear after intent selection, not before.

Failure trigger:
The user must read too much before acting, cannot identify what to click, or sees non-monetizing content above the booking action.

### 2.5 Executive Content Writer

Duty:
Write authentic, useful, concise copy that sounds like a real DFW matchday concierge, not a generic AI marketing page.

Required output behavior:
- Welcomes guests to Dallas/Fort Worth.
- Explains service in plain language.
- Uses concierge as an intake promise: all matchday inquiries accepted for routing, quote, assignment, restriction, or referral.
- Avoids exaggerated luxury claims.
- Avoids unsupported official affiliation or live automation claims.

Failure trigger:
Copy sounds machine-generated, vague, oversized, luxury-for-luxury-sake, or disconnected from what a fan or media guest actually needs.

### 2.6 Executive Online Marketing Director

Duty:
Prioritize monetization across each traffic segment.

Required output behavior:
- Media/corporate lane receives highest monetization treatment.
- Fan lane prioritizes team, language, arrival, Fan Experience, shared ride, food, sightseeing, and matchday packages.
- Every major screen contains booking, quote, or concierge inquiry action.
- Upsells are tied to location, team, route, timing, and selected need.

Failure trigger:
The site educates without converting, or presents content before revenue paths.

### 2.7 Executive Website Consultant

Duty:
Ensure the site is a viable solo-operator scalable business shell.

Required output behavior:
- No public promise beyond current or operator-assisted capability.
- Dispatch, partner intake, payments, and tracking are staged as controlled workflows.
- Driver/delivery recruitment is included as an operational layer.
- DreamHost production remains blocked until validation and approval.

Failure trigger:
The site promises fleet, payment, dispatch, ticket, medical, or official event capabilities not actually controlled.

### 2.8 Executive Product Architect

Duty:
Define the platform as a matchday operating system, not a page set.

Required output behavior:
- Aligns data, pages, components, booking states, payments, routes, hubs, and future automation.
- Treats every public surface as a product interaction.

Failure trigger:
Pages exist without system behavior or reusable product logic.

### 2.9 Executive Operations Director

Duty:
Map each inquiry to fulfillment reality.

Required output behavior:
- Solo driver reality acknowledged.
- 2-3 delivery personnel reality acknowledged.
- Additional driver recruitment and dispatch shell included.
- Inquiry routing distinguishes bookable, quote-required, partner-assigned, restricted, and declined requests.

Failure trigger:
The site markets services without a visible operator-confirmed workflow.

### 2.10 Executive Compliance and Claim Controller

Duty:
Preserve claim governance and liability boundaries.

Required output behavior:
- No official FIFA/tournament affiliation claim.
- No ticket brokerage, marketplace, escrow, authentication, or validity guarantee claim.
- No medical advice for OTC requests.
- No untested multi-currency payment claim.
- No guaranteed driver supply or automated dispatch claim.

Failure trigger:
Public copy implies unsupported capability, official status, medical advice, ticket guarantee, or automated fulfillment.

## 3. Product-Level UI Principle

The platform is:

`DFW World Cup Matchday Operating System for arriving and international fans, media, corporate guests, groups, and event-support traffic.`

The interface must behave like:

- Concierge booking site
- Sports event site
- Tourist utility site
- Route and map guide
- Matchday operations shell

Monetization priority governs layout order.

## 4. Primary User Funnel

### 4.1 Homepage Funnel

Homepage order:

1. Approved logo and DFW welcome
2. One-sentence service explanation
3. Primary lane split:
   - Media / Corporate
   - Local / International Fans
4. Immediate monetizing actions:
   - Book ride
   - Share ride
   - Build matchday package
   - Catering / large group
   - Ask concierge
5. DFW map preview
6. Team selector preview
7. Media/corporate service preview
8. Booking/payment/tracking preview

### 4.2 Media / Corporate Funnel

1. Open Media / Corporate Hub
2. Booking widget above information
3. Select route / schedule / catering / group / dispatch need
4. Submit company and contact details
5. Operator quote
6. Payment or deposit request
7. Assignment and tracking

### 4.3 Fan Funnel

1. Choose team
2. Choose language
3. Open Team Matchday Command Hub
4. Booking widget above information
5. Select ride / shared ride / package / food / Fan Experience / sightseeing / Ask Concierge
6. Submit location, match, group size, timing
7. Operator quote
8. Payment or deposit request
9. Assignment and tracking

## 5. Homepage Funnel Rebuild Architecture

The homepage must not sell abstract luxury. It must route intent.

### 5.1 Above-the-Fold Wireframe

```text
[Approved Logo] DFW Matchday Concierge
Welcome to Dallas/Fort Worth for World Cup Matchday

Choose your lane:
[Media / Corporate]
[Local / International Fans]

Fast actions:
[Book Ride] [Share Ride] [Matchday Package] [Catering / Large Group] [Ask Concierge]
```

### 5.2 DFW Operating Map Preview

The homepage must show a visual map-style panel with:

- DFW Airport
- Dallas Love Field
- Dallas
- Arlington Stadium
- Fort Worth
- FIFA Fan Experience
- Stockyards
- Key route lines

This may begin as a stylized SVG or card-map shell before external map integration.

### 5.3 Monetization Cards

Homepage cards must be action cards, not information cards:

- Airport / hotel / stadium route
- Shared ride
- Matchday package
- Food / snacks / drinks
- Catering / large groups
- Essentials / OTC
- Luggage coordination
- Ask Concierge

Each card links to a booking or inquiry path.

## 6. `/media-corporate/` Architecture

Purpose:
High-value company-card and scheduled operations lane.

### 6.1 Required Hero

```text
Media / Corporate Matchday Command Hub
Move people, gear, food, and schedules across Dallas/Fort Worth.
```

### 6.2 Booking Widget First

Fields:

- Organization
- Contact name
- Phone
- Email
- Role type
- Service needed
- Date(s)
- Pickup
- Drop-off
- Passenger count
- Equipment / luggage count
- Vehicle count
- Credential timing
- Catering request
- Payment method preference
- Notes

Primary actions:

- Airport transfer
- Hotel-stadium-airport
- Matchday route
- Round trip
- Multi-vehicle
- Executive SUV
- Shared media ride
- Credential timing
- Catering
- Large group
- Equipment / luggage
- Recurring schedule
- Dedicated driver
- Dispatch request

### 6.3 Information Below Widget

- Airport timing
- Stadium timing
- credential arrival notes
- group staging
- equipment movement
- catering coordination
- booking status explanation

## 7. `/teams/[team]/` Architecture

Purpose:
Team-specific command hub for fans and international guests.

### 7.1 Required Header

```text
[Team Flag / Team Name]
[English] [Home Language]
Matchday Command Hub
```

### 7.2 Booking Widget First

Primary actions:

- Book ride
- Share ride
- Round trip
- Airport-hotel-stadium
- Hotel-stadium-airport
- FIFA Fan Experience route
- Food / snacks / drinks
- Cooler setup
- Essentials / OTC
- Luggage coordination
- Matchday package
- Sightseeing add-on
- Ask Concierge

### 7.3 Team Intelligence Below Widget

- Upcoming Dallas matches
- Group standings
- Advancement watch
- Food recommendations by team country
- Fan gathering ideas
- DFW attractions
- stadium routes
- Fan Experience route
- merchandise guidance

## 8. Reusable Booking Widget Component Shell

Component name:
`BookingWidget`

Data sources:

- `data/audiences.json`
- `data/booking-products.json`
- `data/payment-methods.json`
- `data/booking-statuses.json`
- `data/team-hubs.json`
- `data/media-corporate-hub.json`

Required behavior:

- Accepts audience ID.
- Loads available products.
- Shows monetization actions first.
- Captures route, team, language, passenger count, timing, luggage, food, catering, and notes.
- Builds inquiry payload.
- Routes to operator-confirmed workflow.

Acceptance criteria:

- User can select a product in one click.
- User can submit an inquiry within three clicks from landing page entry.
- No unsupported payment or dispatch claim appears.

## 9. Route Card Component Shell

Component name:
`RouteCard`

Required data:

- Route ID
- Route label
- Category
- Audience
- Pickup area
- Drop-off target
- Upsells
- Inquiry CTA

Required route examples:

- DFW Airport to Arlington Stadium
- Love Field to Dallas hotel
- Dallas to Arlington Stadium
- Fort Worth to Arlington Stadium
- Hotel-stadium-airport loop
- FIFA Fan Experience route

Acceptance criteria:

- Each route can become a booking path.
- Each route can display upsells after route intent.

## 10. Status-Tracking Component Shell

Component name:
`BookingStatusTracker`

Statuses:

- Inquiry received
- Quote pending
- Quote sent
- Payment pending
- Confirmed
- Assigned
- Driver en route
- Delivery en route
- Picked up
- Delivered
- Matchday active
- Return scheduled
- Completed
- Closed
- Restricted
- Declined

Acceptance criteria:

- Tracking language is honest and operator-confirmed.
- No live automation claim appears before infrastructure exists.

## 11. Map Panel Shell

Component name:
`DFWMapPanel`

Initial version may be stylized, not live map API.

Required visual nodes:

- DFW Airport
- Love Field
- Dallas
- Arlington Stadium
- Fort Worth
- Stockyards
- FIFA Fan Experience
- Hotel area placeholder
- User location placeholder

Required route lines:

- Airport to Dallas
- Airport to Arlington
- Dallas to Arlington
- Fort Worth to Arlington
- Arlington to Fan Experience
- Dallas to Stockyards

Acceptance criteria:

- The map helps users understand DFW geography immediately.
- The map creates booking intent.
- The map does not claim real-time routing unless connected to verified map data.

## 12. Location-Aware Recommendation Shell

Component name:
`LocationRecommendationPanel`

Inputs:

- User location or entered hotel / airport / city
- Audience
- Team
- Language
- Service intent
- Match date

Output categories:

- Nearby food
- Fan Experience
- Stadium route
- Stockyards upsell
- Dallas attractions
- Fort Worth attractions
- Arlington matchday options
- Airport return
- merchandise guidance
- shared ride opportunity

Acceptance criteria:

- Recommendations drive booking or inquiry.
- Recommendations are visual and short.
- Recommendations do not overpromise live local data until verified.

## 13. Content Rules

Allowed tone:

- Welcome to Dallas / Fort Worth
- Tell us what you need
- Choose your team
- Build your matchday plan
- Request a ride, route, delivery, catering, or concierge help
- Operator-confirmed booking

Avoid:

- white-glove as primary language
- luxury-first claims
- generic premium claims
- giant abstract headlines
- official FIFA claim
- guaranteed dispatch claim
- automatic shared-ride matching claim

## 14. Visual Rules

Required visual direction:

- Approved logo
- Dallas / Arlington / Fort Worth identity
- map panels
- route lines
- match cards
- team cards
- booking widgets
- status chips
- payment chips
- language chips
- icons that overcome language barriers

Avoid:

- generic black stealth layout
- oversized serif hero as the main experience
- empty luxury cards
- abstract gradient panels
- logo reinterpretation
- unsupported sports-team branding misuse

## 15. Implementation Gate

Before further public implementation, the next build must:

1. Replace homepage with lane split and booking-first architecture.
2. Create `/media-corporate/` shell.
3. Create at least one `/teams/japan/` shell as the first Team Matchday Command Hub.
4. Implement booking widget shell.
5. Implement map panel shell.
6. Implement route card shell.
7. Implement status tracker shell.
8. Keep DreamHost production blocked.

## 16. Validation Checklist

- Executive role qualification complete.
- Homepage routes to monetizing lanes.
- Media/corporate lane appears before or equal to fan lane.
- Team hub begins with team and language.
- Booking widget appears above information.
- Map panel shows DFW geographic context.
- Route cards create booking action.
- Status tracker is operator-confirmed.
- Location recommendations support upsells.
- Concierge inquiry accepts broad requests but controls outcomes.
- No unsupported claims.
