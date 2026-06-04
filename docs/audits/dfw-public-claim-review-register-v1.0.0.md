# DFW Public Claim Review Register v1.0.0

## 1. Controlled Action

This file satisfies audit corrections R-001 and R-002 by creating a public claim review register for current DFW Matchday Concierge public route files.

This file is a manual claim-control register. It does not approve production, activate QR, deploy to DreamHost, expand public claims, or insert final homepage content.

## 2. Status

Status: ACTIVE CLAIM REVIEW REGISTER

Activation standing:

`CLAIM REGISTER CREATED / PUBLIC CLAIMS REQUIRE USER EVALUATION BEFORE PRODUCTION OR QR ACTIVATION`

## 3. Capability Status Values

| Status | Meaning | Public use rule |
|---|---|---|
| Live | Capability is currently available for public use. | May appear if route and wording are approved. |
| Operator-assisted | Capability is available through manual or operator-managed workflow. | May appear only with clear non-automated expectation. |
| Development | Capability is planned or being built. | May not appear as active public capability. |
| Restricted | Capability is limited by scope, approval, legal, operational, or partner limits. | May appear only with precise limitation or remain internal. |
| Requires evidence | Claim needs additional evidence before approval. | May not be expanded. |

## 4. Public Route Claim Review Table

| Route or file | Claim surface | Current status | Evidence or workflow basis | Public use rule |
|---|---|---|---|---|
| `index.html` | DFW Matchday Concierge brand and public gateway | Operator-assisted | Existing live placeholder surface and manual concierge workflow. | May remain as placeholder only pending user review. |
| `index.html` | Premium private transportation | Operator-assisted / Requires evidence | Manual vehicle and operator delivery model, subject to availability and service scope. | Requires exact wording review before production approval. |
| `index.html` | Airport transfers | Operator-assisted / Requires evidence | Manual operator-assisted routing and inquiry handling. | Requires capability wording tied to available fulfillment. |
| `index.html` | Matchday logistics | Operator-assisted / Requires evidence | Manual planning and coordination workflow. | May not imply official event, venue, or team affiliation. |
| `index.html` | Concierge hospitality | Operator-assisted / Requires evidence | Manual concierge support model. | Requires scope limits before production approval. |
| `connect/index.html` | Direct call, SMS, WhatsApp, email, and inquiry pathways | Operator-assisted | Contact pathways are operational when linked to user-controlled channels. | Must be tested before QR activation. |
| `connect/index.html` | QR destination | Requires evidence | Route exists, but QR activation approval is separate. | May not be marked active until QR review and user approval. |
| `contact/index.html` | Inquiry form or mailto behavior | Operator-assisted / Requires evidence | Static mailto behavior requires UX and privacy review. | Must pass contact-flow review before production approval. |
| `services/index.html` | Service category listing | Requires evidence | Service pages exist, but claims require mapping. | May remain placeholder pending claim review. |
| `private-transportation/index.html` | Private transportation service | Operator-assisted / Requires evidence | Manual operator-assisted delivery. | Wording must avoid guaranteed availability unless confirmed. |
| `airport-transfers/index.html` | Airport transfer service | Operator-assisted / Requires evidence | Manual routing and coordination. | Wording must be capability-mapped. |
| `matchday-logistics/index.html` | Matchday logistics planning | Operator-assisted / Requires evidence | Manual planning and coordination. | Must avoid official affiliation or unsupported operational scale. |
| `concierge-hospitality/index.html` | Concierge hospitality | Operator-assisted / Requires evidence | Manual concierge support. | Requires scope and availability limits. |
| `group-vip-transportation/index.html` | Group and VIP transportation | Restricted / Requires evidence | Dependent on vehicle availability, partner drivers, and scope. | Requires restriction language and approval. |
| `luggage-coordination/index.html` | Luggage coordination | Operator-assisted / Requires evidence | Manual coordination support. | Requires operational scope before production approval. |
| `sitemap.xml` | Final-domain indexed routes | Requires evidence | File lists routes but does not approve claims. | Sitemap inclusion requires production-readiness review. |
| `robots.txt` | Crawler permission | Requires evidence | Allows crawling but does not approve claims. | Crawler posture must be reviewed before production approval. |
| JSON-LD metadata | LocalBusiness or service schema claims | Requires evidence | Schema can amplify claims into search surfaces. | Must be reviewed before production approval. |
| Canonical metadata | Final-domain canonical URLs | Requires evidence | Canonical tags identify intended URL but do not prove approval. | Must align with domain activation boundary. |

## 5. Restricted Claim Rules

1. No public claim may imply official FIFA, venue, team, airport, hotel, sponsor, or government affiliation unless separately approved with evidence.
2. No public claim may imply guaranteed 24/7 fulfillment unless operational coverage is confirmed.
3. No public claim may imply insured, licensed, permitted, or certified status unless evidence is recorded.
4. No public claim may imply sponsor availability, ad inventory, traffic volume, or paid placement results unless approved by a monetization register.
5. No public claim may imply automated booking or dispatch if the workflow is manual or operator-assisted.

## 6. Production Approval Prerequisite

Before production approval, this register must be updated with:

1. Exact public copy by route.
2. Claim-by-claim approval status.
3. Evidence or manual workflow source.
4. User approval record.
5. Any restricted wording required.

## 7. QR Activation Prerequisite

Before QR activation, the `/connect` route must be reviewed for:

1. Exact destination.
2. Mobile load.
3. Contact action behavior.
4. Claims visible on the destination.
5. User approval.

## 8. Final Determination

Audit corrections R-001 and R-002 are satisfied at the manual register level.

Final standing:

`PUBLIC CLAIM REVIEW REGISTER CREATED / CURRENT PUBLIC CLAIMS MAPPED TO MANUAL CAPABILITY STATUS / PRODUCTION AND QR ACTIVATION REMAIN BLOCKED PENDING USER EVALUATION AND FINAL CLAIM APPROVAL`.
