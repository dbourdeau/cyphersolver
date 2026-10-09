import json, sys, re
sys.path.insert(0, '.')
from parse1890 import toks
key = json.load(open('key1889.json')); key['6'] = 'e'
extra = json.load(open('key1890_extra.json')) if __import__('os').path.exists('key1890_extra.json') else {}
key.update(extra)
def clean(t):
    t = t.replace('?', '').replace('_.', '').replace('.', '')
    m = {'l/z': 'z', 'l/zp': ['z', 'p'], 'l/z6': ['z', '6'], 'pla/u': 'plu', 'ple/i': 'ple', 'c/1o/0': ['co'], 'g^a': ['ga']}
    if t in m: v = m[t]; return v if isinstance(v, list) else [v]
    return [t]
lines = []; cur = []
for t in toks:
    if t == '/': lines.append(cur); cur = []; continue
    if t in '|()': continue
    cur += clean(t)
if cur: lines.append(cur)
known = unk = 0
for L in lines:
    out = []
    for t in L:
        v = key.get(t)
        if v is None: out.append('[' + t + ']'); unk += 1
        else: out.append(v.upper() if t in extra else v); known += 1
    print(''.join(out))
print('known', known, 'unknown', unk)
