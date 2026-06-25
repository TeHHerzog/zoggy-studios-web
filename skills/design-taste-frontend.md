---
name: design-taste-frontend
description: Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated.
---

# tasteskill: Anti-Slop Frontend Skill

> Landing pages, portfolios, and redesigns. Not dashboards, not data tables, not multi-step product UI.
> Every rule below is **contextual**. None of it fires automatically. First read the brief, then pull only what fits.

## Core Principles for Zoggy Studios

- Each project page should look like it belongs to Zoggy Studios but have its own visual identity.
- Do not copy the exact same layout across all project pages.
- Vary card sizes, image placement, and section rhythm between projects.
- Use the shared header/footer and brand token set, but give each project its own accent palette.
- Avoid generic centered-hero + three-card patterns. Each project needs a distinct compositional approach.
- Real project screenshots and diagrams are preferred over placeholder images.
- Maintain the honest, solo-led tone: show real progress, not fake polish.

## Current Site Configuration

```
DESIGN_VARIANCE: 8
MOTION_INTENSITY: 4
VISUAL_DENSITY: 4
```

Studio site uses warm light surfaces (#fff7ed family), ink text (#111827), blue accent (#2563eb), card borders (rgba(17,24,39,0.12)), and soft background gradients.

## Project Page Rules

- Each project page starts with a hero that sets a unique atmosphere.
- At least one visual asset per project: screenshot, diagram, artwork, or code block.
- Avoid creating fake screenshots. Use real ones or skip the image slot.
- Status badges should be honest: "Active development", "Internal tool", "Prototype", "Exploring".
- Keep private game data out of public pages. Use redacted examples or simplified YAML excerpts.
- Honor the public/private boundary. Do not expose server URLs, credentials, or internal paths.
