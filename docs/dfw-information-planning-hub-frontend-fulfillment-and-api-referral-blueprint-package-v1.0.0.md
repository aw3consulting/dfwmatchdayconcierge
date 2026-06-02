# DFW Information Planning Hub Front-End Fulfillment and API Referral Blueprint Package v1.0.0

## Status

`UNDER REVIEW / FRONT-END FULFILLMENT BLUEPRINT CREATED / ALL IDENTIFIED ROUTING PATHS INCLUDED / USER REVIEW REQUIRED / NO PRODUCTION AUTHORITY`

## Controlled Action

`dfw_information_planning_hub_frontend_fulfillment_and_api_referral_blueprint_package`

## Core Determination

The DFW Matchday Information + Planning Hub is the first public fulfillment layer.

The primary model is visitor need to fast routing to best information to fulfillment options to Matchday Plan path to inquiry or premium review when needed.

Most visitors should be served through public guides, smart search, need chips, guided inquiry, official-source links, sponsor listings, referral links, affiliate links, API handoffs where available, self-serve planning outputs, inquiry fallback, and premium review only where qualified.

Backend fulfillment remains conditional and capacity-controlled.

## Visitor Service Rule

Every visitor must have a clear path to find relevant information, understand the next planning step, see available fulfillment options, choose a self-serve or external path, and escalate to operator review only when needed.

## Recommended UX Model

The recommended launch model is smart search plus need chips plus guided inquiry plus result cards plus a lightweight Matchday Plan builder.

Primary prompt:

`What do you need for matchday?`

Primary CTA:

`Find My Matchday Plan`

Secondary CTA:

`Ask Concierge`

Fast chips include Airport Arrivals, Stadium Routes, Transportation, Dining, Watch Parties, Hotels, Team Fan Hubs, Fan Festival, Parking, Luggage, Wellness, VIP Support, Media / Corporate, Team Family Support, Advertise, and Ask Concierge.

## Fewest-Clicks Rule

Target routing standard:

- 1 click to category
- 2 clicks to information
- 3 clicks to fulfillment option or inquiry

## Universal Routing Architecture

| Path Type | Purpose | Primary CTA | Status Badge |
|---|---|---|---|
| Information Path | Provide public guidance | Read Guide | Information Only |
| Official-Source Path | Link to airport, stadium, venue, event, or public authority source | Open Official Source | Official Source |
| Search / Guided Inquiry Path | Route ambiguous needs | Find My Matchday Plan | Planning Value |
| Self-Serve Planning Path | Build public plan summary | Create Matchday Plan | Planning Value |
| Sponsor Path | Paid visibility placement | View Sponsor | Sponsored Placement |
| Featured Partner Path | Curated provider or advertiser | View Partner | Featured Partner |
| Affiliate Path | Trackable affiliate or referral link | Continue With Provider | Affiliate / Referral |
| API Handoff Path | External booking or service system | Continue With Provider | Third-Party Provider |
| Inquiry Fallback Path | Help request when public routing is insufficient | Ask Concierge | Operator Review Required |
| Premium Review Path | VIP, Team Family, Media / Corporate, or coordinator support | Request Reviewed Plan | Quote Required |
| Restricted Command Hub Path | Hub preview or access after qualification | Request Command Hub Review | Restricted |
| Backend Fulfillment Path | Operator-managed fulfillment | Submit for Review | Subject to Confirmation |

## Front-End Fulfillment Layers

Layer 1 is information fulfillment through public guides and planning content.

Layer 2 is partner, sponsor, referral, affiliate, and API fulfillment through public cards and handoff paths.

Layer 3 is inquiry fallback for needs that cannot be resolved through public information or external paths.

Layer 4 is premium review for VIP, Team Family, Media / Corporate, high-value coordinators, and complex itinerary requests.

Layer 5 is backend fulfillment after qualification, review, capacity check, payment or deposit status, and confirmation.

## Matchday Plan Builder

The public site must include a lightweight front-end Matchday Plan builder.

Fields include visitor type, team or match interest, arrival airport, hotel or stay area, stadium movement need, dining or watch-party interest, transportation need, parking or shuttle need, luggage need, accessibility or family needs, wellness or recovery need, budget comfort, preferred contact method, and whether operator help is needed.

Outputs include guide links, official-source links, partner options, sponsor cards, referral or affiliate links, API handoff options, next planning steps, inquiry fallback, and premium review option where appropriate.

## Fan Traffic Rule

