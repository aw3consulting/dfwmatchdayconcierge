# DFW Matchday Concierge — Public Route Claim Correction and Logo QR Asset Standardization Record v1.0.0

**Mission:** `dfw_public_route_claim_correction_and_logo_qr_asset_standardization_package_v1_0_0`  
**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** Bounded public-baseline correction completed / production readiness still blocked  

## 1. Boundary

This record documents a bounded correction package applied only to current public baseline route files and a new governance record.

This package does **not** delete files, move files, deploy to DreamHost, rerun a workflow, merge PR #1, promote a prototype, replace the public site with prototype files, change QR activation standing, treat GitHub Pages as approval, or claim production readiness.

## 2. Files changed

| File | Change type | Commit SHA | Summary |
|---|---:|---|---|
| `index.html` | updated | `769c3106370cf29f29a72d640994b2ab9701cef0` | Corrected homepage launch-risk claims, removed absolute arrival guarantee language, bounded availability, standardized logo to PNG public asset. |
| `connect/index.html` | updated | `db4b1ba2be02e7678d84c2e06574d821e4022362` | Corrected connect route claims, changed booking framing to inquiry/operator review, standardized logo to PNG public asset. |
| `contact/index.html` | updated | `17498cb02d3f1fce09800af1f8319676e864db25` | Clarified static inquiry flow, reservation/availability boundary, and operator review; standardized logo to PNG public asset. |
| `services/index.html` | updated | `3246c07af73e2452e7de999bac9a0c8c70f7a00d` | Corrected route from minimal stub into consistent public-baseline page with header, footer, service cards, and safer claim language. |
| `private-transportation/index.html` | updated | `5396d5dfec18392b0b9d676abf83a0e0a7b654f4` | Corrected private transportation copy to operator-coordinated / confirmed-details language and standardized logo to PNG public asset. |
| `airport-transfers/index.html` | updated | `8101835512591823d297c464dfe42c9d5e9f07cd` | Corrected airport transfer claims to provided-flight-detail, confirmed-service-term language and standardized logo to PNG public asset. |
| `matchday-logistics/index.html` | updated | `abe4fea41bc9ee42701a0290c420757252f89ecf` | Corrected matchday logistics claims to timing review, route awareness, and confirmed expectations language; standardized logo to PNG public asset. |
| `concierge-hospitality/index.html` | updated | `e8f0d50870c1f283651b5e66ad2863173f8ddd0f` | Added scoped hospitality boundary and feasibility review language; standardized logo to PNG public asset. |
| `group-vip-transportation/index.html` | updated | `a73df2b8e72dcc819d79495cf95d0ec1561b26d5` | Added capacity, vehicle fit, confirmation, and service-term boundary language; standardized logo to PNG public asset. |
| `luggage-coordination/index.html` | updated | `59f374335e3344156423a42f690b135c9bfbd19a` | Added luggage scope, handling, vehicle fit, and liability boundary language; standardized logo to PNG public asset. |
| `docs/dfw-public-route-claim-correction-and-logo-qr-asset-standardization-record-v1.0.0.md` | created | final commit for this record | Governance record for this correction package. |

## 3. Claim families corrected

| Claim family | Prior risk | Correction made |
|---|---|---|
| Absolute timing / arrival guarantee language | Homepage included absolute outcome language. | Replaced with timing review, timing coordination, route awareness, and prepared-plan language. |
| Coverage / insurance language | Connect and homepage included insurance-style or evidence-sensitive wording. | Replaced with professional coordination, safety/privacy expectations, and service-boundary language. |
| 24/7 availability | Public routes implied unrestricted availability. | Replaced with reservation-based availability, itinerary details, operator availability, confirmation, and accepted terms. |
| Direct booking / rideshare-comparison language | Public routes used unsupported comparison language. | Reframed to direct communication and inquiry/operator review without negative platform-comparison claim. |
| Executive / VIP / world-class positioning | Could imply guaranteed outcome or unsupported status. | Reframed to executive-style standard, service-minded coordination, capacity review, vehicle fit, and confirmed terms. |
| Concierge hospitality | Scope was broad and could imply unbounded white-glove service. | Added scoped hospitality, approved stops, comfort requests, feasibility review, location/timing/operator availability limits. |
| Luggage coordination | Could imply unlimited handling, custody, storage, or liability coverage. | Added bag count, handling limits, vehicle fit, timing, scope, and accepted service details. |
| Group and VIP transportation | Could imply guaranteed capacity/vehicle availability. | Added passenger count review, vehicle class, vehicle fit, capacity, luggage fit, wait time, route plan, and confirmed terms. |
| Booking / reserve language | Could imply completed booking without confirmation. | Reframed primary CTAs to inquiry, request, review, and confirm where needed. |

