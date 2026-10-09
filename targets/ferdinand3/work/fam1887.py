"""R1887 (1634): test the 1640-style hypothesis that the three-letter groups are vowel-series syllables.
Families (frame with the vowel slot): x?r t?s t?n p?n f?r s?l l?s h?s h? ?b ?d ?c ?r. Each family gets one
consonant string C and an orientation (C+v or v+C); every other symbol (numbers, graphic signs) is free over
letters/short syllables/null. Scored with the shared `la` model, segments split at clear-text passages."""
import sys, os, re, json, numpy as np, multiprocessing as mp
sys.path.insert(0, r'C:\Users\dbour\cypher')

def load():
    segs = []; cur = []
    for line in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'transcription', 'R1887.txt'), encoding='utf8'):
        if line.startswith('#') or not line.strip(): continue
        lab, rest = line.split(' ', 1)
        parts = re.split(r'(\[[^\]]*\])', rest.strip())
        for p in parts:
            if p.startswith('['):
                if cur: segs.append(cur); cur = []
                continue
            for t in p.split():
                if not os.environ.get('SUP'): t = re.sub(r'\^.*', '', t)
                t = {'tt/': 'tt', 'S?': 'S', 'ten?': 'ten', 'sed?': 'sed'}.get(t, t)
                if t == 'p?': continue
                cur.append(t)
    if cur: segs.append(cur)
    return segs

SEGS = load()
V = 'aeiou'
FRAMES = [('x', 'r'), ('t', 's'), ('t', 'n'), ('p', 'n'), ('f', 'r'), ('s', 'l'), ('l', 's'), ('h', 's'), ('h', ''),
          ('', 'b'), ('', 'd'), ('', 'c'), ('', 'r')]
FAM = {}
for a, b in FRAMES:
    for v in V:
        FAM[a + v + b] = (a + '_' + b, v)
FAM['sed'] = FAM.get('sel', ('s_l', 'e'))
CONS = ['b', 'c', 'd', 'f', 'g', 'h', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'x', 'qu', 'st', 'tr', 'pr', 'cr',
        'gr', 'br', 'nt', 'ns', 'nd', 'rt', 'sc', 'sp', 'ct', 'ss', 'mp', 'bl', 'pl', 'cl', 'fr', 'dr', 'ph', 'rr', 'll']
FREE = list('abcdefghilmnopqrstux') + ['qu', 'que', 'us', 'um', 'em', 'is', 'am', 'it', 'er', 'en', 'in', 'es', 'ae',
                                       'st', 'nt', 're', 'ri', 'ra', 'ni', 'di', 'si', 'ci', 'ti', 'ta', 'te', 'tu', '']

def job(args):
    seed, iters = args
    from lang import lm
    M = lm.load('la', order=5, spaces=False)
    rng = np.random.default_rng(seed)
    toks = sorted(set(t for s in SEGS for t in s))
    fams = sorted(set(FAM[t][0] for t in toks if t in FAM))
    free = [t for t in toks if t not in FAM]
    cnt = {t: sum(s.count(t) for s in SEGS) for t in toks}
    fixf = json.load(open('fix1887.json', encoding='utf8')) if os.path.exists('fix1887.json') else {'fam': {}, 'sym': {}}
    st = {f: (CONS[rng.integers(len(CONS))], int(rng.integers(2))) for f in fams}
    for f, c in fixf['fam'].items():
        if f in st: st[f] = (c[:-1], 0) if c.endswith('V') else (c[1:], 1)
    fv = {t: FREE[rng.integers(len(FREE))] for t in free}
    for t, v in fixf['sym'].items():
        if t in fv: fv[t] = v
    fams = [f for f in fams if f not in fixf['fam']]
    free = [t for t in free if t not in fixf['sym']]
    NP = float(os.environ.get('NP', '3'))
    def val(t):
        if t in FAM:
            f, v = FAM[t]; c, o = st[f]
            return c + v if o == 0 else v + c
        return fv[t]
    def sc():
        return sum(M.score(''.join(val(t) for t in s)) for s in SEGS) - NP * sum(cnt[t] for t in fv if fv[t] == '')
    cur = sc(); best = (cur, dict(st), dict(fv))
    for it in range(iters):
        T = 6.0 * (1 - it / iters) + 0.2
        if rng.random() < 0.4:
            f = fams[rng.integers(len(fams))]; old = st[f]
            st[f] = (CONS[rng.integers(len(CONS))], int(rng.integers(2))) if rng.random() < .7 else (old[0], 1 - old[1])
            new = sc(); d = new - cur
            if d > 0 or rng.random() < np.exp(d / T): cur = new
            else: st[f] = old
        else:
            t = free[rng.integers(len(free))]; old = fv[t]; fv[t] = FREE[rng.integers(len(FREE))]
            new = sc(); d = new - cur
            if d > 0 or rng.random() < np.exp(d / T): cur = new
            else: fv[t] = old
        if cur > best[0]: best = (cur, dict(st), dict(fv))
    st, fv = best[1], best[2]
    return best[0], {f: (c + 'V' if o == 0 else 'V' + c) for f, (c, o) in st.items()}, fv, ['|'.join(val(t) for t in s) for s in SEGS]

if __name__ == '__main__':
    it = int(os.environ.get('IT', '60000')); nr = int(os.environ.get('NR', '20'))
    print([len(s) for s in SEGS])
    with mp.Pool(20) as p:
        res = p.map(job, [(s, it) for s in range(nr)])
    res.sort(key=lambda r: -r[0])
    json.dump(res, open('fam1887_res.json', 'w'), indent=0)
    for r in res[:5]:
        print(round(r[0]), r[1]); print('   ', r[2])
        for s in r[3]: print('     ', s.replace('|', ''))
