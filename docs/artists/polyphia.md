# Polyphia — Performance 37: POLYPHIA

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/polyphia.json`](../../specs/polyphia.json)

2018 clean processing, 2022 nylon and digital/hybrid production; no implied Neural DSP plugin hosting in Kemper.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | POLY GOAT | G.O.A.T., New Levels New Devils clean leads | pristine boutique Matchless/Chieftain-like clean capture; no amp breakup |
| 2 | PLAYING GOD | Playing God | acoustic nylon-string / piezo DI path; bypass conventional distorted amp/cab; select acoustic/piezo-specific capture if useful |
| 3 | 40OZ CHAMPAGNE | 40oz, Champagne, Light, Goose | ultra-clean boutique amp or direct guitar preamp capture with headroom |
| 4 | OD EGO LEAD | O.D., Ego Death lead passages | tight modern British high-gain / boutique crunch capture, clean low-frequency attack and clear midrange |
| 5 | CHIMERA HEAVY | Chimera, Neurotica, ABC distorted textures | modern high-gain 7/8-string-capable tight voiced amp profile into V30 4x12, e.g. 5150III-style or equivalent |

## Detailed Rig programming targets

### 1. POLY GOAT

**Target:** Extremely even glassy compressed DI-like clean with crisp high-end and restrained stereo widening
**Capture:** pristine boutique Matchless/Chieftain-like clean capture; no amp breakup
**Guitar/pickup dependency:** Ibanez AZ/THBB10 split-coil or middle-plus-bridge pickup
**EQ offsets relative to chosen capture:** `{"bass": -0.48, "middle": 0.25, "treble": 0.15, "presence": 0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"medium-high","attack_target":"moderate"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":110,"high_cut_hz_target":9000}` |
| D | Harmonic Pitch | choose in editor | OFF | `{"mix_percent_target":15}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | ON | `{"mix_percent_target":20,"rate_hz_target":0.45}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":290,"feedback_percent_target":12,"mix_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":10,"decay_seconds_target":1.4}` |

**Remote assignments:** I → A, II → D, III → MOD, IIII → DLY

**Limits/notes:** Strong compression must preserve pick onset. Some Polyphia synth/keyboard-like transients are DAW processing, not from guitar alone.

### 2. PLAYING GOD

**Target:** Dry percussive nylon-string attack, limited compression, stereo studio polish
**Capture:** acoustic nylon-string / piezo DI path; bypass conventional distorted amp/cab; select acoustic/piezo-specific capture if useful
**Guitar/pickup dependency:** Actual nylon string / piezo instrument required for high-fidelity result
**EQ offsets relative to chosen capture:** `{"bass": -0.15, "middle": -0.1, "treble": -0.05, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"low"}` |
| B | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":85}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.4}` |
| D | Harmonic Pitch | choose in editor | OFF | `{"mix_percent_target":7}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":90,"high_cut_hz_target":11500}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":7}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":260,"mix_percent_target":7,"feedback_percent_target":10}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.3,"mix_percent_target":9}` |

**Remote assignments:** I → A, II → D, III → MOD, IIII → DLY

**Limits/notes:** Do not label a distorted electric model as a nylon-string simulator. Original SC500N/TOD10N nylon lineage; recorded/instrument version varies.

### 3. 40OZ CHAMPAGNE

**Target:** Sparkling glassy articulated clean with very fast compression recovery, moderate chorus
**Capture:** ultra-clean boutique amp or direct guitar preamp capture with headroom
**Guitar/pickup dependency:** Split humbucker/neck-middle single-coil
**EQ offsets relative to chosen capture:** `{"bass": -0.4, "middle": 0.2, "treble": 0.1, "presence": 0.06}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"medium-high"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":1.0,"mix_percent_target":100}` |
| C | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":105}` |
| D | Harmonic Pitch | choose in editor | OFF | `{"mix_percent_target":14}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | ON | `{"mix_percent_target":24}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":240,"feedback_percent_target":13,"mix_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → A, II → D, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 4. OD EGO LEAD

**Target:** Stacked guitar layers and bright fluid lead; moderate gain, clear tapped harmonics
**Capture:** tight modern British high-gain / boutique crunch capture, clean low-frequency attack and clear midrange
**Guitar/pickup dependency:** Bridge humbucker on modern Ibanez
**EQ offsets relative to chosen capture:** `{"bass": -0.56, "middle": 0.45, "treble": 0.0, "presence": 0.0}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 2:1 | choose in editor | ON | `{"threshold_db_target":-48}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| D | Harmonic Pitch | choose in editor | OFF | `{"mix_percent_target":18}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":11}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":295,"mix_percent_target":12,"feedback_percent_target":18}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → D, III → MOD, IIII → DLY

**Limits/notes:** Ego Death guest Vai lead may need his own distinct sound. Do not promise exact stacked/orchestrated album production.

### 5. CHIMERA HEAVY

**Target:** Tight filtered low-end, aggressive definition, dry front; some synth/pitch production impossible from Kemper alone
**Capture:** modern high-gain 7/8-string-capable tight voiced amp profile into V30 4x12, e.g. 5150III-style or equivalent
**Guitar/pickup dependency:** 7-/8-string or appropriately down-tuned humbucker guitar for track
**EQ offsets relative to chosen capture:** `{"bass": -0.64, "middle": 0.25, "treble": 0.1, "presence": 0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 4:1 | choose in editor | ON | `{"threshold_db_target":-43}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.2,"volume_db_target":1.7}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Harmonic Pitch | choose in editor | OFF | `{"mix_percent_target":15}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":95,"high_cut_hz_target":8200}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":12}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":300,"mix_percent_target":7,"feedback_percent_target":11}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":5,"decay_seconds_target":1.2}` |

**Remote assignments:** I → B, II → D, III → MOD, IIII → DLY

**Limits/notes:** Kemper Harmonic Pitch is not a replacement for Neural DSP Multivoicer/DAW polyphonic processing. Audit note range and latency.

## Sources

- https://www.premierguitar.com/artists/guitarists/polyphia
- https://www.guitarworld.com/news/ibanez-tim-henson-tod10n

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
