# Playora website (Zoho Catalyst)

Static site (privacy policy, data safety, content rating, permissions, contact) for the Play Store listing.

## Structure
- `build.py` – generates the pages (edit content/email here).
- `site/` – local-dev build (served at `/`).
- `client/` – Catalyst web client build (served under `/app/`). Contains `client-package.json`.
- `catalyst.json` – Catalyst project config (client hosting only).
- `deploy-catalyst.sh` – builds `client/` and deploys it.

## Local preview
```
python3 build.py && cd site && python3 -m http.server 8000
```

## Deploy to Zoho Catalyst (production)
1. `npm i -g zcatalyst-cli && catalyst login`
2. In this folder run `catalyst init` once: choose **Client**, pick/create your Catalyst project, and keep the existing `client` directory.
3. `SITE_URL=https://<project>-<id>.catalystserverless.com/app ./deploy-catalyst.sh`
   (use your real URL from the Catalyst console → Web Client Hosting; `SITE_URL` feeds canonical links and the sitemap).
4. In the Catalyst console, switch the environment from Development to **Production** (Deploy → Production) to publish.

Privacy policy URL for Play Console: `<SITE_URL>/privacy/` (if the host doesn't resolve folder paths, use `<SITE_URL>/privacy/index.html`).
