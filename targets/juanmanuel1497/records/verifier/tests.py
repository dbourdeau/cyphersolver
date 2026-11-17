"""T1 and T2 of PLAN.md (verifier of cyphersolver 2857). One run each.
usage: tests.py <transcription> <map.json> <claver_tsv> <pulgar_txt> <zurita_txt> <order: plan|solver> <label>
Transcription format 'Lx: tokens'. Tokens: Kxx = sheet id; D, #, ?, N0x = hole ('?'); [xxx] = code-group-like break."""
import sys, os, json, re, random, math, unicodedata
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wl2857_copy as wl
tr, mp, ctsv, ptxt, ztxt, order, label = sys.argv[1:8]
m = json.load(open(mp))
CODES = {'bac','bcd','bnh','bon','boo','dae','dah','dal','dcl','dif','dnl','aunque'}
key = {}
for k, lab in m.items():
    if re.fullmatch(r'[A-Z]\d', lab): key[k] = lab[0].lower()
    elif lab == 'nine_dot': key[k] = 'y'
    elif lab == 'D_null': key[k] = ''
    else: key[k] = '<' + lab + '>'
alpha = sorted(k for k, v in key.items() if len(v) == 1)
lines = {}
for l in open(tr, encoding='utf8'):
    mm = re.match(r'(L\d[ab]?):\s*(.*)', l)
    if mm and mm.group(1) not in lines: lines[mm.group(1)] = mm.group(2).split()
seq = ['L1','L2','L3','L4','L5','L6','L7','L8a','L8b'] if order == 'plan' else ['L1','L2','L3','L4','L5','L6','L7','L8']
toks = [t for L in seq for t in lines.get(L, [])]
def decode(k):
    segs, cur = [], ''
    for t in toks:
        if t.startswith('['): segs.append(cur); cur = ''; continue
        v = k.get(t)
        if v is None: cur += '?'
        elif v == '': continue
        elif len(v) == 1: cur += v
        else: segs.append(cur); cur = ''
    segs.append(cur); return segs
rng = random.Random(2857)
tables = []
for _ in range(1000):
    vals = [key[t] for t in alpha]; rng.shuffle(vals)
    k2 = dict(key); k2.update(zip(alpha, vals)); tables.append(k2)
# ---- T1: solver's measure unchanged
wlist = wl.build_claver_pulgar_long(ctsv, ptxt, 4, 5); seg = wl.Seg(wlist)
segs = decode(key)
real1, out1 = wl.sandwich_measure(seg, segs, 3)
c1 = sorted(wl.sandwich_measure(seg, decode(k2), 3)[0] for k2 in tables)
print(f"[{label}] tokens {len(toks)}; letters+holes {sum(len(wl.norm_string(s)) for s in segs)}; holes {sum(s.count('?') for s in segs)}")
print(f"[{label}] decode segments: {segs}")
print(f"[{label}] T1 sandwich measure {real1:.4f}; control mean {sum(c1)/1000:.4f}, p95 {c1[949]:.4f}, max {c1[-1]:.4f}, n>=real {sum(c>=real1 for c in c1)}")
print(f"[{label}] T1 segmentation: {' '.join(out1)}")
# ---- T2: letter trigram model on Pulgar, runs broken at holes/codes
def normtext(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('j','i').replace('v','u').replace('w','u').replace('k','c').replace('x','s')
    return re.sub(r'[^abcdefghilmnopqrstuyz]', '', s)
P = normtext(open(ptxt, encoding='utf8', errors='replace').read())
A = 'abcdefghilmnopqrstuyz'
u = Counter(P); b = Counter(zip(P, P[1:])); t = Counter(zip(P, P[1:], P[2:]))
b1 = Counter(P[:-1]); t2 = Counter(zip(P[:-2], P[1:-1]))
N = len(P); V = len(A)
def pu(c): return (u[c]+.5)/(N+.5*V)
def pb(a, c): return (b[(a,c)]+.5)/(b1[a]+.5*V)
def pt(a, bb, c): return (t[(a,bb,c)]+.5)/(t2[(a,bb)]+.5*V)
def lp_run(r):
    s = 0.0
    for i, c in enumerate(r):
        if i == 0: p = pu(c)
        elif i == 1: p = 0.8*pb(r[0], c) + 0.2*pu(c)
        else: p = 0.7*pt(r[i-2], r[i-1], c) + 0.2*pb(r[i-1], c) + 0.1*pu(c)
        s += math.log10(p)
    return s
def runs(segs): return [r for sgm in segs for r in sgm.split('?') if r]
def score(segs):
    rs = runs(segs); n = sum(len(r) for r in rs)
    return sum(lp_run(r) for r in rs)/n if n else float('nan'), [len(r) for r in rs]
real2, rl = score(segs)
c2 = sorted(score(decode(k2))[0] for k2 in tables)
Z = normtext(open(ztxt, encoding='utf8', errors='replace').read())
zr = random.Random(1497); zs = []
for _ in range(1000):
    tot = 0.0; n = 0
    for L in rl:
        st = zr.randrange(0, len(Z)-L); r = Z[st:st+L]; tot += lp_run(r); n += L
    zs.append(tot/n)
zs.sort()
print(f"[{label}] T2 runs {len(rl)} letters {sum(rl)}; real {real2:.4f}; permuted mean {sum(c2)/1000:.4f} max {c2[-1]:.4f} n>=real {sum(c>=real2 for c in c2)}; Zurita samples p5 {zs[49]:.4f} median {zs[499]:.4f} min {zs[0]:.4f}; real percentile among Zurita {sum(z<real2 for z in zs)/10:.1f}%")
print(f"[{label}] T2 verdict: beats all permuted: {c2[-1] < real2}; at or above Zurita p5: {real2 >= zs[49]}")
