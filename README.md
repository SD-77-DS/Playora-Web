# Playora website

Static site for Play Store requirements. Edit `build.py`, then run `python3 build.py` to regenerate `site/`.

| Path | Purpose |
|---|---|
| `/` | Home |
| `/privacy/` | Privacy policy URL for Play Console |
| `/data-safety/` | Data safety answers |
| `/content-rating/` | Content rating answers |
| `/audience-and-ads/` | Target audience and ads declaration |
| `/permissions/` | Foreground service, media and notification justifications |
| `/contact/` | Contact |

**Before publishing:** set `CONTACT` in `build.py` to a real email.
Preview: `cd site && python3 -m http.server 8000`. Host `site/` on GitHub Pages, Netlify, etc.
