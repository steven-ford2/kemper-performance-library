# Robben Ford: Kemper tone configuration

**Status:** reconstructed_from_prior_conversation_summary; detailed original archive not accessible. No patches have been installed or tested.

**Machine-readable source:** [`../../specs/robben-ford.json`](../../specs/robben-ford.json).

## Canonical Performance locations (subject to device inventory)

| Perf | Name | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 |
|---:|---|---|---|---|---|---|
| 32 | RF CORE | ODS CLEAN | ODS PAB | ODS LEAD | ZENDRIVE CLEAN | LITTLE WALTER |
| 33 | RF EARLY 80S | YELLOWJACKETS | WILD ABOUT | TALK DAUGHTER | BLUE LINE PRE | EARLY LEAD |
| 34 | RF BLUE LINE | B LINE CLEAN | B LINE DRIVE | CANNONBALL | HELP THE POOR | BLUE LINE LEAD |
| 35 | RF 1997-2009 | SOUL ON TEN | HAND FATE | SUPERNATURAL | TRUTH | STUDIO CLEAN |
| 36 | RF 2013-2023 | BRINGING | DAY IN NASH | PURPLE HOUSE | PURE 2021 | MODERN LEAD |
| 37 | RF 2026 | MAKE WEATHER | BLACK NIGHT | TWO SHADES | LIGHT FANDANGO | FANDANGO FM |

## Implementation detail

For each slot, start from the indicated **captured amp gain family**. Relative EQ offsets are starting values **added to the selected capture**, not physical vintage amp dial positions. Every rig has modules A/B/C/D before amp and X/MOD/DLY/REV after amp. A target only exists if that parameter is available in the installed software.

### 32. RF CORE
#### Slot 1: ODS CLEAN
**Songs:** Talk to Your Daughter, Help the Poor
**Profile selector:** Dumble Overdrive Special clean channel captured
**Tone:** Punchy balanced warm clean
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: ODS PAB
**Songs:** Talk to Your Daughter, Ain’t Got Nothin But the Blues
**Profile selector:** Dumble ODS with PAB boost captured
**Tone:** PAB boosted big vocal midrange
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** Prefer captured PAB state, avoid EQ emulation when capture exists.

#### Slot 3: ODS LEAD
**Songs:** Revelation, The Brother
**Profile selector:** Dumble ODS actual OD channel capture
**Tone:** Smooth articulated vocal sustain, defined low bass
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: ZENDRIVE CLEAN
**Songs:** Indianola, Cannonball Shuffle
**Profile selector:** ODS clean or Fender clean + Zendrive approximation
**Tone:** Controlled mid-driven articulation
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: LITTLE WALTER
**Songs:** The Light Fandango, Fire Flute, Fandango
**Profile selector:** Little Walter 59 + 2x12
**Tone:** Clear punchy Strat/Jazz-Fusion 2026 tones
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** Source artist interview verifies Little Walter 59 with 66 Strat for selected recent tracks.

