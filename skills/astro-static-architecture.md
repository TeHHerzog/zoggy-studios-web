# Astro Static Architecture Skill

## Goal

Maintain two independently deployable static Astro sites with shared packages and separate public identities.

## Expected sites

```text
apps/studio
apps/darkfantasy
```

## Expected outputs

```text
dist/studio
dist/darkfantasy
```

## Rules

- use Astro static output
- avoid server adapters
- avoid persistent Node.js production processes
- keep client-side JavaScript minimal
- use shared packages only for genuinely reusable code
- keep site-specific branding and atmosphere separate
- do not create empty future routes
- do not add a frontend framework without a documented need

## Shared candidates

- page shell
- skip link
- accessible buttons
- spacing tokens
- typography tokens
- focus styles
- footer primitives
- branding access helpers

## Site-specific candidates

- hero sections
- visual textures
- color palettes
- iconography
- promotional language
- game atmosphere
- studio portfolio presentation

## Verification

Confirm:

- each app builds independently
- root build builds both
- output paths are correct
- one site cannot overwrite the other's output
- no source files are copied into public output
- build does not require a production server
