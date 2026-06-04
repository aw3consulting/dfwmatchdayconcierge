# DFW DreamHost Deployment Package Manifest v1.0.0

## 1. Controlled Action

This file satisfies audit correction R-006 by defining the DreamHost deployment package criteria for DFW Matchday Concierge.

This file does not deploy to DreamHost, approve production, activate QR, create deployment packages, or authorize final homepage content.

## 2. Status

Status: ACTIVE DEPLOYMENT PACKAGE MANIFEST

Deployment standing:

`DREAMHOST DEPLOYMENT BLOCKED / PACKAGE CRITERIA CREATED / USER APPROVAL REQUIRED BEFORE PRODUCTION DEPLOYMENT`

## 3. Production Host Lock

Production host:

`DreamHost`

Final domain:

`https://dfwmatchdayconcierge.com`

Final QR destination:

`https://dfwmatchdayconcierge.com/connect`

## 4. Included Files for Future Production Package

Future production package may include only validated public site files and assets after approval.

Potential public package candidates:

1. `index.html`
2. `connect/index.html`
3. `contact/index.html`
4. `services/index.html`
5. `private-transportation/index.html`
6. `airport-transfers/index.html`
7. `matchday-logistics/index.html`
8. `concierge-hospitality/index.html`
9. `group-vip-transportation/index.html`
10. `luggage-coordination/index.html`
11. `assets/` public assets approved for production
12. `sitemap.xml`
13. `robots.txt`

Inclusion is conditional. A listed file is not production-approved by being listed here.

## 5. Excluded Files for Future Production Package

Future production package must exclude:

1. `docs/`
2. `docs/prototypes/`
3. `docs/audits/`
4. `docs/deployment/`
5. Rejected prototypes.
6. Audit reports.
7. Correction registers.
8. Internal source-of-truth files.
9. Builder module documents.
10. GitHub workflow files.
11. Development-only files.
12. Any file not explicitly approved for public production.

## 6. Required Prerequisites Before Production Package Approval

Production package may not be approved until all items pass:

1. Public route status reviewed.
2. Claim review completed.
3. Mobile review completed.
4. Accessibility review completed.
5. Link review completed.
6. Contact-flow review completed.
7. QR review completed if QR destination is included.
8. Sitemap and robots review completed.
9. Excluded-file list reviewed.
10. Rollback plan recorded.
11. User explicitly approves production package.

## 7. Rollback Path Requirement

Before deployment, a rollback plan must identify:

1. Prior production package or state.
2. File backup location.
3. Restoration method.
4. Responsible operator.
5. User approval requirement for rollback where feasible.

## 8. Deployment Approval Rule

DreamHost deployment requires explicit user approval after the full validation package is reviewed.

No assistant, audit file, correction file, preview, branch, commit, or route existence may approve production deployment on its own.

## 9. Final Determination

Audit correction R-006 is satisfied at the deployment-manifest level.

Final standing:

`DREAMHOST DEPLOYMENT PACKAGE MANIFEST CREATED / INCLUDED AND EXCLUDED FILE RULES DEFINED / CLAIM, MOBILE, QR, USER APPROVAL, AND ROLLBACK PREREQUISITES RECORDED / DREAMHOST DEPLOYMENT REMAINS BLOCKED UNTIL USER APPROVAL`.
