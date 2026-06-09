# DFW Matchday Concierge — Public Route Claim and Asset Dependency Manifest v1.0.0

**Mission:** `dfw_public_route_claim_and_asset_dependency_manifest_v1_0_0`  
**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** Public route / claim / asset dependency manifest for current public baseline  

## 1. Boundary

This manifest maps the current public baseline to route inventory, claim families, assets, images, scripts, QR/connect dependencies, PR #1 extraction candidates, and unresolved validation gates.

This file does **not** delete, move, deploy, rerun workflow jobs, merge PR #1, promote a prototype, replace public routes, change QR activation standing, or treat GitHub Pages as approval.

## 2. Public route inventory from sitemap and repo paths

| Route | Repo path | Current standing | Route role | Review status |
|---|---|---:|---|---|
| `/` | `index.html` | active authoritative baseline | Homepage / service gateway / QR panel | Reviewed for claims and assets. Needs corrections before launch authority. |
| `/connect/` | `connect/index.html` | active authoritative baseline | QR destination / contact action hub | Reviewed. QR route remains unapproved for final activation until validation. |
| `/contact/` | `contact/index.html` | active authoritative baseline | Static inquiry form route | Reviewed. JS/mailto behavior requires validation. |
| `/services/` | `services/index.html` | active authoritative baseline | Services overview route | Reviewed. Minimal content depth. |
| `/private-transportation/` | `private-transportation/index.html` | active authoritative baseline | Service detail route | Reviewed. Claims require service-scope validation. |
| `/airport-transfers/` | `airport-transfers/index.html` | active authoritative baseline | Service detail route | Reviewed. Claims require service-scope validation. |
| `/matchday-logistics/` | `matchday-logistics/index.html` | active authoritative baseline | Service detail route | Reviewed. Operator-assisted scope must be explicit. |
| `/concierge-hospitality/` | `concierge-hospitality/index.html` | active authoritative baseline | Service detail route | Reviewed. Service language requires capability boundary. |
| `/group-vip-transportation/` | `group-vip-transportation/index.html` | active authoritative baseline | Service detail route | Reviewed. Capacity and vehicle boundary required. |
| `/luggage-coordination/` | `luggage-coordination/index.html` | active authoritative baseline | Service detail route | Reviewed. Handling and liability boundary required. |

## 3. Per-route asset dependency map

| Route | CSS | JS | Logo / image dependencies | Path type | Dependency risk |
|---|---|---|---|---|---|
| `/` | `assets/site.css` | None inline except JSON-LD | `assets/brand-logo.png`, `assets/connect-qr.png`, CSS-generated `.skyline` and `.vehicle-card` | Relative | Mixed PNG and CSS-generated visuals; QR asset must be verified against final destination. |
| `/connect/` | `../assets/site.css` | `../assets/site.js` | `../assets/brand-logo.svg` in header and hero | Parent-relative | SVG logo differs from homepage PNG logo. Script loads but no form exists on this route. |
| `/contact/` | `../assets/site.css` | `../assets/site.js` | `../assets/brand-logo.svg` | Parent-relative | Static form depends on JS and mailto behavior. |
| `/services/` | `/assets/site.css` | None | None in file body; no header logo visible in current minimal page | Absolute | Minimal route; design and nav consistency require correction. |
| `/private-transportation/` | `/assets/site.css` | None | `/assets/brand-logo.svg` | Absolute | Service page depends on root-served SVG asset. |
| `/airport-transfers/` | `/assets/site.css` | None | `/assets/brand-logo.svg` | Absolute | Service page depends on root-served SVG asset. |
| `/matchday-logistics/` | `/assets/site.css` | None | `/assets/brand-logo.svg` | Absolute | Service page depends on root-served SVG asset. |
| `/concierge-hospitality/` | `/assets/site.css` | None | `/assets/brand-logo.svg` | Absolute | Service page depends on root-served SVG asset. |
| `/group-vip-transportation/` | `/assets/site.css` | None | `/assets/brand-logo.svg` | Absolute | Service page depends on root-served SVG asset. |
| `/luggage-coordination/` | `/assets/site.css` | None | `/assets/brand-logo.svg` | Absolute | Service page depends on root-served SVG asset. |

