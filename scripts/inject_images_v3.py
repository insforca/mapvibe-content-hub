#!/usr/bin/env python3
"""Patch existing posts: gift-that-carries-home (2 images), village-map-prints (fixed plaza grid)."""

BASE = "content-hub"

def read(p):
    with open(f"{BASE}/{p}") as f: return f.read()

def write(p, c):
    with open(f"{BASE}/{p}", "w") as f: f.write(c)
    print(f"  ✓ {p}")


# ── gift-that-carries-home ─────────────────────────────────
p = "docs/en/blog/expat-gifts/gift-that-carries-home.md"
c = read(p)

# Update cover_image
c = c.replace(
    "cover_image: /assets/images/hero-gift-that-carries-home.jpg",
    "cover_image: /assets/images/gift-that-carries-home_latin-city-med-vibes-30deg.png"
)
# Replace hero image tag
c = c.replace(
    "![Gift that carries home — custom map print](/assets/images/hero-gift-that-carries-home.jpg)",
    "![Latin city map print — Mediterranean Vibes 30° bearing]"
    "(/assets/images/gift-that-carries-home_latin-city-med-vibes-30deg.png)\n\n"
    "*Cartagena (Spain) at 30° in Mediterranean Vibes — warm terracotta tones, coastal geometry, the kind of print that stops people mid-conversation.*"
)
# Add wall mockup before FAQ
c = c.replace(
    "## Frequently Asked Questions",
    "![Map print on wall — gift mockup]"
    "(/assets/images/gift-that-carries-home_print-wall-mockup.png)\n\n"
    "## Frequently Asked Questions"
)
write(p, c)


# ── village-map-prints (restore real plaza grid image) ────────
p = "docs/en/blog/hidden-gems/village-map-prints.md"
c = read(p)

# Replace the framing tip with the actual image
c = c.replace(
    "*💡 Tip: Frame small-town prints at A2 or larger — the street geometry deserves space to breathe.*",
    "![Small-town plaza grid print — Tiradentes, Minas Gerais]"
    "(/assets/images/village-map-prints_small-town-plaza-grid.png)\n\n"
    "*Tiradentes, Minas Gerais — a colonial town so small it barely appears on regional maps. At street-level zoom in Vintage Noir, the plaza geometry becomes the whole composition.*"
)
write(p, c)

print("\nAll done.")
