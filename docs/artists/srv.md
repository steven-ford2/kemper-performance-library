# Stevie Ray Vaughan: Kemper tone configuration

**Status:** reconstructed_from_prior_conversation_summary; detailed original archive not accessible. No patches have been installed or tested.

**Machine-readable source:** [`../../specs/srv.json`](../../specs/srv.json).

## Canonical Performance locations (subject to device inventory)

| Perf | Name | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 |
|---:|---|---|---|---|---|---|
| 18 | SRV CORE | PRIDE JOY | TEXAS LEAD | COLD SHOT | SCUTTLE | SAY WHAT |
| 19 | SRV TEXAS FLOOD | LOVE STRUCK | PRIDE JOY | TEXAS FLOOD | TELL ME | LENNY |
| 20 | SRV WEATHER | SCUTTLE | COULDNT STAND | TIN PAN | VOODOO CHILE | COLD SHOT |
| 21 | SRV SOUL | SAY WHAT | CHANGE IT | LIFE WITHOUT | LOOK AT LITTLE | GONE HOME |
| 22 | SRV IN STEP | CROSS FIRE | TIGHTROPE | LEAVE MY GIRL | WALL OF DENIAL | RIVIERA |
| 23 | SRV LIVE | MONTREUX 82 | MONTREUX 85 | EL MOCAMBO | LIVE ALIVE | AUSTIN CITY |
| 24 | SRV FAMILY STYLE | HARD TO BE | TELEPHONE SONG | TICK TOCK | WHITE BOOTS | BROTHERS |
| 25 | SRV SKY CRYING | SKY IS CRYING | LITTLE WING | CHITLINS | WHAM | LIFE BY DROP |

## Implementation detail

For each slot, start from the indicated **captured amp gain family**. Relative EQ offsets are starting values **added to the selected capture**, not physical vintage amp dial positions. Every rig has modules A/B/C/D before amp and X/MOD/DLY/REV after amp. A target only exists if that parameter is available in the installed software.

### 18. SRV CORE
#### Slot 1: PRIDE JOY
**Songs:** Pride and Joy, Mary Had a Little Lamb
**Profile selector:** 1964 Vibroverb / Super Reverb clean edge
**Tone:** Dry snappy 15-inch style and sharp transients
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.4, "middle": 0.25, "treble": 0.1, "presence": 0}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: TEXAS LEAD
**Songs:** Texas Flood, Lenny
**Profile selector:** Fender Vibroverb 15 inch clean drive
**Tone:** Open sustained clean and TS for soaring lines
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | ON | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: COLD SHOT
**Songs:** Cold Shot
**Profile selector:** clean blackface Fender Super Reverb
**Tone:** Funky dry clean with tube screamer available
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** No generic wah auto sweep; percussive clean source.

#### Slot 4: SCUTTLE
**Songs:** Scuttle Buttin, Rude Mood
**Profile selector:** Super Reverb + Vibroverb mix proxy
**Tone:** Very tight bright rhythm, minimal delay
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 5, 'decay_seconds_target': 1.0} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: SAY WHAT
**Songs:** Say What!, Voodoo Chile (Slight Return)
**Profile selector:** Dumble Steel String Singer / Super Reverb clean
**Tone:** Heavy wah and optional Fuzz / Octavia
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** Wah expression. Use optional slot D for Octavia; B/C Tube Screamer stack.

### 19. SRV TEXAS FLOOD
#### Slot 1: LOVE STRUCK
**Songs:** Love Struck Baby
**Profile selector:** early Vibroverb/Super Reverb
**Tone:** Snappy Fender bite; low gain
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: PRIDE JOY
**Songs:** Pride and Joy
**Profile selector:** Fender blackface / EV-type speaker
**Tone:** Clear rhythmic breakup
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: TEXAS FLOOD
**Songs:** Texas Flood
**Profile selector:** Vibroverb/Super edge
**Tone:** Full clean sustain with TS accent
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | ON | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: TELL ME
**Songs:** Tell Me
**Profile selector:** blackface Super Reverb crunch
**Tone:** Sharp boogie attack
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: LENNY
**Songs:** Lenny
**Profile selector:** Vibroverb clean
**Tone:** Floating low-gain attack
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 13, 'decay_seconds_target': 2.1} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

### 20. SRV WEATHER
#### Slot 1: SCUTTLE
**Songs:** Scuttle Buttin
**Profile selector:** Fender Vibroverb / clean-mid
**Tone:** Fast bright articulation
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: COULDNT STAND
**Songs:** Couldn’t Stand the Weather
**Profile selector:** Dumble Steel String Singer / Vibroverb clean edge
**Tone:** Clear rhythm with solid bass
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: TIN PAN
**Songs:** Tin Pan Alley
**Profile selector:** clean Vibroverb 15
**Tone:** Wide quiet dynamics and minimal distortion
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 11, 'decay_seconds_target': 2.0} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: VOODOO CHILE
**Songs:** Voodoo Chile (Slight Return)
**Profile selector:** Dumble SSS + Fender profile
**Tone:** Wah- and fuzz-rich midrange
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | ON | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: COLD SHOT
**Songs:** Cold Shot
**Profile selector:** clean blackface Super Reverb
**Tone:** Dry muted rhythm
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 5, 'decay_seconds_target': 1.0} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

