# DFW v1.0.10 Image Visibility Correction and Hardening Execution v1.0.0

Repository: `aw3consulting/dfwmatchdayconcierge`
Branch: `main`
Approved prototype: `docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html`

## Execution standing

The attached audit package was read before correction. The valid v1.0.10 package structure is:

```text
index-v1.0.10.html
assets/css/
assets/images/
assets/icons/
```

## Cause determination

The audit does not prove a browser-level PNG rendering failure and does not justify a full site recode. The corrected cause category is deployment/path/preview-surface fragility:

1. `index-v1.0.10.html` uses local static raster paths.
2. Those paths only work when the `assets/` directory is deployed beside the HTML file.
3. Wrapper preview surfaces or mismatched deployment folders can serve the HTML without serving the matching PNG asset tree.
4. When a direct PNG URL does not return `HTTP 200` with `Content-Type: image/png`, the image cannot render no matter what the layout code says.

## Correction made

Only the approved v1.0.10 prototype path was hardened. No root homepage redesign or full site recode was performed.

Updated files:

```text
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html
docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/css/replica-v1.0.10.css
```

Hardening changes:

- Converted local raster references from `assets/...` to explicit co-located `./assets/...` paths.
- Added a top-of-page raster canary image using the approved header PNG path.
- Added `data-raster-critical="true"` to PNG image elements.
- Added visible image-load failure handling so broken PNG requests generate visible `PNG FAILED` labels instead of silent blank image slots.
- Added CSS diagnostics for `.image-load-failed`, `.raster-load-failed`, `.image-failure-label`, and `.asset-canary`.
- Preserved approved prototype structure and content.
- Did not use SVG as a correction.

## Verified direct static URLs to use

Direct static preview URL:

```text
https://aw3consulting.github.io/dfwmatchdayconcierge/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10.html
```

Direct PNG asset URL proof target:

```text
https://aw3consulting.github.io/dfwmatchdayconcierge/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/logos/dfw-logo-header-raster-v1.0.2.png
```

A passing PNG proof requires:

```text
HTTP 200
Content-Type: image/png
Nonzero content length
Decoded image with naturalWidth > 0 and naturalHeight > 0
```

## Final rule

Do not judge the homepage visual state until at least one direct PNG asset URL from the same deployed directory returns `HTTP 200` and `Content-Type: image/png`.
