# DFW Premium Website Builder Skeleton Rendering Playbook v1.0.0

## 1. Controlled Action

This file defines how the DFW AI-Governed Premium Website Builder Module renders section skeletons.

The skeleton stage exists to review structure, CSS, spacing, hierarchy, responsive behavior, section boundaries, and premium visual logic before any final content appears.

This file does not authorize homepage generation, final homepage content, PDF capture, DreamHost deployment, QR activation, image generation, or production approval.

## 2. Status

Status: CREATED FOR MAIN BRANCH GOVERNED MODULE BUILD

The next execution may build only the CSS-rendered section skeleton and only after it verifies the module files on `main` and presents section options.

## 3. Skeleton Stage Definition

A skeleton is a browser-rendered HTML/CSS review artifact that shows only the approved section name and approved section tagline for each required homepage section.

A skeleton is not:

1. A homepage.
2. A content draft.
3. A final design.
4. A PDF.
5. A visual mockup image.
6. A production file.
7. A QR destination.
8. A DreamHost deployment.

The skeleton stage answers only these questions:

1. Does each section exist as a clear visual unit?
2. Does the selected layout option work in CSS?
3. Does the desktop hierarchy feel premium?
4. Does the mobile stack preserve clarity?
5. Does the section spacing support page flow?
6. Does the section boundary prevent content drift?
7. Does the sponsor surface remain controlled?
8. Does the trust surface remain clear and restrained?

## 4. Allowed Skeleton Content

Only the following public-facing text may appear in the skeleton:

| Section | Allowed section name | Allowed tagline |
|---|---|---|
| Header | Header | Premium identity lockup and top-level access. |
| Navigation | Navigation | Concise visitor, sponsor, and trust pathways. |
| Hero | Hero | Minimal premium introduction for DFW Matchday Concierge. |
| Section 1 | Section 1 | Service orientation without detail overload. |
| Section 2 | Section 2 | Audience pathway selection for visitors and partners. |
| Section 3 | Section 3 | Premium sponsor and partner opportunity surface. |
| Section 4 | Section 4 | Trust, responsibility, and independent platform clarity. |
| Footer | Footer | Compact closure, links, and disclaimer. |

Internal-only comments may appear inside source code comments to identify governed state, provided those comments are not rendered in the browser.

## 5. Blocked Skeleton Content

The skeleton may not include:

1. Final marketing copy.
2. Expanded service explanations.
3. Pricing.
4. Forms.
5. Sponsor names.
6. Sponsor logos.
7. Partner claims.
8. Affiliate or referral claims.
9. Booking claims.
10. Availability claims.
11. Production readiness claims.
12. Unsupported transportation, airport, event, hospitality, or concierge claims.
13. Live QR activation language.
14. Links to production routes except controlled placeholder anchors.
15. Images, PDFs, or raster mockup surfaces.
16. JavaScript-driven behavior.
17. Third-party scripts.
18. Analytics scripts.
19. Fonts loaded from unapproved external sources.
20. Hidden text intended for search indexing.

## 6. CSS Token Rules

Skeleton CSS must be tokenized.

Required CSS files for next execution:

1. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/tokens.css`
2. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/section-skeleton.css`
3. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/preview-fixes.css`

Token rules:

1. Use purpose-based CSS custom properties.
2. Keep color, spacing, typography, container, border, and shadow decisions in `tokens.css`.
3. Keep section layout behavior in `section-skeleton.css`.
4. Keep preview-surface fixes in `preview-fixes.css`.
5. Avoid inline styles.
6. Avoid framework imports.
7. Avoid third-party CSS packages.
8. Avoid unapproved animation.
9. Support premium dark contrast.
10. Preserve readability across desktop and mobile.

## 7. Responsive Rules

Responsive behavior must be governed by CSS and must be visible in browser review.

Desktop rules:

1. Use a clear max-width container.
2. Preserve generous spacing.
3. Keep section identity visible.
4. Avoid dashboard-style tile compression.
5. Avoid content-directory density.
6. Keep sponsor and trust surfaces secondary.

Mobile rules:

1. Stack sections cleanly.
2. Preserve section separation.
3. Use readable type sizes.
4. Prevent horizontal overflow.
5. Keep touch targets large enough for future interactive elements.
6. Avoid condensed microcopy.
7. Avoid hidden critical section names.
8. Keep review surface usable on phone preview.

## 8. Section Boundary Rules

Each section must have:

1. A unique section wrapper.
2. A semantic HTML element where appropriate.
3. A visible section boundary in skeleton stage.
4. A section name.
5. A section tagline.
6. CSS classes tied to governed components.
7. No imported content from another section.
8. No linked-page content.
9. No content escalation beyond skeleton stage.

Boundary failure occurs if:

1. Hero absorbs Section 1.
2. Navigation absorbs header function.
3. Sponsor surface absorbs Section 2 or Section 4.
4. Footer becomes a sitemap before page composition authorization.
5. A section becomes a dashboard, directory, or PDF-style document block.

## 9. Preview URL Rules

The next skeleton review surface may exist only at:

`docs/prototypes/homepage-section-skeleton-v1.0.0/review.html`

The preview must be viewable through GitHub Pages or an approved static preview surface after commit.

The preview must not be treated as production.

The preview must not activate:

1. DreamHost production.
2. Final domain production routing.
3. QR destination production activation.
4. Production analytics.
5. Production metadata.

## 10. Commit Rules

The next skeleton execution may create or edit only:

1. `docs/prototypes/homepage-section-skeleton-v1.0.0/review.html`
2. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/tokens.css`
3. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/section-skeleton.css`
4. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/preview-fixes.css`
5. `docs/prototypes/homepage-section-skeleton-v1.0.0/README.md`

The next skeleton execution may not edit:

1. `docs/prototypes/homepage-v1.0.4/`
2. Production files.
3. Linked pages.
4. PDF files.
5. Image files.
6. DreamHost deployment files.
7. QR files.

Commit requirements:

1. Commit to `main`.
2. Fetch from `main` after commit.
3. Verify every exact path.
4. Return commit SHA.
5. Return final standing.

## 11. Review Rules

A skeleton review must include:

1. Section list confirmation.
2. Selected option confirmation.
3. CSS token review.
4. Desktop review.
5. Mobile review.
6. Accessibility review.
7. Claim-safety review.
8. Sponsor surface review.
9. Failure trigger review.
10. User review request.

Review cannot produce a lock. Only the user can approve and lock.

## 12. Final Content Blocking Rules

Final content remains blocked until:

1. The section option is user-selected.
2. The skeleton is rendered.
3. CSS review passes.
4. Mobile review passes.
5. Accessibility review passes.
6. Sponsor review passes where applicable.
7. User approves the skeleton.
8. User locks the section.
9. User authorizes content insertion.

The acting session must stop before final content insertion unless the user separately authorizes content work after section lock.

## 13. Final Determination

The skeleton rendering playbook is locked for the next execution.

Final standing for this file:

`SKELETON RENDERING PLAYBOOK CREATED / SKELETON CONTENT LIMITED TO SECTION NAME AND TAGLINE / CSS-RENDERED BROWSER REVIEW REQUIRED / FINAL CONTENT, PDF CAPTURE, DREAMHOST DEPLOYMENT, AND QR ACTIVATION REMAIN BLOCKED`.
