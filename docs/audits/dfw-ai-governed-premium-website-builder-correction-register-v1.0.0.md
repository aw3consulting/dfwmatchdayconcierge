# DFW AI-Governed Premium Website Builder Correction Register v1.0.0

## 1. Controlled Action

Mission name:

`dfw_ai_governed_premium_website_builder_module_independent_repo_audit`

This correction register records the blocker, required correction, strong hardening, monitor, and optional findings from the independent repo audit.

This register is not a correction execution file. It does not authorize skeleton activation, homepage generation, final content insertion, PDF capture, DreamHost deployment, QR activation, production approval, or Batch 1 progression.

## 2. Status

Status:

`CREATED / CORRECTIONS REQUIRED / ACTIVATION REMAINS BLOCKED`

## 3. Correction Register Summary

| ID | Severity | Category | Finding | Required outcome | Activation impact |
|---|---|---|---|---|---|
| B-001 | Blocker | Execution hardening | Option-selection and skeleton-rendering steps are compressed in the next handoff. | Add hard stop after option presentation until user selection is recorded. | Activation blocked. |
| B-002 | Blocker | Repository hardening | Existing public route files bypass the new section state machine. | Classify existing public files as live placeholder, legacy, superseded, rejected, or production-authorized. | Activation blocked. |
| B-003 | Blocker | Documentation and prompt hardening | Rejected v1.0.4 prototype remains discoverable without artifact-level quarantine. | Mark rejected prototype surface or create rejected-prototype index. | Activation blocked. |
| B-004 | Blocker | QR and domain hardening | Final-domain QR and indexing language conflict with activation-block clarity. | Add QR and domain activation boundary note. | Activation blocked. |
| B-005 | Blocker | CI and verification hardening | GitHub Pages workflow lacks validation and no statuses were observed. | Add validation or manual verification substitute. | Activation blocked. |
| R-001 | Required Correction | Claim-safety hardening | Claim validation infrastructure is referenced but missing. | Create claim register or claim data file and validation method. | Activation blocked until corrected or user-risk accepted. |
| R-002 | Required Correction | Claim-safety hardening | Existing public claims require renewed claim review. | Map current public claims to capability status. | Activation blocked until corrected or user-risk accepted. |
| R-003 | Required Correction | Execution hardening | Data and automation layer remains aspirational. | Create required data/scripts or manual verification substitute. | Activation blocked before production readiness. |
| R-004 | Required Correction | Documentation hardening | Multiple docs and prototypes compete for source-of-truth status. | Create current-source-of-truth execution index. | Activation blocked until corrected. |
| R-005 | Required Correction | Repository hardening | Direct-to-main execution remains under-governed. | Define branch/PR path or explicit urgent direct-to-main exception. | Activation blocked until corrected. |
| R-006 | Required Correction | Deployment hardening | DreamHost package criteria are undefined in executable repo terms. | Create deploy manifest or package checklist before production. | Blocks production deployment. |
| R-007 | Required Correction | QR and domain hardening | QR route existence is not separated from QR activation approval. | Create QR review record before activation. | Blocks QR activation. |
| SH-001 | Strong Hardening | Research hardening | Unverified research rows are acceptable only as excluded execution inputs. | Mark unverified rows as excluded from execution authority until verified. | User decision required if not corrected. |
| SH-002 | Strong Hardening | Performance hardening | Skeleton performance budget is absent. | Add CSS, asset, DOM, overflow, and no-external-resource budget. | User decision required if not corrected. |
| SH-003 | Strong Hardening | Security hardening | Security control is procedural, not enforced. | Add script, SVG, secret, form, and deploy-hook checks. | User decision required if not corrected. |
| SH-004 | Strong Hardening | Security and UX hardening | Mailto behavior requires production review. | Test inquiry behavior across mobile and desktop environments. | User decision required before production. |
| O-001 | Optional | CI hardening | Add Lighthouse production route review. | Record Lighthouse evidence where useful. | Optional. |
| O-002 | Optional | Visual review hardening | Add Playwright desktop and mobile screenshots. | Store review artifacts for future comparison. | Optional. |
| O-003 | Optional | Accessibility hardening | Add automated axe-style checks. | Pair automated checks with manual review. | Optional. |
| O-004 | Optional | Route governance | Add `data/site-status.json`. | Machine-readable route status. | Optional. |

