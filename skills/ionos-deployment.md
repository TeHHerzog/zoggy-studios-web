# IONOS Deployment Skill

## Goal

Deploy two static outputs to separate IONOS webspace directories without cross-site leakage.

## Mapping

```text
games.herzogit.com
→ /games/
→ contents of dist/studio/

darkfantasy.herzogit.com
→ /darkfantasy/
→ contents of dist/darkfantasy/
```

## Manual deployment procedure

1. install dependencies
2. run checks
3. build both sites
4. run public-output scan
5. inspect each output directory
6. back up current remote directories
7. upload studio output to `/games/`
8. upload game output to `/darkfantasy/`
9. verify HTTPS
10. verify `index.html`
11. verify custom 404 behavior
12. verify `robots.txt`
13. verify no directory listing
14. verify no cross-site files
15. roll back if any check fails

## Important upload rule

Upload the contents of each output directory, not the `dist` parent itself.

## Apache protection

Where supported:

```apache
Options -Indexes
DirectoryIndex index.html
```

Do not add application-server rewrites.

## Never upload

- `.git`
- `node_modules`
- source directories
- environment files
- credentials
- docs with private content
- private MMO files
- build caches
