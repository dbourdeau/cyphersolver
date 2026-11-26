"""Key test of PLAN.md (SHA-256 in PLAN.sha256), reading every input by its repo path.

Usage: python3 -I keytest.py <repo root> [--villa <path to targets/villa1914/key.tsv>]

Keys tested (no value added, changed or fitted):
- K-LIM: targets/limantour1909/key.tsv (phrase codes 77 and 79 left out).
- K-VIL: targets/villa1914/key.tsv of pull request #865 (head b35ba1997, not on main when this was written); pass
  --villa if it is not under the repo root.
- K-SYL-RC, K-SYL-CR: Daniel Jalkut's two-digit card in targets/duron1911/siblings/syl.py (its RC and CR tables).
Positive controls: targets/tellez1913/candidate15.tsv (P-OCT) and targets/rubio1913/key.tsv (Clave 109, P-109).
Ciphertext: targets/tellez1913/oct14.runs, targets/tellez1913/oct15.runs, targets/blanquet1914/may19.runs.
Corpus: targets/esp318/lit/quijote.txt.

This is the frozen run's script (SHA-256 0c09c7e2... in run.sha256, run 22 Nov 2026 21:20 EST) with only the input
paths changed: the frozen script read copies in a local ext/ folder and held the card inline. Same seed, same order
of draws. Prints the results as JSON.
"""
import json, math, random, re, runpy, sys, unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path(sys.argv[1])
VILLA = Path(sys.argv[sys.argv.index('--villa') + 1]) if '--villa' in sys.argv else REPO / 'targets/villa1914/key.tsv'
SEED = 20261122
NSH = 1000

def norm(s):
    s = s.lower().replace('ñ', '\x00')
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    return s.replace('\x00', 'ñ')

ALPHA = set('abcdefghijklmnopqrstuvwxyzñ')
raw = (REPO / 'targets/esp318/lit/quijote.txt').read_text(encoding='utf-8', errors='ignore')
a = raw.find('*** START'); b = raw.find('*** END')
raw = raw[raw.find('\n', a) + 1:b] if a >= 0 and b > a else raw
txt = norm(raw)
words = Counter(re.findall(r'[a-zñ]+', txt))
LEX = {w for w, n in words.items() if n >= 3 and len(w) >= 5}
stream = re.sub(r'[^a-zñ]+', ' ', txt)
tri = Counter(); bi = Counter()
for w in stream.split():
    w = ' ' + w + ' '
    for i in range(len(w) - 2):
        tri[w[i:i + 3]] += 1; bi[w[i:i + 2]] += 1
V = 28
def lp(t):
    return math.log((tri[t] + 1) / (bi[t[:2]] + V))

def letters(v):
    return ''.join(c for c in norm(v) if c in ALPHA)

def runs(path):
    return [l.split() for l in (REPO / path).read_text().splitlines() if l.strip()]

def load_tsv(path, kcol=0, vcol=1, skip=None):
    k = {}
    for l in Path(path).read_text().splitlines():
        if not l.strip() or l.startswith('#'): continue
        p = l.split('\t')
        if p[0] in ('number', 'group'): continue
        if skip and p[kcol] in skip: continue
        if len(p) > vcol and p[vcol].strip() not in ('', '-'):
            k[str(int(p[kcol]))] = p[vcol].strip()
    return k

# K-LIM
klim = load_tsv(REPO / 'targets/limantour1909/key.tsv', skip={'77', '79'})
klim = {k: v for k, v in klim.items() if letters(v)}
# K-VIL
kvil = {}
for l in VILLA.read_text().splitlines()[1:]:
    p = l.split('\t')
    vals = [x for x in (p[1], p[2]) if x != '-']
    if not vals: continue
    if len(set(vals)) > 1: continue
    kvil[str(int(p[0]))] = vals[0]
# K-SYL: the card as Jalkut set it out; keys keep two-digit strings
_syl = runpy.run_path(str(REPO / 'targets/duron1911/siblings/syl.py'), run_name='syl')
RC = _syl['RC']; CR = _syl['CR']
# positive controls
pocf = load_tsv(REPO / 'targets/tellez1913/candidate15.tsv')
p109 = load_tsv(REPO / 'targets/rubio1913/key.tsv')

def lookup(key, g, twodigit):
    if g == '?': return None
    if twodigit:
        return key.get(g) if len(g) == 2 else None
    try: return key.get(str(int(g)))
    except ValueError: return None

def decode(key, rr, twodigit=False):
    """returns list of stretches; each stretch = list of (letters) per group"""
    out = []
    for r in rr:
        cur = []
        for g in r:
            v = lookup(key, g, twodigit)
            v = letters(v) if v else ''
            if not v:
                if cur: out.append(cur); cur = []
            else:
                cur.append(v)
        if cur: out.append(cur)
    return out

