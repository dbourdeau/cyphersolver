"""Word coverage of the decode: which letters do not fall inside a Spanish word, and which signs are to blame.

  python3 scripts/coverage.py WORDS report            per-line coverage and the signs ranked by uncovered share
  python3 scripts/coverage.py WORDS try SIGN ...       score every alternative value for the given signs
  python3 scripts/coverage.py WORDS sweep [MIN]        try every sign with at least MIN tokens (default 2)
  python3 scripts/coverage.py WORDS show [K=V ...]     segmented decode, optionally with values overridden

WORDS: a word-frequency file ("word count" per line), period spelling (u for v, i for j, z for c cedilla). Step 12
used the corpus of build_lm_chancery.py (words seen twice or more; one- and two-letter words limited to a closed list
of Spanish function words; three-letter words seen 5+ times) plus lexicon words of 4+ letters (lang/lexicons/es).
The decode is segmented piece by piece (frame marks split pieces) by a unigram DP: a word costs -log p(word), an
uncovered letter costs UNK. Code-group values are kept as units: a word may not start or end inside a code value.
"""
import sys, os, re, math, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load import lines, is_code
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALIAS = {'gto', 'oo', 'ff', 'll', 'ef'}
CODE_LIKE = lambda t: is_code(t) or (len(t) == 2 and t.isalpha() and t.islower() and t not in ALIAS)
UNK = 9.0

