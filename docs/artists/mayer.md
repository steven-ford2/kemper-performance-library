# John Mayer: Kemper tone configuration

**Status:** detailed_original_artifact_available. No patches have been installed or tested.

**Machine-readable source:** [`../../specs/mayer.json`](../../specs/mayer.json).

## Canonical Performance locations (subject to device inventory)

| Perf | Name | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 |
|---:|---|---|---|---|---|---|
| 06 | MAYER CORE | TRIO - DRIVE | CONTINUUM - SIG | AMERICANA - CLEAN | SEARCH - MODERN | SOB ROCK - 80S |
| 07 | TRIO NOKIA | WHO DID I WAS | GOOD LOVE | WAIT TOMORROW | VULTURES NOKIA | OUT OF MY MIND |
| 08 | CONTINUUM | DONT TRUST SELF | GRAVITY | SLOW DANCING | BELIEF | IN REPAIR / LEAD |
| 09 | AMERICANA | QUEEN / OLIVIA | BORN / LIVING | PARADISE FUNK | DEAR / WAITING | ACOUSTIC / FOLK |
| 10 | SEARCH | STILL FEEL MAN | MOVING ON | HELPLESS | ROSIE | CHANGING / WAVE |
| 11 | SOB ROCK | LAST TRAIN HOME | WILD BLUE | NEW LIGHT | FEEL LIKE OUTRO | SHOT IN DARK |
| 12 | BATTLE EXTRAS | EDGE OF DESIRE | HEARTBREAK WAR | CROSSROADS NG2 | ASSASSIN | MAYER SOUL LEAD |

## Implementation detail

For each slot, start from the indicated **captured amp gain family**. Relative EQ offsets are starting values **added to the selected capture**, not physical vintage amp dial positions. Every rig has modules A/B/C/D before amp and X/MOD/DLY/REV after amp. A target only exists if that parameter is available in the installed software.

### 06. MAYER CORE
#### Slot 1: TRIO - DRIVE
**Songs:** Who Did You Think I Was, Good Love Is on the Way, Out of My Mind
**Profile selector:** TWOROCK_CR
**Tone:** 2007 Nokia raw edge, clear pick attack, amp almost breaking, TS accent.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.5, "middle": 0.5, "treble": 0.1, "presence": 0.0}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: CONTINUUM - SIG
**Songs:** Gravity, Slow Dancing in a Burning Room, Belief, Vultures
**Profile selector:** SINE_SIG_G1265
**Tone:** Two-Rock clean with stacked gain and post-amp solo level.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": -0.1, "presence": -0.1}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | ON | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: AMERICANA - CLEAN
**Songs:** Queen of California, Something Like Olivia, Paper Doll, Dear Marie
**Profile selector:** FENDER_BF
**Tone:** Dryer organic Fender clean, less bass, very low drive.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.35, "middle": 0.15, "treble": 0.0, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | ON | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 4: SEARCH - MODERN
**Songs:** Still Feel Like Your Man, Helpless, Rosie, Moving On and Getting Over
**Profile selector:** JMOD_100
**Tone:** Tight, mid-focused modern Mayer headroom with crisp pedal gain.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": -0.1, "presence": -0.1}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | ON | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 5: SOB ROCK - 80S
**Songs:** Last Train Home, Shot in the Dark, Wild Blue, New Light
**Profile selector:** SOLDANO_SLO
**Tone:** 80s-flavored clean-to-crunch with chorus, delay and restrained gain.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.35, "middle": 0.4, "treble": 0.1, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | CE-1 | ON | {'mix_percent_target': 28, 'rate_hz_target': 0.7} |
| DLY | Single Delay | Digital | ON | {'time_ms_target': 355, 'mix_percent_target': 14, 'feedback_percent_target': 22} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

