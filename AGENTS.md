# AGENTS.md

## Purpose

This file defines the permanent operating rules for AI agents working in the Zoggy Studios public web repository.

Zoggy Studios is the umbrella brand for current and future public projects, including games, technology, IT projects, software, utilities, art, books, media, and other creative work.

The current implementation focus is:

- the Zoggy Studios public website
- the public Dark Fantasy MMO website
- Phase 0 and Phase 1 of the implementation plan unless the user explicitly expands scope

Agents must read this file before planning, editing, testing, committing, or reporting work.

---

## Primary Project Brief

The primary architectural brief is:

```text
ZOGGY_GAME_STUDIOS_WEB_IMPLEMENTATION_PLAN.md
```

Read it before making substantial changes.

The brief may contain the older working name `Zoggy Game Studios`. For all new public-facing work, use:

```text
STUDIO_NAME=Zoggy Studios
STUDIO_SHORT_NAME=Zoggy
GAME_NAME=Dark Fantasy MMO
GAME_STATUS=Pre-alpha
```

Do not delete or silently rewrite the original implementation plan. Record branding changes in project documentation.

When instructions conflict, use this priority order:

1. the user's current explicit request
2. this `AGENTS.md`
3. the implementation plan
4. repository documentation
5. existing code conventions
6. agent assumptions

Stop and report any conflict that would weaken security, violate repository boundaries, or overwrite working systems.

---

## Repository Purpose

This repository owns only the public Zoggy Studios web platform.

Expected public sites:

```text
games.herzogit.com
darkfantasy.herzogit.com
```

### Zoggy Studios site

Domain:

```text
games.herzogit.com
```

Responsibilities:

- Zoggy Studios identity
- games portfolio
- technology and IT projects
- public development news
- media
- contact information
- links to individual projects
- future expansion into software, art, books, and media

### Dark Fantasy MMO site

Domain:

```text
darkfantasy.herzogit.com
```

Responsibilities:

- game landing page
- public game information
- public news and devlogs
- public roadmap
- selected lore
- classes
- monsters
- zones
- media
- alpha information
- public wiki later
- sanitized public status later

---

## Mandatory Public and Private Boundary

The public web repository must remain separate from the private Dark Fantasy MMO repository.

The private MMO repository remains authoritative for:

- Godot client code
- Go game server code
- PostgreSQL persistence
- canonical game content
- content validation
- server-authoritative formulas
- the Go Admin Panel
- private administration
- private logs and metrics
- account and player data
- moderation systems
- public-content export generation

The public website must never connect directly to private MMO systems.

### Never connect to or expose

- PostgreSQL
- database credentials
- `DATABASE_URL`
- private admin endpoints
- the Go Admin Panel
- `http://127.0.0.1:9090/admin/panel`
- private health APIs
- process IDs
- memory usage
- goroutine counts
- raw operational metrics
- internal errors
- logs
- player or account data
- moderation data
- secret quests
- unreleased content
- internal database identifiers
- server-authoritative formulas
- private asset paths
- environment files
- credentials
- secrets

### Allowed future integration

The public site may consume only a versioned, sanitized, approved public-content bundle.

Expected flow:

```text
Private MMO repository
→ validate content
→ approve public release
→ generate sanitized bundle
→ validate public schema
→ copy approved bundle into web repository
→ build static pages
→ deploy only generated public output
```

Do not implement direct database access, private API calls, or automatic bundle generation in this repository.

---

## Current Scope

Unless the user explicitly expands scope, work only on Phase 0 and Phase 1.

### Phase 0

- repository foundation
- architecture documentation
- security boundaries
- configurable branding
- domain mapping
- IONOS deployment documentation
- agent instructions
- content contract placeholder

### Phase 1

- two minimal static placeholder sites
- responsive rendering
- construction-phase `robots.txt`
- custom 404 pages
- directory-listing prevention
- build verification
- output scanning
- HTTPS and deployment verification documentation

### Out of scope

Do not build:

- account registration
- login
- password reset
- player portals
- database integration
- public API services
- complete wiki
- automated deployment
- private admin integration
- content authoring tools
- MMO server features
- Godot features
- moderation tools
- live operational dashboards

---

## Technical Direction

Preferred architecture:

```text
Astro
npm workspaces
static output
```

Expected repository structure:

```text
apps/
  studio/
  darkfantasy/

packages/
  ui/
  branding/
  public-content-contract/

config/
schemas/
scripts/
docs/
skills/

dist/
  studio/
  darkfantasy/
```

Expected build outputs:

```text
dist/studio/
dist/darkfantasy/
```

Do not require a persistent Node.js server in production.

Do not add React, Vue, Svelte, Next.js, a CMS, Docker, Kubernetes, or server-side application logic unless the user explicitly approves it and the need is documented.

Prefer minimal client-side JavaScript.

---

## Branding Rules

Use one shared branding source.

Recommended values:

```json
{
  "studioName": "Zoggy Studios",
  "studioShortName": "Zoggy",
  "studioTagline": "Games, technology, and strange new worlds.",
  "gameName": "Dark Fantasy MMO",
  "gameStatus": "Pre-alpha"
}
```

Do not hardcode temporary names throughout templates.

### Studio visual direction

- clean
- friendly
- memorable
- playful but professional
- flexible for games and technology
- adaptable to future art, books, and media

### Dark Fantasy visual direction

- ancient
- corrupted
- vibrant
- cosmic
- unsettling
- grungy
- influenced by old-school Korean MMORPG presentation

Readability, accessibility, performance, and navigation clarity are more important than decoration.

---

## Required Working Method

Before recommending or making repository changes:

1. inspect the repository
2. identify existing files and working systems
3. separate verified existing paths from proposed paths
4. read the implementation plan
5. check for existing package manager and framework choices
6. preserve working code unless replacement is justified
7. identify security risks
8. state assumptions clearly

Do not claim that a file exists, a command passed, a site builds, or deployment works unless verified.

Do not use destructive Git commands.

Never use:

```text
git reset --hard
git clean -fd
git push --force
```

Do not delete unknown files or directories.

If the working directory contains an unrelated project, stop and report the conflict before restructuring it.

---

## Skills

Use the relevant skill files in `skills/` before performing specialized work.

Available skills:

```text
skills/repository-inspection.md
skills/astro-static-architecture.md
skills/ui-accessibility.md
skills/security-boundary-review.md
skills/public-content-contract.md
skills/ionos-deployment.md
skills/verification-reporting.md
skills/design-taste-frontend.md
skills/high-end-visual-design.md
skills/brandkit-skill.md
```

Design guidance skills (`design-taste-frontend.md`, `high-end-visual-design.md`, `brandkit-skill.md`) are sourced from the leonxlnx/taste-skill project. Use them when building or refining public-facing pages to ensure layouts, typography, spacing, and visual variety avoid generic AI defaults.

For a task that spans multiple areas, read all applicable skill files.

Skill files are guidance, not permission to exceed the user's requested scope.

---

## Build and Verification Expectations

Root commands should remain simple and documented.

Recommended commands:

```text
npm install
npm run dev:studio
npm run dev:darkfantasy
npm run check
npm run build
npm run verify
npm run scan:public
```

Exact names may differ, but the root build must build both sites.

Verification should confirm:

- `dist/studio/` exists
- `dist/darkfantasy/` exists
- each site contains `index.html`
- each site contains `404.html`
- each site contains `robots.txt`
- each site includes directory-listing protection when supported
- no environment files are present
- no credentials are present
- no source directories are copied into `dist`
- no links reference private admin routes
- no output references `127.0.0.1:9090`
- no output references PostgreSQL or `DATABASE_URL`
- no private MMO repository paths appear in public output

Do not report a command as passing unless it completed successfully.

If a command cannot run, report:

- the exact command
- the exact error
- the missing dependency or blocker
- what remains unverified

---

## Accessibility Requirements

At minimum:

- one clear `h1` per page
- semantic landmarks
- skip-to-content link
- keyboard-visible focus
- meaningful link text
- sufficient text contrast
- responsive text sizing
- correct language attribute
- reduced-motion support
- useful image alt text
- no hover-only interactions
- no autoplay audio or video
- no clickable non-semantic `div` elements

Do not claim formal WCAG certification unless a formal audit was performed.

---

## Responsive Requirements

Check approximately:

```text
320px
375px
768px
1024px
1440px
```

Pages must not:

- overflow horizontally
- crop essential text
- hide keyboard focus
- use unreadably small text
- depend on hover
- break when text wraps

---

## Static Hosting and IONOS Rules

Expected mappings:

```text
games.herzogit.com
→ /games/
→ contents of dist/studio/

darkfantasy.herzogit.com
→ /darkfantasy/
→ contents of dist/darkfantasy/
```

