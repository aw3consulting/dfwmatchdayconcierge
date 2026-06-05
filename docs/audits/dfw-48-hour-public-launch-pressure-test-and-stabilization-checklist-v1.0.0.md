# DFW 48-Hour Public Launch Pressure Test and Stabilization Checklist v1.0.0

## Status

ACTIVE RELEASE-CANDIDATE CHECKLIST / VALIDATION REQUIRED BEFORE MERGE, DREAMHOST DEPLOYMENT, QR ACTIVATION, OR PRODUCTION APPROVAL

## Route Matrix

| Route | Launch role | Claim status | Required review |
|---|---|---|---|
| `/` | Public gateway | Operator-assisted / claim-safe candidate | Desktop, mobile, nav, CTA, claims |
| `/connect/` | Final QR destination | Operator-assisted contact hub | Mobile, phone, SMS, WhatsApp, email, claims |
| `/contact/` | Structured inquiry | Static mailto form | Form behavior, mobile, privacy note, claims |
| `/services/` | Service index | Operator-assisted service overview | Claims and route links |
| `/private-transportation/` | Service detail | Confirmed-availability language | Claims and CTA |
| `/airport-transfers/` | Service detail | Confirmed-availability language | Claims and CTA |
| `/matchday-logistics/` | Service detail | No official affiliation claim | Claims and CTA |
| `/concierge-hospitality/` | Service detail | Scope-limited support | Claims and CTA |
| `/group-vip-transportation/` | Service detail | Restricted / availability-based | Claims and CTA |
| `/luggage-coordination/` | Service detail | Scope-limited support | Claims and CTA |

## Desktop Review

- [ ] Homepage renders without horizontal overflow.
- [ ] Header logo is visible.
- [ ] Brand lockup is visible.
- [ ] Navigation labels are visible or intentionally scrollable under constrained widths.
- [ ] CTAs are visible above the fold.
- [ ] Service cards render cleanly.
- [ ] Footer disclaimer is visible.

## Mobile Review

- [ ] Homepage renders at mobile width without horizontal overflow.
- [ ] Header logo and brand lockup remain visible.
- [ ] Navigation remains usable through horizontal scroll or responsive wrapping.
- [ ] `/connect/` action links are tap-friendly.
- [ ] `/contact/` fields are tap-friendly.
- [ ] Footer disclaimer is readable.

## Contact Action Review

- [ ] `tel:+12148926827` opens phone intent.
- [ ] `sms:+12148926827` opens SMS intent.
- [ ] WhatsApp link opens with prefilled text.
- [ ] `mailto:concierge@dfwmatchdayconcierge.com` opens email intent.
- [ ] Contact form generates mailto subject and structured body.
- [ ] Query-string service selection populates the contact form.

## Claim Review

- [ ] No official FIFA, venue, team, airport, hotel, sponsor, or government affiliation claim.
- [ ] No insured, licensed, permitted, or certified claim without evidence.
- [ ] No guaranteed 24/7 fulfillment claim.
- [ ] No guaranteed availability claim.
- [ ] No automated booking or dispatch claim.
- [ ] Group/VIP service remains restricted by scope and availability.
- [ ] Luggage coordination remains scope-limited.

## QR Review

- [ ] Final QR destination remains `https://dfwmatchdayconcierge.com/connect`.
- [ ] `/connect/` loads on mobile.
- [ ] `/connect/` contact actions are visible above or near first scroll.
- [ ] `/connect/` displays launch boundary language.
- [ ] User approves QR activation after review.

## DreamHost Deployment Review

- [ ] Branch/PR is reviewed.
- [ ] User approves merge.
- [ ] DreamHost package is generated or file upload path is confirmed.
- [ ] Production files are backed up before overwrite.
- [ ] Post-deployment `/`, `/connect/`, and `/contact/` are verified on final domain.
- [ ] QR destination is verified on final domain after deployment.

## Final Determination

This checklist authorizes validation only. It does not authorize merge, DreamHost deployment, QR activation, or production approval.
