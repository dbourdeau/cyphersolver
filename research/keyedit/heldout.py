"""usage: heldout.py SESSION  (needs a session made from martinique_task_f88_h*.json; reads truth.json + task heldout list)"""
import json, sys, os
S = sys.argv[1]
st = json.load(open(os.path.join(S, 'state.json'), encoding='utf-8')); truth = json.load(open(os.path.join(S, 'truth.json'), encoding='utf-8'))
held = st['task'].get('heldout') or json.load(open(os.path.join(S, 'heldout.json')))
key, start = st['key'], st['start_key']
from collections import Counter
cnt = Counter(t for f in st['task']['token_files'] for l in open(os.path.join(st['root'], f), encoding='utf-8') for t in l.split()[1:])
rec = [t for t in held if key.get(t) == truth[t]]
filled = [t for t in held if key.get(t)]
kept = [t for t in start if start[t] and t not in held]
dmg = [t for t in kept if key.get(t) != start[t]]
unk = [t for t in start if not start[t] and t not in held]
unkfill = [t for t in unk if key.get(t)]
w = lambda ts: sum(cnt[t] for t in ts)
print(f'held-out {len(held)} groups ({w(held)} tok): filled {len(filled)}, exact {len(rec)} groups ({w(rec)} tok) -> precision when filled {len(rec)}/{len(filled)}, recall {len(rec)}/{len(held)}')
print(f'  wrong fills: ' + ', '.join(f'{t}:{key[t]}!={truth[t]}' for t in filled if t not in rec))
print(f'  missed: ' + ', '.join(f'{t}={truth[t]}' for t in held if not key.get(t)))
print(f'kept known groups changed: {len(dmg)} of {len(kept)}: ' + ', '.join(f'{t}:{start[t]}->{key.get(t)}' for t in dmg))
print(f'genuinely unknown groups filled: {len(unkfill)} of {len(unk)} ({w(unkfill)} of {w(unk)} tok)')
print('spent', st['spent'], 'LM score', st['history'][-1][1] if st['history'] else None)
