# Eric Clapton: Kemper tone configuration

**Status:** reconstructed_from_prior_conversation_summary; detailed original archive not accessible. No patches have been installed or tested.

**Machine-readable source:** [`../../specs/clapton.json`](../../specs/clapton.json).

## Canonical Performance locations (subject to device inventory)

| Perf | Name | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 |
|---:|---|---|---|---|---|---|
| 26 | CLAPTON CORE | BEANO | CREAM WOMAN | LAYLA CHAMP | BLACKIE | JOURNEY |
| 27 | CLAPTON MARSHALL | BEANO BLUES | BEANO CLEAN | CREAM FRESH | WOMAN TONE | CROSSROADS |
| 28 | CLAPTON DOMINOS | LAYLA RIFF | LAYLA SLIDE | BELL BOTTOM | KEY TO HIGHWAY | ANYDAY |
| 29 | CLAPTON BLACKIE | LAY DOWN | COCAINE | WONDERFUL | SHERIFF | 80S BOOST |
| 30 | CLAPTON JOURNEY | PRETENDING | BAD LOVE | OLD LOVE | RUNNING FAITH | NO ALIBIS |
| 31 | CLAPTON BLUES PLUS | FROM CRADLE | UNPLUGGED | RIDING KING | CLAPTON STRAT | RECENT BLUES |

## Implementation detail

For each slot, start from the indicated **captured amp gain family**. Relative EQ offsets are starting values **added to the selected capture**, not physical vintage amp dial positions. Every rig has modules A/B/C/D before amp and X/MOD/DLY/REV after amp. A target only exists if that parameter is available in the installed software.

### 26. CLAPTON CORE
#### Slot 1: BEANO
**Songs:** Hideaway, All Your Love
**Profile selector:** Marshall 1962 Bluesbreaker/JTM45 2x12 driven capture
**Tone:** Les Paul/PAF to compressed KT66 combo bite
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** Prefer high-gain captured JTM45 combination, not high-gain modern amp.

#### Slot 2: CREAM WOMAN
**Songs:** Sunshine of Your Love, Crossroads (live)
**Profile selector:** 100 W JTM45/100 Marshall + 4x12 Greenback
**Tone:** SG/Les Paul tone rolled off, warm singing mids
**Guitar/Pickup:** Humbuckers; neck or bridge with tone rolled way down; adjust by source track
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'high_shelf_db': -3.0, 'high_shelf_hz': 3200} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 5, 'decay_seconds_target': 1.1} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: LAYLA CHAMP
**Songs:** Layla, Bell Bottom Blues
**Profile selector:** Fender tweed Champ small speaker / pushed combo
**Tone:** Bright grainy strat/tweed breakup
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | ON | {'mix_percent_target': 55} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** Vibratone rotary is a possibility for some material, not all Layla overdubs.

#### Slot 4: BLACKIE
**Songs:** Wonderful Tonight, Cocaine, I Shot the Sheriff
**Profile selector:** Music Man HD130 or blackface Fender Twin
**Tone:** Clear Strat rhythm, gradual breakup
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** Keep drive mostly disabled; guitar midboost circuitry varied by era.

