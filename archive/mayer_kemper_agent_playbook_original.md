# John Mayer: Kemper Profiler MK2 + Remote — Rig Manager Agent Playbook

**Status:** proposed, not installed. The JSON file is authoritative for all 35 Rigs.

## Purpose
Seven Performances and 35 Rigs span 2007 Nokia Trio, Continuum, Battle Studies, Born & Raised / Paradise Valley, The Search for Everything, and Sob Rock. Crucial Sob Rock fuzz outro is kept distinct from older Cornish NG-2-style Crossroads fuzz.

## Performance index

| Performance | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 |
|---|---|---|---|---|---|
| 7 07 MAYER CORE | TRIO - DRIVE | CONTINUUM - SIG | AMERICANA - CLEAN | SEARCH - MODERN | SOB ROCK - 80S |
| 8 08 TRIO NOKIA | WHO DID I WAS | GOOD LOVE | WAIT TOMORROW | VULTURES NOKIA | OUT OF MY MIND |
| 9 09 CONTINUUM | DONT TRUST SELF | GRAVITY | SLOW DANCING | BELIEF | IN REPAIR / LEAD |
| 10 10 AMERICANA | QUEEN / OLIVIA | BORN / LIVING | PARADISE FUNK | DEAR / WAITING | ACOUSTIC / FOLK |
| 11 11 SEARCH | STILL FEEL MAN | MOVING ON | HELPLESS | ROSIE | CHANGING / WAVE |
| 12 12 SOB ROCK | LAST TRAIN HOME | WILD BLUE | NEW LIGHT | FEEL LIKE OUTRO | SHOT IN DARK |
| 13 13 BATTLE EXTRAS | EDGE OF DESIRE | HEARTBREAK WAR | CROSSROADS NG2 | ASSASSIN | MAYER SOUL LEAD |

## Profile selection hierarchy
Source profile filenames are UNKNOWN. Filter owned Sinewave OD pack for Sig/Lo/M/OD with G1265 or M75; then inspect actual capture labels. 88 is the advertised profile count (62 Studio, 26 Direct). Never invent filenames. If there is no small-hot-Fender/Vibro Champ profile, explicitly flag requirement; the Sinewave clean is NOT a sonic equivalent.

| Key | Priority / description | Fallback |
|---|---|---|
| SINE_SIG_G1265 | owned Tone Junkie Official Sinewave Continuum OD pack; John Mayer signature low/clean, G12-65 speaker | SINE_LO_G1265 |
| SINE_LO_G1265 | owned Tone Junkie Official Sinewave Continuum OD pack; very clean, wide, bass-rich high-headroom G12-65 clean | SINE_SIG_G1265 |
| SINE_M_G1265 | owned Tone Junkie Official Sinewave Continuum OD pack; mid-switched clean or edge profile with additional focus | SINE_SIG_G1265 |
| SINE_OD_M75 | owned Tone Junkie Official Sinewave Continuum OD pack; captured amp overdrive with singing harmonics and Scumback M75 | SINE_SIG_G1265 + TS drive, mark substitution |
| TWOROCK_CR | owned non-Sinewave profiles or free Rig Exchange; wide clean/edge Two-Rock; suitable Nokia Trio and Continuum | SINE_SIG_G1265 |
| DUMBLE_SSS | owned or free Rig Exchange; fast, authoritative low-end, glassy high headroom; part of 2007 multi-amp aesthetic | SINE_LO_G1265 |
| FENDER_BF | owned or free Rig Exchange; dry Fender clean to lightly pushed; warmer/less subbass than Two-Rock | SINE_LO_G1265 with high-pass and lower bass |
| FENDER_TWEED | owned or free Rig Exchange; soft edged smaller-combo compression with chewy attack | FENDER_BF |
| FENDER_CHAMP_HOT | owned or free Rig Exchange; essential acquisition if absent; highly saturated small Fender combo, small speaker roll-off, not Two-Rock | FENDER_TWEED with hotter capture, no Sinewave as primary |
| JMOD_100 | owned or free Rig Exchange; tight huge-clean-headroom PRS J-MOD / later-era pedal platform | SINE_SIG_G1265 |
| SOLDANO_SLO | owned or free Rig Exchange; moderate gain 80s-inflected tube amp with mid focus, NOT maximum saturated channel | SINE_OD_M75 with carefully limited gain |
| ACOUSTIC_DI | genuine acoustic input preferred; otherwise Acoustic Simulator; acoustic guitar or acoustic simulator to full-range output, not distorted electric speaker | FENDER_BF + Acoustic Simulator, mark compromised |

## Remote button default philosophy

- **I:** Klon-family preamp boost on B (unless fuzz-specialized)
- **II:** TS-808 on C (unless fuzz-specialized)
- **III:** song-specific pedal/slicer/fuzz/filter on D or A
- **IIII:** X post-amp solo boost, MOD chorus, or DLY delay as each Rig specifies
- **Wah:** separate expression input where Wah effect is loaded; avoid enabling Wah-to-Volume.

## Detailed construction ledger

## Performance 7 — 07 MAYER CORE

### 7.1 TRIO - DRIVE

**Target songs:** Who Did You Think I Was, Good Love Is on the Way, Out of My Mind

**Tone:** 2007 Nokia raw edge, clear pick attack, amp almost breaking, TS accent.

