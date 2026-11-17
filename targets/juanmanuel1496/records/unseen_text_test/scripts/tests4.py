"""Parts B and C of PLAN_round4.md (sha256 in PLAN_round4.sha256), run once on letter 2; with --descriptive on letter 1.
usage: python3 -I tests4.py RECONCILED MAPPING LASRY_KEY LASRY_ALL CLAVER_TSV PULGAR ZURITA WL_DIR OUTDIR TAG [--descriptive]
Decodes the agreed-only transcription through the fixed hidden mapping (W id -> Lasry sign -> his letter, key unchanged),
runs B1 (letter trigrams), B2 (word share calibrated on Lasry's letter at the same hole share), C1 (W26 = o), and lists
every code group with context (for C2-C4)."""
import sys, os, re, json, math, random, unicodedata
from collections import Counter
rec_p, map_p, key_p, all_p, ctsv, ptxt, ztxt, wldir, out, tag = sys.argv[1:11]
desc = '--descriptive' in sys.argv
sys.path.insert(0, wldir)
import wl2857_copy as wl
key = {}
for line in open(key_p, encoding='utf8'):
    if line.startswith('#') or ' - ' not in line: continue
    signs, v = line.rstrip('\n').rsplit(' - ', 1)
    for s in signs.split('|'): key[s] = v
LETTERSIGNS = sorted(s for s, v in key.items() if len(v) == 1 and v.isalpha() and v.isupper())
W2L = {}
for l in open(map_p, encoding='utf8'):
    if l.startswith('W'):
        f = l.rstrip('\n').split('\t'); W2L[f[0]] = f[2]
lines, order = {}, []
for ln in open(rec_p, encoding='utf8'):
    m = re.match(r'([A-Z]\d\d):\s*(.*)', ln)
    if m: lines[m.group(1)] = m.group(2).split(); order.append(m.group(1))
seq = [(L, t) for L in order for t in lines[L]]
def item(t, tab, w26=None):
    """letter, '' (null dropped), '?' (hole), or a break label |...|"""
    if t in ('_', '?', '#'): return '?'
    if t == '<clear>': return '|<clear>|'
    if t.startswith('{'): return f'|[{t.strip("{}")}]|'
    if t == 'W26': return w26 if w26 else '?'
    ls = W2L.get(t)
    if ls is None: return '?'
    if ls == 'NONE': return '?'
    if ls == 'D': return ''
    if ls in tab: return tab[ls]
    v = key.get(ls)
    if v and len(v) == 1 and v.isalpha(): return v.lower()
    return f'|{ls}|'
BASE = {s: key[s].lower() for s in LETTERSIGNS}
def decode(tab, w26=None): return [(L, item(t, tab, w26)) for L, t in seq]
def segments(dec):
    segs, cur = [], ''
    for L, x in dec:
        if x == '': continue
        if len(x) == 1: cur += x
        else: segs.append(cur); cur = ''
    segs.append(cur); return [s for s in segs if s]
d0 = decode(BASE)
with open(os.path.join(out, f'decode_{tag}_agreed.txt'), 'w') as f:
    f.write(f'# Agreed-only decode ({tag}) with Lasry no. 95 key unchanged through the fixed round-4 mapping\n'
            '# ? = hole (disagreement, both unsure, W26 barred sign, W27 eight, or a sign off the sheet); |[grp]| Latin-letter group\n')
    for L in order:
        xs = [x for LL, x in d0 if LL == L]
        f.write(f'{L}: ' + ''.join(x if len(x) <= 1 else f' {x} ' for x in xs) + '\n')
segs = segments(d0)
nlet = sum(len(s.replace('?', '')) for s in segs); nhole = sum(s.count('?') for s in segs); h = nhole / (nlet + nhole)
print(f'[{tag}] {"DESCRIPTIVE (not a test)" if desc else "PLANNED TEST"}')
print(f'[decode] agreed letters {nlet}, holes {nhole}, hole share h = {h:.4f}; segments {len(segs)}; '
      f'W26 agreed {sum(1 for L, t in seq if t == "W26")}, W27 agreed {sum(1 for L, t in seq if t == "W27")}')
