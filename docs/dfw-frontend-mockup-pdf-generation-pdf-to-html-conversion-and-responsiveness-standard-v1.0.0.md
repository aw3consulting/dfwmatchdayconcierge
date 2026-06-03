# DFW Frontend Mockup, PDF Generation, PDF-to-HTML Conversion, and Desktop-to-Mobile Responsiveness Standard v1.0.0

## 1. Controlled Action

`dfw_frontend_mockup_pdf_generation_pdf_to_html_conversion_and_responsiveness_standard`

## 2. Status

`LOCKED / STANDARD CREATED / MOCKUP GENERATION PAUSED / HOMEPAGE STANDARDIZATION REQUIRED / BATCH PAGE MOCKUPS BLOCKED UNTIL THIS STANDARD IS ACCEPTED`

## 3. Purpose

This standard governs all remaining DFW Matchday Information + Planning Hub visual mockups, PDF generation, PDF-to-HTML conversion, and desktop-to-mobile responsiveness.

It exists to prevent:

1. inconsistent mockup formats
2. wide-board versus scroll-view drift
3. unrealistic web impressions
4. text overlap
5. microtext
6. fixed-height content collisions
7. inconsistent page widths
8. inconsistent headers and footers
9. sponsor inventory layout drift
10. PDF-to-HTML conversion ambiguity
11. mobile responsiveness failure
12. unsupported claims or backend-heavy public page drift

## 4. Governing Determination

The official mockup standard is:

`FULL-PAGE SCROLL MOCKUP FORMAT`

The approved homepage concept remains valid, but the homepage must be regenerated under this standard for uniformity with every linked page mockup.

The prior wide desktop homepage reference remains the approved concept authority, but not the final PDF-to-HTML conversion format.

## 5. Desktop Mockup Standard

### 5.1 Desktop viewport

All desktop mockups must use:

`1440 CSS px viewport width`

### 5.2 Desktop content container

All desktop mockups must use:

`max-width: 1320px`

The content container must be centered.

Minimum desktop page gutters:

`32px`

### 5.3 Desktop mockup capture

Desktop mockups must be rendered as full-page vertical scroll captures.

The capture must show the real page stack from header to footer.

No desktop mockup may be a presentation board, collage, grid, thumbnail sheet, overview board, or combined multi-page artifact.

### 5.4 Desktop layout behavior

Desktop layout must use realistic browser behavior:

1. sections stack vertically
2. card grids wrap naturally
3. text expands container height when needed
4. cards do not clip text
5. content does not overlap
6. sponsor rows remain readable
7. CTA buttons remain clickable-size
8. header remains within the 1440px viewport
9. footer remains within the 1440px viewport
10. no content extends beyond the viewport unless intentionally scrollable as page content

## 6. Mobile Mockup Standard

### 6.1 Mobile viewport

All mobile mockups must use:

`390 CSS px viewport width`

This represents a practical iPhone review width while still supporting responsive logic.

### 6.2 Mobile content container

All mobile mockups must use:

`width: 100%`

with internal gutters of:

`16px minimum`

### 6.3 Mobile capture

Mobile mockups must be full-page vertical scroll captures.

No mobile mockup may be a cropped phone insert inside a desktop board.

### 6.4 Mobile layout behavior

Mobile layout must:

1. use a single-column primary content stack
2. collapse desktop grids into one-column or two-column card rows only where readable
3. keep every CTA visible and tappable
4. keep every sponsor inventory card readable
5. keep forms and selectors large enough for touch interaction
6. place language and contrast controls near the main action area or inside mobile header controls
7. avoid horizontal scrolling
8. avoid microtext
9. avoid overlapping card text
10. preserve the same page sections as desktop unless a section is intentionally summarized with a clear expansion path

## 7. Breakpoint Standard

All HTML conversion must use the following breakpoint system:

```css
:root {
  --bp-mobile: 480px;
  --bp-tablet: 768px;
  --bp-laptop: 1024px;
  --bp-desktop: 1200px;
  --bp-wide: 1440px;
}
```

Required behavior:

1. 0 to 480px: mobile single-column layout
2. 481 to 767px: large mobile / small tablet layout
3. 768 to 1023px: tablet layout
4. 1024 to 1199px: laptop layout
5. 1200 to 1439px: desktop layout
6. 1440px and above: governed desktop review layout

## 8. Layout System Standard

### 8.1 Page shell

Every page must use the same shell:

```html
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header">...</header>
  <main id="main">...</main>
  <footer class="site-footer">...</footer>
</body>
```

