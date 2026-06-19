# DFW Matchday Concierge — Content Data Model Authority

## Status

This file defines the content and data structures required for team pages, tournament calendar, Fan Festival content, watch events, sponsor inventory, and availability notes.

It is a governing source-authority file.

## Content Principle

Fan and tournament content exists to support ride conversion and guest trust.

It must not overpower the ride reservation business.

Every content module should help answer:

- Where is the guest going?
- When is the event?
- What area are they staying in?
- Should they reserve pickup + return?
- What next ride should they consider?

## Verification Rule

Do not publish unverified live tournament information.

Changing content must include last updated timestamp, source note or source type, fallback state, and manual override option if possible.

Summaries must be original.

Do not copy full articles or copyrighted recaps.

Do not use official logos, crests, or protected graphics unless legally cleared.

## Required Team Entity

Each team page should support team name, country, group, current standing, matches played, wins, draws, losses, goals for, goals against, goal difference, points, last updated timestamp, and source note.

## Required Team Schedule Entity

Each team schedule item should support team, opponent, match date, match time, venue, city/area, status, score if completed, result, recap status, ride relevance, and Reserve a Ride CTA route.

## Required Completed Match Entity

Each completed match should support match date, teams, score, venue, short original recap, key match note, next match implication, last updated timestamp, and source note.

## Required Upcoming Match Entity

Each upcoming match should support match date, match time, teams, venue, city/area, matchup preview, group/tournament stakes, ride relevance, Reserve a Ride CTA, last updated timestamp, and source note.

## Required Tournament News Entity

Tournament news should support headline, short original summary, related team, related match, related venue/area, ride relevance, source note, and last updated timestamp.

Do not copy publisher text. Use original summaries only.

## Required Dallas Stadium Calendar Entity

Dallas Stadium calendar items should support match date, match time, teams, stage/group, venue, area, status, ride window recommendation, Pickup + Return CTA, last updated timestamp, and source note.

## Required Fan Festival Entity

Fan Festival content should support date, open/closed/rest-day status, event area, expected relevance, ride recommendation, Pickup + Return CTA, return planning warning, last updated timestamp, and source note.

## Required Watch Event Entity

Watch events should support event name, area, venue/location if verified, date, time, teams/match if applicable, status, ride relevance, Pickup + Return recommendation, last updated timestamp, and source note.

Do not publish unverified watch events as confirmed.

## Required Area Entity

Area pages should support area name, primary guest type, primary ride lanes, cross-area prompts, airport return prompt, stadium prompt, Fan Festival prompt, experience prompts, and Reserve a Ride CTA.

Areas include Dallas, Fort Worth, Arlington, Fair Park, Airport, Stadium / Texas Live area, and North Dallas / Plano / Frisco as secondary.

## Required Sponsor Inventory Entity

Sponsor inventory should support page, placement, available quantity, ad type, status, notes, sponsor name if approved, start date, end date, and approval status.

Sponsor statuses include Available, Pending, Approved, Live, Paused, Removed, and Rejected.

## Required Availability Entity

Availability notes should support date, time window, status, notes, booking lane, owner availability, alternate driver possible yes/no, and last updated timestamp.

Availability statuses include Available, Limited, Unavailable, Waitlist only, Matchday premium window, Airport-only window, and Alternate driver possible.

## Required Fallback States

Use controlled fallback messages:

- Standings currently updating. Check back shortly.
- Match recap pending.
- Upcoming match details are being verified.
- Watch event details pending verification.
- Ride availability is limited. Submit a request for review.
- Sponsor inventory currently under review.

## Required Last Updated Rule

Every dynamic content module must show or internally store last updated date/time, source note or source type, and update owner if applicable.

If last updated cannot be shown publicly, it must be stored internally.

## Data Ownership Rule

Content updates must be assigned to a specific platform or owner.

Possible content systems include manual markdown, JSON content files, Google Sheets, Airtable, CMS, static repo files, or admin table.

Do not assume dynamic data is live unless the implementation actually supports live updates.

## Ride Relevance Rule

Every team, match, calendar, Fan Festival, and watch-event module should include ride relevance when appropriate.

Examples:

- Reserve Stadium Pickup + Return.
- Reserve Fan Festival Pickup + Return.
- Add Airport Return.
- Add Fort Worth Ride.
- Add Dallas Ride.
- Reserve Watch Event Pickup + Return.

Fan content should support reservations, not distract from them.
