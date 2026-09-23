"""Two measures over reading.txt: strict (sign agrees with key) and sense (sign aligned to a letter of a read word,
or a declared null; signs under '?' or skipped count as unread)."""
import os, sys, json
os.environ.setdefault('KEY', 'key_v7.json')
import check
from decode import load
L = dict(load(['t1.txt', 't2.txt', 't3.txt'])); rd = {}
for line in open(sys.argv[1] if len(sys.argv) > 1 else 'reading.txt', encoding='utf8'):
    if ':' in line and not line.startswith('#'):
        k, v = line.split(':', 1); rd[k.strip()] = v
tot = strict = sense = 0; per = {}
for name, toks in L.items():
    toks = [t for t in toks if t != '...']; tot += len(toks)
    if name not in rd: continue
    text = check.norm(rd[name].replace('*','').replace('?', '').replace('[...]', '')).replace('[', '').replace(']', '')
    s1 = s2 = 0
    for t, ch in check.align(toks, text):
        if t is None: continue
        vs = check.vals(t)
        if ch in vs or (ch == '' and '' in vs): s1 += 1; s2 += 1
        elif ch: s2 += 1
    strict += s1; sense += s2; per[name] = (s1, s2, len(toks))
print(f'strict {strict}/{tot} = {strict/tot:.3f}   sense {sense}/{tot} = {sense/tot:.3f}')
