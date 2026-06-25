# Content Integration

## Current Status

Public content integration is not implemented during this milestone.

This repository includes only a placeholder schema:

```text
schemas/public-content.schema.json
```

## Future Sanitized Flow

```text
MMO repository
-> validate and approve public content
-> generate sanitized versioned bundle
-> manually copy approved bundle
-> web build validates schema
-> static pages are generated
-> only generated static output is deployed
```

## Allowed Public Collections Later

- monsters
- items
- skills
- zones
- quests

## Prohibited Fields

Future public content must exclude drafts, admin notes, secret quests unless explicitly public, hidden drop formulas, server-only AI behavior, internal database identifiers, private asset paths, unreleased areas, account data, player data, operational metrics, security configuration, moderation data, internal errors, and raw logs.

## Compatibility Claim

The placeholder schema does not claim compatibility with any MMO exporter. The exporter is outside this repository and outside this milestone.
