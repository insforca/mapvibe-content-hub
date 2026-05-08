const { defineConfig } = require('@docmd/core');

module.exports = defineConfig({
  title: 'MapVibe Studio — Custom Map Prints for Expats & Diaspora',
  url: 'https://mapvibestudio.com',

  // Source → the content hub lives in /docs
  src: 'docs',
  out: 'out',

  // --- SEO / AI discoverability ---
  // llms.txt + llms-full.txt generated automatically at build
  // sitemap.xml generated automatically
  // OpenGraph + canonical URLs built in

  // --- Internationalisation ---
  // Locale-first URLs: /pt/, /es/, /es-co/ etc.
  // Each locale gets its own search index
  i18n: {
    default: 'en',
    locales: [
      { id: 'en', label: 'English' },
      { id: 'pt', label: 'Português' },       // Brazilian diaspora
      { id: 'es', label: 'Español' },          // Venezuelan / Colombian / Mexican / Cuban
    ]
  },

  // --- Navigation ---
  // Auto-generated from folder structure.
  // Numeric prefixes (01-, 02-) control order.
  // Override here only if needed.
  navigation: [
    {
      label: 'Expat Map Prints',
      items: [
        { label: 'Why Expats Choose MapVibe', href: '/expat-map-prints/' },
        { label: 'Brazilian City Maps',        href: '/expat-map-prints/brazilian-city-maps/' },
        { label: 'Venezuelan City Maps',       href: '/expat-map-prints/venezuelan-city-maps/' },
        { label: 'Colombian City Maps',        href: '/expat-map-prints/colombian-city-maps/' },
        { label: 'Mexican City Maps',          href: '/expat-map-prints/mexican-city-maps/' },
        { label: 'Cuban City Maps',            href: '/expat-map-prints/cuban-city-maps/' },
      ]
    },
    {
      label: 'The Four Pillars',
      items: [
        { label: 'Perspective Shift',     href: '/pillars/perspective-shift/' },
        { label: 'Theme Speed-Run',       href: '/pillars/theme-speed-run/' },
        { label: 'Bearing = Personality', href: '/pillars/bearing-personality/' },
        { label: 'Hidden Gem Zoom',       href: '/pillars/hidden-gem-zoom/' },
      ]
    },
    {
      label: 'Diaspora Gifts',
      items: [
        { label: 'Gift Guide for Expats',         href: '/diaspora-gifts/' },
        { label: 'Housewarming Gifts',            href: '/diaspora-gifts/housewarming/' },
        { label: 'Village & Small Town Maps',     href: '/diaspora-gifts/village-maps/' },
        { label: 'Geometric City Maps',           href: '/diaspora-gifts/geometric-cities/' },
      ]
    },
    {
      label: 'Blog',
      href: '/blog/'
    }
  ],

  // --- Plugins ---
  plugins: [
    // All bundled by default: search, seo, sitemap, git, analytics, llms, mermaid, openapi
    // Add optional plugins here if needed:
    // require('@docmd/plugin-pwa')()
  ],

  // --- Theme ---
  // Brand colors: Navy #1B2A4A | Gold #C9A96E | Surface #F5EDE4
  // Typography: Geist (body) / Playfair Display (headings)
  theme: {
    colors: {
      primary:    '#1B2A4A',   // Navy
      accent:     '#C9A96E',   // Gold
      background: '#F5EDE4',   // Surface
    },
    fonts: {
      heading: '"Playfair Display", Georgia, serif',
      body:    '"Geist", "Inter", system-ui, sans-serif',
    }
  },

  // --- Meta ---
  meta: {
    description: 'Custom city and village map prints for the diaspora and expat community. Your city, your angle, your theme.',
    keywords: [
      'expat map prints',
      'diaspora map art',
      'custom city map poster',
      'personalized map print',
      'Brazilian city maps',
      'Venezuelan map art',
      'Colombian city prints',
      'village map poster',
      'housewarming gift expat',
      'custom map bearing rotation',
    ],
    og: {
      image: '/assets/og-default.jpg',
    }
  }
});