**Amp source:** `TWOROCK_CR` — wide clean/edge Two-Rock; suitable Nokia Trio and Continuum

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.5, 'middle': 0.5, 'treble': 0.1, 'presence': 0.0}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | ON | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 7.2 CONTINUUM - SIG

**Target songs:** Gravity, Slow Dancing in a Burning Room, Belief, Vultures

**Tone:** Two-Rock clean with stacked gain and post-amp solo level.

**Amp source:** `SINE_SIG_G1265` — John Mayer signature low/clean, G12-65 speaker

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.2, 'middle': 0.25, 'treble': -0.1, 'presence': -0.1}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | ON | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 7.3 AMERICANA - CLEAN

**Target songs:** Queen of California, Something Like Olivia, Paper Doll, Dear Marie

**Tone:** Dryer organic Fender clean, less bass, very low drive.

**Amp source:** `FENDER_BF` — dry Fender clean to lightly pushed; warmer/less subbass than Two-Rock

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.35, 'middle': 0.15, 'treble': 0.0, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | ON | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 7.4 SEARCH - MODERN

**Target songs:** Still Feel Like Your Man, Helpless, Rosie, Moving On and Getting Over

**Tone:** Tight, mid-focused modern Mayer headroom with crisp pedal gain.

**Amp source:** `JMOD_100` — tight huge-clean-headroom PRS J-MOD / later-era pedal platform

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.2, 'middle': 0.25, 'treble': -0.1, 'presence': -0.1}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | ON | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 7.5 SOB ROCK - 80S

**Target songs:** Last Train Home, Shot in the Dark, Wild Blue, New Light

**Tone:** 80s-flavored clean-to-crunch with chorus, delay and restrained gain.

**Amp source:** `SOLDANO_SLO` — moderate gain 80s-inflected tube amp with mid focus, NOT maximum saturated channel

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.35, 'middle': 0.4, 'treble': 0.1, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / CE-1 | ON | mix_percent_target: 28, rate_hz_target: 0.7 |
| DLY | Single Delay / Digital | ON | time_ms_target: 355, mix_percent_target: 14, feedback_percent_target: 22 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

## Performance 8 — 08 TRIO NOKIA

### 8.1 WHO DID I WAS

**Target songs:** Who Did You Think I Was, Try!

**Tone:** Thick Nokia riff, medium headroom, edge and controlled aggressive TS.

**Amp source:** `TWOROCK_CR` — wide clean/edge Two-Rock; suitable Nokia Trio and Continuum

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.55, 'middle': 0.5, 'treble': 0.0, 'presence': -0.1}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 1.5 |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | ON | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 8.2 GOOD LOVE

**Target songs:** Good Love Is on the Way, Come When I Call

**Tone:** Pushed choppy blues with mild mid drive, clean snap.

**Amp source:** `TWOROCK_CR` — wide clean/edge Two-Rock; suitable Nokia Trio and Continuum

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.45, 'middle': 0.5, 'treble': 0.05, 'presence': 0.05}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | ON | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 8.3 WAIT TOMORROW

**Target songs:** Wait Until Tomorrow, Bold as Love (live), Every Day I Have the Blues

**Tone:** Hendrix-influenced Nokia live fuzz/clean Marshall-like grit; period-appropriate approximation.

**Amp source:** `TWOROCK_CR` — wide clean/edge Two-Rock; suitable Nokia Trio and Continuum

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.4, 'middle': 0.45, 'treble': -0.1, 'presence': 0.05}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Kemper Fuzz / Red Germanium | OFF | drive_target_0to10: 5.5 |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 8.4 VULTURES NOKIA

**Target songs:** Vultures

**Tone:** Dry fast funk. Moderate pre-drive, compression extremely light, short slap usually OFF.

**Amp source:** `TWOROCK_CR` — wide clean/edge Two-Rock; suitable Nokia Trio and Continuum

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.6, 'middle': 0.1, 'treble': 0.15, 'presence': 0}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | ON | intensity: 1.6 |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Low Pass / Touch | OFF | mode: Touch, touch: adjust by ear |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Room Slap | OFF | time_ms_target: 115, mix_percent_target: 6, feedback_percent_target: 0 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 8.5 OUT OF MY MIND

**Target songs:** Out of My Mind, I Don't Need No Doctor, Gravity (Nokia Trio-style)

**Tone:** Big uncompressed vocal blues lead, clean backbone with smoothly gained lead lift.

**Amp source:** `DUMBLE_SSS` — fast, authoritative low-end, glassy high headroom; part of 2007 multi-amp aesthetic

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.5, 'middle': 0.55, 'treble': -0.25, 'presence': -0.25}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF |  |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Kemper Drive / B Breaker Max | OFF | drive_target_0to10: 1.5 |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

## Performance 9 — 09 CONTINUUM

### 9.1 DONT TRUST SELF

**Target songs:** I Don't Trust Myself (With Loving You)

**Tone:** AdrenaLinn-styled rhythmic filter vs auto-envelope wah: preset cannot fully match synchronized resonant motion.

