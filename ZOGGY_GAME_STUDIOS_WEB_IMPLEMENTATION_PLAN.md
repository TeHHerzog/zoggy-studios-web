# Zoggy Game Studios Web Platform Implementation Plan

This preserved source brief was provided before implementation. It may contain the older working name `Zoggy Game Studios`; new public-facing work uses `Zoggy Studios` as the umbrella brand.

## Current Implementation Round

Implement Phase 0 and Phase 1 only:

- repository foundation
- architecture documentation
- security boundaries
- configurable branding
- domain mapping
- IONOS deployment documentation
- public content contract placeholder
- two minimal static placeholder sites
- responsive rendering
- construction-phase `robots.txt`
- custom 404 pages
- directory-listing prevention
- build verification
- public-output scanning

Do not implement account services, database integration, private admin integration, public wiki, automated deployment, or full future studio sections during this round.

## Public Branding Decision

Use:

```text
STUDIO_NAME=Zoggy Studios
STUDIO_SHORT_NAME=Zoggy
GAME_NAME=Dark Fantasy MMO
GAME_STATUS=Pre-alpha
```

Zoggy Studios is the umbrella organization for games, IT and technology projects, software, utilities, art, books, media, and other creative work. This round only builds placeholders for the studio umbrella and the Dark Fantasy MMO project.

## Domains

```text
games.herzogit.com
darkfantasy.herzogit.com
```

Expected IONOS webspace mapping:

```text
games.herzogit.com -> /games/ -> contents of dist/studio/
darkfantasy.herzogit.com -> /darkfantasy/ -> contents of dist/darkfantasy/
```

Upload the contents of each output directory, not the parent `dist` directory.

## Technology

Use Astro static output and npm workspaces. Do not require a persistent Node.js server in production. Do not add Next.js, a database, PostgreSQL, authentication, CMS, Docker, Kubernetes, private APIs, or automated deployment.

## Private MMO Boundary

The public web repository must remain completely separate from the private Dark Fantasy MMO repository. It must never connect to PostgreSQL, private admin endpoints, `http://127.0.0.1:9090/admin/panel`, private health APIs, player data, moderation data, private logs, operational metrics, internal content errors, private asset paths, environment files, credentials, or server-authoritative formulas.

Future public content may only arrive as a sanitized, approved, versioned public-content bundle. This milestone creates only placeholder schema and documentation.

## Phase 1 Pages

Studio:

- `/`
- `/404.html`

Dark Fantasy:

- `/`
- `/404.html`

Do not create future routes yet.

## Robots During Construction

Both sites must include:

```text
User-agent: *
Disallow: /
```

Do not remove this until public indexing is explicitly approved.
