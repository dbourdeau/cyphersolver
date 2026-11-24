"""Known-plaintext solver: align each figure group with a substring of the printed clear text.

Model: every group (number, with or without '*') stands for one string (letter, syllable,
word, name) or nothing (null). A literal numeral group (e.g. 42000) may also stand for itself.
Words printed in clear inside the figure stream must match the clear text exactly.
Alignments are sampled per paragraph by forward-filtering/backward-sampling, with the
counts from all other paragraphs as a Dirichlet-smoothed table (annealed Gibbs sampling),
then a final max-probability (Viterbi) pass gives the alignment written out.

usage: python3 -I solve.py OUT.json SEED SWEEPS file1.tr [file2.tr ...]
"""
import sys, os, json, math, random
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import parse

KMAX = int(os.environ.get("KMAX", 12))
P_NULL = float(os.environ.get("PNULL", 0.002))
Q = float(os.environ.get("QLEN", 0.45))
ALPHA0 = 0.5
P_LIT = 0.5

BAND = int(os.environ.get("BAND", 90))

def build(files):
    units = []
    for f in files:
        d = parse(f)
        for k, u in enumerate(d['units']):
            u['letter'] = os.path.basename(f).split('.')[0]
            u['idx'] = k
            units.append(u)
    subs = defaultdict(set)
    for u in units:
        t = u['text']
        for k in range(1, KMAX + 1):
            for j in range(len(t) - k + 1):
                subs[k].add(t[j:j + k])
    nk = {k: max(1, len(subs[k])) for k in range(1, KMAX + 1)}
    base = {k: (1 - P_NULL) * Q * (1 - Q) ** (k - 1) / nk[k] for k in range(1, KMAX + 1)}
    for u in units:
        t = u['text']; m = len(t); n = len(u['groups'])
        u['base'] = base
        u['pos'] = {}
        for k in range(1, KMAX + 1):
            for j in range(m - k + 1):
                u['pos'].setdefault((k, t[j:j + k]), []).append(j)
        for g in u['groups']:
            if g[0] == 'w' and len(g[1]) > KMAX:
                k = len(g[1]); j = t.find(g[1])
                while j >= 0:
                    u['pos'].setdefault((k, g[1]), []).append(j); j = t.find(g[1], j + 1)
        # band of admissible end positions after i groups
        r = m / max(1, n)
        u['lo'] = [max(0, int(i * r) - BAND) for i in range(n + 1)]
        u['hi'] = [min(m, int(i * r) + BAND) for i in range(n + 1)]
        u['lo'][n] = u['hi'][n] = m
        u['lo'][0] = u['hi'][0] = 0
    return units

class Table:
    def __init__(self):
        self.c = defaultdict(Counter)
        self.tot = Counter()
    def add(self, al, sign):
        for g, v in al:
            if g[0] != 'g':
                continue
            self.c[g[1]][v] += sign
            self.tot[g[1]] += sign
            if self.c[g[1]][v] == 0:
                del self.c[g[1]][v]

def emis_sparse(u, g, tab, beta):
    """Return (dict k -> const prob for any substring, dict (k,j) -> prob override)."""
    if g[0] == 'w':
        k = len(g[1])
        return {}, {(k, j): 1.0 for j in u['pos'].get((k, g[1]), [])}
    name = g[1]
    denom = tab.tot[name] + ALPHA0
    const = {0: P_NULL ** beta}   # nulls: fixed small probability, never reinforced
    sp = {}
    for k in range(1, KMAX + 1):
        const[k] = (u['base'][k] * ALPHA0 / denom) ** beta
    for v, c in tab.c[name].items():
        k = len(v)
        if k and c > 0:
            p = ((c + u['base'][k] * ALPHA0) / denom) ** beta
            for j in u['pos'].get((k, v), []):
                sp[(k, j)] = p
    digits = name.rstrip('*')
    if digits.isdigit():
        k = len(digits)
        for j in u['pos'].get((k, digits), []):
            sp[(k, j)] = max(sp.get((k, j), 0), P_LIT ** beta)
    return const, sp

