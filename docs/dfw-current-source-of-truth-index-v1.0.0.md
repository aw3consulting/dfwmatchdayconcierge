# DFW Matchday Concierge — Current Source-of-Truth Index v1.0.0

**Mission:** `dfw_repo_source_of_truth_boundary_and_cleanup_stabilization_v1_0_0`  
**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** Structural-Governance-Correction / classification-first stabilization layer  

## 1. Purpose

This file establishes the current source-of-truth boundary before any cleanup move, production deployment, DreamHost workflow run, public route replacement, prototype promotion, or PR merge.

This index does **not** approve production readiness. It does **not** activate the QR destination. It does **not** promote any prototype into the public route surface. It only classifies existing repo surfaces so the next correction can proceed without source-of-truth competition.

## 2. Classification taxonomy

| Classification | Meaning |
|---|---|
| active authoritative | Governs the current repo state for a defined scope. May be authoritative for governance, current public baseline, or prototype reference only. It is not automatically production-ready. |
| preview-only | May be used for visual or technical review only. Must not be treated as public approval or production authority. |
| superseded | Replaced by a later approach or locked path. Must not be used as the next execution base. |
| rejected | Known bad, failed, typo, or invalid execution surface. Must not be used except as failure evidence. |
| historical-retained | Preserved as audit, handoff, or project history. Not an active execution base. |
| archive-required | Should be moved into a controlled archive package in a later cleanup step after index validation. Do not delete during this mission. |
| unresolved / requires evidence | Cannot be promoted, merged, deployed, or used as authority until evidence is collected and recorded. |

## 3. Current active authoritative surfaces

| Surface | Classification | Authority scope | Boundary / notes |
|---|---:|---|---|
| `docs/dfw-current-source-of-truth-index-v1.0.0.md` | active authoritative | Source-of-truth classification index | This file controls cleanup sequencing and prevents prototype / public route / PR authority drift. |
| `docs/dfw-public-surface-boundary-register-v1.0.0.md` | active authoritative | Public surface classification register | Companion register for current public route boundaries. |
| `docs/dfw-prototype-status-register-v1.0.0.md` | active authoritative | Prototype and PR status register | Companion register for prototype, PR, workflow, and archive status. |
| `README.md` | active authoritative | Repo orientation only | Identifies the repo as the static website and records the primary QR destination. Not enough by itself to establish launch readiness. |
| `index.html` | active authoritative | Current public homepage baseline only | Current public root surface. Not the approved final production homepage. Requires validation and claim review before replacement or launch authority. |
| `connect/index.html` | active authoritative | Current public connect route baseline only | Current QR destination route baseline. QR activation standing is unchanged; no new activation is approved by this file. |
| `contact/index.html` | active authoritative | Current public inquiry route baseline only | Static inquiry route. Requires claim / capability validation before launch authority. |
| `services/index.html` | active authoritative | Current public services route baseline only | Static service summary route. Requires claim / capability validation before launch authority. |
| `private-transportation/index.html` | active authoritative | Current public service route baseline only | Public route included by sitemap. |
| `airport-transfers/index.html` | active authoritative | Current public service route baseline only | Public route included by sitemap and homepage service card. |
| `matchday-logistics/index.html` | active authoritative | Current public service route baseline only | Public route included by sitemap and homepage service card. |
| `concierge-hospitality/index.html` | active authoritative | Current public service route baseline only | Public route included by sitemap and homepage service card. |
| `group-vip-transportation/index.html` | active authoritative | Current public service route baseline only | Public route included by sitemap and homepage service card. |
| `luggage-coordination/index.html` | active authoritative | Current public service route baseline only | Public route included by sitemap and homepage service card. |
| `sitemap.xml` | active authoritative | Current public URL inventory | Defines the currently published route set. Must be updated only after route authority changes. |
| `robots.txt` | active authoritative | Current crawler boundary | Allows crawling and points to the sitemap. Must be reviewed before any public indexing change. |
| `assets/site.css` | active authoritative | Current public CSS baseline | Supports current public route baseline. Not the final design system authority. |
| `assets/site.js` | active authoritative | Current public inquiry form script baseline | Handles static mailto inquiry behavior. Not a dynamic booking system. |
| `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html` | active authoritative | Prototype reference base only | Approved prototype base for browser review / visual replication work. Not production and not public-route authority. |

## 4. Preview-only surfaces

| Surface | Classification | Boundary / notes |
|---|---:|---|
| `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.18-raster-image-visibility-corrected.html` | preview-only | Raster image visibility correction candidate / diagnostic preview surface. Must not become production by default. |
| `.github/workflows/pages-preview.yml` | preview-only | GitHub Pages review workflow only. GitHub Pages is not approval, launch authority, or production readiness. |
| `.github/workflows/deploy-dreamhost-preview.yml` | preview-only | DreamHost preview deployment workflow exists, but rerun is blocked by this mission. No production deployment is authorized. |

## 5. Superseded surfaces

| Surface | Classification | Boundary / notes |
|---|---:|---|
| `docs/prototypes/homepage-v1.0.4/review.html` | superseded | Prior minimal premium gateway prototype. Superseded by PDF-reference-first replication path and v1.0.10 prototype base. |
| PR #3 `dfw-48-hour-public-launch-stabilization-v1.0.1` | superseded | Closed, unmerged, draft 48-hour stabilization candidate. Do not merge and do not use as base. |

