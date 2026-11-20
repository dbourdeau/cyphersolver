"""Substitution solve for T-S NS J479 (20 Nov 2026).
Reads the machine blocks of tr_side1.md / tr_side2.md (rows "S1L01: tok tok | tok ..."), keeps the cipher rows
(not the Arabic-script rows S?AR..), and maps every sign label to one of the 22 Hebrew letters (several labels may
share a letter: the scribe used variant signs). Score: lang model 'ja-translit' (Arabic in Hebrew letters, Latin-coded
a b g d h w z c v y k l m n s e f x q r j t = alef..tav), word breaks kept. Simulated annealing with restarts.
A trailing '.' on a label is dropped; 'X?' counts as X; '?' and '[...]' are unknowns.
Usage: solve.py [restarts] [--fix L=a,M=l ...] [--rows S2L01,S2L02] [--show]"""
import sys, os, re, math, random, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.stdout.reconfigure(encoding='utf-8')
from lang import lm
HEB = dict(zip('abgdhwzcvyklmnsefxqrjt', 'אבגדהוזחטיכלמנסעפצקרשת'))
LET = 'abgdhwzcvyklmnsefxqrjt'

def load_rows(files=('tr_side1.md', 'tr_side2.md'), only=None):
    rows = {}
    here = os.path.dirname(os.path.abspath(__file__))
    for f in files:
        p = os.path.join(here, f)
        if not os.path.exists(p): continue
        for l in open(p, encoding='utf-8'):
            m = re.match(r'\s*(S\d(?:L|V|U)\d\d):\s*(.*)', l)
            if not m: continue
            if only and m.group(1) not in only: continue
            words, cur = [], []
            for t in m.group(2).split():
                if t == '|':
                    if cur: words.append(cur); cur = []
                    continue
                t = t.rstrip('.').rstrip('?').rstrip('.')
                if not t or t.startswith('[') or t == '?': t = '?'
                cur.append(t)
            if cur: words.append(cur)
            rows[m.group(1)] = words
    return rows

def render(rows, key, unk='?'):
    out = {}
    for r, ws in rows.items():
        out[r] = ' '.join(''.join(key.get(s, unk) for s in w) for w in ws)
    return out

M = lm.load('ja-translit')
def score_text(t):
    t = re.sub(r'[^a-z ]', '', t)
    t = ' '.join(t.split())
    return M.per_char(t) if t else -9.0

def total(rows, key):
    # unknown signs render as '' (dropped inside the word) so they cost nothing
    txt = '  '.join(render(rows, key, unk='').values())
    return score_text(txt)

def solve(rows, fix, restarts=20, iters=40000, seed=1):
    labels = sorted({s for ws in rows.values() for w in ws for s in w if s != '?'})
    cnt = collections.Counter(s for ws in rows.values() for w in ws for s in w if s != '?')
    free = [l for l in labels if l not in fix]
    rnd = random.Random(seed); best = (-99, None)
    # frequency start: Judaeo-Arabic letter order
    freq_order = 'alymnwhbtrekfqdsxcgjvz'
    for r in range(restarts):
        key = dict(fix)
        order = sorted(free, key=lambda l: -cnt[l])
        for i, l in enumerate(order):
            key[l] = freq_order[i % 22] if r == 0 else rnd.choice(LET)
        cur = total(rows, key); T = 0.6
        for it in range(iters):
            l = rnd.choice(free); old = key[l]
            if rnd.random() < 0.5:
                key[l] = rnd.choice(LET)
            else:                      # swap with another label
                l2 = rnd.choice(free); key[l], key[l2] = key[l2], key[l]
                new = total(rows, key)
                if new >= cur or rnd.random() < math.exp((new - cur) / T * 40): cur = new
                else: key[l2], key[l] = key[l], old
                T = max(0.02, T * 0.9998); continue
            new = total(rows, key)
            if new >= cur or rnd.random() < math.exp((new - cur) / T * 40): cur = new
            else: key[l] = old
            T = max(0.02, T * 0.9998)
        if cur > best[0]: best = (cur, dict(key))
        print(f'restart {r}: {cur:.3f}', flush=True)
    return best, cnt

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    R = int(args[0]) if args else 10
    fix = {}; only = None
    for a in sys.argv[1:]:
        if a.startswith('--fix='): fix.update(dict(x.split('=') for x in a[6:].split(',') if x))
        if a.startswith('--rows='): only = set(a[7:].split(','))
    rows = load_rows(only=only)
    print('rows', len(rows), 'signs', sum(len(w) for ws in rows.values() for w in ws))
    (sc, key), cnt = solve(rows, fix, R)
    print(f'best {sc:.3f}')
    for l in sorted(key, key=lambda l: -cnt[l]): print(f'  {l:4s} -> {key[l]} {HEB[key[l]]}  ({cnt[l]})')
    for r, t in render(rows, key).items():
        print(r, ''.join(HEB.get(c, c) for c in t), '   ', t)
