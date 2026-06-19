# DFW Matchday Concierge — Site Capabilities Authority

## Status

This file defines the required site capabilities for the single-operator DFW Matchday Concierge update.

It is a governing source-authority file.

## Core Capability Goal

The site must convert visitors into private ride reservation requests and capture return and next-leg opportunities.

The site must support:

- Reserve a Ride.
- Pickup + Return.
- Airport return capture.
- Stadium return capture.
- Fan Festival return capture.
- Dallas / Fort Worth / Arlington routing.
- Conditional add-ons.
- Limited availability.
- Alternate driver permission.
- Source tracking when available.
- Team/tournament content as ride-support content.
- Controlled sponsor inventory.

## Required Global CTA Capability

Supported CTA labels:

- Reserve a Ride.
- Reserve Pickup + Return.
- Add Return Trip.
- Add Airport Return.
- Add Stadium Ride.
- Add Fort Worth Ride.
- Add Dallas Ride.
- Request Alternate Driver.
- View Ride Options.

Primary CTA must route to the Reserve a Ride page.

## Required QR Capability

The QR code must route directly to the Reserve a Ride page.

The Reserve page must be mobile-friendly and fast to complete.

QR source parameters should be supported when possible for card, hotel concierge, stadium, Fan Festival, Stockyards, airport, Terry Black’s, Katy Trail, Arlington, Dallas, and Fort Worth sources.

## Required Reserve Form Fields

The Reserve a Ride form must capture:

- Name.
- Phone / WhatsApp.
- Email.
- Pickup date.
- Pickup time.
- Pickup location.
- Drop-off location.
- Passenger count.
- Luggage count.
- Primary ride type.
- Return needed: yes / no / not sure.
- Return pickup location.
- Return pickup time or flexible window.
- Staying area.
- Hotel or lodging area.
- Arrival flight if airport arrival.
- Departure flight if airport return.
- Match/team/event if relevant.
- Add-on interest based on selected ride type.
- Alternate driver permission.
- Limited availability acknowledgment.
- Source/campaign parameter if available.

## Primary Ride Types

The form should support airport arrival, airport departure, stadium pickup + return, Fan Festival / Fair Park pickup + return, watch event pickup + return, Dallas restaurant/nightlife, Fort Worth Stockyards / Rodeo, Arlington bridge ride, Katy Trail Ice House, Terry Black’s Dallas, WinStar route, and other custom requests.

## Required Conditional Prompts

Airport Arrival must prompt airport return, match attendance, Fan Festival pickup + return, and Dallas/Fort Worth experience rides.

Airport Departure must prompt pickup timing before flight, luggage, and optional food stop if time allows.

Stadium must prompt pickup + return, flexible return window, staying area, and restaurant stop before or after the match.

Fan Festival / Fair Park must prompt scheduled return plan, flexible return window, dinner continuation, and hotel return.

Dallas Restaurant / Nightlife must prompt return to hotel, continuation to Fan Festival, stadium, Katy Trail, Fort Worth, and airport return.

Fort Worth / Stockyards / Rodeo must prompt pickup + return, Stockyards/rodeo/restaurant/downtown Fort Worth details, Dallas add-on, stadium add-on, and airport return.

Arlington must prompt stadium pickup + return, Dallas/Fort Worth add-on while staying near the stadium, and airport return.

WinStar route must prompt pickup + return and return-window timing.

## Required Pages

The site must support these pages or equivalent sections:

1. Home.
2. Reserve a Ride.
3. Airport.
4. Stadium.
5. Fan Festival / Fair Park.
6. Dallas Area.
7. Fort Worth Area.
8. Arlington Area.
9. DFW Experiences.
10. Team Pages.
11. Tournament Calendar.
12. Sponsors / Advertise.
13. FAQ.

## Home Page Capability

The homepage must communicate single-operator private SUV service, 2026 Black Tahoe, limited availability, Reserve a Ride CTA, Pickup + Return default, airport/stadium/Fan Festival/watch-event/experience lanes, Dallas/Fort Worth/Arlington routing, 3-day advance reservation recommendation, no official affiliation, and direct route to Reserve page.

## Reserve Page Capability

The Reserve page must be the main conversion page and must capture the first ride, return trip, next possible ride, airport return, conditional add-ons, limited availability acknowledgment, and alternate driver permission.

## Airport Page Capability

The Airport page must support arrival ride, departure ride, hotel transfer, luggage count, flight details, airport return capture, stadium/Fan Festival/experience ride prompts, and Reserve Pickup + Return CTA.

Do not publish unverified terminal-specific pickup instructions.

## Stadium Page Capability

The Stadium page must support stadium pickup + return, return planning, flexible return window, hotel / Texas Live-area coordination when available, pre-match/post-match stop, Dallas/Fort Worth/Arlington pickup logic, and Reserve Stadium Pickup + Return CTA.

Do not promise exact restricted pickup access.

## Fan Festival / Fair Park Page Capability

The Fan Festival page must support pickup + return, flexible return window, Fair Park movement complexity note, Dallas hotel return, dinner continuation, airport return prompt, and Reserve Fan Festival Pickup + Return CTA.

## Dallas Area Page Capability

The Dallas Area page must support Terry Black’s Dallas, Katy Trail Ice House, Fan Festival / Fair Park, airport return, stadium pickup + return, subtle Fort Worth prompts, and Reserve a Ride CTA.

## Fort Worth Area Page Capability

The Fort Worth Area page must support Downtown Fort Worth, Stockyards, rodeo, Fort Worth restaurant/nightlife, stadium pickup + return, Dallas experience ride, airport return, and Reserve a Ride CTA.

Fort Worth must be treated as a proven priority lane.

## Arlington Area Page Capability

The Arlington Area page must support Stadium / Texas Live, Arlington hotel pickup, Fort Worth Stockyards, Dallas restaurants, Fan Festival, airport return, matchday premium pickup planning, and Reserve a Ride CTA.

Arlington must route to both Dallas and Fort Worth.

## DFW Experiences Capability

Approved experience routes include Fort Worth Stockyards / Rodeo, Terry Black’s Dallas, Terry Black’s Fort Worth if owner-approved, Katy Trail Ice House, WinStar route, Fan Festival / Fair Park, and Stadium / Texas Live area.

Each route must include best pickup areas, Pickup + Return recommendation, next-leg prompt, Reserve a Ride CTA, and conditional add-ons only if logical.

## Team Pages Capability

Team pages must support team name, group, current group standings, team schedule, completed match scores, completed match recap, upcoming match, upcoming matchup preview, tournament news, Dallas/Fort Worth/Arlington ride suggestions, Reserve a Ride CTA, and last updated timestamp.

Team pages are support content and must not overpower the ride reservation business.

## Tournament Calendar Capability

Tournament calendar must support all matches, Dallas Stadium matches, team filter, group filter, date filter, completed/upcoming filter, Fan Festival days, watch events, and ride CTA on relevant events.

## Sponsors / Advertise Capability

The Sponsors / Advertise page must show controlled sponsor inventory with page, placement, available quantity, ad type, status, and notes.

Sponsor rules: no sponsor above main Reserve a Ride CTA, no popups, no takeover ads, no misleading official affiliation, no interruption of reservation flow, and sponsor blocks must be labeled.

## Future Capabilities

Future capabilities may include availability calendar, confirmation card generator, internal conversion tracker, sponsor inquiry form, area map cards, booking source tracking dashboard, guest follow-up automation, and owner-only ops dashboard.

Do not implement future capabilities unless assigned in a later phase.
