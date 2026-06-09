# DFW Matchday Concierge — Prototype Status Register v1.0.0

**Mission:** `dfw_repo_source_of_truth_boundary_and_cleanup_stabilization_v1_0_0`  
**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** Prototype / PR / workflow classification-first stabilization record  

## 1. Purpose

This register classifies prototype, preview, handoff, audit, workflow, and PR surfaces before any cleanup movement, route replacement, deployment, PR merge, or prototype promotion.

This register does not approve production readiness.

## 2. Prototype classification ledger

| Surface | Classification | Boundary |
|---|---:|---|
| `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html` | active authoritative | Prototype reference base only. It may guide browser review and future public-route correction, but it is not production authority. |
| `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.18-raster-image-visibility-corrected.html` | preview-only | Raster image visibility correction candidate. Diagnostic / review use only. |
| `docs/prototypes/homepage-v1.0.4/review.html` | superseded | Earlier minimal premium gateway prototype. Do not use as the next homepage base. |
| `docs/prototyp-replica-v1.0.0/` | rejected | Typo / invalid prototype path if present. Requires tree evidence before archive movement. |
| `prototyp-replica-v1.0.0/` | rejected | Typo / invalid root prototype path if present. Requires tree evidence before archive movement. |

## 3. Workflow classification ledger

| Surface | Classification | Boundary |
|---|---:|---|
| `.github/workflows/pages-preview.yml` | preview-only | GitHub Pages preview workflow only. Preview is not approval. |
| `.github/workflows/deploy-dreamhost-preview.yml` | preview-only | Preview workflow only. Do not rerun through this mission. |

## 4. Audit and handoff directories

| Surface | Classification | Boundary |
|---|---:|---|
| `docs/audits/` | historical-retained | Audit evidence directory. Not an active build base. Later archive work requires a per-file manifest. |
| `docs/handoffs/` | historical-retained | Handoff and failure-record directory. Not an active build base. Later archive work requires a per-file manifest. |

## 5. Pull request classification ledger

| PR | Classification | Standing | Boundary |
|---|---:|---|---|
| PR #1 `dfw-platform-rebuild-opening-data-claim-layer` | unresolved / requires evidence | Open draft, unmerged, non-mergeable | Technical extraction only. Not merge-ready authority. Requires file-by-file extraction map. |
| PR #2 temporary GH Pages preview branch | historical-retained | Closed, unmerged, draft | Preview-history record only. Do not merge. |
| PR #3 superseded 48-hour stabilization candidate | superseded | Closed, unmerged, draft | Superseded. Do not merge. |

## 6. Archive-required candidates

| Candidate | Classification | Required precondition |
|---|---:|---|
| Rejected typo prototype paths | archive-required | Full repo tree evidence and archive manifest. |
| Superseded prototype surfaces | archive-required | Confirm no route or workflow dependency remains. |
| Superseded preview branches | archive-required | Preserve PR metadata and branch standing first. |
| Rejected / superseded audit and handoff subsets | archive-required | Per-file archive manifest. Do not archive whole directories blindly. |

## 7. Unresolved evidence items

| Item | Classification | Required evidence |
|---|---:|---|
| PR #1 extraction value | unresolved / requires evidence | Changed-file list and extraction map. |
| PR #1 claim/data files | unresolved / requires evidence | Claim, data, and component review before reuse. |
| DreamHost preview path | unresolved / requires evidence | Document root, target directory, and served URL evidence. |
| GitHub Pages preview state | unresolved / requires evidence | Exact preview URL, asset status, and screenshot evidence. |
| Typo prototype path presence | unresolved / requires evidence | Full repo tree listing or equivalent manifest. |
| Public claim readiness | unresolved / requires evidence | Claim-to-capability map. |
| Mobile and QR review | unresolved / requires evidence | Recorded review output before launch authority. |

## 8. Cleanup sequence

1. Validate this register and the companion source-of-truth / public-boundary registers on `main`.
2. Produce a full repo tree manifest for public routes, prototypes, audits, handoffs, workflows, and assets.
3. Create a prototype archive manifest without deleting files.
4. Create a PR #1 extraction map and copy nothing until the map is approved.
5. Create the public route claim and asset dependency manifest.
6. Only after validation, prepare a bounded correction package for the selected homepage/public route path.

## 9. Next package-native correction step

`dfw_public_route_claim_and_asset_dependency_manifest_v1_0_0`

This is the next safe correction because it connects the public route baseline to assets and claim validation without promoting a prototype or merging PR #1.

## 10. Hard stop

This register does not authorize deletion, archive movement, DreamHost deployment, GitHub Pages approval, QR activation, PR merge, or prototype promotion.
