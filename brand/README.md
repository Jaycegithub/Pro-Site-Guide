# ProSiteGuide logo concepts

Five logo directions built on the website's brand system:

- **Colors:** navy `#0F172A`, brand blue `#1D4ED8`, gradient `#3B82F6 → #1D4ED8`, light blue on dark `#93C5FD`
- **Wordmark:** "ProSite" in navy + "Guide" in blue, set in **Space Grotesk Bold** (the site's headline font), converted to outlines so the SVGs render identically everywhere

Open `logo-concepts-overview.png` to compare them side by side.

| # | Concept | Idea |
|---|---------|------|
| 01 | Layered Check | Refined version of the current icon (stacked site layers + check) |
| 02 | Trust Shield | Shield + check on navy: security and trust for law firms |
| 03 | Browser Check | Website window + check: "websites, reviewed and approved" |
| 04 | P Monogram | Bold "P" with a blue check badge: compact, legible at tiny sizes |
| 05 | Guide Compass | Compass needle: the "guide" in ProSiteGuide |

## Files in each concept folder

| File | Size | Use it for |
|------|------|-----------|
| `logo-horizontal.svg` / `.png` | 1358×240 PNG, transparent | Website header logo (light backgrounds) |
| `logo-horizontal-white.svg` / `.png` | 1358×240 PNG, transparent | Website footer and other dark backgrounds |
| `icon.svg` / `site-icon-512.png` | 512×512, rounded, transparent corners | WordPress **Site Icon** (browser tab / favicon) |
| `icon-square-fullbleed.svg` | 512×512, edge to edge | Source for square/round profile images |
| `facebook-profile-720.png` | 720×720 | Facebook Page profile picture (Facebook crops it to a circle) |
| `facebook-cover-1640x624.png` | 1640×624 | Facebook Page cover photo |
| `linkedin-logo-400.png` | 400×400 | LinkedIn Company Page logo |
| `linkedin-banner-1128x191.png` | 1128×191 | LinkedIn Company Page cover image (text kept right so the logo can overlap bottom-left) |

## Where to upload

- **Website header logo:** Elementor → the "Logo" container in the *ProSiteGuide Header* template (or Appearance → Customize → Site Identity → Logo). Show it at about 36–40px tall.
- **Website footer logo:** the *ProSiteGuide Footer* template, using `logo-horizontal-white.png`.
- **Favicon:** Settings → General → Site Icon (or Customize → Site Identity), using `site-icon-512.png`.
- **Facebook Page:** profile picture `facebook-profile-720.png`, cover photo `facebook-cover-1640x624.png`.
- **LinkedIn Company Page:** logo `linkedin-logo-400.png`, cover `linkedin-banner-1128x191.png`.
