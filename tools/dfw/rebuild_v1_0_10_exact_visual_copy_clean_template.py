from pathlib import Path
from datetime import datetime, timezone
import base64
import hashlib
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'docs/prototypes/pdf-reference-homepage-replica-v1.0.0'
BASELINE = BASE / 'index-v1.0.10.html'
TARGET = BASE / 'index-v1.0.10-production-readiness-preview-full-original-assets-v1.0.0.html'
PRESERVE = BASE / 'index-v1.0.10-failed-clean-template-rebuild-preserved-v1.0.0.html'
LOGO = BASE / 'assets/approved/approved-header-logo-transparent-display-embedded-v1.0.0.base64.txt'
RECORD = ROOT / 'docs/dfw-homepage-v1.0.10-exact-visual-copy-clean-template-rebuild-execution-record-v1.0.0.md'
URL = 'https://aw3consulting.github.io/dfwmatchdayconcierge/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.10-production-readiness-preview-full-original-assets-v1.0.0.html'

if TARGET.exists() and not PRESERVE.exists():
    shutil.copy2(TARGET, PRESERVE)

logo_b64 = ''.join(LOGO.read_text(encoding='utf-8').split())
logo_bytes = base64.b64decode(logo_b64, validate=True)
if not logo_bytes.startswith(b'\x89PNG\r\n\x1a\n'):
    raise SystemExit('approved header logo is not a valid PNG')
logo_sha = hashlib.sha256(logo_bytes).hexdigest()

html = BASELINE.read_text(encoding='utf-8')
if 'DFW Matchday Concierge - Preview Fixed Prototype v1.0.10' not in html:
    raise SystemExit('locked baseline title not found')

html = re.sub(r'\s*<img alt="Raster asset canary"[^>]*data-raster-canary="true"[^>]*/>\s*', '\n', html, count=1)
header_pattern = re.compile(r'<a class="logo-cell" href="#top"><span class="logo-placeholder"><img[^>]*src="\./assets/images/logos/dfw-logo-header-raster-v1\.0\.2\.png"[^>]*/></span></a>')
logo_img = '<a class="logo-cell" href="#top" aria-label="DFW Matchday Concierge"><img class="site-logo approved-header-logo-img" src="data:image/png;base64,' + logo_b64 + '" alt="DFW Matchday Concierge" width="76" height="54" decoding="async"/></a>'
html, count = header_pattern.subn(logo_img, html, count=1)
if count != 1:
    raise SystemExit(f'header logo replacement count was {count}, expected 1')

html = html.replace('href="./assets/css/', 'href="assets/css/')
html = html.replace('src="./assets/', 'src="assets/')
style = '''<style data-header-logo-render-lock="v1.0.0">
.logo-cell > .site-logo.approved-header-logo-img { display:block; width:76px; height:54px; object-fit:contain; visibility:visible; opacity:1; border:0; background:transparent; }
</style>'''
html = html.replace('</head>', style + '</head>', 1)

header = html.split('<header', 1)[1].split('</header>', 1)[0]
checks = {
    'clean rebuild title absent': 'v1.0.10 Clean Template Rebuild' not in html,
    'data uri present once': html.count('data:image/png;base64,') == 1,
    'approved logo class present': 'approved-header-logo-img' in header,
    'header logo placeholder absent': 'logo-placeholder' not in header,
    'old header logo path absent': 'dfw-logo-header-raster-v1.0.2.png' not in header,
    'locked css v1.0.7 present': 'assets/css/replica-v1.0.7.css' in html,
    'locked css v1.0.10 present': 'assets/css/replica-v1.0.10.css' in html,
}
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit('source gate failed: ' + ', '.join(failed))

TARGET.write_text(html, encoding='utf-8')
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%SZ')
RECORD.write_text(f'''# DFW Homepage v1.0.10 Clone Template Rebuild Commit Record v1.0.0

Mission: `dfw_homepage_v1_0_10_clone_template_rebuild_commit_and_review_v1_0_0`

Date: {now}

Status: COMMITTED-CANDIDATE / SERVED-RENDERED-PROOF-REQUIRED

## Correction

The active target was regenerated from the locked baseline `index-v1.0.10.html`. The header logo path wrapper was replaced with a direct embedded PNG data URI using the approved base64 source.

## Source gates

- Locked baseline title preserved: PASS
- Failed clean rebuild title absent: PASS
- Direct data URI present exactly once: PASS
- Header `.logo-placeholder` absent: PASS
- Old header logo path absent from header: PASS
- Approved logo PNG decode: PASS
- Approved logo SHA-256: `{logo_sha}`

## Active preview URL

`{URL}`

## Remaining gates

HTTP 200 and desktop/tablet/mobile served rendered proof remain required before PASS.
''', encoding='utf-8')
print('generated active target from locked v1.0.10 baseline')
print('logo sha256:', logo_sha)
