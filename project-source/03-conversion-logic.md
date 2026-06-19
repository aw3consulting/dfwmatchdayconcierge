# DFW Matchday Concierge — Conversion Logic Authority

## Status

This file defines the operating and conversion logic for the site.

It is a governing source-authority file.

## Core Conversion Rule

The site must not treat a ride request as a one-off transaction.

Every ride request must be treated as the start of a guest movement chain.

The default funnel is:

First ride
→ Return ride
→ Next logical ride
→ Airport return if applicable

## Primary Conversion Objective

The site should help the owner convert:

Airport pickup
→ Hotel drop-off
→ Stadium pickup + return
→ Restaurant / Fan Festival / Fort Worth / Dallas experience
→ Airport return

The site must close known conversion gaps.

## Global CTA Rule

All public-facing “Book a Ride” language must be replaced with:

Reserve a Ride

Approved CTA language:

- Reserve a Ride.
- Reserve Pickup + Return.
- Add Return Trip.
- Add Airport Return.
- Add Stadium Ride.
- Add Fort Worth Ride.
- Add Dallas Ride.
- Request Alternate Driver.
- View Ride Options.

Do not use “Book a Ride” as a public CTA.

## QR Rule

The QR code must link directly to the Reserve a Ride page.

The QR code must not link to:

- Generic homepage.
- Broad landing page.
- Fan hub.
- Team page.
- Informational page.
- Multi-step funnel before reservation.

Recommended route:

/reserve

Optional campaign routes:

/reserve?source=card
/reserve?source=hotel-concierge
/reserve?source=stadium
/reserve?source=fanfest
/reserve?source=stockyards
/reserve?source=airport
/reserve?source=terryblacks
/reserve?source=katytrail

## Pickup + Return Rule

Pickup + Return is the default ride logic.

One-way rides may exist, but every one-way request should prompt one of the following:

- Add return trip.
- Add airport return.
- Add stadium pickup + return.
- Add Fan Festival pickup + return.
- Add Dallas ride.
- Add Fort Worth ride.
- Add Arlington bridge ride.
- Add hotel return.
- Add next-day ride.

## Return Capture Rule

The site must prompt for return capture in these contexts:

Airport arrival:
Prompt airport return and event/experience rides.

Airport departure:
Capture final ride timing.

Stadium:
Strongly prompt pickup + return.

Fan Festival / Fair Park:
Strongly prompt pickup + return.

Restaurant:
Prompt return to hotel or continuation.

Fort Worth:
Prompt Stockyards/rodeo/Dallas/stadium/airport return.

Dallas:
Prompt Fort Worth/stadium/Fan Festival/airport return.

Arlington:
Prompt Dallas/Fort Worth/stadium/airport return.

WinStar:
Prompt round-trip only unless owner approves one-way service.

## Area Routing Logic

### Dallas Guests

Dallas guests should see Dallas attractions first, then subtle Fort Worth and stadium/airport options.

Primary Dallas prompts:

- Terry Black’s Dallas.
- Katy Trail Ice House.
- Fan Festival / Fair Park.
- Airport return.
- Stadium pickup + return.

Subtle cross-area prompts:

- Fort Worth Stockyards.
- Rodeo night.
- Arlington matchday pickup + return.
- Fort Worth restaurant/nightlife route.

### Fort Worth Guests

Fort Worth guests should see Fort Worth attractions first, then subtle Dallas and airport/stadium options.

Primary Fort Worth prompts:

- Downtown Fort Worth.
- Stockyards.
- Rodeo.
- Fort Worth restaurant/nightlife.
- Stadium pickup + return.

Subtle cross-area prompts:

- Dallas dinner.
- Terry Black’s Dallas.
- Katy Trail Ice House.
- Fan Festival / Fair Park.
- Airport return.

### Arlington Guests

Arlington guests should be routed to both Dallas and Fort Worth.

Primary Arlington prompts:

- Stadium pickup + return.
- Texas Live / hotel-area planning.
- Fort Worth Stockyards.
- Fort Worth restaurant/nightlife.
- Dallas restaurants.
- Fan Festival / Fair Park.
- Airport return.

Arlington is a bridge market.

### Frisco / Plano / North Dallas Guests

Frisco, Plano, and North Dallas remain secondary until demand is proven.

They may be presented as available by request for:

- Airport transfers.
- Stadium round trips.
- Dallas experience rides.
- Fort Worth experience rides.

They should not overpower Fort Worth, Arlington, Dallas, airport, stadium, or Fan Festival lanes.