### 07. TRIO NOKIA
#### Slot 1: WHO DID I WAS
**Songs:** Who Did You Think I Was, Try!
**Profile selector:** TWOROCK_CR
**Tone:** Thick Nokia riff, medium headroom, edge and controlled aggressive TS.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.55, "middle": 0.5, "treble": 0.0, "presence": -0.1}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 1.5} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: GOOD LOVE
**Songs:** Good Love Is on the Way, Come When I Call
**Profile selector:** TWOROCK_CR
**Tone:** Pushed choppy blues with mild mid drive, clean snap.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.45, "middle": 0.5, "treble": 0.05, "presence": 0.05}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | ON | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: WAIT TOMORROW
**Songs:** Wait Until Tomorrow, Bold as Love (live), Every Day I Have the Blues
**Profile selector:** TWOROCK_CR
**Tone:** Hendrix-influenced Nokia live fuzz/clean Marshall-like grit; period-appropriate approximation.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.4, "middle": 0.45, "treble": -0.1, "presence": 0.05}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Kemper Fuzz | Red Germanium | OFF | {'drive_target_0to10': 5.5} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: VULTURES NOKIA
**Songs:** Vultures
**Profile selector:** TWOROCK_CR
**Tone:** Dry fast funk. Moderate pre-drive, compression extremely light, short slap usually OFF.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.6, "middle": 0.1, "treble": 0.15, "presence": 0}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | ON | {'intensity': 1.6} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Low Pass | Touch | OFF | {'mode': 'Touch', 'touch': 'adjust by ear'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Room Slap | OFF | {'time_ms_target': 115, 'mix_percent_target': 6, 'feedback_percent_target': 0} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 5: OUT OF MY MIND
**Songs:** Out of My Mind, I Don't Need No Doctor, Gravity (Nokia Trio-style)
**Profile selector:** DUMBLE_SSS
**Tone:** Big uncompressed vocal blues lead, clean backbone with smoothly gained lead lift.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.5, "middle": 0.55, "treble": -0.25, "presence": -0.25}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Kemper Drive | B Breaker Max | OFF | {'drive_target_0to10': 1.5} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 08. CONTINUUM
#### Slot 1: DONT TRUST SELF
**Songs:** I Don't Trust Myself (With Loving You)
**Profile selector:** SINE_SIG_G1265
**Tone:** AdrenaLinn-styled rhythmic filter vs auto-envelope wah: preset cannot fully match synchronized resonant motion.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": -0.1, "presence": -0.1}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Low Pass | Touch | OFF | {'mode': 'Touch', 'manual': 'mid', 'peak': 'adjust after audition'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Pulse Slicer | 1/8 Slicer | ON | {'rate': 'tempo_sync', 'edge': 'moderate', 'mix_percent_target': 45} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Phaser | Subtle | OFF | {'rate_hz_target': 0.6, 'mix_percent_target': 16} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→A+D, IIII→DLY

**Notes:** Switch III toggles both A and D; with opposite initial states it swaps rhythmic slicer ↔ touch filter. The pulse slicer is amplitude modulation, not original resonant pattern. Verify two effects are stored opposite states.

#### Slot 2: GRAVITY
**Songs:** Gravity, The Heart of Life
**Profile selector:** SINE_LO_G1265
**Tone:** Huge warm clean, neck, low sag, small spring, solo brightens without adding high gain.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.35, "middle": 0.2, "treble": -0.15, "presence": -0.2}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | ON | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 300, 'mix_percent_target': 7, 'feedback_percent_target': 11} |
| REV | Spring Reverb | Reverb Fan | ON | {'mix_percent_target': 13, 'decay_seconds_target': 1.6} |

