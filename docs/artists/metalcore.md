# All That Remains / Killswitch Engage / As I Lay Dying — Performance 47: METALCORE

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/metalcore.json`](../../specs/metalcore.json)

Early/mid-2000s 5150/6505-family tight rhythm and Killswitch atmospheric clean. Exact tuning and guitar scale are instrument-dependent.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | ATR SIX | Six, This Calling, Not Alone | Peavey block-letter 5150 or 5150 II/6505+ lead channel, Mesa/Boogie 4x12 Celestion V30-like cab |
| 2 | ATR LEAD | Two Weeks, The Air That I Breathe, All That Remains lead passages | EVH 5150III / Peavey 5150 II/6505 lead into Mesa 4x12 V30, historically varies by record |
| 3 | KSE DIRTY | My Curse, The End of Heartache, Rose of Sharyn | early Peavey 5150/Framus Cobra or later Laney Ironheart head; 4x12 V30; choose track-era capture |
| 4 | KSE CLEAN | My Curse clean passages, The Arms of Sorrow, The End of Heartache clean passages | Matchless Clubman 30/Fuchs Clean Machine or Fender/modern clean capture, not high-gain 5150 channel |
| 5 | AILD 6505 | 94 Hours, Through Struggle, Nothing Left, Confined | Peavey 5150/6505 lead, optionally boosted Framus Cobra period profile, Mesa V30 4x12 |

## Detailed Rig programming targets

### 1. ATR SIX

**Target:** Very fast precise palm-mute attack, tightly gated lows, driven high mids; avoid excessive gain
**Capture:** Peavey block-letter 5150 or 5150 II/6505+ lead channel, Mesa/Boogie 4x12 Celestion V30-like cab
**Guitar/pickup dependency:** High-output bridge humbucker, Oli Herbert/active-equivalent; appropriate drop tuning
**EQ offsets relative to chosen capture:** `{"bass": -0.65, "middle": 0.25, "treble": 0.05, "presence": 0.0}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 4:1 | choose in editor | ON | `{"threshold_db_target":-43}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.2,"volume_db_target":2.0}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Harmonic Pitch | choose in editor | OFF | `{"mix_percent_target":12}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":85,"high_cut_hz_target":8500}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":10}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":300,"mix_percent_target":7,"feedback_percent_target":12}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":4,"decay_seconds_target":1}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** OD808 Level high / drive near zero strategy sourced from Oli Herbert gear interviews. Gate threshold must be set to pickup noise floor.

### 2. ATR LEAD

**Target:** Singing upper mids with some additional sustain, chorus and stereo lead echo without overly scooped rhythm tone
**Capture:** EVH 5150III / Peavey 5150 II/6505 lead into Mesa 4x12 V30, historically varies by record
**Guitar/pickup dependency:** Bridge humbucker high output, match tuning to track
**EQ offsets relative to chosen capture:** `{"bass": -0.57, "middle": 0.38, "treble": -0.07, "presence": -0.15}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 2:1 | choose in editor | ON | `{"threshold_db_target":-45}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.3,"volume_db_target":1.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.2}` |
| D | Harmonic Pitch | choose in editor | OFF | `{"mix_percent_target":12}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":90,"high_cut_hz_target":8200}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":12}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":365,"feedback_percent_target":20,"mix_percent_target":13}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":8,"decay_seconds_target":1.4}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 3. KSE DIRTY

**Target:** Aggressive tight Killswitch rhythm with moderate gain, mids intact, low drive OD808 always on
**Capture:** early Peavey 5150/Framus Cobra or later Laney Ironheart head; 4x12 V30; choose track-era capture
**Guitar/pickup dependency:** Caparison/EVH active high-output bridge pickup, Drop C / per song
**EQ offsets relative to chosen capture:** `{"bass": -0.68, "middle": 0.42, "treble": 0.03, "presence": 0.08}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 4:1 | choose in editor | ON | `{"threshold_db_target":-43}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.15,"volume_db_target":1.8}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":95,"high_cut_hz_target":8600}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":9}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":325,"feedback_percent_target":14,"mix_percent_target":8}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":5,"decay_seconds_target":1.1}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** KSE later uses Laney Ironheart, older records often 5150/Cobra; must pick record-era capture. OD808 used as tightener NOT added distortion.

### 4. KSE CLEAN

**Target:** Wide chime, controlled compression, atmospheric delay and reverb with defined attack
**Capture:** Matchless Clubman 30/Fuchs Clean Machine or Fender/modern clean capture, not high-gain 5150 channel
**Guitar/pickup dependency:** Coil-split high-output pickups or clean humbucker
**EQ offsets relative to chosen capture:** `{"bass": -0.26, "middle": 0.15, "treble": 0.02, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"low"}` |
| B | Kemper Drive | 808 Min | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.4,"mix_percent_target":13}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":90,"high_cut_hz_target":9000}` |
| MOD | Vintage Chorus | choose in editor | ON | `{"rate_hz_target":0.33,"mix_percent_target":18}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":425,"feedback_percent_target":27,"mix_percent_target":20}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":20,"decay_seconds_target":2.8}` |

**Remote assignments:** I → A, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 5. AILD 6505

**Target:** Razor-edged tight drop-tuned rhythm: disciplined low end, aggressive pick, little ambience
**Capture:** Peavey 5150/6505 lead, optionally boosted Framus Cobra period profile, Mesa V30 4x12
**Guitar/pickup dependency:** Bridge active or high-output humbucker, song-specific drop tuning
**EQ offsets relative to chosen capture:** `{"bass": -0.75, "middle": 0.38, "treble": 0.08, "presence": 0.07}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 4:1 | choose in editor | ON | `{"threshold_db_target":-44}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.15,"volume_db_target":2.1}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| D | Harmonic Pitch | choose in editor | OFF | `{"mix_percent_target":14}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":100,"high_cut_hz_target":8300}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":7}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":285,"feedback_percent_target":12,"mix_percent_target":6}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":4,"decay_seconds_target":1}` |

**Remote assignments:** I → B, II → C, III → D, IIII → DLY

**Limits/notes:** As I Lay Dying guitar rigs varied across albums; this is a verified genre/era target family, not an authenticated exact session patch.

## Sources

- https://www.premierguitar.com/artists/all-that-remains-against-the-wind?page=1
- https://www.premierguitar.com/artists/killswitch-engage-ironhearts-redemption-and-big-digits

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
