# Architecture

## Current Verified Architecture

This repository uses Astro static output with npm workspaces.

There are two independently deployable Astro apps:

```text
apps/studio
apps/darkfantasy
```

Their build outputs are configured as:

```text
dist/studio
dist/darkfantasy
```

## Current Product Focus

The approved product focus has moved from placeholder-only setup to Zoggy Studios Foundation. The studio site is now the primary public surface. The Dark Fantasy MMO site remains a separate placeholder until the game has approved public content, screenshots, alpha messaging, or press material.

## Why Astro

Astro was selected because it produces static output by default, keeps client-side JavaScript minimal, works well for placeholder pages and later content-heavy pages, and does not require a persistent Node.js server in production.

## Why Two Sites Are Separate

The studio site and the game site deploy to separate domains and separate IONOS directories. Keeping them as separate apps reduces cross-site leakage risk and makes it clear which files belong to each public domain.

## Shared Pieces

The current shared pieces are intentionally small:

- branding values from `config/branding.json`
- branding exports from `packages/branding`
- layout and accessibility CSS primitives from `packages/ui`
- verification scripts at the repository root

## Not Shared

The sites do not share page routes, private content, site-specific atmospheres, or future sections.

The Dark Fantasy site does not receive private MMO code, private assets, database access, or admin integration.

## Static Build Flow

```text
npm install
npm run check
npm run build
npm run verify
npm run scan:public
```

The root build runs the studio app build and then the Dark Fantasy app build.

## Output Directory Flow

```text
apps/studio       -> dist/studio       -> IONOS /games/
apps/darkfantasy  -> dist/darkfantasy  -> IONOS /darkfantasy/
```

Upload the contents of each output directory, not `dist` itself.

## Current Studio Routes

The studio app currently includes:

- `/`
- `/projects/`
- `/about/`
- `/updates/`
- `/contact/`
- `/privacy/`
- `/terms/`
- `/404.html`

## Future Expansion

Zoggy Studios may later include IT projects, software, utilities, art, books, scripts, film concepts, media, and other creative work. The current brand and architecture allow that expansion without forcing detailed future sections before real work exists.

## Why Some Future Sections Are Not Built Yet

The site includes broad shelves for future work, but not full book catalogs, script portfolios, app stores, media kits, newsletters, account systems, or press kits. Those should be added when the underlying work and operating process are real enough to maintain.
