# IONOS Deployment

This milestone documents a manual deployment process only. Automated deployment is intentionally not implemented.

## Access Methods

IONOS provides two different access paths that are useful for this project.

The Hosting API can manage hosting-related services such as DNS, domains, and SSL where supported by the API. The API key is passed in the `X-API-Key` header. It does not appear to provide a simple static webspace file-upload endpoint for this shared hosting setup.

SFTP/SSH is the practical deployment path for generated static files. Use it to upload the contents of `dist/studio/` to the `/games/` webspace directory.

## IONOS SSH Account Rule

IONOS SSH access is tied to the SSH user or main FTP user. Extra SFTP accounts can transfer files, but they do not include SSH shell access.

For this project, use the main SFTP/SSH user for SSH setup and key-based deploy:

```text
u80057117
```

Do not use the SFTP-only account for `npm run ionos:ssh:install-key`, because it cannot open an SSH shell.

## Local Secret File

Local deployment settings may be stored in:

```text
.env.deploy.local
```

This file is ignored by git through the `.env.*` rule. Do not commit it. Do not paste its contents into documentation or commits.

Expected local values:

```text
IONOS_API_KEY=publicprefix.secret
IONOS_SFTP_HOST=home565324678.1and1-data.host
IONOS_SFTP_PORT=22
IONOS_SFTP_USER=u80057117
IONOS_REMOTE_DIR=/games/
IONOS_SFTP_KEY=C:\Users\Zog\.ssh\zoggy_studios_ionos_ed25519
```

The API key can be tested with:

```text
npm run ionos:api:check
```

This confirms API access only. It does not upload files.

## SSH Key Setup

Create or keep a local SSH key outside the repository. The current expected key path is:

```text
C:\Users\Zog\.ssh\zoggy_studios_ionos_ed25519
```

If IONOS provides a UI field for SSH public keys, add the `.pub` file contents there.

If IONOS requires one password-based SSH login first, run:

```text
npm run ionos:ssh:install-key
```

That helper reads `.env.deploy.local`, connects with SSH, and appends the local public key to `~/.ssh/authorized_keys` on the webspace. It may prompt for the IONOS SFTP/SSH password in your local terminal. Do not save that password in the repository.

After key setup, test key login manually:

```text
ssh -i C:\Users\Zog\.ssh\zoggy_studios_ionos_ed25519 -p 22 u80057117@home565324678.1and1-data.host
```

## Local Studio Upload Command

After building and verifying, upload the studio site with:

```text
npm run deploy:studio
```

The upload command uses `sftp.exe` and the key path from `.env.deploy.local`.

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
