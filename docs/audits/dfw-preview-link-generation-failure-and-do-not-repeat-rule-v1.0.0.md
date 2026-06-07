# DFW Preview Link Generation Failure and Do-Not-Repeat Rule v1.0.0

## Status

FAILURE RECORDED / INVALID PREVIEW LINK GENERATED TWICE / DO-NOT-REPEAT RULE LOCKED / PUBLIC ROUTE REPLACEMENT REMAINS BLOCKED

## Controlled Failure Record

This record documents a repeated preview-link generation failure during the DFW Matchday Concierge homepage prototype execution.

The failure occurred after the user reported that the generated HTML preview surface did not properly generate the website.

## Failed Preview Events

### Failure 1

`index-v1.0.8.html`

Failure type:

- The generated preview path did not render the website properly.
- The likely cause was a fragile CSS dependency pattern using a CSS import chain rather than direct preview-safe stylesheet loading.

### Failure 2

`index-v1.0.11.html`

Failure type:

- The generated preview link was invalid for user review.
- The file was created as an indirect preview loader rather than a direct static prototype page.
- This violated the requirement for reviewable browser output.

## Root Cause

The execution attempted to preserve changes while working around connector write limitations by creating indirect preview surfaces.

That approach failed because the user requires direct, reliable, browser-reviewable prototype files.

A preview link is only valid if it points to a direct static HTML file that loads its CSS directly and renders the full page without loader indirection, fragile import chains, or hidden runtime dependency assumptions.

## Do-Not-Repeat Rule

The following rule is now locked:

Do not generate or provide any future `html-preview.github.io` link unless the linked file is a direct static HTML prototype file that:

1. Contains the full page markup required for review.
2. Does not depend on JavaScript to fetch another HTML file.
3. Does not use a preview-loader wrapper.
4. Does not rely on CSS `@import` as the primary path to load the base prototype stylesheet.
5. Loads all required CSS through direct `<link rel="stylesheet">` tags in the HTML head.
6. Has a committed file path that can be opened directly from GitHub.
7. Has not been described as browser-reviewable unless the output surface is structurally reviewable.

## Additional Preview Rule

If a direct static HTML file cannot be created because of connector limitations, the correct action is to stop and report the blocker.

The incorrect action is to create an indirect loader page and call it a valid browser preview.

## Required Future Preview Standard

Future preview files must use this standard:

1. Create a complete direct HTML file.
2. Create a direct CSS file or direct stylesheet links.
3. Avoid loader indirection.
4. Avoid CSS import chains for active review files.
5. Provide the preview link only after the direct static file has been committed.
6. State clearly if live browser view has not been visually verified.

## Production Boundary

This failure record does not authorize:

1. Public homepage replacement.
2. `/connect` replacement.
3. DreamHost deployment.
4. QR activation.
5. Production approval.
6. Mobile approval.

## Final Standing

INVALID PREVIEW LINK FAILURE RECORDED / SECOND INVALID PREVIEW LINK ACKNOWLEDGED / INDIRECT PREVIEW LOADER METHOD REJECTED / CSS IMPORT PREVIEW METHOD REJECTED / FUTURE PREVIEW LINKS MUST POINT ONLY TO DIRECT STATIC REVIEWABLE HTML FILES / PUBLIC ROUTE REPLACEMENT REMAINS BLOCKED.
