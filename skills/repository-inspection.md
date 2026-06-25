# Repository Inspection Skill

## Use this skill when

- starting work in the repository
- planning structural changes
- validating an existing implementation
- reviewing another agent's changes

## Procedure

1. Identify the current working directory.
2. List the repository root.
3. Check for:
   - `.git`
   - `package.json`
   - lockfiles
   - Astro configuration
   - workspace configuration
   - existing `apps/`
   - existing `packages/`
   - `README.md`
   - `AGENTS.md`
   - implementation plan
4. Run `git status` if Git exists.
5. Identify the current branch and remotes.
6. Inspect scripts in the root `package.json`.
7. Separate findings into:
   - verified existing paths
   - proposed paths
8. Do not alter files until inspection is complete.

## Reporting format

```text
Verified current state
Existing framework
Existing package manager
Existing build commands
Existing output paths
Existing risks
Proposed changes
Unverified assumptions
```

Do not say the repository is empty unless it was actually inspected.
