# Kemper Tone Library — agent-ready Performance specifications

A structured, **non-destructive** blueprint for programming Kemper Profiler MK2 + Kemper Remote in Rig Manager. Consolidated from artist-specific discussions into one collision-free candidate map suitable for Codex and computer control.

**Status as of 2026-11-07: proposed, not installed, source profiles not inventoried, audio not calibrated.** The instructions here are designs for Codex and Rig Manager, not actual programmed device settings.

## Included

- **48 candidate Performances, 240 five-slot Rigs**, across the original five artists (32 Performances), plus 11 single-bank artist/theme additions and five Favorites Performances.
- **Remaining expansion targets**, including Matt Schofield, Robin Trower, Greg Howe, Slash, Gilmour and more. These are explicitly marked as **planning only**.
- An **optional original five-song Continuum bank** (`specs/mayer-continuum-five-song-legacy.json`) preserves the exact song grouping first requested: Don't Trust Myself, Vultures, Gravity, Slow Dancing, Crossroads NG-2. It is not assigned an extra live bank number.
- Full original John Mayer JSON + playbook are preserved in `archive/` and normalized into `specs/mayer.json`.
- Other artist specifications were reconstructed from conversation plans and publicly described rig families. Exact original machine-readable source archives were unavailable. All such rows are flagged.
- `AGENTS.md` — instructions Codex should follow first.
- `data/performance_registry.json` — collision-free candidate locations, which must be remapped if occupied.
- `docs/procedures/build-and-verify.md` — backup, inventory, edit, audition and restore protocol.
- `scripts/validate.py` — specification and remote-assignments validator.

## Crucial distinctions

**This is not a commercial Kemper profile pack and not a native `.kipr`/`.kperform` export.** It contains source-profile *selection criteria*, effect types/preset candidates, parameters, initial states and Remote I–IIII assignments. It contains no proprietary Sinewave/Tone Junkie profile binaries, commercial pack samples, or redistributed presets. The operator must have legitimate copies on the computer.

A Rig Manager agent must inspect source captures and software capabilities, perform backup, and apply these instructions to the user's actual connected profiler. No undocumented Kemper or Rig Manager API is assumed. Some multi-amp recorded tones and studio overdubs require approximations.

## Candidate bank map

| Range | Artist | Performances | Slots |
|---|---|---:|---:|
| 01–05 | Favorites: mixed-artist quick access | 5 | 25 |
| 06–12 | John Mayer | 7 | 35 |
| 13–17 | Jimi Hendrix | 5 | 25 |
| 18–25 | Stevie Ray Vaughan | 8 | 40 |
| 26–31 | Eric Clapton | 6 | 30 |
| 32–37 | Robben Ford | 6 | 30 |
| 38 | Vai / Gilbert / Becker | 1 | 5 |
| 39 | Van Halen | 1 | 5 |
| 40 | Timmons / Govan | 1 | 5 |
| 41 | Eagles | 1 | 5 |
| 42 | Polyphia | 1 | 5 |
| 43 | Eric Johnson | 1 | 5 |
| 44 | Jeff Beck | 1 | 5 |
| 45 | Yngwie Malmsteen | 1 | 5 |
| 46 | Fleetwood Mac — *Rumours* | 1 | 5 |
| 47 | Metalcore (ATR/KSE/AILD) | 1 | 5 |
| 48 | Eagles — One of These Nights / Witchy Woman | 1 | 5 |

These locations are only candidates; earlier chats reused numbers such as 07–12 for several artists. **Never overwrite an occupied Performance**. See `data/performance_registry.json`.

## Start Codex

1. Read `AGENTS.md`, `docs/agent-handoff.md`, and `docs/procedures/build-and-verify.md`.
2. Run `python scripts/validate.py` from this repository. It does not touch the Kemper.
3. Inspect the connected Rig Manager, make two backups, and inventory profiles + Performance occupancy.
4. Select one pilot bank: Mayer Continuum or Hendrix Core. Do not build remaining Rigs before confirming switch assignments and audible quality.
5. Proceed by artist only after pilot verification and an explicit write go-ahead.

## GitHub repository

The intended repository is `steven-ford2/kemper-performance-library`. The GitHub connector may publish commits to the repository; confirm the current remote branch and permissions before any future push. **Never force-push or overwrite existing content.**

## Favorites first

Five full-copy Favorites banks occupy **01–05**, followed by the entire original artist library **06–48**. See [Favorites mapping](docs/favorites.md), [JSON specs](specs/favorites.json), and [source provenance](data/favorites_source_map.json). They have not been installed on the Profiler.

## Artist docs

- [`John Mayer`](docs/artists/mayer.md)
- [`Jimi Hendrix`](docs/artists/hendrix.md)
- [`Stevie Ray Vaughan`](docs/artists/srv.md)
- [`Eric Clapton`](docs/artists/clapton.md)
- [`Robben Ford`](docs/artists/robben-ford.md)

## Newly specified artist Performances

All eleven additions have individual guides and per-Rig machine-readable settings in `specs/`. See [`docs/new-performances.md`](docs/new-performances.md). Distinct source profiles and real instrument types are essential for Eagles 12-string, Polyphia nylon-string and Fleetwood acoustic. These are **proposed**, not installed or tone-tested.

## Sources / confidence

The core source-document links and evidence grades are in `docs/research/sources-and-uncertainties.md`. Effects and gear specifics are **targets** until checked against current installed Kemper OS and played/recorded. No claim of exact recording recreation is made.

### Eagles — early studio supplement

- [One of These Nights / Witchy Woman detailed plan](docs/artists/eagles-early.md) and [`specs/eagles-early.json`](specs/eagles-early.json).
