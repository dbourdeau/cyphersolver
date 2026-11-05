"""Letter-level homophonic annealer for the 250 number groups of the Leopold I letter, with a control.

Each distinct number group maps to one letter of the es-golden-age-nospace model (order 7). The real letter and a
control (own Spanish text, enciphered with a random homophonic key of the same size and length) go through the
same code. Usage:
    python -I solve_homophonic.py real [restarts] [iters]
    python -I solve_homophonic.py control [seed] [restarts] [iters]
"""
import sys, re, math, random, collections
import numpy as np
sys.path.insert(0, '../..')
from lang import lm

M = lm.load('es-golden-age-nospace')
A = M.A
HERE = __file__.rsplit('/', 1)[0] if '/' in __file__ else '.'


def read_tokens(path='transcription.txt'):
    toks = []
    for l in open(path, encoding='utf8'):
        m = re.match(r'^(\d+):\s*(.*)', l)
        if m:
            toks += [int(re.sub(r'\D', '', t)) for t in m.group(2).split()]
    return toks


def anneal(toks, iters=300000, seed=0, t0=2.0, t1=0.05):
    rnd = random.Random(seed)
    syms = sorted(set(toks))
    sid = {s: i for i, s in enumerate(syms)}
    seq = np.array([sid[t] for t in toks])
    n = len(syms)
    # start: frequency-ranked assignment to letters by Spanish unigram order
    freq = collections.Counter(toks)
    key = np.array([rnd.randrange(A) for _ in range(n)])
    cur = M.score_idx(key[seq])
    best, bestkey = cur, key.copy()
    for it in range(iters):
        T = t0 * (t1 / t0) ** (it / iters)
        if rnd.random() < 0.5:
            i = rnd.randrange(n); old = key[i]; key[i] = rnd.randrange(A)
            new = M.score_idx(key[seq])
            if new >= cur or rnd.random() < math.exp((new - cur) / T):
                cur = new
            else:
                key[i] = old
        else:
            i, j = rnd.randrange(n), rnd.randrange(n)
            if key[i] == key[j]:
                continue
            key[i], key[j] = key[j], key[i]
            new = M.score_idx(key[seq])
            if new >= cur or rnd.random() < math.exp((new - cur) / T):
                cur = new
            else:
                key[i], key[j] = key[j], key[i]
        if cur > best:
            best, bestkey = cur, key.copy()
    pt = ''.join(M.alpha[k] for k in bestkey[seq])
    return best, pt, dict(zip(syms, [M.alpha[k] for k in bestkey]))


CONTROL = ("beboserviroeneldeunaconfianzaquevuestramagestadmehaceenesteasuntoyrecibidoconelmayorgustolacartadeochodefebrero"
           "seguramenteloquemehaparecidomasconvenientealbiendelacasaydelareligionesquesejunteneltiempoconlosprincipesdelimperio"
           "yconlosdeitaliaparaquenoseancargadosdeestasarmasporlosdeotraparteenelcasodeverseobligadoeltratadodepazfirmadoenlosultimos"
           "mesesyprocurandoquelaspromesasseancumplidaspormedioquesesepamuybiendeestascosaslequeguardedioscomodeseo")


def make_control(seed, n=250, nsym=85):
    rnd = random.Random(seed)
    letters = [c for c in CONTROL if c in M.alpha]
    start = rnd.randrange(0, max(1, len(letters) - n))
    pt = ''.join(letters[start:start + n])
    cnt = collections.Counter(pt)
    # homophones proportional to frequency, at least one per letter present
    alloc = {c: 1 for c in cnt}
    for _ in range(nsym - len(alloc)):
        c = max(cnt, key=lambda c: cnt[c] / alloc[c])
        alloc[c] += 1
    pool = rnd.sample(range(10, 225), nsym)
    k = 0; table = {}
    for c in alloc:
        table[c] = pool[k:k + alloc[c]]; k += alloc[c]
    toks = [rnd.choice(table[c]) for c in pt]
    return pt, toks


def acc(real, got):
    return sum(a == b for a, b in zip(real, got)) / len(real)


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'real':
        restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        iters = int(sys.argv[3]) if len(sys.argv) > 3 else 200000
        toks = read_tokens()
        res = [anneal(toks, iters, seed=s) for s in range(restarts)]
        for sc, pt, key in sorted(res, key=lambda r: -r[0]):
            print(round(sc, 1), pt)
    else:
        seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        restarts = int(sys.argv[3]) if len(sys.argv) > 3 else 3
        iters = int(sys.argv[4]) if len(sys.argv) > 4 else 200000
        pt, toks = make_control(seed)
        print('distinct', len(set(toks)), 'true score', round(M.score(pt), 1))
        for s in range(restarts):
            sc, got, key = anneal(toks, iters, seed=s)
            print(round(sc, 1), 'acc', round(acc(pt, got), 2), got[:80])
