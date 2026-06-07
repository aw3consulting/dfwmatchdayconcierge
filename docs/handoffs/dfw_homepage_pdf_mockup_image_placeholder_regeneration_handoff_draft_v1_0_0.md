# DFW Homepage PDF Mockup Image Placeholder Regeneration Handoff Draft v1.0.0

## Status

DRAFT FOR USER REVIEW / NEXT CONTROLLED ACTION HANDOFF / DESKTOP `index-v1.0.10` IS PRE-LOCKED DRAFT PENDING REVIEW / ALL NON-IMAGE WEB ELEMENTS MUST REMAIN LOCKED / IMAGE AND ICON PLACEHOLDERS ONLY MAY BE UPDATED

## Controlled Action Name

`dfw_homepage_pdf_mockup_image_placeholder_regeneration_handoff_v1_0_0`

## Purpose

Evaluate the approved PDF mockup against the current desktop pre-locked draft `index-v1.0.10` and define all image, logo, map, icon, flag, and visual placeholder replacement requirements for a separate regeneration session.

The next session must regenerate only the visual placeholder assets and update their placement in the pre-locked desktop draft without changing the approved web structure, text, CTA logic, layout hierarchy, or section order.

## Current Review Base

Direct static desktop pre-locked draft:

`docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html`

Direct preview:

`https://html-preview.github.io/?url=https://github.com/aw3consulting/dfwmatchdayconcierge/blob/main/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html`

Styles loaded by the pre-locked draft:

1. `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/css/replica-v1.0.7.css`
2. `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/css/replica-v1.0.10.css`

## Governing Lock Rule

The current pre-lock locks all non-image web elements.

Locked and not to be changed in the image regeneration session:

1. Section order.
2. Header/navigation text.
3. Form fields and options.
4. CTA text and locations.
5. Section headings.
6. Card titles and card body copy.
7. Grid structure.
8. Desktop layout proportions.
9. Footer text structure.
10. Date picker behavior.
11. Dallas Matchdays click-to-date behavior.
12. Public claim language.
13. Sponsor rail text treatment.
14. Responsibility/read-more card structure.

Allowed changes:

1. Replace image placeholders.
2. Replace logo placeholders.
3. Replace operating hub icon placeholders.
4. Replace map placeholder with a generated/approved map image or SVG.
5. Replace current CSS flag placeholders with approved flag images if needed.
6. Add asset references and minimal CSS needed to display the new image assets inside existing locked containers.

Disallowed changes:

1. Do not rebuild the homepage.
2. Do not redesign the layout.
3. Do not change copy.
4. Do not change CTA positions.
5. Do not change desktop section widths/heights except minimum required image-fit CSS inside existing placeholder containers.
6. Do not reintroduce invalid preview loader files.
7. Do not use CSS `@import` as the active preview dependency path.

## Recommended Asset Upload Structure

All replacement assets should be uploaded inside the existing prototype asset tree so the pre-locked draft can preview locally through the same static HTML route.

Recommended folders:

```text
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/hero/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/cards/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/maps/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/logos/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/flags/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/icons/hubs/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/icons/social/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/icons/ui/
```

All references in `index-v1.0.10.html` must remain relative to that file, for example:

```html
<img src="assets/images/cards/driver-card-v1.0.0.webp" alt="Driver visual placeholder replacement">
```

## Preview Standard for Image Replacement

The next session must create a direct static preview file or update the accepted direct static preview file only after user approval.

Preview rules:

1. Use direct HTML file output.
2. Use direct `<link rel="stylesheet">` references.
3. Do not create a JavaScript loader page.
4. Do not point the user to a loader preview.
5. Do not rely on CSS imports for the active preview file.
6. Provide a preview link only after the file is structurally reviewable.

## Image Placeholder Inventory and Replacement Instructions

### S01-A Header Logo Placeholder

Current placeholder:

- Selector: `.logo-placeholder`
- Location: Header, far left.
- Current text: `L` / `LOGO SIZE`.

Replacement target:

- Use final DFW Matchday Concierge logo or approved logo crop.
- Format: SVG preferred; transparent PNG acceptable; WebP acceptable only if raster logo detail is required.
- Recommended source size: 256 x 256 px minimum, square transparent canvas.
- Display target: approximately 50 x 50 px.
- Upload path:

```text
assets/images/logos/dfw-logo-header-v1.0.0.svg
```

Implementation requirement:

- Replace the inner placeholder span with an image element or CSS background inside the same header logo cell.
- Preserve `.logo-cell` size and header grid.
- Do not change brand text or navigation.

### S02 Main Hero Visual

Current placeholder state:

- The hero currently uses dark overlay / gradient treatment only.
- No live photo asset is inserted yet.

Required hero composition from user:

Left to right:

1. Fort Worth skyline.
2. AT&T Stadium.
3. Dallas skyline.
4. Crown with flags from all 8 countries including the USA flag.

Recommended better-than-mockup design option:

Use one cinematic composite hero image rather than four independent image elements. A single composite image will better preserve the pre-locked layout, reduce responsive drift, and allow the existing text overlay to remain locked.

Hero composition guide:

- Canvas ratio: approximately 4.05:1 to match current desktop hero area.
- Recommended source size: 2400 x 600 px or 2048 x 512 px.
- Safe central text zone: keep the center 45 percent darker and lower contrast so existing headline remains readable.
- Left zone, 0-25 percent: Fort Worth skyline.
- Center-left/center, 25-55 percent: AT&T Stadium.
- Center-right, 55-78 percent: Dallas skyline.
- Far right/top-right, 78-100 percent: crown + eight country flags including USA.
- Color treatment: deep navy, high contrast, gold highlights, subdued saturation.
- No fake official event marks.
- No official FIFA/tournament marks.
- No claims of official affiliation.

Upload path:

```text
assets/images/hero/dfw-hero-fw-att-dallas-crown-flags-v1.0.0.webp
```

Optional source-editing path:

```text
assets/images/hero/source/dfw-hero-fw-att-dallas-crown-flags-layered-v1.0.0.psd
assets/images/hero/source/dfw-hero-fw-att-dallas-crown-flags-layered-v1.0.0.fig
```

Implementation requirement:

- Add the hero image as a background layer or pseudo-element inside `.hero-section`.
- Preserve all hero text and CTA positions.
- Preserve the existing dark overlay.
- Do not place flags behind the headline.
- Keep the image visually subordinate to the existing locked hero text.

Flag set clarification required:

The current Team Hubs card set in `index-v1.0.10` includes Netherlands, Japan, England, Croatia, Argentina, Austria, Sweden, and Jordan.

The user direction for the hero says the crown must include flags from all 8 countries including the USA flag.

Before final hero generation, confirm the final eight-country flag set because the current visible Team Hubs set does not include USA.

Do not invent or finalize the crown flag set without this confirmation.

### S03-A AI Image Placeholder

Current placeholder:

- Selector: `.ai-image-slot`
- Current text: `AI` / image placeholder / `142 x 112 target`.
- Location: left side of AI-assisted inquiry preview panel.

Replacement target:

- AI operator / command-chip style image.
- Should feel premium, technical, and human-assisted, not generic robot stock art.
- Must not overpower the form.

Recommended format:

- SVG if geometric/line-based.
- WebP if rendered glass/gold AI chip illustration.
- Transparent PNG acceptable.

Recommended source size:

- 284 x 224 px minimum for 2x retina display.
- Display target: approximately 142 x 112 px.

Upload path:

```text
assets/images/cards/ai-inquiry-command-chip-v1.0.0.webp
```

Implementation requirement:

- Replace only the image placeholder content.
- Preserve S03 top-line layout, form fields, Dallas Matchdays row, and date activation behavior.

### S04 Operating Command Hub Icons

Current placeholders:

- Selector: `.icon-placeholder`
- Seven icon placeholders in Operating Command Hubs.

Required icon set:

1. VIP Guest Concierge.
2. Team Family Support.
3. Media / Corporate.
4. Fan Hubs.
5. Driver Onboarding.
6. Concierge Onboarding.
7. Fulfillment Hub.

Recommended icon format:

- SVG preferred.
- 32 x 32 viewBox or 48 x 48 viewBox.
- Stroke icon style.
- Use `currentColor` or site gold `#d8a64b`.
- Transparent background.
- Stroke width: 1.75 to 2.25 px depending on viewBox.
- No embedded text inside icons.
- Rounded caps and joins.
- Keep visual weight consistent across all seven.

Recommended filenames:

```text
assets/icons/hubs/vip-guest-concierge-v1.0.0.svg
assets/icons/hubs/team-family-support-v1.0.0.svg
assets/icons/hubs/media-corporate-v1.0.0.svg
assets/icons/hubs/fan-hubs-v1.0.0.svg
assets/icons/hubs/driver-onboarding-v1.0.0.svg
assets/icons/hubs/concierge-onboarding-v1.0.0.svg
assets/icons/hubs/fulfillment-hub-v1.0.0.svg
```

Recommended icon concepts:

- VIP Guest Concierge: diamond, crest, or premium guest marker.
- Team Family Support: family/group with shield/privacy cue.
- Media / Corporate: briefcase + signal/camera cue.
- Fan Hubs: flag, route flag, or crowd flag marker.
- Driver Onboarding: steering wheel or driver credential.
- Concierge Onboarding: service bell or concierge dome.
- Fulfillment Hub: box, route node, or fulfillment cube.

Better-than-mockup recommendation:

Use a single custom SVG icon family rather than mixed stock icons. This will make the section more premium, consistent, and easier to color-match than the PDF mockup.

Implementation requirement:

- Replace icon placeholder content only.
- Preserve card titles, descriptions, grid, card borders, and CTA absence.

### S05 Map and Routes Visual

Current placeholder:

- Selector: `.map-visual`
- Current text: `Precise Area Map Placeholder` plus generic node placeholders.

Replacement target:

- DFW regional command map showing airports, Fort Worth, Arlington, Dallas, stadium zone, Stockyards, and fan experience zones.
- Must remain a planning map, not an official government or transit map.

Recommended format:

- SVG preferred for crisp labels and route lines.
- WebP fallback acceptable if generated visually.

Recommended source size:

- 1000 x 575 px minimum if raster.
- SVG viewBox around 1000 x 575.

Upload path:

```text
assets/images/maps/dfw-matchday-routes-map-v1.0.0.svg
```

Required map nodes:

1. DFW Airport.
2. Love Field.
3. Fort Worth.
4. Arlington.
5. Dallas.
6. Stockyards.
7. Stadium Zone.
8. Fan Experience Zones.

Required map style:

- Dark navy base.
- Gold route paths.
- Gold/blue node markers.
- Compact labels.
- Avoid over-detail.
- Preserve route list on right side of current panel.

Implementation requirement:

- Replace only `.map-visual` content/background.
- Preserve route list, route CTA, section title, and panel split.

### S05 Right Team Hub Flags

Current state:

- CSS-generated flags inside `.opening-team-grid`.
- Current visible teams: Netherlands, Japan, England, Croatia, Argentina, Austria, Sweden, Jordan.

Replacement target:

- Use approved flag SVGs or retain CSS flags if visually sufficient.

Recommended format:

- SVG flag assets preferred.
- Ratio: 3:2.
- No gradients or textures unless required.

Upload path:

```text
assets/images/flags/netherlands-v1.0.0.svg
assets/images/flags/japan-v1.0.0.svg
assets/images/flags/england-v1.0.0.svg
assets/images/flags/croatia-v1.0.0.svg
assets/images/flags/argentina-v1.0.0.svg
assets/images/flags/austria-v1.0.0.svg
assets/images/flags/sweden-v1.0.0.svg
assets/images/flags/jordan-v1.0.0.svg
assets/images/flags/usa-v1.0.0.svg
```

Country set warning:

The hero requirement includes USA, but the current Team Hubs set does not. The next session must verify whether USA should be added to the hero only, replace one of the current eight, or be added as a ninth supporting flag.

### S06 Sponsor Rail Visuals

Current state:

- Text-only sponsor slots.
- No image replacement required unless ad inventory previews are requested.

Optional image asset recommendation:

If ad cards are later visualized, use SVG or WebP placeholder cards in:

```text
assets/images/sponsors/title-sponsor-slot-v1.0.0.svg
assets/images/sponsors/airport-transfer-partner-slot-v1.0.0.svg
assets/images/sponsors/dining-partner-slot-v1.0.0.svg
assets/images/sponsors/hotel-area-partner-slot-v1.0.0.svg
assets/images/sponsors/fan-experience-partner-slot-v1.0.0.svg
```

Do not change the current `[View Ad Inventory]` text link treatment during image placeholder regeneration.

### S07-A Drivers Image Placeholder

