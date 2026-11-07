# Rig Manager execution, calibration and acceptance tests

## Preconditions

- A **real** Kemper Profiler MK2 is connected by USB, recognized by Rig Manager on the user's computer. A Remote is connected to the Profiler using its NETWORK/REMOTE connection. Exact actual model/ports must be visually checked.
- This library's artist specifications are present locally and validated, and the user has authorized writes to the device.
- Important: no official direct Rig Manager automation API is assumed; use supported desktop-control UI or manual application.

## Inventory before mutation

1. Record Rig Manager + Profiler OS versions and current Performance names/slot names including occupancy of 01–32 and nearby empty locations.
2. Record all source Rig candidates and tags: amplifier make/model, clean/edge/crunch/lead capture type, speaker/cab, gain, capture provenance, whether Direct or Studio profile, and guitar pickup assumed in the reference.
3. Check factory effects by actual installed name: `Kemper Fuzz` (e.g., `Red Germanium`, `Mayer Octavia Min` if available), `Kemper Drive` (`808 Min`, `Klon 2` etc.), `Wah Wah`, `Phaser Vibe`, `Rotary Speaker`, `Studio Equalizer`, `Pure Booster`, `Single Delay`, `Natural Reverb`.
4. Record input/monitor/output and any Kemper Kone / Kabinet / power amp arrangement only read-only. Do not change global audio output.

## Backup

1. Create Profiler backup and separate library exports BEFORE changes.
2. Confirm readable nonempty files and save an inventory of their locations plus timestamps and hashes.
3. Record a restoration plan; verify that software exposes the restore/import path. Do not perform destructive restoration for demonstration.

## Build one five-slot pilot

1. Choose a free Performance location, or ask user to approve remapping if original proposed location is occupied.
2. Locate the source Rig closest to the desired *captured amp response*. If not found, use the documented fallback only after reporting it.
3. Load into slot, set **pre-amp** modules A/B/C/D and **post-amp** X/MOD/DLY/REV. Respect any alternate chain where effects must be re-ordered to approximate the recorded sound; no phantom chaining through unavailable blocks.
4. Apply only parameter controls present in current installed version. Write actual values to `state/implementation_log.json` and record substitutions. Do **not** misinterpret relative EQ offsets as absolute values.
5. Assign Remote buttons I/II/III/IIII to the specified **module(s)**. A button toggles loaded effect module state; it does not replace effect types on the fly. Some switches can control multiple independent effects if explicitly assigned.
6. Store each Rig/Performance to the Profiler. Navigate away, then return and verify name, effects loaded, initial on/off states, and switch assignments.
7. For wah expression, calibrate pedal and confirm full usable sweep, verify intended toe/heel bypass mode, and test that wah use doesn't also lower master guitar volume.
8. Measure clean output and driven/fuzz output, comparing perceived loudness at fixed monitoring level; use Rig Volume for matching. Avoid unnecessary global EQ/master volume moves.
9. Let the user audition, adjust tone with fixed guitar/pickup, then approve scaling to next bank.

## QA report per Rig

- Source capture exact name, date/vendor if known, source pack provenance, cabinet capture, intended pickup.
- Pre-/post-amp module layout, each effect type + selected factory preset, actual parameter values, initial state.
- Remote mapping and observed LEDs/switch action for I–IIII.
- Wah behavior; no unwanted Volume/Pitch combination.
- State reload success; Rig Volume trim; notes about audio comparison and unresolved sonic mismatch.
- The directory `state/`, profile backups, IRs and commercial content must not enter Git.

## Known fidelity limits

One Kemper Rig uses one captured amp path, while several historical tones used blended amplifiers, mics, tape tricks, room sound, doubling or different guitar instruments. Mark an approximation as such and offer multiple Rigs or recorded multi-tracking when required. Tone controls, neck/bridge pickups and physical guitar electronics remain important even with perfect amplifier profiling.
