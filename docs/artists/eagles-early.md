# Eagles — Performance 48: ONE OF THESE NIGHTS / WITCHY WOMAN

**Status:** proposed, not installed. These settings are engineering starting points, **not** authenticated original amp control positions. The 1972 and 1975 songs use different lineups.

**Specification:** [`../../specs/eagles-early.json`](../../specs/eagles-early.json)

| Slot | Rig | Main sound | Source capture |
|---:|---|---|---|
| 1 | NIGHTS RHYTHM | Dry articulate, slightly compressed R&B-rock accompaniment; gentle breakup on harder attacks, wide midrange with clean upper-register chime | 1970s Fender blackface Deluxe Reverb or Twin Reverb clean-to-edge, vintage 1x12/2x12, NOT a modern high-gain stack |
| 2 | NIGHTS FELDER | Don Felder sax-like singing lead: rich upper-mid vowel quality and controlled treble, sustain primarily from driven tweed and Les Paul humbuckers | mid-to-hot Fender narrow-panel tweed Deluxe 5E3 1950s capture with original-style 1x12; choose responsive slightly compressed natural overdrive |
| 3 | NIGHTS HARMONY | Clear, less saturated harmony guitar to complement Felder lead; tighter low end, minimal stereo effect; both harmonies are separately recorded guitar parts | narrow-panel Fender tweed Deluxe or balanced blackface Deluxe, crunchy but clean enough to resolve harmonized lines |
| 4 | WITCHY RIFF | Dark nasal, slightly gritty early-Eagles guitar riff; mild edge-of-breakup with restrained ambience and clear string attack | early-1970s Fender Deluxe Reverb 1x12 clean-to-edge; a similar era amp may be used, but exact tracking amp for 1972 recording is not verified |
| 5 | WITCHY SOLO | Focused, saturated P-90 lead with singing sustained notes; firmer attack than the riff, dry mids-forward 1972 studio guitar sound | early-1970s Fender Deluxe Reverb or equivalent small Fender combo at medium breakup, 1x12 |

## Detailed per-Rig specifications

### 1. NIGHTS RHYTHM

**Songs:** One of These Nights - layered rhythm

**Capture:** 1970s Fender blackface Deluxe Reverb or Twin Reverb clean-to-edge, vintage 1x12/2x12, NOT a modern high-gain stack

**Instrument:** single-coil or low-output humbucker; model layered Frey/Leadon parts as one primary guitar, not identical multi-guitar stereo

**Target:** Dry articulate, slightly compressed R&B-rock accompaniment; gentle breakup on harder attacks, wide midrange with clean upper-register chime

**Amp EQ offsets (relative):** `{"bass": -0.25, "middle": 0.15, "treble": -0.05, "presence": -0.1}`

| Module | Type | Candidate preset | Initial | Parameter targets |
|---|---|---|---|---|
| A | Compressor | choose in editor | ON | `{"intensity_target": "low", "mix_percent_target": 65}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10": 0.4}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target": 1.5}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target": 0.5, "mix_percent_target": 18}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target": 80, "high_cut_hz_target": 8000}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target": 12}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target": 215, "feedback_percent_target": 9, "mix_percent_target": 6}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target": 1.4, "mix_percent_target": 8}` |

**Remote I–IIII:** I → B; II → C; III → MOD; IIII → DLY

**Notes:** Rhythm recording combines guitars and studio mixing; avoid putting obviously modern chorus or heavy compression on the default patch. Amp not documented per guitar part. 1975 track with Don Felder and Bernie Leadon, not Joe Walsh.

### 2. NIGHTS FELDER

**Songs:** One of These Nights - main guitar solo

**Capture:** mid-to-hot Fender narrow-panel tweed Deluxe 5E3 1950s capture with original-style 1x12; choose responsive slightly compressed natural overdrive

**Instrument:** 1959 Les Paul Standard-style humbucker, ideally neck/bridge compare; lower tone knob modestly if harsh

**Target:** Don Felder sax-like singing lead: rich upper-mid vowel quality and controlled treble, sustain primarily from driven tweed and Les Paul humbuckers

**Amp EQ offsets (relative):** `{"bass": -0.2, "middle": 0.5, "treble": -0.25, "presence": -0.3}`