**Amp source:** `SINE_SIG_G1265` — John Mayer signature low/clean, G12-65 speaker

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.2, 'middle': 0.25, 'treble': -0.1, 'presence': -0.1}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = A+D, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Wah Low Pass / Touch | OFF | mode: Touch, manual: mid, peak: adjust after audition |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Pulse Slicer / 1/8 Slicer | ON | rate: tempo_sync, edge: moderate, mix_percent_target: 45 |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Phaser / Subtle | OFF | rate_hz_target: 0.6, mix_percent_target: 16 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Switch III toggles both A and D; with opposite initial states it swaps rhythmic slicer ↔ touch filter. The pulse slicer is amplitude modulation, not original resonant pattern. Verify two effects are stored opposite states.

### 9.2 GRAVITY

**Target songs:** Gravity, The Heart of Life

**Tone:** Huge warm clean, neck, low sag, small spring, solo brightens without adding high gain.

**Amp source:** `SINE_LO_G1265` — very clean, wide, bass-rich high-headroom G12-65 clean

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.35, 'middle': 0.2, 'treble': -0.15, 'presence': -0.2}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = DLY, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | ON | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 300, mix_percent_target: 7, feedback_percent_target: 11 |
| REV | Spring Reverb / Reverb Fan | ON | mix_percent_target: 13, decay_seconds_target: 1.6 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 9.3 SLOW DANCING

**Target songs:** Slow Dancing in a Burning Room

**Tone:** Singing blues lead with clean rhythm and stacked Klon/TS drives.

**Amp source:** `SINE_SIG_G1265` — John Mayer signature low/clean, G12-65 speaker

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.3, 'middle': 0.35, 'treble': -0.2, 'presence': -0.25}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Kemper Drive / B Breaker Max | OFF | drive_target_0to10: 1.3 |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | ON | time_ms_target: 320, mix_percent_target: 10, feedback_percent_target: 15 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 9.4 BELIEF

**Target songs:** Belief, Waiting on the World to Change

**Tone:** Driving syncopated clean/edge with overdrive for sustained solo, not blanket compression.

**Amp source:** `SINE_M_G1265` — mid-switched clean or edge profile with additional focus

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.45, 'middle': 0.45, 'treble': 0.1, 'presence': 0.0}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Pulse Slicer / 1/8 Feather | OFF | rate: tempo_sync, mix_percent_target: 10 |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 9.5 IN REPAIR / LEAD

**Target songs:** In Repair, I'm Gonna Find Another You, Dreaming with a Broken Heart

**Tone:** More vocal sustain; Sinewave OD captured channel is preferable to huge distortion added to clean profile.

**Amp source:** `SINE_OD_M75` — captured amp overdrive with singing harmonics and Scumback M75

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.3, 'middle': 0.35, 'treble': -0.15, 'presence': -0.25}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Kemper Drive / B Breaker Max | OFF | drive_target_0to10: 1.1 |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | ON | time_ms_target: 360, mix_percent_target: 11, feedback_percent_target: 18 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

## Performance 10 — 10 AMERICANA

### 10.1 QUEEN / OLIVIA

**Target songs:** Queen of California, Something Like Olivia, Love Is a Verb

**Tone:** Airy rootsy single-coil, woody snap, light spring, very small TS option.

**Amp source:** `FENDER_BF` — dry Fender clean to lightly pushed; warmer/less subbass than Two-Rock

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.45, 'middle': 0.2, 'treble': 0.05, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Spring Reverb / Reverb Fan | ON | mix_percent_target: 10 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 10.2 BORN / LIVING

**Target songs:** Born and Raised, If I Ever Get Around to Living, A Face to Call Home, Whiskey, Whiskey, Whiskey

**Tone:** Dry midrange laid-back roots tones, barely broken low-watt sound.

**Amp source:** `FENDER_TWEED` — soft edged smaller-combo compression with chewy attack

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.2, 'middle': 0.4, 'treble': -0.2, 'presence': -0.2}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Photocell Tremolo / Slow Opto Throb | OFF | rate_hz_target: 2.5, depth_percent_target: 20 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 10.3 PARADISE FUNK

**Target songs:** Wildfire, Call Me the Breeze, Paper Doll

**Tone:** Tighter JJ Cale inspired twang, dry funk and slight amp compression.

**Amp source:** `FENDER_BF` — dry Fender clean to lightly pushed; warmer/less subbass than Two-Rock

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.5, 'middle': 0.05, 'treble': 0.15, 'presence': 0.0}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Phaser / Subtle | OFF | rate_hz_target: 0.55, mix_percent_target: 15 |
| DLY | Single Delay / Tape Slapback 1 | OFF | time_ms_target: 130, mix_percent_target: 7, feedback_percent_target: 6 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 10.4 DEAR / WAITING

**Target songs:** Dear Marie, Waitin' on the Day, On the Way Home, Who You Love

**Tone:** Quiet neck/neck-middle clean, wider atmospheric spring/delay.

**Amp source:** `FENDER_BF` — dry Fender clean to lightly pushed; warmer/less subbass than Two-Rock

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.35, 'middle': 0.2, 'treble': -0.15, 'presence': -0.25}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | ON | time_ms_target: 430, mix_percent_target: 11, feedback_percent_target: 16 |
| REV | Natural Reverb / Small Plate | ON | mix_percent_target: 17, decay_seconds_target: 2.2 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 10.5 ACOUSTIC / FOLK

**Target songs:** Walt Grace's Submarine Test, Badge and Gun, You're No One 'Til Someone Lets You Down, Speak for Me, Shadow Days

