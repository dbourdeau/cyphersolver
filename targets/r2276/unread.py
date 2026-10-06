"""List the unread sign spans per line (signs aligned to '?' or skipped) under the current reading."""
import os, sys
os.environ.setdefault('KEY', 'key_v8.json')
import check
from decode import load
L = dict(load(['t1.txt', 't2.txt', 't3.txt'])); rd = {}
for line in open(sys.argv[1] if len(sys.argv) > 1 else 'reading.txt', encoding='utf8'):
    if ':' in line and not line.startswith('#'):
        k, v = line.split(':', 1); rd[k.strip()] = v.strip()
tot=0
for name, toks in L.items():
    toks = [t for t in toks if t != '...']
    text = check.norm(rd.get(name,'').replace('*','').replace('?', '').replace('[...]', '')).replace('[', '').replace(']', '')
    out=[]; n=0
    for i,(t, ch) in enumerate(check.align(toks, text)):
        if t is None: out.append('+'+ch); continue
        vs = check.vals(t)
        if ch or '' in vs and ch=='': out.append(t if ch in vs else f'{t}={ch}') if ch else out.append(t+'=0')
        else: out.append('['+t+']'); n+=1
    tot+=n
    if n: print(f'{name} ({n}): {rd.get(name,"")}\n   '+' '.join(out))
print('unread',tot)