## 6. Rejected surfaces

| Surface | Classification | Boundary / notes |
|---|---:|---|
| `docs/prototyp-replica-v1.0.0/` | rejected | Typo / invalid prototype path if present. Must not be used as an approval or build base. Full tree evidence still required before archive movement. |
| `prototyp-replica-v1.0.0/` | rejected | Typo / invalid root prototype path if present. Must not be used as an approval or build base. Full tree evidence still required before archive movement. |

## 7. Historical-retained surfaces

| Surface | Classification | Boundary / notes |
|---|---:|---|
| `docs/audits/` | historical-retained | Evidence and audit history. Must remain available until an archive package indexes it. Individual rejected/superseded records may later move to archive. |
| `docs/handoffs/` | historical-retained | Handoff and failure records. Must remain available until an archive package indexes it. Individual rejected/superseded records may later move to archive. |
| PR #2 `gh-pages` temporary preview branch | historical-retained | Closed, unmerged temporary GitHub Pages preview PR. It documents preview history only. |

## 8. Archive-required surfaces

| Surface | Classification | Boundary / notes |
|---|---:|---|
| Rejected typo prototype paths after tree verification | archive-required | Archive only after confirming exact paths and contents. Do not delete. |
| Superseded prototype branches / previews after register validation | archive-required | Archive only after preserving evidence and confirming no active route dependency. |
| Superseded and rejected handoff/audit subsets after evidence index | archive-required | Do not archive the entire `docs/audits/` or `docs/handoffs/` directories without a per-file archive manifest. |

## 9. Unresolved / requires evidence surfaces

| Surface | Classification | Evidence needed before action |
|---|---:|---|
| PR #1 `dfw-platform-rebuild-opening-data-claim-layer` | unresolved / requires evidence | Open draft, unmerged, non-mergeable. May be used only as a technical extraction source. Requires file-by-file extraction map before any usable data, claim, or component is copied into `main`. |
| DreamHost preview document root / target path | unresolved / requires evidence | Prior standing includes DreamHost preview path and document-root uncertainty. Do not rerun workflow until target directory, served URL, and validation gate are confirmed. |
| GitHub Pages preview branch / live preview state | unresolved / requires evidence | Preview-only. Must not be treated as approval. Requires explicit route, asset, and screenshot evidence before a review statement. |
| Public claims across current routes | unresolved / requires evidence | Must be mapped to live, operator-assisted, development, or restricted capability before final launch authority. |
| Mobile review | unresolved / requires evidence | Required before production deployment and QR approval. |
| QR review | unresolved / requires evidence | Current QR destination is known, but activation standing is unchanged. Requires route validation before QR approval. |
| Full repo tree for typo prototype paths | unresolved / requires evidence | Path-specific `index.html` fetch is insufficient to prove full absence or contents. Requires full tree listing or equivalent manifest before movement. |

## 10. PR boundary

| PR | Classification | Standing | Boundary |
|---|---:|---|---|
| PR #1 `dfw-platform-rebuild-opening-data-claim-layer` | unresolved / requires evidence | Open draft / unmerged / non-mergeable | Technical extraction only. Not merge-ready authority. |
| PR #2 temporary GH Pages preview branch | historical-retained | Closed / unmerged / draft | Preview history only. Do not merge. |
| PR #3 superseded 48-hour stabilization candidate | superseded | Closed / unmerged / draft | Superseded by PDF-reference-first path. Do not merge. |

## 11. Recommended cleanup sequence

1. Freeze production and preview execution: no DreamHost deployment, no DreamHost rerun, no PR merge, no QR activation, no prototype promotion.
2. Validate this classification layer on `main`.
3. Produce a full repo tree manifest focused on public routes, prototypes, audits, handoffs, workflows, assets, and branches.
4. Create a per-file archive manifest for rejected and superseded prototype paths, old preview branches, and failed handoff subsets.
5. Extract useful technical data from PR #1 only through a file-by-file extraction map; do not merge PR #1.
6. Reconcile public claims against the DFW capability map: live, operator-assisted, development, restricted, or not allowed.
7. Choose a single homepage correction base: current public baseline vs v1.0.10 prototype reference conversion path.
8. Package the next correction as a bounded PR or direct main update, depending on governance approval, with no deployment side effect.
9. Run mobile, route, asset, claim, QR, and preview validation gates.
10. Only after validation and user approval, prepare DreamHost production deployment readiness.

## 12. Next package-native correction step

`dfw_public_route_claim_and_asset_dependency_manifest_v1_0_0`

Required output for the next package:

- Full public route inventory from `sitemap.xml` and actual repo paths.
- Asset dependency map for every public route.
- Claim-to-capability map for every public-facing claim.
- Current image format and path usage map, including SVG vs PNG references.
- PR #1 technical extraction candidate map without merge authority.
- DreamHost / GitHub Pages workflow boundary check without workflow execution.

## 13. Hard stop

This index does not authorize deletion, movement, deployment, DreamHost workflow rerun, public route replacement, prototype promotion, QR activation, or PR merge.
