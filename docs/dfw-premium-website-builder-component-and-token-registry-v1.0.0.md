# DFW Premium Website Builder Component and Token Registry v1.0.0

## 1. Controlled Action

This file defines the reusable component and token registry for the DFW AI-Governed Premium Website Builder Module.

This zero-drift correction clarifies that the registry is not execution authority for the next action. It supports future skeleton rendering only after explicit user option selection is recorded.

This file does not authorize option selection, skeleton rendering, skeleton file creation, homepage generation, final homepage content, production deployment, QR activation, PDF capture, or image generation.

## 2. Status

Status: ACTIVE COMPONENT AND TOKEN REGISTRY / NOT EXECUTION AUTHORITY

Activation standing:

`NEXT ACTION MAY ONLY BE OPTION-SELECTION REVIEW AFTER USER AUTHORIZATION / SKELETON RENDERING BLOCKED UNTIL USER OPTION SELECTION IS RECORDED`

Active source of truth:

`docs/dfw-current-execution-source-of-truth-index-v1.0.0.md`

Active option-selection handoff:

`docs/dfw-premium-website-builder-execution-handoff-prompt-v1.0.1.md`

Active skeleton rendering playbook:

`docs/dfw-premium-website-builder-skeleton-rendering-playbook-v1.0.1.md`

## 3. Registry Purpose

The registry prevents visual drift by forcing design decisions into named tokens and reusable components before final content exists.

The registry supports:

1. Section-first governance.
2. Future browser-rendered CSS review after user option selection.
3. Desktop and mobile review.
4. Accessibility review.
5. Sponsor surface review.
6. Trust surface review.
7. Future content insertion only after approval.

## 4. Color Tokens

Required token family:

```css
:root {
  --dfw-color-page-bg: #050507;
  --dfw-color-surface: #0d0d10;
  --dfw-color-surface-elevated: #15151a;
  --dfw-color-border: rgba(255, 255, 255, 0.14);
  --dfw-color-border-strong: rgba(255, 255, 255, 0.28);
  --dfw-color-text-primary: #f5f3ef;
  --dfw-color-text-secondary: #c9c3b8;
  --dfw-color-text-muted: #8f887d;
  --dfw-color-accent: #c9a85d;
  --dfw-color-accent-soft: rgba(201, 168, 93, 0.18);
  --dfw-color-trust-surface: rgba(255, 255, 255, 0.06);
  --dfw-color-sponsor-surface: rgba(201, 168, 93, 0.09);
}
```

Rules:

1. Color tokens must be purpose-based.
2. Future skeleton review must use dark premium contrast.
3. Sponsor color treatment must remain restrained.
4. Trust surfaces must read clearly without becoming legal-document blocks.
5. No color may be used as the only source of meaning.

## 5. Typography Tokens

Required token family:

```css
:root {
  --dfw-font-display: Georgia, "Times New Roman", serif;
  --dfw-font-body: Arial, Helvetica, sans-serif;
  --dfw-font-mono: "SFMono-Regular", Consolas, monospace;
  --dfw-type-xs: clamp(0.72rem, 0.7rem + 0.1vw, 0.78rem);
  --dfw-type-sm: clamp(0.86rem, 0.82rem + 0.18vw, 0.96rem);
  --dfw-type-md: clamp(1rem, 0.94rem + 0.28vw, 1.12rem);
  --dfw-type-lg: clamp(1.25rem, 1.06rem + 0.9vw, 1.9rem);
  --dfw-type-xl: clamp(2rem, 1.42rem + 2.6vw, 4.2rem);
  --dfw-line-tight: 1.05;
  --dfw-line-normal: 1.5;
  --dfw-letter-wide: 0.14em;
}
```

Rules:

1. Text must be legible on desktop and mobile.
2. Display typography may express premium tone.
3. Body typography must prioritize clarity.
4. Letter spacing must be controlled and never applied to long text.
5. External font loading remains blocked in future skeleton stage unless separately approved.