**Tone:** Acoustic-oriented patch; use real acoustic or simulator into full-range output, never cab simulation into guitar speaker.

**Amp source:** `ACOUSTIC_DI` — acoustic guitar or acoustic simulator to full-range output, not distorted electric speaker

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': 0, 'middle': 0, 'treble': 0, 'presence': 0}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = A, II = B, III = DLY, IIII = REV

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Acoustic Simulator / Neck SC B | ON |  |
| B | Compressor / Soft | OFF | intensity: 1.2 |
| C | Studio Equalizer / Vintage Mix | ON | low_cut_hz: 85, high_cut_hz: 11000 |
| D | None / custom/none | OFF |  |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Small Plate | ON | mix_percent_target: 14, decay_seconds_target: 2.1 |

**Agent caveat:** No amp/cab if true acoustic DI; profiler output to Kabinet could still color acoustics. Prefer full-range monitoring.

## Performance 11 — 11 SEARCH

### 11.1 STILL FEEL MAN

**Target songs:** Still Feel Like Your Man

**Tone:** Tight compressed neo-soul rhythmic clean, filtered/touch movement and small room.

**Amp source:** `JMOD_100` — tight huge-clean-headroom PRS J-MOD / later-era pedal platform

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.55, 'middle': 0.1, 'treble': 0.05, 'presence': -0.05}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = MOD

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | ON | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Low Pass / Touch | OFF | mode: Touch, peak: medium |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | ON | mix_percent_target: 12, rate_hz_target: 0.55 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 11.2 MOVING ON

**Target songs:** Moving On and Getting Over

**Tone:** Dry funk with strong bass clarity and slight late-70s phase character; do not overdrive.

**Amp source:** `JMOD_100` — tight huge-clean-headroom PRS J-MOD / later-era pedal platform

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.6, 'middle': 0.2, 'treble': 0.1, 'presence': -0.1}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = MOD

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Low Pass / Touch | OFF | mode: Touch, peak: medium |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Phaser / Subtle | OFF | rate_hz_target: 0.5, mix_percent_target: 14 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 11.3 HELPLESS

**Target songs:** Helpless

**Tone:** Aggressive sharp funk-rock blues, mild amp dirt, 808 lead stack.

**Amp source:** `JMOD_100` — tight huge-clean-headroom PRS J-MOD / later-era pedal platform

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.5, 'middle': 0.55, 'treble': 0.0, 'presence': 0.0}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | ON | drive: 1.3, volume_db_target: 0.0 |
| D | Kemper Drive / B Breaker Max | OFF | drive_target_0to10: 2.0 |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 285, mix_percent_target: 9, feedback_percent_target: 12 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 11.4 ROSIE

**Target songs:** Rosie, Love on the Weekend

**Tone:** Rounded chord clean, bright funk bounce, lightly chorused tails.

**Amp source:** `JMOD_100` — tight huge-clean-headroom PRS J-MOD / later-era pedal platform

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.35, 'middle': 0.15, 'treble': -0.2, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | ON | mix_percent_target: 13, rate_hz_target: 0.7 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 300, mix_percent_target: 8, feedback_percent_target: 13 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 11.5 CHANGING / WAVE

**Target songs:** Changing, Emoji of a Wave, In the Blood, Roll It on Home, Never on the Day You Leave

**Tone:** Broader dynamic clean with midrange solo excursion and longer atmospheric ambience.

**Amp source:** `JMOD_100` — tight huge-clean-headroom PRS J-MOD / later-era pedal platform

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.25, 'middle': 0.25, 'treble': -0.2, 'presence': -0.2}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = DLY, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | ON | time_ms_target: 400, mix_percent_target: 12, feedback_percent_target: 18 |
| REV | Natural Reverb / Small Plate | ON | mix_percent_target: 16, decay_seconds_target: 2.2 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

## Performance 12 — 12 SOB ROCK

### 12.1 LAST TRAIN HOME

**Target songs:** Last Train Home

**Tone:** Journeyman-inspired 80s mid-gain solo with CE-1-like chorus and spacious repeats; keep amp below fizz.

**Amp source:** `SOLDANO_SLO` — moderate gain 80s-inflected tube amp with mid focus, NOT maximum saturated channel

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.45, 'middle': 0.6, 'treble': -0.15, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / CE-1 | ON | mix_percent_target: 27, rate_hz_target: 0.7 |
| DLY | Single Delay / Digital | ON | time_ms_target: 360, mix_percent_target: 18, feedback_percent_target: 24 |
| REV | Natural Reverb / Small Plate | ON | mix_percent_target: 13, decay_seconds_target: 2.2 |

**Agent caveat:** Mayer described Silver Sky -> Soldano + chorus approach in published Guitar World interview; exact recorded settings not documented.

### 12.2 WILD BLUE

**Target songs:** Wild Blue

**Tone:** Clean mellow rhythmic Knopfler-like finger-tone; additional Ross Phaser/Distortion double part in interlude.

