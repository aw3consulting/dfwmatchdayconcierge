# DFW Section Review Acceptance Criteria v1.0.0

## 1. Controlled Action

This file satisfies audit-required acceptance criteria for section option scoring, responsive review, accessibility review, token implementation, sponsor surface review, and claim review.

This file does not authorize skeleton rendering, homepage generation, final content insertion, production deployment, QR activation, or public claim expansion.

## 2. Status

Status: ACTIVE ACCEPTANCE CRITERIA RECORD

Activation standing:

`ACCEPTANCE CRITERIA CREATED / USER EVALUATION REQUIRED / SKELETON RENDERING REMAINS BLOCKED UNTIL OPTION SELECTION IS RECORDED`

## 3. Section Option Scoring Criteria

The DFW suitability score must be evaluated using these measurable criteria:

| Criterion | Pass threshold | Evidence required |
|---|---|---|
| Section purpose fit | Option directly supports the section tagline and does not introduce unrelated content. | Written rationale. |
| Content restraint | Option can render with only section name and tagline during skeleton stage. | Skeleton content check. |
| Premium hierarchy | Option provides a clear visual hierarchy without dashboard, directory, or PDF style. | Desktop review note. |
| Mobile viability | Option stacks cleanly and preserves section clarity at required mobile widths. | Mobile review note. |
| Sponsor control | Sponsor surface, if present, does not imply confirmed sponsor or ad inventory. | Sponsor review note. |
| Claim safety | Option does not require public claims to make visual sense during skeleton review. | Claim review note. |
| Boundary clarity | Option clearly separates this section from adjacent sections. | Section boundary note. |

Scoring rule:

- Score 5: All criteria pass with no material sensitivity.
- Score 4: All criteria pass with one monitor item.
- Score 3: Criteria pass with one required adjustment before skeleton rendering.
- Score 2: Two or more criteria require adjustment.
- Score 1: Option cannot be used without violating skeleton or claim boundaries.

## 4. Responsive Review Criteria

Required viewport checks:

1. 390px.
2. 430px.
3. 768px.
4. 1024px.
5. 1280px.
6. 1440px.

Responsive pass criteria:

1. No horizontal overflow.
2. Section name remains visible.
3. Section tagline remains legible.
4. Minimum touch target placeholder size is 44px where interactive placeholders exist.
5. Section spacing remains visually clear.
6. Header and navigation do not crowd the hero.
7. Sponsor surface remains secondary.
8. Trust surface remains readable.
9. Footer remains compact.
10. Layout does not create dashboard compression.

## 5. Accessibility Review Criteria

Working target:

`WCAG 2.2 AA as the working review target for public pages and section skeletons unless the user later approves another target.`

Required checks:

1. Semantic section structure.
2. Proper landmark intent for page shell, header, navigation, main, sections, and footer when rendered.
3. Text contrast target of at least 4.5:1 for normal text where applicable.
4. Large text contrast target of at least 3:1 where applicable.
5. No information communicated by color alone.
6. Keyboard focus visibility for any placeholder link or future interactive element.
7. No image-only text.
8. No hidden search text.
9. Reduced motion readiness if motion is later introduced.
10. Readable text sizing on required viewports.

Evidence required:

1. Manual accessibility note.
2. Contrast review note.
3. Keyboard and focus note if placeholders are interactive.
4. No-horizontal-overflow note.

## 6. Token Implementation Criteria

Required token categories:

1. Color tokens.
2. Typography tokens.
3. Spacing tokens.
4. Grid tokens.
5. Container tokens.
6. Button tokens.
7. Card tokens.
8. Sponsor surface tokens.
9. Trust surface tokens.
10. Section wrapper tokens.
11. Responsive behavior tokens.
12. Accessibility tokens.

Token pass criteria:

1. CSS files use purpose-based custom properties.
2. No inline style dependence.
3. No external framework dependence.
4. No unapproved external font loading.
5. No token names that imply unapproved brand, sponsor, or partner status.
6. Skeleton CSS can be reviewed through the allowed paths only.
7. Token changes are documented in review notes.

## 7. Sponsor Surface Review Criteria

Sponsor surface pass criteria:

1. No sponsor names.
2. No sponsor logos.
3. No paid placement claims.
4. No audience metric claims.
5. No guaranteed exposure claims.
6. No ad inventory claims.
7. Surface is clearly a review area, not a confirmed advertiser placement.
8. Surface remains secondary to visitor and trust pathways.
9. Surface reads premium and restrained.
10. User approval required before sponsor language expansion.

## 8. Claim Review Criteria

Claim review pass criteria:

1. Every public claim maps to live, operator-assisted, development, or restricted capability.
2. Every development or restricted claim has a public-use rule.
3. Every claim in final content has a source file, route, or manual workflow note.
4. Skeleton stage contains no public claim beyond allowed section names and taglines.
5. JSON-LD and metadata claims are reviewed before production approval.
6. QR destination claims are reviewed before QR activation.
7. User approval is required before any claim expansion.

## 9. Final Determination

Final standing:

`ACCEPTANCE CRITERIA CREATED / RESPONSIVE, ACCESSIBILITY, TOKEN, OPTION, SPONSOR, AND CLAIM REVIEW GATES DEFINED / ACTIVATION REMAINS BLOCKED PENDING USER EVALUATION AND NEXT ACTION AUTHORIZATION`.