rng = random.Random(1496); tables = []
for _ in range(1000):
    vals = [BASE[k] for k in LETTERSIGNS]; rng.shuffle(vals); tables.append(dict(zip(LETTERSIGNS, vals)))
def normtext(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('j', 'i').replace('v', 'u').replace('w', 'u').replace('k', 'c').replace('x', 's')
    return re.sub(r'[^abcdefghilmnopqrstuyz]', '', s)
P = normtext(open(ptxt, encoding='utf8', errors='replace').read()); A = 'abcdefghilmnopqrstuyz'
u = Counter(P); b = Counter(zip(P, P[1:])); t3 = Counter(zip(P, P[1:], P[2:])); b1 = Counter(P[:-1])
t2 = Counter(zip(P[:-2], P[1:-1])); N = len(P); V = len(A)
def lp_run(r):
    s = 0.0
    for i, c in enumerate(r):
        if i == 0: p = (u[c] + .5) / (N + .5 * V)
        elif i == 1: p = 0.8 * (b[(r[0], c)] + .5) / (b1[r[0]] + .5 * V) + 0.2 * (u[c] + .5) / (N + .5 * V)
        else:
            p = (0.7 * (t3[(r[i - 2], r[i - 1], c)] + .5) / (t2[(r[i - 2], r[i - 1])] + .5 * V)
                 + 0.2 * (b[(r[i - 1], c)] + .5) / (b1[r[i - 1]] + .5 * V) + 0.1 * (u[c] + .5) / (N + .5 * V))
        s += math.log10(p)
    return s
def runs(sg): return [r for s in sg for r in s.split('?') if r]
def score(sg):
    rs = runs(sg); n = sum(len(r) for r in rs)
    return sum(lp_run(r) for r in rs) / n, [len(r) for r in rs]
real1, rl = score(segs)
c1 = sorted(score(segments(decode(tb)))[0] for tb in tables)
Z = normtext(open(ztxt, encoding='utf8', errors='replace').read())
zr = random.Random(1496); zs = []
for _ in range(1000):
    tot = 0.0; n = 0
    for Lr in rl:
        st = zr.randrange(0, len(Z) - Lr); tot += lp_run(Z[st:st + Lr]); n += Lr
    zs.append(tot / n)
zs.sort(); ok1 = c1[-1] < real1 and real1 >= zs[49]
print(f'[B1] runs {len(rl)}, letters {sum(rl)}; real {real1:.4f}; permuted mean {sum(c1) / 1000:.4f}, max {c1[-1]:.4f}, '
      f'n>=real {sum(c >= real1 for c in c1)}; Zurita p5 {zs[49]:.4f}, median {zs[499]:.4f}; real percentile among Zurita {sum(z < real1 for z in zs) / 10:.1f}%')
print(f'[B1] RESULT: {"PASS" if ok1 else "MISS"} (mark: beats all 1,000 permuted AND >= Zurita p5)')
seg = wl.Seg(wl.build_claver_pulgar_long(ctsv, ptxt, 4, 5))
real2, out2 = wl.sandwich_measure(seg, segs, 3)
toks = []
for line in open(all_p, encoding='utf8'):
    if line.startswith('#') or not line.strip(): continue
    toks += [t for t in line.strip().split(';') if t]
lsegs, cur = [], ''
for t in toks:
    v = key.get(t, '?')
    if len(v) == 1 and v.isalpha(): cur += v.lower()
    elif v == '[null?]': continue
    elif v == '?': cur += '?'
    else: lsegs.append(cur); cur = ''
lsegs.append(cur); lsegs = [s for s in lsegs if s]
cr = random.Random(95); cal = []
for _ in range(200):
    hs = [''.join('?' if (c != '?' and cr.random() < h) else c for c in s) for s in lsegs]
    cal.append(wl.sandwich_measure(seg, hs, 3)[0])
cal.sort(); Mmark = cal[9]; lasry_clean = wl.sandwich_measure(seg, lsegs, 3)[0]
c2 = sorted(wl.sandwich_measure(seg, segments(decode(tb)), 3)[0] for tb in tables)
ok2 = real2 >= Mmark and real2 > c2[989]
print(f'[B2] Lasry no. 95 clean {lasry_clean:.4f}; with holes at h={h:.3f}: 200 draws median {cal[99]:.4f}, 5th pct (mark M) {Mmark:.4f}, min {cal[0]:.4f}')
print(f'[B2] real {real2:.4f}; permuted mean {sum(c2) / 1000:.4f}, p99 {c2[989]:.4f}, max {c2[-1]:.4f}')
print(f'[B2] RESULT: {"PASS" if ok2 else "MISS"} (mark: real >= M AND real > permuted p99)')
open(os.path.join(out, f'B2_segmentation_{tag}.txt'), 'w').write(' '.join(out2) + '\n')
# ---- C1: W26 = o
flat = [(L, x, t) for (L, t), (LL, x) in zip(seq, d0) if x != '']
idx = [i for i, (L, x, t) in enumerate(flat) if t == 'W26']
print(f'[C1] agreed W26 occurrences n = {len(idx)}')
def ctx(i):
    l = []; j = i - 1
    while j >= 0 and len(l) < 8 and len(flat[j][1]) == 1 and flat[j][1] != '?' and flat[j][2] != 'W26': l.insert(0, flat[j][1]); j -= 1
    r = []; j = i + 1
    while j < len(flat) and len(r) < 8 and len(flat[j][1]) == 1 and flat[j][1] != '?' and flat[j][2] != 'W26': r.append(flat[j][1]); j += 1
    return ''.join(l), ''.join(r)
def ok_slot(left, v, right):
    s = wl.norm_string(left + v + right); k = len(wl.norm_string(left + v)) - 1
    toks = seg.segment(s); longw = [isw and len(w) >= 3 for w, isw in toks]; pos = 0
    for i, (w, isw) in enumerate(toks):
        if pos <= k < pos + len(w):
            ok = longw[i]
            if isw and not ok:
                lf = (i == 0) or longw[i - 1]; rt = (i == len(toks) - 1) or longw[i + 1]
                ok = lf and rt and not (i == 0 and i == len(toks) - 1)
            return ok, w
        pos += len(w)
    return False, ''
if len(idx) < 3:
    print('[C1] RESULT: NO RESULT (fewer than 3 agreed occurrences)')
else:
    res = {}
    rows = []
    for v in A:
        mk = br = 0
        for i in idx:
            l, r = ctx(i)
            if len(l) + len(r) < 3: continue
            ok, w = ok_slot(l, v, r)
            if ok: mk += 1
            else: br += 1
            if v == 'o': rows.append((flat[i][0], l, r, ok, w))
        res[v] = (mk, br)
    ev = sum(1 for i in idx if sum(map(len, ctx(i))) >= 3)
    for L, l, r, ok, w in rows: print(f'[C1]  {L}: {l}[o]{r}  -> {"makes" if ok else "BREAKS"} ({w})')
    rank = sorted(A, key=lambda v: -(res[v][0] - res[v][1]))
    print(f'[C1] evaluable {ev}; o makes {res["o"][0]}, breaks {res["o"][1]}; ranking by makes-breaks: ' +
          ', '.join(f'{v} {res[v][0]}-{res[v][1]}' for v in rank[:8]))
    best = max(res[v][0] - res[v][1] for v in A)
    okc = res['o'][0] >= 3 and res['o'][1] == 0 and (res['o'][0] - res['o'][1]) >= best
    print(f'[C1] RESULT: {"PASS" if okc else "MISS"} (mark: o makes >=3, breaks 0, no letter higher on makes-breaks)')
# ---- code groups with context
text = []
for L, x in d0:
    text.append((L, x if len(x) <= 1 else f' {x} '))
flatstr = ''.join(x for L, x in text); pos = 0; marks = []
for L, x in text:
    if x.startswith(' |['): marks.append((L, pos, x.strip()))
    pos += len(x)
with open(os.path.join(out, f'groups_{tag}.txt'), 'w') as f:
    for L, p, g in marks:
        f.write(f'{L}\t{g}\t{flatstr[max(0, p - 45):p]}  {g}  {flatstr[p + len(g) + 2:p + len(g) + 47]}\n')
print('[groups] ' + ', '.join(f'{g}x{n}' for g, n in Counter(g for L, p, g in marks).most_common()))