### 8.2 Section structure

Each major content band must use semantic structure:

```html
<section class="page-section" aria-labelledby="section-heading-id">
  <div class="container">
    <header class="section-header">
      <p class="eyebrow">...</p>
      <h2 id="section-heading-id">...</h2>
      <p class="section-lede">...</p>
    </header>
    ...
  </div>
</section>
```

### 8.3 Grid standard

Use CSS Grid for two-dimensional page areas:

1. hero layouts
2. guide card grids
3. sponsor inventory grids
4. planning module grids
5. page context grids

Use Flexbox for one-dimensional alignment:

1. nav rows
2. CTA rows
3. pill controls
4. card footer actions
5. language/contrast controls

### 8.4 No fixed text boxes

Fixed-height cards are prohibited unless the text is guaranteed to fit.

Content cards must use:

```css
height: auto;
min-height: var(--value);
overflow: visible;
```

Text clipping is prohibited.

## 9. Global CSS Token Standard

All mockups and HTML must share the same design token basis.

```css
:root {
  --color-bg: #06101a;
  --color-bg-deep: #03070d;
  --color-surface: #091827;
  --color-surface-2: #0d2033;
  --color-border: rgba(218, 170, 80, 0.32);
  --color-border-soft: rgba(255, 255, 255, 0.12);
  --color-text: #f7f1e5;
  --color-muted: #c9d0d8;
  --color-subtle: #8f9cab;
  --color-gold: #d6a84f;
  --color-gold-strong: #f1bf63;
  --color-success: #65c56f;
  --color-warning: #f1bf63;
  --color-danger: #e36a5d;

  --font-sans: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-display: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;

  --container: 1320px;
  --gutter-desktop: 32px;
  --gutter-mobile: 16px;

  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 22px;
  --radius-pill: 999px;

  --shadow-card: 0 18px 40px rgba(0, 0, 0, 0.28);

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
}
```

## 10. Typography Standard

### 10.1 Minimum readable type

All PDF mockups and HTML pages must meet these minimums:

1. body text: 16px minimum
2. card body text: 14px minimum
3. label text: 12px minimum
4. navigation text: 13px minimum
5. footer legal text: 11px minimum only if still readable in PDF review
6. CTA text: 13px minimum
7. hero title: 44px to 64px desktop
8. hero title mobile: 32px to 42px

### 10.2 Line height

Use:

1. body: 1.5
2. card text: 1.4
3. compact labels: 1.25 minimum
4. headings: 1.05 to 1.2

### 10.3 Text overlap rule

Any overlapping text is an automatic mockup failure.

Any illegible microtext is an automatic mockup failure.

Any text clipped by a fixed card boundary is an automatic mockup failure.

## 11. Header Standard

Every page must use the same global header architecture.

### 11.1 Desktop header structure

Left:

1. approved DFW logo
2. DFW Matchday
3. Information + Planning Hub descriptor

Center:

1. title sponsor or page sponsor inventory lane
2. clear available sponsor language
3. sponsor CTA where appropriate

Right:

1. Advertise With Us CTA

Navigation row:

1. Find My Matchday Plan
2. Guides
3. Team Hubs
4. Transportation
5. Dining & Watch Parties
6. Hotels & Areas
7. Fan Fest & Events
8. About

The active page may be highlighted, but label language may not drift.

### 11.2 Mobile header structure

Mobile header must include:

1. approved DFW logo
2. DFW Matchday
3. Information + Planning Hub descriptor
4. menu button
5. compact access to language and contrast controls
6. no overloaded navigation row

Mobile navigation may open as a menu.

## 12. Language and Contrast Control Standard

Language and contrast controls must be shown consistently.

Desktop placement:

1. near the primary planning/action module
2. aligned above or beside the main page action panel
3. visible without dominating the header

Mobile placement:

1. inside the mobile header menu or immediately above the main action module
2. visible enough to establish multilingual and accessibility readiness

Controls required:

1. language selector
2. contrast selector or toggle

Mockups must not generate separate black-white page variants unless separately authorized. The control appears as a product function, not as an alternate mockup output in Batch 1.

## 13. CTA Standard

### 13.1 General visitor CTAs

Use planning and guide-first language:

1. Build My Matchday Plan
2. Find My Matchday Plan
3. View Recommended Guides
4. View Guide
5. Compare Options
6. Add to My Plan
7. View Official Sources
8. Explore Options

### 13.2 Premium CTAs

Use premium review language only where appropriate:

1. Request Reviewed Plan
2. Prepare Coordinator Summary
3. Request Reviewed Support

