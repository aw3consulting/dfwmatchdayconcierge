# DFW Matchday Concierge — Asset Handling and Image Rendering Standard v1.0.0

**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** Required asset standard for homepage and 50+ page build / not production approval  

## 1. Purpose

This standard prevents repeat failure where a page text/layout renders but PNG/raster image panels appear blank in served preview.

## 2. Non-negotiable image rules

1. No required image slot may be blank.
2. No compact substitute image may satisfy production-readiness.
3. No placeholder image may satisfy production-readiness.
4. Original approved assets must be used.
5. If an asset path is not proven served-safe, the original optimized asset must be embedded or the page must remain Required-Correction.
6. A page with unproven image rendering may not be production-ready.

## 3. Source asset inventory requirement

Every page must maintain an inventory with:

- asset purpose,
- source path,
- file type,
- source SHA or hash where available,
- byte size where tooling exposes it,
- rendered dimensions,
- alt text,
- served-safe status,
- embedded status,
- validation evidence.

## 4. Served-safe proof requirement

A path is served-safe only when all conditions pass:

1. exact page URL returns non-404,
2. exact asset URL returns non-404,
3. browser renders the asset visibly,
4. mobile viewport renders the asset visibly,
5. no console/raster diagnostic error appears,
6. evidence is recorded.

Source existence alone is not served-safe proof.

## 5. Embedding requirement

If served-safe proof is not available, the production-readiness preview must embed the original optimized image data.

Embedded asset requirements:

- use the actual original source image, not a substitute,
- optimize only losslessly or under an explicit visual-quality rule,
- preserve alt text,
- preserve intended slot sizing,
- document original source path,
- document optimized byte size,
- include no path dependency for required image slots.

## 6. Optimization rule

Allowed optimization:

- PNG crush/optimization,
- dimension-preserving compression when visually lossless,
- WebP/AVIF only if explicitly authorized and browser support is tested,
- SVG only if the source asset is actually SVG or if vector conversion is separately authorized.

Not allowed:

- compact substitute images,
- generic placeholders,
- blank fills masquerading as images,
- replacing approved imagery with unrelated generated graphics,
- changing brand/logo design.

## 7. HTML rules

Every image must include:

- `src` using either a proven-safe path or original embedded data URI,
- `alt` text unless purely decorative,
- width/height or CSS sizing that prevents layout shift,
- `loading="lazy"` only below the fold,
- `decoding="async"` unless critical render demands otherwise.

Critical images should include diagnostic markers in preview builds.

## 8. CSS rules

Image containers must define:

- visible dimensions,
- object-fit behavior,
- overflow rules,
- fallback outline for preview diagnostics,
- no CSS that hides image opacity, visibility, display, width, or height accidentally.

## 9. JavaScript diagnostics

Preview builds should include raster diagnostics that:

- attach error handlers to critical images,
- detect `naturalWidth === 0`,
- write visible failure labels in preview,
- log the failing src,
- never hide the broken region.

Production builds may remove visible diagnostic labels only after served validation passes.

## 10. Required v1.0.10 homepage asset inventory

Required assets for homepage v1.0.10 production-readiness preview:

1. Header raster logo / canary.
2. Footer logo.
3. Hero image.
4. AI inquiry image.
5. VIP Guest Concierge hub icon.
6. Team Family Support hub icon.
7. Media / Corporate hub icon.
8. Fan Hubs hub icon.
9. Driver Onboarding hub icon.
10. Concierge Onboarding hub icon.
11. Fulfillment Hub icon.
12. DFW map/routes image.
13. Driver image.
14. Concierge image.
15. Fulfillment Providers image.
16. Instagram icon.
17. Facebook icon.
18. X icon.
19. LinkedIn icon.
20. Any additional image referenced by the source.

## 11. Validation gate

A page fails image readiness if any of the following is true:

- asset base64 cannot be retrieved intact for required embedding,
- asset path cannot be externally opened,
- asset URL returns 404,
- asset is invisible in browser,
- mobile image layout fails,
- image is a placeholder or compact substitute,
- original authoritative asset changed without authorization.

## 12. Required-Correction outcome

When image validation fails, the page must be classified:

**Required-Correction / not production-ready**

The record must include the affected asset list, affected file path, exact blocker, and method needed to complete full-capability work.
