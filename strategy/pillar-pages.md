# MapVibe Content Hub — Folder Structure

```
content-hub/
├── docmd.config.js                          ← Brand colors, i18n (EN/PT/ES), SEO meta, navigation
├── package.json
│
├── docs/                                    ← PUBLIC CONTENT (served by docmd)
│   │
│   ├── index.md                             ← Homepage: hero + four section cards
│   │
│   ├── expat-map-prints/                    ← PILLAR: nationality-level hub
│   │   ├── index.md                         ← Why expats choose MapVibe
│   │   ├── brazilian-city-maps.md           ← 🇧🇷 Brazilian diaspora
│   │   ├── venezuelan-city-maps.md          ← 🇻🇪 Venezuelan diaspora
│   │   ├── colombian-city-maps.md           ← 🇨🇴 Colombian diaspora
│   │   ├── mexican-city-maps.md             ← 🇲🇽 Mexican diaspora
│   │   └── cuban-city-maps.md               ← 🇨🇺 Cuban diaspora
│   │
│   ├── pillars/                             ← PILLAR: four brand pillars
│   │   ├── perspective-shift.md             ← Pillar 1
│   │   ├── theme-speed-run.md               ← Pillar 2
│   │   ├── bearing-personality.md           ← Pillar 3
│   │   └── hidden-gem-zoom.md               ← Pillar 4
│   │
│   ├── diaspora-gifts/                      ← PILLAR: gift intent
│   │   ├── index.md                         ← Gift guide hub
│   │   ├── housewarming.md                  ← Housewarming gifts
│   │   ├── village-maps.md                  ← Village/small town
│   │   └── geometric-cities.md              ← Geometric grid cities
│   │
│   └── blog/                                ← BLOG
│       ├── index.md                         ← Blog hub
│       │
│       ├── expat-gifts/
│       │   ├── gift-that-carries-home.md    ← ✅ Drafted (Wave 1)
│       │   └── housewarming-diaspora.md     ← 📝 Wave 3
│       │
│       ├── city-map-art/
│       │   ├── geometric-cities.md          ← ✅ Drafted (Wave 1)
│       │   ├── your-angle-vs-tourist-angle.md ← ✅ Drafted (Wave 1)
│       │   ├── bearing-says-about-you.md    ← 📝 Wave 3
│       │   └── theme-guide.md               ← 📝 Wave 3
│       │
│       └── diaspora/
│           ├── expat-memento.md             ← ✅ Drafted (Wave 1)
│           ├── brazil.md                    ← ✅ Drafted (Wave 2)
│           ├── venezuela.md                 ← ✅ Drafted (Wave 2)
│           ├── colombia.md                  ← 📝 Wave 2
│           ├── mexico.md                    ← 📝 Wave 2
│           └── cuba.md                      ← 📝 Wave 2
│
├── assets/                                  ← Images + videos
│   ├── og-default.jpg                       ← Default OG image
│   ├── screenshots/                         ← UI Tars static captures
│   │   ├── perspective-shift/
│   │   ├── bearing-comparisons/
│   │   ├── theme-speed-run/
│   │   ├── hidden-gem-zoom/
│   │   └── wall-mockups/
│   └── videos/                              ← UI Tars screen recordings
│       ├── theme-speed-run.mp4
│       ├── bearing-rotation.mp4
│       └── zoom-progression.mp4
│
└── strategy/                                ← INTERNAL (not served publicly)
    ├── keyword-targets.md                   ← Keyword clusters + AEO/GEO/AIO plan
    ├── blog-calendar.md                     ← 13-post pipeline + publish order
    └── pillar-pages.md                      ← This file
```

---

## Deployment

```bash
cd content-hub
npx @docmd/core build     # → ./out/ (static HTML, sitemap.xml, llms.txt)
```

Deploy `./out/` to:
- **Vercel**: `vercel deploy --prod ./out` (add `vercel.json` with `outputDirectory: out`)
- **Cloudflare Pages**: push to git, configure build command `npx @docmd/core build`
- **Docker**: `docmd deploy` generates Dockerfile
