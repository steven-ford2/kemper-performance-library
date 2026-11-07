# Jimi Hendrix: Kemper tone configuration

**Status:** reconstructed_from_full_current_conversation_and_prior_discussion. No patches have been installed or tested.

**Machine-readable source:** [`../../specs/hendrix.json`](../../specs/hendrix.json).

## Canonical Performance locations (subject to device inventory)

| Perf | Name | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 |
|---:|---|---|---|---|---|---|
| 08 | HENDRIX CORE | EXPERIENCED | AXIS | LADYLAND | GYPSYS | CRY LOVE |
| 09 | HENDRIX 1967 | HEY JOE/WIND | PURPLE HAZE | FOXEY/MANIC | LITTLE WING | BOLD/SPANISH |
| 10 | HENDRIX LADYLAND | VOODOO RETURN | WATCHTOWER | VOODOO CHILE | CROSSTOWN | GYPSY/1983 |
| 11 | HENDRIX GYPSYS | MACHINE GUN | WHO KNOWS | POWER SOUL | MESSAGE LOVE | BOG FUNK |
| 12 | HENDRIX CRY LOVE | FREEDOM/EZY | NIGHT/STORM | ANGEL/DRIFT | STRAIGHT/BELLY | ASTRO/FRIEND |

## Implementation detail

For each slot, start from the indicated **captured amp gain family**. Relative EQ offsets are starting values **added to the selected capture**, not physical vintage amp dial positions. Every rig has modules A/B/C/D before amp and X/MOD/DLY/REV after amp. A target only exists if that parameter is available in the installed software.

### 08. HENDRIX CORE
#### Slot 1: EXPERIENCED
**Songs:** Purple Haze, Foxey Lady, Fire, Manic Depression
**Profile selector:** JTM45/100 or JTM100 into vintage Greenback 4x12
**Tone:** Early 1967 fierce open Marshall, germanium fuzz and discrete Octavia on solo
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.4, "middle": 0.5, "treble": 0.0, "presence": 0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | ON | {} |
| D | Tremolo | none | OFF | {'rate_hz_target': 4.0, 'depth': 'low'} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** No Uni-Vibe asserted on the first album. Purple Haze solo uses Octavia separately.

#### Slot 2: AXIS
**Songs:** Little Wing, Castles Made of Sand, Bold as Love, Spanish Castle Magic
**Profile selector:** JTM100 clean-to-edge or Sound City-inspired clean; vintage 4x12
**Tone:** Warm chord articulation; Leslie/rotary and studio flanging rather than generic vibe
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Flanger | Subtle | OFF | {'mix_percent_target': 30, 'rate_hz_target': 0.16} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | ON | {'speed': 'Slow', 'mix_percent_target': 85} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→MOD, IIII→D

**Notes:** Axis tape flanging cannot be reproduced exactly by an algorithmic flanger.

#### Slot 3: LADYLAND
**Songs:** Voodoo Child (Slight Return), All Along the Watchtower, Gypsy Eyes, 1983
**Profile selector:** Super Lead 100, Greenback 4x12 mid-crunch
**Tone:** Dense 1968 studio rock with wah, tape effects and driven Plexi response
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Flanger | Subtle | OFF | {'mix_percent_target': 35} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** 1968 studio Univibe assignment is not assumed; 1983 cannot be recreated as one mono live rig.

#### Slot 4: GYPSYS
**Songs:** Machine Gun, Who Knows, Power of Soul, Message to Love
**Profile selector:** late-60s Super Lead/JMP + vintage 4x12, moderate driven capture
**Tone:** 1969-70 live punch, silicon fuzz, expressive wah, Uni-Vibe
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Psych 69 Silicon | OFF | {} |
| D | Phaser Vibe | Uni Vintage | ON | {'stages': 4, 'rate_hz_target': 1.35, 'mix_percent_target': 75} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 5, 'decay_seconds_target': 1.1} |

**Remote:** I→C, II→B, III→D, IIII→X

**Notes:** Vibe on, fuzz off initially for Machine Gun; switch I enables fuzz.

#### Slot 5: CRY LOVE
**Songs:** Freedom, Ezy Ryder, Angel, Drifting, Night Bird Flying
**Profile selector:** Super Lead 100, clean-to-edge profile and vintage 4x12
**Tone:** 1970 expressive studio, cleaner foundation than Gypsys and variable fuzz
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Psych 69 Silicon | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 14, 'decay_seconds_target': 2.1} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Cry of Love released posthumously in 1971; verify individual recording era / overdubs.