## 4. Logo asset decision

| Decision | Status |
|---|---:|
| Public routes now reference the PNG public logo asset rather than mixing PNG homepage logo with SVG route logo. | completed |
| Standardized public logo path posture: homepage uses `assets/brand-logo.png`; nested public routes use `../assets/brand-logo.png` or `/assets/brand-logo.png` depending on route depth/path style. | completed |
| No binary asset replacement was performed. | completed |
| Final visual confirmation against the approved transparent logo remains required before production readiness. | unresolved / requires evidence |

## 5. QR asset decision

| Decision | Status |
|---|---:|
| `assets/connect-qr.png` was retained unchanged. | completed |
| QR activation standing was not changed. | completed |
| Public copy continues to route users to `/connect/`. | completed |
| Final QR destination remains recorded as `https://dfwmatchdayconcierge.com/connect`. | recorded |
| Repository asset presence was confirmed as a PNG asset at `assets/connect-qr.png`. | recorded |
| Exact scan validation of the current repository asset and production-served asset remains a required gate before QR approval. | unresolved / requires evidence |
| Locked business-card print package QR reference decoded to `https://dfwmatchdayconcierge.com/connect`; this supports destination consistency but does not replace repository-asset scan validation. | evidence support only |

## 6. `/services/` correction made

The `/services/` route was corrected from a minimal single-section page into a route consistent with the active public baseline:

- Added public header with brand/logo/nav/call action.
- Standardized logo to `/assets/brand-logo.png`.
- Added canonical URL and safer metadata.
- Added page hero with confirmation and operator-review boundary.
- Added service cards for private transportation, airport transfers, matchday logistics, concierge hospitality, and group/VIP transportation.
- Added direct inquiry/connect actions.
- Added footer with contact details and service-area language.
- Removed broad unqualified “premium movement” framing and replaced it with reviewed/confirmed-service language.

## 7. PR #1 boundary

PR #1 was not merged. No PR #1 file was copied into `main` by this package.

PR #1 remains available only for comparison of claim/data/asset structures. Any future PR #1 extraction must identify:

1. exact source file,
2. exact target file,
3. rationale,
4. claim/capability boundary,
5. validation need,
6. approval gate.

## 8. Validation checklist still required before DreamHost readiness

| Gate | Standing | Required evidence |
|---|---:|---|
| Route rendering review | unresolved / requires evidence | Browser review for `/`, `/connect/`, `/contact/`, `/services/`, and all service routes. |
| Mobile review | unresolved / requires evidence | Mobile viewport review for all public routes. |
| Logo visual review | unresolved / requires evidence | Confirm PNG logo renders correctly and matches approved visual source. |
| QR repository asset scan | unresolved / requires evidence | Scan `assets/connect-qr.png` and confirm exact destination. |
| QR production-served scan | unresolved / requires evidence | Scan QR after served route validation before public/print approval. |
| Connect route action test | unresolved / requires evidence | Test phone, SMS, WhatsApp, email, and contact links on mobile and desktop. |
| JS/form behavior test | unresolved / requires evidence | Test `contact/?service=...` preselect and mailto body generation. |
| Claim review | unresolved / requires evidence | Verify no remaining public claim exceeds live/operator-assisted/restricted capability. |
| Asset path review | unresolved / requires evidence | Validate PNG/CSS/JS paths on GitHub Pages preview and DreamHost context if/when authorized. |
| DreamHost document root readiness | unresolved / requires evidence | Confirm document root/target path before any deployment. |
| User approval | unresolved / requires evidence | Required before public launch approval, production deployment, or QR activation. |

## 9. Production readiness standing

Production readiness remains **blocked**.

Blocking reasons:

- No DreamHost deployment was performed.
- No DreamHost workflow was rerun.
- No production-host route validation was performed.
- No final mobile review was performed.
- No final QR asset scan validation was performed against the repository/served QR asset.
- No final user approval was recorded.

## 10. Next safe correction step

Execute:

`dfw_public_route_browser_mobile_qr_and_asset_validation_record_v1_0_0`

Recommended scope:

1. Validate corrected public routes in browser preview.
2. Validate mobile route presentation.
3. Decode/scan `assets/connect-qr.png` and record exact destination.
4. Confirm PNG logo visibility across all public routes.
5. Test contact/WhatsApp/SMS/email/form behavior.
6. Produce DreamHost readiness evidence without deploying.

## 11. Hard stop

This correction package does not authorize deletion, movement, DreamHost deployment, DreamHost workflow rerun, PR #1 merge, prototype promotion, public route replacement with prototype files, QR activation, GitHub Pages approval, or production readiness.
