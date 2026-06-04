# DFW Homepage Minimal Gateway Section Map v1.0.0

## Controlled Action

`dfw_homepage_minimal_gateway_section_map`

## Status

`LOCKED / MINIMAL HOMEPAGE SECTION MAP CREATED / HOMEPAGE PROTOTYPE REVISION BLOCKED UNTIL THIS MAP IS APPLIED`

## Purpose

This section map defines the only approved section structure for the next DFW Matchday Information + Planning Hub homepage prototype.

The homepage must be short, premium, scannable, and directional. It must not become a planning directory or replacement for linked pages.

## Approved Semantic Order

1. skip link
2. site header
3. primary navigation
4. hero and welcome
5. what we help with
6. choose your path
7. premium ad space and sponsorship
8. partner recognition
9. trust and responsibility
10. footer and disclaimer

## Section 1: Skip Link

Semantic element:

`a.skip-link`

Purpose:

Provide accessible skip navigation to the main content.

Failure triggers:

1. missing skip link
2. skip link points to non-existing main content

## Section 2: Site Header

Semantic element:

`header.site-header`

Component name:

`SiteHeader`

Purpose:

Identify the platform and provide concise route access.

Content requirements:

1. approved logo direction
2. DFW Matchday Concierge or DFW Matchday Information + Planning Hub identity
3. compact navigation
4. Advertise With Us CTA

Desktop layout rule:

Brand left, navigation or concise route access center, advertiser CTA right.

Mobile layout rule:

Brand left, compact menu or stacked route access, advertiser path accessible but not dominant over visitor path.

Failure triggers:

1. overloaded navigation
2. brand naming drift
3. missing advertiser path
4. header crowding

## Section 3: Hero and Welcome

Semantic element:

`section.hero`

Component name:

`HeroWelcome`

Purpose:

Introduce DFW Matchday Concierge and welcome teams, supporters, fans, visitors, coordinators, and local partners.

Content requirements:

1. clear brand introduction
2. welcome statement
3. independent platform qualifier
4. three primary CTAs maximum

Allowed CTAs:

1. Start Planning
2. View Guides
3. Advertise With Us

Desktop layout rule:

Premium hero with strong visual hierarchy and one supporting action panel at most.

Mobile layout rule:

Single-column hero with CTAs immediately visible.

Failure triggers:

1. long hero paragraph
2. detailed planning form replacing hero
3. more than three primary CTAs
4. official affiliation implication

## Section 4: What We Help With

Semantic element:

`section.services-summary`

Component name:

`ServiceSummaryCards`

Purpose:

Summarize core service and information categories without giving full page detail.

Allowed cards:

1. Visitor Information
2. Matchday Planning
3. Airport and Transportation Guidance
4. Hotels, Dining, and Area Paths
5. Team Fan and Supporter Routes
6. Reviewed Support for VIP, Team, Media, and Corporate Coordinators

Desktop layout rule:

Compact card grid with short copy.

Mobile layout rule:

Single-column or two-column cards only if readable.

Failure triggers:

1. full category explanations
2. repeated guide descriptions
3. detailed provider handoff copy
4. cards that replace linked pages

## Section 5: Choose Your Path

Semantic element:

`section.pathways`

Component name:

`AudiencePathways`

Purpose:

Route visitors to the right page based on audience type.

Allowed pathways:

1. Fans and Supporters
2. Families and Groups
3. International Visitors
4. VIP / Team / Media / Corporate Coordinators
5. Advertisers and Local Partners

Desktop layout rule:

Five route cards or a compact split layout.

Mobile layout rule:

Stacked route cards with clear CTA per path.

Failure triggers:

1. too many path options
2. repeated service descriptions from the previous section
3. unsupported promise of direct fulfillment

## Section 6: Premium Ad Space and Sponsorship

Semantic element:

`section.sponsor-opportunity`

Component name:

`SponsorOpportunity`

Purpose:

Present homepage and page-level advertising opportunities.

Content requirements:

1. title sponsor available
2. page sponsorship available
3. category sponsorship available
4. CTA to Advertise With Us or sponsor opportunities

Desktop layout rule:

Premium commercial band, not a generic grid.

Mobile layout rule:

Concise commercial card with one CTA.

Failure triggers:

1. fake sponsor logos
2. sold-looking placements without approval
3. full inventory spreadsheet behavior
4. low-value dashboard treatment

## Section 7: Partner Recognition

Semantic element:

`section.partner-recognition`

Component name:

`PartnerRecognition`

Purpose:

Thank and recognize approved partners while preserving available placement status before sales are approved.

Content requirements:

1. thank-you language
2. approved partner recognition when available
3. available partner space language when unsold
4. no invented brands

Desktop layout rule:

Premium recognition strip or reserved logo row.

Mobile layout rule:

Readable partner recognition stack.

Failure triggers:

1. fake logos
2. implying sold partners without approval
3. hiding sponsor opportunity

## Section 8: Trust and Responsibility

Semantic element:

`section.trust-responsibility`

Component name:

`TrustResponsibility`

Purpose:

Establish independence, responsibility, source distinction, privacy, and sponsor disclosure.

Content requirements:

1. independent platform statement
2. no official affiliation statement
3. official-source distinction
4. sponsor disclosure
5. privacy or controlled inquiry statement

Desktop layout rule:

Compact trust row or two-column trust block.

Mobile layout rule:

Stacked short trust statements.

Failure triggers:

1. repeating full legal disclaimer multiple times
2. overlong trust copy
3. unsupported official relationship language

## Section 9: Footer and Disclaimer

Semantic element:

`footer.site-footer` plus `section.disclaimer`

Component name:

`SiteFooter` and `DisclaimerBlock`

Purpose:

Provide final navigation, business path, trust links, and legal qualifier.

Content requirements:

1. platform identity
2. planning links
3. sponsor or advertiser links
4. trust links
5. compact disclaimer

Failure triggers:

1. footer repeats the whole homepage
2. legal qualifier missing
3. business path missing

## Final Determination

`MINIMAL GATEWAY SECTION MAP LOCKED / HOMEPAGE STRUCTURE LIMITED TO INTRODUCTION, ROUTING, SPONSORSHIP, PARTNER RECOGNITION, TRUST, FOOTER, AND DISCLAIMER`
