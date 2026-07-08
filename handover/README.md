# Project Asset Handover

This folder is a local staging area for raw project assets that should not be committed automatically.

## Supported Dark Fantasy MMO Inputs

Place temporary source files here for review:

- class character images;
- transparent character renders;
- class emblems;
- architecture diagrams;
- screenshots;
- video clips;
- raw stat notes;
- JSON or YAML data exports;
- model preview images;
- press-kit drafts.

## Class Image Naming

- royal_male.png
- royal_female.png
- knight_male.png
- knight_female.png
- elf_male.png
- elf_female.png
- mage_male.png
- mage_female.png
- priest_male.png
- priest_female.png

## Required Seven-Stat Order

1. STR — Strength
2. DEX — Dexterity
3. CON — Constitution
4. INT — Intelligence
5. WIS — Wisdom
6. CHA — Charisma
7. LUK — Luck

Mana is a derived resource and must not replace Charisma or Luck.

## Data Notes

Every supplied stat file should state:

- source;
- date;
- repository commit or content version;
- whether values are canonical, approved direction, proposed, inferred, or legacy;
- whether the data is safe for public release.

## Security

Do not place credentials, database exports containing user data, tokens, production logs, private keys, or unpublished security information in this folder.

## Git Behavior

Everything in this folder is ignored except this README.