Premium CTAs are secondary unless the page is specifically for VIP / Team / Media / Corporate Coordinators.

### 13.3 Advertiser CTAs

Use advertiser language:

1. Advertise With Us
2. View Sponsor Options
3. Reserve This Placement
4. Sponsor This Guide
5. Request Sponsor Options
6. View Available Inventory

### 13.4 Blocked CTA drift

The following are blocked for general visitor flow:

1. Connect as a primary visitor CTA
2. QR as a dominant on-site action
3. Command Hub access for general fans
4. Book Now where no booking system is live
5. Dispatch Now where no dispatch system is live
6. Pay Now where payment automation is not live and validated

## 14. Sponsor Inventory Standard

Every page mockup must include page-specific ad inventory.

Inventory must show as available until sold and approved.

Each sponsor card must include:

1. placement label
2. availability status
3. page context
4. sponsor CTA
5. claim-safe status

Required available language:

1. Available Sponsor Placement
2. Available Slot
3. Category Available
4. Reserve This Slot
5. Sponsor This Guide
6. Sponsor This Planning Lane
7. View Sponsor Options

Blocked sponsor treatment:

1. real sponsor logo without approval
2. sold-looking treatment without sale approval
3. official sponsor implication
4. exclusive language unless approved
5. fake brand marks
6. AI-invented advertiser logos

## 15. Footer and Trust Standard

Every page must end with a consistent trust and footer system.

Footer/trust sections must include:

1. independent platform statement
2. information-first statement
3. trusted information / official-source distinction
4. local expertise
5. real-time updates as planned or informational, not a live automation claim unless implemented
6. global welcome / language readiness
7. secure and private statement
8. sponsor disclosure path
9. advertiser path
10. privacy / terms / disclaimer links
11. no official affiliation disclaimer

Short required disclaimer:

`Independent information and planning platform. No official tournament, team, venue, sponsor, airport, or city affiliation implied.`

Full required disclaimer:

`DFW Matchday Concierge is an independent Dallas-area visitor information, planning, and concierge platform. It is not affiliated with, endorsed by, sponsored by, or officially connected to FIFA, the FIFA World Cup, DallasFWC26, participating teams, stadium operators, or official tournament sponsors. Sponsor placements are sold for visibility on the DFW Matchday Concierge platform only.`

## 16. Logo Standard

The approved DFW logo is no longer treated as a placeholder in the generated mockups when it matches the approved logo direction.

The production build must still use the exact approved locked logo asset file.

Blocked logo drift:

1. redrawing the logo
2. changing shield proportions
3. changing typography
4. creating new AI logo marks
5. substituting generic badge marks
6. treating a non-approved mark as production authority

## 17. Image and Icon Standard

All icons in mockups must be simple, consistent, and executable in HTML.

Recommended implementation:

1. inline SVG icons
2. accessible labels where icons convey meaning
3. decorative icons marked as decorative in HTML
4. no complex AI-generated icon images
5. no text embedded inside non-logo images

Hero images and background images must not contain critical text.

## 18. HTML Standard

All final HTML must use semantic structure.

Required elements:

1. `header`
2. `nav`
3. `main`
4. `section`
5. `article` where cards represent reusable content blocks
6. `aside` where supplemental sponsor or support content is separate from main flow
7. `footer`
8. heading hierarchy from one `h1` per page followed by logical `h2` and `h3`

Required attributes and behavior:

1. `lang` on `html`
2. accessible labels on controls
3. descriptive link text
4. meaningful button text
5. no empty links
6. no button-as-link confusion unless behavior is implemented properly
7. no div-only page structure for major sections

## 19. CSS Standard

Final CSS must be componentized and tokenized.

Recommended structure:

```text
assets/css/
  base.css
  tokens.css
  layout.css
  components.css
  pages.css
  responsive.css
```

CSS rules:

1. use CSS custom properties for colors, spacing, radius, and typography
2. use Grid for major section layout
3. use Flexbox for alignment rows
4. use responsive media queries
5. avoid absolute positioning for text-bearing content
6. avoid fixed pixel heights for content cards
7. avoid overflow hidden on text containers
8. avoid inline styles except for audited one-off exceptions
9. preserve keyboard focus styles
10. define print/PDF capture support where needed

## 20. JavaScript Standard

JavaScript must be progressive enhancement only.

Core content must be visible without JavaScript.

Allowed JavaScript:

1. mobile menu toggle
2. language selector state
3. contrast toggle
4. plan-builder interaction
5. filter/sort behavior
6. sponsor inquiry form enhancement
7. analytics only after compliance review

