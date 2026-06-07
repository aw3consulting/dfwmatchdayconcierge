# DFW Homepage index-v1.0.10 Image Placeholder Regeneration Handoff v1.0.0

## Status

HANDOFF DRAFT CREATED FOR USER REVIEW / DESKTOP `index-v1.0.10` IS PRE-LOCKED DRAFT PENDING REVIEW / ALL WEB ELEMENTS LOCKED EXCEPT IMAGE AND ICON PLACEHOLDERS / MOBILE REMAINS PAUSED / PUBLIC ROUTE REPLACEMENT REMAINS BLOCKED

## Controlled Action Name

`dfw_homepage_index_v1_0_10_image_placeholder_regeneration_handoff_v1_0_0`

## Purpose

Define the next controlled action for evaluating the approved PDF mockup against the desktop `index-v1.0.10` pre-locked draft, then replacing only the current image and icon placeholders with regenerated visual assets in a way that can be previewed on the same pre-locked draft structure.

This handoff is for the next chat session. It is not the image regeneration execution itself.

## Governing Review Surface

Current pre-locked desktop draft:

`docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html`

Current direct static preview:

`https://html-preview.github.io/?url=https://github.com/aw3consulting/dfwmatchdayconcierge/blob/main/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html`

PDF mockup reference:

`dfw-homepage-pdf-inspired-premium-commercial-launch-visual-reference-v1.0.0.pdf`

## Pre-Lock Rule

The pre-lock must freeze all non-image website elements.

The next session may modify only:

1. Image placeholders.
2. Icon placeholders.
3. Flag visual assets.
4. Logo placeholder image surfaces.
5. Alt text required for image accessibility.
6. CSS background-image references required to insert generated imagery into existing visual slots.

The next session must not modify:

1. Section order.
2. Layout grid structure.
3. Text copy.
4. Navigation labels.
5. CTA text.
6. Form fields.
7. Input options.
8. Button styles.
9. Panel widths.
10. Section spacing.
11. Footer column structure.
12. Any public production route.

## Do Not Repeat Preview Rule

Do not create another invalid preview surface.

Future preview links must point only to direct static HTML files that:

1. Contain full page markup.
2. Load CSS directly through `<link rel="stylesheet">` tags.
3. Do not use JavaScript to fetch another HTML file.
4. Do not use a preview loader wrapper.
5. Do not rely on CSS `@import` for the active preview path.

## Recommended Next Preview File

For image testing, create a direct static copy rather than changing the pre-locked base immediately:

`docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10-image-preview.html`

Associated CSS:

`docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/css/replica-v1.0.10-image-preview.css`

This image-preview file must preserve all web elements from `index-v1.0.10.html` and change only image/icon placeholder surfaces.

After user approval, the image references may be merged back into the active pre-locked draft under a new version or as a controlled asset-only update.

## Asset Upload Locations

Create these folders if they do not already exist:

```text
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/generated/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/icons/generated/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/flags/generated/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/logos/generated/
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/social/generated/
```

Do not store generated homepage assets outside the prototype asset tree unless the user approves promotion into the global site asset library.

## Master Asset Naming Rules

Use lowercase kebab-case. Include section ID and purpose in filename. Use only stable extensions.

Examples:

```text
s02-hero-fort-worth-skyline.webp
s02-hero-att-stadium.webp
s02-hero-dallas-skyline.webp
s02-hero-crown-flags.webp
s03-ai-inquiry-visual.webp
s04-icon-vip-guest-concierge.svg
s05-dfw-area-map-routes.svg
s07-drivers-card-visual.webp
s09-footer-logo.svg
```

## Image Format Standard

### Photographic or image-like assets

Preferred:

- `.webp`
- sRGB
- 2x export where practical
- compressed but not visibly degraded

Fallback allowed:

- `.png` only when transparency or exact edge quality is required

Avoid:

- heavy JPEG artifacts
- AI text baked into images
- uncontrolled busy backgrounds that reduce text readability

### Icons

Preferred:

- `.svg`
- transparent background
- single-color or two-tone gold treatment
- stroke-based icons
- scalable `viewBox="0 0 64 64"` or `viewBox="0 0 48 48"`

Do not use raster icons unless required by the design.

### Flags

Preferred:

- SVG for clean scaling
- simple national flag geometry
- consistent aspect ratio

Recommended flag ratio:

- 3:2 or 4:3 for cards
- keep consistent across all team/hero placements

### Logos

Preferred:

- SVG for header/footer logo if available
- PNG with transparent background only if vector is unavailable

Do not use the wrong logo. If final logo is not ready, keep the logo placeholder.

## Asset Inventory and Replacement Map

| Section | Current placeholder / visual surface | Required replacement asset | Upload location | Recommended filename | Replacement method |
|---|---|---|---|---|---|
| S01-A | Header logo placeholder `L / LOGO SIZE` | Final logo or reviewed logo placeholder | `assets/logos/generated/` | `s01-header-logo.svg` | Replace placeholder span with `<img>` only after approval |
| S02 | Hero background currently dark overlay only | Composite or layered hero visual | `assets/images/generated/` | see S02 hero assets below | Use CSS background layers or absolute image slots without changing hero text |
| S03-A | AI image placeholder | AI inquiry visual | `assets/images/generated/` | `s03-ai-inquiry-visual.webp` | Replace image placeholder content with `<img>` |
| S04-B | VIP Guest Concierge icon placeholder | VIP concierge icon | `assets/icons/generated/` | `s04-icon-vip-guest-concierge.svg` | Replace `ICON` placeholder only |
| S04-C | Team Family Support icon placeholder | Team family icon | `assets/icons/generated/` | `s04-icon-team-family-support.svg` | Replace `ICON` placeholder only |
| S04-D | Media / Corporate icon placeholder | Media/corporate icon | `assets/icons/generated/` | `s04-icon-media-corporate.svg` | Replace `ICON` placeholder only |
| S04-E | Fan Hubs icon placeholder | Fan hubs icon | `assets/icons/generated/` | `s04-icon-fan-hubs.svg` | Replace `ICON` placeholder only |
| S04-F | Driver Onboarding icon placeholder | Driver icon | `assets/icons/generated/` | `s04-icon-drivers.svg` | Replace `ICON` placeholder only |
| S04-G | Concierge Onboarding icon placeholder | Concierge icon | `assets/icons/generated/` | `s04-icon-concierges.svg` | Replace `ICON` placeholder only |
| S04-H | Fulfillment Hub icon placeholder | Fulfillment hub icon | `assets/icons/generated/` | `s04-icon-fulfillment-hub.svg` | Replace `ICON` placeholder only |
| S05-B | Precise area map placeholder | DFW route-area map | `assets/images/generated/` or `assets/icons/generated/` | `s05-dfw-area-map-routes.svg` | Replace map placeholder only; route list remains locked |
| S05 Team cards | CSS flag blocks | Team flag SVGs if preferred | `assets/flags/generated/` | `flag-netherlands.svg`, etc. | Replace CSS flag spans only if visual improvement is approved |
| S07-B | Drivers image placeholder | Driver/vehicle card visual | `assets/images/generated/` | `s07-drivers-card-visual.webp` | Replace image placeholder only |
| S07-G | Concierges image placeholder | Concierge/operators card visual | `assets/images/generated/` | `s07-concierges-card-visual.webp` | Replace image placeholder only |
| S07 Fulfillment | Fulfillment image placeholder | Fulfillment providers card visual | `assets/images/generated/` | `s07-fulfillment-providers-card-visual.webp` | Replace image placeholder only |
| S09-A | Footer logo placeholder | Footer logo | `assets/logos/generated/` | `s09-footer-logo.svg` | Replace placeholder span with `<img>` only after approval |
| S09-C | Social placeholders | Social icons | `assets/social/generated/` | `social-instagram.svg`, `social-facebook.svg`, `social-x.svg`, `social-linkedin.svg` | Replace social placeholder text with SVG icons |

## S02 Hero Image Regeneration Requirements

### Required hero concept

The main hero must be regenerated left to right as:

1. Fort Worth skyline.
2. AT&T Stadium.
3. Dallas skyline.
4. Crown with flags.

### Required hero atmosphere

- dark blue / navy premium event tone
- gold accent compatibility
- dusk or night environment
- cinematic but not cartoonish
- no fake text in the image
- no visible public claims embedded in the image
- background must preserve readability for the existing hero headline and buttons

### Hero composition recommendation

Preferred implementation:

`single panoramic composite background`

Recommended file:

`assets/images/generated/s02-hero-fw-att-dallas-crown-flags-composite.webp`

Recommended export:

- 2400 x 760 px master
- crop-safe center band for desktop
- dark overlay preserved in CSS
- keep important visual subjects away from the center text zone

### Alternative implementation

Layered assets are allowed if they preview better:

```text
s02-hero-fort-worth-skyline.webp
s02-hero-att-stadium.webp
s02-hero-dallas-skyline.webp
s02-hero-crown-flags.webp
```

Use CSS background-position to place the layers left to right.

### Hero flag ambiguity to confirm

Current Dallas team set used in the desktop draft:

1. Netherlands
2. Japan
3. England
4. Croatia
5. Argentina
6. Austria
7. Sweden
8. Jordan

User also requested inclusion of the USA flag in the hero crown.

The next session must confirm whether the hero crown should contain:

- Option A: 9 flags total = the 8 Dallas team flags plus USA host flag.
- Option B: 8 flags total = USA plus seven selected countries.

Recommended option:

Option A is stronger because it preserves all current Dallas team flags and adds the USA flag as host-market context.

### Crown design recommendation

The crown should be a subtle premium emblem rather than a literal oversized object.

Preferred approach:

- small gold crown silhouette
- flag ribbons or mini shield flags arranged beneath or behind the crown
- low-contrast enough to sit behind the text
- not a competing logo
- no official tournament marks

## S03 AI Inquiry Image Requirements

Replacement asset:

`assets/images/generated/s03-ai-inquiry-visual.webp`

Recommended content:

- abstract AI command chip or luminous concierge planning interface
- gold AI core glow
- dark blue circuit / route-map texture
- no fake UI text
- no official tournament marks

Recommended export:

- 600 x 480 px master
- crop-safe to the current square/vertical placeholder
- WebP

Better-than-mockup recommendation:

Use a refined abstract AI planning chip rather than a generic robot or face. This is more premium and avoids unrealistic AI-person imagery.

## S04 Operating Command Hub Icon Requirements

All S04 icons should be generated as matching SVG icons.

Icon system:

- stroke style: premium thin-line icon
- stroke width: 1.75-2.25 px at 64 px viewBox
- color: site gold
- optional muted blue shadow only through CSS, not baked into SVG
- no filled cartoon icons
- no text inside icons
- consistent visual weight across all seven icons

Recommended icons:

1. VIP Guest Concierge - diamond / premium badge.
2. Team Family Support - three-person group with privacy shield.
3. Media / Corporate - briefcase or credential case.
4. Fan Hubs - flag / route marker.
5. Drivers - steering wheel / vehicle wheel.
6. Concierges - service bell / concierge desk symbol.
7. Fulfillment Hub - package / connected cube.

Better-than-mockup recommendation:

Use a governed custom SVG icon set instead of trying to copy the PDF icon set exactly. Matching stroke weight and gold color will look more professional and scale better than raster icons.

## S05 Map and Route Visual Requirements

Replacement asset:

`assets/images/generated/s05-dfw-area-map-routes.svg`

Purpose:

Replace the generic map placeholder with a precise DFW area route map.

Required labeled areas:

- DFW Airport
- Dallas Love Field
- Fort Worth
- Arlington
- Dallas
- Stockyards
- Stadium Zone
- Fan Experience Zones

Style:

- dark navy base
- gold route lines
- circular or shield nodes
- clean line map, not a photographic map screenshot
- route list on the right remains locked

Recommended format:

- SVG preferred for crisp linework
- WebP acceptable only if SVG becomes too detailed

Better-than-mockup recommendation:

Use a custom vector route-map illustration rather than a map screenshot. This avoids licensing issues, gives cleaner brand control, and supports scalable preview.

## S05 Team Flags Requirements

Current team hub cards:

- Netherlands
- Japan
- England
- Croatia
- Argentina
- Austria
- Sweden
- Jordan

Potential improvement:

Replace CSS flags with clean SVG flag assets only if they preserve the same card layout and improve fidelity.

Upload location:

`assets/flags/generated/`

Required filenames:

```text
flag-netherlands.svg
flag-japan.svg
flag-england.svg
flag-croatia.svg
flag-argentina.svg
flag-austria.svg
flag-sweden.svg
flag-jordan.svg
flag-usa.svg
```

USA flag is required for the hero crown. It does not need to appear in the S05 Team Hubs cards unless the user adds USA to that section.

## S07 Card Image Requirements

### Drivers

Replacement asset:

`assets/images/generated/s07-drivers-card-visual.webp`

Recommended visual:

- black executive SUV or premium vehicle silhouette
- airport/stadium route mood
- no visible license plate
- no identifiable real person unless licensed/approved
- dark navy/gold brand color match

### Concierges

Replacement asset:

`assets/images/generated/s07-concierges-card-visual.webp`

