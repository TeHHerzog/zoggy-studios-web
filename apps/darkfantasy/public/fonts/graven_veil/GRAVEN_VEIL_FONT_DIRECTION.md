# Graven Veil Display — Custom Font Direction

**Status:** Proposed first-pass display alphabet for the dark fantasy MMO project. The name is a working font-family name, not a canonical game title.

## Design conclusion

The project needs a custom **display face**, not a custom body-text face. Its visual identity combines old-school isometric MMORPG readability, occult dark fantasy, cosmic corruption, grotesque organic horror, clean modern silhouette control, and sharp high-contrast presentation. The font therefore uses a narrow Roman-capital skeleton, wedge serifs, low crossbars, angular bowls, and one restrained diagonal “ritual scar” per glyph.

The scar is colored in the concept sheet only to show the system. In a production font it should become a monochrome cutout or an optional alternate glyph. This keeps the face usable in bone, iron, blood, toxic, spectral, or violet UI themes without embedding color into the font.

## Intended hierarchy

| UI role | Typeface choice | Minimum size | Notes |
|---|---|---:|---|
| Game logo / expansion title | Graven Veil Display | 72 px | Custom spacing and manual kerning |
| Zone and dungeon names | Graven Veil Display | 48 px | Brief, centered, all caps |
| Boss introductions | Graven Veil Display | 42 px | Keep effects outside the glyph shapes |
| Codex and inventory section headers | Graven Veil Display | 30 px | Avoid long strings |
| Buttons and tabs | Readable companion sans/serif | 18–22 px | Do not use the display face by default |
| Quest text, chat, item descriptions | Readable companion font | 16–20 px | Never use Graven Veil for paragraphs |

## Visual rules

1. Preserve recognizable Latin letterforms before adding horror details.
2. Keep distress structural: cuts, wedges, asymmetry, and sharp joins. Do not use random grunge texture inside every glyph.
3. Use the same baseline and cap height across the set so menu alignment remains stable.
4. Keep counters open in B, D, O, P, Q, and R for readability over dark scenes.
5. Use the most corrupted alternates only for bosses, cursed items, or event titles.
6. Maintain monochrome master outlines. Glow, outline, shadow, and color belong to the Godot theme or material, not baked into the font.

## Project palette application

- Bone text: `#D8D0B4`
- Near-black background: `#0B0D0C`
- Toxic/fungal accent: `#A3C113`
- Cursed/psychic violet: `#8A5AC2`
- Blood/ritual red: `#A33232`
- Spectral/frost blue: `#6FA6B8`

## Godot 4.7 production target

When the vectors are converted into a real OpenType font, import the `.otf` or `.ttf` as a `FontFile`. Use normal dynamic rendering for small UI text. Use MSDF primarily for large headings that scale, rotate, appear in world-space, or require outlines. Test at 24, 30, 42, 48, 72, and 96 px at 100%, 125%, 150%, and 200% UI scale.

Suggested project paths are **proposed** until the repository is inspected:

```text
client/assets/fonts/graven_veil/
  graven_veil_display.otf
  graven_veil_license.txt
  graven_veil_specimen.png
  graven_veil_source.svg

client/ui/themes/
  dark_fantasy_theme.tres
```

## Acceptance checklist for the compiled version

- Uppercase A–Z, numerals, core punctuation, currency, percent, plus/minus, brackets, apostrophes, quotation marks.
- Latin accented capitals for names and localization.
- Kerning pairs: AV, VA, WA, TA, TO, YO, RO, LA, LY, PA, VE, and punctuation pairs.
- No overlapping contours if MSDF will be used.
- Consistent advance widths and no clipping with 8 px outlines at the largest intended size.
- Legible against terrain, fog, particle effects, and saturated monster accents.
- Fallback font configured for unsupported Unicode, CJK, symbols, and emoji.

## Files in this concept pack

- `graven_veil_concept_sheet.svg` — editable vector specimen and glyph board.
- `graven_veil_concept_sheet.png` — quick visual preview.
- `graven_veil_wordmark.svg` — isolated editable wordmark.
- `graven_veil_metrics.json` — starter metrics and production targets.

## Next production pass

Convert every stroke into closed monochrome contours, replace the colored scars with true cutouts, normalize optical weight, add manual kerning, and test the alphabet inside actual Godot menus before compiling the final font.
