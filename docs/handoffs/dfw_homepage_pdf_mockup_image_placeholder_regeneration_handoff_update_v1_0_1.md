# DFW Homepage PDF Mockup Image Placeholder Regeneration Handoff Update v1.0.1

## Status

USER-REVIEW UPDATE / SUPERSEDES SPECIFIC v1.0.0 HANDOFF ITEMS / DESKTOP `index-v1.0.10` REMAINS PRE-LOCKED DRAFT PENDING REVIEW / ALL NON-IMAGE WEB ELEMENTS REMAIN LOCKED / IMAGE PLACEHOLDERS AND ICON PLACEHOLDERS ONLY REMAIN OPEN

## Relationship to Prior Handoff

This file updates and corrects:

`docs/handoffs/dfw_homepage_pdf_mockup_image_placeholder_regeneration_handoff_draft_v1_0_0.md`

The prior handoff remains useful, but this v1.0.1 update controls the corrected items below.

## Corrected User Requirements

### 1. Hero Typo Correction

The prior handoff incorrectly used the word `Crown`.

Correct term:

`Crowd`

The hero direction is now:

Left to right:

1. Fort Worth skyline.
2. AT&T Stadium.
3. Dallas skyline.
4. Crowd with flags.

### 2. Hero Flag Rule

The hero crowd must include flags from the current eight Dallas team-hub countries plus the USA flag as a ninth flag.

Current locked Fan Hub / Team Hub visible country set:

1. Netherlands.
2. Japan.
3. England.
4. Croatia.
5. Argentina.
6. Austria.
7. Sweden.
8. Jordan.

Hero additional flag:

9. USA.

The USA flag is added to the hero crowd visual only. This does not authorize adding USA to the locked Team Hubs card set unless the user separately approves that change.

### 3. Fan Hub / Team Hub Flags Are Locked

The current Fan Hub / Team Hub flags are not image placeholders.

They are locked web elements in the current desktop pre-locked draft.

Do not replace, regenerate, redesign, add, remove, or reorder the Team Hub flag cards during the image-placeholder regeneration pass.

### 4. DFW Concierge Logo Source Is Already Approved

The DFW Matchday Concierge logo is already saved in the workspace source.

Do not regenerate the logo.

Only size and fit the approved source logo into the existing logo placements:

1. Header logo placement.
2. Footer logo placement.

Logo handling rule:

- Use the approved workspace source logo.
- Preserve the logo design exactly.
- Do not redraw, reinterpret, stylize, recolor, or regenerate it.
- Only create derivative size/export versions as needed to fit the existing HTML/CSS logo containers.

Known workspace logo references include:

1. `/mnt/data/approved-logo-crop-reference-v1.0.14.png`
2. `/mnt/data/approved-logo-transparent-reference-v1.0.15.png`

The next session must locate and use the approved logo source available in the workspace/source files or repository assets. If the source asset is missing from the repo, the session must report that and request/upload the approved file rather than regenerate the logo.

### 5. Premium Execution Requirement

Premium visual quality is a governing requirement.

Image regeneration must be premium, coherent, dark-navy/gold compatible, commercially credible, and visually stronger than a generic mockup.

The task is not only to fill boxes. The task is to upgrade the placeholder layer while preserving the approved web structure.

### 6. Drift and Error Reporting Authority

The next chat session is authorized and required to report any errors, conflicts, drift, missing assets, broken assumptions, schedule/team inconsistencies, unsupported claims, or implementation blockers discovered in this handoff or in the current prototype.

The next session should obtain as much authority as needed to complete the task correctly, including:

1. Asking for missing approved assets.
2. Flagging conflicting instructions before execution.
3. Identifying image dimensions that cannot fit the current containers.
4. Reporting if a placeholder is actually a locked web element.
5. Reporting if any requested visual would create claim, affiliation, copyright, or brand-risk exposure.
6. Requesting user approval before changing anything outside the open image/icon placeholder scope.

## Updated Hero Regeneration Instruction

Create one cinematic composite hero image that fits the existing hero container in `index-v1.0.10`.

Required composition from left to right:

1. Fort Worth skyline.
2. AT&T Stadium.
3. Dallas skyline.
4. Crowd with flags from the eight locked Team Hub countries plus USA.

Required hero flag set:

1. Netherlands.
2. Japan.
3. England.
4. Croatia.
5. Argentina.
6. Austria.
7. Sweden.
8. Jordan.
9. USA.

Hero requirements:

- No official FIFA marks.
- No official team marks.
- No tournament affiliation claim.
- Dark navy and gold visual grade.
- Existing headline and CTA readability must be protected.
- The image must remain subordinate to the locked hero text.
- Do not modify hero copy, buttons, or layout.

Recommended hero asset path remains:

`docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/hero/dfw-hero-fw-att-dallas-crowd-flags-v1.0.0.webp`

## Updated Logo Replacement Instruction

Replace the header and footer `L` logo placeholders with the approved DFW Matchday Concierge logo source only.

Allowed:

- Crop/scale/export approved logo to fit header and footer containers.
- Use transparent PNG or SVG if already available.
- Add minimal image-fit CSS.

Not allowed:

- Logo redesign.
- Logo regeneration.
- Font changes.
- Color changes.
- Alternate logo concepts.
- AI-generated logo recreation.

Recommended output paths:

`docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/logos/dfw-logo-header-v1.0.0.png`

`docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/logos/dfw-logo-footer-v1.0.0.png`

## Updated Team Hub Flag Instruction

Team Hub flags are locked and must remain unchanged in this pass.

Do not replace CSS-generated Team Hub flags with uploaded SVG flag images during the image-placeholder regeneration execution unless the user separately unlocks that item.

The hero crowd flags are a separate visual element and may include the nine-flag set listed above.

## Updated Open Placeholder Scope

Open visual placeholder scope now includes:

1. Header logo placeholder: replace with approved logo only.
2. Footer logo placeholder: replace with approved logo only.
3. Hero background image: generate composite crowd/skyline/stadium visual.
4. S03 AI image placeholder.
5. S04 Operating Command Hub icon placeholders.
6. S05 map visual placeholder.
7. S07 Drivers image placeholder.
8. S07 Concierges image placeholder.
9. S07 Fulfillment Providers image placeholder.
10. Footer social icon placeholders.

Closed visual scope:

1. Fan Hub / Team Hub flag cards.
2. Header/nav layout.
3. Form fields and options.
4. CTA copy and placement.
5. Section text.
6. Footer structure.
7. Sponsor rail text link.
8. S08 responsibility/read-more cards.

## Updated Next Chat Execution Prompt

```text
You are operating inside the DFW Matchday Concierge governed workspace.

Execute: dfw_homepage_pdf_mockup_image_placeholder_regeneration_execution_v1_0_0

Repository: aw3consulting/dfwmatchdayconcierge
Branch: main

Current accepted desktop review base:
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html

Current preview:
https://html-preview.github.io/?url=https://github.com/aw3consulting/dfwmatchdayconcierge/blob/main/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html

Authority handoffs:
1. docs/handoffs/dfw_homepage_pdf_mockup_image_placeholder_regeneration_handoff_draft_v1_0_0.md
2. docs/handoffs/dfw_homepage_pdf_mockup_image_placeholder_regeneration_handoff_update_v1_0_1.md

Task:
Evaluate the PDF mockup against index-v1.0.10 and regenerate only open image, logo, map, and icon placeholder assets. Preserve all locked web elements, copy, layout, form behavior, CTA text, section order, and Team Hub flag cards.

Critical corrections:
1. The hero visual uses CROWD, not crown.
2. Hero composition must be Fort Worth skyline, AT&T Stadium, Dallas skyline, and crowd with flags.
3. Hero flag set must include Netherlands, Japan, England, Croatia, Argentina, Austria, Sweden, Jordan, and USA.
4. Team Hub flags are locked and are not image placeholders.
5. The DFW Matchday Concierge logo must not be regenerated. Use the approved workspace source logo and size it to fit header and footer placements only.
6. Premium visual quality is required.
7. Report any drift, missing source assets, conflicts, broken assumptions, claim risks, brand risks, or implementation blockers before changing locked scope.

Deliverables:
1. Uploaded image/icon/map/logo assets under the approved prototype asset directories.
2. Minimal image-only CSS or HTML replacement changes.
3. Direct static preview link only.
4. Placeholder replacement audit.
5. Confirmation that no locked non-image web element changed.
6. List of any errors or drift discovered and how they were resolved or escalated.
```

## Final Standing

HANDOFF UPDATE v1.0.1 CREATED / CROWN TYPO CORRECTED TO CROWD / HERO FLAG SET CLARIFIED AS EIGHT TEAM HUB FLAGS PLUS USA / TEAM HUB FLAGS LOCKED / APPROVED LOGO MUST BE USED WITHOUT REGENERATION / NEXT SESSION AUTHORIZED TO REPORT DRIFT AND SEEK AUTHORITY / PREMIUM IMAGE REGENERATION STANDARD LOCKED.
