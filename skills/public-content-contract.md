# Public Content Contract Skill

## Goal

Prepare for future public content without exposing private game data.

## Allowed model

The web repository consumes a versioned, sanitized, approved bundle generated elsewhere.

## Minimum metadata

```json
{
  "schema_version": 1,
  "content_version": "example",
  "generated_at": "2026-01-01T00:00:00Z"
}
```

## Candidate public collections

- monsters
- items
- skills
- zones
- quests
- lore

## Exclude

- drafts
- admin notes
- secret quests
- hidden drops
- exact server formulas
- server-only AI
- internal database IDs
- private asset paths
- unreleased areas
- account data
- player data
- moderation data
- raw metrics
- logs
- internal errors

## Compatibility rules

Document:

- supported schema versions
- missing optional fields
- unknown fields
- incompatible versions
- deprecation behavior
- asset URL policy
- generated timestamp
- content version display

## Current milestone restriction

During Phase 0 and Phase 1, create only a placeholder schema and documentation.

Do not implement:

- direct database access
- live private APIs
- automatic exporter execution
- automatic deployment
