# Vai / Paul Gilbert / Jason Becker — Performance 38: VAI GILBERT BECKER

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/shred-triad.json`](../../specs/shred-triad.json)

Five complementary high-gain shred architectures; one Rig per listed target, except Vai uses two.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | VAI FTLOG | For the Love of God, Passion and Warfare leads | 1989–90 high-gain British lead: Carvin X100B or Bogner/Marshall-family 4x12 capture, NOT the later Carvin Legacy |
| 2 | VAI TENDER | Tender Surrender, Alien Love Secrets | Carvin X100B high-gain or early Carvin Legacy lead (latter as live-era alternative), vintage voiced 4x12 |
| 3 | GILBERT GOY | Get Out of My Yard, The Curse of Castle Dragon | Laney VH100R or GH100L driven 4x12; tight British high gain, no Rectifier scoop |
| 4 | GILBERT SILENCE | Silence Followed by a Deafening Roar, Silence Followed by a Deafening Roar era leads | Laney GH100L / VH100R or similar high-gain British amp 4x12 with mid-focused articulation |
| 5 | BECKER ALTIT | Altitudes, Perpetual Burn, Air | Marshall JCM800 2203 driven + Celestion G12T-75 4x12 capture |

## Detailed Rig programming targets

### 1. VAI FTLOG

**Target:** Liquid sustained mid-rich lead, broad ambience, strong harmonics, smooth but not muddy
**Capture:** 1989–90 high-gain British lead: Carvin X100B or Bogner/Marshall-family 4x12 capture, NOT the later Carvin Legacy
**Guitar/pickup dependency:** Humbucker superstrat; bridge; expressive volume/pedal swells
**EQ offsets relative to chosen capture:** `{"bass": -0.2, "middle": 0.25, "treble": -0.15, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.8}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.2}` |
| D | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | ON | `{"mix_percent_target":14,"rate_hz_target":0.35}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":390,"feedback_percent_target":24,"mix_percent_target":17}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":2.7,"mix_percent_target":18}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Do not source a Carvin Legacy for the 1990 studio take; the model was introduced later. Rebuild delay/reverb spatial envelope rather than maxing gain.

### 2. VAI TENDER

**Target:** Creamy Vai legato with more responsive clean-up than FTLOG; smooth top, light chorus
**Capture:** Carvin X100B high-gain or early Carvin Legacy lead (latter as live-era alternative), vintage voiced 4x12
**Guitar/pickup dependency:** As available; compare pickup and output level with source.
**EQ offsets relative to chosen capture:** `{"bass": -0.2, "middle": 0.25, "treble": -0.15, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":1.1}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| D | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | ON | `{"mix_percent_target":18,"rate_hz_target":0.5}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":360,"feedback_percent_target":22,"mix_percent_target":15}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Album/date-specific amp selector must be selected after source-profile inventory; do not claim exact captured recording chain.

### 3. GILBERT GOY

**Target:** Immediate pick transient, forward mids, controlled bass, sharply outlined high-speed notes
**Capture:** Laney VH100R or GH100L driven 4x12; tight British high gain, no Rectifier scoop
**Guitar/pickup dependency:** Bridge humbucker / PGM-style Ibanez
**EQ offsets relative to chosen capture:** `{"bass": -0.45, "middle": 0.55, "treble": 0.05, "presence": -0.05}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 2:1 | choose in editor | ON | `{"threshold_db_target":-45}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.5,"volume_db_target":1.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":10}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":280,"feedback_percent_target":12,"mix_percent_target":9}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":6,"decay_seconds_target":1.2}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Gate modestly; center and edge pick response; use existing Laney profile if available.

### 4. GILBERT SILENCE

**Target:** Smoother lyrical sustain than GOY without sacrificing pick articulation
**Capture:** Laney GH100L / VH100R or similar high-gain British amp 4x12 with mid-focused articulation
**Guitar/pickup dependency:** Bridge humbucker, roll treble slightly if bright
**EQ offsets relative to chosen capture:** `{"bass": -0.35, "middle": 0.45, "treble": -0.12, "presence": -0.16}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.5}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":14}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":335,"feedback_percent_target":19,"mix_percent_target":12}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":10,"decay_seconds_target":1.7}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Capture choice is inferred from Gilbert era, not verified per track.

### 5. BECKER ALTIT

**Target:** Bright, incisive neo-classical lead with front-end SD-1-like boost, short bright digital delay
**Capture:** Marshall JCM800 2203 driven + Celestion G12T-75 4x12 capture
**Guitar/pickup dependency:** Superstrat bridge Seymour Duncan JB-type humbucker
**EQ offsets relative to chosen capture:** `{"bass": -0.4, "middle": 0.45, "treble": 0.0, "presence": -0.1}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Noise Gate 2:1 | choose in editor | ON | `{"threshold_db_target":-47}` |
| B | Kemper Drive | 808 Min | ON | `{"drive_target_0_10":0.6,"volume_db_target":1.0}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.2}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":14}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":320,"feedback_percent_target":20,"mix_percent_target":13}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":2,"mix_percent_target":12}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Source gear JCM800/SD-1 from historical retrospective; delay/reverb settings engineered.

## Sources

- https://www.dialmytone.com/examples/jason-becker/altitudes

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
