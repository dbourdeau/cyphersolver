"""Candidates for the unread words ({?}) of a System A' reading, constrained by the signs.

  python fill.py REC [--top 5] [--out fill_REC.txt]

1. Pooled key: every sign value attested in the hand readings of R9408, R9409, R9410 (both letters), R9413, R9427 and
   R9407 (measure2.py's aligner, as supkey.py), kept per letter; a sign's score mixes its own letter's counts (the
   hand) with the pooled counts: p = (own + 0.3*pooled + 0.05) / (N_own + 0.3*N_pooled + 1).
2. Each {?} run of a line is located on the signs by a wildcard alignment (known words aligned letter by letter,
   {?} absorbing any number of signs).
3. The span's signs are decoded by a beam that only allows lexicon words (DTA 1470-1610 + vocab.txt + the words of all
   the readings; for the Latin letter the Latin corpus) and only attested sign values; ranked by the value
   probabilities + word frequencies + the character LM over the words on either side.
4. Verification: for each candidate word, every other occurrence of the same sign string in the six letters is listed
   with what the reading has there ('=' agrees, '!' disagrees, '?' unread there).
"""
import io, json, math, os, re, runpy, sys, contextlib
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..'))
from lang import lm
args = sys.argv[1:]
def opt(n, d):
    if n in args:
        i = args.index(n); v = args[i + 1]; del args[i:i + 2]; return v
    return d
REC = args[0]; TOP = int(opt('--top', '5')); OUT = opt('--out', f'fill_{REC}.txt'); BEAM = int(opt('--beam', '400'))
LANG = 'la' if REC == 'r9410b' else 'de'
PAIRS = {'r9408': '../r9408/reading.txt', 'r9409': '../r9409/reading.txt', 'r9410': '../r9410/reading.txt',
         'r9410b': '../r9410/reading_p3p6.txt', 'r9413': '../r9413/reading.txt', 'r9427': '../r9427/reading.txt',
         'r9407': 'r9407_reading_fg.txt'}
if REC == 'r9408m': PAIRS['r9408m'] = PAIRS.pop('r9408')        # the v4 re-transcription of R9408

def run_measure(rec):
    sys.argv = ['measure2.py', os.path.join(HERE, rec + '.tok'), os.path.join(HERE, PAIRS[rec])]
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(os.path.join(HERE, 'measure2.py'))
G = {r: run_measure(r) for r in PAIRS}
OWN = {r: G[r]['P'] for r in PAIRS}
POOL = defaultdict(Counter)
for r in PAIRS:
    for s, c in OWN[r].items(): POOL[s].update(c)

def values(rec, s):
    own = OWN[rec].get(s, Counter()); pool = POOL.get(s, Counter())
    No = sum(own.values()); Np = sum(pool.values())
    out = {}
    nul = (own.get('', 0) + pool.get('', 0)) / max(1, No + Np)
    for v in set(own) | set(pool):
        if v == '' and nul < 0.3: continue
        k = own.get(v, 0) + 0.3 * pool.get(v, 0)
        if k < 1.0: continue
        out[v] = (k + 0.05) / (No + 0.3 * Np + 1)
    if not out:                                   # an unseen sign: any single letter, flat
        out = {c: 0.02 for c in 'abcdefghiklmnoprstuwz'}
    return out

# lexicon
def normw(w):
    w = w.lower().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ß', 'ss').replace('j', 'i').replace('v', 'u')
    if LANG == 'la': w = w.replace('y', 'i').replace('k', 'c').replace('w', 'u')
    return re.sub(r'[^a-z]', '', w)
if LANG == 'de':
    W0 = json.load(open(os.path.join(HERE, '..', 'r9407', 'de1500_words.json'), encoding='utf8'))
    MINC = {1: 10**9, 2: 3000, 3: 300, 4: 30, 5: 5}
    LEX = {w: c for w, c in W0.items() if c >= MINC.get(len(w), 2)}
    for l in open(os.path.join(HERE, 'vocab.txt'), encoding='utf8'):
        if l.startswith('#'): continue
        for x in l.split():
            x, _, c = x.partition(':'); LEX[x] = max(LEX.get(x, 0), int(c or 50))
else:
    C = Counter(lm.norm(open(os.path.join(HERE, '..', '..', '..', 'lang', 'corpora', 'la-gutenberg.txt'), encoding='utf8').read(), 'latin').split())
    LEX = {w: c for w, c in C.items() if c >= 3 and len(w) >= 2}
for r, f in PAIRS.items():                       # the correspondence's own words
    if (r == 'r9410b') != (LANG == 'la'): continue
    for l in open(os.path.join(HERE, f), encoding='utf8'):
        m = re.match(r'\s*P\d+\.\d\d\s+(.*)', l)
        if not m: continue
        for w in re.sub(r'\[[^\]]*\]', ' ', re.sub(r'(\w)\[(\w+)\](\w*)', r'\1\2\3', m.group(1))).split():
            if '{' in w or '?' in w: continue
            w = normw(w)
            if len(w) >= 2: LEX[w] = LEX.get(w, 0) + 30
NW = sum(LEX.values())
TRIE = set()
for w in LEX:
    for i in range(1, len(w) + 1): TRIE.add(w[:i])
M = lm.load('de-1500s' if LANG == 'de' else 'la', spaces=True)
K = M.order; IDX = M.index; SPC = IDX[' ']
def lmscore(text):
    t = lm.norm(text, 'early' if LANG == 'de' else 'latin')
    x = [SPC] * (K - 1) + [IDX[c] for c in t if c in IDX]
    s = 0.0
    for i in range(K - 1, len(x)):
        h = 0
        for c in x[i - K + 1:i]: h = h * M.A + c
        s += float(M.lp[h * M.A + x[i]])
    return s

