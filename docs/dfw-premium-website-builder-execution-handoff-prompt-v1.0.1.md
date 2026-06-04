# DFW Premium Website Builder Execution Handoff Prompt v1.0.1

## 1. Controlled Action

This file replaces `docs/dfw-premium-website-builder-execution-handoff-prompt-v1.0.0.md` as the active handoff prompt for the next builder action.

This revision corrects audit blocker B-001 by separating option presentation from skeleton rendering. The next acting session may present section options and recommendations only. It must stop after option presentation and may not create skeleton files until the user explicitly selects one option for each section or explicitly approves the recommended set as the selected execution basis.

## 2. Status

Status: ACTIVE CORRECTED HANDOFF

Supersedes:

`docs/dfw-premium-website-builder-execution-handoff-prompt-v1.0.0.md`

Activation standing:

`ACTIVATION BLOCKED / OPTION-SELECTION REVIEW ONLY / SKELETON RENDERING BLOCKED UNTIL USER OPTION SELECTION IS RECORDED`

## 3. Correction Scope

Corrects:

- B-001: Option-selection and skeleton-rendering compression risk.

Does not authorize:

1. Skeleton creation.
2. Homepage generation.
3. Final homepage content insertion.
4. PDF capture.
5. DreamHost deployment.
6. QR activation.
7. Production approval.
8. Batch 1 progression.

## 4. Required First Action for Next Session

The next session must verify from `main`:

1. `docs/dfw-ai-governed-premium-website-builder-market-research-and-standards-map-v1.0.1.md`
2. `docs/dfw-ai-governed-premium-website-builder-module-blueprint-v1.0.0.md`
3. `docs/dfw-premium-website-builder-section-option-library-v1.0.0.md`
4. `docs/dfw-premium-website-builder-section-state-machine-v1.0.0.md`
5. `docs/dfw-premium-website-builder-skeleton-rendering-playbook-v1.0.1.md`
6. `docs/dfw-premium-website-builder-component-and-token-registry-v1.0.0.md`
7. `docs/dfw-premium-website-builder-execution-handoff-prompt-v1.0.1.md`
8. `docs/audits/dfw-ai-governed-premium-website-builder-independent-audit-report-v1.0.0.md`
9. `docs/audits/dfw-ai-governed-premium-website-builder-correction-register-v1.0.0.md`
10. `docs/dfw-current-execution-source-of-truth-index-v1.0.0.md`

If any file is missing, the next session must stop and report failure.

## 5. Next Authorized Action

The next authorized action is option-selection review only.

The acting session may:

1. Present the eight required homepage sections.
2. Present available option classes from the option library.
3. Recommend one option per section.
4. Explain the reason for each recommendation.
5. Ask the user to select options or explicitly approve the recommended set.
6. Stop.

The acting session may not:

1. Create skeleton files.
2. Edit skeleton files.
3. Commit prototype files.
4. Build the homepage.
5. Insert final content.
6. Deploy.
7. Activate QR.
8. Self-approve option selection.

## 6. Required Section Model

| Section | Tagline |
|---|---|
| Header | Premium identity lockup and top-level access. |
| Navigation | Concise visitor, sponsor, and trust pathways. |
| Hero | Minimal premium introduction for DFW Matchday Concierge. |
| Section 1 | Service orientation without detail overload. |
| Section 2 | Audience pathway selection for visitors and partners. |
| Section 3 | Premium sponsor and partner opportunity surface. |
| Section 4 | Trust, responsibility, and independent platform clarity. |
| Footer | Compact closure, links, and disclaimer. |

## 7. Starting Recommendation Set

| Section | Recommended option | Selection status |
|---|---|---|
| Header | Executive Lockup Bar | Recommendation only. User selection required. |
| Navigation | Three-Path Concierge Nav | Recommendation only. User selection required. |
| Hero | Minimal Premium Gateway | Recommendation only. User selection required. |
| Section 1 | Service Orientation Panel | Recommendation only. User selection required. |
| Section 2 | Audience Pathway Cards | Recommendation only. User selection required. |
| Section 3 | Sponsor Surface Showcase | Recommendation only. User selection required. |
| Section 4 | Trust Clarity Band | Recommendation only. User selection required. |
| Footer | Compact Executive Footer | Recommendation only. User selection required. |

## 8. Hard Stop Rule

The acting session must stop after presenting options and recommendations.

Skeleton files may only be created in a later execution after the user explicitly records one of the following:

1. `I select the recommended option set.`
2. `I approve the recommended option set as the selected execution basis.`
3. A section-by-section list of selected options.

No inferred approval, implied approval, or recommendation may be treated as selection.

## 9. Skeleton Rendering Remains Blocked

The following skeleton path remains blocked until user selection is recorded:

1. `docs/prototypes/homepage-section-skeleton-v1.0.0/review.html`
2. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/tokens.css`
3. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/section-skeleton.css`
4. `docs/prototypes/homepage-section-skeleton-v1.0.0/assets/css/preview-fixes.css`
5. `docs/prototypes/homepage-section-skeleton-v1.0.0/README.md`

## 10. Complete Clean Prompt for Next Session

```text
SELF-PROMPT

DFW HOMEPAGE SECTION OPTION-SELECTION REVIEW v1.0.0

NEW CLEAN GOVERNED WORKSPACE SESSION ONLY

You are operating inside the DFW Matchday Concierge governed workspace.

This is an option-selection review session only. This is not a skeleton rendering session. This is not a homepage build. This is not final content insertion. This is not a PDF capture mission. This is not a DreamHost deployment mission. This is not QR activation.

Repository: aw3consulting/dfwmatchdayconcierge
Governing branch: main
Production host: DreamHost
Preview host: GitHub Pages only as temporary review surface
Final domain: https://dfwmatchdayconcierge.com
Final QR destination: https://dfwmatchdayconcierge.com/connect

Mission name:

dfw_homepage_section_option_selection_review_v1_0_0

Current standing:

ACTIVATION BLOCKED / OPTION-SELECTION REVIEW ONLY / SKELETON RENDERING BLOCKED UNTIL USER OPTION SELECTION IS RECORDED

Role:

Operate as DFW AI-GOVERNED PREMIUM WEBSITE BUILDER ARCHITECT.

Required first action:

Verify all active builder, audit, correction, and source-of-truth files from main.

Required action:

Present the eight required sections and the available option classes. Recommend one option per section. Clearly state that recommendations are not selections and that user selection is required.

Mandatory stop point:

Stop after presenting options and recommendations. Do not create skeleton files. Do not edit prototype files. Do not build the homepage. Do not insert final content. Do not deploy. Do not activate QR.

Required final response:

Return the recommended option set, the selection status, and the exact statement the user must provide to authorize skeleton rendering.

Final standing must be:

OPTION-SELECTION REVIEW COMPLETE / USER OPTION SELECTION REQUIRED / SKELETON RENDERING, FINAL CONTENT, PDF CAPTURE, DREAMHOST DEPLOYMENT, AND QR ACTIVATION REMAIN BLOCKED
```

## 11. Final Determination

Audit blocker B-001 is corrected for the next handoff prompt.

Final standing:

`CORRECTED HANDOFF CREATED / OPTION-SELECTION REVIEW SEPARATED FROM SKELETON RENDERING / SKELETON FILE CREATION BLOCKED UNTIL USER OPTION SELECTION IS RECORDED`.