## 6. Spacing Tokens

Required token family:

```css
:root {
  --dfw-space-1: 0.25rem;
  --dfw-space-2: 0.5rem;
  --dfw-space-3: 0.75rem;
  --dfw-space-4: 1rem;
  --dfw-space-5: 1.5rem;
  --dfw-space-6: 2rem;
  --dfw-space-7: 3rem;
  --dfw-space-8: 4.5rem;
  --dfw-space-section: clamp(3rem, 7vw, 7rem);
}
```

Rules:

1. Premium spacing must remain generous.
2. Mobile spacing may compress, but section distinction must remain clear.
3. Layout may not become dashboard-dense.
4. Spacing changes must be reviewed as CSS behavior.

## 7. Grid Tokens

Required token family:

```css
:root {
  --dfw-grid-gap: clamp(1rem, 2vw, 2rem);
  --dfw-grid-two: repeat(2, minmax(0, 1fr));
  --dfw-grid-three: repeat(3, minmax(0, 1fr));
  --dfw-grid-four: repeat(4, minmax(0, 1fr));
}
```

Rules:

1. Grid usage must serve section review, not content density.
2. Mobile grids must stack cleanly.
3. Sponsor grids must remain visibly secondary.
4. Trust grids must remain calm and readable.

## 8. Container Tokens

Required token family:

```css
:root {
  --dfw-container-max: 1180px;
  --dfw-container-wide: 1320px;
  --dfw-container-narrow: 860px;
  --dfw-container-pad: clamp(1rem, 4vw, 3rem);
}
```

Rules:

1. Containers must prevent edge crowding.
2. Wide containers may be used for hero and sponsor surfaces after authorization.
3. Narrow containers may be used for trust clarity.
4. Container behavior must pass mobile review.

## 9. Button Tokens

Required token family:

```css
:root {
  --dfw-button-radius: 999px;
  --dfw-button-border: 1px solid var(--dfw-color-border-strong);
  --dfw-button-pad-y: 0.85rem;
  --dfw-button-pad-x: 1.2rem;
  --dfw-button-min-height: 44px;
}
```

Rules:

1. Placeholder buttons may appear only when authorized for future layout review.
2. Placeholder buttons may not contain final CTA copy.
3. Touch target minimum height must be preserved.
4. Active form or booking behavior is blocked in future skeleton stage.

## 10. Card Tokens

Required token family:

```css
:root {
  --dfw-card-radius: 1.25rem;
  --dfw-card-border: 1px solid var(--dfw-color-border);
  --dfw-card-bg: linear-gradient(180deg, rgba(255,255,255,0.07), rgba(255,255,255,0.025));
  --dfw-card-pad: clamp(1rem, 3vw, 2rem);
  --dfw-card-shadow: 0 24px 80px rgba(0, 0, 0, 0.28);
}
```

Rules:

1. Cards must not become dense directories.
2. Cards must preserve premium spacing.
3. Card count must match selected section option after user selection.
4. Card text in future skeleton stage is limited to section name, tagline, or nonpublic source comments.

## 11. Sponsor Surface Tokens

Required token family:

```css
:root {
  --dfw-sponsor-bg: var(--dfw-color-sponsor-surface);
  --dfw-sponsor-border: 1px solid rgba(201, 168, 93, 0.26);
  --dfw-sponsor-radius: 1.5rem;
  --dfw-sponsor-pad: clamp(1.25rem, 4vw, 3rem);
}
```

Rules:

1. Sponsor surfaces must not imply confirmed sponsors.
2. Sponsor surfaces must not include logos in future skeleton stage.
3. Sponsor surfaces must not include ad metrics without validation.
4. Sponsor surfaces must remain premium and secondary.

## 12. Trust Surface Tokens

Required token family:

