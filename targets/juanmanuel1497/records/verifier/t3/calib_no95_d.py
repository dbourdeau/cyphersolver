"""Fourth calibration (lists: Claver + Pulgar forms of 4+ letters seen 2+ or 5+ times) on Lasry's no. 95 (before 2857 is decoded): Claver-only word list vs Claver+Pulgar>=2,
plain coverage (LMIN 3) and the sandwich variant. 1,000 permutations, seed 95.
python3 -I calib_no95_c.py <key.txt> <transcription_all.txt> <claver_tsv> <pulgar_txt>"""
import sys, random, os
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
letters = sorted(s for s, v in key.items() if len(v) == 1 and v.isalpha())
def decode(toks, k):
    segs, cur = [], ''
    for t in toks:
        v = k.get(t, '?')
        if len(v) == 1 and v.isalpha(): cur += v.lower()
        elif v == '[null?]': continue
        elif v == '?': cur += '?'
        else: segs.append(cur); cur = ''
    segs.append(cur); return [s for s in segs if s]
lists = {'cp_len4_n2': wl2857.build_claver_pulgar_long(sys.argv[3], sys.argv[4], 4, 2), 'cp_len4_n5': wl2857.build_claver_pulgar_long(sys.argv[3], sys.argv[4], 4, 5)}
for lname, counts in lists.items():
    seg = wl2857.Seg(counts)
    for mname, fn in (('cover3', lambda s, x: s.measure(x, 3)), ('sandwich3', lambda s, x: wl2857.sandwich_measure(s, x, 3))):
        for n in (225, 450, len(rows)):
            rng = random.Random(95)
            toks = rows[:n]
            real = fn(seg, decode(toks, key))[0]
            ctrl = []
            for _ in range(1000):
                vals = [key[s] for s in letters]; rng.shuffle(vals)
                k2 = dict(key); k2.update(zip(letters, vals))
                ctrl.append(fn(seg, decode(toks, k2))[0])
            ctrl.sort()
            print(f'{lname:15s} {mname:10s} signs {n:5d}: true {real:.3f}; permuted mean {sum(ctrl)/1000:.3f} 95th {ctrl[949]:.3f} max {ctrl[-1]:.3f}')