Current placeholder:

- Selector: first `.photo-card .card-image-slot`.
- Text: `Driver visual update pending`.

Replacement target:

- Premium black SUV / driver command visual.
- Should imply transportation readiness without unsupported fleet claims.

Recommended format:

- WebP preferred.
- JPEG acceptable if photo source.
- Aspect ratio: approximately 16:7 or 2.75:1 to fit current card image slot.
- Recommended source size: 800 x 300 px minimum.

Upload path:

```text
assets/images/cards/driver-hub-visual-v1.0.0.webp
```

Implementation requirement:

- Preserve Drivers title, copy, bullets, and CTA.
- Do not add vehicle model claims.
- Do not use logos or third-party brand marks unless owned or licensed.

### S07-B Concierges Image Placeholder

Current placeholder:

- Selector: second `.photo-card .card-image-slot`.
- Text: `Concierge visual update pending`.

Replacement target:

- Professional concierge/operator team visual.
- Premium but neutral.
- No fake uniforms or official affiliations.

Recommended format:

- WebP preferred.
- Aspect ratio: approximately 16:7 or 2.75:1.
- Recommended source size: 800 x 300 px minimum.

Upload path:

```text
assets/images/cards/concierge-hub-visual-v1.0.0.webp
```

Implementation requirement:

- Preserve Concierges title, copy, bullets, and CTA.

### S07-C Fulfillment Providers Image Placeholder

Current placeholder:

- Selector: third `.photo-card .card-image-slot`.
- Text: `Fulfillment visual update pending`.

Replacement target:

- Local service provider / package / prepared items / delivery coordination visual.
- Should communicate capability without implying guaranteed fulfillment.

Recommended format:

- WebP preferred.
- Aspect ratio: approximately 16:7 or 2.75:1.
- Recommended source size: 800 x 300 px minimum.

Upload path:

```text
assets/images/cards/fulfillment-providers-visual-v1.0.0.webp
```

Implementation requirement:

- Preserve Fulfillment Providers title, copy, bullets, and CTA.
- Do not use internal-only language such as `self-fulfillment first`.

### S09-A Footer Logo Placeholder

Current placeholder:

- Selector: `.footer-logo-placeholder`.
- Current text: `L` / `LOGO`.

Replacement target:

- Footer version of final DFW Matchday Concierge logo.
- Should match header logo but may use a smaller optimized SVG.

Recommended format:

- SVG preferred.
- Transparent PNG acceptable.

Upload path:

```text
assets/images/logos/dfw-logo-footer-v1.0.0.svg
```

Implementation requirement:

- Preserve footer grid, brand lockup, contact block, social icons, footer links, and copyright.

### S09-C Social Icon Placeholders

Current placeholders:

- Selector: `.social-icons i`.
- Text placeholders: `IG`, `FB`, `X`, `IN`.

Replacement target:

- Social icons for Instagram, Facebook, X, and LinkedIn.

Recommended format:

- SVG preferred.
- 24 x 24 viewBox.
- Single-color line or filled icons.
- Use site gold or currentColor.

Upload path:

```text
assets/icons/social/instagram-v1.0.0.svg
assets/icons/social/facebook-v1.0.0.svg
assets/icons/social/x-v1.0.0.svg
assets/icons/social/linkedin-v1.0.0.svg
```

Implementation requirement:

- Replace text placeholders only.
- Preserve icon positions under contact information.

## Icon Design Standard

All icon assets should follow this standard:

1. SVG preferred over PNG for icons.
2. Transparent background.
3. 32 x 32 or 48 x 48 viewBox for hub icons.
4. 24 x 24 viewBox for social icons.
5. Gold line treatment matching site gold.
6. Consistent stroke width across the set.
7. No embedded raster images inside SVG icons.
8. No official tournament marks.
9. No copyrighted sports/event logos.
10. No text inside icons.
11. Accessible alt text must be provided when inserted as `<img>`.

## Raster Image Standard

All raster image assets should follow this standard:

1. WebP preferred for preview and production readiness.
2. PNG allowed for transparency.
3. JPEG allowed for photo-only assets if WebP is not available.
4. Hero image should be at least 2048 px wide.
5. Card images should be at least 800 px wide.
6. Avoid over-compression artifacts.
7. Use dark navy/gold color grading to match site UI.
8. Preserve readability under existing text overlays.