```css
:root {
  --dfw-trust-bg: var(--dfw-color-trust-surface);
  --dfw-trust-border: 1px solid var(--dfw-color-border);
  --dfw-trust-radius: 1.25rem;
  --dfw-trust-pad: clamp(1rem, 3vw, 2rem);
}
```

Rules:

1. Trust surfaces must support clarity and independent platform language after content authorization.
2. Future skeleton trust surfaces may show only section name and tagline.
3. Trust surfaces must avoid over-legal density.
4. Trust surfaces must pass readability and contrast review.

## 13. Section Wrapper Components

Required components:

| Component | Purpose | Required class pattern | Use rule |
|---|---|---|---|
| Page shell | Overall review canvas | `.dfw-page-shell` | Future use only after user option selection. |
| Section wrapper | Individual section boundary | `.dfw-section` | Future use only after user option selection. |
| Section inner | Controlled section content width | `.dfw-section__inner` | Future use only after user option selection. |
| Section name | Skeleton section label | `.dfw-section__name` | Must render authorized section name only after skeleton authorization. |
| Section tagline | Skeleton tagline | `.dfw-section__tagline` | Must render authorized tagline only after skeleton authorization. |
| Header shell | Header structure | `.dfw-header` | Header section only after authorization. |
| Navigation shell | Navigation structure | `.dfw-nav` | Navigation section only after authorization. |
| Hero shell | Hero section emphasis | `.dfw-hero` | Hero section only after authorization. |
| Sponsor shell | Sponsor surface review | `.dfw-sponsor-surface` | Section 3 or approved sponsor surface only after authorization. |
| Trust shell | Trust surface review | `.dfw-trust-surface` | Section 4 or approved trust surface only after authorization. |
| Footer shell | Footer closure | `.dfw-footer` | Footer section only after authorization. |

## 14. Responsive Behavior Tokens

Required token family:

```css
:root {
  --dfw-breakpoint-sm: 640px;
  --dfw-breakpoint-md: 820px;
  --dfw-breakpoint-lg: 1024px;
  --dfw-breakpoint-xl: 1280px;
}
```

Rules:

1. Use CSS media queries tied to these breakpoints after skeleton authorization.
2. Mobile review must include stack, spacing, type, and overflow checks.
3. Desktop review must include hierarchy, section flow, and premium spacing checks.
4. Future section skeleton must work without JavaScript.

## 15. Accessibility Tokens

Required token family:

```css
:root {
  --dfw-focus-ring: 0 0 0 3px rgba(201, 168, 93, 0.42);
  --dfw-min-touch-target: 44px;
  --dfw-readable-measure: 68ch;
}
```

Rules:

1. Interactive placeholders must preserve focus visibility where present.
2. Touch target minimums must be maintained.
3. Long-form future content must use readable measure.
4. Contrast must remain readable on dark surfaces.
5. Reduced motion must be respected if motion is later introduced.

## 16. Component Governance Rules

1. Components must map to a section option or registry entry.
2. Components must render in browser through HTML/CSS only after skeleton authorization.
3. Components must not introduce final content in future skeleton stage.
4. Components must not load unapproved external scripts.
5. Components must not load unapproved external fonts.
6. Components must not create production routes.
7. Components must not activate QR pathways.
8. Components must not include sponsor logos, partner names, pricing, forms, or final CTAs.
9. Components must preserve mobile behavior.
10. Components must support accessibility review.
11. Component registry language may not be treated as user option selection.
12. Component registry language may not authorize skeleton rendering.

## 17. Final Determination

The component and token registry is ready as a governed reference for future use after user option selection.

Final standing for this file:

`COMPONENT AND TOKEN REGISTRY CORRECTED / NOT EXECUTION AUTHORITY / NEXT ACTION MAY ONLY BE OPTION-SELECTION REVIEW AFTER USER AUTHORIZATION / SKELETON RENDERING BLOCKED UNTIL USER OPTION SELECTION IS RECORDED`.
