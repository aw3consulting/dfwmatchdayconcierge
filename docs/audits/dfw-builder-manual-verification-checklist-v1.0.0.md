# DFW Builder Manual Verification Checklist v1.0.0

## 1. Controlled Action

This file corrects audit blocker B-005 by creating a manual verification substitute for validation until executable CI is created.

This file does not replace future CI. It provides the minimum manual verification record required before option review, skeleton activation, production approval, DreamHost deployment, or QR activation can proceed.

## 2. Status

Status: ACTIVE MANUAL VERIFICATION SUBSTITUTE

Activation standing:

`MANUAL VERIFICATION SUBSTITUTE CREATED / FAILED CHECKS BLOCK PROGRESSION / USER EVALUATION REQUIRED`

## 3. Verification Scope

This checklist applies to:

1. Builder correction files.
2. Option-selection review sessions.
3. Future skeleton rendering sessions.
4. Future production readiness reviews.
5. Future QR activation reviews.
6. Future DreamHost deployment reviews.

## 4. Required Checks Before Option-Selection Review

| Check | Pass requirement | Evidence required |
|---|---|---|
| Active handoff | `docs/dfw-premium-website-builder-execution-handoff-prompt-v1.0.1.md` exists on `main`. | Exact path fetch. |
| Audit files | Audit report and correction register exist on `main`. | Exact path fetch. |
| Source-of-truth index | Current execution source-of-truth index exists on `main`. | Exact path fetch. |
| Public boundary | Public surface route status register exists on `main`. | Exact path fetch. |
| QR boundary | QR/domain boundary record exists on `main`. | Exact path fetch. |
| Stop point | Next prompt states hard stop after option presentation. | Line or section reference. |
| No skeleton creation | No skeleton files are created during option-selection review. | File status or commit scope. |

## 5. Required Checks Before Skeleton Rendering

| Check | Pass requirement | Evidence required |
|---|---|---|
| User option selection | User explicitly selects one option per section or approves recommended set. | Chat record summary. |
| Allowed paths | Skeleton execution is limited to approved skeleton path. | File list review. |
| Blocked paths | No homepage, production, linked page, PDF, image, DreamHost, or QR files are edited. | Commit diff review. |
| Skeleton text | Public skeleton text is limited to section names and authorized taglines. | Rendered text review. |
| No JavaScript | Skeleton path contains no JavaScript. | File review. |
| No third-party scripts | No script imports or analytics appear. | File review. |
| No external fonts | No external font loading appears. | CSS review. |
| No images or PDFs | Skeleton path uses no image or PDF assets. | File review. |
| Tokenized CSS | CSS uses purpose-based variables and approved file structure. | CSS review. |
| Responsive review | Required viewport checks completed. | Review notes. |
| Accessibility review | WCAG 2.2 AA working target checks completed. | Review notes. |
| Claim review | Skeleton contains no unapproved public claims. | Claim review note. |
| Sponsor review | Sponsor surface contains no sponsor names, logos, metrics, or placement claims. | Sponsor review note. |
| Link review | Placeholder links do not imply production activation. | Link review note. |
| Preview/prod boundary | Preview surface is not treated as production. | Boundary note. |

## 6. Required Checks Before Production Approval

| Check | Pass requirement | Evidence required |
|---|---|---|
| Claim register | Public claim review register completed. | Exact path fetch. |
| Route status | Public surface boundary register updated if needed. | Exact path fetch. |
| Mobile review | Production public routes pass mobile review. | Review record. |
| Accessibility review | Public routes reviewed against working target. | Review record. |
| Contact behavior | Contact, SMS, WhatsApp, email, and mailto behavior reviewed. | Review record. |
| Sitemap and robots | Sitemap and robots reviewed for activation standing. | Review record. |
| Deployment manifest | DreamHost package manifest completed. | Exact path fetch. |
| User approval | User explicitly approves production readiness. | Chat record summary. |

## 7. Required Checks Before QR Activation

| Check | Pass requirement | Evidence required |
|---|---|---|
| QR destination | Exact destination confirmed. | QR review record. |
| Mobile load | Destination loads on mobile. | QR review record. |
| Claim safety | Destination claims reviewed. | Claim register. |
| Contact actions | Call, SMS, WhatsApp, and email actions reviewed. | QR review record. |
| User approval | User explicitly approves QR activation. | Chat record summary. |
| Activation status | QR marked active only after approval. | QR review record. |

## 8. Failure Rules

Progression fails if:

1. Any required check is missing.
2. Any blocked path is edited.
3. Skeleton content exceeds section name and tagline.
4. User approval is inferred rather than explicit.
5. Preview is treated as production.
6. QR route existence is treated as QR activation.
7. Public claims remain unmapped before production approval.
8. DreamHost package lacks included and excluded file controls.

## 9. Final Determination

Audit blocker B-005 is corrected with a manual verification substitute.

Final standing:

`MANUAL VERIFICATION CHECKLIST CREATED / VALIDATION SUBSTITUTE AVAILABLE / FAILED CHECKS BLOCK PROGRESSION / ACTIVATION REMAINS BLOCKED PENDING USER EVALUATION AND NEXT ACTION AUTHORIZATION`.
