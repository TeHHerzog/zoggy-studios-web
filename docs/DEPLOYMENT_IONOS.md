# IONOS Deployment

This milestone documents a manual deployment process only. Automated deployment is intentionally not implemented.

## Manual Process

1. Install dependencies with `npm install`.
2. Run checks with `npm run check`.
3. Build both sites with `npm run build`.
4. Run local verification with `npm run verify`.
5. Run public-output scanning with `npm run scan:public`.
6. Inspect `dist/studio/` and `dist/darkfantasy/`.
7. Back up the current remote `/games/` directory.
8. Back up the current remote `/darkfantasy/` directory.
9. Upload the contents of `dist/studio/` to `/games/`.
10. Upload the contents of `dist/darkfantasy/` to `/darkfantasy/`.
11. Verify `https://games.herzogit.com/`.
12. Verify `https://darkfantasy.herzogit.com/`.
13. Verify each custom 404 page remotely.
14. Verify each `robots.txt` remotely.
15. Verify directory listing is disabled remotely.
16. Verify no cross-site leakage after upload.
17. Roll back if any verification fails.

## Static Hosting Protection

Each site includes an Apache-compatible `.htaccess` file with:

```apache
Options -Indexes
DirectoryIndex index.html
```

This prepares directory-listing protection where supported by IONOS Apache webspace.

## Do Not Upload

- repository root
- `.git`
- `node_modules`
- `apps/`
- `packages/`
- `docs/`
- `scripts/`
- `config/`
- `schemas/`
- environment files
- credentials
- private MMO files
- build caches

## Manual Checks Still Required

Local verification cannot prove live HTTPS, DNS, IONOS mapping, remote 404 behavior, or remote directory-listing behavior.
