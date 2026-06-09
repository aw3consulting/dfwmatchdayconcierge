# DFW Matchday Concierge — Homepage v1.0.10 Authorized Preview Publication and Raster Visibility Correction Record v1.0.0

**Mission:** `dfw_homepage_v1_0_10_authorized_preview_publication_and_raster_visibility_correction_package_v1_0_0`  
**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** Preview publication path corrected / exact v1.0.10 preview URL established / browser visual validation still requires external served-URL confirmation  

## 1. Controlling authority

Controlling authority:

`docs/dfw-homepage-v1.0.10-authority-relock-and-drift-correction-record-v1.0.0.md`

Amendment authority:

`docs/dfw-homepage-v1.0.10-prior-records-amendment-and-superseding-notes-v1.0.0.md`

Latest validation record:

`docs/dfw-homepage-v1.0.10-served-preview-raster-logo-and-information-hub-validation-record-v1.0.0.md`

Homepage authority surface:

`docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html`

## 2. Preview-only publication correction

The GitHub Pages preview workflow was corrected so Pages can publish from `main` instead of the stale `gh-pages` branch.

Updated file:

`.github/workflows/pages-preview.yml`

Commit:

`f9db0f39ae556bcea73e363b10c2482442cced75`

Correction made:

- Pages workflow push trigger now targets `main` only.
- Pages workflow still supports `workflow_dispatch`.
- Pages checkout now explicitly checks out `main`.
- Pages artifact path remains `.` so the existing v1.0.10 prototype path and assets can be served from the repository tree.
- DreamHost workflow was not changed or rerun.

## 3. Exact served preview URL established

Expected authorized GitHub Pages preview-only URL:

`https://aw3consulting.github.io/dfwmatchdayconcierge/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html`

Boundary:

- This is preview-only evidence, not approval.
- GitHub Pages must not be treated as production readiness.
- This URL must be externally opened after Pages deployment completes before visual validation is claimed complete.

## 4. HTTP / non-404 evidence

| Evidence item | Result | Finding |
|---|---:|---|
| `main` contains v1.0.10 path | pass | `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html` exists on `main`. |
| Pages workflow now publishes `main` | pass | `.github/workflows/pages-preview.yml` now checks out `main`. |
| Exact GitHub Pages URL established | pass | URL is derived from Pages base plus the v1.0.10 repository path. |
| External HTTP status check | unresolved / requires evidence | The execution environment could not independently resolve/open the GitHub Pages URL. |
| Non-404 browser proof | unresolved / requires evidence | Must be confirmed by opening the exact URL externally or through a browser-capable validation run. |

Result: preview publication path is corrected and exact URL is established. Actual non-404 and browser-rendered validation are not claimed until the URL is externally verified.

## 5. Raster asset validation results

Source/path validation confirms v1.0.10 references raster-critical PNG assets and representative assets exist on `main`. Served visual validation remains pending.

| Target | Source/path result | Served visual result |
|---|---:|---:|
| Header raster logo / canary | pass: `./assets/images/logos/dfw-logo-header-raster-v1.0.2.png` exists on `main` | unresolved / requires served preview |
| Footer logo | source reference present | unresolved / requires served preview |
| Hero image | pass: `./assets/images/hero/dfw-hero-fw-att-dallas-crowd-flags-v1.0.0.png` exists on `main` | unresolved / requires served preview |
| AI inquiry image | pass: `./assets/images/cards/ai-inquiry-command-chip-v1.0.0.png` exists on `main` | unresolved / requires served preview |
| Hub icons | pass: v1.0.10 references hub PNG icons; representative hub icon exists on `main` | unresolved / requires served preview |
| DFW map/routes image | pass: `./assets/images/maps/dfw-matchday-routes-map-v1.0.0.png` exists on `main` | unresolved / requires served preview |
| Driver image | source reference present: `./assets/images/cards/driver-hub-visual-v1.0.0.png` | unresolved / requires served preview |
| Concierge image | source reference present: `./assets/images/cards/concierge-hub-visual-v1.0.0.png` | unresolved / requires served preview |
| Fulfillment image | source reference present: `./assets/images/cards/fulfillment-providers-visual-v1.0.0.png` | unresolved / requires served preview |
| Social icons | source references present under `./assets/icons/social/*.png` | unresolved / requires served preview |

## 6. Logo visibility result

| Logo target | Source/path result | Visual result |
|---|---:|---:|
| Header logo asset | pass: raster PNG exists on `main` | unresolved / requires served preview |
| Header logo CSS visibility hardening | pass: v1.0.10 patch CSS contains visible image/logo rules | unresolved / requires served preview |
| Footer logo source reference | pass: footer references PNG logo | unresolved / requires served preview |
| Footer logo CSS visibility hardening | pass: v1.0.10 patch CSS contains footer/logo visibility rules | unresolved / requires served preview |

No visible logo claim is made until the exact preview URL is opened and visually checked.

## 7. CSS load validation

