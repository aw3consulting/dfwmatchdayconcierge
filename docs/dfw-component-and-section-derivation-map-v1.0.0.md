# DFW Matchday Concierge — Component and Section Derivation Map v1.0.0

**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** 50+ page derivation map / not production approval  

## 1. Purpose

This map defines how future DFW Matchday Concierge pages inherit from the approved homepage v1.0.10 information-hub / command-hub standard.

## 2. Global sections

The following sections are global or near-global:

| Section | Global use | Notes |
|---|---:|---|
| Header navigation | required | Must remain accessible and brand-consistent. |
| Footer information hub | required | Contact/resource/navigation structure. |
| Responsibility / public claims boundary | required where claims appear | Prevents unsupported launch claims. |
| Inquiry / CTA strip | recommended | Must not imply automatic confirmation. |
| Sponsor/ad inventory rail | optional global | Only if sponsor inventory is part of the page purpose. |

## 3. Reusable homepage-derived sections

| v1.0.10 section | Reusable page family | Derivation rule |
|---|---|---|
| Title Sponsor Hero | sponsor, partner, homepage, fan hub | Keep sponsor language conditional unless sponsor is live. |
| Command Hub Hero | homepage, hub pages, route pages | Use page-specific headline but preserve command-hub hierarchy. |
| AI-Assisted Inquiry Preview | inquiry, planning, VIP, coordinator pages | Use only where an intake path exists or is clearly previewed. |
| Operating Command Hubs | hub index, lane pages | Cards may be filtered by page type. |
| DFW Map & Routes | airport, matchday, fan, hotel, city pages | Must remain planning guidance, not timing guarantee. |
| Team Hubs | team/fan pages | Team data must be current and verified before public production. |
| Drivers panel | driver onboarding, fulfillment, route ops pages | Must preserve provider responsibility boundaries. |
| Concierges panel | concierge, VIP, hospitality pages | Must preserve operator review boundaries. |
| Fulfillment Providers panel | fulfillment, errands, delivery, partner pages | Must not imply live provider network without mapping. |
| Responsibility panel | all public pages with service claims | Required for production-bound pages. |

## 4. Page-specific sections

Future pages may add page-specific modules only after authority mapping:

- airport-specific routing module,
- stadium/venue module,
- hotel/area module,
- team/fan module,
- language/localization module,
- sponsor category module,
- driver eligibility module,
- concierge task module,
- fulfillment provider module,
- route timing disclaimer module.

## 5. Page types needing unique templates

| Page type | Template need | Required unique elements |
|---|---|---|
| Homepage | unique | Full information-hub / command-hub assembly. |
| Hub index page | semi-unique | filtered hub card grid and lane routing. |
| Service lane page | reusable | page-title hero, service cards, inquiry CTA, scope boundaries. |
| Route/city page | reusable | route map, pickup/drop-off context, operator timing note. |
| Team/fan page | reusable with data | verified team/fan data and localization. |
| Driver page | unique compliance | driver role, onboarding scope, provider responsibility. |
| Concierge page | unique compliance | concierge role, task boundaries, operator review. |
| Fulfillment page | unique compliance | provider/task boundaries and no unverified network claims. |
| Sponsor/advertising page | unique commercial | ad inventory, category terms, no false sponsor status. |
| Contact/inquiry page | unique operational | intake mechanics and response expectation. |

## 6. Asset reuse map

| Asset family | Reuse status | Rule |
|---|---:|---|
| Logo | global | Must be embedded or served-safe; no blank logo allowed. |
| Hero image | homepage-specific unless approved | Do not reuse as generic placeholder. |
| Hub icons | reusable | Must be actual original/approved assets, not compact substitutes. |
| Route/map image | reusable with route pages | Must be verified at served preview. |
| Driver/concierge/fulfillment visuals | reusable in relevant lanes | Must preserve alt text and no claim inflation. |
| Social icons | global if approved | Must render or be removed until approved. |

## 7. Inheritance rule

A future page inherits the homepage standard only if it preserves:

1. global header,
2. global footer,
3. source claim boundaries,
4. image rendering rules,
5. mobile rules,
6. accessibility rules,
7. validation gates.

## 8. Preview admission gate

Before any page may enter preview:

- authority route must be documented,
- page type must be identified,
- component derivation must be mapped,
- all assets must be embedded or served-safe,
- no unsupported public claim may remain,
- desktop/mobile source review must pass.

## 9. Production admission gate

Before any page may enter production:

- exact served URL must return non-404,
- desktop browser evidence must pass,
- mobile browser evidence must pass,
- every image must render,
- CSS and JS must load and execute safely,
- claim review must pass,
- QR implications must be reviewed if route is linked from QR flow,
- user approval must be recorded.