### 09. HENDRIX 1967
#### Slot 1: HEY JOE/WIND
**Songs:** Hey Joe, The Wind Cries Mary, May This Be Love
**Profile selector:** clean JTM100 / JTM45-era amp
**Tone:** Early clean-to-edge and air
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 9, 'decay_seconds_target': 1.3} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Fuzz/Octavia off by default.

#### Slot 2: PURPLE HAZE
**Songs:** Purple Haze, Stone Free, Highway Chile
**Profile selector:** early Marshall plexi/JTM at crunch
**Tone:** Tearing upper mids and discrete Octavia solo
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | ON | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Switch II Octavia for solo; compare fuzz bypass when octave loses clarity.

#### Slot 3: FOXEY/MANIC
**Songs:** Foxey Lady, Manic Depression, Fire, I Don’t Live Today
**Profile selector:** early Marshall crunch, greenback 4x12
**Tone:** Aggressive raspy fuzz and dry amp
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | ON | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Avoid modern preamp saturation.

#### Slot 4: LITTLE WING
**Songs:** Little Wing, Castles Made of Sand, One Rainy Wish
**Profile selector:** clean Marshall/Sound City-ish capture
**Tone:** Clean edge, slow Leslie/rotary, touch-responsive
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | ON | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→MOD, IIII→DLY

**Notes:** Use slow Rotary Speaker in MOD and minimal clipping.

#### Slot 5: BOLD/SPANISH
**Songs:** Bold as Love, Spanish Castle Magic, If 6 Was 9, Up from the Skies
**Profile selector:** mid-crunch Marshall or edge capture
**Tone:** Fuzz and controllable tape-style modulation
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Flanger | Subtle | OFF | {'mix_percent_target': 30} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Tape-flanged Bold as Love outro is a studio-production approximation.

### 10. HENDRIX LADYLAND
#### Slot 1: VOODOO RETURN
**Songs:** Voodoo Child (Slight Return)
**Profile selector:** mid-crunch Super Lead 100
**Tone:** Strong wah sweep into cranked Marshall
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.5, "middle": 0.6, "treble": 0, "presence": 0}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Prefer wah expression as primary tone control; fuzz optional.

#### Slot 2: WATCHTOWER
**Songs:** All Along the Watchtower, Come On (Part I)
**Profile selector:** mid-gain Super Lead / JMP 100
**Tone:** Melodic compressed lead without artificial high-gain amp
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 340, 'mix_percent_target': 12, 'feedback_percent_target': 18} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Recorded multitracked electric/acoustic parts are separate; this is core lead approximation.

#### Slot 3: VOODOO CHILE
**Songs:** Voodoo Chile (long), Rainy Day, Dream Away, Still Raining, Still Dreaming
**Profile selector:** clean-to-edge Marshall capture
**Tone:** Round blues clean into drive when guitar output is raised
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Big clean dynamics, minimal modulation.

#### Slot 4: CROSSTOWN
**Songs:** Crosstown Traffic, Burning of the Midnight Lamp, Long Hot Summer Night
**Profile selector:** mid-crunch Super Lead
**Tone:** Nasal biting fuzz; tight rhythm
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | ON | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Do not fake kazoo/doubling as part of single fuzz effect.

#### Slot 5: GYPSY/1983
**Songs:** Gypsy Eyes, House Burning Down, 1983, ...And the Gods Made Love
**Profile selector:** relatively clean British amp capture
**Tone:** Complex 1968 studio flanging and delays
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Flanger | Subtle | ON | {'rate_hz_target': 0.2, 'mix_percent_target': 35} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 375, 'mix_percent_target': 20, 'feedback_percent_target': 17} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** Requires overdubs/DAW for full record texture; core electric tone only.

### 11. HENDRIX GYPSYS
#### Slot 1: MACHINE GUN
**Songs:** Machine Gun
**Profile selector:** late Super Lead/JMP with open 4x12
**Tone:** Vibe dominated feedback and aggressive, not fizzy, silicon fuzz
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Psych 69 Silicon | OFF | {} |
| D | Phaser Vibe | Uni Vintage | ON | {'stages': 4, 'rate_hz_target': 1.35, 'mix_percent_target': 75} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 5, 'decay_seconds_target': 1.1} |

