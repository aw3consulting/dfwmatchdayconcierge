#!/usr/bin/env bash
set -euo pipefail

: "${DFW_PREVIEW_BASIC_AUTH_USER_B64:?missing DFW_PREVIEW_BASIC_AUTH_USER_B64}"
: "${DFW_PREVIEW_BASIC_AUTH_PASS_B64:?missing DFW_PREVIEW_BASIC_AUTH_PASS_B64}"
: "${LIVE_ROOT:?missing LIVE_ROOT}"
: "${STAGING_ROOT:?missing STAGING_ROOT}"
: "${PREVIEW_PATH:?missing PREVIEW_PATH}"

DFW_PREVIEW_BASIC_AUTH_USER="$(printf '%s' "$DFW_PREVIEW_BASIC_AUTH_USER_B64" | base64 -d)"
DFW_PREVIEW_BASIC_AUTH_PASS="$(printf '%s' "$DFW_PREVIEW_BASIC_AUTH_PASS_B64" | base64 -d)"
PREVIEW_ROOT="$LIVE_ROOT/$PREVIEW_PATH"
STAMP="$(date +%Y%m%d-%H%M%S)"
HTPASSWD_FILE="$HOME/.htpasswd_dfw_preview"

if [ "$PREVIEW_ROOT" = "$LIVE_ROOT" ] || [ -z "$PREVIEW_PATH" ]; then
  echo "FAIL: unsafe preview path"
  exit 1
fi

case "$LIVE_ROOT" in
  /home/dfw_webadmin/preview.dfwmatchdayconcierge.com) ;;
  *) echo "FAIL: LIVE_ROOT outside governed path: $LIVE_ROOT"; exit 1 ;;
esac

case "$STAGING_ROOT" in
  /home/dfw_webadmin/staging.dfwmatchdayconcierge.com) ;;
  *) echo "FAIL: STAGING_ROOT outside governed path: $STAGING_ROOT"; exit 1 ;;
esac

test -d "$LIVE_ROOT"
test -d "$STAGING_ROOT"
test -f "$STAGING_ROOT/index.html"
test -d "$STAGING_ROOT/assets"
test -f "$STAGING_ROOT/connect/index.html"

if [ -d "$PREVIEW_ROOT" ]; then
  mv "$PREVIEW_ROOT" "$LIVE_ROOT/preview.backup.$STAMP"
fi

mkdir -p "$PREVIEW_ROOT"
rsync -a --delete --exclude ".git" "$STAGING_ROOT"/ "$PREVIEW_ROOT"/

printf "%s:%s\n" "$DFW_PREVIEW_BASIC_AUTH_USER" "$(openssl passwd -apr1 "$DFW_PREVIEW_BASIC_AUTH_PASS")" > "$HTPASSWD_FILE"
chmod 600 "$HTPASSWD_FILE"

cat > "$PREVIEW_ROOT/.htaccess" <<EOF
AuthType Basic
AuthName "DFW Matchday Preview"
AuthUserFile $HTPASSWD_FILE
Require valid-user
Options -Indexes

<IfModule mod_headers.c>
Header set X-Robots-Tag "noindex, nofollow, noarchive"
</IfModule>
EOF

find "$PREVIEW_ROOT" -type f -name "*.html" -exec perl -0pi -e 's#</head>#<meta name="robots" content="noindex,nofollow,noarchive"></head>#i unless /name=["'"'"'']robots["'"'"'']/i' {} \;
find "$PREVIEW_ROOT" -type f \( -name "*.html" -o -name "*.css" -o -name "*.js" \) -exec perl -0pi -e '
  s#(src|href)=["'"'"'']/(assets/)#$1="/preview/$2#g;
  s#(src|href)=["'"'"'']/(connect/)#$1="/preview/$2#g;
  s#url\((["'"'"'']?)/(assets/)#url($1/preview/$2#g;
' {} +

echo "PREVIEW_DEPLOYED=https://dfwmatchdayconcierge.com/preview/"
echo "LIVE_ROOT_PRESERVED=$LIVE_ROOT"
echo "PREVIEW_ROOT=$PREVIEW_ROOT"