Recommended visual:

- professional concierge/operator desk or coordinated support team
- premium hospitality tone
- avoid stock-photo awkwardness
- avoid official tournament marks

### Fulfillment Providers

Replacement asset:

`assets/images/generated/s07-fulfillment-providers-card-visual.webp`

Recommended visual:

- local provider / delivery / errand / packaged support visual
- premium task execution tone
- avoid making it look like a generic food-delivery app
- show capability without unsupported service guarantees

Recommended export for all S07 images:

- 900 x 420 px master
- WebP
- dark overlay compatible
- crop-safe center subject

## S09 Footer Logo and Social Icons

### Footer logo

Use the same approved brand direction as S01 header logo after approval.

Upload:

`assets/logos/generated/s09-footer-logo.svg`

### Social icons

Upload:

```text
assets/social/generated/social-instagram.svg
assets/social/generated/social-facebook.svg
assets/social/generated/social-x.svg
assets/social/generated/social-linkedin.svg
```

Format:

- SVG
- gold stroke or gold fill
- 24 x 24 viewBox
- transparent background
- no enclosing bitmap circle unless the design calls for it

## Replacement Implementation Rules

### HTML allowed changes

Allowed:

- replace placeholder `<span>` or `<div>` content with `<img>` or `<picture>`
- add `alt` text
- add `loading="lazy"` where appropriate below hero
- add `decoding="async"` below hero

Not allowed:

- changing copy
- changing CTA labels
- changing form fields
- changing layout wrappers
- changing section order
- changing navigation
- changing public claim text

### CSS allowed changes

Allowed:

- `background-image`
- `object-fit`
- `object-position`
- image slot sizing when required to preserve current layout
- icon color handling if SVGs use `currentColor`

Not allowed:

- section layout changes
- grid changes
- unrelated spacing changes
- button style changes
- typography changes not required for image fit

## Preview Validation Checklist

The next session must verify:

1. Direct static preview link opens.
2. No invalid loader pages.
3. No CSS import chain on active review file.
4. Hero text remains readable.
5. Image replacements do not alter layout.
6. Icons align inside existing card positions.
7. Map remains within the existing map panel.
8. S07 images fill their card slots evenly.
9. Footer logo and social icons do not break equal column layout.
10. No public route replacement occurs.

## Handoff Prompt for Next Chat Session

Use the following prompt to open the next session:

```text
You are operating inside the DFW Matchday Concierge governed workspace.

Execute controlled action:

dfw_homepage_index_v1_0_10_image_placeholder_regeneration_execution_v1_0_0

Current desktop review base:

docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html

Current standing:

DESKTOP index-v1.0.10 PASSED INITIAL HOMEPAGE PRE-LOCKED DRAFT / PENDING REVIEW / NOT FULLY LOCKED / MOBILE PAUSED / PUBLIC ROUTE REPLACEMENT BLOCKED.

Use this handoff as authority:

docs/handoffs/dfw-homepage-index-v1.0.10-image-placeholder-regeneration-handoff-v1.0.0.md

Mission:

Evaluate the PDF mockup against index-v1.0.10 only for image and icon placeholder replacement. Preserve all web elements, copy, layout, form fields, CTAs, navigation, sections, and public-route boundaries. Replace only image placeholders, icon placeholders, flag visuals where approved, footer logo placeholder, and social icon placeholders.

Do not create a loader-style preview. Do not use CSS import chains for active preview files. Create a direct static image-preview file and direct CSS file. Provide only direct static preview links.

Hero requirement:

Build the main hero left to right as Fort Worth skyline, AT&T Stadium, Dallas skyline, and a crown with flags. Confirm whether the crown uses 9 flags total - the 8 Dallas team flags plus USA - or 8 total including USA before final generation.

Required output:

1. Asset inventory confirmation.
2. Generated asset file paths.
3. Direct static image-preview HTML path.
4. Direct static preview link.
5. Verification that only image/icon placeholders changed.
6. No public route replacement.
```

## Final Standing

HANDOFF DRAFT READY FOR USER REVIEW / DESKTOP `index-v1.0.10` REMAINS PRE-LOCKED DRAFT PENDING REVIEW / ALL NON-IMAGE WEB ELEMENTS MUST REMAIN FROZEN / NEXT SESSION MAY TOUCH IMAGE AND ICON PLACEHOLDERS ONLY / MOBILE PAUSED / PUBLIC ROUTE REPLACEMENT BLOCKED.