**Remote:** I→B, II→C, III→DLY, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: SLOW DANCING
**Songs:** Slow Dancing in a Burning Room
**Profile selector:** SINE_SIG_G1265
**Tone:** Singing blues lead with clean rhythm and stacked Klon/TS drives.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.3, "middle": 0.35, "treble": -0.2, "presence": -0.25}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Kemper Drive | B Breaker Max | OFF | {'drive_target_0to10': 1.3} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 320, 'mix_percent_target': 10, 'feedback_percent_target': 15} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: BELIEF
**Songs:** Belief, Waiting on the World to Change
**Profile selector:** SINE_M_G1265
**Tone:** Driving syncopated clean/edge with overdrive for sustained solo, not blanket compression.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.45, "middle": 0.45, "treble": 0.1, "presence": 0.0}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Pulse Slicer | 1/8 Feather | OFF | {'rate': 'tempo_sync', 'mix_percent_target': 10} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: IN REPAIR / LEAD
**Songs:** In Repair, I'm Gonna Find Another You, Dreaming with a Broken Heart
**Profile selector:** SINE_OD_M75
**Tone:** More vocal sustain; Sinewave OD captured channel is preferable to huge distortion added to clean profile.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.3, "middle": 0.35, "treble": -0.15, "presence": -0.25}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Kemper Drive | B Breaker Max | OFF | {'drive_target_0to10': 1.1} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 360, 'mix_percent_target': 11, 'feedback_percent_target': 18} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 09. AMERICANA
#### Slot 1: QUEEN / OLIVIA
**Songs:** Queen of California, Something Like Olivia, Love Is a Verb
**Profile selector:** FENDER_BF
**Tone:** Airy rootsy single-coil, woody snap, light spring, very small TS option.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.45, "middle": 0.2, "treble": 0.05, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Spring Reverb | Reverb Fan | ON | {'mix_percent_target': 10} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 2: BORN / LIVING
**Songs:** Born and Raised, If I Ever Get Around to Living, A Face to Call Home, Whiskey, Whiskey, Whiskey
**Profile selector:** FENDER_TWEED
**Tone:** Dry midrange laid-back roots tones, barely broken low-watt sound.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.2, "middle": 0.4, "treble": -0.2, "presence": -0.2}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Photocell Tremolo | Slow Opto Throb | OFF | {'rate_hz_target': 2.5, 'depth_percent_target': 20} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 3: PARADISE FUNK
**Songs:** Wildfire, Call Me the Breeze, Paper Doll
**Profile selector:** FENDER_BF
**Tone:** Tighter JJ Cale inspired twang, dry funk and slight amp compression.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.5, "middle": 0.05, "treble": 0.15, "presence": 0.0}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Phaser | Subtle | OFF | {'rate_hz_target': 0.55, 'mix_percent_target': 15} |
| DLY | Single Delay | Tape Slapback 1 | OFF | {'time_ms_target': 130, 'mix_percent_target': 7, 'feedback_percent_target': 6} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 4: DEAR / WAITING
**Songs:** Dear Marie, Waitin' on the Day, On the Way Home, Who You Love
**Profile selector:** FENDER_BF
**Tone:** Quiet neck/neck-middle clean, wider atmospheric spring/delay.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.35, "middle": 0.2, "treble": -0.15, "presence": -0.25}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 430, 'mix_percent_target': 11, 'feedback_percent_target': 16} |
| REV | Natural Reverb | Small Plate | ON | {'mix_percent_target': 17, 'decay_seconds_target': 2.2} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 5: ACOUSTIC / FOLK
**Songs:** Walt Grace's Submarine Test, Badge and Gun, You're No One 'Til Someone Lets You Down, Speak for Me, Shadow Days
**Profile selector:** ACOUSTIC_DI
**Tone:** Acoustic-oriented patch; use real acoustic or simulator into full-range output, never cab simulation into guitar speaker.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": 0, "middle": 0, "treble": 0, "presence": 0}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Acoustic Simulator | Neck SC B | ON | {} |
| B | Compressor | Soft | OFF | {'intensity': 1.2} |
| C | Studio Equalizer | Vintage Mix | ON | {'low_cut_hz': 85, 'high_cut_hz': 11000} |
| D | None | none | OFF | {} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Small Plate | ON | {'mix_percent_target': 14, 'decay_seconds_target': 2.1} |

