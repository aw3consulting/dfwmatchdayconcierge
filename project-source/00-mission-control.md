# DFW Matchday Concierge — Mission Control Authority

## Status

This file is a governing source-authority file for the DFW Matchday Concierge project.

It defines the mission-control structure, platform boundaries, and execution responsibilities for the single-operator booking/fan site update.

This file must be followed before any site implementation begins.

## Core Mission

DFW Matchday Concierge is being updated into a single-operator, single-vehicle private ride reservation and fan-support site for Dallas/Fort Worth match visitors, airport arrivals, stadium movement, Fan Festival movement, area watch events, and selected local experience routes.

The operating model is:

- Single operator.
- Single vehicle.
- 2026 Black Tahoe.
- Premium private ride reservation service.
- Limited availability.
- Pickup + Return default logic.
- Next-leg conversion after the first ride.
- Dallas / Fort Worth / Arlington routing.
- Direct QR-to-reservation flow.
- Controlled sponsor inventory.
- Approved design standard preserved.

The business objective is:

Capture the first ride, secure the return trip, and convert the guest into the next logical paid ride before the opportunity is missed.

## Platform Boundary Rule

Claude is not the mission owner.

Claude must not create, reinterpret, summarize, expand, modify, or reason out the source-authority files.

Claude may only place owner-approved source files into the repository exactly as provided, then execute one assigned implementation phase at a time.

## Mission Owner

The mission owner is the owner/operator.

The owner/operator controls:

- Final business decisions.
- Availability.
- Pricing or quote rules.
- Accepted bookings.
- Alternate driver approval.
- Vehicle details.
- Driver details.
- Hotel concierge relationships.
- Field observations.
- Service lane approval.
- Sponsor approval.
- Payment/deposit approval if used.
- Final publish approval.

## ChatGPT Mission Control Role

ChatGPT Mission Control owns the reasoning and orchestration layer.

ChatGPT Mission Control is responsible for:

- Creating source-authority files.
- Structuring the mission.
- Breaking the work into phases.
- Writing Claude implementation prompts.
- Preserving platform boundaries.
- Auditing conversion logic.
- Preventing redesign drift.
- Identifying missing responsibilities.
- Creating QA checklists.
- Creating correction prompts when needed.
- Reviewing Claude output reports with the owner.

ChatGPT Mission Control does not publish the site unless separately authorized through an approved execution platform.

## Claude Role

Claude is responsible only for the site execution lane.

Claude may:

- Place locked source-authority files into the repo exactly as provided.
- Implement one approved site phase at a time.
- Preserve the approved design standard.
- Update site copy/components/pages only when directly instructed.
- Perform in-app review of its implemented changes.
- Report changed files.
- Report unresolved risks or implementation limits.

Claude must not:

- Create source authority.
- Rewrite source authority.
- Summarize source authority in place of preserving it.
- Expand the mission.
- Redesign the site.
- Invent new services.
- Invent driver claims.
- Invent sponsor claims.
- Invent official affiliations.
- Decide platform responsibilities.
- Decide business strategy.
- Decide booking logic.
- Decide handoff structure.
- Deploy without explicit authorization.
- Claim success for external systems it has not tested.

## GitHub / Repository Role

GitHub or the active repository system controls:

- Source control.
- File history.
- Diff review.
- Branch management.
- Commit tracking.
- Pull request review if used.
- Rollback path.
- Storage of source-authority files.
- Storage of site implementation files.

Repository changes must be reviewable before deployment.

## Hosting / Deployment Role

Hosting/deployment platforms may include GitHub Pages, Netlify, DreamHost, or another approved deployment environment.

Hosting/deployment controls:

- Preview deployment.
- Production deployment only after owner approval.
- Build logs.
- Live URLs.
- Redirects.
- SSL.
- Rollback.

No production deployment may be claimed unless the deployment actually occurred and was verified.

## Domain / DNS Role