def score(stretches):
    tot = 0.0; n = 0
    for s in stretches:
        if len(s) < 2: continue
        txt = ''.join(s); bounds = []; pos = 0
        for g in s[:-1]:
            pos += len(g); bounds.append(pos)
        for i in range(len(txt) - 2):
            if any(i < b <= i + 2 for b in bounds):
                tot += lp(txt[i:i + 3]); n += 1
    return (tot / n if n else float('-inf')), n

def wordhits(stretches, runs_of):
    found = {}
    for si, s in enumerate(stretches):
        if len(s) < 2: continue
        txt = ''.join(s); starts = [0]
        for g in s: starts.append(starts[-1] + len(g))
        for i in range(len(txt)):
            for j in range(i + 5, min(len(txt), i + 14) + 1):
                w = txt[i:j]
                if w in LEX:
                    gi = max(k for k in range(len(s)) if starts[k] <= i)
                    gj = max(k for k in range(len(s)) if starts[k] < j)
                    if gj > gi and w not in found:
                        found[w] = runs_of[si]
    return found, len(set(found.values()))

def stretch_runs(key, rr, twodigit):
    ids = []
    for ri, r in enumerate(rr):
        cur = 0
        for g in r:
            v = lookup(key, g, twodigit); v = letters(v) if v else ''
            if not v:
                if cur: ids.append(ri); cur = 0
            else: cur += 1
        if cur: ids.append(ri)
    return ids

def coverage(key, rr, twodigit):
    tot = sum(len(r) for r in rr)
    cov = sum(1 for r in rr for g in r if (lambda v: v and letters(v))(lookup(key, g, twodigit)))
    return cov, tot

def run_test(name, key, tel, rr, twodigit, rng):
    cov, tot = coverage(key, rr, twodigit)
    st = decode(key, rr, twodigit)
    obs, n = score(st)
    rid = stretch_runs(key, rr, twodigit)
    wh, wruns = wordhits(st, rid)
    res = dict(key=name, telegram=tel, covered=cov, positions=tot, cov_share=round(cov / tot, 3), boundary_trigrams=n)
    if n < 10:
        res.update(result='too little coverage to test', score=None, words=sorted(wh))
        return res
    ks = list(key.keys()); vs = [key[k] for k in ks]
    beaten = 0; ctrl_words = []
    for _ in range(NSH):
        sv = vs[:]; rng.shuffle(sv); sk = dict(zip(ks, sv))
        sst = decode(sk, rr, twodigit)
        s, _n = score(sst)
        if obs > s: beaten += 1
        cw, _ = wordhits(sst, stretch_runs(sk, rr, twodigit)); ctrl_words.append(len(cw))
    ctrl_words.sort(); p99 = ctrl_words[int(0.99 * NSH) - 1]
    passes = beaten >= 999 and cov / tot >= 0.30 and len(wh) >= 2 and wruns >= 2 and len(wh) > p99
    res.update(score=round(obs, 4), shuffles_beaten=beaten, words=sorted(wh), word_runs=wruns,
               control_words_p99=p99, result='PASS' if passes else 'miss',
               sample=' | '.join(''.join(s) for s in st)[:300])
    return res

def agreement(ext, ours, twodigit):
    same = diff = 0; rows = []
    for k, v in ext.items():
        kk = k if not twodigit else (str(int(k)) if k[0] != '0' else None)
        if kk is None or kk not in ours: continue
        a, b = letters(v), letters(ours[kk])
        if not a or not b: continue
        if a == b: same += 1
        else: diff += 1
        rows.append(f'{kk}:{a}/{b}')
    return dict(shared=same + diff, same=same, rows=rows)

rng = random.Random(SEED)
tels = [('oct14', runs('targets/tellez1913/oct14.runs')), ('oct15', runs('targets/tellez1913/oct15.runs')),
        ('may19', runs('targets/blanquet1914/may19.runs'))]
keys = [('K-LIM', klim, False), ('K-VIL', kvil, False), ('K-SYL-RC', RC, True), ('K-SYL-CR', CR, True)]
out = {'positive_controls': [], 'tests': [], 'agreement': {}}
for tel, rr in tels[:2]:
    out['positive_controls'].append(run_test('P-OCT', pocf, tel, rr, False, rng))
out['positive_controls'].append(run_test('P-109', p109, 'may19', tels[2][1], False, rng))
for name, key, td in keys:
    for tel, rr in tels:
        out['tests'].append(run_test(name, key, tel, rr, td, rng))
    out['agreement'][name] = {'vs_october_table': agreement(key, pocf, td), 'vs_clave109': agreement(key, p109, td)}
print(json.dumps(out, ensure_ascii=False, indent=1))
