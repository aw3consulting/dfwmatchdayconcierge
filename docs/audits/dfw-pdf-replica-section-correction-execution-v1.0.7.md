# DFW PDF Replica Section Correction Execution v1.0.7

## Status

EXECUTED / S03 DATE AND DURATION UPDATED / COMMAND HUBS UPDATED / FULFILLMENT PROVIDERS UPDATED / S08 READ MORE CONTROLS ADDED / DESKTOP PROTOTYPE ONLY / MOBILE PAUSED / PUBLIC ROUTE REPLACEMENT STILL BLOCKED

## Controlled Action

`dfw_pdf_replica_user_called_section_correction_execution_v1_0_7`

## Scope Boundary

This execution applies the latest user section corrections to the isolated desktop prototype only.

No production route is changed.

Blocked surfaces remain:

1. `index.html`
2. `/connect`
3. public service routes
4. DreamHost deployment
5. QR activation
6. production approval
7. mobile correction and mobile approval

## Files Created

1. `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.7.html`
2. `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/css/replica-v1.0.7.css`
3. `docs/audits/dfw-pdf-replica-section-correction-execution-v1.0.7.md`

## Corrections Applied

| Section | Correction Applied |
|---|---|
| S03-C | Updated subtitle to `Provide your Matchday. Our AI-operator will build your plan.` |
| S03 Form | Added `Duration of Stay` after Date. |
| S03-H | Replaced Time with `Duration of Stay` because multi-day service is more important to this public intake flow. |
| S03-G | Changed Date to a calendar picker using `type="date"`, `min="2026-06-09"`, `max="2026-07-20"`, and default `2026-06-09`. |
| S03-G | Added a Dallas Matchdays highlight strip for Jun 14, Jun 17, Jun 22, Jun 25, Jun 27, Jun 30, Jul 03, Jul 06, and Jul 14. |
| S04-A | Changed title to `Operating Command Hubs`. |
| S04-H | Changed final hub title to `Fulfillment Hub`. |
| S06-A | Rebuilt sponsor rail heading with title `Advertising / Sponsor` and a site CTA button `View Ad Inventory →`. |
| S07-K | Changed right lower tile title to `Fulfillment Providers`. |
| S08 | Added `Read More` controls to all cards and kept them visually separate from CTA styling. |

## Date and Matchday Basis

The date picker supports the planning window from June 9, 2026 through July 20, 2026.

The Dallas matchday highlights were added for the current Dallas Stadium match dates:

1. June 14, 2026
2. June 17, 2026
3. June 22, 2026
4. June 25, 2026
5. June 27, 2026
6. June 30, 2026
7. July 3, 2026
8. July 6, 2026
9. July 14, 2026

These are prototype schedule highlights and must be verified against the final authoritative schedule before production.

## Decision Recorded

`Time` was replaced with `Duration of Stay`.

Rationale: multi-day service planning is more commercially important than time-of-day intake at this stage. Same-day timing can be collected in notes or downstream operator review.

## Mobile Pause

Mobile remains paused by user instruction.

The v1.0.7 CSS contains a mobile pause marker and does not attempt mobile correction.

## Verification Requirement

The v1.0.7 preview must be visually reviewed before scoring or advancement.

Preview:

`https://html-preview.github.io/?url=https://github.com/aw3consulting/dfwmatchdayconcierge/blob/main/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.7.html`

## Current Standing

v1.0.7 implements the latest desktop corrections. It does not yet pass final visual review, mobile review, claim review, production review, DreamHost deployment, QR activation, or public homepage replacement.

## Final Standing

S03 DATE / DURATION / MATCHDAY HIGHLIGHT CONTROLS ADDED / OPERATING COMMAND HUBS UPDATED / SPONSOR CTA UPDATED / FULFILLMENT PROVIDERS UPDATED / S08 READ MORE CONTROLS ADDED / DESKTOP PROTOTYPE v1.0.7 CREATED / MOBILE PAUSED / BROWSER VISUAL REVIEW REQUIRED / PUBLIC ROUTE REPLACEMENT REMAINS BLOCKED.
