# DFW Matchday Concierge — 50+ Page Build Readiness Checklist v1.0.0

**Repository:** `aw3consulting/dfwmatchdayconcierge`  
**Branch:** `main`  
**Created:** 2026-06-09  
**Standing:** Build-readiness checklist / not production approval  

## 1. Purpose

This checklist governs the upcoming 50+ page build so every page derives from the approved homepage v1.0.10 information-hub / command-hub standard instead of drifting into a disconnected booking/service baseline.

## 2. Global sections

These sections are global:

- header navigation,
- footer information hub,
- inquiry / contact CTA pattern,
- public claims / responsibility boundary,
- brand/logo handling,
- core CSS naming and spacing system,
- mobile responsiveness rules,
- accessibility rules,
- preview/production validation gates.

## 3. Reusable sections

These sections may be reused:

- command hub card grid,
- route/map section,
- team/fan hub grid,
- sponsor/ad inventory rail,
- driver panel,
- concierge panel,
- fulfillment provider panel,
- inquiry preview panel,
- responsibility cards.

## 4. Page-specific sections

These sections are page-specific:

- route details,
- airport details,
- hotel/area details,
- team-specific content,
- fan group content,
- sponsor category content,
- driver onboarding requirements,
- concierge task menus,
- fulfillment provider categories,
- localized language support,
- event-specific dates and venue rules.

## 5. Reusable assets

Assets may be reused only if approved and rendered-safe:

- brand logo,
- hub icons,
- route/map visuals,
- driver/concierge/fulfillment visuals,
- social icons,
- sponsor placeholders only as clearly empty inventory, not claimed partners.

No image reuse is allowed if it becomes a placeholder or generic substitute for a required unique page visual.

## 6. Unique template needs

| Page family | Unique template need |
|---|---|
| Homepage | full command-hub information architecture. |
| Route pages | route/map module and route-specific CTA. |
| Airport pages | airport arrival/departure logic and luggage note. |
| Matchday logistics pages | matchday timing, venue movement, operator review. |
| Fan hub pages | fan discovery, route examples, team/venue context. |
| Team hub pages | verified team data and localization. |
| VIP/team family pages | privacy, scope, operator review, no guarantee language. |
| Driver pages | role boundaries and provider responsibility. |
| Concierge pages | task boundaries and acceptance rules. |
| Fulfillment pages | provider/task boundaries and no false network claims. |
| Sponsor pages | ad inventory and commercial inquiry structure. |
| Contact/inquiry pages | form behavior, response rules, no auto-confirmation. |

## 7. Preview admission checklist

Before a page is allowed into preview:

- authority/source record exists,
- page type is defined,
- inherited sections are mapped,
- page-specific sections are mapped,
- all claims are capability-mapped,
- all images are inventoried,
- required images are embedded or served-safe,
- no compact substitutes are used,
- no placeholder image pass is used,
- desktop source review passes,
- mobile source review passes,
- accessibility source review passes,
- JavaScript behavior is documented.

## 8. Production admission checklist

Before a page is allowed into production:

- exact served URL returns non-404,
- page visually renders on desktop,
- page visually renders on mobile,
- all images render,
- no blank panels remain,
- CSS loads,
- JavaScript does not break rendering,
- forms/CTAs behave as expected,
- claims are capability-approved,
- QR implications are reviewed if relevant,
- user approval is recorded,
- deployment target is authorized.

## 9. Required evidence per page

Each page must produce:

1. source path,
2. preview URL,
3. asset inventory,
4. claim map,
5. desktop evidence,
6. mobile evidence,
7. accessibility notes,
8. unresolved blockers,
9. production-readiness standing.

## 10. Build sequence

Recommended order:

1. Finish v1.0.10 homepage production-readiness standard.
2. Lock global header/footer/component system.
3. Lock asset handling standard.
4. Build hub index pages.
5. Build service lane pages.
6. Build airport/route pages.
7. Build fan/team pages.
8. Build driver/concierge/fulfillment pages.
9. Build sponsor/contact/support pages.
10. Validate every page through preview gates before production consideration.

## 11. Block condition

No page should proceed if any required original asset cannot be retrieved, embedded, served-safe-proven, or visually validated.
