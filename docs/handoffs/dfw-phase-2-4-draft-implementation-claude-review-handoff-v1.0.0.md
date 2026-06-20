# DFW Matchday Concierge — Phase 2–4 Draft Implementation Claude Review Handoff

Version: v1.0.0

Status: DRAFT REVIEW HANDOFF

Repository: aw3consulting/dfwmatchdayconcierge

Branch: main

Prepared for: Claude web-page author review, enhanced development, and owner confirmation inside the Claude app

Prepared by: ChatGPT Mission Control execution lane

## Governing Status

Phases 2, 3, and 4 are draft implementation only.

They are not final web-page authority.

They are not production approved.

They are not DreamHost deployment approved.

They are not owner-confirmed public launch authority.

Claude retains web-page author authority for page-level review, design refinement, implementation enhancement, and in-app owner review preparation.

Owner review and confirmation must occur inside the Claude app before any draft implementation is treated as approved.

## Active Owner Instruction

The public service must not be marketed as a "single-operator, single-vehicle private ride reservation" product.

The public positioning is:

DFW Matchday Concierge is a premium private ride and ultimate fan experience in Dallas/Fort Worth.

The final QR destination remains:

/connect

The /connect path must immediately route to:

/reserve

An /about page is required to qualify the concierge experience using the operator background approved by the owner:

- 19 years of living abroad.
- First-time visitor experience across 14 countries.
- More than 15,000 rides completed in the greater DFW metroplex.
- Practical understanding of what it feels like to travel to a country for the first time.
- Deep DFW route familiarity from traveling on, near, and around nearly every major road in the DFW area.

## Draft Scope Already Implemented

### Phase 2 Draft — CTA and Routing Layer

Draft changes included:

- Homepage CTA draft changed toward Reserve a Ride.
- /connect draft changed into immediate redirect route to /reserve.
- /reserve draft route created.
- /about draft route created.
- Existing active service page CTAs routed toward /reserve with source parameters.
- Source authority files updated to reflect the owner correction.

Important limitation:

The Phase 2 homepage/index work is draft only. Claude retains web-page author authority and may enhance or replace page-level implementation during review.

### Phase 3 Draft — Reserve a Ride Logic

Draft changes included:

- /reserve page rebuilt into a structured static reservation request form.
- Pickup + Return capture added.
- Return needed, return location, return time/window, and next-leg fields added.
- Airport arrival/departure, stadium, Fan Festival, Dallas, Fort Worth, Arlington, restaurant/nightlife, and DFW experience conditional prompts added.
- Add-ons appear only after primary ride context.
- Alternate driver permission added.
- Limited availability acknowledgment added.
- Independent service acknowledgment added.
- Static mailto submission retained.

Important limitation:

The form does not confirm live availability, process payment, dispatch a ride, store requests, send server-side notifications, or guarantee alternate fulfillment. It prepares an email request only.

### Phase 4 Draft — Core Service Pages

Draft changes included:

Updated pages:

- airport-transfers/index.html
- matchday-logistics/index.html
- services/index.html

Created pages:

- stadium/index.html
- fan-festival/index.html
- dallas-area/index.html
- fort-worth-area/index.html
- arlington-area/index.html
- dfw-experiences/index.html

Draft route coverage includes:

- Airport arrival/departure.
- Stadium pickup + return.
- Fan Festival / Fair Park pickup + return.
- Dallas Area.
- Fort Worth Area.
- Arlington Area.
- Selected DFW Experiences.
- Pickup + Return recommendations.
- Next-leg capture.
- Airport return capture.
- Independent service and no-official-affiliation language.

## Claude Review Boundary

Claude must treat the draft pages as implementation inputs, not as final authority.

Claude may improve:

- Page hierarchy.
- Premium UI/UX.
- Copy structure.
- Mobile layout.
- CTA placement.
- Route navigation.
- Reserve form usability.
- Conditional prompt clarity.
- Claim-boundary visibility.
- Conversion continuity.

Claude must not:

- Create or rewrite governing source authority files unless owner explicitly authorizes it.
- Treat Phase 2–4 draft pages as final without owner confirmation.
- Publish production-ready claims.
- Deploy to DreamHost.
- Change final QR destination away from /connect.
- Remove the /connect to /reserve routing rule.
- Use official FIFA, team, stadium, airport, venue, restaurant, or organizer affiliation language.
- Promise restricted pickup access.
- Promise guaranteed alternate driver fulfillment.
- Turn the site into a marketplace, fleet platform, sponsor media portal, or generic tourism site.
- Use rejected Tahoe PNG assets.

## Required Claude Review Tasks

Claude should perform the following bounded review in the Claude app:

1. Read the committed project-source files needed for authority.
2. Review Phase 2, Phase 3, and Phase 4 draft page changes.
3. Confirm whether the public positioning matches premium private ride + ultimate fan experience in Dallas/Fort Worth.
4. Confirm /connect immediately routes to /reserve.
5. Confirm /reserve captures pickup, return, next-leg, airport return, and conditional add-ons.
6. Confirm /about qualifies the concierge experience without unsupported claims.
7. Confirm service pages support the required route logic.
8. Review mobile layout and CTA visibility.
9. Review claim boundaries.
10. Produce an owner-review report listing approved items, recommended corrections, blockers, and exact files changed if Claude makes updates.

## Owner Review Gate

Owner review must confirm:

- Public positioning.
- Homepage treatment.
- /connect behavior.
- /reserve form logic.
- /about credibility language.
- Core service page clarity.
- Mobile usability.
- Claim boundaries.
- QR behavior.
- No unauthorized official affiliation language.
- No production deployment.

## Production Block

DreamHost deployment remains blocked until all required gates pass:

- Claude review.
- Owner in-app review.
- Mobile review.
- QR review.
- Claim review.
- Final owner approval.

## Recommended Next Claude Prompt

Use this prompt inside Claude after ensuring it has repo access and the source files are visible:

```text
Review the DFW Matchday Concierge Phase 2–4 draft implementation.

Repository:
aw3consulting/dfwmatchdayconcierge

Branch:
main

This is review and enhanced development only.

Phases 2, 3, and 4 are draft implementation pending Claude review, enhanced development, and owner confirmation.

Claude retains web-page author authority. Treat the current draft pages as implementation inputs, not final authority.

Do not deploy.
Do not claim production readiness.
Do not change the final QR destination away from /connect.
Do not remove the /connect to /reserve routing rule.
Do not rewrite governing source-authority files unless owner explicitly authorizes it.
Do not use official tournament, team, stadium, airport, venue, restaurant, or organizer affiliation language.
Do not promise restricted pickup access or guaranteed alternate driver fulfillment.

Review and improve only the Phase 2–4 draft public page implementation as needed.

Required review targets:
1. project-source governing files needed for authority.
2. index.html as draft only.
3. connect/index.html.
4. reserve/index.html.
5. about/index.html.
6. airport-transfers/index.html.
7. matchday-logistics/index.html.
8. services/index.html.
9. stadium/index.html.
10. fan-festival/index.html.
11. dallas-area/index.html.
12. fort-worth-area/index.html.
13. arlington-area/index.html.
14. dfw-experiences/index.html.

Required outcome:
Return an owner-review-ready report with:
- What passes.
- What you changed, if anything.
- What remains blocked.
- Mobile review notes.
- QR route review notes.
- Claim-boundary review notes.
- Exact file list.
- Confirmation that no DreamHost deployment occurred.
```

## Current Standing

Next build expansion should not proceed until Claude review and owner confirmation are completed or the owner explicitly authorizes continued draft expansion.
