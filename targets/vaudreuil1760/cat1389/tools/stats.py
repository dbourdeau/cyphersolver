"""Reading statistics: python tools/stats.py  (tokens read / unresolved / lost in the gutter)"""
import json, re, sys
sys.path.insert(0, 'tools')
from lines import lines
def spans(s):
    out = set()
    for p in [x for x in s.split(',') if x]:
        a, _, b = p.partition('-'); out.update(range(int(a), int(b or a) + 1))
    return out
gaps = json.load(open('gaps.json'))
restored = json.load(open('restored.json'))
rest = full3 = 0
tot = clear = part = unres = 0
for fol, n, cur in lines():
    g = spans(gaps.get(f'{fol}.{n}', ''))
    for i, (t, v) in enumerate(cur, 1):
        if not t or t.startswith('('): continue
        if t.startswith('['): clear += 1; continue
        tot += 1
        if t.endswith('~'):
            digits = len(t.rstrip('?~'))
            if digits >= 3: full3 += 1
            elif f'{fol}.{n}' in restored: rest += 1
            else: part += 1
        elif i in g: unres += 1
solo = sum(re.sub(r'\[[^\]]*\]|\([^)]*\)', '', l).split().count('~') for l in open('transcription.txt', encoding='utf8') if not l.startswith('#') and not l.startswith('@'))
print('number groups seen complete or partly:', tot, '| clear words:', clear)
print('three digits visible at the gutter (counted read):', full3, '| restored from 1-2 visible digits + context (counted read):', rest)
print('partly visible at the gutter, not restored:', part, '| groups wholly lost at the gutter (standalone ~):', solo)
allg = tot + solo
print('all groups (seen + wholly lost):', allg)
read = tot - part - unres
print('read (complete groups giving sense):', read, f'= {100*read/allg:.1f}% of all groups, {100*read/(tot-part):.1f}% of the complete groups')
print('legible but unread:', unres, f'= {100*unres/allg:.1f}%')
print('gutter-lost (partial + wholly lost):', part + solo, f'= {100*(part+solo)/allg:.1f}%')
