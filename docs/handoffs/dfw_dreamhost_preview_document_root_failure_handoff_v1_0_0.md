# DFW DreamHost Preview Document Root Failure Handoff v1.0.0

## Mission

Create a clean handoff for a new execution lane to resolve DreamHost preview visibility for the DFW Matchday Concierge homepage raster logo.

Repository: `aw3consulting/dfwmatchdayconcierge`

Branch: `main`

Final domain: `https://dfwmatchdayconcierge.com`

Preview attempt paths:

- Rejected html-preview surface: `https://html-preview.github.io/?url=https://github.com/aw3consulting/dfwmatchdayconcierge/blob/main/docs/prototypes/pdf-reference-homepage-replica-v1.0.0/index-v1.0.18-raster-image-visibility-corrected.html`
- Failed DreamHost subdomain attempt: `https://preview.dfwmatchdayconcierge.com/`
- Failed DreamHost main-domain subfolder attempt: `https://dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/`

## Current standing

`FAILED / DREAMHOST PREVIEW NOT VERIFIED / ACTIVE DOCUMENT ROOT NOT IDENTIFIED / DO NOT CLAIM IMAGE CORRECTION`

The current execution lane failed after repeated incorrect routing assumptions. Do not continue by guessing DreamHost panel wording, adding DNS records blindly, or moving files without first identifying the active Apache document root for `dfwmatchdayconcierge.com`.

## Evidence summary

### 1. html-preview remained invalid for approval

The user uploaded a PDF of the html-preview surface showing the homepage header text and navigation, but the far-left header logo area was still blank. Therefore html-preview did not satisfy browser-visible raster image verification.

### 2. GitHub Actions deploy pipeline was created

Workflow file created:

`.github/workflows/deploy-dreamhost-preview.yml`

Relevant commits:

- `467ae7121a4f950f29342892028be42599c47d4f` — Add manual DreamHost preview deploy workflow.
- `2bd108b4c87dadb793702cc2baf482631d10bfb5` — Add push trigger to force workflow run.
- `e974e2d23da143f85b765d60863c927ed4e56e9a` — Add directory creation and move deployment toward main-domain subfolder preview path.

The GitHub Actions deployment succeeded after the `DREAMHOST_SSH_KEY` secret was corrected.

### 3. GitHub Actions secrets configured

The following repo secrets were created:

- `DREAMHOST_HOST`
- `DREAMHOST_USER`
- `DREAMHOST_SSH_KEY`
- `DREAMHOST_PORT`
- `DREAMHOST_TARGET_DIR`

Known prior values used during this lane:

- `DREAMHOST_HOST`: `iad1-shared-e1-16.dreamhost.com`
- `DREAMHOST_USER`: `dfw_webadmin`
- `DREAMHOST_PORT`: `22`

`DREAMHOST_TARGET_DIR` was changed from the failed subdomain directory to:

`/home/dfw_webadmin/dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/`

### 4. SSH key installed on DreamHost user

A public key was added to:

`/home/dfw_webadmin/.ssh/authorized_keys`

GitHub Actions authenticated successfully after the matching full OpenSSH private key was stored in `DREAMHOST_SSH_KEY`.

### 5. Files exist on DreamHost server but are not publicly served

User ran:

```bash
ls -la /home/dfw_webadmin/dfwmatchdayconcierge.com/
ls -la /home/dfw_webadmin/dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/
```

Output confirmed:

```text
/home/dfw_webadmin/dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/index.html
/home/dfw_webadmin/dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/assets/
```

### 6. Public URL returns 404 despite files existing

User ran:

```bash
curl -I https://dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/
curl -I https://dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/assets/images/logos/dfw-logo-header-raster-v1.0.3.png
```

Both returned:

```text
HTTP/2 404
server: Apache
```

### 7. Root test proves the assumed document root is not active

User created:

```bash
printf 'DFW ROOT TEST\n' > /home/dfw_webadmin/dfwmatchdayconcierge.com/aw3-root-test.txt
```

Then tested:

```bash
curl -I https://dfwmatchdayconcierge.com/aw3-root-test.txt
```

Result:

```text
HTTP/2 404
server: Apache
```

This conclusively proves:

`/home/dfw_webadmin/dfwmatchdayconcierge.com/` is not the active Apache document root serving `https://dfwmatchdayconcierge.com/`.

### 8. Preview subdomain attempt should remain abandoned

The attempted CNAME `preview.dfwmatchdayconcierge.com` was deleted by the user after failed routing.

Do not recreate `preview.dfwmatchdayconcierge.com` without first identifying the correct DreamHost hosting model and active web root.

