# DFW Operating System GH-Pages Preview Source Publication Package v1.0.0

## 1. Purpose

This file executes the controlled action:

`dfw_operating_system_gh_pages_preview_source_publication_package`

The purpose is to authorize and bound creation of a temporary GitHub Pages preview source branch for review of the bounded static frontend shell.

This package does not itself create or update `gh-pages`.

## 2. Governing Decision

This package is governed by:

`docs/dfw-operating-system-github-pages-preview-source-configuration-decision-v1.0.0.md`

Decision standing:

`CREATE GOVERNED GH-PAGES PREVIEW SOURCE FROM ACTIVE PR HEAD`

## 3. Current Active PR Standing

Active repo:

`aw3consulting/dfwmatchdayconcierge`

Active PR:

`https://github.com/aw3consulting/dfwmatchdayconcierge/pull/1`

PR state:

`open draft`

Base branch:

`main`

Source branch:

`dfw-platform-rebuild-opening-data-claim-layer`

Source branch head SHA for this publication package:

`5e250798f6229f0c6af7a6566226a61fe78ebc01`

Target preview branch:

`gh-pages`

Expected preview URL pattern:

`https://aw3consulting.github.io/dfwmatchdayconcierge/`

Expected QR preview path pattern:

`https://aw3consulting.github.io/dfwmatchdayconcierge/connect/`

## 4. Publication Scope

This package authorizes only one bounded action:

`Create gh-pages from source branch head SHA 5e250798f6229f0c6af7a6566226a61fe78ebc01 if gh-pages does not exist.`

If `gh-pages` already exists at execution time, do not force-update it under this package. Return to governance and create a refresh package instead.

## 5. Allowed Publication Method

Allowed method:

- create a new `gh-pages` branch pointing to the selected source branch head SHA

Allowed target:

- `gh-pages`

Allowed source SHA:

- `5e250798f6229f0c6af7a6566226a61fe78ebc01`

Allowed result:

- temporary GitHub Pages review source for bounded frontend shell review

## 6. Prohibited Publication Actions

This package does not authorize:

- DreamHost deployment
- DNS changes
- production domain changes
- final QR production changes
- repository Pages settings changes
- workflow changes
- force-updating an existing `gh-pages` branch
- merging the active PR
- marking the active PR ready for review
- closing the active PR
- final launch
- live AI intake automation
- live authentication
- live payment processing
- live deposit collection
- live dispatch
- live routing
- official affiliation claims
- credential validation claims
- fulfillment guarantees
- affiliate, ad, API, or third-party integrations

## 7. Required Pre-Publication Checks

Before branch creation, verify:

1. active PR remains open
2. active PR remains draft
3. source branch is `dfw-platform-rebuild-opening-data-claim-layer`
4. source SHA is `5e250798f6229f0c6af7a6566226a61fe78ebc01`
5. no existing `gh-pages` branch is found
6. DreamHost production remains blocked
7. final public launch remains blocked
8. live AI, payment, dispatch, routing, authentication, official affiliation, credential validation, and fulfillment automation remain blocked

## 8. Required Post-Publication Verification

After creating `gh-pages`, verify:

1. `gh-pages` branch exists
2. `gh-pages` points to `5e250798f6229f0c6af7a6566226a61fe78ebc01` or documented publication SHA
3. Pages workflow can deploy from `gh-pages`
4. candidate preview URL is checked
5. candidate `/connect/` preview path is checked
6. homepage shell is reviewed from the live preview URL before any review record is finalized
7. DreamHost remains untouched
8. final public launch remains blocked
9. production QR use remains blocked

## 9. Required Publication Record

After branch creation, create:

`docs/dfw-operating-system-gh-pages-preview-source-publication-record-v1.0.0.md`

The record must include:

- source branch
- source SHA
- target branch
- branch creation result
- preview URL checked
- QR preview path checked
- Pages workflow status if observable
- blockers remaining
- DreamHost block confirmation
- final launch block confirmation
- next controlled action

## 10. Required Preview Review Record After Live URL Confirmation

After the preview URL is confirmed live, create:

`docs/dfw-operating-system-github-pages-preview-review-record-v1.0.0.md`

The review record must include:

- preview URL reviewed
- review date
- reviewed branch
- reviewed commit SHA
- pages reviewed
- mobile review result
- QR review result
- claim review result
- map review result
- monetization review result
- asset review result
- accessibility observations
- performance observations
- blockers found
- required fixes
- production deployment status
- next controlled action

## 11. Rollback and Refresh Rule

If `gh-pages` publishes the wrong source, fails to deploy, or exposes a claim failure:

1. stop preview review
2. preserve DreamHost block
3. preserve final launch block
4. create a preview correction or refresh package
5. do not force-push without a governed refresh package

If the active PR branch advances after publication, do not automatically update `gh-pages`. Create a governed refresh package first.

## 12. Review Surface Reminder

GitHub Pages is allowed only as a temporary review surface.

It is not a production host.

It is not the final domain.

It is not the final QR production destination.

The final production domain remains:

`https://dfwmatchdayconcierge.com`

The final production QR destination remains:

`https://dfwmatchdayconcierge.com/connect`

## 13. Production Block Confirmation

DreamHost production deployment:

`BLOCKED`

Final public launch:

`BLOCKED`

Final QR production use:

`BLOCKED`

Live AI, payment, dispatch, routing, authentication, official affiliation, credential validation, and fulfillment automation:

`BLOCKED`

## 14. Publication Authorization

This package authorizes a bounded `gh-pages` branch creation only if pre-publication checks pass.

Authorized command equivalent:

`Create branch gh-pages at 5e250798f6229f0c6af7a6566226a61fe78ebc01`

No other publication or deployment action is authorized.

## 15. Next Controlled Action

The next controlled action is:

`dfw_operating_system_gh_pages_preview_source_publication_execution`

Purpose:

Create `gh-pages` from the authorized source SHA if it does not exist, then create the required publication record and proceed to live preview URL confirmation only after the branch publication state is verified.
