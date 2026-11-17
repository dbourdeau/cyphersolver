"""SECONDARY to T3: Lasry's key on each disjoint 225-sign window of his own no. 95 transcription, solver's measure."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wl2857
key = {}
for line in open(sys.argv[1], encoding='utf8'):
    if line.startswith('#') or ' - ' not in line: continue
    signs, v = line.rstrip('\n').rsplit(' - ', 1)
    for s in signs.split('|'): key[s] = v
rows = []
for line in open(sys.argv[2], encoding='utf8'):
    if line.startswith('#') or not line.strip(): continue
    rows += [t for t in line.strip().split(';') if t]
def decode(toks, k):
    segs, cur = [], ''
    for t in toks:
        v = k.get(t, '?')
        if len(v) == 1 and v.isalpha(): cur += v.lower()
        elif v == '[null?]': continue
        elif v == '?': cur += '?'
        else: segs.append(cur); cur = ''
    segs.append(cur); return [s for s in segs if s]
seg = wl2857.Seg(wl2857.build_claver_pulgar_long(sys.argv[3], sys.argv[4], 4, 5))
sc = []
for i in range(0, len(rows) - 224, 225):
    s = wl2857.sandwich_measure(seg, decode(rows[i:i+225], key), 3)[0]; sc.append(s); print(f"signs {i}-{i+224}: {s:.3f}")
print(f"windows {len(sc)}: min {min(sc):.3f} mean {sum(sc)/len(sc):.3f} max {max(sc):.3f}; below 0.70: {sum(s<0.7 for s in sc)}")
