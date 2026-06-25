# Branding

## Public Brand

The public umbrella brand is:

```text
Zoggy Studios
```

Zoggy Studios is broad enough for games, apps, IT and technology projects, software, utilities, books, scripts, art, media, and future creative work.

Dark Fantasy MMO is one current project under the Zoggy Studios umbrella.

## Positioning

The public positioning is intentionally honest and flexible:

```text
A solo-led creative and technology studio for games, apps, stories, and strange new worlds.
```

This avoids locking the brand to one game or pretending the studio already has a large catalog, team, publisher operation, or release pipeline.

## Branding Configuration

The single branding source is:

```text
config/branding.json
```

Current values:

```json
{
  "studioName": "Zoggy Studios",
  "studioShortName": "Zoggy",
  "studioTagline": "Games, technology, and strange new worlds.",
  "gameName": "Dark Fantasy MMO",
  "gameStatus": "Pre-alpha"
}
```

## How To Change Branding

To change the studio name, edit `studioName`.

To change the short name, edit `studioShortName`.

To change the tagline, edit `studioTagline`.

To change the game name, edit `gameName`.

To change the game status, edit `gameStatus`.

After changing branding, run:

```text
npm run check
npm run build
npm run verify
npm run scan:public
```

## Source Brief Note

The original implementation plan may refer to `Zoggy Game Studios`. It is preserved as source context. New public-facing implementation uses `Zoggy Studios`.
