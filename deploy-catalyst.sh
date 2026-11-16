#!/usr/bin/env bash
# Build the site for Zoho Catalyst Web Client Hosting and deploy it.
# Usage: SITE_URL=https://<project>-<id>.catalystserverless.com/app ./deploy-catalyst.sh
set -euo pipefail
cd "$(dirname "$0")"
: "${SITE_URL:?Set SITE_URL to your Catalyst app URL, e.g. https://playora-12345678.catalystserverless.com/app}"
mkdir -p client/assets
cp site/assets/* client/assets/
# Catalyst serves web client files under /app/
BASE_PATH=/app OUT_DIR=client python3 build.py
command -v catalyst >/dev/null || { echo "Install the CLI first: npm i -g zcatalyst-cli && catalyst login"; exit 1; }
catalyst deploy --only client