| Module | Type | Candidate preset | Initial | Parameter targets |
|---|---|---|---|---|
| A | Compressor | choose in editor | OFF | `{"intensity_target": "low"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10": 0.2, "tone_target_0_10": 4.0}` |
| C | Kemper Fuzz | choose in editor | OFF | `{"drive_target_0_10": 2}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target": 0.35, "mix_percent_target": 8}` |
| X | Pure Booster | choose in editor | OFF | `{"volume_db_target": 2.0}` |
| MOD | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target": 80, "high_cut_hz_target": 7200, "mid_peak_hz_target": 900, "mid_peak_db_target": 1.0}` |
| DLY | Single Delay | choose in editor | ON | `{"time_ms_target": 245, "feedback_percent_target": 12, "mix_percent_target": 8}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target": 1.4, "mix_percent_target": 7}` |

**Remote I–IIII:** I → B; II → X; III → D; IIII → DLY

**Notes:** Felder personally identified his 1959 Les Paul through narrow-panel Fender Tweed Deluxe for this song; melodic sax-like contour is tonal intent, NOT an envelope filter. Exact Echoplex inclusion on this master unconfirmed. Never save with heavy fuzz or phaser active.

### 3. NIGHTS HARMONY

**Songs:** One of These Nights - harmony electric guitars

**Capture:** narrow-panel Fender tweed Deluxe or balanced blackface Deluxe, crunchy but clean enough to resolve harmonized lines

**Instrument:** Les Paul humbucker or Telecaster bridge depending on available instrument, tone slightly more open than NIGHTS FELDER

**Target:** Clear, less saturated harmony guitar to complement Felder lead; tighter low end, minimal stereo effect; both harmonies are separately recorded guitar parts

**Amp EQ offsets (relative):** `{"bass": -0.3, "middle": 0.3, "treble": 0.0, "presence": -0.05}`

| Module | Type | Candidate preset | Initial | Parameter targets |
|---|---|---|---|---|
| A | Compressor | choose in editor | OFF | `{"intensity_target": "low"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10": 0.4}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target": 1.5}` |
| D | Phaser | choose in editor | OFF | `{"mix_percent_target": 12, "rate_hz_target": 0.4}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target": 92, "high_cut_hz_target": 8200}` |
| MOD | Vintage Chorus | choose in editor | OFF | `{"mix_percent_target": 10}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target": 170, "feedback_percent_target": 9, "mix_percent_target": 6}` |
| REV | Natural Reverb | choose in editor | ON | `{"decay_seconds_target": 1.2, "mix_percent_target": 7}` |

**Remote I–IIII:** I → B; II → C; III → MOD; IIII → DLY

**Notes:** A recorded two-guitar harmony cannot be faithfully generated by one Kemper mono signal with static pitch shifting; create two mono tracked parts or add a separately validated harmonizer if needed. Rig is the harmony-guitar source tone.

### 4. WITCHY RIFF

**Songs:** Witchy Woman - Bernie Leadon riff

**Capture:** early-1970s Fender Deluxe Reverb 1x12 clean-to-edge; a similar era amp may be used, but exact tracking amp for 1972 recording is not verified

**Instrument:** Gibson Les Paul Deluxe mini-humbuckers (documented as Leadon Witchy Woman guitar in retrospective gear coverage); if unavailable compare P-90 / lower-output humbuckers

**Target:** Dark nasal, slightly gritty early-Eagles guitar riff; mild edge-of-breakup with restrained ambience and clear string attack

**Amp EQ offsets (relative):** `{"bass": -0.15, "middle": 0.25, "treble": -0.2, "presence": -0.2}`

| Module | Type | Candidate preset | Initial | Parameter targets |
|---|---|---|---|---|
| A | Compressor | choose in editor | OFF | `{"intensity_target": "low"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10": 0.5}` |
| C | Pure Booster | choose in editor | OFF | `{"volume_db_target": 1.4}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target": 0.36, "mix_percent_target": 18}` |
| X | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target": 85, "high_cut_hz_target": 6700}` |
| MOD | Tremolo | choose in editor | OFF | `{"rate_hz_target": 3.0, "depth_percent_target": 18}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target": 230, "feedback_percent_target": 9, "mix_percent_target": 6}` |
| REV | Spring Reverb | choose in editor | ON | `{"decay_seconds_target": 1.2, "mix_percent_target": 9}` |

