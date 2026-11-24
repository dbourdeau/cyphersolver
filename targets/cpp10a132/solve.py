"""Key recovery from the TRAIN split only (p75r + p76r). Never reads p76v lines."""
import sys, re, random, math, collections
sys.path.insert(0, '/home/claude/keyless/_cs')
from lang import lm
TRAIN = {'p75r', 'p76r'}
def load(pages):
    out = []
    for ln in open('/home/claude/keyless/cpp10a132/TRANSCRIPTION.tsv').read().splitlines()[1:]:
        p, l, t = ln.split('\t')
        if p in pages: out.append(t)
    return out
def words(lines):
    ws = []
    for t in lines:
        t = re.sub(r'\{[^}]*\}', ' ', t)           # clear numerals out
        t = re.sub(r'<S\d\d>', '', t)              # two drawn signs: not letters
        t = t.replace('?', '').replace('[...]', '').replace('[.]', '').replace('[..]', '')
        t = re.sub(r'[./]', ' ', t).lower()
        ws += t.split()
    return ws
W = words(load(TRAIN))
text = ' '.join(W)
letters = text.replace(' ', '')
print('train words', len(W), 'letters', len(letters))
cnt = collections.Counter(letters)
print('freq', ' '.join(f'{c}:{n}' for c, n in cnt.most_common()))
N = len(letters); ic = sum(n*(n-1) for n in cnt.values())/(N*(N-1))
print('IC %.4f (Latin about 0.072, random/21 about 0.048)' % ic)
print('absent letters:', ''.join(c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in cnt))
M = lm.load('la-letters')
def score(pt): return M.per_char(lm.norm(pt, 'latin'))
# A. alphabet shifts
print('\n== A. shift hypothesis, all shifts, three alphabets ==')
ALPH = {'23 (a-z less j,v,w)': 'abcdefghiklmnopqrstuxyz', '24 (with v after u)': 'abcdefghiklmnopqrstuvxyz',
        '21 (no k,y)': 'abcdefghilmnopqrstuxz', '26 modern': 'abcdefghijklmnopqrstuvwxyz'}
res = []
for name, A in ALPH.items():
    for sh in range(1, len(A)):
        ok = all(c in A for c in cnt)
        pt = ''.join(A[(A.index(c)-sh) % len(A)] if c in A else ('#' if c != ' ' else ' ') for c in text)
        res.append((score(pt.replace('#', 'x')), name, sh, ok, pt[:60]))
res.sort(reverse=True)
for r in res[:6]: print('%.3f  alph %s  shift -%d  all-letters-in-alphabet=%s  %s' % r)
print('...worst %.3f' % res[-1][0])
# B. free substitution hill-climb (no shift assumed)
print('\n== B. free substitution, hill-climb with restarts (la-letters, order 5, spaces) ==')
syms = sorted(cnt); PL = 'abcdefghilmnopqrstuxz'
def dec(key): return ''.join(key.get(c, ' ') for c in text)
best = (-9, None)
for seed in (20261112, 7, 1, 2, 3, 4):
    rnd = random.Random(seed)
    for rs in range(8):
        pl = list(PL); rnd.shuffle(pl)
        key = dict(zip(syms, pl)); spare = pl[len(syms):]
        cur = score(dec(key)); T = 0.25
        for it in range(6000):
            a = rnd.choice(syms); k2 = dict(key); sp2 = list(spare)
            if sp2 and rnd.random() < 0.15:
                j = rnd.randrange(len(sp2)); k2[a], sp2[j] = sp2[j], k2[a]
            else:
                b = rnd.choice(syms); k2[a], k2[b] = k2[b], k2[a]
            s = score(dec(k2))
            if s > cur or rnd.random() < math.exp((s-cur)/T*len(text)/60):
                key, cur, spare = k2, s, sp2
            T = max(0.01, T*0.9993)
        if cur > best[0]: best = (cur, dict(key))
        print('seed %d restart %d score %.3f  %s' % (seed, rs, cur, dec(key)[:50]))
print('\nbest free key score %.3f' % best[0])
print(' '.join(f'{c}>{best[1][c]}' for c in syms))
print(dec(best[1])[:400])
