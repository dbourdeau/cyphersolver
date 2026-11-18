"""Crawford 1813, second code (the = 285): score a key against the contemporary interlinear decipherment.

    python score.py we025      Weber's WE025, the rows public in this repository (Beling's two cuts)
    python score.py reversed   the jqa table read with morris1813's block reversal (Morris 100*i + r = JQA 100*(15-i) + r)

One measure: share of covered word units (interlinear_pairs.tsv) whose decoded value equals the interlinear word
(spelling, plural/-ed allowed); 200 shuffles of the key's values within length classes (1-2, 3-4, >=5 letters), seed 1813.
Bar written before the run: M >= 0.85 and M >= best shuffle + 0.30. For 'reversed', pairs containing the three anchor groups
285, 76, 1516 (which suggested the hypothesis) are left out."""
import os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..')
def norm(s): return re.sub(r'[^a-z]', '', s.lower())
def tsv(path, skip_header):
    out = {}
    for i, l in enumerate(open(path, encoding='utf-8')):
        if l.startswith('#') or not l.strip() or (skip_header and i == 0): continue
        p = l.rstrip('\n').split('\t')
        try: out.setdefault(int(p[0]), p[1])
        except ValueError: pass
    return out
mode = sys.argv[1] if len(sys.argv) > 1 else 'reversed'
if mode == 'we025':
    key = tsv(os.path.join(T, 'poinsett1813', 'beling', 'key', 'we025_poinsett.tsv'), True)
    for n, v in tsv(os.path.join(T, 'crawford1814', 'key', 'we025_crawford1814.tsv'), True).items(): key.setdefault(n, v)
    anchors = set()
else:
    jqa = tsv(os.path.join(T, 'jqa', 'code_table.tsv'), False)
    def rev(n):
        i, r = divmod(n - 1, 100); return 100 * (15 - i) + r + 1
    key = {rev(n): v for n, v in jqa.items() if 1 <= n <= 1600}
    anchors = {285, 76, 1516}
pairs = []
for l in open(os.path.join(HERE, 'interlinear_pairs.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    pg, ln, g, gl = l.rstrip('\n').split('\t'); gs = [int(x) for x in g.split()]
    if anchors & set(gs): continue
    pairs.append((pg, ln, gs, gl))
def ok(val, gl):
    v, g = norm(val), norm(gl)
    return v == g or (len(v) >= 3 and (g in (v + 's', v + 'ed', v + 'd') or v == g + 's'))
def measure(k):
    cov = hit = 0; det = []
    for pg, ln, gs, gl in pairs:
        if all(x in k for x in gs):
            cov += 1; val = ' '.join(k[x] for x in gs); h = ok(val.replace(' ', ''), gl); hit += h; det.append((pg, ln, gs, gl, val, h))
    return cov, hit, det
cov, hit, det = measure(key); M = hit / cov if cov else 0
print('key=%s  units=%d  covered=%d  agree=%d  M=%.3f  strict(agree/units)=%.3f' % (mode, len(pairs), cov, hit, M, hit / len(pairs)))
for d in det:
    if not d[5]: print('  differs', d[0], d[1], ' '.join(map(str, d[2])), 'interlinear=%s' % d[3], 'key=%s' % d[4], sep='\t')
cls = lambda v: 1 if len(norm(v)) <= 2 else (2 if len(norm(v)) <= 4 else 3)
rng = random.Random(1813); ctl = []; nums = sorted(key)
for _ in range(200):
    k2 = {}
    for c in (1, 2, 3):
        ns = [n for n in nums if cls(key[n]) == c]; vs = [key[n] for n in ns]; rng.shuffle(vs); k2.update(zip(ns, vs))
    c2, h2, _ = measure(k2); ctl.append(h2 / c2 if c2 else 0)
ctl.sort()
print('shuffles: mean %.3f  p99 %.3f  best %.3f' % (sum(ctl) / 200, ctl[197], ctl[-1]))
print('verdict:', 'pass' if (M >= 0.85 and M >= ctl[-1] + 0.30) else 'fail')
