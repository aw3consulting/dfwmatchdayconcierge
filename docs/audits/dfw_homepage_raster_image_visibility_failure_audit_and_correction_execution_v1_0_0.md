# DFW Homepage Raster Image Visibility Failure Audit and Correction Execution v1.0.0

Mission: `dfw_homepage_raster_image_visibility_failure_audit_and_correction_execution_v1_0_0`

Repository: `aw3consulting/dfwmatchdayconcierge`

Branch: `main`

Accepted review base: `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html`

Diagnostic page: `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-raster-visibility-diagnostic-v1.0.0.html`

Corrected candidate: `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.18-raster-image-visibility-corrected.html`

## Root cause summary

The accepted base is not a broad raster-image implementation. It contains only one active raster image dependency: the approved header PNG logo at `assets/images/logos/dfw-logo-header-raster-v1.0.2.png`. All other homepage visual dependencies in `index-v1.0.10.html` are SVG-based.

Source review confirms the approved header PNG is already a direct HTML `<img>` in the accepted base. CSS review confirms the v1.0.10 correction layer explicitly forces the header PNG to `display:block`, `visibility:visible`, `opacity:1`, `width:54px`, `height:54px`, `max-width:54px`, `max-height:54px`, `object-fit:contain`, and `filter:none`. Therefore the failure is not a missing `<img>` tag and not a global CSS rule hiding all `<img>` tags.

Most likely remaining causes are: preview-surface asset serving/cache behavior, raster asset content/contrast, stale review URL, or binary asset/path behavior. Live html-preview/GitHub Pages browser verification could not be completed inside this execution environment because external GitHub/browser fetches were blocked or unsafe-gated. This audit therefore does not claim final live browser-visible success; it commits a raster-only diagnostic page and a raster-visible correction candidate to make the issue testable in a direct static browser.

## Mandatory repository search summary

| Search | Finding |
|---|---|
| `.svg` | Active in `index-v1.0.10.html` for hero, AI chip, hub icons, map, lower cards, footer logo, and social icons. |
| `.png` | Active in `index-v1.0.10.html` only for the approved header logo. |
| `.jpg` | No active JPG dependency found in the accepted draft. |
| `.jpeg` | No active JPEG dependency found in the accepted draft. |
| `.webp` | No active WebP dependency found in the accepted draft. |
| `<img` | Present for one PNG and multiple SVGs. |
| `background-image` / `url(` | No corrected-candidate image dependency uses CSS URL image loading. |
| `data:image` | Not used in the corrected homepage candidate. Used once in the diagnostic page only for a generated PNG browser-control swatch. |

## Active image dependency table for `index-v1.0.10.html`

| # | Section | Element | Type | Path | Status |
|---:|---|---|---|---|---|
| 1 | Header | `.logo-placeholder img` | PNG | `assets/images/logos/dfw-logo-header-raster-v1.0.2.png` | Exists; reported invisible in review. |
| 2 | Hero | `.hero-visual` | SVG | `assets/images/hero/dfw-hero-fw-att-dallas-crowd-flags-v1.0.0.svg` | SVG. |
| 3 | Inquiry | `.ai-image-slot img` | SVG | `assets/images/cards/ai-inquiry-command-chip-v1.0.0.svg` | SVG. |
| 4 | Hubs | VIP icon | SVG | `assets/icons/hubs/vip-guest-concierge-v1.0.0.svg` | SVG. |
| 5 | Hubs | Team Family icon | SVG | `assets/icons/hubs/team-family-support-v1.0.0.svg` | SVG. |
| 6 | Hubs | Media/Corporate icon | SVG | `assets/icons/hubs/media-corporate-v1.0.0.svg` | SVG. |
| 7 | Hubs | Fan Hubs icon | SVG | `assets/icons/hubs/fan-hubs-v1.0.0.svg` | SVG. |
| 8 | Hubs | Driver icon | SVG | `assets/icons/hubs/driver-onboarding-v1.0.0.svg` | SVG. |
| 9 | Hubs | Concierge icon | SVG | `assets/icons/hubs/concierge-onboarding-v1.0.0.svg` | SVG. |
| 10 | Hubs | Fulfillment icon | SVG | `assets/icons/hubs/fulfillment-hub-v1.0.0.svg` | SVG. |
| 11 | Routes | `.map-visual img` | SVG | `assets/images/maps/dfw-matchday-routes-map-v1.0.0.svg` | SVG. |
| 12 | Lower cards | Driver visual | SVG | `assets/images/cards/driver-hub-visual-v1.0.0.svg` | SVG. |
| 13 | Lower cards | Concierge visual | SVG | `assets/images/cards/concierge-hub-visual-v1.0.0.svg` | SVG. |
| 14 | Lower cards | Fulfillment visual | SVG | `assets/images/cards/fulfillment-providers-visual-v1.0.0.svg` | SVG. |
| 15 | Footer | Footer logo | SVG | `assets/images/logos/dfw-logo-footer-v1.0.0.svg` | SVG. |
| 16 | Footer social | Instagram | SVG | `assets/icons/social/instagram-v1.0.0.svg` | SVG. |
| 17 | Footer social | Facebook | SVG | `assets/icons/social/facebook-v1.0.0.svg` | SVG. |
| 18 | Footer social | X | SVG | `assets/icons/social/x-v1.0.0.svg` | SVG. |
| 19 | Footer social | LinkedIn | SVG | `assets/icons/social/linkedin-v1.0.0.svg` | SVG. |

