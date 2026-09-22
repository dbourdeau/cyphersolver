"""Align reading_v3 lines to sign strings; for each unread gap / '?' word, list lexicon candidates
(<=1 substitution + <=1 indel against the per-sign alternatives), scored by de-1500s in context."""
import re, sys, os, math, collections, pickle
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

ALT = {}
for kv in open('cp12/alt_p12.txt', encoding='utf8').read().split():
    k, v = kv[0], kv[2:]; ALT[k] = set(v.split('/'))
ALT['0'] = {'n'}; ALT[')'] = {'f'}; ALT[']'] = {'s'}; ALT['R'] |= {'r'}
ALT['o'] |= {'r'}; ALT['N'] = {'a', 'e', 'u', 'i', 'n'}; ALT['e'] = {'#'}   # e = F.G. code
for k in 'ZΨXK?': ALT[k] = {'*'}                                             # code / blot
ALT.setdefault('h', {'i'}); ALT.setdefault('4', {'a'})

def signs_of(s):
    s = re.sub(r'\{-\}', '', s); s = re.sub(r'\{[^}]*\}', '?', s).replace('o/', '0')
    s = re.sub(r'\[[^\]]*\]', '|', s)
    return s
TR = {}
for fn, pages in (('transcription_p12.txt', 'P1 P2'), ('transcription_p34.txt', 'P3 P4'), ('transcription_v2.txt', 'P5')):
    pg = None
    for l in open(fn, encoding='utf8'):
        m = re.match(r'== (P\d)', l)
        if m: pg = m.group(1); continue
        m = re.match(r'(\d\d) (.*)', l)
        if m and pg in pages.split(): TR[f'{pg}.{m.group(1)}'] = signs_of(m.group(2).strip())

def rnorm(w):
    w = w.lower().replace('j', 'i').replace('v', 'u')
    return re.sub(r'[^a-z]', '', w)

# lexicon
cache = os.path.join(os.environ.get('TEMP', '.'), 'r9414_lex.pkl')
if os.path.exists(cache): LEX = pickle.load(open(cache, 'rb'))
else:
    t = corpora.text(['de-dta-1470-1610'])
    t = lm.norm(t, 'early', spaces=True)
    LEX = collections.Counter(t.split()); pickle.dump(LEX, open(cache, 'wb'))
READ = collections.Counter()
lines = [l.rstrip('\n') for l in open('reading_v3.txt', encoding='utf8')]
for l in lines:
    if l[:1] != 'P': continue
    for w in re.sub(r'<[^>]*>', ' ', l[6:]).split():
        if '?' not in w and '[' not in w and rnorm(w): READ[rnorm(w)] += 1
M = lm.load('de-1500s')

def match(sg, w):
    """edit distance between sign string sg and word w: sub cost 1 (sign alt mismatch), indel 1; '*' sign = wildcard."""
    n, m = len(sg), len(w)
    D = [[9] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        a = ALT.get(sg[i-1], set())
        for j in range(1, m + 1):
            ok = w[j-1] in a or '*' in a
            D[i][j] = min(D[i-1][j-1] + (0 if ok else 1), D[i-1][j] + 1, D[i][j-1] + 1)
    return D[n][m]

def rtoks(line):
    """reading line -> list of (token, kind) with kind word/gap/unread; clear <..> -> '|'."""
    out = []
    for tok in re.findall(r'<[^>]*>|\S+', line):
        if tok.startswith('<'): out.append(('|', 'clear')); continue
        m = re.fullmatch(r'\[\.\.(\d+)\]', tok)
        if m: out.append((tok, 'gap')); continue
        if tok in ('F.G.', 'F.G'): out.append(('#', 'fg')); continue
        k = 'unread' if '?' in tok else 'word'
        out.append((tok, k))
    return out

def align(sg, toks):
    """DP: sequence of reading units vs signs. Returns for each token the (start,end) sign span."""
    units = []  # (char or None for gap, token index)
    for ti, (t, k) in enumerate(toks):
        if k == 'gap': units.append(('*', ti))
        elif k == 'clear': units.append(('|', ti))
        elif k == 'fg': units.append(('#', ti))
        else:
            for c in rnorm(t): units.append((c, ti))
    n, m = len(sg), len(units); INF = 1e9
    D = [[INF] * (n + 1) for _ in range(m + 1)]; B = [[None] * (n + 1) for _ in range(m + 1)]
    D[0][0] = 0
    for j in range(1, n + 1): D[0][j] = j * 0.8; B[0][j] = 's'
    for i in range(1, m + 1):
        c = units[i-1][0]
        for j in range(n + 1):
            best = (D[i-1][j] + 1, 'u')                      # reading char with no sign
            if c == '*':
                best = min(best, (D[i-1][j] + 0.5, 'u'))
                if j: best = min(best, (D[i][j-1] + 0.3, 'g'), (D[i-1][j-1] + 0.3, 'm'))
            elif j:
                sgn = sg[j-1]; a = ALT.get(sgn, set())
                if c == '|': cost = 0 if sgn == '|' else 3
                else: cost = 0 if (c in a or '*' in a) else 1
                best = min(best, (D[i-1][j-1] + cost, 'm'), (D[i][j-1] + 1, 's'))
            D[i][j], B[i][j] = best
    i, j = m, n; span = collections.defaultdict(list)
    while i > 0 or j > 0:
        b = B[i][j] if i > 0 else 's'
        if b == 'm': span[units[i-1][1]].append(j-1); i -= 1; j -= 1
        elif b == 'g': span[units[i-1][1]].append(j-1); j -= 1
        elif b == 'u': i -= 1
        else: j -= 1
    return span, D[m][n]

def ctxscore(left, w, right):
    s = lm.norm(f'{left} {w} {right}', 'early', spaces=True)
    return M.score(s)

lexset = {w: c for w, c in LEX.items() if c >= 2 and 1 < len(w) < 16}
for w in READ: lexset[w] = lexset.get(w, 0) + 50
BYLEN = collections.defaultdict(list)
for w in lexset: BYLEN[len(w)].append(w)

for l in lines:
    if l[:1] != 'P': continue
    lab, body = l[:5], l[6:]
    sg = TR.get(lab)
    if sg is None: continue
    toks = rtoks(body)
    if not any(k in ('gap', 'unread') for _, k in toks): continue
    span, cost = align(sg, toks)
    print(f'\n{lab}  {body}\n      signs {sg}   (align cost {cost:.1f})')
    for ti, (t, k) in enumerate(toks):
        if k not in ('gap', 'unread'): continue
        ss = ''.join(sg[p] for p in sorted(span.get(ti, [])))
        left = ' '.join(x for x, kk in toks[max(0, ti-4):ti] if kk == 'word')
        right = ' '.join(x for x, kk in toks[ti+1:ti+4] if kk == 'word')
        cands = []
        L = len(ss)
        if 0 < L <= 14 and '|' not in ss:
            for ln in range(max(1, L-1), L+2):
                for w in BYLEN[ln]:
                    d = match(ss, w)
                    if d <= 1 or (d == 2 and abs(len(w) - L) == 1):
                        cands.append((d, w))
        sc = sorted(((d, ctxscore(left, w, right) - 0.0, w) for d, w in cands), key=lambda x: (x[0], -x[1]))
        top = ', '.join(f'{w}({d},{s:.0f}{"*" if w in READ else ""})' for d, s, w in sc[:12])
        print(f'   [{t}] signs "{ss}"  ctx: {left} _ {right}\n       -> {top}')
