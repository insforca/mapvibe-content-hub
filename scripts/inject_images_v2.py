#!/usr/bin/env python3
"""Inject real image assets into blog posts, replacing placeholder hero images and <!-- IMAGE --> comments."""
import re

BASE = "content-hub"
IMGS = "/assets/images"

def read(path):
    with open(f"{BASE}/{path}") as f:
        return f.read()

def write(path, content):
    with open(f"{BASE}/{path}", "w") as f:
        f.write(content)
    print(f"  ✓ {path}")


# ────────────────────────────────────────────────
# 1. expat-memento.md
# ────────────────────────────────────────────────
p = "docs/en/blog/diaspora/expat-memento.md"
c = read(p)

# Fix cover_image frontmatter
c = c.replace(
    "cover_image: /assets/images/hero-expat-memento.jpg",
    "cover_image: /assets/images/expat-memento_sao-paulo-vila-madalena-30deg.png"
)
# Fix injected hero image tag (from Wave 1 pass)
c = c.replace(
    "![Neighbourhood map print — expat memento](/assets/images/hero-expat-memento.jpg)",
    "![São Paulo Vila Madalena at 30° bearing — Mediterranean Vibes theme]"
    "(/assets/images/expat-memento_sao-paulo-vila-madalena-30deg.png)"
)
# Replace the bearing comparison IMAGE comment
# (captures context: "## The Angle You Know It From\n\n...\n<!-- IMAGE: bearing comparison... -->")
c = c.replace(
    "<!-- IMAGE: bearing comparison — same neighbourhood at 0° vs 30° vs 45° -->",
    "![Caracas 0° vs 30° bearing — full spread comparison]"
    "(/assets/images/expat-memento_before-after-bearing.png)\n\n"
    "*Left: Caracas Chacao at 0° (north-up). Right: same neighbourhood at 30° Mediterranean Vibes.*\n\n"
    "![Caracas Chacao — 0° Mediterranean Vibes]"
    "(/assets/images/expat-memento_caracas-chacao-0deg-med-vibes.png)\n\n"
    "![Caracas Chacao — 30° Mediterranean Vibes]"
    "(/assets/images/expat-memento_caracas-chacao-30deg-med-vibes.png)"
)
# Insert print mockup before the FAQ
c = c.replace(
    "## Frequently Asked Questions",
    "![Expat memento map print — wall mockup]"
    "(/assets/images/expat-memento_print-mockup.png)\n\n"
    "## Frequently Asked Questions"
)
write(p, c)


# ────────────────────────────────────────────────
# 2. village-map-prints.md
# ────────────────────────────────────────────────
p = "docs/en/blog/hidden-gems/village-map-prints.md"
c = read(p)

# Fix cover_image frontmatter (no previous cover_image was set since hero img 404'd on first pass)
# Add it or update placeholder
if "cover_image:" not in c:
    c = re.sub(
        r'(---\n)([\s\S]*?)(^---)',
        lambda m: m.group(1) + m.group(2) + "cover_image: /assets/images/village-zoom-demo.png\n" + m.group(3),
        c, count=1, flags=re.MULTILINE
    )
else:
    c = re.sub(r"cover_image:.*", "cover_image: /assets/images/village-zoom-demo.png", c)

# Replace zoom progression IMAGE comment
c = c.replace(
    "<!-- IMAGE: zoom progression — starting from country level, zooming into a small town, then street level -->",
    "![Village zoom progression — country level to street level in one map]"
    "(/assets/images/village-zoom-demo.png)\n\n"
    "*Zoom in from any level. The editor starts from country scale and goes down to individual streets.*"
)
# Skip the blank small-town-plaza-grid image — replace comment with note
c = c.replace(
    "<!-- IMAGE: example small-town print on wall with warm framing -->",
    "*💡 Tip: Frame small-town prints at A2 or larger — the street geometry deserves space to breathe.*"
)
write(p, c)


# ────────────────────────────────────────────────
# 3. geometric-cities.md
# ────────────────────────────────────────────────
p = "docs/en/blog/city-map-art/geometric-cities.md"
c = read(p)

# Fix cover_image
c = c.replace(
    "cover_image: /assets/images/hero-geometric-cities.jpg",
    "cover_image: /assets/images/grid-brasilia.png"
)
# Fix injected hero (first IMAGE comment was replaced in Wave 1 pass)
c = c.replace(
    "![Geometric city map art — Savannah grid](/assets/images/hero-geometric-cities.jpg)",
    "![Brasília pilot plan — north-up, the geometric masterplan revealed]"
    "(/assets/images/grid-brasilia.png)\n\n"
    "![Brasília pilot plan at 45° — the axis rotates, the geometry intensifies]"
    "(/assets/images/grid-brasilia-45deg.png)"
)
# Replace Chicago IMAGE comment → La Plata (we have those assets, not Chicago)
c = c.replace(
    "<!-- IMAGE: Chicago at 35° bearing, vintage noir theme, showing grid and lakefront -->",
    "![La Plata, Argentina — orthogonal grid, north-up]"
    "(/assets/images/grid-la-plata.png)\n\n"
    "![La Plata at 30° bearing — the diagonal reveals the full Eixample-like plan]"
    "(/assets/images/grid-la-plata-30deg.png)"
)
# Replace Washington DC IMAGE comment → Brasília 45° (already used above, use La Plata 30° as secondary)
c = c.replace(
    "<!-- IMAGE: Washington DC central plan, showing radial + grid intersection -->",
    "*Both Brasília (above) and La Plata share the same principle: a geometric plan so intentional that any bearing other than north reveals something new.*"
)
write(p, c)


# ────────────────────────────────────────────────
# 4. your-angle-vs-tourist-angle.md
# ────────────────────────────────────────────────
p = "docs/en/blog/city-map-art/your-angle-vs-tourist-angle.md"
c = read(p)

# Fix cover_image
c = c.replace(
    "cover_image: /assets/images/hero-your-angle.jpg",
    "cover_image: /assets/images/bearing-grid-sao-paulo.png"
)
# Fix injected hero (first IMAGE comment was replaced in Wave 1 pass)
c = c.replace(
    "![Your angle vs tourist angle — bearing comparison](/assets/images/hero-your-angle.jpg)",
    "![São Paulo 4-bearing comparison grid — how rotation changes everything]"
    "(/assets/images/bearing-grid-sao-paulo.png)"
)
# Add bearing-control-ui.png before "The Bearing That Changes Everything"
c = c.replace(
    "## The Bearing That Changes Everything",
    "![MapVibe bearing control UI — rotate your map to any angle]"
    "(/assets/images/bearing-control-ui.png)\n\n"
    "![São Paulo bearing rotation — animated]"
    "(/assets/images/bearing-grid-sao-paulo.gif)\n\n"
    "## The Bearing That Changes Everything"
)
write(p, c)


# ────────────────────────────────────────────────
# 5. venezuelan-city-maps.md — add theme-grid-caracas.png
# ────────────────────────────────────────────────
p = "docs/en/expat-map-prints/venezuelan-city-maps.md"
c = read(p)

# Insert after the Popular Cities heading
c = c.replace(
    "## Popular Cities",
    "## Popular Cities\n\n"
    "![Caracas multi-theme grid — same neighbourhood, 6 different visual styles]"
    "(/assets/images/theme-grid-caracas.png)\n\n"
    "*Caracas Chacao across 6 MapVibe themes. Each one changes the feeling — pick the one that matches your memory.*"
)
write(p, c)

print("\nAll done.")
