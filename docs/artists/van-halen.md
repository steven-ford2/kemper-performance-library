# Eddie Van Halen — Performance 34: VAN HALEN

**Status:** proposed; NOT installed or level matched. Settings are engineering starting targets, not documented original physical amp knob positions.

**Specification:** [`../../specs/van-halen.json`](../../specs/van-halen.json)

Five album-era target captures; no assumption that a Peavey 5150 was used for the 1986 album.

| Slot | Name | Songs | Source-profile selection |
|---:|---|---|---|
| 1 | VH1 BROWN | Ain’t Talkin’ ’Bout Love, Runnin’ with the Devil, Eruption | 1968 Marshall Super Lead 100 used with reduced line voltage, 4x12 Greenback; use a capture of the correct response |
| 2 | VH2 WOMEN | Beautiful Girls, Dance the Night Away, Everybody Wants Some!! | Vintage 1968 Marshall Super Lead 100 cranked 4x12 Greenback; slightly clearer response |
| 3 | VH FAIR | Mean Street, Unchained, So This Is Love? | Marshall Super Lead/Plexi driven capture with dense, dark mid bite and Greenback 4x12 |
| 4 | VH PANAMA | Panama, Hot for Teacher, Jump guitar | Marshall Super Lead 100 vintage 4x12, captured at a more saturated performance level |
| 5 | VH 5150 ERA | 5150 (song, 1986), Poundcake (1991), Right Now (1991) | For 1986–91 use driven Marshall Super Lead or transitional Soldano-type capture; optional alternate later Peavey 5150 capture only for post-1992 tone |

## Detailed Rig programming targets

### 1. VH1 BROWN

**Target:** Dry loud brown sound with sharp hair, warm low mids and distinct transients
**Capture:** 1968 Marshall Super Lead 100 used with reduced line voltage, 4x12 Greenback; use a capture of the correct response
**Guitar/pickup dependency:** Hot vintage bridge humbucker; volume 10
**EQ offsets relative to chosen capture:** `{"bass": -0.4, "middle": 0.3, "treble": -0.12, "presence": -0.3}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10":0.4}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":1.5}` |
| D | Flanger | choose in editor | OFF | `{"rate_hz_target":0.14,"mix_percent_target":32}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Phaser | choose in editor | OFF | `{"rate_hz_target":0.55,"mix_percent_target":40}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":285,"feedback_percent_target":8,"mix_percent_target":7}` |
| REV | Natural Reverb | choose in editor | ON | `{"mix_percent_target":8,"decay_seconds_target":1.5}` |

**Remote assignments:** I → B, II → D, III → MOD, IIII → DLY

**Limits/notes:** Do NOT alter mains voltage or advise a physical Variac. Select captured brown-sound profile; subtle plate/room rather than modern high gain.

### 2. VH2 WOMEN

**Target:** Open crunch, spongy lower mids, subtle slap; less compression than modern 5150
**Capture:** Vintage 1968 Marshall Super Lead 100 cranked 4x12 Greenback; slightly clearer response
**Guitar/pickup dependency:** As available; compare pickup and output level with source.
**EQ offsets relative to chosen capture:** `{"bass": -0.38, "middle": 0.28, "treble": 0, "presence": -0.15}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Flanger | choose in editor | OFF | `{"mix_percent_target":27,"rate_hz_target":0.15}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Phaser | choose in editor | OFF | `{"mix_percent_target":33,"rate_hz_target":0.5}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":310,"feedback_percent_target":10,"mix_percent_target":8}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → C, II → D, III → MOD, IIII → DLY

**Limits/notes:** Instrument and source capture are primary determinants.

### 3. VH FAIR

**Target:** Dark raw Fair Warning; dramatic flanger available for Unchained
**Capture:** Marshall Super Lead/Plexi driven capture with dense, dark mid bite and Greenback 4x12
**Guitar/pickup dependency:** As available; compare pickup and output level with source.
**EQ offsets relative to chosen capture:** `{"bass": -0.45, "middle": 0.6, "treble": -0.25, "presence": -0.28}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Flanger | choose in editor | ON | `{"rate_hz_target":0.18,"mix_percent_target":50,"feedback_target":"moderate"}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Phaser | choose in editor | OFF | `{"mix_percent_target":30}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target":300,"feedback_percent_target":11,"mix_percent_target":8}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → C, II → D, III → MOD, IIII → DLY

**Limits/notes:** Save flanger ON for Unchained but OFF in variants of Mean Street.

### 4. VH PANAMA

**Target:** Upper-mid punch, dry biting attack, tight echo and occasional chorus-like widening
**Capture:** Marshall Super Lead 100 vintage 4x12, captured at a more saturated performance level
**Guitar/pickup dependency:** As available; compare pickup and output level with source.
**EQ offsets relative to chosen capture:** `{"bass": -0.5, "middle": 0.5, "treble": -0.05, "presence": -0.12}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Flanger | choose in editor | OFF | `{"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":12,"rate_hz_target":0.6}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":310,"feedback_percent_target":15,"mix_percent_target":11}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.5,"mix_percent_target":9}` |

**Remote assignments:** I → C, II → D, III → MOD, IIII → DLY

**Limits/notes:** Post-amp widening is an optional live approximation, not an authenticated part of the original Panama track.

### 5. VH 5150 ERA

**Target:** Fuller, tighter Sammy-era lead; optional post-1992 Peavey variant must be separate, not mislabeled as 1986 recording
**Capture:** For 1986–91 use driven Marshall Super Lead or transitional Soldano-type capture; optional alternate later Peavey 5150 capture only for post-1992 tone
**Guitar/pickup dependency:** As available; compare pickup and output level with source.
**EQ offsets relative to chosen capture:** `{"bass": -0.5, "middle": 0.45, "treble": -0.1, "presence": -0.18}`
**Gain policy:** Select a captured profile at the target gain. Limit initial Amp Gain edits to ±0.7; never force clean captures to emulate fully driven amps.

| Module | Effect | Candidate preset | Initial | Proposed parameters |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | `{"pedal_mode":"Bypass @ Toe"}` |
| B | Kemper Drive | choose in editor | OFF | `{}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target":2.0}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target":0.7,"mix_percent_target":30}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target":80,"high_cut_hz_target":7900}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target":16}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target":360,"feedback_percent_target":18,"mix_percent_target":12}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target":1.8,"mix_percent_target":12}` |

**Remote assignments:** I → B, II → C, III → MOD, IIII → DLY

**Limits/notes:** Historically: 1986 5150 is the album, not the Peavey amp introduced 1992.

## Sources

- https://www.uaudio.com/blogs/ua/the-history-of-the-peavey-5150

## Interpretation notes
- Every field named `*_target` or `amp_eq_offsets` represents a starting setting. Confirm actual availability/range in Rig Manager, log substitutions.
- The Kemper cannot load arbitrary Neural DSP plugins or reproduce physically different instrument strings, multitracked layered guitars, or unsupported external processors as one Rig.
- Use a captured amp near the desired level of gain rather than trying to create the captured sound by massive Kemper Gain movement.
- Check Remote effects assigned per Rig, not globally.
- Never overwrite a used Performance without a backup and user-approved destination.
