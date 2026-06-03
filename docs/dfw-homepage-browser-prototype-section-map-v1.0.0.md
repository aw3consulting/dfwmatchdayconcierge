# DFW Homepage Browser Prototype Section Map v1.0.0

## 1. Controlled Action

`dfw_homepage_browser_prototype_section_map_package`

## 2. Status

`LOCKED / BROWSER-PROTOTYPE SECTION MAP CREATED / HOMEPAGE V1.0.3 HTML-CSS PROTOTYPE MUST FOLLOW THIS MAP / MOCKUP GENERATION REMAINS BLOCKED`

## 3. Purpose

This section map defines the required semantic homepage structure before future HTML/CSS prototype work begins.

It supports browser-prototype-first execution, PDF-to-HTML conversion readiness, responsive layout control, sponsor monetization clarity, visitor utility, and claim-safe public presentation.

## 4. Source Authority

This map must be used with:

1. `docs/mockups/dfw-information-planning-hub-front-page-desktop-dark-contrast-final-review-v1.0.0.pdf`
2. `docs/mockups/dfw-information-planning-hub-front-page-mobile-dark-contrast-final-review-v1.0.0.pdf`
3. `docs/dfw-frontend-mockup-pdf-generation-pdf-to-html-conversion-and-responsiveness-standard-v1.0.0.md`
4. `docs/dfw-frontend-website-ux-density-and-above-the-fold-action-standard-v1.0.0.md`
5. `docs/dfw-frontend-mockup-standard-browser-prototype-first-addendum-v1.0.0.md`
6. `docs/dfw-homepage-preservation-matrix-v1.0.0.md`

## 5. Required Semantic Order

The homepage browser prototype must use this semantic order:

1. skip link
2. site header
3. primary navigation
4. title sponsor lane
5. hero
6. main action module
7. popular needs fast paths
8. guide gateway
9. sponsor inventory
10. official-source lane
11. provider and referral handoff
12. reviewed support boundary
13. trust row
14. footer
15. disclaimer

Visual layouts may use multi-column desktop composition, but the DOM and reading order must remain logical and conversion-ready.

## 6. Section Map