Fan traffic should be served primarily through front-end fulfillment. Fans should receive team-specific guides, language or country preference where possible, airport guidance, stadium movement guidance, dining and watch-party discovery, hotel-area information, official-source links, sponsor listings, referral or affiliate links, provider CTAs, self-serve Matchday Plan builder, and inquiry fallback only where needed.

Fans should not be routed first into backend concierge assignment, driver assignment, internal fulfillment queue, or premium Command Hub.

## Premium Lane Rule

VIP, Team Family, Media / Corporate, and high-value coordinator groups can be offered reviewed Command Hub experiences after qualification and operator review.

Backend fulfillment remains conditional.

## Required Public Pages

Immediate public front-end fulfillment pages:

1. `/`
2. `/connect/`
3. `/fans/`
4. `/airport-arrivals/`
5. `/transportation/`
6. `/dining-watch-parties/`
7. `/hotels-area-guide/`
8. `/vip-media-coordinator-support/`
9. `/advertise/`
10. `/sponsors/`

Recommended expansion pages include `/stadium-movement/`, `/fan-festival/`, `/parking-shuttles/`, `/luggage-support/`, `/wellness-recovery/`, `/team-guides/`, and `/matchday-plan/`.

## Result Card Components

Every result card should include title, short explanation, source type, status badge, primary CTA, secondary CTA, disclosure, tracking tag, category, audience, last reviewed date, and claim review status.

Card types include Information, Official Source, Sponsor, Featured Partner, Affiliate / Referral, API Handoff, Inquiry Fallback, and Premium Review.

## API / Referral / Partner Framework

API and referral paths are front-end fulfillment infrastructure. Potential categories include maps and navigation, airport transport providers, black car providers, rideshare links where applicable, hotel booking links, dining reservation links, watch-party venue links, parking links, shuttle links, luggage storage links, wellness / IV / recovery links, urgent care links, tours and attractions, eSIM / international traveler services, travel insurance, and legally appropriate official-source event links.

Every external provider path must be labeled as third-party, sponsor, affiliate/referral, featured partner, or official source.

## Advertiser Integration

Sponsor placements may appear in homepage sponsor rail, team fan hub pages, airport arrivals, transportation, dining/watch parties, hotel-area guide, VIP/media/coordinator public page, Matchday Plan result cards, and public guide cards.

Sponsor placements must be labeled and must avoid unsupported official relationship claims.

## Data Model Requirements

Each guide, link, sponsor, referral, affiliate, API, and inquiry card should support title, category, audience, route, status_badge, source_type, description, primary_cta, secondary_cta, url, phone, whatsapp, email, utm_source, utm_campaign, sponsor_status, affiliate_status, claim_review_status, availability_required, last_reviewed, and internal_notes.

## Claim Controls

Every public fulfillment card must map to Information Only, Official Source, Sponsored Placement, Featured Partner, Affiliate / Referral, Third-Party Provider, Operator Review Required, Quote Required, Subject to Confirmation, or Restricted.

Blocked claims include guaranteed booking, guaranteed ride, guaranteed driver, guaranteed vehicle, guaranteed seating, guaranteed provider availability, guaranteed command hub access, guaranteed fulfillment, official tournament relationship, official team relationship, official venue relationship, official host city relationship, official sponsor relationship, live AI confirmation, live dispatch, live payment automation, and live routing automation.

## Homepage Structure

The homepage should include hero, universal Find My Matchday Plan search or intake, fast chips, public guide grid, Team Fan Hub entry, premium reviewed support entry, sponsor-safe rail, featured fulfillment options, DFW orientation map, how planning works, advertise / partner CTA, independent platform disclaimer, and contact / Connect / QR CTA.

## Connect Page Structure

The Connect page should include need prompt, fast chips, search or intake field, visitor type selection, suggested path results, Matchday Plan builder, front-end fulfillment options, premium review path, sponsor/advertiser inquiry split, and contact fallback.

## Mobile Requirement

Mobile must prioritize search or intake field, fast chips, top guide cards, result cards, Ask Concierge fallback, sponsor cards below useful content, premium review CTA where relevant, and visible disclaimer language.

## Implementation Priority

Immediate build priority is homepage public information gateway, Connect routing page, Fan Hub public pages, Airport Arrivals, Transportation, Dining and Watch Parties, Hotels and Area Guide, VIP/Media/Coordinator public support, Advertise page, Sponsors page, Matchday Plan builder, result-card data model, and sponsor/referral/official-source card system.

Backend dashboards remain staged after public front-end fulfillment is functional.

## Next Controlled Action

`dfw_advertiser_readiness_and_outreach_asset_package_v1.0.0`