**Remote:** I→A, II→B, III→DLY, IIII→REV

**Notes:** No amp/cab if true acoustic DI; profiler output to Kabinet could still color acoustics. Prefer full-range monitoring.

### 10. SEARCH
#### Slot 1: STILL FEEL MAN
**Songs:** Still Feel Like Your Man
**Profile selector:** JMOD_100
**Tone:** Tight compressed neo-soul rhythmic clean, filtered/touch movement and small room.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.55, "middle": 0.1, "treble": 0.05, "presence": -0.05}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | ON | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Low Pass | Touch | OFF | {'mode': 'Touch', 'peak': 'medium'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | ON | {'mix_percent_target': 12, 'rate_hz_target': 0.55} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→MOD

**Notes:** None; evaluate by ear.

#### Slot 2: MOVING ON
**Songs:** Moving On and Getting Over
**Profile selector:** JMOD_100
**Tone:** Dry funk with strong bass clarity and slight late-70s phase character; do not overdrive.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.6, "middle": 0.2, "treble": 0.1, "presence": -0.1}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Low Pass | Touch | OFF | {'mode': 'Touch', 'peak': 'medium'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Phaser | Subtle | OFF | {'rate_hz_target': 0.5, 'mix_percent_target': 14} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→MOD

**Notes:** None; evaluate by ear.

#### Slot 3: HELPLESS
**Songs:** Helpless
**Profile selector:** JMOD_100
**Tone:** Aggressive sharp funk-rock blues, mild amp dirt, 808 lead stack.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.5, "middle": 0.55, "treble": 0.0, "presence": 0.0}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | ON | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Kemper Drive | B Breaker Max | OFF | {'drive_target_0to10': 2.0} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 285, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: ROSIE
**Songs:** Rosie, Love on the Weekend
**Profile selector:** JMOD_100
**Tone:** Rounded chord clean, bright funk bounce, lightly chorused tails.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.35, "middle": 0.15, "treble": -0.2, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | ON | {'mix_percent_target': 13, 'rate_hz_target': 0.7} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 300, 'mix_percent_target': 8, 'feedback_percent_target': 13} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 5: CHANGING / WAVE
**Songs:** Changing, Emoji of a Wave, In the Blood, Roll It on Home, Never on the Day You Leave
**Profile selector:** JMOD_100
**Tone:** Broader dynamic clean with midrange solo excursion and longer atmospheric ambience.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.25, "middle": 0.25, "treble": -0.2, "presence": -0.2}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 400, 'mix_percent_target': 12, 'feedback_percent_target': 18} |
| REV | Natural Reverb | Small Plate | ON | {'mix_percent_target': 16, 'decay_seconds_target': 2.2} |

**Remote:** I→B, II→C, III→DLY, IIII→X

**Notes:** None; evaluate by ear.

### 11. SOB ROCK
#### Slot 1: LAST TRAIN HOME
**Songs:** Last Train Home
**Profile selector:** SOLDANO_SLO
**Tone:** Journeyman-inspired 80s mid-gain solo with CE-1-like chorus and spacious repeats; keep amp below fizz.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.45, "middle": 0.6, "treble": -0.15, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | CE-1 | ON | {'mix_percent_target': 27, 'rate_hz_target': 0.7} |
| DLY | Single Delay | Digital | ON | {'time_ms_target': 360, 'mix_percent_target': 18, 'feedback_percent_target': 24} |
| REV | Natural Reverb | Small Plate | ON | {'mix_percent_target': 13, 'decay_seconds_target': 2.2} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** Mayer described Silver Sky -> Soldano + chorus approach in published Guitar World interview; exact recorded settings not documented.