## What is not the current root cause

Do not continue re-solving these already-isolated areas:

- Not a missing GitHub Actions secret.
- Not an rsync failure.
- Not a missing deployed `index.html` under the assumed target directory.
- Not a missing deployed PNG under the assumed target directory.
- Not the original html-preview-only relative path issue.
- Not a need to use SVG.
- Not a basis for production launch approval.

## Active root cause to solve

The active root cause is:

`The actual Apache document root for https://dfwmatchdayconcierge.com/ is unknown and is not /home/dfw_webadmin/dfwmatchdayconcierge.com/.`

The next execution lane must identify the real served directory and then update deployment target accordingly.

## Required next execution sequence

1. Do not change DNS.
2. Do not recreate preview CNAME.
3. Do not rerun GitHub Actions until the active document root is identified.
4. Determine the active DreamHost document root for `dfwmatchdayconcierge.com`.
5. Once the actual document root is known, update only `DREAMHOST_TARGET_DIR` or workflow target path.
6. Deploy a harmless root test file and confirm it returns `HTTP 200` before deploying the homepage preview again.
7. Deploy the homepage preview into a non-production subfolder only.
8. Verify:
   - preview HTML returns `200`
   - direct PNG URL returns `200`
   - header logo visibly renders in a browser
9. Do not claim correction until browser-visible verification succeeds on a DreamHost-served URL.

## Exact DreamHost support request

If the active document root cannot be found in the DreamHost panel, open DreamHost support with this exact request:

```text
For dfwmatchdayconcierge.com, what is the active Apache document root and assigned Unix user? Files placed at /home/dfw_webadmin/dfwmatchdayconcierge.com/ are not publicly reachable, including /aw3-root-test.txt, which returns HTTP 404. Please confirm the actual served web directory for https://dfwmatchdayconcierge.com/ and whether the domain is served by a different user, mirrored/redirected configuration, Passenger app, or managed/static site location.
```

## New execution lane prompt

```text
You are operating inside the DFW Matchday Concierge governed workspace.

MISSION:
dfw_dreamhost_active_document_root_identification_and_preview_redeployment_v1_0_0

Repository:
aw3consulting/dfwmatchdayconcierge

Branch:
main

FINAL LAUNCH CONTEXT:
The homepage raster logo visibility issue has not been accepted. GitHub/html-preview is rejected as an approval surface. DreamHost deployment automation exists and succeeds, but the deployed files are not publicly reachable because the active Apache document root for dfwmatchdayconcierge.com has not been identified.

DO NOT:
- Do not claim the image correction is complete.
- Do not deploy to production root.
- Do not recreate preview.dfwmatchdayconcierge.com DNS.
- Do not use SVG as the logo solution.
- Do not continue guessing DreamHost routing.
- Do not rerun GitHub Actions until the active document root is confirmed.

READ FIRST:
docs/handoffs/dfw_dreamhost_preview_document_root_failure_handoff_v1_0_0.md

KNOWN FACTS:
1. GitHub Actions deploy workflow exists at .github/workflows/deploy-dreamhost-preview.yml.
2. GitHub Actions deployment succeeded after DREAMHOST_SSH_KEY was corrected.
3. Files exist at /home/dfw_webadmin/dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/index.html.
4. Public URL https://dfwmatchdayconcierge.com/_preview/homepage-raster-v1-0-19/ returns HTTP/2 404.
5. Root test /home/dfw_webadmin/dfwmatchdayconcierge.com/aw3-root-test.txt also returns HTTP/2 404 at https://dfwmatchdayconcierge.com/aw3-root-test.txt.
6. Therefore /home/dfw_webadmin/dfwmatchdayconcierge.com/ is not the active public web root.

REQUIRED EXECUTION:
1. Identify the actual Apache/DreamHost document root for dfwmatchdayconcierge.com.
2. Verify document root with a harmless test file that returns HTTP 200.
3. Update DREAMHOST_TARGET_DIR or the deploy workflow only after root confirmation.
4. Redeploy the preview to a non-production subfolder.
5. Verify:
   - preview page returns HTTP 200
   - direct PNG URL returns HTTP 200
   - header logo is browser-visible
6. Return files changed, server path, public preview URL, verification commands, verification outputs, and remaining risks.

FAILURE CONDITION:
If the page or logo is not browser-visible through a DreamHost-served URL, do not claim correction.
```

## Final standing

`HANDOFF CREATED / PRIOR EXECUTION LANE FAILED / NEXT LANE MUST START WITH ACTIVE DOCUMENT ROOT IDENTIFICATION`
