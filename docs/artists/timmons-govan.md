# Andy Timmons / Guthrie Govan — Performance 35: TIMMONS GOVAN

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/timmons-govan.json`](../../specs/timmons-govan.json)

Mesa Lone Star and Cornford/Victory families; Electric Gypsy has two related slots.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | ELECTRIC GYPSY | Electric Gypsy | Mesa/Boogie Lone Star or Lone Star Special singing overdriven 1x12/2x12 capture |
| 2 | GYPSY CLEAN | Electric Gypsy introductory clean/edge passages | Mesa/Boogie Lone Star low gain capture |
| 3 | GOVAN WAVES | Waves | Cornford MK50 II mid-gain 4x12 or equivalent British boutique articulate capture |
| 4 | GOVAN FIVES | Fives, Erotic Cakes era lead | Cornford MK50 II / Cornford lead 4x12 capture, medium-high gain not saturated scooped metal |
| 5 | GOVAN ARISTOCRATS | Aristocrats live, Modern fusion solo | Victory V30 The Countess / V30 Jack / Cornford boutique lead capture, choose based on song period |

## Detailed Rig programming targets

### 1. ELECTRIC GYPSY

**Target:** Rounded, touch-sensitive violin-like Andy Timmons lead: thick midrange, not heavily gated
**Capture:** Mesa/Boogie Lone Star or Lone Star Special singing overdriven 1x12/2x12 capture
**Guitar/pickup dependency:** Bridge humbucker / Ibanez AT-style HSS guitar; compare neck
**EQ offsets relative to chosen capture:** `{"bass": -0.25, "middle": 0.5, "treble": -0.32, "presence": -0.38}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":1.0}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.8}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":10}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":405,"feedback_percent_target":29,"mix_percent_target":22}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":12,"decay_seconds_target":2.0}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Analog and digital delay layers on record/live rigs may need a second delay module; this single-delay approximation is an initial live tone.

### 2. GYPSY CLEAN

**Target:** Articulate warm clean/edge with rounded upper mids and spacious delay
**Capture:** Mesa/Boogie Lone Star low gain capture
**Guitar/pickup dependency:** Neck or neck/middle single coils
**EQ offsets relative to chosen capture:** `{"bass": -0.2, "middle": 0.2, "treble": -0.23, "presence": -0.2}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.9}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | ON | `{"mix_percent_target":14,"rate_hz_target":0.32}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":420,"feedback_percent_target":27,"mix_percent_target":19}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":16,"decay_seconds_target":2.1}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 3. GOVAN WAVES

**Target:** Three-dimensional dynamic clean-to-crunch with mild compression; preserves touch articulation
**Capture:** Cornford MK50 II mid-gain 4x12 or equivalent British boutique articulate capture
**Guitar/pickup dependency:** Suhr/Charvel bridge pickup split or neck pickup as appropriate
**EQ offsets relative to chosen capture:** `{"bass": -0.35, "middle": 0.35, "treble": -0.1, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.6}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | ON | `{"mix_percent_target":10}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":350,"feedback_percent_target":18,"mix_percent_target":12}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 4. GOVAN FIVES

**Target:** Highly vocal fusion lead with immediate dynamic response and dry articulation
**Capture:** Cornford MK50 II / Cornford lead 4x12 capture, medium-high gain not saturated scooped metal
**Guitar/pickup dependency:** Bridge humbucker for lead / mixed pickups for fusion rhythm
**EQ offsets relative to chosen capture:** `{"bass": -0.38, "middle": 0.55, "treble": -0.1, "presence": -0.12}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":1.0}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.1}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":8}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":315,"feedback_percent_target":18,"mix_percent_target":10}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 5. GOVAN ARISTOCRATS

**Target:** Tight modern fusion tone; clean low-end separation and high dynamic control
**Capture:** Victory V30 The Countess / V30 Jack / Cornford boutique lead capture, choose based on song period
**Guitar/pickup dependency:** Suhr/Charvel humbucker with moderately hot but non-active response
**EQ offsets relative to chosen capture:** `{"bass": -0.42, "middle": 0.45, "treble": 0.0, "presence": -0.07}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.7}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":11}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":290,"feedback_percent_target":18,"mix_percent_target":10}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

## Sources

- https://www.premierguitar.com/gear/rig-rundown-andy-timmons

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