#### Slot 2: WILD BLUE
**Songs:** Wild Blue
**Profile selector:** FENDER_BF
**Tone:** Clean mellow rhythmic Knopfler-like finger-tone; additional Ross Phaser/Distortion double part in interlude.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.4, "middle": 0.0, "treble": -0.15, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | ON | {'intensity': 1.2} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Phaser | Stone 1 | OFF | {'rate_hz_target': 0.65, 'mix_percent_target': 24} |
| DLY | Single Delay | Tape Slapback 1 | OFF | {'time_ms_target': 130, 'mix_percent_target': 6, 'feedback_percent_target': 8} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** Mayer independently described using a Ross phaser on the double of guitar interlude, not necessarily main guitar track. Another reference says his scratch pass used Fractal clean. Do not assert all tracks used Fender amp.

#### Slot 3: NEW LIGHT
**Songs:** New Light, Carry Me Away, Til the Right One Comes
**Profile selector:** FENDER_BF
**Tone:** Clean compressed/chorused pop guitar with minimalist 80s-width, medium slap.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.35, "middle": 0.0, "treble": 0.15, "presence": -0.05}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | CE-1 | ON | {'mix_percent_target': 20, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape Slapback 2 | ON | {'time_ms_target': 165, 'mix_percent_target': 9, 'feedback_percent_target': 9} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 4: FEEL LIKE OUTRO
**Songs:** I Guess I Just Feel Like (outro fuzz)
**Profile selector:** FENDER_CHAMP_HOT
**Tone:** EPIPHONE CASINO P-90 -> BC109 silicon fuzz family -> cranked Fender Vibro Champ, low-fi warmly clipped vocal sustain with rolled-off highs.
**Guitar/Pickup:** Closest: Epiphone Casino P-90 neck; on Strat use neck pickup with tone rolled down ~4–6 and apply post EQ shaping
**EQ offsets:** `{"bass": -0.2, "middle": 0.6, "treble": -0.5, "presence": -0.5}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Kemper Fuzz | Dark Blue Silicon | ON | {'drive_target_0to10': 6.5, 'mix_percent_target': 100, 'volume_db_target': 0.0} |
| B | Kemper Fuzz | Tyco Octavia Min | OFF | {'drive_target_0to10': 3.0} |
| C | Kemper Drive | Klon 1 | OFF | {'drive_target_0to10': 1.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Studio Equalizer | Vintage Mix | ON | {'low_cut_hz_target': 90, 'high_cut_hz_target': 6000, 'low_mid_boost_freq_hz': 400, 'low_mid_gain_db_target': 1.2, 'high_mid_cut_freq_hz': 3200, 'high_mid_gain_db_target': -2.0} |
| MOD | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.1, 'mix_percent_target': 35} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 260, 'mix_percent_target': 5, 'feedback_percent_target': 9} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 7, 'decay_seconds_target': 1.1} |

**Remote:** I→A, II→B, III→MOD, IIII→DLY

**Notes:** High priority: do NOT use Sinewave clean as primary. The documented Shin-ei Psychedelic Machine offers fuzz, vibe, octavia, but there is no confirmed evidence all were active. Start fuzz ON, Octavia and Vibe OFF. Capture should already sound broken up. Not a Big Muff or Cornish NG-2 tone. A/B against alternate silicon and Muffin, record short DI loops.

#### Slot 5: SHOT IN DARK
**Songs:** Shot in the Dark, Why You No Love Me, All I Want Is to Be with You, Shouldn't Matter but It Does
**Profile selector:** SOLDANO_SLO
**Tone:** Moderate polished 80s overdrive lead with slower chorus and time-domain width.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.35, "middle": 0.4, "treble": -0.1, "presence": -0.1}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 2 | ON | {'mix_percent_target': 23, 'rate_hz_target': 0.5} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 410, 'mix_percent_target': 16, 'feedback_percent_target': 18} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

### 12. BATTLE EXTRAS
#### Slot 1: EDGE OF DESIRE
**Songs:** Edge of Desire
**Profile selector:** TWOROCK_CR
**Tone:** Bright pushed clean carrying sustained expressive lead; minimal chorus and mids from stacked 808.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.5, "middle": 0.5, "treble": 0.0, "presence": -0.05}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 315, 'mix_percent_target': 10, 'feedback_percent_target': 17} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→DLY, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: HEARTBREAK WAR
**Songs:** Heartbreak Warfare, Perfectly Lonely
**Profile selector:** TWOROCK_CR
**Tone:** Spacious clean with rhythmic delay and wet modern pop edge.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.3, "middle": 0.2, "treble": 0.0, "presence": -0.2}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.5} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 415, 'mix_percent_target': 17, 'feedback_percent_target': 22} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→MOD, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 3: CROSSROADS NG2
**Songs:** Crossroads (Battle Studies)
**Profile selector:** SINE_LO_G1265
**Tone:** Pete Cornish NG-2-style angular, almost gated and highly saturated fuzz, different architecture from Sob Rock outro.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.45, "middle": 0.55, "treble": -0.45, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Kemper Fuzz | Dark Blue Silicon | ON | {'drive_target_0to10': 8.0} |
| B | Kemper Drive | 808 Min | OFF | {'drive_target_0to10': 1.0} |
| C | Noise Gate 4:1 | Basic | ON | {'threshold': 'tune until staccato decay without chopping pick attack'} |
| D | Wah Wah | Vox Old | OFF | {} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 5} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 330, 'mix_percent_target': 9, 'feedback_percent_target': 14} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 5, 'decay_seconds_target': 1.0} |

**Remote:** I→A, II→B, III→C, IIII→X

**Notes:** Mayer named NG-2 directly in 2010 interview and guitar volume around 4. Emulation is analog behavior approximation; do not claim modeled NG-2 circuit.

#### Slot 4: ASSASSIN
**Songs:** Assassin, Half of My Heart
**Profile selector:** SINE_OD_M75
**Tone:** More saturated but articulate lead with medium delay and dry rhythm.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.45, "middle": 0.5, "treble": -0.1, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 335, 'mix_percent_target': 11, 'feedback_percent_target': 13} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→DLY, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: MAYER SOUL LEAD
**Songs:** I'm Gonna Find Another You, Covered in Rain, Slow Dancing (extended live solos), I Don't Need No Doctor
**Profile selector:** SINE_M_G1265
**Tone:** Two-Rock/Dumble-like expressive midrange, TS/Bluesbreaker/Klon in layers, true post-amp level boost.
**Guitar/Pickup:** Strat/Silver Sky; neck/neck-middle to start
**EQ offsets:** `{"bass": -0.4, "middle": 0.55, "treble": -0.1, "presence": -0.15}`
**Gain:** first choose correctly captured gain; then adjust Amp Gain ≤±0.7 if necessary

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Compressor | Soft | OFF | {'intensity': 2.0, 'attack': 'use factory Soft initially'} |
| B | Kemper Drive | Klon 2 | OFF | {'drive': 1.0, 'volume_db_target': 0.0} |
| C | Kemper Drive | 808 Min | OFF | {'drive': 1.3, 'volume_db_target': 0.0} |
| D | Kemper Drive | B Breaker Max | OFF | {'drive_target_0to10': 1.5} |
| X | Pure Booster | 4dB Solo | OFF | {'volume_db_target': 2.0} |
| MOD | Vintage Chorus | Subtle 1 | OFF | {'mix_percent_target': 15, 'rate_hz_target': 0.65} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 360, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.7} |

**Remote:** I→B, II→C, III→D, IIII→X

**Notes:** None; evaluate by ear.

## Provenance
All specification values are initial engineering targets. Names such as `Kemper Drive / 808 Min` are candidates; verify against the device and installed preset list. Exact owned profile names are not known. Historical authenticity is not guaranteed. See `docs/procedures/build-and-verify.md`.
