#!/usr/bin/env python3
"""Patch DFW v1.0.10 production-readiness preview with approved header logo boundary.

This script is intentionally repo-native: it reads the approved logo base64 source from
repository files and patches the generated preview HTML inside the checked-out repo.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import re
from pathlib import Path

TARGET = Path("docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10-production-readiness-preview-full-original-assets-v1.0.0.html")
APPROVED_B64 = Path("docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/approved/approved-header-logo-transparent-display-embedded-v1.0.0.base64.txt")
RECORD = Path("docs/dfw-homepage-v1.0.10-repo-native-actions-approved-header-logo-data-uri-patch-and-preview-proof-record-v1.0.0.md")

NEW_BANNER = "PRODUCTION-READINESS PREVIEW CANDIDATE — APPROVED HEADER LOGO EMBEDDED — REMAINING VISUAL ASSETS PENDING APPROVAL — NOT PRODUCTION APPROVED"
TITLE_TEXT = "DFW Matchday Concierge - v1.0.10 Production Readiness Preview Approved Header Logo Embedded and Pending Visual Assets"
META_CONTENT = "approved-header-logo-embedded; remaining-visual-assets-pending-approval; generated-from-v1.0.10; not-production-approved"

PENDING_SLOTS = [
    "Footer logo",
    "Hero image",
    "AI inquiry image",
    "VIP Guest Concierge hub icon",
    "Team Family Support hub icon",
    "Media / Corporate hub icon",
    "Fan Hubs hub icon",
    "Driver Onboarding hub icon",
    "Concierge Onboarding hub icon",
    "Fulfillment Hub icon",
    "DFW map/routes image",
    "Driver image",
    "Concierge image",
    "Fulfillment Providers image",
    "Instagram icon",
    "Facebook icon",
    "X icon",
    "LinkedIn icon",
    "Any additional image/icon not explicitly approved",
]

OLD_HEADER_PATHS = [
    "assets/images/logos/dfw-logo-header-raster-v1.0.2.png",
    "assets/images/logos/dfw-logo-header-raster-v1.0.3.png",
    "docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/logos/dfw-logo-header-raster-v1.0.2.png",
    "docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/logos/dfw-logo-header-raster-v1.0.3.png",
    "raw.githubusercontent.com/aw3consulting/dfwmatchdayconcierge/main/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/logos/dfw-logo-header-raster-v1.0.2.png",
    "raw.githubusercontent.com/aw3consulting/dfwmatchdayconcierge/main/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/assets/images/logos/dfw-logo-header-raster-v1.0.3.png",
]

BOUNDARY_CSS = f"""
<style data-approved-header-logo-boundary="v1.0.0">
body[data-asset-approval-boundary="approved-header-logo-only"] .asset-canary,
body[data-asset-approval-boundary="approved-header-logo-only"] .hero-visual,
body[data-asset-approval-boundary="approved-header-logo-only"] .image-slot img:not(.approved-header-logo-img),
body[data-asset-approval-boundary="approved-header-logo-only"] .map-visual img,
body[data-asset-approval-boundary="approved-header-logo-only"] .card-image-slot img,
body[data-asset-approval-boundary="approved-header-logo-only"] .icon-placeholder img,
body[data-asset-approval-boundary="approved-header-logo-only"] .footer-logo-placeholder img,
body[data-asset-approval-boundary="approved-header-logo-only"] .social-icons img {{display:none!important;visibility:hidden!important;opacity:0!important}}
body[data-asset-approval-boundary="approved-header-logo-only"] .approved-header-logo,
body[data-asset-approval-boundary="approved-header-logo-only"] .approved-header-logo img {{display:block!important;visibility:visible!important;opacity:1!important;background:transparent!important;border:0!important}}
body[data-asset-approval-boundary="approved-header-logo-only"] .approved-header-logo {{width:62px!important;height:54px!important;display:grid!important;place-items:center!important;overflow:visible!important}}
body[data-asset-approval-boundary="approved-header-logo-only"] .approved-header-logo-img {{width:62px!important;height:54px!important;max-width:62px!important;max-height:54px!important;object-fit:contain!important;filter:none!important;mix-blend-mode:normal!important}}
body[data-asset-approval-boundary="approved-header-logo-only"] .image-slot,
body[data-asset-approval-boundary="approved-header-logo-only"] .map-visual,
body[data-asset-approval-boundary="approved-header-logo-only"] .card-image-slot,
body[data-asset-approval-boundary="approved-header-logo-only"] .icon-placeholder,
body[data-asset-approval-boundary="approved-header-logo-only"] .footer-logo-placeholder,
body[data-asset-approval-boundary="approved-header-logo-only"] .social-icons i {{position:relative!important;overflow:hidden!important;background:linear-gradient(135deg,rgba(216,166,75,.12),rgba(8,31,52,.88))!important;border:1px dashed rgba(240,200,107,.65)!important;color:#f0c86b!important}}
body[data-asset-approval-boundary="approved-header-logo-only"] .image-slot::after,
body[data-asset-approval-boundary="approved-header-logo-only"] .map-visual::after,
body[data-asset-approval-boundary="approved-header-logo-only"] .card-image-slot::after,
body[data-asset-approval-boundary="approved-header-logo-only"] .footer-logo-placeholder::after {{content:"PENDING APPROVED ASSET"!important;position:absolute!important;inset:0!important;display:grid!important;place-items:center!important;text-align:center!important;padding:6px!important;font:900 9px/1.15 Arial,sans-serif!important;letter-spacing:.06em!important;text-transform:uppercase!important;color:#f0c86b!important;background:rgba(3,24,39,.76)!important;z-index:5!important}}
body[data-asset-approval-boundary="approved-header-logo-only"] .icon-placeholder::after,
body[data-asset-approval-boundary="approved-header-logo-only"] .social-icons i::after {{content:"PENDING"!important;position:absolute!important;inset:0!important;display:grid!important;place-items:center!important;text-align:center!important;font:900 5px/1 Arial,sans-serif!important;letter-spacing:.02em!important;text-transform:uppercase!important;color:#f0c86b!important;background:rgba(3,24,39,.78)!important;z-index:5!important}}
body[data-asset-approval-boundary="approved-header-logo-only"] .hero-section::before {{content:"HERO VISUAL ASSET PENDING APPROVAL"!important;position:absolute!important;top:10px!important;right:10px!important;z-index:2!important;padding:6px 8px!important;border:1px dashed rgba(240,200,107,.65)!important;background:rgba(3,24,39,.82)!important;color:#f0c86b!important;font:900 8px/1 Arial,sans-serif!important;letter-spacing:.05em!important;text-transform:uppercase!important}}
</style>
<script type="application/json" id="dfw-asset-approval-boundary">{json.dumps({"approved": ["Header logo"], "pending_approved_asset": PENDING_SLOTS}, separators=(",", ":"))}</script>
""".strip()


def replace_or_insert_block(html: str, marker_attr: str, block: str) -> str:
    pattern = re.compile(rf"\n?<style\s+{re.escape(marker_attr)}=\"v1\.0\.0\">.*?</style>\s*(?:<script\s+type=\"application/json\"\s+id=\"dfw-asset-approval-boundary\">.*?</script>)?", re.S)
    if pattern.search(html):
        return pattern.sub("\n" + block + "\n", html, count=1)
    return html.replace("</head>", block + "\n</head>", 1)


def replace_header_logo(html: str, data_uri: str) -> tuple[str, int]:
    logo_markup = (
        '<div class="logo-placeholder approved-header-logo" data-asset-approval="approved" '
        'data-approved-asset="header-logo" aria-label="DFW Matchday Concierge approved header logo">'
        f'<img class="approved-header-logo-img" src="{data_uri}" '
        'alt="DFW Matchday Concierge approved header logo" width="62" height="54" decoding="async"/>'
        '</div>'
    )

    header_marker_match = re.search(r'class=["\'][^"\']*site-header[^"\']*["\']', html, re.I)
    if not header_marker_match:
        return html, 0
    header_start = html.rfind("<", 0, header_marker_match.start())
    next_section_candidates = [
        html.find("</header>", header_marker_match.end()),
        html.find("<section", header_marker_match.end()),
        html.find("<main", header_marker_match.end()),
        html.find("<div class=\"sponsor-hero\"", header_marker_match.end()),
        html.find("<div class='sponsor-hero'", header_marker_match.end()),
    ]
    next_section_candidates = [x for x in next_section_candidates if x != -1]
    header_end = min(next_section_candidates) if next_section_candidates else min(len(html), header_marker_match.end() + 5000)
    segment = html[header_start:header_end]

    new_segment, count = re.subn(
        r'<div\b(?=[^>]*class=["\'][^"\']*logo-placeholder[^"\']*["\'])[^>]*>.*?</div>',
        logo_markup,
        segment,
        count=1,
        flags=re.S | re.I,
    )
    if count == 0:
        new_segment, count = re.subn(
            r'<img\b(?=[^>]*(?:logo|canary))[^>]*>',
            f'<img class="approved-header-logo-img" src="{data_uri}" alt="DFW Matchday Concierge approved header logo" width="62" height="54" decoding="async"/>',
            segment,
            count=1,
            flags=re.S | re.I,
        )
    if count == 0:
        return html, 0
    return html[:header_start] + new_segment + html[header_end:], count


def main() -> None:
    if not TARGET.exists():
        raise SystemExit(f"FAIL: target preview HTML missing: {TARGET}")
    if not APPROVED_B64.exists():
        raise SystemExit(f"FAIL: approved logo base64 source missing: {APPROVED_B64}")

    html = TARGET.read_text(encoding="utf-8")
    original_sha = hashlib.sha256(html.encode("utf-8")).hexdigest()
    b64 = "".join(APPROVED_B64.read_text(encoding="utf-8").split())
    if len(b64) < 100:
        raise SystemExit("FAIL: approved logo base64 source is unexpectedly short")
    data_uri = f"data:image/png;base64,{b64}"

    html = re.sub(r'<title>.*?</title>', f'<title>{TITLE_TEXT}</title>', html, count=1, flags=re.S | re.I)
    html = html.replace("PRODUCTION-READINESS PREVIEW CANDIDATE — FULL ORIGINAL ASSETS EMBEDDED — NOT PRODUCTION APPROVED", NEW_BANNER)
    html = html.replace("Production-readiness preview candidate — full original assets embedded — not production approved", NEW_BANNER)
    html = html.replace("Preview-safe version of the DFW Matchday Concierge desktop prototype with section corrections.", "Preview candidate with approved header logo embedded and remaining visual assets pending approval.")
    html = html.replace("full-original-assets; generated-from-v1.0.10; not production-approved", META_CONTENT)

    html = replace_or_insert_block(html, "data-approved-header-logo-boundary", BOUNDARY_CSS)

    if "data-asset-approval-boundary=" not in html:
        html = re.sub(r'<body\b([^>]*)>', r'<body\1 data-asset-approval-boundary="approved-header-logo-only">', html, count=1, flags=re.I)
    else:
        html = re.sub(r'data-asset-approval-boundary=["\'][^"\']*["\']', 'data-asset-approval-boundary="approved-header-logo-only"', html, count=1, flags=re.I)

    html, header_replacements = replace_header_logo(html, data_uri)
    if header_replacements != 1:
        raise SystemExit(f"FAIL: expected exactly one header logo replacement, got {header_replacements}")

    for old in OLD_HEADER_PATHS:
        html = html.replace(old, "")

    if data_uri not in html:
        raise SystemExit("FAIL: approved header logo data URI missing after patch")
    if any(old in html for old in OLD_HEADER_PATHS):
        raise SystemExit("FAIL: old header logo path reference remains after patch")
    if "FULL ORIGINAL ASSETS EMBEDDED" in html:
        raise SystemExit("FAIL: misleading full-original-assets wording remains after patch")
    if "Pending Approved Asset" not in html and "PENDING APPROVED ASSET" not in html:
        raise SystemExit("FAIL: Pending Approved Asset classification not present after patch")

    TARGET.write_text(html, encoding="utf-8")
    patched_sha = hashlib.sha256(html.encode("utf-8")).hexdigest()

    record = f"""# DFW v1.0.10 Repo-Native Actions Approved Header Logo Data URI Patch and Preview Proof Record v1.0.0

Mission: `dfw_homepage_v1_0_10_repo_native_actions_approved_header_logo_data_uri_patch_and_preview_proof_v1_0_0`

Date: {_dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')}

Status: REQUIRED-CORRECTION until Pages deployment, HTTP 200, desktop/mobile/rendered/CSS/JS validation, and user approval gates pass.

## Execution method

Repo-native GitHub Actions/local filesystem script patch. Direct full-HTML connector replacement was not used.

## Files patched

- `{TARGET}`

## Approved header logo data URI embedding

PASS at source level. The approved header logo base64 source was read from:

`{APPROVED_B64}`

The header logo was embedded into the target preview HTML as `data:image/png;base64,...`.

## Header logo path-reference clearance

PASS at source level. Known header logo path references were removed from the target preview HTML.

## Asset boundary

Approved visual asset:

- Header logo only

Pending Approved Asset visual slots:

{chr(10).join(f'- {slot}' for slot in PENDING_SLOTS)}

## Wording correction

PASS at source level. Misleading `FULL ORIGINAL ASSETS EMBEDDED` wording was replaced with:

`{NEW_BANNER}`

## Source hash evidence

- Original target HTML sha256 before patch: `{original_sha}`
- Patched target HTML sha256 after patch: `{patched_sha}`

## Remaining proof gates

- Pages deployment after this patch must be proven.
- HTTP 200 / non-404 must be proven.
- Desktop rendering must be proven.
- Mobile rendering must be proven.
- Approved header logo visibility must be proven.
- Pending Approved Asset panel visibility must be proven.
- CSS runtime must be proven.
- JS runtime must be proven.
- User approval remains NOT GRANTED unless explicitly provided.

## Production readiness standing

BLOCKED / REQUIRED-CORRECTION.
"""
    RECORD.write_text(record, encoding="utf-8")

    print("Patched target:", TARGET)
    print("Record:", RECORD)
    print("Original sha256:", original_sha)
    print("Patched sha256:", patched_sha)
    print("Approved data URI present:", data_uri in html)
    print("Old header path references remaining:", sum(html.count(old) for old in OLD_HEADER_PATHS))
    print("Misleading full-original-assets wording remaining:", html.count("FULL ORIGINAL ASSETS EMBEDDED"))


if __name__ == "__main__":
    main()
