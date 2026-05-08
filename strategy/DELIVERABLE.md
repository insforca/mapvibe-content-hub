---
type: markdown
title: MapVibe Content Hub — Full Scaffold Delivered
---

# MapVibe Content Hub — Scaffold Complete

## What's Ready (23 files)

### `docmd.config.js`
Brand colors (Navy/Gold/Surface), Playfair/Geist fonts, i18n (EN/PT/ES), full navigation, SEO meta with diaspora keyword list, sitemap + `llms.txt` auto-generated at build.

---

### Pillar Pages (4 pages)
`/pillars/perspective-shift/` · `/pillars/theme-speed-run/` · `/pillars/bearing-personality/` · `/pillars/hidden-gem-zoom/`

Each pillar page: full copy, feature tabs, visual asset placeholders for UI Tars, CTA → `app.mapvibestudio.com`.

---

### Expat Collections (5 nationality pages)
`/expat-map-prints/` → Brazilian · Venezuelan · Colombian · Mexican · Cuban

---

### Blog Posts — Wave 1 ✅ (Publish First)

| Post | Slug | Pillar |
|---|---|---|
| When You Move Abroad, You Start Seeing Home Differently | `/blog/diaspora/expat-memento/` | Perspective Shift |
| Not Just Big Cities: The Village Map You Never Knew You Needed | `/blog/hidden-gems/village-map-prints/` | Hidden Gem Zoom |
| Your Angle vs. The Tourist's Angle | `/blog/city-map-art/your-angle-vs-tourist-angle/` | Perspective + Bearing |
| The Gift That Carries Home | `/blog/expat-gifts/gift-that-carries-home/` | Hidden Gem + Gifts |
| Cities With Extraordinary Map Geometry | `/blog/city-map-art/geometric-cities/` | Hidden Gem Zoom |

### Blog Posts — Wave 2 (Nationality SEO)
🇧🇷 Brazil · 🇻🇪 Venezuela — **drafted**  
🇨🇴 Colombia · 🇲🇽 Mexico · 🇨🇺 Cuba — **queued**

### Blog Posts — Wave 3 (Pillar Deep-Dives, queued)
- What Your Map's Bearing Says About You
- 62 Ways to See Your City: A Theme Guide
- Housewarming Gifts for People Who Left Everything Behind

---

### Strategy Docs (Internal, not published)
- `keyword-targets.md` — 6 keyword clusters, AEO/GEO/AIO plan, schema recommendations per page type
- `blog-calendar.md` — 13-post pipeline with publish order, Wave 1/2/3 cadence, visual asset matrix
- `pillar-pages.md` — full annotated folder tree + deployment instructions

---

## Visual Assets
**UI Tars** has been briefed with 8 asset sets covering all Wave 1+2 posts:
bearing comparisons (0°/30°/90°/180°), theme speed-run video, zoom progression, neighbourhood wall mockups, geometric city captures (Savannah, Chicago, DC).

---

## One Gap: "Rusty SEO Agent"
No agent by that name is visible in this project. The SEO/GEO skill repo (`seo-geo-claude-skills`) is referenced in memory but maps to the **Geo Agent** (not currently in the project). Once you add that agent, I can brief them on the keyword clusters and AEO targets from `strategy/keyword-targets.md`.

---

## Deploy When Ready
```bash
cd content-hub
npx @docmd/core build   # → ./out/ (static HTML + sitemap.xml + llms.txt)
```
Deploy `./out/` to Vercel or Cloudflare Pages.
