# DFW Premium Website Builder Skeleton Rendering Playbook v1.0.1

## 1. Controlled Action

This file is the active corrected version of the DFW Premium Website Builder Skeleton Rendering Playbook.

It supersedes:

`docs/dfw-premium-website-builder-skeleton-rendering-playbook-v1.0.0.md`

This revision satisfies strong hardening action SH-002 by adding a skeleton performance budget and clearer validation checkpoints.

## 2. Status

Status: ACTIVE CORRECTED SKELETON PLAYBOOK

Activation standing:

`SKELETON RENDERING BLOCKED UNTIL USER OPTION SELECTION IS RECORDED / PERFORMANCE BUDGET CREATED / FINAL CONTENT, PDF CAPTURE, DREAMHOST DEPLOYMENT, AND QR ACTIVATION REMAIN BLOCKED`

## 3. Hard Start Rule

Skeleton rendering may not start until the user explicitly selects one option for each section or explicitly approves the recommended option set as the selected execution basis.

No inferred approval, recommendation, or prior preference may be treated as option selection.

## 4. Allowed Skeleton Content

Only the required section name and authorized tagline may appear as public-facing text during skeleton rendering.

The authorized section model remains:

1. Header: Premium identity lockup and top-level access.
2. Navigation: Concise visitor, sponsor, and trust pathways.
3. Hero: Minimal premium introduction for DFW Matchday Concierge.
4. Section 1: Service orientation without detail overload.
5. Section 2: Audience pathway selection for visitors and partners.
6. Section 3: Premium sponsor and partner opportunity surface.
7. Section 4: Trust, responsibility, and independent platform clarity.
8. Footer: Compact closure, links, and disclaimer.

## 5. Required Skeleton Paths

Future skeleton rendering may create or edit only:

1. `docs/prototypes/homepage-section-skeleton-v1.0.0/review.html`
2. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/tokens.css`
3. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/section-skeleton.css`
4. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/preview-fixes.css`
5. `docs/prototypes/homepage-section-skeleton-v1.0.0/README.md`

## 6. Skeleton Performance Budget

| Performance item | Budget rule | Evidence required |
|---|---|---|
| JavaScript | None in the skeleton path. | File review. |
| External fonts | None loaded in skeleton review. | CSS and HTML review. |
| External CSS | No framework or CDN CSS imports. | CSS and HTML review. |
| Images | No image assets in skeleton rendering. | HTML and path review. |
| PDFs | No PDF assets in skeleton rendering. | Path review. |
| Third-party resources | No third-party embeds, analytics, or remote review dependencies. | HTML review. |
| CSS structure | Only approved CSS files in the approved skeleton path. | File path review. |
| DOM density | Eight required sections plus minimal wrappers only. | HTML review. |
| Horizontal overflow | None at required viewport widths. | Responsive review. |
| Layout shift | Static CSS layout only. | Review note. |

## 7. Responsive Review Rules

Required viewport checks:

1. 390px.
2. 430px.
3. 768px.
4. 1024px.
5. 1280px.
6. 1440px.

Pass criteria:

1. No horizontal overflow.
2. Section name remains visible.
3. Tagline remains readable.
4. Section spacing remains clear.
5. Header and navigation remain compact.
6. Sponsor surface remains secondary.
7. Trust surface remains readable.
8. Footer remains compact.

## 8. Accessibility Review Rules

Working target:

`WCAG 2.2 AA`

Required checks:

1. Semantic section structure.
2. Proper landmark intent.
3. Contrast review.
4. Keyboard-safe placeholders.
5. Visible focus if any placeholder is interactive.
6. No color-only meaning.
7. No image-only text.
8. No hidden search text.
9. Reduced motion readiness.
10. Legible type sizes.

## 9. Required Review Output After Future Skeleton Rendering

A future skeleton rendering response must report:

1. User option selection evidence.
2. Created skeleton paths.
3. Commit SHA.
4. Exact fetch verification from `main`.
5. Skeleton content review.
6. CSS token review.
7. Performance budget review.
8. Desktop review.
9. Mobile review.
10. Accessibility review.
11. Claim-safety review.
12. Sponsor surface review.
13. Remaining blocked actions.

## 10. Final Determination

Strong hardening action SH-002 is satisfied.

Final standing:

`CORRECTED SKELETON PLAYBOOK CREATED / PERFORMANCE BUDGET ADDED / SKELETON RENDERING REMAINS BLOCKED UNTIL USER OPTION SELECTION IS RECORDED`.
