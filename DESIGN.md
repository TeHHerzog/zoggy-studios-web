# Zoggy Studios Web Design System

## Purpose

This file records the small Phase 1 design system for the public Zoggy Studios web platform. It exists before UI implementation so placeholder pages use intentional tokens instead of one-off visual choices.

## Brand Model

Zoggy Studios is the umbrella brand. It can support games, apps, IT and technology projects, software, utilities, art, books, scripts, media, and future creative work.

Dark Fantasy MMO is one project under that umbrella. It has its own visual atmosphere and must not consume the whole studio identity.

## Shared Foundations

- Static, fast, readable pages.
- One clear `h1` per page.
- Semantic header, main, and footer landmarks.
- Skip-to-content link on every page.
- Visible focus rings for keyboard users.
- Fluid type and spacing for 320px through desktop widths.
- No hover-only interactions.
- No autoplay media.
- Motion must respect `prefers-reduced-motion`.

## Shared Tokens

```css
--font-sans: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
--font-display: "Trebuchet MS", Inter, ui-sans-serif, system-ui, sans-serif;
--space-page: clamp(1rem, 4vw, 4rem);
--space-section: clamp(3rem, 8vw, 7rem);
--radius-card: 1.25rem;
--focus-ring: 0 0 0 3px;
```

## Studio Site Direction

- Clean, friendly, memorable, creative, and professional.
- Use warm light surfaces, ink text, and lively but controlled accent colors.
- Feel like a flexible home base, not only a game landing page.
- Mention current and future focus areas without faking a finished portfolio.
- Avoid dark fantasy dominance.
- Make it clear that the studio is solo-led and early.

## Dark Fantasy Site Direction

- Ancient, corrupted, vibrant, cosmic, unsettling, and grungy.
- Use dark surfaces, ember/violet/cyan accents, rough borders, and atmospheric gradients.
- Keep text readable before decoration.
- Do not use private game assets or unreleased content.

## Component Scope

Phase 1 only needs a page shell, skip link, cards, call-to-action links, footer treatment, and error-page structure. Do not build a large design system yet.