## 4. Per-route public claim inventory

| Route | Public-facing claim families found | Initial classification | Required correction / validation |
|---|---|---:|---|
| `/` | Premium private transportation; airport transfers; matchday logistics; concierge hospitality; DFW Airport / Love Field / Dallas / Arlington / Fort Worth service area; timing control; discreet communication; luggage planning; executive-level service; 24/7 availability; direct booking; arrival guarantee language; QR connect. | Mixed: operator-assisted, restricted, unresolved | Remove absolute guarantee wording; validate coverage/availability statements; map all services to actual operator-assisted scope. |
| `/connect/` | Call/message/book/inquire; premium private transportation; airport transfers; matchday logistics; concierge hospitality; direct booking; coverage/insurance-style language; 24/7 availability; world-class events. | Mixed: live contact, operator-assisted, restricted, unresolved | Keep direct contact claims; validate service and availability claims; confirm final QR route. |
| `/contact/` | Book/inquire/reserve; private service request; direct service plan; static email request; direct contact options; 24/7 service by reservation; private transportation / matchday logistics / concierge hospitality. | Mixed: live contact, operator-assisted, restricted, unresolved | Clarify static inquiry vs booking; validate availability language; test JS/mailto behavior. |
| `/services/` | Premium movement; private transportation; airport transfers; matchday logistics; concierge hospitality; group/VIP transportation; luggage coordination. | Operator-assisted / unresolved | Needs claim-to-capability map and deeper route consistency. |
| `/private-transportation/` | Executive private ride service across DFW; reliable timing; professional coordination; direct communication; elevated guest experience. | Operator-assisted / unresolved | Confirm vehicle/operator capacity and avoid unsupported outcome language. |
| `/airport-transfers/` | Executive airport movement; DFW Airport and Love Field; flight-aware pickup planning; terminal coordination; luggage coordination; hotel transfer support. | Operator-assisted / unresolved | Confirm operational boundaries, airport access, and service terms. |
| `/matchday-logistics/` | Private event movement; timing, pickup control, return planning, traffic positioning, guest confidence. | Operator-assisted / unresolved | Keep planning/coordination language; avoid guaranteed traffic or access implications. |
| `/concierge-hospitality/` | Service beyond the ride; guest comfort; stops; timing; special requests; prepared operator. | Operator-assisted / restricted | Define what hospitality support actually includes and excludes. |
| `/group-vip-transportation/` | Coordinated transportation for executives, families, teams, VIP groups; discretion; timing discipline; direct communication. | Operator-assisted / restricted | Add capacity, confirmation, and non-affiliation boundaries. |
| `/luggage-coordination/` | Travel lighter; luggage support between airports, hotels, events, private stops; loading coordination; handling strategy. | Operator-assisted / restricted | Add handling limits, liability boundaries, and confirmation requirement. |

## 5. Claim-to-capability classification

| Claim family | Classification | Public use rule |
|---|---:|---|
| Phone, SMS, WhatsApp, and email contact paths | live capability | Allowed after link validation. |
| Static inquiry form that opens a prepared email | live capability | Allowed if JS/mailto behavior passes validation. Must not be described as a backend booking engine. |
| Private transportation | operator-assisted capability | Allowed as direct operator-coordinated service language after capacity validation. |
| Airport transfers | operator-assisted capability | Allowed after airport pickup, timing, and service-term boundaries are recorded. |
| Matchday logistics | operator-assisted capability | Allowed as planning and coordination. Avoid guaranteed traffic, access, or timing outcomes. |
| Concierge hospitality | operator-assisted capability / restricted capability | Allowed only with scoped examples and confirmation requirement. |
| Group and VIP transportation | operator-assisted capability / restricted capability | Allowed only with capacity, vehicle, and confirmation boundaries. |
| Luggage coordination | operator-assisted capability / restricted capability | Allowed only with handling limits and confirmed scope. |
| AI-assisted intake / command hub | development capability | Not live on current public baseline. May be extracted from PR #1 only after review. |
| Scores, updates, multilingual pages, tickets, advanced route data | development capability / restricted capability | Not present in current public baseline. PR #1 candidates require separate validation before public use. |
| Coverage, insurance, 24/7, direct booking, comparison language | unresolved / requires evidence | Must be validated or rewritten before launch authority. |
| Absolute arrival guarantee language | restricted / correction required | Replace with supportable timing-control language. |
| Official tournament, team, venue, federation, sponsor, credential, or event affiliation | restricted capability | Must not be claimed unless separately authorized and evidenced. |