## Recommended Implementation Pattern

Use one new asset stylesheet after the current CSS files:

```html
<link rel="stylesheet" href="assets/css/replica-image-assets-v1.0.0.css">
```

Recommended new CSS file:

```text
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/css/replica-image-assets-v1.0.0.css
```

This file should do only image replacement and visual fitting.

It must not change locked structure, copy, grid, or CTA rules.

## Suggested Image Replacement CSS Pattern

Hero background:

```css
.hero-section::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: linear-gradient(180deg, rgba(4,20,35,.18), rgba(2,8,14,.82)), url("../images/hero/dfw-hero-fw-att-dallas-crown-flags-v1.0.0.webp");
  background-size: cover;
  background-position: center;
  z-index: 0;
}
.hero-content { position: relative; z-index: 1; }
```

Card image replacement:

```html
<div class="image-slot card-image-slot">
  <img src="assets/images/cards/driver-hub-visual-v1.0.0.webp" alt="Driver hub visual">
</div>
```

Icon replacement:

```html
<span class="icon-placeholder" aria-hidden="true">
  <img src="assets/icons/hubs/vip-guest-concierge-v1.0.0.svg" alt="">
</span>
```

Map replacement:

```html
<div class="map-visual">
  <img src="assets/images/maps/dfw-matchday-routes-map-v1.0.0.svg" alt="DFW matchday route map showing airport, Dallas, Fort Worth, Arlington, stadium, and fan zones">
</div>
```

## Required Handoff Inputs for Next Chat

The next chat/session should receive:

1. This handoff file.
2. The valid preview link for `index-v1.0.10.html`.
3. The PDF mockup reference image or PDF.
4. Any approved logo files.
5. Any generated image assets to upload.
6. Confirmation of the hero crown flag country set.
7. Confirmation whether Team Hubs flags should remain CSS placeholders or be replaced with SVG flag images.

## Next Chat Execution Prompt

Use this prompt to open the next image-regeneration session:

```text
You are operating inside the DFW Matchday Concierge governed workspace.

Execute: dfw_homepage_pdf_mockup_image_placeholder_regeneration_execution_v1_0_0

Repository: aw3consulting/dfwmatchdayconcierge
Branch: main
Current accepted desktop review base: docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html
Current preview: https://html-preview.github.io/?url=https://github.com/aw3consulting/dfwmatchdayconcierge/blob/main/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html

Authority handoff: docs/handoffs/dfw_homepage_pdf_mockup_image_placeholder_regeneration_handoff_draft_v1_0_0.md

Task:
Evaluate the PDF mockup against index-v1.0.10 and regenerate only image, logo, map, flag, and icon placeholder assets. Preserve all locked web elements, copy, layout, form behavior, CTA text, and section order. Replace placeholder assets using direct static asset paths inside the existing prototype folder. Create a direct static preview only. Do not create loader pages. Do not use CSS import chains for active preview files. Do not replace public index.html, /connect, DreamHost, or QR routes.

Hero requirement:
Create a main hero composite from left to right: Fort Worth skyline, AT&T Stadium, Dallas skyline, crown with flags from all 8 countries including USA. Confirm final country set before final crown generation if the current Team Hubs country list conflicts with the required USA flag.

Deliverables:
1. Uploaded image/icon/map/logo assets under the approved asset directories.
2. Minimal image-only CSS or HTML replacement changes.
3. Direct static preview link.
4. Placeholder replacement audit.
5. Confirmation that no locked non-image web element changed.
```

## Open Clarification Before Final Regeneration

The only current ambiguity is the hero crown flag set.

The current visible Team Hubs set is:

1. Netherlands
2. Japan
3. England
4. Croatia
5. Argentina
6. Austria
7. Sweden
8. Jordan

The new hero requirement says:

`all 8 countries including the USA flag`

Therefore, the next session must confirm the final eight-country set before final hero generation.

## Final Standing

HANDOFF DRAFT CREATED FOR REVIEW / DESKTOP `index-v1.0.10` REMAINS PRE-LOCKED DRAFT PENDING REVIEW / ALL NON-IMAGE WEB ELEMENTS MUST REMAIN LOCKED / IMAGE PLACEHOLDER AND ICON REGENERATION IS THE ONLY AUTHORIZED NEXT EXECUTION SCOPE.
