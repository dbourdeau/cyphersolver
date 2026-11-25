"""SECONDARY: Lasry's key on 225-sign windows of his own no. 95 with a share of signs replaced by holes ('?'), to show
what the solver's measure gives for a correct key when the transcription has as many holes as mine (47 of 234 = 20%)."""
import sys, os, random
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
rng = random.Random(20)
for share in (0.05, 0.10, 0.15, 0.20):
    sc = []
    for i in range(0, len(rows) - 224, 225):
        for rep in range(20):
            w = list(rows[i:i+225])
            for j in rng.sample(range(225), int(round(share*225))): w[j] = 'HOLE'
            sc.append(wl2857.sandwich_measure(seg, decode(w, key), 3)[0])
    sc.sort()
    print(f"holes {share:.0%}: {len(sc)} trials, min {sc[0]:.3f} median {sc[len(sc)//2]:.3f} max {sc[-1]:.3f}; share >= 0.70: {sum(s>=0.7 for s in sc)/len(sc):.2f}")