def wildcard_align(signs, items, P):
    """items: list of words (str) or None for {?}; returns per item (start, end) sign span"""
    flat = []; owner = []
    for k, it in enumerate(items):
        if it is None: flat.append('*'); owner.append(k)
        else:
            for ch in it: flat.append(ch); owner.append(k)
    n, m = len(signs), len(flat)
    def sc(g, v):
        d = P.get(g)
        if not d: return -3.0 if v else -6.0
        if not v: return -8.0
        c = d.get(v, 0); N = sum(d.values())
        return math.log((c + 0.2) / (N + 1))
    NEG = -1e18
    D = [[NEG] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == NEG: continue
            if j < m and flat[j] == '*':          # leave the wildcard
                if D[i][j] > D[i][j + 1]: D[i][j + 1] = D[i][j]; B[i][j + 1] = (i, j, 'skip')
                if i < n:
                    v = D[i][j] - 0.7              # the wildcard eats a sign
                    if v > D[i + 1][j]: D[i + 1][j] = v; B[i + 1][j] = (i, j, 'eat')
                continue
            if i < n:
                for L in (0, 1, 2, 3):
                    if j + L > m or '*' in flat[j:j + L]: break
                    v = D[i][j] + sc(signs[i], ''.join(flat[j:j + L]))
                    if v > D[i + 1][j + L]: D[i + 1][j + L] = v; B[i + 1][j + L] = (i, j, 'emit')
    if D[n][m] == NEG: return None
    spans = defaultdict(list); i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, kind = B[i][j]
        if kind == 'eat': spans[owner[j]].append(pi)
        i, j = pi, pj
    return {k: (min(v), max(v) + 1) for k, v in spans.items()}

def constrained(rec, span, left, right):
    """beam over lexicon words; returns [(score, [words])]"""
    cand = [values(rec, s) for s in span]
    states = {('', ()): (0.0, [])}                      # key: (current prefix,) -> (score, words)
    for vs in cand:
        new = {}
        for (pre, _l), (sc, ws) in states.items():
            for v, p in vs.items():
                v2 = normw(v) if v else ''
                cost = math.log(p)
                for brk in (False, True):
                    w = pre + v2
                    if w and w not in TRIE: continue
                    if brk:
                        if w not in LEX: continue
                        key = ('', tuple(ws[-2:]) + (w,)); val = (sc + cost + math.log(LEX[w] / NW), ws + [w])
                    else:
                        key = (w, tuple(ws[-2:])); val = (sc + cost, ws)
                    if len(w) > 18: continue
                    if key not in new or new[key][0] < val[0]: new[key] = val
        states = dict(sorted(new.items(), key=lambda kv: -kv[1][0])[:BEAM])
    res = [(sc, ws) for (pre, _l), (sc, ws) in states.items() if pre == '' and ws]
    out = []
    for sc, ws in res:
        out.append((sc + 0.5 * lmscore(' '.join([left] + ws + [right])), ws))
    out.sort(key=lambda x: -x[0])
    return out[:TOP]

def main():
    g = G[REC]; P = OWN[REC]
    _, T, R = g['data'][0]
    # sign strings of every reading's words, for verification
    ALL = {}
    for r in PAIRS:
        if r == 'r9407': continue
        _, T2, R2 = G[r]['data'][0]
        ALL[r] = (T2, R2)
    out = []
    nspans = 0
    for no, r in R.items():
        if '{?}' not in r: continue
        toks = [w for w in re.sub(r'\[[^\]]*[A-Za-z.][^\]]*\]', ' ', r).split()]
        items = []
        for w in toks:
            if '{?}' in w: items.append(None)
            else:
                nw = normw(re.sub(r'\[(\w+)\]', r'\1', w))
                if nw: items.append(nw)
        sp = wildcard_align(T[no], items, P)
        if sp is None: out.append(f'{no}: alignment failed'); continue
        k = 0
        while k < len(items):
            if items[k] is not None: k += 1; continue
            k2 = k
            while k2 < len(items) and items[k2] is None: k2 += 1
            ss = [sp[x] for x in range(k, k2) if x in sp]
            if not ss: k = k2; continue
            a, b = min(s[0] for s in ss), max(s[1] for s in ss)
            left = items[k - 1] if k > 0 and items[k - 1] else ''
            right = items[k2] if k2 < len(items) and items[k2] else ''
            signs = T[no][a:b]; nspans += 1
            cands = constrained(REC, signs, left, right) if len(signs) <= 40 else []
            out.append(f'{no} [{k}:{k2}] {k2 - k} unread, signs {signs!r}  context: {left} _ {right}')
            for sc, ws in cands:
                out.append(f'    {sc:8.1f}  {" ".join(ws)}')
            # other occurrences of the same sign string (len >= 4) in all the letters, with the reading there
            if len(signs) >= 4:
                seen = 0
                for r2, (T2, R2) in ALL.items():
                    for no2, s2 in T2.items():
                        if (r2, no2) == (REC, no) or signs not in s2: continue
                        out.append(f'      also {r2} {no2}: {R2.get(no2, "")[:90]}'); seen += 1
                        if seen >= 4: break
                    if seen >= 4: break
            k = k2
    open(os.path.join(HERE, OUT), 'w', encoding='utf8').write('\n'.join(out) + '\n')
    print(REC, nspans, 'spans ->', OUT)

if __name__ == '__main__':
    main()
