# Eric Johnson — Performance 38: ERIC JOHNSON

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/eric-johnson.json`](../../specs/eric-johnson.json)

Separate Johnson clean, crunchy rhythm, and Plexi/Tube Driver violin leads; effects cannot substitute for multiple independent amps.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | CLIFFS STUDIO | Cliffs of Dover studio - main lead | 1969 100 W Marshall 1959 Super Lead, cab G12-80 style 4x12; capture warm with muted high end |
| 2 | CLIFFS LIVE | Cliffs of Dover live, Zap lead | 1969 50/100 W Marshall Plexi lead capture, dark input/cab |
| 3 | EJ CLEAN STEREO | Manhattan clean intro, Trademark, East Wes clean passages | Fender Twin Reverb or Deluxe Reverb 2x12 clean capture (two amps in stereo originally) |
| 4 | EJ DIRTY RHTHM | Righteous rhythm, Desert Rose rhythm, Trademark crunch | Two-Rock Traditional Clean driven / Marshall 50 W mid-crunch capture, selectable alternate |
| 5 | EJ FUZZ LEAD | Righteous lead, Desert Rose lead, High Landrons | warm cranked Marshall Plexi 50/100 with 4x12 G12H/G12-80 |

## Detailed Rig programming targets

### 1. CLIFFS STUDIO

**Target:** Violin lead: long liquid sustain, softened attack, low treble/presence, pronounced low mids
**Capture:** 1969 100 W Marshall 1959 Super Lead, cab G12-80 style 4x12; capture warm with muted high end
**Guitar/pickup dependency:** ES-335 bridge dominates album body; 1954 Strat used for segments
**EQ offsets relative to chosen capture:** `{"bass": -0.2, "middle": 0.3, "treble": -0.6, "presence": -0.65}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | ON | `{"source_reference":"Chandler/Butler Tube Driver","drive_target_0_10":2.3,"tone_target":"dark","volume_db_target":1.0}` |
| C | Kemper Fuzz | Red Germanium | OFF | `{}` |
| D | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.7}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":6}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":310,"feedback_percent_target":20,"mix_percent_target":13}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":7,"decay_seconds_target":1.4}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** Original order can include Echoplex before Tube Driver; Kemper DLY after Amp is a live approximation. Do not assert it reproduces preamp-loading of the original.

### 2. CLIFFS LIVE

**Target:** More immediate attack than studio, still smooth violin sustain and dark top
**Capture:** 1969 50/100 W Marshall Plexi lead capture, dark input/cab
**Guitar/pickup dependency:** Strat neck/bridge custom wiring as applicable
**EQ offsets relative to chosen capture:** `{"bass": -0.26, "middle": 0.4, "treble": -0.55, "presence": -0.6}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | ON | `{"source_reference":"Tube Driver","drive_target_0_10":2}` |
| C | Kemper Fuzz | Red Germanium | OFF | `{}` |
| D | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":18,"rate_hz_target":0.6}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":365,"feedback_percent_target":22,"mix_percent_target":15}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 3. EJ CLEAN STEREO

**Target:** Bell-like dry clean with wide TC-style chorus and restrained Echoplex echo
**Capture:** Fender Twin Reverb or Deluxe Reverb 2x12 clean capture (two amps in stereo originally)
**Guitar/pickup dependency:** Strat neck or neck-middle
**EQ offsets relative to chosen capture:** `{"bass": -0.2, "middle": -0.04, "treble": -0.05, "presence": -0.14}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"low"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.5}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | ON | `{"mix_percent_target":25,"rate_hz_target":0.35}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":360,"feedback_percent_target":14,"mix_percent_target":12}` |
| REV | Spring Reverb | choose in editor | ON | `{"mix_percent_target":13,"decay_seconds_target":1.5}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Single Kemper rig cannot produce true dual Fender head stereo interaction.

### 4. EJ DIRTY RHTHM

**Target:** Pushed sparkly but articulate crunch, no modern scooped fizz
**Capture:** Two-Rock Traditional Clean driven / Marshall 50 W mid-crunch capture, selectable alternate
**Guitar/pickup dependency:** Strat bridge or neck pickup
**EQ offsets relative to chosen capture:** `{"bass": -0.25, "middle": 0.35, "treble": -0.28, "presence": -0.25}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.9}` |
| C | Kemper Fuzz | Red Germanium | OFF | `{}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":7}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":310,"feedback_percent_target":11,"mix_percent_target":7}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Eric Johnson used separate amps for rhythm and lead; do not use lead amp and turn guitar volume down as sole substitute.

### 5. EJ FUZZ LEAD

**Target:** Fat Fuzz Face lead with guitar-volume cleanup, dark smooth high-end and vocal mids
**Capture:** warm cranked Marshall Plexi 50/100 with 4x12 G12H/G12-80
**Guitar/pickup dependency:** Strat bridge or neck according to song
**EQ offsets relative to chosen capture:** `{"bass": -0.22, "middle": 0.4, "treble": -0.5, "presence": -0.55}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | OFF | `{"drive_target_0_10":0.8}` |
| C | Kemper Fuzz | Red Germanium | ON | `{"drive_target_0_10":5.5}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":8}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":365,"feedback_percent_target":23,"mix_percent_target":13}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → C, II → B, III → MOD, IIII → DLY

**Limits/notes:** Place Fuzz Face before buffered/drive blocks for believable guitar-volume cleanup, check effective module order.

## Sources

- https://www.guitarworld.com/gear/the-secrets-behind-eric-johnsons-guitar-tone-on-cliffs-of-dover
- https://www.premierguitar.com/gear/rig-rundown-eric-johnson-2018

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