**Amp source:** `FENDER_BF` — dry Fender clean to lightly pushed; warmer/less subbass than Two-Rock

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.4, 'middle': 0.0, 'treble': -0.15, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | ON | intensity: 1.2 |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Phaser / Stone 1 | OFF | rate_hz_target: 0.65, mix_percent_target: 24 |
| DLY | Single Delay / Tape Slapback 1 | OFF | time_ms_target: 130, mix_percent_target: 6, feedback_percent_target: 8 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Mayer independently described using a Ross phaser on the double of guitar interlude, not necessarily main guitar track. Another reference says his scratch pass used Fractal clean. Do not assert all tracks used Fender amp.

### 12.3 NEW LIGHT

**Target songs:** New Light, Carry Me Away, Til the Right One Comes

**Tone:** Clean compressed/chorused pop guitar with minimalist 80s-width, medium slap.

**Amp source:** `FENDER_BF` — dry Fender clean to lightly pushed; warmer/less subbass than Two-Rock

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.35, 'middle': 0.0, 'treble': 0.15, 'presence': -0.05}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / CE-1 | ON | mix_percent_target: 20, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape Slapback 2 | ON | time_ms_target: 165, mix_percent_target: 9, feedback_percent_target: 9 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 12.4 FEEL LIKE OUTRO

**Target songs:** I Guess I Just Feel Like (outro fuzz)

**Tone:** EPIPHONE CASINO P-90 -> BC109 silicon fuzz family -> cranked Fender Vibro Champ, low-fi warmly clipped vocal sustain with rolled-off highs.

**Amp source:** `FENDER_CHAMP_HOT` — highly saturated small Fender combo, small speaker roll-off, not Two-Rock

**Instrument/pickups:** Closest: Epiphone Casino P-90 neck; on Strat use neck pickup with tone rolled down ~4–6 and apply post EQ shaping