def sample(u, tab, beta, rng, viterbi=False):
    t = u['text']; m = len(t); gs = u['groups']; n = len(gs)
    lo, hi = u['lo'], u['hi']
    alpha = [None] * (n + 1)
    alpha[0] = {0: 1.0}
    EM = []
    for i, g in enumerate(gs):
        const, sp = emis_sparse(u, g, tab, beta)
        EM.append((const, sp))
        prev = alpha[i]
        row = {}
        L, H = lo[i + 1], hi[i + 1]
        isw = g[0] == 'w'
        for j, a in prev.items():
            if not isw:
                # all lengths with constant prob
                for k in range(0, KMAX + 1):
                    e = j + k
                    if e > m: break
                    if e < L or e > H: continue
                    p = sp.get((k, j), const[k]) if k else const[0]
                    w = a * p
                    if viterbi:
                        if w > row.get(e, 0): row[e] = w
                    else:
                        row[e] = row.get(e, 0) + w
            else:
                k = len(g[1]); p = sp.get((k, j), 0)
                e = j + k
                if p and L <= e <= H:
                    w = a * p
                    row[e] = max(row.get(e, 0), w) if viterbi else row.get(e, 0) + w
        s = sum(row.values())
        if s <= 0:
            return None
        alpha[i + 1] = {e: w / s for e, w in row.items() if w > 0}
    if m not in alpha[n]:
        return None
    al = []
    j = m
    for i in range(n - 1, -1, -1):
        const, sp = EM[i]; g = gs[i]
        opts = []; ws = []
        for k in ([len(g[1])] if g[0] == 'w' else range(0, KMAX + 1)):
            s0 = j - k
            if s0 < 0: break
            a = alpha[i].get(s0)
            if not a: continue
            if g[0] == 'w':
                p = sp.get((k, s0), 0)
            else:
                p = sp.get((k, s0), const[k]) if k else const[0]
            if p > 0:
                opts.append(k); ws.append(a * p)
        if not opts:
            return None
        if viterbi:
            k = opts[max(range(len(ws)), key=ws.__getitem__)]
        else:
            k = rng.choices(opts, weights=ws)[0]
        al.append((g, t[j - k:j], j - k))
        j -= k
    al.reverse()
    return al

def run(files, seed, sweeps, log=None):
    rng = random.Random(seed)
    units = build(files)
    tab = Table()
    aligns = [None] * len(units)
    for sw in range(sweeps):
        beta = min(3.0, 0.4 + 2.6 * sw / max(1, sweeps * 0.8))
        order = list(range(len(units))); rng.shuffle(order)
        for ui in order:
            u = units[ui]
            if aligns[ui]:
                tab.add([(a[0], a[1]) for a in aligns[ui]], -1)
            al = sample(u, tab, beta, rng)
            if al is None:
                al = sample(u, tab, 1.0, rng)
            if al is None:
                print('unit failed', u['letter'], u['idx'], file=sys.stderr)
            aligns[ui] = al
            if al:
                tab.add([(a[0], a[1]) for a in al], +1)
        if log and (sw % 10 == 0 or sw == sweeps - 1):
            nv = sum(len(c) for c in tab.c.values())
            print(f'sweep {sw} beta {beta:.2f} distinct (group,value) pairs {nv}', file=log, flush=True)
    # final viterbi with leave-one-unit-out counts
    final = []
    for ui, u in enumerate(units):
        if aligns[ui]:
            tab.add([(a[0], a[1]) for a in aligns[ui]], -1)
        al = sample(u, tab, 1.0, rng, viterbi=True) or aligns[ui]
        if aligns[ui]:
            tab.add([(a[0], a[1]) for a in aligns[ui]], +1)
        final.append(al)
    out = []
    for u, al in zip(units, final):
        out.append({'letter': u['letter'], 'unit': u['idx'], 'text': u['text'],
                    'align': [[g[0], g[1], g[2], v, j] for (g, v, j) in al] if al else None})
    return out

if __name__ == '__main__':
    outp, seed, sweeps = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    res = run(sys.argv[4:], seed, sweeps, log=sys.stderr)
    json.dump(res, open(outp, 'w'), ensure_ascii=False, indent=0)