**Remote I–IIII:** I → B; II → C; III → D; IIII → DLY

**Notes:** Original 1972 record features Leadon and Frey; no Don Felder or Joe Walsh. Mini-humbucker Les Paul is documented for later performances of the song; do NOT assert it is independently proven for studio master. Avoid asserting exact Fender Twin original amp; choose blackface clean-to-edge capture based on period sound.

### 5. WITCHY SOLO

**Songs:** Witchy Woman - Glenn Frey solo

**Capture:** early-1970s Fender Deluxe Reverb or equivalent small Fender combo at medium breakup, 1x12

**Instrument:** Glenn Frey 1950s Les Paul Junior "Old Black" with P-90 (candidate from retrospective reporting; not direct studio session confirmation)

**Target:** Focused, saturated P-90 lead with singing sustained notes; firmer attack than the riff, dry mids-forward 1972 studio guitar sound

**Amp EQ offsets (relative):** `{"bass": -0.3, "middle": 0.48, "treble": -0.12, "presence": -0.2}`

| Module | Type | Candidate preset | Initial | Parameter targets |
|---|---|---|---|---|
| A | Compressor | choose in editor | OFF | `{"intensity_target": "low"}` |
| B | Kemper Drive | 808 Min | OFF | `{"drive_target_0_10": 0.35, "tone_target_0_10": 4.5}` |
| C | Kemper Fuzz | choose in editor | OFF | `{"drive_target_0_10": 2.5}` |
| D | Phaser | choose in editor | OFF | `{"rate_hz_target": 0.45, "mix_percent_target": 10}` |
| X | Pure Booster | choose in editor | OFF | `{"volume_db_target": 2.0}` |
| MOD | Studio Equalizer | choose in editor | ON | `{"low_cut_hz_target": 90, "high_cut_hz_target": 7600, "mid_peak_hz_target": 850, "mid_peak_db_target": 1.0}` |
| DLY | Single Delay | choose in editor | OFF | `{"time_ms_target": 210, "feedback_percent_target": 9, "mix_percent_target": 7}` |
| REV | Spring Reverb | choose in editor | ON | `{"decay_seconds_target": 1.3, "mix_percent_target": 8}` |

**Remote I–IIII:** I → B; II → X; III → D; IIII → DLY

**Notes:** Glenn Frey is credited with Witchy Woman lead in secondary accounts; plausible Les Paul Jr and modified Deluxe Reverb gear is retrospective inference. No fuzz/phaser active by default. Preserve articulation; tone is amp gain, not boosted preamp distortion.

## Sources and certainty

- [Don Felder direct account: 1959 Les Paul + narrow-panel Tweed Deluxe on One of These Nights](https://www.guitarworld.com/features/don-felder-eagles-dear-guitar-2013). High confidence guitar and amp family.
- [Felder interview on sax-like solo voice](https://www.guitarplayer.com/music/don-felder-on-his-eagles-one-of-these-nights-solo). High confidence musical tone target.
- [Reverb survey of Bernie Leadon gear](https://reverb.com/ca/news/the-gear-of-the-eagles). Mini-humbucker Les Paul reported for Witchy Woman performances; no independent confirmation this exact guitar appeared on 1972 master.
- [Guitar editorial on early Eagles lineup and Glenn Frey lead](https://www.musicradar.com/news/eagles-songs-guitar-glenn-frey-bernie-leadon-don-felder-joe-walsh). Secondary recollection; studio equipment candidates, not verified.
- [MusicBrainz credits for Witchy Woman](https://musicbrainz.org/release/9175ffb2-97c0-48ac-9b2d-8c66b19a1e27). Confirms 1972 lineup/recording personnel.

## Codex-specific constraints

1. Keep this separate from Performance 36; do not overwrite existing Eagles bank. Registry location 43 is candidate only.
2. Verify 5E3 vs Deluxe Reverb captures by listening. Do not create an exact-match claim from guessed mic/speaker/cab.
3. Match recorded lead quality primarily through amp capture + guitar; no automatically added wah, excessive drive or fuzz.
4. Verify single-guitar constraints: studio harmonies require distinct recordings/players or an independently auditioned harmonizer.
5. Back up and save each Rig; navigate away and return to verify initial states and Remote assignments.