def load_key():
    """key/key.tsv: value '-' = none, '0' = null. Status = the class column."""
    key, st = {}, {}
    for l in open(os.path.join(ROOT, 'key', 'key.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('kind\t') or not l.strip(): continue
        kind, tok, val, s = l.rstrip('\n').split('\t')[:4]
        key[tok], st[tok] = val, s
    return key, st

def load_words(p):
    c = {}
    for l in open(p, encoding='utf-8'):
        w, n = l.split()[:2]; c[w] = c.get(w, 0) + float(n)
    tot = sum(c.values())
    return {w: -math.log(n / tot) for w, n in c.items()}

def pieces():
    """Token stream split at frame marks / piece ends: list of [(line, token)]."""
    out = []
    for b in 'ABCD':
        cur = []
        for tag, ts in lines(b):
            for t in ts:
                if t in ('ratio', '¶'):
                    if cur: out.append(cur); cur = []
                else: cur.append((tag, t))
        if cur: out.append(cur)
    return out

def units(piece, key, over):
    """[(text, token, is_code)] with the key (and overrides) applied; unread code groups give text None."""
    u = []
    for tag, t in piece:
        v = over.get(t, key.get(t))
        if v == '0': continue                   # null
        if v in ('-', '?', ''): v = None
        if v and '|' in v: v = v.split('|')[0]
        if CODE_LIKE(t): u.append((v, t, True, tag))
        else: u.append((v, t, False, tag))
    return u

def segment(u, W, maxlen=16):
    """DP over the letters of the units. Returns (cost, covered flags per letter, letters, owner unit per letter)."""
    letters, owner, cut_ok = [], [], [True]
    for i, (v, t, code, tag) in enumerate(u):
        if v is None:                       # unread code group: a hard break, costs UNK*4
            letters.append('#'); owner.append(i); cut_ok.append(True); continue
        for k, ch in enumerate(v):
            letters.append(ch); owner.append(i)
            cut_ok.append(k == len(v) - 1 or not code)
    n = len(letters); INF = 1e18
    best = [INF] * (n + 1); back = [None] * (n + 1); best[0] = 0
    for i in range(n):
        if best[i] >= INF: continue
        if letters[i] == '#':
            if best[i] + UNK * 4 < best[i + 1]: best[i + 1] = best[i] + UNK * 4; back[i + 1] = (i, False)
            continue
        if best[i] + UNK < best[i + 1]:                         # one uncovered letter (also inside a code value)
            best[i + 1] = best[i] + UNK; back[i + 1] = (i, False)
        if not cut_ok[i]: continue                              # a word may not start inside a code value
        w = ''
        for j in range(i, min(n, i + maxlen)):
            if letters[j] == '#': break
            w += letters[j]
            if cut_ok[j + 1] and w in W and best[i] + W[w] < best[j + 1]:
                best[j + 1] = best[i] + W[w]; back[j + 1] = (i, True)
    cov = [False] * n; words = []; j = n
    while j > 0:
        i, isw = back[j]
        if isw:
            for k in range(i, j): cov[k] = True
            words.append(''.join(letters[i:j]))
        else: words.append(letters[i:j][0].upper() if letters[i] != '#' else '#')
        j = i
    return best[n], cov, letters, owner, words[::-1]

def score(key, W, over={}):
    tot, unc, letters_all = 0.0, 0, 0
    for p in pieces():
        c, cov, letters, owner, _ = segment(units(p, key, over), W)
        tot += c; unc += sum(1 for k, ch in enumerate(letters) if ch != '#' and not cov[k]); letters_all += sum(ch != '#' for ch in letters)
    return tot, unc, letters_all

def report(key, st, W):
    bad, all_ = collections.Counter(), collections.Counter()
    unc = tot = 0
    for p in pieces():
        u = units(p, key, {})
        c, cov, letters, owner, words = segment(u, W)
        for k, ch in enumerate(letters):
            if ch == '#': continue
            t = u[owner[k]][1]; all_[t] += 1; tot += 1
            if not cov[k]: bad[t] += 1; unc += 1
    print(f'letters {tot}, uncovered {unc} ({unc / tot:.3f})')
    print('signs by uncovered letters (token, value, status, letters, uncovered, share):')
    rows = [(t, bad[t], all_[t]) for t in all_ if not CODE_LIKE(t)]
    for t, b, a in sorted(rows, key=lambda r: -r[1])[:40]:
        print(f'  {t:6} {key.get(t, "?"):5} {st.get(t, "-"):6} {a:4} {b:4} {b / a:.2f}')

def alternatives(key):
    vals = set()
    for t, v in key.items():
        if not CODE_LIKE(t) and v and v not in ('-', '?'): vals.add(v)
    vals |= set('abcdefghilmnopqrstuxyz') | {'0'}
    return sorted(vals)

def try_signs(key, st, W, signs):
    base = score(key, W)
    print(f'base cost {base[0]:.1f}, uncovered {base[1]}/{base[2]}')
    for s in signs:
        res = []
        for v in alternatives(key):
            if v == key.get(s): continue
            c = score(key, W, {s: v}); res.append((c[0] - base[0], c[1] - base[1], v))
        res.sort()
        print(f'{s} = {key.get(s)} ({st.get(s)}): ' + '  '.join(f'{v}:{d:+.0f}/{du:+d}' for d, du, v in res[:6]))

def show(key, W, over):
    for p in pieces():
        u = units(p, key, over)
        c, cov, letters, owner, words = segment(u, W)
        first, last = p[0][0], p[-1][0]
        out, run = [], ''
        for w in words:
            if len(w) == 1 and (w.isupper() or w == '#'): run += w.lower() if w != '#' else '#'
            else:
                if run: out.append('<' + run + '>'); run = ''
                out.append(w)
        if run: out.append('<' + run + '>')
        print(f'[{first}-{last}] ' + ' '.join(out))

if __name__ == '__main__':
    W = load_words(sys.argv[1]); key, st = load_key(); cmd = sys.argv[2]
    if cmd == 'report': report(key, st, W)
    elif cmd == 'try': try_signs(key, st, W, sys.argv[3:])
    elif cmd == 'sweep':
        mn = int(sys.argv[3]) if len(sys.argv) > 3 else 2
        cnt = collections.Counter(t for p in pieces() for _, t in p)
        try_signs(key, st, W, [t for t in key if not CODE_LIKE(t) and cnt[t] >= mn])
    elif cmd == 'show': show(key, W, dict(a.split('=', 1) for a in sys.argv[3:]))

FIRM = {'firm'}

def group_classes(key, st):
    """class (initial + final letter) -> set of first letters of the firm values in it."""
    cl = collections.defaultdict(set)
    for t, v in key.items():
        if is_code(t) and st.get(t) in FIRM and v and v not in ('-', '?'):
            cl[t[0] + t[-1]].add(v.split('|')[0][0])
    return cl

def try_groups(key, st, W, groups, cands, top=5):
    """Delta cost (raw: each candidate pays its own word probability; env LAM subtracts LAM per letter), over the pieces holding
    the group. Candidates obey the class rule where the class has a firm member."""
    P = pieces(); base_all = score(key, W); LAM = float(os.environ.get("LAM", "0"))
    cl = group_classes(key, st)
    for g in groups:
        sub = [p for p in P if any(t == g for _, t in p)]
        def sc(over):
            c = n = 0
            for p in sub:
                r = segment(units(p, key, over), W); c += r[0]; n += sum(ch != '#' for ch in r[2])
            return c - LAM * n
        b = sc({}); first = cl.get(g[0] + g[-1])
        res = []
        for w in cands:
            if first and w[0] not in first: continue
            res.append((sc({g: w}) - b, w))
        res.sort()
        n = sum(1 for p in P for _, t in p if t == g)
        print(f'{g:4} = {key.get(g, "-"):10} {st.get(g, "-"):7} n={n} class {"".join(sorted(first)) if first else "?"}: '
              + '  '.join(f'{w}:{d:+.0f}' for d, w in res[:top]))

if __name__ == '__main__' and sys.argv[2] == 'groups':
    cands = [l.split()[0] for l in open(sys.argv[3])]
    which = sys.argv[4:] or [t for t in key if is_code(t) or (CODE_LIKE(t) and t in key)]
    try_groups(key, st, W, which, cands)
