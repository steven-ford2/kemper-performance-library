# New Performances 38–48 — Codex index

**Status:** proposed, not installed. 11 five-slot Performances, 55 Rigs.

These append to existing 06–37; proposed numbers must be remapped if occupied on the connected Kemper.

| Number | Artist / theme | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 |
|---:|---|---|---|---|---|---|
| 38 | VAI GILBERT BECKER | VAI FTLOG | VAI TENDER | GILBERT GOY | GILBERT SILENCE | BECKER ALTIT |
| 39 | VAN HALEN | VH1 BROWN | VH2 WOMEN | VH FAIR | VH PANAMA | VH 5150 ERA |
| 40 | TIMMONS GOVAN | ELECTRIC GYPSY | GYPSY CLEAN | GOVAN WAVES | GOVAN FIVES | GOVAN ARISTOCRATS |
| 41 | EAGLES | HOTEL 12STR | HOTEL FELDER | HOTEL WALSH | FAST LANE | EAGLES CLEAN |
| 42 | POLYPHIA | POLY GOAT | PLAYING GOD | 40OZ CHAMPAGNE | OD EGO LEAD | CHIMERA HEAVY |
| 43 | ERIC JOHNSON | CLIFFS STUDIO | CLIFFS LIVE | EJ CLEAN STEREO | EJ DIRTY RHTHM | EJ FUZZ LEAD |
| 44 | JEFF BECK | CAUSE LOVERS | FREEWAY JAM | LED BOOTS | WHERE WERE YOU | NADIA / LATE |
| 45 | YNGWIE MALMSTEEN | BLACK STAR CLEAN | RISING FORCE | FAR BEYOND | TRILOGY ODYSSEY | MODERN YJM |
| 46 | FLEETWOOD RUMOURS | DREAMS CLEAN | GO YOUR WAY | THE CHAIN OUTRO | NEVER GOING | GOLD DUST |
| 47 | METALCORE | ATR SIX | ATR LEAD | KSE DIRTY | KSE CLEAN | AILD 6505 |
| 48 | EAGLES EARLY | NIGHTS RHYTHM | NIGHTS FELDER | NIGHTS HARMONY | WITCHY RIFF | WITCHY SOLO |

## Agent implementation sequence

1. Run `python scripts/validate.py`; inspect the registry and `AGENTS.md`.
2. Inventory profile captures and factory effect types. Do not assume every brand capture or factory preset exists.
3. Export backups, inspect and get approval for any occupied or remapped Performance destination.
4. Build one Rig and read it back; only then apply full Performance.
5. If acoustic or nylon instrument needed, report that requirement rather than silently applying distorted electric amp.
6. For unsupported multivoicer, talk box, external studio overdubs, do not claim exact recreation. Log substitutions.
7. Save each Performance, switch away, reload, validate all eight effect modules and all four Remote mappings.

## Highest-priority authenticity checks

- **Van Halen:** Peavey 5150 did not exist for the *5150* (1986) record; it debuted in 1992.
- **Fleetwood Mac:** *Rumours* used boosted Stratocaster into Hiwatt; Turner Model 1 came later.
- **Eagles:** the Hotel California introduction includes an actual twelve-string acoustic plus Echoplex and Leslie; Walsh and Felder leads have different instruments and amps.
- **Polyphia:** nylon guitar sound needs nylon instrument; Kemper cannot host the Neural DSP plugin as a Kemper effect.
- **Jeff Beck:** the original studio recording of Cause We’ve Ended as Lovers used Seymour Duncan Tele-Gib.
- **Yngwie:** DOD 250-like boost into vintage Marshall, generally dry leads; not generic high-gain modern metal.
- **Metalcore:** 5150/6505+V30 with low-drive OD808 tightener, carefully set noise gate, high-pass filters; match tuning separately.

## Individual specifications

- [VAI GILBERT BECKER](artists/shred-triad.md) and [`specs/shred-triad.json`](../specs/shred-triad.json)
- [VAN HALEN](artists/van-halen.md) and [`specs/van-halen.json`](../specs/van-halen.json)
- [TIMMONS GOVAN](artists/timmons-govan.md) and [`specs/timmons-govan.json`](../specs/timmons-govan.json)
- [EAGLES](artists/eagles.md) and [`specs/eagles.json`](../specs/eagles.json)
- [POLYPHIA](artists/polyphia.md) and [`specs/polyphia.json`](../specs/polyphia.json)
- [ERIC JOHNSON](artists/eric-johnson.md) and [`specs/eric-johnson.json`](../specs/eric-johnson.json)
- [JEFF BECK](artists/jeff-beck.md) and [`specs/jeff-beck.json`](../specs/jeff-beck.json)
- [YNGWIE MALMSTEEN](artists/yngwie.md) and [`specs/yngwie.json`](../specs/yngwie.json)
- [FLEETWOOD RUMOURS](artists/fleetwood-rumours.md) and [`specs/fleetwood-rumours.json`](../specs/fleetwood-rumours.json)
- [METALCORE](artists/metalcore.md) and [`specs/metalcore.json`](../specs/metalcore.json)

- [EAGLES EARLY](artists/eagles-early.md) and [`specs/eagles-early.json`](../specs/eagles-early.json)