| # | Section | Semantic HTML element | Component name | UX purpose | Content requirements | Sponsor or claim controls | Desktop layout rule | Mobile layout rule | Failure triggers |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | Skip link | `a.skip-link` | SkipLink | Provide accessibility path to main content | Link to `#main` | No sponsor or claim content | Visually hidden until focus | Visually hidden until focus | Missing keyboard skip path |
| 2 | Site header | `header.site-header` | SiteHeader | Establish brand, logo, and site identity | Approved logo direction, DFW Matchday Information + Planning Hub naming, business CTA access | No official affiliation implication | Header fits 1440px viewport and supports sponsor lane | Compact header with menu access | Brand drift, logo drift, overloaded mobile header |
| 3 | Primary navigation | `nav.primary-nav` | PrimaryNavigation | Provide stable route access | Find My Matchday Plan, Guides, Team Hubs, Transportation, Dining & Watch Parties, Hotels & Areas, Fan Fest & Events, About | No Connect visitor CTA | Horizontal desktop nav with stable labels | Menu or compact disclosure | Label drift, missing primary routes |
| 4 | Title sponsor lane | `aside.sponsor-header-lane` | SponsorHeaderLane | Present premium available title sponsor placement | Available title sponsor label, placement context, advertiser CTA | Available until sold and approved; no real logos unless approved | Integrated near header without crowding | Compact sponsor card or collapsible sponsor lane | Missing sponsor lane, sold-looking treatment, fake mark |
| 5 | Hero | `section.hero` | PageHero | Create premium public gateway and immediate value | Concise hero statement, city/event planning positioning, high-utility orientation | Independent platform framing; no official affiliation claim | Strong visual hierarchy with adjacent action utility | Compact hero before action module | Weak hero, document heading feel, dashboard compression |
| 6 | Main action module | `section.primary-action-hub` | PrimaryActionHub | Let visitors start planning immediately | Find My Matchday Plan search/selector, Build My Matchday Plan CTA, View Recommended Guides CTA, language and contrast controls | No live AI, dispatch, booking, or payment claim | Above-the-fold utility panel with readable controls | First-screen or near-first-screen action card | Actions hidden below copy, unreadable controls, unvalidated live claims |
| 7 | Popular needs fast paths | `section.popular-needs` | PopularNeedsGrid | Route visitors to core needs quickly | Airport Arrivals, Stadium Route, Transportation, Dining, Hotels, Team Hubs, Parking/Shuttles, Official Sources | No provider guarantee or official-source implication | Compact route tile grid near top | Chips or stacked cards near top | Missing fast paths, text-only route list, slow utility |
| 8 | Guide gateway | `section.guide-gateway` | GuideGateway | Open the main public guide system | Guide cards for airport, stadium, transportation, dining, hotels, fans, events, support needs | Guides must remain independent platform content | Card grid with clear CTAs | Stacked or two-column readable cards | Guide access buried, microtext, missing CTAs |
| 9 | Sponsor inventory | `section.sponsor-inventory` | SponsorInventoryGrid | Show commercial placement opportunities | Available category slots, page context, advertiser CTAs | Available status until sold and approved; no official sponsor implication | Premium inventory grid with commercial value | Compact readable sponsor cards | Missing inventory, buried value, sold-looking treatment |
| 10 | Official-source lane | `section.official-sources` | OfficialSourceLane | Distinguish official sources from platform guidance | Source cards for airports, venues, city, transit, tournament or team references where applicable | Clear distinction that platform is independent | Structured source cards | Compact source cards or disclosure | Affiliation confusion, plain text-only source dump |
| 11 | Provider and referral handoff | `section.provider-handoff` | ProviderHandoffGrid | Present third-party/provider paths without overclaim | Transportation, dining, hotels, visitor services, traveler support where relevant | No guaranteed availability, no live booking claim unless validated | Interface cards with handoff labels | Compact cards | Fulfillment overclaim, unclear handoff status |
| 12 | Reviewed support boundary | `section.reviewed-support` | PremiumReviewBoundary | Control when reviewed support applies | VIP, Team, Media, Corporate Coordinators, complex groups, complex arrivals/routes | Secondary support only; no Command Hub access for general fans | Distinct support boundary below self-serve routes | Concise secondary support card | General visitor backend drift, support presented as primary path |
| 13 | Trust row | `section.trust-row` | TrustRow | Reinforce confidence and safe use | Information-first, local expertise, language readiness, secure/private, sponsor disclosure | Planned/live status must be claim-safe | Multi-card trust row | Stacked compact trust cards | Unsupported real-time claim, missing trust cues |
| 14 | Footer | `footer.site-footer` | SiteFooter | Close with navigation, business path, policy links | Footer nav, sponsor path, advertiser path, privacy, terms, disclaimer links | No official affiliation implication | Full footer with clear link groups | Compact footer accordions or groups | Missing links, unclear sponsor disclosure |
| 15 | Disclaimer | `section.disclaimer-block` or footer legal block | DisclaimerBlock | State independent platform status | Required short or full disclaimer based on page depth | Must include no official tournament, team, venue, sponsor, airport, or city affiliation implication | Readable legal/trust block | Readable compact legal block | Missing, unreadable, or diluted disclaimer |

## 7. Desktop Layout Rules

Homepage desktop prototype must use:

1. native 1440 CSS px review viewport
2. 1320px centered content container unless superseded by later locked standard
3. purposeful multi-column utility where speed to information improves
4. strong hero and action hub relationship
5. sponsor lane that is visible and premium
6. guide and Popular Needs modules near the top
7. no shrink-to-fit behavior
8. no static visual-board layout
9. no dashboard overcompression
10. no document-like long-copy first viewport

## 8. Mobile Layout Rules

Homepage mobile prototype must use:

1. native 390 CSS px review viewport
2. tap-first action hierarchy
3. compact brand header and menu access
4. immediate Find My Matchday Plan action
5. Build My Matchday Plan CTA near the top
6. Popular Needs chips or cards near the top
7. guide shortcuts before long support or trust content
8. compact sponsor inventory
9. readable official-source and provider handoff cards
10. no horizontal scrolling
11. no phone mockup inside desktop board
12. no long briefing-page run before actions appear

## 9. Final Determination

`HOMEPAGE BROWSER-PROTOTYPE SECTION MAP LOCKED / SEMANTIC HOMEPAGE ORDER DEFINED / HOMEPAGE V1.0.3 HTML-CSS PROTOTYPE MUST FOLLOW THIS MAP / PDF OUTPUT BLOCKED UNTIL BROWSER PROTOTYPE PASSES GOVERNED REVIEW`
