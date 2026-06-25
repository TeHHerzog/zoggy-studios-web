# Security Boundary Review Skill

## Goal

Prevent accidental publication of private MMO systems, data, assets, or operational information.

## Prohibited output

Search source and generated output for:

```text
/admin/
127.0.0.1:9090
PostgreSQL
DATABASE_URL
password
secret
token
private key
player data
moderation
goroutine
process ID
memory usage
internal error
```

The search terms are indicators, not proof. Review context before reporting.

## Required review areas

- public/private repository separation
- environment files
- credentials
- local machine paths
- source maps
- private asset paths
- internal identifiers
- draft content
- secret quests
- raw logs
- health endpoints
- cross-site leakage
- directory listing
- deployment allowlist

## Deployment allowlist principle

Only deploy files generated under:

```text
dist/studio/
dist/darkfantasy/
```

Never deploy repository roots.

## Response to a violation

1. stop deployment
2. identify the exposed file or reference
3. remove it from generated output
4. determine whether the secret was committed
5. recommend credential rotation if exposure is possible
6. document the incident honestly
