# DFW Public Surface Boundary and Route Status Register v1.0.0

## 1. Controlled Action

This file corrects audit blocker B-002 by classifying existing public-facing repository surfaces so they cannot bypass the DFW AI-Governed Premium Website Builder Module state machine.

This file does not authorize production approval, QR activation, DreamHost deployment, homepage generation, final content expansion, or skeleton rendering.

## 2. Status

Status: ACTIVE PUBLIC SURFACE BOUNDARY REGISTER

Activation standing:

`ACTIVATION BLOCKED / PUBLIC SURFACES CLASSIFIED / CLAIM REVIEW AND USER APPROVAL STILL REQUIRED BEFORE PRODUCTION OR QR ACTIVATION`

## 3. Classification Rules

Allowed status values:

1. Live placeholder.
2. Legacy.
3. Superseded.
4. Rejected.
5. Production-authorized.
6. Preview-only.
7. Requires claim review.

No route in this register is production-authorized by this file.

## 4. Public Surface Status Table

| Surface | Current status | May remain public | May be used as builder input | Claim review required | Notes |
|---|---|---:|---:|---:|---|
| `index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Existing public homepage surface predates the corrected section-first builder workflow. It may not be used as the source for skeleton content. |
| `connect/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Final QR destination route exists, but route existence is not QR activation approval. |
| `contact/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Contains contact and inquiry behavior that requires separate claim, privacy, and UX review before production approval. |
| `services/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Existing service copy cannot be used as skeleton content. |
| `private-transportation/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Public claim surface requiring capability mapping. |
| `airport-transfers/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Public airport transfer claim surface requiring capability mapping. |
| `matchday-logistics/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Public logistics claim surface requiring capability mapping. |
| `concierge-hospitality/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Public hospitality claim surface requiring capability mapping. |
| `group-vip-transportation/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Public VIP/group transport claim surface requiring capability mapping. |
| `luggage-coordination/index.html` | Live placeholder / Requires claim review | Yes, if already live | No | Yes | Public luggage coordination claim surface requiring capability mapping. |
| `sitemap.xml` | Live placeholder / Requires review | Yes, if already live | No | Yes | Route listing exists, but sitemap presence is not production approval. |
| `robots.txt` | Live placeholder / Requires review | Yes, if already live | No | Yes | Crawler permission exists, but crawler permission is not activation approval. |
| `assets/connect-qr.svg` | QR asset / Requires QR review | Yes as an asset reference | No | Yes | Asset existence is not QR activation approval. |
| `docs/prototypes/homepage-v1.0.4/review.html` | Rejected | Yes only as archived evidence | No | Yes if publicly previewed | Hard-failed prototype, prohibited as execution basis. |
| `docs/prototypes/homepage-section-skeleton-v1.0.0/` | Not started / Blocked | No until created and approved | Yes only after user option selection | Yes before public production | Skeleton path remains blocked until option selection is recorded. |

## 5. Boundary Rules

1. Existing public route files are classified as live placeholder surfaces that require claim review.
2. Existing public route files are not active builder input.
3. Existing public route files are not proof that the new builder workflow is complete.
4. Final-domain references are route references only unless separately approved for production activation.
5. QR asset references are not QR activation approval.
6. Existing service pages may remain as live placeholder surfaces only if the user accepts the current live standing while claim review remains pending.
7. Future homepage or skeleton work must proceed through the section state machine and cannot copy final public route content into the skeleton.

## 6. Activation Impact

Corrects audit blocker B-002 at the documentation-boundary level.

Activation still remains blocked until:

1. Claim review register is completed.
2. QR boundary and QR review records are completed.
3. Manual verification or validation substitute is completed.
4. User evaluates correction package.
5. User explicitly authorizes the next permitted action.

## 7. Final Determination

Final standing:

`PUBLIC SURFACE BOUNDARY CREATED / EXISTING ROUTES CLASSIFIED AS LIVE PLACEHOLDER OR REVIEW SURFACES / ROUTES MAY NOT BYPASS SECTION-FIRST BUILDER STATE MACHINE / ACTIVATION REMAINS BLOCKED PENDING USER EVALUATION`.
