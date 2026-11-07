# Yngwie Malmsteen — Performance 40: YNGWIE MALMSTEEN

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/yngwie.json`](../../specs/yngwie.json)

Vintage Marshall with DOD 250-style level boost and relatively dry lead; distinct clean/acoustic slot.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | BLACK STAR CLEAN | Black Star intro, Icarus Dream Suite acoustic sections | Fender clean or Marshall Plexi clean capture; nylon for source-specific acoustic parts |
| 2 | RISING FORCE | Black Star lead, Rising Force 1984 | 50/100 W Marshall JMP/Plexi 4x12 at driven volume, not a modern 5150 |
| 3 | FAR BEYOND | Far Beyond the Sun, Evil Eye, As Above So Below | loud Marshall 50/100 W Plexi lead with vintage 4x12; stronger mids than modern rhythm capture |
| 4 | TRILOGY ODYSSEY | You Don’t Remember, I’ll Never Forget, Trilogy Suite Op. 5, Rising Force (Odyssey) | mid/late 1980s Marshall vintage Super Lead/JMP 4x12 driven capture |
| 5 | MODERN YJM | Arpeggios from Hell, Red Devil, Modern live neoclassical lead | Marshall YJM100 vintage voiced 4x12 (Celestion 75 W) or old JMP/Plexi equivalent |

## Detailed Rig programming targets

### 1. BLACK STAR CLEAN

**Target:** Clear delicate clean, minimal pedals, moderate room ambience
**Capture:** Fender clean or Marshall Plexi clean capture; nylon for source-specific acoustic parts
**Guitar/pickup dependency:** Single-coil Strat; for actual nylon recording use nylon instrument
**EQ offsets relative to chosen capture:** `{"bass": -0.1, "middle": 0.18, "treble": -0.05, "presence": -0.05}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | OFF | `{"intensity_target":"very_low"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":8}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":280,"mix_percent_target":6,"feedback_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":12,"decay_seconds_target":2}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Nylon acoustic sections require real acoustic source for fidelity.

### 2. RISING FORCE

**Target:** Treble-defined edge, fast attack, relatively low distortion, low-output stacked Strat pickups
**Capture:** 50/100 W Marshall JMP/Plexi 4x12 at driven volume, not a modern 5150
**Guitar/pickup dependency:** DiMarzio HS-3-era low-output Strat, bridge or neck depending phrase
**EQ offsets relative to chosen capture:** `{"bass": -0.3, "middle": 0.58, "treble": -0.1, "presence": -0.18}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 2:1 | choose in editor | OFF | `{"threshold_db_target":-49}` |
| B | Kemper Drive | choose in editor | ON | `{"source_reference":"DOD 250 / 308 preamp","drive_target_0_10":1.3,"volume_db_target":2}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.8}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":7}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":275,"mix_percent_target":7,"feedback_percent_target":10}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":7,"decay_seconds_target":1.3}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Do not substitute saturated modern metal head; DOD-style boost remains central. Preset type is an approximation pending exact installed drive model.

### 3. FAR BEYOND

**Target:** Clear high harmonics, rapid note separation, no excessive gated sustain
**Capture:** loud Marshall 50/100 W Plexi lead with vintage 4x12; stronger mids than modern rhythm capture
**Guitar/pickup dependency:** HS-3 Fender Strat bridge/neck
**EQ offsets relative to chosen capture:** `{"bass": -0.35, "middle": 0.65, "treble": -0.15, "presence": -0.17}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | ON | `{"source_reference":"DOD 250","drive_target_0_10":1.5,"volume_db_target":2}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.9}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":18,"rate_hz_target":0.6}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":285,"mix_percent_target":6,"feedback_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":7,"decay_seconds_target":1.3}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 4. TRILOGY ODYSSEY

**Target:** Slightly smoother, rounder lead than 1984, mid-forward and fast
**Capture:** mid/late 1980s Marshall vintage Super Lead/JMP 4x12 driven capture
**Guitar/pickup dependency:** As available; compare pickup and output level with source.
**EQ offsets relative to chosen capture:** `{"bass": -0.33, "middle": 0.6, "treble": -0.18, "presence": -0.2}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | ON | `{"source_reference":"DOD 250","drive_target_0_10":1.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.8}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":7}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":280,"mix_percent_target":8,"feedback_percent_target":10}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 5. MODERN YJM

**Target:** Immediate, extremely bright harmonic articulation with dry midrange and small stage echo
**Capture:** Marshall YJM100 vintage voiced 4x12 (Celestion 75 W) or old JMP/Plexi equivalent
**Guitar/pickup dependency:** Seymour Duncan YJM Fury noiseless low-output Strat
**EQ offsets relative to chosen capture:** `{"bass": -0.38, "middle": 0.56, "treble": -0.08, "presence": -0.17}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 2:1 | choose in editor | OFF | `{"threshold_db_target":-47}` |
| B | Kemper Drive | choose in editor | ON | `{"source_reference":"DOD 250/YJM308","drive_target_0_10":1.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.7}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":8}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":290,"mix_percent_target":6,"feedback_percent_target":10}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":5,"decay_seconds_target":1.2}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Yngwie says primary solo rig typically dry; leave delay off. DOD-style gain push and vintage Marshall predominate.

## Sources

- https://www.premierguitar.com/gear/rig-rundown-yngwie-malmsteen
- https://www.premierguitar.com/artists/interview-yngwie-malmsteen-on-his-new-album-guitar

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