## 6. Image format and path usage map

| Asset / visual | Format | Referenced by | Current path | Status |
|---|---:|---|---|---|
| Homepage logo | PNG | `/` header and footer | `assets/brand-logo.png` | Exists. Needs consistency check against approved transparent logo and SVG route usage. |
| Connect QR | PNG | `/` QR panel | `assets/connect-qr.png` | Exists. Must be validated against final `/connect/` destination before QR approval. |
| Shared route logo | SVG | `/connect/`, `/contact/`, service detail routes | `../assets/brand-logo.svg` or `/assets/brand-logo.svg` | Exists. Inconsistent with homepage PNG. |
| Homepage hero visual | CSS-generated | `/` | `.hero-visual`, `.skyline`, `.vehicle-card` in `assets/site.css` | No raster dependency; premium final image decision still open. |
| Service card icons | Text/CSS-generated | `/` service cards | Inline symbols styled by CSS | No image dependency; visual standards review needed. |
| Trust / process icons | Text/CSS-generated | `/`, `/connect/` | Inline symbols styled by CSS | No image dependency; visual standards review needed. |
| Prototype raster image set | PNG | Prototype surfaces only | `docs/prototypes/.../assets/...` | Not public baseline; extraction/promotion not authorized by this manifest. |

## 7. JS / form behavior map

| File / behavior | Route dependency | Current behavior | Validation needed |
|---|---|---|---|
| `assets/site.js` | `/connect/`, `/contact/` | Loads on both routes. Only acts when a form with `data-inquiry-form` exists. | Confirm no console errors on `/connect/` where no form exists. |
| `serviceSubjects` mapping | `/contact/` | Maps `ride`, `matchday`, `airport`, `hospitality`, `group`, and `luggage` to email subjects. | Validate all connect links use supported query values. |
| Query parameter preselect | `/contact/?service=...` | Reads `service` query parameter and preselects matching form option. | Test all service links from connect route. |
| Form submit handler | `/contact/` | Prevents default submit, builds a mailto body, and redirects browser to email app. | Validate on mobile and desktop. |
| JSON-LD LocalBusiness | `/` | Inline schema includes name, URL, phone, email, area served, and description. | Claim review required before launch. |

## 8. QR / connect dependency map

| Dependency | Current standing | Risk / required validation |
|---|---:|---|
| Final QR destination | `https://dfwmatchdayconcierge.com/connect` | Standing unchanged; no activation approval by this manifest. |
| Public route path | `/connect/` exists in sitemap and repo | Must verify production host serves the route with correct trailing-slash behavior. |
| Homepage QR image | `assets/connect-qr.png` exists | Must decode/scan and confirm exact destination before print/public QR approval. |
| Connect route contact actions | Call, WhatsApp, SMS, contact-route links, email display | Must validate on mobile and desktop. |
| Connect route service links | Point to `../contact/?service=ride`, `matchday`, `airport`, `hospitality`, `group`, `luggage` | Must test preselection and form behavior. |
| QR activation gate | unresolved / requires evidence | Requires route validation, QR scan validation, mobile review, claim review, and user approval. |

## 9. PR #1 technical extraction candidates without merge authority

PR #1 remains a technical extraction source only. No merge authority is granted.

