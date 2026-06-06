# DFW PDF Replica Independent HTML/CSS Code Quality Gap Register v1.0.0

## Status

HTML/CSS CODE QUALITY GAP CONFIRMED / VISUAL REPLICA SCORE SEPARATED FROM CODE QUALITY SCORE / PUBLIC ROUTE EDITS STILL BLOCKED

## Controlled Action

`dfw_pdf_replica_independent_html_css_code_quality_gap_register_v1_0_0`

## Purpose

This register separates two different evaluations:

1. Visual PDF-to-HTML replica progress.
2. Independent HTML/CSS code quality readiness.

The current 74/100 score applies to the isolated visual replica prototype, not to production-grade frontend code quality.

## Current Split Score

| Evaluation lane | Current score | Standing |
|---|---:|---|
| PDF visual replica prototype | 74 / 100 | Valid hardened prototype, not final replica |
| Independent HTML/CSS code quality | 58 / 100 | Functional prototype code, not production-hardened frontend code |
| Combined launch-readiness score | 66 / 100 | Not ready for public homepage replacement |

## Confirmed HTML/CSS Code Gaps Independent of Replica Fidelity

| Code area | Gap | Required correction |
|---|---|---|
| HTML structure | Prototype HTML is compressed and difficult to audit line-by-line | Reformat into readable, sectioned semantic markup |
| Component boundaries | Sections exist visually but are not clearly componentized | Add component comments or split reusable partial logic if build system is later introduced |
| CSS architecture | CSS is dense and difficult to maintain | Rebuild into layered sections: tokens, base, layout, components, responsive |
| Design tokens | Tokens exist but are incomplete | Expand tokens for spacing, typography, panel, border, shadow, z-index, and breakpoints |
| Naming system | Class naming is functional but not governed | Normalize class naming around component intent |
| Accessibility | Basic semantic structure exists, but form labels, focus states, nav behavior, and contrast require review | Add focus states, improve form accessibility, verify keyboard traversal |
| Mobile code | Responsive rules exist, but need browser screenshot proof and overflow testing | Validate at 390px, 430px, 768px, and 1024px |
| Asset strategy | Many visuals are CSS approximations rather than governed assets | Decide which visual objects remain CSS and which require image/SVG assets |
| Performance | No heavy JS exists, but CSS density and visual effects need review | Minimize unnecessary effects after visual acceptance |
| Production claims | Prototype includes PDF-reference metrics | Replace or evidence-map before production |

## Code Quality Pass Criteria

Before public homepage replacement, independent code quality must reach at least 80/100.

Required improvements:

1. Readable HTML formatting.
2. Clear section comments for each PDF-defined region.
3. CSS split or clearly grouped into governed layers.
4. Token system expanded and applied consistently.
5. Responsive breakpoints documented in CSS comments or audit.
6. Accessibility pass for nav, forms, focus states, labels, and tap targets.
7. Browser proof for desktop, tablet, and mobile.
8. Production-safe copy map separated from prototype-reference copy.
9. Public-route adaptation plan created before editing `index.html`.
10. No public route replacement without user approval.

## Recalibrated Launch Gate

Public homepage replacement requires two separate passes:

1. PDF visual replica score: `80+ / 100` minimum.
2. Independent HTML/CSS code quality score: `80+ / 100` minimum.

Current standing does not meet either public-route launch gate.

## Blocked Actions

Still blocked:

1. Editing public `index.html`.
2. Editing `/connect`.
3. DreamHost deployment.
4. QR activation.
5. Production approval.
6. Treating the visual score as code-quality approval.

## Final Standing

HTML/CSS CODE QUALITY GAP CONFIRMED / CURRENT VISUAL REPLICA SCORE 74 / CURRENT INDEPENDENT CODE QUALITY SCORE 58 / COMBINED LAUNCH-READINESS SCORE 66 / PUBLIC HOMEPAGE REPLACEMENT REMAINS BLOCKED UNTIL BOTH VISUAL FIDELITY AND CODE QUALITY PASS 80+.
