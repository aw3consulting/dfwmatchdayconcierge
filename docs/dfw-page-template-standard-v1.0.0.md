# DFW Matchday Concierge — Reusable Page Template Standard v1.0.0

**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** Template foundation standard / not production approval  

## 1. Authority boundary

This standard derives from the re-locked homepage v1.0.10 information-hub / command-hub authority. It must not be used to promote the current public booking/service baseline, PR #1, v1.0.18, v1.0.19, or the compact embedded diagnostic derivative as homepage authority.

## 2. Required HTML document structure

Every future page must use:

1. `<!doctype html>`.
2. `<html lang="en">` unless a language-specific page requires a different language code.
3. UTF-8 charset.
4. Mobile viewport meta.
5. Canonical title and meta description.
6. Noindex only for preview-only or diagnostic surfaces.
7. A skip link before the visual shell.
8. A global header component.
9. One semantic `<main>` region.
10. A global footer component.
11. Defer or inline only the JavaScript needed for the page.

## 3. Header / navigation rules

The global header inherits the v1.0.10 header logic:

- visible logo region,
- brand name lockup,
- primary navigation,
- call-to-action region,
- keyboard focus states,
- responsive wrap behavior,
- no hidden inaccessible navigation,
- no image-path dependency for the logo unless served-safe proof exists.

Required navigation categories for homepage-derived hub pages:

- Matchday Guides,
- Command Hubs,
- Fan Hubs,
- Drivers,
- Concierges,
- Fulfillment,
- About / Responsibility / Contact.

## 4. Footer rules

Every future page must include:

- brand lockup,
- phone and email where approved,
- Dallas / Fort Worth location context,
- operating system links,
- hubs and services links,
- resources links,
- company/responsibility links,
- social icons only if assets are approved and either embedded or proven served-safe,
- copyright line.

## 5. Hero section rules

The homepage hero standard is:

- a visual hero image or safe approved visual region,
- a locality or lane eyebrow,
- a command-hub headline,
- one concise subtitle,
- primary and secondary CTAs,
- a clear operator-assisted / scope-reviewed note,
- no guarantee language unless separately mapped to live capability.

Future pages may use a smaller page-title hero but must preserve the same hierarchy.

## 6. Page-title section rules

Non-homepage pages must have:

- page title,
- short purpose statement,
- route/lane context,
- scope boundary note,
- primary inquiry CTA,
- related hub links.

## 7. Card-grid rules

Card grids must be used for:

- command hubs,
- service lanes,
- route options,
- fan resources,
- coordinator tasks,
- driver/concierge/fulfillment functions.

Every card must include:

- title,
- short body,
- approved image/icon only if asset is embedded or served-safe,
- clear CTA or no CTA,
- no unsupported claim.

## 8. Route / map section rules

Map and routing sections must:

- use approved map visuals only,
- never imply guaranteed timing,
- include route examples as planning references,
- distinguish airport/stadium/hotel/fan-zone routes,
- include operator review language.

## 9. Sponsor / ad inventory section rules

Sponsor sections may include:

- title sponsor placement,
- airport transfer partner,
- dining partner,
- hotel/area partner,
- fan experience partner,
- sponsor inquiry CTA.

No sponsor claim may imply an active partner unless the partner is live and documented.

## 10. Team / fan hub rules

Team and fan hub pages must define:

- team/fan context,
- venue relation,
- route options,
- discovery resources,
- matchday timing notes,
- language/localization needs where applicable.

## 11. Driver / concierge / fulfillment rules

Driver, concierge, and fulfillment pages must preserve:

- role definition,
- acceptance/availability boundary,
- operator review workflow,
- provider responsibility boundaries,
- no insurance/licensing claims unless mapped and verified.

## 12. Inquiry / CTA rules

All inquiry interactions must be:

- source-visible,
- keyboard accessible,
- non-breaking if JavaScript fails,
- clear that inquiry is not automatic confirmation,
- mapped to an approved email, form, or intake mechanism.

## 13. Image sizing and embedding rules

Required images must follow the asset handling standard:

- use original approved assets,
- embed optimized data only when path serving is not proven safe,
- no compact substitutes,
- no placeholder image passes,
- no blank image panels,
- preserve dimensions and alt text.

## 14. CSS naming and component rules

Use stable component naming:

- `.site-header`,
- `.primary-nav`,
- `.hero-section`,
- `.inquiry-panel`,
- `.path-grid`,
- `.path-card`,
- `.command-grid`,
- `.map-panel`,
- `.team-mini-panel`,
- `.sponsor-rail`,
- `.photo-card`,
- `.responsibility-panel`,
- `.site-footer`.

CSS must avoid route-specific hacks unless scoped to the page.

## 15. JavaScript behavior rules

JavaScript must be:

- small,
- deterministic,
- non-blocking,
- accessibility-aware,
- error-visible in preview,
- tested on desktop and mobile.

Every script must have a documented purpose.

## 16. Mobile responsiveness rules

Every page must pass:

- single-column mobile stacking,
- readable navigation,
- no horizontal overflow,
- visible images,
- usable CTAs,
- readable form fields,
- footer link clarity.

## 17. Accessibility rules

Every page must include:

- skip link,
- semantic headings,
- meaningful alt text,
- keyboard focus states,
- sufficient contrast,
- form labels,
- no image-only critical content.

## 18. SEO / meta rules

Every production candidate must include:

- unique title,
- unique description,
- canonical URL when production-bound,
- Open Graph basics when approved,
- noindex for preview-only surfaces,
- schema only when claims are verified.

## 19. Schema / structured-data rules

Schema may be added only after:

- business identity is verified,
- service areas are approved,
- contact data is approved,
- claims are capability-mapped,
- production route is approved.

## 20. Validation gates

No future page may enter preview unless it passes:

1. authority classification,
2. claim map,
3. asset map,
4. image rendering map,
5. desktop source review,
6. mobile source review,
7. accessibility review,
8. no unsupported claims.

No future page may enter production unless it passes served desktop/mobile validation and user approval.