### 33. RF EARLY 80S
#### Slot 1: YELLOWJACKETS
**Songs:** Imperial Strut
**Profile selector:** Dumble clean / Fender blackface
**Tone:** Early smooth fusion clean with low chorus
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | ON | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: WILD ABOUT
**Songs:** Wild About You
**Profile selector:** Dumble ODS clean medium
**Tone:** Big cleaner 80s rhythm
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: TALK DAUGHTER
**Songs:** Talk to Your Daughter
**Profile selector:** Dumble ODS PAB / OD
**Tone:** Vocal rhythm-to-lead mid boost
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: BLUE LINE PRE
**Songs:** Help the Poor
**Profile selector:** Dumble ODS clean
**Tone:** Raw punchy first-half blues
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: EARLY LEAD
**Songs:** Revelation
**Profile selector:** ODS OD driven capture
**Tone:** Bright but full note sustain
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 34. RF BLUE LINE
#### Slot 1: B LINE CLEAN
**Songs:** Start It Up
**Profile selector:** Dumble ODS clean big cabinet
**Tone:** Sharp confident blue line funk
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: B LINE DRIVE
**Songs:** The Brother
**Profile selector:** Dumble ODS mild OD
**Tone:** Solid vocal overdrive
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: CANNONBALL
**Songs:** Cannonball Shuffle
**Profile selector:** Dumble ODS pushed clean
**Tone:** Singing but percussive articulation
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: HELP THE POOR
**Songs:** Help the Poor
**Profile selector:** Dumble ODS PAB
**Tone:** Controlled rich clean crunch
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: BLUE LINE LEAD
**Songs:** You Cut Me to the Bone
**Profile selector:** Dumble ODS OD
**Tone:** Singing fat blues lead
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 300, 'mix_percent_target': 9, 'feedback_percent_target': 11} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 35. RF 1997-2009
#### Slot 1: SOUL ON TEN
**Songs:** Indianola
**Profile selector:** Dumble ODS clean / Fender big clean
**Tone:** Warm adult-blues articulation
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: HAND FATE
**Songs:** Handful of Blues
**Profile selector:** Dumble ODS medium gain
**Tone:** Mid-forward rich lead
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: SUPERNATURAL
**Songs:** Supernatural
**Profile selector:** Dumble ODS clean
**Tone:** Big spacious singing clean
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 12, 'decay_seconds_target': 2} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: TRUTH
**Songs:** Truth
**Profile selector:** Dumble ODS OD
**Tone:** Smooth blues-rock lead
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: STUDIO CLEAN
**Songs:** Lateral Climb
**Profile selector:** ODS clean vintage speaker
**Tone:** Articulate low-gain fusion
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 36. RF 2013-2023
#### Slot 1: BRINGING
**Songs:** Bringing It Back Home
**Profile selector:** Dumble ODS clean
**Tone:** Natural jazz-blues small room
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: DAY IN NASH
**Songs:** A Day in Nashville
**Profile selector:** Fender / ODS clean edge
**Tone:** Raw fast-recorded sound
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: PURPLE HOUSE
**Songs:** Purple House
**Profile selector:** ODS OD driven
**Tone:** Vocal warm blues rock
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: PURE 2021
**Songs:** Pure
**Profile selector:** ODS clean/lead captures
**Tone:** Refined smooth fusion sustain
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: MODERN LEAD
**Songs:** Everything I Do Gonna Be Funky
**Profile selector:** ODS PAB/OD
**Tone:** Forward mid punch, modest delay
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | ON | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 37. RF 2026
#### Slot 1: MAKE WEATHER
**Songs:** Make My Own Weather
**Profile selector:** Dumble ODS + Les Paul
**Tone:** Punchy rounded OD 2026 recorded main riff/solo
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: BLACK NIGHT
**Songs:** Black Night
**Profile selector:** Dumble ODS + Les Paul
**Tone:** Warm biting OD solos
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: TWO SHADES
**Songs:** Two Shades of Blue
**Profile selector:** Dumble ODS / Tele clean depending part
**Tone:** Vocal ODS melody / clean Tele rhythm
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** Track has both instrument/amp combinations; this is lead proxy.

#### Slot 4: LIGHT FANDANGO
**Songs:** The Light Fandango, Fire Flute
**Profile selector:** Little Walter 59 + mismatched 2x12 / 66 Strat
**Tone:** Articulate spanky Jeff Beck-influenced modern clean with headroom
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: FANDANGO FM
**Songs:** Fandango, Feeling’s Mutual
**Profile selector:** Little Walter 59 + 66 Strat
**Tone:** More expression with minimal OD
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Studio Equalizer | none | OFF | {'mid_boost_db_target': 2.4, 'mid_center_hz_target': 800} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.4} |
| D | Vintage Chorus | Subtle | OFF | {'mix_percent_target': 12} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 8, 'decay_seconds_target': 1.2} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

## Provenance
All specification values are initial engineering targets. Names such as `Kemper Drive / 808 Min` are candidates; verify against the device and installed preset list. Exact owned profile names are not known. Historical authenticity is not guaranteed. See `docs/procedures/build-and-verify.md`.