## Raw raster validation

Only one active raster asset is used by the accepted draft.

| Raster asset | Exists | Size | Dimensions | Path validation | Transparency/contrast |
|---|---:|---:|---|---|---|
| `assets/images/logos/dfw-logo-header-raster-v1.0.2.png` | Yes, fetched by GitHub contents API. | Greater than zero; binary PNG returned. | PNG header indicates 700 × 525. | Relative path matches exactly from `index-v1.0.10.html`. | Full pixel inspection could not be completed through the text-only GitHub fetch path; contrast remains a live review item. |

## Browser/network audit standing

Live network browser verification could not be completed by the available tools.

Evidence:

1. Container `git clone` failed with `Could not resolve host: github.com`.
2. Browser/web open of the provided html-preview URL returned a cache-miss fetch failure.
3. GitHub Pages direct open was blocked by the browsing safety gate because the URL was not returned by search or supplied by the user.
4. GitHub text fetch rejects direct binary PNG inspection as a binary file.
5. Local Playwright navigation to `file://` and `127.0.0.1` was administrator-blocked. A content-injected Chromium check with raster data confirmed the browser engine computes raster images as loaded and visible, but it does not prove the live relative GitHub asset path.

## Corrected candidate actions

| Placement | Before | After |
|---|---|---|
| Header logo | Direct PNG inside `.logo-placeholder` wrapper. | Direct PNG as immediate header anchor child, explicit 54×54. |
| Footer logo | SVG. | Direct PNG, explicit 44×44. |
| Hero visual | SVG. | Clean raster placeholder pending final PNG/JPEG. |
| AI visual | SVG. | Clean raster placeholder pending final PNG/JPEG. |
| Hub icons | SVG. | Clean text placeholders pending raster icon set. |
| Map | SVG. | Clean raster placeholder pending final PNG/JPEG. |
| Driver/Concierge/Fulfillment cards | SVG. | Clean raster placeholders pending final PNG/JPEG. |
| Footer socials | SVG. | Text placeholders. |
| Team flags | CSS-gradient locked web elements. | Unchanged. |

## Controls preserved

- No public `index.html` replacement.
- No `/connect` replacement.
- No DreamHost deployment.
- No QR activation.
- `assets/connect-qr.svg` remains untouched.
- Team Hub / Fan Hub flags remain locked CSS-rendered web elements.
- No non-QR SVG image reference remains in the corrected candidate page.
- Corrected candidate uses no CSS import chain; it is self-contained.
- No intentional change to locked non-image copy, labels, forms, route labels, phone, email, dates, navigation, sponsor labels, or responsibility copy.

## Remaining blockers

1. Direct static browser review must be completed outside this blocked execution environment.
2. If the diagnostic page shows the generated PNG swatch but not the header PNG, the header asset must be replaced with a verified repository PNG/JPEG through a binary-capable commit path.
3. If the diagnostic header PNG shows but the corrected candidate header does not, the remaining fault is candidate CSS/layout specific.
4. Final raster assets are still required for hero, AI visual, hub icon set, map, cards, and social icons.

## Final standing

CORRECTION CANDIDATE CREATED / RASTER-ONLY DIAGNOSTIC CREATED / NON-QR SVG IMAGE REFERENCES REMOVED FROM CANDIDATE / QR UNTOUCHED / TEAM FLAGS UNCHANGED / NO PRODUCTION DEPLOYMENT / LIVE BROWSER-VISIBLE SUCCESS NOT CLAIMED BECAUSE NETWORK/BROWSER REVIEW IS BLOCKED IN THIS EXECUTION ENVIRONMENT.
