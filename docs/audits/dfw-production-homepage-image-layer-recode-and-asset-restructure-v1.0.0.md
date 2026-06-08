# DFW Production Homepage Image Layer Recode and Asset Restructure v1.0.0

Repository: aw3consulting/dfwmatchdayconcierge
Branch: main

## Standing

The production root homepage has been recoded away from prototype directory dependency and now uses a governed production image root.

## Production image root

```text
assets/img/
├── brand/
├── hero/
└── qr/
```

## Production pages updated

- `/index.html`
- `/connect/index.html`

## Production CSS/JS root

- `assets/css/site.css`
- `assets/js/site.js`

## Production rule

The live homepage must not depend on `docs/prototypes/...` for image loading.

## Final deployment gate

DreamHost production deployment remains blocked until validation, mobile review, QR review, claim review, and user approval pass.
