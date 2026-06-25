# Rollback

## Keep Previous Known-Good Output

Before uploading new files to IONOS, download or copy the current remote `/games/` and `/darkfantasy/` directories into a dated backup location outside the deploy target.

## Restore Remote Directories

If verification fails after upload:

1. Stop further uploads.
2. Remove the failed uploaded files from the affected remote directory.
3. Restore the previous known-good files to that same remote directory.
4. Re-check the domain over HTTPS.
5. Re-check `robots.txt`.
6. Re-check custom 404 behavior.
7. Re-check directory listing behavior.

## Source And Output Consistency

Do not roll back remote output while continuing to describe the failed build as deployed. Record which source revision or local build produced the deployed output.

## Local Rebuild Rollback

If a local build is bad, keep the generated `dist/` output out of deployment. Fix source, rebuild, and rerun verification before upload.
