# Zoggy Studios Web

Public static web platform for Zoggy Studios and the Dark Fantasy MMO project.

## Current Milestone

Phase 0 and Phase 1 are complete locally. The current approved focus is Phase 2: Zoggy Studios Foundation.

The studio site is being built first as the broad public home for games, apps, books, scripts, technology projects, and future creative work. The separate Dark Fantasy MMO site remains a placeholder until more game-specific public material is ready.

## Sites

```text
games.herzogit.com
```

Public umbrella site for Zoggy Studios. Zoggy Studios is broad enough for games, IT and technology projects, software, utilities, art, books, media, and future creative work.

```text
darkfantasy.herzogit.com
```

Public placeholder site for Dark Fantasy MMO, currently in pre-alpha development.

## Repository Structure

```text
apps/studio/                 Astro app for games.herzogit.com
apps/darkfantasy/            Astro app for darkfantasy.herzogit.com
packages/branding/           Shared branding access
packages/ui/                 Minimal shared CSS primitives
packages/public-content-contract/
config/branding.json         Shared public branding values
schemas/public-content.schema.json
scripts/verify-build.mjs
scripts/scan-public-output.mjs
docs/
dist/studio/                 Generated studio output
dist/darkfantasy/            Generated Dark Fantasy output
```

## Studio Routes

```text
/
/projects/
/about/
/updates/
/contact/
/privacy/
/terms/
/404.html
```

## Dark Fantasy Routes

```text
/
/404.html
```

The Dark Fantasy app is intentionally minimal for now.

## Prerequisites

- Node.js 24.11.0 was available during setup.
- npm 11.6.1 was available during setup.

Other current Node/npm versions may work, but build verification should be rerun after any runtime change.

## Installation

```text
npm install
```

## Development Commands

```text
npm run dev:studio
npm run dev:darkfantasy
```

## Build Commands

```text
npm run check
npm run build
```

The root build command builds both sites.

## Verification Commands

```text
npm run verify
npm run scan:public
```

`npm run verify` checks required generated files and construction protections.

`npm run scan:public` checks generated output for obvious private references, forbidden files, source leakage, and cross-site leakage indicators.

## Generated Output Locations

```text
dist/studio/
dist/darkfantasy/
```

Only generated files under these directories are intended for deployment.

## Deployment Warning

Do not upload the repository root, source directories, `.git`, `node_modules`, documentation, environment files, credentials, build caches, or private MMO files.

Upload only the contents of each generated output directory:

```text
dist/studio/      -> IONOS /games/
dist/darkfantasy/ -> IONOS /darkfantasy/
```

## Security Boundary Summary

This repository must not connect to the private Dark Fantasy MMO repository, PostgreSQL, private admin endpoints, private health APIs, account data, player data, moderation data, private logs, operational metrics, private content, or environment files.

Future public content may only arrive through a sanitized, approved, versioned public-content bundle. That flow is documented but not implemented in this milestone.