## 4. Blocker Corrections

### B-001: Correct next handoff stop point

Required file target:

`docs/dfw-premium-website-builder-execution-handoff-prompt-v1.0.1.md`

Required correction:

Create a v1.0.1 full clean copy of the execution handoff prompt that separates the next action into two permitted phases:

1. Option presentation and recommendation only.
2. Skeleton rendering only after user selection or explicit user approval of the recommended option set.

Required acceptance criteria:

1. The prompt states that recommendations are not selections.
2. The prompt states that the acting session must stop after presenting the options.
3. The prompt states that no skeleton files may be created until user option selection is recorded.
4. The final standing for the option presentation phase does not claim skeleton readiness.

### B-002: Classify existing public route files

Required file target:

`docs/audits/dfw-public-surface-boundary-and-route-status-register-v1.0.0.md`

Required correction:

Create a route status register covering at minimum:

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
11. `sitemap.xml`
12. `robots.txt`
13. `assets/connect-qr.svg`

Required status values:

1. Live placeholder.
2. Legacy.
3. Superseded.
4. Rejected.
5. Production-authorized.
6. Preview-only.
7. Requires claim review.

Required acceptance criteria:

1. Every public route has one status.
2. Every public route identifies whether it may remain public.
3. Every public route identifies whether it may be used as builder input.
4. Every public route identifies whether claim review is required.

### B-003: Quarantine rejected v1.0.4 prototype surface

Required file target options:

1. `docs/prototypes/homepage-v1.0.4/README.md`
2. `docs/audits/dfw-rejected-prototype-index-v1.0.0.md`
3. Or a visible status marker in `docs/prototypes/homepage-v1.0.4/review.html` if explicitly authorized.

Required correction:

Mark `docs/prototypes/homepage-v1.0.4/review.html` as rejected, hard-failed, and prohibited as an execution basis.

Required acceptance criteria:

1. The prototype cannot be mistaken as approved.
2. The correction points to the hard failure record.
3. The correction states section-first skeleton is the only permitted next path.
4. No prototype content is reused as skeleton content.

### B-004: Clarify QR and final-domain activation standing

Required file target:

`docs/audits/dfw-qr-domain-activation-boundary-record-v1.0.0.md`

Required correction:

Create a QR and domain boundary record that distinguishes:

1. Route exists in repo.
2. Route exists on preview.
3. Route exists on production domain.
4. QR destination printed on assets.
5. QR destination activated for public scanning.
6. QR destination approved by user.
7. QR destination claim review status.

Required acceptance criteria:

1. `/connect` route existence is not treated as QR activation approval.
2. Final-domain canonical URLs are not treated as DreamHost production approval.
3. Printed QR references are not treated as route validation.
4. User approval is required before clearing QR activation.

### B-005: Add validation or manual verification substitute

Required file target options:

1. `.github/workflows/dfw-builder-validation.yml`
2. `docs/audits/dfw-builder-manual-verification-checklist-v1.0.0.md`

Required correction:

Add either executable validation or a manual verification substitute covering:

1. Allowed skeleton paths.
2. Blocked production paths.
3. Skeleton public text limits.
4. No JavaScript in skeleton.
5. No third-party scripts.
6. No external fonts.
7. No images or PDFs.
8. Claim-safety review.
9. Sponsor-surface review.
10. Mobile and accessibility review.
11. Link review.
12. Preview/prod boundary review.

Required acceptance criteria:

1. Validation exists before skeleton activation.
2. The validation result is cited in final execution response.
3. Failed validation blocks progression.

## 5. Required Corrections

### R-001: Create claim register or claim data file

Required target:

`docs/audits/dfw-public-claim-review-register-v1.0.0.md`

Optional future machine-readable target:

`data/claims.json`

Required acceptance criteria:

1. Each current public claim is listed.
2. Each claim maps to live, operator-assisted, development, or restricted capability.
3. Each claim maps to evidence or a manual workflow.
4. Each restricted or development claim has a public-use rule.

### R-002: Review public claims in route files

Required target:

Same as R-001 or a companion file.

Required acceptance criteria:

