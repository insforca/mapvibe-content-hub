#!/usr/bin/env python3
"""Update cover_image frontmatter to permanent Shopify CDN URLs."""

BASE = "content-hub"

UPDATES = [
    # (file_path, old_cover_image_value, new_cdn_url)
    (
        "docs/en/blog/diaspora/expat-memento.md",
        "/assets/images/expat-memento_sao-paulo-vila-madalena-30deg.png",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-expat-memento.jpg",
    ),
    (
        "docs/en/blog/hidden-gems/village-map-prints.md",
        "/assets/images/village-zoom-demo.png",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-village-map-prints.jpg",
    ),
    (
        "docs/en/blog/city-map-art/geometric-cities.md",
        "/assets/images/grid-brasilia.png",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-geometric-cities.jpg",
    ),
    (
        "docs/en/blog/city-map-art/your-angle-vs-tourist-angle.md",
        "/assets/images/bearing-grid-sao-paulo.png",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-your-angle-vs-tourist-angle.jpg",
    ),
    (
        "docs/en/blog/expat-gifts/gift-that-carries-home.md",
        "/assets/images/gift-that-carries-home_latin-city-med-vibes-30deg.png",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-gift-that-carries-home.jpg",
    ),
    (
        "docs/en/expat-map-prints/brazilian-city-maps.md",
        "/assets/images/hero-brazil.jpg",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-brazilian-city-maps.jpg",
    ),
    (
        "docs/en/expat-map-prints/venezuelan-city-maps.md",
        "/assets/images/hero-venezuela.jpg",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-venezuelan-city-maps.jpg",
    ),
    (
        "docs/en/expat-map-prints/colombian-city-maps.md",
        "/assets/images/hero-colombia.jpg",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-colombian-city-maps.jpg",
    ),
    (
        "docs/en/expat-map-prints/mexican-city-maps.md",
        "/assets/images/hero-mexico.jpg",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-mexican-city-maps.jpg",
    ),
    (
        "docs/en/expat-map-prints/cuban-city-maps.md",
        "/assets/images/hero-cuba.jpg",
        "https://cdn.shopify.com/s/files/1/1036/6422/2549/t/5/assets/blog-hero-cuban-city-maps.jpg",
    ),
]

for rel_path, old_val, new_val in UPDATES:
    full = f"{BASE}/{rel_path}"
    with open(full) as f:
        content = f.read()
    old_line = f"cover_image: {old_val}"
    new_line = f"cover_image: {new_val}"
    if old_line not in content:
        print(f"  ✗ MISS  {rel_path}  (expected: {old_val})")
        continue
    content = content.replace(old_line, new_line, 1)
    with open(full, "w") as f:
        f.write(content)
    print(f"  ✓ {rel_path}")

print("\nDone.")
