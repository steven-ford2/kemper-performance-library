# Codex / computer-control agent operating contract

Read before ANY GUI changes. The user wants **tone fidelity and fast usable sound**, not a lecture on how to play songs. Treat all configuration values as proposed starts until actual amp captures and rig libraries are inventoried.

## Absolute safety requirements

1. **Never overwrite any existing user Rig/Performance or preset** without a reliable export/backup and an explicit recorded choice. The proposed 01–48 numbers may be occupied.
2. Before editing, inventory: profiler exact model and serial-independent identifier, Profiler OS, Rig Manager version, connected path, available amp profile names/gain/cabinets, preset availability, Remote firmware and expression pedal mappings.
3. Make BOTH (a) entire Profiler content backup and (b) separate Rig Manager Local Library/selected Rigs export. Check that backup files exist and are nonempty. Preserve originals unmodified.
4. Do not modify system-wide Output, input sensitivity, global pedal/volume routing, firmware, or Kemper Kabinet/Kone parameters without separate user confirmation and a recovery plan.
5. Never automatically download or purchase paid commercial Rig Packs. The owned Sinewave Continuum OD and Tone Junkie free profile may be used from local legitimate copies. Never commit pack binaries into this repo.
6. If Rig Manager controls cannot be accessed, do not fake progress; produce an exact click-list and list blockers.
7. Do not claim a tone is "exact" or historically verified when profile source, speaker, pickup or multi-amp signal chain is unknown.
8. Use UI-visible effects and parameter names; **do not assume unsupported Rig Manager API, MIDI write capability or native file format**. Correct any spec target whose named control is absent; log deviations.
9. Save each Rig / Performance to the intended location, switch away, then reload and verify state was persisted.
10. Dry-run first, then pilot Performance, then scale in batches after user authorization. Stop and request permission for irreversible actions.

## Required workflow

- **Phase 0 — preflight:** `python scripts/validate.py`. Read registry and exact priority. Ask for missing computer permissions only if actual access fails.
- **Phase 1 — read-only inventory:** create `state/local_inventory.json` with profile name, source, amplifier, cab, gain, preset search hits; and `state/performance_occupancy.json` with all currently used locations. These are ignored in Git by default.
- **Phase 2 — backups:** export to `backups/` or another user-chosen local path, verify the path; never commit backups to Git. Screenshot/capture the existing mappings.
- **Phase 3 — proposal diff:** resolve conflicts in bank numbers and missing profiles. Produce `state/implementation_plan.json` specifying exact selection per slot, all deviations and free destination locations.
- **Phase 4 — single pilot:** default to Continuum or Hendrix Core. Build five slots, assign all Remote switches, save, reload, compare sounds, trim levels only after the user auditions.
- **Phase 5 — expand:** systematically build remaining approved Performances. Keep a log of source Rig names, profile SHA where possible, and successful read-after-write checks.
- **Phase 6 — QA:** run the defined acceptance tests, report complete/partial/missing status and provide a restoration path.

## Rig Manager semantics

A Performance contains five Rig slots; Remote Bank up/down selects Performance locations in Performance Mode, Rig footswitches 1–5 recall slots, switches I–IIII control per-Rig assigned modules. This repository specifies A/B/C/D before the amp and X/MOD/DLY/REV after it, but exact hardware/software module topology must be verified before using optional MK2 Fixed FX slots.

The global wah expression assignment should not be changed blindly. A wah pedal may coexist with other expression functions only if intentionally configured. Prior reports described accidental volume control when moving wah; disable WahPedal-to-Volume unless specifically requested.

**Physical audio:** do not infer amp/speaker/monitor output wiring or a Kabinet/Kone setting from a picture of the Remote. Ask to inspect the user's setup before altering power-amplifier output.

## Required numeric Favorites order

**The user wants the Favorites first, numerically.** `specs/favorites.json` defines full-copy Performances **01–05**, then the existing 43 artist Performances occupy **06–48**. `data/favorites_source_map.json` traces every copied Rig. Do not append the favorites after the artists, overwrite occupied real Kemper banks, or discard original source Rigs. The new order exists only in the repository until the hardware is inspected. Pilot FAVORITES 01 before loading the rest.

## Artist priorities

1. Mayer: include the separately requested five-song Continuum pilot in `specs/mayer-continuum-five-song-legacy.json`; import exact previous detailed spec from `archive`, preserve Sinewave Continuum character, especially AdrenaLinn-style "Don't Trust Myself" filter and "I Guess I Just Feel Like" fuzz outro experimental rig.
2. Hendrix: era-dependent Marshall capture; Octavia/fuzz/vibe/Leslie differ by era. Machine Gun and Little Wing intentionally need different starting active modules.
3. SRV: Dumble SSS/Fender dynamic cleans, two TS gain stages, Vibratone; one Kemper cannot reproduce independent multi-amp outputs.
4. Clapton: Beano JTM45 2x12, Cream woman tone, Layla tweed Champ, Blackie, Journeyman; pickup tone control matters.
5. Robben Ford: actual Dumble ODS clean/PAB/OD captures preferred over EQ approximations. 2026 Little Walter 59 is a distinct sound.
6. New Performances 38–48: researched design candidates exist in `specs/` and `docs/new-performances.md`. These are structurally validated, but not installed, preset-confirmed, profile-matched or audio-calibrated. Instrument restrictions matter: Eagles intro requires a 12-string; early Eagles 1972 songs must not use Joe Walsh or Don Felder as session players; Polyphia Playing God requires nylon; Fleetwood acoustic needs acoustic strings.
7. Metalcore: use era-appropriate 5150/6505 or Laney profile, an OD808-style low-drive tightener and measured gate threshold; do not simply increase gain.
8. Remaining backlog: research missing source profiles and tone targets before implementation; planning-only items are not production-ready.

## Mandatory final report

Supply: (1) new location map, (2) precise profile filename/source per slot, (3) effect/remote assignment status for every slot, (4) output level comparison data when available, (5) missing sources or fallback changes, (6) backup paths and restore test, (7) what was actually changed and what was not. A screenshot alone does not prove saved Performance state.

## Additional Eagles 43 — special instruction

Performance 43 is a separate early-Eagles bank. See `specs/eagles-early.json` and `docs/artists/eagles-early.md`. For *One of These Nights*, Felder identified a 1959 Les Paul into a 1950s narrow-panel Tweed Deluxe. For *Witchy Woman*, original 1972 personnel were Leadon and Frey (before Felder/Walsh joined). Do not assign generic 1976 Eagles gear automatically.