Blocked JavaScript claims:

1. live AI fulfillment unless implemented and validated
2. live dispatch unless implemented and validated
3. live provider booking unless implemented and validated
4. live payment automation unless implemented and validated
5. hidden required content that only appears through script

## 21. Accessibility Standard

Minimum target:

`WCAG 2.2 AA`

Required accessibility rules:

1. color contrast at AA level
2. reflow to 320 CSS px without horizontal page scrolling
3. keyboard navigation
4. visible focus states
5. semantic headings
6. descriptive link text
7. accessible controls
8. form labels
9. error states where forms exist
10. no content loss when text spacing is increased
11. no information conveyed by color alone
12. no inaccessible icon-only buttons

## 22. PDF Mockup Generation Standard

Each PDF mockup must be generated from a realistic browser-like frame.

### 22.1 Desktop PDF

Desktop PDF requirements:

1. 1440 CSS px viewport
2. 1320 CSS px max content container
3. full-page vertical scroll capture
4. visible header through footer
5. no board framing
6. no multi-page collage
7. no miniaturized page thumbnails
8. readable body text
9. no overlapping text
10. no clipped card content

### 22.2 Mobile PDF

Mobile PDF requirements:

1. 390 CSS px viewport
2. full-page vertical scroll capture
3. single-column mobile-first stacking
4. visible header through footer
5. no phone mockup inside desktop board
6. no unreadable text
7. no clipped sponsor inventory
8. no horizontal scroll dependency

### 22.3 File naming

Homepage standardized files:

1. `docs/mockups/dfw-information-planning-hub-front-page-desktop-scroll-dark-contrast-final-review-v1.0.1.pdf`
2. `docs/mockups/dfw-information-planning-hub-front-page-mobile-scroll-dark-contrast-final-review-v1.0.1.pdf`

Batch 1 regenerated files:

1. `docs/mockups/matchday-plan-desktop-scroll-dark-contrast-review-v1.0.1.pdf`
2. `docs/mockups/matchday-plan-mobile-scroll-dark-contrast-review-v1.0.1.pdf`
3. `docs/mockups/guides-desktop-scroll-dark-contrast-review-v1.0.1.pdf`
4. `docs/mockups/guides-mobile-scroll-dark-contrast-review-v1.0.1.pdf`
5. `docs/mockups/airport-arrivals-desktop-scroll-dark-contrast-review-v1.0.1.pdf`
6. `docs/mockups/airport-arrivals-mobile-scroll-dark-contrast-review-v1.0.1.pdf`
7. `docs/mockups/stadium-movement-desktop-scroll-dark-contrast-review-v1.0.1.pdf`
8. `docs/mockups/stadium-movement-mobile-scroll-dark-contrast-review-v1.0.1.pdf`
9. `docs/mockups/transportation-desktop-scroll-dark-contrast-review-v1.0.1.pdf`
10. `docs/mockups/transportation-mobile-scroll-dark-contrast-review-v1.0.1.pdf`
11. `docs/mockups/dining-watch-parties-desktop-scroll-dark-contrast-review-v1.0.1.pdf`
12. `docs/mockups/dining-watch-parties-mobile-scroll-dark-contrast-review-v1.0.1.pdf`
13. `docs/mockups/hotels-area-guide-desktop-scroll-dark-contrast-review-v1.0.1.pdf`
14. `docs/mockups/hotels-area-guide-mobile-scroll-dark-contrast-review-v1.0.1.pdf`
15. `docs/mockups/fans-desktop-scroll-dark-contrast-review-v1.0.1.pdf`
16. `docs/mockups/fans-mobile-scroll-dark-contrast-review-v1.0.1.pdf`

## 23. PDF-to-HTML Conversion Standard

The HTML build must not trace pixels blindly from the PDF.

The conversion must translate the approved PDF into semantic, responsive components.

Required conversion order:

1. extract page sections
2. map each section to semantic HTML
3. define shared components
4. define design tokens
5. implement desktop layout at 1440px
6. implement mobile layout at 390px
7. validate reflow at 320px
8. validate text readability
9. validate sponsor inventory
10. validate claim language
11. validate keyboard and focus behavior
12. validate mobile menu
13. validate footer/disclaimer
14. validate no overlap or clipping
15. validate no unsupported live-fulfillment claim

## 24. Conversion Component Library

Every page must be built from reusable components:

1. SiteHeader
2. SponsorHeaderLane
3. PrimaryNavigation
4. LanguageControl
5. ContrastControl
6. PageHero
7. PlanningPanel
8. GuideCard
9. StatusCard
10. SponsorInventoryCard
11. OfficialSourceCard
12. ProviderHandoffCard
13. PremiumReviewBoundary
14. TrustRow
15. DisclaimerBlock
16. SiteFooter

## 25. Mockup Audit Checklist

Every mockup must pass the following before approval:

1. correct file name
2. correct page route
3. full-page scroll format
4. approved logo direction used
5. approved header system preserved
6. title sponsor lane present
7. Advertise With Us present as business CTA
8. language control present
9. contrast control present
10. page-specific hero present
11. page-specific content present
12. page-specific sponsor inventory present
13. no sold sponsor treatment unless approved
14. official-source lane present where relevant
15. referral/provider lane present where relevant
16. premium review boundary controlled
17. no backend Command Hub drift
18. no Connect visitor CTA drift
19. no QR dominant on-site CTA
20. no unsupported official affiliation
21. no overlapping text
22. no clipped text
23. no microtext
24. realistic web component spacing
25. footer/trust structure present
26. disclaimer present
27. mobile counterpart required
28. conversion-ready component structure visible

## 26. Automatic Failure Triggers

A mockup fails automatically if it includes:

1. board or collage output
2. multiple pages in one artifact
3. non-scroll desktop format
4. non-scroll mobile format
5. overlapping text
6. clipped text
7. unreadable microtext
8. fixed boxes that cannot translate to HTML
9. inconsistent navigation labels
10. missing sponsor inventory
11. sold sponsor presentation without approval
12. official affiliation implication
13. backend fulfillment claims
14. live AI, dispatch, API, booking, or payment claim without validation
15. QR as dominant on-site visitor action
16. Connect as a general visitor CTA
17. unapproved logo drift
18. missing disclaimer
19. missing mobile counterpart
20. missing page route label

## 27. Required Regeneration Sequence

The correct sequence is now:

1. accept and lock this standard
2. commit this standard to `main`
3. regenerate the homepage desktop scroll mockup under this standard
4. regenerate the homepage mobile scroll mockup under this standard
5. audit and approve the regenerated homepage standardization pair
6. regenerate Matchday Plan desktop scroll mockup under this standard
7. regenerate Matchday Plan mobile scroll mockup under this standard
8. audit and approve File 1 pair
9. proceed file-by-file through Batch 1
10. commit only approved mockups after user authorization
11. proceed to Batch 2 only after Batch 1 approval record is locked
12. begin PDF-to-HTML conversion only after all governed mockup approvals are complete

## 28. Recommendations

### 28.1 Create a design-token source file before HTML conversion

Create:

`assets/css/tokens.css`

Purpose:

Centralize colors, spacing, typography, borders, radius, and breakpoints before any HTML build.

### 28.2 Create a component checklist file

Create:

`docs/dfw-frontend-component-library-checklist-v1.0.0.md`

Purpose:

Ensure every PDF section maps to an HTML component before coding.

### 28.3 Create a responsive QA checklist

Create:

`docs/dfw-responsive-accessibility-and-reflow-qa-checklist-v1.0.0.md`

Purpose:

Validate 1440px, 1200px, 1024px, 768px, 480px, 390px, and 320px behavior.

### 28.4 Create a sponsor inventory data file

Create:

`data/sponsor-inventory.json`

Purpose:

Avoid hardcoding sponsor inventory into pages and prevent sold/available status drift.

### 28.5 Create a claim-control data file

Create:

`data/claim-controls.json`

Purpose:

Ensure public claims, sponsor claims, provider claims, reviewed support claims, and restricted capability claims remain governed.

### 28.6 Use real HTML/CSS prototypes for final mockups when possible

The most precise future method is to generate final mockup PDFs from actual HTML/CSS prototype pages rather than image-only mockups.

This creates a direct path from mockup to production and reduces conversion drift.

## 29. Final Determination

`STANDARD CREATED / FULL-PAGE SCROLL VIEW SELECTED / HOMEPAGE MUST BE REGENERATED FOR UNIFORMITY / PAGE MOCKUPS MUST BE GENERATED UNDER THIS STANDARD / PDF-TO-HTML CONVERSION MUST FOLLOW SEMANTIC HTML, CSS GRID, FLEXBOX, RESPONSIVE BREAKPOINTS, WCAG 2.2 AA, AND CLAIM-CONTROL REQUIREMENTS / MOCKUP GENERATION REMAINS PAUSED UNTIL THIS STANDARD IS ACCEPTED`
