# Jeff Beck — Performance 44: JEFF BECK

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/jeff-beck.json`](../../specs/jeff-beck.json)

1975 Tele-Gib into amp, Wired-era fusion, later Strat touch and volume/whammy vocabulary.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | CAUSE LOVERS | Cause We’ve Ended as Lovers | small driven vintage British/Marshall combo or Fender low/medium gain capture, low noise |
| 2 | FREEWAY JAM | Freeway Jam | mid-1970s driven vintage British tube amp 4x12 / Fender combo if capture auditions closer |
| 3 | LED BOOTS | Led Boots, Scatterbrain | mid-high gain 1970s Marshall British rock capture, non-modern 4x12 |
| 4 | WHERE WERE YOU | Where Were You, Guitar Shop | Fender-style clean/edge-of-breakup amp or vintage Marshall with very open pickup dynamics |
| 5 | NADIA / LATE | Nadia, Brush with the Blues, A Day in the Life | loud mid-gain Marshall JCM2000/DSL or later Fender-like amp, medium power-stage compression |

## Detailed Rig programming targets

### 1. CAUSE LOVERS

**Target:** Rounded swelling vocal note with moderate medium-gain amp, little added effect
**Capture:** small driven vintage British/Marshall combo or Fender low/medium gain capture, low noise
**Guitar/pickup dependency:** Seymour Duncan Tele-Gib humbucker hybrid (not Strat on original studio master); use low-output humbucker
**EQ offsets relative to chosen capture:** `{"bass": -0.12, "middle": 0.4, "treble": -0.35, "presence": -0.3}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | OFF | `{"intensity_target":"very_low"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.6}` |
| D | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":6}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":285,"feedback_percent_target":12,"mix_percent_target":5}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":9,"decay_seconds_target":1.45}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** Do not turn on compression to simulate finger touch; preserve dynamic range. Original Tele-Gib confirmed by Seymour Duncan interview.

### 2. FREEWAY JAM

**Target:** Fat but nimble funky fusion: strong note edges and bass tight enough for rhythm
**Capture:** mid-1970s driven vintage British tube amp 4x12 / Fender combo if capture auditions closer
**Guitar/pickup dependency:** Humbucker Tele-Gib / period Beck guitar
**EQ offsets relative to chosen capture:** `{"bass": -0.35, "middle": 0.35, "treble": -0.15, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.4,"mix_percent_target":17}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":10}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":300,"feedback_percent_target":10,"mix_percent_target":6}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":8,"decay_seconds_target":1.3}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 3. LED BOOTS

**Target:** Sharper mid-forward fusion rock attack with disciplined dynamic drive
**Capture:** mid-high gain 1970s Marshall British rock capture, non-modern 4x12
**Guitar/pickup dependency:** Humbucker bridge
**EQ offsets relative to chosen capture:** `{"bass": -0.4, "middle": 0.48, "treble": -0.05, "presence": -0.08}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.5,"mix_percent_target":15}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":9}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":265,"feedback_percent_target":13,"mix_percent_target":8}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 4. WHERE WERE YOU

**Target:** Vocal/pseudo-human theremin-like legato, clean-to-crunch sweep, minimal extra modulation
**Capture:** Fender-style clean/edge-of-breakup amp or vintage Marshall with very open pickup dynamics
**Guitar/pickup dependency:** Jeff Beck Strat-style single coils; floating whammy tremolo and guitar volume critical
**EQ offsets relative to chosen capture:** `{"bass": -0.14, "middle": 0.25, "treble": -0.2, "presence": -0.2}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | OFF | `{"intensity_target":"very_low"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| D | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":7}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":385,"feedback_percent_target":15,"mix_percent_target":11}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.8,"mix_percent_target":13}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** Harmonically vocal tone primarily instrument/tremolo/volume technique, not envelope follower. Do not approximate with drastic compressor flattening.

### 5. NADIA / LATE

**Target:** Expressive Strat lead, dynamic clean-up, warm attack and limited echo
**Capture:** loud mid-gain Marshall JCM2000/DSL or later Fender-like amp, medium power-stage compression
**Guitar/pickup dependency:** Strat-style single coil; finger and tremolo articulation
**EQ offsets relative to chosen capture:** `{"bass": -0.23, "middle": 0.42, "treble": -0.25, "presence": -0.35}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":9}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":330,"feedback_percent_target":16,"mix_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.7,"mix_percent_target":11}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** This combines multiple eras as a generalized late-style platform rather than a source-verified exact track chain.

## Sources

- https://www.guitarworld.com/features/jeff-beck-discusses-gear-technique-and-hendrix-1985-guitar-world-interview-part-2
- https://www.vintageguitar.com/56032/remembering-jeff-beck-2/

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