| PR #1 file / surface | Extraction value | Required review before reuse |
|---|---|---|
| `data/claim-capability-map.json` | Launch claim boundaries and blocked-claim rules. | Compare with current public claims and convert into `main`-native claim register. |
| `data/claims.json` | Claim status model using Live, Operator-Assisted, Development, and Restricted classifications. | Normalize terminology against this manifest. |
| `data/services.json` | Service slugs, service titles, capability status, and positioning. | Reconcile with current service route copy before public update. |
| `data/routes.json` | DFW airport / hotel / stadium route concepts and upsell tags. | Require claim, route, and non-affiliation review before public use. |
| `data/site.json` | Domain, QR destination, contact data, production host, preview host rule, route targets. | Use only after checking against current registers and approval gates. |
| `data/seo-route-map.json` | Candidate SEO route structure. | Do not publish without route, claim, and content validation. |
| `assets/full-gateway.js`, `assets/os-shell.css` | Candidate frontend shell assets. | Do not copy until visual, asset, and route integration review. |
| PR #1 route files | Candidate expanded public route layer. | Do not replace current routes without a bounded correction package. |
| PR #1 docs and scripts | Governance and validation references. | Extract selectively into `main` only through a file-by-file extraction map. |

## 10. Validation gates still required before production or QR approval

| Gate | Standing | Required evidence |
|---|---:|---|
| Public route inventory validation | unresolved / requires evidence | Confirm every sitemap route returns expected content from production host. |
| Asset dependency validation | unresolved / requires evidence | Confirm PNG, SVG, CSS, and JS load from deployed route context. |
| Logo consistency validation | unresolved / requires evidence | Decide PNG vs SVG vs approved transparent logo usage and confirm visible rendering. |
| QR scan validation | unresolved / requires evidence | Scan `assets/connect-qr.png` and confirm exact final destination. |
| Connect route validation | unresolved / requires evidence | Test phone, SMS, WhatsApp, email, and contact links. |
| JS/form validation | unresolved / requires evidence | Test service preselect and prepared email body on mobile and desktop. |
| Public claim review | unresolved / requires evidence | Map every claim to capability status or rewrite/remove. |
| Mobile review | unresolved / requires evidence | Review all public routes on mobile dimensions. |
| DreamHost readiness | unresolved / requires evidence | Confirm document root, target path, route serving, and deployment boundary. |
| GitHub Pages preview review | preview-only | Can support review but cannot act as approval. |
| User approval | unresolved / requires evidence | Required before production deployment, route replacement, or QR activation. |

## 11. Claims requiring correction before launch authority

| Claim family | Correction requirement |
|---|---|
| Absolute timing / arrival guarantee language | Rewrite to timing-control and planning language. |
| Coverage / insurance language | Validate evidence or rewrite to a safer service-standard phrase. |
| 24/7 availability | Add reservation / confirmation / availability boundary or rewrite. |
| Direct booking / comparison language | Keep direct-contact truth but reduce unsupported platform comparison wording. |
| Executive / VIP / world-class positioning | Keep premium positioning only where service scope supports it. |
| Concierge hospitality | Define included and excluded support. |
| Luggage coordination | Add handling, scope, and liability boundaries. |
| Group and VIP transportation | Add capacity, vehicle, and confirmation language. |

## 12. Assets requiring correction before launch authority

| Asset issue | Correction requirement |
|---|---|
| Homepage PNG logo vs other-route SVG logo | Decide one approved logo source and standardize all public routes. |
| QR PNG validation | Confirm scanned QR destination and visual placement before public/print approval. |
| CSS-generated homepage hero visual | Decide whether acceptable for current launch or replace with governed approved image. |
| Minimal `/services/` route | Bring route design/header/footer consistency into line with other public routes. |
| Absolute vs relative asset paths | Validate on DreamHost and preview contexts before deployment. |
| Non-embedded image behavior | Decide whether public baseline should keep file-path assets or move to embedded assets for preview hardening. |

## 13. Next correction recommendation

Execute:

`dfw_public_route_claim_correction_and_logo_qr_asset_standardization_package_v1_0_0`

Recommended scope:

1. Rewrite or remove the claim families listed in Section 11.
2. Standardize public route logo usage against the approved logo source.
3. Validate and record QR destination from `assets/connect-qr.png` without changing QR activation standing.
4. Correct `/services/` route consistency.
5. Produce a route/asset validation checklist for DreamHost readiness without deployment.

## 14. Hard stop

This manifest does not authorize deletion, file movement, DreamHost deployment, DreamHost workflow rerun, PR #1 merge, prototype promotion, public route replacement, QR activation, or GitHub Pages approval.