| CSS dependency | Source/path result | Served result |
|---|---:|---:|
| `./assets/css/replica-v1.0.7.css` | pass: file exists on `main` | unresolved / requires served preview |
| `./assets/css/replica-v1.0.10.css` | pass: file exists on `main` | unresolved / requires served preview |

The v1.0.10 page references both CSS files in order. Served CSS loading must still be browser-verified at the exact preview URL.

## 8. Inline JS validation

| JS target | Source result | Runtime result |
|---|---:|---:|
| Date selector JS | pass: inline date selector script present | unresolved / requires served browser test |
| Raster diagnostics JS | pass: inline raster failure diagnostic script present | unresolved / requires served browser test |
| Page rendering impact | source does not show replacement of v1.0.10 structure | unresolved / requires served browser test |

No runtime claim is made until browser execution is confirmed.

## 9. Information-hub / command-hub section visual result

Source preservation remains confirmed. Visual rendering remains pending served preview check.

| Section | Source preservation | Visual result |
|---|---:|---:|
| Header navigation | pass | unresolved / requires served preview |
| Title Sponsor Hero | pass | unresolved / requires served preview |
| Matchday Planning Command Hub Activated hero | pass | unresolved / requires served preview |
| AI-assisted inquiry preview | pass | unresolved / requires served preview |
| Operating Command Hubs | pass | unresolved / requires served preview |
| DFW Matchday Map & Routes | pass | unresolved / requires served preview |
| Team Hubs | pass | unresolved / requires served preview |
| Sponsor / advertising rail | pass | unresolved / requires served preview |
| Drivers panel | pass | unresolved / requires served preview |
| Concierges panel | pass | unresolved / requires served preview |
| Fulfillment Providers panel | pass | unresolved / requires served preview |
| Independent service scope / public claims | pass | unresolved / requires served preview |
| Footer information hub | pass | unresolved / requires served preview |

Result: v1.0.10 structure remains preserved and authoritative. It was not replaced with the current public booking/service baseline.

## 10. Mobile viewport result

| Mobile target | Result | Finding |
|---|---:|---|
| v1.0.10 viewport meta | source-level pass | v1.0.10 includes viewport meta. |
| Mobile served visual review | unresolved / requires evidence | Must be performed after exact preview URL is confirmed non-404. |
| Mobile raster/logo review | unresolved / requires evidence | Must be performed after exact preview URL is confirmed non-404. |

## 11. v1.0.18 / v1.0.19 boundary

v1.0.18 / v1.0.19 remains diagnostic / preview-only.

No v1.0.18 or v1.0.19 draft was promoted over v1.0.10.

Permitted lessons only:

1. PNG visibility hardening.
2. Header/footer logo sizing and object-fit rules.
3. Raster failure labeling.
4. Asset canary diagnostics.
5. Host/path assumptions must be proven by served preview.

## 12. Prohibited actions confirmation

This package did **not**:

- delete files,
- move files,
- deploy to DreamHost production,
- rerun DreamHost workflow,
- merge PR #1,
- promote v1.0.18 or v1.0.19,
- promote current `index.html` as homepage authority,
- replace v1.0.10 with service-card / booking-style baseline,
- claim production readiness.

## 13. Remaining blockers

1. GitHub Pages deployment from `main` must complete after workflow correction.
2. Exact preview URL must be externally opened and confirmed non-404.
3. Header logo visibility must be visually verified.
4. Footer logo visibility must be visually verified.
5. Every v1.0.10 raster PNG must be verified from the served preview.
6. Hero image must be visually verified.
7. AI inquiry image must be visually verified.
8. Hub icons must be visually verified.
9. DFW map/routes image must be visually verified.
10. Driver, concierge, and fulfillment images must be visually verified.
11. Footer/social raster assets must be visually verified where present.
12. CSS files must be confirmed served and loaded.
13. Inline JS date selector and raster diagnostics must be runtime-tested.
14. Information-hub sections must be visually verified from the exact URL.
15. Mobile viewport must be captured or reviewed.
16. User approval remains required.

## 14. Production readiness standing

Production readiness remains **blocked**.

Reason: this package corrects the GitHub Pages preview publication path and establishes the exact v1.0.10 preview URL, but it does not prove external HTTP status, visual rendering, raster visibility, mobile rendering, or user approval.

## 15. Next safe correction step

Execute:

`dfw_homepage_v1_0_10_live_pages_url_visual_validation_and_mobile_evidence_record_v1_0_0`

Recommended scope:

1. Open the exact GitHub Pages v1.0.10 URL.
2. Confirm HTTP 200 / non-404.
3. Visually confirm v1.0.10 page served, not current public baseline.
4. Confirm header and footer logo visibility.
5. Confirm every raster image category renders.
6. Confirm CSS loaded.
7. Confirm inline JS does not break rendering.
8. Capture desktop and mobile viewport evidence.
9. Record remaining blockers and production readiness standing.

## 16. Hard stop

No future execution may claim v1.0.10 visual validation complete until the exact preview URL is actually opened and checked. No future execution may replace v1.0.10 with the current public booking/service baseline or treat current `index.html` as homepage authority unless the user explicitly unlocks and changes the authority decision.