## Add-On Logic Rule

Food, snacks, cooler, and concierge services are not standalone public service lanes.

They must only appear after a primary ride path is selected.

Add-ons must match the guest’s actual route stage.

Do not offer illogical add-ons.

Example:

Do not lead airport-arrival users with cooler service.

Better airport-arrival add-ons:

- Luggage support.
- Hotel drop-off.
- Short essentials stop if needed.
- Future stadium ride.
- Future Fan Festival ride.
- Airport return.

## Route-Specific Add-On Logic

### Airport Arrival

Logical prompts:

- Luggage count.
- Hotel/lodging area.
- Departure date/time if known.
- Airport return.
- Stadium pickup + return.
- Fan Festival pickup + return.
- Dallas/Fort Worth experience ride.
- Short essentials stop if needed.

Do not lead with cooler service.

### Airport Departure

Logical prompts:

- Hotel pickup.
- Luggage timing.
- Departure flight.
- Restaurant stop before airport if time allows.
- Final ride confirmation.

### Stadium / Matchday

Logical prompts:

- Pickup + return.
- Return pickup timing.
- Flexible return window.
- Hotel/Texas Live-area coordination when available.
- Pre-match restaurant stop.
- Post-match food stop.
- Group timing support.

Do not promise exact restricted curb access.

### Fan Festival / Fair Park

Logical prompts:

- Pickup + return.
- Flexible return window.
- Post-Festival dinner stop.
- Dallas hotel return.
- Airport return.
- Group pickup coordination.

Do not treat Fan Festival as a simple drop-off.

### Fort Worth / Stockyards / Rodeo

Logical prompts:

- Pickup + return.
- Restaurant stop.
- Rodeo timing.
- Downtown Fort Worth return.
- Arlington hotel return.
- Dallas hotel return.
- Airport return.

### Terry Black’s / Restaurant Rides

Logical prompts:

- Return to hotel.
- Continue to Stockyards.
- Continue to Katy Trail.
- Continue to Fan Festival.
- Continue to stadium if timing fits.
- Airport return.

### Katy Trail Ice House

Logical prompts:

- Pickup + return.
- Dinner/nightlife continuation.
- Hotel return.
- Airport return.
- Dallas-to-Fort Worth next-day prompt.

### WinStar Casino

Logical prompts:

- Pickup + return.
- Wait-and-return option if owner approves.
- Long-route timing confirmation.
- Food/rest stop if needed.

Do not create open-ended one-way casino drop-off logic unless owner approves.

## Stadium Public Copy Logic

The site may describe matchday transportation as complicated and worth planning in advance.

The site may say:

Matchday transportation can be confusing and time-consuming. Reserve pickup + return in advance so you are not trying to solve transportation after the match.

The site must not publicly accuse Uber, rideshare companies, drivers, data networks, event organizers, or venues.

Do not publish:

- Unsupported claims about Uber dispatch.
- Claims of manipulation.
- Driver app accusations.
- Network failure claims.
- Claims that rideshare will fail.

## Fan Festival Public Copy Logic

The site may say:

Fair Park event movement and post-event pickup can be complicated. Reserve your return plan in advance so you are not trying to arrange transportation after the event.

Do not claim exact pickup points unless verified.

## Alternate Driver Logic

If the owner is unavailable, an alternate similar-class driver may be attempted.

This is not guaranteed.

Public language must say:

If I am unable to fulfill a requested ride, I may attempt to connect you with an alternate driver using a similar-class vehicle. Alternate driver availability, pricing, timing, and confirmation are not guaranteed.

## Sponsor Logic

Sponsor placements must not interrupt reservation conversion.

Sponsor placements must not appear above the primary Reserve a Ride CTA.

Sponsor blocks must be labeled.

Sponsor content must not imply official affiliation.

## Legal / Affiliation Logic

The site must not imply official affiliation with:

- FIFA.
- FIFA World Cup.
- Dallas Stadium.
- AT&T Stadium.
- Fair Park.
- Any national team.
- Any airport.
- Any venue.
- Any official tournament organizer.
- Any official sponsor.

Event names, team names, venue names, and location names may be used only for identification and travel-planning context.

## Design Logic

The approved design standard must be preserved.

This is not a redesign.

Implementation must not drift into:

- New visual identity.
- New logo system.
- Generic FIFA-style visuals.
- Overcrowded tourism portal.
- Marketplace-style UI.
- Sponsor-heavy media page.