1. `index.html` claims reviewed.
2. `connect/index.html` claims reviewed.
3. `contact/index.html` claims reviewed.
4. `services/index.html` claims reviewed.
5. Service route claims reviewed.
6. JSON-LD schema reviewed.
7. Canonical and metadata claims reviewed.

### R-003: Create automation substitute

Required target:

`docs/audits/dfw-automation-readiness-gap-register-v1.0.0.md`

Required acceptance criteria:

1. Required data files are listed as present, missing, or deferred.
2. Required scripts are listed as present, missing, or deferred.
3. Manual substitute steps are listed for any missing automation.
4. Production readiness remains blocked until automation or substitute validation passes.

### R-004: Create source-of-truth index

Required target:

`docs/dfw-current-execution-source-of-truth-index-v1.0.0.md`

Required acceptance criteria:

1. Active builder module listed.
2. Active audit report listed.
3. Next authorized action listed.
4. Rejected prototypes listed.
5. Superseded homepage artifacts listed.
6. Public route status register linked.

### R-005: Define branch and PR governance

Required target:

`docs/dfw-github-execution-governance-and-branch-policy-v1.0.0.md`

Required acceptance criteria:

1. Default correction path uses branch and PR.
2. Direct-to-main exception requires explicit user authorization.
3. Emergency direct-to-main commits require post-commit fetch and verification.
4. Audit and correction files require commit SHA return.

### R-006: Create DreamHost deploy manifest

Required target:

`docs/deployment/dfw-dreamhost-deployment-package-manifest-v1.0.0.md`

Required acceptance criteria:

1. Included files listed.
2. Excluded files listed.
3. Prototype and docs exclusion listed.
4. Claim review prerequisite listed.
5. Mobile review prerequisite listed.
6. QR review prerequisite listed.
7. User approval prerequisite listed.
8. Rollback path listed.

### R-007: Create QR review record

Required target:

`docs/audits/dfw-qr-destination-review-record-v1.0.0.md`

Required acceptance criteria:

1. Exact QR destination confirmed.
2. Mobile load confirmed.
3. Route claim review confirmed.
4. Contact actions confirmed.
5. User approval recorded.
6. QR activation status recorded.

## 6. Strong Hardening Actions

### SH-001: Mark unverified research as excluded from execution authority

Target:

`docs/dfw-ai-governed-premium-website-builder-market-research-and-standards-map-v1.0.1.md`

Action:

Add language that unverified rows may remain in the market scan but cannot influence execution until verified.

### SH-002: Add skeleton performance budget

Target:

`docs/dfw-premium-website-builder-skeleton-rendering-playbook-v1.0.1.md`

Action:

Add skeleton performance checks for no external resources, no JavaScript, no images, CSS path review, no horizontal overflow, and lean DOM structure.

### SH-003: Add security review checklist

Target:

`docs/audits/dfw-static-site-security-review-checklist-v1.0.0.md`

Action:

Add checks for third-party scripts, analytics, unsafe SVG, secrets, forms, mailto behavior, and deploy hooks.

### SH-004: Review mailto inquiry UX

Target:

`docs/audits/dfw-contact-flow-mobile-and-mailto-review-v1.0.0.md`

Action:

Test mailto behavior on mobile and desktop and define fallback guidance.

## 7. Optional Hardening Actions

1. Add Lighthouse review records.
2. Add Playwright screenshot review records.
3. Add axe-style accessibility scan records.
4. Add `data/site-status.json`.
5. Add sponsor inventory governance before advertiser expansion.
6. Add visual regression records for section skeleton reviews.

## 8. Next Authorized Correction Mission Name

Recommended next correction mission:

`dfw_ai_governed_premium_website_builder_audit_corrections_blocker_clearance_package`

Recommended mission boundary:

Create correction files only. Do not create skeleton files. Do not edit homepage files unless the user explicitly authorizes artifact-level rejected/superseded markers. Do not deploy. Do not activate QR. Do not self-clear activation.

## 9. Final Register Standing

Final standing:

`CORRECTION REGISTER CREATED / BLOCKERS AND REQUIRED CORRECTIONS IDENTIFIED / ACTIVATION REMAINS BLOCKED PENDING USER EVALUATION AND CORRECTION SATISFACTION`
