# Security

## Public And Private Boundary

This repository owns only the public Zoggy Studios web platform.

The private Dark Fantasy MMO repository remains authoritative for game client code, game server code, PostgreSQL persistence, canonical content, private administration, private logs, account data, player data, moderation data, and public-content export generation.

## Prohibited Integrations

Do not connect this repository to:

- PostgreSQL
- database credentials
- private admin endpoints
- private health APIs
- game server process information
- private logs
- player data
- account data
- moderation data
- raw operational metrics
- internal content errors
- environment files
- server-authoritative formulas
- private asset paths

## Deployment Allowlist

Only deploy generated files under:

```text
dist/studio/
dist/darkfantasy/
```

Never deploy repository roots or source directories.

## Secret Scanning Expectations

Before deployment, run:

```text
npm run scan:public
```

Also manually inspect generated output before upload. The scanner is a safety net, not a complete security audit.

## Content Sanitization Boundary

Future public game content must arrive only as a sanitized, approved, versioned bundle. The website must not read private MMO databases, private admin endpoints, internal exports, or draft content directly.

## Directory Listing Prevention

Each site includes `.htaccess` with:

```apache
Options -Indexes
DirectoryIndex index.html
```

Remote behavior must be verified on IONOS after upload.

## Cross-Site Separation

The studio output and Dark Fantasy output are generated into separate directories. The scanner checks for obvious route-only leakage indicators, but manual inspection is still required before upload.

## No Admin Endpoint Exposure

The public sites must not link to or proxy private admin routes. Do not reuse private admin URLs for public status, account, or content features.

## No Direct Database Access

The browser and static site build must never access PostgreSQL directly.