**Relative amp EQ deltas:** `{'bass': -0.2, 'middle': 0.6, 'treble': -0.5, 'presence': -0.5}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = A, II = B, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Kemper Fuzz / Dark Blue Silicon | ON | drive_target_0to10: 6.5, mix_percent_target: 100, volume_db_target: 0.0 |
| B | Kemper Fuzz / Tyco Octavia Min | OFF | drive_target_0to10: 3.0 |
| C | Kemper Drive / Klon 1 | OFF | drive_target_0to10: 1.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Studio Equalizer / Vintage Mix | ON | low_cut_hz_target: 90, high_cut_hz_target: 6000, low_mid_boost_freq_hz: 400, low_mid_gain_db_target: 1.2, high_mid_cut_freq_hz: 3200, high_mid_gain_db_target: -2.0 |
| MOD | Phaser Vibe / Uni Vintage | OFF | stages: 4, rate_hz_target: 1.1, mix_percent_target: 35 |
| DLY | Single Delay / Tape | ON | time_ms_target: 260, mix_percent_target: 5, feedback_percent_target: 9 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 7, decay_seconds_target: 1.1 |

**Agent caveat:** High priority: do NOT use Sinewave clean as primary. The documented Shin-ei Psychedelic Machine offers fuzz, vibe, octavia, but there is no confirmed evidence all were active. Start fuzz ON, Octavia and Vibe OFF. Capture should already sound broken up. Not a Big Muff or Cornish NG-2 tone. A/B against alternate silicon and Muffin, record short DI loops.

### 12.5 SHOT IN DARK

**Target songs:** Shot in the Dark, Why You No Love Me, All I Want Is to Be with You, Shouldn't Matter but It Does

**Tone:** Moderate polished 80s overdrive lead with slower chorus and time-domain width.

**Amp source:** `SOLDANO_SLO` — moderate gain 80s-inflected tube amp with mid focus, NOT maximum saturated channel

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.35, 'middle': 0.4, 'treble': -0.1, 'presence': -0.1}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 2 | ON | mix_percent_target: 23, rate_hz_target: 0.5 |
| DLY | Single Delay / Tape | ON | time_ms_target: 410, mix_percent_target: 16, feedback_percent_target: 18 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

## Performance 13 — 13 BATTLE EXTRAS

### 13.1 EDGE OF DESIRE

**Target songs:** Edge of Desire

**Tone:** Bright pushed clean carrying sustained expressive lead; minimal chorus and mids from stacked 808.

**Amp source:** `TWOROCK_CR` — wide clean/edge Two-Rock; suitable Nokia Trio and Continuum

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.5, 'middle': 0.5, 'treble': 0.0, 'presence': -0.05}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = DLY, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | ON | time_ms_target: 315, mix_percent_target: 10, feedback_percent_target: 17 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 13.2 HEARTBREAK WAR

**Target songs:** Heartbreak Warfare, Perfectly Lonely

**Tone:** Spacious clean with rhythmic delay and wet modern pop edge.

**Amp source:** `TWOROCK_CR` — wide clean/edge Two-Rock; suitable Nokia Trio and Continuum

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.3, 'middle': 0.2, 'treble': 0.0, 'presence': -0.2}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = MOD, IIII = DLY

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.5 |
| DLY | Single Delay / Tape | ON | time_ms_target: 415, mix_percent_target: 17, feedback_percent_target: 22 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 13.3 CROSSROADS NG2

**Target songs:** Crossroads (Battle Studies)

**Tone:** Pete Cornish NG-2-style angular, almost gated and highly saturated fuzz, different architecture from Sob Rock outro.

**Amp source:** `SINE_LO_G1265` — very clean, wide, bass-rich high-headroom G12-65 clean

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.45, 'middle': 0.55, 'treble': -0.45, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = A, II = B, III = C, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Kemper Fuzz / Dark Blue Silicon | ON | drive_target_0to10: 8.0 |
| B | Kemper Drive / 808 Min | OFF | drive_target_0to10: 1.0 |
| C | Noise Gate 4:1 / Basic | ON | threshold: tune until staccato decay without chopping pick attack |
| D | Wah Wah / Vox Old | OFF |  |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 5 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 330, mix_percent_target: 9, feedback_percent_target: 14 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 5, decay_seconds_target: 1.0 |

**Agent caveat:** Mayer named NG-2 directly in 2010 interview and guitar volume around 4. Emulation is analog behavior approximation; do not claim modeled NG-2 circuit.

### 13.4 ASSASSIN

**Target songs:** Assassin, Half of My Heart

**Tone:** More saturated but articulate lead with medium delay and dry rhythm.

**Amp source:** `SINE_OD_M75` — captured amp overdrive with singing harmonics and Scumback M75

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.45, 'middle': 0.5, 'treble': -0.1, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = DLY, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Wah Wah / Vox Old | OFF | pedal_mode: Bypass @ Toe |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | ON | time_ms_target: 335, mix_percent_target: 11, feedback_percent_target: 13 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

### 13.5 MAYER SOUL LEAD

**Target songs:** I'm Gonna Find Another You, Covered in Rain, Slow Dancing (extended live solos), I Don't Need No Doctor

**Tone:** Two-Rock/Dumble-like expressive midrange, TS/Bluesbreaker/Klon in layers, true post-amp level boost.

**Amp source:** `SINE_M_G1265` — mid-switched clean or edge profile with additional focus

**Instrument/pickups:** Strat/Silver Sky; neck/neck-middle to start

**Relative amp EQ deltas:** `{'bass': -0.4, 'middle': 0.55, 'treble': -0.1, 'presence': -0.15}`; capture gain first, no default large Amp Gain modifications.

**Remote mapping:** I = B, II = C, III = D, IIII = X

| Module | Effect type / starting preset | State | Initial editable target |
|---|---|---|---|
| A | Compressor / Soft | OFF | intensity: 2.0, attack: use factory Soft initially |
| B | Kemper Drive / Klon 2 | OFF | drive: 1.0, volume_db_target: 0.0 |
| C | Kemper Drive / 808 Min | OFF | drive: 1.3, volume_db_target: 0.0 |
| D | Kemper Drive / B Breaker Max | OFF | drive_target_0to10: 1.5 |
| X | Pure Booster / 4dB Solo | OFF | volume_db_target: 2.0 |
| MOD | Vintage Chorus / Subtle 1 | OFF | mix_percent_target: 15, rate_hz_target: 0.65 |
| DLY | Single Delay / Tape | OFF | time_ms_target: 360, mix_percent_target: 9, feedback_percent_target: 12 |
| REV | Natural Reverb / Room | ON | mix_percent_target: 10, decay_seconds_target: 1.7 |

**Agent caveat:** Verify stored effect states, switch behavior and dynamics; defaults are sonic starting points.

## High-priority A/B: Sob Rock “I Guess I Just Feel Like” outro

This is **not** a generic overdrive and not the Pete Cornish NG-2 from Crossroads. Community gear analyses indicate Epiphone Casino P-90 + Shin-ei Psychedelic Machine + cranked Vibro Champ. The original studio stem signal path has not been independently confirmed by Mayer.

**Primary target:** Casino/P-90 tone -> **Kemper Fuzz Dark Blue Silicon** (BC109-family approximation) -> genuinely broken-up Fender Champ profile -> post-amp EQ high cut around 6kHz, low-mid push around 400Hz and slight cut near 3.2kHz -> dry-ish tape echo/room.

**Crucial:** Factory Psychedelic Machine offers fuzz, octave, and vibe, but that does not establish that Octavia and vibe were enabled on the record. Both start OFF. Try Psych 69 Silicon and Muffin Soft as A/B alternatives only, label them substitutes.

**Detailed A/B instructions:**
- **target_slot**: 12.4 FEEL LIKE OUTRO
- **reconstruction_source**: ['Epiphone Casino E230TD with two P90s', 'Cranked small Fender Vibro Champ/Champ', 'Shin-ei Psychedelic Machine reported by gear analysis']
- **manufacturer_reference**: Shin-ei describes internal effects as BC109 Fuzz, Tycobrahe-style Octave, Uni-Vibe
- **signal_priority**: P90-like front end -> silicon fuzz -> genuinely overdriven low-watt Champ capture -> 6 kHz post low-pass -> sparse echo/room
- **routing_nonnegotiables**: ['Fuzz before amplifier; do not post-amp place fuzz', 'Do not use a large pristine Two-Rock head as the primary amp', 'Do not turn on Octavia or Uni-Vibe merely because they are housed in reported Shin-ei unit', 'Use tonal A/B and match loudness within 0.5 dB before judging', 'If no Champ capture is present, pause exact-match claim and mark profile absent']
- **primary**: {'profile_key': 'FENDER_CHAMP_HOT', 'fuzz_effect': 'Kemper Fuzz', 'fuzz_preset': 'Dark Blue Silicon', 'fuzz_on': True, 'octave_off': True, 'vibe_off': True}
- **alternate_a**: {'profile_key': 'FENDER_CHAMP_HOT', 'fuzz_effect': 'Kemper Fuzz', 'fuzz_preset': 'Psych 69 Silicon', 'starting_note': 'alternate silicon clipping/feel'}
- **alternate_b**: {'profile_key': 'FENDER_CHAMP_HOT', 'fuzz_effect': 'Muffin', 'fuzz_preset': 'Soft', 'starting_note': 'nonhistorical spectral fallback if heavy compressed texture missing; labeled approximation'}
- **alternate_c**: {'profile_key': 'FENDER_TWEED', 'fuzz_effect': 'Kemper Fuzz', 'fuzz_preset': 'Dark Blue Silicon', 'starting_note': 'only if Champ unavailable; flag speaker/response mismatch'}
- **listener_test**: Compare isolated outro reference level-matched to 10-second recorded Kemper DI reamp phrases (single notes, double stops, note-decay), rank attack rounding, midrange vowel, high-frequency rolloff, controlled feedback, decay shape
- **critical_uncertainty**: Reported gear comes from fan documentation/gear analyses, not independently confirmed session stem list. Shin-ei model used does not establish which individual effects were enabled.

## All-album song tone lookup
The following is a core guitar-tone target, not a claim that every recorded layer is reproduced by one mono Kemper Rig.

### Nokia Trio live Dec 8 2007

| Song | Target Performance.Slot |
|---|---|
| Everyday I Have the Blues | 08.5 |
| Wait Until Tomorrow | 08.3 |
| Who Did You Think I Was | 08.1 |
| Come When I Call | 08.2 |
| Good Love Is on the Way | 08.2 |
| Out of My Mind | 08.5 |
| Vultures | 08.4 |
| Bold as Love | 08.3 |

### Continuum (2006)

| Song | Target Performance.Slot |
|---|---|
| Waiting on the World to Change | 09.4 |
| I Don't Trust Myself (With Loving You) | 09.1 |
| Belief | 09.4 |
| Gravity | 09.2 |
| The Heart of Life | 09.2 |
| Vultures | 08.4 |
| Stop This Train | 10.5 |
| Slow Dancing in a Burning Room | 09.3 |
| Bold as Love | 08.3 |
| Dreaming with a Broken Heart | 09.5 |
| In Repair | 09.5 |
| I'm Gonna Find Another You | 09.5 |

### Battle Studies (2009)

| Song | Target Performance.Slot |
|---|---|
| Heartbreak Warfare | 13.2 |
| All We Ever Do Is Say Goodbye | 10.4 |
| Half of My Heart | 13.4 |
| Who Says | 10.5 |
| Perfectly Lonely | 13.2 |
| Assassin | 13.4 |
| Crossroads | 13.3 |
| War of My Life | 10.4 |
| Edge of Desire | 13.1 |
| Do You Know Me | 10.5 |
| Friends, Lovers or Nothing | 13.5 |

### Born and Raised (2012)

| Song | Target Performance.Slot |
|---|---|
| Queen of California | 10.1 |
| The Age of Worry | 10.5 |
| Shadow Days | 10.5 |
| Speak for Me | 10.5 |
| Something Like Olivia | 10.1 |
| Born and Raised | 10.2 |
| If I Ever Get Around to Living | 10.2 |
| Love Is a Verb | 10.1 |
| Walt Grace's Submarine Test, January 1967 | 10.5 |
| Whiskey, Whiskey, Whiskey | 10.2 |
| A Face to Call Home | 10.2 |
| Born and Raised (Reprise) | 10.5 |

### Paradise Valley (2013)

| Song | Target Performance.Slot |
|---|---|
| Wildfire | 10.3 |
| Dear Marie | 10.4 |
| Waitin' on the Day | 10.4 |
| Paper Doll | 10.3 |
| Call Me the Breeze | 10.3 |
| Who You Love | 10.4 |
| I Will Be Found (Lost at Sea) | 10.5 |
| Wildfire (Reprise) | 10.5 |
| You're No One 'Til Someone Lets You Down | 10.5 |
| Badge and Gun | 10.5 |
| On the Way Home | 10.4 |

### The Search for Everything (2017)

| Song | Target Performance.Slot |
|---|---|
| Still Feel Like Your Man | 11.1 |
| Emoji of a Wave | 11.5 |
| Helpless | 11.3 |
| Love on the Weekend | 11.4 |
| In the Blood | 11.5 |
| Changing | 11.5 |
| Theme from The Search for Everything | 11.5 |
| Moving On and Getting Over | 11.2 |
| Never on the Day You Leave | 11.5 |
| Rosie | 11.4 |
| Roll It on Home | 11.5 |
| You're Gonna Live Forever in Me | 10.5 |

### Sob Rock (2021)

| Song | Target Performance.Slot |
|---|---|
| Last Train Home | 12.1 |
| Shouldn't Matter but It Does | 12.5 |
| New Light | 12.3 |
| Why You No Love Me | 12.5 |
| Wild Blue | 12.2 |
| Shot in the Dark | 12.5 |
| I Guess I Just Feel Like | 12.4 |
| Til the Right One Comes | 12.3 |
| Carry Me Away | 12.3 |
| All I Want Is to Be with You | 12.5 |

## Execution instructions (for a desktop agent)

1. Read connected device details and software/firmware versions. Build inventory of existing Performances 1-13 and amp source Rigs; do not write yet.
2. Backup all current profiler content and save screenshots. Any occupied desired destination 07..13 requires alternate unused slot selection or explicit approval to overwrite.
3. Search Sinewave pack using metadata tags: Sig/Lo/M/OD/G1265/M75, not fabricated exact Rig names; prefer Studio over Direct if using existing capture cabinet.
4. Find Fender Champ driven profile and Soldano SLO profile by source, rated dynamic accuracy, version and cab; if missing, search Rig Exchange, do not assert that arbitrary free files are authenticated.
5. Create each Performance and each slot per JSON, selecting a best-fit source Rig with captured drive amount. Preserve cabinet unless clear reason to substitute.
6. Load only documented Kemper effect types/presets. Enter initial state and approximate numeric target ranges; record actual UI setting after update. For empty effects use Type None.
7. For special filters, set Touch response in Wah Low Pass and confirm on-screen fields. For slicer set 1/8 Slicer at 84 BPM; it cannot reproduce full AdrenaLinn resonant sequencing by itself.
8. Assign upper Remote effects separately in each Rig, verify assignments and initial states persist after changing slots.
9. Configure any wah pedal to Wah only; do not overwrite a functional pedal configuration without backup.
10. Store all Performances in My Profiler, not only computer Local Library. Reboot or change Performances then inspect state after reload.
11. Record 10-second reference dry/lead reamp examples for each distinct amp family, keep loudness matched, adjust Rig Volume only for cross-bank normalization.
12. For Sob 12.4 conduct A/B fuzz procedure and archive primary plus alternatives as local Rig copies. Choose final based on measured spectral/attack similarity and ear, not brand/model assumption.
13. Deliver final ledger of exact original profile name, selected cabinet, full actual setting values, footswitch map and changed global settings for each rig. Flag any unverified tones and missing profiles.

## Acceptance criteria

- [ ] 7 Performances at confirmed free destinations, with five named slots each; no accidental overwrite of any occupied location.
- [ ] 35 sound slots can be selected from Remote and recall exactly after changing bank and returning.
- [ ] Sinewave pack profile tags match selected sounds; no non-existent capture filenames are asserted.
- [ ] Every effect has a valid existing effect type and preset or is marked None/custom with UI verification.
- [ ] Each Rig retains four switch assignments and intended initial effect states, with A/B/alternate modules per specification.
- [ ] Mayer Sob 12.4 uses a driven Champ-family capture, fuzz before amp, EQ high cut, octave/vibe OFF initially, and separate alternate audition notes.
- [ ] Wah pedal is calibrated; not unexpectedly changing volume; effects bypass at toe where needed.
- [ ] No unintended source/library or system/global setting changes; all existing performances backed up.
- [ ] All changes are auditable with before/after screenshots or setting export and profile list.

## Verification and provenance

- All numerical values are engineering targets and must be confirmed in current Rig Manager. Some values are relative or conceptual, not literal Rig Manager fields.
- Exact profile filenames cannot be known from a product sales page.
- Tube amps and cabinet variations cannot be recreated by large Profile Gain edits; use matching captured amplifier sounds.
- Some recorded multitracks, acoustic guitars and parallel amps are not reproducible in one mono Rig; document substitutes.

### Sources

- [Kemper drive/fuzz](https://www.kemper-amps.com/effects/distortion)
- [Kemper tremolo/slicer](https://www.kemper-amps.com/effects/tremolo)
- [Kemper chorus](https://www.kemper-amps.com/effects/chorus)
- [Kemper delay](https://www.kemper-amps.com/effects/delay)
- [Kemper reverb](https://www.kemper-amps.com/effects/reverb)
- [Kemper phaser](https://www.kemper-amps.com/effects/phaser-and-flanger)
- [Kemper compressor](https://www.kemper-amps.com/effects/compressor)
- [Kemper EQ](https://www.kemper-amps.com/effects/equalizer)
- [Sinewave pack](https://tonejunkiestore.com/profile-packs/p/official-sinewave-continuum-od-kemper-profile-pack)
- [Nokia show list](https://www.nugs.net/live-download-of-john-mayer-where-the-light-is%3A-nokia-theatre-los-angeles-ca-12-08-2007-mp3-flac-or-online-music-streaming/20827.html)
- [Mayer first person gear (2010 interview)](https://johnmayer.info/subjects/gear)
- [Mayer Sob Rock 2021 interview](https://www.guitarworld.com/features/john-mayer-sob-rock)
- [Shin-ei official circuit description](https://www.shin-ei.com/)
- [Casino photo background](https://www.groundguitar.com/john-mayer-guitars-and-gear/john-mayers-epiphone-casino-e230td/)
- [Outtro reconstruction](https://www.jonkaneshiroguitar.com/products/line-6-helix-hx-stomp-john-mayer-i-guess-i-just-feel-like)
- [Mayer NG2 first person interview](https://www.musicradar.com/news/john-mayer-interview-251957)
- [Mayer gear eras](https://www.guitarworld.com/features/john-mayers-guitar-gear-era-by-era)
- [Wild Blue Ross](https://equipboard.com/albums/john-mayer-last-train-home-ballad-version)