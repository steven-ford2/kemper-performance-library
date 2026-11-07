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
for name in ('favorites','mayer','hendrix','srv','clapton','robben-ford','shred-triad','van-halen','timmons-govan','eagles','eagles-early','polyphia','eric-johnson','jeff-beck','yngwie','fleetwood-rumours','metalcore'):
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
if set(seen)!=set(range(1,49)):bad('performance locations expected 1-48 contiguous')
if len(reg)!=48:bad('registry should have 48 entries')
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
# Favorites must occupy 01-05 and preserve each full source Rig sound and effects assignments.
favorites=json.loads((ROOT/'specs/favorites.json').read_text())['performances']
if [p['proposed_global_performance_number'] for p in favorites]!=[1,2,3,4,5]:
 bad('Favorites must be first numeric Performances 01-05')
for fp in favorites:
 for rig in fp['slots']:
  src=rig.get('favorite_source',{})
  old=src.get('original_performance_number')
  shifted=src.get('shifted_performance_number')
  source_slot=src.get('source_slot')
  if not isinstance(old,int) or not isinstance(source_slot,int) or shifted!=old+5 or shifted not in map_by_number:
   bad(f'Missing or invalid source for favorite {fp["name"]}/{rig["name"]}')
   continue
  p=map_by_number[shifted][1]
  if not 1<=source_slot<=len(p['slots']):
   bad(f'Favorite source slot out of range: {fp["name"]}')
   continue
  actual=p['slots'][source_slot-1]
  for key in ('effects','remote_buttons','capture_selector','tone_target','amp_eq_offsets','amp_gain_policy'):
   if rig.get(key)!=actual.get(key):bad(f'Favorite {fp["name"]}/{rig["name"]} changed source {key}')
# Do not equate file correctness to an installed or audio-verified result
if errors:
 print('\n'.join(f'ERROR: {x}' for x in errors))
 sys.exit(1)
print(f'VALID: {len(seen)} proposed Performances, {count} candidate Rigs, 8 modules each, 4 Remote effect buttons each.')
print('Status: JSON structural consistency ONLY. No connection, preset existence, audio match or device write verified.')