#### Slot 5: JOURNEY
**Songs:** Bad Love, Pretending, Old Love
**Profile selector:** Soldano SLO-100 low/mid gain lead or Clapton 1989 stage amp
**Tone:** Thick active midboost and well-behaved sustain
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 11, 'feedback_percent_target': 15} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 27. CLAPTON MARSHALL
#### Slot 1: BEANO BLUES
**Songs:** Hideaway, Steppin Out
**Profile selector:** Marshall 1962 Bluesbreaker combo (KT66)
**Tone:** Cranked Les Paul and KT66 2x12 mids
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: BEANO CLEAN
**Songs:** Have You Heard, Double Crossing Time
**Profile selector:** JTM45/Marshall 1962 edge capture
**Tone:** Cranked amp but articulate guitar volume cleanup
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: CREAM FRESH
**Songs:** I Feel Free, Strange Brew
**Profile selector:** JTM45/100 Marshall 4x12
**Tone:** Open dynamic SG/Les Paul attack
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: WOMAN TONE
**Songs:** Sunshine of Your Love, White Room
**Profile selector:** 100 W Marshall JTM45/100
**Tone:** Thick dark singing with rolled tone and EQ
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: CROSSROADS
**Songs:** Crossroads, Spoonful
**Profile selector:** Marshall Super 100 / 4x12 crunch
**Tone:** Hard lively Cream live lead, little reverb
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 3, 'decay_seconds_target': 1.0} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 28. CLAPTON DOMINOS
#### Slot 1: LAYLA RIFF
**Songs:** Layla
**Profile selector:** small tweed Champ driven capture
**Tone:** Raw double-track Strat/amp bite
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: LAYLA SLIDE
**Songs:** Layla slide lines
**Profile selector:** small tweed Champ driven capture
**Tone:** Singing slide track; real guitar/slide attack remains required
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: BELL BOTTOM
**Songs:** Bell Bottom Blues
**Profile selector:** tweed Fender medium breakup
**Tone:** Tender transparent overdrive
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: KEY TO HIGHWAY
**Songs:** Key to the Highway
**Profile selector:** small Fender edge breakup
**Tone:** Unprocessed blues dry room
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: ANYDAY
**Songs:** Anyday, Why Does Love Got to Be So Sad
**Profile selector:** Fender tweed/blackface crunched
**Tone:** Layered loud Strat brightness
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 29. CLAPTON BLACKIE
#### Slot 1: LAY DOWN
**Songs:** Lay Down Sally
**Profile selector:** Fender / Music Man very clean
**Tone:** Low-drive country Strat chime
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: COCAINE
**Songs:** Cocaine
**Profile selector:** Music Man HD-130 or Fender big clean driven
**Tone:** Dark midrange punch with moderate amp drive
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: WONDERFUL
**Songs:** Wonderful Tonight
**Profile selector:** Fender/Music Man clean
**Tone:** Warm round long sustain, less saturation
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 12, 'decay_seconds_target': 1.9} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: SHERIFF
**Songs:** I Shot the Sheriff
**Profile selector:** Fender Music Man clean edge
**Tone:** Tighter funk and medium spring ambience
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: 80S BOOST
**Songs:** Forever Man, Behind the Sun
**Profile selector:** 80s clean Fender/Music Man
**Tone:** Active mid-boost-style sustain
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 30. CLAPTON JOURNEY
#### Slot 1: PRETENDING
**Songs:** Pretending
**Profile selector:** Soldano SLO clean/lead capture
**Tone:** Big smooth modern blues sustain
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: BAD LOVE
**Songs:** Bad Love
**Profile selector:** Soldano SLO 100 medium drive
**Tone:** Compressed high-headroom lead with strong mids
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | ON | {'mix_percent_target': 16} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: OLD LOVE
**Songs:** Old Love
**Profile selector:** Soldano SLO low-to-mid-gain
**Tone:** Expansive long sustain with expressive dynamics
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 360, 'mix_percent_target': 12, 'feedback_percent_target': 15} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: RUNNING FAITH
**Songs:** Running on Faith
**Profile selector:** Soldano/Fender clean
**Tone:** Soft clear guitar attack
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 15, 'decay_seconds_target': 2.3} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: NO ALIBIS
**Songs:** No Alibis
**Profile selector:** Soldano-inspired medium lead
**Tone:** 1989 polished presence and controlled chorus
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | ON | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 31. CLAPTON BLUES PLUS
#### Slot 1: FROM CRADLE
**Songs:** Five Long Years, Reconsider Baby
**Profile selector:** Fender tweed Twin + low gain
**Tone:** Modern straightforward blues clean/crunch
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: UNPLUGGED
**Songs:** Tears in Heaven, Layla (Unplugged)
**Profile selector:** acoustic guitar / appropriate acoustic capture
**Tone:** Actual acoustic guitar resonance, not equivalent to electric profile
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** Switch to acoustic instrument for high fidelity.

#### Slot 3: RIDING KING
**Songs:** Riding with the King
**Profile selector:** Fender Twin / low gain
**Tone:** Clean blues duet response
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: CLAPTON STRAT
**Songs:** Before You Accuse Me, Key to the Highway
**Profile selector:** Fender Custom Twin or tweed
**Tone:** Warm bluesman Strat with active-mid available
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: RECENT BLUES
**Songs:** Further on Up the Road, Crossroads late live
**Profile selector:** Fender Twin/Clapton stage low medium
**Tone:** Open modern blues tone, subtle chorus or solo boost
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 4.0, 'mid_center_hz_target': 500} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.6} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 17} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

## Provenance
All specification values are initial engineering targets. Names such as `Kemper Drive / 808 Min` are candidates; verify against the device and installed preset list. Exact owned profile names are not known. Historical authenticity is not guaranteed. See `docs/procedures/build-and-verify.md`.
