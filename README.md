# Playora website (Zoho Catalyst Slate)

Static site (privacy policy, data safety, content rating, permissions, contact) for the Play Store listing.
The deployable files are already built and committed in **`site/`**; no build tooling is needed on the host.

## Slate settings
| Setting | Value |
|---|---|
| Source | GitHub repo `SD-77-DS/Playora-Web`, branch `main` (or zip/CLI upload) |
| Framework preset | Other / Static |
| Install command | *(none)* |
| Build command | `npm run build` (a no-op) or leave empty |
| Output directory | `site` |

URLs are served from the root of your Slate domain:
`/`, `/privacy/`, `/data-safety/`, `/content-rating/`, `/audience-and-ads/`, `/permissions/`, `/contact/`.

### Deploy
- **From Git:** Catalyst console → Slate → create app → connect GitHub → select the repo → enter the settings above → Deploy.
- **From CLI:** `npm i -g zcatalyst-cli && catalyst login && catalyst slate:create` and follow the prompts (output directory: `site`).

Privacy policy URL for Play Console: `https://<your-slate-domain>/privacy/`.

## Editing content
Edit `build.py`, run `python3 build.py`, commit the regenerated `site/`. Optionally set `SITE_URL=https://<slate-domain>` while building to add canonical links and `sitemap.xml`.

## Local preview
```
python3 build.py && cd site && python3 -m http.server 8000
```