Domain/DNS controls:

- Domain records.
- Subdomain records.
- Redirects.
- SSL routing.
- QR destination stability.
- Reserve page URL stability.

Domain/DNS changes require owner approval.

## Booking Intake Role

The booking intake system controls:

- Ride request capture.
- Pickup + Return fields.
- Guest contact capture.
- Passenger count.
- Luggage count.
- Trip type.
- Airport return need.
- Conditional add-ons.
- Alternate driver permission.
- Limited availability acknowledgment.
- Owner notification.
- Guest confirmation.

Possible booking systems include native site form, Netlify Forms, Google Forms, Typeform, Airtable, Tally, Jotform, custom backend, WhatsApp fallback, or another approved intake system.

No booking intake system may be considered ready until test submissions are verified.

## Content / Data Role

The content/data system controls:

- Team pages.
- Group standings.
- Team schedules.
- Completed match scores.
- Match recaps.
- Upcoming matchup previews.
- Tournament news.
- Tournament calendar.
- Fan Festival dates.
- Watch events.
- Sponsor inventory.
- Availability notes.
- Last updated timestamps.
- Fallback states.

Live or changing content must not be published unless it is verified or clearly marked as pending.

## QR / Field Materials Role

QR and field materials control:

- QR code.
- QR target URL.
- Print cards.
- Hotel concierge cards.
- Campaign source URLs.
- Scan testing.
- Mobile landing testing.

The QR code must link directly to the Reserve a Ride page.

QR traffic must not be routed to a broad landing page, fan hub, or multi-step informational page.

## Analytics Role

Analytics controls:

- QR scans.
- Reserve page visits.
- Form starts.
- Form submissions.
- Submission source tracking.
- Campaign source tracking.
- Hotel concierge source tracking.
- Airport source tracking.
- Stadium source tracking.
- Fan Festival source tracking.
- Stockyards source tracking.
- Restaurant/nightlife source tracking.

Analytics is useful but must not delay immediate booking-flow correction if the site is not yet tracking everything.

## Payment / Deposit Role

Payment/deposit systems may include Stripe, Square, Zelle, Cash App, Venmo, manual invoice, payment link, or another owner-approved method.

Payment/deposit controls:

- Deposit collection if approved.
- Quote payment.
- Payment confirmation.
- Refund/cancellation language.
- Manual payment link rules.

Do not add payment or deposit language unless the owner approves the payment method and policy.

## Sponsor System Role

The sponsor system controls:

- Sponsor inventory.
- Sponsor inquiry intake.
- Sponsor approval.
- Ad asset collection.
- Sponsor placement rules.
- Sponsor labeling.
- No official affiliation confusion.

Sponsor placements must remain limited and controlled.

## Field Operations Role

Owner field operations controls:

- Actual ride fulfillment.
- Daily availability.
- Confirmed bookings.
- Waitlist.
- Guest communication.
- Matchday staging.
- Airport workflow.
- Stadium workflow.
- Fan Festival workflow.
- Dallas / Fort Worth / Arlington route decisions.
- Alternate driver handoff if approved.
- Hotel concierge opportunities.
- Missed conversion tracking.
- Post-ride follow-up.

## Controlled Execution Rule

The mission must proceed through controlled phases.

Claude must not receive the whole mission as an implementation request.

Each phase must have:

1. Source files or source excerpts.
2. A direct implementation prompt.
3. Clear boundaries.
4. Explicit non-authorizations.
5. Expected output.
6. Review handoff.

No phase is complete until its handoff artifact is produced and reviewed.

## Correct Phase 1 Structure

Phase 1A:

ChatGPT Mission Control produces exact source-authority file contents.

Phase 1B:

Owner reviews and locks the source-authority file package.

Phase 1C:

Claude places the locked files into the repository exactly as provided.

Phase 1D:

Claude reports file placement only.

Claude must not implement public site changes during Phase 1C or Phase 1D.