### 21. SRV SOUL
#### Slot 1: SAY WHAT
**Songs:** Say What!
**Profile selector:** Super Reverb / Dumble SSS
**Tone:** Deep wah with light overdrive
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: CHANGE IT
**Songs:** Change It
**Profile selector:** Fender Super Reverb medium edge
**Tone:** Clean articulate riff sound
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: LIFE WITHOUT
**Songs:** Life Without You
**Profile selector:** Vibroverb clean
**Tone:** Long sustain from amp/headroom and gentle TS
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | ON | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: LOOK AT LITTLE
**Songs:** Look at Little Sister
**Profile selector:** Super Reverb driven
**Tone:** Pushed crisp blues
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: GONE HOME
**Songs:** Gone Home
**Profile selector:** Fender / steel string singer clean
**Tone:** Clean jazz-blues with reverb
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 14, 'decay_seconds_target': 2.0} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

### 22. SRV IN STEP
#### Slot 1: CROSS FIRE
**Songs:** Crossfire
**Profile selector:** Dumble SSS + Fender Super clean
**Tone:** Punchy later clean with drive accents
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | ON | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: TIGHTROPE
**Songs:** Tightrope
**Profile selector:** late SRV Fender/Dumble clean edge
**Tone:** Confident clean-mid core
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: LEAVE MY GIRL
**Songs:** Leave My Girl Alone
**Profile selector:** Vibroverb + Super driven
**Tone:** Sustained vocal Texas lead
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | ON | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: WALL OF DENIAL
**Songs:** Wall of Denial
**Profile selector:** Dumble + Marshall proxy
**Tone:** High-headroom with defined dirty mid attack
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | ON | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: RIVIERA
**Songs:** Riviera Paradise
**Profile selector:** clean SSS + Vibroverb
**Tone:** Very clean expansive stereo-feeling ambience
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 350, 'mix_percent_target': 9, 'feedback_percent_target': 13} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 18, 'decay_seconds_target': 2.8} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

### 23. SRV LIVE
#### Slot 1: MONTREUX 82
**Songs:** Pride and Joy, Hide Away
**Profile selector:** early hot Fender clean edge
**Tone:** Raw bright live attack
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: MONTREUX 85
**Songs:** Texas Flood, Scuttle Buttin
**Profile selector:** Dumble + Fender/EV speaker proxy
**Tone:** Bigger cleaner mid-80s stage response
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: EL MOCAMBO
**Songs:** Texas Flood, Lenny
**Profile selector:** Vibroverb + Super Reverb
**Tone:** Flexible articulate live clean
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: LIVE ALIVE
**Songs:** Superstition, Voodoo Chile
**Profile selector:** large Dumble/Fender live rig
**Tone:** Huge clean/fuzz/wah options
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: AUSTIN CITY
**Songs:** Pride and Joy, Crossfire
**Profile selector:** late Super/Dumble live proxy
**Tone:** Controlled bright big-stage clean
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

### 24. SRV FAMILY STYLE
#### Slot 1: HARD TO BE
**Songs:** Hard to Be
**Profile selector:** clean Dumble SSS/Fender
**Tone:** 1990 polished Texas clean
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: TELEPHONE SONG
**Songs:** Telephone Song
**Profile selector:** Dumble clean edge
**Tone:** Articulate funk attack
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: TICK TOCK
**Songs:** Tick Tock
**Profile selector:** Fender clean / natural delay
**Tone:** Chime and air
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 16, 'decay_seconds_target': 2.0} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: WHITE BOOTS
**Songs:** White Boots
**Profile selector:** mid-drive Fender
**Tone:** Tighter medium crunch
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: BROTHERS
**Songs:** Brothers, Hillbillies From Outerspace
**Profile selector:** clear clean-to-crunch profile
**Tone:** Instrumental lead with controlled compression
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

### 25. SRV SKY CRYING
#### Slot 1: SKY IS CRYING
**Songs:** The Sky Is Crying
**Profile selector:** Vibroverb 15, clean edge
**Tone:** Singing low-mid sustain
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | ON | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: LITTLE WING
**Songs:** Little Wing
**Profile selector:** Vibroverb/Super clean edge
**Tone:** Clear dynamic lead with light Vibrotone
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | ON | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 14, 'decay_seconds_target': 2.0} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: CHITLINS
**Songs:** Chitlins Con Carne
**Profile selector:** Super Reverb clean
**Tone:** Round jazz-inflected clean rhythm
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: WHAM
**Songs:** Wham
**Profile selector:** Super Reverb driven
**Tone:** Aggressive short-decay overdrive
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | ON | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: LIFE BY DROP
**Songs:** Life By the Drop
**Profile selector:** acoustic guitar or acoustic simulation
**Tone:** Raw unplugged resonance; needs acoustic guitar
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Drive | 808 Min | OFF | {'drive': 1.1} |
| C | Kemper Drive | 808 Mid | OFF | {'drive': 1.7} |
| D | Kemper Fuzz | Tyco Octavia Min | OFF | {} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'mix_percent_target': 65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→MOD, IIII→X

**Notes:** Do not claim close fidelity with an electric amp profile.

## Provenance
All specification values are initial engineering targets. Names such as `Kemper Drive / 808 Min` are candidates; verify against the device and installed preset list. Exact owned profile names are not known. Historical authenticity is not guaranteed. See `docs/procedures/build-and-verify.md`.
