# Verification and Reporting Skill

## Goal

Produce evidence-based reports that distinguish completed, failed, and unverified work.

## Commands

Use repository-defined commands. Expected examples:

```text
npm install
npm run check
npm run build
npm run verify
npm run scan:public
```

## For every command report

- exact command
- working directory
- result
- relevant output
- failure reason
- remaining impact

## Result labels

Use:

```text
PASS
FAIL
NOT RUN
BLOCKED
MANUAL CHECK REQUIRED
```

Do not use `PASS` for checks inferred from code review alone.

## Final report structure

1. objective
2. initial repository state
3. architecture implemented
4. files added
5. files modified
6. files preserved
7. commands run
8. command results
9. tests
10. generated outputs
11. security checks
12. local deployment checks
13. remote checks still required
14. unverified items
15. known risks
16. rollback
17. recommended next milestone

## Honesty rule

Never claim:

- live DNS works
- HTTPS works
- IONOS mapping works
- a remote 404 works
- directory listing is disabled remotely

unless those checks were actually performed.