**Remote:** I→C, II→B, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 2: WHO KNOWS
**Songs:** Who Knows
**Profile selector:** late 100 W JMP; punchy open 4x12
**Tone:** Snarling dry late Hendrix fuzz
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Psych 69 Silicon | ON | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 4, 'decay_seconds_target': 1.0} |

**Remote:** I→C, II→B, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 3: POWER SOUL
**Songs:** Power of Soul, Power to Love
**Profile selector:** late JMP high-headroom cranked
**Tone:** Thick fuzz + vibe rock funk
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Psych 69 Silicon | ON | {} |
| D | Phaser Vibe | Uni Vintage | ON | {'stages': 4, 'rate_hz_target': 1.5, 'mix_percent_target': 72} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 4: MESSAGE LOVE
**Songs:** Message to Love, Message of Love
**Profile selector:** later JMP mid driven
**Tone:** Articulated midrange and restrained modulation
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Psych 69 Silicon | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→X

**Notes:** None; evaluate by ear.

#### Slot 5: BOG FUNK
**Songs:** Changes, We Gotta Live Together
**Profile selector:** late Marshall edge-of-breakup capture
**Tone:** Low-gain, dynamic live funk from Band of Gypsys
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→X

**Notes:** None; evaluate by ear.

### 12. HENDRIX CRY LOVE
#### Slot 1: FREEDOM/EZY
**Songs:** Freedom, Ezy Ryder
**Profile selector:** late Marshall 100 W driven
**Tone:** Tight layered rhythm and open expressive lead
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.45, "middle": 0.55, "treble": 0, "presence": 0}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 2: NIGHT/STORM
**Songs:** Night Bird Flying, In From the Storm
**Profile selector:** later Marshall 100 W mid crunch
**Tone:** Warm forward studio lead, less raw than BOG
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 3: ANGEL/DRIFT
**Songs:** Angel, Drifting
**Profile selector:** late Marshall clean / edge
**Tone:** Very clear warm layered-clean with spatial ambience
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | ON | {'time_ms_target': 390, 'mix_percent_target': 13, 'feedback_percent_target': 17} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 16, 'decay_seconds_target': 2.4} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** True harp and multitracked sources not reproducible by a single Rig.

#### Slot 4: STRAIGHT/BELLY
**Songs:** Straight Ahead, Belly Button Window
**Profile selector:** late Marshall clean edge
**Tone:** Bare articulate guitar with little effect density
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 7, 'decay_seconds_target': 1.2} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** None; evaluate by ear.

#### Slot 5: ASTRO/FRIEND
**Songs:** Astro Man, My Friend
**Profile selector:** period-correct low-drive guitar or acoustic simulator
**Tone:** Intermediate clean-to-driven 1970 sound; My Friend predates main sessions
**Guitar/Pickup:** Guitar-dependent; see tone target. Do not change the guitar without approval.
**EQ offsets:** `{"bass": -0.2, "middle": 0.25, "treble": 0.0, "presence": -0.1}`
**Gain:** Select the closest captured gain before adjusting Kemper Amp Gain; no more than ±0.7 initially.

| Module | Effect | Suggested preset | Start | Candidate targets |
|---|---|---|---|---|
| A | Wah Wah | Vox Old | OFF | {'pedal_mode': 'Bypass @ Toe'} |
| B | Kemper Fuzz | Mayer Octavia Min | OFF | {} |
| C | Kemper Fuzz | Red Germanium | OFF | {} |
| D | Phaser Vibe | Uni Vintage | OFF | {'stages': 4, 'rate_hz_target': 1.2, 'mix_percent_target': 65} |
| X | Pure Booster | none | OFF | {'volume_db_target': 2.0} |
| MOD | Rotary Speaker | Slow | OFF | {'speed': 'Slow', 'mix_percent_target': 70} |
| DLY | Single Delay | Tape | OFF | {'time_ms_target': 320, 'mix_percent_target': 9, 'feedback_percent_target': 12} |
| REV | Natural Reverb | Room | ON | {'mix_percent_target': 10, 'decay_seconds_target': 1.6} |

**Remote:** I→C, II→B, III→D, IIII→DLY

**Notes:** My Friend: actual acoustic-based recording needs acoustic source, do not claim electric exactness.

## Provenance
All specification values are initial engineering targets. Names such as `Kemper Drive / 808 Min` are candidates; verify against the device and installed preset list. Exact owned profile names are not known. Historical authenticity is not guaranteed. See `docs/procedures/build-and-verify.md`.
