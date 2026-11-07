# Fleetwood Mac — Performance 46: FLEETWOOD RUMOURS

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/fleetwood-rumours.json`](../../specs/fleetwood-rumours.json)

Only 1977 Rumours album tone families. Buckingham boosted Strat to Hiwatt, acoustic roots, minimal modern effects.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | DREAMS CLEAN | Dreams, You Make Loving Fun, Don’t Stop | Hiwatt Custom 100 clean or Fender blackface clean; low-drive studio amp with broad headroom |
| 2 | GO YOUR WAY | Go Your Own Way, Second Hand News, I Don’t Want to Know | Hiwatt Custom 100 driven input boosted by Alembic Stratoblaster, cab Hiwatt-style 4x12 |
| 3 | THE CHAIN OUTRO | The Chain - electric outro | Hiwatt Custom 100 very hot boosted Strat capture and 4x12; amp distortion from input saturation |
| 4 | NEVER GOING | Never Going Back Again, Songbird accompaniment | genuine steel-string acoustic DI/mic or clean acoustic profile, not a cranked Hiwatt |
| 5 | GOLD DUST | Gold Dust Woman, Oh Daddy | Hiwatt pushed clean-to-mid gain / period vintage 1970s British amp with 4x12 |

## Detailed Rig programming targets

### 1. DREAMS CLEAN

**Target:** Transparent percussive clean electric with round low mids, slight room and almost imperceptible modulation
**Capture:** Hiwatt Custom 100 clean or Fender blackface clean; low-drive studio amp with broad headroom
**Guitar/pickup dependency:** Lindsey Buckingham 1970s Strat single-coil / comparable
**EQ offsets relative to chosen capture:** `{"bass": -0.2, "middle": 0.18, "treble": -0.1, "presence": -0.2}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"low"}` |
| B | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":7}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":265,"feedback_percent_target":12,"mix_percent_target":6}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":12,"decay_seconds_target":1.6}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Do not impose later 1980s chorus sound. A stereo mix and keyboard space cannot be replicated by the guitar only.

### 2. GO YOUR WAY

**Target:** Brittle biting but full percussive amp overdrive, clean enough for note separation
**Capture:** Hiwatt Custom 100 driven input boosted by Alembic Stratoblaster, cab Hiwatt-style 4x12
**Guitar/pickup dependency:** 1970s Fender Strat with onboard Stratoblaster analog front-end, or transparent preboost
**EQ offsets relative to chosen capture:** `{"bass": -0.36, "middle": 0.43, "treble": -0.06, "presence": -0.05}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | OFF | `{}` |
| B | Pure Booster | choose in editor | ON | `{"volume_db_target":3.0}` |
| C | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.3}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Flanger | choose in editor | OFF | `{"mix_percent_target":9,"rate_hz_target":0.2}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":250,"mix_percent_target":6,"feedback_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":7,"decay_seconds_target":1.2}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Rick Turner documents a ~12 dB Stratoblaster on the real rig; +3 dB is a conservative boost into a captured amp, not a historical knob match.

### 3. THE CHAIN OUTRO

**Target:** Screaming compressed upper mids, prominent single-coil bite and controlled bass
**Capture:** Hiwatt Custom 100 very hot boosted Strat capture and 4x12; amp distortion from input saturation
**Guitar/pickup dependency:** Lindsey boosted Strat; bridge single-coil
**EQ offsets relative to chosen capture:** `{"bass": -0.45, "middle": 0.65, "treble": -0.12, "presence": -0.16}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Pure Booster | choose in editor | ON | `{"volume_db_target":3.0}` |
| C | Kemper Drive | choose in editor | OFF | `{"drive_target_0_10":0.5}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":6}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":265,"feedback_percent_target":11,"mix_percent_target":7}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":8,"decay_seconds_target":1.3}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** The iconic bass riff preceding outro is a separate bass track, not a guitar effect. Avoid altering amp captured response by excess Kemper Gain.

### 4. NEVER GOING

**Target:** Intimate dry close-miked steel-string acoustic with low compression and very short room sound
**Capture:** genuine steel-string acoustic DI/mic or clean acoustic profile, not a cranked Hiwatt
**Guitar/pickup dependency:** Steel-string acoustic guitar required; electric pickup cannot reproduce natural acoustic string/body noise
**EQ offsets relative to chosen capture:** `{"bass": -0.1, "middle": -0.1, "treble": -0.05, "presence": -0.05}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"very_low"}` |
| B | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":85}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":4}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":220,"mix_percent_target":4,"feedback_percent_target":6}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":8,"decay_seconds_target":1.2}` |

**Remote assignments:** I → A, II → B, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 5. GOLD DUST

**Target:** Dark, ominous, grainy layered texture, short echo/room; fuzz may be a useful live approximation
**Capture:** Hiwatt pushed clean-to-mid gain / period vintage 1970s British amp with 4x12
**Guitar/pickup dependency:** Single coil or humbucker depending source layer
**EQ offsets relative to chosen capture:** `{"bass": -0.3, "middle": 0.4, "treble": -0.4, "presence": -0.25}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.5}` |
| C | Kemper Fuzz | Red Germanium | OFF | `{}` |
| D | Flanger | choose in editor | OFF | `{"rate_hz_target":0.22,"mix_percent_target":17}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Rotary Speaker | Slow | OFF | `{"mix_percent_target":14}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":390,"feedback_percent_target":21,"mix_percent_target":13}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":16,"decay_seconds_target":2.2}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** Fuzz/flanger not asserted on actual isolated master track; record uses composite overdubs and studio treatments.

## Sources

- https://rickturnerguitars.com/fleetwood-mac-lindsey-buckingham-and-the-birth-of-the-turner-model-1-guitar/
- https://www.fleetwoodmacofficial.com/album/rumours

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
