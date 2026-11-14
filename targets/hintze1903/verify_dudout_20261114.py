"""hintze1903: independent check (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).
Reads only code_values.tsv, the two transcriptions, m0003_contemporary.txt and m0003_decryption.txt.
Run from targets/hintze1903/. No numpy needed."""
import re, random, unicodedata

def lines(p):
    return [l.rstrip('\n') for l in open(p, encoding='utf-8') if not l.startswith('#')]

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')

code = {}
for l in lines('code_values.tsv')[1:]:
    g, v, conf = l.split('\t')[:3]
    code[int(g)] = (v, conf)

def tokens(p):
    return ' '.join(lines(p)).replace('=', ' ').split()

# 1. word count: figure groups of up to 5 figures = 1 word; clear words = 1; punctuation (. .+ .- ,) not counted
ADDR = {'m0001': 'SA MAJESTE LA REINE DE PORTUGAL A\' BORD DU YACHT AMELIA NAPLES',
        'm0003': 'SA MAGESTE LA REINE DE PORTUGAL HOTEL BRISTOL PARIS'}
HEAD = {'m0001': 75, 'm0003': 46}
print('1. word count')
for m in ('m0001', 'm0003'):
    t = tokens(m + '_transcription.txt')
    n = sum(1 for x in t if re.fullmatch(r'\d{1,5}', x) or re.fullmatch(r"[A-Z']+", x))
    a = len(ADDR[m].split())
    print(f'  {m}: address {a} + text {n} = {a+n}, header {HEAD[m]}')

# 2. decode m0003 with the key file and compare with the published decryption, group by group
print('2. m0003 decoded from code_values.tsv against m0003_decryption.txt')
t3 = tokens('m0003_transcription.txt')
groups3 = [int(x) for x in t3 if x.isdigit()]
pub = [l.split(None, 1) for l in lines('m0003_decryption.txt') if l[:1].isdigit()]
ok = 0
for g, (pg, pv) in zip(groups3, pub):
    mine = code[g][0]
    ABBR = {'v. m.': 'vossa magestade'}  # the decryption keeps the decoder's abbreviation
    pv = ABBR.get(norm(pv).strip(), pv)
    same = int(pg) == g and norm(pv).split('[')[0].replace('?', '').strip().startswith(norm(mine)[:6])
    ok += same
    if not same:
        print('   differs:', g, mine, '|', pg, pv)
print(f'  {ok}/{len(groups3)} groups agree; {len(pub)} rows published')

# 3. segment check against the decode of the time: groups between clear words vs the decode's text
print('3. segments (groups between clear words) and the decode of the time')
dec = norm(' '.join(lines('m0003_contemporary.txt')))
segs, cur = [], []
for x in t3:
    if x.isdigit(): cur.append(int(x))
    elif cur: segs.append(cur); cur = []
if cur: segs.append(cur)
for s in segs:
    print('  ', len(s), 'groups:', ' | '.join(code[g][0] for g in s))
print('   decode of the time:', dec)

# 4. m0001: groups with a value in the key file
t1 = tokens('m0001_transcription.txt')
g1 = [int(x) for x in t1 if x.isdigit()]
have = [g for g in g1 if g in code and code[g][1] != 'guess']
print(f'4. m0001: {len(g1)} groups, {len(set(g1))} distinct; with a non-guess value: {have}')
print('   groups of m0001 also in m0003:', sorted(set(g1) & set(groups3)))

# 5. page model, own implementation
dec_items = {g: norm(v) for g, (v, c) in code.items() if c != 'guess'}
def key_word(v):  # alphabetical key: first word, "vossa magestade" filed under magestade
    w = v.replace('.', ' ').split()
    return 'magestade' if w[0] == 'vossa' else w[0]
def model(g, split):
    p, l = divmod(g, 100)
    return (split - p) * 100 + l if p < split else p * 100 + l  # lower pages reversed, lines kept
def rank(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0]*len(xs)
    for k, i in enumerate(o): r[i] = k
    return r
def rho(a, b):
    ra, rb = rank(a), rank(b); n = len(a)
    return 1 - 6*sum((x-y)**2 for x, y in zip(ra, rb))/(n*(n*n-1))
def best(items):
    gs = list(items); ws = [items[g] for g in gs]
    raw = rho(gs, ws)
    top = max((rho([model(g, s) for g in gs], ws), s) for s in range(1, 700))
    return raw, top
def lis(seq):  # longest increasing subsequence length
    import bisect; t = []
    for x in seq:
        i = bisect.bisect_left(t, x)
        if i == len(t): t.append(x)
        else: t[i] = x
    return len(t)
def report(label, items):
    raw, (r, s) = best(items)
    gs = sorted(items, key=lambda g: model(g, s))
    inorder = lis([items[g] for g in gs])
    print(f'  {label}: n={len(items)} raw rho {raw:.3f}; page model best rho {r:.3f} at split {s}; '
          f'longest alphabetical run {inorder}/{len(items)}')
    return s
print('5. page model (page = n // 100 reflected below the split, lines kept)')
A = {g: key_word(v) for g, v in dec_items.items()}
s = report('A, decode split as published (3707 da, 49641 franceza)', A)
for g in sorted(A, key=lambda g: model(g, s)):
    print(f'     {g:>6} -> {model(g, s):>6}  {A[g]}')
B = dict(A); B[50554] = 'presidente'; B[3707] = 'franceza'; B[49641] = 'ponto'
report('B, 50554 Presidente da Republica, 3707 franceza, 49641 ponto (the "." after franceza)', B)
C = dict(B); del C[67398]
report('C, as B without Livorno (place names at the end of the book?)', C)
# null: shuffled words, same choice of split
random.seed(20261114)
gs = list(A); ws = [A[g] for g in gs]; obs = best(A)[1][0]; hits = 0; vals = []
for _ in range(500):
    random.shuffle(ws)
    v = best(dict(zip(gs, ws)))[1][0]; vals.append(v); hits += v >= obs
vals.sort()
print(f'  null (500 shuffles of A, split refitted each time): median {vals[250]:.3f}, max {vals[-1]:.3f}, '
      f'>= observed {obs:.3f}: {hits}')
# where the open m0001 groups would file, and the place-name block
print('6. high groups (>= 67000), all documents:', sorted({g for g in g1 + groups3 if g >= 67000}))
