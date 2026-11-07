#!/usr/bin/env python3
"""Static, read-only structural validator. No USB/MIDI/GUI access."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
modules={'A','B','C','D','X','MOD','DLY','REV'}
errors=[]
def bad(s):errors.append(s)
reg=json.loads((ROOT/'data/performance_registry.json').read_text())['canonical_registry']
seen=set()
map_by_number={}
count=0
for name in ('mayer','hendrix','srv','clapton','robben-ford','shred-triad','van-halen','timmons-govan','eagles','eagles-early','polyphia','eric-johnson','jeff-beck','yngwie','fleetwood-rumours','metalcore'):
 path=ROOT/f'specs/{name}.json'
 data=json.loads(path.read_text())
 for p in data['performances']:
  number=p['proposed_global_performance_number']
  if number in seen:bad(f'duplicate Performance {number}')
  map_by_number[number]=(name,p)
  seen.add(number)
  if len(p['slots'])!=5:bad(f'{name}/{number}: has {len(p["slots"])} slots')
  for i,rig in enumerate(p['slots'],1):
   count+=1
   if rig['slot'] != i:bad(f'{name}/{number}: slot index mismatch {i}')
   fx=rig['effects']
   if set(fx)!=modules:bad(f'{name}/{number}.{i}: module mismatch')
   sw=rig['remote_buttons']
   if set(sw)!={'I','II','III','IIII'}:bad(f'{name}/{number}.{i}: switch labels mismatch')
   for b,ass in sw.items():
    if not isinstance(ass,list) or any(s not in fx for s in ass):bad(f'{name}/{number}.{i}: bad assignment {b}={ass}')
   if not rig.get('capture_selector'):bad(f'{name}/{number}.{i}: missing capture selector')
   if rig.get('calibration_status')!='not_auditioned':bad(f'{name}/{number}.{i}: surprising calibration status')
   for mod,block in fx.items():
    if not {'type','preset_candidate','initial_active','parameter_targets','notes'} <= set(block):bad(f'{name}/{number}.{i}/{mod}: incomplete effect spec')
    if not isinstance(block['initial_active'],bool):bad(f'{name}/{number}.{i}/{mod}: not boolean')
if set(seen)!=set(range(1,44)):bad('performance locations expected 1-43 contiguous')
if len(reg)!=43:bad('registry should have 43 entries')
legacy=json.loads((ROOT/'specs/mayer-continuum-five-song-legacy.json').read_text())
if len(legacy['slots'])!=5:bad('legacy Continuum must have five slots')
else:
 for i,r in enumerate(legacy['slots'],1):
  if r['slot']!=i or set(r['effects'])!=modules:bad(f'legacy Continuum slot {i}: invalid')
backlog=json.loads((ROOT/'specs/expansion-backlog.json').read_text())
for x in backlog['artists']:
 if len(x['proposed_slots'])!=5 or not isinstance(x['requested_song_targets'],list):bad(f'bad backlog {x["slug"]}')
for r in reg:
 if r['global_number'] not in seen:bad(f'registry unexpected number {r}')
 else:
  slug,p=map_by_number[r['global_number']]
  if slug!=r['artist_slug']:bad(f'registry source slug mismatch at {r["global_number"]}')
  if p['name']!=r['name']:bad(f'registry name mismatch at {r["global_number"]}')
  if [x['name'] for x in p['slots']]!=r['slots']:bad(f'registry slots mismatch at {r["global_number"]}')
# Do not equate file correctness to an installed or audio-verified result
if errors:
 print('\n'.join(f'ERROR: {x}' for x in errors))
 sys.exit(1)
print(f'VALID: {len(seen)} proposed Performances, {count} candidate Rigs, 8 modules each, 4 Remote effect buttons each.')
print('Status: JSON structural consistency ONLY. No connection, preset existence, audio match or device write verified.')
