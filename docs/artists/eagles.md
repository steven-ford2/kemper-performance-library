# Eagles — Performance 41: EAGLES

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/eagles.json`](../../specs/eagles.json)

Split Felder and Walsh electric timbres. Real 12-string acoustic intro requires appropriate instrument.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | HOTEL 12STR | Hotel California - 12-string intro | No electric amp if genuine Takamine 12-string DI; fallback ultra-clean acoustic/piezo profile |
| 2 | HOTEL FELDER | Hotel California - Don Felder lead | Fender Tweed Deluxe narrow-panel 5E3 cranked with 1x12 vintage Jensen-like cab |
| 3 | HOTEL WALSH | Hotel California - Joe Walsh lead | Fender blackface Deluxe or Roland Cube-era clean-to-crunch small combo (Walsh recollection); 1x10/1x12 speaker |
| 4 | FAST LANE | Life in the Fast Lane | small driven Roland Cube / Tweed Deluxe 1x12 captures, compare to session references |
| 5 | EAGLES CLEAN | Take It Easy, One of These Nights, New Kid in Town, Lyin’ Eyes | blackface Fender Deluxe Reverb/Twin clean-to-edge capture, 1x12/2x12 |

## Detailed Rig programming targets

### 1. HOTEL 12STR

**Target:** Bright percussive 12-string acoustic direct center plus optional Echoplex/Leslie wet component
**Capture:** No electric amp if genuine Takamine 12-string DI; fallback ultra-clean acoustic/piezo profile
**Guitar/pickup dependency:** 12-string acoustic with pickup strongly preferred; electric-to-12-string cannot accurately create physical doubled courses
**EQ offsets relative to chosen capture:** `{"bass": -0.25, "middle": -0.15, "treble": 0.1, "presence": 0}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"low"}` |
| B | Pure Booster | choose in editor | OFF | `{"volume_db_target":1}` |
| C | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":95}` |
| D | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":12}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Rotary Speaker | Slow | ON | `{"mix_percent_target":35,"speed":"Slow"}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":260,"feedback_percent_target":12,"mix_percent_target":11}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.7,"mix_percent_target":12}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Felder described DeArmond pickup -> Echoplex -> Leslie blended with direct mic. A single Kemper cannot produce original stereo microphone mix.

### 2. HOTEL FELDER

**Target:** Warm singing LP-humbucker lead with grainy amp edge, very little stomp dirt
**Capture:** Fender Tweed Deluxe narrow-panel 5E3 cranked with 1x12 vintage Jensen-like cab
**Guitar/pickup dependency:** 1959 Les Paul-style bridge humbucker
**EQ offsets relative to chosen capture:** `{"bass": -0.25, "middle": 0.3, "treble": -0.16, "presence": -0.18}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.4}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Rotary Speaker | Slow | OFF | `{"mix_percent_target":12}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":260,"feedback_percent_target":17,"mix_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":8,"decay_seconds_target":1.5}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Do not mistake the 12-string intro Leslie treatment for the electric solo rig.

### 3. HOTEL WALSH

**Target:** Brighter, thinner and more percussive Telecaster voice to contrast Felder Les Paul
**Capture:** Fender blackface Deluxe or Roland Cube-era clean-to-crunch small combo (Walsh recollection); 1x10/1x12 speaker
**Guitar/pickup dependency:** Telecaster bridge single-coil
**EQ offsets relative to chosen capture:** `{"bass": -0.35, "middle": 0.35, "treble": -0.05, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.6}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Phaser | choose in editor | OFF | `{"mix_percent_target":10}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":270,"feedback_percent_target":15,"mix_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Walsh suggested Tele through Roland Cube (uncertain exact track); use contrasting tone rather than identical LP amp.

### 4. FAST LANE

**Target:** Dry cutting riff attack, gritty not modern high-gain, minimal ambience
**Capture:** small driven Roland Cube / Tweed Deluxe 1x12 captures, compare to session references
**Guitar/pickup dependency:** Single-coil Strat bridge for Walsh; Les Paul overdub variant
**EQ offsets relative to chosen capture:** `{"bass": -0.4, "middle": 0.3, "treble": 0.1, "presence": 0}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Flanger | choose in editor | OFF | `{"rate_hz_target":0.2,"mix_percent_target":35}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Phaser | choose in editor | OFF | `{"mix_percent_target":12}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":225,"feedback_percent_target":8,"mix_percent_target":5}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":5,"decay_seconds_target":1}` |

**Remote assignments:** I → B, II → D, III → MOD, IIII → DLY

**Limits/notes:** Tape flanging on the song end is in production; D is a performance approximation.

### 5. EAGLES CLEAN

**Target:** Open 1970s country-rock comping: glassy, rounded single-coil, light compression and spring ambience
**Capture:** blackface Fender Deluxe Reverb/Twin clean-to-edge capture, 1x12/2x12
**Guitar/pickup dependency:** Telecaster or Strat single-coil; song-by-song response
**EQ offsets relative to chosen capture:** `{"bass": -0.2, "middle": 0.1, "treble": 0, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target":"low"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":10}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":260,"mix_percent_target":8,"feedback_percent_target":12}` |
| REV | Spring Reverb | choose in editor | ON | `{"mix_percent_target":12,"decay_seconds_target":1.5}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

## Sources

- https://www.guitarworld.com/artists/guitarists/the-eagles-hotel-california-guitar-gear
- https://reverb.com/ca/news/the-gear-of-the-eagles

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
