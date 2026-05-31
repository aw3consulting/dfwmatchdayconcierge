# DFW Operating System GitHub Pages Preview Source Configuration Decision v1.0.0

## 1. Purpose

This file executes the controlled action:

`dfw_operating_system_github_pages_preview_source_configuration_decision`

The purpose is to determine the safest governed source configuration for opening the temporary GitHub Pages preview review surface after the active bounded frontend shell was confirmed preview-ready but the live Pages URL was not confirmed.

## 2. Decision Summary

Decision:

`CREATE GOVERNED GH-PAGES PREVIEW SOURCE FROM ACTIVE PR HEAD`

The safest next preview configuration is to create a governed `gh-pages` preview source from the active bounded frontend shell branch head.

This is selected because:

- the repository contains a Pages Preview workflow configured to deploy from `gh-pages`
- no existing `gh-pages` branch was found during branch search
- the active bounded shell exists on `dfw-platform-rebuild-opening-data-claim-layer`
- the active PR remains draft and cannot be treated as production
- DreamHost production must remain blocked
- DNS and production domain settings must remain unchanged
- a temporary GitHub Pages review surface is the approved preview host

## 3. Active Repo and Branch Standing

Active repo:

`aw3consulting/dfwmatchdayconcierge`

Active PR:

`https://github.com/aw3consulting/dfwmatchdayconcierge/pull/1`

PR state:

`open draft`

Base branch:

`main`

Active shell branch:

`dfw-platform-rebuild-opening-data-claim-layer`

Current active PR head SHA at decision:

`ad468166438bf363d577538fcf4e831f89278a99`

Repository visibility:

`public`

Repository permissions observed:

`admin, maintain, pull, push, triage`

## 4. Pages Workflow Standing

Existing Pages workflow:

`/.github/workflows/pages-preview.yml`

Workflow source behavior:

- triggered on pushes to `main`
- triggered on pushes to `gh-pages`
- supports `workflow_dispatch`
- checks out `gh-pages`
- deploys Pages artifact from repository root of the checked-out `gh-pages` branch

Implication:

The active PR branch is not deployed by the workflow unless the active shell is copied to or represented by `gh-pages`, or unless the workflow is changed under separate governance.

## 5. Alternatives Considered

### 5.1 Modify Pages Workflow

Decision:

`REJECTED FOR THIS STEP`

Reason:

Changing the workflow introduces unnecessary deployment-control surface area. The existing workflow already supports deployment from `gh-pages`.

### 5.2 Modify Repository Pages Settings

Decision:

`REJECTED FOR THIS STEP`

Reason:

Repository settings changes are outside file-level execution and carry a higher risk of unintended launch posture.

### 5.3 Use DreamHost Preview

Decision:

`REJECTED`

Reason:

DreamHost production deployment remains blocked until validation, mobile review, QR review, claim review, and explicit user approval pass.

### 5.4 Use Active PR Branch Directly As Pages Source

Decision:

`REJECTED FOR THIS STEP`

Reason:

The existing workflow deploys from `gh-pages`, and repository Pages source settings were not changed.

### 5.5 Create Governed `gh-pages` Preview Source From Active PR Head

Decision:

`SELECTED`

Reason:

This uses the existing Pages workflow path, avoids DreamHost, avoids DNS changes, avoids production-domain changes, and creates a bounded temporary review surface that can be traced back to the active PR head SHA.

## 6. Selected Configuration

Selected preview source branch:

`gh-pages`

Selected source commit:

`ad468166438bf363d577538fcf4e831f89278a99`

Selected preview host pattern:

`https://aw3consulting.github.io/dfwmatchdayconcierge/`

Selected QR preview path pattern:

`https://aw3consulting.github.io/dfwmatchdayconcierge/connect/`

Preview source handling:

`Create gh-pages from active PR head if missing. If gh-pages later exists, update only under governed preview refresh control.`

## 7. Controls Required Before Publication

Before creating or updating `gh-pages`, record:

1. source branch
2. source commit SHA
3. target branch
4. expected preview URL
5. expected QR preview path
6. DreamHost block status
7. final launch block status
8. live AI/payment/dispatch/routing/authentication block status
9. official affiliation and fulfillment claim block status

## 8. Prohibited During Preview Source Configuration

Do not change:

- DreamHost configuration
- DNS records
- production domain settings
- final QR production destination
- payment processor configuration
- backend authentication
- live AI systems
- live dispatch systems
- live routing systems
- official marks
- tournament marks
- team marks
- unapproved photography
- unapproved Tahoe imagery
- affiliate, ad, API, or third-party integrations

## 9. Required Post-Configuration Verification

After `gh-pages` is created or updated, verify:

1. branch exists
2. branch points to the selected source commit or documented publication commit
3. Pages workflow triggers or can be triggered
4. preview URL resolves
5. `/connect/` preview path resolves
6. homepage serves the bounded shell
7. DreamHost remains untouched
8. final launch remains blocked
9. full preview review record can be created only after live review evidence is captured

## 10. Required Next Package

Before branch creation or update, create a governed execution package:

`docs/dfw-operating-system-gh-pages-preview-source-publication-package-v1.0.0.md`

The package must define:

- exact source SHA
- target branch
- branch creation/update method
- prohibited changes
- expected preview URL
- expected QR preview path
- post-publication verification steps
- review record requirements
- rollback or refresh rule

## 11. Production Block Confirmation

DreamHost production deployment:

`BLOCKED`

Final public launch:

`BLOCKED`

Final QR production use:

`BLOCKED`

Live AI, payment, dispatch, routing, authentication, official affiliation, credential validation, and fulfillment automation:

`BLOCKED`

## 12. Final Decision

The preview source configuration decision is complete.

The selected path is to create a governed `gh-pages` preview source from the active PR head SHA:

`ad468166438bf363d577538fcf4e831f89278a99`

No branch creation, branch update, workflow change, Pages settings change, DNS change, DreamHost change, or production deployment action is authorized by this decision file alone.

## 13. Next Controlled Action

The next controlled action is:

`dfw_operating_system_gh_pages_preview_source_publication_package`

Purpose:

Create the governed package that authorizes and bounds the `gh-pages` preview source publication from the active bounded frontend shell, then proceed to preview source publication only if the package passes its own controls.