Upload the contents of each output directory, not the parent `dist` directory.

Deploy only generated public files.

Never deploy:

- repository roots
- source code
- `.git`
- `node_modules`
- environment files
- docs containing private details
- private content bundles
- SSH keys
- CI secrets
- build caches
- private game assets

Prepare Apache-compatible directory-listing protection where supported:

```apache
Options -Indexes
DirectoryIndex index.html
```

Do not add rewrite rules that assume a persistent application server.

---

## Robots Rules

During private construction, both sites must contain:

```text
User-agent: *
Disallow: /
```

Do not remove the block until the user explicitly approves public indexing.

---

## Security Review Requirements

Every implementation round must check for:

- private admin links
- direct database references
- local machine paths
- secrets
- environment files
- source maps
- private asset paths
- raw operational metrics
- internal identifiers
- cross-site file leakage
- directory listing
- accidental repository-root deployment
- exposure of draft or secret game content

Security findings must be reported even when they are outside the current requested feature.

Do not silently fix unrelated private systems from this repository.

---

## Documentation Requirements

Keep these documents current when relevant:

```text
README.md
docs/ARCHITECTURE.md
docs/BRANDING.md
docs/CONTENT_INTEGRATION.md
docs/DEPLOYMENT_IONOS.md
docs/DOMAIN_MAPPING.md
docs/SECURITY.md
docs/ROLLBACK.md
```

Documentation must distinguish:

- verified current behavior
- proposed future behavior
- manual steps
- automated steps
- completed work
- unverified work

---

## Git Rules

Before editing:

- inspect `git status`
- inspect current branch
- inspect existing remotes
- avoid overwriting uncommitted work
- preserve user-created files

Do not:

- create or change a remote without permission
- push without permission
- force-push
- rewrite shared history
- commit secrets
- commit build caches
- commit `node_modules`

Use small, focused commits when authorized.

Recommended commit style:

```text
feat(studio): add placeholder landing page
feat(darkfantasy): add pre-alpha placeholder
docs(security): document public/private boundary
chore(build): add static output verification
```

---

## Final Report Requirements

Every implementation agent must report:

1. objective
2. verified initial state
3. verified existing paths
4. proposed paths
5. files added
6. files modified
7. files preserved
8. commands run
9. command results
10. tests run
11. build outputs
12. security checks
13. deployment checks completed
14. deployment checks not completed
15. anything unverified
16. known risks
17. rollback considerations
18. recommended next milestone

Do not fabricate results.

Do not claim live HTTPS, DNS, IONOS mapping, or remote 404 behavior unless actually tested.

---

## Stop Conditions

Stop and ask for direction when:

- the repository contains an unrelated existing application
- the requested change would expose private MMO systems
- a task requires credentials not provided
- a task requires destructive Git history changes
- a task would exceed the approved milestone
- an existing working system would need replacement without clear justification
- private or secret content is discovered in a public output path
- the requested design creates an accessibility or security regression

When stopping, explain:

- what was found
- why it is risky
- the safest recommended next action

---

## Current Recommended Milestone

Unless explicitly changed by the user:

```text
Phase 0 and Phase 1 only
```

After Phase 0 and Phase 1 are verified, recommend Phase 2 for approval.

Do not begin Phase 2 automatically.

---

## Client Work / Portfolio Projects

The `/work/` page at `apps/studio/src/pages/work.astro` lists client and commissioned projects.

### Adding a client project

Add a new `<article>` inside the `Delivered work` section's `wide-grid` div.

Required fields:

```astro
<article class="card project-card">
  <span class="status-pill">Live</span>
  <h3>Client or Project Name</h3>
  <p>What was built, the tech used, and what the project involved. Keep it professional and factual.</p>
  <a class="button button-secondary" href="https://live-site-url.com">Visit site</a>
</article>
```

Status pill options: `Live`, `In development`, `Launched`, `Maintained`, `Archived`.

Rules:

- Only list projects you actually built or substantially contributed to.
- Link only to public, live sites or public repositories. Do not link to private admin panels.
- Do not expose client credentials, API keys, database details, or private infrastructure.
- If a client project is under NDA or not public, use a generic description without revealing the client identity.
- Run `npm run build && npm run verify && npm run scan:public` after adding a project.
- Run `npm run deploy:studio` to upload after build verification passes.
